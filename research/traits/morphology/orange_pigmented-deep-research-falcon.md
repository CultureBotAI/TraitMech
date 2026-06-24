---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:46:11.826597'
end_time: '2026-06-18T09:05:07.207475'
duration_seconds: 1135.38
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: orange pigmented
  trait_identifier: METPO:1003026
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: orange_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    orange due to production and accumulation of orange pigments such as carotenoids.
  parent_traits: METPO:1003021
  synonyms: Pigment_orange
  evidence_summary: 'DOI:10.1080/1040841X.2025.2526423: orange ... pigmentation in
    bacteria (Supports orange microbial pigmentation as a bacterial carotenoid-associated
    color phenotype.)'
  causal_graph_summary: 'orange_pigmented_carotenoid_accumulation: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** orange pigmented
- **METPO identifier:** METPO:1003026
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear orange due to production and accumulation of orange pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_orange
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: orange ... pigmentation in bacteria (Supports orange microbial pigmentation as a bacterial carotenoid-associated color phenotype.)
- **Existing causal graph summary:** orange_pigmented_carotenoid_accumulation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **orange pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/orange_pigmented.yaml`.

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
- **Trait label:** orange pigmented
- **METPO identifier:** METPO:1003026
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear orange due to production and accumulation of orange pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_orange
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: orange ... pigmentation in bacteria (Supports orange microbial pigmentation as a bacterial carotenoid-associated color phenotype.)
- **Existing causal graph summary:** orange_pigmented_carotenoid_accumulation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **orange pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/orange_pigmented.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **orange pigmented** (METPO:1003026)

### Executive scope summary
The trait **orange pigmented** (METPO:1003026) is best operationalized as an **assay-observed colony/cell coloration** in which microbes appear orange (often described as orange, golden, or yellow-orange) due to **accumulation of carotenoid-class isoprenoid pigments**. In 2023–2024 primary and review literature, orange coloration is frequently linked to (i) **C30 carotenoids** such as **staphyloxanthin** and related diaponeurosporene-family intermediates in **Staphylococcus** and other Firmicutes, (ii) **C40 carotenoids** such as **β-carotene** (orange) and related xanthophylls/ketocarotenoids in diverse bacteria, and (iii) **monocyclic marine carotenoids** (e.g., flexixanthin derivatives) yielding orange-to-red hues in Bacteroidota genera such as **Algoriphagus**. (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, sosafajardo2024genomicexplorationof pages 16-17, takatani2024identificationofa pages 1-2)

**Boundary cases for curation**:
- **Red pigmentation** can reflect accumulation of red carotenoids such as **lycopene** (a pathway intermediate). This should generally map to a different trait (e.g., “red pigmented”) unless the observable is explicitly orange. In *Mycobacterium kansasii*, mutants accumulating lycopene exhibit a red phenotype (RR), illustrating a clear mechanistic boundary. (janisch2023geneticunderpinningsof pages 5-8)
- **Photochromogenic phenotypes** (white in dark, yellow/orange in light) are environment-dependent; the causal graph should represent light as an upstream environmental node for taxa where this is relevant. (janisch2023geneticunderpinningsof pages 5-8, janisch2023geneticunderpinningsof media 296b2fee)
- **Assay/media artifacts**: media composition can substantially change measured pigment abundance and apparent shade, so media should be represented as experimental factors rather than intrinsic mechanisms. In *S. aureus*, beetroot/carrot/milk agar increased pigment absorbance and shifted UV-Vis maxima. (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11)

### Key concepts and definitions (current understanding)
1. **Carotenoids as the dominant mechanistic substrate of orange coloration**
   - Staphylococcal orange/golden pigmentation is attributed to the carotenoid **staphyloxanthin** (a membrane-associated C30 carotenoid), with chemical identity reported as **β-D-glucopyranosyl 1-O-(4,4′-diaponeurosporen-4-oate)-6-O-(12-methyltetradecanoate)**. (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2)
   - In marine bacteria such as *Algoriphagus*, orange-to-red pigments can be monocyclic carotenoids such as **flexixanthin** and **2-hydroxyflexixanthin**. (takatani2024identificationofa pages 1-2)
   - Canonical (often C40) carotenoid pathways proceed from IPP/DMAPP-derived precursors to GGPP, then to phytoene, then to colored intermediates and end products (e.g., lycopene → β-carotene), which are associated with yellow/orange/red appearance. (stra2023carotenoidmetabolismnew pages 1-2)

2. **Trait-mechanism mapping principle for METPO:1003026**
   - For TraitMech, the trait is primarily a **morphological readout**. Mechanistic nodes should therefore connect: precursor metabolism → carotenoid biosynthesis genes/enzymes → pigment accumulation → **orange visible phenotype**. Operon/cluster nodes (crtOPQMN; crtEIBYcYd) are useful “mid-level” abstractions when individual enzymatic steps are not yet curated per taxon. (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, janisch2023geneticunderpinningsof pages 5-8)

### Recent developments and latest research (prioritize 2023–2024)
#### A. C30 carotenoids and orange/golden pigmentation in staphylococci (2024)
- **Biosynthetic genetics and chemistry**: Staphyloxanthin biosynthesis is encoded by the **crtOPQMN operon** and proceeds through **CrtM** and subsequent steps leading to glycosylation and acylation to yield the final pigment. (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2)
- **Experimental modulation and quantification**: A 2024 study showed that agar media altered pigment abundance measured at 460 nm (microtiter): nutrient agar 0.13; beetroot+carrot 0.19; carrot 0.26; milk 0.29; beetroot 0.46, with strong correlation between pigment concentration and incubation time (r = 0.93, p < 0.01). This supports explicit experimental-factor nodes (media composition, incubation time) as upstream modifiers. (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11)

#### B. Photochromogenic carotenoid regulation and red-vs-orange boundary in *Mycobacterium kansasii* (2023)
- A 2023 genetics/transposon study identified a crt gene cluster (**crtEIBYcYd**) and regulators controlling light-induced pigmentation; **crtR** was required for normal pigmentation and mutants displayed altered phenotypes. Mutants accumulated red lycopene (RR phenotype), supporting a mechanistic boundary between orange/yellow outcomes and red pigmentation. (janisch2023geneticunderpinningsof pages 5-8)
- Visual figures from the same study summarize phenotype classes (white/yellow/orange/red) and the proposed pathway to β-carotene under light regulation. (janisch2023geneticunderpinningsof media 296b2fee, janisch2023geneticunderpinningsof media 6e3589e1, janisch2023geneticunderpinningsof media b3277b04)

#### C. Discovery of novel monocyclic carotenoids and gene sets in marine Bacteroidota (2024)
- In *Algoriphagus* sp. oki45, chemical analysis identified **flexixanthin** and a novel **2-hydroxyflexixanthin**, and genome comparison predicted **eight carotenoid genes** (crtE, crtB, crtI, cruF, crtD, crtYcd, crtW, crtZ) plus a **crtG homolog** likely involved in 2-hydroxylation. This provides a tractable taxon-specific branch of orange pigmentation beyond the common staphyloxanthin/β-carotene narratives. (takatani2024identificationofa pages 1-2)

#### D. Canonical crt gene→product mapping consolidated in 2023 reviews
- A 2023 review explicitly maps canonical gene sets to products (e.g., β-carotene: crtE/crtY/crtI/crtB; zeaxanthin: crtE/crtB/crtI/crtY/crtZ; astaxanthin: crtW/crtZ; canthaxanthin: crtE/crtY/crtI/crtB/crtW), supporting node reuse across taxa and enabling consistent curation of gene→product edges. (agarwal2023bacterialpigmentsand pages 6-7)

### Current applications and real-world implementations
1. **Media/formulation-driven pigment enhancement (laboratory and potential scale-up)**
   - Beetroot and carrot agar formulations increased *S. aureus* pigment signal and shifted visible and spectral characteristics, demonstrating a practical route to modulate pigment yield and shade in culture. While this is not necessarily industrially optimized, it is directly relevant for phenotype assay design and for “experimental factor” nodes in TraitMech. (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11)

2. **Microbial and yeast fermentation to produce orange carotenoids**
   - A 2024 review of **Rhodotorula** fermentation highlights bioreactor considerations (pH, temperature, aeration, agitation) and use of low-cost substrates; it reports multiple quantitative yields across strains/media and notes that β-carotene can comprise up to **70% of total carotenoids** in Rhodotorula. (ochoavinals2024currentadvancesin pages 2-5, ochoavinals2024currentadvancesin pages 1-2)
   - A dissertation (2024 DOI record) demonstrates an applied biorefinery approach using sugarcane bagasse hydrolysate to produce up to **117.52 mg/L total carotenoids** (with supplements) and **128.43 mg/L** in synthetic glucose medium at 72 h, linking orange pigmentation to process optimization and downstream antioxidant/antimicrobial assays. (ruizUnknownyearproduçãodecarotenóides pages 9-13)

3. **Metabolic engineering to increase carotenoid titers**
   - In Deinococcus-focused 2024 review material, pathway engineering strategies (overexpression of precursor and committed-step enzymes such as **dxs** and **crtB**, gene deletions to redirect flux) are summarized as routes to higher production of carotenoids like lycopene and deinoxanthin, supporting an “engineering intervention” layer in causal graphs when relevant. (wang2024insightsintothe pages 6-8)

### Expert opinions and authoritative analysis (as represented by high-citation reviews)
- Reviews emphasize that microbial pigments (including orange carotenoids) are valuable as **biodegradable, non-toxic substitutes** for synthetic colorants, with broad applications across **food, cosmetics, textiles, and pharmaceuticals**, and highlight metabolic engineering and process optimization as major near-term levers for scalability. (agarwal2023bacterialpigmentsand pages 6-7)
- A Rhodotorula-focused review frames carotenoid accumulation as a **secondary-metabolite stress response**, modulated by pH, light, temperature, oxygen, and metal ions, reinforcing a causal-graph design in which environmental stressors regulate biosynthetic output. (ochoavinals2024currentadvancesin pages 1-2)

### Relevant statistics and data (recent)
- **Staphylococcal pigment modulation by media** (2024): A460nm pigment signal increased from 0.13 (nutrient agar) to 0.46 (beetroot agar) (~3.5×), with incubation time correlation r = 0.93 (p < 0.01). (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11)
- **Yeast carotenoid production** (2024): Examples reported include 2.59 mg/L total carotenoids in one Rhodotorula strain/condition and strain-specific cellular carotenoid contents (µg/g to mg/g ranges) across diverse substrates/conditions. (ochoavinals2024currentadvancesin pages 2-5)
- **Biorefinery-oriented production** (DOI record 2024): up to 117.52 mg/L carotenoids from sugarcane bagasse hydrolysate with supplementation after 72 h; 128.43 mg/L in synthetic glucose medium after 72 h. (ruizUnknownyearproduçãodecarotenóides pages 9-13)
- **Market context (review-reported)**: carotenoid market growth estimates and the prominence of β-carotene fractions in yeast carotenoids (up to 70%). (ochoavinals2024currentadvancesin pages 1-2)

---

## Curation-ready artifacts
The following tables are designed to be directly useful for populating `data/traits/morphology/orange_pigmented.yaml`.

| Node label | Node type | Brief role in orange pigmentation | Suggested grounding CURIE(s) if known (or 'label-only') | Key supporting citation ids |
|---|---|---|---|---|
| orange pigmented | phenotype | Visible orange colony/cell coloration; often reflects carotenoid accumulation rather than non-pigment assay artifacts | METPO:1003026 | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 13-14, takatani2024identificationofa pages 1-2) |
| carotenoid accumulation | phenotype | High-level mechanistic basis for many orange microbial phenotypes across bacteria, archaea, and yeasts | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, takatani2024identificationofa pages 1-2, ochoavinals2024currentadvancesin pages 1-2) |
| carotenoid biosynthetic process | pathway | Core pathway generating colored isoprenoid pigments from IPP/DMAPP via GGPP and downstream desaturation/cyclization steps | GO:0016117 | (janisch2023geneticunderpinningsof pages 5-8, agarwal2023bacterialpigmentsand pages 6-7, stra2023carotenoidmetabolismnew pages 1-2) |
| C30 carotenoid biosynthesis | pathway | Produces orange/golden C30 pigments such as diaponeurosporene and staphyloxanthin in Firmicutes/staphylococci | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, lebeer2024distributionofc30 pages 5-7) |
| staphyloxanthin biosynthesis | pathway | Specific S. aureus carotenoid pathway responsible for golden yellow-orange pigmentation | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, sosafajardo2024genomicexplorationof pages 16-17, nirmala2024enhancingstaphyloxanthinsynthesis pages 13-14) |
| C40 carotenoid biosynthesis | pathway | Canonical bacterial/yeast route yielding β-carotene and related orange pigments | label-only | (janisch2023geneticunderpinningsof pages 5-8, agarwal2023bacterialpigmentsand pages 6-7, stra2023carotenoidmetabolismnew pages 1-2) |
| flexixanthin biosynthesis | pathway | Monocyclic carotenoid pathway linked to orange-to-red pigmentation in Algoriphagus | label-only | (takatani2024identificationofa pages 1-2) |
| mevalonate pathway | pathway | Supplies isoprenoid precursors for carotenoid synthesis in staphylococci and yeasts | KEGG:map00900 | (sosafajardo2024genomicexplorationof pages 16-17, ochoavinals2024currentadvancesin pages 2-5, ruizUnknownyearproduçãodecarotenóides pages 41-46) |
| methylerythritol phosphate pathway | pathway | Alternative isoprenoid precursor pathway used in many bacteria for carotenoid production engineering | KEGG:map00908 | (agarwal2023bacterialpigmentsand pages 6-7) |
| crtOPQMN operon | gene/protein | Staphyloxanthin biosynthetic operon encoding the core C30 pathway in S. aureus | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2) |
| crtE | gene/protein | Geranylgeranyl diphosphate synthase feeding C40 carotenoid biosynthesis | KEGG:K02291 | (janisch2023geneticunderpinningsof pages 5-8, agarwal2023bacterialpigmentsand pages 6-7, takatani2024identificationofa pages 1-2) |
| crtB | gene/protein | Phytoene synthase; early committed step in C40 carotenoid formation | KEGG:K02291 or label-only | (wang2024insightsintothe pages 6-8, takatani2024identificationofa pages 1-2) |
| crtI | gene/protein | Phytoene desaturase/dehydrogenase forming downstream colored carotenoid intermediates | KEGG:K10027 | (janisch2023geneticunderpinningsof pages 5-8, wang2024insightsintothe pages 6-8, nagar2024genomicinsightson pages 5-6) |
| crtY | gene/protein | Lycopene β-cyclase converting lycopene toward β-carotene | KEGG:K06443 | (agarwal2023bacterialpigmentsand pages 6-7, stra2023carotenoidmetabolismnew pages 1-2) |
| crtYc/crtYd | gene/protein | Heterodimeric lycopene cyclase used in some bacteria such as Mycobacterium kansasii | label-only | (janisch2023geneticunderpinningsof pages 5-8, janisch2023geneticunderpinningsof media 296b2fee) |
| crtZ | gene/protein | β-carotene hydroxylase producing zeaxanthin and related oxygenated carotenoids | KEGG:K09836 | (agarwal2023bacterialpigmentsand pages 6-7, stra2023carotenoidmetabolismnew pages 1-2) |
| crtW | gene/protein | Ketolase producing orange/red ketocarotenoids such as canthaxanthin/astaxanthin | KEGG:K09837 | (agarwal2023bacterialpigmentsand pages 6-7, takatani2024identificationofa pages 1-2, stra2023carotenoidmetabolismnew pages 1-2) |
| crtO | gene/protein | β-carotene ketolase linked to ketocarotenoid formation; part of staphyloxanthin operon naming and Deinococcus engineering | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, wang2024insightsintothe pages 6-8) |
| crtM | gene/protein | Dehydrosqualene synthase; first dedicated enzyme in C30 staphyloxanthin/diaponeurosporene biosynthesis | KEGG:K06045 | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, lebeer2024distributionofc30 pages 5-7, nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11) |
| crtN | gene/protein | Dehydrosqualene desaturase generating diaponeurosporene-family carotenoids | KEGG:K13789 | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, lebeer2024distributionofc30 pages 5-7) |
| crtR | gene/protein | Transcriptional regulator required for normal light-responsive carotenoid pigmentation in M. kansasii | label-only | (janisch2023geneticunderpinningsof pages 5-8) |
| dxs | gene/protein | Rate-limiting precursor-supply enzyme whose overexpression boosts carotenoid titers | KEGG:K01662 | (wang2024insightsintothe pages 6-8, agarwal2023bacterialpigmentsand pages 6-7) |
| crtLm | gene/protein | Lycopene cyclase in Deinococcus; deletion redirects flux to lycopene | label-only | (wang2024insightsintothe pages 6-8) |
| cruF | gene/protein | Carotenoid hydratase/membrane-associated biosynthetic factor in Deinococcus, Algoriphagus, and haloarchaea | label-only | (wang2024insightsintothe pages 11-11, takatani2024identificationofa pages 1-2, nagar2024genomicinsightson pages 5-6) |
| crtD | gene/protein | Carotenoid desaturase involved in downstream modification of carotenoid backbones | label-only | (wang2024insightsintothe pages 6-8, takatani2024identificationofa pages 1-2, nagar2024genomicinsightson pages 5-6) |
| crtG | gene/protein | Putative 2,2′-β-hydroxylase predicted to convert flexixanthin to 2-hydroxyflexixanthin | label-only | (takatani2024identificationofa pages 1-2) |
| idsA1 | gene/protein | Archaeal GGPP synthase analogue supporting carotenoid/bacterioruberin biosynthesis | label-only | (nagar2024genomicinsightson pages 5-6) |
| CrtYB | gene/protein | Fungal bifunctional phytoene synthase/lycopene cyclase supporting yeast orange carotenoids | label-only | (ochoavinals2024currentadvancesin pages 2-5, hoondee2024comparativegenomicanalysis pages 1-2) |
| CrtS | gene/protein | Fungal astaxanthin synthase in Rhodotorula astaxanthin-producing strains | label-only | (hoondee2024comparativegenomicanalysis pages 1-2) |
| CrtR (fungal) | gene/protein | Fungal carotenoid-pathway reductase/regulator notation reported with astaxanthin genes | label-only | (hoondee2024comparativegenomicanalysis pages 1-2) |
| geranylgeranyl diphosphate (GGPP) | metabolite | Universal C40 carotenoid precursor produced by CrtE/IdsA1-like enzymes | CHEBI:58057 | (janisch2023geneticunderpinningsof pages 5-8, nagar2024genomicinsightson pages 5-6, stra2023carotenoidmetabolismnew pages 1-2) |
| farnesyl diphosphate (FPP) | metabolite | C30 carotenoid precursor feeding CrtM-dependent diaponeurosporene/staphyloxanthin synthesis | CHEBI:66913 | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, lebeer2024distributionofc30 pages 5-7, sosafajardo2024genomicexplorationof pages 16-17) |
| phytoene | metabolite | Colorless early carotenoid intermediate upstream of desaturation | CHEBI:26171 | (wang2024insightsintothe pages 6-8, nagar2024genomicinsightson pages 5-6) |
| lycopene | metabolite | Red carotenoid intermediate; accumulation marks a boundary case shifting phenotype toward red rather than orange | CHEBI:15948 | (janisch2023geneticunderpinningsof pages 5-8, wang2024insightsintothe pages 6-8, stra2023carotenoidmetabolismnew pages 1-2) |
| β-carotene | metabolite | Common orange carotenoid end product or branch intermediate in many microbes | CHEBI:17579 | (janisch2023geneticunderpinningsof pages 5-8, agarwal2023bacterialpigmentsand pages 6-7, stra2023carotenoidmetabolismnew pages 1-2) |
| zeaxanthin | metabolite | Oxygenated carotenoid that can contribute yellow-orange coloration | CHEBI:27325 | (agarwal2023bacterialpigmentsand pages 6-7, stra2023carotenoidmetabolismnew pages 1-2) |
| canthaxanthin | metabolite | Orange-red ketocarotenoid formed by ketolase activity | CHEBI:28172 | (wang2024insightsintothe pages 6-8, stra2023carotenoidmetabolismnew pages 1-2) |
| astaxanthin | metabolite | Orange-red ketocarotenoid and important industrial product in engineered microbes/yeasts | CHEBI:26949 | (agarwal2023bacterialpigmentsand pages 6-7, hoondee2024comparativegenomicanalysis pages 1-2) |
| 4,4′-diaponeurosporene | metabolite | Orange C30 carotenoid product of crtMN pathway | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, lebeer2024distributionofc30 pages 5-7) |
| staphyloxanthin | metabolite | Golden yellow-orange membrane carotenoid producing characteristic S. aureus pigmentation | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, sosafajardo2024genomicexplorationof pages 16-17, nirmala2024enhancingstaphyloxanthinsynthesis pages 13-14) |
| flexixanthin | metabolite | Monocyclic carotenoid contributing to orange/red pigmentation in Algoriphagus | label-only | (takatani2024identificationofa pages 1-2) |
| 2-hydroxyflexixanthin | metabolite | Newly described monocyclic carotenoid contributing to orange/red pigmentation in Algoriphagus | label-only | (takatani2024identificationofa pages 1-2) |
| deinoxanthin | metabolite | Deinococcus carotenoid associated with antioxidant and radiation-protective functions; often orange-red | label-only | (wang2024insightsintothe pages 11-11, wang2024insightsintothe pages 6-8) |
| bacterioruberin | metabolite | Archaeal C50 carotenoid giving red-orange hues in haloarchaea | label-only | (nagar2024genomicinsightson pages 5-6, wang2024insightsintothe pages 11-11) |
| torulene | metabolite | Major orange-red yeast carotenoid in Rhodotorula/Rhodosporidium | label-only | (ochoavinals2024currentadvancesin pages 2-5) |
| torularhodin | metabolite | Oxidized yeast carotenoid contributing orange-red coloration | label-only | (ochoavinals2024currentadvancesin pages 2-5) |
| light exposure | environment | Induces photochromogenic carotenoid gene expression and orange/yellow pigmentation in some taxa | ENVO:01000324 or label-only | (janisch2023geneticunderpinningsof pages 5-8, janisch2023geneticunderpinningsof media 296b2fee) |
| oxidative stress / ROS | environment | Stressor that stimulates or explains carotenoid accumulation and protective function | GO:0006979 or label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 13-14, hoondee2024comparativegenomicanalysis pages 1-2) |
| UV radiation | environment | Selective pressure/stressor against which carotenoids confer protection; associated with carotenoid-positive strains | ENVO:01001001 or label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 13-14, wang2024insightsintothe pages 11-11, lebeer2024distributionofc30 pages 5-7) |
| gamma irradiation | environment | Extreme stress context highlighting carotenoid protective roles in Deinococcus | label-only | (wang2024insightsintothe pages 11-11) |
| low temperature / cold stress | environment | Reported inducer of staphylococcal carotenoid production in a taxon-specific context | label-only | (mushomba2023inducedantibioticresistance pages 65-71) |
| oxygen availability / microaerophily | environment | Environmental factor affecting carotenoid-related stress physiology and expression in some taxa | label-only | (hoondee2024comparativegenomicanalysis pages 1-2, wang2024insightsintothe pages 11-11) |
| salts / salinity | environment | Stress variable modulating yeast carotenoid accumulation and central to halophilic archaeal pigmentation ecology | ENVO:01001700 or label-only | (ochoavinals2024currentadvancesin pages 1-2, nagar2024genomicinsightson pages 5-6) |
| metal ions / sodium selenite | environment | Stressor/supplement that can increase yeast carotenoid production under defined conditions | CHEBI:32149 | (ochoavinals2024currentadvancesin pages 1-2, hoondee2024comparativegenomicanalysis pages 1-2) |
| beetroot agar | assay | Experimental medium that increased S. aureus pigment signal and shifted visible hue/spectral profile | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11) |
| carrot agar | assay | Experimental medium enhancing orange pigment production in S. aureus | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11) |
| milk agar | assay | Historical/experimental medium supporting stronger staphyloxanthin signal than nutrient agar | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11) |
| incubation time | assay | Positive assay variable correlated with measured pigment accumulation | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11) |
| UV-Vis absorbance at 460 nm | assay | Quantitative readout used to estimate orange carotenoid abundance in extracts | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11) |
| paper chromatography orange/golden bands | assay | Separation-based evidence that multiple yellow-orange pigment species are present | label-only | (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11) |
| photochromogenic pigmentation | phenotype | Light-dependent appearance of yellow/orange carotenoid pigment; key boundary case for trait scoring | label-only | (janisch2023geneticunderpinningsof pages 5-8, janisch2023geneticunderpinningsof media 296b2fee) |
| red-pigmented phenotype | phenotype | Nearby trait often caused by lycopene accumulation; should be separated from orange-pigmented curation when possible | label-only | (janisch2023geneticunderpinningsof pages 5-8, takatani2024identificationofa pages 1-2) |


*Table: This table lists candidate nodes for curating the microbial orange-pigmented causal graph, spanning phenotypes, pathways, genes, metabolites, environmental modulators, and assays. It is useful for assembling a TraitMech YAML because it pairs each node with a concise mechanistic role, tentative grounding, and supporting evidence contexts.*

| Edge (triple) | Node types | Example taxa | Suggested ontology grounding (CURIEs where known) | Evidence (citation id) | Supporting snippet (short) | Notes/uncertainty |
|---|---|---|---|---|---|---|
| geranylgeranyl diphosphate synthase/CrtE **produces** geranylgeranyl diphosphate (GGPP) | enzyme → metabolite | *Mycobacterium kansasii* | enzyme: EC candidate for GGPP synthase; metabolite: GGPP (label-only if no CURIE assigned) | (janisch2023geneticunderpinningsof pages 5-8) | “CrtE is predicted to make geranylgeranyl diphosphate (GGPP)” | Strong for canonical C40 carotenoid pathway; taxon example from *M. kansasii*. |
| phytoene dehydrogenase/CrtI **participates_in** carotenoid biosynthesis from phytoene to downstream carotenoids | enzyme → biological process/pathway | *Mycobacterium kansasii*; *Deinococcus* spp. | enzyme: EC candidate for phytoene desaturase; process: carotenoid biosynthetic process (GO candidate) | (janisch2023geneticunderpinningsof pages 5-8, wang2024insightsintothe pages 6-8) | “crtI encodes phytoene dehydrogenase (desaturase)”; “Phytoene desaturase (crtI) converts phytoene to downstream carotenoids” | Strong pathway edge; exact product depends on taxon/pathway branch. |
| crtEIBYcYd carotenoid gene cluster **enables** beta-carotene biosynthesis | gene cluster → metabolite/pathway outcome | *Mycobacterium kansasii* | genes: crtE/crtI/crtB/crtYc/crtYd (label-only); metabolite: beta-carotene (CHEBI candidate) | (janisch2023geneticunderpinningsof pages 5-8, janisch2023geneticunderpinningsof media 296b2fee) | “crt gene cluster (noted as crtEIBYcYd)… pathway depiction shows β-carotene as the major final product” | Strong but cluster-level; suitable as a higher-level node if individual gene curation is incomplete. |
| lycopene cyclase/CrtY **converts** lycopene to beta-carotene | enzyme → metabolite conversion | diverse bacteria | enzyme: crtY / lycopene beta-cyclase; substrate/product: lycopene, beta-carotene (CHEBI candidates) | (agarwal2023bacterialpigmentsand pages 6-7, stra2023carotenoidmetabolismnew pages 1-2) | “crtY… encode lycopene β-cyclase”; “lycopene is converted to beta-carotene by ring-forming lycopene cyclases — in bacteria the enzyme is crtY” | Strong general edge; broad microbial applicability. |
| crtZ/beta-carotene hydroxylase **converts** beta-carotene to zeaxanthin | enzyme → metabolite conversion | diverse bacteria | enzyme: crtZ; metabolites: beta-carotene, zeaxanthin (CHEBI candidates) | (agarwal2023bacterialpigmentsand pages 6-7, stra2023carotenoidmetabolismnew pages 1-2) | “crtZ encode… a β-carotene hydroxylase”; “conversion of beta-carotene to zeaxanthin by crtZ” | Strong general edge; supports orange/yellow pigmentation branches. |
| crtW/ketolase **contributes_to** ketocarotenoid biosynthesis (e.g., canthaxanthin/astaxanthin) | enzyme → pathway/product class | diverse bacteria; engineered hosts | enzyme: crtW; metabolites: canthaxanthin, astaxanthin (CHEBI candidates) | (agarwal2023bacterialpigmentsand pages 6-7, stra2023carotenoidmetabolismnew pages 1-2) | “crtW and crtZ for astaxanthin”; “ketolation… by ketolases such as crtW” | Strong for ketocarotenoid branch; pigment hue can range orange to red. |
| CrtO **converts** beta-carotene to ketocarotenoids such as canthaxanthin | enzyme → metabolite class | *Deinococcus* engineering context | enzyme: crtO (label-only/UniProt candidate if strain-specific); product: canthaxanthin (CHEBI candidate) | (wang2024insightsintothe pages 6-8) | “CrtO converts β-carotene into ketocarotenoids such as canthaxanthin” | Strong but cited from heterologous expression/engineering context. |
| crtM (dehydrosqualene synthase) **produces** dehydrosqualene from farnesyl diphosphate-derived precursors | enzyme → metabolite | *Staphylococcus aureus*; engineered *Bacillus subtilis* | enzyme: crtM; precursor pathway metabolite: farnesyl diphosphate/FPP (CHEBI candidate) | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2) | “proceeds via dehydrosqualene synthase (CrtM)” | Strong for C30 staphyloxanthin branch; exact stoichiometric substrate wording abbreviated in source excerpt. |
| crtN (dehydrosqualene desaturase) **converts** dehydrosqualene to diaponeurosporene intermediates | enzyme → metabolite conversion | *Staphylococcus aureus*; Lactobacillaceae | enzyme: crtN; product: 4,4’-diaponeurosporene (label-only/CHEBI candidate) | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, lebeer2024distributionofc30 pages 5-7) | “dehydrosqualene desaturase… to form diaponeurosporene”; “crtN, encoding… 4,4’-diapophytoene desaturase” | Strong for C30 orange/golden pigments. |
| crtOPQMN operon **enables** staphyloxanthin biosynthesis | operon → metabolite | *Staphylococcus aureus* | genes: crtO/crtP/crtQ/crtM/crtN (label-only); metabolite: staphyloxanthin (label-only/CHEBI candidate unclear) | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2) | “Biosynthesis is encoded by the crtOPQMN operon” | Strong operon-level edge for *S. aureus* golden/orange phenotype. |
| staphyloxanthin biosynthesis **causes** golden yellow-orange/orange pigmentation | pathway/metabolite → phenotype | *Staphylococcus aureus*; staphylococci | phenotype: METPO:1003026; metabolite: staphyloxanthin | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, sosafajardo2024genomicexplorationof pages 16-17, nirmala2024enhancingstaphyloxanthinsynthesis pages 13-14) | “natural golden pigment”; “yields orange pigmentation”; “rich golden yellow-orange pigment” | Strong phenotype-defining edge; note color descriptors vary from golden to orange. |
| flexixanthin and 2-hydroxyflexixanthin accumulation **causes** orange-to-red pigmentation | metabolites → phenotype | *Algoriphagus* sp. oki45 | metabolites: flexixanthin, 2-hydroxyflexixanthin (label-only); phenotype: METPO:1003026 or nearby red/orange trait | (takatani2024identificationofa pages 1-2) | “identified monocyclic carotenoids flexixanthin and a novel 2-hydroxyflexixanthin responsible for orange/red pigmentation” | Good evidence, but boundary with red-pigmented trait should be curated carefully. |
| crtG homolog (2,2′-beta-hydroxylase) **converts** flexixanthin to 2-hydroxyflexixanthin | enzyme → metabolite conversion | *Algoriphagus* sp. oki45 | enzyme: crtG homolog; product: 2-hydroxyflexixanthin | (takatani2024identificationofa pages 1-2) | “crtG homolog… likely catalyzing 2-hydroxylation to yield 2-hydroxyflexixanthin” | Plausible and source-backed, but phrased as prediction/likely role; mark uncertain. |
| cruF/crtD/crtYcd/crtW/crtZ carotenoid genes **contribute_to** flexixanthin biosynthesis | genes/enzymes → pathway | *Algoriphagus* sp. oki45 | genes: cruF, crtD, crtYcd, crtW, crtZ (label-only) | (takatani2024identificationofa pages 1-2) | “eight genes (crtE, crtB, crtI, cruF, crtD, crtYcd, crtW, crtZ) implicated in flexixanthin biosynthesis” | Cluster-level prediction from genome comparison; weaker than direct biochemical validation. |
| light exposure **upregulates** carotenoid biosynthesis genes / photochromogenic pigmentation | environmental factor → gene expression/phenotype | *Mycobacterium kansasii* | environment: light (ENVO candidate); process: carotenoid biosynthetic process | (janisch2023geneticunderpinningsof pages 5-8, janisch2023geneticunderpinningsof media 296b2fee) | “some genes… were co-regulated by light”; WT is “white in dark, yellow in light” and mutant WO is “white in dark, orange in light” | Strong for photochromogenic taxa; should be marked taxon-specific, not universal for all orange pigmentation. |
| crtR regulator **positively_regulates** normal yellow carotenoid pigmentation | regulator → phenotype/pathway | *Mycobacterium kansasii* | gene/regulator: crtR (label-only) | (janisch2023geneticunderpinningsof pages 5-8) | “a transcriptional regulator crtR is required for normal pigmentation” | Strong for *M. kansasii*; regulatory logic may not generalize across taxa. |
| lycopene accumulation **causes** red colony phenotype | metabolite → phenotype | *Mycobacterium kansasii* mutants | metabolite: lycopene (CHEBI candidate); phenotype: red pigmented (nearby trait) | (janisch2023geneticunderpinningsof pages 5-8) | “abnormal accumulation of the red pathway intermediate lycopene” | Useful boundary-case edge: supports distinction between orange/yellow carotenoid states and red-pigmented states. |
| deletion of crtLm (lycopene cyclase) **increases** lycopene accumulation | genetic perturbation → metabolite | *Deinococcus* engineering context | gene: crtLm (label-only); metabolite: lycopene | (wang2024insightsintothe pages 6-8) | “Deletion of crtLm… redirects flow to lycopene” | Engineering-specific; supports pathway direction but not directly orange phenotype. |
| overexpression of dxs and crtB **increases** lycopene/deinoxanthin production | genes → metabolite abundance | *Deinococcus* spp. | genes: dxs, crtB; metabolites: lycopene, deinoxanthin | (wang2024insightsintothe pages 6-8) | “overexpression of crtB and dxs… raised lycopene and deinoxanthin titers substantially” | Strong for production engineering; quantitative values not provided in excerpt. |
| carotenoid accumulation **protects_against** oxidative stress / reactive oxygen species | metabolite class → stress tolerance | *Staphylococcus aureus*; *Deinococcus*; Rhodotorula | process: oxidative stress response (GO candidate); chemical class: carotenoids | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, sosafajardo2024genomicexplorationof pages 16-17, wang2024insightsintothe pages 11-11) | “acts as an antioxidant protecting against hydrogen peroxide and hydroxyl radicals”; “deactivating reactive oxygen species” | Strong, broad functional edge across taxa. |
| carotenoid accumulation **protects_against** UV or radiation stress | metabolite class → stress tolerance | *Staphylococcus aureus*; *Deinococcus* | environment/stressor: UV radiation, gamma radiation (ENVO/label-only); process: response to radiation | (nirmala2024enhancingstaphyloxanthinsynthesis pages 13-14, wang2024insightsintothe pages 11-11) | “ROS from radiation”; “contributions to extreme radiation resistance” | Strong function edge, but exact mechanism may vary by pigment and taxon. |
| carotenoid accumulation **is_associated_with** increased oxidative and UV stress resistance | metabolite/pathway → phenotype/fitness | Lactobacillaceae | pathway: C30 carotenoid biosynthesis via crtMN | (lebeer2024distributionofc30 pages 5-7) | “C30 carotenoid-producing strains were more resistant to oxidative and UV-stress” | Association from comparative study; likely suitable but note not direct biochemical causation in every strain. |
| crtMN presence **enables** C30 carotenoid biosynthesis phenotype | genes → phenotype/pathway | Lactobacillaceae | genes: crtM, crtN | (lebeer2024distributionofc30 pages 5-7) | “These genes encode the key enzymes that transform two farnesyl pyrophosphate molecules into the C30 carotenoid 4,4’-diaponeurosporene” | Strong gene→pathway edge; color output may vary from yellow to orange depending on downstream chemistry. |
| media composition (beetroot agar) **increases** staphyloxanthin accumulation | experimental factor → metabolite abundance | *Staphylococcus aureus* | environment/assay factor: beetroot agar (label-only); metabolite: staphyloxanthin | (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11) | “beetroot agar 0.46” vs “nutrient agar 0.13” at 460 nm | Strong assay/media effect but should be marked experimental-factor-specific, not intrinsic biology. |
| incubation time **positively_correlates_with** staphyloxanthin concentration | experimental factor → metabolite abundance | *Staphylococcus aureus* | assay factor: incubation time | (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11) | “strong positive correlation… (r = 0.93, p < 0.01)” | Good quantitative assay edge; not a constitutive causal trait mechanism. |
| sodium selenite supplementation **increases** total carotenoids | chemical/environmental factor → metabolite abundance | *Rhodotorula glutinis* | chemical: sodium selenite (CHEBI candidate); metabolite class: carotenoids | (hoondee2024comparativegenomicanalysis pages 1-2) | “Adding 1 mM and 3 mM sodium selenite… increased total and cellular carotenoids” | Useful for environmental modulation, but fungal/yeast and concentration-specific. |
| active oxidative metabolism **increases** carotenoid production | physiological process → metabolite abundance | *Rhodotorula mucilaginosa* | process: oxidative metabolism / ROS generation | (hoondee2024comparativegenomicanalysis pages 1-2) | “active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species” | Good stress-response edge, but fungal and context-specific. |
| orange pigmented phenotype **has_material_basis_in** carotenoid accumulation | phenotype → metabolite class | diverse bacteria, yeasts, protists | phenotype: METPO:1003026; chemical class: carotenoids | (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 13-14, takatani2024identificationofa pages 1-2, ochoavinals2024currentadvancesin pages 1-2) | “orange carotenoid”; “golden yellow-orange pigment”; “orange/red pigmentation” | High-level summary edge suitable for TraitMech root graph, though pigment chemistry is taxon-diverse. |


*Table: This table summarizes candidate subject–predicate–object edges for curating the microbial trait orange pigmented, centered on carotenoid and staphyloxanthin biosynthesis, regulation, and function. It highlights which edges are broadly supported versus taxon-specific or assay-specific.*

---

## Minimal visual evidence (figure-derived support)
The *Mycobacterium kansasii* study provides figures showing (i) pigmentation phenotypes (including orange under light), (ii) CRT gene cluster organization, and (iii) a proposed pathway to β-carotene; these can be used to support photochromogenic and pathway-structure edges. (janisch2023geneticunderpinningsof media 296b2fee, janisch2023geneticunderpinningsof media 6e3589e1, janisch2023geneticunderpinningsof media b3277b04)

---

## Warnings / claims not yet ready for robust TraitMech curation
1. **Predicted enzyme roles without direct biochemical validation**
   - The role of *Algoriphagus* **crtG homolog** in 2-hydroxylation to form 2-hydroxyflexixanthin is explicitly presented as “likely/suggesting” based on genome comparison; curate as **uncertain** unless corroborated by knockout/heterologous expression. (takatani2024identificationofa pages 1-2)

2. **Assay/media-dependent effects**
   - Media-driven increases in pigment signal (beetroot/carrot/milk agar) are strong experimentally but should be encoded as **experimental-factor edges** rather than organism-intrinsic regulatory mechanisms. (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11)

3. **Taxon-specific regulation**
   - Light-dependent pigmentation (photochromogenicity) is central in *M. kansasii* but should not be generalized to all orange-pigmented microbes. (janisch2023geneticunderpinningsof pages 5-8, janisch2023geneticunderpinningsof media 296b2fee)

4. **Orange vs red phenotype conflation**
   - Lycopene-associated red phenotypes (RR mutants) provide a concrete example of a nearby trait; ensure orange-pigmented curation does not inadvertently include red-pigmented nodes unless explicitly intended. (janisch2023geneticunderpinningsof pages 5-8)

---

## DOI-first bibliography (with URLs and publication dates where available)
- Janisch N, Levendosky K, Budell WC, Quadri LEN. **Genetic Underpinnings of Carotenogenesis and Light-Induced Transcriptome Remodeling in the Opportunistic Pathogen Mycobacterium kansasii**. *Pathogens*. 2023-01. https://doi.org/10.3390/pathogens12010086 (janisch2023geneticunderpinningsof pages 5-8)
- Agarwal H, Bajpai S, Mishra A, et al. **Bacterial Pigments and Their Multifaceted Roles in Contemporary Biotechnology and Pharmacological Applications**. *Microorganisms*. 2023-02. https://doi.org/10.3390/microorganisms11030614 (agarwal2023bacterialpigmentsand pages 6-7)
- Stra A, Almarwaey LO, Alagoz Y, Moreno JC, Al-Babili S. **Carotenoid metabolism: New insights and synthetic approaches**. *Frontiers in Plant Science*. 2023-01. https://doi.org/10.3389/fpls.2022.1072061 (stra2023carotenoidmetabolismnew pages 1-2)
- Nirmala B, Omar BJ, Omar Sr B. **Enhancing Staphyloxanthin Synthesis in Staphylococcus aureus Using Innovative Agar Media Formulations**. *Cureus*. 2024-05. https://doi.org/10.7759/cureus.59892 (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2, nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11)
- Sosa-Fajardo A, Díaz-Muñoz C, Van der Veken D, et al. **Genomic exploration of the fermented meat isolate Staphylococcus shinii IMDO-S216 with a focus on competitiveness-enhancing secondary metabolites**. *BMC Genomics*. 2024-06. https://doi.org/10.1186/s12864-024-10490-0 (sosafajardo2024genomicexplorationof pages 16-17)
- Takatani N, Maoka T, Sawabe T, Beppu F, Hosokawa M. **Identification of a novel monocyclic carotenoid and prediction of its biosynthetic genes in Algoriphagus sp. oki45**. *Applied Microbiology and Biotechnology*. 2024-01. https://doi.org/10.1007/s00253-023-12995-2 (takatani2024identificationofa pages 1-2)
- Wang Y, Liu J, Yi Y, et al. **Insights into the synthesis, engineering, and functions of microbial pigments in Deinococcus bacteria**. *Frontiers in Microbiology*. 2024-07. https://doi.org/10.3389/fmicb.2024.1447785 (wang2024insightsintothe pages 11-11, wang2024insightsintothe pages 6-8)
- Ochoa-Viñals N, Alonso-Estrada D, Pacios-Michelena S, et al. **Current Advances in Carotenoid Production by Rhodotorula sp.** *Fermentation*. 2024-03. https://doi.org/10.3390/fermentation10040190 (ochoavinals2024currentadvancesin pages 2-5, ochoavinals2024currentadvancesin pages 1-2)
- Hoondee P, Phuengjayaem S, Kingkaew E, et al. **Comparative genomic analysis and optimization of astaxanthin production of Rhodotorula paludigena TL35-5 and Rhodotorula sampaioana PL61-2**. *PLOS ONE*. 2024-07. https://doi.org/10.1371/journal.pone.0304699 (hoondee2024comparativegenomicanalysis pages 1-2)
- Lebeer S, Legein M, Eilers T, et al. **Distribution of C30 carotenoid biosynthesis genes suggests habitat adaptation function in insect-adapted and nomadic Lactobacillaceae**. 2024 (preprint/record). https://doi.org/10.21203/rs.3.rs-4637278/v1 (lebeer2024distributionofc30 pages 5-7)
- Ruiz ED. **Produção de carotenóides a partir de bagaço de cana-de-açúcar por Rhodotorula glutinis CCT-2186**. 2024 (DOI record; thesis/dissertation). https://doi.org/10.11606/d.97.2024.tde-12122024-113132 (ruizUnknownyearproduçãodecarotenóides pages 9-13)

---

### Notes toward YAML integration
- Treat **orange pigmented (METPO:1003026)** as the phenotype root; attach pigment accumulation nodes (carotenoids; specific pigments) and connect via taxon-specific biosynthetic gene clusters/operons.
- Include explicit **environmental/assay factor nodes** (light exposure; media composition; incubation time; oxidative stress/ROS) as modulators rather than attributing all variability to genetic regulation.
- Where stable identifiers are missing in evidence (e.g., staphyloxanthin, diaponeurosporene, bacterioruberin, deinoxanthin), keep nodes as **label-only** until a definitive ChEBI/MetaCyc/Rhea mapping is confirmed.


References

1. (nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2): B Nirmala, BJ Omar, and B Omar Sr. Enhancing staphyloxanthin synthesis in staphylococcus aureus using innovative agar media formulations. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.59892, doi:10.7759/cureus.59892. This article has 5 citations.

2. (sosafajardo2024genomicexplorationof pages 16-17): Ana Sosa-Fajardo, Cristian Díaz-Muñoz, David Van der Veken, Inés Pradal, Marko Verce, Stefan Weckx, and Frédéric Leroy. Genomic exploration of the fermented meat isolate staphylococcus shinii imdo-s216 with a focus on competitiveness-enhancing secondary metabolites. BMC Genomics, Jun 2024. URL: https://doi.org/10.1186/s12864-024-10490-0, doi:10.1186/s12864-024-10490-0. This article has 9 citations and is from a peer-reviewed journal.

3. (takatani2024identificationofa pages 1-2): Naoki Takatani, Takashi Maoka, Tomoo Sawabe, Fumiaki Beppu, and Masashi Hosokawa. Identification of a novel monocyclic carotenoid and prediction of its biosynthetic genes in algoriphagus sp. oki45. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12995-2, doi:10.1007/s00253-023-12995-2. This article has 7 citations and is from a domain leading peer-reviewed journal.

4. (janisch2023geneticunderpinningsof pages 5-8): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

5. (janisch2023geneticunderpinningsof media 296b2fee): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

6. (nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11): B Nirmala, BJ Omar, and B Omar Sr. Enhancing staphyloxanthin synthesis in staphylococcus aureus using innovative agar media formulations. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.59892, doi:10.7759/cureus.59892. This article has 5 citations.

7. (stra2023carotenoidmetabolismnew pages 1-2): Alice Stra, Lamyaa O. Almarwaey, Yagiz Alagoz, Juan C. Moreno, and Salim Al-Babili. Carotenoid metabolism: new insights and synthetic approaches. Frontiers in Plant Science, Jan 2023. URL: https://doi.org/10.3389/fpls.2022.1072061, doi:10.3389/fpls.2022.1072061. This article has 110 citations.

8. (janisch2023geneticunderpinningsof media 6e3589e1): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

9. (janisch2023geneticunderpinningsof media b3277b04): Niklas Janisch, Keith Levendosky, William C. Budell, and Luis E. N. Quadri. Genetic underpinnings of carotenogenesis and light-induced transcriptome remodeling in the opportunistic pathogen mycobacterium kansasii. Pathogens, 12:86, Jan 2023. URL: https://doi.org/10.3390/pathogens12010086, doi:10.3390/pathogens12010086. This article has 5 citations.

10. (agarwal2023bacterialpigmentsand pages 6-7): Himani Agarwal, Sneh Bajpai, Arti Mishra, Isha Kohli, Ajit Varma, Mireille Fouillaud, Laurent Dufossé, and Naveen Chandra Joshi. Bacterial pigments and their multifaceted roles in contemporary biotechnology and pharmacological applications. Microorganisms, 11:614, Feb 2023. URL: https://doi.org/10.3390/microorganisms11030614, doi:10.3390/microorganisms11030614. This article has 118 citations.

11. (ochoavinals2024currentadvancesin pages 2-5): Nayra Ochoa-Viñals, Dania Alonso-Estrada, Sandra Pacios-Michelena, Ariel García-Cruz, Rodolfo Ramos-González, Evelyn Faife-Pérez, Lourdes Georgina Michelena-Álvarez, José Luis Martínez-Hernández, and Anna Iliná. Current advances in carotenoid production by rhodotorula sp. Fermentation, 10:190, Mar 2024. URL: https://doi.org/10.3390/fermentation10040190, doi:10.3390/fermentation10040190. This article has 49 citations.

12. (ochoavinals2024currentadvancesin pages 1-2): Nayra Ochoa-Viñals, Dania Alonso-Estrada, Sandra Pacios-Michelena, Ariel García-Cruz, Rodolfo Ramos-González, Evelyn Faife-Pérez, Lourdes Georgina Michelena-Álvarez, José Luis Martínez-Hernández, and Anna Iliná. Current advances in carotenoid production by rhodotorula sp. Fermentation, 10:190, Mar 2024. URL: https://doi.org/10.3390/fermentation10040190, doi:10.3390/fermentation10040190. This article has 49 citations.

13. (ruizUnknownyearproduçãodecarotenóides pages 9-13): Erick Diaz Ruiz. Produção de carotenóides a partir de bagaço de cana-de-açúcar por rhodotorula glutinis cct-2186. ArXiv, Unknown year. URL: https://doi.org/10.11606/d.97.2024.tde-12122024-113132, doi:10.11606/d.97.2024.tde-12122024-113132. This article has 0 citations.

14. (wang2024insightsintothe pages 6-8): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 17 citations and is from a peer-reviewed journal.

15. (nirmala2024enhancingstaphyloxanthinsynthesis pages 13-14): B Nirmala, BJ Omar, and B Omar Sr. Enhancing staphyloxanthin synthesis in staphylococcus aureus using innovative agar media formulations. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.59892, doi:10.7759/cureus.59892. This article has 5 citations.

16. (lebeer2024distributionofc30 pages 5-7): Sarah Lebeer, Marie Legein, Tom Eilers, Jari Temmermans, Jelle Dillen, Ine Vandendriessche, Koen Sandra, Peter Bron, and Stijn Wittouck. Distribution of c30 carotenoid biosynthesis genes suggests habitat adaptation function in insect-adapted and nomadic lactobacillaceae. Unknown journal, Aug 2024. URL: https://doi.org/10.21203/rs.3.rs-4637278/v1, doi:10.21203/rs.3.rs-4637278/v1.

17. (ruizUnknownyearproduçãodecarotenóides pages 41-46): Erick Diaz Ruiz. Produção de carotenóides a partir de bagaço de cana-de-açúcar por rhodotorula glutinis cct-2186. ArXiv, Unknown year. URL: https://doi.org/10.11606/d.97.2024.tde-12122024-113132, doi:10.11606/d.97.2024.tde-12122024-113132. This article has 0 citations.

18. (nagar2024genomicinsightson pages 5-6): DN Nagar, K Mani, and JM Braganca. Genomic insights on carotenoid synthesis by extremely halophilic archaea haloarcula rubripromontorii bs2, haloferax lucentense bbk2 and halogeometricum …. Unknown journal, 2024.

19. (wang2024insightsintothe pages 11-11): Yuxian Wang, Jiayu Liu, Yuanyang Yi, Liying Zhu, Minghui Liu, Zhidong Zhang, Qiong Xie, and Ling Jiang. Insights into the synthesis, engineering, and functions of microbial pigments in deinococcus bacteria. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1447785, doi:10.3389/fmicb.2024.1447785. This article has 17 citations and is from a peer-reviewed journal.

20. (hoondee2024comparativegenomicanalysis pages 1-2): Patcharaporn Hoondee, Sukanya Phuengjayaem, Engkarat Kingkaew, Pornchai Rojsitthisak, Boonchoo Sritularak, Somphob Thompho, Natapol Pornputtapong, Worathat Thitikornpong, and Somboon Tanasupawat. Comparative genomic analysis and optimization of astaxanthin production of rhodotorula paludigena tl35-5 and rhodotorula sampaioana pl61-2. PLOS ONE, 19:e0304699, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0304699, doi:10.1371/journal.pone.0304699. This article has 9 citations and is from a peer-reviewed journal.

21. (mushomba2023inducedantibioticresistance pages 65-71): MM Mushomba. Induced antibiotic resistance and staphyloxanthin as a prospective target for treatment against pathogenic antibiotic-resistant staphylococci. Unknown journal, 2023.