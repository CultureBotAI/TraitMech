---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T00:54:03.665493'
end_time: '2026-08-04T01:02:55.592152'
duration_seconds: 531.93
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: halotolerant
  trait_identifier: METPO:1000622
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: halotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A halophily preference in which an organism can tolerate high salt concentrations
    but does not require them for growth.
  parent_traits: METPO:1000629
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: highly halotolerant representatives
    (Supports halotolerant microorganisms as high-salt tolerant without strict salt
    requirement.) | PMID:27621824: Halomonas massiliensis sp. nov., a new halotolerant
    bacterium (Organism example: Halomonas massiliensis is described as halotolerant.)'
  causal_graph_summary: 'halotolerant_salt_stress_response: 12 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** halotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000622
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can tolerate high salt concentrations but does not require them for growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: highly halotolerant representatives (Supports halotolerant microorganisms as high-salt tolerant without strict salt requirement.) | PMID:27621824: Halomonas massiliensis sp. nov., a new halotolerant bacterium (Organism example: Halomonas massiliensis is described as halotolerant.)
- **Existing causal graph summary:** halotolerant_salt_stress_response: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **halotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/halotolerant.yaml`.

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
- **Trait label:** halotolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000622
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A halophily preference in which an organism can tolerate high salt concentrations but does not require them for growth.
- **Parent traits:** METPO:1000629
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: highly halotolerant representatives (Supports halotolerant microorganisms as high-salt tolerant without strict salt requirement.) | PMID:27621824: Halomonas massiliensis sp. nov., a new halotolerant bacterium (Organism example: Halomonas massiliensis is described as halotolerant.)
- **Existing causal graph summary:** halotolerant_salt_stress_response: 12 nodes, 12 edges

## Research Objective

Research the microbial trait **halotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/halotolerant.yaml`.

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


# Curation report: microbial halotolerance

## Trait record and scope

- **Trait label:** halotolerant
- **Trait identifier:** **METPO:1000622**
- **Category / kind / status:** ENVIRONMENT / CLASS / REVIEWED
- **Definition:** “A halophily preference in which an organism can tolerate high salt concentrations but does not require them for growth.”
- **Parent:** METPO:1000629

### Operational interpretation

Halotolerance is a **whole-organism growth phenotype**, not a single pathway. A strain should grow reproducibly at elevated salt while also growing at low or zero added salt. The phenotype therefore needs at least a salt-tolerance endpoint and evidence of non-requirement, ideally a growth curve or growth range rather than survival alone.

This distinguishes halotolerant organisms from obligate halophiles, whose optimum and sometimes structural stability require salt. Extreme “salt-in” organisms may maintain molar cytoplasmic KCl and possess acidic, salt-adapted proteins that lose stability at low salt; this is a boundary phenotype rather than the default halotolerant mechanism. By contrast, the compatible-solute or “salt-out” strategy permits a broad salinity range without sustained high cytoplasmic ionic strength (sleator2002bacterialosmoadaptationthe pages 1-2, oren2008microbiallifeat pages 10-11, bremer2019responsesofmicroorganisms pages 3-5).

The trait is assay-dependent. Record salt identity, concentration and units, medium composition, pH, temperature, exposure duration, growth versus survival endpoint, and whether salt was imposed abruptly or chronically. NaCl combines **osmotic stress** with Na⁺/Cl⁻ toxicity; an iso-osmotic nonionic solute tests osmotic tolerance but does not establish NaCl tolerance. Salt shock and long-term acclimation can also produce different mechanisms and timing.

### Important boundary cases

1. **Halophilic versus halotolerant:** growth at high salt alone is insufficient; growth without salt must also be shown.
2. **Osmotolerant versus halotolerant:** tolerance of sucrose or polyethylene glycol does not necessarily imply tolerance of Na⁺ toxicity.
3. **Haloalkaliphilic:** combined high salt/high pH resistance may depend strongly on Na⁺/H⁺ antiport and should retain its pH context.
4. **Transient survival versus growth:** viability after exposure is weaker evidence than increased biomass or colony formation.
5. **Genomic potential versus phenotype:** compatible-solute or antiporter genes predict capacity but do not establish expression, flux, or halotolerant growth.
6. **Plant-beneficial effect:** enhancement of plant salt tolerance by a bacterium is an application phenotype, not direct evidence that the bacterium itself is halotolerant.

## Current mechanistic model

A high-salinity upshift lowers external water activity, causing water efflux, reduced hydration and turgor, increased macromolecular crowding, and—when NaCl is used—ionic and oxidative stress. Sustained growth requires restoration of osmotic potential without intolerable cytoplasmic Na⁺. Most candidate graphs should therefore contain: (i) an early ion-response branch, especially K⁺; (ii) compatible-solute synthesis or uptake; (iii) Na⁺ and pH homeostasis; (iv) antioxidant and energy-management branches; and (v) mechanosensitive release following a hypoosmotic downshift (bremer2019responsesofmicroorganisms pages 3-5, yu2024temporaldynamicsof pages 1-2).

Recent research indicates that the response is dynamic rather than a single fixed strategy. In *Halomonas elongata*, 1–8% NaCl shock produced rapid Na⁺/K⁺ and amino-acid accumulation, followed after approximately 20 minutes by ectoine becoming the dominant osmoprotectant. At 8% shock, ectoine productivity reached 1,450 ± 99 mg L⁻¹ h⁻¹; 13% caused strong, nonrecovering inhibition of growth and respiration. The ectA, ectB and ectC transcripts rose 22.0-, 7.1- and 3.3-fold at one hour, respectively (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 13-14, yu2024temporaldynamicsof pages 2-5).

A 2024 multi-omics study of the extremely halophilic alkalithermophile *Natranaerobius thermophilus* found a hybrid strategy: compatible-solute accumulation plus K⁺-based “salt-in” physiology. Glycine betaine rose from 52.7 mM at 2.5 M Na⁺ to 893.1 mM at 4.3 M; glutamate reached 221.3 mM and proline 130 mM at 4.3 M. Opu/ProU transporters, amino-acid synthesis, Na⁺/K⁺/H⁺ transport and a Na⁺-translocating F₀F₁-ATPase were implicated. Because this organism grows optimally around 3.3–3.9 M Na⁺, it is primarily an extreme-halophile model and its hybrid strategy should not be generalized to all halotolerant organisms (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 10-14).

## Candidate nodes grouped by type

### Environmental and experimental nodes

- high external NaCl concentration — **CHEBI:26710** for sodium chloride
- sodium ion — **CHEBI:29101**
- potassium ion — **CHEBI:29103**
- chloride — **CHEBI:17996**
- high external osmolarity / hyperosmotic stress — label-only unless the project’s preferred ontology supplies a verified term
- hypoosmotic downshift
- alkaline pH
- acute salt shock
- chronic salinity acclimation
- low water activity
- reduced cellular hydration and turgor

### Chemicals and metabolites

- ectoine — **CHEBI:42263**
- glycine betaine — **CHEBI:17750**
- L-proline — **CHEBI:17203**
- L-glutamate — **CHEBI:29985**
- L-glutamine — **CHEBI:18050**
- trehalose — **CHEBI:27082**
- hydroxyectoine — label-only pending identifier verification
- cysteine — **CHEBI:15356**
- reactive oxygen species — **CHEBI:26523**
- ATP — **CHEBI:15422**
- compatible-solute pool — label-only aggregate node

### Genes, proteins, transporters and complexes

- **ectA, ectB, ectC** — ectoine biosynthetic genes; use taxon-specific locus or UniProt identifiers only after strain selection
- Opu-family compatible-solute transport systems
- ProU ABC transporter
- OpuE proline transporter
- Trk/Kdp/Kup potassium-uptake systems
- Na⁺/H⁺ antiporter
- Na⁺(K⁺)/H⁺ antiporters **Ha-NhaD2, Ha-NhaP**
- multisubunit **Ha-Mrp** antiporter
- Na⁺-translocating F₀F₁-ATPase
- mechanosensitive channels MscL/MscS-family
- CysB transcriptional regulator
- peroxidase/peroxiredoxin
- catalase — molecular function **GO:0004096**
- respiratory-chain complex I
- ATP synthase complex
- glutamate/proline biosynthetic enzymes; retain gene-level nodes only where the source resolves the specific enzyme

### Processes and cellular functions

- cellular response to osmotic stress — **GO:0071470**
- response to oxidative stress — **GO:0006979**
- potassium-ion transport — **GO:0006813**
- sodium-ion transport — **GO:0006814**
- transmembrane transport — **GO:0055085**
- ectoine biosynthesis
- compatible-solute synthesis, uptake and accumulation
- ion homeostasis
- cytoplasmic pH homeostasis
- osmotic potential restoration
- antioxidant defense
- membrane/proteome adaptation
- solute efflux after hypoosmotic downshift
- growth under elevated salt — phenotype endpoint linked to **METPO:1000622**

Identifiers above should be validated against the exact ontology release used by TraitMech. No gene-level UniProt, KEGG, Rhea, EC or NCBITaxon identifier should be assigned without selecting the precise strain and sequence.

## Priority causal edges

The following table emphasizes edges that can be translated into subject–predicate–object statements. “Strong” denotes direct physiological, biochemical, loss-of-function, or metabolite evidence; “moderate” generally denotes multi-omic association or a mechanistic interpretation without direct perturbation.

| subject | predicate | object | evidence strength | taxon/assay | DOI and date | short supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| high external NaCl | causes | osmotic stress | strong | *Halomonas elongata* NaCl-shock physiology/metabolomics/transcriptomics | 10.1186/s12934-024-02358-5; Mar 2024 | “NaCl shock induced two major stresses, namely osmotic stress and oxidative stress.” (yu2024temporaldynamicsof pages 1-2) | Generalizable stress input node for halotolerance graph. |
| high external NaCl | causes | oxidative stress | strong | *Halomonas elongata* NaCl-shock physiology/metabolomics/transcriptomics | 10.1186/s12934-024-02358-5; Mar 2024 | “NaCl shock induced two major stresses, namely osmotic stress and oxidative stress.” (yu2024temporaldynamicsof pages 1-2) | Use as parallel branch to antioxidant defenses. |
| osmotic upshift / NaCl shock | increases | intracellular Na+ and K+ uptake | strong | *H. elongata*; metabolomic/ion measurements after 1–8% NaCl shock | 10.1186/s12934-024-02358-5; Mar 2024 | “within the cell’s tolerable range (1–8% NaCl shock), *H. elongata* urgently balanced the surging osmotic pressure by uptaking sodium and potassium ions” (yu2024temporaldynamicsof pages 1-2) | Good causal edge; taxon-specific kinetics but broadly plausible. |
| early Na+/K+ uptake | increases | osmotic balance / immediate osmoadaptation | moderate | *H. elongata*; short-term shock response | 10.1186/s12934-024-02358-5; Mar 2024 | “urgently balanced the surging osmotic pressure by uptaking sodium and potassium ions” (yu2024temporaldynamicsof pages 1-2) | Mechanistically supported in this organism; phenotype term may be modeled as “osmotic balance” label-only. |
| ectA/ectB/ectC expression | increases | ectoine biosynthesis/accumulation | moderate | *H. elongata* transcriptomics + metabolomics after NaCl shock | 10.1186/s12934-024-02358-5; Mar 2024 | “ectA, ectB, and ectC genes upregulated 22.0, 7.1, and 3.3-fold at 1 hour respectively” and “ectoine content did not significantly increase until 20 minutes post-shock” (yu2024temporaldynamicsof pages 13-14) | Expression-to-metabolite link is strong but partly inferred; mark uncertain if curating direct gene→metabolite edges. |
| ectoine accumulation | supports | osmoadaptation under salt stress | strong | *H. elongata* physiology/metabolomics; broader review support | 10.1186/s12934-024-02358-5; Mar 2024 | “ectoine content started to increase until 20 min post-shock, rapidly becoming the dominant osmoprotectant” (yu2024temporaldynamicsof pages 1-2) | High-priority compatible-solute node; organism-specific dynamics. |
| Opu/ProU-family transporters | increases | intracellular glycine betaine | moderate | *Natranaerobius thermophilus* proteome/transcripts/metabolites across 2.5–4.3 M Na+ | 10.1128/AEM.00145-24; May 2024 | “employs the glycine betaine ABC transporters (Opu and ProU families)… The intracellular content of compatible solutes, including glycine betaine… increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19) | Strong at pathway level, but transporter-specific causality is expression/correlation rather than knockout. Mark uncertain. |
| glutamate and proline synthesis pathways | increase | compatible-solute pools | moderate | *N. thermophilus* proteome/transcripts/metabolites across salinity gradient | 10.1128/AEM.00145-24; May 2024 | “glutamate and proline synthesis pathways” are used to adapt to high salinity; “glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 1-2) | Suitable pathway→metabolite edges; direct enzyme-level grounding may need follow-up. |
| compatible-solute pools | maintain | cellular osmotic potential / salt-out adaptation | strong | broad bacterial osmoadaptation review | 10.1146/annurev-micro-020518-115504; Sep 2019 | “bacteria accumulate compatible solutes while tightly controlling K+ and Na+ pools. This allows osmotic potential maintenance without increasing ionic strength” (bremer2019responsesofmicroorganisms pages 3-5) | Broad, authoritative edge for generic trait graph. |
| Ha-NhaD2 antiporter | supports | growth at high Na+(Li+) / osmotic homeostasis | strong | *Halomonas* sp. Y2 deletion + complementation assays | 10.1074/jbc.M116.751016; Dec 2016 | “A ΔHa-nhaD2 mutant showed growth inhibition at high Na+(Li+) concentrations across multiple pH conditions” (cheng(程彬)2016alkalineresponseof pages 1-2) | High-confidence gene→phenotype edge from loss-of-function evidence. |
| Ha-Mrp antiporter complex | supports | alkaline cation homeostasis | strong | *Halomonas* sp. Y2 deletion phenotypes under Na+/Li+/K+ and alkaline pH | 10.1074/jbc.M116.751016; Dec 2016 | “Ha-mrp deletion significantly inhibited growth under alkaline stress at pH 10.0” and mutant was “severely inhibited by high Na+(Li+, K+) concentrations, but specifically under alkaline conditions” (cheng(程彬)2016alkalineresponseof pages 1-2, cheng(程彬)2016alkalineresponseof pages 8-9) | Curate as antiporter-complex contribution to pH/cation homeostasis rather than generic halotolerance alone. |
| cysB transcription factor | increases | sulfur metabolism and cysteine biosynthesis response | moderate | *H. elongata* transcriptomics after NaCl shock | 10.1186/s12934-024-02358-5; Mar 2024 | “transcription factor cys B was significantly upregulated, positively regulating the sulfur metabolism and cysteine biosynthesis” (yu2024temporaldynamicsof pages 1-2) | Expression/regulatory interpretation from one study; mark uncertain. |
| peroxidase/catalase defense | reduces | oxidative stress damage | moderate | *H. elongata* transcriptomics + enzyme assays after NaCl shock | 10.1186/s12934-024-02358-5; Mar 2024 | “upregulation of the crucial peroxidase gene… and the simultaneous enhancement of peroxidase (POD) and catalase (CAT) activities collectively constitute the antioxidant defense” (yu2024temporaldynamicsof pages 1-2) | Good process-level edge; direct damage reduction is inferred from defense role. |
| excessive NaCl beyond tolerance threshold | inhibits | respiratory chain / ATP synthase and growth | moderate | *H. elongata* high-shock experiments, especially 13% NaCl | 10.1186/s12934-024-02358-5; Mar 2024 | “When exceeding the tolerance threshold… (1–13% NaCl shock), the sustained compromised energy status, resulting from the pronounced inhibition of the respiratory chain and ATP synthase, may be a crucial factor leading to the stagnation of both cell growth and ectoine biosynthesis” (yu2024temporaldynamicsof pages 1-2) | Important negative edge; causal wording includes “may,” so mark uncertain/inferred. |
| mechanosensitive channels | release | organic and inorganic solutes after hypoosmotic downshift | strong | broad bacterial osmotic-stress review | 10.1146/annurev-micro-020518-115504; Sep 2019 | “Under hypoosmotic conditions, mechanosensitive channels rapidly release organic and inorganic compounds nonspecifically” (bremer2019responsesofmicroorganisms pages 3-5) | Valuable recovery/transition edge; not specific to high-salt growth assay. |
| KCl salt-in strategy | requires | acidic proteome adaptation | strong | broad halophile review across taxa | 10.1186/1746-1448-4-2; Apr 2008 | “The primary osmotic adaptation strategy involves accumulation of KCl and enzymatic machinery adapted to high salt presence” and such proteomes are “highly acidic” (oren2008microbiallifeat pages 10-11, sleator2002bacterialosmoadaptationthe pages 1-2) | Boundary-case edge: more typical of obligate/extreme halophiles than general halotolerant microbes; curate cautiously. |


*Table: This table summarizes the highest-priority causal edges for curating a microbial halotolerance TraitMech graph, emphasizing direct experimental evidence where available and clearly marking expression-based or inferred claims. It helps separate broadly supported osmoadaptation mechanisms from taxon-specific or boundary-case features.*

## Additional high-confidence antiporter evidence

The strongest gene-level perturbation evidence comes from *Halomonas* sp. Y2. A ΔHa-nhaD2 mutant was inhibited at high Na⁺/Li⁺ across pH 6.2, 8.0 and 10.0. At pH 8 with 15% NaCl, ΔHa-mrp reached OD₆₂₀ 0.21 versus 2.81 for wild type; at pH 10 with 15% NaCl it reached 0.09 versus 2.11. Under pH 10 plus 8% KCl, ΔHa-mrp reached 0.05 versus 4.48. Heterologous complementation in Na⁺-antiporter-deficient *E. coli* KNabc and K⁺-uptake-deficient TK2420 further separated the functions of Ha-NhaD1, Ha-NhaD2, Ha-NhaP and Ha-Mrp (cheng(程彬)2016alkalineresponseof pages 18-21, cheng(程彬)2016alkalineresponseof pages 4-5, cheng(程彬)2016alkalineresponseof pages 1-2, cheng(程彬)2016alkalineresponseof pages 17-18).

Recommended triples are therefore:

- **Ha-NhaD2 — positively_regulates — growth under high Na⁺/Li⁺** [strong; *Halomonas* sp. Y2]
- **Ha-Mrp complex — positively_regulates — alkaline cation homeostasis** [strong; high-pH dependent]
- **Ha-NhaP — contributes_to — K⁺ homeostasis across pH** [moderate; taxon-specific]

Do not collapse these into “all Na⁺/H⁺ antiporters cause halotolerance.” The study demonstrates division of labor, and some activities were weak or conditional (cheng(程彬)2016alkalineresponseof pages 6-8, cheng(程彬)2016alkalineresponseof pages 8-9).

## Evidence strength and recommended graph architecture

### Core graph appropriate for broad curation

1. high external NaCl → increased osmotic and ionic stress;
2. osmotic stress → water efflux/reduced hydration and turgor;
3. early K⁺ uptake → partial restoration of osmotic balance;
4. compatible-solute synthesis/uptake → compatible-solute accumulation;
5. compatible-solute accumulation → restored osmotic potential with limited ionic interference;
6. Na⁺/H⁺ antiport → Na⁺ and pH homeostasis;
7. antioxidant enzymes → mitigation of salt-associated oxidative stress;
8. restored osmotic, ionic and redox homeostasis → growth at elevated salt;
9. hypoosmotic downshift → mechanosensitive-channel opening → solute release and lysis avoidance.

Compatible solutes documented across bacteria include proline, glycine betaine, ectoine/hydroxyectoine, trehalose, carnitine, proline betaine, dimethylsulfoniopropionate and glucosylglycerol. Mechanosensitive channels rapidly release organic and inorganic solutes during hypoosmotic downshift (bremer2019responsesofmicroorganisms pages 3-5).

### Optional taxon-specific branches

- *H. elongata*: ectABC induction, delayed ectoine accumulation, CysB/sulfur metabolism, peroxidase and catalase response, and energy limitation above the shock threshold (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 13-14, yu2024temporaldynamicsof pages 14-16).
- *N. thermophilus*: Opu/ProU-mediated betaine uptake, glutamate/proline accumulation, K⁺ retention, cytoplasmic/proteome acidification and hybrid salt-in/salt-out adaptation (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 1-2).
- *Halomonas* sp. Y2: Ha-NhaD2 and Ha-Mrp loss-of-function branches for saline and haloalkaline growth (cheng(程彬)2016alkalineresponseof pages 1-2, cheng(程彬)2016alkalineresponseof pages 17-18).
- Extreme halophiles: molar KCl and an acidic proteome; treat as a boundary module rather than a universal halotolerance mechanism (sleator2002bacterialosmoadaptationthe pages 1-2, oren2008microbiallifeat pages 10-11).

## Recent developments, applications and real-world relevance

### Industrial ectoine production

*H. elongata* is an industrial ectoine producer. The 2024 time-resolved study shows that process performance depends on shock magnitude and timing: ectoine synthesis is delayed relative to ion/amino-acid responses, reaches 1,450 ± 99 mg L⁻¹ h⁻¹ after tolerable shock, and collapses when excessive shock compromises respiration and ATP production. This supports staged salinity control rather than assuming that more NaCl always increases ectoine yield (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 14-16, yu2024temporaldynamicsof pages 2-5).

### Saline and alkaline bioprocesses

Halotolerant microbes are relevant to open or low-sterility fermentation, hypersaline wastewater treatment, bioremediation and production of compatible solutes, enzymes, pigments and polymers. The isolation of *Halomonas* sp. Y2 from alkaline pulp-mill wastewater illustrates a real environmental setting in which simultaneous salt and pH homeostasis is advantageous (cheng(程彬)2016alkalineresponseof pages 8-9).

### Agriculture

Salt-tolerant plant-growth-promoting bacteria are being investigated as inoculants for saline agriculture. Proposed benefits include rhizosphere colonization, biofilms/exopolysaccharides, nutrient mobilization, phytohormone modulation and improved plant K⁺/Na⁺ balance. However, these plant outcomes should be represented in a separate host-interaction graph unless the same study directly measures bacterial growth over a defined salinity range. They are applications of halotolerant organisms, not defining causal evidence for METPO:1000622.

## Warnings: claims not yet ready for TraitMech

1. **Do not curate gene presence as causality.** Genome annotation of ectABC, betaine transporters or antiporters is hypothesis-generating without expression, mutant, transport, metabolite or growth evidence.
2. **Do not generalize extreme-halophile salt-in physiology.** *N. thermophilus* and haloarchaea may require high salt and therefore fail the strict “does not require salt” criterion.
3. **Mark transcript-only edges uncertain.** ectABC→ectoine, cysB→cysteine defense and transporter→solute accumulation are strengthened by matched metabolite or enzyme data, but not necessarily by targeted knockouts.
4. **Treat oxidative-defense edges as contributory.** Increased catalase or peroxidase activity after salt shock does not by itself prove that the enzyme is necessary for halotolerant growth.
5. **Retain threshold and time context.** In *H. elongata*, 5–8% shocks allowed recovery whereas 13% did not; a categorical edge that omits dose would hide a biologically important reversal (yu2024temporaldynamicsof pages 2-5).
6. **Do not equate osmotic and ionic stress.** Results from nonionic osmolytes cannot automatically be assigned to NaCl tolerance.
7. **Do not infer broad taxonomy from one strain.** Antiporter paralogs have distinct functions even within one *Halomonas* strain.
8. **Separate acclimation from evolution.** Short-term transcriptional responses do not establish stable inherited adaptation.
9. **Avoid unverified CURIEs.** Label-only nodes are preferable to guessed GO, KEGG, Rhea, EC, MetaCyc or UniProt identifiers.
10. **Avoid curating the salt requirement boundary without low-salt controls.** A high maximum tolerated concentration does not demonstrate halotolerance if the organism’s minimum salt requirement is unknown.

## DOI-first bibliography

1. Yu J. et al. “Temporal dynamics of stress response in *Halomonas elongata* to NaCl shock: physiological, metabolomic, and transcriptomic insights.” *Microbial Cell Factories* 23, March 2024. DOI: [10.1186/s12934-024-02358-5](https://doi.org/10.1186/s12934-024-02358-5). (yu2024temporaldynamicsof pages 1-2, yu2024temporaldynamicsof pages 13-14)
2. Xing Q. et al. “The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K⁺.” *Applied and Environmental Microbiology* 90, May 2024. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 1-2)
3. Cheng B. et al. “Alkaline Response of a Halotolerant Alkaliphilic *Halomonas* Strain and Functional Diversity of Its Na⁺(K⁺)/H⁺ Antiporters.” *Journal of Biological Chemistry* 291:26056–26065, December 2016. DOI: [10.1074/jbc.M116.751016](https://doi.org/10.1074/jbc.M116.751016). (cheng(程彬)2016alkalineresponseof pages 6-8, cheng(程彬)2016alkalineresponseof pages 17-18)
4. Bremer E., Krämer R. “Responses of Microorganisms to Osmotic Stress.” *Annual Review of Microbiology* 73:313–334, September 2019. DOI: [10.1146/annurev-micro-020518-115504](https://doi.org/10.1146/annurev-micro-020518-115504). (bremer2019responsesofmicroorganisms pages 3-5)
5. Gunde-Cimerman N., Plemenitaš A., Oren A. “Strategies of adaptation of microorganisms of the three domains of life to high salt concentrations.” *FEMS Microbiology Reviews* 42:353–375, May 2018. DOI: [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009).
6. Oren A. “Microbial life at high salt concentrations: phylogenetic and metabolic diversity.” *Saline Systems* 4:2, April 2008. DOI: [10.1186/1746-1448-4-2](https://doi.org/10.1186/1746-1448-4-2). (oren2008microbiallifeat pages 10-11)
7. Sleator R.D., Hill C. “Bacterial osmoadaptation: the role of osmolytes in bacterial stress and virulence.” *FEMS Microbiology Reviews* 26:49–71, March 2002. DOI: [10.1111/j.1574-6976.2002.tb00598.x](https://doi.org/10.1111/j.1574-6976.2002.tb00598.x). (sleator2002bacterialosmoadaptationthe pages 1-2)

## Curation recommendation

The existing 12-node/12-edge `halotolerant_salt_stress_response` graph should be expanded conservatively around three strongly supported modules: **compatible-solute homeostasis**, **cation/pH homeostasis**, and **oxidative/energy stress**. The broad graph should terminate in experimentally measured growth at elevated salt while preserving a low/no-salt growth condition. Extreme-halophile hybrid strategies, individual antiporter paralogs and expression-only regulatory edges should be represented as taxon-specific or uncertain subgraphs rather than universal causes of **METPO:1000622**.

References

1. (sleator2002bacterialosmoadaptationthe pages 1-2): Roy D. Sleator and Colin Hill. Bacterial osmoadaptation: the role of osmolytes in bacterial stress and virulence. FEMS Microbiology Reviews, 26:49-71, Mar 2002. URL: https://doi.org/10.1111/j.1574-6976.2002.tb00598.x, doi:10.1111/j.1574-6976.2002.tb00598.x. This article has 1112 citations and is from a domain leading peer-reviewed journal.

2. (oren2008microbiallifeat pages 10-11): Aharon Oren. Microbial life at high salt concentrations: phylogenetic and metabolic diversity. Saline Systems, 4:2-2, Apr 2008. URL: https://doi.org/10.1186/1746-1448-4-2, doi:10.1186/1746-1448-4-2. This article has 1323 citations.

3. (bremer2019responsesofmicroorganisms pages 3-5): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

4. (yu2024temporaldynamicsof pages 1-2): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 28 citations and is from a peer-reviewed journal.

5. (yu2024temporaldynamicsof pages 13-14): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 28 citations and is from a peer-reviewed journal.

6. (yu2024temporaldynamicsof pages 2-5): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 28 citations and is from a peer-reviewed journal.

7. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

8. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

9. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

10. (cheng(程彬)2016alkalineresponseof pages 1-2): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

11. (cheng(程彬)2016alkalineresponseof pages 8-9): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

12. (cheng(程彬)2016alkalineresponseof pages 18-21): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

13. (cheng(程彬)2016alkalineresponseof pages 4-5): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

14. (cheng(程彬)2016alkalineresponseof pages 17-18): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

15. (cheng(程彬)2016alkalineresponseof pages 6-8): Bin Cheng(程彬), Yiwei Meng(孟艺伟), Yanbing Cui(崔延冰), Chunfang Li(李春芳), Fei Tao(陶飞), Huijia Yin(殷会佳), Chunyu Yang(杨春玉), and Ping Xu(许平). Alkaline response of a halotolerant alkaliphilic halomonas strain and functional diversity of its na+(k+)/h+ antiporters. Journal of Biological Chemistry, 291:26056-26065, Dec 2016. URL: https://doi.org/10.1074/jbc.m116.751016, doi:10.1074/jbc.m116.751016. This article has 58 citations and is from a domain leading peer-reviewed journal.

16. (yu2024temporaldynamicsof pages 14-16): Junxiong Yu, Yue Zhang, Hao Liu, Yuxuan Liu, Ali Mohsin, Zebo Liu, Yanning Zheng, Jianmin Xing, Jing Han, Yingping Zhuang, Meijin Guo, and Zejian Wang. Temporal dynamics of stress response in halomonas elongata to nacl shock: physiological, metabolomic, and transcriptomic insights. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02358-5, doi:10.1186/s12934-024-02358-5. This article has 28 citations and is from a peer-reviewed journal.