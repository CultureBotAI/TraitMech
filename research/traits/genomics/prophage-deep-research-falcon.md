---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:14:50.868640'
end_time: '2026-08-04T05:23:39.190794'
duration_seconds: 528.32
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: prophage
  trait_identifier: traitmech:000091
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: prophage
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A genomics trait describing possession of an integrated (or extrachromosomal)
    temperate bacteriophage genome (a prophage) maintained in the host during lysogeny,
    often contributing genes that alter host phenotype.
  parent_traits: traitmech:000089
  synonyms: lysogen
  evidence_summary: 'DOI:10.1128/MMBR.67.2.238-276.2003:  (Canchaya et al. review
    prophage genomics, showing most sequenced bacterial genomes carry prophage sequences.)
    | DOI:10.1038/ismej.2017.16:  (Howard-Varona et al. review lysogeny in nature,
    the maintenance of temperate phage genomes within hosts.)'
  causal_graph_summary: 'prophage_lysogeny: 13 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** prophage
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000091
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of an integrated (or extrachromosomal) temperate bacteriophage genome (a prophage) maintained in the host during lysogeny, often contributing genes that alter host phenotype.
- **Parent traits:** traitmech:000089
- **Synonyms:** lysogen
- **Existing evidence:** DOI:10.1128/MMBR.67.2.238-276.2003:  (Canchaya et al. review prophage genomics, showing most sequenced bacterial genomes carry prophage sequences.) | DOI:10.1038/ismej.2017.16:  (Howard-Varona et al. review lysogeny in nature, the maintenance of temperate phage genomes within hosts.)
- **Existing causal graph summary:** prophage_lysogeny: 13 nodes, 9 edges

## Research Objective

Research the microbial trait **prophage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/prophage.yaml`.

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
- **Trait label:** prophage
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000091
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of an integrated (or extrachromosomal) temperate bacteriophage genome (a prophage) maintained in the host during lysogeny, often contributing genes that alter host phenotype.
- **Parent traits:** traitmech:000089
- **Synonyms:** lysogen
- **Existing evidence:** DOI:10.1128/MMBR.67.2.238-276.2003:  (Canchaya et al. review prophage genomics, showing most sequenced bacterial genomes carry prophage sequences.) | DOI:10.1038/ismej.2017.16:  (Howard-Varona et al. review lysogeny in nature, the maintenance of temperate phage genomes within hosts.)
- **Existing causal graph summary:** prophage_lysogeny: 13 nodes, 9 edges

## Research Objective

Research the microbial trait **prophage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/prophage.yaml`.

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


# Curation report: prophage (`traitmech:000091`)

## Executive summary

The reviewed class should represent **possession and lysogenic maintenance of a temperate bacteriophage genome**, ordinarily integrated into the bacterial chromosome but sometimes maintained as a low-copy extrachromosomal replicon. The core causal graph should terminate at the stable lysogenic state: site-specific integration or episomal maintenance, repression of lytic genes, vertical inheritance, and the resulting prophage-positive cell. Induction and host phenotypes are important downstream or contextual branches, not necessary defining conditions.

Recent work substantially refines this picture. A 2023 *Staphylococcus aureus* study showed that SOS-mediated CI cleavage is not necessarily sufficient for induction: ClpX must inactivate the residual DNA-binding CI N-terminal fragment, and loss of ClpX reduced spontaneous prophage release by more than two orders of magnitude. This is a strong but taxon/model-specific extension of the classical RecA–CI switch (thabet2023theclpxprotease pages 6-8, thabet2023theclpxprotease pages 11-12, thabet2023theclpxprotease pages 10-11). Large 2024 surveys also demonstrate that prevalence and completeness are strongly dataset- and taxon-dependent: 105,613 predicted regions occurred in approximately 92% of 43,942 human-gut bacterial genomes, whereas prophages occurred in 29.5% of 1,011 closed *Helicobacter pylori* genomes and only 32.2% of prophage-positive *H. pylori* genomes contained a complete prophage (pei2024auniverseof pages 1-2, vale2024genecontentphage pages 1-2).

## 1. Scope and boundaries

### Recommended scope

**Trait label:** prophage  
**Identifier:** `traitmech:000091`  
**Category:** GENOMICS  
**Term kind:** CLASS  
**Parent:** `traitmech:000089`  
**Synonym:** lysogen

Recommended operational definition:

> A genomic trait in which a microbial cell possesses a temperate-phage genome maintained during lysogeny, usually by chromosomal integration and vertical inheritance, but potentially as a stably maintained low-copy extrachromosomal replicon. Most lytic-cycle genes are transcriptionally repressed; element-specific accessory genes may remain expressed and alter host phenotype.

Temperate phages become prophages by entering lysogeny and are inherited with the host genome. Stable persistence requires repression because virion-production and lysis genes are toxic to the bacterial host; in the lambda paradigm, CI alone can maintain lysogeny (vale2024genecontentphage pages 1-2, owen2020awindowinto pages 1-2). The class therefore denotes **element carriage/state**, not a universal physiological outcome such as virulence, resistance, biofilm formation, or inducibility.

### Boundary cases

1. **Free lytic infection:** exclude. A lytic phage immediately proceeds through genome replication, packaging, progeny production, and host lysis; it is not a prophage-positive lysogen (vale2024genecontentphage pages 1-2).
2. **Induced prophage:** retain as a downstream transition from the trait, but do not equate it with the trait itself. Induction ends stable lysogenic repression and initiates productive development.
3. **Defective or cryptic prophage:** annotate with a qualifier or child state. Such remnants can no longer complete excision, particle production, lysis, or infectivity, yet may retain functional host-modifying genes. Most prophages show some degree of defect or decay, and *H. pylori* decay involves rearrangement, pseudogene accumulation, deletion, and merger with other mobile elements (bobay2014pervasivedomesticationof pages 1-2, vale2024genecontentphage pages 1-2).
4. **Prophage-like genomic region predicted in silico:** evidence for the trait, not definitive proof. Completeness and activity require intact boundaries/modules or experimental induction.
5. **Phage-inducible chromosomal islands and other satellites:** exclude from the class unless a bona fide temperate-phage genome is independently present. Satellites require a helper phage, although they also encode integrases and use att sites. A 2023 study observed composite excision, replication, and later satellite excision and mapped 491 helper-embedded PICIs, illustrating why automated tools can confuse nested satellites with prophage sequence (tommasini2023helperembeddedsatellitesfrom pages 1-2).
6. **Gene-transfer agents, plasmids, ICEs, and other genomic islands:** exclude unless evidence establishes a temperate-phage genome. Integrase and attachment sites alone are not specific.
7. **“Lysogen”:** properly denotes the host cell carrying a prophage, rather than the phage DNA itself.

## 2. Candidate nodes

### Trait and element-state nodes

- `traitmech:000091` — prophage
- temperate bacteriophage genome — label-only candidate
- integrated prophage genome — label-only candidate
- extrachromosomal prophage/episomal temperate-phage genome — label-only candidate
- lysogen / prophage-positive host cell — label-only candidate
- complete, inducible prophage — label-only candidate
- defective/cryptic prophage — label-only candidate
- prophage remnant — label-only candidate
- prophage induction; lysogenic-to-lytic transition — label-only unless a suitable ontology term is verified

### Genes, proteins, and molecular complexes

- **Phage integrase (Int):** site-specific recombinase acting at attachment sites. Use the applicable protein-family or gene identifier for the actual phage; do not assign one universal UniProt identifier.
- **Attachment sites:** attP, attB, attL, attR; sequence features rather than genes.
- **CI-like master repressor:** maintains repression of lytic transcription. CI is not universal across all temperate phages, so use a family/model-specific label.
- **Cro/antirepressor:** candidate switch regulators; include only where demonstrated for the selected system.
- **RecA:** activated RecA nucleoprotein state (`RecA*`) promotes autocleavage of susceptible repressors. Gene/protein identifiers should be taxon-specific.
- **LexA:** bacterial SOS repressor; useful upstream of induction but not a prophage component.
- **ClpX and ClpP:** host ATP-dependent protease machinery. The demonstrated ClpX–CI mechanism is specific to *S. aureus* Φ11/80α; ClpP acts upstream in the staphylococcal SOS response (thabet2023theclpxprotease pages 3-4, thabet2023theclpxprotease pages 11-12).
- **Excisionase/recombination directionality factor (Xis/RDF; sometimes AlpA-like):** redirects integrase-mediated recombination toward excision.
- **Terminase, portal, capsid, tail, holin, endolysin:** useful completeness and productive-cycle markers, but not required to define a decayed prophage. In one large survey, only 43% of predictions had an annotated integrase and 45.7% of predicted prophage ORFs lacked functional annotation (kang2017prophagegenomicsreveals pages 4-7).
- **Accessory/moron loci:** element-specific genes expressed during lysogeny.
- **STnc6030 antisense RNA:** BTP1-specific superinfection-exclusion factor in *Salmonella* (owen2020awindowinto pages 1-2).
- **KilR, DicB, YfdK, YfdO, YfdS:** *E. coli* cryptic-prophage proteins with experimentally observed host effects; contextual rather than core nodes (wang2010crypticprophageshelp pages 1-2).

### Processes and molecular functions

Conservative grounding candidates include:

- DNA integration — `GO:0015074`
- DNA recombination — `GO:0006310`
- DNA damage response — `GO:0006974`
- response to DNA damage stimulus — `GO:0006974`
- viral genome integration into host DNA — use a verified ontology term only after checking the current GO release
- lysogenic repression / repression of lytic transcription — label-only candidate
- vertical inheritance of prophage DNA — label-only candidate
- site-specific recombination — label-only if a release-verified GO identifier is unavailable
- prophage excision; in situ prophage replication; phage DNA packaging; bacterial-cell lysis; lysogenic conversion; superinfection exclusion — label-only candidates pending ontology verification

### Environmental and experimental factors

- DNA damage/genotoxic stress
- mitomycin C — `CHEBI:27504`
- ciprofloxacin — `CHEBI:100241`
- quinolone exposure, UV radiation, oxidative stress, and some antibiotics — contextual induction factors; effects are phage- and host-dependent
- spontaneous induction/noise — label-only
- high-fructose diet — reported to increase prophage-particle release by *Lactobacillus reuteri*, but should remain an uncertain ecological edge rather than a core mechanism (pei2024auniverseof pages 13-15)

### Host-effect nodes

- superinfection immunity/exclusion
- toxin production and virulence
- antimicrobial-resistance-gene carriage
- oxidative-, acid-, and osmotic-stress tolerance
- antibiotic tolerance
- early biofilm formation
- host-gene disruption
- restriction–modification-system disruption
- altered DNA methylation/methylome
- horizontal gene transfer and specialized transduction

These outcomes are **possible effects of particular prophages**, not defining features of every prophage-positive organism.

## 3. Candidate causal edges

The table below gives the most actionable edges. “Core” means suitable for the central graph, “conditional” means common but not universal, and “contextual” means taxon-, element-, or assay-specific.

| subject | predicate | object | evidence tier (core/conditional/contextual) | taxon or scope | DOI/year | concise supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| CI repressor | represses | phage lytic genes / lysogenic state maintenance | core | temperate prophages, especially lambdoid/staphylococcal models | 10.1099/mgen.0.000330 (2020); 10.1038/s41467-023-42413-0 (2023) | “the synthesis of a single protein, the CI repressor, is sufficient to maintain the lysogenic state” and prophages are maintained by “repression of phage lytic genes” (owen2020awindowinto pages 1-2, vale2024genecontentphage pages 1-2) | Strongly curatable as a central maintenance edge; phrasing should remain generic, with CI as a model-specific repressor family label rather than universal to all temperate phages. |
| DNA damage / SOS response | activates | RecA* | core | bacterial SOS-mediated prophage induction | 10.1038/s41467-023-42413-0 (2023) | “DNA damage activates RecA*, which catalyzes CI repressor autocleavage” (thabet2023theclpxprotease pages 10-11) | Use GO label for SOS response if desired; RecA* is an activated conformational state, so may need label-only node or note on statefulness. |
| RecA* | promotes autocleavage of | CI repressor | core | *Staphylococcus aureus* prophage Φ11/80α model; canonical SOS induction logic | 10.1038/s41467-023-42413-0 (2023) | “RecA*-mediated initial CI autocleavage requires SOS induction” and “DNA damage activates RecA*, which catalyzes CI repressor autocleavage” (thabet2023theclpxprotease pages 6-8, thabet2023theclpxprotease pages 10-11) | Excellent direct mechanistic edge; taxon-specific experiment but broadly canonical. |
| ClpX protease | inactivates / removes | CI N-terminal DNA-binding fragment | core | *S. aureus* prophage Φ11/80α | 10.1038/s41467-023-42413-0 (2023) | “ClpX acts post-SOS by binding to the N-terminal domain (NTD) of autocleaved CI repressor and inactivating its DNA-binding capacity” (thabet2023theclpxprotease pages 11-12) | Strong 2023 mechanistic update; curate with taxon note because ClpX dependence is not yet established as universal. |
| CI NTD inactivation / prophage derepression | enables | prophage induction / lytic development | core | *S. aureus* prophage Φ11/80α | 10.1038/s41467-023-42413-0 (2023) | “ClpX removal of CI-NTD is required for completing lytic development” and is “sufficient for prophage activation after SOS-mediated CI auto-cleavage” (thabet2023theclpxprotease pages 6-8, thabet2023theclpxprotease pages 8-8) | Best represented as derepression → induction; in *S. aureus* this precedes in situ replication/excision. |
| Integrase + attP/attB sites | mediates site-specific recombination for | prophage integration | core | temperate phages / genomic islands broadly; supported in helper-embedded satellite literature and integrase biology | 10.1093/nargab/lqad036 (2023); 10.1016/j.jmb.2003.09.082 (2004) | “Each GI usually encodes an integrase that specifies its chromosomal integration (attachment) site, attB, and the corresponding site in the GI, attP. Integration converts attB and attP into… attL and attR” (tommasini2023helperembeddedsatellitesfrom pages 1-2) | Curate as a general integration mechanism; satellite paper is not a prophage per se but accurately states site-specific integrase logic shared with prophages. |
| Excisionase / RDF + integrase | promotes | prophage excision | conditional | temperate phages and related genomic islands; not directly demonstrated for trait in a single prophage paper here | 10.1093/nargab/lqad036 (2023); 10.1016/j.jmb.2003.09.082 (2004) | “AlpA… [relatives] are also known as recombination directionality factors or excisionases” and “In the presence of integrase and excisionase…” recombination can reverse (tommasini2023helperembeddedsatellitesfrom pages 1-2) | Mechanistically standard but evidence here is partly from satellites/reviews; mark conditional unless a prophage-specific direct experiment is added. |
| Prophage insertion | disrupts | host genes | contextual | *Helicobacter pylori* complete clinical genomes | 10.1080/19490976.2024.2379440 (2024) | “Prophage insertion occasionally results in gene disruption” and “14.8%… of all H. pylori prophage insertion sites” had flanking pseudogenes (vale2024genecontentphage pages 1-2, vale2024genecontentphage pages 8-9) | Strong genomic consequence edge; phenotype consequence may vary by insertion site. |
| Prophage insertion disrupting RM genes | changes | host methylome / epigenome | contextual | *H. pylori* | 10.1080/19490976.2024.2379440 (2024) | “62.5% (15/24) of the prophage genomes flanked by RM genes present RM disruption, disrupting bacterial genomic methylation” (vale2024genecontentphage pages 8-9) | Curate as taxon-specific, high-value host-effect edge; likely best linked through RM system disruption node. |
| STnc6030 antisense RNA | mediates | superinfection exclusion of phage BTP1 | contextual | *Salmonella enterica* serovar Typhimurium D23580, prophage BTP1 | 10.1099/mgen.0.000330 (2020) | “we identify a novel antisense RNA species in prophage BTP1, STnc6030, which mediates superinfection exclusion of phage BTP1” (owen2020awindowinto pages 1-2) | Strong direct accessory-function edge, but highly element-specific; should be curated as a possible accessory branch, not core to all prophages. |
| Cryptic prophage genes (e.g., KilR, DicB) | increase resistance to | quinolone and β-lactam stress | contextual | defective/cryptic prophages in *E. coli* K-12 | 10.1038/ncomms1146 (2010) | “cryptic prophages contribute significantly to resistance to sub-lethal concentrations of quinolone and β-lactam antibiotics primarily through proteins that inhibit cell division” (wang2010crypticprophageshelp pages 1-2) | Important but defective-prophage specific; do not generalize to intact prophage trait without caution. |
| Cryptic prophage genes (e.g., YfdK/YfdO/YfdS; e14/rac factors) | enhance | oxidative stress resistance / acid resistance / early biofilm formation | contextual | defective/cryptic prophages in *E. coli* K-12 | 10.1038/ncomms1146 (2010) | “YfdK, YfdO and YfdS enhanced resistance to oxidative stress… e14, CPS-53 and CP4-57 increased resistance to acid, and e14 and rac proteins increased early biofilm formation” (wang2010crypticprophageshelp pages 1-2) | Valuable host-benefit branch, but specifically for cryptic/defective prophages; mark outside strict core scope of intact prophage carriage. |


*Table: This table compiles the strongest candidate causal edges for curating the prophage trait graph, emphasizing core lysogeny and induction mechanisms plus contextual host-effect branches. It distinguishes broadly curatable mechanisms from taxon-specific, satellite-derived, or defective-prophage evidence.*

### Additional recommended triples

| Subject | Predicate | Object | Evidence and supporting snippet | Curation assessment |
|---|---|---|---|---|
| temperate-phage genome | **integrates_into** | bacterial chromosome | Temperate phages “follow the lysogenic cycle integrating into the bacterial genome to become a prophage” (DOI 10.1080/19490976.2024.2379440, published August 2024) (vale2024genecontentphage pages 1-2) | **Core**, while permitting a separate episomal-maintenance route. |
| chromosomally integrated prophage | **is_vertically_inherited_with** | host chromosome | “The prophages are vertically inherited during cell division” (vale2024genecontentphage pages 1-2) | **Core.** |
| CI-like repressor | **represses** | lytic-gene transcription | Stable prophages require most genes to be repressed; CI is sufficient in the lambda model (DOI 10.1099/mgen.0.000330, published February 5, 2020) (owen2020awindowinto pages 1-2) | **Core architecture**, but CI-like identity is not universal. |
| lytic-gene repression | **maintains** | lysogenic state | The *H. pylori* report states that lysogeny is maintained by “repression of phage lytic genes” (vale2024genecontentphage pages 1-2) | **Core.** |
| prophage carriage | **enables_expression_of** | accessory/moron loci | Although most phage genes are repressed, accessory loci are often highly expressed; 40 of 278 genes across five *Salmonella* prophages exceeded 100 TPM in at least one lysogenic condition (owen2020awindowinto pages 9-11, owen2020awindowinto pages 1-2) | **Conditional.** Do not imply every prophage has an expressed accessory locus. |
| DNA damage | **activates** | RecA* | “DNA damage activates RecA*” in the Φ11/80α induction model (DOI 10.1038/s41467-023-42413-0, published October 2023) (thabet2023theclpxprotease pages 8-8, thabet2023theclpxprotease pages 10-11) | **Core induction branch** for SOS-responsive systems, not all prophages. |
| RecA* | **promotes_autocleavage_of** | CI repressor | Directly supported in *S. aureus* lysogens (thabet2023theclpxprotease pages 6-8, thabet2023theclpxprotease pages 10-11) | **Strong, conditional.** |
| cleaved CI N-terminal fragment | **retains** | operator DNA-binding/repression | CI-NTD accumulated in ΔclpX cells and repressed the cro promoter (thabet2023theclpxprotease pages 6-8) | **Strong, taxon/model-specific.** |
| ClpX | **binds_and_inactivates** | cleaved CI N-terminal fragment | ClpX acts after SOS and removes residual repression; fragment accumulation caused a >5-log reduction in phage titre in the tested background (thabet2023theclpxprotease pages 6-8, thabet2023theclpxprotease pages 11-12) | **Strong 2023 edge; mark Φ11/80α-specific.** |
| loss of lytic repression | **causes** | prophage induction | ClpX-mediated CI-NTD inactivation completed prophage activation (thabet2023theclpxprotease pages 6-8, thabet2023theclpxprotease pages 8-8) | **Core logical edge.** |
| prophage induction | **precedes** | replication, packaging/excision, and progeny release | Φ11/80α use an RPE—replication, packaging, excision—rather than a universal excision-first order (thabet2023theclpxprotease pages 3-4) | **Do not impose one universal event order.** |
| prophage integration | **may_disrupt** | host gene | In *H. pylori*, 109 of 736 genes flanking prophages were pseudogenes, corresponding to 14.8% of insertion-site flanks (DOI 10.1080/19490976.2024.2379440) (vale2024genecontentphage pages 8-9) | **Contextual but strong genomic evidence.** |
| prophage-mediated RM-gene disruption | **alters** | host methylation pattern | Fifteen of 24 prophages flanked by restriction–modification genes showed RM disruption associated with altered genomic methylation (vale2024genecontentphage pages 8-9) | **Strong, *H. pylori*-specific.** |
| STnc6030 | **mediates** | BTP1 superinfection exclusion | Directly identified as a BTP1 antisense RNA mediating exclusion (owen2020awindowinto pages 1-2) | **Strong, element-specific.** |
| cryptic prophage KilR/DicB | **inhibits** | cell division under antibiotic exposure | The nine-prophage deletion strain had a 2.1-fold lower nalidixic-acid MIC99 and 379-fold lower viability at 2 μg/mL; CP4-6 and rac deletions reduced survival 33- and 41-fold (DOI 10.1038/ncomms1146, published December 21, 2010) (wang2010crypticprophageshelp pages 1-2, wang2010crypticprophageshelp pages 2-3) | **Contextual; defective prophages and *E. coli* K-12 only.** |

## 4. Recent developments and quantitative evidence

### 2023: an added proteolytic step in prophage induction

Thabet, Penadés, and Haag resolved why CI autocleavage may not fully derepress staphylococcal prophages. In Φ11 and 80α lysogens, the cleaved CI N-terminal domain retained DNA-binding activity. ClpX specifically recognized this fragment, relieved cro-promoter repression, and enabled productive induction. ΔclpX reduced spontaneous release by more than 2 logs, while forced accumulation of the fragment caused a greater than 5-log titre reduction. The work distinguishes ClpX’s post-SOS role from ClpP’s upstream contribution to staphylococcal SOS activation (thabet2023theclpxprotease pages 6-8, thabet2023theclpxprotease pages 3-4, thabet2023theclpxprotease pages 11-12). This should be curated as a taxon-qualified mechanistic refinement, not as a universal prophage step.

### 2024: global gut-prophage landscape

Pei and colleagues analyzed 43,942 bacterial genomes representing 439 species and 12 phyla. They detected 105,613 prophage regions in approximately 92% of genomes, but only 16,254 complete prophages in approximately 24% of bacteria. About 4% had predicted cross-genus integration capacity and approximately 17% had inferred host ranges spanning 2–35 genera. ARGs and toxin-related genes occurred in approximately 2.5% and 5.8% of predicted prophages, respectively, and approximately 72% of nonredundant prophage genomes were previously unreported (DOI 10.1080/19490976.2024.2309684, published February 2024) (pei2024auniverseof pages 13-15, pei2024auniverseof pages 1-2). These are computational predictions affected by database composition and should not be interpreted as functional carriage or mobilization rates.

### 2024: completeness, decay, and epigenomic effects in *H. pylori*

Among 1,011 clinical genomes from 50 countries, 298 genomes (29.5%) contained 368 prophage sequences; only 96 of the 298 prophage-positive genomes (32.2%) contained a complete prophage. Prevalence differed by geography and ancestry but not by human-host disease status. Prophage insertion disrupted genes at 14.8% of insertion-site flanks, and 15/24 prophages adjacent to restriction–modification systems disrupted an RM gene, sometimes eliminating its methylation target signal. Rearrangement, mobile-element merger, and pseudogene accumulation were proposed as inactivation mechanisms (DOI 10.1080/19490976.2024.2379440, received March 24, accepted July 8, published August 2024) (vale2024genecontentphage pages 8-9, vale2024genecontentphage pages 1-2). The cycle-regulation model is primarily comparative-genomic and awaits wet-lab validation.

### 2024: population-scale transmission diversity

An *Acinetobacter baumannii* analysis included 4,152 prophages plus 122 virulent phages from 46 countries. Using an operational species threshold of 95% nucleotide identity over 90% coverage, 875 of 963 prophage species (91%) had four or fewer members; only five species exceeded 100 members. Most were host-range-restricted and geographically limited, while a few broad-host-range species were cosmopolitan and abundant. Polylysogens commonly carried divergent prophages, and gains and losses occurred within bacterial lineages (DOI 10.1128/mbio.02377-24, published October 2024) (tenoriocarnalla2024hostpopulationstructure pages 1-2). This argues against representing “prophage” as one homogeneous genomic module.

## 5. Current applications and implementations

1. **Genome surveillance and strain typing.** Prophage presence, insertion sites, and cargo help resolve bacterial lineages, transmission, and genome plasticity. Closed genomes are preferable because fragmented assemblies obscure boundaries, module order, and whether apparent pieces belong to one element (tenoriocarnalla2024hostpopulationstructure pages 1-2, vale2024genecontentphage pages 1-2).
2. **Virulence and AMR risk assessment.** Complete prophage reconstruction can identify toxin, immune-evasion, and resistance cargo. However, the gut survey’s 2.5% ARG and 5.8% toxin frequencies are annotation results, not evidence that the genes are expressed or transferable (pei2024auniverseof pages 13-15, pei2024auniverseof pages 1-2).
3. **Phage-therapy design and safety.** Candidate therapeutic phages should be screened for temperate lifestyle, repressors/integrases, toxin or AMR cargo, and transduction potential. Resident prophages and superinfection-exclusion systems can also determine whether a treatment phage infects a strain.
4. **Microbiome ecology.** Prophage induction can alter bacterial abundance, release cellular DNA and metabolites, and reshape competition. Current gut data reveal enormous unexplored diversity but remain prediction-heavy; approximately 72% of nonredundant gut prophages were previously unreported (pei2024auniverseof pages 1-2).
5. **Functional discovery with transcriptomics.** RNA-seq distinguishes highly expressed lysogenic accessory loci from repressed structural genes. In five *Salmonella* prophages, only 14% of genes were highly expressed under at least one tested condition, enriching for known regulators/accessory genes and revealing STnc6030 (owen2020awindowinto pages 9-11, owen2020awindowinto pages 1-2).
6. **Synthetic biology.** Phage integrases and RDFs provide precise, directional DNA integration and excision systems. Nevertheless, this application supports integrase mechanism rather than the microbial prophage trait itself; synthetic constructs should not automatically be annotated as prophages.

## 6. Expert interpretation

The most defensible graph architecture is a **small conserved core plus qualified branches**:

- **Core:** temperate-phage genome → integration or episomal maintenance → lytic-gene repression → stable lysogeny/vertical inheritance → `traitmech:000091`.
- **Conditional induction branch:** genotoxic stress → SOS/RecA* → repressor inactivation → derepression → productive phage development.
- **Optional host-effect branches:** accessory-locus expression, superinfection exclusion, gene disruption, methylome alteration, stress tolerance, toxins, and AMR.
- **Decay branch:** mutation/rearrangement/deletion or mobile-element insertion → incomplete/cryptic prophage → loss of productive cycle, possibly with retained host functions.

This structure reflects the authoritative view that most prophage genes are repressed during lysogeny while accessory loci may remain active, and it avoids the common error of making virulence or inducibility defining properties (vale2024genecontentphage pages 1-2, owen2020awindowinto pages 1-2). It also accommodates biological diversity: only 43% of one large prediction set had annotated integrases, and nearly half of its ORFs lacked annotation, so absence of one canonical marker is not decisive (kang2017prophagegenomicsreveals pages 4-7).

## 7. Warnings: claims not yet ready for TraitMech curation

- **Do not curate “all bacterial genomes contain prophages.”** Estimates range widely by taxon, assembly quality, database composition, and algorithm: approximately 92% in the selected gut collection, 82.76% in an older broad computational survey, and 29.5% in closed *H. pylori* genomes (pei2024auniverseof pages 1-2, kang2017prophagegenomicsreveals pages 4-7, vale2024genecontentphage pages 1-2).
- **Do not equate predicted region with intact inducible prophage.** Only 32.2% of prophage-positive *H. pylori* genomes contained complete elements; incomplete predictions can be remnants or false boundary calls (vale2024genecontentphage pages 1-2).
- **Do not require an annotated integrase.** Only 43% of predictions in a large survey had one, reflecting alternative mechanisms, decay, or annotation failure (kang2017prophagegenomicsreveals pages 4-7).
- **Do not make SOS/RecA universal.** Some prophages use different sensors, antirepressors, or regulatory switches.
- **Do not universalize ClpX.** The compelling 2023 evidence concerns *S. aureus* Φ11 and 80α (thabet2023theclpxprotease pages 6-8, thabet2023theclpxprotease pages 11-12).
- **Do not impose excision-before-replication.** Φ11/80α can replicate while integrated and follow an RPE order (thabet2023theclpxprotease pages 3-4).
- **Do not make AMR, toxin carriage, biofilm, or stress tolerance necessary consequences.** These are accessory and often rare or strain-specific. The strongest stress/biofilm evidence here is from defective *E. coli* K-12 elements (wang2010crypticprophageshelp pages 1-2, wang2010crypticprophageshelp pages 2-3).
- **Do not treat PICIs as prophages.** They are helper-dependent satellites even when integrated within a helper prophage and carrying integrase/excision machinery (tommasini2023helperembeddedsatellitesfrom pages 1-2).
- **Do not infer phenotype solely from cargo annotation.** Expression, protein function, element completeness, mobility, and host background require validation.
- **Avoid unverified ontology identifiers.** Use label-only nodes where a current ontology release has not been checked; never manufacture CURIEs.

## DOI-first bibliography

1. Thabet MA, Penadés JR, Haag AF. “The ClpX protease is essential for inactivating the CI master repressor and completing prophage induction in *Staphylococcus aureus*.” *Nature Communications* 14 (October 2023). DOI: [10.1038/s41467-023-42413-0](https://doi.org/10.1038/s41467-023-42413-0). (thabet2023theclpxprotease pages 6-8)
2. Vale FF et al. “Gene content, phage cycle regulation model and prophage inactivation disclosed by prophage genomics in the *Helicobacter pylori* Genome Project.” *Gut Microbes* 16 (August 2024; accepted July 8, 2024). DOI: [10.1080/19490976.2024.2379440](https://doi.org/10.1080/19490976.2024.2379440). (vale2024genecontentphage pages 8-9, vale2024genecontentphage pages 1-2)
3. Pei Z et al. “A universe of human gut-derived bacterial prophages: unveiling the hidden viral players in intestinal microecology.” *Gut Microbes* 16 (February 2024). DOI: [10.1080/19490976.2024.2309684](https://doi.org/10.1080/19490976.2024.2309684). (pei2024auniverseof pages 13-15, pei2024auniverseof pages 1-2)
4. Tenorio-Carnalla K et al. “Host population structure and species resolution reveal prophage transmission dynamics.” *mBio* 15 (October 2024). DOI: [10.1128/mbio.02377-24](https://doi.org/10.1128/mbio.02377-24). (tenoriocarnalla2024hostpopulationstructure pages 1-2)
5. Tommasini D, Mageeney CM, Williams KP. “Helper-embedded satellites from an integrase clade that repeatedly targets prophage late genes.” *NAR Genomics and Bioinformatics* 5 (published online April 18, 2023). DOI: [10.1093/nargab/lqad036](https://doi.org/10.1093/nargab/lqad036). (tommasini2023helperembeddedsatellitesfrom pages 1-2)
6. Owen SV et al. “A window into lysogeny: revealing temperate phage biology with transcriptomics.” *Microbial Genomics* 6 (published February 5, 2020). DOI: [10.1099/mgen.0.000330](https://doi.org/10.1099/mgen.0.000330). (owen2020awindowinto pages 9-11, owen2020awindowinto pages 1-2)
7. Wang X et al. “Cryptic prophages help bacteria cope with adverse environments.” *Nature Communications* 1:147 (published December 21, 2010). DOI: [10.1038/ncomms1146](https://doi.org/10.1038/ncomms1146). (wang2010crypticprophageshelp pages 1-2, wang2010crypticprophageshelp pages 2-3)
8. Bobay L-M, Touchon M, Rocha EPC. “Pervasive domestication of defective prophages by bacteria.” *Proceedings of the National Academy of Sciences* 111:12127–12132 (August 2014). DOI: [10.1073/pnas.1405336111](https://doi.org/10.1073/pnas.1405336111). (bobay2014pervasivedomesticationof pages 1-2)
9. Kang HS et al. “Prophage genomics reveals patterns in phage genome organization and replication.” *bioRxiv* (March 2017; preprint). DOI: [10.1101/114819](https://doi.org/10.1101/114819). Use as supporting computational evidence rather than a primary mechanistic authority. (kang2017prophagegenomicsreveals pages 1-4, kang2017prophagegenomicsreveals pages 4-7, kang2017prophagegenomicsreveals pages 7-10)

References

1. (thabet2023theclpxprotease pages 6-8): Mohammed A. Thabet, José R. Penadés, and Andreas F. Haag. The clpx protease is essential for inactivating the ci master repressor and completing prophage induction in staphylococcus aureus. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42413-0, doi:10.1038/s41467-023-42413-0. This article has 13 citations and is from a highest quality peer-reviewed journal.

2. (thabet2023theclpxprotease pages 11-12): Mohammed A. Thabet, José R. Penadés, and Andreas F. Haag. The clpx protease is essential for inactivating the ci master repressor and completing prophage induction in staphylococcus aureus. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42413-0, doi:10.1038/s41467-023-42413-0. This article has 13 citations and is from a highest quality peer-reviewed journal.

3. (thabet2023theclpxprotease pages 10-11): Mohammed A. Thabet, José R. Penadés, and Andreas F. Haag. The clpx protease is essential for inactivating the ci master repressor and completing prophage induction in staphylococcus aureus. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42413-0, doi:10.1038/s41467-023-42413-0. This article has 13 citations and is from a highest quality peer-reviewed journal.

4. (pei2024auniverseof pages 1-2): Zhangming Pei, Yufei Liu, Yutao Chen, Tong Pan, Xihao Sun, Hongchao Wang, R. Paul Ross, Wenwei Lu, and Wei Chen. A universe of human gut-derived bacterial prophages: unveiling the hidden viral players in intestinal microecology. Gut Microbes, Feb 2024. URL: https://doi.org/10.1080/19490976.2024.2309684, doi:10.1080/19490976.2024.2309684. This article has 56 citations and is from a peer-reviewed journal.

5. (vale2024genecontentphage pages 1-2): Filipa F. Vale, Hp GP Research Network, R. J. Roberts, Ichizo Kobayashi, M. H, C. Rabkin, Difei Wang, B. Hicks, Bin Zhu, Meredith Yeager, A. Hutchinson, Kedest Teshome, Kristie Jones, Wen Luo, Alisa M. Goldstein, Nan Hu, Philip R. Taylor, Minkyo Song, A. Gutiérrez-Escobar, Kai Yu, C. Abnet, S. Chanock, M. Constanza, J. Romero-Gallo, U. Krishna, R. Peek, M. Piazuelo, Keith T. Wilson, J. Loh, T. Cover, Naïma Raaf, Hafeza Aftab, J. Akada, Takashi Matsumoto, Yoshio Yamaoka, F. Haesebrouck, T. Bartelli, Diana N. Nunes, A. Pelosof, C. Zitron, Emmanuel Dias-Neto, Paulo Pimentel de Assumpção, I. Tishkov, Karen J. Goodman, Janis Geary, Taylor J Cromarty, Nancy L. Price, Douglas Quilty, Alejandro H. Corvalán, Carolina A Serrano, Robinson Gonzalez, Arnoldo Riquelme, Francisco Castillo, M. Bravo, Alvaro Pazos, Luis Eduardo Bravo, James G. Fox, Vanessa Ramírez-Mayorga, S. Molina-Castro, Sundry Durán-Bermúdez, Christian Campos-Núñez, Manuel Chaves-Cervantes, E. Tshibangu-Kabamba, G. Disashi, Tumba, Antoine Tshimpi-Wola, Patrick de, Jesus Ngoma-Kisoko, Dieudonné N Mumba, Ngoyi, D. M. Ngoyi, M. Cruz, Celso Hosking, J. Abreu, C. Varon, L. Bénejat, Quentin Jehanne, P. Lehours, Francis Mégraud, Ousman Secka, Alexander Link, P. Malfertheiner, M. B. Adinortey, A. Bockarie, C. Adinortey, E. Ofori, D. Sgouras, B. Martinez-Gonzalez, S. Michopoulos, Sotirios Georgopoulos, Elisa Hernandez, R. Domínguez, Douglas R. Morgan, H. Harðardóttir, A. I. Gunnarsdottir, Hallgrímur Guðjónsson, Jón Gunnlaugur, Einar S. Björnsson, M. Ballal, V. Shetty, M. Miftahussurur, Titong Sugihartono, R. Alfaray, Langgeng Agung, Waskito Kartika, Afrida Fauzia, Ari Fahrial, Hasan Maulahela, Reza Malekzadeh, M. Sotoudeh, Avi Peretz, M. Azrad, Avi On, V. Re, Stefania Zanussi, R. Cannizzaro, Vincenzo Canzonieri, T. Shimura, Kengo Tokunaga, T. Osaki, Shigeru Kamiya, Khaled Jadallah, Ismail Matalka, Igissin Nurbek Sagynbekuly, Mariia Satarovna, Attokurova Rakhat, Il-Ju Choi, Jae Gyu Kim, Nayoung Kim, M. Leja, Aigars Vanags, G. Skenders, D. Rudzīte, J. Vadivelu, Mun Fai, Loke Kumutha, Malar Vellasamy, R. Herrera-Goepfert, J. Alonso-Lárraga, Than Than, Kyaw Htet, T. Matsuhisa, Pradeep Krishna, Shrestha, Shamshul Ansari, O. Abiodun, Christopher Jemilohun, K. Akande, F. Magaji, A. Omotoso, U. Okonkwo, C. C. Osuagwu, Opeyemi O. Owoseni, Carlos A. Castaneda, Miluska Castillo, Billie Velapatiño, Robert H. Gilman, P. Krzyżek, Grażyna Gościniak, D. Pawełka, Izabela Korona-Glowniak, Halina Cichoż-Lach, Instituto Nacional de Saúde Dr, Ricardo Jorge, Lisboa, Portugal Monica, Oleastro, Ceu Figueiredo, Jose C. Machado, Rui M. Ferreira, Dmitry S. Bordin, M. Livzan, V. Tsukanov, Patrick Tan, Khay Guan, Feng Zhu, Yeoh, Reid Ally, Rainer Haas, W. Fischer, Milagrosa Montes, María Fernández-Reyes, E. Tamayo, Jacobo Lizasoain, L. Bujanda, Sergio Lario, M. J. Ramírez-Lázaro, X. Calvet, E. Brunet-Mas, M. Domper-Arnal, S. García-Mateo, Daniel Abad-Baroja, J. Botargués, I. Pérez-Martínez, E. Barreiro-Alonso, Javier P. Gisbert, Edurne Amorena Muro, Pedro Linares, Laura Alcoba, Vicente Martín, T. Fleitas-Kanonnikoff, H. Altayeb, Lars Engstrand, H. Enroth, Peter M. Keller, Karoline Wagner, Daniel Pohl, Yi-Chia Lee, Jyh-Ming Liou, Ming-Shiang Wu, B. Kocazeybek, S. Sarıbaş, I. Tasci, S. Demiryas, N. Kepil, Luis Quiel, Miguel Villagra, Morgan Norton, Deborah Johnson, Robert J. Huang, Joo Ha Hwang, Wendy Szymczak, S. Rajagopalan, Emmanuel Asare, William R. Jacobs, Haejin In, R. Bollag, Aileen Lopez, Edward J. Kruse, Joseph White, D. Y. Graham, Charlotte Lane, Yang Gao, Benjamin D. Gold, Marcia Cruz-Correa, María González-Pons, Luz M. Rodriguez, V. Phước, Ho Tuan, Dang Quy Dung, T. Thành, Binh, Tran Thi Huyen, T. Vũ, Van Khien, Xiongfong Chen, Yongmei Zhao, C. Raley, Bailey Kessing, Bao Tran, Yukako Katsura, Patricio Gonzalez-Hormazabal, Xavier Didelot, Sam Sheppard, E. Tarazona-Santos, Roxana Zamudio, Leonardo Mariño-Ramírez, S. Backert, Michael Naumann, A. Smet, Douglas E. Berg, Á. Chiner-Oms, Koji Yahara, Martin J. Blaser, Tamas Vincze, Richard D. Morgan, J. P. Dekker, J. Torres, Mehwish Noureen, Joshua L. Cherry, Naoki Osada, Masaki Fukuyo, Masanori Arita, Santiago Sandoval-Motta, Rajiv Boscolo, S. Ghirotto, Zilia Y. Muñoz-Ramírez, Roberto C. Torres, D. Falush, Kaisa Thorell, and I. Uchiyama. Gene content, phage cycle regulation model and prophage inactivation disclosed by prophage genomics in the helicobacter pylori genome project. Gut Microbes, Aug 2024. URL: https://doi.org/10.1080/19490976.2024.2379440, doi:10.1080/19490976.2024.2379440. This article has 15 citations and is from a peer-reviewed journal.

6. (owen2020awindowinto pages 1-2): Siân V. Owen, Rocío Canals, Nicolas Wenner, Disa L. Hammarlöf, Carsten Kröger, and Jay C. D. Hinton. A window into lysogeny: revealing temperate phage biology with transcriptomics. Microbial Genomics, Feb 2020. URL: https://doi.org/10.1099/mgen.0.000330, doi:10.1099/mgen.0.000330. This article has 73 citations and is from a peer-reviewed journal.

7. (bobay2014pervasivedomesticationof pages 1-2): Louis-Marie Bobay, Marie Touchon, and Eduardo P. C. Rocha. Pervasive domestication of defective prophages by bacteria. Proceedings of the National Academy of Sciences, 111:12127-12132, Aug 2014. URL: https://doi.org/10.1073/pnas.1405336111, doi:10.1073/pnas.1405336111. This article has 465 citations and is from a highest quality peer-reviewed journal.

8. (tommasini2023helperembeddedsatellitesfrom pages 1-2): Dario Tommasini, Catherine M Mageeney, and Kelly P Williams. Helper-embedded satellites from an integrase clade that repeatedly targets prophage late genes. NAR Genomics and Bioinformatics, Mar 2023. URL: https://doi.org/10.1093/nargab/lqad036, doi:10.1093/nargab/lqad036. This article has 8 citations and is from a peer-reviewed journal.

9. (thabet2023theclpxprotease pages 3-4): Mohammed A. Thabet, José R. Penadés, and Andreas F. Haag. The clpx protease is essential for inactivating the ci master repressor and completing prophage induction in staphylococcus aureus. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42413-0, doi:10.1038/s41467-023-42413-0. This article has 13 citations and is from a highest quality peer-reviewed journal.

10. (kang2017prophagegenomicsreveals pages 4-7): Han Suh Kang, Katelyn McNair, Daniel A. Cuevas, Barbara A. Bailey, Anca M. Segall, and Robert A. Edwards. Prophage genomics reveals patterns in phage genome organization and replication. bioRxiv, Mar 2017. URL: https://doi.org/10.1101/114819, doi:10.1101/114819. This article has 52 citations.

11. (wang2010crypticprophageshelp pages 1-2): Xiaoxue Wang, Younghoon Kim, Qun Ma, Seok Hoon Hong, Karina Pokusaeva, Joseph M. Sturino, and Thomas K. Wood. Cryptic prophages help bacteria cope with adverse environments. Nature Communications, Dec 2010. URL: https://doi.org/10.1038/ncomms1146, doi:10.1038/ncomms1146. This article has 816 citations and is from a highest quality peer-reviewed journal.

12. (pei2024auniverseof pages 13-15): Zhangming Pei, Yufei Liu, Yutao Chen, Tong Pan, Xihao Sun, Hongchao Wang, R. Paul Ross, Wenwei Lu, and Wei Chen. A universe of human gut-derived bacterial prophages: unveiling the hidden viral players in intestinal microecology. Gut Microbes, Feb 2024. URL: https://doi.org/10.1080/19490976.2024.2309684, doi:10.1080/19490976.2024.2309684. This article has 56 citations and is from a peer-reviewed journal.

13. (thabet2023theclpxprotease pages 8-8): Mohammed A. Thabet, José R. Penadés, and Andreas F. Haag. The clpx protease is essential for inactivating the ci master repressor and completing prophage induction in staphylococcus aureus. Nature Communications, Oct 2023. URL: https://doi.org/10.1038/s41467-023-42413-0, doi:10.1038/s41467-023-42413-0. This article has 13 citations and is from a highest quality peer-reviewed journal.

14. (vale2024genecontentphage pages 8-9): Filipa F. Vale, Hp GP Research Network, R. J. Roberts, Ichizo Kobayashi, M. H, C. Rabkin, Difei Wang, B. Hicks, Bin Zhu, Meredith Yeager, A. Hutchinson, Kedest Teshome, Kristie Jones, Wen Luo, Alisa M. Goldstein, Nan Hu, Philip R. Taylor, Minkyo Song, A. Gutiérrez-Escobar, Kai Yu, C. Abnet, S. Chanock, M. Constanza, J. Romero-Gallo, U. Krishna, R. Peek, M. Piazuelo, Keith T. Wilson, J. Loh, T. Cover, Naïma Raaf, Hafeza Aftab, J. Akada, Takashi Matsumoto, Yoshio Yamaoka, F. Haesebrouck, T. Bartelli, Diana N. Nunes, A. Pelosof, C. Zitron, Emmanuel Dias-Neto, Paulo Pimentel de Assumpção, I. Tishkov, Karen J. Goodman, Janis Geary, Taylor J Cromarty, Nancy L. Price, Douglas Quilty, Alejandro H. Corvalán, Carolina A Serrano, Robinson Gonzalez, Arnoldo Riquelme, Francisco Castillo, M. Bravo, Alvaro Pazos, Luis Eduardo Bravo, James G. Fox, Vanessa Ramírez-Mayorga, S. Molina-Castro, Sundry Durán-Bermúdez, Christian Campos-Núñez, Manuel Chaves-Cervantes, E. Tshibangu-Kabamba, G. Disashi, Tumba, Antoine Tshimpi-Wola, Patrick de, Jesus Ngoma-Kisoko, Dieudonné N Mumba, Ngoyi, D. M. Ngoyi, M. Cruz, Celso Hosking, J. Abreu, C. Varon, L. Bénejat, Quentin Jehanne, P. Lehours, Francis Mégraud, Ousman Secka, Alexander Link, P. Malfertheiner, M. B. Adinortey, A. Bockarie, C. Adinortey, E. Ofori, D. Sgouras, B. Martinez-Gonzalez, S. Michopoulos, Sotirios Georgopoulos, Elisa Hernandez, R. Domínguez, Douglas R. Morgan, H. Harðardóttir, A. I. Gunnarsdottir, Hallgrímur Guðjónsson, Jón Gunnlaugur, Einar S. Björnsson, M. Ballal, V. Shetty, M. Miftahussurur, Titong Sugihartono, R. Alfaray, Langgeng Agung, Waskito Kartika, Afrida Fauzia, Ari Fahrial, Hasan Maulahela, Reza Malekzadeh, M. Sotoudeh, Avi Peretz, M. Azrad, Avi On, V. Re, Stefania Zanussi, R. Cannizzaro, Vincenzo Canzonieri, T. Shimura, Kengo Tokunaga, T. Osaki, Shigeru Kamiya, Khaled Jadallah, Ismail Matalka, Igissin Nurbek Sagynbekuly, Mariia Satarovna, Attokurova Rakhat, Il-Ju Choi, Jae Gyu Kim, Nayoung Kim, M. Leja, Aigars Vanags, G. Skenders, D. Rudzīte, J. Vadivelu, Mun Fai, Loke Kumutha, Malar Vellasamy, R. Herrera-Goepfert, J. Alonso-Lárraga, Than Than, Kyaw Htet, T. Matsuhisa, Pradeep Krishna, Shrestha, Shamshul Ansari, O. Abiodun, Christopher Jemilohun, K. Akande, F. Magaji, A. Omotoso, U. Okonkwo, C. C. Osuagwu, Opeyemi O. Owoseni, Carlos A. Castaneda, Miluska Castillo, Billie Velapatiño, Robert H. Gilman, P. Krzyżek, Grażyna Gościniak, D. Pawełka, Izabela Korona-Glowniak, Halina Cichoż-Lach, Instituto Nacional de Saúde Dr, Ricardo Jorge, Lisboa, Portugal Monica, Oleastro, Ceu Figueiredo, Jose C. Machado, Rui M. Ferreira, Dmitry S. Bordin, M. Livzan, V. Tsukanov, Patrick Tan, Khay Guan, Feng Zhu, Yeoh, Reid Ally, Rainer Haas, W. Fischer, Milagrosa Montes, María Fernández-Reyes, E. Tamayo, Jacobo Lizasoain, L. Bujanda, Sergio Lario, M. J. Ramírez-Lázaro, X. Calvet, E. Brunet-Mas, M. Domper-Arnal, S. García-Mateo, Daniel Abad-Baroja, J. Botargués, I. Pérez-Martínez, E. Barreiro-Alonso, Javier P. Gisbert, Edurne Amorena Muro, Pedro Linares, Laura Alcoba, Vicente Martín, T. Fleitas-Kanonnikoff, H. Altayeb, Lars Engstrand, H. Enroth, Peter M. Keller, Karoline Wagner, Daniel Pohl, Yi-Chia Lee, Jyh-Ming Liou, Ming-Shiang Wu, B. Kocazeybek, S. Sarıbaş, I. Tasci, S. Demiryas, N. Kepil, Luis Quiel, Miguel Villagra, Morgan Norton, Deborah Johnson, Robert J. Huang, Joo Ha Hwang, Wendy Szymczak, S. Rajagopalan, Emmanuel Asare, William R. Jacobs, Haejin In, R. Bollag, Aileen Lopez, Edward J. Kruse, Joseph White, D. Y. Graham, Charlotte Lane, Yang Gao, Benjamin D. Gold, Marcia Cruz-Correa, María González-Pons, Luz M. Rodriguez, V. Phước, Ho Tuan, Dang Quy Dung, T. Thành, Binh, Tran Thi Huyen, T. Vũ, Van Khien, Xiongfong Chen, Yongmei Zhao, C. Raley, Bailey Kessing, Bao Tran, Yukako Katsura, Patricio Gonzalez-Hormazabal, Xavier Didelot, Sam Sheppard, E. Tarazona-Santos, Roxana Zamudio, Leonardo Mariño-Ramírez, S. Backert, Michael Naumann, A. Smet, Douglas E. Berg, Á. Chiner-Oms, Koji Yahara, Martin J. Blaser, Tamas Vincze, Richard D. Morgan, J. P. Dekker, J. Torres, Mehwish Noureen, Joshua L. Cherry, Naoki Osada, Masaki Fukuyo, Masanori Arita, Santiago Sandoval-Motta, Rajiv Boscolo, S. Ghirotto, Zilia Y. Muñoz-Ramírez, Roberto C. Torres, D. Falush, Kaisa Thorell, and I. Uchiyama. Gene content, phage cycle regulation model and prophage inactivation disclosed by prophage genomics in the helicobacter pylori genome project. Gut Microbes, Aug 2024. URL: https://doi.org/10.1080/19490976.2024.2379440, doi:10.1080/19490976.2024.2379440. This article has 15 citations and is from a peer-reviewed journal.

15. (owen2020awindowinto pages 9-11): Siân V. Owen, Rocío Canals, Nicolas Wenner, Disa L. Hammarlöf, Carsten Kröger, and Jay C. D. Hinton. A window into lysogeny: revealing temperate phage biology with transcriptomics. Microbial Genomics, Feb 2020. URL: https://doi.org/10.1099/mgen.0.000330, doi:10.1099/mgen.0.000330. This article has 73 citations and is from a peer-reviewed journal.

16. (wang2010crypticprophageshelp pages 2-3): Xiaoxue Wang, Younghoon Kim, Qun Ma, Seok Hoon Hong, Karina Pokusaeva, Joseph M. Sturino, and Thomas K. Wood. Cryptic prophages help bacteria cope with adverse environments. Nature Communications, Dec 2010. URL: https://doi.org/10.1038/ncomms1146, doi:10.1038/ncomms1146. This article has 816 citations and is from a highest quality peer-reviewed journal.

17. (tenoriocarnalla2024hostpopulationstructure pages 1-2): Karen Tenorio-Carnalla, Alejandro Aguilar-Vera, Alfredo J. Hernández-Alvarez, Gamaliel López-Leal, Valeria Mateo-Estrada, Rosa Isela Santamaria, and Santiago Castillo-Ramírez. Host population structure and species resolution reveal prophage transmission dynamics. Oct 2024. URL: https://doi.org/10.1128/mbio.02377-24, doi:10.1128/mbio.02377-24. This article has 11 citations and is from a domain leading peer-reviewed journal.

18. (kang2017prophagegenomicsreveals pages 1-4): Han Suh Kang, Katelyn McNair, Daniel A. Cuevas, Barbara A. Bailey, Anca M. Segall, and Robert A. Edwards. Prophage genomics reveals patterns in phage genome organization and replication. bioRxiv, Mar 2017. URL: https://doi.org/10.1101/114819, doi:10.1101/114819. This article has 52 citations.

19. (kang2017prophagegenomicsreveals pages 7-10): Han Suh Kang, Katelyn McNair, Daniel A. Cuevas, Barbara A. Bailey, Anca M. Segall, and Robert A. Edwards. Prophage genomics reveals patterns in phage genome organization and replication. bioRxiv, Mar 2017. URL: https://doi.org/10.1101/114819, doi:10.1101/114819. This article has 52 citations.