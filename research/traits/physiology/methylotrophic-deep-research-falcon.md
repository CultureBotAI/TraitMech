---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:45:40.946491'
end_time: '2026-06-18T12:16:03.074915'
duration_seconds: 1822.13
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: methylotrophic
  trait_identifier: METPO:1000651
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: methylotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy and carbon from reduced
    one-carbon compounds.
  parent_traits: METPO:1000631
  synonyms: TT_methylotroph, methylotroph, methylotrophy
  evidence_summary: 'DOI:10.3389/fbioe.2021.787791: methanol utilization in methylotrophy
    (Review supports methanol oxidation and formaldehyde assimilation as central methylotrophy
    mechanisms.)'
  causal_graph_summary: 'methylotrophic_methanol_assimilation: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 73
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** methylotrophic
- **METPO identifier:** METPO:1000651
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy and carbon from reduced one-carbon compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_methylotroph, methylotroph, methylotrophy
- **Existing evidence:** DOI:10.3389/fbioe.2021.787791: methanol utilization in methylotrophy (Review supports methanol oxidation and formaldehyde assimilation as central methylotrophy mechanisms.)
- **Existing causal graph summary:** methylotrophic_methanol_assimilation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **methylotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/methylotrophic.yaml`.

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
- **Trait label:** methylotrophic
- **METPO identifier:** METPO:1000651
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy and carbon from reduced one-carbon compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_methylotroph, methylotroph, methylotrophy
- **Existing evidence:** DOI:10.3389/fbioe.2021.787791: methanol utilization in methylotrophy (Review supports methanol oxidation and formaldehyde assimilation as central methylotrophy mechanisms.)
- **Existing causal graph summary:** methylotrophic_methanol_assimilation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **methylotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/methylotrophic.yaml`.

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


## Research report: Microbial trait **methylotrophic** (METPO:1000651) — TraitMech causal-graph curation

### 0. Scope summary (TraitMech-ready)
The trait **methylotrophic** denotes an organism’s physiological capacity to obtain energy and carbon from **reduced one‑carbon (C1) compounds**. In recent literature, methylotrophs are described as organisms able to use reduced C1 substrates (e.g., **methanol, formaldehyde, formate**, and in some definitions **methane**) as their carbon/energy sources, deriving energy by oxidizing C1 substrates through specific dehydrogenases. (samanta2024fromgenometo pages 18-20)

**Formaldehyde is a central metabolic intermediate** connecting C1 oxidation to assimilation and/or complete oxidation in both methylotrophs and methanotrophs. (ahmadi2024recentfindingsin pages 1-2, schmider2024physiologicalbasisfor pages 6-7)

**Boundary cases / nearby traits**
- **Methanotrophic** is a *subset* of methylotrophic: methanotrophs oxidize **methane** using methane monooxygenases (sMMO/pMMO) to produce methanol, then route methanol/formaldehyde through methylotrophy modules. (samanta2024fromgenometo pages 16-18, ahmadi2024recentfindingsin pages 1-2)
- **C1-trophic** is a broader framing used in circular-carbon literature that includes organisms growing on CO2, formate, methanol, methane, CO, etc.; “methylotrophy” is often used for the reduced C1 organics portion of that space. (orsi2023synergisticinvestigationof pages 1-2)
- **Autotrophy** (CO2 fixation alone, e.g., CBB cycle) can be C1-trophy but is not necessarily methylotrophy; conversely, methylotrophy often includes CO2 incorporation (e.g., serine cycle) but is defined by reduced C1 organics as carbon/energy sources. (orsi2023synergisticinvestigationof pages 1-2, samanta2024fromgenometo pages 18-20)

### 1. Key concepts and current understanding (mechanistic)
#### 1.1 Canonical biochemical architecture
A widely used mechanistic decomposition of methylotrophy is:
1) **C1 substrate oxidation** (e.g., methanol → formaldehyde via methanol dehydrogenase) (samanta2024fromgenometo pages 18-20)
2) **Formaldehyde handling** (assimilation and/or detox/oxidation) (schmider2024physiologicalbasisfor pages 6-7)
3) **Downstream assimilation into central metabolism** (serine cycle, RuMP/XuMP, etc.) (mitic2023theoxygentolerantreductive pages 1-2)

A pathway overview figure that explicitly juxtaposes **XuMP, RuMP, serine cycle, and reductive glycine pathway variants** for methanol/formate assimilation is available from Mitic et al. 2023 (Fig. 1). (mitic2023theoxygentolerantreductive media c3651b92)

#### 1.2 Core assimilation pathways (natural and engineered)
- **RuMP pathway (bacteria):** formaldehyde fixation depends on hallmark enzymes **Hps** and **Phi**. (mitic2023theoxygentolerantreductive pages 1-2)
- **XuMP pathway (methylotrophic yeasts):** described as the main yeast methanol assimilation route; **Das1/Das2** are hallmark assimilation enzymes. (mitic2023theoxygentolerantreductive pages 1-2)
- **Serine cycle (many type II methylotrophs and methanotrophs):** formaldehyde is assimilated primarily through the serine cycle, with strong comparative genomic support for widespread presence of **GlyA/SHMT**, **SGT**, **HPR** across surveyed type II methylotroph genomes. (samanta2024fromgenometo pages 18-20, samanta2024fromgenometo pages 12-14)
- **H4MPT/H4F-linked pathways (formaldehyde oxidation/transfer):** in methanotroph physiology, formaldehyde oxidation proceeds via **H4MPT** intermediates and also involves **H4F/THF** species; these connect detox/oxidation to central metabolism. (schmider2024physiologicalbasisfor pages 6-7)
- **Reductive glycine pathway (rGlyP):** prominent in C1-trophy engineering and highlighted as an assimilation option in the circular-carbon framing and in pathway comparisons. (orsi2023synergisticinvestigationof pages 1-2, mitic2023theoxygentolerantreductive pages 1-2)

#### 1.3 Methanol oxidation enzymes and the lanthanide paradigm
Methanol oxidation is frequently catalyzed by **PQQ-dependent alcohol dehydrogenase family enzymes**, including two major MDH types:
- **Mxa-type MDH (classical):** calcium-dependent. (gorniak2024changesingrowth pages 1-2)
- **XoxF-type MDH:** lanthanide-dependent and associated with broad ecological distribution. (gorniak2024changesingrowth pages 1-2, voutsinos2024weatheredgranitesand pages 1-2)

A key regulatory/eco-physiological concept is the **“lanthanide switch”**, i.e., lanthanide availability driving inverse regulation of Ca-dependent vs Ln-dependent PQQ-ADHs/MDHs (demonstrated clearly in a model regulatory system using PedE/PedH and PedS2R2). (gorniak2024changesingrowth pages 1-2)

### 2. Recent developments and latest research (prioritizing 2023–2024)
#### 2.1 Expanding ecological breadth of lanthanide-dependent methylotrophy (2024)
A 2024 BMC Biology study of weathered granite/soil microbiomes reported that **xoxF-containing gene clusters (primarily xoxF3 and xoxF5)** are common in moderately weathered granite, with **no MxaF homologs detected** at the studied site; XoxF systems span multiple phyla and appear embedded in conserved gene clusters with partners (e.g., **xoxJ, xoxG**) and transport/metal-related genes. (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 4-7, voutsinos2024weatheredgranitesand pages 2-4)

This work also links methylotrophy-related lanthanide use to **granite weathering**: candidate **metallophore** biosynthetic systems are prevalent where lanthanide phosphate minerals dissolve, and the authors argue that phosphate mineral dissolution, metallophore production, and lanthanide-dependent methanol oxidation (linked to carbonic acid production) co-occur in the zone of moderate granite weathering. (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 12-14)

#### 2.2 Quantitative comparative genomics of type II methylotrophs (2024)
A 2024 mSystems pangenome analysis of 75 type II methylotrophs reported:
- **GlyA/SHMT present in 74/75 genomes**; **SGT and HPR present in all 75**, supporting serine-cycle centrality. (samanta2024fromgenometo pages 12-14)
- **Formaldehyde dehydrogenase (FDH) relatively rare** (present in only 10 organisms), warning against treating FDH as a universal methylotrophy marker. (samanta2024fromgenometo pages 12-14)

#### 2.3 Native pathway versatility in methylotrophic yeast (2023–2024)
In Komagataella phaffii, Mitic et al. (2023) reported discovery/confirmation of an **oxygen-tolerant reductive glycine pathway** that can assimilate methanol, formate and CO2, in addition to canonical formaldehyde-fixation routes. (mitic2023theoxygentolerantreductive pages 1-2)

### 3. Current applications and real-world implementations
#### 3.1 Circular-carbon biomanufacturing framing
A 2023 Nature Communications perspective frames **C1-trophic microorganisms** (including methylotrophs) as a foundation for converting **CO2/formate/methanol/methane/CO** into value-added products, emphasizing synergy between optimizing natural C1-trophs and engineering synthetic C1 assimilation into model organisms. (orsi2023synergisticinvestigationof pages 1-2, orsi2023synergisticinvestigationof pages 2-4)

#### 3.2 Plant-associated methylotrophy and agricultural outcomes
A 2024 Nature Communications study evolved Methylorubrum extorquens under low-methanol conditions and identified a mutation acting as a **“metabolic valve”** that redirects limited C1 resources toward biomass, yielding strains with **superior phyllosphere colonization** and improved plant growth. (zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2)

#### 3.3 Tools enabling methylotrophy engineering: formaldehyde growth biosensors
A 2024 Microbial Biotechnology paper engineered E. coli **formaldehyde growth biosensors** with a reported detection range of **~30 μM to 13 mM** formaldehyde, enabling high-throughput screening of formaldehyde-producing enzymes such as MDHs. (schann2024designconstructionand pages 1-2)

### 4. Expert opinions and analysis (authoritative sources)
- Circular carbon economy experts emphasize that progress requires combining insights from **natural C1 specialists** with **synthetic pathway reconstruction** in model hosts, but current synthetic C1 strains often have lower growth rates/yields than natural counterparts. (orsi2023synergisticinvestigationof pages 1-2, orsi2023synergisticinvestigationof pages 5-6)
- A 2024 methanotroph review underscores that formaldehyde is central to both catabolism and anabolism in methane-oxidizing methylotrophs, and highlights constraints like electron donor requirements for MMO-driven conversions. (ahmadi2024recentfindingsin pages 1-2, ahmadi2024recentfindingsin pages 7-9)

### 5. Relevant recent statistics and quantitative data
- **Serine-cycle genomic prevalence:** GlyA/SHMT present in **74/75** type II methylotroph genomes; FDH present in **10** organisms (minority). (samanta2024fromgenometo pages 12-14)
- **Formaldehyde biosensor range:** **~30 μM–13 mM** detection. (schann2024designconstructionand pages 1-2)
- **Engineered methanol assimilation via membrane remodeling (2024):** phosphatidylcholine-harboring E. coli consumed **up to 4.7 g/L methanol**, **23×** higher than control (0.2 g/L). (li2024aeukaryotefeaturedmembrane pages 1-2)
- **Methanol production from methane (reviewed 2024):** methanotroph coculture with H2 addition reported methanol production **~0.32 g/L** with **~66% conversion efficiency** (as cited in the review). (ahmadi2024recentfindingsin pages 7-9)

### 6. Candidate nodes for `methylotrophic.yaml`
The following table is a curation-oriented candidate node inventory grouped by entity type and includes ontology grounding suggestions and evidence.

| Node label | Node type | Suggested ontology grounding | Evidence/supporting source(s) | Notes for curation |
|---|---|---|---|---|
| **A. Substrates/electron donors & C1 intermediates** |  |  |  |  |
| methanol | chemical substrate / C1 compound | CHEBI:17790 | (rasmussen2024diverseandunconventional pages 1-2, mitic2023theoxygentolerantreductive pages 1-2, samanta2024fromgenometo pages 18-20, orsi2023synergisticinvestigationof pages 1-2) | Core methylotrophic substrate across natural and synthetic systems. |
| formaldehyde | chemical intermediate | CHEBI:16842 | (rasmussen2024diverseandunconventional pages 1-2, ahmadi2024recentfindingsin pages 1-2, shao2024transcriptomicdatareveals pages 1-2, wu2023engineeringasynthetic pages 1-2) | Central intermediate in catabolism and assimilation; toxicity-handling is often essential. |
| formate | chemical substrate/intermediate | CHEBI:15740 | (mitic2023theoxygentolerantreductive pages 1-2, schann2024theserineshunt pages 1-6, orsi2023synergisticinvestigationof pages 1-2) | Used directly by some C1-trophs and produced during formaldehyde oxidation. |
| methane | chemical substrate | CHEBI:16183 | (rasmussen2024diverseandunconventional pages 1-2, samanta2024fromgenometo pages 16-18, ahmadi2024recentfindingsin pages 1-2, orsi2023synergisticinvestigationof pages 1-2) | Important boundary case: substrate of methanotrophs, a subset of methylotrophs. |
| methylamine | chemical substrate | CHEBI:16836 | (rasmussen2024diverseandunconventional pages 1-2) | Relevant for broader methylotrophy; substrate-specific methyltransferase systems may apply. |
| carbon dioxide | chemical substrate/product | CHEBI:16526 | (mitic2023theoxygentolerantreductive pages 1-2, orsi2023synergisticinvestigationof pages 1-2, orsi2023synergisticinvestigationof pages 4-4) | Often co-assimilated in serine/rGly routes; not sufficient alone to define methylotrophy. |
| glycine | metabolite | CHEBI:15428 | (schmider2024physiologicalbasisfor pages 6-7, schann2024theserineshunt pages 1-6) | Central in serine-cycle/rGly-associated assimilation routes. |
| serine | metabolite | CHEBI:17115 | (samanta2024fromgenometo pages 18-20, shao2024transcriptomicdatareveals pages 2-4, schann2024theserineshunt pages 1-6) | Key assimilation intermediate in serine-cycle methylotrophs. |
| xylulose-5-phosphate | metabolite | CHEBI:16255 | (mitic2023theoxygentolerantreductive pages 1-2, wang2024metabolicengineeringof pages 2-4) | Formaldehyde acceptor in XuMP; taxon-specific to methylotrophic yeasts and engineered systems. |
| ribulose-5-phosphate | metabolite | CHEBI:17363 | (mitic2023theoxygentolerantreductive pages 1-2, wu2023engineeringasynthetic pages 1-2) | Formaldehyde-acceptor context for RuMP. |
| dihydroxyacetone phosphate (DHAP) | metabolite | CHEBI:16001 | (wu2023engineeringasynthetic pages 1-2) | Included because EuMP and XuMP-related engineering evidence depends on it; synthetic/engineered relevance. |
| lanthanide-dependent electron donor context | process context | label-only | (gorniak2024changesingrowth pages 1-2, phi2024assessinglanthanidedependentmethanol pages 21-24) | Not a chemical node per se; indicates methanol oxidation regime when Ln-dependent MDHs are active. |
| **B. Key pathways/modules** |  |  |  |  |
| methylotrophy | trait / physiological capacity | METPO:1000651 | (rasmussen2024diverseandunconventional pages 1-2, orsi2023synergisticinvestigationof pages 1-2, samanta2024fromgenometo pages 18-20) | Root trait; use as class-level node. |
| methanol oxidation | biological process / pathway | GO:0015947 | (gorniak2024changesingrowth pages 1-2, warters2024widespreadbacterialuse pages 9-13, zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2) | Strongly supported as upstream module for many methylotrophs. |
| formaldehyde oxidation | biological process / pathway | label-only | (tarasov2023cytobacilluspseudoceanisediminissp. pages 6-8, shao2024transcriptomicdatareveals pages 1-2, schmider2024physiologicalbasisfor pages 6-7, wang2024metabolicengineeringof pages 2-4) | Common detox/dissimilation branch; ontology grounding may need later refinement. |
| ribulose monophosphate pathway (RuMP) | pathway | MetaCyc:PWY-1861 | (mitic2023theoxygentolerantreductive pages 1-2, shao2024transcriptomicdatareveals pages 1-2, wu2023engineeringasynthetic pages 1-2) | Canonical bacterial formaldehyde assimilation route. |
| xylulose monophosphate pathway (XuMP) | pathway | label-only | (mitic2023theoxygentolerantreductive pages 1-2, wang2024metabolicengineeringof pages 2-4, mitic2023theoxygentolerantreductive media c3651b92) | Canonical yeast formaldehyde assimilation route; label-only unless stable pathway ID chosen during curation. |
| serine cycle | pathway | MetaCyc:SERCYC-PWY | (samanta2024fromgenometo pages 18-20, shao2024transcriptomicdatareveals pages 2-4, samanta2024fromgenometo pages 12-14) | Canonical assimilation route in many type II methylotrophs. |
| tetrahydromethanopterin (H4MPT) pathway | pathway | label-only | (shao2024transcriptomicdatareveals pages 1-2, schmider2024physiologicalbasisfor pages 6-7) | Major formaldehyde oxidation route in many methanotrophs/methylotrophs. |
| tetrahydrofolate (H4F/THF) C1 pathway | pathway | GO:0035999 | (tarasov2023cytobacilluspseudoceanisediminissp. pages 6-8, mitic2023theoxygentolerantreductive pages 1-2, schmider2024physiologicalbasisfor pages 6-7) | Supports formate/formaldehyde-linked one-carbon transfers. |
| reductive glycine pathway (rGlyP) | pathway | label-only | (mitic2023theoxygentolerantreductive pages 1-2, schann2024theserineshunt pages 1-6, orsi2023synergisticinvestigationof pages 1-2) | Native or engineered depending taxon; useful as candidate but often not canonical for natural methylotrophy. |
| erythrulose monophosphate cycle (EuMP) | synthetic pathway | label-only | (wu2023engineeringasynthetic pages 1-2) | Synthetic only; do not curate as native methylotrophy mechanism. |
| glyoxylate cycle | pathway | GO:0006097 | (samanta2024fromgenometo pages 18-20) | Supports acetyl-CoA assimilation in some methylotrophs; secondary to core trait. |
| ethylmalonyl-CoA pathway (EMC) | pathway | label-only | (shao2024transcriptomicdatareveals pages 2-4, samanta2024fromgenometo pages 18-20) | Important in some serine-cycle methylotrophs; may be supportive rather than defining. |
| lanthanide switch | regulatory program / environmental response | label-only | (gorniak2024changesingrowth pages 1-2, phi2024assessinglanthanidedependentmethanol pages 21-24, kamachi2025switchingbetweenmethanol pages 1-2, kamachi2025switchingbetweenmethanol pages 10-10) | Strong mechanistic concept, but wording is regulatory shorthand rather than a single molecular entity. |
| **C. Enzymes/proteins/complexes (include gene symbols)** |  |  |  |  |
| methanol dehydrogenase (MDH) | enzyme | EC:1.1.2.7 | (samanta2024fromgenometo pages 18-20, gorniak2024changesingrowth pages 1-2, warters2024widespreadbacterialuse pages 9-13) | Broad parent node for methanol oxidation; useful umbrella node. |
| MxaFI methanol dehydrogenase (mxaF/mxaI) | enzyme complex | EC:1.1.2.7 | (gorniak2024changesingrowth pages 1-2, phi2024assessinglanthanidedependentmethanol pages 21-24, kamachi2025switchingbetweenmethanol pages 1-2) | Ca2+-dependent classical MDH; not universal. |
| XoxF methanol dehydrogenase (xoxF) | enzyme | EC:1.1.2.7 | (gorniak2024changesingrowth pages 1-2, phi2024assessinglanthanidedependentmethanol pages 21-24, voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 4-7) | Ln-dependent MDH; widespread and often central in environmental methylotrophy. |
| XoxJ | accessory protein | label-only | (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 4-7) | Frequently colocated with xoxF; functional role supportive but not always essential to encode as separate causal node. |
| XoxG | cytochrome c electron acceptor | label-only | (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 17-18) | Accessory electron transfer component in XoxF systems; uncertain breadth across taxa. |
| Hps / 3-hexulose-6-phosphate synthase (hps) | enzyme | EC:4.1.2.43 | (mitic2023theoxygentolerantreductive pages 1-2, zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2) | Hallmark RuMP enzyme; strong node candidate. |
| Phi / phosphohexose isomerase (phi) | enzyme | EC:5.3.1.9 | (mitic2023theoxygentolerantreductive pages 1-2, zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2) | Hallmark RuMP partner enzyme; consider pairing with Hps in pathway edges. |
| GlyA / SHMT / serine hydroxymethyltransferase (glyA) | enzyme | EC:2.1.2.1 | (shao2024transcriptomicdatareveals pages 1-2, schmider2024physiologicalbasisfor pages 6-7, samanta2024fromgenometo pages 12-14) | Central serine-cycle/H4F-linked enzyme; near-universal in surveyed type II methylotrophs. |
| GcvP/GcvT/GcvH glycine cleavage system | enzyme complex | GO:0005960 | (schmider2024physiologicalbasisfor pages 6-7) | Relevant to glycine/serine/rGly-associated C1 metabolism; may be context-dependent. |
| SgaA serine-glyoxylate aminotransferase | enzyme | EC:2.6.1.45 | (schmider2024physiologicalbasisfor pages 6-7, samanta2024fromgenometo pages 12-14) | Strong serine-cycle node candidate. |
| HprA hydroxypyruvate reductase | enzyme | EC:1.1.1.81 | (schmider2024physiologicalbasisfor pages 6-7, samanta2024fromgenometo pages 12-14) | Widespread serine-cycle enzyme. |
| Aox1 / alcohol oxidase 1 (AOX1) | enzyme | EC:1.1.3.13 | (mitic2023theoxygentolerantreductive pages 1-2, wang2024metabolicengineeringof pages 2-4) | Yeast-specific methanol oxidation enzyme; taxon-specific. |
| Das1/Das2 / dihydroxyacetone synthase | enzyme | EC:2.2.1.3 | (mitic2023theoxygentolerantreductive pages 1-2, wang2024metabolicengineeringof pages 2-4) | XuMP hallmark enzyme; especially relevant in Komagataella/Pichia. |
| Fld / formaldehyde dehydrogenase | enzyme | EC:1.2.1.46 | (wang2024metabolicengineeringof pages 2-4) | Yeast detox/dissimilation node; strong but taxon-specific naming. |
| Fgh / S-formylglutathione hydrolase | enzyme | EC:3.1.2.12 | (wang2024metabolicengineeringof pages 2-4) | Part of glutathione-dependent formaldehyde oxidation; taxon-specific evidence here. |
| Fdh / formate dehydrogenase | enzyme | EC:1.17.1.9 | (tarasov2023cytobacilluspseudoceanisediminissp. pages 6-8, schmider2024physiologicalbasisfor pages 6-7, wang2024metabolicengineeringof pages 2-4) | Common downstream oxidation step from formate to CO2. |
| Fae / formaldehyde-activating enzyme | enzyme | label-only | (schmider2024physiologicalbasisfor pages 6-7) | Mentioned in H4MPT context; may be useful but evidence here is indirect/downregulation-focused. |
| FolD | enzyme | EC:1.5.1.5 | (schmider2024physiologicalbasisfor pages 6-7) | THF-linked one-carbon oxidation/transfer node. |
| FchA | enzyme | EC:3.5.4.9 | (schmider2024physiologicalbasisfor pages 6-7) | THF/H4MPT-associated formaldehyde oxidation branch support. |
| MtdA | enzyme | EC:1.5.1.15 | (schmider2024physiologicalbasisfor pages 6-7) | C1 oxidation/transfer node in H4-linked pathways. |
| PedE | PQQ alcohol dehydrogenase | label-only | (gorniak2024changesingrowth pages 1-2) | Non-methylotroph exemplar of Ca-dependent/Ln-responsive ADH regulation; regulatory analogy useful, but not core methylotrophy node. |
| PedH | Ln-dependent PQQ alcohol dehydrogenase | label-only | (gorniak2024changesingrowth pages 1-2) | Same caution as PedE; useful for lanthanide-switch regulation concept. |
| PedS2R2 two-component system | regulatory complex | label-only | (gorniak2024changesingrowth pages 1-2) | Strong support for lanthanide-responsive transcriptional control, but derived from Pseudomonas not canonical methylotroph. Mark uncertain/taxon-specific. |
| LanM / lanmodulin | lanthanide-binding protein | label-only | (phi2024assessinglanthanidedependentmethanol pages 21-24, voutsinos2024weatheredgranitesand pages 16-17, voutsinos2024weatheredgranitesand pages 17-18) | Strongly relevant to lanthanide uptake/handling; not universal across methylotrophs. |
| metallophore / lanthanophore biosynthetic cluster (LCC) | biosynthetic system | label-only | (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 2-4, voutsinos2024weatheredgranitesand pages 12-14) | Environmental acquisition module for lanthanides; inferred from genomics in weathered rock. |
| methane monooxygenase (pMMO/sMMO) | enzyme complex | EC:1.14.18.3 / EC:1.14.13.25 | (rasmussen2024diverseandunconventional pages 1-2, samanta2024fromgenometo pages 16-18, ahmadi2024recentfindingsin pages 1-2) | Boundary node: defines methanotrophy rather than generic methylotrophy. |
| **D. Cofactors/metals** |  |  |  |  |
| pyrroloquinoline quinone (PQQ) | cofactor | CHEBI:26355 | (gorniak2024changesingrowth pages 1-2, phi2024assessinglanthanidedependentmethanol pages 21-24, zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2) | Core cofactor for periplasmic Mxa/XoxF-type MDHs. |
| calcium ion (Ca2+) | metal cofactor | CHEBI:29108 | (gorniak2024changesingrowth pages 1-2, kamachi2025switchingbetweenmethanol pages 1-2, warters2024widespreadbacterialuse pages 9-13) | Canonical MxaFI cofactor. |
| lanthanides (Ln3+) | metal cofactor class | CHEBI:33302 | (gorniak2024changesingrowth pages 1-2, phi2024assessinglanthanidedependentmethanol pages 21-24, tucci2024directmethaneoxidation pages 38-40, voutsinos2024weatheredgranitesand pages 1-2) | Important class-level node for XoxF activity and lanthanide switch. |
| lanthanum(III) | metal ion | CHEBI:33341 | (gorniak2024changesingrowth pages 1-2, warters2024widespreadbacterialuse pages 9-13, warters2024widespreadbacterialuse pages 39-41) | Commonly cited light lanthanide supporting XoxF activity. |
| cerium(III) | metal ion | CHEBI:33348 | (kamachi2025switchingbetweenmethanol pages 1-2, kamachi2025switchingbetweenmethanol pages 10-10, warters2024widespreadbacterialuse pages 9-13) | Frequently used exemplar of lanthanide switch induction. |
| neodymium(III) | metal ion | CHEBI:33358 | (tucci2024directmethaneoxidation pages 38-40, voutsinos2024weatheredgranitesand pages 1-2) | Supported as XoxF cofactor/environmental lanthanide. |
| glutathione | cofactor / metabolite | CHEBI:16856 | (tarasov2023cytobacilluspseudoceanisediminissp. pages 6-8, wang2024metabolicengineeringof pages 2-4) | Relevant to glutathione-dependent formaldehyde oxidation; not universal. |
| **E. Environmental/experimental factors** |  |  |  |  |
| weathered granite | environment | ENVO:01000807 | (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 4-7, voutsinos2024weatheredgranitesand pages 10-12) | Strong environmental association for lanthanide-dependent methylotrophy. |
| soil | environment | ENVO:00001998 | (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 4-7) | Broad environmental context; not specific enough alone to infer trait. |
| phosphate mineral dissolution | geochemical process | label-only | (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 12-14) | Mechanistically linked to lanthanide mobilization in granite weathering study; environmental, not universal. |
| lanthanide phosphate mineral solubilisation | geochemical process | label-only | (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 2-4) | Useful for environmental causal graph extensions; evidence from metagenomic/geochemical co-occurrence. |
| lanthanide availability | experimental/environmental factor | label-only | (gorniak2024changesingrowth pages 1-2, phi2024assessinglanthanidedependentmethanol pages 21-24, kamachi2025switchingbetweenmethanol pages 1-2) | Strong regulator of MDH isoform usage. |
| formaldehyde stress | experimental factor | label-only | (shao2024transcriptomicdatareveals pages 1-2, shao2024transcriptomicdatareveals pages 2-4, li2024aeukaryotefeaturedmembrane pages 1-2) | Important assay/stress condition revealing detox and tolerance modules. |
| low methanol condition | experimental factor | label-only | (zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2) | Selection condition in plant-associated Methylorubrum evolution study. |
| phyllosphere | environment | ENVO:01001874 | (zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2) | Important ecological niche for plant-associated methylotrophs. |
| **F. Application/assay entities** |  |  |  |  |
| formaldehyde growth biosensor | assay entity | label-only | (schann2024designconstructionand pages 1-2) | Strong application node; not native biology. |
| methanol-dependent synthetic methylotroph E. coli | engineered phenotype | label-only | (wu2023engineeringasynthetic pages 1-2, schann2024designconstructionand pages 1-2, sun2023engineeringandadaptive pages 12-12) | Useful application context; do not curate as native-trait mechanism. |
| membrane-remodeled E. coli for methanol assimilation | engineered system | label-only | (li2024aeukaryotefeaturedmembrane pages 1-2) | Engineering application improving formaldehyde tolerance; not native mechanism. |
| plant growth promotion by Methylobacterium/Methylorubrum | application phenotype | label-only | (zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2) | Downstream ecological/biotech outcome associated with efficient methylotrophy. |
| methanol biomanufacturing / C1-based biomanufacturing | application domain | label-only | (orsi2023synergisticinvestigationof pages 1-2, orsi2023synergisticinvestigationof pages 2-4, orsi2023synergisticinvestigationof pages 5-6) | Useful high-level application node; likely outside core TraitMech graph. |


*Table: This table lists curation-ready candidate nodes for a methylotrophic trait causal graph, grouped by biological and environmental entity type. It emphasizes core native methylotrophy modules while flagging taxon-specific, environmental, and synthetic-engineering entities that may require cautious curation.*

### 7. Candidate causal edges (evidence-backed triples)
The following table lists proposed subject–predicate–object triples with evidence snippets, DOI-first references/URLs, and curation notes.

| Subject node | Predicate | Object node | Evidence snippet | Reference | Citation ID | Curation notes/uncertainty |
|---|---|---|---|---|---|---|
| methanol dehydrogenase (MDH) | oxidizes_to | formaldehyde | “methanol is oxidized to formaldehyde by methanol dehydrogenase (MDH)” | Samanta et al., 2024, doi:10.1128/msystems.00248-24, https://doi.org/10.1128/msystems.00248-24 | (samanta2024fromgenometo pages 18-20) | Core methylotrophy edge; broadly curatable. |
| methane monooxygenase (pMMO/sMMO) | oxidizes_to | methanol | “methane is oxidized by methane monooxygenases (sMMO or pMMO) to produce methanol” | Samanta et al., 2024, doi:10.1128/msystems.00248-24, https://doi.org/10.1128/msystems.00248-24 | (samanta2024fromgenometo pages 16-18) | Boundary edge: defines methanotrophy, a subset of methylotrophy. |
| methylotroph | assimilates_via | ribulose monophosphate pathway (RuMP) | “many methylotrophs encoding… either the ribulose monophosphate (RuMP), serine cycle and tetrahydrofolate pathway” | Rasmussen et al., 2024, doi:10.1128/msystems.00314-24, https://doi.org/10.1128/msystems.00314-24 | (rasmussen2024diverseandunconventional pages 1-2) | Broad comparative/genomic support; not universal across all taxa. |
| 3-hexulose-6-phosphate synthase (Hps) | catalyzes | RuMP formaldehyde assimilation | “The ribulose 5-phosphate (RuMP) pathway relies on enzymes 3-hexulose 6-phosphate synthase (Hps) and phosphohexose isomerase (Phi) to assimilate formaldehyde” | Mitic et al., 2023, doi:10.1038/s41467-023-43610-7, https://doi.org/10.1038/s41467-023-43610-7 | (mitic2023theoxygentolerantreductive pages 1-2) | Strong pathway-marker edge. |
| phosphohexose isomerase (Phi) | catalyzes | RuMP formaldehyde assimilation | “Hps and phosphohexose isomerase (Phi)… assimilate formaldehyde” | Mitic et al., 2023, doi:10.1038/s41467-023-43610-7, https://doi.org/10.1038/s41467-023-43610-7 | (mitic2023theoxygentolerantreductive pages 1-2) | Strong pathway-marker edge. |
| methylotrophic yeast | assimilates_via | xylulose monophosphate pathway (XuMP) | “The main yeast methanol assimilation route is the xylulose 5-phosphate pathway (XuMP)” | Mitic et al., 2023, doi:10.1038/s41467-023-43610-7, https://doi.org/10.1038/s41467-023-43610-7 | (mitic2023theoxygentolerantreductive pages 1-2) | Taxon-specific to yeasts such as Komagataella/Pichia. |
| dihydroxyacetone synthase (Das1/Das2) | catalyzes | XuMP formaldehyde assimilation | “Aox1&2, Das1&2… roles in dissimilation/assimilation” and Das overexpression “drives formaldehyde assimilation” | Mitic et al., 2023, doi:10.1038/s41467-023-43610-7, https://doi.org/10.1038/s41467-023-43610-7; Wang et al., 2024, doi:10.1186/s12934-024-02475-1, https://doi.org/10.1186/s12934-024-02475-1 | (mitic2023theoxygentolerantreductive pages 1-2, wang2024metabolicengineeringof pages 2-4) | Strong in methylotrophic yeasts. |
| methylotroph | assimilates_via | serine cycle | “Formaldehyde is… assimilated primarily through the serine cycle” | Samanta et al., 2024, doi:10.1128/msystems.00248-24, https://doi.org/10.1128/msystems.00248-24 | (samanta2024fromgenometo pages 18-20) | Strong for many type II methylotrophs; not universal. |
| GlyA/SHMT | catalyzes | serine-cycle C1 assimilation | “serine hydroxymethyltransferase (SHMT, GlyA) is present in 74/75 genomes” | Samanta et al., 2024, doi:10.1128/msystems.00248-24, https://doi.org/10.1128/msystems.00248-24 | (samanta2024fromgenometo pages 12-14) | Strong comparative support; presence supports serine-cycle capacity. |
| serine-glyoxylate aminotransferase (SgaA/SGT) | catalyzes | serine cycle | “Serine-glyoxylate transaminase (SGT) occurs in all 75 organisms” | Samanta et al., 2024, doi:10.1128/msystems.00248-24, https://doi.org/10.1128/msystems.00248-24 | (samanta2024fromgenometo pages 12-14) | Strong serine-cycle marker. |
| hydroxypyruvate reductase (HprA/HPR) | catalyzes | serine cycle | “Hydroxypyruvate reductase (HPR) is ubiquitous (all 75)” | Samanta et al., 2024, doi:10.1128/msystems.00248-24, https://doi.org/10.1128/msystems.00248-24 | (samanta2024fromgenometo pages 12-14) | Strong serine-cycle marker. |
| formaldehyde | assimilates_via | serine cycle | “formaldehyde-derived carbon into biomass” and “formation of L-serine from glycine and formaldehyde” | Hying et al., 2024, doi:10.1128/aem.02090-23, https://doi.org/10.1128/aem.02090-23; Samanta et al., 2024, doi:10.1128/msystems.00248-24, https://doi.org/10.1128/msystems.00248-24 | (samanta2024fromgenometo pages 12-14, samanta2024fromgenometo pages 18-20) | Useful direct trait edge. |
| formaldehyde | assimilates_via | tetrahydrofolate (H4F/THF) pathway | “formate feeds into the tetrahydrofolate (THF) pathway to give methylene-THF” | Mitic et al., 2023, doi:10.1038/s41467-023-43610-7, https://doi.org/10.1038/s41467-023-43610-7 | (mitic2023theoxygentolerantreductive pages 1-2) | Better framed as linked one-carbon transfer pathway; may support rather than define methylotrophy. |
| formaldehyde oxidation | assimilates_via | tetrahydromethanopterin (H4MPT) pathway | “formaldehyde… catabolic oxidation proceeds via the H4MPT pathway” | Schmider et al., 2024, doi:10.1038/s41467-024-48197-1, https://doi.org/10.1038/s41467-024-48197-1 | (schmider2024physiologicalbasisfor pages 6-7) | Use predicate cautiously; pathway is oxidation/detox, not assimilation. |
| formaldehyde oxidation | assimilates_via | tetrahydrofolate (H4F) pathway | “and via tetrahydrofolate (H4F) species (methylene-H4F)” | Schmider et al., 2024, doi:10.1038/s41467-024-48197-1, https://doi.org/10.1038/s41467-024-48197-1 | (schmider2024physiologicalbasisfor pages 6-7) | Oxidation/transfer pathway; curatable as formaldehyde handling. |
| formaldehyde dehydrogenase (Fld/FDH) | oxidizes_to | formate | “FDH — which converts formaldehyde to formate — is relatively rare, present in only 10 organisms” | Samanta et al., 2024, doi:10.1128/msystems.00248-24, https://doi.org/10.1128/msystems.00248-24 | (samanta2024fromgenometo pages 12-14) | Strong edge; note low prevalence in surveyed type II methylotrophs. |
| formaldehyde dehydrogenase (Fld) | enables_growth_on | methanol | “knocking out… Fld… caused growth defects in methanol medium” | Wang et al., 2024, doi:10.1186/s12934-024-02475-1, https://doi.org/10.1186/s12934-024-02475-1 | (wang2024metabolicengineeringof pages 2-4) | Strong but yeast-specific experimental evidence. |
| Fgh (S-formylglutathione hydrolase) | detoxifies | formaldehyde | “Detox/oxidation components explicitly named include Fld… Fdh… and Fgh” | Wang et al., 2024, doi:10.1186/s12934-024-02475-1, https://doi.org/10.1186/s12934-024-02475-1 | (wang2024metabolicengineeringof pages 2-4) | Inferred from pathway component naming; somewhat weaker than direct kinetic evidence. |
| formate dehydrogenase (Fdh) | oxidizes_to | carbon dioxide | “supporting oxidation of formaldehyde via H4F/RuMP routes to formate and then to CO2” | Tarasov et al., 2023, doi:10.1007/s00284-022-03141-8, https://doi.org/10.1007/s00284-022-03141-8 | (tarasov2023cytobacilluspseudoceanisediminissp. pages 6-8) | Strong downstream dissimilation edge. |
| XoxF methanol dehydrogenase | requires_cofactor | pyrroloquinoline quinone (PQQ) | “XoxF-type MDHs are lanthanide (Ln)-dependent and use the quinone cofactor PQQ” | Phi, 2024, doi:10.5282/edoc.33507, https://doi.org/10.5282/edoc.33507 | (phi2024assessinglanthanidedependentmethanol pages 21-24) | Good mechanistic support; dissertation source, but consistent with peer-reviewed reviews. |
| XoxF methanol dehydrogenase | requires_cofactor | lanthanides | “XoxF… is a homologous form that utilizes light lanthanides (Lns) as catalytic cofactors” | Warters, 2024, URL unavailable in standard form | (warters2024widespreadbacterialuse pages 9-13) | Good support; source is thesis/unknown journal, so mark moderate confidence. |
| MxaFI methanol dehydrogenase | requires_cofactor | pyrroloquinoline quinone (PQQ) | “Mxa-type MDHs are calcium-dependent… PQQ-dependent alcohol dehydrogenase family” | Gorniak et al., 2024, doi:10.1128/msphere.00685-24, https://doi.org/10.1128/msphere.00685-24 | (gorniak2024changesingrowth pages 1-2) | Strong family-level evidence. |
| MxaFI methanol dehydrogenase | requires_cofactor | calcium ion (Ca2+) | “MxaF contains a calcium ion in its active site” | Kamachi & Ito, 2025, doi:10.1016/b978-0-443-13307-7.00014-1, https://doi.org/10.1016/b978-0-443-13307-7.00014-1 | (kamachi2025switchingbetweenmethanol pages 1-2) | Mechanistically strong but 2025 book chapter; acceptable as supplementary support. |
| lanthanide availability | induces_expression_of | pedH | “when La is present… activation of pedH transcription” | Gorniak et al., 2024, doi:10.1128/msphere.00685-24, https://doi.org/10.1128/msphere.00685-24 | (gorniak2024changesingrowth pages 1-2) | Strong regulatory edge; non-methylotroph exemplar, taxon-specific. |
| lanthanide availability | represses_expression_of | pedE | “presence of La… leading to decreased pedE expression” | Gorniak et al., 2024, doi:10.1128/msphere.00685-24, https://doi.org/10.1128/msphere.00685-24 | (gorniak2024changesingrowth pages 1-2) | Strong regulatory edge; non-methylotroph exemplar. |
| cerium | represses_expression_of | mxaF | “increasing cerium concentration represses mxaF” | Kamachi & Ito, 2025, doi:10.1016/b978-0-443-13307-7.00014-1, https://doi.org/10.1016/b978-0-443-13307-7.00014-1 | (kamachi2025switchingbetweenmethanol pages 1-2) | Strong lanthanide-switch edge; 2025 secondary source. |
| cerium | induces_expression_of | xoxF | “increasing cerium… induces xoxF expression” | Kamachi & Ito, 2025, doi:10.1016/b978-0-443-13307-7.00014-1, https://doi.org/10.1016/b978-0-443-13307-7.00014-1 | (kamachi2025switchingbetweenmethanol pages 1-2) | Strong lanthanide-switch edge; 2025 secondary source. |
| xoxF gene cluster | co_occurs_with | XoxJ/XoxG accessory genes | “The gene clusters often include canonical partners (XoxJ, XoxG)” | Voutsinos et al., 2024, doi:10.1186/s12915-024-01841-0, https://doi.org/10.1186/s12915-024-01841-0 | (voutsinos2024weatheredgranitesand pages 1-2) | Good genomic co-occurrence edge. |
| xoxF gene cluster | co_occurs_with | metallophore biosynthetic cluster (LCC) | “candidate metallophore biosynthetic systems… particularly associated with Acidobacteria harboring lanthanide systems” | Voutsinos et al., 2024, doi:10.1186/s12915-024-01841-0, https://doi.org/10.1186/s12915-024-01841-0 | (voutsinos2024weatheredgranitesand pages 1-2) | Environmental/genomic co-occurrence; does not prove direct biochemical interaction. |
| xoxF gene cluster | co_occurs_with | weathered granite microbiomes across multiple phyla | “xoxF-containing gene clusters… are common in moderately weathered granite” across Acidobacteria, Gemmatimonadetes, Verrucomicrobia, Alphaproteobacteria | Voutsinos et al., 2024, doi:10.1186/s12915-024-01841-0, https://doi.org/10.1186/s12915-024-01841-0 | (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 4-7) | Ecological distribution edge; phrase as association, not trait-defining mechanism. |
| formaldehyde stress | decreases | membrane integrity | “formaldehyde greatly impairs cell membranes” | Li et al., 2024, doi:10.1021/acssynbio.4c00499, https://doi.org/10.1021/acssynbio.4c00499 | (li2024aeukaryotefeaturedmembrane pages 1-2) | Engineering-focused but mechanistically relevant for tolerance. |
| phosphatidylcholine remodeling | increases | methanol consumption | “consumed up to 4.7 g/L methanol, which is 23-fold higher than… control (0.2 g/L)” | Li et al., 2024, doi:10.1021/acssynbio.4c00499, https://doi.org/10.1021/acssynbio.4c00499 | (li2024aeukaryotefeaturedmembrane pages 1-2) | Application/engineering edge, not native mechanism. |
| formaldehyde growth biosensor | enables_growth_on | formaldehyde detection range 30 μM–13 mM | “detect formaldehyde concentrations ranging approximately from 30 μM to 13 mM” | Schann et al., 2024, doi:10.1111/1751-7915.14527, https://doi.org/10.1111/1751-7915.14527 | (schann2024designconstructionand pages 1-2) | Assay edge only; not direct native trait biology. |
| hydrogen addition | increases | methanol production in methanotroph coculture | “addition of hydrogen nearly doubled methanol production to ~0.32 g L−1 with ~66% conversion efficiency” | Ahmadi & Lackner, 2024, doi:10.1007/s00253-023-12978-3, https://doi.org/10.1007/s00253-023-12978-3 | (ahmadi2024recentfindingsin pages 7-9) | Real-world/biotech implementation; secondary review citing Zhou et al. 2020. |
| DAS2 overexpression | decreases | formaldehyde accumulation | “overexpression of the endogenous DAS2 drives formaldehyde assimilation, reduces formaldehyde accumulation” | Wang et al., 2024, doi:10.1186/s12934-024-02475-1, https://doi.org/10.1186/s12934-024-02475-1 | (wang2024metabolicengineeringof pages 2-4) | Strong yeast engineering edge. |
| DAS2 overexpression | increases | biomass fatty acid yield | “drives formaldehyde assimilation… and increases biomass fatty acid yield” | Wang et al., 2024, doi:10.1186/s12934-024-02475-1, https://doi.org/10.1186/s12934-024-02475-1 | (wang2024metabolicengineeringof pages 2-4) | Engineering phenotype edge. |
| GlyA/SHMT | co_occurs_with | type II methylotroph genomes | “SHMT, GlyA is present in 74/75 genomes” | Samanta et al., 2024, doi:10.1128/msystems.00248-24, https://doi.org/10.1128/msystems.00248-24 | (samanta2024fromgenometo pages 12-14) | Useful prevalence/statistics edge for pathway confidence. |
| formaldehyde dehydrogenase (FDH) | co_occurs_with | minority of type II methylotroph genomes | “FDH… is relatively rare, present in only 10 organisms” | Samanta et al., 2024, doi:10.1128/msystems.00248-24, https://doi.org/10.1128/msystems.00248-24 | (samanta2024fromgenometo pages 12-14) | Prevalence edge; supports warning against treating FDH as universal. |


*Table: This table lists curation-ready candidate causal edges for the methylotrophic trait, with controlled predicates, faithful evidence snippets, DOI-first references, and uncertainty notes. It covers core native mechanisms, regulatory/environmental modifiers, and selected assay or engineering edges that should be curated cautiously.*

### 8. Ontology grounding notes
- Use METPO:1000651 for the trait class; consider representing **methanotrophic** as a child trait/subclass (subset) rather than an edge when modeling trait taxonomy, because methane oxidation machinery (MMO) is a defining module. (samanta2024fromgenometo pages 16-18, ahmadi2024recentfindingsin pages 1-2)
- Prefer stable identifiers for pathways when available (e.g., MetaCyc for serine cycle/RuMP). Where stable IDs are unclear in evidence, keep **label-only** nodes until resolved. (mitic2023theoxygentolerantreductive pages 1-2, samanta2024fromgenometo pages 12-14)
- For lanthanide-related concepts, curate both **(i) metal availability** as an environmental factor and **(ii) XoxF MDH** as an enzyme node; represent the “lanthanide switch” as a regulatory process with taxon-specific implementations. (gorniak2024changesingrowth pages 1-2, voutsinos2024weatheredgranitesand pages 1-2)

### 9. Warnings / claims not yet ready for TraitMech curation
1) **Engineering-only pathways** (e.g., EuMP synthetic cycle) should not be curated as native methylotrophy mechanisms, but can be placed in an “engineering context” section if your schema supports it. (wu2023engineeringasynthetic pages 1-2)
2) **PedE/PedH/PedS2R2 lanthanide switch** evidence is strong but comes from a non-methylotroph exemplar; curate as a *candidate regulatory analog* unless corroborated in canonical methylotrophs within your evidence set. (gorniak2024changesingrowth pages 1-2)
3) **Metallophore/LCC → lanthanide phosphate dissolution → enhanced methylotrophy** is currently supported mainly by co-occurrence and environmental inference in weathered granite; treat causal direction as **uncertain** unless validated experimentally. (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 12-14)
4) **FDH as a universal formaldehyde oxidation node** is contradicted by prevalence data (minority presence in type II methylotroph genomes); model FDH as optional/lineage-specific. (samanta2024fromgenometo pages 12-14)

### 10. DOI-first bibliography (with URLs and dates)
| Topic area | Full citation (authors, title, journal) | Publication date (month/year) | DOI | URL |
|---|---|---|---|---|
| C1-trophic framing / circular carbon economy | Orsi E, Nikel PI, Nielsen LK, Donati S. *Synergistic investigation of natural and synthetic C1-trophic microorganisms to foster a circular carbon economy*. Nature Communications. (orsi2023synergisticinvestigationof pages 1-2, orsi2023synergisticinvestigationof pages 2-4) | 10/2023 | 10.1038/s41467-023-42166-w | https://doi.org/10.1038/s41467-023-42166-w |
| Methanol, formate, and CO2 assimilation pathways | Mitic BM, Troyer C, Lutz L, Baumschabl M, Hann S, Mattanovich D. *The oxygen-tolerant reductive glycine pathway assimilates methanol, formate and CO2 in the yeast Komagataella phaffii*. Nature Communications. (mitic2023theoxygentolerantreductive pages 1-2, mitic2023theoxygentolerantreductive media c3651b92) | 11/2023 | 10.1038/s41467-023-43610-7 | https://doi.org/10.1038/s41467-023-43610-7 |
| Synthetic formaldehyde assimilation | Wu T, Gómez-Coronado PA, Kubis A, Lindner SN, Marlière P, Erb TJ, Bar-Even A, He H. *Engineering a synthetic energy-efficient formaldehyde assimilation cycle in Escherichia coli*. Nature Communications. (wu2023engineeringasynthetic pages 1-2) | 12/2023 | 10.1038/s41467-023-44247-2 | https://doi.org/10.1038/s41467-023-44247-2 |
| Methanotroph/methylotroph scope and biopotential | Ahmadi F, Lackner M. *Recent findings in methanotrophs: genetics, molecular ecology, and biopotential*. Applied Microbiology and Biotechnology. (ahmadi2024recentfindingsin pages 1-2, ahmadi2024recentfindingsin pages 7-9) | 01/2024 | 10.1007/s00253-023-12978-3 | https://doi.org/10.1007/s00253-023-12978-3 |
| Type II methylotroph comparative genomics | Samanta D, Rauniyar S, Saxena P, Sani RK. *From genome to evolution: investigating type II methylotrophs using a pangenomic analysis*. mSystems. (samanta2024fromgenometo pages 12-14, samanta2024fromgenometo pages 18-20, samanta2024fromgenometo pages 16-18) | 06/2024 | 10.1128/msystems.00248-24 | https://doi.org/10.1128/msystems.00248-24 |
| Lanthanide-dependent methylotrophy in weathered rock/soil | Voutsinos MY, West-Roberts JA, Sachdeva R, Moreau JW, Banfield JF. *Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes*. BMC Biology. (voutsinos2024weatheredgranitesand pages 1-2, voutsinos2024weatheredgranitesand pages 4-7, voutsinos2024weatheredgranitesand pages 2-4, voutsinos2024weatheredgranitesand pages 10-12, voutsinos2024weatheredgranitesand pages 12-14, voutsinos2024weatheredgranitesand pages 16-17, voutsinos2024weatheredgranitesand pages 17-18) | 02/2024 | 10.1186/s12915-024-01841-0 | https://doi.org/10.1186/s12915-024-01841-0 |
| Plant-associated methylotrophy / phyllosphere colonization | Zhang C, Zhou D-F, Wang M-Y, Song Y-Z, Zhang C, Zhang M-M, Sun J, Yao L, Mo X-H, Ma Z-X, Yuan X-J, Shao Y, Wang H-R, Dong S-H, Bao K, Lu S-H, Sadilek M, Kalyuzhnaya MG, Xing X-H, Yang S. *Phosphoribosylpyrophosphate synthetase as a metabolic valve advances Methylobacterium/Methylorubrum phyllosphere colonization and plant growth*. Nature Communications. (zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2) | 07/2024 | 10.1038/s41467-024-50342-9 | https://doi.org/10.1038/s41467-024-50342-9 |
| Methylotrophic yeast engineering / methanol utilization | Wang Y, Li R, Zhao F, Wang S, Zhang Y, Fan D, Han S. *Metabolic engineering of Komagataella phaffii for the efficient utilization of methanol*. Microbial Cell Factories. (wang2024metabolicengineeringof pages 2-4) | 07/2024 | 10.1186/s12934-024-02475-1 | https://doi.org/10.1186/s12934-024-02475-1 |
| Formaldehyde biosensors for methylotrophy engineering | Schann K, Bakker J, Boinot M, Kuschel P, He H, Nattermann M, Paczia N, Erb T, Bar-Even A, Wenk S. *Design, construction and optimization of formaldehyde growth biosensors with broad application in biotechnology*. Microbial Biotechnology. (schann2024designconstructionand pages 1-2) | 07/2024 | 10.1111/1751-7915.14527 | https://doi.org/10.1111/1751-7915.14527 |
| Formaldehyde tolerance / engineered methanol assimilation | Li MK, Sun W, Wang X, Chen K, Feng Y, Tan Z. *A eukaryote-featured membrane phospholipid enhances bacterial formaldehyde tolerance and assimilation of one-carbon feedstocks*. ACS Synthetic Biology. (li2024aeukaryotefeaturedmembrane pages 1-2) | 11/2024 | 10.1021/acssynbio.4c00499 | https://doi.org/10.1021/acssynbio.4c00499 |
| H4MPT/H4F-linked formaldehyde oxidation in methanotrophs | Schmider T, Hestnes AG, Brzykcy J, Schmidt H, Schintlmeister A, Roller BRK, Teran EJ, Söllinger A, Schmidt O, Polz MF, Richter A, Svenning MM, Tveit AT. *Physiological basis for atmospheric methane oxidation and methanotrophic growth on air*. Nature Communications. (schmider2024physiologicalbasisfor pages 6-7) | 05/2024 | 10.1038/s41467-024-48197-1 | https://doi.org/10.1038/s41467-024-48197-1 |
| Environmental distribution of methylotrophy / MAG evidence | Rasmussen AN, Tolar BB, Bargar JR, Boye K, Francis CA. *Diverse and unconventional methanogens, methanotrophs, and methylotrophs in metagenome-assembled genomes from subsurface sediments of the Slate River floodplain, Crested Butte, CO, USA*. mSystems. (rasmussen2024diverseandunconventional pages 1-2) | 07/2024 | 10.1128/msystems.00314-24 | https://doi.org/10.1128/msystems.00314-24 |
| Lanthanide-responsive ADH regulation / lanthanide switch | Gorniak L, Bucka SL, Nasr B, Cao J, Hellmann S, Schäfer T, Westermann M, Bechwar J, Wegner C-E. *Changes in growth, lanthanide binding, and gene expression in Pseudomonas alloputida KT2440 in response to light and heavy lanthanides*. mSphere. (gorniak2024changesingrowth pages 1-2) | 10/2024 | 10.1128/msphere.00685-24 | https://doi.org/10.1128/msphere.00685-24 |
| Methane monooxygenase context for methanotrophic boundary case | Tucci FJ, Rosenzweig AC. *Direct Methane Oxidation by Copper- and Iron-Dependent Methane Monooxygenases*. Chemical Reviews. (tucci2024directmethaneoxidation pages 38-40) | 02/2024 | 10.1021/acs.chemrev.3c00727 | https://doi.org/10.1021/acs.chemrev.3c00727 |


*Table: This table compiles the main 2023–2024 sources used to support the methylotrophic trait report, emphasizing mechanistic, ecological, and applied studies. It is useful as a DOI-first reading list for curation and follow-up verification.*

### 11. Visual evidence
Mitic et al. 2023 Figure 1 provides a compact, curation-useful schematic of methanol/formate assimilation options (XuMP, RuMP, serine cycle, reductive glycine variants). (mitic2023theoxygentolerantreductive media c3651b92)


References

1. (samanta2024fromgenometo pages 18-20): Dipayan Samanta, Shailabh Rauniyar, Priya Saxena, and Rajesh K. Sani. From genome to evolution: investigating type ii methylotrophs using a pangenomic analysis. Jun 2024. URL: https://doi.org/10.1128/msystems.00248-24, doi:10.1128/msystems.00248-24. This article has 10 citations and is from a peer-reviewed journal.

2. (ahmadi2024recentfindingsin pages 1-2): Fatemeh Ahmadi and Maximilian Lackner. Recent findings in methanotrophs: genetics, molecular ecology, and biopotential. Applied Microbiology and Biotechnology, 108:1-21, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12978-3, doi:10.1007/s00253-023-12978-3. This article has 33 citations and is from a domain leading peer-reviewed journal.

3. (schmider2024physiologicalbasisfor pages 6-7): Tilman Schmider, Anne Grethe Hestnes, Julia Brzykcy, Hannes Schmidt, Arno Schintlmeister, Benjamin R. K. Roller, Ezequiel Jesús Teran, Andrea Söllinger, Oliver Schmidt, Martin F. Polz, Andreas Richter, Mette M. Svenning, and Alexander T. Tveit. Physiological basis for atmospheric methane oxidation and methanotrophic growth on air. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48197-1, doi:10.1038/s41467-024-48197-1. This article has 50 citations and is from a highest quality peer-reviewed journal.

4. (samanta2024fromgenometo pages 16-18): Dipayan Samanta, Shailabh Rauniyar, Priya Saxena, and Rajesh K. Sani. From genome to evolution: investigating type ii methylotrophs using a pangenomic analysis. Jun 2024. URL: https://doi.org/10.1128/msystems.00248-24, doi:10.1128/msystems.00248-24. This article has 10 citations and is from a peer-reviewed journal.

5. (orsi2023synergisticinvestigationof pages 1-2): Enrico Orsi, Pablo Ivan Nikel, Lars Keld Nielsen, and Stefano Donati. Synergistic investigation of natural and synthetic c1-trophic microorganisms to foster a circular carbon economy. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42166-w, doi:10.1038/s41467-023-42166-w. This article has 51 citations and is from a highest quality peer-reviewed journal.

6. (mitic2023theoxygentolerantreductive pages 1-2): Bernd M. Mitic, Christina Troyer, Lisa Lutz, Michael Baumschabl, Stephan Hann, and Diethard Mattanovich. The oxygen-tolerant reductive glycine pathway assimilates methanol, formate and co2 in the yeast komagataella phaffii. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43610-7, doi:10.1038/s41467-023-43610-7. This article has 47 citations and is from a highest quality peer-reviewed journal.

7. (mitic2023theoxygentolerantreductive media c3651b92): Bernd M. Mitic, Christina Troyer, Lisa Lutz, Michael Baumschabl, Stephan Hann, and Diethard Mattanovich. The oxygen-tolerant reductive glycine pathway assimilates methanol, formate and co2 in the yeast komagataella phaffii. Nature Communications, Nov 2023. URL: https://doi.org/10.1038/s41467-023-43610-7, doi:10.1038/s41467-023-43610-7. This article has 47 citations and is from a highest quality peer-reviewed journal.

8. (samanta2024fromgenometo pages 12-14): Dipayan Samanta, Shailabh Rauniyar, Priya Saxena, and Rajesh K. Sani. From genome to evolution: investigating type ii methylotrophs using a pangenomic analysis. Jun 2024. URL: https://doi.org/10.1128/msystems.00248-24, doi:10.1128/msystems.00248-24. This article has 10 citations and is from a peer-reviewed journal.

9. (gorniak2024changesingrowth pages 1-2): Linda Gorniak, Sarah Luise Bucka, Bayan Nasr, Jialan Cao, Steffen Hellmann, Thorsten Schäfer, Martin Westermann, Julia Bechwar, and Carl-Eric Wegner. Changes in growth, lanthanide binding, and gene expression in <i>pseudomonas alloputida</i> kt2440 in response to light and heavy lanthanides. Oct 2024. URL: https://doi.org/10.1128/msphere.00685-24, doi:10.1128/msphere.00685-24. This article has 5 citations and is from a peer-reviewed journal.

10. (voutsinos2024weatheredgranitesand pages 1-2): Marcos Y. Voutsinos, Jacob A. West-Roberts, Rohan Sachdeva, John W. Moreau, and Jillian F. Banfield. Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes. BMC Biology, Feb 2024. URL: https://doi.org/10.1186/s12915-024-01841-0, doi:10.1186/s12915-024-01841-0. This article has 13 citations and is from a domain leading peer-reviewed journal.

11. (voutsinos2024weatheredgranitesand pages 4-7): Marcos Y. Voutsinos, Jacob A. West-Roberts, Rohan Sachdeva, John W. Moreau, and Jillian F. Banfield. Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes. BMC Biology, Feb 2024. URL: https://doi.org/10.1186/s12915-024-01841-0, doi:10.1186/s12915-024-01841-0. This article has 13 citations and is from a domain leading peer-reviewed journal.

12. (voutsinos2024weatheredgranitesand pages 2-4): Marcos Y. Voutsinos, Jacob A. West-Roberts, Rohan Sachdeva, John W. Moreau, and Jillian F. Banfield. Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes. BMC Biology, Feb 2024. URL: https://doi.org/10.1186/s12915-024-01841-0, doi:10.1186/s12915-024-01841-0. This article has 13 citations and is from a domain leading peer-reviewed journal.

13. (voutsinos2024weatheredgranitesand pages 12-14): Marcos Y. Voutsinos, Jacob A. West-Roberts, Rohan Sachdeva, John W. Moreau, and Jillian F. Banfield. Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes. BMC Biology, Feb 2024. URL: https://doi.org/10.1186/s12915-024-01841-0, doi:10.1186/s12915-024-01841-0. This article has 13 citations and is from a domain leading peer-reviewed journal.

14. (orsi2023synergisticinvestigationof pages 2-4): Enrico Orsi, Pablo Ivan Nikel, Lars Keld Nielsen, and Stefano Donati. Synergistic investigation of natural and synthetic c1-trophic microorganisms to foster a circular carbon economy. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42166-w, doi:10.1038/s41467-023-42166-w. This article has 51 citations and is from a highest quality peer-reviewed journal.

15. (zhang2024phosphoribosylpyrophosphatesynthetaseas pages 1-2): Cong Zhang, Di-Fei Zhou, Meng-Ying Wang, Ya-Zhen Song, Chong Zhang, Ming-Ming Zhang, Jing Sun, Lu Yao, Xu-Hua Mo, Zeng-Xin Ma, Xiao-Jie Yuan, Yi Shao, Hao-Ran Wang, Si-Han Dong, Kai Bao, Shu-Huan Lu, Martin Sadilek, Marina G. Kalyuzhnaya, Xin-Hui Xing, and Song Yang. Phosphoribosylpyrophosphate synthetase as a metabolic valve advances methylobacterium/methylorubrum phyllosphere colonization and plant growth. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50342-9, doi:10.1038/s41467-024-50342-9. This article has 31 citations and is from a highest quality peer-reviewed journal.

16. (schann2024designconstructionand pages 1-2): Karin Schann, Jenny Bakker, Maximilian Boinot, Pauline Kuschel, Hai He, Maren Nattermann, Nicole Paczia, Tobias Erb, Arren Bar‐Even, and Sebastian Wenk. Design, construction and optimization of formaldehyde growth biosensors with broad application in biotechnology. Microbial Biotechnology, Jul 2024. URL: https://doi.org/10.1111/1751-7915.14527, doi:10.1111/1751-7915.14527. This article has 17 citations and is from a peer-reviewed journal.

17. (orsi2023synergisticinvestigationof pages 5-6): Enrico Orsi, Pablo Ivan Nikel, Lars Keld Nielsen, and Stefano Donati. Synergistic investigation of natural and synthetic c1-trophic microorganisms to foster a circular carbon economy. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42166-w, doi:10.1038/s41467-023-42166-w. This article has 51 citations and is from a highest quality peer-reviewed journal.

18. (ahmadi2024recentfindingsin pages 7-9): Fatemeh Ahmadi and Maximilian Lackner. Recent findings in methanotrophs: genetics, molecular ecology, and biopotential. Applied Microbiology and Biotechnology, 108:1-21, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12978-3, doi:10.1007/s00253-023-12978-3. This article has 33 citations and is from a domain leading peer-reviewed journal.

19. (li2024aeukaryotefeaturedmembrane pages 1-2): MengKun Li, Wenjie Sun, Xin Wang, Kequan Chen, Yan Feng, and Zaigao Tan. A eukaryote-featured membrane phospholipid enhances bacterial formaldehyde tolerance and assimilation of one-carbon feedstocks. ACS synthetic biology, 13:4074-4084, Nov 2024. URL: https://doi.org/10.1021/acssynbio.4c00499, doi:10.1021/acssynbio.4c00499. This article has 7 citations and is from a domain leading peer-reviewed journal.

20. (rasmussen2024diverseandunconventional pages 1-2): Anna N. Rasmussen, Bradley B. Tolar, John R. Bargar, Kristin Boye, and Christopher A. Francis. Diverse and unconventional methanogens, methanotrophs, and methylotrophs in metagenome-assembled genomes from subsurface sediments of the slate river floodplain, crested butte, co, usa. Jul 2024. URL: https://doi.org/10.1128/msystems.00314-24, doi:10.1128/msystems.00314-24. This article has 11 citations and is from a peer-reviewed journal.

21. (shao2024transcriptomicdatareveals pages 1-2): Yunhai Shao, Shuang Li, Yanxin Wang, Pei Qiao, and Weihong Zhong. Transcriptomic data reveals an auxiliary detoxification mechanism that alleviates formaldehyde stress in methylobacterium sp. xjlw. BMC Genomics, Oct 2024. URL: https://doi.org/10.1186/s12864-024-10923-w, doi:10.1186/s12864-024-10923-w. This article has 6 citations and is from a peer-reviewed journal.

22. (wu2023engineeringasynthetic pages 1-2): Tong Wu, Paul A. Gómez-Coronado, Armin Kubis, Steffen N. Lindner, Philippe Marlière, Tobias J. Erb, Arren Bar-Even, and Hai He. Engineering a synthetic energy-efficient formaldehyde assimilation cycle in escherichia coli. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-44247-2, doi:10.1038/s41467-023-44247-2. This article has 53 citations and is from a highest quality peer-reviewed journal.

23. (schann2024theserineshunt pages 1-6): Karin Schann and Sebastian Wenk. The serine shunt enables formate conversion to formaldehyde in vivo. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.31.605843, doi:10.1101/2024.07.31.605843. This article has 4 citations.

24. (orsi2023synergisticinvestigationof pages 4-4): Enrico Orsi, Pablo Ivan Nikel, Lars Keld Nielsen, and Stefano Donati. Synergistic investigation of natural and synthetic c1-trophic microorganisms to foster a circular carbon economy. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42166-w, doi:10.1038/s41467-023-42166-w. This article has 51 citations and is from a highest quality peer-reviewed journal.

25. (shao2024transcriptomicdatareveals pages 2-4): Yunhai Shao, Shuang Li, Yanxin Wang, Pei Qiao, and Weihong Zhong. Transcriptomic data reveals an auxiliary detoxification mechanism that alleviates formaldehyde stress in methylobacterium sp. xjlw. BMC Genomics, Oct 2024. URL: https://doi.org/10.1186/s12864-024-10923-w, doi:10.1186/s12864-024-10923-w. This article has 6 citations and is from a peer-reviewed journal.

26. (wang2024metabolicengineeringof pages 2-4): Yuanyuan Wang, Ruisi Li, Fengguang Zhao, Shuai Wang, Yaping Zhang, Dexun Fan, and Shuangyan Han. Metabolic engineering of komagataella phaffii for the efficient utilization of methanol. Microbial Cell Factories, Jul 2024. URL: https://doi.org/10.1186/s12934-024-02475-1, doi:10.1186/s12934-024-02475-1. This article has 19 citations and is from a peer-reviewed journal.

27. (phi2024assessinglanthanidedependentmethanol pages 21-24): Assessing lanthanide-dependent methanol dehydrogenase activity and the syntheses of citrate based siderophores This article has 0 citations.

28. (warters2024widespreadbacterialuse pages 9-13): L Warters. Widespread bacterial use of lanthanides for methylotrophy across ecosystems. Unknown journal, 2024.

29. (tarasov2023cytobacilluspseudoceanisediminissp. pages 6-8): Kirill Tarasov, Alena Yakhnenko, Mikhail Zarubin, Albert Gangapshev, Natalia V. Potekhina, Alexander N. Avtukh, and Elena Kravchenko. Cytobacillus pseudoceanisediminis sp. nov., a novel facultative methylotrophic bacterium with high heavy metal resistance isolated from the deep underground saline spring. Current Microbiology, Dec 2023. URL: https://doi.org/10.1007/s00284-022-03141-8, doi:10.1007/s00284-022-03141-8. This article has 22 citations and is from a peer-reviewed journal.

30. (kamachi2025switchingbetweenmethanol pages 1-2): Toshiaki Kamachi and Hidehiro Ito. Switching between methanol accumulation and cell growth by expression control of methanol dehydrogenase in Methylosinus trichosporium OB3b, pages 267-283. Elsevier, Jan 2025. URL: https://doi.org/10.1016/b978-0-443-13307-7.00014-1, doi:10.1016/b978-0-443-13307-7.00014-1. This article has 0 citations.

31. (kamachi2025switchingbetweenmethanol pages 10-10): Toshiaki Kamachi and Hidehiro Ito. Switching between methanol accumulation and cell growth by expression control of methanol dehydrogenase in Methylosinus trichosporium OB3b, pages 267-283. Elsevier, Jan 2025. URL: https://doi.org/10.1016/b978-0-443-13307-7.00014-1, doi:10.1016/b978-0-443-13307-7.00014-1. This article has 0 citations.

32. (voutsinos2024weatheredgranitesand pages 17-18): Marcos Y. Voutsinos, Jacob A. West-Roberts, Rohan Sachdeva, John W. Moreau, and Jillian F. Banfield. Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes. BMC Biology, Feb 2024. URL: https://doi.org/10.1186/s12915-024-01841-0, doi:10.1186/s12915-024-01841-0. This article has 13 citations and is from a domain leading peer-reviewed journal.

33. (voutsinos2024weatheredgranitesand pages 16-17): Marcos Y. Voutsinos, Jacob A. West-Roberts, Rohan Sachdeva, John W. Moreau, and Jillian F. Banfield. Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes. BMC Biology, Feb 2024. URL: https://doi.org/10.1186/s12915-024-01841-0, doi:10.1186/s12915-024-01841-0. This article has 13 citations and is from a domain leading peer-reviewed journal.

34. (tucci2024directmethaneoxidation pages 38-40): Frank J. Tucci and Amy C. Rosenzweig. Direct methane oxidation by copper- and iron-dependent methane monooxygenases. Chemical reviews, 124:1288-1320, Feb 2024. URL: https://doi.org/10.1021/acs.chemrev.3c00727, doi:10.1021/acs.chemrev.3c00727. This article has 142 citations and is from a highest quality peer-reviewed journal.

35. (warters2024widespreadbacterialuse pages 39-41): L Warters. Widespread bacterial use of lanthanides for methylotrophy across ecosystems. Unknown journal, 2024.

36. (voutsinos2024weatheredgranitesand pages 10-12): Marcos Y. Voutsinos, Jacob A. West-Roberts, Rohan Sachdeva, John W. Moreau, and Jillian F. Banfield. Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes. BMC Biology, Feb 2024. URL: https://doi.org/10.1186/s12915-024-01841-0, doi:10.1186/s12915-024-01841-0. This article has 13 citations and is from a domain leading peer-reviewed journal.

37. (sun2023engineeringandadaptive pages 12-12): Qing Sun, De‐hua Liu, and Zhen Chen. Engineering and adaptive laboratory evolution of escherichia coli for improving methanol utilization based on a hybrid methanol assimilation pathway. Frontiers in Bioengineering and Biotechnology, Jan 2023. URL: https://doi.org/10.3389/fbioe.2022.1089639, doi:10.3389/fbioe.2022.1089639. This article has 18 citations.