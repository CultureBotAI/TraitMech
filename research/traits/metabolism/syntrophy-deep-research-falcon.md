---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:01:41.629188'
end_time: '2026-06-18T06:18:05.594732'
duration_seconds: 983.97
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Syntrophy
  trait_identifier: METPO:1002006
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: syntrophy
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which the metabolism of one species is thermodynamically
    dependent on the removal of its products by another species.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2166: Interspecies electron transfer is a
    key process (Review supports hydrogen/formate-mediated electron transfer in syntrophic
    communities.)'
  causal_graph_summary: 'syntrophy_interspecies_electron_transfer: 7 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Syntrophy
- **METPO identifier:** METPO:1002006
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which the metabolism of one species is thermodynamically dependent on the removal of its products by another species.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2166: Interspecies electron transfer is a key process (Review supports hydrogen/formate-mediated electron transfer in syntrophic communities.)
- **Existing causal graph summary:** syntrophy_interspecies_electron_transfer: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **Syntrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/syntrophy.yaml`.

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
- **Trait label:** Syntrophy
- **METPO identifier:** METPO:1002006
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which the metabolism of one species is thermodynamically dependent on the removal of its products by another species.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2166: Interspecies electron transfer is a key process (Review supports hydrogen/formate-mediated electron transfer in syntrophic communities.)
- **Existing causal graph summary:** syntrophy_interspecies_electron_transfer: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **Syntrophy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/syntrophy.yaml`.

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


## Microbial Trait Causal Graph Research Report: **Syntrophy** (METPO:1002006)

### Publication window emphasized
This report prioritizes 2023–2024 literature where available and uses earlier high-impact synthesis work only when needed for core definitions/mechanistic framing.

---

## 1) Trait scope (what METPO:1002006 captures)

### Working definition aligned to METPO
**Syntrophy** is a *thermodynamic dependency* phenotype: one organism’s metabolism proceeds only when another organism removes products/electrons sufficiently to make the overall reaction energetically feasible—typically by keeping **H2**/**formate** low or by accepting electrons directly (**DIET**). This operationalization is consistent with current anaerobic digestion (AD) and anoxic-environment frameworks that define syntrophy through **interspecies electron transfer (IET)** modes (H2/formate-mediated MIET vs DIET) and their thermodynamic constraints. For example, a 2023 review states that H2-mediated IET is feasible only at very low hydrogen partial pressure (H2 < 10−4 atm) (su2023areviewon pages 3-4), while a 2023 DIET-focused review notes DIET can “overcome the inhibition of hydrogen pressure and formate concentration” (kong2023enhancedanaerobicdigestion pages 1-2).

### Boundary cases (what should *not* be curated as syntrophy)
* **Generic cross-feeding without thermodynamic dependence**: exchange of metabolites (e.g., acetate used by a methanogen) is not necessarily syntrophy unless the producer’s metabolism is thermodynamically constrained and depends on product removal.
* **Biofilm/aggregation traits alone**: co-aggregation can facilitate syntrophy but does not define it unless tied to thermodynamic/product-removal dependence.
* **Nonmutualistic IET**: electron exchange can occur outside mutual thermodynamic coupling; curate as syntrophy only when evidence supports dependence of one partner’s metabolism on the other.

### Practical assay/observation criteria for curation
Evidence consistent with syntrophy includes: (i) partner-required growth/turnover; (ii) sensitivity to H2/formate accumulation; (iii) signatures of MIET (hydrogenases/formate dehydrogenases, formate transporters) or DIET (conductive pili, multiheme cytochromes, conductive-material dependence); and (iv) reduced hydrogenase/formate dehydrogenase expression in DIET-dominant systems (nozhevnikova2020syntrophyandinterspecies pages 9-11, su2023areviewon pages 3-4).

---

## 2) Key concepts and current mechanistic understanding

### 2.1 Interspecies electron transfer (IET): MIET vs DIET
**MIET** (mediated IET) uses soluble carriers:
* **Interspecies hydrogen transfer (IHT)**: constrained by extremely low H2 partial pressure (H2 < 10−4 atm) in one 2023 review (su2023areviewon pages 3-4).
* **Interspecies formate transfer (IFT)**: often framed as kinetically advantageous because formate can diffuse faster and be present at higher concentrations than H2 (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15, nobu2020catabolismandinteractions pages 8-10).

**DIET** (direct IET) uses conductive biological/abiotic conduits:
* Conductive **pili (e-pili/type IV pili)** and **outer-surface multiheme c-type cytochromes** are repeatedly presented as DIET mediators (nozhevnikova2020syntrophyandinterspecies pages 9-11, zhuang2024electrontransferin pages 3-5).
* Reviews emphasize that DIET can bypass hydrogen/formate limitations (kong2023enhancedanaerobicdigestion pages 1-2) and may increase methane yields and stability in engineered systems (kong2023enhancedanaerobicdigestion pages 1-2).

### 2.2 Energy conservation at the thermodynamic edge
Syntrophic reactions (e.g., propionate/acetate oxidation) operate near energetic limits. Contemporary work in ammonia-stressed reactors highlights expression of **hydrogenases**, **formate dehydrogenases**, and associated maturation/energy-conservation machinery (e.g., HypABCDE; F0F1 ATP synthase subunits) consistent with maintaining redox balance and generating low-potential products under low-energy conditions (singh2023syntrophicentanglementsfor pages 8-9). 

### 2.3 Syntrophy in ANME–SRB consortia (AOM)
A distinct, well-studied syntrophy occurs in **anaerobic oxidation of methane (AOM)**: obligate consortia of **ANME archaea** with **sulfate-reducing bacteria (SRB)**. Comparative metagenomics supports conserved DIET-related outer/periplasmic cytochromes (e.g., **OetA/OetB**, **OmcX**, **OmcS-like**) and variability in inner-membrane electron-transfer solutions (e.g., **Qrc**, **Qmo**, **DsrMKJOP**, clade-specific **CbcBA**) that ultimately drive sulfate reduction (murali2023physiologicalpotentialand pages 12-13). A 2024 review also frames AOM as occurring in syntrophic ANME–SRB aggregates where MIET and/or DIET may operate (zhuang2024electrontransferin pages 3-5).

A curated schematic of these SRB electron-transfer chains is shown in Murali et al. Figure 3 (murali2023physiologicalpotentialand media d028f686).

---

## 3) Recent developments (2023–2024 prioritized)

### 3.1 High-ammonia syntrophic communities: multi-omics resolves partners and carriers
Two 2023–2024 studies highlight **high ammonia** as a critical stressor that reshapes methanogenic ecosystems by inhibiting acetate-utilizing methanogens and selecting for **syntrophic acetate oxidation (SAO)** and **syntrophic propionate oxidation (SPO)** coupled to hydrogenotrophic methanogenesis (pinela2024impactofadditives pages 1-2, weng2024catabolismandinteractions pages 1-2).

* **Thermophilic, high-ammonia propionate/acetate oxidation (2023, ISME J)**: expression of **hydrogenases** and **formate dehydrogenases** (e.g., FrhABDG; FdhABD) and maturation factors (HypABCDE) supports active H2/formate-mediated syntrophy under thermodynamic constraints (singh2023syntrophicentanglementsfor pages 8-9).
* **Mesophilic, high-ammonia enrichments (2024, Frontiers in Microbiology)** identified key taxa and electron carriers: a syntrophic propionate oxidizer (“Ca. *Syntrophopropionicum ammoniitolerans*”), a SAOB (*Syntrophaceticus schinkii*), and a hydrogenotrophic methanogen (“Ca. *Methanoculleus ammoniitolerans*”), with gene expression consistent with use of both **H2 and formate** as electron outlets/sources (weng2024catabolismandinteractions pages 1-2).

### 3.2 Engineering DIET in anaerobic digestion (2023 reviews; 2024 additive experiments)
A 2023 review on conductive materials frames DIET as an approach to improve AD performance, listing carbon- and iron-based conductors (biochar, activated carbon, graphite, CNTs; magnetite, hematite, goethite, zero-valent iron) and asserting these can reduce lag time, stabilize systems, and increase methane while inhibiting VFA accumulation (kong2023enhancedanaerobicdigestion pages 1-2). 

A 2024 additive study under high ammonia reports that adding **iron oxide** (conductive) or **zeolite** (non-conductive) increased acetate (except graphene) and propionate degradation rates, with enrichment of floc-forming syntrophs on these surfaces—supporting the role of **cell proximity/surface colonization** and not only conductivity per se (pinela2024impactofadditives pages 1-2).

### 3.3 Hydrochar and short-chain fatty-acid (SCFA) syntrophy
In continuous-flow digesters treating waste activated sludge, **hydrochar increased methane production by 19%**, plausibly via effects on acidification/methanogenesis and stimulation of syntrophic SCFA oxidizers (shi2024syntrophicmicrobesinvolved pages 13-14). This provides a quantitative anchor for “real-world” implementation-oriented edges (material amendment → increased methane/syntrophic flux).

### 3.4 Sulfur-cycle electron transfer and syntrophic growth (2024)
A 2024 review on sulfur-cycle electron transfer highlights MIET (H2/formate) and DIET mechanisms (pili/nanowires/cytochromes), and notes DIET may enable faster electron transfer and improved energy yield relative to MIET in some syntrophic partnerships (zhuang2024electrontransferin pages 3-5).

---

## 4) Current applications and real-world implementations

### 4.1 Anaerobic digestion and industrial biogas
**Primary application**: stabilizing and accelerating anaerobic digestion by engineering syntrophic interactions.
* **Conductive material amendment** (biochar, activated carbon, magnetite, iron oxides, etc.) is a widely discussed strategy to stimulate DIET and improve methane recovery and stability, particularly under inhibitory conditions (kong2023enhancedanaerobicdigestion pages 1-2).
* **High-ammonia mitigation**: selection for SAO/SPO communities and targeted additives (e.g., zeolites as ion exchangers; iron oxides) to restore VFA conversion and methane yields (pinela2024impactofadditives pages 1-2, weng2024catabolismandinteractions pages 1-2).

### 4.2 Natural ecosystem biogeochemistry
* **Methane seep and marine sediments**: ANME–SRB syntrophy drives AOM and sulfate reduction through complex, conserved electron-transfer machineries (murali2023physiologicalpotentialand pages 12-13, murali2023physiologicalpotentialand media d028f686).
* **Sulfur cycling interfaces**: electroactive sulfur-cycle microbes show DIET/MIET-like interactions with implications for bioremediation and bioelectronics (zhuang2024electrontransferin pages 3-5).

---

## 5) Candidate causal-graph nodes (curation inventory)

| Group | Node label | Node type | Suggested ontology grounding | Brief evidence note |
|---|---|---|---|---|
| A. Processes/phenotypes | syntrophy | process/trait | METPO:1002006 | Core trait: metabolism of one species depends thermodynamically on partner removal of products/electrons; framed around H2/formate transfer and DIET in methanogenic systems (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15, nozhevnikova2020syntrophyandinterspecies pages 9-11, kong2023enhancedanaerobicdigestion pages 1-2) |
| A. Processes/phenotypes | interspecies hydrogen transfer | process | GO:0043547 | Canonical mediated IET mode in syntrophic communities; requires very low H2 and is often rate limiting (su2023areviewon pages 3-4, pinela2024impactofadditives pages 1-2) |
| A. Processes/phenotypes | interspecies formate transfer | process | unmapped | Alternative mediated IET route; often kinetically favorable because formate diffuses faster / occurs at higher concentrations than H2 (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15, nobu2020catabolismandinteractions pages 8-10) |
| A. Processes/phenotypes | direct interspecies electron transfer | process | GO:0099536 | DIET occurs via conductive pili/cytochromes or conductive materials and can bypass hydrogen/formate limitations (nozhevnikova2020syntrophyandinterspecies pages 9-11, su2023areviewon pages 3-4, kong2023enhancedanaerobicdigestion pages 1-2) |
| A. Processes/phenotypes | syntrophic propionate oxidation | metabolic process | unmapped | Major model of syntrophy and a rate-limiting step in anoxic decomposition / AD (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15, weng2024catabolismandinteractions pages 1-2) |
| A. Processes/phenotypes | syntrophic acetate oxidation | metabolic process | unmapped | Important under high-ammonia digestion where aceticlastic methanogens are inhibited (pinela2024impactofadditives pages 1-2, weng2024catabolismandinteractions pages 1-2) |
| A. Processes/phenotypes | anaerobic oxidation of methane in ANME-SRB consortia | metabolic process | GO:0015948 | Obligate syntrophy between ANME and sulfate-reducing bacteria involves conserved DIET-associated complexes (murali2023physiologicalpotentialand pages 12-13) |
| B. Pathways/modules | methylmalonyl-CoA pathway | pathway/module | MetaCyc:PWY-5973 | Key route for syntrophic propionate oxidation; expression documented in ammonia-tolerant SPOB (singh2023syntrophicentanglementsfor pages 8-9, weng2024catabolismandinteractions pages 1-2) |
| B. Pathways/modules | sulfate reduction pathway | pathway/module | GO:0019419 | Terminal electron-accepting pathway in syntrophic SRB partners; linked to Qmo, DsrMKJOP, DsrAB, AprAB, Sat (murali2023physiologicalpotentialand pages 12-13) |
| B. Pathways/modules | CO2-reducing hydrogenotrophic methanogenesis | pathway/module | GO:0015948 | Methanogenic partner metabolism that consumes H2/formate and maintains favorable energetics for syntrophs (nobu2020catabolismandinteractions pages 10-11, weng2024catabolismandinteractions pages 1-2) |
| B. Pathways/modules | reverse electron transport | pathway/module | GO:0006118 | Needed to generate low-potential carriers for H2/formate production near thermodynamic limit (singh2023syntrophicentanglementsfor pages 8-9, nobu2020catabolismandinteractions pages 8-10) |
| B. Pathways/modules | flavin-based electron bifurcation/confurcation | pathway/module | GO:0050136 | Proposed energy-conserving solution in syntrophic propionate oxidizers and related anaerobes (singh2023syntrophicentanglementsfor pages 8-9, westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15) |
| B. Pathways/modules | menaquinone loop | pathway/module | unmapped | Suggested in high-ammonia syntrophic communities as part of electron disposal / conservation (singh2023syntrophicentanglementsfor pages 8-9) |
| C. Molecular machines/complexes | hydrogenase complex | enzyme complex | GO:0018781 | Central for H2 production/consumption during mediated syntrophy; multiple hydrogenases expressed in syntrophic communities (singh2023syntrophicentanglementsfor pages 8-9, nobu2020catabolismandinteractions pages 8-10) |
| C. Molecular machines/complexes | formate dehydrogenase complex | enzyme complex | GO:0008863 | Central for formate production/consumption; periplasmic and Fdh-N/Fdh-H type systems implicated in syntrophy (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15, nobu2020catabolismandinteractions pages 8-10) |
| C. Molecular machines/complexes | electron-bifurcating hydrogenase FrhABDG | enzyme complex | UniProtKB:unmapped | Reported as expressed in thermophilic ammonia-tolerant syntrophic consortia (singh2023syntrophicentanglementsfor pages 8-9) |
| C. Molecular machines/complexes | FdhABD complex | enzyme complex | UniProtKB:unmapped | Specific formate dehydrogenase complex expressed in syntrophic communities under high ammonia (singh2023syntrophicentanglementsfor pages 8-9) |
| C. Molecular machines/complexes | F0F1 ATP synthase | enzyme complex | GO:0045259 | Energy conservation under near-equilibrium syntrophic growth; subunit C emphasized in transcript profiles (singh2023syntrophicentanglementsfor pages 8-9) |
| C. Molecular machines/complexes | Rnf complex | enzyme complex | GO:0043190 | Candidate ferredoxin/NAD coupling and ion-translocating complex supporting syntrophic redox balance (singh2023syntrophicentanglementsfor pages 8-9, nobu2020catabolismandinteractions pages 8-10) |
| C. Molecular machines/complexes | HdrABC complex | enzyme complex | GO:0034578 | Colocated with formate dehydrogenase genes in methanogens; implicated in low-energy electron flow (nobu2020catabolismandinteractions pages 10-11) |
| C. Molecular machines/complexes | Nfn electron-bifurcating complex | enzyme complex | UniProtKB:unmapped | Identified in methanogenic bioprocesses as part of eco-thermodynamic solutions (nobu2020catabolismandinteractions pages 8-10) |
| C. Molecular machines/complexes | conductive pili / e-pili / type IV pili | cell surface structure | GO:0009289 | Structural conduit for DIET; present in syntrophs and associated with DIET enrichment (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15, nozhevnikova2020syntrophyandinterspecies pages 9-11) |
| C. Molecular machines/complexes | multiheme c-type cytochrome conduits | molecular machine | GO:0009055 | Outer-surface/periplasmic EET components in DIET-capable syntrophs and ANME-SRB partners (nobu2020catabolismandinteractions pages 10-11, murali2023physiologicalpotentialand pages 12-13) |
| C. Molecular machines/complexes | QmoABC complex | enzyme complex | UniProtKB:unmapped | In syntrophic SRB, transfers quinone-derived electrons toward AprAB in sulfate reduction (murali2023physiologicalpotentialand pages 12-13) |
| C. Molecular machines/complexes | DsrMKJOP complex | enzyme complex | UniProtKB:unmapped | Inner-membrane electron transfer complex reducing DsrC/DsrAB-linked pathway in syntrophic SRB (murali2023physiologicalpotentialand pages 12-13) |
| C. Molecular machines/complexes | Qrc complex | enzyme complex | UniProtKB:unmapped | Links periplasmic electrons to quinone pool and contributes to proton motive force in syntrophic SRB (murali2023physiologicalpotentialand pages 12-13) |
| C. Molecular machines/complexes | CbcBA complex | enzyme complex | UniProtKB:unmapped | Alternative periplasm-to-quinone transfer complex in Seep-SRB2; evidence is clade-specific (murali2023physiologicalpotentialand pages 12-13) |
| D. Genes/proteins (families) | fdhA / formate dehydrogenase alpha subunit | gene/protein family | UniProtKB:unmapped | Marker of formate-mediated syntrophy; colocated with hdrABC/ferredoxins in methanogens (nobu2020catabolismandinteractions pages 10-11, nobu2020catabolismandinteractions pages 8-10) |
| D. Genes/proteins (families) | hypABCDE | gene family | UniProtKB:unmapped | Hydrogenase maturation factors expressed in high-ammonia syntrophic communities (singh2023syntrophicentanglementsfor pages 8-9) |
| D. Genes/proteins (families) | omcS-like cytochrome | gene/protein family | UniProtKB:unmapped | Canonical DIET-associated extracellular cytochrome; implicated in conductive electron transfer (nozhevnikova2020syntrophyandinterspecies pages 9-11, murali2023physiologicalpotentialand pages 12-13) |
| D. Genes/proteins (families) | oetA | gene/protein family | UniProtKB:unmapped | Conserved extracellular electron-transfer component in syntrophic SRB clades partnering ANME (murali2023physiologicalpotentialand pages 12-13) |
| D. Genes/proteins (families) | oetB | gene/protein family | UniProtKB:unmapped | Outer membrane conduit component of DIET-associated machinery in ANME-SRB partnerships (murali2023physiologicalpotentialand pages 12-13) |
| D. Genes/proteins (families) | omcX | gene/protein family | UniProtKB:unmapped | Conserved cytochrome candidate in extracellular/periplasmic transfer of syntrophic SRB (murali2023physiologicalpotentialand pages 12-13) |
| D. Genes/proteins (families) | apc2a | gene/protein family | UniProtKB:unmapped | Periplasmic/extracellular cytochrome candidate in syntrophic SRB electron transfer chain (murali2023physiologicalpotentialand pages 12-13) |
| D. Genes/proteins (families) | tmc complex genes | gene family | UniProtKB:unmapped | Divergent in some syntrophic SRB, consistent with adaptation to non-H2/non-formate donors from ANME (murali2023physiologicalpotentialand pages 12-13) |
| D. Genes/proteins (families) | pel genes | gene family | UniProtKB:unmapped | Biofilm formation pathway highlighted as horizontally transferred/adaptive in DIET-based syntrophic SRB; taxon-specific and should be curated cautiously (murali2023physiologicalpotentialand pages 12-13) |
| E. Metabolites/chemicals | hydrogen | metabolite | CHEBI:18276 | Principal soluble electron carrier in mediated syntrophy; low partial pressure required for feasibility (su2023areviewon pages 3-4, pinela2024impactofadditives pages 1-2) |
| E. Metabolites/chemicals | formate | metabolite | CHEBI:15740 | Soluble electron carrier often favored kinetically in syntrophy (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15, nobu2020catabolismandinteractions pages 8-10) |
| E. Metabolites/chemicals | acetate | metabolite | CHEBI:30089 | End/intermediate metabolite whose removal/oxidation is central in syntrophic acetate and propionate conversion (pinela2024impactofadditives pages 1-2, weng2024catabolismandinteractions pages 1-2) |
| E. Metabolites/chemicals | propionate | metabolite | CHEBI:17571 | Model substrate for syntrophic oxidation; often accumulates when syntrophy is impaired (weng2024catabolismandinteractions pages 1-2, kong2023enhancedanaerobicdigestion pages 1-2) |
| E. Metabolites/chemicals | carbon dioxide | metabolite | CHEBI:16526 | Methanogenic electron acceptor and substrate in hydrogenotrophic methanogenesis; interconverts with formate (su2023areviewon pages 3-4, weng2024catabolismandinteractions pages 1-2) |
| E. Metabolites/chemicals | methane | metabolite | CHEBI:16183 | Major end product of many syntrophic consortia in anaerobic digestion and natural methanogenic systems (kong2023enhancedanaerobicdigestion pages 1-2, su2023areviewon pages 13-15) |
| E. Metabolites/chemicals | sulfate | metabolite | CHEBI:16189 | Terminal electron acceptor for syntrophic sulfate-reducing partners in AOM consortia (murali2023physiologicalpotentialand pages 12-13) |
| E. Metabolites/chemicals | sulfide | metabolite | CHEBI:16199 | Sulfur-cycle syntrophy / sulfide oxidation can couple to methanogenesis through DIET-like interactions (zhuang2024electrontransferin pages 3-5) |
| E. Metabolites/chemicals | magnetite | chemical/material | CHEBI:46661 | Conductive iron oxide repeatedly reported to stimulate DIET/syntrophic degradation in digestion systems (pinela2024impactofadditives pages 17-18, kong2023enhancedanaerobicdigestion pages 1-2) |
| E. Metabolites/chemicals | biochar | chemical/material | unmapped | Conductive amendment enriching DIET-capable taxa and improving methanogenesis; mechanism still partly indirect (kong2023enhancedanaerobicdigestion pages 1-2) |
| E. Metabolites/chemicals | hydrochar | chemical/material | unmapped | Increased methane production by 19% in SCFA-oxidizing digester study; likely via stimulation of syntrophs (shi2024syntrophicmicrobesinvolved pages 13-14) |
| E. Metabolites/chemicals | zeolite | chemical/material | CHEBI:46727 | Non-conductive additive that can enhance syntrophy by surface colonization/flocculation and ammonia exchange (pinela2024impactofadditives pages 1-2) |
| F. Environmental/experimental factors | low hydrogen partial pressure | environmental factor | ENVO:unmapped | Required to make classic syntrophic H2 transfer thermodynamically feasible; DIET can bypass this limitation (su2023areviewon pages 3-4, kong2023enhancedanaerobicdigestion pages 1-2) |
| F. Environmental/experimental factors | high ammonia | environmental factor | CHEBI:16134 | Inhibits acetate-utilizing methanogens, causes VFA accumulation, and selects for SAOB/SPOB plus hydrogenotrophic methanogens (pinela2024impactofadditives pages 1-2, weng2024catabolismandinteractions pages 1-2) |
| F. Environmental/experimental factors | thermophilic condition | environmental factor | ENVO:01001023 | Supports distinct ammonia-tolerant syntrophic communities and interaction modes (singh2023syntrophicentanglementsfor pages 8-9) |
| F. Environmental/experimental factors | mesophilic condition | environmental factor | ENVO:01001022 | Supports distinct high-ammonia syntrophic communities described in enrichment studies (weng2024catabolismandinteractions pages 1-2) |
| F. Environmental/experimental factors | close cell proximity / co-aggregation / flocculation | experimental factor | GO:0098743 | Improves interspecies transfer efficiency; enriched syntrophs found in flocs and aggregates (pinela2024impactofadditives pages 1-2, pinela2024impactofadditives pages 17-18) |
| F. Environmental/experimental factors | conductive materials amendment | experimental factor | unmapped | Activated carbon, biochar, graphite, CNTs, magnetite, iron oxides can shorten lag and increase methane yield via DIET (kong2023enhancedanaerobicdigestion pages 1-2, su2023areviewon pages 13-15) |
| F. Environmental/experimental factors | trace metal availability (molybdate/tungstate) | environmental factor | CHEBI:23363 / CHEBI:27998 | Affects formate dehydrogenase activity and can shift balance between H2 and formate transfer (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15) |
| F. Environmental/experimental factors | low oxygen / nanomolar O2 | environmental factor | CHEBI:15379 | Ancillary electron sink in some methanogenic systems via cytochrome bd oxidase; not core syntrophy but may modulate thermodynamics (nobu2020catabolismandinteractions pages 10-11, nobu2020catabolismandinteractions pages 8-10) |
| G. Example taxa | Syntrophaceticus schinkii | taxon | NCBITaxon:unmapped | Canonical syntrophic acetate oxidizer enriched under high ammonia (pinela2024impactofadditives pages 1-2, weng2024catabolismandinteractions pages 1-2) |
| G. Example taxa | Candidatus Syntrophopropionicum ammoniitolerans | taxon | NCBITaxon:unmapped | Ammonia-tolerant syntrophic propionate oxidizer identified by omics in 2024 study (weng2024catabolismandinteractions pages 1-2) |
| G. Example taxa | Candidatus Thermosyntrophopropionicum ammoniitolerans | taxon | NCBITaxon:unmapped | Thermophilic ammonia-tolerant syntrophic propionate oxidizer expressing mmc pathway genes (singh2023syntrophicentanglementsfor pages 8-9) |
| G. Example taxa | Candidatus Methanoculleus ammoniitolerans | taxon | NCBITaxon:unmapped | Hydrogenotrophic methanogenic partner consuming H2/formate in high-ammonia syntrophic communities (weng2024catabolismandinteractions pages 1-2) |
| G. Example taxa | Methanothermobacter sp. | taxon | NCBITaxon:unmapped | Important hydrogen/formate-utilizing methanogenic partner in thermophilic propionate degradation (singh2023syntrophicentanglementsfor pages 8-9) |
| G. Example taxa | Methanospirillum hungatei | taxon | NCBITaxon:216 | Classic hydrogenotrophic syntrophic partner in propionate/fatty-acid oxidation cocultures (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15, shi2024syntrophicmicrobesinvolved pages 13-14) |
| G. Example taxa | Methanosarcina barkeri | taxon | NCBITaxon:2208 | Frequently cited DIET-capable methanogen with Geobacter and in conductive-material studies (pinela2024impactofadditives pages 17-18, su2023areviewon pages 13-15) |
| G. Example taxa | Methanothrix sp. | taxon | NCBITaxon:unmapped | Exoelectrogenic methanogen able to accept extracellular electrons/formate in methanogenic systems (nobu2020catabolismandinteractions pages 10-11, shi2024syntrophicmicrobesinvolved pages 13-14) |
| G. Example taxa | Pelotomaculum thermopropionicum | taxon | NCBITaxon:351627 | Classic syntrophic propionate oxidizer; often discussed for co-aggregation and possible DIET-related nanowires (pinela2024impactofadditives pages 1-2, pinela2024impactofadditives pages 17-18) |
| G. Example taxa | ANME archaea | taxon | NCBITaxon:unmapped | Obligate syntrophic methane oxidizers in AOM consortia with sulfate-reducing bacteria (murali2023physiologicalpotentialand pages 12-13) |
| G. Example taxa | Seep-SRB1a / Seep-SRB1g / Seep-SRB2 / HotSeep-1 | taxon | NCBITaxon:unmapped | Syntrophic SRB clades with conserved DIET complexes and distinct inner-membrane electron transfer solutions (murali2023physiologicalpotentialand pages 12-13, murali2023physiologicalpotentialand media d028f686) |


*Table: This table lists evidence-backed candidate nodes for a TraitMech causal graph of syntrophy, grouped by biological type and annotated with suggested ontology grounding. It is useful as a starting inventory for curating syntrophy.yaml with recent mechanistic evidence and caution flags for taxon-specific components.*

---

## 6) Evidence-backed candidate edges (triples) for `syntrophy.yaml`

| Subject node | Predicate | Object node | Evidence snippet (short quote) | Reference (DOI + year) | Notes |
|---|---|---|---|---|---|
| low hydrogen partial pressure | enables | interspecies hydrogen transfer | “H2-mediated transfer is thermodynamically feasible only when hydrogen partial pressures are extremely low (H2 < 10−4 atm)” | 10.3390/fermentation9050467 (2023) (su2023areviewon pages 3-4) | Classic MIET constraint; curate as environmental factor enabling GO:0043547 interspecies hydrogen transfer. Subject: low hydrogen partial pressure [unmapped ENVO candidate]; Object: GO:0043547. Strong review-supported claim. |
| hydrogenotrophic methanogenesis | decreases | hydrogen concentration | “consume and maintain formate/H2 at low levels to make the reactions feasible” | 10.1007/s00253-024-13263-7 (2024) (pinela2024impactofadditives pages 1-2) | Partner methanogens remove H2/formate, making syntrophic oxidation thermodynamically favorable. Subject: CO2-reducing hydrogenotrophic methanogenesis [GO:0015948 candidate]; Object: CHEBI:18276 hydrogen. Moderate strength; phrased from systems study/review background. |
| interspecies hydrogen transfer | mediates | syntrophy | “three main interspecies electron transfer (IET) modes relevant to syntrophy: H2-mediated MIET (IHT)” | 10.3390/fermentation9050467 (2023) (su2023areviewon pages 3-4) | Direct mechanistic sub-process of syntrophy. Subject: GO:0043547; Object: METPO:1002006. Strong review-supported edge. |
| interspecies formate transfer | mediates | syntrophy | “three interspecies electron transfer mechanisms in syntrophic propionate oxidation: interspecies H2 transfer, interspecies formate transfer, and direct interspecies electron transfer (DIET)” | 10.1093/femsre/fuab057 (2022) (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15) | Formate-based MIET is a core syntrophic mechanism. Subject: interspecies formate transfer [unmapped]; Object: METPO:1002006. Strong review-supported edge. |
| formate | kinetically_favors | interspecies electron transfer | “formate diffuses faster and typically occurs at higher concentrations, making formate kinetically and often energetically favorable” | 10.1093/femsre/fuab057 (2022) (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15) | Supports formate as an efficient MIET carrier. Subject: CHEBI:15740; Object: interspecies electron transfer [unmapped higher-level process]. Moderate strength; comparative interpretation. |
| formate dehydrogenase complex | mediates | interspecies formate transfer | “formate dehydrogenases Fdh-H and Fdh-N” and “formate transporters ... expressed by 88.9% of FA-degrading species” | 10.1186/s40168-020-00885-y (2020) (nobu2020catabolismandinteractions pages 8-10) | Enzymatic basis for formate production/consumption in syntrophy. Subject: GO:0008863; Object: interspecies formate transfer [unmapped]. Strong but somewhat system-general. |
| hydrogenase complex | mediates | interspecies hydrogen transfer | “Hydrogen- and formate-mediated transfer is supported by expression of hydrogenases and formate dehydrogenases” | 10.1038/s41396-023-01504-y (2023) (singh2023syntrophicentanglementsfor pages 8-9) | Expression evidence in high-ammonia thermophilic syntrophic communities. Subject: GO:0018781; Object: GO:0043547. Strong within studied enrichments. |
| direct interspecies electron transfer | bypasses | hydrogen pressure inhibition | “DIET ... can overcome the inhibition of hydrogen pressure and formate concentration” | 10.3390/fermentation9100884 (2023) (kong2023enhancedanaerobicdigestion pages 1-2) | Important boundary distinction: DIET is syntrophy without soluble H2/formate intermediates. Subject: GO:0099536; Object: hydrogen pressure inhibition [label node]. Strong review-supported claim. |
| conductive pili (e-pili) | mediates | direct interspecies electron transfer | “DIET occurs via (A) conductive pili (e-pili)” | 10.1134/S0026261720020101 (2020) (nozhevnikova2020syntrophyandinterspecies pages 9-11) | Canonical DIET conduit. Subject: GO:0009289 candidate; Object: GO:0099536. Strong review-supported edge. |
| multiheme c-type cytochromes | mediates | direct interspecies electron transfer | “DIET operates via ... outer-surface c-type cytochromes” | 10.3390/life14050591 (2024) (zhuang2024electrontransferin pages 3-5) | Core DIET redox conduit family. Subject: multiheme c-type cytochromes [unmapped family]; Object: GO:0099536. Strong review-supported edge. |
| conductive materials amendment | promotes | direct interspecies electron transfer | “conductive materials can shorten the lag time, promote the stability of the system, increase biogas production” | 10.3390/fermentation9100884 (2023) (kong2023enhancedanaerobicdigestion pages 1-2) | Engineering intervention widely reported in AD. Subject: conductive materials amendment [label node]; Object: GO:0099536. Strong but application-focused. |
| iron oxide | increases | syntrophic acetate and propionate degradation rate | “addition of conductive (iron oxide) and non-conductive (zeolite) additives increased acetate ... and propionate degradation rates” | 10.1007/s00253-024-13263-7 (2024) (pinela2024impactofadditives pages 1-2) | Experimental enrichment evidence under high ammonia; mechanism may include DIET and/or improved colonization. Subject: iron oxide [CHEBI candidate/unmapped]; Object: syntrophic acid degradation [label node]. Moderate strength; mechanism partly uncertain. |
| zeolite | increases | syntrophic acetate and propionate degradation rate | “increased acetate (except graphene) and propionate degradation rates” | 10.1007/s00253-024-13263-7 (2024) (pinela2024impactofadditives pages 1-2) | Non-conductive additive suggests benefits can arise via flocculation/surface colonization or ammonia exchange, not only DIET. Subject: CHEBI:46727; Object: syntrophic acid degradation [label node]. Moderate strength; mechanism uncertain. |
| close cell proximity / flocculation | promotes | syntrophy | “floc-forming syntrophs ... were enriched in flocs, suggesting benefits of cell proximity and surface-mediated electron transfer” | 10.1007/s00253-024-13263-7 (2024) (pinela2024impactofadditives pages 1-2) | Important experimental factor; not specific to DIET only. Subject: close cell proximity/flocculation [label node]; Object: METPO:1002006. Moderate strength. |
| high ammonia | inhibits | acetate-utilizing methanogens | “high ammonia inhibits members of anaerobic digestion communities—particularly acetate-utilizing methanogens” | 10.3389/fmicb.2024.1389257 (2024) (weng2024catabolismandinteractions pages 1-2) | Major selective pressure shifting community structure. Subject: ammonia [CHEBI:16134]; Object: acetate-utilizing methanogens [label node]. Strong study-backed claim. |
| high ammonia | promotes | syntrophic acetate oxidation | “High ammonia inhibits aceticlastic methanogens and promotes reliance on SAOB/SPOB plus hydrogenotrophic methanogens” | 10.1007/s00253-024-13263-7 (2024) (pinela2024impactofadditives pages 1-2) | Selective-pressure edge; community-level rather than cell-autonomous. Subject: CHEBI:16134; Object: syntrophic acetate oxidation [label node]. Moderate-strong. |
| high ammonia | promotes | syntrophic propionate oxidation partnerships | “promotes reliance on SAOB/SPOB plus hydrogenotrophic methanogens” | 10.1007/s00253-024-13263-7 (2024) (pinela2024impactofadditives pages 1-2) | Similar selection for SPOB–methanogen cooperation under ammonia stress. Subject: CHEBI:16134; Object: syntrophic propionate oxidation [label node]. Moderate. |
| OetA/OetB outer-membrane conduit | mediates | extracellular electron transfer from ANME to SRB | “Conserved extracellular and periplasmic cytochromes implicated in DIET include OetA, OetB” | 10.1371/journal.pbio.3002292 (2023) (murali2023physiologicalpotentialand pages 12-13) | Taxon-specific to ANME-associated SRB clades; suitable as DIET machinery node in AOM syntrophy. Subject: OetA/OetB [unmapped family]; Object: extracellular electron transfer / DIET [GO:0099536 candidate]. Strong within ANME–SRB systems. |
| OmcS-like / OmcX cytochromes | mediates | extracellular electron transfer from ANME to SRB | “Conserved extracellular and periplasmic cytochromes implicated in DIET include ... OmcX, OmcS-like” | 10.1371/journal.pbio.3002292 (2023) (murali2023physiologicalpotentialand pages 12-13) | Adds specific cytochrome families for ANME–SRB syntrophy. Subject: OmcS-like/OmcX [unmapped family]; Object: GO:0099536 candidate. Strong but clade-specific. |
| Qrc complex | transfers | periplasmic electrons to quinone pool | “Qrc (links periplasmic electrons to quinone pool and contributes to pmf)” | 10.1371/journal.pbio.3002292 (2023) (murali2023physiologicalpotentialand pages 12-13) | Inner-membrane coupling step in syntrophic SRB. Subject: Qrc complex [unmapped]; Object: quinone pool [label node]. Strong in ANME–SRB context; taxon-specific. |
| QmoABC complex | transfers | quinone-derived electrons to AprAB | “Qmo (quinone→AprAB)” | 10.1371/journal.pbio.3002292 (2023) (murali2023physiologicalpotentialand pages 12-13) | Sulfate-reduction-linked edge downstream of syntrophic electron uptake. Subject: QmoABC [unmapped]; Object: AprAB adenylylsulfate reductase [unmapped]. Strong but clade/system-specific. |
| DsrMKJOP complex | transfers | quinone-derived electrons to DsrC/DsrAB pathway | “DsrMKJOP (quinone→DsrC→DsrAB)” | 10.1371/journal.pbio.3002292 (2023) (murali2023physiologicalpotentialand pages 12-13) | Mechanistic inner-membrane edge linking incoming electrons to sulfate reduction. Subject: DsrMKJOP [unmapped]; Object: DsrC/DsrAB sulfate reduction pathway [GO:0019419 candidate]. Strong but taxon-specific. |
| CbcBA complex | mediates | periplasm-to-quinone electron transfer | “CbcBA (in Seep-SRB2, likely mediating periplasm→quinone transfer)” | 10.1371/journal.pbio.3002292 (2023) (murali2023physiologicalpotentialand pages 12-13) | Useful candidate node, but clearly clade-specific and should be flagged uncertain for generic syntrophy. Subject: CbcBA [unmapped]; Object: periplasm-to-quinone electron transfer [label node]. Uncertain/generalizability warning. |
| direct interspecies electron transfer | enables | sulfate-coupled ANME–SRB syntrophy | “AOM is carried out by syntrophic ANME–SRB consortia that form granule-like aggregates likely facilitating electron exchange” | 10.3390/life14050591 (2024) (zhuang2024electrontransferin pages 3-5) | Broad systems-level edge for marine methane seep syntrophy. Subject: GO:0099536; Object: ANME–SRB syntrophy [label node]. Moderate strength; mechanism may vary by consortium. |


*Table: This table lists evidence-backed candidate subject-predicate-object edges for curating a TraitMech causal graph of syntrophy, covering mediated H2/formate transfer, DIET, thermodynamic constraints, ammonia effects, and ANME–SRB electron-transfer machinery.*

---

## 7) Expert/authoritative interpretations (what to curate vs defer)

### Strong, generally curatable themes
* **Thermodynamic dependence via product removal** is central to syntrophy; MIET often requires extremely low H2 (H2 < 10−4 atm) (su2023areviewon pages 3-4).
* **DIET mechanisms** via conductive pili/cytochromes/conductive materials are repeatedly supported across reviews and system studies, and DIET is framed as bypassing H2/formate limitations (nozhevnikova2020syntrophyandinterspecies pages 9-11, kong2023enhancedanaerobicdigestion pages 1-2).
* **High ammonia as a selective pressure**: inhibits acetate-utilizing methanogens and favors SAO/SPO + hydrogenotrophic methanogenesis (pinela2024impactofadditives pages 1-2, weng2024catabolismandinteractions pages 1-2).

### Taxon- or context-specific components (curate with flags)
* **ANME–SRB complexes** (OetA/OetB, Qrc, QmoABC, DsrMKJOP, CbcBA) are very strong for AOM consortia but should be marked as **AOM/SRB-specific** rather than universal syntrophy machinery (murali2023physiologicalpotentialand pages 12-13, murali2023physiologicalpotentialand media d028f686).
* **CbcBA** is explicitly clade-specific (Seep-SRB2) and should be curated with an uncertainty/generalizability warning (murali2023physiologicalpotentialand pages 12-13).

---

## 8) Statistics and data points suitable for causal edges

* **Thermodynamic threshold**: H2-mediated MIET feasible only when **H2 partial pressure is extremely low (H2 < 10−4 atm)** (su2023areviewon pages 3-4).
* **Implementation outcome**: **hydrochar increased methane production by 19%** in a continuous-flow AD context (shi2024syntrophicmicrobesinvolved pages 13-14).

(Additional quantitative effect sizes for individual conductive materials/additives are frequently referenced in reviews, but not consistently extractable from the retrieved excerpts; treat as “needs full-text extraction” if required for curation-grade numeric edges.)

---

## 9) DOI-first bibliography (with URLs and publication dates where available)

* Su K, Li L, Wang Q, Cao R. **A Review on the Interspecies Electron Transfer of Methane Production in Anaerobic Digestion System**. *Fermentation*. **May 2023**. DOI: **10.3390/fermentation9050467**. URL: https://doi.org/10.3390/fermentation9050467 (su2023areviewon pages 3-4)
* Kong T, Zhang W-Q. **Enhanced Anaerobic Digestion Using Conductive Materials through Mediation of Direct Microbial Interspecies Electron Transfer: A Review**. *Fermentation*. **Sep 2023**. DOI: **10.3390/fermentation9100884**. URL: https://doi.org/10.3390/fermentation9100884 (kong2023enhancedanaerobicdigestion pages 1-2)
* Singh A, Schnürer A, Dolfing J, Westerholm M. **Syntrophic entanglements for propionate and acetate oxidation under thermophilic and high-ammonia conditions**. *The ISME Journal*. **Sep 2023**. DOI: **10.1038/s41396-023-01504-y**. URL: https://doi.org/10.1038/s41396-023-01504-y (singh2023syntrophicentanglementsfor pages 8-9)
* Murali R, Yu H, Speth DR, et al. **Physiological potential and evolutionary trajectories of syntrophic sulfate-reducing bacterial partners of anaerobic methanotrophic archaea**. *PLOS Biology*. **Sep 2023**. DOI: **10.1371/journal.pbio.3002292**. URL: https://doi.org/10.1371/journal.pbio.3002292 (murali2023physiologicalpotentialand pages 12-13, murali2023physiologicalpotentialand media d028f686)
* Weng N, Singh A, Ohlsson JA, Dolfing J, Westerholm M. **Catabolism and interactions of syntrophic propionate- and acetate oxidizing microorganisms under mesophilic, high-ammonia conditions**. *Frontiers in Microbiology*. **Jun 2024**. DOI: **10.3389/fmicb.2024.1389257**. URL: https://doi.org/10.3389/fmicb.2024.1389257 (weng2024catabolismandinteractions pages 1-2)
* Pinela E, Schnürer A, Neubeck A, Moestedt J, Westerholm M. **Impact of additives on syntrophic propionate and acetate enrichments under high-ammonia conditions**. *Applied Microbiology and Biotechnology*. **Aug 2024**. DOI: **10.1007/s00253-024-13263-7**. URL: https://doi.org/10.1007/s00253-024-13263-7 (pinela2024impactofadditives pages 1-2)
* Shi Z, Zhang C, Tan X, Xie L, Luo G. **Syntrophic microbes involved in the oxidation of short-chain fatty acids in continuous-flow anaerobic digesters treating waste activated sludge with hydrochar**. *Applied and Environmental Microbiology*. **Feb 2024**. DOI: **10.1128/aem.02047-23**. URL: https://doi.org/10.1128/aem.02047-23 (shi2024syntrophicmicrobesinvolved pages 13-14)
* Zhuang X, Wang S, Wu S. **Electron Transfer in the Biogeochemical Sulfur Cycle**. *Life*. **May 2024**. DOI: **10.3390/life14050591**. URL: https://doi.org/10.3390/life14050591 (zhuang2024electrontransferin pages 3-5)

Supporting (pre-2023) high-impact context used for grounding mechanisms:
* Westerholm M, Calusinska M, Dolfing J. *FEMS Microbiology Reviews*. **Dec 2022**. DOI: **10.1093/femsre/fuab057**. URL: https://doi.org/10.1093/femsre/fuab057 (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15)
* Nobu MK, Narihiro T, Mei R, et al. *Microbiome*. **Jul 2020**. DOI: **10.1186/s40168-020-00885-y**. URL: https://doi.org/10.1186/s40168-020-00885-y (nobu2020catabolismandinteractions pages 10-11, nobu2020catabolismandinteractions pages 8-10)
* Nozhevnikova AN, et al. *Microbiology*. **Mar 2020**. DOI: **10.1134/S0026261720020101**. URL: https://doi.org/10.1134/S0026261720020101 (nozhevnikova2020syntrophyandinterspecies pages 9-11)

---

## 10) Warnings / “do-not-curate-yet” items

1. **DIET attribution is often indirect in engineered systems**: conductive materials can improve performance, but whether the dominant mechanism is DIET vs improved aggregation/trace-metal effects can be unresolved; curate “material → increased syntrophic rate/methane” separately from “material → DIET” unless direct evidence is present (pinela2024impactofadditives pages 1-2, kong2023enhancedanaerobicdigestion pages 1-2).
2. **Taxon specificity of ANME–SRB electron-transfer machinery**: complexes like **OetA/OetB** and **CbcBA** are well supported in ANME-partner SRB but should not be generalized to all syntrophic communities without corroboration (murali2023physiologicalpotentialand pages 12-13, murali2023physiologicalpotentialand media d028f686).
3. **Ontology grounding gaps**: several cytochrome conduit names (e.g., OetA/OetB, OmcX) lack universally stable identifiers in the extracted evidence; curate as label-only nodes unless you can map to UniProt/GO terms during YAML curation.


References

1. (su2023areviewon pages 3-4): Kai Su, Linxiao Li, Qin Wang, and Rong Cao. A review on the interspecies electron transfer of methane production in anaerobic digestion system. Fermentation, 9:467, May 2023. URL: https://doi.org/10.3390/fermentation9050467, doi:10.3390/fermentation9050467. This article has 54 citations.

2. (kong2023enhancedanaerobicdigestion pages 1-2): Tianqi Kong and Wan-Qing Zhang. Enhanced anaerobic digestion using conductive materials through mediation of direct microbial interspecies electron transfer: a review. Fermentation, 9:884, Sep 2023. URL: https://doi.org/10.3390/fermentation9100884, doi:10.3390/fermentation9100884. This article has 37 citations.

3. (nozhevnikova2020syntrophyandinterspecies pages 9-11): A. N. Nozhevnikova, Yu. I. Russkova, Yu. V. Litti, S. N. Parshina, E. A. Zhuravleva, and A. A. Nikitina. Syntrophy and interspecies electron transfer in methanogenic microbial communities. Microbiology, 89:129-147, Mar 2020. URL: https://doi.org/10.1134/s0026261720020101, doi:10.1134/s0026261720020101. This article has 141 citations and is from a peer-reviewed journal.

4. (westerholm2022syntrophicpropionateoxidizingbacteria pages 14-15): Maria Westerholm, Magdalena Calusinska, and Jan Dolfing. Syntrophic propionate-oxidizing bacteria in methanogenic systems. FEMS Microbiology Reviews, Dec 2022. URL: https://doi.org/10.1093/femsre/fuab057, doi:10.1093/femsre/fuab057. This article has 162 citations and is from a domain leading peer-reviewed journal.

5. (nobu2020catabolismandinteractions pages 8-10): Masaru K. Nobu, Takashi Narihiro, Ran Mei, Yoichi Kamagata, Patrick K. H. Lee, Po-Heng Lee, Michael J. McInerney, and Wen-Tso Liu. Catabolism and interactions of uncultured organisms shaped by eco-thermodynamics in methanogenic bioprocesses. Microbiome, Jul 2020. URL: https://doi.org/10.1186/s40168-020-00885-y, doi:10.1186/s40168-020-00885-y. This article has 101 citations and is from a highest quality peer-reviewed journal.

6. (zhuang2024electrontransferin pages 3-5): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

7. (singh2023syntrophicentanglementsfor pages 8-9): Abhijeet Singh, Anna Schnürer, Jan Dolfing, and Maria Westerholm. Syntrophic entanglements for propionate and acetate oxidation under thermophilic and high-ammonia conditions. The ISME Journal, 17:1966-1978, Sep 2023. URL: https://doi.org/10.1038/s41396-023-01504-y, doi:10.1038/s41396-023-01504-y. This article has 68 citations.

8. (murali2023physiologicalpotentialand pages 12-13): Ranjani Murali, Hang Yu, Daan R. Speth, Fabai Wu, Kyle S. Metcalfe, Antoine Crémière, Rafael Laso-Pèrez, Rex R. Malmstrom, Danielle Goudeau, Tanja Woyke, Roland Hatzenpichler, Grayson L. Chadwick, Stephanie A. Connon, and Victoria J. Orphan. Physiological potential and evolutionary trajectories of syntrophic sulfate-reducing bacterial partners of anaerobic methanotrophic archaea. Sep 2023. URL: https://doi.org/10.1371/journal.pbio.3002292, doi:10.1371/journal.pbio.3002292. This article has 55 citations and is from a highest quality peer-reviewed journal.

9. (murali2023physiologicalpotentialand media d028f686): Ranjani Murali, Hang Yu, Daan R. Speth, Fabai Wu, Kyle S. Metcalfe, Antoine Crémière, Rafael Laso-Pèrez, Rex R. Malmstrom, Danielle Goudeau, Tanja Woyke, Roland Hatzenpichler, Grayson L. Chadwick, Stephanie A. Connon, and Victoria J. Orphan. Physiological potential and evolutionary trajectories of syntrophic sulfate-reducing bacterial partners of anaerobic methanotrophic archaea. Sep 2023. URL: https://doi.org/10.1371/journal.pbio.3002292, doi:10.1371/journal.pbio.3002292. This article has 55 citations and is from a highest quality peer-reviewed journal.

10. (pinela2024impactofadditives pages 1-2): Eduardo Pinela, Anna Schnürer, Anna Neubeck, Jan Moestedt, and Maria Westerholm. Impact of additives on syntrophic propionate and acetate enrichments under high-ammonia conditions. Applied Microbiology and Biotechnology, Aug 2024. URL: https://doi.org/10.1007/s00253-024-13263-7, doi:10.1007/s00253-024-13263-7. This article has 7 citations and is from a domain leading peer-reviewed journal.

11. (weng2024catabolismandinteractions pages 1-2): Nils Weng, Abhijeet Singh, Jonas A. Ohlsson, Jan Dolfing, and Maria Westerholm. Catabolism and interactions of syntrophic propionate- and acetate oxidizing microorganisms under mesophilic, high-ammonia conditions. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1389257, doi:10.3389/fmicb.2024.1389257. This article has 17 citations and is from a peer-reviewed journal.

12. (shi2024syntrophicmicrobesinvolved pages 13-14): Zhijian Shi, Chen Zhang, Xuejun Tan, Li Xie, and Gang Luo. Syntrophic microbes involved in the oxidation of short-chain fatty acids in continuous-flow anaerobic digesters treating waste activated sludge with hydrochar. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.02047-23, doi:10.1128/aem.02047-23. This article has 4 citations and is from a peer-reviewed journal.

13. (nobu2020catabolismandinteractions pages 10-11): Masaru K. Nobu, Takashi Narihiro, Ran Mei, Yoichi Kamagata, Patrick K. H. Lee, Po-Heng Lee, Michael J. McInerney, and Wen-Tso Liu. Catabolism and interactions of uncultured organisms shaped by eco-thermodynamics in methanogenic bioprocesses. Microbiome, Jul 2020. URL: https://doi.org/10.1186/s40168-020-00885-y, doi:10.1186/s40168-020-00885-y. This article has 101 citations and is from a highest quality peer-reviewed journal.

14. (su2023areviewon pages 13-15): Kai Su, Linxiao Li, Qin Wang, and Rong Cao. A review on the interspecies electron transfer of methane production in anaerobic digestion system. Fermentation, 9:467, May 2023. URL: https://doi.org/10.3390/fermentation9050467, doi:10.3390/fermentation9050467. This article has 54 citations.

15. (pinela2024impactofadditives pages 17-18): Eduardo Pinela, Anna Schnürer, Anna Neubeck, Jan Moestedt, and Maria Westerholm. Impact of additives on syntrophic propionate and acetate enrichments under high-ammonia conditions. Applied Microbiology and Biotechnology, Aug 2024. URL: https://doi.org/10.1007/s00253-024-13263-7, doi:10.1007/s00253-024-13263-7. This article has 7 citations and is from a domain leading peer-reviewed journal.