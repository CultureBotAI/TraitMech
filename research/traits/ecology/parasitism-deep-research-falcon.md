---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:32:19.586688'
end_time: '2026-08-03T23:42:17.342793'
duration_seconds: 597.76
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: parasitism
  trait_identifier: traitmech:000043
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: parasitism
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A symbiosis in which the microorganism benefits at the expense of its
    host's fitness, deriving resources from the host while causing it harm.
  parent_traits: traitmech:000040
  synonyms: parasitic
  evidence_summary: 'DOI:10.1038/s41579-021-00550-7:  (Drew et al. define parasitism
    as the harmful pole of the parasite-mutualist continuum and describe evolutionary
    transitions along it.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support
    host-exploitative associations as one outcome of the shared host-colonization
    toolkit.)'
  causal_graph_summary: 'parasitism_host_fitness_cost: 12 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** parasitism
- **METPO identifier:** traitmech:000043
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits at the expense of its host's fitness, deriving resources from the host while causing it harm.
- **Parent traits:** traitmech:000040
- **Synonyms:** parasitic
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. define parasitism as the harmful pole of the parasite-mutualist continuum and describe evolutionary transitions along it.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support host-exploitative associations as one outcome of the shared host-colonization toolkit.)
- **Existing causal graph summary:** parasitism_host_fitness_cost: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **parasitism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/parasitism.yaml`.

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
- **Trait label:** parasitism
- **METPO identifier:** traitmech:000043
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism benefits at the expense of its host's fitness, deriving resources from the host while causing it harm.
- **Parent traits:** traitmech:000040
- **Synonyms:** parasitic
- **Existing evidence:** DOI:10.1038/s41579-021-00550-7:  (Drew et al. define parasitism as the harmful pole of the parasite-mutualist continuum and describe evolutionary transitions along it.) | DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. support host-exploitative associations as one outcome of the shared host-colonization toolkit.)
- **Existing causal graph summary:** parasitism_host_fitness_cost: 12 nodes, 11 edges

## Research Objective

Research the microbial trait **parasitism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/parasitism.yaml`.

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


# TraitMech curation report: microbial parasitism

## Executive curation recommendation

**Target:** parasitism (`traitmech:000043`; ECOLOGY; CLASS; REVIEWED).

The trait should represent an **ecological interaction outcome**, not a single virulence pathway: the microorganism obtains resources or reproductive benefit from a host while causing a net reduction in host fitness. The most defensible cross-taxon graph is therefore a small backbone—host association/colonization → host-resource access → microbial maintenance or reproduction, together with host damage or resource diversion → reduced host survival/reproduction—supplemented by explicitly taxon-specific mechanistic modules.

The literature treats host–microbe effects as a continuum rather than immutable categories. Pathobionts, for example, can move between harmless and harmful states depending on host immunity and microbiota composition; temperature, transmission route, and community context can also change the interaction outcome. Host-cell lysis and resource theft leading to castration are clear parasitic endpoints. Thus, a mechanism should not be sufficient by itself to assign this trait unless host-fitness harm is demonstrated or strongly established for the association. (drew2021microbialevolutionand pages 11-12)

## 1. Scope and boundaries

### Inclusion criterion

Curate `traitmech:000043` when evidence supports both:

1. **Microbial benefit:** resource acquisition, energy acquisition, persistence, growth, reproduction, or transmission derived from the host; and
2. **Host cost:** reduced survival, fecundity, growth, physiological performance, or another defensible component of host fitness.

Obligate intracellular bacterial parasites are a strong mechanistic subset: they require invasion of a eukaryotic cell to reproduce, occupy cytosolic or vacuolar niches, commonly show genome reduction, and scavenge costly metabolites rather than synthesizing them de novo. These properties explain dependence and exploitation, but host dependence alone still does not establish the ecological fitness cost. (mandel2024metabolismandphysiology pages 1-2)

### Nearby traits that should remain distinct

- **Mutualism:** both partners have a net fitness benefit under the measured conditions.
- **Commensalism:** the microbe benefits while no significant host-fitness effect is detected.
- **Pathogenicity/virulence:** capacities to cause disease or damage. These are frequent mechanisms or manifestations of parasitism, but disease is neither required nor by itself proof of an evolutionary fitness cost.
- **Pathobiont:** a context-dependent state, not a constitutively parasitic class. The same organism may be commensal under one immune/community environment and harmful under another. (drew2021microbialevolutionand pages 11-12)
- **Obligate host dependence:** inability to reproduce without a host. This supports parasitic resource dependence but does not distinguish a harmful parasite from an obligate mutualist.
- **Predation:** normally involves killing and consuming multiple prey individuals rather than sustained exploitation of a host association. Lytic phages are a boundary case; include only if TraitMech’s operational scope treats viral infection as microbial parasitism.
- **Parasitoidism/parasitic castration:** host reproduction is eliminated and resources are redirected to the exploiter. This is an extreme, readily measurable parasitic fitness cost; *Pasteuria*–*Daphnia* is a microbial example. (drew2021microbialevolutionand pages 11-12)

### Assay recommendation

A trait assertion should record: host taxon, microbial strain, infection stage, environment, comparator, microbial benefit endpoint, and host-fitness endpoint. Suitable host endpoints include survival, lifetime fecundity, offspring number, growth, or competitive performance. Cell death, cytokine induction, metabolite depletion, or clinical symptoms are useful intermediate nodes but should not automatically be equated with organismal fitness.

## 2. Candidate nodes grouped by type

### Trait and outcome nodes

- parasitism — `traitmech:000043`
- host-derived resource acquisition — label-only
- microbial intracellular growth/replication — label-only pending GO review
- microbial transmission — label-only
- host cellular damage; host-cell lysis — label-only
- host metabolic dysbiosis — label-only
- reduced host survival; reduced host reproduction; host castration; host fitness cost — label-only
- parasite–mutualist continuum; context-dependent pathobiont state — label-only

### Organisms and cellular niches

Candidate taxon nodes, requiring NCBITaxon lookup during YAML implementation: *Chlamydia trachomatis*, *C. muridarum*, *Coxiella burnetii*, *Rickettsia prowazekii*, *Neisseria gonorrhoeae*, *Staphylococcus aureus*, *Plasmodium* spp., *Toxoplasma gondii*, *Cryptosporidium* spp., *Trypanosoma brucei*, *T. cruzi*, and *Leishmania donovani*.

Compartments include the chlamydial inclusion/inclusion membrane, acidic Coxiella-containing vacuole (CCV), host cytosol, lysosome-derived compartment, erythrocyte, hepatocyte, intestinal epithelial cell, Golgi, endoplasmic reticulum, multivesicular body, mitochondrion, and apicoplast. Leave these label-only until exact GO or host-cell ontology terms are verified.

### Genes, proteins, and complexes

- Chlamydial inclusion effectors: IncA, IncD, IncE/CT116, IncF, IncG, CT229, CT442, CT449, CT622/TaiP, CT813/InaC, Cpn0585.
- Host trafficking machinery: Rab1, Rab4, Rab6, Rab10, Rab11, Rab14, Rab35, Rab39; ARF1/ARF4; GBF1; CERT; FIP2; RUFY1; BICD1; SNAP-23; syntaxins 4/10; VAMP3/4.
- Energy and metabolic functions: ATP/ADP translocase/Npt1; GpsA; hexokinase II; p53; HIF1α; YtgR; FeoAB.
- Coxiella virulence machinery: Dot/Icm type IVB secretion system and its effectors; eIF2α/UPR host targets.
- Host-adaptation factors: InlA, TbpA, TdfH, IsdB, bacterial toxins and leukocidins.
- Protozoan metabolic enzymes: acyl-CoA acyltransferases, diacylglycerol acyltransferases, ribulose-5-phosphate isomerase.

These should remain label-only unless organism-specific UniProt accessions and exact gene products are checked. Gene symbols such as Rab11 or p53 must be host-species qualified.

### Chemicals and nutrients

Conservative candidate grounding:

- ATP — `CHEBI:15422`
- ADP — `CHEBI:16761`
- cholesterol — `CHEBI:16113`
- sphingomyelin — `CHEBI:64583`
- ceramide — `CHEBI:17761`
- iron atom — `CHEBI:18248`; ferrous iron — `CHEBI:29033`
- acetyl-CoA — `CHEBI:15351`
- glutamine — `CHEBI:18050`
- glycolysis — `GO:0006096`

Additional label-only candidates pending identifier verification include GTP/NTPs, glucose, glucose-6-phosphate, DHAP, glycerol-3-phosphate, amino acids, tryptophan, purines, transferrin, hemoglobin/heme, calprotectin-bound zinc, cholesterol esters, lactate, succinate, and indolepyruvate.

### Environmental and experimental factors

- acidic intravacuolar pH;
- iron, tryptophan, glutamine, glucose, or lipid availability;
- host immune status and microbiota composition;
- temperature;
- cytosolic versus vacuolar replication niche;
- gene knockout/knockdown, transporter inhibition, glycolysis inhibition, and nutrient supplementation.

Drew and colleagues identify temperature, community composition, transmission route, and environmental constraints as factors capable of moving interactions along the parasite–mutualist continuum. (drew2021microbialevolutionand pages 11-12)

## 3. Candidate causal edges

The following table is deliberately modular: only its first edge is a general trait-level outcome. Molecular edges are exemplars for named taxa and should not be asserted universally.

| subject | predicate | object | proposed grounding | taxon/context | evidence snippet | DOI/date | confidence/curation note |
|---|---|---|---|---|---|---|---|
| microbial parasitism | causes | host fitness cost | METPO: traitmech:000043; host fitness cost [label-only] | General ecological scope | “parasitism as the harmful pole of the parasite–mutualist continuum” and examples include host cell lysis and host castration/resource theft (drew2021microbialevolutionand pages 11-12) | 10.1038/s41579-021-00550-7; 2021-04 | **High for trait scope**, but mechanistically broad; curate as backbone ecological outcome, not as a taxon-specific molecular edge. |
| host-associated microbe | can transition along | parasite–mutualist continuum | parasite–mutualist continuum [label-only] | General symbiosis theory | “microbial symbionts can evolve rapidly, resulting in drastic transitions along the parasite–mutualist continuum” (drew2021microbialevolutionand pages 11-12) | 10.1038/s41579-021-00550-7; 2021-04 | **High for concept**, not a molecular mechanism; useful as warning/boundary edge. |
| Chlamydia spp. inclusion membrane effectors (Inc proteins) | recruit | Rab GTPases to inclusion membrane | Rab GTPase [label-only]; inclusion membrane [label-only] | Chlamydia intracellular parasitism | “recruits Rab GTPases and their effector proteins to the inclusion membrane to manipulate host cell vesicular trafficking” (wenbo2024hijackinghostcell pages 1-2) | 10.1080/21505594.2024.2351234; 2024-05 | **Moderate-high**; review-level synthesis but mechanistically central and repeatedly supported. |
| Rab GTPase recruitment to chlamydial inclusion | promotes acquisition of | sphingomyelin/cholesterol/iron | CHEBI:64583 sphingomyelin; CHEBI:16113 cholesterol; CHEBI:18248 iron atom | Chlamydia inclusion development | Hijacking vesicular transport enables acquisition of “sphingomyelin, cholesterol, iron… essential for inclusion development and bacterial growth” (wenbo2024hijackinghostcell pages 1-2) | 10.1080/21505594.2024.2351234; 2024-05 | **Moderate**; review-level but directly tied to nutrient acquisition and growth. |
| CERT co-option by Chlamydia | increases | ceramide delivery for sphingomyelin biosynthesis | CERT [label-only]; CHEBI:17761 ceramide; CHEBI:64583 sphingomyelin | Chlamydia, ER-to-Golgi/non-vesicular lipid transport | “CERT-mediated non-vesicular transport of ceramide… for sphingomyelin biosynthesis, with CERT depletion reducing infectious progeny” (wenbo2024hijackinghostcell pages 3-4) | 10.1080/21505594.2024.2351234; 2024-05 | **High** for Chlamydia-specific edge; includes intervention phenotype (depletion reduces progeny). |
| Rab6/Rab11/Rab14 function | positively regulates | chlamydial progeny production | Rab6 [label-only]; Rab11 [label-only]; Rab14 [label-only] | Chlamydia developmental cycle | “knockdown of Rab6, Rab11, or Rab14 reduces progeny production” (wenbo2024hijackinghostcell pages 6-8) | 10.1080/21505594.2024.2351234; 2024-05 | **High**; strongest experimentally anchored Chlamydia edge in this set. |
| Rab4/Rab11/Rab35 recruitment | redirects transport of | transferrin and mannose-6-phosphate receptor to inclusion-associated pathways | transferrin [label-only]; mannose-6-phosphate receptor [label-only] | Chlamydia nutrient acquisition | “Rab4, Rab11, and Rab35… control transport of transferrin and mannose-6-phosphate receptor (M6PR), both essential for chlamydial development” (wenbo2024hijackinghostcell pages 9-11) | 10.1080/21505594.2024.2351234; 2024-05 | **Moderate**; mechanistic and specific, but cited here through review summary. |
| Chlamydia trachomatis | scavenges | host ATP / NTPs | ATP [CHEBI:15422]; NTPs [label-only] | Obligate intracellular bacterial parasitism | “C. trachomatis is described as an energy parasite scavenging ATP and NTPs from host cells” (mandel2024metabolismandphysiology pages 5-6) | 10.3389/fcimb.2024.1284701; 2024-03 | **Moderate-high**; central metabolic parasitism edge, though framed in review language. |
| ATP/ADP translocases | enable | host ATP scavenging (“energy parasitism”) | ATP/ADP translocase [label-only]; ATP [CHEBI:15422]; ADP [CHEBI:16761] | Chlamydia and Rickettsia | “Chlamydia and Rickettsia scavenge ATP from hosts via ATP/ADP translocases” (mandel2024metabolismandphysiology pages 2-4) | 10.3389/fcimb.2024.1284701; 2024-03 | **Moderate**; broad but highly relevant backbone mechanism for intracellular parasitism. |
| Chlamydia trachomatis | downregulates | host p53 | p53 [label-only] | Chlamydia host metabolic reprogramming | “Chlamydia downregulates host p53 to enhance pentose phosphate pathway activity and glucose-6P/ATP production” (mandel2024metabolismandphysiology pages 8-9) | 10.3389/fcimb.2024.1284701; 2024-03 | **Moderate**; promising mechanistic edge, but curate with note that causality is summarized from prior studies. |
| host hexokinase II upregulation by C. muridarum | increases | host glucose metabolism supporting infection | hexokinase II [label-only]; glucose metabolism [label-only] | Chlamydia muridarum | “C. muridarum upregulates host hexokinase II for glucose metabolism” (mandel2024metabolismandphysiology pages 8-9) | 10.3389/fcimb.2024.1284701; 2024-03 | **Moderate**; species-specific and host-metabolism edge rather than general parasitism backbone. |
| Coxiella burnetii FeoAB transporter | acquires | Fe2+ from acidic CCV | FeoAB [label-only]; CHEBI:29033 Fe2+; CCV [label-only] | C. burnetii in acidic Coxiella-containing vacuole | “acquires iron via the Fe2+-specific FeoAB transporter from the acidic CCV” (mandel2024metabolismandphysiology pages 8-9) | 10.3389/fcimb.2024.1284701; 2024-03 | **High**; concrete transporter-to-nutrient edge suitable for curation. |
| acidic pH of CCV | activates/supports | Coxiella nutrient transport and metabolism | acidic pH [label-only]; CCV [label-only] | C. burnetii intracellular niche | “moderately acidic pH requirement for nutrient transport and metabolic activation” (mandel2024metabolismandphysiology pages 14-15) | 10.3389/fcimb.2024.1284701; 2024-03 | **High**; strong environmental-factor edge for intracellular parasitic niche. |
| Coxiella Dot/Icm type IVB secretion system effectors | regulate | host UPR / eIF2α phosphorylation to promote CCV expansion and replication | Dot/Icm T4BSS [label-only]; UPR [label-only]; eIF2α [label-only] | C. burnetii host manipulation | “Type IVB secretion system effectors regulate unfolded protein response (UPR) signaling and translation initiation factor eIF2α phosphorylation, affecting CCV expansion and replication” (mandel2024metabolismandphysiology pages 9-10) | 10.3389/fcimb.2024.1284701; 2024-03 | **Moderate-high**; strong mechanistic statement but review-synthesized. |
| Rickettsia prowazekii DHAP transport + GpsA | supports | glycerol-3-phosphate / phospholipid biosynthesis | DHAP [label-only]; GpsA [label-only]; glycerol-3-phosphate [label-only] | Rickettsia metabolic parasitism | “imports dihydroxyacetone phosphate (DHAP) which it converts to glycerol-3-phosphate via GpsA for phospholipid biosynthesis” (mandel2024metabolismandphysiology pages 5-6) | 10.3389/fcimb.2024.1284701; 2024-03 | **High**; specific nutrient-import-to-biomass edge suitable for curation. |
| bacterial adhesin–host receptor specificity | restricts | host colonization/tropism | adhesin [label-only]; receptor [label-only] | Cross-taxon bacterial host adaptation | “Adhesins are critical surface proteins that facilitate species-specific colonization through direct interactions with host cell receptors” (barber2024mechanismsofhost pages 3-5) | 10.1093/femsre/fuae019; 2024-07 | **High for general principle**, but broad; good backbone edge linking colonization to parasitic host range. |
| transferrin-binding protein A (TbpA) / TdfH / IsdB specificity | enables | host-specific iron, zinc, or heme acquisition | TbpA [label-only]; TdfH [label-only]; IsdB [label-only]; transferrin [label-only]; calprotectin [label-only]; hemoglobin [label-only] | Neisseria, Haemophilus, Staphylococcus host adaptation | “TbpA… binds rapidly evolving regions of transferrin”; “TdfH receptor selectively binds human calprotectin”; “IsdB receptor binds human hemoglobin more effectively than mouse” (barber2024mechanismsofhost pages 5-6, barber2024mechanismsofhost pages 6-7) | 10.1093/femsre/fuae019; 2024-07 | **High but taxon-specific**; excellent nutrient-acquisition exemplars, avoid overgeneralizing to all parasites. |
| toxins that lyse host cells/RBCs | facilitate | nutrient acquisition and transmission | toxin [label-only]; red blood cell lysis [label-only] | General bacterial pathogenesis/host exploitation | “toxins damage host cells, facilitate nutrient acquisition (particularly by lysing red blood cells…)” (barber2024mechanismsofhost pages 10-11) | 10.1093/femsre/fuae019; 2024-07 | **Moderate-high**; useful host-damage-to-resource edge, but mostly pathogenic-bacteria literature rather than broad symbiosis. |
| Cryptosporidium-induced increase in host glucose uptake | promotes | intracellular replication | glucose uptake [label-only] | Cryptosporidium in intestinal epithelial cells | “Cryptosporidium increases host glucose uptake and lactate release, with glycolysis inhibition reducing intracellular replication” (ewald2024theintersectionof pages 19-21) | 10.1128/mmbr.00164-22; 2024-03 | **High**; strong host-metabolism-to-parasite-growth edge with intervention support. |
| Toxoplasma gondii acyl-CoA acyltransferases / diacylglycerol acyltransferases | scavenge | host acetyl-CoA and cholesterol esters | acyl-CoA acyltransferase [label-only]; diacylglycerol acyltransferase [label-only]; acetyl-CoA [CHEBI:15351]; cholesterol ester [label-only] | T. gondii intracellular parasitism | “Toxoplasma uses specific acyl-CoA acyltransferases and diacylglycerol acyltransferases to scavenge acetyl-CoA and cholesterol esters from hosts” (ewald2024theintersectionof pages 19-21) | 10.1128/mmbr.00164-22; 2024-03 | **Moderate-high**; good eukaryotic parasite nutrient-scavenging exemplar, though enzyme IDs not grounded here. |
| Plasmodium dependence on host glycolysis / glutamine acquisition | supports | asexual replication and liver-stage growth | glycolysis [GO:0006096]; glutamine [CHEBI:18050] | Plasmodium spp. in erythrocytes/liver stages | “Plasmodium depends on host glycolysis for asexual replication” and “cationic amino acid uptake [is] critical for liver stage parasites”; low plasma glutamine associates with severe malaria (ewald2024theintersectionof pages 19-21, ewald2024theintersectionof pages 7-9) | 10.1128/mmbr.00164-22; 2024-03 | **Moderate**; partially mixed across life stages and taxa, so curate carefully with context note. |


*Table: This table compiles strong candidate causal edges for curating the microbial trait parasitism, emphasizing host exploitation, nutrient acquisition, trafficking manipulation, and host-damaging processes. It distinguishes broad backbone edges from taxon-specific mechanisms and notes where support is direct versus review-synthesized.*

### Recommended minimal YAML backbone

1. `host association` **enables** `access to host-derived resources`.
2. `host-derived resource acquisition` **promotes** `microbial maintenance or reproduction`.
3. `microbial effector activity / resource diversion / host-cell lysis` **causes** `host physiological damage or resource loss`.
4. `host physiological damage or resource loss` **reduces** `host survival or reproduction`.
5. `microbial reproduction or transmission` **benefits** `microorganism`.
6. Joint presence of microbial benefit and host-fitness cost **realizes** `parasitism (traitmech:000043)`.

Edges 1–5 are conceptual abstractions. Their molecular realizations should be separate, taxon-qualified subgraphs.

## 4. Recent developments and quantitative evidence

### Intracellular bacterial metabolism

A 2024 synthesis emphasizes that the historical label “energy parasite” is too simple. *Chlamydia* and *Rickettsia* scavenge host ATP through ATP/ADP translocases, but chlamydial replication forms can also generate ATP; *Coxiella* does not follow the same energy-parasitism model. Replication niche predicts retained metabolism: vacuolar organisms face stronger pressure to retain amino-acid synthesis than cytosolic organisms. (mandel2024metabolismandphysiology pages 5-6, mandel2024metabolismandphysiology pages 2-4)

The same review reports unusually limited transcriptional responses to iron limitation: only **12 genes** changed in *C. trachomatis*, while **5 genes at ≥3-fold** changed in *R. rickettsii*. These are useful descriptive statistics but should not become causal graph edges without the primary perturbation studies. (mandel2024metabolismandphysiology pages 8-9)

### Host-trafficking hijacking by Chlamydia

The 2024 trafficking review connects inclusion effectors to Rab, ARF, SNARE, retromer, and CERT pathways. Particularly strong intervention evidence is that depletion of CERT reduces infectious progeny, knockdown of Rab6/Rab11/Rab14 reduces progeny production, and inhibition of ceramide transport decreases offspring. These provide experimentally anchored links from host trafficking to nutrient delivery and microbial reproduction. (wenbo2024hijackinghostcell pages 3-4, wenbo2024hijackinghostcell pages 6-8)

### Host specificity as a mechanistic gate

Recent expert synthesis argues that host adaptation is often controlled by molecular compatibility rather than generic “virulence.” InlA–E-cadherin compatibility, TbpA–transferrin, TdfH–calprotectin, and IsdB–hemoglobin interactions determine colonization or nutrient access in a host-specific manner. In one striking experimental example, supplying human plasminogen enhanced *S. pyogenes* virulence in mice. A single amino-acid difference in the relevant host receptor can alter susceptibility, and one mutation in *S. aureus dltB* has been associated with rabbit adaptation. (barber2024mechanismsofhost pages 5-6, barber2024mechanismsofhost pages 3-5, barber2024mechanismsofhost pages 2-3)

### Protozoan immunometabolism

The 2024 MMBR review identifies common host exploitation despite deep phylogenetic differences. *Cryptosporidium* increases host glucose uptake and lactate release, while glycolysis inhibition reduces intracellular replication. *Plasmodium* depends on host glycolysis during erythrocytic replication and depletes circulating amino acids; low plasma glutamine is associated with severe malaria. *T. brucei* secretes indolepyruvate, suppressing inflammatory cytokines and immune-cell glycolysis. (ewald2024theintersectionof pages 19-21, ewald2024theintersectionof pages 7-9)

These data support a causal-graph design in which nutrient acquisition, immune modulation, and host harm are connected but not collapsed into one node. Metabolic changes may benefit the parasite, defend the host, or be collateral pathology depending on tissue and infection stage. (ewald2024theintersectionof pages 2-4)

## 5. Applications and real-world implementation

1. **Host-directed anti-infective discovery:** CERT, Rab-dependent trafficking, host glycolysis, and metabolite availability are intervention points that can reduce intracellular replication without directly targeting a microbial enzyme. This may reduce conventional resistance selection, although toxicity to the host pathway is a major constraint. (wenbo2024hijackinghostcell pages 3-4, wenbo2024hijackinghostcell pages 6-8, ewald2024theintersectionof pages 19-21)
2. **Nutritional immunity and nutrient supplementation:** FeoAB-mediated ferrous-iron uptake, transferrin/calprotectin piracy, and glutamine or tryptophan dependence can inform nutrient restriction or supplementation strategies. Direction is context-specific: nutrient restriction may starve parasites but also weaken protective immunity. (mandel2024metabolismandphysiology pages 8-9, barber2024mechanismsofhost pages 5-6, ewald2024theintersectionof pages 7-9)
3. **Host-range and spillover prediction:** adhesin–receptor and nutrient-receptor compatibility can improve mechanistic risk assessment for host jumps. Sequence similarity alone is insufficient; the relevant binding phenotype should be tested. (barber2024mechanismsofhost pages 6-7, barber2024mechanismsofhost pages 3-5)
4. **Diagnostic and assay design:** graph nodes suggest measurable biomarkers—circulating amino-acid depletion, lactate release, iron-response signatures, inclusion trafficking, infectious progeny, and host survival/fecundity—but biomarker association must remain distinct from causation.
5. **Evolution-informed microbiome management:** because parasitism is context dependent, interventions that change community composition, immunity, transmission, or temperature can move an interaction along the parasite–mutualist continuum rather than simply eliminate a fixed phenotype. (drew2021microbialevolutionand pages 11-12)

## 6. Warnings: claims not yet ready for TraitMech

- **Do not curate “pathogen → parasitism” as an unconditional edge.** Pathogenicity is a capacity; parasitism is the net ecological relationship under specified conditions.
- **Do not infer host-fitness cost from intracellular replication alone.** Obligate intracellular dependence and genome reduction establish dependence, not necessarily harm. (mandel2024metabolismandphysiology pages 1-2)
- **Do not generalize Chlamydia, Coxiella, or Rickettsia mechanisms to all microbial parasites.** Even these three bacterial groups differ in ATP use, carbon metabolism, vacuolar pH, and biosynthetic retention. (mandel2024metabolismandphysiology pages 5-6, mandel2024metabolismandphysiology pages 2-4)
- **Do not collapse pathogen fitness and host fitness.** “Fitness cost” in antimicrobial-resistance literature often refers to the parasite’s own competitive fitness, not damage to the host.
- **Do not use review-level summary as if it were a primary perturbation result.** The Rab/CERT knockdowns and glycolysis inhibition are strong candidates, but primary papers should be retrieved before production curation.
- **Do not curate associations as causal edges:** low glutamine associated with severe malaria, metabolite enrichment during infection, or a gene under positive selection are not by themselves causal.
- **Qualify host genes by species.** Rab proteins, p53, eIF2α, receptors, transferrin, and hemoglobin are host products; unqualified identifiers could incorrectly imply microbial proteins.
- **Resolve identifier inconsistencies before YAML insertion.** Exact ChEBI records, UniProt accessions, GO compartments, NCBITaxon IDs, and Rhea reactions should be verified against current ontology releases. Label-only nodes are safer than guessed CURIEs.
- **Treat temperature/community effects as modifiers, not universal causes.** Their effects can reverse according to the symbiosis and host context. (drew2021microbialevolutionand pages 11-12)
- **Direct evidence tying molecular exploitation to organismal host fitness remains sparse.** Most 2024 mechanisms terminate at intracellular growth, pathogen burden, or disease metabolism rather than lifetime survival/fecundity. The existing `parasitism_host_fitness_cost` graph should therefore preserve a distinct, evidence-gated bridge from molecular damage to organismal fitness.

## 7. DOI-first bibliography

1. **Mandel CG, Sanchez SE, Monahan CC, Phuklia W, Omsland A.** “Metabolism and physiology of pathogenic bacterial obligate intracellular parasites.” *Frontiers in Cellular and Infection Microbiology* 14. **March 2024.** DOI: [10.3389/fcimb.2024.1284701](https://doi.org/10.3389/fcimb.2024.1284701). (mandel2024metabolismandphysiology pages 1-2)
2. **Ewald S, Nasuhidehnavi A, Feng T-Y, Lesani M, McCall L-I.** “The intersection of host in vivo metabolism and immune responses to infection with kinetoplastid and apicomplexan parasites.” *Microbiology and Molecular Biology Reviews* 88(1). **March 2024.** DOI: [10.1128/mmbr.00164-22](https://doi.org/10.1128/mmbr.00164-22). (ewald2024theintersectionof pages 19-21)
3. **Lei W, Yang Y, Zhou H, Li Z.** “Hijacking host cell vesicular transport: New insights into the nutrient acquisition mechanism of Chlamydia.” *Virulence* 15(1). **May 2024.** DOI: [10.1080/21505594.2024.2351234](https://doi.org/10.1080/21505594.2024.2351234). (wenbo2024hijackinghostcell pages 1-2)
4. **Barber MF, Fitzgerald JR.** “Mechanisms of host adaptation by bacterial pathogens.” *FEMS Microbiology Reviews* 48(4). **July 2024.** DOI: [10.1093/femsre/fuae019](https://doi.org/10.1093/femsre/fuae019). (barber2024mechanismsofhost pages 10-11)
5. **Drew GC, Stevens EJ, King KC.** “Microbial evolution and transitions along the parasite–mutualist continuum.” *Nature Reviews Microbiology* 19:623–638. **April 2021.** DOI: [10.1038/s41579-021-00550-7](https://doi.org/10.1038/s41579-021-00550-7). (drew2021microbialevolutionand pages 11-12)

## Bottom line for `parasitism.yaml`

The safest first revision is to retain the existing host-fitness-cost backbone and add **taxon-qualified modules** for: (i) adhesin/receptor-enabled colonization, (ii) host ATP and nutrient scavenging, (iii) vesicular-traffic hijacking, (iv) secretion-system-mediated niche construction, (v) toxin/lysis-mediated resource release, and (vi) metabolic or immune manipulation. Require every module to connect independently to microbial benefit and, through separately supported evidence, to host-fitness loss. This avoids encoding “parasitism” as a synonym for intracellular lifestyle, virulence, or disease.

References

1. (drew2021microbialevolutionand pages 11-12): Georgia C. Drew, Emily J. Stevens, and Kayla C. King. Microbial evolution and transitions along the parasite–mutualist continuum. Nature Reviews. Microbiology, 19:623-638, Apr 2021. URL: https://doi.org/10.1038/s41579-021-00550-7, doi:10.1038/s41579-021-00550-7. This article has 405 citations.

2. (mandel2024metabolismandphysiology pages 1-2): Cameron G. Mandel, Savannah E. Sanchez, Colleen C. Monahan, Weerawat Phuklia, and Anders Omsland. Metabolism and physiology of pathogenic bacterial obligate intracellular parasites. Frontiers in Cellular and Infection Microbiology, Mar 2024. URL: https://doi.org/10.3389/fcimb.2024.1284701, doi:10.3389/fcimb.2024.1284701. This article has 9 citations.

3. (wenbo2024hijackinghostcell pages 1-2): Lei Wenbo, Yang Yewei, Zhou Hui, and Li Zhongyu. Hijacking host cell vesicular transport: new insights into the nutrient acquisition mechanism of chlamydia. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2351234, doi:10.1080/21505594.2024.2351234. This article has 10 citations and is from a peer-reviewed journal.

4. (wenbo2024hijackinghostcell pages 3-4): Lei Wenbo, Yang Yewei, Zhou Hui, and Li Zhongyu. Hijacking host cell vesicular transport: new insights into the nutrient acquisition mechanism of chlamydia. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2351234, doi:10.1080/21505594.2024.2351234. This article has 10 citations and is from a peer-reviewed journal.

5. (wenbo2024hijackinghostcell pages 6-8): Lei Wenbo, Yang Yewei, Zhou Hui, and Li Zhongyu. Hijacking host cell vesicular transport: new insights into the nutrient acquisition mechanism of chlamydia. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2351234, doi:10.1080/21505594.2024.2351234. This article has 10 citations and is from a peer-reviewed journal.

6. (wenbo2024hijackinghostcell pages 9-11): Lei Wenbo, Yang Yewei, Zhou Hui, and Li Zhongyu. Hijacking host cell vesicular transport: new insights into the nutrient acquisition mechanism of chlamydia. Virulence, May 2024. URL: https://doi.org/10.1080/21505594.2024.2351234, doi:10.1080/21505594.2024.2351234. This article has 10 citations and is from a peer-reviewed journal.

7. (mandel2024metabolismandphysiology pages 5-6): Cameron G. Mandel, Savannah E. Sanchez, Colleen C. Monahan, Weerawat Phuklia, and Anders Omsland. Metabolism and physiology of pathogenic bacterial obligate intracellular parasites. Frontiers in Cellular and Infection Microbiology, Mar 2024. URL: https://doi.org/10.3389/fcimb.2024.1284701, doi:10.3389/fcimb.2024.1284701. This article has 9 citations.

8. (mandel2024metabolismandphysiology pages 2-4): Cameron G. Mandel, Savannah E. Sanchez, Colleen C. Monahan, Weerawat Phuklia, and Anders Omsland. Metabolism and physiology of pathogenic bacterial obligate intracellular parasites. Frontiers in Cellular and Infection Microbiology, Mar 2024. URL: https://doi.org/10.3389/fcimb.2024.1284701, doi:10.3389/fcimb.2024.1284701. This article has 9 citations.

9. (mandel2024metabolismandphysiology pages 8-9): Cameron G. Mandel, Savannah E. Sanchez, Colleen C. Monahan, Weerawat Phuklia, and Anders Omsland. Metabolism and physiology of pathogenic bacterial obligate intracellular parasites. Frontiers in Cellular and Infection Microbiology, Mar 2024. URL: https://doi.org/10.3389/fcimb.2024.1284701, doi:10.3389/fcimb.2024.1284701. This article has 9 citations.

10. (mandel2024metabolismandphysiology pages 14-15): Cameron G. Mandel, Savannah E. Sanchez, Colleen C. Monahan, Weerawat Phuklia, and Anders Omsland. Metabolism and physiology of pathogenic bacterial obligate intracellular parasites. Frontiers in Cellular and Infection Microbiology, Mar 2024. URL: https://doi.org/10.3389/fcimb.2024.1284701, doi:10.3389/fcimb.2024.1284701. This article has 9 citations.

11. (mandel2024metabolismandphysiology pages 9-10): Cameron G. Mandel, Savannah E. Sanchez, Colleen C. Monahan, Weerawat Phuklia, and Anders Omsland. Metabolism and physiology of pathogenic bacterial obligate intracellular parasites. Frontiers in Cellular and Infection Microbiology, Mar 2024. URL: https://doi.org/10.3389/fcimb.2024.1284701, doi:10.3389/fcimb.2024.1284701. This article has 9 citations.

12. (barber2024mechanismsofhost pages 3-5): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

13. (barber2024mechanismsofhost pages 5-6): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

14. (barber2024mechanismsofhost pages 6-7): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

15. (barber2024mechanismsofhost pages 10-11): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

16. (ewald2024theintersectionof pages 19-21): Sarah Ewald, Azadeh Nasuhidehnavi, Tzu-Yu Feng, Mahbobeh Lesani, and Laura-Isobel McCall. The intersection of host <i>in vivo</i> metabolism and immune responses to infection with kinetoplastid and apicomplexan parasites. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00164-22, doi:10.1128/mmbr.00164-22. This article has 16 citations and is from a domain leading peer-reviewed journal.

17. (ewald2024theintersectionof pages 7-9): Sarah Ewald, Azadeh Nasuhidehnavi, Tzu-Yu Feng, Mahbobeh Lesani, and Laura-Isobel McCall. The intersection of host <i>in vivo</i> metabolism and immune responses to infection with kinetoplastid and apicomplexan parasites. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00164-22, doi:10.1128/mmbr.00164-22. This article has 16 citations and is from a domain leading peer-reviewed journal.

18. (barber2024mechanismsofhost pages 2-3): Matthew F Barber and J Ross Fitzgerald. Mechanisms of host adaptation by bacterial pathogens. FEMS Microbiology Reviews, Jul 2024. URL: https://doi.org/10.1093/femsre/fuae019, doi:10.1093/femsre/fuae019. This article has 53 citations and is from a domain leading peer-reviewed journal.

19. (ewald2024theintersectionof pages 2-4): Sarah Ewald, Azadeh Nasuhidehnavi, Tzu-Yu Feng, Mahbobeh Lesani, and Laura-Isobel McCall. The intersection of host <i>in vivo</i> metabolism and immune responses to infection with kinetoplastid and apicomplexan parasites. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00164-22, doi:10.1128/mmbr.00164-22. This article has 16 citations and is from a domain leading peer-reviewed journal.