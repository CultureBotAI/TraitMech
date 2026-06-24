---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:35:21.353929'
end_time: '2026-06-18T05:54:11.089981'
duration_seconds: 1129.74
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: propionic acid fermentation
  trait_identifier: traitmech:000029
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: propionic_acid_fermentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A fermentation that produces propionate (with acetate and CO2) from
    sugars or lactate, typically via the Wood-Werkman (methylmalonyl-CoA) pathway.
    Characteristic of propionibacteria (e.g. Propionibacterium freudenreichii).
  parent_traits: METPO:1002005
  synonyms: propionate fermentation
  evidence_summary: 'DOI:10.3390/molecules31020333:  (Review of classical fermentations
    describes propionic acid fermentation (acetic acid, propionic acid, CO2) and propionibacteria
    as its agents, including the Wood-Werkman route.) | DOI:10.3389/fmicb.2021.703525:  (Review
    of fermentative energy conservation supports propionate formation as a redox-balancing,
    energy-conserving fermentation route.)'
  causal_graph_summary: 'propionic_acid_fermentation_propionate: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** propionic acid fermentation
- **METPO identifier:** traitmech:000029
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation that produces propionate (with acetate and CO2) from sugars or lactate, typically via the Wood-Werkman (methylmalonyl-CoA) pathway. Characteristic of propionibacteria (e.g. Propionibacterium freudenreichii).
- **Parent traits:** METPO:1002005
- **Synonyms:** propionate fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes propionic acid fermentation (acetic acid, propionic acid, CO2) and propionibacteria as its agents, including the Wood-Werkman route.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports propionate formation as a redox-balancing, energy-conserving fermentation route.)
- **Existing causal graph summary:** propionic_acid_fermentation_propionate: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **propionic acid fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/propionic_acid_fermentation.yaml`.

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
- **Trait label:** propionic acid fermentation
- **METPO identifier:** traitmech:000029
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation that produces propionate (with acetate and CO2) from sugars or lactate, typically via the Wood-Werkman (methylmalonyl-CoA) pathway. Characteristic of propionibacteria (e.g. Propionibacterium freudenreichii).
- **Parent traits:** METPO:1002005
- **Synonyms:** propionate fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes propionic acid fermentation (acetic acid, propionic acid, CO2) and propionibacteria as its agents, including the Wood-Werkman route.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports propionate formation as a redox-balancing, energy-conserving fermentation route.)
- **Existing causal graph summary:** propionic_acid_fermentation_propionate: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **propionic acid fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/propionic_acid_fermentation.yaml`.

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


## Microbial TraitMech Curation Report: Propionic Acid Fermentation (METPO: traitmech:000029)

### Scope summary (trait meaning and boundaries)
Propionic acid fermentation is an anaerobic metabolic mode in which reduced substrates (commonly glucose, glycerol, or lactate) are converted to propionic acid/propionate, typically with co-production of acetate and CO2 (and often succinate as an additional by-product in some taxa/processes). (rymuszka2026classicalfoodfermentations pages 19-20)

**Canonical (“classical”) definition and stoichiometry.** A recent synthesis of classical fermentations summarizes propionic fermentation as conversion of glucose/glycerol/lactate to propionate “accompanied by acetic acid and CO2 formation” and provides idealized stoichiometries (e.g., for glucose: C6H12O6 → 4/3 propionate + 2/3 acetate + 2/3 CO2 + 4/3 H2O + 4 ATP; for lactate: lactate → 2/3 propionate + 1/3 acetate + 1/3 CO2 + 2/3 H2O + ATP). (rymuszka2026classicalfoodfermentations pages 19-20)

**Boundary cases / nearby traits.** Multiple biochemical routes produce propionate; the curation boundary depends on whether the trait is restricted to the Wood–Werkman (methylmalonyl-CoA) fermentation typical of propionibacteria or broadened to “propionate-producing fermentation” more generally.
* The same review states three major routes to propionate: (1) Wood–Werkman (dicarboxylic acid / methylmalonyl-CoA) cycle, (2) acrylate pathway (lactate-to-propionate), and (3) 1,2-propanediol pathway. (rymuszka2026classicalfoodfermentations pages 19-20)
* A 2024 Bacteroidia-focused study similarly frames propionate formation through the “succinate pathway, the acrylate pathway or the 1,2-propanediol pathway,” emphasizing that many gut bacteria produce mixed acid spectra. (doring2024propionateproductionby pages 1-2)
* Environmental boundary: aerobic growth can suppress propionate accumulation in *Propionibacterium freudenreichii* despite lactate consumption, so assay conditions (anaerobic vs aerobic/microaerobic) matter for calling the trait. (loivamaa2024aerobicadaptationand pages 9-12)

### Key concepts and current mechanistic understanding (2023–2024 prioritized where available)

#### 1) Wood–Werkman (methylmalonyl-CoA / transcarboxylase) route (propionibacteria; also used by *Cutibacterium*)
This is described as the predominant route in *Propionibacterium* spp. (and related propionibacteria). (rymuszka2026classicalfoodfermentations pages 19-20)

Mechanistic steps explicitly described in the fermentation review include:
* **Pyruvate → oxaloacetate** via a **biotin-dependent methylmalonyl-CoA carboxytransferase** (transfers a carboxyl group from methylmalonyl-CoA to pyruvate, producing oxaloacetate and propionyl-CoA). (rymuszka2026classicalfoodfermentations pages 19-20)
* Oxaloacetate → malate → fumarate → succinate; **succinate → succinyl-CoA** by **succinyl-CoA synthetase**. (rymuszka2026classicalfoodfermentations pages 19-20)
* **Vitamin B12-dependent methylmalonyl-CoA mutase** rearrangements connecting succinyl-CoA/methylmalonyl-CoA/propionyl-CoA. (rymuszka2026classicalfoodfermentations pages 19-20)
* **Propionyl-CoA → propionate** via a **CoA-transferase**. (rymuszka2026classicalfoodfermentations pages 19-20)
* A parallel **acetate branch**: pyruvate → acetyl-CoA (pyruvate dehydrogenase complex), then acetate via **phosphotransacetylase (PTA)** and **acetate kinase (AK)** generating ATP. (rymuszka2026classicalfoodfermentations pages 19-20)

**Redox balancing / NAD regeneration (recent evidence).** A 2023 genome-scale metabolic model (GEM) study of *Cutibacterium acnes* (skin-associated propionate producer) provides recent, quantitative systems-level evidence that propionate formation through the Wood–Werkman cycle is tightly coupled to NAD regeneration under glycerol-rich conditions (sebum context). The study reports: (i) Wood–Werkman reactions have up to ~2.5-fold higher flux under glycerol than glucose; (ii) NAD turnover increased by ~42.2% under glycerol-rich conditions; and (iii) the authors interpret this as use of Wood–Werkman flux to “replenish depleted NAD,” potentially leading to propionate overproduction in acne-associated skin conditions. (kim2023genomescalemetabolicmodeling pages 7-10)

A cropped view of the study’s Figure 3 supports the qualitative direction of these claims (higher Wood–Werkman flux and increased carbon fraction to propionate under glycerol vs glucose). (kim2023genomescalemetabolicmodeling media 9fcb0a88)

**Energy/redox cofactor accounting and knowledge gaps.** A 2024 FEMS Microbiology Reviews synthesis quantifies ATP and reduced cofactor bookkeeping for glucose fermentations to different end products (including propionate; values based on *Prevotella* spp.), and highlights that redox cofactor-balancing enzymes and complexes (e.g., Ferredoxin–NAD+ reductase, Nfn, Rnf) are central to fermentation energetics. (hackmann2024thevastlandscape pages 10-11)
Importantly for TraitMech curation, the same review explicitly flags an “outstanding gap” in the propionibacterial propionate pathway: propionibacteria form reduced ferredoxin via **pyruvate:ferredoxin oxidoreductase**, and knockout impairs growth, but the enzyme(s) transferring electrons from reduced ferredoxin to NAD+ remain unresolved; it also notes propionibacteria lack genes for Rnf. (hackmann2024thevastlandscape pages 9-10, hackmann2024thevastlandscape pages 10-11)

#### 2) Succinate pathway in gut Bacteroidia (propionate as one of mixed-acid outputs)
A 2024 experimental comparison across Bacteroidia highlights that propionate can be produced from glucose with strongly species-dependent product ratios, often including acetate, succinate, lactate, and formate. (doring2024propionateproductionby pages 1-2, doring2024propionateproductionby pages 12-13)
Mechanistically, it notes phosphoenolpyruvate can be converted to oxaloacetate via PEP carboxykinase, entering a reductive TCA/succinate route toward propionate. (doring2024propionateproductionby pages 1-2)

#### 3) Acrylate pathway (lactate-to-propionate)
A synthesis of fermentation routes describes the acrylate pathway as a distinct lactate-utilization route where lactate is converted through lactoyl-CoA and acryloyl-CoA intermediates, with enzymes including L-lactate dehydrogenase, lactoyl-CoA dehydratase, and acryloyl-CoA reductase (ETF/ETFH2-dependent), producing propionyl-CoA en route to propionate; the review notes that acryloyl-CoA toxicity and pH-linked redox disturbances can reduce propionate yield and shift flux toward acetate. (rymuszka2026classicalfoodfermentations pages 20-23)

### Candidate nodes (entities) for causal graph curation
Below are candidate entities grouped by type. Grounding suggestions are provided where broadly stable identifiers exist; some nodes remain label-only because the evidence excerpts do not supply database IDs.

#### A) Pathways / modules
* Wood–Werkman cycle / methylmalonyl-CoA pathway (label; often represented in KEGG/MetaCyc as methylmalonyl-CoA pathway components) (rymuszka2026classicalfoodfermentations pages 19-20)
* Succinate pathway to propionate (gut Bacteroidia context) (doring2024propionateproductionby pages 1-2)
* Acrylate pathway (lactate → propionate) (rymuszka2026classicalfoodfermentations pages 20-23)
* 1,2-propanediol pathway to propionate (mentioned as third major route) (rymuszka2026classicalfoodfermentations pages 19-20)
* Acetate formation branch (PTA/AK) as coupled ATP-generating module (rymuszka2026classicalfoodfermentations pages 19-20)

#### B) Enzymes / complexes (candidate mechanistic nodes)
* Methylmalonyl-CoA carboxytransferase / transcarboxylase (biotin-dependent) (rymuszka2026classicalfoodfermentations pages 19-20)
* Succinyl-CoA synthetase (rymuszka2026classicalfoodfermentations pages 19-20)
* Methylmalonyl-CoA mutase (vitamin B12-dependent) (rymuszka2026classicalfoodfermentations pages 19-20)
* CoA-transferase converting propionyl-CoA → propionate (label-only; specific enzyme varies by taxa) (rymuszka2026classicalfoodfermentations pages 19-20)
* Pyruvate dehydrogenase complex; phosphotransacetylase (PTA); acetate kinase (AK) (rymuszka2026classicalfoodfermentations pages 19-20)
* L-lactate dehydrogenase; lactoyl-CoA dehydratase; acryloyl-CoA reductase (ETF/ETFH2-dependent) (rymuszka2026classicalfoodfermentations pages 20-23)
* Pyruvate:ferredoxin oxidoreductase (propionibacteria redox; supports growth) (hackmann2024thevastlandscape pages 9-10)
* Redox/energy conservation entities appearing in 2024 fermentation energetics: Ferredoxin–NAD+ reductase, Nfn, Rnf (hackmann2024thevastlandscape pages 10-11)

#### C) Metabolites, products, and cofactors
* Propionate / propionic acid; acetate / acetic acid; CO2 (trait-defining outputs) (rymuszka2026classicalfoodfermentations pages 19-20)
* Succinate, lactate, formate (common mixed-acid co-products in gut taxa or process-dependent by-products) (doring2024propionateproductionby pages 12-13)
* Pyruvate, PEP, oxaloacetate, malate, fumarate, succinyl-CoA, methylmalonyl-CoA, propionyl-CoA (pathway intermediates) (rymuszka2026classicalfoodfermentations pages 19-20, doring2024propionateproductionby pages 1-2)
* Biotin; vitamin B12 (cobalamin); ATP; NAD/NADH; reduced ferredoxin (cofactors/energy carriers) (rymuszka2026classicalfoodfermentations pages 19-20, kim2023genomescalemetabolicmodeling pages 7-10, hackmann2024thevastlandscape pages 10-11, hackmann2024thevastlandscape pages 9-10)

#### D) Environmental / experimental factors
* Anaerobic conditions (defining environment) (rymuszka2026classicalfoodfermentations pages 19-20)
* Oxygen / aerobic vs microaerobic vs anaerobic (modulates propionate accumulation and B12 in *P. freudenreichii*) (loivamaa2024aerobicadaptationand pages 9-12)
* Carbon source: glycerol-rich (sebum-like) vs glucose (modulates Wood–Werkman flux and NAD turnover in *C. acnes* model) (kim2023genomescalemetabolicmodeling pages 7-10, kim2023genomescalemetabolicmodeling media 9fcb0a88)
* CO2 availability (affects growth/product spectrum in Bacteroidia comparison) (doring2024propionateproductionby pages 12-13)
* Bioprocess modes: high-cell-density with cell recycling; pH-controlled fed-batch; mineral salt medium; yeast extract supplementation (dishisha2024highcelldensity pages 2-4, doring2024propionateproductionby pages 12-13, neves2024expandingpseudomonastaiwanensis pages 7-10)

#### E) Taxa (organism nodes)
* *Acidipropionibacterium acidipropionici* DSM 4900 (propionate producer) (dishisha2024highcelldensity pages 1-2)
* *Propionibacterium freudenreichii* DSM 20271T (propionibacterium; oxygen effects on metabolites) (loivamaa2024aerobicadaptationand pages 9-12)
* *Cutibacterium acnes* (skin propionate producer; Wood–Werkman redox coupling) (kim2023genomescalemetabolicmodeling pages 7-10)
* Bacteroidia: *Bacteroides propionicifaciens* SV434 and *B. graminisolvens* XDT-1 (glucose → propionate + mixed acids) (doring2024propionateproductionby pages 12-13)
* Prevotella spp. (basis for propionate ATP/redox accounting in 2024 review) (hackmann2024thevastlandscape pages 10-11)

### Candidate causal edges (evidence-backed triples)
The following artifact provides a curation-oriented edge table. Each row indicates a proposed triple with evidence citations and curator notes.

| Subject node | Predicate | Object node | Pathway/context | Evidence summary | Citation id(s) | Curation notes |
|---|---|---|---|---|---|---|
| propionic acid fermentation | has_major_pathway | Wood–Werkman cycle | Classical propionibacterial fermentation | The Wood–Werkman methylmalonyl-CoA cycle is described as the predominant propionate-forming route in Propionibacterium and Acidipropionibacterium. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong; central defining route for the trait in propionibacteria. |
| propionic acid fermentation | has_major_pathway | succinate pathway | Bacteroidia and gut-associated propionate formation | Comparative work in Bacteroidia notes propionate formation via the succinate pathway, alongside acrylate and 1,2-propanediol routes. | (doring2024propionateproductionby pages 1-2) | Strong for broader propionate fermentation; not exclusive to classical propionibacteria. |
| propionic acid fermentation | has_alternative_pathway | acrylate pathway | Lactate-to-propionate fermentation | Reviews identify the acrylate route as a principal alternative route from lactate to propionate in taxa such as Megasphaera and Anaerotignum or Clostridium propionicum. | (rymuszka2026classicalfoodfermentations pages 20-23, facchin2025rethinkingshortchainfatty pages 2-4) | Strong as alternative route; boundary case relative to a narrower Wood–Werkman-centered definition. |
| pyruvate | causally_upstream_of | oxaloacetate | Wood–Werkman cycle | In the Wood–Werkman route, pyruvate is carboxylated to oxaloacetate by methylmalonyl-CoA carboxytransferase or transcarboxylase in a biotin-dependent reaction. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong biochemical step; enzyme naming should be checked against preferred database term. |
| biotin | cofactor_for | methylmalonyl-CoA carboxytransferase | Wood–Werkman cycle | The transcarboxylation step converting pyruvate to oxaloacetate is explicitly described as biotin-dependent. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong; cofactor edge suitable for pathway support. |
| methylmalonyl-CoA carboxytransferase | produces | oxaloacetate | Wood–Werkman cycle | The enzyme transfers a carboxyl group to pyruvate, yielding oxaloacetate as part of carbon-conserving propionate fermentation. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong; could also be modeled as enzyme enables reaction. |
| methylmalonyl-CoA carboxytransferase | produces | propionyl-CoA | Wood–Werkman cycle | The same transcarboxylation step is described as yielding oxaloacetate plus propionyl-CoA from methylmalonyl-CoA and pyruvate. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong; key mechanistic edge for propionate-forming flux. |
| oxaloacetate | causally_upstream_of | malate | Wood–Werkman cycle | Oxaloacetate is reduced to malate in the reductive branch leading toward succinate. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong pathway edge; enzyme not named in snippet. |
| malate | causally_upstream_of | fumarate | Wood–Werkman cycle | Malate is dehydrated to fumarate in the Wood–Werkman route. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong pathway edge. |
| fumarate | causally_upstream_of | succinate | Wood–Werkman cycle | Fumarate is reduced to succinate en route to propionate formation. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong pathway edge. |
| succinate | causally_upstream_of | succinyl-CoA | Wood–Werkman cycle | Succinate is converted to succinyl-CoA by succinyl-CoA synthetase before rearrangement steps. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong biochemical step. |
| succinyl-CoA | causally_upstream_of | methylmalonyl-CoA | Wood–Werkman cycle | The pathway proceeds through succinyl-CoA and methylmalonyl-CoA intermediates during propionate formation. | (rymuszka2026classicalfoodfermentations pages 19-20, rymuszka2026classicalfoodfermentations pages 20-23) | Strong, though exact reaction direction and epimerization details are simplified. |
| vitamin B12 | cofactor_for | methylmalonyl-CoA mutase | Wood–Werkman cycle | The rearrangement step involving methylmalonyl-CoA mutase is explicitly described as vitamin B12-dependent. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong; important taxon-level dependency in many propionibacteria. |
| methylmalonyl-CoA mutase | causally_upstream_of | propionyl-CoA formation | Wood–Werkman cycle | The B12-dependent mutase-mediated rearrangement is part of the final conversion sequence leading to propionyl-CoA and then propionate. | (rymuszka2026classicalfoodfermentations pages 19-20) | Moderate; snippet compresses intermediate details, so exact object may need refinement. |
| propionyl-CoA | causally_upstream_of | propionate | Wood–Werkman cycle | Propionyl-CoA is finally converted to propionic acid or propionate by a CoA-transferase. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong; enzyme label may need grounding to a specific CoA-transferase. |
| pyruvate | causally_upstream_of | acetyl-CoA | Wood–Werkman-associated acetate branch | A parallel branch converts pyruvate to acetyl-CoA via pyruvate dehydrogenase. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong; useful by-product branch rather than trait-defining route. |
| acetyl-CoA | causally_upstream_of | acetate | Wood–Werkman-associated acetate branch | Acetyl-CoA is converted to acetate through phosphotransacetylase and acetate kinase, generating ATP. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong; explains typical acetate co-production. |
| propionic acid fermentation | has_byproduct | acetate | Classical propionibacterial fermentation | The fermentation is defined as producing propionic acid with acetate as a co-product. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong; high-level phenotype edge. |
| propionic acid fermentation | has_byproduct | CO2 | Classical propionibacterial fermentation | The defining end-product spectrum includes propionate with acetate and CO2. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong at phenotype level; note Wood–Werkman is more carbon-conserving than a classical CO2-releasing succinate route. |
| glucose fermentation | yields | propionate plus acetate plus CO2 | Classical propionibacterial fermentation | Stoichiometry is given for glucose conversion to 4/3 propionate, 2/3 acetate, and 2/3 CO2, plus water and ATP. | (rymuszka2026classicalfoodfermentations pages 19-20) | Strong but represents an idealized stoichiometric summary, not a universal assay observation. |
| phosphoenolpyruvate | causally_upstream_of | oxaloacetate | Succinate pathway in Bacteroidia | The Bacteroidia study notes PEP can be converted to oxaloacetate via PEP carboxykinase, entering the reductive TCA and succinate route toward propionate. | (doring2024propionateproductionby pages 1-2) | Strong for Bacteroidia succinate route; taxon-specific. |
| succinate pathway | causally_upstream_of | propionate production | Bacteroidia | Comparative Bacteroidia evidence supports succinate as a major intermediate route to propionate, with product spectra including propionate, succinate, acetate, lactate, and formate. | (doring2024propionateproductionby pages 1-2) | Strong at pathway level; exact downstream enzymes are not fully resolved in the snippet. |
| low CO2 conditions | differentially_affect | propionate production in Bacteroides propionicifaciens versus Bacteroides graminisolvens | Bacteroidia physiology | Bacteroides propionicifaciens was less affected by low CO2 than Bacteroides graminisolvens, indicating environmental modulation of succinate-route propionate production. | (doring2024propionateproductionby pages 12-13) | Useful environmental edge, but comparative and organism-specific; uncertain for a generic trait graph. |
| lactate | causally_upstream_of | lactoyl-CoA | Acrylate pathway | In the acrylate route, lactate is converted to lactoyl-CoA via propionyl-CoA transferase while releasing propionate. | (rymuszka2026classicalfoodfermentations pages 20-23) | Moderate; wording is summarized from a review and may need reaction-level confirmation. |
| lactoyl-CoA | causally_upstream_of | acryloyl-CoA | Acrylate pathway | Lactoyl-CoA dehydratase converts lactoyl-CoA to acryloyl-CoA. | (rymuszka2026classicalfoodfermentations pages 20-23) | Strong pathway step for the acrylate route. |
| acryloyl-CoA | causally_upstream_of | propionyl-CoA | Acrylate pathway | Acryloyl-CoA reductase reduces acryloyl-CoA to propionyl-CoA using ETF or ETFH2-linked electron transfer. | (rymuszka2026classicalfoodfermentations pages 20-23) | Strong pathway step; enzyme and cofactor pair are route-defining. |
| propionyl-CoA | causally_upstream_of | propionate | Acrylate pathway | In the acrylate route, propionyl-CoA is the immediate precursor to propionate. | (rymuszka2026classicalfoodfermentations pages 20-23, facchin2025rethinkingshortchainfatty pages 2-4) | Strong, though the terminal enzyme may vary by organism. |
| lactoyl-CoA dehydratase | enables | lactoyl-CoA to acryloyl-CoA conversion | Acrylate pathway | The review explicitly names lactoyl-CoA dehydratase for the dehydration step. | (rymuszka2026classicalfoodfermentations pages 20-23) | Strong; enzyme node candidate. |
| acryloyl-CoA reductase | enables | acryloyl-CoA to propionyl-CoA conversion | Acrylate pathway | The review explicitly names acryloyl-CoA reductase and notes ETF or ETFH2 dependence. | (rymuszka2026classicalfoodfermentations pages 20-23) | Strong; enzyme and cofactor candidate. |
| acryloyl-CoA | negatively_affects | propionate yield | Acrylate pathway | Acryloyl-CoA toxicity and pH-linked redox disturbances are noted to shift flux toward acetate and lower propionate yield. | (rymuszka2026classicalfoodfermentations pages 20-23) | Moderate; mechanism is pathway-specific and partly process-dependent. |
| glycerol-rich conditions | positively_regulate | Wood–Werkman cycle flux | Cutibacterium acnes skin-associated metabolism | Flux analysis in Cutibacterium acnes showed significantly higher Wood–Werkman flux under glycerol than glucose, with propionate as the dominant secreted SCFA. | (kim2023genomescalemetabolicmodeling pages 7-10) | Strong but taxon- and model-specific; useful as a conditional regulation edge. |
| Wood–Werkman cycle | contributes_to | NAD regeneration | Cutibacterium acnes glycerol metabolism | Modeling suggests overproduction of propionate via the Wood–Werkman cycle is strongly linked to NAD regeneration and redox balancing. | (kim2023genomescalemetabolicmodeling pages 10-11, kim2023genomescalemetabolicmodeling pages 7-10) | Strong for the C. acnes model; should be marked taxon- and context-specific rather than universal. |
| anaerobic conditions | positively_regulate | lactate utilization operon expression | Propionibacterium freudenreichii | Under anaerobic growth, the glcA-lutABC operon including an L-lactate permease was upregulated, matching faster lactate consumption. | (loivamaa2024aerobicadaptationand pages 9-12) | Relevant for substrate use feeding propionate fermentation, but indirect to propionate output. |
| aerobic conditions | negatively_affect | propionate accumulation | Propionibacterium freudenreichii | Under more aerobic conditions, lactate consumption did not lead to propionate accumulation and B12 production was reduced compared with microaerobic conditions. | (loivamaa2024aerobicadaptationand pages 9-12) | Strong but strain- and process-specific; useful environmental modifier edge. |


*Table: This table lists evidence-backed candidate causal edges for curation of propionic acid fermentation, emphasizing the Wood–Werkman route, Bacteroidia succinate pathway, and lactate-based acrylate pathway. It distinguishes broad trait-defining edges from taxon- or condition-specific edges that may need cautious curation.*

### Recent developments and quantitative data (2023–2024 prioritized)
The following artifact compiles reported 2023–2024 titers/yields/productivities and relevant benchmarks.

| Organism/strain | Process/condition | Substrate(s) | Propionate/propionic acid titer | Yield | Productivity/rate | By-products or notes | Reference (DOI, year, URL) | Citation id (pqac-...) |
|---|---|---|---|---|---|---|---|---|
| *Acidipropionibacterium acidipropionici* DSM 4900 | High-cell-density sequential batch fermentation with cell recycle; heat-treated potato juice as N-source | 40 g/L glucose | 18.76 ± 1.34 g/L average PA across 9 batches; individual final PA 17.51–21.27 g/L | 0.59 g PA/g glucose average; individual 0.53–0.59 g/g | Maximum 1.15 g/L·h; batch Qp increased from 0.18 to 1.15 g/L·h | Major by-products succinic acid and acetic acid; average PA:SA:AA = 100:23:25; biomass up to 39.89 g CDW/L | 10.1186/s12934-024-02366-5, 2024, https://doi.org/10.1186/s12934-024-02366-5 | (dishisha2024highcelldensity pages 1-2, dishisha2024highcelldensity pages 2-4) |
| *Acidipropionibacterium acidipropionici* DSM 4900 | High-cell-density sequential batch co-fermentation with cell recycle | Crude glycerol/glucose mixture (60 g/L:30 g/L) | 35.36 ± 2.17 g/L average PA across 6 batches | 0.51 g PA/g carbon source | Maximum 0.35 g/L·h; with 0.75 mg/L biotin, productivity increased to 0.48 g/L·h | Lower acetate than glucose-only process; PA:SA:AA = 100:29:3; biotin increased biomass to 21.89 g CDW/L but doubled acetate | 10.1186/s12934-024-02366-5, 2024, https://doi.org/10.1186/s12934-024-02366-5 | (dishisha2024highcelldensity pages 1-2) |
| *Bacteroides propionicifaciens* SV434 | pH-controlled fed-batch cultivation | Glucose; 130 mM supplied in fed-batch context | 8.8 g/L propionate; also reported as 119 mM | 0.9 mol propionate/mol glucose or 0.37 g/g; elsewhere summarized as 0.39 g/g | Overall 0.09 g/L·h; peak 0.21 g/L·h | Succinate appeared under carbon excess; authors note Bacteroidia still below propionibacterial performance but promising for plant-polymer conversion | 10.1186/s13068-024-02539-9, 2024, https://doi.org/10.1186/s13068-024-02539-9 | (doring2024propionateproductionby pages 12-13, doring2024propionateproductionby pages 1-2) |
| *Bacteroides graminisolvens* XDT-1 | pH-controlled fed-batch cultivation | Glucose; 160 mM supplied, 107 mM consumed | 2.4 g/L propionate; also reported as 33 mM | 0.31 mol propionate/mol glucose or 0.13 g/g; elsewhere summarized as 0.25 g/g in comparative screen | Not directly reported as g/L·h in excerpt | Produced 14 mM acetate, 25 mM formate, 25 mM lactate, 45 mM succinate; succinate became main product under further cultivation | 10.1186/s13068-024-02539-9, 2024, https://doi.org/10.1186/s13068-024-02539-9 | (doring2024propionateproductionby pages 12-13, doring2024propionateproductionby pages 1-2) |
| Engineered *Pseudomonas taiwanensis* VLB120 | Aerobic fed-batch bioreactor; mineral salt medium; single genomic copy of sleeping beauty mutase genes plus methylcitrate synthase deletion | Not fully specified in excerpt; mineral salt medium fed-batch | 2.8 ± 0.4 g/L propionate; also reported as 39 ± 6 mM | Not directly reported in excerpt | Maximal specific productivity 11 mg h−1 g−1 | Minimal engineering strategy; no by-products noted; positioned as non-traditional chassis for propionyl-CoA-derived odd-chain products | 10.1111/1751-7915.14309, 2024, https://doi.org/10.1111/1751-7915.14309 | (neves2024expandingpseudomonastaiwanensis pages 1-2, neves2024expandingpseudomonastaiwanensis pages 7-10) |
| *Cutibacterium acnes* (GEM iCA843; RT5-related model) | In silico skin-condition simulation comparing glycerol vs glucose; Wood–Werkman flux analysis | Endogenous skin carbon source context, especially glycerol vs glucose | Propionate was predicted as the dominant secreted SCFA; under glycerol, ~68% of carbon output directed to propionate vs ~40% under glucose | Not reported as g/g | Wood–Werkman reactions increased up to ~2.5-fold under glycerol; NAD turnover increased 42.2% in glycerol-rich condition | Quantitative values are model-predicted, not fermentation titers; supports glycerol-linked redox balancing and propionate overproduction in acne-associated conditions | 10.3389/fcimb.2023.1099314, 2023, https://doi.org/10.3389/fcimb.2023.1099314 | (kim2023genomescalemetabolicmodeling pages 10-11, kim2023genomescalemetabolicmodeling pages 7-10, kim2023genomescalemetabolicmodeling media 9fcb0a88) |
| Competitive benchmark for glucose-based microbial propionate fermentation | Industry/economic benchmark cited in 2024 Bacteroidia study | Glucose | Target titer 100 g/L | Target yield 0.6 g propionate/g glucose | Target productivity 1–2 g/L·h | Benchmark for economic competitiveness; authors note no commercial microbial propionate production known to them | 10.1186/s13068-024-02539-9, 2024, https://doi.org/10.1186/s13068-024-02539-9 | (doring2024propionateproductionby pages 1-2) |
| Prior comparator cited within 2024 Bacteroidia study: *Propionibacterium acidipropionici* | pH-controlled setup, comparator from earlier literature summarized by authors | Up to 40 g/L glucose | 16.3 g/L propionate | ~0.41 g/g | Not stated in excerpt | Comparator used to contextualize Bacteroidia performance; immobilized-cell whey-lactose studies reported titers well above 100 g/L | 10.1186/s13068-024-02539-9, 2024, https://doi.org/10.1186/s13068-024-02539-9 | (doring2024propionateproductionby pages 12-13) |


*Table: This table compiles the main quantitative 2023–2024 performance data and benchmarks for microbial propionate production relevant to propionic acid fermentation. It is useful for comparing taxa, processes, and industrially relevant targets across natural and engineered systems.*

Notable recent data points include:
* High-cell-density sequential batch fermentation using *A. acidipropionici* achieved ~18.8 g/L propionic acid from 40 g/L glucose (yield ~0.59 g/g) with maximum productivity 1.15 g/L·h; glycerol/glucose co-fermentation achieved ~35.4 g/L propionic acid (0.51 g/g C-source). (dishisha2024highcelldensity pages 1-2, dishisha2024highcelldensity pages 2-4)
* In Bacteroidia fed-batch, *B. propionicifaciens* reached 8.8 g/L propionate (0.37 g/g; peak 0.21 g/L·h), while *B. graminisolvens* produced lower propionate and accumulated succinate/lactate/formate. (doring2024propionateproductionby pages 12-13)
* Engineered aerobic *Pseudomonas taiwanensis* achieved ~2.8 g/L propionate in mineral salt medium (fed-batch), illustrating non-anaerobic chassis use for propionyl-CoA derived products. (neves2024expandingpseudomonastaiwanensis pages 7-10)
* Systems biology (GEM) evidence in *C. acnes* links higher Wood–Werkman flux under glycerol (up to ~2.5×) to higher NAD turnover (42.2%), interpreted as NAD regeneration driving propionate overproduction in acne-associated conditions. (kim2023genomescalemetabolicmodeling pages 7-10, kim2023genomescalemetabolicmodeling media 9fcb0a88)

### Current applications and real-world implementations
**Food/feed preservation and additives.** Propionic acid and salts (propionates) are widely used as preservatives, especially in bakery and feed/silage contexts; they inhibit molds and some bacteria, and are a major driver of propionate demand. (rymuszka2026classicalfoodfermentations pages 24-25)

**Platform chemical and derivatives.** A 2024 analysis emphasizes propionic acid as a platform chemical, with reported market/trade statistics: ~463,000 t traded in 2022 and projected ~600,000 t by 2030; prices ~1–2 €/kg for propionic acid and much higher for derivatives (up to ~600 €/kg). (doring2024propionateproductionby pages 1-2)

**Industrial fermentation co-products (vitamin B12).** Propionibacteria (e.g., *P. freudenreichii*, *P. acidipropionici*) are noted for industrial vitamin B12 production in the context of propionic fermentation platforms. (rymuszka2026classicalfoodfermentations pages 24-25)

**Bioprocess implementation themes (expert synthesis).** Recent work emphasizes that biological propionate production is constrained by product inhibition and mixed-acid by-products; process intensification approaches such as cell recycling/high-cell-density cultivation can increase volumetric productivities and support use of industrial by-products as media components (e.g., crude glycerol, potato juice). (dishisha2024highcelldensity pages 1-2)

### Expert opinions / authoritative analysis (what is solid vs still uncertain)
* **Solid consensus:** Multiple routes to propionate exist; Wood–Werkman dominates in classical propionibacteria; acetate and CO2 are typical co-products in classical propionic fermentation and are linked to ATP generation via PTA/AK. (rymuszka2026classicalfoodfermentations pages 19-20)
* **Mechanistic uncertainty relevant for curation:** The 2024 FEMS Microbiology Reviews article explicitly states that, despite being first delineated in propionibacteria, the propionate pathway still has unresolved steps in propionibacteria concerning electron transfer from reduced ferredoxin to NAD+, and calls for biochemical verification; it also notes propionibacteria lack genes for Rnf. (hackmann2024thevastlandscape pages 9-10, hackmann2024thevastlandscape pages 10-11)
* **Context dependence:** Oxygen can shift metabolite outputs in *P. freudenreichii* (aerobic growth altered propionate accumulation and reduced B12 vs microaerobic), indicating that trait assays should control pO2 or record it. (loivamaa2024aerobicadaptationand pages 9-12)

### Bibliography (DOI-first; URLs and publication dates)
* Kim S-K, et al. (2023-07). Genome-scale metabolic modeling and in silico analysis of opportunistic skin pathogen *Cutibacterium acnes*. *Frontiers in Cellular and Infection Microbiology*. DOI:10.3389/fcimb.2023.1099314. https://doi.org/10.3389/fcimb.2023.1099314 (kim2023genomescalemetabolicmodeling pages 7-10)
* Hackmann TJ. (2024-05). The vast landscape of carbohydrate fermentation in prokaryotes. *FEMS Microbiology Reviews*. DOI:10.1093/femsre/fuae016. https://doi.org/10.1093/femsre/fuae016 (hackmann2024thevastlandscape pages 10-11)
* Dishisha T, Jain M, Hatti-Kaul R. (2024-03). High cell density sequential batch fermentation for enhanced propionic acid production… *Microbial Cell Factories*. DOI:10.1186/s12934-024-02366-5. https://doi.org/10.1186/s12934-024-02366-5 (dishisha2024highcelldensity pages 2-4)
* Döring C, Basen M. (2024-07). Propionate production by Bacteroidia gut bacteria… *Biotechnology for Biofuels and Bioproducts*. DOI:10.1186/s13068-024-02539-9. https://doi.org/10.1186/s13068-024-02539-9 (doring2024propionateproductionby pages 12-13)
* Loivamaa I, et al. (2024-10). Aerobic adaptation and metabolic dynamics of *Propionibacterium freudenreichii* DSM 20271… *mSystems*. DOI:10.1128/msystems.00615-24. https://doi.org/10.1128/msystems.00615-24 (loivamaa2024aerobicadaptationand pages 9-12)
* Neves D, et al. (2024-08). Expanding *Pseudomonas taiwanensis* VLB120's acyl-CoA portfolio: Propionate production… *Microbial Biotechnology*. DOI:10.1111/1751-7915.14309. https://doi.org/10.1111/1751-7915.14309 (neves2024expandingpseudomonastaiwanensis pages 7-10)
* Rymuszka A, Gorczynska W. (2026-01). Classical Food Fermentations… Propionic pathways and applications. *Molecules*. DOI:10.3390/molecules31020333. https://doi.org/10.3390/molecules31020333 (rymuszka2026classicalfoodfermentations pages 19-20)

### Warnings / “do not curate yet” items
* **Do not over-specify the electron-transfer step(s) linking reduced ferredoxin to NAD+ in propionibacterial propionate fermentation**: the 2024 authoritative review notes this remains unresolved and needs biochemical verification; modeling this edge as a specific enzyme reaction would be premature without direct evidence. (hackmann2024thevastlandscape pages 9-10)
* **Treat model-based (in silico) flux regulation edges as condition- and model-specific** (e.g., *C. acnes* GEM predictions under glycerol vs glucose), and avoid curating them as universal mechanistic truths across propionate fermenters without additional experimental validation. (kim2023genomescalemetabolicmodeling pages 7-10, kim2023genomescalemetabolicmodeling media 9fcb0a88)
* **Taxon specificity:** The succinate pathway physiology and limiting steps (e.g., discussion of succinyl-CoA-transferase limitation) may not generalize from propionibacteria to Bacteroidia; annotate edges as taxon-specific where appropriate. (doring2024propionateproductionby pages 12-13)


References

1. (rymuszka2026classicalfoodfermentations pages 19-20): Anna Rymuszka and Wiktoria Gorczynska. Classical food fermentations as modern biotechnological platforms: alcoholic, acetic, butyric, lactic and propionic pathways and applications. Molecules, 31(2):333, Jan 2026. URL: https://doi.org/10.3390/molecules31020333, doi:10.3390/molecules31020333. This article has 3 citations.

2. (doring2024propionateproductionby pages 1-2): Carolin Döring and Mirko Basen. Propionate production by bacteroidia gut bacteria and its dependence on substrate concentrations differs among species. Biotechnology for Biofuels and Bioproducts, Jul 2024. URL: https://doi.org/10.1186/s13068-024-02539-9, doi:10.1186/s13068-024-02539-9. This article has 22 citations and is from a domain leading peer-reviewed journal.

3. (loivamaa2024aerobicadaptationand pages 9-12): Iida Loivamaa, Annika Sillanpää, Paulina Deptula, Bhawani Chamlagain, Minnamari Edelmann, Petri Auvinen, Tuula A. Nyman, Kirsi Savijoki, Vieno Piironen, and Pekka Varmanen. Aerobic adaptation and metabolic dynamics of <i>propionibacterium freudenreichii</i> dsm 20271: insights from comparative transcriptomics and surfaceome analysis. Oct 2024. URL: https://doi.org/10.1128/msystems.00615-24, doi:10.1128/msystems.00615-24. This article has 5 citations and is from a peer-reviewed journal.

4. (kim2023genomescalemetabolicmodeling pages 7-10): Su-Kyung Kim, Minouk Lee, Yi Qing Lee, Hyun Jun Lee, Mina Rho, Yunkwan Kim, Jung Yeon Seo, Sung Hun Youn, Seung Jin Hwang, Nae Gyu Kang, Choong-Hwan Lee, Seo-Young Park, and Dong-Yup Lee. Genome-scale metabolic modeling and in silico analysis of opportunistic skin pathogen cutibacterium acnes. Frontiers in Cellular and Infection Microbiology, Jul 2023. URL: https://doi.org/10.3389/fcimb.2023.1099314, doi:10.3389/fcimb.2023.1099314. This article has 16 citations.

5. (kim2023genomescalemetabolicmodeling media 9fcb0a88): Su-Kyung Kim, Minouk Lee, Yi Qing Lee, Hyun Jun Lee, Mina Rho, Yunkwan Kim, Jung Yeon Seo, Sung Hun Youn, Seung Jin Hwang, Nae Gyu Kang, Choong-Hwan Lee, Seo-Young Park, and Dong-Yup Lee. Genome-scale metabolic modeling and in silico analysis of opportunistic skin pathogen cutibacterium acnes. Frontiers in Cellular and Infection Microbiology, Jul 2023. URL: https://doi.org/10.3389/fcimb.2023.1099314, doi:10.3389/fcimb.2023.1099314. This article has 16 citations.

6. (hackmann2024thevastlandscape pages 10-11): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

7. (hackmann2024thevastlandscape pages 9-10): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 24 citations and is from a domain leading peer-reviewed journal.

8. (doring2024propionateproductionby pages 12-13): Carolin Döring and Mirko Basen. Propionate production by bacteroidia gut bacteria and its dependence on substrate concentrations differs among species. Biotechnology for Biofuels and Bioproducts, Jul 2024. URL: https://doi.org/10.1186/s13068-024-02539-9, doi:10.1186/s13068-024-02539-9. This article has 22 citations and is from a domain leading peer-reviewed journal.

9. (rymuszka2026classicalfoodfermentations pages 20-23): Anna Rymuszka and Wiktoria Gorczynska. Classical food fermentations as modern biotechnological platforms: alcoholic, acetic, butyric, lactic and propionic pathways and applications. Molecules, 31(2):333, Jan 2026. URL: https://doi.org/10.3390/molecules31020333, doi:10.3390/molecules31020333. This article has 3 citations.

10. (dishisha2024highcelldensity pages 2-4): Tarek Dishisha, Mridul Jain, and Rajni Hatti-Kaul. High cell density sequential batch fermentation for enhanced propionic acid production from glucose and glycerol/glucose mixture using acidipropionibacterium acidipropionici. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02366-5, doi:10.1186/s12934-024-02366-5. This article has 14 citations and is from a peer-reviewed journal.

11. (neves2024expandingpseudomonastaiwanensis pages 7-10): Dário Neves, Daniel Meinen, Tobias B. Alter, Lars M. Blank, and Birgitta E. Ebert. Expanding pseudomonas taiwanensis vlb120's acyl‐coa portfolio: propionate production in mineral salt medium. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14309, doi:10.1111/1751-7915.14309. This article has 3 citations and is from a peer-reviewed journal.

12. (dishisha2024highcelldensity pages 1-2): Tarek Dishisha, Mridul Jain, and Rajni Hatti-Kaul. High cell density sequential batch fermentation for enhanced propionic acid production from glucose and glycerol/glucose mixture using acidipropionibacterium acidipropionici. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02366-5, doi:10.1186/s12934-024-02366-5. This article has 14 citations and is from a peer-reviewed journal.

13. (facchin2025rethinkingshortchainfatty pages 2-4): Sonia Facchin, Matteo Calgaro, and Edoardo V. Savarino. Rethinking short-chain fatty acids: a closer look at propionate in inflammation, metabolism, and mucosal homeostasis. Cells, 14:1130, Jul 2025. URL: https://doi.org/10.3390/cells14151130, doi:10.3390/cells14151130. This article has 43 citations.

14. (kim2023genomescalemetabolicmodeling pages 10-11): Su-Kyung Kim, Minouk Lee, Yi Qing Lee, Hyun Jun Lee, Mina Rho, Yunkwan Kim, Jung Yeon Seo, Sung Hun Youn, Seung Jin Hwang, Nae Gyu Kang, Choong-Hwan Lee, Seo-Young Park, and Dong-Yup Lee. Genome-scale metabolic modeling and in silico analysis of opportunistic skin pathogen cutibacterium acnes. Frontiers in Cellular and Infection Microbiology, Jul 2023. URL: https://doi.org/10.3389/fcimb.2023.1099314, doi:10.3389/fcimb.2023.1099314. This article has 16 citations.

15. (neves2024expandingpseudomonastaiwanensis pages 1-2): Dário Neves, Daniel Meinen, Tobias B. Alter, Lars M. Blank, and Birgitta E. Ebert. Expanding pseudomonas taiwanensis vlb120's acyl‐coa portfolio: propionate production in mineral salt medium. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14309, doi:10.1111/1751-7915.14309. This article has 3 citations and is from a peer-reviewed journal.

16. (rymuszka2026classicalfoodfermentations pages 24-25): Anna Rymuszka and Wiktoria Gorczynska. Classical food fermentations as modern biotechnological platforms: alcoholic, acetic, butyric, lactic and propionic pathways and applications. Molecules, 31(2):333, Jan 2026. URL: https://doi.org/10.3390/molecules31020333, doi:10.3390/molecules31020333. This article has 3 citations.