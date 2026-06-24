---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:20:09.473030'
end_time: '2026-06-18T03:33:59.769254'
duration_seconds: 830.3
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: genomic island
  trait_identifier: traitmech:000093
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: genomic_island
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A genomics trait describing possession of a genomic island \u2014 a\
    \ horizontally acquired chromosomal region (e.g. a pathogenicity, symbiosis, or\
    \ metabolic island) that often retains mobility signatures such as flanking repeats\
    \ and atypical nucleotide composition."
  parent_traits: traitmech:000089
  synonyms: pathogenicity island
  evidence_summary: 'DOI:10.1038/nrmicro884:  (Dobrindt et al. review genomic islands
    in pathogenic and environmental microorganisms.) | DOI:10.1111/j.1574-6976.2008.00136.x:  (Juhas
    et al. review genomic islands as tools of bacterial horizontal gene transfer and
    evolution.)'
  causal_graph_summary: 'gi_hgt_accessory_function: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** genomic island
- **METPO identifier:** traitmech:000093
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of a genomic island — a horizontally acquired chromosomal region (e.g. a pathogenicity, symbiosis, or metabolic island) that often retains mobility signatures such as flanking repeats and atypical nucleotide composition.
- **Parent traits:** traitmech:000089
- **Synonyms:** pathogenicity island
- **Existing evidence:** DOI:10.1038/nrmicro884:  (Dobrindt et al. review genomic islands in pathogenic and environmental microorganisms.) | DOI:10.1111/j.1574-6976.2008.00136.x:  (Juhas et al. review genomic islands as tools of bacterial horizontal gene transfer and evolution.)
- **Existing causal graph summary:** gi_hgt_accessory_function: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **genomic island** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genomic_island.yaml`.

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
- **Trait label:** genomic island
- **METPO identifier:** traitmech:000093
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of a genomic island — a horizontally acquired chromosomal region (e.g. a pathogenicity, symbiosis, or metabolic island) that often retains mobility signatures such as flanking repeats and atypical nucleotide composition.
- **Parent traits:** traitmech:000089
- **Synonyms:** pathogenicity island
- **Existing evidence:** DOI:10.1038/nrmicro884:  (Dobrindt et al. review genomic islands in pathogenic and environmental microorganisms.) | DOI:10.1111/j.1574-6976.2008.00136.x:  (Juhas et al. review genomic islands as tools of bacterial horizontal gene transfer and evolution.)
- **Existing causal graph summary:** gi_hgt_accessory_function: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **genomic island** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genomic_island.yaml`.

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


## Curation-focused research report: **Genomic island** (TraitMech `traitmech:000093`)

**Target trait definition (given):** possession of a genomic island (GI)—a horizontally acquired chromosomal region (e.g., pathogenicity, symbiosis, metabolic island) that often retains mobility signatures such as flanking repeats and atypical nucleotide composition.

### 1) Scope summary (trait meaning + boundary cases)

**Current understanding.** Recent mechanistic work treats “genomic island” as an umbrella term for diverse *horizontally acquired* genome regions, typically recognized by **local compositional disparities** (e.g., atypical GC content, codon usage, gene organization, short repeats) and/or **mobility-associated genes** (e.g., integrases, transposases; sometimes conjugation machinery). (audrey2023asystematicapproach pages 2-3)

**GI versus related mobile genetic elements (MGEs).** In a mobility-centric framework, GIs can encompass multiple chromosomally integrated MGEs (ciMGEs), including **prophages, transposons, integrated plasmids, integrative and mobilizable elements (IMEs), and integrative and conjugative elements (ICEs)**; distinguishing these subclasses depends on mobility modules and transmission route (intracellular relocation vs intercellular transfer). (audrey2023asystematicapproach pages 1-2)

**Pathogenicity islands (PAIs) as a GI subclass.** PAIs are distinct genomic segments that contribute to **virulence** and often show **GC-content differences** versus the core genome and **integration near tRNA genes**; they are frequently acquired by HGT via plasmids, phages, or ICEs. (lyu2024theintricaterelationship pages 1-2)

**Boundary cases to distinguish in curation.**
- **Plasmid vs GI:** plasmids are extrachromosomal replicons; a GI is chromosomal. However, some virulence regions can be plasmid-borne and are not strictly “islands” unless chromosomally integrated (curation should follow the trait definition). (lyu2024theintricaterelationship pages 1-2)
- **ICE vs IME (both GI subclasses):** ICEs are self-transmissible via conjugation and encode a **type IV secretion system (T4SS)**; IMEs lack full conjugation machinery and exploit a helper ICE/plasmid for transfer. (audrey2023asystematicapproach pages 1-2)
- **Transposon vs GI:** many islands are mosaics that may include transposons/integrons; islands integrated by **DDE transposases** often show **short target site duplications** flanking the insertion. (audrey2023asystematicapproach pages 1-2)

### 2) Candidate causal-graph entities (grouped)

#### A. Mobile-element modules / processes
- **Integration/excision:** DDE transposase; tyrosine recombinase; serine integrase; att sites / target-site duplications (audrey2023asystematicapproach pages 1-2)
- **Conjugation / transfer modules:** relaxase/oriT-binding (DTR); type IV coupling protein (T4CP); mating pore formation / T4SS (MPF) (audrey2023asystematicapproach pages 3-5)
- **Stress response controlling mobility (regulatory trigger):** SOS response; RecA–LexA regulatory axis (pons2023conjugativeinccplasmid pages 2-4)

#### B. Functional cargo commonly carried by GIs
- **Antibiotic resistance, heavy metal resistance, toxins, colonization and pathogenicity loci, alternative metabolic pathways, anti-phage defense systems** (audrey2023asystematicapproach pages 1-2)

#### C. Island-host interaction/phenotype nodes (examples supported by recent experiments)
- **Salmonella pathogenicity islands:** SPI-1 (intestinal invasion), SPI-2 (intracellular survival/replication), SPI-14 (systemic infection in chicken model; bile-acid resistance) (picorodriguez2024effectofsalmonella pages 1-2, hu2024salmonellapathogenicityisland14 pages 4-5)
- **Vibrio pathogenicity island 2 (VPI-2):** restriction–modification (T1RM) system; novel modification-dependent restriction (TgvAB); nan-nag sialic-acid utilization region (vizzarro2024vibriocholeraepathogenicity pages 1-2)

#### D. Environmental / experimental factors
- **Bile acids** (growth inhibition phenotype upon SPI-14 deletion) (hu2024salmonellapathogenicityisland14 pages 4-5, hu2024salmonellapathogenicityisland14 media cf566ba3)
- **Conjugative plasmid entry** (trigger for SOS response, enabling mobilization of an IME) (pons2023conjugativeinccplasmid pages 2-4)

### 3) Evidence-backed candidate causal edges (triples)

The following table is designed to be directly reusable for curation into `genomic_island.yaml`.

| Subject node | Predicate | Object node | Edge type (mechanistic/observational) | Evidence snippet (short quote) | Reference (DOI, year, URL) | Notes/uncertainty | Suggested ontology grounding (GO/ENVO/CHEBI/NCBITaxon etc where possible) |
|---|---|---|---|---|---|---|---|
| genomic island | carries | integrase/recombinase/transposase mobility module | mechanistic | “Intracellular mobility… often mediated by dedicated DDE transposases or integrases belonging to… serine or tyrosine recombinases” (audrey2023asystematicapproach pages 1-2) | 10.1093/nar/gkad644, 2023, https://doi.org/10.1093/nar/gkad644 | Core mechanistic hallmark of many GIs; broad but not universal across all island subclasses | METPO:traitmech:000093; GO:0015074 DNA integration; label:tyrosine recombinase; label:serine recombinase; label:DDE transposase |
| tyrosine recombinase-containing genomic island | tends to integrate at | tRNA gene insertion site | observational | “tRNA genes are more frequently targeted as insertion sites by GIs encoding a tyrosine recombinase” (audrey2023asystematicapproach pages 1-2) | 10.1093/nar/gkad644, 2023, https://doi.org/10.1093/nar/gkad644 | Statistical tendency, not absolute; curate as probabilistic/association edge if allowed | label:tyrosine recombinase; GO:0006399 tRNA metabolic process; SO:0000253 tRNA_gene |
| DDE transposase-mediated genomic island integration | produces | short target sequence duplication | mechanistic | “A short target sequence duplication usually flanks GIs integrated by DDE transposases” (audrey2023asystematicapproach pages 1-2) | 10.1093/nar/gkad644, 2023, https://doi.org/10.1093/nar/gkad644 | Structural signature useful for detection; applies to a subset of GIs | label:DDE transposase; label:target site duplication |
| serine integrase-mediated genomic island integration | produces | short target sequence duplication | mechanistic | “A short target sequence duplication usually flanks GIs integrated by… serine integrases” (audrey2023asystematicapproach pages 1-2) | 10.1093/nar/gkad644, 2023, https://doi.org/10.1093/nar/gkad644 | Subclass-specific integration signature | label:serine integrase; label:target site duplication |
| tyrosine recombinase-mediated genomic island integration | produces | imperfect target sequence duplication | mechanistic | “Tyrosine recombinases often lead to a longer yet imperfect target sequence duplication” (audrey2023asystematicapproach pages 1-2) | 10.1093/nar/gkad644, 2023, https://doi.org/10.1093/nar/gkad644 | Structural hallmark; “often” indicates non-universality | label:tyrosine recombinase; label:target site duplication |
| integrative conjugative element (ICE) | disseminates by | conjugation | mechanistic | “ICEs disseminate by conjugation” (audrey2023asystematicapproach pages 1-2) | 10.1093/nar/gkad644, 2023, https://doi.org/10.1093/nar/gkad644 | Relevant for GI subclasses with self-transmissibility | GO:0000746 conjugation; label:integrative conjugative element |
| ICE | requires | type IV secretion system | mechanistic | “ICEs disseminate by conjugation using a type IV secretion system (T4SS)” (audrey2023asystematicapproach pages 1-2) | 10.1093/nar/gkad644, 2023, https://doi.org/10.1093/nar/gkad644 | Strong mechanistic support for self-transmissible chromosomal islands | GO:0030254 protein secretion by the type IV secretion system; label:T4SS |
| integrative mobilizable element (IME) | uses | helper ICE or conjugative plasmid conjugation apparatus | mechanistic | “IMEs… spread via the conjugative apparatus encoded by a helper ICE or conjugative plasmid” (audrey2023asystematicapproach pages 1-2) | 10.1093/nar/gkad644, 2023, https://doi.org/10.1093/nar/gkad644 | Important boundary-case relation between GIs and mobilization | label:integrative mobilizable element; GO:0000746 conjugation; label:conjugative plasmid |
| conjugative IncC/IncA plasmid entry | triggers | SOS response | mechanistic | “the conjugative entry of IncC/IncA plasmids is detected at an early stage by SGI1 through the transient activation of the SOS response” (pons2023conjugativeinccplasmid pages 2-4) | 10.1128/spectrum.02201-22, 2023, https://doi.org/10.1128/spectrum.02201-22 | Demonstrated for SGI1 system; taxon/element specific | GO:0009432 SOS response; label:IncC plasmid |
| SOS response | derepresses | sgaDC master activator expression | mechanistic | “SOS response… induces the expression of the SGI1 master activators SgaDC” (pons2023conjugativeinccplasmid pages 2-4) | 10.1128/spectrum.02201-22, 2023, https://doi.org/10.1128/spectrum.02201-22 | Specific to SGI1 regulatory circuitry | label:sgaDC; GO:0006355 regulation of DNA-templated transcription |
| sgaDC master activator | promotes | SGI1 mobilization/transfer | mechanistic | “sgaDC, shown to play a crucial role in the complex biology between SGI1 and IncC plasmids” and SOS activation “promotes effective transfer” (pons2023conjugativeinccplasmid pages 2-4) | 10.1128/spectrum.02201-22, 2023, https://doi.org/10.1128/spectrum.02201-22 | Mobilization edge is strongly supported, though exact downstream steps are summarized here | label:SGI1; GO:0000746 conjugation |
| Vibrio pathogenicity island 2 (VPI-2) T1RM system | methylates | host genome DNA at specific motif | mechanistic | “methylates the host genomes… identify a specific recognition sequence” (vizzarro2024vibriocholeraepathogenicity pages 1-2, vizzarro2024vibriocholeraepathogenicity pages 2-5) | 10.1128/jb.00145-24, 2024, https://doi.org/10.1128/jb.00145-24 | Supported by SMRT methylome data; V. cholerae-specific example | GO:0009007 site-specific DNA-methyltransferase activity; CHEBI:16991 DNA; NCBITaxon:666 Vibrio cholerae |
| VPI-2 HsdR restriction system | restricts | non-methylated plasmid DNA | mechanistic | “targets non-methylated plasmids for restriction” (vizzarro2024vibriocholeraepathogenicity pages 1-2); “deletion of the T1RM cluster or hsdR restored Pmotif+ transformants” (vizzarro2024vibriocholeraepathogenicity pages 2-5) | 10.1128/jb.00145-24, 2024, https://doi.org/10.1128/jb.00145-24 | Strong causal evidence from knockout/transformant assays | GO:0009307 DNA restriction-modification system; label:HsdR; label:plasmid DNA |
| VPI-2-encoded TgvAB system | inhibits | Tevenvirinae phages | mechanistic | “has potent anti-phage activity against diverse members of the Tevenvirinae” (vizzarro2024vibriocholeraepathogenicity pages 1-2, vizzarro2024vibriocholeraepathogenicity pages 2-5) | 10.1128/jb.00145-24, 2024, https://doi.org/10.1128/jb.00145-24 | Strong but clade-specific defense example | GO:0099048 defense response to virus; label:TgvAB; NCBITaxon:2560083 Tevenvirinae |
| VPI-2 nan-nag region | enhances | gut colonization fitness via sialic acid use | mechanistic | “enhance pathogenicity by giving the pathogen a competitive advantage in using sialic acid as a carbon source during gut colonization” (vizzarro2024vibriocholeraepathogenicity pages 1-2) | 10.1128/jb.00145-24, 2024, https://doi.org/10.1128/jb.00145-24 | Functional claim is presented as accepted background in this paper; may be indirect for curation | CHEBI:26667 sialic acid; ENVO:01000925 gut; NCBITaxon:666 Vibrio cholerae |
| SPI-1 | enables | intestinal invasion/cecal colonization | mechanistic | “SPI-1 allows the bacteria to invade the intestine” (picorodriguez2024effectofsalmonella pages 1-2) | 10.1007/s11259-023-10185-z, 2024, https://doi.org/10.1007/s11259-023-10185-z | Strong in Salmonella chicken model; may vary by host age and serovar | label:SPI-1; GO:0044409 entry into host; NCBITaxon:28901 Salmonella enterica |
| SPI-2 | enables | intracellular survival and replication | mechanistic | “SPI-2 is important for intracellular survival and replication” (picorodriguez2024effectofsalmonella pages 1-2) | 10.1007/s11259-023-10185-z, 2024, https://doi.org/10.1007/s11259-023-10185-z | Canonical Salmonella mechanism, supported here in avian infection context | label:SPI-2; GO:0044403 symbiont intracellular survival |
| deletion of SPI-1 | decreases | cecal colonization in chicks | observational | “ΔSPI-1 was recovered at 10^7 CFU/g at 24 hpi and then not recovered at 48–72 h” vs WT “10^9–10^10 CFU/g” (picorodriguez2024effectofsalmonella pages 2-4) | 10.1007/s11259-023-10185-z, 2024, https://doi.org/10.1007/s11259-023-10185-z | Quantitative in 1-day-old chicks; age-dependent effect in older birds | label:ΔSPI-1 mutant; label:cecum; NCBITaxon:9031 Gallus gallus |
| deletion of SPI-1 | abolishes | liver dissemination in chicks | observational | “WT liver loads were 10^7–10^8 CFU/g… while no mutant was recovered from liver” (picorodriguez2024effectofsalmonella pages 2-4) | 10.1007/s11259-023-10185-z, 2024, https://doi.org/10.1007/s11259-023-10185-z | Strong phenotype in 1-day-old chicks | label:ΔSPI-1 mutant; label:liver; NCBITaxon:9031 Gallus gallus |
| deletion of SPI-2 | decreases | cecal colonization in chicks | observational | “ΔSPI-2 was not recovered at any time” in 1-day-old chick ceca; in 1-week-old chicks “only being recovered at 3 and 7 dpi at lower amounts” (picorodriguez2024effectofsalmonella pages 2-4) | 10.1007/s11259-023-10185-z, 2024, https://doi.org/10.1007/s11259-023-10185-z | Quantitative and age-dependent | label:ΔSPI-2 mutant; label:cecum; NCBITaxon:9031 Gallus gallus |
| deletion of SPI-2 | abolishes | liver dissemination in chicks | observational | “no mutant was recovered from liver” (picorodriguez2024effectofsalmonella pages 2-4) | 10.1007/s11259-023-10185-z, 2024, https://doi.org/10.1007/s11259-023-10185-z | Strong avian-model phenotype | label:ΔSPI-2 mutant; label:liver; NCBITaxon:9031 Gallus gallus |
| deletion of SPI-1 or SPI-2 | attenuates | cecal and hepatic lesions | observational | “∆SPI-1 and ∆SPI-2 produced no cecal/hepatic lesions in 1-day-old birds and only scarce/moderate lesions in 1-week-old birds” (picorodriguez2024effectofsalmonella pages 2-4) | 10.1007/s11259-023-10185-z, 2024, https://doi.org/10.1007/s11259-023-10185-z | Histopathology-based edge; assay-specific but strong | label:histopathological lesion; label:cecum; label:liver |
| SPI-14 | promotes | bile acid resistance | mechanistic | “mSPI-14 was significantly more sensitive to bile acid” with “significantly reduced OD values” (hu2024salmonellapathogenicityisland14 pages 4-5) | 10.3389/fvets.2024.1401392, 2024, https://doi.org/10.3389/fvets.2024.1401392 | Based on deletion phenotype; mechanism within SPI-14 not fully resolved here | label:SPI-14; CHEBI:3098 bile acid; NCBITaxon:28901 Salmonella enterica |
| deletion of SPI-14 | decreases | systemic organ colonization | observational | “the number of viable bacteria in the organs was significantly lower than that of the WT-infected chickens” (hu2024salmonellapathogenicityisland14 pages 7-9); liver and spleen CFU markedly reduced (hu2024salmonellapathogenicityisland14 pages 5-7) | 10.3389/fvets.2024.1401392, 2024, https://doi.org/10.3389/fvets.2024.1401392 | Strong chicken-model evidence with quantitative organ burdens | label:ΔSPI-14 mutant; label:liver; label:spleen; NCBITaxon:9031 Gallus gallus |
| deletion of SPI-14 | reduces | mortality in infected chickens | observational | WT birds “died by 9 days post-infection” whereas mSPI-14-infected chickens “all survived” (hu2024salmonellapathogenicityisland14 pages 5-7) | 10.3389/fvets.2024.1401392, 2024, https://doi.org/10.3389/fvets.2024.1401392 | Strong virulence phenotype; host/model specific | label:ΔSPI-14 mutant; NCBITaxon:9031 Gallus gallus |
| deletion of SPI-14 | decreases | pro-inflammatory cytokine expression in liver | observational | “no significant changes in cytokine expression were observed in the liver of the mSPI-14 inoculated group” and key cytokines were “significantly lower” than WT (hu2024salmonellapathogenicityisland14 pages 7-9) | 10.3389/fvets.2024.1401392, 2024, https://doi.org/10.3389/fvets.2024.1401392 | Includes IL-1β, TNF-α, IFN-γ, IL-12, CXCLi1; downstream host-response phenotype | GO:0001816 cytokine production; label:IL-1β; label:TNF-α; label:IFN-γ; label:IL-12; label:CXCLi1 |


*Table: This table lists curation-ready causal edges for the TraitMech genomic island trait, linking island presence and mobility modules to transfer, insertion signatures, defense, virulence, and experimental deletion phenotypes. It is useful as a starting point for YAML graph curation because each edge includes a short evidence quote, source DOI/URL, uncertainty notes, and suggested ontology grounding.*

### 4) Recent developments (prioritizing 2023–2024) and “expert” synthesis

#### 4.1 Mobility-first GI classification (2023)
A 2023 Nucleic Acids Research study operationalizes GI classification using **protein-signature modules** (INT/DTR/T4CP/MPF/REP) and links element class to insertion and cargo patterns, e.g., **self-transmissible GIs (including ICEs) tend to be larger and accumulate antibiotic/phage resistance genes**, while **non-mobilizable GIs tend to use DDE transposases** for integration. (audrey2023asystematicapproach pages 1-2, audrey2023asystematicapproach pages 3-5)

#### 4.2 Regulatory triggers of GI mobilization (2023)
A 2023 Microbiology Spectrum paper provides a mechanistic chain in which **conjugative IncC/IncA plasmid entry triggers the SOS response**, which **induces expression of the SGI1 master activator (SgaDC)**, promoting IME transfer. This is directly curatable as a regulatory edge connecting environmental/experimental conditions to island mobility. (pons2023conjugativeinccplasmid pages 2-4)

#### 4.3 Defense and fitness cargo on PAIs/GIs (2024)
A 2024 Journal of Bacteriology study shows that **Vibrio cholerae VPI-2 encodes two restriction systems**: a functional **type I RM** system restricting non-methylated plasmids, and a **novel modification-dependent system (TgvAB)** with potent anti-phage activity. This supports a GI→defense mechanism edge and highlights that virulence-associated islands can simultaneously function as “defense islands.” (vizzarro2024vibriocholeraepathogenicity pages 1-2, vizzarro2024vibriocholeraepathogenicity pages 2-5)

### 5) Real-world applications / implementations

1. **Public health genomics & outbreak investigation:** Pathogen virulence/AMR often depends on accessory genome regions; experimental work demonstrates that loss of specific islands (SPI-1/SPI-2/SPI-14) strongly alters host colonization/systemic dissemination in poultry models, motivating genomic-island-aware surveillance in agriculture and One Health. (picorodriguez2024effectofsalmonella pages 2-4, hu2024salmonellapathogenicityisland14 pages 5-7)
2. **Predicting and managing horizontal gene transfer risk:** Mobility module classification (ICE vs IME) supports assessment of whether an island is likely self-transmissible or “hitchhikes” on helper conjugative elements, which is central for AMR control strategies. (audrey2023asystematicapproach pages 1-2)
3. **Biotechnology and phage therapy context:** GI-encoded restriction systems (e.g., VPI-2 RM and type IV restriction) can determine plasmid transformability and phage susceptibility—critical variables in genetic engineering, vector design, and phage-based control. (vizzarro2024vibriocholeraepathogenicity pages 2-5, vizzarro2024vibriocholeraepathogenicity pages 1-2)

### 6) Key statistics and quantitative data points (recent studies)

**Salmonella SPI-1/SPI-2 deletion effects in chickens (quantitative CFU).** In 1-day-old chicks infected with *S. Typhimurium* WT, cecal burdens were **10^9–10^10 CFU/g**, while ΔSPI-1 dropped to **10^7 CFU/g at 24 h** and then was not recovered, and ΔSPI-2 was **not recovered**; WT liver burdens were **10^7–10^8 CFU/g**, while no mutants were recovered from liver. (picorodriguez2024effectofsalmonella pages 2-4)

**Salmonella SPI-14 deletion effects (mortality + organ loads).** In an oral chicken model, WT *S. gallinarum* caused death by **9 dpi**, whereas the SPI-14 deletion mutant group **all survived**; WT liver CFU rose to **2.09×10^7 CFU/g (day 7)** and spleen to **1.7×10^7 CFU/g (day 7)**, while the SPI-14 mutant had dramatically reduced organ burdens. (hu2024salmonellapathogenicityisland14 pages 5-7, hu2024salmonellapathogenicityisland14 media cf566ba3)

**Bile-acid sensitivity (SPI-14 mutant).** The SPI-14 mutant had “significantly reduced OD values from 4 h” in LB with **0.01–0.02 mM bile acid**, indicating reduced bile tolerance (a plausible colonization/fitness component). (hu2024salmonellapathogenicityisland14 pages 4-5, hu2024salmonellapathogenicityisland14 media cf566ba3)

### 7) Warnings / claims not yet suitable for curation

- **tRNA insertion as a universal GI hallmark:** Several sources support enrichment of tRNA-proximal integration for certain GI subclasses (e.g., tyrosine recombinase islands), but it is explicitly a tendency (“more frequently targeted”) rather than a rule; curate as probabilistic/association edges only. (audrey2023asystematicapproach pages 1-2)
- **“Enhances pathogenicity” background statements:** Some VPI-2 functional statements (e.g., nan-nag sialic acid use enhancing pathogenicity) are presented as background in the J Bacteriol article; if strict curation requires primary experimental confirmation for that claim, mark uncertain until backed by direct experiments in a primary source. (vizzarro2024vibriocholeraepathogenicity pages 1-2)
- **G-quadruplex mechanisms in PAIs:** The 2024 eLife report offers correlations and hypotheses about G4s modulating integration efficiency; absent direct perturbation experiments in the provided excerpts, treat G4→integration edges as speculative unless further primary evidence is added. (lyu2024theintricaterelationship pages 4-6, lyu2024theintricaterelationship pages 1-2)

---

## DOI-first bibliography (with publication dates/URLs where available)

1. **Bioteau A, Cellier N, White F, Jacques P-É, Burrus V.** *A systematic approach to classify and characterize genomic islands driven by conjugative mobility using protein signatures.* **Nucleic Acids Research** (Aug 2023). DOI: **10.1093/nar/gkad644**. URL: https://doi.org/10.1093/nar/gkad644 (audrey2023asystematicapproach pages 1-2, audrey2023asystematicapproach pages 3-5, audrey2023asystematicapproach pages 2-3)
2. **Botelho J.** *Defense systems are pervasive across chromosomally integrated mobile genetic elements and are inversely correlated to virulence and antimicrobial resistance.* **Nucleic Acids Research** (Mar 2023). DOI: **10.1093/nar/gkad282**. URL: https://doi.org/10.1093/nar/gkad282 (botelho2023defensesystemsare pages 1-2)
3. **Pons MC et al.** *Conjugative IncC plasmid entry triggers the SOS response and promotes effective transfer of the integrative antibiotic resistance element SGI1.* **Microbiology Spectrum** (Feb 2023). DOI: **10.1128/spectrum.02201-22**. URL: https://doi.org/10.1128/spectrum.02201-22 (pons2023conjugativeinccplasmid pages 2-4)
4. **Vizzarro G et al.** *Vibrio cholerae pathogenicity island 2 encodes two distinct types of restriction systems.* **Journal of Bacteriology** (Sep 2024). DOI: **10.1128/jb.00145-24**. URL: https://doi.org/10.1128/jb.00145-24 (vizzarro2024vibriocholeraepathogenicity pages 2-5, vizzarro2024vibriocholeraepathogenicity pages 1-2)
5. **Pico-Rodríguez JT et al.** *Effect of Salmonella pathogenicity island 1 and 2 (SPI-1 and SPI-2) deletion on intestinal colonization and systemic dissemination in chickens.* **Veterinary Research Communications** (Jul 2024). DOI: **10.1007/s11259-023-10185-z**. URL: https://doi.org/10.1007/s11259-023-10185-z (picorodriguez2024effectofsalmonella pages 2-4)
6. **Hu Z et al.** *Salmonella pathogenicity island-14 is a critical virulence factor responsible for systemic infection in chickens caused by Salmonella gallinarum.* **Frontiers in Veterinary Science** (May 2024). DOI: **10.3389/fvets.2024.1401392**. URL: https://doi.org/10.3389/fvets.2024.1401392 (hu2024salmonellapathogenicityisland14 pages 7-9, hu2024salmonellapathogenicityisland14 pages 4-5, hu2024salmonellapathogenicityisland14 pages 5-7, hu2024salmonellapathogenicityisland14 media cf566ba3)
7. **Lyu B, Song Q.** *The intricate relationship of G-Quadruplexes and bacterial pathogenicity islands.* **eLife** (Feb 2024). DOI: **10.7554/eLife.91985.3**. URL: https://doi.org/10.7554/elife.91985.3 (lyu2024theintricaterelationship pages 1-2, lyu2024theintricaterelationship pages 4-6, lyu2024theintricaterelationship pages 6-7)
8. **Kushwaha SK et al.** *Comprehensive blueprint of Salmonella genomic plasticity identifies hotspots for pathogenicity genes.* **PLOS Biology** (Aug 2024). DOI: **10.1371/journal.pbio.3002746**. URL: https://doi.org/10.1371/journal.pbio.3002746 (kushwaha2024comprehensiveblueprintof pages 1-2)



References

1. (audrey2023asystematicapproach pages 2-3): Bioteau Audrey, Nicolas Cellier, Frédérique White, Pierre-Étienne Jacques, and Vincent Burrus. A systematic approach to classify and characterize genomic islands driven by conjugative mobility using protein signatures. Nucleic Acids Research, 51:8402-8412, Aug 2023. URL: https://doi.org/10.1093/nar/gkad644, doi:10.1093/nar/gkad644. This article has 26 citations and is from a highest quality peer-reviewed journal.

2. (audrey2023asystematicapproach pages 1-2): Bioteau Audrey, Nicolas Cellier, Frédérique White, Pierre-Étienne Jacques, and Vincent Burrus. A systematic approach to classify and characterize genomic islands driven by conjugative mobility using protein signatures. Nucleic Acids Research, 51:8402-8412, Aug 2023. URL: https://doi.org/10.1093/nar/gkad644, doi:10.1093/nar/gkad644. This article has 26 citations and is from a highest quality peer-reviewed journal.

3. (lyu2024theintricaterelationship pages 1-2): Bo Lyu and Qisheng Song. The intricate relationship of g-quadruplexes and bacterial pathogenicity islands. Feb 2024. URL: https://doi.org/10.7554/elife.91985.3, doi:10.7554/elife.91985.3. This article has 9 citations and is from a domain leading peer-reviewed journal.

4. (audrey2023asystematicapproach pages 3-5): Bioteau Audrey, Nicolas Cellier, Frédérique White, Pierre-Étienne Jacques, and Vincent Burrus. A systematic approach to classify and characterize genomic islands driven by conjugative mobility using protein signatures. Nucleic Acids Research, 51:8402-8412, Aug 2023. URL: https://doi.org/10.1093/nar/gkad644, doi:10.1093/nar/gkad644. This article has 26 citations and is from a highest quality peer-reviewed journal.

5. (pons2023conjugativeinccplasmid pages 2-4): Marine C. Pons, Karine Praud, Sandra Da Re, Axel Cloeckaert, and Benoît Doublet. Conjugative incc plasmid entry triggers the sos response and promotes effective transfer of the integrative antibiotic resistance element sgi1. Feb 2023. URL: https://doi.org/10.1128/spectrum.02201-22, doi:10.1128/spectrum.02201-22. This article has 18 citations and is from a domain leading peer-reviewed journal.

6. (picorodriguez2024effectofsalmonella pages 1-2): Jwerlly Tatiana Pico-Rodríguez, Hugo Martínez-Jarquín, José de Jesús Gómez-Chávez, Mireya Juárez-Ramírez, and Luary Carolina Martínez-Chavarría. Effect of salmonella pathogenicity island 1 and 2 (spi-1 and spi-2) deletion on intestinal colonization and systemic dissemination in chickens. Veterinary Research Communications, 48:49-60, Jul 2024. URL: https://doi.org/10.1007/s11259-023-10185-z, doi:10.1007/s11259-023-10185-z. This article has 24 citations and is from a peer-reviewed journal.

7. (hu2024salmonellapathogenicityisland14 pages 4-5): Zuo Hu, Shinjiro Ojima, Zhihao Zhu, Xiaoying Yu, Makoto Sugiyama, Takeshi Haneda, Masashi Okamura, Hisaya K. Ono, and Dong-Liang Hu. Salmonella pathogenicity island-14 is a critical virulence factor responsible for systemic infection in chickens caused by salmonella gallinarum. Frontiers in Veterinary Science, May 2024. URL: https://doi.org/10.3389/fvets.2024.1401392, doi:10.3389/fvets.2024.1401392. This article has 10 citations and is from a peer-reviewed journal.

8. (vizzarro2024vibriocholeraepathogenicity pages 1-2): Grazia Vizzarro, Alexandre Lemopoulos, David William Adams, and Melanie Blokesch. <i>vibrio cholerae</i> pathogenicity island 2 encodes two distinct types of restriction systems. Sep 2024. URL: https://doi.org/10.1128/jb.00145-24, doi:10.1128/jb.00145-24. This article has 22 citations and is from a peer-reviewed journal.

9. (hu2024salmonellapathogenicityisland14 media cf566ba3): Zuo Hu, Shinjiro Ojima, Zhihao Zhu, Xiaoying Yu, Makoto Sugiyama, Takeshi Haneda, Masashi Okamura, Hisaya K. Ono, and Dong-Liang Hu. Salmonella pathogenicity island-14 is a critical virulence factor responsible for systemic infection in chickens caused by salmonella gallinarum. Frontiers in Veterinary Science, May 2024. URL: https://doi.org/10.3389/fvets.2024.1401392, doi:10.3389/fvets.2024.1401392. This article has 10 citations and is from a peer-reviewed journal.

10. (vizzarro2024vibriocholeraepathogenicity pages 2-5): Grazia Vizzarro, Alexandre Lemopoulos, David William Adams, and Melanie Blokesch. <i>vibrio cholerae</i> pathogenicity island 2 encodes two distinct types of restriction systems. Sep 2024. URL: https://doi.org/10.1128/jb.00145-24, doi:10.1128/jb.00145-24. This article has 22 citations and is from a peer-reviewed journal.

11. (picorodriguez2024effectofsalmonella pages 2-4): Jwerlly Tatiana Pico-Rodríguez, Hugo Martínez-Jarquín, José de Jesús Gómez-Chávez, Mireya Juárez-Ramírez, and Luary Carolina Martínez-Chavarría. Effect of salmonella pathogenicity island 1 and 2 (spi-1 and spi-2) deletion on intestinal colonization and systemic dissemination in chickens. Veterinary Research Communications, 48:49-60, Jul 2024. URL: https://doi.org/10.1007/s11259-023-10185-z, doi:10.1007/s11259-023-10185-z. This article has 24 citations and is from a peer-reviewed journal.

12. (hu2024salmonellapathogenicityisland14 pages 7-9): Zuo Hu, Shinjiro Ojima, Zhihao Zhu, Xiaoying Yu, Makoto Sugiyama, Takeshi Haneda, Masashi Okamura, Hisaya K. Ono, and Dong-Liang Hu. Salmonella pathogenicity island-14 is a critical virulence factor responsible for systemic infection in chickens caused by salmonella gallinarum. Frontiers in Veterinary Science, May 2024. URL: https://doi.org/10.3389/fvets.2024.1401392, doi:10.3389/fvets.2024.1401392. This article has 10 citations and is from a peer-reviewed journal.

13. (hu2024salmonellapathogenicityisland14 pages 5-7): Zuo Hu, Shinjiro Ojima, Zhihao Zhu, Xiaoying Yu, Makoto Sugiyama, Takeshi Haneda, Masashi Okamura, Hisaya K. Ono, and Dong-Liang Hu. Salmonella pathogenicity island-14 is a critical virulence factor responsible for systemic infection in chickens caused by salmonella gallinarum. Frontiers in Veterinary Science, May 2024. URL: https://doi.org/10.3389/fvets.2024.1401392, doi:10.3389/fvets.2024.1401392. This article has 10 citations and is from a peer-reviewed journal.

14. (lyu2024theintricaterelationship pages 4-6): Bo Lyu and Qisheng Song. The intricate relationship of g-quadruplexes and bacterial pathogenicity islands. Feb 2024. URL: https://doi.org/10.7554/elife.91985.3, doi:10.7554/elife.91985.3. This article has 9 citations and is from a domain leading peer-reviewed journal.

15. (botelho2023defensesystemsare pages 1-2): João Botelho. Defense systems are pervasive across chromosomally integrated mobile genetic elements and are inversely correlated to virulence and antimicrobial resistance. Nucleic Acids Research, 51:4385-4397, Mar 2023. URL: https://doi.org/10.1093/nar/gkad282, doi:10.1093/nar/gkad282. This article has 59 citations and is from a highest quality peer-reviewed journal.

16. (lyu2024theintricaterelationship pages 6-7): Bo Lyu and Qisheng Song. The intricate relationship of g-quadruplexes and bacterial pathogenicity islands. Feb 2024. URL: https://doi.org/10.7554/elife.91985.3, doi:10.7554/elife.91985.3. This article has 9 citations and is from a domain leading peer-reviewed journal.

17. (kushwaha2024comprehensiveblueprintof pages 1-2): Simran Krishnakant Kushwaha, Yi Wu, Hugo Leonardo Avila, Abhirath Anand, Thomas Sicheritz-Pontén, Andrew Millard, Sandhya Amol Marathe, and Franklin L. Nobrega. Comprehensive blueprint of salmonella genomic plasticity identifies hotspots for pathogenicity genes. PLOS Biology, 22:e3002746, Aug 2024. URL: https://doi.org/10.1371/journal.pbio.3002746, doi:10.1371/journal.pbio.3002746. This article has 18 citations and is from a highest quality peer-reviewed journal.