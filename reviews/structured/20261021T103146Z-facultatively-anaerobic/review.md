# Whole-record review of facultative anaerobiosis: documentary support and representation

- Review: 20261021T103146Z-facultatively-anaerobic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T10:24:38Z
- Finished UTC: 2026-10-21T10:31:46Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Active METPO identity,broader parent,generic definition,both canonical classifications and current node identities are supported. One major groups two imported RO role conflicts;two minor findings concern the fixed predicate wordform and unlinked local human acceptance. Nine references resolve to nine publications across thirteen placements. Five of six quotations are exact and one remains unverified. All eight detailed biological edge claims remain UNASSESSED_SCOPE;no mechanism is validated or repaired.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: One entire maintained TraitRecord, fully read before native capture. All identity, model, example, evidence, graph and history fields are inventoried, including eight nodes, eight edges, two canonical examples and seven history events. Source identity, quotation fidelity, generic classification, formal ontology roles and provenance are reviewed. All eight detailed biological edge claims are UNASSESSED_SCOPE; no pathogen fitness or respiration mechanism is validated, reconstructed or improved. The parent, authorities, mappings, writers and historical research report are context rather than additional targets.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000605 | data/traits/environment/facultatively_anaerobic.yaml | maintained | facultatively anaerobic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000605 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000605 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000605 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1000605 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000605 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000605 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000605 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1000605 | Passed 10:25:14–15Z. Native structural success does not certify external predicate semantics or detailed biology. |
| Focused strict validation | passed | True | METPO:1000605 | Passed 10:25:14–16Z. External-role findings are independent of the maintained structural checks. |
| Focused abstract snippet verification | passed | True | METPO:1000605 | Passed 10:25:18–24Z: five snippets over three references, two VERIFIED and three NOT_IN_ABSTRACT. The URL-based definition snippet was outside this native command. Manual documentary inspection separately verifies five of all six snippets; the remaining quotation is unknown, not false. |
| Reused full-corpus QC | passed | True | METPO:1000605 | B5 actual execution 10:21:03–10:23:38Z passed. B6 byte comparisons cover scientific and common inputs, with a separately recorded ready environment. This is reuse of B5 diagnostics, not a fresh B6 QC execution; warnings, baselines and original scope remain. |
| Focused protein/taxon audit applicability | not_applicable | False | METPO:1000605 | NONMECHANISTIC graph has two explicit REVIEWED_LABEL_ONLY protein nodes and zero instances. No new accession or mandatory anchor is justified. Detailed organism mechanisms remain unassessed. |
| UniProt instance audit applicability | not_applicable | False | METPO:1000605 | No UniProt instance or accession is asserted; no instance-specific audit is applicable. Reviewed label-only nodes are permitted by native policy. |

## Scientific And Domain Assessments

### Native checklist: ID,label,synonyms,polarity and term kind

identity: supported. Targets: METPO:1000605.

Active exact METPO1000605 denotes a positive environmental CLASS. Related synonyms are correctly scoped;facultative is shared vocabulary rather than a unique exact class identity. O₂/O2 differs only typographically. Current active identity is not replaced with a similar or obsolete term.

### Native checklist: growth with or without oxygen

evidence: supported. Targets: METPO:1000605.

The pinned definition matches the current concept. The actual indexed NBK482349 chapter excerpt positively supports the generic oxygen-presence/absence growth distinction. The chapter URL is linked through its actual PMID metadata;browser challenges do not supply body evidence.

### Native checklist: strictly broader parent and source semantics

identity: supported. Targets: METPO:1000605.

Direct parentMETPO1000601 oxygen preference is strictly broader and exact in the pinned source. Obsolete replacement annotations are used only where actually present. No fallback identifier,opposite-parent or xref-equivalence finding is established.

### Native checklist: category,term kind,graph scope and optional fields

representation: supported. Targets: METPO:1000605.

ENVIRONMENT,CLASS and NONMECHANISTIC scope fit the broad phenotype. Current protein nodes carry legitimate reviewed-label-only explanations;zero instances require no token accession. Process operation and chemical aggregates are not automatically wrong node kinds. Empty optional slots are not defects by themselves.

### Native checklist: both canonical identities and nearest classification support

evidence: supported. Targets: METPO:1000605.

Official NCBI562 and1280 species identities match. PMID7747938 abstract supports the existing general E.coli classification and growth-mode note. PMID24628867 describes S.aureus DSM20231T as known to be facultatively anaerobic;this supports the exemplar without inferring a newly measured assay or all-strain uniformity. Both nearest sources were checked separately from the definition source.

### Native checklist: all eight represented node identities and kinds

grounding: supported. Targets: METPO:1000605.

The current GO grounds are active biological processes;CHEBI15379 is dioxygen. Label-only protein and ungrounded chemical aggregate representations are permitted. No unsupported token ground,instance or forced pathway/component conversion is required. Biological descriptions are not certified by identity agreement.

causal_graphs[0].nodes[0]: supported_identity; biological mechanism UNASSESSED_SCOPE.
causal_graphs[0].nodes[1]: supported_chemical_identity; biological mechanism UNASSESSED_SCOPE.
causal_graphs[0].nodes[2]: supported_process_identity; biological mechanism UNASSESSED_SCOPE.
causal_graphs[0].nodes[3]: supported_process_identity; biological mechanism UNASSESSED_SCOPE.
causal_graphs[0].nodes[4]: permitted_label_only_protein; biological mechanism UNASSESSED_SCOPE.
causal_graphs[0].nodes[5]: permitted_label_only_protein; biological mechanism UNASSESSED_SCOPE.
causal_graphs[0].nodes[6]: permitted_chemical_aggregate; biological mechanism UNASSESSED_SCOPE.
causal_graphs[0].nodes[7]: permitted_process; biological mechanism UNASSESSED_SCOPE.

### Native checklist: asserted predicate roles across all eight edges

consistency: concern. Targets: METPO:1000605.

Edges0/1 import two incompatible RO meanings:executor versus available-input wording,and process-only regulation versus material endpoints. Six other edges assert no predicate_id and inherit no invented RO constraints. The edge6 wordform is a separate repository vocabulary convention. Native structural acceptance does not adjudicate these semantic distinctions.

causal_graphs[0].edges[0]: major_external_executor_role_mismatch; detailed biology UNASSESSED_SCOPE.
causal_graphs[0].edges[1]: major_external_process_role_mismatch; detailed biology UNASSESSED_SCOPE.
causal_graphs[0].edges[2]: free_text_no_asserted_external_constraint; detailed biology UNASSESSED_SCOPE.
causal_graphs[0].edges[3]: free_text_no_asserted_external_constraint; detailed biology UNASSESSED_SCOPE.
causal_graphs[0].edges[4]: free_text_no_asserted_external_constraint; detailed biology UNASSESSED_SCOPE.
causal_graphs[0].edges[5]: free_text_no_asserted_external_constraint; detailed biology UNASSESSED_SCOPE.
causal_graphs[0].edges[6]: free_text_no_asserted_external_constraint; detailed biology UNASSESSED_SCOPE.
causal_graphs[0].edges[7]: free_text_no_asserted_external_constraint; detailed biology UNASSESSED_SCOPE.

### Native checklist: each detailed biological edge claim

evidence: unknown. Targets: METPO:1000605.

All eight detailed biological claims,including source-specific direction,sufficiency,necessity and mechanistic notes,remain UNASSESSED_SCOPE. Neither literal quotation matches nor formal role compatibility validate them. The review supplies no missing steps,replacement mechanism,organism intervention or optimization.

causal_graphs[0].edges[0]: citation identity verified; quotation=VERIFIED_EXACT; biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.
causal_graphs[0].edges[1]: citation identity verified; quotation=UNVERIFIED; biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.
causal_graphs[0].edges[2]: citation identity verified; quotation=VERIFIED_EXACT; biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.
causal_graphs[0].edges[3]: citation identity verified; quotation=VERIFIED_EXACT; biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.
causal_graphs[0].edges[4]: citation identity verified; quotation=NOT_APPLICABLE_NO_SNIPPET_FIELD; biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.
causal_graphs[0].edges[5]: citation identity verified; quotation=NOT_APPLICABLE_NO_SNIPPET_FIELD; biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.
causal_graphs[0].edges[6]: citation identity verified; quotation=NOT_APPLICABLE_NO_SNIPPET_FIELD; biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.
causal_graphs[0].edges[7]: citation identity verified; quotation=NOT_APPLICABLE_NO_SNIPPET_FIELD; biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.

### Native checklist: nine identities and thirteen citation placements

evidence: supported. Targets: METPO:1000605.

All nine literal references resolve to nine distinct publications. PMID7747938/DOIbf00871629 is not an alias of graph PMID1854188/DOIbf00445650. NBK482349 identity is linked to its indexed chapter. The2025DOI remains a preprint in inspected metadata;no later-version or peer-review assertion is made.

### Native checklist: six snippets and their exact inspected surfaces

evidence: unknown. Targets: METPO:1000605.

Five snippets are exact:definition excerpt,generic E.coli introductory body,title text,and two abstract passages. One assigned phrase remains unverified in an unseen body,not demonstrated nonliteral. Notes without snippet fields remain interpretation rather than quotations. Native abstract output is retained separately from manual follow-up.

### Native checklist: whole-record coverage and explicit unresolved scope

completeness: supported. Targets: METPO:1000605.

All present fields,eight nodes,eight edges,two examples,nine references,thirteen placements,six snippets and seven history events are accounted for. Full field coverage is distinct from complete biological validation or full-body reading. The historical research report is captured context,not independent primary evidence. No placeholder discussion,dataset,protein or mechanism is added.

### Native checklist: structured catalog applicability

evidence: supported. Targets: METPO:1000605.

Both canonical species are represented in the retained20-organism28-dataset catalog. Dataset membership is documentary context only;strain coverage is not generalized. No gene,module,fitness or respiratory query was conducted. Historical runner discovery is explicitly bounded and not a fresh B6/global absence claim.

### Native checklist: maintained owner recurrence and bounded fixes

ownership: concern. Targets: METPO:1000605.

Predicate table rows9/11 and the guarded grounding writer can restore the incompatible assignments after ID-only clearing. Preserve valid node grounds. A wordform-only edge6 edit must not silently create an external predicate assertion. Actions are confined to existing representation and provenance rather than scientific mechanism completion.

### Native checklist: REVIEWED status and local acceptance linkage

provenance: concern. Targets: METPO:1000605.

Seven per-record events disclose six AI-assisted changes plus automated seeding. Ignored-inclusive local target and graph/node searches found no explicit human scientific-acceptance link or target repository-history artifact. This is a bounded documentation concern;remote/private acceptance remains unknown.

### Native checklist: focused execution and historical reuse

schema: supported. Targets: METPO:1000605.

Focused validation,strict validation and snippet commands passed with their actual outputs. B5 QC passed10:21:03–10:23:38;B6 unchanged inputs and readiness are documented without claiming fresh execution. B3 history and OLD product failure/retry/skips retain original bounds. No required executed check is unavailable;unassessed biology is explicitly separate.

## Findings

### external-predicate-roles: Two imported RO meanings conflict with the represented roles

major / open / confirmed; issue key: facultatively-anaerobic-external-predicate-roles.

Edge0 uses RO0002327 while its own wording describes available input rather than an entity executing the process. Its material/process categories are compatible;the conflict is the additional capability/execution meaning,not a categorical chemical exclusion. Edge1 uses RO0002211,whose domain and range are processes,with a CHEMICAL subject and GENE_OR_PROTEIN object. These grouped semantic mismatches concern asserted identifiers and existing representation,not demonstrated false biology or a native reasoner failure. Broad maintained mapping gates can recreate the IDs after clearing.

### predicate-wordform: One predicate label differs from the fixed repository wordform

minor / open / confirmed; issue key: facultatively-anaerobic-predicate-wordform.

Edge6 has free-text predicate enable. That form can be grammatical with its plural surface subject,but CURATION_PLAYBOOK explicitly fixes predicate labels to third-person singular and gives enables rather than enable as its example. This is a vocabulary normalization inconsistency only. No predicate_id is present here,so this finding does not import the RO executor criticism from edge0 or adjudicate the biological claim.

### human-acceptance-link: Human scientific acceptance is not linked in the inspected local provenance

minor / open / confirmed; issue key: facultatively-anaerobic-human-acceptance-link.

The current mapping status is REVIEWED,while seven history events disclose six AI-assisted changes and one automated seed. The declared ignored-inclusive target and graph/node searches found no explicit target human scientific-acceptance link in local history or review targets. Native policy requires human sign-off for REVIEWED. This is a bounded provenance gap,not proof that no human reviewed the record privately or remotely,and does not make the definition or examples false.

## Recommended Actions And Acceptance Checks

### reconcile-external-relation-roles

Reconcile the two existing external predicate assignments with their represented roles and maintained mapping owners.

- Any retained identifier agrees with both endpoint kinds and its textual role;preserve valid material/process identities instead of retyping them solely to retain a process-only relation.
- Address mapping recurrence together with the record;no compulsory replacement CURIE,new causal step or mechanistic completion is prescribed.
- Keep all eight detailed biological claims unassessed within this documentary review;formal correction does not certify pathogen fitness or respiration biology.
- Any separately authorized change uses guarded writes and append-only record/repository history,focused native validation and maintained relevant audits/QC;regenerate affected outputs with existing recipes. This review performs no such mutation.

### normalize-predicate-label

Apply the documented canonical predicate wordform to the existing free-text label.

- The edge6 label follows the fixed third-person-singular vocabulary convention while preserving its existing scientific content.
- The normalization alone does not create a predicate_id or import an external executor meaning;inspect maintained writer recurrence before subsequent automated grounding.
- No new mechanism,endpoint,condition or organism-specific assertion is introduced.
- Any separately authorized change uses guarded writes and append-only record/repository history,focused native validation and maintained relevant audits/QC;regenerate affected outputs with existing recipes. This review performs no such mutation.

### link-human-acceptance

Link existing human scientific acceptance or obtain it through the established review process.

- The acceptance record identifies the reviewed revision and actual scientific scope,including the one unverified quotation and all eight biological claims unassessed here.
- Preserve AI disclosure and append-only provenance. Automated validation,this agent review and inherited ontology metadata are not substitutes for human scientific acceptance;reassess status if required.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-006.nq5qngor/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-facultatively-anaerobic-validate | /private/tmp/traitmech-record-sweep-006.nq5qngor/facultatively-anaerobic-validate.log; Executed 2026-10-21T10:25:14Z through 2026-10-21T10:25:15Z; metadata facultatively-anaerobic-validate.json | context_only | Passed 10:25:14–15Z. Native structural success does not certify external predicate semantics or detailed biology. |
| check-facultatively-anaerobic-strict | /private/tmp/traitmech-record-sweep-006.nq5qngor/facultatively-anaerobic-strict.log; Executed 2026-10-21T10:25:14Z through 2026-10-21T10:25:16Z; metadata facultatively-anaerobic-strict.json | context_only | Passed 10:25:14–16Z. External-role findings are independent of the maintained structural checks. |
| check-facultatively-anaerobic-snippets | /private/tmp/traitmech-record-sweep-006.nq5qngor/facultatively-anaerobic-snippets.log; Executed 2026-10-21T10:25:18Z through 2026-10-21T10:25:24Z; metadata facultatively-anaerobic-snippets.json | context_only | Passed 10:25:18–24Z: five snippets over three references, two VERIFIED and three NOT_IN_ABSTRACT. The URL-based definition snippet was outside this native command. Manual documentary inspection separately verifies five of all six snippets; the remaining quotation is unknown, not false. |
| check-batch005-qc | /private/tmp/traitmech-record-sweep-005.klfwsp1f/batch005-qc.log; Executed 2026-10-21T10:21:03Z through 2026-10-21T10:23:38Z; metadata batch005-qc.json | context_only | B5 actual execution 10:21:03–10:23:38Z passed. B6 byte comparisons cover scientific and common inputs, with a separately recorded ready environment. This is reuse of B5 diagnostics, not a fresh B6 QC execution; warnings, baselines and original scope remain. |
| reuse | B6 scientific and common-input comparison; Original verification 10:14:46.298715Z;1130 traits,1278 history files and19 common inputs | supports | The original receipt correctly named B4 QC as latest at its own timestamp. The separate later supplement records actual B5 QC. The f25-to8eee delta has only seven workflow,skill and infrastructure-history additions; original execution dates, product failures, retry and adapter skips remain. |
| reuse-independent | Independent common-check and environment review; B5 QC10:21:03–10:23:38;contract4passed;nativecheck102valid;19common and59target inputs rehashed | supports | Later B5 check metadata and logs are hash-recorded. B6 readiness records its own locked dev environment but is not a B6 QC result.1278 history files and1277 history records validated in B3 are distinct counts. |
| capture | Native selected-record capture; 59 inputs;10:24:38–39Z following full record read | supports | Target, parent, policies, ontology snapshots, mappings, writers and historical provider report were captured before assessment. No target-specific history was discovered that requires supplemental capture. |
| record | data/traits/environment/facultatively_anaerobic.yaml; Entire record;8nodes,8edges,2examples,2label-only protein nodes,0instances,7history events | partial | Active environmental CLASS with REVIEWED status and NONMECHANISTIC scope. Six events disclose AI assistance and one is automated seeding. Complete field inspection does not establish detailed biological correctness. |
| native-policy | Native field-by-field review checklist; Evidence standard and Status/audit row;grounding-agent actual read10:26:57.013274Z,independently reread during builder preparation | supports | Definition, example and edge support are distinct; optional fields need no token additions. Predictions and association do not establish mechanisms. REVIEWED requires human sign-off and explicit AI assistance and unresolved gaps. |
| predicate-label-policy | Repository predicate vocabulary convention; docs/CURATION_PLAYBOOK.md:641–644;exact read/hash receipt10:29:31.233122Z | supports | The fixed predicate-label convention explicitly requires third-person singular, using enables rather than enable. This convention is distinct from grammatical agreement with a plural surface label and imposes no external RO identifier. |
| identity | Pinned METPO active/deprecated term and synonym scan; METPO1000605 and broader oxygen-preference parent1000601;complete label/synonym declaration scan | supports | Active exact label,related synonyms and direct parent agree. O₂/O2 is harmless typography. The related synonym facultative is shared and is not an exclusive exact identity. Actual obsolete replacement annotations are retained; none is invented for obsolete1000116. |
| local-authority | Maintained schema,grounding mappings and writers; Eight local policy/writer excerpts at10:26:57.010492–10:26:57.013712Z | supports | The process and chemical categories and reviewed-label-only protein treatment are permitted. Current node mappings match official identities. Broad predicate gates and populated-ID skips explain recurrence without making external roles valid. |
| official-identities | Official GO,ChEBI and NCBI identity responses; GO0009060/GO0009061 biological_process;CHEBI15379 dioxygen;NCBI562/1280 species | supports | The asserted process and chemical identities and both canonical species labels match the retained official responses. This verifies identity and aspect/rank only; detailed physiological mechanism remains unassessed. |
| authority-reuse | Hash-verified official response reuse; Original GO9060,ChEBI15379,NCBI56209:57:47;GO9061 08:46:57–58;NCBI1280 07:14:56–57 | supports | All five saved response copies preserve the original SHA256 and acquisition times. Copy verification at10:26:57Z is not a new network request; unrelated taxa in paired payloads are outside assessment. |
| ro | Cached RO definitions and recursive domain/range statements; Original authority read09:52:45.989262Z;DB SHA849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb;reuse10:26:57 | supports | RO2327 requires capability and actual execution; compatible material/process categories alone do not establish that role. RO2211 requires process endpoints. These external meanings do not imply a native validator or reasoner failure; no RO meaning is attached to the six free-text-only edges. |
| grounding-ledger | Complete documentary grounding assessment; All8nodes and8edges;59captured inputs unchanged | partial | One grouped major concerns the two imported predicate roles. Canonical and node identities are valid. Every detailed biological claim remains UNASSESSED_SCOPE; no missing optional accession, pathway or mechanism step is inferred. |
| node-edges | Complete node and edge role ledger; nodes[0–7],edges[0–7],zero-based;8biological correctness assessments UNASSESSED_SCOPE | partial | All represented kinds and asserted ontology roles are inventoried. Process operation is not forced to a physical component or pathway. Free-text edges are distinguished from the two asserted external predicates. |
| captured-hashes | Final grounding input receipt; 59/59native input SHA256 values match at10:26:57.086574Z | supports | All scientific inputs and contextual artifacts captured for this single target remain the same bytes. This is integrity evidence rather than biological validation. |
| owners | Maintained mapping and writer recurrence assessment; Predicate rows9/11;writerlines138–179;node rows2/20/21 | supports | Broad enables/regulates mapping rows can restore inappropriate predicate IDs after ID-only removal. Node identities are valid. Canonical-label normalization of free-text edge6 must not silently add the RO2327 assignment. |
| provenance | Bounded local human-acceptance linkage search; 192matching files;7events6AI+seed;no target repository history or targeted review bundle | partial | The inspected local evidence links no target-specific human scientific acceptance. Automated validation,AI history and seeding do not supply it. This does not establish absence of private or remote review. |
| graph-owner-search | Supplemental graph/node provenance search; Exact graph andnode keys;10:26:00.732965Z;exit1no matches | partial | A bounded ignored-inclusive graph/node search found no additional target history or writer. This does not imply no general grounding writer exists; general owners are independently identified. |
| expression | https://imodulondb.org/api/datasets; Original07:36:12.732638–07:36:12.858149Z;20organisms28datasets;hash-verified10:26:57reuse | context_only | Both canonical species have catalog entries: E.coli5datasets and S.aureus2datasets. Membership does not verify this record or every strain. Detailed gene/module/fitness queries were deliberately not assessed; no data-absence or negative-phenotype inference follows. |
| runner | Historical bounded structured-runner discovery; OriginalB5PATH/project search09:27:57.380287–09:27:57.542053Z;older external bounds08:17:15 | context_only | The runner search receipt is hash-verified historical reuse, not new B6 discovery. Its bounded no-runner result is not global absence. Catalog membership was checked separately; no downstream mechanism query was performed. |
| source-ledger | Complete documentary source assessment; 9references9publications13placements6snippets;final10:28:26.412575Z | partial | All identities resolve; generic definition and both canonical classifications are positively supported. Five quotations are exact and one remains unknown. All eight detailed edge claims remain UNASSESSED_SCOPE. Source genre alone establishes no false-citation finding. |
| bibliography | Every cited publication and placement; source0–source8;each identity,original metadata receipt,scope and nearest placement retained | supports | PMID7747938 resolves to DOI10.1007/bf00871629 and is distinct from graph DOI10.1007/BF00445650,PMID1854188. NBK482349 corresponds to PMID29493974. The DOI10.1101 preprint remains a preprint,not an assumed peer-reviewed journal publication. |
| placements | Complete citation inventory; 13placements:definition_source,2top evidence,2canonical examples and8edges | supports | Nearest citation placement is preserved; positive classification support is not transferred to unassessed graph mechanisms. Notes without snippet fields are not counted as quotations. |
| snippets | Literal quotation checks across inspected primary surfaces; 6snippets:5exact at chapter excerpt,introduction,title or abstracts;1unknown | partial | Exact wording is distinct from biological correctness. The CMI quotation is exact title text. The one unknown assigned phrase was not found in the inspected abstract; inaccessible body text is not presumed absent. |
| edge-source-scope | Complete documentary edge-source ledger; edges[0–7];8/8biological_correctness and claim_support UNASSESSED_SCOPE | context_only | Citation identity and declared quotation status are inventoried for every edge. No detailed pathogen fitness,respiration,regulatory or engineering mechanism was validated,completed or repaired. |
| classification-excerpts | Bounded generic classification passages; PMC9075585 Introduction/sec1-1 bodyparagraph4;PMC3985588 Methods/sec5/Straininformation/sec6 bodyparagraph2 | supports | The first supplies the existing generic E.coli quotation. The second describes DSM20231T as known to be facultatively anaerobic. The S.aureus exemplar has descriptive classification support;no new direct growth assay,genome-derived causation or species-wide strain uniformity is claimed. |
| metadata-source0 | DOI:10.1093/femsre/fuac008; Original indexed identity retrieval; E. coli vertebrate-gut ecology review | supports | Publication identity and explicitly declared source type only; detailed mechanisms remain unassessed. Complete XML available;only assigned quotation and generic introductory classification adopted. |
| body-source0 | DOI:10.1093/femsre/fuac008; PMC9075585 Introduction/sec1-1 (Escherichia coli: a versatile organism),body paragraph4 zero-based | supports | Exact assigned quotation and generic oxygen-preference classification. Only this bounded classification/quotation passage was inspected;availability of a complete file is not full biological-body review. |
| metadata-source1 | PMID:7747938; Original indexed identity retrieval; Broad bacterial oxygen-regulation review | supports | Publication identity and explicitly declared source type only; detailed mechanisms remain unassessed. Indexed abstract only;detailed regulatory programs and source mechanisms unassessed. |
| metadata-source2 | PMID:24628867; Original indexed identity retrieval; S. aureus subsp. aureus type-strain genome publication | supports | Publication identity and explicitly declared source type only; detailed mechanisms remain unassessed. Complete XML available but read only bounded classification;adjacent protocols,virulence/resistance and genome mechanisms unassessed. |
| body-source2 | PMID:24628867; PMC3985588 Methods/sec5 &gt; Strain information/sec6,body paragraph2 zero-based,second sentence | supports | Strain DSM20231T is described as known to have the phenotype. This is descriptive classification support,not a new direct growth assay or genome-derived causal proof. Adjacent procedures/pathogen characteristics unassessed. Only this bounded classification/quotation passage was inspected;availability of a complete file is not full biological-body review. |
| metadata-source3 | DOI:10.1111/cmi.13338; Original indexed identity retrieval; Facultative-anaerobe infection-context review | supports | Publication identity and explicitly declared source type only; detailed mechanisms remain unassessed. No complete body obtained;title fidelity does not validate biological edge support,fitness or infection mechanisms. |
| metadata-source4 | DOI:10.1007/BF00445650; Original indexed identity retrieval; E. coli oxygen-regulation review | supports | Publication identity and explicitly declared source type only; detailed mechanisms remain unassessed. No complete body obtained;absent abstract wording does not prove absence from unseen body. All detailed edge biology unassessed. |
| metadata-source5 | DOI:10.1101/2025.01.08.631794; Original indexed identity retrieval; E. coli trace-metal/electron-acceptor preprint | supports | Publication identity and explicitly declared source type only; detailed mechanisms remain unassessed. Metadata identity/context only;no complete body or independent peer-review/version-history determination. Detailed biological claims unassessed. |
| metadata-source6 | DOI:10.1128/mbio.01448-23; Original indexed identity retrieval; Bacteremia-context regulatory primary publication | supports | Publication identity and explicitly declared source type only; detailed mechanisms remain unassessed. No complete body obtained;no source-claim correctness or host-fitness mechanism adjudication. |
| metadata-source7 | DOI:10.1038/s41467-024-51029-x; Original indexed identity retrieval; Biochemical-engineering publication | supports | Publication identity and explicitly declared source type only; detailed mechanisms remain unassessed. No complete body obtained;engineering,respiratory-module claims and all detailed mechanisms unassessed. No corrective design or optimization. |
| metadata-source8 | https://www.ncbi.nlm.nih.gov/books/NBK482349/; Original indexed identity retrieval; StatPearls Anaerobic Infections chapter,NBK482349 | supports | Publication identity and explicitly declared source type only; detailed mechanisms remain unassessed. Indexed chapter excerpt only;browser attempts returned challenge/footer. No full chapter inspected. Clinical and pathogen mechanisms unassessed. |
| source-access | Actual successful classification XML acquisitions; E.coli10:26:40.348094–10:26:41.811484Z;S.aureus10:26:40.348624–10:26:41.431844Z | supports | Two actual XML responses succeeded and retain their SHA256. Only generic classification and assigned quotation passages were inspected;adjacent procedures and mechanisms are outside scope. |
| source-access-failure | Retained initial sandbox DNS failures; 10:26:30.592226–10:26:30.605773Z | context_only | Initial DNS failures were superseded by successful XML retrieval. These failed attempts are retained as access history and provide no article-absence evidence. |
| browser-access | Retained primary browser access attempts; 10:25:09–10:25:24Z;Bookshelf challenge and PubMed footer only | context_only | Browser pages supplied no chapter text. The later actual indexed chapter excerpt supports the definition. Search result leads and challenge/footer surfaces were not treated as primary passages;receipt hash is not a saved HTML-body hash. |
| source-copy-reuse | Original source metadata copy/hash chain; Original root metadata10:25:32.046098–10:25:34.827996Z;definition10:25:48.391372–10:25:49.025576Z | supports | Source-agent copies preserve the original response bytes and acquisition bounds;copy and final assessment times are not relabelled as network retrieval. |

## Limits And Additional Notes

- All eight detailed biological edge claims remain UNASSESSED_SCOPE. Source identity,quotation fidelity,formal roles and generic classification do not validate pathogen fitness,respiration,regulatory or engineering mechanisms. No target,step,condition,replacement mechanism or optimization is proposed.
- Two complete XML files were available,but only the assigned generic classification/quotation passages were inspected. Other sources were indexed title,abstract,chapter-excerpt or metadata surfaces;availability is not full-body review.
- One assigned graph quotation remains unverified because its actual body was not obtained. Abstract nonmatch is inconclusive. The CMI phrase is exact title text,which establishes literal fidelity rather than edge support.
- The canonical S.aureus source reports DSM20231T as known to have the phenotype. No newly measured oxygen-growth assay,genome-derived causation or all-strain uniformity is inferred. The E.coli canonical review and graph review are distinct publications.
- The DOI10.1101/2025.01.08.631794 source is explicitly a preprint in inspected metadata. No journal peer-review status or later-version search is claimed. An engineering or infection-focused title alone does not establish wrong citation.
- The generic definition is supported by an actual indexed chapter excerpt linked to NBK482349. Failed browser challenges and footer-only pages were not article text;the original failures remain retained.
- External RO meanings come from a hash-identified cached authority,with original09:52read and B6reuse times distinguished. GO,ChEBI and NCBI responses retain their original07:14,08:46 and09:57 acquisition bounds;no new ontology-release certification is implied.
- Common diagnostics,B3 history and actual B5 QC are reused within recorded byte-equality scope,with original dates,failed product attempts,network retry and no-adapter skips. B6 environment readiness is separate from a fresh execution. Native success does not certify all source or biological claims.
- Catalog membership is positive for both canonical species but no downstream gene/module or fitness query was performed. Historical runner discovery is bounded B5/external reuse,not fresh B6 or global absence;dataset membership does not imply all strains or this record are validated.
- The free-text edge6 convention concerns a fixed predicate label,not ordinary subject-verb grammar or an unasserted RO identifier. The other free-text relations impose no invented external constraints.
- No human scientific-acceptance link was found within the declared ignored-inclusive local scope. Remote/private acceptance remains unknown;AI disclosure,seeding and this agent review are not human sign-off.
- No scientific record,mapping,history,generated product,environment or Git state was modified by this review. No paid research,experimental procedure or organism intervention was performed.
- Three findings:one major and two minor;all node/edge indices are zero-based.
- Native59-input capture10:24:38–39Z followed full target read;all captured hashes independently match. No missing target-history capture was identified.
- Source ledger finalized10:28:26.412575Z with9references9publications13placements6snippets5exact1unknown. Full-field review is distinct from complete mechanistic or whole-body source verification.
- Seven history events comprise six explicit AI-assisted changes plus one automated seed;two protein nodes are reviewed-label-only and there are zero instances.
- B5 full QC executed10:21:03–10:23:38Z. Original B3 history and OLD common diagnostic failures/retry/skips remain in the reused evidence chain.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103146Z-facultatively-anaerobic
kind: record
repository: CultureBotAI/TraitMech
title: 'Whole-record review of facultative anaerobiosis: documentary support and representation'
started_at: '2026-10-21T10:24:38Z'
finished_at: '2026-10-21T10:31:46Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: This session did not author or modify the captured TraitRecord.
    Separate agents inspected documentary sources and grounding; the parent reviewer
    independently reads this complete builder before serialization and validation.
    Historical AI curation and this agent review are distinct from human scientific
    acceptance.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Active METPO identity,broader parent,generic definition,both canonical classifications
  and current node identities are supported. One major groups two imported RO role
  conflicts;two minor findings concern the fixed predicate wordform and unlinked local
  human acceptance. Nine references resolve to nine publications across thirteen placements.
  Five of six quotations are exact and one remains unverified. All eight detailed
  biological edge claims remain UNASSESSED_SCOPE;no mechanism is validated or repaired.
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
  - path: data/traits/environment/facultatively_anaerobic.yaml
    sha256: 705d29c245efc54d1c2df91e2bf8e69ab9be31ec09bf19c60acddbcd6a895ccf
    role: target
  - path: data/traits/environment/oxygen_preference.yaml
    sha256: 16829173ea947f2fef083f673c51519aad962d6812fcd54826ea86f055c5a40b
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
  - path: research/traits/environment/facultatively_anaerobic-deep-research-falcon.md
    sha256: f0ceb3198305897de66642929899d6094669befa07f4565e6f1d5833ef7d7eee
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
- target_id: METPO:1000605
  path: data/traits/environment/facultatively_anaerobic.yaml
  label: facultatively anaerobic
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/facultatively_anaerobic.yaml
    role: Maintained TraitRecord; scientific changes require guarded curation
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Maintained seeder for ontology-backed identity and hierarchy
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: One entire maintained TraitRecord, fully read before native capture.
    All identity, model, example, evidence, graph and history fields are inventoried,
    including eight nodes, eight edges, two canonical examples and seven history events.
    Source identity, quotation fidelity, generic classification, formal ontology roles
    and provenance are reviewed. All eight detailed biological edge claims are UNASSESSED_SCOPE;
    no pathogen fitness or respiration mechanism is validated, reconstructed or improved.
    The parent, authorities, mappings, writers and historical research report are
    context rather than additional targets.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000605
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000605
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000605
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000605
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000605
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000605
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000605
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000605
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: facultatively-anaerobic-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1000605
  command: just validate data/traits/environment/facultatively_anaerobic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed 10:25:14–15Z. Native structural success does not certify external
    predicate semantics or detailed biology.
  evidence_ids:
  - check-facultatively-anaerobic-validate
- check_id: facultatively-anaerobic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000605
  command: just validate-strict data/traits/environment/facultatively_anaerobic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed 10:25:14–16Z. External-role findings are independent of the maintained
    structural checks.
  evidence_ids:
  - check-facultatively-anaerobic-strict
- check_id: facultatively-anaerobic-snippets
  name: Focused abstract snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1000605
  command: just verify-snippets --record data/traits/environment/facultatively_anaerobic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed 10:25:18–24Z: five snippets over three references, two VERIFIED
    and three NOT_IN_ABSTRACT. The URL-based definition snippet was outside this native
    command. Manual documentary inspection separately verifies five of all six snippets;
    the remaining quotation is unknown, not false.'
  evidence_ids:
  - check-facultatively-anaerobic-snippets
- check_id: batch005-qc
  name: Reused full-corpus QC
  status: passed
  required: true
  target_ids:
  - METPO:1000605
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: B5 actual execution 10:21:03–10:23:38Z passed. B6 byte comparisons cover
    scientific and common inputs, with a separately recorded ready environment. This
    is reuse of B5 diagnostics, not a fresh B6 QC execution; warnings, baselines and
    original scope remain.
  evidence_ids:
  - check-batch005-qc
  scope_note: B5 and B6 share the same 8eee scientific base; 1130 traits,1278 history
    files and19 common inputs match in the retained comparison. B6 readiness does
    not turn the historical command into a new execution or certify all biological
    claims.
- check_id: protein-taxon-applicability
  name: Focused protein/taxon audit applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000605
  summary: NONMECHANISTIC graph has two explicit REVIEWED_LABEL_ONLY protein nodes
    and zero instances. No new accession or mandatory anchor is justified. Detailed
    organism mechanisms remain unassessed.
  evidence_ids:
  - record
  - node-edges
- check_id: uniprot-applicability
  name: UniProt instance audit applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000605
  summary: No UniProt instance or accession is asserted; no instance-specific audit
    is applicable. Reviewed label-only nodes are permitted by native policy.
  evidence_ids:
  - record
  - native-policy
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-facultatively-anaerobic-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/facultatively-anaerobic-validate.log
  locator: Executed 2026-10-21T10:25:14Z through 2026-10-21T10:25:15Z; metadata facultatively-anaerobic-validate.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: Passed 10:25:14–15Z. Native structural success does not certify external
    predicate semantics or detailed biology.
  snapshot_sha256: bf9b28d46b1c5f21c14c39e889df7bf86bdcfaf784333ba1822fd82bb755b989
- evidence_id: check-facultatively-anaerobic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/facultatively-anaerobic-strict.log
  locator: Executed 2026-10-21T10:25:14Z through 2026-10-21T10:25:16Z; metadata facultatively-anaerobic-strict.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: Passed 10:25:14–16Z. External-role findings are independent of the maintained
    structural checks.
  snapshot_sha256: e044c4bb4be028c617b17574d443965ead53b6e67c5e638dee150b41ec39dc24
- evidence_id: check-facultatively-anaerobic-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/facultatively-anaerobic-snippets.log
  locator: Executed 2026-10-21T10:25:18Z through 2026-10-21T10:25:24Z; metadata facultatively-anaerobic-snippets.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: 'Passed 10:25:18–24Z: five snippets over three references, two VERIFIED
    and three NOT_IN_ABSTRACT. The URL-based definition snippet was outside this native
    command. Manual documentary inspection separately verifies five of all six snippets;
    the remaining quotation is unknown, not false.'
  snapshot_sha256: 2f912da9012de4dce6d7080878887ea8b95bb414e00608628d4934fed21b7205
- evidence_id: check-batch005-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/batch005-qc.log
  locator: Executed 2026-10-21T10:21:03Z through 2026-10-21T10:23:38Z; metadata batch005-qc.json
  accessed_at: '2026-10-21T10:31:46Z'
  support: context_only
  summary: B5 actual execution 10:21:03–10:23:38Z passed. B6 byte comparisons cover
    scientific and common inputs, with a separately recorded ready environment. This
    is reuse of B5 diagnostics, not a fresh B6 QC execution; warnings, baselines and
    original scope remain.
  snapshot_sha256: 206638ef702eef1ea64f13c4be3ef11180f9659383be68d1e492a9760c8f79be
- evidence_id: reuse
  kind: validation
  reference: B6 scientific and common-input comparison
  locator: Original verification 10:14:46.298715Z;1130 traits,1278 history files and19
    common inputs
  accessed_at: '2026-10-21T10:14:46.298715Z'
  support: supports
  summary: The original receipt correctly named B4 QC as latest at its own timestamp.
    The separate later supplement records actual B5 QC. The f25-to8eee delta has only
    seven workflow,skill and infrastructure-history additions; original execution
    dates, product failures, retry and adapter skips remain.
  snapshot_sha256: 91de0fcd8f598a37b867033da1a4d732eaf5676848023a41dd6963612a78aa44
- evidence_id: reuse-independent
  kind: validation
  reference: Independent common-check and environment review
  locator: B5 QC10:21:03–10:23:38;contract4passed;nativecheck102valid;19common and59target
    inputs rehashed
  accessed_at: '2026-10-21T10:28:10.859819Z'
  support: supports
  summary: Later B5 check metadata and logs are hash-recorded. B6 readiness records
    its own locked dev environment but is not a B6 QC result.1278 history files and1277
    history records validated in B3 are distinct counts.
  snapshot_sha256: f5e234e9de85ff4dbd486c2f4e4c9c8df915a767fb67afa4da204ab28f57a7f4
- evidence_id: capture
  kind: validation
  reference: Native selected-record capture
  locator: 59 inputs;10:24:38–39Z following full record read
  accessed_at: '2026-10-21T10:24:39Z'
  support: supports
  summary: Target, parent, policies, ontology snapshots, mappings, writers and historical
    provider report were captured before assessment. No target-specific history was
    discovered that requires supplemental capture.
  snapshot_sha256: cab9d173604d40b256e2f633ca805292154fbf190cfdacb55f09ffcbfe535465
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/facultatively_anaerobic.yaml
  locator: Entire record;8nodes,8edges,2examples,2label-only protein nodes,0instances,7history
    events
  accessed_at: '2026-10-21T10:24:38Z'
  support: partial
  summary: Active environmental CLASS with REVIEWED status and NONMECHANISTIC scope.
    Six events disclose AI assistance and one is automated seeding. Complete field
    inspection does not establish detailed biological correctness.
  snapshot_sha256: 705d29c245efc54d1c2df91e2bf8e69ab9be31ec09bf19c60acddbcd6a895ccf
- evidence_id: native-policy
  kind: authority
  reference: Native field-by-field review checklist
  locator: Evidence standard and Status/audit row;grounding-agent actual read10:26:57.013274Z,independently
    reread during builder preparation
  accessed_at: '2026-10-21T10:26:57.013274Z'
  support: supports
  summary: Definition, example and edge support are distinct; optional fields need
    no token additions. Predictions and association do not establish mechanisms. REVIEWED
    requires human sign-off and explicit AI assistance and unresolved gaps.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: predicate-label-policy
  kind: authority
  reference: Repository predicate vocabulary convention
  locator: docs/CURATION_PLAYBOOK.md:641–644;exact read/hash receipt10:29:31.233122Z
  accessed_at: '2026-10-21T10:29:31.233122Z'
  support: supports
  summary: The fixed predicate-label convention explicitly requires third-person singular,
    using enables rather than enable. This convention is distinct from grammatical
    agreement with a plural surface label and imposes no external RO identifier.
  snapshot_sha256: bd7d9bdf1c391e3747ecb13688e501a0668d0ad2b97cc30f9155425c30938c5a
- evidence_id: identity
  kind: authority
  reference: Pinned METPO active/deprecated term and synonym scan
  locator: METPO1000605 and broader oxygen-preference parent1000601;complete label/synonym
    declaration scan
  accessed_at: '2026-10-21T10:25:10.690159Z'
  support: supports
  summary: Active exact label,related synonyms and direct parent agree. O₂/O2 is harmless
    typography. The related synonym facultative is shared and is not an exclusive
    exact identity. Actual obsolete replacement annotations are retained; none is
    invented for obsolete1000116.
  snapshot_sha256: 566965d1fb9ea7ab36590346fa6c10b74533925a00d82be1dcf55d90ac9bf3f3
- evidence_id: local-authority
  kind: authority
  reference: Maintained schema,grounding mappings and writers
  locator: Eight local policy/writer excerpts at10:26:57.010492–10:26:57.013712Z
  accessed_at: '2026-10-21T10:26:57.013712Z'
  support: supports
  summary: The process and chemical categories and reviewed-label-only protein treatment
    are permitted. Current node mappings match official identities. Broad predicate
    gates and populated-ID skips explain recurrence without making external roles
    valid.
  snapshot_sha256: 65f501ffef0470a79d31ceeb70256ded1e9323e05dcf05cd99984fab02640fb9
- evidence_id: official-identities
  kind: database
  reference: Official GO,ChEBI and NCBI identity responses
  locator: GO0009060/GO0009061 biological_process;CHEBI15379 dioxygen;NCBI562/1280
    species
  accessed_at: '2026-10-21T10:26:57.006705Z'
  support: supports
  summary: The asserted process and chemical identities and both canonical species
    labels match the retained official responses. This verifies identity and aspect/rank
    only; detailed physiological mechanism remains unassessed.
  snapshot_sha256: 6af8f91f56c38ee0c058ef04a5f76c1b67cfe653ebe209b200d1b79601b9133c
- evidence_id: authority-reuse
  kind: database
  reference: Hash-verified official response reuse
  locator: Original GO9060,ChEBI15379,NCBI56209:57:47;GO9061 08:46:57–58;NCBI1280
    07:14:56–57
  accessed_at: '2026-10-21T10:26:57.004812Z'
  support: supports
  summary: All five saved response copies preserve the original SHA256 and acquisition
    times. Copy verification at10:26:57Z is not a new network request; unrelated taxa
    in paired payloads are outside assessment.
  snapshot_sha256: d27f87bf6beeba8ce01dc7ed3f40efe660b4baff8264d4e95622f3589b19d87f
- evidence_id: ro
  kind: authority
  reference: Cached RO definitions and recursive domain/range statements
  locator: Original authority read09:52:45.989262Z;DB SHA849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb;reuse10:26:57
  accessed_at: '2026-10-21T10:26:57.009750Z'
  support: supports
  summary: RO2327 requires capability and actual execution; compatible material/process
    categories alone do not establish that role. RO2211 requires process endpoints.
    These external meanings do not imply a native validator or reasoner failure; no
    RO meaning is attached to the six free-text-only edges.
  snapshot_sha256: de652fd67a953e8985e6c84944a9d54814a7a26e8592affad1dc9310926d531d
- evidence_id: grounding-ledger
  kind: validation
  reference: Complete documentary grounding assessment
  locator: All8nodes and8edges;59captured inputs unchanged
  accessed_at: '2026-10-21T10:26:57.086996Z'
  support: partial
  summary: One grouped major concerns the two imported predicate roles. Canonical
    and node identities are valid. Every detailed biological claim remains UNASSESSED_SCOPE;
    no missing optional accession, pathway or mechanism step is inferred.
  snapshot_sha256: e311554ca09b508139a728cb8f78ad3e9570b870bf73c3f028652a13bfae0bb6
- evidence_id: node-edges
  kind: validation
  reference: Complete node and edge role ledger
  locator: nodes[0–7],edges[0–7],zero-based;8biological correctness assessments UNASSESSED_SCOPE
  accessed_at: '2026-10-21T10:26:57.013995Z'
  support: partial
  summary: All represented kinds and asserted ontology roles are inventoried. Process
    operation is not forced to a physical component or pathway. Free-text edges are
    distinguished from the two asserted external predicates.
  snapshot_sha256: b340317f68196a73a2b87c58f310b369b2ed9027f33741b3e6191249525e8185
- evidence_id: captured-hashes
  kind: validation
  reference: Final grounding input receipt
  locator: 59/59native input SHA256 values match at10:26:57.086574Z
  accessed_at: '2026-10-21T10:26:57.086574Z'
  support: supports
  summary: All scientific inputs and contextual artifacts captured for this single
    target remain the same bytes. This is integrity evidence rather than biological
    validation.
  snapshot_sha256: 2ffacd661fc0fdd3e18a316dfab08b8552ad7fdae2b82d899c7fb5c00b7548a0
- evidence_id: owners
  kind: authority
  reference: Maintained mapping and writer recurrence assessment
  locator: Predicate rows9/11;writerlines138–179;node rows2/20/21
  accessed_at: '2026-10-21T10:26:57.073113Z'
  support: supports
  summary: Broad enables/regulates mapping rows can restore inappropriate predicate
    IDs after ID-only removal. Node identities are valid. Canonical-label normalization
    of free-text edge6 must not silently add the RO2327 assignment.
  snapshot_sha256: a805af54a86713a002a7794d3c00a821b8430bb940147a88362157234ae96168
- evidence_id: provenance
  kind: search
  reference: Bounded local human-acceptance linkage search
  locator: 192matching files;7events6AI+seed;no target repository history or targeted
    review bundle
  accessed_at: '2026-10-21T10:25:12.823367Z'
  support: partial
  summary: The inspected local evidence links no target-specific human scientific
    acceptance. Automated validation,AI history and seeding do not supply it. This
    does not establish absence of private or remote review.
  snapshot_sha256: ec31891ee4381dc8b24f5dd0d1c49066d9991f70e246466c32cc45a481345839
  search_scope: 'Own B6 repository: rg --hidden --no-ignore -l with exact target slug,label,related
    phrase and METPO:1000605; .git/** and .venv/** explicitly excluded. Matching repository-history
    content and structured target lists inspected. No remote/private acceptance or
    whole-filesystem absence claim.'
- evidence_id: graph-owner-search
  kind: search
  reference: Supplemental graph/node provenance search
  locator: Exact graph andnode keys;10:26:00.732965Z;exit1no matches
  accessed_at: '2026-10-21T10:26:00.732965Z'
  support: partial
  summary: A bounded ignored-inclusive graph/node search found no additional target
    history or writer. This does not imply no general grounding writer exists; general
    owners are independently identified.
  snapshot_sha256: 0ef1dbed90fc1e52f5475306066476ad11ec4b4b426f02ec79a4ae00ace7d850
  search_scope: Only B6 repo history,scripts,mappings,reviews;rg --no-ignore --hidden
    -l with exact graph/node keys; .git/** and .venv/** excluded. No other directories
    or remote provenance searched by this command.
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Original07:36:12.732638–07:36:12.858149Z;20organisms28datasets;hash-verified10:26:57reuse
  accessed_at: '2026-10-21T10:26:57.016211Z'
  support: context_only
  summary: 'Both canonical species have catalog entries: E.coli5datasets and S.aureus2datasets.
    Membership does not verify this record or every strain. Detailed gene/module/fitness
    queries were deliberately not assessed; no data-absence or negative-phenotype
    inference follows.'
  snapshot_sha256: 9ca0f0d4fedd88d1774434d6b38928409c92f36f73859dcefa4294b744446501
- evidence_id: runner
  kind: search
  reference: Historical bounded structured-runner discovery
  locator: OriginalB5PATH/project search09:27:57.380287–09:27:57.542053Z;older external
    bounds08:17:15
  accessed_at: '2026-10-21T09:27:57.542053Z'
  support: context_only
  summary: The runner search receipt is hash-verified historical reuse, not new B6
    discovery. Its bounded no-runner result is not global absence. Catalog membership
    was checked separately; no downstream mechanism query was performed.
  snapshot_sha256: 43597ec8b007fc605fabf9069534281f331a33bda5615b9ce9c473facf744179
  search_scope: Original B5 PATH and ignored/hidden-inclusive project filenames and
    pyprojects with .git excluded; older external install/project bounds are retained
    in prior-runner-discovery.json. No fresh B6 or whole-filesystem runner search
    is claimed.
- evidence_id: source-ledger
  kind: validation
  reference: Complete documentary source assessment
  locator: 9references9publications13placements6snippets;final10:28:26.412575Z
  accessed_at: '2026-10-21T10:28:26.412575Z'
  support: partial
  summary: All identities resolve; generic definition and both canonical classifications
    are positively supported. Five quotations are exact and one remains unknown. All
    eight detailed edge claims remain UNASSESSED_SCOPE. Source genre alone establishes
    no false-citation finding.
  snapshot_sha256: 4d23819b28d15d58a05763402bf0e5227023d1cdceb36a758dc15f9b971f1cee
- evidence_id: bibliography
  kind: database
  reference: Every cited publication and placement
  locator: source0–source8;each identity,original metadata receipt,scope and nearest
    placement retained
  accessed_at: '2026-10-21T10:28:26.412575Z'
  support: supports
  summary: PMID7747938 resolves to DOI10.1007/bf00871629 and is distinct from graph
    DOI10.1007/BF00445650,PMID1854188. NBK482349 corresponds to PMID29493974. The
    DOI10.1101 preprint remains a preprint,not an assumed peer-reviewed journal publication.
  snapshot_sha256: 67a40530e54bc8be11d038baa03f5c47d862978f03ba3d7e9051c279a099a014
- evidence_id: placements
  kind: record_content
  reference: Complete citation inventory
  locator: 13placements:definition_source,2top evidence,2canonical examples and8edges
  accessed_at: '2026-10-21T10:28:26.412575Z'
  support: supports
  summary: Nearest citation placement is preserved; positive classification support
    is not transferred to unassessed graph mechanisms. Notes without snippet fields
    are not counted as quotations.
  snapshot_sha256: dbd92e18b0c43bc76fe4528371894da79da9b165a9e7c4ecedab5d1ca7609089
- evidence_id: snippets
  kind: primary_source
  reference: Literal quotation checks across inspected primary surfaces
  locator: 6snippets:5exact at chapter excerpt,introduction,title or abstracts;1unknown
  accessed_at: '2026-10-21T10:28:26.412575Z'
  support: partial
  summary: Exact wording is distinct from biological correctness. The CMI quotation
    is exact title text. The one unknown assigned phrase was not found in the inspected
    abstract; inaccessible body text is not presumed absent.
  snapshot_sha256: eaaa0fbc1f84c8683aa91c2e60b6f8913fcac397410385b37eab1945bd000954
- evidence_id: edge-source-scope
  kind: validation
  reference: Complete documentary edge-source ledger
  locator: edges[0–7];8/8biological_correctness and claim_support UNASSESSED_SCOPE
  accessed_at: '2026-10-21T10:28:26.412575Z'
  support: context_only
  summary: Citation identity and declared quotation status are inventoried for every
    edge. No detailed pathogen fitness,respiration,regulatory or engineering mechanism
    was validated,completed or repaired.
  snapshot_sha256: 97bfda9dccee8daee63183e0ee13f60e37e5fe3d25d0d165627b14e13c4e76fb
- evidence_id: classification-excerpts
  kind: primary_source
  reference: Bounded generic classification passages
  locator: PMC9075585 Introduction/sec1-1 bodyparagraph4;PMC3985588 Methods/sec5/Straininformation/sec6
    bodyparagraph2
  accessed_at: '2026-10-21T10:28:26.411481Z'
  support: supports
  summary: The first supplies the existing generic E.coli quotation. The second describes
    DSM20231T as known to be facultatively anaerobic. The S.aureus exemplar has descriptive
    classification support;no new direct growth assay,genome-derived causation or
    species-wide strain uniformity is claimed.
  snapshot_sha256: f652a5ade12dac5e0bff8a52f4099c835475b6ef40b98cbbaf8866dee6db181d
- evidence_id: metadata-source0
  kind: database
  reference: DOI:10.1093/femsre/fuac008
  locator: Original indexed identity retrieval; E. coli vertebrate-gut ecology review
  accessed_at: '2026-10-21T10:25:32.790920Z'
  support: supports
  summary: Publication identity and explicitly declared source type only; detailed
    mechanisms remain unassessed. Complete XML available;only assigned quotation and
    generic introductory classification adopted.
  snapshot_sha256: ceab9f59dfed758a4e8cb09fc1f5e3c3d88bd6d1eee07ce84478fec57a38995d
- evidence_id: body-source0
  kind: primary_source
  reference: DOI:10.1093/femsre/fuac008
  locator: 'PMC9075585 Introduction/sec1-1 (Escherichia coli: a versatile organism),body
    paragraph4 zero-based'
  accessed_at: '2026-10-21T10:26:41.811484Z'
  support: supports
  summary: Exact assigned quotation and generic oxygen-preference classification.
    Only this bounded classification/quotation passage was inspected;availability
    of a complete file is not full biological-body review.
  snapshot_sha256: 8a9898da7793607e5b7e16a7a2b6a92d51fed0d5510650b3b59010be112ec907
- evidence_id: metadata-source1
  kind: database
  reference: PMID:7747938
  locator: Original indexed identity retrieval; Broad bacterial oxygen-regulation
    review
  accessed_at: '2026-10-21T10:25:34.481191Z'
  support: supports
  summary: Publication identity and explicitly declared source type only; detailed
    mechanisms remain unassessed. Indexed abstract only;detailed regulatory programs
    and source mechanisms unassessed.
  snapshot_sha256: c6a2e91b5aa9bcd991f47286e81bf18c699d4e53d32be720d25ed76fb1c42d47
- evidence_id: metadata-source2
  kind: database
  reference: PMID:24628867
  locator: Original indexed identity retrieval; S. aureus subsp. aureus type-strain
    genome publication
  accessed_at: '2026-10-21T10:25:32.738286Z'
  support: supports
  summary: Publication identity and explicitly declared source type only; detailed
    mechanisms remain unassessed. Complete XML available but read only bounded classification;adjacent
    protocols,virulence/resistance and genome mechanisms unassessed.
  snapshot_sha256: 95b007a073572ca5e2bcf85dcec7b7cb00d7cc556a6b671e11cc10d4069a0cda
- evidence_id: body-source2
  kind: primary_source
  reference: PMID:24628867
  locator: PMC3985588 Methods/sec5 > Strain information/sec6,body paragraph2 zero-based,second
    sentence
  accessed_at: '2026-10-21T10:26:41.431844Z'
  support: supports
  summary: Strain DSM20231T is described as known to have the phenotype. This is descriptive
    classification support,not a new direct growth assay or genome-derived causal
    proof. Adjacent procedures/pathogen characteristics unassessed. Only this bounded
    classification/quotation passage was inspected;availability of a complete file
    is not full biological-body review.
  snapshot_sha256: 12f0cb41473ef085e19e0aa39742a60a40cfee97ba5d89e2981999cc261ffd5f
- evidence_id: metadata-source3
  kind: database
  reference: DOI:10.1111/cmi.13338
  locator: Original indexed identity retrieval; Facultative-anaerobe infection-context
    review
  accessed_at: '2026-10-21T10:25:32.759409Z'
  support: supports
  summary: Publication identity and explicitly declared source type only; detailed
    mechanisms remain unassessed. No complete body obtained;title fidelity does not
    validate biological edge support,fitness or infection mechanisms.
  snapshot_sha256: eff37363e3deb0cb7c529d75988516983cf17176bddb26a48de3a1d25a5c02d0
- evidence_id: metadata-source4
  kind: database
  reference: DOI:10.1007/BF00445650
  locator: Original indexed identity retrieval; E. coli oxygen-regulation review
  accessed_at: '2026-10-21T10:25:33.590446Z'
  support: supports
  summary: Publication identity and explicitly declared source type only; detailed
    mechanisms remain unassessed. No complete body obtained;absent abstract wording
    does not prove absence from unseen body. All detailed edge biology unassessed.
  snapshot_sha256: 0750bf8067b2ec7502f94e9f56532c25be29efe481bb4384feb96b608007f63c
- evidence_id: metadata-source5
  kind: database
  reference: DOI:10.1101/2025.01.08.631794
  locator: Original indexed identity retrieval; E. coli trace-metal/electron-acceptor
    preprint
  accessed_at: '2026-10-21T10:25:33.713095Z'
  support: supports
  summary: Publication identity and explicitly declared source type only; detailed
    mechanisms remain unassessed. Metadata identity/context only;no complete body
    or independent peer-review/version-history determination. Detailed biological
    claims unassessed.
  snapshot_sha256: 176c2ec04a7594c73643035bfd646349a0dee92e9cda0ea4d63c4ebda5bd94ff
- evidence_id: metadata-source6
  kind: database
  reference: DOI:10.1128/mbio.01448-23
  locator: Original indexed identity retrieval; Bacteremia-context regulatory primary
    publication
  accessed_at: '2026-10-21T10:25:34.827996Z'
  support: supports
  summary: Publication identity and explicitly declared source type only; detailed
    mechanisms remain unassessed. No complete body obtained;no source-claim correctness
    or host-fitness mechanism adjudication.
  snapshot_sha256: 6ebe8706f07f1c94065ea68a72cf3158533920920dbf9fcea9ad8313f783116a
- evidence_id: metadata-source7
  kind: database
  reference: DOI:10.1038/s41467-024-51029-x
  locator: Original indexed identity retrieval; Biochemical-engineering publication
  accessed_at: '2026-10-21T10:25:34.344824Z'
  support: supports
  summary: Publication identity and explicitly declared source type only; detailed
    mechanisms remain unassessed. No complete body obtained;engineering,respiratory-module
    claims and all detailed mechanisms unassessed. No corrective design or optimization.
  snapshot_sha256: effb700b7a9154ebb8061b91b2431d694189fc0ca5c6a4a4169b90e47f48452c
- evidence_id: metadata-source8
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/books/NBK482349/
  locator: Original indexed identity retrieval; StatPearls Anaerobic Infections chapter,NBK482349
  accessed_at: '2026-10-21T10:25:49.025576Z'
  support: supports
  summary: Publication identity and explicitly declared source type only; detailed
    mechanisms remain unassessed. Indexed chapter excerpt only;browser attempts returned
    challenge/footer. No full chapter inspected. Clinical and pathogen mechanisms
    unassessed.
  snapshot_sha256: 51b8d1584800f6c7ce65ea00267399d0656999482006883ad7aaae4949cd6e71
- evidence_id: source-access
  kind: database
  reference: Actual successful classification XML acquisitions
  locator: E.coli10:26:40.348094–10:26:41.811484Z;S.aureus10:26:40.348624–10:26:41.431844Z
  accessed_at: '2026-10-21T10:26:41.811484Z'
  support: supports
  summary: Two actual XML responses succeeded and retain their SHA256. Only generic
    classification and assigned quotation passages were inspected;adjacent procedures
    and mechanisms are outside scope.
  snapshot_sha256: 31472c3a5235574917336ebc9e8b949290239ebfbf093173fa4239a954c8a7e2
- evidence_id: source-access-failure
  kind: database
  reference: Retained initial sandbox DNS failures
  locator: 10:26:30.592226–10:26:30.605773Z
  accessed_at: '2026-10-21T10:26:30.605773Z'
  support: context_only
  summary: Initial DNS failures were superseded by successful XML retrieval. These
    failed attempts are retained as access history and provide no article-absence
    evidence.
  snapshot_sha256: 8091993d24ab8316e5bae44a43cc58c5703003aca1a5fe4afb065d6828a2bb6c
- evidence_id: browser-access
  kind: database
  reference: Retained primary browser access attempts
  locator: 10:25:09–10:25:24Z;Bookshelf challenge and PubMed footer only
  accessed_at: '2026-10-21T10:25:24Z'
  support: context_only
  summary: Browser pages supplied no chapter text. The later actual indexed chapter
    excerpt supports the definition. Search result leads and challenge/footer surfaces
    were not treated as primary passages;receipt hash is not a saved HTML-body hash.
  snapshot_sha256: 1eaa544e6a3ee4799da446cb5a49a5e84c838ed8617ec95263b8589c2843ae82
- evidence_id: source-copy-reuse
  kind: validation
  reference: Original source metadata copy/hash chain
  locator: Original root metadata10:25:32.046098–10:25:34.827996Z;definition10:25:48.391372–10:25:49.025576Z
  accessed_at: '2026-10-21T10:28:26.412575Z'
  support: supports
  summary: Source-agent copies preserve the original response bytes and acquisition
    bounds;copy and final assessment times are not relabelled as network retrieval.
  snapshot_sha256: 9253f34f0881a8a99691ca266044dbd51ec446f64a40f7a1d852140ede7178a3
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: ID,label,synonyms,polarity and term kind'
  outcome: supported
  target_ids:
  - METPO:1000605
  summary: Active exact METPO1000605 denotes a positive environmental CLASS. Related
    synonyms are correctly scoped;facultative is shared vocabulary rather than a unique
    exact class identity. O₂/O2 differs only typographically. Current active identity
    is not replaced with a similar or obsolete term.
  evidence_ids:
  - identity
  - record
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: growth with or without oxygen'
  outcome: supported
  target_ids:
  - METPO:1000605
  summary: The pinned definition matches the current concept. The actual indexed NBK482349
    chapter excerpt positively supports the generic oxygen-presence/absence growth
    distinction. The chapter URL is linked through its actual PMID metadata;browser
    challenges do not supply body evidence.
  evidence_ids:
  - identity
  - metadata-source8
  - source-ledger
  - browser-access
- assessment_id: hierarchy
  area: identity
  topic: 'Native checklist: strictly broader parent and source semantics'
  outcome: supported
  target_ids:
  - METPO:1000605
  summary: Direct parentMETPO1000601 oxygen preference is strictly broader and exact
    in the pinned source. Obsolete replacement annotations are used only where actually
    present. No fallback identifier,opposite-parent or xref-equivalence finding is
    established.
  evidence_ids:
  - identity
  - record
- assessment_id: category-model
  area: representation
  topic: 'Native checklist: category,term kind,graph scope and optional fields'
  outcome: supported
  target_ids:
  - METPO:1000605
  summary: ENVIRONMENT,CLASS and NONMECHANISTIC scope fit the broad phenotype. Current
    protein nodes carry legitimate reviewed-label-only explanations;zero instances
    require no token accession. Process operation and chemical aggregates are not
    automatically wrong node kinds. Empty optional slots are not defects by themselves.
  evidence_ids:
  - record
  - node-edges
  - native-policy
  - local-authority
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: both canonical identities and nearest classification support'
  outcome: supported
  target_ids:
  - METPO:1000605
  summary: Official NCBI562 and1280 species identities match. PMID7747938 abstract
    supports the existing general E.coli classification and growth-mode note. PMID24628867
    describes S.aureus DSM20231T as known to be facultatively anaerobic;this supports
    the exemplar without inferring a newly measured assay or all-strain uniformity.
    Both nearest sources were checked separately from the definition source.
  evidence_ids:
  - official-identities
  - authority-reuse
  - metadata-source1
  - body-source2
  - classification-excerpts
  - source-ledger
- assessment_id: node-grounding
  area: grounding
  topic: 'Native checklist: all eight represented node identities and kinds'
  outcome: supported
  target_ids:
  - METPO:1000605
  summary: The current GO grounds are active biological processes;CHEBI15379 is dioxygen.
    Label-only protein and ungrounded chemical aggregate representations are permitted.
    No unsupported token ground,instance or forced pathway/component conversion is
    required. Biological descriptions are not certified by identity agreement.
  evidence_ids:
  - official-identities
  - node-edges
  - local-authority
  details: 'causal_graphs[0].nodes[0]: supported_identity; biological mechanism UNASSESSED_SCOPE.

    causal_graphs[0].nodes[1]: supported_chemical_identity; biological mechanism UNASSESSED_SCOPE.

    causal_graphs[0].nodes[2]: supported_process_identity; biological mechanism UNASSESSED_SCOPE.

    causal_graphs[0].nodes[3]: supported_process_identity; biological mechanism UNASSESSED_SCOPE.

    causal_graphs[0].nodes[4]: permitted_label_only_protein; biological mechanism
    UNASSESSED_SCOPE.

    causal_graphs[0].nodes[5]: permitted_label_only_protein; biological mechanism
    UNASSESSED_SCOPE.

    causal_graphs[0].nodes[6]: permitted_chemical_aggregate; biological mechanism
    UNASSESSED_SCOPE.

    causal_graphs[0].nodes[7]: permitted_process; biological mechanism UNASSESSED_SCOPE.'
- assessment_id: external-relations
  area: consistency
  topic: 'Native checklist: asserted predicate roles across all eight edges'
  outcome: concern
  target_ids:
  - METPO:1000605
  summary: Edges0/1 import two incompatible RO meanings:executor versus available-input
    wording,and process-only regulation versus material endpoints. Six other edges
    assert no predicate_id and inherit no invented RO constraints. The edge6 wordform
    is a separate repository vocabulary convention. Native structural acceptance does
    not adjudicate these semantic distinctions.
  evidence_ids:
  - ro
  - node-edges
  - owners
  - predicate-label-policy
  details: 'causal_graphs[0].edges[0]: major_external_executor_role_mismatch; detailed
    biology UNASSESSED_SCOPE.

    causal_graphs[0].edges[1]: major_external_process_role_mismatch; detailed biology
    UNASSESSED_SCOPE.

    causal_graphs[0].edges[2]: free_text_no_asserted_external_constraint; detailed
    biology UNASSESSED_SCOPE.

    causal_graphs[0].edges[3]: free_text_no_asserted_external_constraint; detailed
    biology UNASSESSED_SCOPE.

    causal_graphs[0].edges[4]: free_text_no_asserted_external_constraint; detailed
    biology UNASSESSED_SCOPE.

    causal_graphs[0].edges[5]: free_text_no_asserted_external_constraint; detailed
    biology UNASSESSED_SCOPE.

    causal_graphs[0].edges[6]: free_text_no_asserted_external_constraint; detailed
    biology UNASSESSED_SCOPE.

    causal_graphs[0].edges[7]: free_text_no_asserted_external_constraint; detailed
    biology UNASSESSED_SCOPE.'
- assessment_id: biological-edge-support
  area: evidence
  topic: 'Native checklist: each detailed biological edge claim'
  outcome: unknown
  target_ids:
  - METPO:1000605
  summary: All eight detailed biological claims,including source-specific direction,sufficiency,necessity
    and mechanistic notes,remain UNASSESSED_SCOPE. Neither literal quotation matches
    nor formal role compatibility validate them. The review supplies no missing steps,replacement
    mechanism,organism intervention or optimization.
  evidence_ids:
  - edge-source-scope
  - node-edges
  - source-ledger
  details: 'causal_graphs[0].edges[0]: citation identity verified; quotation=VERIFIED_EXACT;
    biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.

    causal_graphs[0].edges[1]: citation identity verified; quotation=UNVERIFIED; biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.

    causal_graphs[0].edges[2]: citation identity verified; quotation=VERIFIED_EXACT;
    biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.

    causal_graphs[0].edges[3]: citation identity verified; quotation=VERIFIED_EXACT;
    biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.

    causal_graphs[0].edges[4]: citation identity verified; quotation=NOT_APPLICABLE_NO_SNIPPET_FIELD;
    biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.

    causal_graphs[0].edges[5]: citation identity verified; quotation=NOT_APPLICABLE_NO_SNIPPET_FIELD;
    biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.

    causal_graphs[0].edges[6]: citation identity verified; quotation=NOT_APPLICABLE_NO_SNIPPET_FIELD;
    biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.

    causal_graphs[0].edges[7]: citation identity verified; quotation=NOT_APPLICABLE_NO_SNIPPET_FIELD;
    biological_correctness=UNASSESSED_SCOPE;claim_support=UNASSESSED_SCOPE.'
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: nine identities and thirteen citation placements'
  outcome: supported
  target_ids:
  - METPO:1000605
  summary: All nine literal references resolve to nine distinct publications. PMID7747938/DOIbf00871629
    is not an alias of graph PMID1854188/DOIbf00445650. NBK482349 identity is linked
    to its indexed chapter. The2025DOI remains a preprint in inspected metadata;no
    later-version or peer-review assertion is made.
  evidence_ids:
  - bibliography
  - placements
  - metadata-source1
  - metadata-source4
  - metadata-source5
  - metadata-source8
- assessment_id: quotation-fidelity
  area: evidence
  topic: 'Native checklist: six snippets and their exact inspected surfaces'
  outcome: unknown
  target_ids:
  - METPO:1000605
  summary: Five snippets are exact:definition excerpt,generic E.coli introductory
    body,title text,and two abstract passages. One assigned phrase remains unverified
    in an unseen body,not demonstrated nonliteral. Notes without snippet fields remain
    interpretation rather than quotations. Native abstract output is retained separately
    from manual follow-up.
  evidence_ids:
  - snippets
  - classification-excerpts
  - check-facultatively-anaerobic-snippets
  - source-ledger
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole-record coverage and explicit unresolved scope'
  outcome: supported
  target_ids:
  - METPO:1000605
  summary: All present fields,eight nodes,eight edges,two examples,nine references,thirteen
    placements,six snippets and seven history events are accounted for. Full field
    coverage is distinct from complete biological validation or full-body reading.
    The historical research report is captured context,not independent primary evidence.
    No placeholder discussion,dataset,protein or mechanism is added.
  evidence_ids:
  - record
  - capture
  - placements
  - grounding-ledger
  - edge-source-scope
  - native-policy
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: structured catalog applicability'
  outcome: supported
  target_ids:
  - METPO:1000605
  summary: Both canonical species are represented in the retained20-organism28-dataset
    catalog. Dataset membership is documentary context only;strain coverage is not
    generalized. No gene,module,fitness or respiratory query was conducted. Historical
    runner discovery is explicitly bounded and not a fresh B6/global absence claim.
  evidence_ids:
  - expression
  - runner
- assessment_id: ownership
  area: ownership
  topic: 'Native checklist: maintained owner recurrence and bounded fixes'
  outcome: concern
  target_ids:
  - METPO:1000605
  summary: Predicate table rows9/11 and the guarded grounding writer can restore the
    incompatible assignments after ID-only clearing. Preserve valid node grounds.
    A wordform-only edge6 edit must not silently create an external predicate assertion.
    Actions are confined to existing representation and provenance rather than scientific
    mechanism completion.
  evidence_ids:
  - owners
  - local-authority
  - ro
  - predicate-label-policy
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: REVIEWED status and local acceptance linkage'
  outcome: concern
  target_ids:
  - METPO:1000605
  summary: Seven per-record events disclose six AI-assisted changes plus automated
    seeding. Ignored-inclusive local target and graph/node searches found no explicit
    human scientific-acceptance link or target repository-history artifact. This is
    a bounded documentation concern;remote/private acceptance remains unknown.
  evidence_ids:
  - provenance
  - graph-owner-search
  - native-policy
  - record
- assessment_id: check-status
  area: schema
  topic: 'Native checklist: focused execution and historical reuse'
  outcome: supported
  target_ids:
  - METPO:1000605
  summary: Focused validation,strict validation and snippet commands passed with their
    actual outputs. B5 QC passed10:21:03–10:23:38;B6 unchanged inputs and readiness
    are documented without claiming fresh execution. B3 history and OLD product failure/retry/skips
    retain original bounds. No required executed check is unavailable;unassessed biology
    is explicitly separate.
  evidence_ids:
  - check-facultatively-anaerobic-validate
  - check-facultatively-anaerobic-strict
  - check-facultatively-anaerobic-snippets
  - check-batch005-qc
  - reuse
  - reuse-independent
findings:
- finding_id: external-predicate-roles
  issue_key: facultatively-anaerobic-external-predicate-roles
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two imported RO meanings conflict with the represented roles
  description: Edge0 uses RO0002327 while its own wording describes available input
    rather than an entity executing the process. Its material/process categories are
    compatible;the conflict is the additional capability/execution meaning,not a categorical
    chemical exclusion. Edge1 uses RO0002211,whose domain and range are processes,with
    a CHEMICAL subject and GENE_OR_PROTEIN object. These grouped semantic mismatches
    concern asserted identifiers and existing representation,not demonstrated false
    biology or a native reasoner failure. Broad maintained mapping gates can recreate
    the IDs after clearing.
  target_ids:
  - METPO:1000605
  field_paths:
  - causal_graphs[0].edges[0].predicate_id
  - causal_graphs[0].edges[1].predicate_id
  evidence_ids:
  - ro
  - node-edges
  - record
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/facultatively_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Rows9/11 wildcard enables/regulates mappings
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Populated-ID skip and mapping endpoint gates,lines138–179
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: predicate-wordform
  issue_key: facultatively-anaerobic-predicate-wordform
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: One predicate label differs from the fixed repository wordform
  description: Edge6 has free-text predicate enable. That form can be grammatical
    with its plural surface subject,but CURATION_PLAYBOOK explicitly fixes predicate
    labels to third-person singular and gives enables rather than enable as its example.
    This is a vocabulary normalization inconsistency only. No predicate_id is present
    here,so this finding does not import the RO executor criticism from edge0 or adjudicate
    the biological claim.
  target_ids:
  - METPO:1000605
  field_paths:
  - causal_graphs[0].edges[6].predicate
  evidence_ids:
  - predicate-label-policy
  - record
  - node-edges
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/facultatively_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: facultatively-anaerobic-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked in the inspected local provenance
  description: The current mapping status is REVIEWED,while seven history events disclose
    six AI-assisted changes and one automated seed. The declared ignored-inclusive
    target and graph/node searches found no explicit target human scientific-acceptance
    link in local history or review targets. Native policy requires human sign-off
    for REVIEWED. This is a bounded provenance gap,not proof that no human reviewed
    the record privately or remotely,and does not make the definition or examples
    false.
  target_ids:
  - METPO:1000605
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - graph-owner-search
  - native-policy
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/facultatively_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-external-relation-roles
  description: Reconcile the two existing external predicate assignments with their
    represented roles and maintained mapping owners.
  finding_ids:
  - external-predicate-roles
  target_ids:
  - METPO:1000605
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/facultatively_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Any retained identifier agrees with both endpoint kinds and its textual role;preserve
    valid material/process identities instead of retyping them solely to retain a
    process-only relation.
  - Address mapping recurrence together with the record;no compulsory replacement
    CURIE,new causal step or mechanistic completion is prescribed.
  - Keep all eight detailed biological claims unassessed within this documentary review;formal
    correction does not certify pathogen fitness or respiration biology.
  - Any separately authorized change uses guarded writes and append-only record/repository
    history,focused native validation and maintained relevant audits/QC;regenerate
    affected outputs with existing recipes. This review performs no such mutation.
- action_id: normalize-predicate-label
  description: Apply the documented canonical predicate wordform to the existing free-text
    label.
  finding_ids:
  - predicate-wordform
  target_ids:
  - METPO:1000605
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/facultatively_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The edge6 label follows the fixed third-person-singular vocabulary convention
    while preserving its existing scientific content.
  - The normalization alone does not create a predicate_id or import an external executor
    meaning;inspect maintained writer recurrence before subsequent automated grounding.
  - No new mechanism,endpoint,condition or organism-specific assertion is introduced.
  - Any separately authorized change uses guarded writes and append-only record/repository
    history,focused native validation and maintained relevant audits/QC;regenerate
    affected outputs with existing recipes. This review performs no such mutation.
- action_id: link-human-acceptance
  description: Link existing human scientific acceptance or obtain it through the
    established review process.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000605
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/facultatively_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The acceptance record identifies the reviewed revision and actual scientific scope,including
    the one unverified quotation and all eight biological claims unassessed here.
  - Preserve AI disclosure and append-only provenance. Automated validation,this agent
    review and inherited ontology metadata are not substitutes for human scientific
    acceptance;reassess status if required.
limitations:
- All eight detailed biological edge claims remain UNASSESSED_SCOPE. Source identity,quotation
  fidelity,formal roles and generic classification do not validate pathogen fitness,respiration,regulatory
  or engineering mechanisms. No target,step,condition,replacement mechanism or optimization
  is proposed.
- Two complete XML files were available,but only the assigned generic classification/quotation
  passages were inspected. Other sources were indexed title,abstract,chapter-excerpt
  or metadata surfaces;availability is not full-body review.
- One assigned graph quotation remains unverified because its actual body was not
  obtained. Abstract nonmatch is inconclusive. The CMI phrase is exact title text,which
  establishes literal fidelity rather than edge support.
- The canonical S.aureus source reports DSM20231T as known to have the phenotype.
  No newly measured oxygen-growth assay,genome-derived causation or all-strain uniformity
  is inferred. The E.coli canonical review and graph review are distinct publications.
- The DOI10.1101/2025.01.08.631794 source is explicitly a preprint in inspected metadata.
  No journal peer-review status or later-version search is claimed. An engineering
  or infection-focused title alone does not establish wrong citation.
- The generic definition is supported by an actual indexed chapter excerpt linked
  to NBK482349. Failed browser challenges and footer-only pages were not article text;the
  original failures remain retained.
- External RO meanings come from a hash-identified cached authority,with original09:52read
  and B6reuse times distinguished. GO,ChEBI and NCBI responses retain their original07:14,08:46
  and09:57 acquisition bounds;no new ontology-release certification is implied.
- Common diagnostics,B3 history and actual B5 QC are reused within recorded byte-equality
  scope,with original dates,failed product attempts,network retry and no-adapter skips.
  B6 environment readiness is separate from a fresh execution. Native success does
  not certify all source or biological claims.
- Catalog membership is positive for both canonical species but no downstream gene/module
  or fitness query was performed. Historical runner discovery is bounded B5/external
  reuse,not fresh B6 or global absence;dataset membership does not imply all strains
  or this record are validated.
- The free-text edge6 convention concerns a fixed predicate label,not ordinary subject-verb
  grammar or an unasserted RO identifier. The other free-text relations impose no
  invented external constraints.
- No human scientific-acceptance link was found within the declared ignored-inclusive
  local scope. Remote/private acceptance remains unknown;AI disclosure,seeding and
  this agent review are not human sign-off.
- No scientific record,mapping,history,generated product,environment or Git state
  was modified by this review. No paid research,experimental procedure or organism
  intervention was performed.
notes:
- Three findings:one major and two minor;all node/edge indices are zero-based.
- Native59-input capture10:24:38–39Z followed full target read;all captured hashes
  independently match. No missing target-history capture was identified.
- Source ledger finalized10:28:26.412575Z with9references9publications13placements6snippets5exact1unknown.
  Full-field review is distinct from complete mechanistic or whole-body source verification.
- Seven history events comprise six explicit AI-assisted changes plus one automated
  seed;two protein nodes are reviewed-label-only and there are zero instances.
- B5 full QC executed10:21:03–10:23:38Z. Original B3 history and OLD common diagnostic
  failures/retry/skips remain in the reused evidence chain.
tags:
- record-review
- facultatively-anaerobic
- environment
- needs-curation
```
