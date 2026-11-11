# Whole-record review of strictly anaerobic

- Review: 20261021T231810Z-strictly-anaerobic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T23:09:24.391328Z
- Finished UTC: 2026-10-21T23:18:10Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact METPO identity, hierarchy and canonical species/classification are supported. Three major issues concern the absolute growth definition, the anoxic-condition PATO referent and an imported process relation; one minor concerns bounded local human-acceptance traceability. Six work identities resolve, four supplied snippets are literal and two remain unknown. Detailed oxygen/ROS survival and enzyme biology is explicitly unassessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: First record of the actual locally initialized batch 013 queue. Entire 228-line target and all 61 captured inputs verified before assessment. Local continuation follows verified B12 local finalization and does not assert remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000611 | data/traits/environment/strictly_anaerobic.yaml | maintained | strictly anaerobic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000611 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000611 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000611 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000611 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000611 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000611 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000611 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000611 | Successful schema validation; source semantics separately assessed. |
| Focused strict validation | passed | True | METPO:1000611 | Successful strict validation; no detailed biological certification. |
| Focused network snippet check | passed | True | METPO:1000611 | Five fields over two references: three VERIFIED and two NOT_IN_ABSTRACT. Separate manual six-field accounting gives four literal and two unknown; no false quotation inferred from inaccessibility. |
| Reused maintained batch-twelve QC | passed | True | METPO:1000611 | Actual prior QC qualified against B13 bytes; local continuation is independent of publication. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000611 | Four reviewed label-only protein aggregates and no instances; no forced accession or instance. |

## Scientific And Domain Assessments

### Native checklist: active term and exact taxonomy

identity: supported. Targets: METPO:1000611.

Active METPO1000611 and parent1000607 identify the current class; official817 is B. fragilis. A separate source-scope finding does not negate these identities.

### Native checklist: absolute growth criterion

evidence: concern. Targets: METPO:1000611.

Assigned canonical primary calls B. fragilis a strict anaerobe while reporting growth with oxygen present. Absolute wording in the definition and linked descriptions exceeds that classification evidence; survival and growth endpoints remain distinct.

### Native checklist: parent and related synonym

identity: supported. Targets: METPO:1000611.

Active direct parent and RELATED synonym are coherent documentary context. Faithful imported wording does not resolve the independent source-scope conflict, and related synonymy is not exact equivalence.

### Native checklist: six works and twelve placements

evidence: unknown. Targets: METPO:1000611.

All identities resolved; current/reused metadata times are distinct. Detailed enzyme, oxygen/ROS survival and intervention material remains UNASSESSED_SCOPE. No title-only mechanistic support is inferred.

### Native checklist: six snippets and three quoted notes

evidence: unknown. Targets: METPO:1000611.

Four supplied snippets are literal: three indexed abstract matches and one retained-body phrase-only match. NBK and Cdiff phrases remain unknown, not false quotes. Three detailed quoted mechanism notes are unassessed.

### Native checklist: B. fragilis classification

evidence: supported. Targets: METPO:1000611.

Exact species identity and assigned author strict-anaerobe classification are positive. The title supplies the growth-scope counterexample, not a wrong-species finding. Abundance/model language and alternative examples remain unverified.

### Native checklist: all eight referents

consistency: concern. Targets: METPO:1000611.

Anoxic environmental absence is distinct from PATO1456 bearer oxygen independence. Two chemical identities and four label-only aggregates are formally positive; their detailed biological vulnerabilities remain unassessed.

### Native checklist: all seven relation roles

consistency: concern. Targets: METPO:1000611.

RO2212 edge1 has chemical and trait endpoints, contrary to inherited process/process roles. Local confers and Biolink formal gates are compatible; lexical edges have no invented imported constraints. Biological efficacy remains unassessed.

### Native checklist: restricted scientific reading

scope: unknown. Targets: METPO:1000611.

Only general classification, exact identity and existing literal attribution are assessed. Detailed pathogen oxygen/ROS survival, enzyme/defense, mutant/intervention mechanisms, culture parameters and optimization are UNASSESSED_SCOPE.

### Native checklist: contextual graph and proteins

completeness: supported. Targets: METPO:1000611.

One NONMECHANISTIC component, four reviewed label-only protein aggregates and no instances do not require additional connectors, accessions or examples.

### Native checklist: canonical catalog scope

evidence: unknown. Targets: METPO:1000611.

Retained20-organism/28-dataset catalog lacks an exact B. fragilis canonical match. This is no broad source-organism absence or biological conclusion; no detailed module query was performed.

### Native checklist: current record and conditional owners

provenance: supported. Targets: METPO:1000611.

Record owns existing assertions. Exact node/predicate mappings and generic grounders affect future empty fields and skip existing nonempty IDs. Current confers and oxygen selectors are excluded from historical migrations on replay; sibling writers remain context.

### Native checklist: bounded acceptance trace

provenance: concern. Targets: METPO:1000611.

Eleven AI events plus a seed, two whole contextual histories,187 ignored-inclusive matching paths and67 parsed review arrays with zero exact targets do not establish attributable current acceptance. Private/remote review remains unknown.

### Native checklist: actual checks and qualified reuse

consistency: supported. Targets: METPO:1000611.

All61 current inputs match and focused checks passed. Original errors/retries/skips and source acquisitions remain explicit. Reused B12 QC and B13 local initialization do not assert new QC or publication.

## Findings

### absolute-oxygen-growth-scope: Absolute growth wording exceeds the assigned classification evidence

major / open / confirmed; issue key: strictly-anaerobic-absolute-oxygen-growth-scope.

The record states no growth in the presence of oxygen and requires oxygen-excluding conditions, while its own canonical primary calls B. fragilis a strict anaerobe and reports growth with oxygen present. Canonical identity and author classification remain positive. This concerns documentary scope, not a new mechanism or culture-condition prescription.

### anoxic-anaerobic-grounding: Environmental absence and bearer oxygen independence are conflated

major / open / confirmed; issue key: strictly-anaerobic-anoxic-anaerobic-grounding.

Current node1 denotes oxygen-excluding environmental conditions; actual PATO1456 denotes independence of oxygen in a bearer. The referents differ independently of the source growth-scope issue. No replacement identifier or biological repair is proposed.

### imported-process-roles: Imported process regulation has incompatible current endpoints

major / open / confirmed; issue key: strictly-anaerobic-imported-process-roles.

RO2212 inherits process/process roles from RO2211, but edge1 represents a chemical subject and trait object. This formal defect is independent of whether oxygen inhibits particular biological activity.

### human-acceptance-link: Reviewed status lacks a locally attributable acceptance link

minor / open / confirmed; issue key: strictly-anaerobic-human-acceptance-link.

Bounded ignored-inclusive local evidence does not establish attributable current-target acceptance: eleven AI events plus a seed, two histories and zero exact current targets among67 review arrays. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### reconcile-classification-scope

Resolve documentary scope between trait wording and assigned classification evidence.

- Preserve exact canonical identity and author classification.
- Keep growth and survival endpoints distinct; reconcile only definition and node0/node1 descriptions with the assigned primary classification scope.
- After authorized edits, run just validate and just validate-strict for data/traits/environment/strictly_anaerobic.yaml.
- No culture parameters, mechanism reconstruction or optimization.

### reconcile-node-grounding

Reconcile the environmental referent with its ontology grounding during authorized curation.

- Use actual authority definitions and exact current mapping context.
- Respect skip-existing guards; no automatic replacement identifier.
- Review python scripts/ground_causal_nodes.py in its default dry-run mode with scratch --out, without --apply; verify the exact mapping key and unchanged nonempty-ID guard.
- After authorized edits, run just validate and just validate-strict for the current record.

### reconcile-relation-roles

Reconcile imported relation semantics with represented endpoints.

- Preserve formal positive controls and detailed biology exclusions.
- Respect nonempty-ID guards; no mechanistic repair prescription.
- Review python scripts/ground_causal_predicates.py in its default dry-run mode with scratch --out, without --apply; verify RO2212 roles independently of the mapping.
- After authorized edits, run just validate and just validate-strict for the current record.

### link-human-acceptance

Link attributable acceptance if available or clarify status while preserving provenance.

- Retain bounded search evidence and events; any acceptance link must identify the current target and reviewed version.
- After authorized provenance edits, run just validate and just validate-strict for the current record.
- No contact or automatic status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. |
| check-validate-history | /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-strictly-anaerobic-validate | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-validate.log; Executed 2026-10-21T23:09:41.135081+00:00 through 2026-10-21T23:09:41.783205+00:00; metadata strictly-anaerobic-validate.json | context_only | Successful schema validation; source semantics separately assessed. |
| check-strictly-anaerobic-strict | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-strict.log; Executed 2026-10-21T23:09:41.135080+00:00 through 2026-10-21T23:09:41.998972+00:00; metadata strictly-anaerobic-strict.json | context_only | Successful strict validation; no detailed biological certification. |
| check-strictly-anaerobic-snippets-network | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-snippets-network.log; Executed 2026-10-21T23:09:51.024976+00:00 through 2026-10-21T23:09:54.576057+00:00; metadata strictly-anaerobic-snippets-network.json | context_only | Five fields over two references: three VERIFIED and two NOT_IN_ABSTRACT. Separate manual six-field accounting gives four literal and two unknown; no false quotation inferred from inaccessibility. |
| check-batch012-qc | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log; Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00; metadata batch012-qc.json | context_only | Actual prior QC qualified against B13 bytes; local continuation is independent of publication. |
| record | data/traits/environment/strictly_anaerobic.yaml; Entire current228-line record | supports | All eight nodes, seven edges, six snippets, three quoted notes and one canonical example accounted. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Actual referents and optional protein applicability. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Copied spans and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current node/relation facets. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Whole-record checklist. |
| node-mapping-primary | mappings/node_grounding.tsv; Captured maintained authority | supports | Exact node row42 is conditional for future empty grounding. |
| predicate-mapping-primary | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Exact predicate row58 does not erase imported process roles. |
| reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json; Actual B12-to-B13 qualification | supports | Original outcomes and current byte comparisons. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json; Independent actual-output verification | supports | Actual qualification output/hash postcheck, not new QC. |
| local-init | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual local initialization preserves separately observed publication status. |
| capture | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/capture-verification.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | All61 captured inputs verified before assessment. |
| identity | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/identity-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Active exact target and parent; imported wording distinguished from source scope. |
| node-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/node-edge-grounding-ledger.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Complete eight-node/seven-edge ledger with positive controls and excluded biology. |
| owners | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/owner-provenance-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Record plus exact conditional mapping/grounder responsibility; sibling writers contextual. |
| expression | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/expression-and-readiness.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Exact canonical absence in retained catalog; no broader source-species absence claim or module query. |
| catalog-reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/catalog-reuse-receipt.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Original catalog access and current copy distinct. |
| local-authority | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/local-authority-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual v8 confers gate is formally compatible. |
| owner-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/owner-primary-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Exact skip-existing grounding guards and contextual migration selectors. |
| ground-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/reading-scope-receipt.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual primary scope, two whole histories and twelve events. |
| ground-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/evidence-manifest.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Frozen28 grounding artifacts verified. |
| ground-disposition | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/documentary-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Final grounding subset and nonfindings. |
| metpo-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl; Selected actual primary ontology statements; projection separately retained | supports | Active exact1000611 and parent1000607; faithful imported absolute wording is still subject to source-scope reconciliation. |
| metpo-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/metpo-authority.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Bounded primary-reading projection, not the raw authority itself. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Selected actual primary ontology statements; projection separately retained | supports | RO2212 inherits RO2211 process/process roles. |
| ro-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/selected-ro-primary-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Bounded primary-reading projection, not the raw authority itself. |
| pato-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db; Selected actual primary ontology statements; projection separately retained | supports | PATO1456 means oxygen independence of a bearer, not environmental oxygen absence. |
| pato-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/selected-pato-primary-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Bounded primary-reading projection, not the raw authority itself. |
| chebi-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/chebi.db; Selected actual primary ontology statements; projection separately retained | supports | Both chemical identities positive; no toxicology assessment. |
| chebi-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/selected-chebi-primary-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Bounded primary-reading projection, not the raw authority itself. |
| biolink-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/biolink-model.yaml; Selected actual primary ontology statements; projection separately retained | supports | Broad NamedThing endpoints and material-subject prose do not create an additional formal defect. |
| biolink-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/biolink-primary-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Bounded primary-reading projection, not the raw authority itself. |
| taxon | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/taxon817-network-retry.xml; Whole successful official XML; initial DNS error separate | supports | Exact Bacteroides fragilis species817 identity; no phenotype inference. |
| taxon-access | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/taxonomy-access-network-retry.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Official success acquired23:10:35; first XML-named file is DNS error text. |
| meta-book | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/book-metadata-reused.json; Exact reused indexed metadata; original acquisition time | supports | Indexed Anaerobic Infections identity/general classification only; book survival quotation unknown and no body claim. |
| meta-oxygen-review | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/oxygen-review-metadata-reused.json; Exact reused indexed metadata; original acquisition time | supports | Assigned review identity and three supplied abstract literal matches; detailed molecular biology unassessed. |
| meta-detox | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/detox-metadata-reused.json; Exact reused indexed metadata; original acquisition time | supports | Assigned ISME work identity/status only; mechanism abstract and body unassessed. |
| literal-body | /private/tmp/traitmech-record-sweep-009.x21w9b3v/obligately-anaerobic-source-agent/oxygen-review-bioc.xml; Existing supplied phrase only; BioC passage218 offset58317 | supports | Literal-only match for the supplied hypoxic/anoxic phrase. Surrounding mechanism text not scientifically read or newly copied. |
| meta-canonical | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/canonical-metadata-network-retry.json; Successful fresh indexed metadata; initial DNS error retained separately | supports | Actual primary title calls B. fragilis a strict anaerobe while reporting growth with oxygen present; generic classification/survival distinction only, no mechanism or culture parameters. |
| meta-example | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/example-metadata-network-retry.json; Successful fresh indexed metadata; initial DNS error retained separately | supports | PMID39189748 author obligate-anaerobe classification positive; supplied phrase abstract miss, body unassessed. Comment-in notice is not a retraction. |
| meta-enzyme | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/enzyme-metadata-network-retry.json; Successful fresh indexed metadata; initial DNS error retained separately | supports | IAI work identity/status only; no detailed mechanism abstract/body assessment. |
| sources | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Six identities and all placement coverage; overall UNKNOWN for excluded detailed claims. |
| source-status | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-status-ledger.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Six identities, bounded notice scope, commentary versus correction distinguished. |
| placements | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-placement-ledger.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | All12 external placements assessed individually. |
| snippets | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/snippet-ledger.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Six snippets: four literal and two unknown; three detailed quoted notes unassessed. |
| node-sources | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/node-edge-source-ledger.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Complete eight-node/seven-edge source scope ledger. |
| source-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/primary-reading-scope.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual restricted general classification/identity/literal scopes. |
| source-access | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-access-limits.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | NBK CAPTCHA, unknown Cdiff body, opaque mechanism sources; error bytes not primary metadata. |
| source-reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-reuse-receipt.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Original acquisition, current copy and literal-only matching times separate. |
| canonical-scope | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/canonical-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Canonical identity/classification positive; same assigned source challenges absolute trait wording. |
| native-checks | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/native-check-context.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Root-owned validate/strict/network commands and actual native counts. |
| source-capture | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/input-verification.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | All61 inputs verified before source judgment. |
| source-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/evidence-manifest.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Frozen25 source artifacts verified. |
| source-construction | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-ledger-construction-correction.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Wrong synonym projection key corrected before freeze; original script/partial outputs retained, no native failure. |
| root-reading-72 | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/canonical-title-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual bounded root reading receipt; not raw primary text or a full mechanism assessment. |
| root-reading-73 | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/formal-authority-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual bounded root reading receipt; not raw primary text or a full mechanism assessment. |
| root-reading-74 | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/fresh-metadata-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual bounded root reading receipt; not raw primary text or a full mechanism assessment. |
| root-reading-75 | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/grounding-ledger-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual bounded root reading receipt; not raw primary text or a full mechanism assessment. |
| root-reading-76 | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/identity-hierarchy-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual bounded root reading receipt; not raw primary text or a full mechanism assessment. |
| root-reading-77 | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/owners-and-provenance-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual bounded root reading receipt; not raw primary text or a full mechanism assessment. |
| root-reading-78 | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/source-ledger-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual bounded root reading receipt; not raw primary text or a full mechanism assessment. |
| challenge | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-semantic-challenge-agent/semantic-severity-challenge.json; Final independent challenge | supports | Actual disposition and bindings verified. |
| adjudication | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-root-adjudication.json; Final root disposition | supports | Final findings control serialization. |

## Limits And Additional Notes

- Detailed pathogen oxygen/ROS survival, enzyme/defense, mutant and intervention mechanisms, culture parameters and optimization remain UNASSESSED_SCOPE.
- Canonical author classification and exact species identity are positive; the same title qualifies the absolute growth criterion. No precise experimental condition or mechanism is proposed.
- NBK CAPTCHA does not support the supplied survival-threshold quotation; Cdiff abstract miss is inconclusive. Neither is treated as a false quote.
- Four short supplied snippets are literal; exactness does not establish causal biological efficacy. Three detailed quoted notes remain unassessed.
- Reused indexed metadata preserves original acquisition times. Fresh initial DNS errors are not source responses, and a Comment-in annotation is not a correction or retraction.
- The retained body was queried only for an existing short phrase; surrounding mechanism text was not scientifically read or newly copied.
- Canonical catalog absence is bounded and does not imply broad source-species absence or require protein instances or graph expansion.
- Qualified historical diagnostics and local initialization do not certify fresh B13 QC or remote publication; private acceptance remains unknown.
- Final root and independent challenge pins verified; builder/helper have not been imported or executed during preparation.
- Coverage: six works, twelve external placements, seven grounding fields, eight nodes/seven edges, six snippets, three quoted notes, one canonical example, one component, twelve events and two whole contextual histories.
- Standalone source preparation corrected synonym.source projection before freeze; this was not a native or review validation failure. Scientific records, Git and sweep state are not modified by this serializer preparation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T231810Z-strictly-anaerobic
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of strictly anaerobic
started_at: '2026-10-21T23:09:24.391328Z'
finished_at: '2026-10-21T23:18:10Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits, independent semantic challenge
    and root primary/owner readings. Only general classification, canonical identity,
    existing literal spans, documentary scope and formal roles assessed. Detailed
    pathogen oxygen/ROS survival, enzyme/defense, mutant and intervention mechanisms,
    culture parameters and optimization remain UNASSESSED_SCOPE.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Exact METPO identity, hierarchy and canonical species/classification are
  supported. Three major issues concern the absolute growth definition, the anoxic-condition
  PATO referent and an imported process relation; one minor concerns bounded local
  human-acceptance traceability. Six work identities resolve, four supplied snippets
  are literal and two remain unknown. Detailed oxygen/ROS survival and enzyme biology
  is explicitly unassessed.
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
  - path: conf/record_review.yaml
    sha256: 5adc6244761fb2baf8a059d81f23b0c9b32a33f9426ab84094234c3ec417269d
    role: context
  - path: data/raw/biolink-model.yaml
    sha256: 4955709e1cac1d26fd657f7a0c29d6c8390f42e41f9ebfab859c82b102f2bebb
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/environment/obligately_anaerobic.yaml
    sha256: 1b12125f8ec6d84631f89b837dd2568e670cdeca8997b3afabca31c122130a60
    role: context
  - path: data/traits/environment/strictly_anaerobic.yaml
    sha256: f7872f0e68be32ac4e6ccb62c33212750018544dfe7ab67446f1e1b1b2893bd0
    role: target
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
  - path: history/infrastructure/oxygen-senses/2026-08-17T031421Z-claude-code-76561e.yaml
    sha256: 2a021c768e6db37eed31e3ab73c9714bd85ef31bc5f04e986ac0642c16fbe2a3
    role: context
  - path: history/records/fumarate_respiration/2026-09-15T002553Z-codex-389845.yaml
    sha256: f85c236e6eabde0d2c7a731e7893c36284d7a62aeea7d2109bc9de0328742bc8
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
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
    role: context
  - path: proposals/metpo_traitmech_v8/proposal.md
    sha256: 119d51e7b7194890514a9e313505212bab92aeba607f7c1b8f9d9d2edeef67e7
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
  - path: research/traits/environment/strictly_anaerobic-deep-research-falcon.md
    sha256: 11b1e6b2a642eff5cc9293334a207dcc4231cf85524773ba799414c4a1c3f490
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_fumarate_respiration_trait.py
    sha256: ce55e178c3b67b572ccb145b279d187f062f4b4da7165a3fc24d20cab71e4350
    role: context
  - path: scripts/add_selenate_respiration_trait.py
    sha256: e34bf139883b8f763e4c429717fd2b62c84fd72a9dbef4d2c97043f1d28f48bf
    role: context
  - path: scripts/audit_causal_graphs.py
    sha256: e0c26506c9de712700317284f142097e7bf69334806b8010db5d6517e905e834
    role: context
  - path: scripts/audit_graph_protein_taxa.py
    sha256: d3375861829c612483b3545dd0f5e2b79872a4576b626edc08714a09fbd9a24d
    role: context
  - path: scripts/audit_predicate_domains.py
    sha256: 35be8589638b8b21379f2dfd7fa7fb7d4eb422ccf71063e1e21a6bc19b767bcf
    role: context
  - path: scripts/audit_unapplied_groundings.py
    sha256: 5afa6a602f0d7d5107adebf8b067d61bde9ea9adb267f9dfaed8a0b7cc0cc76b
    role: context
  - path: scripts/audit_uniprot_grounding.py
    sha256: 91eb2165c69b3a4fcb53154dc8c835ac1070577f88065a43dfc881284d3d1052
    role: context
  - path: scripts/backfill_canonical_examples_444.py
    sha256: 18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c
    role: context
  - path: scripts/document_evidence_reference_churn.py
    sha256: 84f8638faa59e3909cdde0ccf2efbdf98521c8c423367fa78c139726ea545669
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
  - path: scripts/migrate_enables_range_edges.py
    sha256: 3d0d1bddcaa76baef5833973e2e979e4fee1f834c67d1abcc69a8d866ecb8f32
    role: context
  - path: scripts/migrate_enables_trait_edges.py
    sha256: a5e7965ee4f6b6ba5bae3a06bced2a83cbf755f3b9b150ce6acc0cd808cb1d88
    role: context
  - path: scripts/migrate_metpo_2026_06_12.py
    sha256: 0f3945e7b8e6ddccdc9eaeed32737a2a1cf0832748af2b72a6a0195ba661188f
    role: context
  - path: scripts/migrate_microbe_domain_edges.py
    sha256: 5187ccfb2897d415b243792a27afd6002c0eea4b167068639ff5be73ed583bb6
    role: context
  - path: scripts/migrate_name_match_groundings.py
    sha256: 9b3ea1153839b9b260638cef95eba2d1ccc6d7b3825e7352c33cceb21bfe4dd4
    role: context
  - path: scripts/migrate_node_type_consistency.py
    sha256: a3e7bc170e60f406a73e06c893d74f5253671028d3d40cc15ecf882b6684a69e
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
  - path: scripts/migrate_remaining_microbe_domain_edges.py
    sha256: 110542d49e25007122c7c254966ad87dc3f7f054358766e933aff89e8ef0a994
    role: context
  - path: scripts/migrate_uniprot_instance_groundings.py
    sha256: 07d2a5405cff5857239757e0a3791f411b1d25709a5760c1e49553eed066993d
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
- target_id: METPO:1000611
  path: data/traits/environment/strictly_anaerobic.yaml
  label: strictly anaerobic
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/strictly_anaerobic.yaml
    role: Maintained target; read-only review.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained predicate context; recurrence assessed only after capture.
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Maintained grounding context; recurrence assessed only after capture.
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: First record of the actual locally initialized batch 013 queue. Entire
    228-line target and all 61 captured inputs verified before assessment. Local continuation
    follows verified B12 local finalization and does not assert remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000611
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000611
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC ran23:02:31.440808–23:04:01.628423UTC; B13 byte qualification
    completed23:05:39.165510 and independent postcheck23:07:53.187524. Original failures/retries/skips
    and seven-file delta remain explicit; no fresh B13 QC or remote publication claimed.
    Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000611
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC ran23:02:31.440808–23:04:01.628423UTC; B13 byte qualification
    completed23:05:39.165510 and independent postcheck23:07:53.187524. Original failures/retries/skips
    and seven-file delta remain explicit; no fresh B13 QC or remote publication claimed.
    Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000611
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot.
  evidence_ids:
  - check-check-pathway-links
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC ran23:02:31.440808–23:04:01.628423UTC; B13 byte qualification
    completed23:05:39.165510 and independent postcheck23:07:53.187524. Original failures/retries/skips
    and seven-file delta remain explicit; no fresh B13 QC or remote publication claimed.
    Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000611
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC ran23:02:31.440808–23:04:01.628423UTC; B13 byte qualification
    completed23:05:39.165510 and independent postcheck23:07:53.187524. Original failures/retries/skips
    and seven-file delta remain explicit; no fresh B13 QC or remote publication claimed.
    Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000611
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC ran23:02:31.440808–23:04:01.628423UTC; B13 byte qualification
    completed23:05:39.165510 and independent postcheck23:07:53.187524. Original failures/retries/skips
    and seven-file delta remain explicit; no fresh B13 QC or remote publication claimed.
    Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000611
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC ran23:02:31.440808–23:04:01.628423UTC; B13 byte qualification
    completed23:05:39.165510 and independent postcheck23:07:53.187524. Original failures/retries/skips
    and seven-file delta remain explicit; no fresh B13 QC or remote publication claimed.
    Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000611
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC ran23:02:31.440808–23:04:01.628423UTC; B13 byte qualification
    completed23:05:39.165510 and independent postcheck23:07:53.187524. Original failures/retries/skips
    and seven-file delta remain explicit; no fresh B13 QC or remote publication claimed.
    Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: strictly-anaerobic-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000611
  command: just validate data/traits/environment/strictly_anaerobic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful schema validation; source semantics separately assessed.
  evidence_ids:
  - check-strictly-anaerobic-validate
- check_id: strictly-anaerobic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000611
  command: just validate-strict data/traits/environment/strictly_anaerobic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful strict validation; no detailed biological certification.
  evidence_ids:
  - check-strictly-anaerobic-strict
- check_id: strictly-anaerobic-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000611
  command: just verify-snippets --record data/traits/environment/strictly_anaerobic.yaml
    --out /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-snippets-network.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Five fields over two references: three VERIFIED and two NOT_IN_ABSTRACT.
    Separate manual six-field accounting gives four literal and two unknown; no false
    quotation inferred from inaccessibility.'
  evidence_ids:
  - check-strictly-anaerobic-snippets-network
- check_id: batch012-qc
  name: Reused maintained batch-twelve QC
  status: passed
  required: true
  target_ids:
  - METPO:1000611
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual prior QC qualified against B13 bytes; local continuation is independent
    of publication.
  evidence_ids:
  - check-batch012-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000611
  summary: Four reviewed label-only protein aggregates and no instances; no forced
    accession or instance.
  evidence_ids:
  - record
  - policy
  - node-edges
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-19T07:33:29Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-19T07:33:33Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-19T07:33:28Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T07:03:30Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-19T07:34:01Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-19T07:35:24Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-19T07:36:03Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-strictly-anaerobic-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-validate.log
  locator: Executed 2026-10-21T23:09:41.135081+00:00 through 2026-10-21T23:09:41.783205+00:00;
    metadata strictly-anaerobic-validate.json
  accessed_at: '2026-10-21T23:09:41.783205Z'
  support: context_only
  summary: Successful schema validation; source semantics separately assessed.
  snapshot_sha256: 8b75c48238e9e1c77a9447979371ccb24360b714e30765ea0a335d688543514b
- evidence_id: check-strictly-anaerobic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-strict.log
  locator: Executed 2026-10-21T23:09:41.135080+00:00 through 2026-10-21T23:09:41.998972+00:00;
    metadata strictly-anaerobic-strict.json
  accessed_at: '2026-10-21T23:09:41.998972Z'
  support: context_only
  summary: Successful strict validation; no detailed biological certification.
  snapshot_sha256: d660e6a3c00439b1fa8c77ac456e2c18d35cafbc4717b4de32300583b7293da6
- evidence_id: check-strictly-anaerobic-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-snippets-network.log
  locator: Executed 2026-10-21T23:09:51.024976+00:00 through 2026-10-21T23:09:54.576057+00:00;
    metadata strictly-anaerobic-snippets-network.json
  accessed_at: '2026-10-21T23:09:54.576057Z'
  support: context_only
  summary: 'Five fields over two references: three VERIFIED and two NOT_IN_ABSTRACT.
    Separate manual six-field accounting gives four literal and two unknown; no false
    quotation inferred from inaccessibility.'
  snapshot_sha256: d8d7b607e7baff93c0fdcd5a920622051235b88ead4ecd1e022387f85fabe03e
- evidence_id: check-batch012-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log
  locator: Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00;
    metadata batch012-qc.json
  accessed_at: '2026-10-21T23:04:01.628423Z'
  support: context_only
  summary: Actual prior QC qualified against B13 bytes; local continuation is independent
    of publication.
  snapshot_sha256: 8ab67b821055863ce13616ed79a0acacaf61b632dcb80f6aa63fd45f0485c52b
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/strictly_anaerobic.yaml
  locator: Entire current228-line record
  accessed_at: '2026-10-21T23:09:25.070166Z'
  support: supports
  summary: All eight nodes, seven edges, six snippets, three quoted notes and one
    canonical example accounted.
  snapshot_sha256: f7872f0e68be32ac4e6ccb62c33212750018544dfe7ab67446f1e1b1b2893bd0
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:12:08.813442Z'
  support: supports
  summary: Actual referents and optional protein applicability.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:12:08.813442Z'
  support: supports
  summary: Copied spans and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:12:08.813442Z'
  support: supports
  summary: Current node/relation facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:12:08.813442Z'
  support: supports
  summary: Whole-record checklist.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: node-mapping-primary
  kind: authority
  reference: mappings/node_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:12:08.813442Z'
  support: supports
  summary: Exact node row42 is conditional for future empty grounding.
  snapshot_sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
- evidence_id: predicate-mapping-primary
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:12:08.813442Z'
  support: supports
  summary: Exact predicate row58 does not erase imported process roles.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json
  locator: Actual B12-to-B13 qualification
  accessed_at: '2026-10-21T23:05:39.165510Z'
  support: supports
  summary: Original outcomes and current byte comparisons.
  snapshot_sha256: e1fa58cb626ef76e2b2066404078b9893b069a5b53a0cffbc3a184e68f0cd9f1
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Independent actual-output verification
  accessed_at: '2026-10-21T23:07:53.187524Z'
  support: supports
  summary: Actual qualification output/hash postcheck, not new QC.
  snapshot_sha256: 42a5580991e7251963a9b83d0817facda019de29d9e13208e870c27e1c62ad7d
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:09:00.804479Z'
  support: supports
  summary: Actual local initialization preserves separately observed publication status.
  snapshot_sha256: cda5c0d3753e7a2a3ceb9ba723261fa79d4f760aad1713ff2d33b08def3577f7
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/capture-verification.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:10:12.428164Z'
  support: supports
  summary: All61 captured inputs verified before assessment.
  snapshot_sha256: c4faf0ced745281a52442692e41635bbbe667d79f3c77daa6792c44d5a6782f5
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/identity-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:08.812653Z'
  support: supports
  summary: Active exact target and parent; imported wording distinguished from source
    scope.
  snapshot_sha256: b2eee897a8134ca010268eab2df55bf64b459584564cae423bd8290d55836af7
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/node-edge-grounding-ledger.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:08.812826Z'
  support: supports
  summary: Complete eight-node/seven-edge ledger with positive controls and excluded
    biology.
  snapshot_sha256: f602210f6b1f776307ff191794d82b3c5ae3d83b775721385d06863af471a7c5
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/owner-provenance-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:08.812941Z'
  support: supports
  summary: Record plus exact conditional mapping/grounder responsibility; sibling
    writers contextual.
  snapshot_sha256: b52075f059bd79b6a84bf94715e95fb2d25bc16a8577c1ad7e8fa93191452286
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/expression-and-readiness.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:08.813206Z'
  support: supports
  summary: Exact canonical absence in retained catalog; no broader source-species
    absence claim or module query.
  snapshot_sha256: 8915931744eb4424b3b13d89699511e0b4cc77cfe80753f469fd90d1abe2921c
- evidence_id: catalog-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/catalog-reuse-receipt.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:10:34.153820Z'
  support: supports
  summary: Original catalog access and current copy distinct.
  snapshot_sha256: 02412a38ca5f4245052fe951ba8c8c54c0acd9e97e88ea83f187b77723a9f207
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/local-authority-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:08.588218Z'
  support: supports
  summary: Actual v8 confers gate is formally compatible.
  snapshot_sha256: 65061854d71927abe52547b84a57d1a8261709b312d7423c0d492f02f6000265
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/owner-primary-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:08.789325Z'
  support: supports
  summary: Exact skip-existing grounding guards and contextual migration selectors.
  snapshot_sha256: f5fb4cce9946de0d411c823537fad38c3a1891239c3aa95a18fc683940ec44cf
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/reading-scope-receipt.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:08.813589Z'
  support: supports
  summary: Actual primary scope, two whole histories and twelve events.
  snapshot_sha256: 6db21f862f8f1c197fecdf997769ca985bef7c3e8969dd7b70e5fdd32bc7e99f
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/evidence-manifest.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:08.818924Z'
  support: supports
  summary: Frozen28 grounding artifacts verified.
  snapshot_sha256: b5f2446b9ef78e820ea0d7e84c93c1f653e39d4472144cf9a7684273720cd2d8
- evidence_id: ground-disposition
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/documentary-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:08.813442Z'
  support: supports
  summary: Final grounding subset and nonfindings.
  snapshot_sha256: 722937b6136c24a564eccf83af49b751fb4ff2b2e35e0f81dbbaf27d459e053a
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl
  locator: Selected actual primary ontology statements; projection separately retained
  accessed_at: '2026-10-21T23:10:14.398425Z'
  support: supports
  summary: Active exact1000611 and parent1000607; faithful imported absolute wording
    is still subject to source-scope reconciliation.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: metpo-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/metpo-authority.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:10:14.398425Z'
  support: supports
  summary: Bounded primary-reading projection, not the raw authority itself.
  snapshot_sha256: 98bc80996ed1c489dcce9abb9dccc2aa1b1cd7f635da19811dbd86747643a539
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Selected actual primary ontology statements; projection separately retained
  accessed_at: '2026-10-21T23:10:12.435290Z'
  support: supports
  summary: RO2212 inherits RO2211 process/process roles.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: ro-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/selected-ro-primary-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:10:12.435290Z'
  support: supports
  summary: Bounded primary-reading projection, not the raw authority itself.
  snapshot_sha256: dcac5d5073eff06ad1da7859a0faecf9391b73e9f791dacb68d092f08c35c962
- evidence_id: pato-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db
  locator: Selected actual primary ontology statements; projection separately retained
  accessed_at: '2026-10-21T23:10:12.440733Z'
  support: supports
  summary: PATO1456 means oxygen independence of a bearer, not environmental oxygen
    absence.
  snapshot_sha256: 179ab512b5c3a8827c74e2a496da575e2908a84740429deef265d58c9ce61d3b
- evidence_id: pato-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/selected-pato-primary-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:10:12.440733Z'
  support: supports
  summary: Bounded primary-reading projection, not the raw authority itself.
  snapshot_sha256: ceb51eb1f647154ddbde839af41f40deb2ba4cbb82cabbbc8cd64c1624633098
- evidence_id: chebi-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/chebi.db
  locator: Selected actual primary ontology statements; projection separately retained
  accessed_at: '2026-10-21T23:10:12.513262Z'
  support: supports
  summary: Both chemical identities positive; no toxicology assessment.
  snapshot_sha256: 26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f
- evidence_id: chebi-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/selected-chebi-primary-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:10:12.513262Z'
  support: supports
  summary: Bounded primary-reading projection, not the raw authority itself.
  snapshot_sha256: fc096a81b1ba3398704642aafab3551e4b094e7dba8004d5b2d79f5362cbf582
- evidence_id: biolink-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/biolink-model.yaml
  locator: Selected actual primary ontology statements; projection separately retained
  accessed_at: '2026-10-21T23:12:08.787312Z'
  support: supports
  summary: Broad NamedThing endpoints and material-subject prose do not create an
    additional formal defect.
  snapshot_sha256: 4955709e1cac1d26fd657f7a0c29d6c8390f42e41f9ebfab859c82b102f2bebb
- evidence_id: biolink-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/biolink-primary-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:08.787312Z'
  support: supports
  summary: Bounded primary-reading projection, not the raw authority itself.
  snapshot_sha256: bb9dbb919e9632b73f84dde64d764b63ac8adeddf282f9d54dfb59f4b8bd2ece
- evidence_id: taxon
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/taxon817-network-retry.xml
  locator: Whole successful official XML; initial DNS error separate
  accessed_at: '2026-10-21T23:10:35.875438Z'
  support: supports
  summary: Exact Bacteroides fragilis species817 identity; no phenotype inference.
  snapshot_sha256: f146c9e49d4be9d733cf672946db0ef42c343c608bf134bf24456fc8547b7bdb
- evidence_id: taxon-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-grounding-agent/taxonomy-access-network-retry.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:10:35.875438Z'
  support: supports
  summary: Official success acquired23:10:35; first XML-named file is DNS error text.
  snapshot_sha256: f3e2501e94a0a85a7e891c16edef79e38e4f3921bf8f45e69a9092ee72be6995
- evidence_id: meta-book
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/book-metadata-reused.json
  locator: Exact reused indexed metadata; original acquisition time
  accessed_at: '2026-10-21T10:25:49.025576Z'
  support: supports
  summary: Indexed Anaerobic Infections identity/general classification only; book
    survival quotation unknown and no body claim.
  snapshot_sha256: 51b8d1584800f6c7ce65ea00267399d0656999482006883ad7aaae4949cd6e71
- evidence_id: meta-oxygen-review
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/oxygen-review-metadata-reused.json
  locator: Exact reused indexed metadata; original acquisition time
  accessed_at: '2026-10-21T15:58:19.564228Z'
  support: supports
  summary: Assigned review identity and three supplied abstract literal matches; detailed
    molecular biology unassessed.
  snapshot_sha256: 31797ff6d30f7def5ac758b895c2bef99d443fe063f754f3a9de05dcd95fd8f6
- evidence_id: meta-detox
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/detox-metadata-reused.json
  locator: Exact reused indexed metadata; original acquisition time
  accessed_at: '2026-10-21T16:25:18.817015Z'
  support: supports
  summary: Assigned ISME work identity/status only; mechanism abstract and body unassessed.
  snapshot_sha256: e8c45bd7f37459db0ea353e2c1ea2e32e6115b3f7b1aa2825c616f538d4afae3
- evidence_id: literal-body
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-009.x21w9b3v/obligately-anaerobic-source-agent/oxygen-review-bioc.xml
  locator: Existing supplied phrase only; BioC passage218 offset58317
  accessed_at: '2026-10-21T08:25:23Z'
  support: supports
  summary: Literal-only match for the supplied hypoxic/anoxic phrase. Surrounding
    mechanism text not scientifically read or newly copied.
  snapshot_sha256: 8ce53770e39dc8f72cd5dc03fff9676954ed0f43c0ac36be40e2b78466239430
- evidence_id: meta-canonical
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/canonical-metadata-network-retry.json
  locator: Successful fresh indexed metadata; initial DNS error retained separately
  accessed_at: '2026-10-21T23:10:39.853649Z'
  support: supports
  summary: Actual primary title calls B. fragilis a strict anaerobe while reporting
    growth with oxygen present; generic classification/survival distinction only,
    no mechanism or culture parameters.
  snapshot_sha256: e56763b548e2961700197c72c782f7b75241577985217b5f2bcb688e0018738e
- evidence_id: meta-example
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/example-metadata-network-retry.json
  locator: Successful fresh indexed metadata; initial DNS error retained separately
  accessed_at: '2026-10-21T23:10:39.887922Z'
  support: supports
  summary: PMID39189748 author obligate-anaerobe classification positive; supplied
    phrase abstract miss, body unassessed. Comment-in notice is not a retraction.
  snapshot_sha256: 1472a662f87bbf310d87db6f3f417cd2e937d698827439ccb667c855f85b3282
- evidence_id: meta-enzyme
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/enzyme-metadata-network-retry.json
  locator: Successful fresh indexed metadata; initial DNS error retained separately
  accessed_at: '2026-10-21T23:10:39.878478Z'
  support: supports
  summary: IAI work identity/status only; no detailed mechanism abstract/body assessment.
  snapshot_sha256: 8e849ba564eb63ba0ad0e3b5603f9f9ed7aa0d763c7873789170449e998fe3c2
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:20.504887Z'
  support: supports
  summary: Six identities and all placement coverage; overall UNKNOWN for excluded
    detailed claims.
  snapshot_sha256: 14a4d1adee8f882883496fefde172812850c610acf2184f7943a1ccc2aef8a9a
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-status-ledger.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:07.690461Z'
  support: supports
  summary: Six identities, bounded notice scope, commentary versus correction distinguished.
  snapshot_sha256: 12e9cdf066ffa91a9d4f916ad491bfba24b2b1031572585a01e2f0d8b821bb64
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-placement-ledger.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:20.501955Z'
  support: supports
  summary: All12 external placements assessed individually.
  snapshot_sha256: a82db25950d99f3d6b55fedf881cb8957c650f2c90f050f78ac9f8428d704d94
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/snippet-ledger.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:20.502640Z'
  support: supports
  summary: 'Six snippets: four literal and two unknown; three detailed quoted notes
    unassessed.'
  snapshot_sha256: e2c1f1e21929187c5ae7086a4b6d64d3bf6344d53353416684957d6011b98b86
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/node-edge-source-ledger.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:20.503367Z'
  support: supports
  summary: Complete eight-node/seven-edge source scope ledger.
  snapshot_sha256: a92a45d8abbd8b6c8dcb44d84bcc2587188150bbc049f9b7bf2fef1f11ef71a8
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/primary-reading-scope.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:20.504380Z'
  support: supports
  summary: Actual restricted general classification/identity/literal scopes.
  snapshot_sha256: 9109e863cecfd437b5e90ab72dc45bc82ebea597a101a1734de064e5fbd57666
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-access-limits.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:07.689858Z'
  support: supports
  summary: NBK CAPTCHA, unknown Cdiff body, opaque mechanism sources; error bytes
    not primary metadata.
  snapshot_sha256: f1d3ae9eb8a35772586330f8249192635ee6d7ab39cfd7c54ee992ccba8bcc06
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-reuse-receipt.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:07.689591Z'
  support: supports
  summary: Original acquisition, current copy and literal-only matching times separate.
  snapshot_sha256: 3f810542961397ec6ecd27b302ab4daedd56f6992d0bdfb4c2f602563aa8eb1e
- evidence_id: canonical-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/canonical-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:20.503054Z'
  support: supports
  summary: Canonical identity/classification positive; same assigned source challenges
    absolute trait wording.
  snapshot_sha256: 29ea8db94e549156c8da0ad105c27c9783f795d43312e689dcad9083788f3586
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/native-check-context.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:20.504182Z'
  support: supports
  summary: Root-owned validate/strict/network commands and actual native counts.
  snapshot_sha256: 1bbb142296333b964359ebf0a4de5b2f58fb52eed4fd2fda65d16fd483253687
- evidence_id: source-capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/input-verification.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:09:50.731942Z'
  support: supports
  summary: All61 inputs verified before source judgment.
  snapshot_sha256: ed06d3688aa672c02223c1b0e13443b95d4a4d2d3566e3c7ea891ddfa0483f5c
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/evidence-manifest.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:20.507511Z'
  support: supports
  summary: Frozen25 source artifacts verified.
  snapshot_sha256: 2e525934f705e0d09e2b1c3aec5d083ffb86b08081e5cb314d99b78e4f397432
- evidence_id: source-construction
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-agent/source-ledger-construction-correction.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:20.460334Z'
  support: supports
  summary: Wrong synonym projection key corrected before freeze; original script/partial
    outputs retained, no native failure.
  snapshot_sha256: 6d18fa5f1831a86976883a7d96bdbebed08557ac5c3e988fbd603f2499ea6250
- evidence_id: root-reading-72
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/canonical-title-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:11:34.896616Z'
  support: supports
  summary: Actual bounded root reading receipt; not raw primary text or a full mechanism
    assessment.
  snapshot_sha256: 900f43ee21561c12683562698e5417a002ff49f65ea8cbcc9884b31fa81c2ab3
- evidence_id: root-reading-73
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/formal-authority-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:11:00.113397Z'
  support: supports
  summary: Actual bounded root reading receipt; not raw primary text or a full mechanism
    assessment.
  snapshot_sha256: 795468acaa7e090951e1ab7ccef7c3eaaea9196e5af708840b479ebb236c748f
- evidence_id: root-reading-74
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/fresh-metadata-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:13:37.157282Z'
  support: supports
  summary: Actual bounded root reading receipt; not raw primary text or a full mechanism
    assessment.
  snapshot_sha256: f50aad0afdc394b838946dcaf134a97c11dffc9912a4ec3f76af4efba0df9c56
- evidence_id: root-reading-75
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/grounding-ledger-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:33.411683Z'
  support: supports
  summary: Actual bounded root reading receipt; not raw primary text or a full mechanism
    assessment.
  snapshot_sha256: 1002305445e983b882f988373b07c505cf8b81c62d2d51d00040afdf46fa7cbe
- evidence_id: root-reading-76
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/identity-hierarchy-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:10:25.476253Z'
  support: supports
  summary: Actual bounded root reading receipt; not raw primary text or a full mechanism
    assessment.
  snapshot_sha256: 1c34ceb83c87e8badc93863a323256e522dc6ca99b445699225e20ede5a1b9a9
- evidence_id: root-reading-77
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/owners-and-provenance-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:12:17.293532Z'
  support: supports
  summary: Actual bounded root reading receipt; not raw primary text or a full mechanism
    assessment.
  snapshot_sha256: 8c3b90f761050d6778b6a73047c7139c102b8324180c7db3d0a6132dd0d5c7cd
- evidence_id: root-reading-78
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-source-root/source-ledger-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:14:42.345511Z'
  support: supports
  summary: Actual bounded root reading receipt; not raw primary text or a full mechanism
    assessment.
  snapshot_sha256: c8d326ec923d799b247323162b3299132ee556e2777332e802eda20a88dffc35
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent challenge
  accessed_at: '2026-10-21T23:15:27.582693Z'
  support: supports
  summary: Actual disposition and bindings verified.
  snapshot_sha256: b88b0d0897f40ae2c471de7bcb028d5dcdbd3a9ac2c8cc8fae0a6b4174401df1
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/strictly-anaerobic-root-adjudication.json
  locator: Final root disposition
  accessed_at: '2026-10-21T23:16:06.980694Z'
  support: supports
  summary: Final findings control serialization.
  snapshot_sha256: bceefeceef5bb243b43a73a1ba0cabe415bf3157ad65d520fb9495c4cff05a65
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active term and exact taxonomy'
  outcome: supported
  target_ids:
  - METPO:1000611
  summary: Active METPO1000611 and parent1000607 identify the current class; official817
    is B. fragilis. A separate source-scope finding does not negate these identities.
  evidence_ids:
  - record
  - identity
  - metpo-primary
  - taxon
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: absolute growth criterion'
  outcome: concern
  target_ids:
  - METPO:1000611
  summary: Assigned canonical primary calls B. fragilis a strict anaerobe while reporting
    growth with oxygen present. Absolute wording in the definition and linked descriptions
    exceeds that classification evidence; survival and growth endpoints remain distinct.
  evidence_ids:
  - sources
  - meta-canonical
  - canonical-scope
  - adjudication
- assessment_id: hierarchy
  area: identity
  topic: 'Native checklist: parent and related synonym'
  outcome: supported
  target_ids:
  - METPO:1000611
  summary: Active direct parent and RELATED synonym are coherent documentary context.
    Faithful imported wording does not resolve the independent source-scope conflict,
    and related synonymy is not exact equivalence.
  evidence_ids:
  - identity
  - metpo-primary
  - sources
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: six works and twelve placements'
  outcome: unknown
  target_ids:
  - METPO:1000611
  summary: All identities resolved; current/reused metadata times are distinct. Detailed
    enzyme, oxygen/ROS survival and intervention material remains UNASSESSED_SCOPE.
    No title-only mechanistic support is inferred.
  evidence_ids:
  - sources
  - placements
  - source-status
  - node-sources
  - source-access
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: six snippets and three quoted notes'
  outcome: unknown
  target_ids:
  - METPO:1000611
  summary: 'Four supplied snippets are literal: three indexed abstract matches and
    one retained-body phrase-only match. NBK and Cdiff phrases remain unknown, not
    false quotes. Three detailed quoted mechanism notes are unassessed.'
  evidence_ids:
  - snippets
  - literal-body
  - source-reading
  - native-checks
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: B. fragilis classification'
  outcome: supported
  target_ids:
  - METPO:1000611
  summary: Exact species identity and assigned author strict-anaerobe classification
    are positive. The title supplies the growth-scope counterexample, not a wrong-species
    finding. Abundance/model language and alternative examples remain unverified.
  evidence_ids:
  - canonical-scope
  - meta-canonical
  - taxon
- assessment_id: nodes
  area: consistency
  topic: 'Native checklist: all eight referents'
  outcome: concern
  target_ids:
  - METPO:1000611
  summary: Anoxic environmental absence is distinct from PATO1456 bearer oxygen independence.
    Two chemical identities and four label-only aggregates are formally positive;
    their detailed biological vulnerabilities remain unassessed.
  evidence_ids:
  - node-edges
  - pato-primary
  - chebi-primary
  - schema
  - policy
- assessment_id: predicates
  area: consistency
  topic: 'Native checklist: all seven relation roles'
  outcome: concern
  target_ids:
  - METPO:1000611
  summary: RO2212 edge1 has chemical and trait endpoints, contrary to inherited process/process
    roles. Local confers and Biolink formal gates are compatible; lexical edges have
    no invented imported constraints. Biological efficacy remains unassessed.
  evidence_ids:
  - node-edges
  - ro-primary
  - local-authority
  - biolink-primary
  - owners
  - adjudication
- assessment_id: biology
  area: scope
  topic: 'Native checklist: restricted scientific reading'
  outcome: unknown
  target_ids:
  - METPO:1000611
  summary: Only general classification, exact identity and existing literal attribution
    are assessed. Detailed pathogen oxygen/ROS survival, enzyme/defense, mutant/intervention
    mechanisms, culture parameters and optimization are UNASSESSED_SCOPE.
  evidence_ids:
  - node-sources
  - source-reading
  - source-access
  - ground-reading
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: contextual graph and proteins'
  outcome: supported
  target_ids:
  - METPO:1000611
  summary: One NONMECHANISTIC component, four reviewed label-only protein aggregates
    and no instances do not require additional connectors, accessions or examples.
  evidence_ids:
  - record
  - node-edges
  - policy
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical catalog scope'
  outcome: unknown
  target_ids:
  - METPO:1000611
  summary: Retained20-organism/28-dataset catalog lacks an exact B. fragilis canonical
    match. This is no broad source-organism absence or biological conclusion; no detailed
    module query was performed.
  evidence_ids:
  - expression
  - catalog-reuse
  - taxon
- assessment_id: ownership
  area: provenance
  topic: 'Native checklist: current record and conditional owners'
  outcome: supported
  target_ids:
  - METPO:1000611
  summary: Record owns existing assertions. Exact node/predicate mappings and generic
    grounders affect future empty fields and skip existing nonempty IDs. Current confers
    and oxygen selectors are excluded from historical migrations on replay; sibling
    writers remain context.
  evidence_ids:
  - owners
  - owner-primary
  - node-mapping-primary
  - predicate-mapping-primary
- assessment_id: human
  area: provenance
  topic: 'Native checklist: bounded acceptance trace'
  outcome: concern
  target_ids:
  - METPO:1000611
  summary: Eleven AI events plus a seed, two whole contextual histories,187 ignored-inclusive
    matching paths and67 parsed review arrays with zero exact targets do not establish
    attributable current acceptance. Private/remote review remains unknown.
  evidence_ids:
  - owners
  - ground-reading
  - playbook
  - challenge
  - adjudication
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: actual checks and qualified reuse'
  outcome: supported
  target_ids:
  - METPO:1000611
  summary: All61 current inputs match and focused checks passed. Original errors/retries/skips
    and source acquisitions remain explicit. Reused B12 QC and B13 local initialization
    do not assert new QC or publication.
  evidence_ids:
  - capture
  - source-capture
  - native-checks
  - reuse
  - reuse-postcheck
  - local-init
findings:
- finding_id: absolute-oxygen-growth-scope
  issue_key: strictly-anaerobic-absolute-oxygen-growth-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Absolute growth wording exceeds the assigned classification evidence
  description: The record states no growth in the presence of oxygen and requires
    oxygen-excluding conditions, while its own canonical primary calls B. fragilis
    a strict anaerobe and reports growth with oxygen present. Canonical identity and
    author classification remain positive. This concerns documentary scope, not a
    new mechanism or culture-condition prescription.
  target_ids:
  - METPO:1000611
  field_paths:
  - definition
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].nodes[1].description
  evidence_ids:
  - sources
  - canonical-scope
  - meta-canonical
  - metpo-primary
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/strictly_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: anoxic-anaerobic-grounding
  issue_key: strictly-anaerobic-anoxic-anaerobic-grounding
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Environmental absence and bearer oxygen independence are conflated
  description: Current node1 denotes oxygen-excluding environmental conditions; actual
    PATO1456 denotes independence of oxygen in a bearer. The referents differ independently
    of the source growth-scope issue. No replacement identifier or biological repair
    is proposed.
  target_ids:
  - METPO:1000611
  field_paths:
  - causal_graphs[0].nodes[1].grounding
  evidence_ids:
  - node-edges
  - pato-primary
  - owners
  - node-mapping-primary
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/strictly_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Exact row42 applies to empty grounding; current nonempty field is skipped.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_nodes.py
    role: Skip-existing guard; table-only change does not rewrite current node.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: imported-process-roles
  issue_key: strictly-anaerobic-imported-process-roles
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Imported process regulation has incompatible current endpoints
  description: RO2212 inherits process/process roles from RO2211, but edge1 represents
    a chemical subject and trait object. This formal defect is independent of whether
    oxygen inhibits particular biological activity.
  target_ids:
  - METPO:1000611
  field_paths:
  - causal_graphs[0].edges[1]
  evidence_ids:
  - node-edges
  - ro-primary
  - owners
  - predicate-mapping-primary
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/strictly_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Exact row58 is conditional for future empty IDs; imported role constraints
      remain.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing nonempty IDs are skipped; current assertion needs separately authorized
      curation.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: strictly-anaerobic-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Reviewed status lacks a locally attributable acceptance link
  description: 'Bounded ignored-inclusive local evidence does not establish attributable
    current-target acceptance: eleven AI events plus a seed, two histories and zero
    exact current targets among67 review arrays. Private or remote acceptance remains
    unknown.'
  target_ids:
  - METPO:1000611
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - owners
  - ground-reading
  - playbook
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/strictly_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-classification-scope
  description: Resolve documentary scope between trait wording and assigned classification
    evidence.
  finding_ids:
  - absolute-oxygen-growth-scope
  target_ids:
  - METPO:1000611
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/strictly_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve exact canonical identity and author classification.
  - Keep growth and survival endpoints distinct; reconcile only definition and node0/node1
    descriptions with the assigned primary classification scope.
  - After authorized edits, run just validate and just validate-strict for data/traits/environment/strictly_anaerobic.yaml.
  - No culture parameters, mechanism reconstruction or optimization.
- action_id: reconcile-node-grounding
  description: Reconcile the environmental referent with its ontology grounding during
    authorized curation.
  finding_ids:
  - anoxic-anaerobic-grounding
  target_ids:
  - METPO:1000611
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/strictly_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Exact row42 applies to empty grounding; current nonempty field is skipped.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_nodes.py
    role: Skip-existing guard; table-only change does not rewrite current node.
  acceptance_checks:
  - Use actual authority definitions and exact current mapping context.
  - Respect skip-existing guards; no automatic replacement identifier.
  - Review python scripts/ground_causal_nodes.py in its default dry-run mode with
    scratch --out, without --apply; verify the exact mapping key and unchanged nonempty-ID
    guard.
  - After authorized edits, run just validate and just validate-strict for the current
    record.
- action_id: reconcile-relation-roles
  description: Reconcile imported relation semantics with represented endpoints.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000611
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/strictly_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Exact row58 is conditional for future empty IDs; imported role constraints
      remain.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing nonempty IDs are skipped; current assertion needs separately authorized
      curation.
  acceptance_checks:
  - Preserve formal positive controls and detailed biology exclusions.
  - Respect nonempty-ID guards; no mechanistic repair prescription.
  - Review python scripts/ground_causal_predicates.py in its default dry-run mode
    with scratch --out, without --apply; verify RO2212 roles independently of the
    mapping.
  - After authorized edits, run just validate and just validate-strict for the current
    record.
- action_id: link-human-acceptance
  description: Link attributable acceptance if available or clarify status while preserving
    provenance.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000611
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/strictly_anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain bounded search evidence and events; any acceptance link must identify the
    current target and reviewed version.
  - After authorized provenance edits, run just validate and just validate-strict
    for the current record.
  - No contact or automatic status promotion.
limitations:
- Detailed pathogen oxygen/ROS survival, enzyme/defense, mutant and intervention mechanisms,
  culture parameters and optimization remain UNASSESSED_SCOPE.
- Canonical author classification and exact species identity are positive; the same
  title qualifies the absolute growth criterion. No precise experimental condition
  or mechanism is proposed.
- NBK CAPTCHA does not support the supplied survival-threshold quotation; Cdiff abstract
  miss is inconclusive. Neither is treated as a false quote.
- Four short supplied snippets are literal; exactness does not establish causal biological
  efficacy. Three detailed quoted notes remain unassessed.
- Reused indexed metadata preserves original acquisition times. Fresh initial DNS
  errors are not source responses, and a Comment-in annotation is not a correction
  or retraction.
- The retained body was queried only for an existing short phrase; surrounding mechanism
  text was not scientifically read or newly copied.
- Canonical catalog absence is bounded and does not imply broad source-species absence
  or require protein instances or graph expansion.
- Qualified historical diagnostics and local initialization do not certify fresh B13
  QC or remote publication; private acceptance remains unknown.
notes:
- Final root and independent challenge pins verified; builder/helper have not been
  imported or executed during preparation.
- 'Coverage: six works, twelve external placements, seven grounding fields, eight
  nodes/seven edges, six snippets, three quoted notes, one canonical example, one
  component, twelve events and two whole contextual histories.'
- Standalone source preparation corrected synonym.source projection before freeze;
  this was not a native or review validation failure. Scientific records, Git and
  sweep state are not modified by this serializer preparation.
tags:
- record-review
- strictly-anaerobic
- environment
- needs-curation
native_verdict: needs_curation
```
