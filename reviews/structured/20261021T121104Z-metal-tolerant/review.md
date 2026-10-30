# Whole-record review of metal tolerant

- Review: 20261021T121104Z-metal-tolerant
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T11:59:23.706771Z
- Finished UTC: 2026-10-21T12:11:04Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The retained local identity, broad definition, canonical CH34 example and current relation roles are supported. One major finding concerns a zinc-specific prevalence statement generalized to heavy metals. Three minor findings concern quoted-note context, an ion-versus-condition wording ambiguity and bounded human-acceptance attribution. All nine nodes, eight edges and fourteen citation placements are covered. Both snippet fields are literal; the three quoted notes comprise two literal but context-sensitive substrings and one supported paraphrase. GO0030001 remains a valid broad transport grounding with a precision limitation only.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: First record in the seventh path-ordered batch. One entire maintained environmental TraitRecord and its parent context were read. All 59 captured inputs, nine nodes, eight edges, two components, three label-only protein classes, one canonical example, five assigned works, fourteen citation placements, two snippets, three quoted notes and nine explicit AI events are accounted for. The historical provider report supplies a lead and limited provenance context only; no complete report read is claimed. Existing general environmental claims receive bounded review; incidental pathogen-specific and engineering fitness details remain UNASSESSED_SCOPE. No new mechanism, target, experiment or optimization is supplied.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000012 | data/traits/environment/metal_tolerant.yaml | maintained | metal tolerant |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000012 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000012 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000012 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000012 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | traitmech:000012 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000012 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000012 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native record validation | passed | True | traitmech:000012 | Actual execution at 11:59:58–11:59:59 UTC passed. Structural validation is separate from scientific support. |
| Focused strict validation | passed | True | traitmech:000012 | Actual execution at 11:59:58–11:59:59 UTC passed. Native acceptance does not certify source scope or ontology precision. |
| Focused native snippet verification | passed | True | traitmech:000012 | Actual execution at 12:00:01–12:00:05 UTC passed: two snippets, one VERIFIED and one NOT_IN_ABSTRACT. Manual full-body inspection confirms the second. No initial DNS failure occurred for this record. |
| Reused corpus protein/taxon audit | passed | True | traitmech:000012 | Original batch-four execution at 08:55:04–08:55:10 UTC passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC, one protected and no gaps or errors. The unchanged corpus supports reuse, not a fresh focused scientific check. |
| Reused batch-six maintained QC | passed | True | traitmech:000012 | Original just qc passed at 11:54:49–11:57:53 UTC. The qualified batch-seven byte comparison supports reuse; no new batch-seven QC execution is claimed. |
| Protein instance metadata applicability | not_applicable | False | traitmech:000012 | Three contextual REVIEWED_LABEL_ONLY protein classes and zero protein instances occur in a NONMECHANISTIC graph. No instance metadata assertion requires a target UniProt audit, and no token accession is required. |

## Scientific And Domain Assessments

### Native checklist: identifier, hierarchy and synonym scope

identity: supported. Targets: traitmech:000012.

Active METPO1007074 overlaps this local concept, but the maintained release disposition explicitly retains traitmech:000012. V5 proposed 1007611 carries its definition, parent and crosswalk. Parent METPO1000059 is supported. Related synonyms are conservative source-backed uses; no forced migration or exact synonym upgrade is warranted.

### Native checklist: complete definition and contextual mechanism emphasis

evidence: supported. Targets: traitmech:000012.

The broad tolerance definition and typical efflux emphasis have positive review support. Typical does not mean exclusive or universally necessary, and no fixed concentration threshold is asserted. Nies abstract-only limits do not prove the unseen body lacks more specific support.

### Native checklist: canonical organism, strain and example note

evidence: supported. Targets: traitmech:000012.

The official species identity matches Cupriavidus metallidurans. The assigned CH34 primary paper supports model status, broad resistance and plasmid-borne determinants; it does not require every determinant to be plasmid-borne. BS1 context remains strain-specific and is not transferred as uniform species behavior.

### Native checklist: all nine node identities and represented facets

grounding: concern. Targets: traitmech:000012.

Node 1 alternates between an ion material, an environmental factor and cytoplasmic excess, leaving its intended referent unclear. GO0030001 is a valid broad transport process and explicitly includes export as a narrow synonym; export specificity remains a limitation only. The other current chemical, protein and trait facets are coherent.

Nodes 0 and 8 are trait classes. Node 1 has the bounded facet ambiguity. Node 3 is biological transport. Nodes 4 and 5 are chemical classes. Nodes 2, 6 and 7 are contextual material protein classes; current module wording does not denote the retired operon node.

### Native checklist: all eight predicate roles

consistency: supported. Targets: traitmech:000012.

The material pump to transport process meets RO2327 executor semantics. Local challenges and both confers assignments fit current endpoint meanings; RDFS subclass direction fits the trait classes. Free-text conversion and mediation do not require IDs or inherit unasserted RO constraints. The edge-7 concern is source attribution, not a formal predicate failure.

Edge 0: contextual challenge. Edge 1: material executor to process. Edges 2 and 5: local conferral. Edges 3 and 4: stated free-text conversion roles. Edge 6: trait subclass. Edge 7: free-text mediation with independently assessed breadth.

### Native checklist: all eight nearest-source assertions

evidence: concern. Targets: traitmech:000012.

Existing generic efflux and environmental background have positive support. Edge 7 expands a zinc-specific named-family prevalence statement to heavy metals in most bacteria. Broad page-53 background and Nies family support do not themselves establish that exact expanded prevalence claim. No other contextual branch is declared universal merely from its generic nodes.

### Native checklist: two snippets and three quoted notes

evidence: concern. Targets: traitmech:000012.

Both snippet fields are literal in inspected source surfaces. Among three quoted notes, one is a meaning-supported paraphrase; two are literal substrings whose context matters. The grouped minor concerns edge-3 quote form and edge-5 cooperation context. Edge-7 zinc scope is the separate material attribution finding, without duplicate severity.

### Native checklist: concentration, substrate and prevalence scope

quantity: concern. Targets: traitmech:000012.

No universal concentration cutoff or new assay is required by this broad record. The material quantified breadth is most bacteria on edge 7, whose nearest statement is zinc-specific. Arsenic oxidation-state labels do not specify universal ionic charge, and contextual cation wording does not redefine the entire metal/metalloid trait.

### Native checklist: five works and fourteen placements

evidence: supported. Targets: traitmech:000012.

All five publication identities resolve. Four bodies are available at stated inspected passage scopes, while Nies is abstract-only. Registry/publisher resolution establishes JMMG despite index noncoverage. Metadata status, access failures and original reuse dates remain bounded; no global notice-absence claim is made.

### Native checklist: protein classes, instances and graph components

completeness: supported. Targets: traitmech:000012.

Three explicitly reviewed label-only protein classes and zero instances are permitted in the NONMECHANISTIC sketch. The current Ars module is explicitly a protein aggregate with gene and operon metadata. Its two components do not require artificial connectors or token accessions; retired accessions and prior trait-object RO assignments are not current defects.

### Native checklist: canonical-only catalog applicability

evidence: not_applicable. Targets: traitmech:000012.

The retained official catalog has no Cupriavidus metallidurans or documented historical-name match. No substitute organism or downstream module query is used. Noncoverage is not negative biological evidence or a required-record defect; runner discovery retains its earlier bounded scope.

### Native checklist: current text ownership and maintained recurrence

ownership: supported. Targets: traitmech:000012.

The current record owns the source-scope, quoted-note and node-1 wording concerns. Bounded searches do not identify an exact generating assignment for those textual defects. Maintained finalizer/proposal retention and existing-value mapping guards explain the supported identity and preserved annotations; no speculative shared-writer repair is required.

### Native checklist: REVIEWED status and local acceptance attribution

provenance: concern. Targets: traitmech:000012.

Nine explicit AI events document proposal, curation and prior corrections. Ignored-inclusive bounded searches do not attribute a human acceptance decision for this current target. Positive maintenance and upstream creator attribution are preserved; remote or private decisions remain unknown.

### Native checklist: required focused checks and scoped historical reuse

schema: supported. Targets: traitmech:000012.

Focused record, strict and snippet checks passed. The manual source assessment resolves the abstract-only snippet miss. Reused B6 QC and earlier common diagnostics retain original times, OLD product failures and successful retry, adapter skips and B3 history scope. No new native corpus execution or scientific mutation is claimed.

## Findings

### zinc-prevalence-scope: A zinc-specific prevalence statement is generalized to heavy metals

major / open / confirmed; issue key: metal-tolerant-zinc-prevalence-scope.

Edge 7 states that the named three transporter families mediate heavy-metal resistance in most bacteria. Its quoted source passage on printed page 55 explicitly concerns zinc. Page 53 supplies positive broad active-efflux context, and Nies supports the family-level background, but neither inspected passage establishes the exact expanded named-family prevalence statement. This is a nearest-source attribution overreach, not a denial that these families have other metal roles or a universal defect inferred from generic graph nodes.

### quoted-context-precision: Two quoted notes need literal wording and context distinguished

minor / open / confirmed; issue key: metal-tolerant-quoted-context-precision.

Edge 3 places quotation marks around a meaning-supported paraphrase rather than a contiguous source excerpt. Edge 5 quotes a literal cooperation prefix whose immediate context combines reduction with methylation; separate discussion supports the represented reduction/efflux background. Preserve that positive background and the study’s inferred community evidence tier. This grouped documentary concern does not declare the underlying existing biology false.

### ion-condition-facet: The challenge node mixes ion identity with an excess condition

minor / open / confirmed; issue key: metal-tolerant-ion-condition-facet.

Node 1 labels a toxic heavy-metal ion, is typed ENVIRONMENTAL_FACTOR, and describes cytoplasmic excess. Those phrases leave unclear whether it represents a material ion, an exposure condition or the existing intracellular excess condition. Native environmental factors can represent conditions, so this is bounded referent precision rather than an automatic chemical-type error. Clarify the intended current meaning without imposing a retype, adding a new mechanism or expanding the trait scope.

### human-acceptance-link: Local provenance does not attribute human scientific acceptance

minor / open / confirmed; issue key: metal-tolerant-human-acceptance-link.

The REVIEWED record has nine explicit AI maintenance events. The inspected ignored-inclusive local provenance does not identify a human acceptance decision covering this current target. Maintenance history and explicit duplicate retention are positive provenance, but do not establish that acceptance. Private or remote review remains unassessed; this is not a claim that no human review ever occurred.

## Recommended Actions And Acceptance Checks

### bound-prevalence-attribution

Align the existing prevalence attribution with its inspected source scope.

- Retain the cited substrate scope or supply independently inspected support for the exact current breadth; acknowledge the positive general efflux and exporter-family context.
- Do not turn this documentary correction into a new biological route, experiment or intervention.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation and source checks, maintained QC and generated-output recipes. This review changes no scientific input.

### clarify-quoted-evidence

Separate paraphrase, literal wording and the immediate cooperation context.

- Use verifiable literal wording or clearly marked interpretive prose for edge 3. Distinguish edge 5 quoted cooperation context from its separate positive background support.
- Preserve the community inference evidence tier without inventing a required individual-protein assay or altering the mechanism.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation and source checks, maintained QC and generated-output recipes. This review changes no scientific input.

### clarify-challenge-referent

Make node 1 consistently denote its intended existing referent.

- Label, type, description and incident challenge wording agree on the chosen existing material or condition meaning.
- Do not force CHEMICAL solely from the label, invent a new exposure condition or redefine the whole trait from a contextual cation node.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation and source checks, maintained QC and generated-output recipes. This review changes no scientific input.

### attribute-human-acceptance

Link existing human acceptance or leave acceptance unresolved for the curator.

- Acceptance identifies the reviewed revision and scope, including source limits and unassessed incidental details. Retain all nine AI events.
- Automated validation and this AI review do not substitute for human scientific acceptance; remote/private decisions are not presumed absent.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-007.n_925exy/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-metal-validate | /private/tmp/traitmech-record-sweep-007.n_925exy/metal-validate.log; Executed 2026-10-21T11:59:58Z through 2026-10-21T11:59:59Z; metadata metal-validate.json | context_only | Actual execution at 11:59:58–11:59:59 UTC passed. Structural validation is separate from scientific support. |
| check-metal-strict | /private/tmp/traitmech-record-sweep-007.n_925exy/metal-strict.log; Executed 2026-10-21T11:59:58Z through 2026-10-21T11:59:59Z; metadata metal-strict.json | context_only | Actual execution at 11:59:58–11:59:59 UTC passed. Native acceptance does not certify source scope or ontology precision. |
| check-metal-snippets | /private/tmp/traitmech-record-sweep-007.n_925exy/metal-snippets.log; Executed 2026-10-21T12:00:01Z through 2026-10-21T12:00:05Z; metadata metal-snippets.json | context_only | Actual execution at 12:00:01–12:00:05 UTC passed: two snippets, one VERIFIED and one NOT_IN_ABSTRACT. Manual full-body inspection confirms the second. No initial DNS failure occurred for this record. |
| check-corpus-protein-taxa | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log; Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json | context_only | Original batch-four execution at 08:55:04–08:55:10 UTC passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC, one protected and no gaps or errors. The unchanged corpus supports reuse, not a fresh focused scientific check. |
| check-batch006-qc | /private/tmp/traitmech-record-sweep-006.nq5qngor/batch006-qc.log; Executed 2026-10-21T11:54:49Z through 2026-10-21T11:57:53Z; metadata batch006-qc.json | context_only | Original just qc passed at 11:54:49–11:57:53 UTC. The qualified batch-seven byte comparison supports reuse; no new batch-seven QC execution is claimed. |
| capture | Native selected-record capture; 59 inputs; actual inspect 11:59:23.706771–11:59:24.738705 UTC | supports | Every current captured input hash matches. Parent, proposals, policies and writer inputs are context, not additional targets. |
| record | data/traits/environment/metal_tolerant.yaml; Entire record, including all nine history events | partial | The target is REVIEWED with nine explicit AI events, one NONMECHANISTIC graph, three contextual protein classes and no individual protein instance. |
| native-policy | Native field-by-field review checklist; Identity, evidence placement, represented meanings, completeness and human acceptance | supports | Review distinguishes source truth, quotation context, current semantic meaning and provenance. Optional datasets, protein instances and predicate identifiers are not blanket completeness requirements. |
| native-types | Native node type definitions; CausalNodeTypeEnum, schema lines 660–702 | supports | Environmental conditions, material chemicals, proteins, biological processes and traits have different intended facets. A wording ambiguity does not itself prove formal disjointness or dictate a particular retype. |
| protein-policy | Protein grounding and instance policy; Grounding policy lines 174–195; contextual class versus optional instance | supports | Label-only classes may remain in generic contextual sketches. Protein-module wording and operon metadata do not require a genetic-element node or one assembled complex. |
| reuse | Original B6 to B7 byte comparison; Original verification 11:36:30.388266 UTC | context_only | The full trait/history and common-input comparison retains the original execution scopes. Its older QC statement is superseded for timing by the qualified supplement, not silently rewritten. |
| reuse-supplement | Qualified B6 QC reuse supplement; Qualified 12:01:47.374200 UTC; original QC 11:54:49–11:57:53 UTC | supports | The newer successful QC log, unchanged inputs and environment readiness are retained. The all-file history recheck distinguishes 1,277 YAML records from 1,278 total files. Reuse is not a fresh command or certification against later releases. |
| identity | Complete pinned identity and retention assessment; Local 000012; active METPO1007074; v5 row 14; active-review row 41; release-delta row 1182 | supports | The active overlapping metal-tolerance term exists. Explicit DUPLICATE_NO_NEW_PRIMARY handling preserves the local primary record and v5 crosswalk; no automatic migration or false upstream-absence claim follows. |
| retention-authority | Maintained METPO release disposition; METPO1007074 row 41, DUPLICATE_NO_NEW_PRIMARY | supports | The maintained table explicitly retains traitmech:000012 as the existing reviewed record. This ownership decision is distinct from human acceptance of every current claim. |
| go-transport | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0030001; Actual access 12:00:15.329199–12:00:15.952388 UTC | supports | Active GO:0030001 is the biological process metal ion transport. Its definition includes multiple directions and it explicitly has metal ion export as a narrow synonym. The record supplies export specificity in its own wording without an exact-equivalence assertion. |
| taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=119219,303,266264&amp;retmode=xml; Original access 11:36:34.547761–11:36:34.845702 UTC; only canonical taxon 119219 used | supports | NCBI119219 resolves to Cupriavidus metallidurans with documented historical names. Taxonomic identity does not itself establish the phenotype in every strain. |
| predicate-authority | Recursive RO, RDFS and local relation assessment; RO original access 09:52:45.989262 UTC; RDFS original access 09:28:41.654521 UTC; current assessment 12:03:06.439740 UTC | supports | The current material pump to biological-process RO2327 edge fits inherited executor roles. Local challenges/confers and class-to-class RDFS roles also fit. Free-text predicates do not acquire unasserted RO constraints. No ontology reasoner execution is claimed. |
| authority-reuse | Authority and catalog reuse receipts; Hash verification 12:00:58.170679 UTC; original acquisitions retained | supports | RO, RDFS, NCBI, catalog and bounded runner receipts retain original times and hashes. Current interpretation and copying are not new external observations. |
| ground-ledger | Complete documentary grounding ledger; Nine nodes, eight edges, two components and 59 matching inputs | partial | The node-1 facet ambiguity remains. The preliminary broad-GO candidate is declined as a separate finding by final adjudication; the active transport ground remains valid with a precision limitation. |
| node-edges | Complete node and edge ledger; Nodes 0–8 and edges 0–7, zero-based | partial | All endpoints resolve. Current protein modules, chemicals, processes and trait classes retain their intended roles. A generic contextual sketch does not require artificial links between its two components. |
| owners | Maintained ownership and recurrence assessment; Finalizer line 51; v5 row 14; predicate mappings rows 8, 9, 38, 102; existing-value writer guards | supports | Current textual source claims and node-1 wording belong to the record. The retained identity and historical migrations have maintained owners; no exact writer or mapping assignment for those textual defects was found in the bounded search. Correct historical fixes are preserved. |
| provenance | Bounded ignored-inclusive local provenance; Search 12:00:58.185188–12:01:09.176484 UTC; exact follow-ups through 12:01:09.301859 UTC | partial | Nine explicit AI events document maintenance. The inspected local material does not attribute human scientific acceptance of this target. No target-specific repository history or targeted local review was found within these bounds; remote/private decisions remain unknown. |
| expression | Canonical-only catalog applicability; Retained catalog: 20 organisms and 28 datasets, originally acquired 07:36:12.732638–07:36:12.858149 UTC | context_only | Cupriavidus metallidurans and its documented historical names have no catalog match. No other species or strain was substituted and no downstream gene/module query was performed. Noncoverage is not negative phenotype evidence. |
| runner | Reused bounded structured-runner discovery; Original B5 PATH/project discovery 09:27:57 UTC; earlier external bounds 08:17:15 UTC | context_only | Historical bounded discovery supports the official catalog fallback. It is neither a fresh B7 search nor a whole-machine absence claim. |
| source-ledger | Qualified source assessment; Five works, fourteen placements, two snippets and three quoted notes; qualified 12:04:22.441455 UTC | partial | The final source assessment preserves positive definition, synonym, example and general environmental support, while distinguishing the material prevalence-attribution error from bounded quotation/context precision. |
| placements | Complete citation-placement ledger; All fourteen placements, including definition, synonyms, canonical example and every edge | partial | Actual abstracts, primary-body passages, generic background and study-specific inference are distinguished. No aggregate NONMECHANISTIC node is automatically read as a universal biological claim. |
| snippets | All literal snippet and quoted-note occurrences; Two literal snippets; two literal quoted-note substrings with contextual qualifiers; one nonliteral quoted paraphrase | partial | Exact substring matching is separate from contextual attribution. The native abstract miss for the BS1 snippet is resolved by its complete source body; the other concerns arise from inspected primary text. |
| edge-sources | Complete eight-edge source assessment; Edges 0–7 at bounded existing environmental scope | partial | Generic efflux and represented background have positive support. The exact family-prevalence attribution on edge 7 expands its nearest zinc context. Incidental pathogen-specific and engineered fitness details remain UNASSESSED_SCOPE. |
| meta-nies | PMID:12829273; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12829273+AND+SRC%3AMED&amp;format=json&amp;resultType=core | supports | Efflux-mediated heavy metal resistance in prokaryotes. Source access: Actual current indexed abstract only; publisher PDF403 and direct ScienceDirect403. Search-indexed section snippets were not used as verified body. |
| meta-bs1 | PMID:32117100; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffmicb.2020.00047&amp;format=json&amp;resultType=core | supports | Comparative Insights Into the Complete Genome Sequence of Highly Metal Resistant &lt;i&gt;Cupriavidus metallidurans&lt;/i&gt; Strain BS1 Isolated From a Gold-Copper Mine. Source access: Actual reused full JATS, original08:55:31.339754Z; fresh indexed identity/status. |
| meta-ch34 | PMID:20463976; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20463976+AND+SRC%3AMED&amp;format=json&amp;resultType=core | supports | The complete genome sequence of Cupriavidus metallidurans strain CH34, a master survivalist in harsh and anthropogenic environments. Source access: Actual reused full JATS, original08:55:43.673652Z; fresh indexed identity/status. |
| meta-jmmg | DOI:10.52700/jmmg.v5i1.155; https://api.crossref.org/works/10.52700%2Fjmmg.v5i1.155 | supports | Mechanisms of Toxicity of Heavy Metals and the Microbial Strategies for their Mitigation: A Review Source access: Actual publisher landing HTML, Crossref record and downloaded version-of-record PDF; EPMC0 is index absence, not invalidity. |
| meta-peerj | PMID:39494289; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7717%2Fpeerj.18383&amp;format=json&amp;resultType=core | supports | The role of microbiomes in cooperative detoxification mechanisms of arsenate reduction and arsenic methylation in surface agricultural soil. Source access: Actual reused full JATS, original08:55:35.366361Z; fresh indexed identity/status. |
| nies-primary | PMID:12829273; Actual indexed abstract; acquired 12:00:07.351029 UTC | supports | The abstract explicitly supports metal-exporting systems and the named broad families. The complete first snippet is literal. Unseen body compartments and precise dominance are not verified from the abstract alone. |
| bs1-primary | DOI:10.3389/fmicb.2020.00047; Abstract, Introduction paragraph 1, Results S3.SS4/body paragraph 25; original acquisition 08:55:31.339754 UTC | supports | The second snippet is literal in its BS1 context. The metallophilic usage and genomic comparison provide scoped support without proving uniform resistance or causality from gene presence alone. |
| ch34-primary | PMID:20463976; Abstract and Introduction s1/body paragraph 2; original acquisition 08:55:43.673652 UTC | supports | CH34 is a broad metal-tolerance model and has plasmid-borne resistance determinants. The record does not state that all determinants are plasmid-borne or that all strains behave identically. |
| jmmg-primary | DOI:10.52700/jmmg.v5i1.155; Section 7, printed page 53/PDF page 9; zinc paragraph printed page 55/PDF page 11; acquired 12:01:13.414428 UTC | partial | Page 53 positively supports broad active-efflux background and the existing generic context. Page 55 attributes the exact named-family most-bacteria statement specifically to zinc. This does not establish the expanded heavy-metal prevalence statement or deny other metal roles for those families. |
| peerj-primary | DOI:10.7717/peerj.18383; Abstract, Introduction paragraph 2, Discussion paragraphs 35–36; original acquisition 08:55:35.366361 UTC | partial | The literal cooperation prefix concerns reduction together with methylation. Separate discussion supports the existing reduction/efflux background. The study infers community functional potential; it is not a direct protein assay or uniform organism-level tolerance measurement. |
| source-reuse | Original primary-body reuse receipts; BS1, CH34 and PeerJ copied 12:00:16 UTC with original 08:55 acquisition times and hashes | supports | Three complete retained bodies were reused; copying and current passage inspection are distinct from original retrieval. JMMG was freshly acquired separately. |
| publication-status | Bounded publication-status audit; Current indexed metadata and JMMG Crossref/publisher fields; assessed 12:03:53.047243 UTC | context_only | No corrective relation appeared in the inspected fields and landing page. This is not a globally exhaustive absence claim. JMMG index noncoverage is resolved by its registry and actual publisher PDF. |
| root-primary-read | Independent primary-passage read receipt; Actual indexed abstracts and BS1/PeerJ passage windows; read 12:01:28.825919 UTC | supports | The parent inspected critical existing text and verified retained body hashes. This receipt records a later read, not new body acquisition or blanket mechanism validation. |
| root-jmmg-read | Independent JMMG passage read receipt; Printed pages 53 and 55; recorded 12:02:17.348856 UTC | partial | The parent confirmed quotation fidelity and zinc-specific attribution. The final adjudication additionally records inspection of the positive broad page-53 efflux context; neither observation establishes universal prevalence. |
| adjudication | Final parent scientific adjudication; Finalized 12:07:31.019853 UTC; one major and three minor findings | supports | Final adjudication declines a separate GO-direction finding, preserves maintained identity and positive source context, and limits corrections to documentary scope and represented meaning. |

## Limits And Additional Notes

- Active METPO1007074 is a real overlap, explicitly retained against local 000012; proposed v5 1007611 and local properties remain provisional. No false absence claim, automatic migration or synonym upgrade follows.
- GO0030001 is a biological transport process with export as a narrow synonym. The record supplies direction in its own wording and does not assert exact equivalence; no separate finding is assigned for that precision limit.
- Nies was inspected at indexed-abstract scope. Failed body access and unusable search-indexed leads do not establish body absence. Broad family support is positive; exact aggregate compartment and dominance details remain bounded.
- JMMG page 53 positively supports broad active-efflux background. The material finding is the exact named-family most-bacteria attribution on page 55, whose zinc qualifier is lost; it does not deny other metal roles.
- BS1 and CH34 results remain strain-scoped. Canonical CH34 and plasmid-borne determinants are supported without claiming every determinant is plasmid-borne or every strain has equal resistance.
- PeerJ distinguishes community functional-potential inference from its literature background. The existing reduction/efflux background is positive, while the cooperation quotation has a different immediate combined context; no mandatory protein assay is inferred.
- Generic NONMECHANISTIC context, two components and three label-only classes do not require token accessions, new biological links or an assembled complex. The former operon node, retired accession and trait-object RO assignment are historical corrections, not present defects.
- Incidental pathogen-specific and engineered fitness details in acquired sources remain UNASSESSED_SCOPE. Acquisition of full files does not imply validation of every detailed mechanism; no new target, pathway, experiment, exposure condition or optimization is supplied.
- Catalog and structured-runner observations retain original times and bounded discovery scope. There is no matching canonical organism dataset; absent coverage is not negative phenotype evidence.
- Publication status is limited to inspected indexed/registry fields and the publisher landing page. Failed accesses, original body acquisitions, later copying, independent passage reads and final interpretation remain distinct.
- Nine AI events and bounded ignored-inclusive local searches do not attribute human acceptance. Positive maintenance remains intact; private or remote acceptance is unknown. The historical provider report was a lead/limited provenance input, not fully read scientific evidence.
- B6 QC, B4 protein audit, B3 history validation and OLD product failures/retry retain original execution dates and scopes. The qualified history proof separates 1,277 YAML records from 1,278 total files. No fresh corpus execution or environment, repository, Git or state mutation occurred in this builder preparation.
- Four findings: one major and three minor. Field indices are zero-based. The native needs_changes judgment is normalized to structured verdict needs_curation.
- All 59 capture hashes match. Coverage includes five works, fourteen placements, two snippet fields, three quoted notes, nine nodes, eight edges, two components, three label-only proteins, zero instances and nine explicit AI events.
- Source observations completed at 12:03:53.047913 UTC and severity qualified at 12:04:22.441455 UTC. Grounding completed at 12:03:06.449556 UTC; parent adjudication at 12:07:31.019853 UTC. Primary acquisition times remain separate.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T121104Z-metal-tolerant
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of metal tolerant
started_at: '2026-10-21T11:59:23.706771Z'
finished_at: '2026-10-21T12:11:04Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: This session did not author or modify the captured scientific
    record. Separate source and grounding agents supplied complete ledgers; the parent
    independently read critical primary passages and adjudicated the findings. This
    AI review and automated maintenance are distinct from human scientific acceptance.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The retained local identity, broad definition, canonical CH34 example and
  current relation roles are supported. One major finding concerns a zinc-specific
  prevalence statement generalized to heavy metals. Three minor findings concern quoted-note
  context, an ion-versus-condition wording ambiguity and bounded human-acceptance
  attribution. All nine nodes, eight edges and fourteen citation placements are covered.
  Both snippet fields are literal; the three quoted notes comprise two literal but
  context-sensitive substrings and one supported paraphrase. GO0030001 remains a valid
  broad transport grounding with a precision limitation only.
source:
  git_revision: 8eee04a8c65609fbaff6df7c54597dcaf1b9d282
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
    role: context
  - path: .claude/skills/manage-identifiers/SKILL.md
    sha256: a5c5aaa10943ee6d15423a5878ed2189e4e0b28a5c6e09fda80ba299ab779ebb
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: bb03efa3bbd3748ee1dccf57612a6ce8fcc861f20eb57c33eb16e3ac1dd728bd
    role: context
  - path: CLAUDE.md
    sha256: 4d328127022388e1affe9b71be24bc93944a971636d0d0ea902f6511e0b405c5
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: cbe5c82379e796446366b292f15194d80625b928119b482a67d857a379ab31a7
    role: context
  - path: data/raw/biolink-model.yaml
    sha256: 4955709e1cac1d26fd657f7a0c29d6c8390f42e41f9ebfab859c82b102f2bebb
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/environment/metal_tolerant.yaml
    sha256: 907f78048e48c547d03e3b2b073216a32007a0c0608fb361fba976a3812710c5
    role: target
  - path: data/traits/upper/phenotype.yaml
    sha256: 502760fa1b7179bf4e25ab56ecb91d0b25d5f50ed5cfe44133c63a9b821cc4a4
    role: context
  - path: docs/CURATION_PLAYBOOK.md
    sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
    role: context
  - path: docs/GROUNDING_POLICY.md
    sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
    role: context
  - path: docs/PATHWAY_LINKS.md
    sha256: 800492750fb3c025dfdf7164813e7a00b3bd72dc8cc6f8e754e2aed5d7bbf414
    role: context
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 008643042a721e84f647be6beda104ae02fe616361ff9b34fc608643a7526ee2
    role: context
  - path: mappings/node_grounding.tsv
    sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: mappings/trait_exact_match_review.tsv
    sha256: 7728593d526d9a723716e5daad64beb7e1ab5c2e4221ae8d43dd9480cd02f62b
    role: context
  - path: mappings/uniprot_regrounding_candidates.tsv
    sha256: c36d8e038886d137d5a1ae609240e59ce74b6aeee17ae24f21b6c4a0d7407391
    role: context
  - path: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
    sha256: 4ab5ca37ff8595210254b1099563b4425ecd737ed375dc5a932b44e2ad5c332e
    role: context
  - path: proposals/metpo_traitmech_v2/proposal.md
    sha256: fe0601356b120ef9babc6f90a417f860bf02aa628c46af661517f168e01bc48f
    role: context
  - path: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
    sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v5/proposal.md
    sha256: 5d54623dd00ac80a8d67a0eab7b70385f7f57b36daa205c28aa1f9d6f9be6167
    role: context
  - path: proposals/metpo_traitmech_v6/metpo_proposal_properties_robot.tsv
    sha256: ed877efe2d59f43c51898e2dc85440188711455dcc5c882af2dc1384fc38fc19
    role: context
  - path: proposals/metpo_traitmech_v6/proposal.md
    sha256: aecbd48fd73712ccab57619d753b6084a7fa2fbf616f80623f63ce15b65871ae
    role: context
  - path: proposals/metpo_traitmech_v7/metpo_proposal_classes_robot.tsv
    sha256: 99e779afa894363b32966bd15415417035d246970aab02931ce896f37c910a73
    role: context
  - path: proposals/metpo_traitmech_v7/proposal.md
    sha256: bc6ea10ebc4bec0f446cee92578602889ec464295ce5ecce27fed76eb06528ce
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
    role: context
  - path: proposals/metpo_traitmech_v8/proposal.md
    sha256: 119d51e7b7194890514a9e313505212bab92aeba607f7c1b8f9d9d2edeef67e7
    role: context
  - path: proposals/metpo_traitmech_v9/metpo_proposal_properties_robot.tsv
    sha256: 5ae84dd1351a4bec39adf7bcd5b3a8982af2e95fbccd0b53c0efa3efbfc89b0e
    role: context
  - path: proposals/metpo_traitmech_v9/proposal.md
    sha256: 85fde22f4733863188b437cfcf7552a31fea07ad1d32c0400cf493295c1e1156
    role: context
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/ontology_snapshot_manifest.tsv
    sha256: 4a157279a8c4e3fc2afb5382a45c31961991bbd1f330f26d0061b0cfd0b4d213
    role: context
  - path: research/traits/environment/metal_tolerant-deep-research-falcon.md
    sha256: 7ea51cb18101fc734faf9378b86abfef0c722bd83997bb29e425a6e88a263940
    role: context
  - path: scripts/audit_causal_graphs.py
    sha256: e0c26506c9de712700317284f142097e7bf69334806b8010db5d6517e905e834
    role: context
  - path: scripts/audit_graph_protein_taxa.py
    sha256: d3375861829c612483b3545dd0f5e2b79872a4576b626edc08714a09fbd9a24d
    role: context
  - path: scripts/audit_uniprot_grounding.py
    sha256: 91eb2165c69b3a4fcb53154dc8c835ac1070577f88065a43dfc881284d3d1052
    role: context
  - path: scripts/backfill_canonical_examples_444.py
    sha256: 18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c
    role: context
  - path: scripts/curate_knowledge_gaps.py
    sha256: 9e0fb7e01a901d84189a28f1912a2552f28d2da8733c113589e4947359d48c73
    role: context
  - path: scripts/finalize_metpo_2026_06_12_review.py
    sha256: b850b386183b2d86647dada43f7f157059017dbb881f7e1fb2e220ae697d3bea
    role: context
  - path: scripts/ground_causal_nodes.py
    sha256: 204ce4162544154b1752b65da2136538847ea25ced26a52f5708eadff08f5d42
    role: context
  - path: scripts/ground_causal_predicates.py
    sha256: 5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381
    role: context
  - path: scripts/migrate_disposition_typing.py
    sha256: ebafdd145fc0729d32f3b8a45f570d97a8e001838afadd698e2b246cb8950714
    role: context
  - path: scripts/migrate_enables_trait_edges.py
    sha256: a5e7965ee4f6b6ba5bae3a06bced2a83cbf755f3b9b150ce6acc0cd808cb1d88
    role: context
  - path: scripts/migrate_microbe_domain_edges.py
    sha256: 5187ccfb2897d415b243792a27afd6002c0eea4b167068639ff5be73ed583bb6
    role: context
  - path: scripts/migrate_name_match_groundings.py
    sha256: 9b3ea1153839b9b260638cef95eba2d1ccc6d7b3825e7352c33cceb21bfe4dd4
    role: context
  - path: scripts/migrate_oxygen_senses.py
    sha256: 372e977a58ec6e17cdd45021c5849895142c67187eb29b995b8c39f0e899d2f3
    role: context
  - path: scripts/migrate_pathway_vs_process.py
    sha256: f236de7183048732e9001b7fac4367affff58d8b7a7d5c63286e6b058a4b38c2
    role: context
  - path: scripts/migrate_process_quality_consistency.py
    sha256: 1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a
    role: context
  - path: scripts/migrate_protein_vs_activity.py
    sha256: 0b183248ff22d3d8aa66b35aece40c53b516684ca499cf73b7714206031dad49
    role: context
  - path: scripts/migrate_uniprot_instance_groundings.py
    sha256: 07d2a5405cff5857239757e0a3791f411b1d25709a5760c1e49553eed066993d
    role: context
  - path: scripts/seed_from_metpo.py
    sha256: 0fb9c9f7ea6a8f137eecd5c319775b511c398dba6158c81b1fbfb94210f7d851
    role: context
  - path: scripts/verify_metpo_proposal.py
    sha256: f58355151f7d6a807bb50dc8b732184994b0d6145d3c57f54e29fd0bb76268b6
    role: context
  - path: src/traitmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: src/traitmech/validation/write_validated.py
    sha256: 68cfeb876a60d67fd72d5a2800cd29e41b5cf563be5a27b698398a5bb3e67231
    role: context
targets:
- target_id: traitmech:000012
  path: data/traits/environment/metal_tolerant.yaml
  label: metal tolerant
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/metal_tolerant.yaml
    role: Maintained TraitRecord; scientific edits require separate curation authorization
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: First record in the seventh path-ordered batch. One entire maintained
    environmental TraitRecord and its parent context were read. All 59 captured inputs,
    nine nodes, eight edges, two components, three label-only protein classes, one
    canonical example, five assigned works, fourteen citation placements, two snippets,
    three quoted notes and nine explicit AI events are accounted for. The historical
    provider report supplies a lead and limited provenance context only; no complete
    report read is claimed. Existing general environmental claims receive bounded
    review; incidental pathogen-specific and engineering fitness details remain UNASSESSED_SCOPE.
    No new mechanism, target, experiment or optimization is supplied.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000012
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000012
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - traitmech:000012
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - traitmech:000012
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - traitmech:000012
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - traitmech:000012
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - traitmech:000012
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - traitmech:000012
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: metal-validate
  name: Focused native record validation
  status: passed
  required: true
  target_ids:
  - traitmech:000012
  command: just validate data/traits/environment/metal_tolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual execution at 11:59:58–11:59:59 UTC passed. Structural validation
    is separate from scientific support.
  evidence_ids:
  - check-metal-validate
- check_id: metal-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000012
  command: just validate-strict data/traits/environment/metal_tolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual execution at 11:59:58–11:59:59 UTC passed. Native acceptance does
    not certify source scope or ontology precision.
  evidence_ids:
  - check-metal-strict
- check_id: metal-snippets
  name: Focused native snippet verification
  status: passed
  required: true
  target_ids:
  - traitmech:000012
  command: just verify-snippets --record data/traits/environment/metal_tolerant.yaml
    --out /private/tmp/traitmech-record-sweep-007.n_925exy/metal-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual execution at 12:00:01–12:00:05 UTC passed: two snippets, one VERIFIED
    and one NOT_IN_ABSTRACT. Manual full-body inspection confirms the second. No initial
    DNS failure occurred for this record.'
  evidence_ids:
  - check-metal-snippets
- check_id: corpus-protein-taxa
  name: Reused corpus protein/taxon audit
  status: passed
  required: true
  target_ids:
  - traitmech:000012
  command: just audit-graph-protein-taxa --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Original batch-four execution at 08:55:04–08:55:10 UTC passed: 719 graphs,
    129 PASS, 589 NONMECHANISTIC, one protected and no gaps or errors. The unchanged
    corpus supports reuse, not a fresh focused scientific check.'
  evidence_ids:
  - check-corpus-protein-taxa
- check_id: batch006-qc
  name: Reused batch-six maintained QC
  status: passed
  required: true
  target_ids:
  - traitmech:000012
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Original just qc passed at 11:54:49–11:57:53 UTC. The qualified batch-seven
    byte comparison supports reuse; no new batch-seven QC execution is claimed.
  evidence_ids:
  - check-batch006-qc
  scope_note: The original comparison covers 1,130 traits, 1,278 history files and
    19 common inputs. The qualified supplement freshly rechecks all 1,278 history
    files, comprising 1,277 YAML records and history/README.md, separately from its
    earlier YAML-only comparison. Original B3 history and OLD product failures, successful
    retry, baselines and skips remain unchanged.
- check_id: uniprot-applicability
  name: Protein instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000012
  summary: Three contextual REVIEWED_LABEL_ONLY protein classes and zero protein instances
    occur in a NONMECHANISTIC graph. No instance metadata assertion requires a target
    UniProt audit, and no token accession is required.
  evidence_ids:
  - record
  - protein-policy
  - node-edges
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-007.n_925exy/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-metal-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-007.n_925exy/metal-validate.log
  locator: Executed 2026-10-21T11:59:58Z through 2026-10-21T11:59:59Z; metadata metal-validate.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: Actual execution at 11:59:58–11:59:59 UTC passed. Structural validation
    is separate from scientific support.
  snapshot_sha256: feed5f05f285cbaffb6f057cf38ad256ca34a35508103ceffde5a13a30d2d2a4
- evidence_id: check-metal-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-007.n_925exy/metal-strict.log
  locator: Executed 2026-10-21T11:59:58Z through 2026-10-21T11:59:59Z; metadata metal-strict.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: Actual execution at 11:59:58–11:59:59 UTC passed. Native acceptance does
    not certify source scope or ontology precision.
  snapshot_sha256: d895aeef3aa60bfcc4f17575f57287c9ec224daf5a05de63808788dbe32d1d47
- evidence_id: check-metal-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-007.n_925exy/metal-snippets.log
  locator: Executed 2026-10-21T12:00:01Z through 2026-10-21T12:00:05Z; metadata metal-snippets.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: 'Actual execution at 12:00:01–12:00:05 UTC passed: two snippets, one VERIFIED
    and one NOT_IN_ABSTRACT. Manual full-body inspection confirms the second. No initial
    DNS failure occurred for this record.'
  snapshot_sha256: e3280aeaa8164dba32babe12092291dafe782797eee679206ad6fda61ee061f6
- evidence_id: check-corpus-protein-taxa
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log
  locator: Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: 'Original batch-four execution at 08:55:04–08:55:10 UTC passed: 719 graphs,
    129 PASS, 589 NONMECHANISTIC, one protected and no gaps or errors. The unchanged
    corpus supports reuse, not a fresh focused scientific check.'
  snapshot_sha256: f5f1a6be7789f2b3e487fcbc354361f8f1f0d0d0f90a9ba59864d26ed7ac49ef
- evidence_id: check-batch006-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/batch006-qc.log
  locator: Executed 2026-10-21T11:54:49Z through 2026-10-21T11:57:53Z; metadata batch006-qc.json
  accessed_at: '2026-10-21T12:11:04Z'
  support: context_only
  summary: Original just qc passed at 11:54:49–11:57:53 UTC. The qualified batch-seven
    byte comparison supports reuse; no new batch-seven QC execution is claimed.
  snapshot_sha256: 8d583fb60333a9fc3c697349f3684d7f35e85ed7f49e71f11acab84142106853
- evidence_id: capture
  kind: validation
  reference: Native selected-record capture
  locator: 59 inputs; actual inspect 11:59:23.706771–11:59:24.738705 UTC
  accessed_at: '2026-10-21T11:59:24.738705Z'
  support: supports
  summary: Every current captured input hash matches. Parent, proposals, policies
    and writer inputs are context, not additional targets.
  snapshot_sha256: e0a0dbde40f4842914fba48f92e7c5420a21c060bdec189b2a0232db9cd41c42
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/metal_tolerant.yaml
  locator: Entire record, including all nine history events
  accessed_at: '2026-10-21T12:03:06.449556Z'
  support: partial
  summary: The target is REVIEWED with nine explicit AI events, one NONMECHANISTIC
    graph, three contextual protein classes and no individual protein instance.
  snapshot_sha256: 907f78048e48c547d03e3b2b073216a32007a0c0608fb361fba976a3812710c5
- evidence_id: native-policy
  kind: authority
  reference: Native field-by-field review checklist
  locator: Identity, evidence placement, represented meanings, completeness and human
    acceptance
  accessed_at: '2026-10-21T12:03:06.449556Z'
  support: supports
  summary: Review distinguishes source truth, quotation context, current semantic
    meaning and provenance. Optional datasets, protein instances and predicate identifiers
    are not blanket completeness requirements.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: native-types
  kind: authority
  reference: Native node type definitions
  locator: CausalNodeTypeEnum, schema lines 660–702
  accessed_at: '2026-10-21T12:03:06.449556Z'
  support: supports
  summary: Environmental conditions, material chemicals, proteins, biological processes
    and traits have different intended facets. A wording ambiguity does not itself
    prove formal disjointness or dictate a particular retype.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: protein-policy
  kind: authority
  reference: Protein grounding and instance policy
  locator: Grounding policy lines 174–195; contextual class versus optional instance
  accessed_at: '2026-10-21T12:03:06.449556Z'
  support: supports
  summary: Label-only classes may remain in generic contextual sketches. Protein-module
    wording and operon metadata do not require a genetic-element node or one assembled
    complex.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: reuse
  kind: validation
  reference: Original B6 to B7 byte comparison
  locator: Original verification 11:36:30.388266 UTC
  accessed_at: '2026-10-21T11:36:30.388266Z'
  support: context_only
  summary: The full trait/history and common-input comparison retains the original
    execution scopes. Its older QC statement is superseded for timing by the qualified
    supplement, not silently rewritten.
  snapshot_sha256: c574f87e084e0f076ffb7d60ec06f9f86c2dcd4f16512746c9120854e88f0bf1
- evidence_id: reuse-supplement
  kind: validation
  reference: Qualified B6 QC reuse supplement
  locator: Qualified 12:01:47.374200 UTC; original QC 11:54:49–11:57:53 UTC
  accessed_at: '2026-10-21T12:01:47.374200Z'
  support: supports
  summary: The newer successful QC log, unchanged inputs and environment readiness
    are retained. The all-file history recheck distinguishes 1,277 YAML records from
    1,278 total files. Reuse is not a fresh command or certification against later
    releases.
  snapshot_sha256: 26b4a1e134156fe6cb29f9c238316c846eb1e7b517adcdf25c73bace6aa28355
- evidence_id: identity
  kind: validation
  reference: Complete pinned identity and retention assessment
  locator: Local 000012; active METPO1007074; v5 row 14; active-review row 41; release-delta
    row 1182
  accessed_at: '2026-10-21T12:03:06.438429Z'
  support: supports
  summary: The active overlapping metal-tolerance term exists. Explicit DUPLICATE_NO_NEW_PRIMARY
    handling preserves the local primary record and v5 crosswalk; no automatic migration
    or false upstream-absence claim follows.
  snapshot_sha256: 25b825864e8851024ecb33e67b7816bd39d2b6480b9231ef24f67abaf54cb4ca
- evidence_id: retention-authority
  kind: authority
  reference: Maintained METPO release disposition
  locator: METPO1007074 row 41, DUPLICATE_NO_NEW_PRIMARY
  accessed_at: '2026-10-21T12:03:06.438429Z'
  support: supports
  summary: The maintained table explicitly retains traitmech:000012 as the existing
    reviewed record. This ownership decision is distinct from human acceptance of
    every current claim.
  snapshot_sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
- evidence_id: go-transport
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0030001
  locator: Actual access 12:00:15.329199–12:00:15.952388 UTC
  accessed_at: '2026-10-21T12:00:15.952388Z'
  support: supports
  summary: Active GO:0030001 is the biological process metal ion transport. Its definition
    includes multiple directions and it explicitly has metal ion export as a narrow
    synonym. The record supplies export specificity in its own wording without an
    exact-equivalence assertion.
  snapshot_sha256: 328406a7b5f77827815c907c7a7ec3b8f2ad152e4df8ae5ad49fc6afb88e90c0
- evidence_id: taxon
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=119219,303,266264&retmode=xml
  locator: Original access 11:36:34.547761–11:36:34.845702 UTC; only canonical taxon
    119219 used
  accessed_at: '2026-10-21T11:36:34.845702Z'
  support: supports
  summary: NCBI119219 resolves to Cupriavidus metallidurans with documented historical
    names. Taxonomic identity does not itself establish the phenotype in every strain.
  snapshot_sha256: 0c892ed9811561679f663813500550dfe1a0b839dd0cf720dc9590c8495bc7d6
- evidence_id: predicate-authority
  kind: validation
  reference: Recursive RO, RDFS and local relation assessment
  locator: RO original access 09:52:45.989262 UTC; RDFS original access 09:28:41.654521
    UTC; current assessment 12:03:06.439740 UTC
  accessed_at: '2026-10-21T12:03:06.439740Z'
  support: supports
  summary: The current material pump to biological-process RO2327 edge fits inherited
    executor roles. Local challenges/confers and class-to-class RDFS roles also fit.
    Free-text predicates do not acquire unasserted RO constraints. No ontology reasoner
    execution is claimed.
  snapshot_sha256: d506ad55558444de2091bd0aca100be82a3fafadc5e15ec3e3e0e7886418cfa7
- evidence_id: authority-reuse
  kind: validation
  reference: Authority and catalog reuse receipts
  locator: Hash verification 12:00:58.170679 UTC; original acquisitions retained
  accessed_at: '2026-10-21T12:00:58.170679Z'
  support: supports
  summary: RO, RDFS, NCBI, catalog and bounded runner receipts retain original times
    and hashes. Current interpretation and copying are not new external observations.
  snapshot_sha256: 48abd128500b0af37789df29db34c4278ad2296921f73fc8a8e8cd1529e73e7b
- evidence_id: ground-ledger
  kind: validation
  reference: Complete documentary grounding ledger
  locator: Nine nodes, eight edges, two components and 59 matching inputs
  accessed_at: '2026-10-21T12:03:06.449556Z'
  support: partial
  summary: The node-1 facet ambiguity remains. The preliminary broad-GO candidate
    is declined as a separate finding by final adjudication; the active transport
    ground remains valid with a precision limitation.
  snapshot_sha256: f511e392ef520bfdf3af2c07202a34399a185a8182fa44d8b867167d3352f0c8
- evidence_id: node-edges
  kind: validation
  reference: Complete node and edge ledger
  locator: Nodes 0–8 and edges 0–7, zero-based
  accessed_at: '2026-10-21T12:03:06.444841Z'
  support: partial
  summary: All endpoints resolve. Current protein modules, chemicals, processes and
    trait classes retain their intended roles. A generic contextual sketch does not
    require artificial links between its two components.
  snapshot_sha256: 79e4e92b020ef90cbe4b57ac44d150d400234dbf21d3a1d16bf1cca43766779d
- evidence_id: owners
  kind: validation
  reference: Maintained ownership and recurrence assessment
  locator: Finalizer line 51; v5 row 14; predicate mappings rows 8, 9, 38, 102; existing-value
    writer guards
  accessed_at: '2026-10-21T12:03:06.446581Z'
  support: supports
  summary: Current textual source claims and node-1 wording belong to the record.
    The retained identity and historical migrations have maintained owners; no exact
    writer or mapping assignment for those textual defects was found in the bounded
    search. Correct historical fixes are preserved.
  snapshot_sha256: 2ae0cbdd93c9bb6edb465d96af7b4d3a9a04496991fdbbca1f7777852850fcf8
- evidence_id: provenance
  kind: search
  reference: Bounded ignored-inclusive local provenance
  locator: Search 12:00:58.185188–12:01:09.176484 UTC; exact follow-ups through 12:01:09.301859
    UTC
  accessed_at: '2026-10-21T12:03:06.445748Z'
  support: partial
  summary: Nine explicit AI events document maintenance. The inspected local material
    does not attribute human scientific acceptance of this target. No target-specific
    repository history or targeted local review was found within these bounds; remote/private
    decisions remain unknown.
  snapshot_sha256: c58b363cac2eddd4292d24f7b4afbc76931959485ef4c515f9aa7351b6f6f9de
  search_scope: Own B7 repository searches included ignored and hidden files, excluding
    .git and .venv, with exact target ID, slug, label, graph and module terms. Follow-ups
    covered history for current and legacy node IDs; scripts/mappings/history for
    the GO and node names; history/scripts for the canonical taxon, source PMID and
    retired accession. The primary result contained 185 matching files. No private
    or remote material was searched.
- evidence_id: expression
  kind: validation
  reference: Canonical-only catalog applicability
  locator: 'Retained catalog: 20 organisms and 28 datasets, originally acquired 07:36:12.732638–07:36:12.858149
    UTC'
  accessed_at: '2026-10-21T12:03:06.447721Z'
  support: context_only
  summary: Cupriavidus metallidurans and its documented historical names have no catalog
    match. No other species or strain was substituted and no downstream gene/module
    query was performed. Noncoverage is not negative phenotype evidence.
  snapshot_sha256: 8977c1f6cb256f17ec95734a438598c1169a70625a0f2d345616725504c66ad1
- evidence_id: runner
  kind: search
  reference: Reused bounded structured-runner discovery
  locator: Original B5 PATH/project discovery 09:27:57 UTC; earlier external bounds
    08:17:15 UTC
  accessed_at: '2026-10-21T09:27:57.542053Z'
  support: context_only
  summary: Historical bounded discovery supports the official catalog fallback. It
    is neither a fresh B7 search nor a whole-machine absence claim.
  snapshot_sha256: 43597ec8b007fc605fabf9069534281f331a33bda5615b9ce9c473facf744179
  search_scope: Retained B5 PATH and ignored-inclusive project search plus the separately
    retained bounded external installation search in prior-runner-discovery-external.json.
    Original roots, exclusions and timestamps govern; no fresh B7 or global absence
    claim.
- evidence_id: source-ledger
  kind: validation
  reference: Qualified source assessment
  locator: Five works, fourteen placements, two snippets and three quoted notes; qualified
    12:04:22.441455 UTC
  accessed_at: '2026-10-21T12:04:22.441455Z'
  support: partial
  summary: The final source assessment preserves positive definition, synonym, example
    and general environmental support, while distinguishing the material prevalence-attribution
    error from bounded quotation/context precision.
  snapshot_sha256: d2f03e0cd4672da23e988209d2d2e642cae304cc5dd036cd3b181f90ce8a7745
- evidence_id: placements
  kind: validation
  reference: Complete citation-placement ledger
  locator: All fourteen placements, including definition, synonyms, canonical example
    and every edge
  accessed_at: '2026-10-21T12:03:53.046832Z'
  support: partial
  summary: Actual abstracts, primary-body passages, generic background and study-specific
    inference are distinguished. No aggregate NONMECHANISTIC node is automatically
    read as a universal biological claim.
  snapshot_sha256: 98aef5d24ab7a1f7958e393739fd07562b211ba0e034a3e5dbdd10626018b93f
- evidence_id: snippets
  kind: validation
  reference: All literal snippet and quoted-note occurrences
  locator: Two literal snippets; two literal quoted-note substrings with contextual
    qualifiers; one nonliteral quoted paraphrase
  accessed_at: '2026-10-21T12:03:53.045574Z'
  support: partial
  summary: Exact substring matching is separate from contextual attribution. The native
    abstract miss for the BS1 snippet is resolved by its complete source body; the
    other concerns arise from inspected primary text.
  snapshot_sha256: a10b4e0171918c9da58095c723e431a4c48c05c5ed047876ec9d2fccf87f4d9d
- evidence_id: edge-sources
  kind: validation
  reference: Complete eight-edge source assessment
  locator: Edges 0–7 at bounded existing environmental scope
  accessed_at: '2026-10-21T12:03:53.046324Z'
  support: partial
  summary: Generic efflux and represented background have positive support. The exact
    family-prevalence attribution on edge 7 expands its nearest zinc context. Incidental
    pathogen-specific and engineered fitness details remain UNASSESSED_SCOPE.
  snapshot_sha256: 9c3f236d2fc74a36939bae55a803c8d4c3da7328b203535b23089d658b97e1e7
- evidence_id: meta-nies
  kind: database
  reference: PMID:12829273
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12829273+AND+SRC%3AMED&format=json&resultType=core
  accessed_at: '2026-10-21T12:00:07.351029Z'
  support: supports
  summary: 'Efflux-mediated heavy metal resistance in prokaryotes. Source access:
    Actual current indexed abstract only; publisher PDF403 and direct ScienceDirect403.
    Search-indexed section snippets were not used as verified body.'
  snapshot_sha256: ab66a791a5245cbb2bd7274916dba2349cf69ed1b105f965af95e8f3d6279302
- evidence_id: meta-bs1
  kind: database
  reference: PMID:32117100
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffmicb.2020.00047&format=json&resultType=core
  accessed_at: '2026-10-21T12:00:07.422924Z'
  support: supports
  summary: 'Comparative Insights Into the Complete Genome Sequence of Highly Metal
    Resistant <i>Cupriavidus metallidurans</i> Strain BS1 Isolated From a Gold-Copper
    Mine. Source access: Actual reused full JATS, original08:55:31.339754Z; fresh
    indexed identity/status.'
  snapshot_sha256: a8416d42dd4c6f8db4c5bdef3797d5c443794ce80876fe8c2034d12cccf96c4a
- evidence_id: meta-ch34
  kind: database
  reference: PMID:20463976
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20463976+AND+SRC%3AMED&format=json&resultType=core
  accessed_at: '2026-10-21T12:00:07.388752Z'
  support: supports
  summary: 'The complete genome sequence of Cupriavidus metallidurans strain CH34,
    a master survivalist in harsh and anthropogenic environments. Source access: Actual
    reused full JATS, original08:55:43.673652Z; fresh indexed identity/status.'
  snapshot_sha256: 6cd8c24e2ee951ad75351dc482041a45c2049bde8ea4c7d3b11b2f30dba85bde
- evidence_id: meta-jmmg
  kind: database
  reference: DOI:10.52700/jmmg.v5i1.155
  locator: https://api.crossref.org/works/10.52700%2Fjmmg.v5i1.155
  accessed_at: '2026-10-21T12:00:38.326938Z'
  support: supports
  summary: 'Mechanisms of Toxicity of Heavy Metals and the Microbial Strategies for
    their Mitigation: A Review Source access: Actual publisher landing HTML, Crossref
    record and downloaded version-of-record PDF; EPMC0 is index absence, not invalidity.'
  snapshot_sha256: c900273150c21c034f3e876386bd858099ac52477874f7b7f4eee170936629a6
- evidence_id: meta-peerj
  kind: database
  reference: PMID:39494289
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7717%2Fpeerj.18383&format=json&resultType=core
  accessed_at: '2026-10-21T12:00:07.998944Z'
  support: supports
  summary: 'The role of microbiomes in cooperative detoxification mechanisms of arsenate
    reduction and arsenic methylation in surface agricultural soil. Source access:
    Actual reused full JATS, original08:55:35.366361Z; fresh indexed identity/status.'
  snapshot_sha256: 7c74cdad915a710ad9ffd11d974895c0bb1cb2cfe1203a3ef4243f3536cb2ddd
- evidence_id: nies-primary
  kind: primary_source
  reference: PMID:12829273
  locator: Actual indexed abstract; acquired 12:00:07.351029 UTC
  accessed_at: '2026-10-21T12:00:07.351029Z'
  support: supports
  summary: The abstract explicitly supports metal-exporting systems and the named
    broad families. The complete first snippet is literal. Unseen body compartments
    and precise dominance are not verified from the abstract alone.
  snapshot_sha256: ab66a791a5245cbb2bd7274916dba2349cf69ed1b105f965af95e8f3d6279302
- evidence_id: bs1-primary
  kind: primary_source
  reference: DOI:10.3389/fmicb.2020.00047
  locator: Abstract, Introduction paragraph 1, Results S3.SS4/body paragraph 25; original
    acquisition 08:55:31.339754 UTC
  accessed_at: '2026-10-21T08:55:31.339754Z'
  support: supports
  summary: The second snippet is literal in its BS1 context. The metallophilic usage
    and genomic comparison provide scoped support without proving uniform resistance
    or causality from gene presence alone.
  snapshot_sha256: 64d52eb8778d5b00a469f8d82deeeeb5d3a0102de2faa89badc5d55f7e72db81
- evidence_id: ch34-primary
  kind: primary_source
  reference: PMID:20463976
  locator: Abstract and Introduction s1/body paragraph 2; original acquisition 08:55:43.673652
    UTC
  accessed_at: '2026-10-21T08:55:43.673652Z'
  support: supports
  summary: CH34 is a broad metal-tolerance model and has plasmid-borne resistance
    determinants. The record does not state that all determinants are plasmid-borne
    or that all strains behave identically.
  snapshot_sha256: bc3ff60f3133a5ec3ac949d7f319d52401370ffaa038d9c498d330529cccd821
- evidence_id: jmmg-primary
  kind: primary_source
  reference: DOI:10.52700/jmmg.v5i1.155
  locator: Section 7, printed page 53/PDF page 9; zinc paragraph printed page 55/PDF
    page 11; acquired 12:01:13.414428 UTC
  accessed_at: '2026-10-21T12:01:13.414428Z'
  support: partial
  summary: Page 53 positively supports broad active-efflux background and the existing
    generic context. Page 55 attributes the exact named-family most-bacteria statement
    specifically to zinc. This does not establish the expanded heavy-metal prevalence
    statement or deny other metal roles for those families.
  snapshot_sha256: fdde8cef7eda612f7ba83cef6f17004419f01020fec03f43ab4cb821b82f6e05
- evidence_id: peerj-primary
  kind: primary_source
  reference: DOI:10.7717/peerj.18383
  locator: Abstract, Introduction paragraph 2, Discussion paragraphs 35–36; original
    acquisition 08:55:35.366361 UTC
  accessed_at: '2026-10-21T08:55:35.366361Z'
  support: partial
  summary: The literal cooperation prefix concerns reduction together with methylation.
    Separate discussion supports the existing reduction/efflux background. The study
    infers community functional potential; it is not a direct protein assay or uniform
    organism-level tolerance measurement.
  snapshot_sha256: e80b4e4a3d59afdc5c57c7240339f0ebac05a146daa9a950d1989b4bb4ee494f
- evidence_id: source-reuse
  kind: validation
  reference: Original primary-body reuse receipts
  locator: BS1, CH34 and PeerJ copied 12:00:16 UTC with original 08:55 acquisition
    times and hashes
  accessed_at: '2026-10-21T12:00:16.285144Z'
  support: supports
  summary: Three complete retained bodies were reused; copying and current passage
    inspection are distinct from original retrieval. JMMG was freshly acquired separately.
  snapshot_sha256: e25562438d24590ecf8bec89b972a9e6273f6ccff402d7bd457cb26a64d2f785
- evidence_id: publication-status
  kind: validation
  reference: Bounded publication-status audit
  locator: Current indexed metadata and JMMG Crossref/publisher fields; assessed 12:03:53.047243
    UTC
  accessed_at: '2026-10-21T12:03:53.047243Z'
  support: context_only
  summary: No corrective relation appeared in the inspected fields and landing page.
    This is not a globally exhaustive absence claim. JMMG index noncoverage is resolved
    by its registry and actual publisher PDF.
  snapshot_sha256: a373454566519c475c6eba15ed7d580465cdd0305c56a2e1b7526f3dae5546a6
- evidence_id: root-primary-read
  kind: validation
  reference: Independent primary-passage read receipt
  locator: Actual indexed abstracts and BS1/PeerJ passage windows; read 12:01:28.825919
    UTC
  accessed_at: '2026-10-21T12:01:28.825919Z'
  support: supports
  summary: The parent inspected critical existing text and verified retained body
    hashes. This receipt records a later read, not new body acquisition or blanket
    mechanism validation.
  snapshot_sha256: 82988d591b7cecc81722a96720b4a759ac8ff2333af1936792f45289d908a081
- evidence_id: root-jmmg-read
  kind: validation
  reference: Independent JMMG passage read receipt
  locator: Printed pages 53 and 55; recorded 12:02:17.348856 UTC
  accessed_at: '2026-10-21T12:02:17.348856Z'
  support: partial
  summary: The parent confirmed quotation fidelity and zinc-specific attribution.
    The final adjudication additionally records inspection of the positive broad page-53
    efflux context; neither observation establishes universal prevalence.
  snapshot_sha256: f716afdd57ac3cc5e7eaaee259bdeb783b4b90e3f20fbf96705f0edb498bb7e0
- evidence_id: adjudication
  kind: validation
  reference: Final parent scientific adjudication
  locator: Finalized 12:07:31.019853 UTC; one major and three minor findings
  accessed_at: '2026-10-21T12:07:31.019853Z'
  support: supports
  summary: Final adjudication declines a separate GO-direction finding, preserves
    maintained identity and positive source context, and limits corrections to documentary
    scope and represented meaning.
  snapshot_sha256: bd7349e84551334c4f8a4e5c11dfa6e754f869ebe4ff4e6948a52a6c77f91325
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, hierarchy and synonym scope'
  outcome: supported
  target_ids:
  - traitmech:000012
  summary: Active METPO1007074 overlaps this local concept, but the maintained release
    disposition explicitly retains traitmech:000012. V5 proposed 1007611 carries its
    definition, parent and crosswalk. Parent METPO1000059 is supported. Related synonyms
    are conservative source-backed uses; no forced migration or exact synonym upgrade
    is warranted.
  evidence_ids:
  - identity
  - retention-authority
  - placements
  - record
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: complete definition and contextual mechanism emphasis'
  outcome: supported
  target_ids:
  - traitmech:000012
  summary: The broad tolerance definition and typical efflux emphasis have positive
    review support. Typical does not mean exclusive or universally necessary, and
    no fixed concentration threshold is asserted. Nies abstract-only limits do not
    prove the unseen body lacks more specific support.
  evidence_ids:
  - nies-primary
  - jmmg-primary
  - placements
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: canonical organism, strain and example note'
  outcome: supported
  target_ids:
  - traitmech:000012
  summary: The official species identity matches Cupriavidus metallidurans. The assigned
    CH34 primary paper supports model status, broad resistance and plasmid-borne determinants;
    it does not require every determinant to be plasmid-borne. BS1 context remains
    strain-specific and is not transferred as uniform species behavior.
  evidence_ids:
  - taxon
  - ch34-primary
  - bs1-primary
  - placements
- assessment_id: nodes
  area: grounding
  topic: 'Native checklist: all nine node identities and represented facets'
  outcome: concern
  target_ids:
  - traitmech:000012
  summary: Node 1 alternates between an ion material, an environmental factor and
    cytoplasmic excess, leaving its intended referent unclear. GO0030001 is a valid
    broad transport process and explicitly includes export as a narrow synonym; export
    specificity remains a limitation only. The other current chemical, protein and
    trait facets are coherent.
  evidence_ids:
  - record
  - native-types
  - go-transport
  - node-edges
  - adjudication
  details: Nodes 0 and 8 are trait classes. Node 1 has the bounded facet ambiguity.
    Node 3 is biological transport. Nodes 4 and 5 are chemical classes. Nodes 2, 6
    and 7 are contextual material protein classes; current module wording does not
    denote the retired operon node.
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all eight predicate roles'
  outcome: supported
  target_ids:
  - traitmech:000012
  summary: The material pump to transport process meets RO2327 executor semantics.
    Local challenges and both confers assignments fit current endpoint meanings; RDFS
    subclass direction fits the trait classes. Free-text conversion and mediation
    do not require IDs or inherit unasserted RO constraints. The edge-7 concern is
    source attribution, not a formal predicate failure.
  evidence_ids:
  - predicate-authority
  - node-edges
  - owners
  details: 'Edge 0: contextual challenge. Edge 1: material executor to process. Edges
    2 and 5: local conferral. Edges 3 and 4: stated free-text conversion roles. Edge
    6: trait subclass. Edge 7: free-text mediation with independently assessed breadth.'
- assessment_id: edge-evidence
  area: evidence
  topic: 'Native checklist: all eight nearest-source assertions'
  outcome: concern
  target_ids:
  - traitmech:000012
  summary: Existing generic efflux and environmental background have positive support.
    Edge 7 expands a zinc-specific named-family prevalence statement to heavy metals
    in most bacteria. Broad page-53 background and Nies family support do not themselves
    establish that exact expanded prevalence claim. No other contextual branch is
    declared universal merely from its generic nodes.
  evidence_ids:
  - edge-sources
  - placements
  - jmmg-primary
  - nies-primary
  - peerj-primary
  - adjudication
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: two snippets and three quoted notes'
  outcome: concern
  target_ids:
  - traitmech:000012
  summary: Both snippet fields are literal in inspected source surfaces. Among three
    quoted notes, one is a meaning-supported paraphrase; two are literal substrings
    whose context matters. The grouped minor concerns edge-3 quote form and edge-5
    cooperation context. Edge-7 zinc scope is the separate material attribution finding,
    without duplicate severity.
  evidence_ids:
  - snippets
  - bs1-primary
  - jmmg-primary
  - peerj-primary
  - check-metal-snippets
- assessment_id: quantity
  area: quantity
  topic: 'Native checklist: concentration, substrate and prevalence scope'
  outcome: concern
  target_ids:
  - traitmech:000012
  summary: No universal concentration cutoff or new assay is required by this broad
    record. The material quantified breadth is most bacteria on edge 7, whose nearest
    statement is zinc-specific. Arsenic oxidation-state labels do not specify universal
    ionic charge, and contextual cation wording does not redefine the entire metal/metalloid
    trait.
  evidence_ids:
  - placements
  - jmmg-primary
  - node-edges
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: five works and fourteen placements'
  outcome: supported
  target_ids:
  - traitmech:000012
  summary: All five publication identities resolve. Four bodies are available at stated
    inspected passage scopes, while Nies is abstract-only. Registry/publisher resolution
    establishes JMMG despite index noncoverage. Metadata status, access failures and
    original reuse dates remain bounded; no global notice-absence claim is made.
  evidence_ids:
  - source-ledger
  - placements
  - meta-nies
  - meta-bs1
  - meta-ch34
  - meta-jmmg
  - meta-peerj
  - publication-status
  - source-reuse
- assessment_id: protein-completeness
  area: completeness
  topic: 'Native checklist: protein classes, instances and graph components'
  outcome: supported
  target_ids:
  - traitmech:000012
  summary: Three explicitly reviewed label-only protein classes and zero instances
    are permitted in the NONMECHANISTIC sketch. The current Ars module is explicitly
    a protein aggregate with gene and operon metadata. Its two components do not require
    artificial connectors or token accessions; retired accessions and prior trait-object
    RO assignments are not current defects.
  evidence_ids:
  - protein-policy
  - node-edges
  - record
  - check-corpus-protein-taxa
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical-only catalog applicability'
  outcome: not_applicable
  target_ids:
  - traitmech:000012
  summary: The retained official catalog has no Cupriavidus metallidurans or documented
    historical-name match. No substitute organism or downstream module query is used.
    Noncoverage is not negative biological evidence or a required-record defect; runner
    discovery retains its earlier bounded scope.
  evidence_ids:
  - expression
  - runner
  - authority-reuse
- assessment_id: ownership
  area: ownership
  topic: 'Native checklist: current text ownership and maintained recurrence'
  outcome: supported
  target_ids:
  - traitmech:000012
  summary: The current record owns the source-scope, quoted-note and node-1 wording
    concerns. Bounded searches do not identify an exact generating assignment for
    those textual defects. Maintained finalizer/proposal retention and existing-value
    mapping guards explain the supported identity and preserved annotations; no speculative
    shared-writer repair is required.
  evidence_ids:
  - owners
  - identity
  - provenance
  - retention-authority
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: REVIEWED status and local acceptance attribution'
  outcome: concern
  target_ids:
  - traitmech:000012
  summary: Nine explicit AI events document proposal, curation and prior corrections.
    Ignored-inclusive bounded searches do not attribute a human acceptance decision
    for this current target. Positive maintenance and upstream creator attribution
    are preserved; remote or private decisions remain unknown.
  evidence_ids:
  - provenance
  - record
  - native-policy
- assessment_id: checks
  area: schema
  topic: 'Native checklist: required focused checks and scoped historical reuse'
  outcome: supported
  target_ids:
  - traitmech:000012
  summary: Focused record, strict and snippet checks passed. The manual source assessment
    resolves the abstract-only snippet miss. Reused B6 QC and earlier common diagnostics
    retain original times, OLD product failures and successful retry, adapter skips
    and B3 history scope. No new native corpus execution or scientific mutation is
    claimed.
  evidence_ids:
  - check-metal-validate
  - check-metal-strict
  - check-metal-snippets
  - check-batch006-qc
  - reuse
  - reuse-supplement
findings:
- finding_id: zinc-prevalence-scope
  issue_key: metal-tolerant-zinc-prevalence-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: A zinc-specific prevalence statement is generalized to heavy metals
  description: Edge 7 states that the named three transporter families mediate heavy-metal
    resistance in most bacteria. Its quoted source passage on printed page 55 explicitly
    concerns zinc. Page 53 supplies positive broad active-efflux context, and Nies
    supports the family-level background, but neither inspected passage establishes
    the exact expanded named-family prevalence statement. This is a nearest-source
    attribution overreach, not a denial that these families have other metal roles
    or a universal defect inferred from generic graph nodes.
  target_ids:
  - traitmech:000012
  field_paths:
  - causal_graphs[0].edges[7].description
  - causal_graphs[0].edges[7].evidence[0].notes
  evidence_ids:
  - jmmg-primary
  - nies-primary
  - placements
  - snippets
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/metal_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: quoted-context-precision
  issue_key: metal-tolerant-quoted-context-precision
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Two quoted notes need literal wording and context distinguished
  description: Edge 3 places quotation marks around a meaning-supported paraphrase
    rather than a contiguous source excerpt. Edge 5 quotes a literal cooperation prefix
    whose immediate context combines reduction with methylation; separate discussion
    supports the represented reduction/efflux background. Preserve that positive background
    and the study’s inferred community evidence tier. This grouped documentary concern
    does not declare the underlying existing biology false.
  target_ids:
  - traitmech:000012
  field_paths:
  - causal_graphs[0].edges[3].evidence[0].notes
  - causal_graphs[0].edges[5].evidence[0].notes
  evidence_ids:
  - snippets
  - jmmg-primary
  - peerj-primary
  - placements
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/metal_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: ion-condition-facet
  issue_key: metal-tolerant-ion-condition-facet
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: The challenge node mixes ion identity with an excess condition
  description: Node 1 labels a toxic heavy-metal ion, is typed ENVIRONMENTAL_FACTOR,
    and describes cytoplasmic excess. Those phrases leave unclear whether it represents
    a material ion, an exposure condition or the existing intracellular excess condition.
    Native environmental factors can represent conditions, so this is bounded referent
    precision rather than an automatic chemical-type error. Clarify the intended current
    meaning without imposing a retype, adding a new mechanism or expanding the trait
    scope.
  target_ids:
  - traitmech:000012
  field_paths:
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].node_type
  - causal_graphs[0].nodes[1].description
  evidence_ids:
  - record
  - native-types
  - node-edges
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/metal_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: metal-tolerant-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Local provenance does not attribute human scientific acceptance
  description: The REVIEWED record has nine explicit AI maintenance events. The inspected
    ignored-inclusive local provenance does not identify a human acceptance decision
    covering this current target. Maintenance history and explicit duplicate retention
    are positive provenance, but do not establish that acceptance. Private or remote
    review remains unassessed; this is not a claim that no human review ever occurred.
  target_ids:
  - traitmech:000012
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - record
  - native-policy
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/metal_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: bound-prevalence-attribution
  description: Align the existing prevalence attribution with its inspected source
    scope.
  finding_ids:
  - zinc-prevalence-scope
  target_ids:
  - traitmech:000012
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/metal_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain the cited substrate scope or supply independently inspected support for
    the exact current breadth; acknowledge the positive general efflux and exporter-family
    context.
  - Do not turn this documentary correction into a new biological route, experiment
    or intervention.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation and source checks, maintained QC and generated-output
    recipes. This review changes no scientific input.
- action_id: clarify-quoted-evidence
  description: Separate paraphrase, literal wording and the immediate cooperation
    context.
  finding_ids:
  - quoted-context-precision
  target_ids:
  - traitmech:000012
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/metal_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Use verifiable literal wording or clearly marked interpretive prose for edge 3.
    Distinguish edge 5 quoted cooperation context from its separate positive background
    support.
  - Preserve the community inference evidence tier without inventing a required individual-protein
    assay or altering the mechanism.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation and source checks, maintained QC and generated-output
    recipes. This review changes no scientific input.
- action_id: clarify-challenge-referent
  description: Make node 1 consistently denote its intended existing referent.
  finding_ids:
  - ion-condition-facet
  target_ids:
  - traitmech:000012
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/metal_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Label, type, description and incident challenge wording agree on the chosen existing
    material or condition meaning.
  - Do not force CHEMICAL solely from the label, invent a new exposure condition or
    redefine the whole trait from a contextual cation node.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation and source checks, maintained QC and generated-output
    recipes. This review changes no scientific input.
- action_id: attribute-human-acceptance
  description: Link existing human acceptance or leave acceptance unresolved for the
    curator.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - traitmech:000012
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/metal_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies the reviewed revision and scope, including source limits
    and unassessed incidental details. Retain all nine AI events.
  - Automated validation and this AI review do not substitute for human scientific
    acceptance; remote/private decisions are not presumed absent.
limitations:
- Active METPO1007074 is a real overlap, explicitly retained against local 000012;
  proposed v5 1007611 and local properties remain provisional. No false absence claim,
  automatic migration or synonym upgrade follows.
- GO0030001 is a biological transport process with export as a narrow synonym. The
  record supplies direction in its own wording and does not assert exact equivalence;
  no separate finding is assigned for that precision limit.
- Nies was inspected at indexed-abstract scope. Failed body access and unusable search-indexed
  leads do not establish body absence. Broad family support is positive; exact aggregate
  compartment and dominance details remain bounded.
- JMMG page 53 positively supports broad active-efflux background. The material finding
  is the exact named-family most-bacteria attribution on page 55, whose zinc qualifier
  is lost; it does not deny other metal roles.
- BS1 and CH34 results remain strain-scoped. Canonical CH34 and plasmid-borne determinants
  are supported without claiming every determinant is plasmid-borne or every strain
  has equal resistance.
- PeerJ distinguishes community functional-potential inference from its literature
  background. The existing reduction/efflux background is positive, while the cooperation
  quotation has a different immediate combined context; no mandatory protein assay
  is inferred.
- Generic NONMECHANISTIC context, two components and three label-only classes do not
  require token accessions, new biological links or an assembled complex. The former
  operon node, retired accession and trait-object RO assignment are historical corrections,
  not present defects.
- Incidental pathogen-specific and engineered fitness details in acquired sources
  remain UNASSESSED_SCOPE. Acquisition of full files does not imply validation of
  every detailed mechanism; no new target, pathway, experiment, exposure condition
  or optimization is supplied.
- Catalog and structured-runner observations retain original times and bounded discovery
  scope. There is no matching canonical organism dataset; absent coverage is not negative
  phenotype evidence.
- Publication status is limited to inspected indexed/registry fields and the publisher
  landing page. Failed accesses, original body acquisitions, later copying, independent
  passage reads and final interpretation remain distinct.
- Nine AI events and bounded ignored-inclusive local searches do not attribute human
  acceptance. Positive maintenance remains intact; private or remote acceptance is
  unknown. The historical provider report was a lead/limited provenance input, not
  fully read scientific evidence.
- B6 QC, B4 protein audit, B3 history validation and OLD product failures/retry retain
  original execution dates and scopes. The qualified history proof separates 1,277
  YAML records from 1,278 total files. No fresh corpus execution or environment, repository,
  Git or state mutation occurred in this builder preparation.
notes:
- 'Four findings: one major and three minor. Field indices are zero-based. The native
  needs_changes judgment is normalized to structured verdict needs_curation.'
- All 59 capture hashes match. Coverage includes five works, fourteen placements,
  two snippet fields, three quoted notes, nine nodes, eight edges, two components,
  three label-only proteins, zero instances and nine explicit AI events.
- Source observations completed at 12:03:53.047913 UTC and severity qualified at 12:04:22.441455
  UTC. Grounding completed at 12:03:06.449556 UTC; parent adjudication at 12:07:31.019853
  UTC. Primary acquisition times remain separate.
tags:
- record-review
- metal-tolerant
- environment
- needs-curation
native_verdict: needs_changes
```
