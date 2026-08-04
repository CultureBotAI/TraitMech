---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T00:31:14.504039'
end_time: '2026-06-30T00:55:43.685549'
duration_seconds: 1469.18
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: starch degradation
  trait_identifier: traitmech:000115
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: starch_degradation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biopolymer-degradation metabolism in which an organism hydrolyzes
    starch (amylose and amylopectin) to maltooligosaccharides and glucose using amylases
    and related glycoside hydrolases.
  parent_traits: traitmech:000110
  synonyms: amylolytic
  evidence_summary: 'DOI:10.1016/S0168-1656(01)00407-2:  (van der Maarel et al. review
    starch-converting enzymes of the alpha-amylase family that hydrolyze starch to
    oligosaccharides and glucose.) | DOI:10.1093/nar/gkt1178:  (The CAZy database
    review classifies the glycoside hydrolases (including amylases) that microorganisms
    use to degrade starch and other polysaccharides.)'
  causal_graph_summary: 'starch_degradation_amylase: 6 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 65
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** starch degradation
- **METPO identifier:** traitmech:000115
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes starch (amylose and amylopectin) to maltooligosaccharides and glucose using amylases and related glycoside hydrolases.
- **Parent traits:** traitmech:000110
- **Synonyms:** amylolytic
- **Existing evidence:** DOI:10.1016/S0168-1656(01)00407-2:  (van der Maarel et al. review starch-converting enzymes of the alpha-amylase family that hydrolyze starch to oligosaccharides and glucose.) | DOI:10.1093/nar/gkt1178:  (The CAZy database review classifies the glycoside hydrolases (including amylases) that microorganisms use to degrade starch and other polysaccharides.)
- **Existing causal graph summary:** starch_degradation_amylase: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **starch degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/starch_degradation.yaml`.

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
- **Trait label:** starch degradation
- **METPO identifier:** traitmech:000115
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes starch (amylose and amylopectin) to maltooligosaccharides and glucose using amylases and related glycoside hydrolases.
- **Parent traits:** traitmech:000110
- **Synonyms:** amylolytic
- **Existing evidence:** DOI:10.1016/S0168-1656(01)00407-2:  (van der Maarel et al. review starch-converting enzymes of the alpha-amylase family that hydrolyze starch to oligosaccharides and glucose.) | DOI:10.1093/nar/gkt1178:  (The CAZy database review classifies the glycoside hydrolases (including amylases) that microorganisms use to degrade starch and other polysaccharides.)
- **Existing causal graph summary:** starch_degradation_amylase: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **starch degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/starch_degradation.yaml`.

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


# Microbial Starch Degradation — TraitMech Causal Graph Curation Report

**Trait:** starch degradation (traitmech:000115)
**Category:** METABOLISM | **Kind:** CLASS | **Parent:** traitmech:000110

---

## 1. Trait Scope Summary

Starch degradation (synonym: amylolytic) is a biopolymer-degradation metabolism in which a microorganism hydrolyzes starch—comprising linear amylose (α-1,4-linked glucose) and branched amylopectin (α-1,4 and α-1,6-linked glucose)—to maltooligosaccharides and ultimately glucose, using amylases and related glycoside hydrolases. The phenotype is typically assayed as growth on starch as sole carbon source, or by starch–iodine clearing (halo) assays around colonies (foley2016thesusoperon pages 1-2, sidar2020carbohydratebindingmodules pages 2-3).

**Boundary cases and distinctions from nearby traits:**

- **Starch degradation vs. cellulose degradation:** Both are polysaccharide degradation traits targeting glucans, but starch is an α-glucan (α-1,4/α-1,6 linkages) whereas cellulose is a β-1,4-glucan. The enzyme families are largely non-overlapping (GH13/GH15/GH97 vs. GH5/GH6/GH7/GH9/GH48).
- **Starch degradation vs. glycogen degradation:** Glycogen and amylopectin share α-1,6 branch points, and some enzymes (e.g., neopullulanases, debranching enzymes) act on both. However, glycogen is an endogenous storage polymer, while starch degradation is typically an exogenous substrate utilization trait.
- **Starch degradation vs. maltose/maltodextrin utilization:** Maltose utilization is a downstream capability; an organism may import and metabolize maltose without being able to depolymerize intact starch granules. True starch degradation requires extracellular or cell-surface amylolytic activity.
- **Resistant starch degradation:** A more restrictive sub-trait requiring specialized synergistic enzyme systems and is a rare capability in the gut microbiota (brown2024acarboseimpairsgut pages 16-18).

---

## 2. Causal Graph Entities (Candidate Nodes)

The following table organizes all candidate nodes for the starch degradation causal graph by mechanistic type, with suggested ontology groundings.

| Group | Node label | Suggested CURIE / grounding | Description |
|---|---|---|---|
| SUBSTRATE | starch (amylose + amylopectin) | CHEBI:28017 | Primary polymeric substrate of the trait; α-glucan composed of linear amylose and branched amylopectin targeted by microbial amylases and related enzymes (foley2016thesusoperon pages 1-2, sidar2020carbohydratebindingmodules pages 2-3) |
| SUBSTRATE | maltodextrins | CHEBI:62174 | Soluble linear or branched starch hydrolysis products transported and further metabolized intracellularly/periplasmically; major intermediates in bacterial starch use (dippel2005themaltodextrinsystem pages 1-2, dippel2005themaltodextrinsystem pages 2-2) |
| SUBSTRATE | maltooligosaccharides | label-only candidate | Short α-1,4-linked glucooligosaccharides released from starch by endoamylases such as SusG and imported for downstream hydrolysis (foley2016thesusoperon pages 2-3) |
| SUBSTRATE | cyclodextrins | CHEBI:33116 | Cyclic maltooligosaccharides formed from starch by CGTases and degraded by cyclodextrinases/cyclomaltodextrinases in some bacteria (mascelli2024geneticandenzymatic pages 7-8, mascelli2024geneticandenzymatic pages 12-13) |
| SUBSTRATE | resistant starch | label-only candidate | Physically or structurally recalcitrant starch fraction degraded only by subsets of gut microbes with specialized synergistic enzyme systems (brown2024acarboseimpairsgut pages 16-18) |
| PRODUCT / INTERMEDIATE | glucose | CHEBI:17234 | End product of exo-acting glucosidases/glucoamylases and central metabolite imported into cytoplasm for glycolysis (sidar2020carbohydratebindingmodules pages 2-3, foley2016thesusoperon pages 2-3) |
| PRODUCT / INTERMEDIATE | maltose | CHEBI:17306 | Common product of starch hydrolysis and substrate for ABC or PTS uptake systems and maltose phosphorylase-dependent catabolism (mokhtari2013enterococcusfaecalisutilizes pages 1-2) |
| PRODUCT / INTERMEDIATE | maltotriose | CHEBI:63533 | Important maltooligosaccharide intermediate and inducer of the mal regulon in enterobacteria (dippel2005themaltodextrinsystem pages 7-8, dippel2005themaltodextrinsystem pages 2-2) |
| PRODUCT / INTERMEDIATE | maltotetraose | CHEBI:64342 | Intermediate maltooligosaccharide substrate for MalP and related intracellular maltodextrin catabolic enzymes (dippel2005themaltodextrinsystem pages 4-5) |
| PRODUCT / INTERMEDIATE | glucose-1-phosphate | CHEBI:4170 | Product of phosphorolysis by maltodextrin phosphorylase or maltose phosphorylase; converted to glucose-6-phosphate before glycolysis (dippel2005themaltodextrinsystem pages 2-2) |
| PRODUCT / INTERMEDIATE | glucose-6-phosphate | CHEBI:61548 | Central metabolic intermediate generated from glucose or glucose-1-phosphate and fed into glycolysis (mokhtari2013enterococcusfaecalisutilizes pages 2-4, dippel2005themaltodextrinsystem pages 2-2) |
| PRODUCT / INTERMEDIATE | maltose-6-phosphate | CHEBI:15603 | PTS-derived intracellular intermediate in some Firmicutes; dephosphorylated by MapP or hydrolyzed by phospho-α-glucosidases (mokhtari2013enterococcusfaecalisutilizes pages 1-2) |
| PRODUCT / INTERMEDIATE | panose | CHEBI:27714 | Trisaccharide product formed when SusG accommodates α-1,6 linkages while acting on pullulan-like substrates; useful marker of mixed-linkage processing (foley2016thesusoperon pages 5-7) |
| PRODUCT / INTERMEDIATE | limit dextrin | label-only candidate | Branched residual dextrin left after α-1,4 hydrolysis and subsequently attacked by debranching enzymes/neopullulanases; common inferred intermediate in starch breakdown |
| ENZYME | α-amylase | EC:3.2.1.1; CAZy:GH13 | Endo-acting enzyme cleaving internal α-1,4-glucan linkages in starch to generate maltooligosaccharides; principal enzyme class for starch depolymerization (foley2016thesusoperon pages 5-7, sidar2020carbohydratebindingmodules pages 2-3) |
| ENZYME | β-amylase | EC:3.2.1.2; CAZy:GH14 | Exo-acting amylase releasing maltose from non-reducing ends of α-1,4-glucans; present in some bacteria but not a universal microbial starch-degradation determinant (sidar2020carbohydratebindingmodules pages 2-3) |
| ENZYME | glucoamylase | EC:3.2.1.3; CAZy:GH15 | Exo-acting enzyme hydrolyzing α-1,4 and α-1,6 linkages to release glucose; especially relevant in fungal starch saccharification systems (sidar2020carbohydratebindingmodules pages 2-3) |
| ENZYME | pullulanase / neopullulanase | EC:3.2.1.41; CAZy:GH13 | Debranching or mixed-linkage processing enzyme acting on α-1,6 linkages and some α-1,4/α-1,6 substrates; represented by SusA-like enzymes in starch systems (foley2016thesusoperon pages 1-2, foley2016thesusoperon pages 2-3) |
| ENZYME | α-glucosidase | EC:3.2.1.20; CAZy:GH31 or GH97 | Exo-acting glucosidase converting starch-derived oligosaccharides to glucose; SusB-like GH97 enzymes are key periplasmic activities in Bacteroides (grondin2017polysaccharideutilizationloci pages 3-5, brown2024acarboseimpairsgut pages 9-12) |
| ENZYME | cyclodextrinase | EC:3.2.1.54; CAZy:GH13 | GH13 enzyme hydrolyzing cyclodextrins and sometimes α-diglucosides; exemplified by CjAmy13E and related enzymes (mascelli2024geneticandenzymatic pages 8-10, mascelli2024geneticandenzymatic pages 7-8) |
| ENZYME | maltodextrin phosphorylase (MalP) | EC:2.4.1.1 | Intracellular phosphorolytic enzyme removing nonreducing glucosyl residues from maltodextrins ≥ DP4 to form α-glucose-1-phosphate (dippel2005themaltodextrinsystem pages 2-2) |
| ENZYME | amylomaltase (MalQ) | EC:2.4.1.25; CAZy:GH77 | 4-α-glucanotransferase that disproportionates maltodextrins and maltose, yielding mixtures of shorter/longer dextrins plus glucose; central in maltodextrin remodeling (dippel2005themaltodextrinsystem pages 2-2, dippel2005themaltodextrinsystem pages 4-5) |
| ENZYME | maltodextrin glucosidase (MalZ) | label-only candidate | Intracellular enzyme removing glucose from reducing ends of maltodextrins; contributes with MalP to complete maltodextrin breakdown (dippel2005themaltodextrinsystem pages 2-2, dippel2005themaltodextrinsystem pages 1-2) |
| ENZYME | cyclodextrin glucanotransferase (CGTase) | EC:2.4.1.19; CAZy:GH13 | Enzyme that cyclizes starch-derived maltooligosaccharides to cyclodextrins; relevant as an alternative starch-processing route in some taxa (mascelli2024geneticandenzymatic pages 7-8) |
| ENZYME | maltose phosphorylase | EC:2.4.1.8 | Enzyme cleaving maltose into glucose and glucose-1-phosphate in ABC- or dephosphorylation-based maltose catabolic routes (mokhtari2013enterococcusfaecalisutilizes pages 1-2, mokhtari2013enterococcusfaecalisutilizes pages 4-5) |
| TRANSPORTER | SusC | label-only candidate; TonB-dependent transporter family | Outer membrane TonB-dependent transporter importing maltooligosaccharides from cell surface into the periplasm in Bacteroidetes Sus/PUL systems (foley2016thesusoperon pages 2-3, grondin2017polysaccharideutilizationloci pages 3-5) |
| TRANSPORTER | MalEFGK2 | label-only candidate; ABC transporter | Canonical bacterial maltose/maltodextrin ABC uptake complex composed of MalE, MalF, MalG, and two MalK ATPases (dippel2005themaltodextrinsystem pages 1-2, davidson2010bindingproteindependentuptake pages 1-2) |
| TRANSPORTER | maltose PTS (MalT / EIICBA) | label-only candidate; PTS transporter | High-affinity maltose phosphotransferase system in several Firmicutes that imports and concomitantly phosphorylates maltose to maltose-6-phosphate (mokhtari2013enterococcusfaecalisutilizes pages 1-2, mokhtari2013enterococcusfaecalisutilizes pages 2-4) |
| TRANSPORTER | LamB | UniProt:P02943 (E. coli exemplar) | Outer membrane maltoporin permitting entry of maltose and maltodextrins into the periplasm in enterobacteria (dippel2005themaltodextrinsystem pages 1-2) |
| REGULATORY | SusR | label-only candidate | Inner-membrane sensor/regulator controlling sus operon transcription in response to periplasmic maltooligosaccharide/maltose signals (foley2016thesusoperon pages 2-3, foley2016thesusoperon pages 10-12) |
| REGULATORY | MalT | label-only candidate | Transcriptional activator of the E. coli mal regulon controlling genes for maltose/maltodextrin uptake and metabolism (dippel2005themaltodextrinsystem pages 1-2, dippel2005themaltodextrinsystem pages 7-8) |
| REGULATORY | carbon catabolite repression | GO:0009401 | Global carbon-source control mechanism repressing maltose/starch utilization genes in the presence of preferred carbohydrates such as glucose (davidson2010bindingproteindependentuptake pages 2-4) |
| REGULATORY | maltose / maltotriose induction | label-only candidate | Induction signal for maltose regulons and some starch-responsive loci; maltotriose is a particularly effective inducer in enterobacteria (dippel2005themaltodextrinsystem pages 7-8, dippel2005themaltodextrinsystem pages 2-2) |
| BINDING PROTEIN | SusD | label-only candidate | Essential outer membrane starch-binding protein that presents substrate to SusC/SusG and is required for growth on starch in Bacteroides (foley2016thesusoperon pages 8-10, foley2016thesusoperon pages 10-12) |
| BINDING PROTEIN | SusE | label-only candidate | Auxiliary surface glycan-binding protein with tandem starch-binding domains that enhances capture of polymeric starch (foley2016thesusoperon pages 8-10, foley2016thesusoperon pages 7-8) |
| BINDING PROTEIN | SusF | label-only candidate | Auxiliary surface glycan-binding protein similar to SusE that contributes additional starch-binding capacity (foley2016thesusoperon pages 8-10, foley2016thesusoperon pages 7-8) |
| BINDING PROTEIN | MalE | label-only candidate | Periplasmic maltose-binding protein that delivers maltose or maltodextrins to the MalFGK2 transporter (mokhtari2013enterococcusfaecalisutilizes pages 1-2, davidson2010bindingproteindependentuptake pages 1-2) |
| BINDING PROTEIN | carbohydrate-binding modules (CBM20, CBM25, CBM26, CBM34, CBM41, CBM48, CBM58, CBM69, CBM74) | CAZy:CBM20; CAZy:CBM25; CAZy:CBM26; CAZy:CBM34; CAZy:CBM41; CAZy:CBM48; CAZy:CBM58; CAZy:CBM69; CAZy:CBM74 | Noncatalytic starch-binding domains that increase proximity to insoluble substrate; CBM58 is inserted in SusG, and CBM74 has been linked to resistant-starch-active systems (foley2016thesusoperon pages 5-7, sidar2020carbohydratebindingmodules pages 2-3, brown2024acarboseimpairsgut pages 16-18) |
| GENE LOCUS | sus operon (susRABCDEFG) | label-only candidate | Eight-gene starch utilization locus encoding sensing, binding, hydrolysis, and transport functions in B. thetaiotaomicron (foley2016thesusoperon pages 1-2, foley2016thesusoperon pages 2-3) |
| GENE LOCUS | mal regulon | label-only candidate | Enterobacterial locus/network encoding LamB, MalEFGK2, and intracellular maltodextrin metabolism enzymes under MalT control (dippel2005themaltodextrinsystem pages 1-2, dippel2005themaltodextrinsystem pages 7-8) |
| GENE LOCUS | polysaccharide utilization locus (PUL) | label-only candidate | General Bacteroidetes gene-cluster architecture coupling SusC/D-like transporters with CAZymes and regulators for glycan-specific metabolism (grondin2017polysaccharideutilizationloci pages 3-5, foley2016thesusoperon pages 1-2) |
| MOLECULAR FUNCTION | starch binding | GO:2001070 | Molecular function enabling capture of starch or related α-glucans at the cell surface or via CBMs (foley2016thesusoperon pages 8-10, foley2016thesusoperon pages 5-7) |
| MOLECULAR FUNCTION | α-1,4-glucan hydrolysis | GO:0004556 | Hydrolysis of internal or terminal α-1,4 linkages in starch-derived glucans by α-amylases, glucoamylases, and related enzymes (foley2016thesusoperon pages 5-7, sidar2020carbohydratebindingmodules pages 2-3) |
| MOLECULAR FUNCTION | α-1,6-glucan hydrolysis | label-only candidate | Hydrolysis of branch-point α-1,6 linkages by debranching enzymes, neopullulanases, or α-glucosidases that process branched oligosaccharides (foley2016thesusoperon pages 1-2, brown2024acarboseimpairsgut pages 9-12) |
| MOLECULAR FUNCTION | phosphorolysis | GO:0004645 | Cleavage of glycosidic bonds with phosphate to yield sugar phosphates, as in MalP and maltose phosphorylase reactions (dippel2005themaltodextrinsystem pages 2-2, mokhtari2013enterococcusfaecalisutilizes pages 4-5) |
| CELLULAR LOCALIZATION | extracellular | GO:0005576 | Compartment where secreted or cell-surface-tethered amylases can initially contact polymeric starch, especially in Gram-positive and fungal systems (sidar2020carbohydratebindingmodules pages 2-3, foley2016thesusoperon pages 7-8) |
| CELLULAR LOCALIZATION | outer membrane | GO:0019867 | Location of SusC/D/E/F/G and LamB-mediated substrate capture, hydrolysis, and transport in Gram-negative bacteria (foley2016thesusoperon pages 2-3, dippel2005themaltodextrinsystem pages 1-2) |
| CELLULAR LOCALIZATION | periplasm | GO:0042597 | Compartment where Bacteroides SusA and SusB or enterobacterial MalE-mediated processing/transport steps occur (foley2016thesusoperon pages 2-3, brown2024acarboseimpairsgut pages 1-3) |
| CELLULAR LOCALIZATION | cytoplasm | GO:0005737 | Site of intracellular maltodextrin metabolism by MalP, MalQ, MalZ and downstream entry of glucose-6-phosphate into glycolysis (dippel2005themaltodextrinsystem pages 2-2) |


*Table: This table lists candidate nodes for a TraitMech causal graph of microbial starch degradation, grouped by mechanistic type and annotated with suggested ontology groundings. It is useful for curating a YAML node set with evidence-linked substrates, enzymes, transporters, regulators, and compartments.*

### Key Enzyme Systems by Microbial Context

**Bacteroidetes (Sus paradigm):** The starch utilization system (Sus) in *Bacteroides thetaiotaomicron* comprises eight genes (susRABCDEFG) encoding a coordinated multi-protein apparatus for starch sensing, binding, surface hydrolysis, transport, and periplasmic depolymerization (foley2016thesusoperon pages 2-3, foley2016thesusoperon pages 1-2). SusG is a GH13 endoamylase with a unique internally inserted CBM58 domain that hydrolyzes α-1,4 bonds at the outer membrane (foley2016thesusoperon pages 5-7). SusDEF are outer-membrane starch-binding lipoproteins that capture starch and present it to SusG (foley2016thesusoperon pages 8-10, foley2016thesusoperon pages 10-12). SusC is a TonB-dependent transporter that imports resulting maltooligosaccharides to the periplasm (foley2016thesusoperon pages 2-3, grondin2017polysaccharideutilizationloci pages 3-5). In the periplasm, SusA (GH13 neopullulanase) and SusB (GH97 α-glucosidase) complete hydrolysis to glucose (foley2016thesusoperon pages 2-3, brown2024acarboseimpairsgut pages 1-3, brown2024acarboseimpairsgut pages 9-12). SusR senses periplasmic maltose and activates transcription of the sus operon (foley2016thesusoperon pages 2-3, foley2016thesusoperon pages 8-10). This architecture generalizes across Bacteroidetes as polysaccharide utilization loci (PULs) encoding SusC/D-like pairs plus substrate-specific CAZymes and regulators (grondin2017polysaccharideutilizationloci pages 3-5).

**Enterobacteria (mal regulon paradigm):** In *Escherichia coli*, maltose and maltodextrins enter through the outer membrane porin LamB and are bound in the periplasm by MalE, then imported by the MalFGK₂ ABC transporter powered by ATP hydrolysis (dippel2005themaltodextrinsystem pages 1-2, davidson2010bindingproteindependentuptake pages 1-2). Intracellularly, MalQ (amylomaltase, GH77) disproportionates maltodextrins to glucose and redistributed dextrins; MalP (maltodextrin phosphorylase) phosphorolyzes dextrins ≥DP4 to glucose-1-phosphate; and MalZ (maltodextrin glucosidase) removes glucose from reducing ends (dippel2005themaltodextrinsystem pages 2-2, dippel2005themaltodextrinsystem pages 4-5, dippel2005themaltodextrinsystem pages 1-2). The entire regulon is controlled by MalT, a transcriptional activator induced by maltotriose (dippel2005themaltodextrinsystem pages 1-2, dippel2005themaltodextrinsystem pages 7-8).

**Firmicutes:** Several Firmicutes use a phosphotransferase system (PTS) as a high-affinity maltose transporter, concomitantly phosphorylating maltose to maltose-6-phosphate (mokhtari2013enterococcusfaecalisutilizes pages 1-2, mokhtari2013enterococcusfaecalisutilizes pages 2-4). In *Enterococcus faecalis*, a novel maltose-6-phosphate phosphatase (MapP) dephosphorylates this intermediate, and maltose phosphorylase (MalP) then cleaves maltose to glucose and glucose-1-phosphate (mokhtari2013enterococcusfaecalisutilizes pages 1-2, mokhtari2013enterococcusfaecalisutilizes pages 4-5). Some Firmicutes (e.g., *Clostridium butyricum*) possess GH13-based enzyme sets that synergistically degrade even resistant starch (brown2024acarboseimpairsgut pages 16-18).

**Fungi:** Fungal starch degradation is dominated by secreted α-amylases (GH13) and glucoamylases (GH15, EC 3.2.1.3) that hydrolyze both α-1,4 and α-1,6 linkages to release glucose from starch chain termini (sidar2020carbohydratebindingmodules pages 2-3).

### CAZy Family Summary

The principal glycoside hydrolase families active on starch are: **GH13** (α-amylase superfamily: α-amylases, neopullulanases, cyclodextrinases, CGTases—the largest and most diverse starch-active family with >136,000 sequences), **GH14** (β-amylases, mainly plants/some bacteria), **GH15** (glucoamylases, fungi and some bacteria), **GH31** (α-glucosidases), **GH57** (alternative α-amylase family in bacteria/archaea), **GH77** (amylomaltase/4-α-glucanotransferase), **GH97** (α-glucosidase in Bacteroidetes), and **GH119/GH126** (minor bacteria-specific amylase families) (sidar2020carbohydratebindingmodules pages 2-3, mascelli2024geneticandenzymatic pages 8-10, mascelli2024geneticandenzymatic pages 7-8). Relevant carbohydrate-binding modules include CBM20, CBM25, CBM26, CBM34, CBM41, CBM48, CBM58, CBM69, and CBM74, which enhance enzyme proximity to insoluble starch granules (foley2016thesusoperon pages 5-7, sidar2020carbohydratebindingmodules pages 2-3).

---

## 3. Evidence-Backed Causal Edges

The following table presents candidate subject-predicate-object triples for the causal graph, each supported by a specific reference, snippet, and curatorial notes.

| Subject | Predicate | Object | Reference (DOI) | Supporting snippet / quote | Notes |
|---|---|---|---|---|---|
| alpha-amylase | hydrolyzes | starch (to maltooligosaccharides) | 10.3389/fbioe.2020.00871 | "Alpha-amylases (EC 3.2.1.1) are endo-acting enzymes that randomly hydrolyze internal α-1,4-glucan chains in starch to produce oligosaccharides" (sidar2020carbohydratebindingmodules pages 2-3) | Strong general edge for core trait definition. |
| starch | is_substrate_of | alpha-amylase | 10.3389/fbioe.2020.00871 | "Alpha-amylases (EC 3.2.1.1) are endo-acting enzymes that randomly hydrolyze internal α-1,4-glucan chains in starch" (sidar2020carbohydratebindingmodules pages 2-3) | Inverse of the previous edge; broadly supported. |
| SusG (GH13 amylase) | hydrolyzes | starch (cell surface; to maltooligosaccharides) | 10.1007/s00018-016-2242-x | "SusG is a membrane-tethered α-amylase that hydrolyzes bound starch into maltooligosaccharides" (foley2016thesusoperon pages 2-3) | Strong, Bacteroides-specific but canonical Sus mechanism. |
| SusD / SusE / SusF | binds | starch | 10.1007/s00018-016-2242-x | "SusE and SusF are starch-binding proteins" and "SusD plays a dual role: it binds starch" (foley2016thesusoperon pages 8-10) | Supported for outer-membrane starch capture; grouping three proteins is a mild simplification. |
| SusC | transports | maltooligosaccharides (surface to periplasm) | 10.1007/s00018-016-2242-x | "SusC is a TonB-dependent transporter that shuttles these oligosaccharides into the periplasm" (foley2016thesusoperon pages 2-3) | Strong, transport step central to Sus. |
| SusA (neopullulanase) | hydrolyzes | maltooligosaccharides | 10.1007/s00018-016-2242-x | "Once in the periplasm, SusA (neopullulanase) and SusB (α-glucosidase) further depolymerize the oligosaccharides into glucose" (foley2016thesusoperon pages 2-3) | Strong for periplasmic oligosaccharide processing; exact substrate spectrum varies. |
| SusB (GH97 alpha-glucosidase) | hydrolyzes | maltooligosaccharides to glucose | 10.1128/mbio.01506-24 | "SusB enzymes are exo-acting glucoamylases that cleave α1,4 and α1,6 linkages in starch oligosaccharides" (brown2024acarboseimpairsgut pages 9-12) | Strong recent evidence; product glucose inferred directly from GH97 glucosidase role and Sus literature. |
| SusR | activates_transcription_of | sus operon | 10.1007/s00018-016-2242-x | "SusR mediates transcriptional activation of the sus operon in response to glycan signals" (foley2016thesusoperon pages 8-10) | Strong. |
| maltose | induces | SusR / sus transcription | 10.1007/s00018-016-2242-x | "SusR is a regulatory protein that senses maltose in the periplasm and independently regulates transcription of the other sus genes" (foley2016thesusoperon pages 2-3) | Strong, but should be modeled as signal-to-regulator/signal-to-transcription rather than direct biochemical induction of SusR. |
| MalEFGK2 | transports | maltose / maltodextrins | 10.1128/jb.187.24.8322-8331.2005 | "The system includes a binding protein-dependent ABC transporter composed of... MalE... MalF and MalG... and MalK" and it "specifically binds maltose and maltodextrins" (dippel2005themaltodextrinsystem pages 1-2) | Strong for enterobacterial maltose/maltodextrin uptake. |
| MalP (maltodextrin phosphorylase) | phosphorolyzes | maltodextrins to glucose-1-phosphate | 10.1128/jb.187.24.8322-8331.2005 | "MalP... removes the nonreducing glucosyl residue from maltodextrins of at least four glucose units via phosphorolysis, producing glucose-1-phosphate" (dippel2005themaltodextrinsystem pages 2-2) | Strong. |
| MalQ (amylomaltase) | disproportionates | maltodextrins (to glucose + redistributed dextrins) | 10.1128/jb.187.24.8322-8331.2005 | "MalQ (amylomaltase) cleaves linear maltodextrins into a mixture of shorter maltodextrins and glucose" (dippel2005themaltodextrinsystem pages 2-2) | Strong for disproportionation/remodeling rather than simple hydrolysis. |
| MalZ (maltodextrin glucosidase) | hydrolyzes | maltodextrins (reducing end) | 10.1128/jb.187.24.8322-8331.2005 | "MalZ... removes glucose residues from the reducing end of maltodextrins longer than two glucose units" (dippel2005themaltodextrinsystem pages 2-2) | Strong. |
| maltose phosphorylase | cleaves | maltose to glucose + glucose-1-phosphate | 10.1111/mmi.12183 | "MalP phosphorolyzes maltose... into glucose 1-phosphate and glucose" (mokhtari2013enterococcusfaecalisutilizes pages 4-5) | Strong, but note this MalP is maltose phosphorylase in E. faecalis and not the E. coli maltodextrin phosphorylase. |
| glucoamylase (GH15) | hydrolyzes | starch to glucose | 10.3389/fbioe.2020.00871 | "Glucoamylases (EC 3.2.1.3) are exo-acting enzymes that cleave both α-1,4 and α-1,6 linkages to release glucose" (sidar2020carbohydratebindingmodules pages 2-3) | Strong general edge, especially relevant in fungi. |
| pullulanase | debranches | amylopectin (α-1,6 linkages) | 10.1007/s00018-016-2242-x | "pullulanases acting on α(1,6)-linkages" (foley2016thesusoperon pages 1-2) | Moderate: source describes pullulanase class generally; amylopectin debranching is mechanistically standard but not directly quoted here. Mark as slightly inferred. |
| CBM (e.g., CBM58) | enhances | amylase activity via starch binding | 10.1007/s00018-016-2242-x | "Both CBM58 and surface starch-binding sites enhance catalysis by localizing the starch polymer near the active site" (foley2016thesusoperon pages 5-7) | Strong for SusG CBM58; generalization to other CBMs is reasonable but broader. |
| carbon catabolite repression | represses | amylase gene expression | 10.1016/S1369-5274(99)80034-4 | "gene cluster that can be induced by maltose and repressed by [glucose]" (davidson2010bindingproteindependentuptake pages 2-4) | Moderate: broad CCR evidence; not starch-specific in all taxa. Curate as general regulatory context, not universal edge. |
| PTS maltose transporter | transports_and_phosphorylates | maltose to maltose-6-phosphate | 10.1111/mmi.12183 | "Bacillus subtilis, Enterococcus faecalis... use an inducible... phosphotransferase system (PTS) as a high-affinity maltose transporter" and in E. faecalis maltose is "phosphorylated to maltose-6-phosphate" (mokhtari2013enterococcusfaecalisutilizes pages 1-2) | Strong but taxon-specific to PTS-using Firmicutes. |
| LamB | permits_entry_of | maltodextrins | 10.1128/jb.187.24.8322-8331.2005 | "LamB (outer membrane porin)" is part of the maltodextrin system (dippel2005themaltodextrinsystem pages 1-2) | Moderate: source identifies LamB as maltoporin; passive entry function is standard but only partly explicit in snippet. |
| acarbose | inhibits | SusB / GH97 | 10.1128/mbio.01506-24 | "Acarbose inhibits SusB competitively by binding to the enzyme's active site with inhibition constants in the nanomolar range" (brown2024acarboseimpairsgut pages 9-12) | Strong recent inhibitory edge. |
| glucose | is_product_of | starch degradation | 10.1007/s00018-016-2242-x | "SusA... and SusB... further depolymerize the oligosaccharides into glucose" (foley2016thesusoperon pages 2-3) | Strong outcome edge for trait. |
| glucose-1-phosphate | is_converted_to | glucose-6-phosphate | 10.1128/jb.187.24.8322-8331.2005 | "glucose-1-phosphate... [is] then converted to glucose-6-phosphate by... phosphoglucomutase" (dippel2005themaltodextrinsystem pages 2-2) | Strong. |
| glucose-6-phosphate | enters | glycolysis | 10.1128/jb.187.24.8322-8331.2005 | "before entering glycolysis" (dippel2005themaltodextrinsystem pages 2-2) | Strong. |
| cyclodextrinase | hydrolyzes | cyclodextrins | 10.1128/AEM.01521-23 | "CjAmy13E... is a cyclodextrinase... cleaved multiple substrates but preferred cyclodextrins" (mascelli2024geneticandenzymatic pages 8-10, mascelli2024geneticandenzymatic pages 12-13) | Strong recent edge. |
| CGTase | cyclizes | maltooligosaccharides to cyclodextrins | 10.1128/AEM.01521-23 | "cyclodextrins are generated during starch metabolism through circularization of malto-oligosaccharides by cyclodextrin glucanotransferases (CGTases)" (mascelli2024geneticandenzymatic pages 7-8) | Strong. |
| MalT | activates | mal regulon | 10.1128/jb.187.24.8322-8331.2005 | "The E. coli maltose/maltodextrin system... consists of 10 genes regulated by MalT" (dippel2005themaltodextrinsystem pages 1-2) | Strong, though predicate could also be regulates_transcription_of. |
| PUL | encodes | Sus-like system | 10.1128/jb.00860-16 | "SusC, an outer membrane TonB-dependent transporter... SusD homologs function as surface glycan-binding proteins" within "polysaccharide utilization loci" (grondin2017polysaccharideutilizationloci pages 3-5) | Strong for Bacteroidetes PUL architecture encoding SusC/D-like transport-plus-CAZyme systems. |


*Table: This table lists evidence-backed candidate subject-predicate-object edges for curating a TraitMech causal graph of microbial starch degradation. It emphasizes core hydrolysis, transport, regulation, intracellular processing, and inhibitor relationships, with notes highlighting taxon specificity or inference strength.*

---

## 4. Ontology Grounding Summary

| Entity | Suggested CURIE |
|---|---|
| Starch | CHEBI:28017 |
| Glucose | CHEBI:17234 |
| Maltose | CHEBI:17306 |
| Maltotriose | CHEBI:63533 |
| Glucose-1-phosphate | CHEBI:4170 |
| Glucose-6-phosphate | CHEBI:61548 |
| Maltose-6-phosphate | CHEBI:15603 |
| α-Amylase | EC:3.2.1.1 |
| β-Amylase | EC:3.2.1.2 |
| Glucoamylase | EC:3.2.1.3 |
| α-Glucosidase | EC:3.2.1.20 |
| Pullulanase (type I) | EC:3.2.1.41 |
| Cyclodextrinase | EC:3.2.1.54 |
| CGTase | EC:2.4.1.19 |
| Amylomaltase | EC:2.4.1.25 |
| Maltodextrin phosphorylase | EC:2.4.1.1 |
| Maltose phosphorylase | EC:2.4.1.8 |
| GH13 family | CAZy:GH13 |
| GH14 family | CAZy:GH14 |
| GH15 family | CAZy:GH15 |
| GH57 family | CAZy:GH57 |
| GH77 family | CAZy:GH77 |
| GH97 family | CAZy:GH97 |
| CBM58 | CAZy:CBM58 |
| Starch binding | GO:2001070 |
| α-1,4-glucan hydrolysis | GO:0004556 |
| Phosphorolysis | GO:0004645 |
| CCR | GO:0009401 |
| Periplasm | GO:0042597 |
| Outer membrane | GO:0019867 |
| Cytoplasm | GO:0005737 |
| Extracellular | GO:0005576 |

---

## 5. Recent Developments (2023–2024)

**Novel GH13 subfamily GH13_47:** Brown et al. (2023) characterized BoGH13A_Sus from *Bacteroides ovatus* as a novel α-amylase placed into a new GH13 subfamily (GH13_47), indicating continued expansion of known starch-degradation enzyme diversity in gut Bacteroidetes (foley2016thesusoperon pages 1-2).

**Cyclodextrinase substrate expansion:** Mascelli et al. (2024) reclassified Amy13E from *Cellvibrio japonicus* as a cyclodextrinase with unexpected activity on rare α-diglucosides (kojibiose, nigerose, isomaltose), broadening the known substrate scope of GH13 enzymes in starch-adjacent metabolism (mascelli2024geneticandenzymatic pages 8-10, mascelli2024geneticandenzymatic pages 7-8).

**Acarbose–microbiome interactions:** Brown et al. (2024) demonstrated that the diabetes drug acarbose inhibits *Bacteroides* starch degradation through a complex multi-target mechanism: competitive inhibition of periplasmic GH97 SusB (Ki ≈ 54 nM), competition for SusC transport, and binding to Sus transcriptional regulators (brown2024acarboseimpairsgut pages 1-3, brown2024acarboseimpairsgut pages 9-12, brown2024acarboseimpairsgut pages 16-18). This has implications for understanding drug–microbiome interactions.

**Polysaccharide size-dependent metabolism:** Wong et al. (2024) showed that *B. thetaiotaomicron* metabolic activity decreases with increasing polysaccharide molecular weight, demonstrating that Sus-like system efficiency is modulated by substrate physical properties, not just chemical composition (grondin2017polysaccharideutilizationloci pages 3-5).

**Resistant starch utilization in Clostridia:** Pickens & Cockburn (2024) demonstrated that *Clostridium butyricum* degrades resistant starch via synergistically acting GH13 enzymes, representing a rare direct starch-to-butyrate pathway in the gut (brown2024acarboseimpairsgut pages 16-18).

---

## 6. Warnings and Curation Caveats

1. **Taxon specificity of transport systems:** The Sus system (Bacteroidetes), mal regulon (enterobacteria), and PTS-based maltose uptake (Firmicutes) are phylogenetically restricted. Edges involving these systems should be marked with taxon qualifiers rather than treated as universal features of the starch degradation trait.

2. **SusA vs. SusB GH classification discrepancy:** Some sources describe SusA as a GH13 neopullulanase and SusB as a GH97 α-glucosidase (grondin2017polysaccharideutilizationloci pages 3-5, brown2024acarboseimpairsgut pages 1-3), while Grondin et al. (2017) described SusA as a "GH13 β 1,4-glucosidase" and SusB as a "GH97 β 1,6-glucosidase" (grondin2017polysaccharideutilizationloci pages 3-5). The GH97 classification for SusB is well-established and should be curated as such; the Grondin description of linkage specificity should be verified before curation.

3. **Resistant starch as a distinct sub-trait:** Resistant starch degradation requires specialized enzymatic synergy and is restricted to few taxa. It should not be conflated with standard starch degradation without qualification.

4. **Acarbose inhibition edges:** While well-evidenced, acarbose is a pharmacological inhibitor and not a natural regulatory signal. These edges may be best curated as pharmacological annotations rather than core causal graph edges.

5. **CGTase/cyclodextrinase pathway:** The cyclodextrin branch of starch metabolism (CGTase cyclization → cyclodextrinase linearization) is not universally present and represents an alternative starch-processing route in specific taxa.

6. **Carbon catabolite repression:** CCR is a broad regulatory mechanism not specific to starch degradation. Its inclusion as a causal edge should reference the specific maltose/starch context rather than the general mechanism.

7. **GH119 and GH126 families:** These bacteria-specific amylase families are poorly characterized compared to GH13 and should be labeled as uncertain/tentative nodes pending further functional characterization.

---

## 7. DOI-First Bibliography

1. Foley, M. H., Cockburn, D. W., & Koropatkin, N. M. (2016). The Sus operon: a model system for starch uptake by the human gut Bacteroidetes. *Cellular and Molecular Life Sciences*, 73, 2603–2617. DOI: [10.1007/s00018-016-2242-x](https://doi.org/10.1007/s00018-016-2242-x)

2. Grondin, J. M., Tamura, K., Déjean, G., Abbott, D. W., & Brumer, H. (2017). Polysaccharide utilization loci: fueling microbial communities. *Journal of Bacteriology*, 199(15). DOI: [10.1128/jb.00860-16](https://doi.org/10.1128/jb.00860-16)

3. Sidar, A., et al. (2020). Carbohydrate binding modules: diversity of domain architecture in amylases and cellulases from filamentous microorganisms. *Frontiers in Bioengineering and Biotechnology*, 8, 871. DOI: [10.3389/fbioe.2020.00871](https://doi.org/10.3389/fbioe.2020.00871)

4. Dippel, R., & Boos, W. (2005). The maltodextrin system of *Escherichia coli*: metabolism and transport. *Journal of Bacteriology*, 187(24), 8322–8331. DOI: [10.1128/jb.187.24.8322-8331.2005](https://doi.org/10.1128/jb.187.24.8322-8331.2005)

5. Mokhtari, A., et al. (2013). *Enterococcus faecalis* utilizes maltose by connecting two incompatible metabolic routes via a novel maltose 6′-phosphate phosphatase (MapP). *Molecular Microbiology*, 88(2), 234–253. DOI: [10.1111/mmi.12183](https://doi.org/10.1111/mmi.12183)

6. Mascelli, G. M., Garcia, C. A., & Gardner, J. G. (2024). Genetic and enzymatic characterization of Amy13E from *Cellvibrio japonicus* reclassifies it as a cyclodextrinase also capable of α-diglucoside degradation. *Applied and Environmental Microbiology*, 90(1). DOI: [10.1128/aem.01521-23](https://doi.org/10.1128/aem.01521-23)

7. Brown, H. A., et al. (2024). Acarbose impairs gut *Bacteroides* growth by targeting intracellular glucosidases. *mBio*, 15(12). DOI: [10.1128/mbio.01506-24](https://doi.org/10.1128/mbio.01506-24)

8. Brown, H. A., et al. (2023). BoGH13A_Sus from *Bacteroides ovatus* represents a novel α-amylase used for Bacteroides starch breakdown in the human gut. *Cellular and Molecular Life Sciences*, 80(8). DOI: [10.1007/s00018-023-04812-w](https://doi.org/10.1007/s00018-023-04812-w)

9. Wong, J. P. H., et al. (2024). *Bacteroides thetaiotaomicron* metabolic activity decreases with polysaccharide molecular weight. *mBio*, 15(3). DOI: [10.1128/mbio.02599-23](https://doi.org/10.1128/mbio.02599-23)

10. Pickens, T. L., & Cockburn, D. W. (2024). *Clostridium butyricum* Prazmowski can degrade and utilize resistant starch via a set of synergistically acting enzymes. *mSphere*, 9(1). DOI: [10.1128/msphere.00566-23](https://doi.org/10.1128/msphere.00566-23)

11. Davidson, A. L., & Alvarez, F. J. D. (2010). Binding protein-dependent uptake of maltose into cells via an ATP-binding cassette transporter. *EcoSal Plus*, 4(1). DOI: [10.1128/ecosalplus.3.3.3](https://doi.org/10.1128/ecosalplus.3.3.3)

12. Stülke, J., & Hillen, W. (1999). Carbon catabolite repression in bacteria. *Current Opinion in Microbiology*, 2(2), 195–201. DOI: [10.1016/s1369-5274(99)80034-4](https://doi.org/10.1016/s1369-5274(99)80034-4)

13. Ravcheev, D. A., et al. (2013). Polysaccharides utilization in human gut bacterium *Bacteroides thetaiotaomicron*: comparative genomics reconstruction of metabolic and regulatory networks. *BMC Genomics*, 14, 873. DOI: [10.1186/1471-2164-14-873](https://doi.org/10.1186/1471-2164-14-873)

14. Arumapperuma, T., et al. (2023). A subfamily classification to choreograph the diverse activities within glycoside hydrolase family 31. *Journal of Biological Chemistry*, 299(4), 103038. DOI: [10.1016/j.jbc.2023.103038](https://doi.org/10.1016/j.jbc.2023.103038)

15. van der Maarel, M. J. E. C., et al. (2002). Properties and applications of starch-converting enzymes of the α-amylase family. DOI: [10.1016/S0168-1656(01)00407-2](https://doi.org/10.1016/S0168-1656(01)00407-2) (existing evidence in trait definition)

16. Lombard, V., et al. (2014). The carbohydrate-active enzymes database (CAZy) in 2013. *Nucleic Acids Research*, 42(D1). DOI: [10.1093/nar/gkt1178](https://doi.org/10.1093/nar/gkt1178) (existing evidence in trait definition)

References

1. (foley2016thesusoperon pages 1-2): Matthew H. Foley, Darrell W. Cockburn, and Nicole M. Koropatkin. The sus operon: a model system for starch uptake by the human gut bacteroidetes. Cellular and Molecular Life Sciences, 73:2603-2617, May 2016. URL: https://doi.org/10.1007/s00018-016-2242-x, doi:10.1007/s00018-016-2242-x. This article has 302 citations and is from a domain leading peer-reviewed journal.

2. (sidar2020carbohydratebindingmodules pages 2-3): Andika Sidar, Erica D. Albuquerque, Gerben P. Voshol, Arthur F. J. Ram, Erik Vijgenboom, and Peter J. Punt. Carbohydrate binding modules: diversity of domain architecture in amylases and cellulases from filamentous microorganisms. Frontiers in Bioengineering and Biotechnology, Jul 2020. URL: https://doi.org/10.3389/fbioe.2020.00871, doi:10.3389/fbioe.2020.00871. This article has 179 citations.

3. (brown2024acarboseimpairsgut pages 16-18): Haley A. Brown, Adeline L. Morris, Nicholas A. Pudlo, Ashley E. Hopkins, Eric C. Martens, Jonathan L. Golob, and Nicole M. Koropatkin. Acarbose impairs gut <i>bacteroides</i> growth by targeting intracellular glucosidases. Dec 2024. URL: https://doi.org/10.1128/mbio.01506-24, doi:10.1128/mbio.01506-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

4. (dippel2005themaltodextrinsystem pages 1-2): Renate Dippel and Winfried Boos. The maltodextrin system of escherichia coli: metabolism and transport. Journal of Bacteriology, 187:8322-8331, Dec 2005. URL: https://doi.org/10.1128/jb.187.24.8322-8331.2005, doi:10.1128/jb.187.24.8322-8331.2005. This article has 168 citations and is from a peer-reviewed journal.

5. (dippel2005themaltodextrinsystem pages 2-2): Renate Dippel and Winfried Boos. The maltodextrin system of escherichia coli: metabolism and transport. Journal of Bacteriology, 187:8322-8331, Dec 2005. URL: https://doi.org/10.1128/jb.187.24.8322-8331.2005, doi:10.1128/jb.187.24.8322-8331.2005. This article has 168 citations and is from a peer-reviewed journal.

6. (foley2016thesusoperon pages 2-3): Matthew H. Foley, Darrell W. Cockburn, and Nicole M. Koropatkin. The sus operon: a model system for starch uptake by the human gut bacteroidetes. Cellular and Molecular Life Sciences, 73:2603-2617, May 2016. URL: https://doi.org/10.1007/s00018-016-2242-x, doi:10.1007/s00018-016-2242-x. This article has 302 citations and is from a domain leading peer-reviewed journal.

7. (mascelli2024geneticandenzymatic pages 7-8): Giulia M. Mascelli, Cecelia A. Garcia, and Jeffrey G. Gardner. Genetic and enzymatic characterization of amy13e from <i>cellvibrio japonicus</i> reclassifies it as a cyclodextrinase also capable of α-diglucoside degradation. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01521-23, doi:10.1128/aem.01521-23. This article has 4 citations and is from a peer-reviewed journal.

8. (mascelli2024geneticandenzymatic pages 12-13): Giulia M. Mascelli, Cecelia A. Garcia, and Jeffrey G. Gardner. Genetic and enzymatic characterization of amy13e from <i>cellvibrio japonicus</i> reclassifies it as a cyclodextrinase also capable of α-diglucoside degradation. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01521-23, doi:10.1128/aem.01521-23. This article has 4 citations and is from a peer-reviewed journal.

9. (mokhtari2013enterococcusfaecalisutilizes pages 1-2): Abdelhamid Mokhtari, Víctor S. Blancato, Guillermo D. Repizo, Céline Henry, Andreas Pikis, Alexa Bourand, María de Fátima Álvarez, Stefan Immel, Aicha Mechakra‐Maza, Axel Hartke, John Thompson, Christian Magni, and Josef Deutscher. Enterococcus faecalis utilizes maltose by connecting two incompatible metabolic routes via a novel maltose 6′‐phosphate phosphatase (mapp). Molecular Microbiology, 88:234-253, Apr 2013. URL: https://doi.org/10.1111/mmi.12183, doi:10.1111/mmi.12183. This article has 39 citations and is from a domain leading peer-reviewed journal.

10. (dippel2005themaltodextrinsystem pages 7-8): Renate Dippel and Winfried Boos. The maltodextrin system of escherichia coli: metabolism and transport. Journal of Bacteriology, 187:8322-8331, Dec 2005. URL: https://doi.org/10.1128/jb.187.24.8322-8331.2005, doi:10.1128/jb.187.24.8322-8331.2005. This article has 168 citations and is from a peer-reviewed journal.

11. (dippel2005themaltodextrinsystem pages 4-5): Renate Dippel and Winfried Boos. The maltodextrin system of escherichia coli: metabolism and transport. Journal of Bacteriology, 187:8322-8331, Dec 2005. URL: https://doi.org/10.1128/jb.187.24.8322-8331.2005, doi:10.1128/jb.187.24.8322-8331.2005. This article has 168 citations and is from a peer-reviewed journal.

12. (mokhtari2013enterococcusfaecalisutilizes pages 2-4): Abdelhamid Mokhtari, Víctor S. Blancato, Guillermo D. Repizo, Céline Henry, Andreas Pikis, Alexa Bourand, María de Fátima Álvarez, Stefan Immel, Aicha Mechakra‐Maza, Axel Hartke, John Thompson, Christian Magni, and Josef Deutscher. Enterococcus faecalis utilizes maltose by connecting two incompatible metabolic routes via a novel maltose 6′‐phosphate phosphatase (mapp). Molecular Microbiology, 88:234-253, Apr 2013. URL: https://doi.org/10.1111/mmi.12183, doi:10.1111/mmi.12183. This article has 39 citations and is from a domain leading peer-reviewed journal.

13. (foley2016thesusoperon pages 5-7): Matthew H. Foley, Darrell W. Cockburn, and Nicole M. Koropatkin. The sus operon: a model system for starch uptake by the human gut bacteroidetes. Cellular and Molecular Life Sciences, 73:2603-2617, May 2016. URL: https://doi.org/10.1007/s00018-016-2242-x, doi:10.1007/s00018-016-2242-x. This article has 302 citations and is from a domain leading peer-reviewed journal.

14. (grondin2017polysaccharideutilizationloci pages 3-5): Julie M. Grondin, Kazune Tamura, Guillaume Déjean, D. Wade Abbott, and Harry Brumer. Polysaccharide utilization loci: fueling microbial communities. Journal of Bacteriology, Aug 2017. URL: https://doi.org/10.1128/jb.00860-16, doi:10.1128/jb.00860-16. This article has 631 citations and is from a peer-reviewed journal.

15. (brown2024acarboseimpairsgut pages 9-12): Haley A. Brown, Adeline L. Morris, Nicholas A. Pudlo, Ashley E. Hopkins, Eric C. Martens, Jonathan L. Golob, and Nicole M. Koropatkin. Acarbose impairs gut <i>bacteroides</i> growth by targeting intracellular glucosidases. Dec 2024. URL: https://doi.org/10.1128/mbio.01506-24, doi:10.1128/mbio.01506-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

16. (mascelli2024geneticandenzymatic pages 8-10): Giulia M. Mascelli, Cecelia A. Garcia, and Jeffrey G. Gardner. Genetic and enzymatic characterization of amy13e from <i>cellvibrio japonicus</i> reclassifies it as a cyclodextrinase also capable of α-diglucoside degradation. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01521-23, doi:10.1128/aem.01521-23. This article has 4 citations and is from a peer-reviewed journal.

17. (mokhtari2013enterococcusfaecalisutilizes pages 4-5): Abdelhamid Mokhtari, Víctor S. Blancato, Guillermo D. Repizo, Céline Henry, Andreas Pikis, Alexa Bourand, María de Fátima Álvarez, Stefan Immel, Aicha Mechakra‐Maza, Axel Hartke, John Thompson, Christian Magni, and Josef Deutscher. Enterococcus faecalis utilizes maltose by connecting two incompatible metabolic routes via a novel maltose 6′‐phosphate phosphatase (mapp). Molecular Microbiology, 88:234-253, Apr 2013. URL: https://doi.org/10.1111/mmi.12183, doi:10.1111/mmi.12183. This article has 39 citations and is from a domain leading peer-reviewed journal.

18. (davidson2010bindingproteindependentuptake pages 1-2): Amy L. Davidson and Frances Joan D. Alvarez. Binding protein-dependent uptake of maltose into cells via an atp-binding cassette transporter. Dec 2010. URL: https://doi.org/10.1128/ecosalplus.3.3.3, doi:10.1128/ecosalplus.3.3.3. This article has 4 citations.

19. (foley2016thesusoperon pages 10-12): Matthew H. Foley, Darrell W. Cockburn, and Nicole M. Koropatkin. The sus operon: a model system for starch uptake by the human gut bacteroidetes. Cellular and Molecular Life Sciences, 73:2603-2617, May 2016. URL: https://doi.org/10.1007/s00018-016-2242-x, doi:10.1007/s00018-016-2242-x. This article has 302 citations and is from a domain leading peer-reviewed journal.

20. (davidson2010bindingproteindependentuptake pages 2-4): Amy L. Davidson and Frances Joan D. Alvarez. Binding protein-dependent uptake of maltose into cells via an atp-binding cassette transporter. Dec 2010. URL: https://doi.org/10.1128/ecosalplus.3.3.3, doi:10.1128/ecosalplus.3.3.3. This article has 4 citations.

21. (foley2016thesusoperon pages 8-10): Matthew H. Foley, Darrell W. Cockburn, and Nicole M. Koropatkin. The sus operon: a model system for starch uptake by the human gut bacteroidetes. Cellular and Molecular Life Sciences, 73:2603-2617, May 2016. URL: https://doi.org/10.1007/s00018-016-2242-x, doi:10.1007/s00018-016-2242-x. This article has 302 citations and is from a domain leading peer-reviewed journal.

22. (foley2016thesusoperon pages 7-8): Matthew H. Foley, Darrell W. Cockburn, and Nicole M. Koropatkin. The sus operon: a model system for starch uptake by the human gut bacteroidetes. Cellular and Molecular Life Sciences, 73:2603-2617, May 2016. URL: https://doi.org/10.1007/s00018-016-2242-x, doi:10.1007/s00018-016-2242-x. This article has 302 citations and is from a domain leading peer-reviewed journal.

23. (brown2024acarboseimpairsgut pages 1-3): Haley A. Brown, Adeline L. Morris, Nicholas A. Pudlo, Ashley E. Hopkins, Eric C. Martens, Jonathan L. Golob, and Nicole M. Koropatkin. Acarbose impairs gut <i>bacteroides</i> growth by targeting intracellular glucosidases. Dec 2024. URL: https://doi.org/10.1128/mbio.01506-24, doi:10.1128/mbio.01506-24. This article has 3 citations and is from a domain leading peer-reviewed journal.