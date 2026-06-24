---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:59:53.831456'
end_time: '2026-06-18T06:17:25.365307'
duration_seconds: 1051.53
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: sulfur oxidation
  trait_identifier: traitmech:000106
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: sulfur_oxidation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which an organism oxidizes reduced inorganic sulfur
    compounds (sulfide, elemental sulfur, thiosulfate) to sulfate, conserving energy
    and often supporting chemolithotrophic growth.
  parent_traits: METPO:1000060
  synonyms: sulfide oxidation
  evidence_summary: 'DOI:10.1111/j.1574-6976.2009.00187.x:  (Ghosh & Dam review the
    biochemistry and molecular biology of lithotrophic sulfur oxidation across bacteria
    and archaea.) | DOI:10.1128/AEM.67.7.2873-2882.2001:  (Friedrich et al. describe
    a common mechanism for bacterial oxidation of reduced inorganic sulfur compounds
    (the Sox system).)'
  causal_graph_summary: 'sulfur_oxidation_sox: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sulfur oxidation
- **METPO identifier:** traitmech:000106
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes reduced inorganic sulfur compounds (sulfide, elemental sulfur, thiosulfate) to sulfate, conserving energy and often supporting chemolithotrophic growth.
- **Parent traits:** METPO:1000060
- **Synonyms:** sulfide oxidation
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00187.x:  (Ghosh & Dam review the biochemistry and molecular biology of lithotrophic sulfur oxidation across bacteria and archaea.) | DOI:10.1128/AEM.67.7.2873-2882.2001:  (Friedrich et al. describe a common mechanism for bacterial oxidation of reduced inorganic sulfur compounds (the Sox system).)
- **Existing causal graph summary:** sulfur_oxidation_sox: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **sulfur oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/sulfur_oxidation.yaml`.

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
- **Trait label:** sulfur oxidation
- **METPO identifier:** traitmech:000106
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes reduced inorganic sulfur compounds (sulfide, elemental sulfur, thiosulfate) to sulfate, conserving energy and often supporting chemolithotrophic growth.
- **Parent traits:** METPO:1000060
- **Synonyms:** sulfide oxidation
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00187.x:  (Ghosh & Dam review the biochemistry and molecular biology of lithotrophic sulfur oxidation across bacteria and archaea.) | DOI:10.1128/AEM.67.7.2873-2882.2001:  (Friedrich et al. describe a common mechanism for bacterial oxidation of reduced inorganic sulfur compounds (the Sox system).)
- **Existing causal graph summary:** sulfur_oxidation_sox: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **sulfur oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/sulfur_oxidation.yaml`.

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


## Research report: Microbial sulfur oxidation (TraitMech: sulfur oxidation; METPO traitmech:000106)

### Publication focus
This report prioritizes 2024 peer‑reviewed literature (and 2023–2024 where available) and is designed for curation into `data/traits/metabolism/sulfur_oxidation.yaml`.

---

## 1) Trait scope (what the trait represents)

### Operational definition (curation-ready)
**Sulfur oxidation** is a microbial energy metabolism that **oxidizes reduced inorganic sulfur compounds** (e.g., sulfide, elemental sulfur/polysulfide/sulfane sulfur, thiosulfate, tetrathionate, sulfite) toward **sulfate**, often supporting chemolithotrophic or mixotrophic growth and strongly influencing environmental acidity and sulfur speciation (twible2024phandthiosulfate pages 1-2, rudenko2024mechanismofintracellular pages 1-2).

### Boundary cases and distinctions
1. **Complete Sox vs. incomplete Sox**: systems possessing the full Sox complement can fully oxidize reduced sulfur to sulfate, whereas incomplete Sox lacks key components (often SoxCD) and leads to accumulation/handling of **sulfane sulfur or S0** that must be further processed by cytoplasmic systems (yan2024characterizationofsulfur pages 59-63, liu2024determinantsofsulfuroxidizinga pages 17-20).
2. **Sulfur oxidation vs. sulfur reduction/disproportionation**: sulfur reduction or tetrathionate reduction uses oxidized sulfur species as terminal electron acceptors; these are distinct traits (even if encoded in the same genome) (gordon2024microbialsulfurpathways pages 1-5, gordon2024microbialsulfurpathways pages 5-8).
3. **Detoxification vs. energy conservation**: some organisms may use enzymes such as **SQR** primarily for sulfide detoxification rather than net energy generation; treat this as a boundary case unless growth/yield evidence supports chemolithotrophy (conceptual boundary; mechanistic SQR role supported in sulfur oxidizers) (rudenko2024mechanismofintracellular pages 1-2, petushkova2024thecompletegenome pages 19-20).

---

## 2) Key concepts and current mechanistic understanding

### 2.1 Canonical pathway modules
#### A. Sox system (periplasmic thiosulfate/sulfur oxidation module)
A widely used oxidation strategy is the **Sox multienzyme system**, commonly described as **periplasmic**, converting reduced sulfur species to sulfate (liu2024determinantsofsulfuroxidizinga pages 17-20). In a mechanistic model described for sulfur oxidizers, thiosulfate is oxidized via Sox components (SoxAX, SoxYZ, SoxB, and SoxCD when present), and the presence/absence of SoxCD strongly affects whether oxidation is “complete” or leaves sulfane intermediates (liu2024determinantsofsulfuroxidizinga pages 17-20).

#### B. rDSR (reverse dissimilatory sulfite reductase) module for oxidation of reduced sulfur
The **rDSR pathway** is a major strategy used to oxidize reduced sulfur species (especially when sulfur is stored/handled intracellularly). In mining‑impacted habitats, “**rdsr genes… operate in the reverse direction by oxidizing reduced sulfur species**” (yan2024characterizationofsulfur pages 59-63).

#### C. S4I (tetrathionate intermediate) module
The **S4I/tetrathionate-intermediate** module can proceed via **TsdA (thiosulfate dehydrogenase)** generating tetrathionate from thiosulfate (twible2024phandthiosulfate pages 1-2), followed by tetrathionate turnover that may involve **TetH** and can yield sulfur intermediates including elemental sulfur, thiosulfate, and sulfate depending on organism and conditions (twible2024phandthiosulfate pages 5-6).

#### D. Sulfide oxidation entry points: SQR and FccAB
Sulfide oxidation can begin at membrane/periplasm entry enzymes. In Thiocapsa bogorovii, **SQR** is described as a cytoplasmic‑membrane bound flavoprotein producing polysulfide as a primary product (petushkova2024thecompletegenome pages 19-20). Beggiatoa leptomitoformis similarly uses SQR to oxidize sulfide to sulfane sulfur (S0/polysulfide) (rudenko2024mechanismofintracellular pages 1-2).

### 2.2 Example of an integrated intracellular/periplasmic sulfur oxidation network (Beggiatoa)
Rudenko et al. (2024) provide a mechanistically explicit model connecting sulfide oxidation, intracellular sulfur storage, and periplasmic Sox oxidation:
- SQR oxidizes sulfide to sulfane sulfur/polysulfide (rudenko2024mechanismofintracellular pages 1-2).
- Sulfane sulfur is transferred to glutathione persulfide (GSSH), and **PDO oxidizes GSSH to sulfite** with an explicit O2‑dependent reaction: “GSSH + O2 + H2O → GSH + SO3(2−) + 2H+” (rudenko2024mechanismofintracellular pages 1-2).
- Sulfite can react with sulfane sulfur to form **thiosulfate**, which is then oxidized by the Sox system toward sulfate (rudenko2024mechanismofintracellular pages 1-2).
- Quantitative regulation in this system: RT‑qPCR showed ~6‑fold upregulation of **pdo** and ~15‑fold upregulation of **Sox genes** when grown on elemental sulfur vs sulfide (rudenko2024mechanismofintracellular pages 12-13).

---

## 3) Recent developments and latest research (2023–2024 prioritized)

### 3.1 Sulfur import and regulation: SoxT/YeeE-like transporters and SoxR (2024)
A major 2024 development is direct genetic evidence that **YeeE/YedE-like “SoxT” proteins** can be essential for sulfur oxidation and regulation in some sulfur oxidizers:
- **SoxT1A**: “SoxT1A delivers sulfur to the cytoplasm for its further oxidation” (li2024yeeelikebacterialsoxt pages 1-2), and “all SoxT1A‑deficient strains are unable to oxidize thiosulfate” (li2024yeeelikebacterialsoxt pages 7-8).
- **SoxT1B**: acts in regulation/signal transduction—“SoxT1B serves as a signal transduction unit for the transcriptional repressor SoxR” (li2024yeeelikebacterialsoxt pages 7-8). Deleting soxT1B in the tested background “abolishes thiosulfate oxidation” and complementation restores oxidation (li2024yeeelikebacterialsoxt pages 5-7).
- Regulation: “SoxR… binds the sox promoter-operator to prevent transcription when sulfur is absent” (li2024yeeelikebacterialsoxt pages 1-2). Thiosulfate induces soxT1A transcript abundance “more than tenfold” (li2024yeeelikebacterialsoxt pages 2-3).

Curation implication: SoxT/SoxR are strong candidate nodes/edges for a regulatory subgraph, but should be tagged **taxon-specific** until broader conservation is demonstrated (li2024yeeelikebacterialsoxt pages 2-3, li2024yeeelikebacterialsoxt pages 7-8).

### 3.2 Evolutionary/ecological innovation: soxY gene-family expansion in symbiotic SOB (2024)
Sudo et al. (2024) analyzed **234** genomes of symbiotic and free-living sulfur oxidizers and found “a gene family expansion of soxY… with up to five distinct copies per genome” (sudo2024soxygenefamily pages 1-2). Their SoxY dataset included **1,631 full-length SoxY sequences** and multiple “swinging arm” signature variants, supporting diversification (sudo2024soxygenefamily pages 4-6, sudo2024soxygenefamily pages 8-11).

They also propose an expert interpretation that **copy number and divergence of SoxY** correlates with ecological strategy: canonical-only soxY tends to associate with “specialists,” while multiple divergent soxY copies associate with broader host/environment ranges (“generalists”) (sudo2024soxygenefamily pages 1-2, sudo2024soxygenefamily pages 15-17). This is best modeled as an ecology/modifier layer rather than a core biochemical edge.

---

## 4) Current applications and real-world implementations

### 4.1 Mining-impacted waters and tailings impoundments (field + mesocosm)
#### pH/thiosulfate management as a lever on pathway selection and acidity
Twible et al. (2024) linked pathway distributions to real-world mine tailings impoundments over **four years (2016–2019)** and reported **pH-partitioned sulfur oxidizer groups**:
- At lower pH (~5 to ~6.5), “csox dominant” taxa drove acidity generation and thiosulfate consumption (twible2024phandthiosulfate pages 1-2).
- At circumneutral pH (~6.5 to ~8.5), non‑csox taxa (incomplete sox, rDSR, other reactions) associated with higher thiosulfate and limited acidity (twible2024phandthiosulfate pages 1-2).

Quantitative field statistics underpinning implementable monitoring/controls:
- Across sites, pH ranged **5.1–11.8** (twible2024phandthiosulfate pages 10-11).
- Thiosulfate was “strongly positively correlated with pH (p < 0.0001, r = 0.80)” (twible2024phandthiosulfate pages 10-11).
- Total SOB abundance was “negatively correlated with pH (p < 0.01, r = −0.64)” (twible2024phandthiosulfate pages 10-11).
- tetH (S4I part 2) was rare: found in “5 of 31 Thiobacillus genomes,” implying possible cross‑taxon pathway coupling in situ (twible2024phandthiosulfate pages 5-6).

The same paper provides schematic support for pathway modules and an explicit conceptual model tying them to pH and thiosulfate (twible2024phandthiosulfate media 771cb74e, twible2024phandthiosulfate media 2248cb0f).

#### Terminal electron acceptor (TEA) control: O2 vs nitrate affects acidity yield
Gordon et al. (2024) used **500 L mesocosms** (28 days) with sulfur/nitrate amendments (2.0 mM sulfur substrates; 2.0 mM nitrate) to connect TEA regimes to net acidity outcomes:
- “complete SOx with O2 yields acidity (ΔH+/ΔS = 1), whereas NO3− as TEA yields no net proton production (ΔH+/ΔS = 0)” (gordon2024microbialsulfurpathways pages 1-5).

This provides a practical design principle for remediation: **nitrate-based TEA management** can decouple sulfur oxidation from acid generation, depending on community/pathway state (gordon2024microbialsulfurpathways pages 1-5).

### 4.2 Sulfide-rich natural biofilms and symbioses (ecosystem function)
Sulfide-rich springs and marine symbioses are dominated by sulfur oxidizers that store or cycle sulfur intermediates. Twible et al.’s conceptual model indicates that pathway partitioning by pH and thiosulfate can be broadly relevant beyond mining systems (twible2024phandthiosulfate pages 10-11, twible2024phandthiosulfate media 2248cb0f), while Sudo et al. suggest gene family diversification (soxY expansion) may underpin adaptability across hosts and environments (sudo2024soxygenefamily pages 1-2, sudo2024soxygenefamily pages 15-17).

---

## 5) Candidate nodes for the TraitMech causal graph (grouped by type)

### Pathways / modules
- **Sox sulfur oxidation system** (complete and incomplete variants) (liu2024determinantsofsulfuroxidizinga pages 17-20, twible2024phandthiosulfate pages 1-2)
- **rDSR sulfur oxidation module** (yan2024characterizationofsulfur pages 59-63)
- **S4I / tetrathionate intermediate module** (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate pages 5-6)
- **Cytoplasmic sulfane sulfur oxidation via PDO (GSSH → sulfite)** (rudenko2024mechanismofintracellular pages 1-2)

### Genes / proteins / complexes (examples)
- **Sox components**: SoxAX, SoxYZ, SoxB, SoxCD; alternative SoxL (petushkova2024thecompletegenome pages 19-20)
- **S4I components**: TsdA; TetH (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate pages 5-6)
- **rDSR-associated**: dsr genes (rdsr) (yan2024characterizationofsulfur pages 59-63)
- **Sulfide oxidation entry**: SQR; FccAB (petushkova2024thecompletegenome pages 19-20, rudenko2024mechanismofintracellular pages 1-2)
- **Sulfane sulfur handling**: PDO; sulfur transfer proteins Rhd, DsrE, TusA (rudenko2024mechanismofintracellular pages 12-13)
- **Transport/regulation**: SoxT1A, SoxT1B; SoxR (li2024yeeelikebacterialsoxt pages 1-2, li2024yeeelikebacterialsoxt pages 7-8)
- **Ecology/modifier**: soxY copy-number/divergent paralogs (sudo2024soxygenefamily pages 1-2, sudo2024soxygenefamily pages 8-11)

### Chemicals / electron donors and acceptors
- Electron donors / substrates: sulfide (H2S/HS−), elemental sulfur/sulfane sulfur/polysulfide, thiosulfate, tetrathionate, sulfite (rudenko2024mechanismofintracellular pages 1-2, twible2024phandthiosulfate pages 1-2).
- Products: sulfate; sometimes S0 storage and intermediate pools (twible2024phandthiosulfate pages 1-2, rudenko2024mechanismofintracellular pages 1-2).
- Electron acceptors / drivers: O2, nitrate; and proton yield (acidity) as an outcome variable (gordon2024microbialsulfurpathways pages 1-5).

### Environmental and experimental factors
- **pH** as a major driver of which sulfur oxidation strategy dominates (twible2024phandthiosulfate pages 10-11, twible2024phandthiosulfate pages 1-2).
- **Thiosulfate availability/speciation** as a control variable and monitoring target (twible2024phandthiosulfate pages 9-10, twible2024phandthiosulfate pages 10-11).
- **TEA regime (O2 vs NO3−)** controlling acidity yield (gordon2024microbialsulfurpathways pages 1-5).

---

## 6) Evidence-backed causal edges (curation table)
The following table is designed for direct trait-graph curation work (triples + snippet + grounding suggestions).

| Edge (S-P-O) | Node type(s) | Evidence snippet (short quote) | Reference (DOI, year, URL) | Notes/uncertainty | Suggested ontology grounding (CURIEs where possible) |
|---|---|---|---|---|---|
| sulfide:quinone oxidoreductase (SQR) — oxidizes → sulfide to sulfane sulfur / elemental sulfur / polysulfide | enzyme → chemical process → chemical | “SQR oxidizing sulfide to sulfane sulfur (S0/polysulfide)” (rudenko2024mechanismofintracellular pages 1-2) | 10.3390/ijms252010962 (2024), https://doi.org/10.3390/ijms252010962 | Strong for Beggiatoa model and broadly consistent with sulfur oxidizer literature; product wording varies by taxon (sulfane sulfur, S0, polysulfide). | EC:1.8.5.4; GO:0016652; CHEBI:18421 hydrogen sulfide; CHEBI:15037 sulfane sulfur; CHEBI:26806 polysulfide |
| glutathione persulfide (GSSH) — is substrate of → persulfide dioxygenase (PDO) | chemical → enzyme | “PDO... oxidizes glutathione persulfide (GSSH)” (rudenko2024mechanismofintracellular pages 1-2) | 10.3390/ijms252010962 (2024), https://doi.org/10.3390/ijms252010962 | Strong in Beggiatoa and other PDO-containing systems; GSSH node may remain label-only if no stable CHEBI curie is confirmed during curation. | label-only: glutathione persulfide (GSSH); EC:1.13.11.18 persulfide dioxygenase |
| persulfide dioxygenase (PDO) — produces → sulfite | enzyme → chemical | “GSSH + O2 + H2O → GSH + SO3(2-) + 2H+” (rudenko2024mechanismofintracellular pages 1-2) | 10.3390/ijms252010962 (2024), https://doi.org/10.3390/ijms252010962 | Strong biochemical edge; explicitly oxygen-dependent. | EC:1.13.11.18; CHEBI:18421 hydrogen sulfide; CHEBI:16526 sulfite; CHEBI:15378 H+ |
| sulfite — reacts with → sulfane sulfur to form thiosulfate | chemical → chemical transformation → chemical | “The generated sulfite can react with sulfane sulfur to form thiosulfate” (rudenko2024mechanismofintracellular pages 1-2) | 10.3390/ijms252010962 (2024), https://doi.org/10.3390/ijms252010962 | Supported as non-enzymatic in this context; curate as chemical causation, not gene-encoded step. | CHEBI:16526 sulfite; CHEBI:15037 sulfane sulfur; CHEBI:30087 thiosulfate |
| thiosulfate — is oxidized by → Sox system to sulfate | chemical → pathway/complex → chemical | “thiosulfate... is then oxidized to sulfate via the Sox-system” (rudenko2024mechanismofintracellular pages 1-2) | 10.3390/ijms252010962 (2024), https://doi.org/10.3390/ijms252010962 | Strong as generic Sox trait edge; exact stoichiometry depends on complete vs incomplete Sox. | KEGG:Module label-only Sox sulfur oxidation system; GO:0019419 sulfate oxidation; CHEBI:30087 thiosulfate; CHEBI:16189 sulfate |
| Sox multienzyme complex (SoxXYZABCD) — located in → periplasm | complex/pathway → cellular localization | “the Sox multienzyme complex (SoxXYZABCD) is periplasmic” (liu2024determinantsofsulfuroxidizinga pages 17-20) | 10.1007/s10230-024-01016-x?* / thesis excerpt summarized in evidence (2024); use caution | Useful mechanistic localization, but evidence here comes from a summarized thesis-like source; prefer corroboration before hard curation if possible. | GO:0042597 periplasmic space; label-only: Sox multienzyme complex |
| absence of SoxCD — causes → incomplete Sox pathway with terminal sulfane intermediates / S0 storage | protein absence → pathway state | “Absence of SoxCD yields an incomplete Sox pathway, producing terminal sulfane intermediates that can be stored as S0” (liu2024determinantsofsulfuroxidizinga pages 17-20) | 10.1007/s10230-024-01016-x?* / thesis excerpt summarized in evidence (2024); use caution | Mechanistically central boundary edge; strong conceptually, but source in evidence is secondary/summary. | label-only: SoxCD; CHEBI:15037 sulfane sulfur; CHEBI:24866 elemental sulfur |
| rDSR genes — enable → oxidation of reduced sulfur species | gene set/pathway → biological process | “rdsr genes... operate in the reverse direction by oxidizing reduced sulfur species” (yan2024characterizationofsulfur pages 59-63) | 10.1093/ismejo/wrae110 (2024), https://doi.org/10.1093/ismejo/wrae110 | Strong for rDSR role in sulfur oxidation. | label-only: rDsr pathway; GO:0000103 sulfate assimilation? (not appropriate)—prefer label-only; dsrAB/dsrC/dsrMKJOP label-only |
| complete sox-dominant sulfur oxidizers — drive → acidity generation | pathway-bearing taxa → environmental outcome | “csox dominant SOB... drove acidity generation” (twible2024phandthiosulfate pages 1-2) | 10.3389/fmicb.2024.1426584 (2024), https://doi.org/10.3389/fmicb.2024.1426584 | Strong ecological edge from field data; applies to tailings impoundments under primarily oxic conditions. | label-only: complete Sox pathway; ENVO:00002274 mine tailings? / label-only: tailings impoundment water; PATO/label-only: acidity generation |
| lower pH (~5 to ~6.5) — favors → complete-sox dominant SOB | environmental factor → taxon/pathway preference | “csox dominant taxa... drove acidity generation... at lower pH (~5 to ~6.5)” (twible2024phandthiosulfate pages 1-2) | 10.3389/fmicb.2024.1426584 (2024), https://doi.org/10.3389/fmicb.2024.1426584 | Strong field association; environmental selection edge rather than direct biochemical causation. | label-only: low pH; label-only: complete Sox-dominant sulfur oxidizers |
| circumneutral pH (~6.5 to ~8.5) — favors → non-csox sulfur oxidizers with incomplete sox / rDSR | environmental factor → pathway preference | “non-csox taxa... hosting incomplete sox, rDSR... at circumneutral pH (~6.5 to ~8.5)” (twible2024phandthiosulfate pages 1-2) | 10.3389/fmicb.2024.1426584 (2024), https://doi.org/10.3389/fmicb.2024.1426584 | Strong field association. | label-only: circumneutral pH; label-only: incomplete Sox pathway; label-only: rDSR pathway |
| thiosulfate concentration — positively correlates with → pH | chemical abundance → environmental variable | “Thiosulfate... was strongly positively correlated with pH (p < 0.0001, r = 0.80)” (twible2024phandthiosulfate pages 10-11) | 10.3389/fmicb.2024.1426584 (2024), https://doi.org/10.3389/fmicb.2024.1426584 | Not a mechanistic gene edge but useful environment node relationship for graph context. | CHEBI:30087 thiosulfate; label-only: pH |
| total sulfur-oxidizing bacteria abundance — negatively correlates with → pH | community abundance → environmental variable | “total SOB abundance was negatively correlated with pH (p < 0.01, r = -0.64)” (twible2024phandthiosulfate pages 10-11) | 10.3389/fmicb.2024.1426584 (2024), https://doi.org/10.3389/fmicb.2024.1426584 | Community-level statistical edge; useful but not pathway-specific. | label-only: sulfur-oxidizing bacteria; label-only: pH |
| tsdA — oxidizes → thiosulfate to tetrathionate | enzyme → chemical transformation | “ts dA (S2O32- to S4O62-)” (twible2024phandthiosulfate pages 1-2) | 10.3389/fmicb.2024.1426584 (2024), https://doi.org/10.3389/fmicb.2024.1426584 | Strong for S4I part 1. | label-only: TsdA/thiosulfate dehydrogenase; EC:1.8.2.2; CHEBI:30087 thiosulfate; CHEBI:30926 tetrathionate |
| tetH — disproportionates / hydrolyzes → tetrathionate to sulfur-containing products | enzyme → chemical transformation | “tetrathionate generated by tsdA can be disproportionated by tetH to yield elemental sulfur (S0), thiosulfate (S2O32-), and sulfate (SO42-)” (twible2024phandthiosulfate pages 5-6) | 10.3389/fmicb.2024.1426584 (2024), https://doi.org/10.3389/fmicb.2024.1426584 | Product wording differs across sources; Kanao review emphasizes hydrolysis. Curate with note that mechanism/product balance is pH- and taxon-dependent. | label-only: TetH/tetrathionate hydrolase; EC:3.12.1.1; CHEBI:30926 tetrathionate; CHEBI:24866 elemental sulfur; CHEBI:30087 thiosulfate; CHEBI:16189 sulfate |
| tetH occurrence in Thiobacillus genomes — supports → completion of S4I pathway under circumneutral pH | gene occurrence → pathway capacity | “tetH was rare (found in 5 of 31 Thiobacillus genomes)” (twible2024phandthiosulfate pages 5-6) | 10.3389/fmicb.2024.1426584 (2024), https://doi.org/10.3389/fmicb.2024.1426584 | Quantitative genomics evidence; taxon-specific and should be marked uncertain for broad trait graph. | NCBITaxon:Thiobacillus (genus-level label); label-only: tetH |
| oxygen as terminal electron acceptor — with complete SOx yields → acidity (ΔH+/ΔS = 1) | electron acceptor → environmental outcome | “complete SOx with O2 yields acidity (ΔH+/ΔS = 1)” (gordon2024microbialsulfurpathways pages 1-5) | 10.1007/s10230-024-01016-x (2024), https://doi.org/10.1007/s10230-024-01016-x | Strong system-level stoichiometric edge from mesocosm interpretation. | CHEBI:15379 dioxygen; label-only: complete SOx; label-only: acidity generation |
| nitrate as terminal electron acceptor — with complete SOx yields → no net proton production | electron acceptor → environmental outcome | “whereas NO3- as TEA yields no net proton production (ΔH+/ΔS = 0)” (gordon2024microbialsulfurpathways pages 1-5) | 10.1007/s10230-024-01016-x (2024), https://doi.org/10.1007/s10230-024-01016-x | Strong and practically important for bioremediation models. | CHEBI:17632 nitrate; label-only: complete SOx; label-only: no net proton production |
| anoxic conditions / low oxygen — favor → incomplete SOx + rDSR pathway | environmental factor → pathway preference | “anoxic conditions... favor the incomplete SOx + rDSR pathway” (gordon2024microbialsulfurpathways pages 5-8) | 10.1007/s10230-024-01016-x (2024), https://doi.org/10.1007/s10230-024-01016-x | Strong mesocosm inference; pathway preference may vary by system. | ENVO:01000379 anoxic water? / label-only: anoxic conditions; label-only: incomplete SOx + rDSR |
| oxygen availability — favors → complete SOx pathway | environmental factor → pathway preference | “Oxygen availability strongly favors the complete SOx pathway” (gordon2024microbialsulfurpathways pages 5-8) | 10.1007/s10230-024-01016-x (2024), https://doi.org/10.1007/s10230-024-01016-x | Strong mesocosm inference. | CHEBI:15379 dioxygen; label-only: complete SOx pathway |
| SoxT1A — required for → sulfur import into cytoplasm for further oxidation | transporter → process | “SoxT1A delivers sulfur to the cytoplasm for its further oxidation” (li2024yeeelikebacterialsoxt pages 1-2) | 10.1038/s42003-024-07270-7 (2024), https://doi.org/10.1038/s42003-024-07270-7 | Strong but taxon-specific (Hyphomicrobium denitrificans). Good candidate causal edge with uncertainty note. | label-only: SoxT1A (YeeE-like transporter); GO:0006810 transport; GO:0005737 cytoplasm |
| loss of SoxT1A — causes → thiosulfate oxidation-negative phenotype | genotype perturbation → phenotype | “all SoxT1A-deficient strains are unable to oxidize thiosulfate” (li2024yeeelikebacterialsoxt pages 7-8) | 10.1038/s42003-024-07270-7 (2024), https://doi.org/10.1038/s42003-024-07270-7 | Very strong mutant evidence; taxon-specific. | label-only: SoxT1A deficiency; CHEBI:30087 thiosulfate; label-only: sulfur oxidation-negative phenotype |
| SoxT1B — mediates → signal transduction to SoxR repressor | transporter/regulatory module → regulation | “SoxT1B serves as a signal transduction unit for the transcriptional repressor SoxR” (li2024yeeelikebacterialsoxt pages 7-8) | 10.1038/s42003-024-07270-7 (2024), https://doi.org/10.1038/s42003-024-07270-7 | Strong in H. denitrificans; not yet generalizable to all sulfur oxidizers. | label-only: SoxT1B; label-only: SoxR; GO:0007165 signal transduction |
| deletion of soxT1B — abolishes → thiosulfate oxidation | genotype perturbation → phenotype | “an in-frame deletion of soxT1B... abolishes thiosulfate oxidation” (li2024yeeelikebacterialsoxt pages 5-7) | 10.1038/s42003-024-07270-7 (2024), https://doi.org/10.1038/s42003-024-07270-7 | Strong mutant evidence; taxon-specific. | label-only: soxT1B deletion; CHEBI:30087 thiosulfate; label-only: thiosulfate oxidation |
| SoxR — represses → sulfur oxidation gene transcription in sulfur absence | transcriptional regulator → biological process | “SoxR itself binds the sox promoter-operator to prevent transcription when sulfur is absent” (li2024yeeelikebacterialsoxt pages 1-2) | 10.1038/s42003-024-07270-7 (2024), https://doi.org/10.1038/s42003-024-07270-7 | Strong regulatory edge in one alphaproteobacterial model. | label-only: SoxR; GO:0006355 regulation of transcription, DNA-templated |
| thiosulfate addition — induces → soxT1A transcription (>10-fold) | chemical signal → gene expression | “soxT1A transcript abundance increased more than tenfold upon thiosulfate addition” (li2024yeeelikebacterialsoxt pages 2-3) | 10.1038/s42003-024-07270-7 (2024), https://doi.org/10.1038/s42003-024-07270-7 | Strong quantitative expression edge; species-specific. | CHEBI:30087 thiosulfate; label-only: soxT1A transcription |
| multiple divergent soxY copies — associated with → generalist host/environment range | gene family architecture → ecological strategy | “symbionts possessing multiple divergent soxY genes are associated with broader, versatile host and environmental ranges” (sudo2024soxygenefamily pages 1-2) | 10.1128/msystems.01135-23 (2024), https://doi.org/10.1128/msystems.01135-23 | Comparative-genomics association, not direct mechanistic proof; useful as higher-level trait modifier, not core biochemical edge. | label-only: soxY gene family expansion; label-only: generalist sulfur oxidizer ecology |
| canonical-only soxY repertoire — associated with → specialist ecology | gene family architecture → ecological strategy | “symbionts with only the ‘canonical’ soxY tend to be ecological ‘specialists’” (sudo2024soxygenefamily pages 1-2) | 10.1128/msystems.01135-23 (2024), https://doi.org/10.1128/msystems.01135-23 | Comparative-genomics association; likely too distal for initial TraitMech graph unless ecological breadth is modeled. | label-only: canonical SoxY; label-only: specialist ecology |
| Thiocapsa bogorovii encodes SoxA/X/B/Y/Z and lacks SoxCD — supports → Sox-mediated thiosulfate oxidation without canonical SoxCD | genome content → pathway capacity | “T. bogorovii encodes canonical Sox proteins... and SoxL is present as an alternative to SoxCD, while SoxCD genes are absent” (petushkova2024thecompletegenome pages 19-20) | 10.3390/microorganisms12020391 (2024), https://doi.org/10.3390/microorganisms12020391 | Strong genomic evidence but species-specific and partly inferential for function of SoxL. | NCBITaxon:label-only Thiocapsa bogorovii; label-only: SoxL; label-only: SoxCD |
| SQR genes in Thiocapsa bogorovii — support → sulfide oxidation to polysulfide | gene/enzyme → chemical transformation | “SQRs are single-subunit flavoproteins bound to the cytoplasmic membrane and produce polysulfide as a primary product” (petushkova2024thecompletegenome pages 19-20) | 10.3390/microorganisms12020391 (2024), https://doi.org/10.3390/microorganisms12020391 | Strong mechanistic description, species genome context provided. | EC:1.8.5.4; CHEBI:18421 hydrogen sulfide; CHEBI:26806 polysulfide |
| genes for CBB cycle, rDSR, Sox, fccA, sqrA — co-express with → sulfide oxidation regime in vent symbionts | gene modules → metabolic state | “The genes for the CBB cycle, reverse dissimilatory sulfate reductase system (rDSR), sulfur oxidizing system (Sox) and periplasmic sulfide oxidation (such as fccA and sqrA) grouped” (yan2024characterizationofsulfur pages 59-63) | 10.1038/s41564-024-01704-y (2024), https://doi.org/10.1038/s41564-024-01704-y | Supportive systems-level edge, but snippet is less explicit than others; use cautiously. | label-only: CBB cycle; label-only: rDSR; label-only: Sox; label-only: fccA; label-only: sqrA |
| sulfide oxidation — allied with → Calvin-Benson-Bassham cycle expression | process → process association | “the CBB is allied to sulfide oxidation” (from abstract summary in paper-search result; not direct context id)—avoid hard curation | 10.1038/s41564-024-01704-y (2024), https://doi.org/10.1038/s41564-024-01704-y | Weak for TraitMech here because direct gathered-evidence quote is limited; better left as warning/not yet curated. | label-only: sulfide oxidation; GO/KEGG for CBB cycle if later confirmed |
| Figure-based support: complete Sox / S4I / incomplete Sox / rDSR modules — are partitioned by → pH and thiosulfate concentration | pathway modules → environmental control | “Figure 5... links these pathways... to their environmental controls, showing how they are partitioned by pH and thiosulfate” (twible2024phandthiosulfate media 771cb74e) | 10.3389/fmicb.2024.1426584 (2024), https://doi.org/10.3389/fmicb.2024.1426584 | Useful as figure-level corroboration for environmental-control edges; not a primary mechanistic quote. | label-only: complete Sox; label-only: S4I; label-only: incomplete Sox; label-only: rDSR; label-only: pH; CHEBI:30087 thiosulfate |


*Table: This table lists evidence-backed candidate causal edges for a TraitMech sulfur oxidation graph, spanning biochemical steps, transport/regulation, and environmental controls. It is designed to help prioritize which nodes and relations are strong enough for curation and which should remain taxon-specific or tentative.*

---

## 7) Warnings / claims not yet suitable for hard curation
- **Generalization of SoxT import/regulation**: SoxT1A/B and SoxR roles are strongly evidenced in Hyphomicrobium denitrificans, but SoxT is not universal; treat as taxon-conditional edges unless additional broad evidence is added (li2024yeeelikebacterialsoxt pages 2-3, li2024yeeelikebacterialsoxt pages 7-8).
- **Periplasmic localization and complete Sox mechanistic steps**: some localization/mechanistic statements appear in secondary or “unknown journal” sources; prefer corroboration from peer‑reviewed reviews or primary studies before treating as definitive in the core TraitMech graph (liu2024determinantsofsulfuroxidizinga pages 17-20, liu2024determinantsofsulfuroxidizing pages 17-20).
- **Ecological “generalist vs specialist” inference from soxY**: strong comparative association but not direct biochemical causation; include only if TraitMech graph models ecological breadth explicitly (sudo2024soxygenefamily pages 1-2, sudo2024soxygenefamily pages 15-17).

---

## 8) Figure evidence (visual support)
Twible et al. (2024) provide: (i) a pathway schematic summarizing Sox/rDSR/S4I modules and (ii) a conceptual model linking pathway dominance to pH and thiosulfate; these were retrieved as cropped images for curation support (twible2024phandthiosulfate media 771cb74e, twible2024phandthiosulfate media 2248cb0f).

---

## 9) DOI-first bibliography (with dates and URLs where available)

1. **Twible, L.E. et al.** (Jul 2024). *pH and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments.* Frontiers in Microbiology 15. DOI: **10.3389/fmicb.2024.1426584**. https://doi.org/10.3389/fmicb.2024.1426584 (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate pages 10-11, twible2024phandthiosulfate pages 5-6, twible2024phandthiosulfate media 771cb74e)
2. **Gordon, J. et al.** (Nov 2024). *Microbial Sulfur Pathways and Outcomes in Tailings Impoundments: A Mesocosm Study.* Mine Water and the Environment 43:658–674. DOI: **10.1007/s10230-024-01016-x**. https://doi.org/10.1007/s10230-024-01016-x (gordon2024microbialsulfurpathways pages 1-5, gordon2024microbialsulfurpathways pages 5-8)
3. **Li, J. et al.** (Nov 2024). *YeeE-like bacterial SoxT proteins mediate sulfur import for oxidation and signal transduction.* Communications Biology 7. DOI: **10.1038/s42003-024-07270-7**. https://doi.org/10.1038/s42003-024-07270-7 (li2024yeeelikebacterialsoxt pages 1-2, li2024yeeelikebacterialsoxt pages 7-8, li2024yeeelikebacterialsoxt pages 5-7, li2024yeeelikebacterialsoxt pages 2-3)
4. **Sudo, M. et al.** (Jun 2024). *soxY gene family expansion underpins adaptation to diverse hosts and environments in symbiotic sulfide oxidizers.* mSystems 9. DOI: **10.1128/msystems.01135-23**. https://doi.org/10.1128/msystems.01135-23 (sudo2024soxygenefamily pages 1-2, sudo2024soxygenefamily pages 4-6, sudo2024soxygenefamily pages 8-11)
5. **Rudenko, T.S. et al.** (Oct 2024). *Mechanism of Intracellular Elemental Sulfur Oxidation in Beggiatoa leptomitoformis, Where Persulfide Dioxygenase Plays a Key Role.* Int. J. Mol. Sci. 25:10962. DOI: **10.3390/ijms252010962**. https://doi.org/10.3390/ijms252010962 (rudenko2024mechanismofintracellular pages 1-2, rudenko2024mechanismofintracellular pages 12-13)
6. **Petushkova, E. et al.** (Feb 2024). *The Complete Genome of a Novel Typical Species Thiocapsa bogorovii and Analysis of Its Central Metabolic Pathways.* Microorganisms 12:391. DOI: **10.3390/microorganisms12020391**. https://doi.org/10.3390/microorganisms12020391 (petushkova2024thecompletegenome pages 19-20)
7. **Sun, X. et al.** (Jan 2024). *Microbially mediated sulfur oxidation coupled with arsenate reduction within oligotrophic mining–impacted habitats.* ISME Journal 18. DOI: **10.1093/ismejo/wrae110**. https://doi.org/10.1093/ismejo/wrae110 (yan2024characterizationofsulfur pages 59-63)

(Additional contextual/secondary sources were present in evidence but lacked clear bibliographic metadata in the retrieved text; they are therefore not promoted to primary bibliography items.)


References

1. (twible2024phandthiosulfate pages 1-2): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

2. (rudenko2024mechanismofintracellular pages 1-2): Tatyana S. Rudenko, Liubov I. Trubitsina, Vasily V. Terentyev, Ivan V. Trubitsin, Valentin I. Borshchevskiy, Svetlana V. Tishchenko, Azat G. Gabdulkhakov, Alexey A. Leontievsky, and Margarita Yu. Grabovich. Mechanism of intracellular elemental sulfur oxidation in beggiatoa leptomitoformis, where persulfide dioxygenase plays a key role. International Journal of Molecular Sciences, 25:10962, Oct 2024. URL: https://doi.org/10.3390/ijms252010962, doi:10.3390/ijms252010962. This article has 6 citations.

3. (yan2024characterizationofsulfur pages 59-63): Y Yan. Characterization of sulfur cycling in the first oil sands pilot end pit lake, base mine lake. Unknown journal, 2024.

4. (liu2024determinantsofsulfuroxidizinga pages 17-20): FYL Liu. Determinants of sulfur-oxidizing bacteria and water quality outcomes in metal mining wastewaters. Unknown journal, 2024.

5. (gordon2024microbialsulfurpathways pages 1-5): Jay Gordon, Simon C. Apte, Tara E. Colenbrander Nelson, Kelly J. Whaley-Martin, Lauren E. Twible, LinXing Chen, Felicia Liu, Samantha McGarry, Jillian F. Banfield, and Lesley A. Warren. Microbial sulfur pathways and outcomes in tailings impoundments: a mesocosm study. Mine Water and the Environment, 43:658-674, Nov 2024. URL: https://doi.org/10.1007/s10230-024-01016-x, doi:10.1007/s10230-024-01016-x. This article has 3 citations and is from a peer-reviewed journal.

6. (gordon2024microbialsulfurpathways pages 5-8): Jay Gordon, Simon C. Apte, Tara E. Colenbrander Nelson, Kelly J. Whaley-Martin, Lauren E. Twible, LinXing Chen, Felicia Liu, Samantha McGarry, Jillian F. Banfield, and Lesley A. Warren. Microbial sulfur pathways and outcomes in tailings impoundments: a mesocosm study. Mine Water and the Environment, 43:658-674, Nov 2024. URL: https://doi.org/10.1007/s10230-024-01016-x, doi:10.1007/s10230-024-01016-x. This article has 3 citations and is from a peer-reviewed journal.

7. (petushkova2024thecompletegenome pages 19-20): Ekaterina Petushkova, Makhmadyusuf Khasimov, Ekaterina Mayorova, Yanina Delegan, Ekaterina Frantsuzova, Alexander Bogun, Elena Galkina, and Anatoly Tsygankov. The complete genome of a novel typical species thiocapsa bogorovii and analysis of its central metabolic pathways. Microorganisms, 12:391, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020391, doi:10.3390/microorganisms12020391. This article has 6 citations.

8. (twible2024phandthiosulfate pages 5-6): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

9. (rudenko2024mechanismofintracellular pages 12-13): Tatyana S. Rudenko, Liubov I. Trubitsina, Vasily V. Terentyev, Ivan V. Trubitsin, Valentin I. Borshchevskiy, Svetlana V. Tishchenko, Azat G. Gabdulkhakov, Alexey A. Leontievsky, and Margarita Yu. Grabovich. Mechanism of intracellular elemental sulfur oxidation in beggiatoa leptomitoformis, where persulfide dioxygenase plays a key role. International Journal of Molecular Sciences, 25:10962, Oct 2024. URL: https://doi.org/10.3390/ijms252010962, doi:10.3390/ijms252010962. This article has 6 citations.

10. (li2024yeeelikebacterialsoxt pages 1-2): Jingjing Li, Fabienne Göbel, Hsun Yun Hsu, Julian Nikolaus Koch, Natalie Hager, Wanda Antonia Flegler, Tomohisa Sebastian Tanabe, and Christiane Dahl. Yeee-like bacterial soxt proteins mediate sulfur import for oxidation and signal transduction. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07270-7, doi:10.1038/s42003-024-07270-7. This article has 7 citations and is from a peer-reviewed journal.

11. (li2024yeeelikebacterialsoxt pages 7-8): Jingjing Li, Fabienne Göbel, Hsun Yun Hsu, Julian Nikolaus Koch, Natalie Hager, Wanda Antonia Flegler, Tomohisa Sebastian Tanabe, and Christiane Dahl. Yeee-like bacterial soxt proteins mediate sulfur import for oxidation and signal transduction. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07270-7, doi:10.1038/s42003-024-07270-7. This article has 7 citations and is from a peer-reviewed journal.

12. (li2024yeeelikebacterialsoxt pages 5-7): Jingjing Li, Fabienne Göbel, Hsun Yun Hsu, Julian Nikolaus Koch, Natalie Hager, Wanda Antonia Flegler, Tomohisa Sebastian Tanabe, and Christiane Dahl. Yeee-like bacterial soxt proteins mediate sulfur import for oxidation and signal transduction. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07270-7, doi:10.1038/s42003-024-07270-7. This article has 7 citations and is from a peer-reviewed journal.

13. (li2024yeeelikebacterialsoxt pages 2-3): Jingjing Li, Fabienne Göbel, Hsun Yun Hsu, Julian Nikolaus Koch, Natalie Hager, Wanda Antonia Flegler, Tomohisa Sebastian Tanabe, and Christiane Dahl. Yeee-like bacterial soxt proteins mediate sulfur import for oxidation and signal transduction. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07270-7, doi:10.1038/s42003-024-07270-7. This article has 7 citations and is from a peer-reviewed journal.

14. (sudo2024soxygenefamily pages 1-2): Marta Sudo, Jay Osvatic, John D. Taylor, Suzanne C. Dufour, Anchana Prathep, Laetitia G. E. Wilkins, Thomas Rattei, Benedict Yuen, and Jillian M. Petersen. <i>soxy</i> gene family expansion underpins adaptation to diverse hosts and environments in symbiotic sulfide oxidizers. mSystems, Jun 2024. URL: https://doi.org/10.1128/msystems.01135-23, doi:10.1128/msystems.01135-23. This article has 16 citations and is from a peer-reviewed journal.

15. (sudo2024soxygenefamily pages 4-6): Marta Sudo, Jay Osvatic, John D. Taylor, Suzanne C. Dufour, Anchana Prathep, Laetitia G. E. Wilkins, Thomas Rattei, Benedict Yuen, and Jillian M. Petersen. <i>soxy</i> gene family expansion underpins adaptation to diverse hosts and environments in symbiotic sulfide oxidizers. mSystems, Jun 2024. URL: https://doi.org/10.1128/msystems.01135-23, doi:10.1128/msystems.01135-23. This article has 16 citations and is from a peer-reviewed journal.

16. (sudo2024soxygenefamily pages 8-11): Marta Sudo, Jay Osvatic, John D. Taylor, Suzanne C. Dufour, Anchana Prathep, Laetitia G. E. Wilkins, Thomas Rattei, Benedict Yuen, and Jillian M. Petersen. <i>soxy</i> gene family expansion underpins adaptation to diverse hosts and environments in symbiotic sulfide oxidizers. mSystems, Jun 2024. URL: https://doi.org/10.1128/msystems.01135-23, doi:10.1128/msystems.01135-23. This article has 16 citations and is from a peer-reviewed journal.

17. (sudo2024soxygenefamily pages 15-17): Marta Sudo, Jay Osvatic, John D. Taylor, Suzanne C. Dufour, Anchana Prathep, Laetitia G. E. Wilkins, Thomas Rattei, Benedict Yuen, and Jillian M. Petersen. <i>soxy</i> gene family expansion underpins adaptation to diverse hosts and environments in symbiotic sulfide oxidizers. mSystems, Jun 2024. URL: https://doi.org/10.1128/msystems.01135-23, doi:10.1128/msystems.01135-23. This article has 16 citations and is from a peer-reviewed journal.

18. (twible2024phandthiosulfate pages 10-11): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

19. (twible2024phandthiosulfate media 771cb74e): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

20. (twible2024phandthiosulfate media 2248cb0f): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

21. (twible2024phandthiosulfate pages 9-10): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

22. (liu2024determinantsofsulfuroxidizing pages 17-20): FYL Liu. Determinants of sulfur-oxidizing bacteria and water quality outcomes in metal mining wastewaters. Unknown journal, 2024.