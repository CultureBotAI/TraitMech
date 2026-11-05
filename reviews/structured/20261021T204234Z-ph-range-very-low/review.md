# Whole-record review of pH range very low

- Review: 20261021T204234Z-ph-range-very-low
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T20:29:25.607566Z
- Finished UTC: 2026-10-21T20:42:34Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Final root disposition: two majors concern confirmed category/bin scope and RO2212 edge 3; one minor concerns bounded human acceptance. All three snippets verified literally or after typography normalization; canonical upper 4/optimum 0.7 positive.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Ninth record of the actual batch 011 queue. Whole 266-line target and all 136 successful capture inputs verified before source judgment. Source, grounding, independent challenge and root readings remain separately attributed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000459 | data/traits/environment/ph_range_very_low.yaml | maintained | pH range very low |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000459 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000459 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000459 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000459 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000459 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000459 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000459 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000459 | Successful focused schema validation; scientific semantics separately assessed. |
| Focused strict validation | passed | True | METPO:1000459 | Successful focused strict validation; not biological efficacy certification. |
| Focused snippet verification | passed | True | METPO:1000459 | Three fields over two references: one VERIFIED and two NOT_IN_ABSTRACT. Actual publisher HTML separately verifies two typography-normalized Krulwich occurrences; Baker phrase is literal in its indexed abstract. |
| Reused maintained batch-ten QC | passed | True | METPO:1000459 | Actual B10 final QC at original time, qualified against B11 bytes. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000459 | Zero protein classes and instances in a quantitative NONMECHANISTIC graph; no token accession required. |

## Scientific And Domain Assessments

### Native checklist: active identity and exact category scope

identity: concern. Targets: METPO:1000459.

Active numerical identity, hierarchy, predecessors and supplied synonym provenance are positive. Exact Acidophile alias is broader than the complete 0–4 convention; other qualitative aliases remain unresolved.

### Native checklist: reach versus complete interval

evidence: concern. Targets: METPO:1000459.

Definition and node 0 describe reaching at or below 4, which can include growth above 4 and differs from the explicit complete 0–4 convention. Approximation is preserved; no universal cutoff or raw-OWL containment axiom is invented.

### Native checklist: direct parent and local authorities

identity: supported. Targets: METPO:1000459.

Parent 1000332, explicit predecessor links, local confers and RDFS hierarchy match the captured authorities.

### Native checklist: all assigned identities and placements

evidence: supported. Targets: METPO:1000459.

Six works resolve through four current EPMC records, chapter Crossref and actual Frontiers PDF. All ten external placements and source-specific limitations are covered; unavailable chapter body is unknown rather than false.

### Native checklist: literal and typography fidelity

evidence: supported. Targets: METPO:1000459.

Baker reversed-membrane-potential phrase is literal in the actual abstract; two Krulwich occurrences match retained publisher Key Points after dash normalization. Native 1 VERIFIED/2 NOT_IN_ABSTRACT retained unchanged.

### Native checklist: canonical phenotype and identity

evidence: unknown. Targets: METPO:1000459.

Assigned abstract directly supports obligacy, optimum 0.7 and no growth above 4, but not measured lower growth endpoint 0. Current taxonomy synonymy is positive; historical named-study measurement transfer remains explicitly limited.

### Native checklist: all eleven represented facets

consistency: supported. Targets: METPO:1000459.

Current steady membrane potential, permeability quality, compartment and explicit processes are coherent. Envelope/prevention and near-neutral maintenance language remain bounded facet qualifications; no automatic additional retype or mandatory grounding.

[{"index": 0, "field": "causal_graphs[0].nodes[0]", "node": {"node_id": "ph_range_very_low_trait", "label": "pH range very low", "node_type": "TRAIT", "grounding": "METPO:1000459", "description": "pH growth-supporting range reaching ≤ ~4."}, "status": "supported", "assessment": "Active numerical trait METPO:1000459. Its reaching-at-or-below-4 wording is distinct from the complete 0–4 interval used by its canonical note; source-scope adjudication is separate."}, {"index": 1, "field": "causal_graphs[0].nodes[1]", "node": {"node_id": "ph_range", "label": "pH range", "node_type": "TRAIT", "grounding": "METPO:1000332", "description": "Span of external pH values supporting growth."}, "status": "supported", "assessment": "Explicit active parent METPO:1000332, matching raw direct superclass."}, {"index": 2, "field": "causal_graphs[0].nodes[2]", "node": {"node_id": "extreme_acidophile_envelope", "label": "extreme-acidophile envelope barrier", "node_type": "BIOLOGICAL_PROCESS", "description": "Combined low-permeability membrane and reversed membrane potential preventing cytoplasmic acidification at strongly acidic external pH."}, "status": "limitation", "assessment": "Envelope barrier label suggests material structure or properties, but prevention wording permits a composite protection process. BIOLOGICAL_PROCESS is not conclusively wrong from this text alone. Clarify referent if curated; no forced enum or new mechanism."}, {"index": 3, "field": "causal_graphs[0].nodes[3]", "node": {"node_id": "potassium_influx", "label": "potassium influx / K+ transport", "node_type": "BIOLOGICAL_PROCESS", "description": "Active influx of cations such as K+ across the cytoplasmic membrane."}, "status": "supported", "assessment": "Explicit influx/transport process, consistent with BIOLOGICAL_PROCESS. Biological efficacy is not established by formal fit."}, {"index": 4, "field": "causal_graphs[0].nodes[4]", "node": {"node_id": "reversed_membrane_potential", "label": "inside-positive (reversed) membrane potential", "node_type": "STATE", "description": "Inside-positive transmembrane electrical potential characteristic of extreme acidophiles."}, "status": "supported", "assessment": "Explicit inside-positive electrical steady state, consistent with STATE and exact maintained migration rationale. It is not the process that establishes the potential; this creates edge 3 role conflict."}, {"index": 5, "field": "causal_graphs[0].nodes[5]", "node": {"node_id": "proton_influx", "label": "passive proton influx", "node_type": "BIOLOGICAL_PROCESS", "description": "Passive entry of protons/hydronium ions into the cytoplasm down the steep pH gradient."}, "status": "supported", "assessment": "Explicit passive entry process; consistent BIOLOGICAL_PROCESS and compatible object of negative process regulation."}, {"index": 6, "field": "causal_graphs[0].nodes[6]", "node": {"node_id": "low_proton_permeability", "label": "low passive proton permeability", "node_type": "QUALITY", "description": "Low permeability of the cell envelope to passive proton flux."}, "status": "supported", "assessment": "Measurable permeability property is QUALITY; no mandatory PATO grounding."}, {"index": 7, "field": "causal_graphs[0].nodes[7]", "node": {"node_id": "near_neutral_cytoplasmic_ph", "label": "near-neutral cytoplasmic pH", "node_type": "STATE", "description": "Maintenance of a near-neutral intracellular pH despite strongly acidic external pH."}, "status": "limitation", "assessment": "Near-neutral intracellular pH names a state; description uses maintenance language that could denote a process. Current state reading is coherent and free predicate explicitly says maintenance. No automatic retype finding; scope of near-neutral value remains source-specific."}, {"index": 8, "field": "causal_graphs[0].nodes[8]", "node": {"node_id": "weak_organic_acids", "label": "protonated weak organic acids", "node_type": "CHEMICAL", "description": "Lipophilic protonated weak organic acids (e.g., acetic acid) that can permeate the membrane."}, "status": "supported", "assessment": "Class of protonated weak organic acids denotes chemical material. No compulsory single ChEBI species for an aggregate class."}, {"index": 9, "field": "causal_graphs[0].nodes[9]", "node": {"node_id": "cytoplasm", "label": "cytoplasm", "node_type": "CELLULAR_LOCALIZATION", "description": "Intracellular cytoplasmic compartment.", "grounding": "GO:0005737"}, "status": "supported", "assessment": "GO:0005737 is cytoplasm, cellular_component, with actual definition excluding plasma membrane/nucleus and including other subcellular structures. Current compartment/localization referent fits."}, {"index": 10, "field": "causal_graphs[0].nodes[10]", "node": {"node_id": "cytoplasmic_acidification", "label": "cytoplasmic acidification", "node_type": "BIOLOGICAL_PROCESS", "description": "Acidification of the cytoplasm by influx and dissociation of permeant protons/acids."}, "status": "supported", "assessment": "Explicit cytoplasmic acidification process; no formal type defect or required additional grounding."}]

### Native checklist: all seven relation roles

consistency: concern. Targets: METPO:1000459.

RO2212 edge 3 inherits process-subject requirements through 2211 and conflicts with the explicit electrical state. Process object is positive; local confers, Biolink causes and free predicates have no invented executor restriction.

[{"index": 0, "field": "causal_graphs[0].edges[0]", "subject": "extreme_acidophile_envelope", "predicate": "confers", "predicate_id": "METPO:2007700", "object": "ph_range_very_low_trait", "status": "supported", "assessment": "Local v8 confers takes broad causal-node endpoints and presence/activity/state as basis of a trait. Current process-facet subject and trait object fit; source efficacy/bin calibration remains separate.", "biology_scope": "Generic referents/formal ontology and existing classification only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."}, {"index": 1, "field": "causal_graphs[0].edges[1]", "subject": "ph_range_very_low_trait", "predicate": "is a", "predicate_id": "rdfs:subClassOf", "object": "ph_range", "status": "supported", "assessment": "RDFS subclass connects current class to its explicit raw parent. Literature excerpt does not replace ontology hierarchy authority.", "biology_scope": "Generic referents/formal ontology and existing classification only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."}, {"index": 2, "field": "causal_graphs[0].edges[2]", "subject": "potassium_influx", "predicate": "causes", "predicate_id": "biolink:causes", "object": "reversed_membrane_potential", "status": "supported", "assessment": "Actual Biolink causes inherits named-thing endpoints; process-to-state is formally permitted. No material-only endpoint rule is invented.", "biology_scope": "Generic referents/formal ontology and existing classification only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."}, {"index": 3, "field": "causal_graphs[0].edges[3]", "subject": "reversed_membrane_potential", "predicate": "decreases", "predicate_id": "RO:0002212", "object": "proton_influx", "status": "major", "assessment": "RO:0002212 negatively regulates is a subproperty of RO:0002211, whose domain and range are BFO:0000015 process. Current steady electrical STATE subject fails that role; proton-influx process object fits. Current history notes lack of direct domain/range but omits inherited endpoints. One current formal-role finding, not a separate biology/sign allegation.", "biology_scope": "Generic referents/formal ontology and existing classification only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."}, {"index": 4, "field": "causal_graphs[0].edges[4]", "subject": "low_proton_permeability", "predicate": "enables maintenance of", "predicate_id": null, "object": "near_neutral_cytoplasmic_ph", "status": "limitation", "assessment": "Free enables maintenance of is not asserted RO:0002327. Quality-to-state maintenance wording has no imported executor requirement. Source-specific near-neutral range and efficacy remain separate/unassessed.", "biology_scope": "Generic referents/formal ontology and existing classification only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."}, {"index": 5, "field": "causal_graphs[0].edges[5]", "subject": "weak_organic_acids", "predicate": "diffuse into", "predicate_id": null, "object": "cytoplasm", "status": "unassessed_scope", "assessment": "Free diffuse into connects chemical material to cytoplasmic compartment; no imported role or mandatory predicate identifier. Literal/source identity may be audited separately; detailed acid-defense/intervention efficacy excluded.", "biology_scope": "Generic referents/formal ontology and existing classification only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."}, {"index": 6, "field": "causal_graphs[0].edges[6]", "subject": "weak_organic_acids", "predicate": "cause", "predicate_id": null, "object": "cytoplasmic_acidification", "status": "unassessed_scope", "assessment": "Free cause connects chemical class to process without an asserted imported predicate. No generic chemical exclusion; detailed pathogen/defense/fitness/AMR/intervention biology is unassessed.", "biology_scope": "Generic referents/formal ontology and existing classification only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."}]

### Native checklist: bounded environmental support and exclusions

evidence: unknown. Targets: METPO:1000459.

Existing generic environmental statements receive selected source context. Chapter nearest-body attribution remains unknown, near-neutral exception retained, and exact-bin universal mechanism calibration is unestablished. Detailed pathogen acid-defense/fitness/AMR/ROS and intervention efficacy are UNASSESSED_SCOPE.

### Native checklist: quantitative NONMECHANISTIC applicability

completeness: supported. Targets: METPO:1000459.

Four components, zero proteins and zero instances are compatible with the recorded quantitative NONMECHANISTIC scope. No mandatory connectivity, token protein, extra pathway or experimental design is imposed.

### Native checklist: structured catalog applicability

evidence: not_applicable. Targets: METPO:1000459.

No exact canonical, current synonym or type alias in the retained 20-organism/28-dataset catalog; no substitute organism/module query. Catalog original acquisition remains separate from current reading.

### Native checklist: actual writers and recurrence guards

provenance: supported. Targets: METPO:1000459.

Record, synonym seeder, mapping/grounder and exact process-quality node-family writer are identified. Existing predicate IDs are skipped; node migration retains outgoing relation. Historical enables/microbe-domain selectors and sibling review/repair are not automatic current repairs.

### Native checklist: bounded current acceptance

provenance: concern. Targets: METPO:1000459.

Eleven AI events plus seed and 14 AI histories do not identify attributable current acceptance. Ignored-inclusive 170 paths/67 parsed arrays/zero exact targets bound the concern; private/remote review is not ruled out.

### Native checklist: actual checks and provenance chronology

consistency: supported. Targets: METPO:1000459.

All 136 captured inputs and frozen source/ground/root/challenge bindings match. Focused native/strict/snippet checks passed. Reused common failures/skips and actual B10 QC retain original times; failed primary accesses remain separate.

## Findings

### category-and-bin-scope: Acidophile category and lower-end reach exceed complete 0–4 scope

major / open / confirmed; issue key: ph-range-very-low-category-and-bin-scope.

Assigned Frontiers Table 1 lists acidophilic growth intervals extending above 4, so exact Acidophile alias is not complete 0–4 equivalence. Definition and node 0 likewise permit a lower-end reach without confining the complete interval. Numeric identity and faithful import remain positive. Other qualitative aliases are unverified, not additional confirmed fields.

### imported-relation-role: Negative regulation requires a process subject

major / open / confirmed; issue key: ph-range-very-low-imported-relation-role.

Edge 3 RO2212 inherits process/process roles from RO2211. Its current inside-positive electrical STATE subject is not the process establishing it; proton-influx process object fits. The historical direct-domain statement is incomplete, not a second finding or biological-sign allegation.

### human-acceptance-link: Current local provenance lacks an attributable acceptance link

minor / open / confirmed; issue key: ph-range-very-low-human-acceptance-link.

Eleven AI events plus seed, 14 captured AI histories and REVIEWED status do not identify linked current human acceptance. Ignored-inclusive 170 paths/67 parsed review arrays/zero exact targets bound this traceability concern; no private or remote absence claim.

## Recommended Actions And Acceptance Checks

### reconcile-category-and-bin-scope

Reconcile confirmed category and reach-versus-complete-interval wording during authorized curation.

- Preserve numerical identity, related 0–4 alias, faithful import and positive canonical upper 4/optimum 0.7.
- Keep other qualitative aliases and precise canonical lower 0 as explicit follow-ups, not already-proven defects.
- Preserve source-specific conventions and guarded history/validation; no universal cutoff or silent source substitution.

### reconcile-imported-role

Reconcile the current imported relation with the explicitly represented electrical state and process referents.

- Preserve current STATE interpretation and positive process object.
- Respect nonempty-ID guard, node-family scope and historical selector limits; mapping change alone is insufficient.
- Do not prescribe an unverified mechanism, new route, perturbation or optimized condition.

### link-human-acceptance

Link attributable current acceptance if available, or clarify status while preserving provenance.

- Retain actual AI/seed and bounded local search evidence.
- No contact or automatic status promotion authorized.

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
| check-ph-range-very-low-native | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-native.log; Executed 2026-10-21T20:29:39.699384+00:00 through 2026-10-21T20:29:40.308696+00:00; metadata ph-range-very-low-native.json | context_only | Successful focused schema validation; scientific semantics separately assessed. |
| check-ph-range-very-low-strict | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-strict.log; Executed 2026-10-21T20:29:39.700491+00:00 through 2026-10-21T20:29:40.729088+00:00; metadata ph-range-very-low-strict.json | context_only | Successful focused strict validation; not biological efficacy certification. |
| check-ph-range-very-low-snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-snippets.log; Executed 2026-10-21T20:30:42.060163+00:00 through 2026-10-21T20:30:45.498635+00:00; metadata ph-range-very-low-snippets.json | context_only | Three fields over two references: one VERIFIED and two NOT_IN_ABSTRACT. Actual publisher HTML separately verifies two typography-normalized Krulwich occurrences; Baker phrase is literal in its indexed abstract. |
| check-batch010-qc | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/batch010-qc.log; Executed 2026-10-21T19:06:27.731868+00:00 through 2026-10-21T19:08:11.219124+00:00; metadata batch010-qc.json | context_only | Actual B10 final QC at original time, qualified against B11 bytes. |
| record | data/traits/environment/ph_range_very_low.yaml; Entire current 266-line record | supports | Eleven nodes, seven edges, three snippets, one canonical and twelve record events covered. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Meaning of explicit process/state/quality/chemical/compartment facets; no mandatory token protein. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source scope, literal fidelity and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current node facets and closed scientific representation contract. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Complete identity, source, graph, ownership and readiness checklist. |
| reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json; Actual B10-to-B11 qualification | supports | Original outcomes and current byte comparisons bound. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json; Actual independent qualifier verification | supports | Actual output/hash postcheck; no new QC. |
| capture | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/capture-verification.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | All 136 captured inputs verified before judgment. |
| identity | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/identity-assessment.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Active identity, direct parent, both explicit replacements and numerical convention. |
| node-edges | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/node-edge-ledger.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Every eleven nodes/seven edges; firm RO2212 issue at edge 3 only. |
| owners | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/owner-provenance-assessment.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Exact current/shared owners versus guarded historical and sibling context; bounded human search. |
| expression | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/expression-assessment.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Twenty-organism/28-dataset catalog lacks exact canonical/current synonym/type aliases; no substitute query. |
| authority-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/authority-reuse-receipts.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Original catalog and runner acquisitions retained. |
| local-authority | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/local-authority-excerpts.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Actual v8 confers, historical v9 reduces and maintained mapping/schema rows. |
| ground-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/actual-reading-scope.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Fourteen whole-history reads belong to grounding; source/root shorter scopes remain separate. |
| ground-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/evidence-manifest.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Twenty-six frozen grounding artifacts verified. |
| taxon-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/identity-reuse.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Current copy is identical to original official taxonomy response; not a fresh request. |
| metpo-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl; Selected actual target/parent/predecessor XML | supports | Active 1000459, direct 1000332, inclusive 0–4 and both explicit predecessors 0000181/000182 positive. Raw existential restriction alone is not universal interval containment. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Actual RO2212→2211 inherited process/process endpoints | supports | Explicit steady electrical state cannot be process subject; proton-influx process object fits. Direct-domain absence does not remove inherited roles. |
| biolink-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/biolink-model.yaml; Actual complete causes chain | supports | Broad named-thing endpoints allow process-to-state; no material-only domain/range invented. |
| go-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/go.db; Actual cached GO5737 label/namespace/definition | supports | Cytoplasm cellular component matches the current compartment; no new remote refresh claimed. |
| taxon-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/taxon46632.xml; Whole retained official taxonomy response at original acquisition time | supports | Current Picrophilus oshimae species and P.torridus synonym/type aliases. Current synonymy does not silently transfer a historically named study measurement into the assigned canonical note. |
| meta-canonical | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/canonical-metadata.json; Actual indexed metadata/abstract response at original acquisition | supports | Actual indexed abstract: obligacy, optimum 0.7 and no growth above 4 positive; precise lower growth endpoint 0 not established. No body claim. |
| meta-krulwich | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/krulwich-metadata.json; Actual indexed metadata/abstract response at original acquisition | supports | Actual indexed review abstract and status only; detailed publisher/BioC readings separately bound. |
| meta-baker | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/baker-metadata.json; Actual indexed metadata/abstract response at original acquisition | supports | Actual low-pH homeostasis abstract contains reversed membrane potential literally and defines acidophiles by optimum below 3. |
| meta-organic | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/organic-metadata.json; Actual indexed metadata/abstract response at original acquisition | supports | Actual environmental Nitrosotalea study identity/status; generic selected Introduction clause is separate from metadata and efficacy excluded. |
| meta-chapter | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/chapter-crossref.json; Crossref DOI/title/type/author/date fields; no abstract | supports | The Microbiology of Extremely Acidic Environments resolves as ASM Press book chapter. Identity does not establish unavailable body statements. |
| body-krulwich-bioc | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/krulwich-bioc.xml; Selected BioC generic classification/PMF passages | supports | Generic extreme-acidophile/reversed-potential context positive; detailed pathogen/efficacy branches not assessed. |
| body-krulwich-publisher | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/krulwich-publisher.html; Publisher Key Points | supports | Actual publisher pH 1.0–3.0 wording verifies two snippets after dash normalization; acid exposure context does not independently establish exact alias 0. |
| body-organic | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/organic.xml; JATS article identity and Introduction body paragraph 3 generic organic-acid clause | supports | Generic organic-acid membrane passage/proton release/acidification clause supports existing environmental context; incidental pathogen mechanisms and perturbation outcomes unassessed. |
| body-permeability | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/permeability.pdf; Publisher PDF page 1 abstract/identity, page 3 exception and page 4 Table 1 | supports | Acidophilic examples can extend above 4; existing permeability note positive with Picrophilus intracellular 4.6 exception. Table viewed as rendered image; no historical phenotype transfer. |
| sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/source-assessment.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Six assigned works and bounded source decisions; root controls final disposition. |
| source-ledger | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/source-ledger.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Actual EPMC/Crossref/publisher identity shapes and original acquisition times. |
| placements | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/placement-ledger.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Ten external placements, three grounding fields and six synonym-source placements. |
| snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/snippet-ledger.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | One literal Baker abstract phrase and two typography-normalized publisher phrases; no unknown schema snippet. |
| node-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/node-source-ledger.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | All eleven node-source contexts. |
| edge-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/edge-source-ledger.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | All seven edge-source contexts and unavailable chapter limits. |
| source-status | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/publication-status-ledger.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Actual returned status fields; zero EPMC hits/429 do not mean nonexistent sources. |
| source-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/selected-primary-reading.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Selected actual primary reading scopes, PDF table image and incidental excluded passages. |
| source-access | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/access-limitations.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Chapter 403 and browser failure; Springer 200 challenge differs from root successful abstract preview. |
| source-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/reuse-and-copy-receipt.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Actual original publisher/BioC acquisition separate from current metadata, copies and readings. |
| source-acquisition | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/primary-access-receipts.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Two primary successes and retained failed/challenge responses; none relabeled as native failure. |
| bin-scope | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/classification-and-bin-assessment.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Confirmed source group only alias 1, definition and node 0 description; other qualitative aliases unresolved. |
| canonical-scope | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/canonical-assessment.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Positive obligacy/upper 4/optimum 0.7; precise lower 0 remains unknown. |
| near-neutral-scope | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/near-neutral-exception-assessment.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Source explicitly qualifies Picrophilus intracellular 4.6; generic branch remains positive, no uniform canonical assignment. |
| native-checks | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/native-check-context.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Actual native/strict/snippet receipts and retained logs. |
| source-capture | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/final-capture-verification.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | All 136 successful capture inputs unchanged. |
| source-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/evidence-manifest.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Thirty-six frozen source artifacts verified. |
| root-reading-87 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-root/publisher-browser-observations.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Only the actual bounded root reading/observation/verification scope; receipt hash is not an article-body hash. |
| root-reading-88 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-root/root-final-evidence-reading.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Only the actual bounded root reading/observation/verification scope; receipt hash is not an article-body hash. |
| root-reading-89 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-root/root-metadata-reading.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Only the actual bounded root reading/observation/verification scope; receipt hash is not an article-body hash. |
| root-reading-90 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-root/root-primary-reading.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Only the actual bounded root reading/observation/verification scope; receipt hash is not an article-body hash. |
| root-reading-91 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-root/whole-target-root-reading.json; Derived audit or actual reading/access receipt; primary snapshots separately identified | supports | Only the actual bounded root reading/observation/verification scope; receipt hash is not an article-body hash. |
| challenge | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-semantic-challenge-agent/semantic-severity-challenge.json; Final independent challenge | supports | Final recommendation, exact field anchors and evidence bindings verified. |
| adjudication | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-root-adjudication.json; Final root disposition | supports | Final root controls findings, severities and declined cases. |

## Limits And Additional Notes

- Detailed pathogen acid-defense, fitness, AMR, ROS and perturbation efficacy are UNASSESSED_SCOPE. Only existing generic environmental context, literal/source identity and formal roles were assessed.
- Aliases 0/2/3/4 remain unresolved exact-equivalence questions; extreme 1–3 inside 0–4 alone is not a confirmed class conflict. Related numeric alias and hierarchy remain positive.
- Complete-interval convention comes from the current record/canonical owner; raw existential numerical restriction alone is not universal containment.
- Canonical lower growth endpoint approximately 0 is not explicitly established by inspected assigned abstract or subscription preview; upper 4/optimum 0.7 and obligacy positive. Current P.torridus synonymy does not silently transfer historical named-study measurements into that note.
- Near-neutral source phrase is positive generic context with explicit Picrophilus intracellular 4.6 exception. No uniform canonical-to-every-branch assignment or additional false-mechanism finding.
- Chapter identity resolves but body statements remain unknown after 403/browser failure. Organic generic introductory support is supplemental context, not replacement verification of chapter wording.
- Springer download returned a client challenge despite 200; separate root browser actual abstract/preview is accurately attributed. Frontiers PDF/image/text and organic JATS are actual successful snapshots.
- Four disconnected components and zero protein classes/instances are permitted by NONMECHANISTIC scope. No compulsory connector, accession, new pathway or optimization.
- Fourteen whole-history reads are grounding-agent work. Root summary/projections and source selected readings remain separately attributed. Current report frontmatter is a lead, not proof of the exact earlier enrichment version.
- Original publisher 07:56:32–36/BioC 07:57:33, catalog and taxonomy 18:48:17 acquisitions remain separate from current metadata/body requests, copies and reading times. Browser observation receipts do not invent downloaded-body hashes or unclocked call intervals.
- Final root adjudication and independent challenge are pinned and verified. Author preparation did not import or execute this serializer; the root owns its later single execution, native validation and save.
- Coverage: six works, ten external placements, three grounding fields, six synonym-source placements, eleven nodes/seven edges, one canonical, three snippets: one literal and two typography-normalized.
- No scientific record, native inventory, Git or sweep state mutation by serializer preparation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T204234Z-ph-range-very-low
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of pH range very low
started_at: '2026-10-21T20:29:25.607566Z'
finished_at: '2026-10-21T20:42:34Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Independent source and grounding audits, separate semantic challenge
    and bounded root primary/owner readings. Safe environmental classification, existing
    reported phenotype, literal source alignment and formal roles assessed. Detailed
    pathogen acid-defense, fitness, AMR, ROS and perturbation efficacy are UNASSESSED_SCOPE.
    No scientific record edited.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Final root disposition: two majors concern confirmed category/bin scope
  and RO2212 edge 3; one minor concerns bounded human acceptance. All three snippets
  verified literally or after typography normalization; canonical upper 4/optimum
  0.7 positive.'
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
  - path: data/traits/environment/growth_range_phenotype_with_numerical_limits.yaml
    sha256: ad223791fa379c8f7302c8334153dbbd157fbf9a015a902a6ebb92f5513bfd9b
    role: context
  - path: data/traits/environment/ph_phenotype_with_numerical_limits.yaml
    sha256: 643abb9898dc920fe3aeeb0fa337c1d3a7efa6f0b540cb4ad979a3a28e0702d4
    role: context
  - path: data/traits/environment/ph_range.yaml
    sha256: 8a9cac2ea39eaf0aaafb950fce9b8119713bbef55c43e84550f22c3ee9d13d1a
    role: context
  - path: data/traits/environment/ph_range_very_low.yaml
    sha256: 0955dd61255a701972cd23984962e4b7ad32cb4139ecd6dae6b411d6d119eae4
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
  - path: history/infrastructure/disposition-typing-burndown/2026-08-08T014114Z-claude-code-5d4383.yaml
    sha256: 8fecb441b9374b0a0f69f131afce56f86ff69c212c52f45967c2e05ccb8ee98a
    role: context
  - path: history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    sha256: 21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510
    role: context
  - path: history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml
    sha256: e35d99e8285d488d98584d046aa001825527609cfd62575b3b839c4a31230642
    role: context
  - path: history/mappings/name-match-groundings/2026-08-17T042357Z-claude-code-2a9f93.yaml
    sha256: c3f93d5c8c0da5c538af391bfdbad3a8bcbe238a26a8727764c3f0ddc3422ad8
    role: context
  - path: history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    sha256: c938f2928f2eb41505d58c2fb72d8de01d99534d766de9af400010e8778988a4
    role: context
  - path: history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml
    sha256: 23be5f6ab519511e3e23feffa85813eec4fa3c7e6b900e77fd4a3adc0c26da0e
    role: context
  - path: history/records/autophagy/2026-10-06T133812Z-codex-a9b1dc.yaml
    sha256: 080914fc91767fd96e3b07f149b763842e0a4b58272f9463fb01df683793e212
    role: context
  - path: history/records/cellular_contraction/2026-10-15T000059Z-codex-057ea1.yaml
    sha256: aa455dfb438d7f42f2c6e287d8faadde6eddcc4655906e69c17deb70d3eed6a8
    role: context
  - path: history/records/cytoplasmic_bacterial_predation/2026-10-11T153412Z-codex-1e630f.yaml
    sha256: 1b1f39751efa6df3940652eb4160fa478a9eb62233ce466e1324306858af7679
    role: context
  - path: history/records/free_living/2026-08-31T204506Z-claude-code-ca81b1.yaml
    sha256: 0c2d8296d829bf97b806e44163c6138eac07431dbedc34e99a70bcbb191c7fe4
    role: context
  - path: history/records/hyphal_anastomosis/2026-10-04T221217Z-codex-05ba2b.yaml
    sha256: 7f52a69411eb64dda28cb49eeaaf5c9db493454838cf941e62ee071049bdb098
    role: context
  - path: history/records/ph_delta_mid2/2026-09-04T012000Z-codex-c2b994.yaml
    sha256: 20f81cb8a888c5b27c69b3443ac5dedf5a8eea4e80f9a045093bd3629b418eb6
    role: context
  - path: history/records/ph_delta_mid2/2026-09-04T150000Z-codex-183.yaml
    sha256: 7e63e01287759bd24840902179eeef44c47a919ac1e89f989882263f2c388aa9
    role: context
  - path: history/records/ph_range_mid2/2026-09-04T024000Z-codex-3036b8.yaml
    sha256: 5ac1f0e4fed3207531b7a5db26c67ff29e3e2a5c06ec1127107311d9e194f6a2
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
  - path: research/traits/environment/ph_range_very_low-deep-research-falcon.md
    sha256: 981832ed73b21ab21ae1ef461f9d32859eff64b92003f4b7022f9fbd249636a1
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_adhesive_net_trait.py
    sha256: ad6bd9ab13449fb7adb74db66650278bbaf74c1110d69e6c066a2c88e279c63d
    role: context
  - path: scripts/add_automixis_trait.py
    sha256: 72cc2408bcf655a5bef12f0e2cdec7392a2d9b92e2ed1db1ac8615707eea8b41
    role: context
  - path: scripts/add_autophagic_glycogen_degradation_trait.py
    sha256: 4fc118ae460a6ad8b3e0c7bd98d3a9ed5c7a0f9cc7c96dd72e34046c4ebbe2aa
    role: context
  - path: scripts/add_autophagy_trait.py
    sha256: e9d60ed8f467d30eb3b1e391f76dc48a6fe6379ff98fdb17bc8f004be9862151
    role: context
  - path: scripts/add_carbon_source_memory_trait.py
    sha256: 290cbffea8a884d60116a69aaf44069fecbd91b6df71cc176458264638ced777
    role: context
  - path: scripts/add_cellular_buoyancy_trait.py
    sha256: 8d9080a62ea0b48f88efa9b22b5f2b6a684d32a900976bf7d45f78373749a786
    role: context
  - path: scripts/add_cellular_contraction_trait.py
    sha256: e924e40ae9145b59f7e6ec4a43c337ff64cf118c0b6f621abb83c4ceb98be5ee
    role: context
  - path: scripts/add_cellular_rejuvenation_trait.py
    sha256: 2155ebb0bc3a76b86cdf525ce97657bcbc4e3ee8e4424c25b32b28eac4bd89a5
    role: context
  - path: scripts/add_cold_shock_response_trait.py
    sha256: d90be1ba41afbc2c8194466485291a02c7f46c078cf4356c2635c169add6f521
    role: context
  - path: scripts/add_collective_predation_trait.py
    sha256: 776ae4362e7d4f71b957746c6d92b53b9a6f291d16924407e9d40f982a2db902
    role: context
  - path: scripts/add_contact_dependent_outer_membrane_exchange_trait.py
    sha256: 47875df17691d01610e7cf79755374d53cce05f6c9160bff94a8ac4d5b7717a6
    role: context
  - path: scripts/add_cytogamy_trait.py
    sha256: 11f7be9bcdef251a549db16b237420b26502e48b9fab22c73a745b5b9ca18fe4
    role: context
  - path: scripts/add_cytoplasmic_predation_trait.py
    sha256: 3b09dbec145dafbed9804b3ba32acbbed9257e527f10b60d0f36134d5a556343
    role: context
  - path: scripts/add_endocytosis_trait.py
    sha256: fb069a29dd7bb340002a86014bd18338620fee91f680a8002c161dee8901aa7a
    role: context
  - path: scripts/add_er_phagy_trait.py
    sha256: 98183c56641be875730cdeed50139c8e984eb9098510a3c82fb25f2832a051e9
    role: context
  - path: scripts/add_exocytosis_trait.py
    sha256: 37db3f74563302dd73d8445aa042f0421f43b3b7813dd71f2c6f8622b98ef5e2
    role: context
  - path: scripts/add_extracellular_membrane_vesicle_production_trait.py
    sha256: 16faa5e9c3ca214c128c972589cd4e5c341a5c7762b603aa0b3f191e9029ae1a
    role: context
  - path: scripts/add_fungal_arbuscule_formation_trait.py
    sha256: cf6b652d611c1326259ade640e3a729710d5cce22e6bdd7b59925f87dfce1098
    role: context
  - path: scripts/add_fungal_internal_mycorrhizal_vesicle_formation_trait.py
    sha256: 35b1a91b8c9dbe05085fb7bcf9c685ebecfa43e94bc8c95983eefc712f9b1560
    role: context
  - path: scripts/add_fungal_mycelial_cord_formation_trait.py
    sha256: 6081f877ff92c501a82ea29eb5098ae38608af7b4211e28696e7db0ab5fd8d6e
    role: context
  - path: scripts/add_heterokaryosis_trait.py
    sha256: a9d249dc5bcc45ed0993f0ed6c8c14e31840a9e6ec0f22d3c79564b4da921fe4
    role: context
  - path: scripts/add_homothallism_trait.py
    sha256: 55ca1485df9740901e4dbb53824e1dc42389929fdd43bb2914bdd2983bcc05b9
    role: context
  - path: scripts/add_hyphal_anastomosis_trait.py
    sha256: 6b4782d18c88a4d2f6f1da9d27b3f0885be66e10ec156010dc08c012771b5786
    role: context
  - path: scripts/add_microbial_haustorium_formation_trait.py
    sha256: fd505889d281c8c2f227984aa7360a56ce8d77fcffa652fbfba36505f72d770a
    role: context
  - path: scripts/add_mitophagy_trait.py
    sha256: 553c9fd3db7adf5884be8a1cce1c2946fee699b25c49238c9b5e383a2bd1384b
    role: context
  - path: scripts/add_myzocytosis_trait.py
    sha256: 764fedf8cb1123c5db31a849169b462efe7117495666912f77800d6309f28f59
    role: context
  - path: scripts/add_negative_autotropism_trait.py
    sha256: 4886c03e15e49f0e3ae0960e7fa9b2b7864026ec9b3e312182c2ab8e45f12a12
    role: context
  - path: scripts/add_nucleophagy_trait.py
    sha256: e8d63d59766effc3900d83905762ed6a9d27680529e296795c69d1320703fd07
    role: context
  - path: scripts/add_pallium_feeding_trait.py
    sha256: 695765f1df0c278b71ad843fffa7bfae8db7fbd4856c9593c830d838cb011005
    role: context
  - path: scripts/add_periplasmic_predation_trait.py
    sha256: c83649a2c376180778e11432aa1e3d10594218338b52717184526bdb2eedcdc2
    role: context
  - path: scripts/add_pexophagy_trait.py
    sha256: 0cfd1750d2e0840c70e8351b5067769b0e38b432a30d792d951cacad6a17a147
    role: context
  - path: scripts/add_pinocytosis_trait.py
    sha256: 5305f920be87a8c12d564cee69487b46d7a3d3e95fb20095110ffe2d39da3195
    role: context
  - path: scripts/add_ribophagy_trait.py
    sha256: f69f39f6387ba7ff4aae412a40d809eacfbdcf68d90c9b90fef1083295151eb7
    role: context
  - path: scripts/add_stalk_contraction_trait.py
    sha256: 90bb195961248869a838853d8bc51c561a741b40b002bcc146bdf3e01c5d6298
    role: context
  - path: scripts/add_synnema_formation_trait.py
    sha256: b5dedf14bb98bdada69570de4608c5fe68729bfff4c2fef39469aeac7b03bad5
    role: context
  - path: scripts/add_toxicyst_discharge_trait.py
    sha256: 34dfa520e8d4de58198f4c0f4959aec8c20f83e8bab7a98cfb1b44c7419faf8d
    role: context
  - path: scripts/add_zorya_system_trait.py
    sha256: 327c27ac2e1cb445205ec1448907e475806046b7a3b91e4603b4605158c0fa55
    role: context
  - path: scripts/add_zorya_type_i_system_trait.py
    sha256: 162b4da3dac47042bae9b14e04d50e88b4fa7e09a19e8cf1d86a8f1bd17b9b45
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
  - path: scripts/audit_schema.py
    sha256: ea8eb5b6f5355a87f6270ec67793e0a05811b14a67828543dad90f2465c5ddb1
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
  - path: scripts/build_embedding_index.py
    sha256: d5ebf6612a04a67d74b2a245014a3624253d25f8d2b810e0b0ce528b7c851cd7
    role: context
  - path: scripts/connect_free_living_trehalose_osmotic.py
    sha256: 7b39fbf6fdae76a319dd88115888ac66137c1cbc5e798d1aaaaa35692df26252
    role: context
  - path: scripts/connect_mesophilic_graph_183.py
    sha256: 3f1fa78321d7aa98dc2fedde9784e71ed60624a94f825bf3af1674753af56f85
    role: context
  - path: scripts/connect_morphology_tail_graphs_183.py
    sha256: eefc69133e0d628a130215dbc439d7e86e1b4f08b0c6f2b4b024c6849f80a7f0
    role: context
  - path: scripts/connect_nacl_optimum_graph_183.py
    sha256: f1608bd82c1323c7d2306268860502ae3483d40f093e055b9b70cd463a1ecf04
    role: context
  - path: scripts/connect_ph_delta_mid2_graph_183.py
    sha256: 21e16ff508b7448d6a60bf0729585a2fa1879ce9ac98562de4652689aec75d91
    role: context
  - path: scripts/connect_ph_delta_mid3_graph_183.py
    sha256: cf65890b2797032dcf9d2fa7b249a47cfe710501b3b2d8f610f323c6f27366e4
    role: context
  - path: scripts/connect_ph_delta_very_low_graph_183.py
    sha256: 5abcdea4fbf7793bc718406439e63203726284d2c2d3222b4bdd00d3de2b6390
    role: context
  - path: scripts/connect_ph_phenotype_graph_183.py
    sha256: 7d13d108660bede28937d3f180e90c542c47869c10f34ca497f9ab6f8f5db4ba
    role: context
  - path: scripts/connect_temperature_delta_very_low_graph_183.py
    sha256: 19eb2722de2fae0c76bf4c83b5f5b13f09841b17def22cdccb86d373711bf879
    role: context
  - path: scripts/connect_temperature_optimum_high_graph_183.py
    sha256: 7d2c6bee0f2af46cec82afe93b93b5a993ffb6042f953e7793b2bbc6ea713504
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
  - path: scripts/refine_cellular_contraction_proposal.py
    sha256: fbb44f299bc654bfeaa6c01a17a3bc6d7505f732a828c5b195a591c10945f07b
    role: context
  - path: scripts/repair_pr664_adversarial_review.py
    sha256: 5717a89bee383aa0e12aec9bf30434ccff74efcbe64684d13ef9b290b1accf96
    role: context
  - path: scripts/review_nacl_delta_graph_183.py
    sha256: 91b85da640baff48e0d317c206aaa24c1216b3725d9c9814c6fb9d4d975e192c
    role: context
  - path: scripts/review_nacl_optimum_graph_183.py
    sha256: 6d0de1ccb1604fb87294432692cc051e3a8a1d52e082eaff6aa1f8d3cb621ffd
    role: context
  - path: scripts/review_nacl_range_low_graph_183.py
    sha256: d7e6669f6d2aa295487a34cba7fe14666a979404614bdbdd3be529194649accf
    role: context
  - path: scripts/review_ph_delta_mid2_graph_183.py
    sha256: a7fcd17ebe8668b31f47c78b655ba908ffd537c3422f9bb2fd1cf3a66145b6c6
    role: context
  - path: scripts/review_ph_delta_mid3_graph_183.py
    sha256: 47d0d2b09f3acce565d9779443d8a5ee6784989ae34c23c6f0875f74ad4a1532
    role: context
  - path: scripts/review_ph_delta_very_low_graph_183.py
    sha256: 3fb1c239de9fb1bf91a5a97696053c7d652a619dc824ce160dd1063b44aad499
    role: context
  - path: scripts/review_ph_phenotype_graph_183.py
    sha256: 651b46611c5e630e4db00f8d7525378ddb3a9f552c83e7f53387d14ab95dd2e2
    role: context
  - path: scripts/review_ph_range_mid2_graph_183.py
    sha256: 2788c907439099c64cbc25c50b973e5ac0d2b93bc07ff7ed89e4cddaae500bd3
    role: context
  - path: scripts/review_temperature_delta_very_low_graph_183.py
    sha256: 1ac23973b6cf54861f6ae79afefe93e39cc9382a93c73c36a8daa37b376334d0
    role: context
  - path: scripts/review_temperature_optimum_high_graph_183.py
    sha256: ed7b046129400db1fa4352250d27569e0844ef837000577f1448e565a0e60576
    role: context
  - path: scripts/review_temperature_range_very_low_graph_183.py
    sha256: 4a48e54f1e448c2a4f67088cce8ecfe248f81034faf7271ab272e45e9e2541d4
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
- target_id: METPO:1000459
  path: data/traits/environment/ph_range_very_low.yaml
  label: pH range very low
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_very_low.yaml
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
  selection: Ninth record of the actual batch 011 queue. Whole 266-line target and
    all 136 successful capture inputs verified before source judgment. Source, grounding,
    independent challenge and root readings remain separately attributed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000459
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000459
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000459
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000459
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot.
  evidence_ids:
  - check-check-pathway-links
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000459
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000459
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000459
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000459
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: ph-range-very-low-native
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000459
  command: just validate data/traits/environment/ph_range_very_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful focused schema validation; scientific semantics separately assessed.
  evidence_ids:
  - check-ph-range-very-low-native
- check_id: ph-range-very-low-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000459
  command: just validate-strict data/traits/environment/ph_range_very_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful focused strict validation; not biological efficacy certification.
  evidence_ids:
  - check-ph-range-very-low-strict
- check_id: ph-range-very-low-snippets
  name: Focused snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1000459
  command: just verify-snippets --record data/traits/environment/ph_range_very_low.yaml
    --out /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Three fields over two references: one VERIFIED and two NOT_IN_ABSTRACT.
    Actual publisher HTML separately verifies two typography-normalized Krulwich occurrences;
    Baker phrase is literal in its indexed abstract.'
  evidence_ids:
  - check-ph-range-very-low-snippets
- check_id: batch010-qc
  name: Reused maintained batch-ten QC
  status: passed
  required: true
  target_ids:
  - METPO:1000459
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual B10 final QC at original time, qualified against B11 bytes.
  evidence_ids:
  - check-batch010-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000459
  summary: Zero protein classes and instances in a quantitative NONMECHANISTIC graph;
    no token accession required.
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
- evidence_id: check-ph-range-very-low-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-native.log
  locator: Executed 2026-10-21T20:29:39.699384+00:00 through 2026-10-21T20:29:40.308696+00:00;
    metadata ph-range-very-low-native.json
  accessed_at: '2026-10-21T20:29:40.308696Z'
  support: context_only
  summary: Successful focused schema validation; scientific semantics separately assessed.
  snapshot_sha256: cf0e627e3405ce0b2e9c122bc383feb2d50b9a5358c22aa625e4837ea3636fb5
- evidence_id: check-ph-range-very-low-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-strict.log
  locator: Executed 2026-10-21T20:29:39.700491+00:00 through 2026-10-21T20:29:40.729088+00:00;
    metadata ph-range-very-low-strict.json
  accessed_at: '2026-10-21T20:29:40.729088Z'
  support: context_only
  summary: Successful focused strict validation; not biological efficacy certification.
  snapshot_sha256: 11fdb605ebbaabac7879020d7867221835a52f5fe88cc11527c9a0e9c89415ef
- evidence_id: check-ph-range-very-low-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-snippets.log
  locator: Executed 2026-10-21T20:30:42.060163+00:00 through 2026-10-21T20:30:45.498635+00:00;
    metadata ph-range-very-low-snippets.json
  accessed_at: '2026-10-21T20:30:45.498635Z'
  support: context_only
  summary: 'Three fields over two references: one VERIFIED and two NOT_IN_ABSTRACT.
    Actual publisher HTML separately verifies two typography-normalized Krulwich occurrences;
    Baker phrase is literal in its indexed abstract.'
  snapshot_sha256: 37173b7ab1b9c9bea4dc8cab1a14745d63048e6d578482facfdad708c0b3ff61
- evidence_id: check-batch010-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/batch010-qc.log
  locator: Executed 2026-10-21T19:06:27.731868+00:00 through 2026-10-21T19:08:11.219124+00:00;
    metadata batch010-qc.json
  accessed_at: '2026-10-21T19:08:11.219124Z'
  support: context_only
  summary: Actual B10 final QC at original time, qualified against B11 bytes.
  snapshot_sha256: a97d2cc68e7db1ebd1a0edd19a7b0d03a4b1f45b55f8c6e6c2c48252f1705201
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/ph_range_very_low.yaml
  locator: Entire current 266-line record
  accessed_at: '2026-10-21T20:29:26.411681Z'
  support: supports
  summary: Eleven nodes, seven edges, three snippets, one canonical and twelve record
    events covered.
  snapshot_sha256: 0955dd61255a701972cd23984962e4b7ad32cb4139ecd6dae6b411d6d119eae4
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T20:33:54.459145Z'
  support: supports
  summary: Meaning of explicit process/state/quality/chemical/compartment facets;
    no mandatory token protein.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T20:33:54.459145Z'
  support: supports
  summary: Source scope, literal fidelity and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T20:33:54.459145Z'
  support: supports
  summary: Current node facets and closed scientific representation contract.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T20:33:54.459145Z'
  support: supports
  summary: Complete identity, source, graph, ownership and readiness checklist.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json
  locator: Actual B10-to-B11 qualification
  accessed_at: '2026-10-21T19:08:29.388400Z'
  support: supports
  summary: Original outcomes and current byte comparisons bound.
  snapshot_sha256: a728777b9987b1283d7d1382168af40739074fce5c05f9a3bd93d3738f56880f
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Actual independent qualifier verification
  accessed_at: '2026-10-21T19:08:41.804361Z'
  support: supports
  summary: Actual output/hash postcheck; no new QC.
  snapshot_sha256: a3a6f33363e71b00e8db09cbc318cae0027844aba584f7b4cafb282d11ab027a
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/capture-verification.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:30:56.474939Z'
  support: supports
  summary: All 136 captured inputs verified before judgment.
  snapshot_sha256: 099c7832645a08b72251f8fb120a14f7a303fcd5b8729c84ec1b8d018bdfabfb
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/identity-assessment.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:54.459145Z'
  support: supports
  summary: Active identity, direct parent, both explicit replacements and numerical
    convention.
  snapshot_sha256: 30386219bd708f06c9b306a813c7b701776874a0b6302eb90ca5486eea98ddeb
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/node-edge-ledger.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:54.459145Z'
  support: supports
  summary: Every eleven nodes/seven edges; firm RO2212 issue at edge 3 only.
  snapshot_sha256: 188d50daf9fb2947b56bd5d6833933525a2fe944c155db91e5d9105c3ade2c05
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/owner-provenance-assessment.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:54.459145Z'
  support: supports
  summary: Exact current/shared owners versus guarded historical and sibling context;
    bounded human search.
  snapshot_sha256: 2ab2628c321173906d6ae79d0c6a23ddf9125b45f866583b3f71899ab8f1fc95
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/expression-assessment.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:54.459145Z'
  support: supports
  summary: Twenty-organism/28-dataset catalog lacks exact canonical/current synonym/type
    aliases; no substitute query.
  snapshot_sha256: c83fb9dff8e9b82ed4b1603334283a65d102feb20bafe2719c18ac09252b0fe1
- evidence_id: authority-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/authority-reuse-receipts.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:31:08.569417Z'
  support: supports
  summary: Original catalog and runner acquisitions retained.
  snapshot_sha256: 72f7626e3e21cbaa319d726d4d1bafc371dae72595e69c30537841da6f3f6bda
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/local-authority-excerpts.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:31:08.547109Z'
  support: supports
  summary: Actual v8 confers, historical v9 reduces and maintained mapping/schema
    rows.
  snapshot_sha256: 91369d9115178c65bb5d5f9e3ecb3ed0563ba2b06cf8ff1fd3aa9b73afc15fdd
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/actual-reading-scope.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:54.459145Z'
  support: supports
  summary: Fourteen whole-history reads belong to grounding; source/root shorter scopes
    remain separate.
  snapshot_sha256: bf7352e7c6fb0204d486598575fcb729ac71f90dbf0f681795035b5eca2d9e0a
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/evidence-manifest.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:54.493098Z'
  support: supports
  summary: Twenty-six frozen grounding artifacts verified.
  snapshot_sha256: b670dca2fdc1548d9cefcf637645fdc2dc443c564e0f56efc2799bee45daa165
- evidence_id: taxon-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/identity-reuse.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:32:17.265243Z'
  support: supports
  summary: Current copy is identical to original official taxonomy response; not a
    fresh request.
  snapshot_sha256: be10141d608c3de7bef28a26c5cf9e5b7d46183e643cb675c78c81376a7cd24d
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl
  locator: Selected actual target/parent/predecessor XML
  accessed_at: '2026-10-21T20:31:08.538547Z'
  support: supports
  summary: Active 1000459, direct 1000332, inclusive 0–4 and both explicit predecessors
    0000181/000182 positive. Raw existential restriction alone is not universal interval
    containment.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Actual RO2212→2211 inherited process/process endpoints
  accessed_at: '2026-10-21T20:31:08.540297Z'
  support: supports
  summary: Explicit steady electrical state cannot be process subject; proton-influx
    process object fits. Direct-domain absence does not remove inherited roles.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: biolink-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/biolink-model.yaml
  locator: Actual complete causes chain
  accessed_at: '2026-10-21T20:32:18.217445Z'
  support: supports
  summary: Broad named-thing endpoints allow process-to-state; no material-only domain/range
    invented.
  snapshot_sha256: 4955709e1cac1d26fd657f7a0c29d6c8390f42e41f9ebfab859c82b102f2bebb
- evidence_id: go-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/go.db
  locator: Actual cached GO5737 label/namespace/definition
  accessed_at: '2026-10-21T20:32:17.269751Z'
  support: supports
  summary: Cytoplasm cellular component matches the current compartment; no new remote
    refresh claimed.
  snapshot_sha256: 018a7ef0a5bd1c0767abc3d71b413264a25be7579533daf5349f739cd9a122cd
- evidence_id: taxon-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-grounding-agent/taxon46632.xml
  locator: Whole retained official taxonomy response at original acquisition time
  accessed_at: '2026-10-21T18:48:17.418961Z'
  support: supports
  summary: Current Picrophilus oshimae species and P.torridus synonym/type aliases.
    Current synonymy does not silently transfer a historically named study measurement
    into the assigned canonical note.
  snapshot_sha256: d3301fb634b8dfc61b814e080afb6ac0973223501d8b47d1b3f96820458ec5cd
- evidence_id: meta-canonical
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/canonical-metadata.json
  locator: Actual indexed metadata/abstract response at original acquisition
  accessed_at: '2026-10-21T20:29:52.100771Z'
  support: supports
  summary: 'Actual indexed abstract: obligacy, optimum 0.7 and no growth above 4 positive;
    precise lower growth endpoint 0 not established. No body claim.'
  snapshot_sha256: 9d9fea8e5308404e512d4cb133ffdb3753b5f344dcb4bf1d31fec8b3c282ce96
- evidence_id: meta-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/krulwich-metadata.json
  locator: Actual indexed metadata/abstract response at original acquisition
  accessed_at: '2026-10-21T20:29:52.196752Z'
  support: supports
  summary: Actual indexed review abstract and status only; detailed publisher/BioC
    readings separately bound.
  snapshot_sha256: 429676cee65fc86210f134f6297d9e819c407728fa9b4079b74b2bb91871ba84
- evidence_id: meta-baker
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/baker-metadata.json
  locator: Actual indexed metadata/abstract response at original acquisition
  accessed_at: '2026-10-21T20:29:52.065859Z'
  support: supports
  summary: Actual low-pH homeostasis abstract contains reversed membrane potential
    literally and defines acidophiles by optimum below 3.
  snapshot_sha256: bbb644768a65e861ab90856bb709193ba9d2af21b8a8f380e3a66718db7208cd
- evidence_id: meta-organic
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/organic-metadata.json
  locator: Actual indexed metadata/abstract response at original acquisition
  accessed_at: '2026-10-21T20:29:52.081612Z'
  support: supports
  summary: Actual environmental Nitrosotalea study identity/status; generic selected
    Introduction clause is separate from metadata and efficacy excluded.
  snapshot_sha256: aca857cf1fbbc6aa2276a55d54bcb2f6bec41896977d1bc87167e7ea9aae4d1e
- evidence_id: meta-chapter
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/chapter-crossref.json
  locator: Crossref DOI/title/type/author/date fields; no abstract
  accessed_at: '2026-10-21T20:30:03.484929Z'
  support: supports
  summary: The Microbiology of Extremely Acidic Environments resolves as ASM Press
    book chapter. Identity does not establish unavailable body statements.
  snapshot_sha256: f28afbcff1b0b2426502b524bb51c02972ee0de8e13385ce65d8ad94fd59fc9a
- evidence_id: body-krulwich-bioc
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/krulwich-bioc.xml
  locator: Selected BioC generic classification/PMF passages
  accessed_at: '2026-10-21T07:57:33Z'
  support: supports
  summary: Generic extreme-acidophile/reversed-potential context positive; detailed
    pathogen/efficacy branches not assessed.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: body-krulwich-publisher
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/krulwich-publisher.html
  locator: Publisher Key Points
  accessed_at: '2026-10-21T07:56:36Z'
  support: supports
  summary: Actual publisher pH 1.0–3.0 wording verifies two snippets after dash normalization;
    acid exposure context does not independently establish exact alias 0.
  snapshot_sha256: 4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66
- evidence_id: body-organic
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/organic.xml
  locator: JATS article identity and Introduction body paragraph 3 generic organic-acid
    clause
  accessed_at: '2026-10-21T20:30:48.873702Z'
  support: supports
  summary: Generic organic-acid membrane passage/proton release/acidification clause
    supports existing environmental context; incidental pathogen mechanisms and perturbation
    outcomes unassessed.
  snapshot_sha256: 51c46be8eed16a45cdb14b5e3aa58a4312acd66a3c27b49e1ef3435d35b132fa
- evidence_id: body-permeability
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/permeability.pdf
  locator: Publisher PDF page 1 abstract/identity, page 3 exception and page 4 Table
    1
  accessed_at: '2026-10-21T20:30:47.724629Z'
  support: supports
  summary: Acidophilic examples can extend above 4; existing permeability note positive
    with Picrophilus intracellular 4.6 exception. Table viewed as rendered image;
    no historical phenotype transfer.
  snapshot_sha256: 6049ec0d36851a2b18f6cc546949b1c90bf02663e8dc4693d74c98cf02c0ecd9
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/source-assessment.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.838755Z'
  support: supports
  summary: Six assigned works and bounded source decisions; root controls final disposition.
  snapshot_sha256: 51a8895ea43ca957eceabc3d16278caadd42dd6d1282c7bc6024b47d8fca5f96
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: Actual EPMC/Crossref/publisher identity shapes and original acquisition
    times.
  snapshot_sha256: f26fd893bcc4407ebf5f90e7623e3ed1d6231a5014b9d3646c446f57a2e824d3
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/placement-ledger.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: Ten external placements, three grounding fields and six synonym-source
    placements.
  snapshot_sha256: e6512e46c551f8fe4c113eb3ba2401aaae02edac7ba9baf4754cfe9c25980165
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/snippet-ledger.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: One literal Baker abstract phrase and two typography-normalized publisher
    phrases; no unknown schema snippet.
  snapshot_sha256: 633b30d37cfb7e242eed492e7d305d48ee346aae70537dfa2ca53bb4017be8d9
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/node-source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: All eleven node-source contexts.
  snapshot_sha256: e7226092b5f4cac9c1223f25cb36725077ffcf635a8776c08a7e2c3f74c6742d
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/edge-source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: All seven edge-source contexts and unavailable chapter limits.
  snapshot_sha256: 96908fc9c209797df98c938ee0982b7cf376345bf9feb58c0e38e839b4aaf10b
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/publication-status-ledger.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: Actual returned status fields; zero EPMC hits/429 do not mean nonexistent
    sources.
  snapshot_sha256: c002ffd479643919cfeaf9533ccdcc23f5a27e022794585857af477da8a885d3
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/selected-primary-reading.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: Selected actual primary reading scopes, PDF table image and incidental
    excluded passages.
  snapshot_sha256: e7800406e7c7b3efbb90f02f2e0936395383930851ae2b025ab2ac7e4edfae72
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/access-limitations.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: Chapter 403 and browser failure; Springer 200 challenge differs from root
    successful abstract preview.
  snapshot_sha256: 5616a75c4855ae72238420c23990474b355d75863878f49469bafb0188f87860
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/reuse-and-copy-receipt.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:30:55.308242Z'
  support: supports
  summary: Actual original publisher/BioC acquisition separate from current metadata,
    copies and readings.
  snapshot_sha256: 7a23e8d0bbc1a1a1948f2c6184d8650ed80744b2aa59ae5964bbd23168e724eb
- evidence_id: source-acquisition
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/primary-access-receipts.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:30:48.874057Z'
  support: supports
  summary: Two primary successes and retained failed/challenge responses; none relabeled
    as native failure.
  snapshot_sha256: b4507c46753a8dcb7e41624594e2a84f9db37e9e0d5f07c508c5ae91d848516e
- evidence_id: bin-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/classification-and-bin-assessment.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: Confirmed source group only alias 1, definition and node 0 description;
    other qualitative aliases unresolved.
  snapshot_sha256: af94e0169fe3727e3b1ad10f900d8cf966d13edb1199d033bf0a4c5cfc094066
- evidence_id: canonical-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/canonical-assessment.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: Positive obligacy/upper 4/optimum 0.7; precise lower 0 remains unknown.
  snapshot_sha256: 428ab74ddadbb2c8a813ea9753c212340140f5598c52589a2577c611f1580167
- evidence_id: near-neutral-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/near-neutral-exception-assessment.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: Source explicitly qualifies Picrophilus intracellular 4.6; generic branch
    remains positive, no uniform canonical assignment.
  snapshot_sha256: be7643a27f78bed6e3169b7e6a5c4239d43e9f2939c4cf407e4f3749d72e7b1a
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/native-check-context.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.829770Z'
  support: supports
  summary: Actual native/strict/snippet receipts and retained logs.
  snapshot_sha256: 38233d2d56fa1a035e07949d9c2b58b2957dcf5a1d398f3f15ac2dc53ed18cb4
- evidence_id: source-capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/final-capture-verification.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.838899Z'
  support: supports
  summary: All 136 successful capture inputs unchanged.
  snapshot_sha256: d6b2f5a09b10f106e0b34af33a4a812fa0628d01669dec2756677fb384fed3df
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-agent/evidence-manifest.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:33:21.845327Z'
  support: supports
  summary: Thirty-six frozen source artifacts verified.
  snapshot_sha256: 220a5ce4be5e529e224c253aca1cbdc9b7d407df9167ae313253e8f14f2cbe76
- evidence_id: root-reading-87
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-root/publisher-browser-observations.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:31:20.097542Z'
  support: supports
  summary: Only the actual bounded root reading/observation/verification scope; receipt
    hash is not an article-body hash.
  snapshot_sha256: bb421d197097f71901e54a7574d13dcdf1605de47a5157381d1778343fedcf50
- evidence_id: root-reading-88
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-root/root-final-evidence-reading.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:34:25.343128Z'
  support: supports
  summary: Only the actual bounded root reading/observation/verification scope; receipt
    hash is not an article-body hash.
  snapshot_sha256: ef32d9757b289c414a595df0d68a7c7570a9b4b8aee907caef6848c993ec8067
- evidence_id: root-reading-89
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-root/root-metadata-reading.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:31:20.097542Z'
  support: supports
  summary: Only the actual bounded root reading/observation/verification scope; receipt
    hash is not an article-body hash.
  snapshot_sha256: 81db93dd1280bc72ae0e3eaf7358a2cda2f7a4afe30bb7457d8bac4ffb62cc3c
- evidence_id: root-reading-90
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-root/root-primary-reading.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:32:36.125096Z'
  support: supports
  summary: Only the actual bounded root reading/observation/verification scope; receipt
    hash is not an article-body hash.
  snapshot_sha256: 3df9533cbe3c365ebcb91ef7aa11fa802ca3e13f9c069682105889d4180ad304
- evidence_id: root-reading-91
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-source-root/whole-target-root-reading.json
  locator: Derived audit or actual reading/access receipt; primary snapshots separately
    identified
  accessed_at: '2026-10-21T20:29:25.607235Z'
  support: supports
  summary: Only the actual bounded root reading/observation/verification scope; receipt
    hash is not an article-body hash.
  snapshot_sha256: 645f06f81ab410ed8d77f8e68b175bd1b0c9341c5dc09055a3114bca54103874
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent challenge
  accessed_at: '2026-10-21T20:37:32.848033Z'
  support: supports
  summary: Final recommendation, exact field anchors and evidence bindings verified.
  snapshot_sha256: be349a0ea230db36ca08130285e1c2da07af2a716b00b39cfd3a1cae94ffc977
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-very-low-root-adjudication.json
  locator: Final root disposition
  accessed_at: '2026-10-21T20:41:33.290106Z'
  support: supports
  summary: Final root controls findings, severities and declined cases.
  snapshot_sha256: af16c6f5839442301ca68d8543306ad8ceacc75eb4657498ea08a62750ff9722
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active identity and exact category scope'
  outcome: concern
  target_ids:
  - METPO:1000459
  summary: Active numerical identity, hierarchy, predecessors and supplied synonym
    provenance are positive. Exact Acidophile alias is broader than the complete 0–4
    convention; other qualitative aliases remain unresolved.
  evidence_ids:
  - record
  - identity
  - metpo-primary
  - bin-scope
  - body-permeability
  - challenge
  - adjudication
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: reach versus complete interval'
  outcome: concern
  target_ids:
  - METPO:1000459
  summary: Definition and node 0 describe reaching at or below 4, which can include
    growth above 4 and differs from the explicit complete 0–4 convention. Approximation
    is preserved; no universal cutoff or raw-OWL containment axiom is invented.
  evidence_ids:
  - record
  - bin-scope
  - identity
  - owners
  - challenge
  - adjudication
- assessment_id: hierarchy
  area: identity
  topic: 'Native checklist: direct parent and local authorities'
  outcome: supported
  target_ids:
  - METPO:1000459
  summary: Parent 1000332, explicit predecessor links, local confers and RDFS hierarchy
    match the captured authorities.
  evidence_ids:
  - metpo-primary
  - identity
  - local-authority
  - node-edges
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: all assigned identities and placements'
  outcome: supported
  target_ids:
  - METPO:1000459
  summary: Six works resolve through four current EPMC records, chapter Crossref and
    actual Frontiers PDF. All ten external placements and source-specific limitations
    are covered; unavailable chapter body is unknown rather than false.
  evidence_ids:
  - source-ledger
  - placements
  - source-status
  - source-access
  - meta-chapter
  - body-permeability
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: literal and typography fidelity'
  outcome: supported
  target_ids:
  - METPO:1000459
  summary: Baker reversed-membrane-potential phrase is literal in the actual abstract;
    two Krulwich occurrences match retained publisher Key Points after dash normalization.
    Native 1 VERIFIED/2 NOT_IN_ABSTRACT retained unchanged.
  evidence_ids:
  - snippets
  - meta-baker
  - body-krulwich-publisher
  - native-checks
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: canonical phenotype and identity'
  outcome: unknown
  target_ids:
  - METPO:1000459
  summary: Assigned abstract directly supports obligacy, optimum 0.7 and no growth
    above 4, but not measured lower growth endpoint 0. Current taxonomy synonymy is
    positive; historical named-study measurement transfer remains explicitly limited.
  evidence_ids:
  - canonical-scope
  - meta-canonical
  - taxon-primary
  - taxon-reuse
- assessment_id: nodes
  area: consistency
  topic: 'Native checklist: all eleven represented facets'
  outcome: supported
  target_ids:
  - METPO:1000459
  summary: Current steady membrane potential, permeability quality, compartment and
    explicit processes are coherent. Envelope/prevention and near-neutral maintenance
    language remain bounded facet qualifications; no automatic additional retype or
    mandatory grounding.
  evidence_ids:
  - node-edges
  - node-sources
  - schema
  - go-primary
  - near-neutral-scope
  details: '[{"index": 0, "field": "causal_graphs[0].nodes[0]", "node": {"node_id":
    "ph_range_very_low_trait", "label": "pH range very low", "node_type": "TRAIT",
    "grounding": "METPO:1000459", "description": "pH growth-supporting range reaching
    ≤ ~4."}, "status": "supported", "assessment": "Active numerical trait METPO:1000459.
    Its reaching-at-or-below-4 wording is distinct from the complete 0–4 interval
    used by its canonical note; source-scope adjudication is separate."}, {"index":
    1, "field": "causal_graphs[0].nodes[1]", "node": {"node_id": "ph_range", "label":
    "pH range", "node_type": "TRAIT", "grounding": "METPO:1000332", "description":
    "Span of external pH values supporting growth."}, "status": "supported", "assessment":
    "Explicit active parent METPO:1000332, matching raw direct superclass."}, {"index":
    2, "field": "causal_graphs[0].nodes[2]", "node": {"node_id": "extreme_acidophile_envelope",
    "label": "extreme-acidophile envelope barrier", "node_type": "BIOLOGICAL_PROCESS",
    "description": "Combined low-permeability membrane and reversed membrane potential
    preventing cytoplasmic acidification at strongly acidic external pH."}, "status":
    "limitation", "assessment": "Envelope barrier label suggests material structure
    or properties, but prevention wording permits a composite protection process.
    BIOLOGICAL_PROCESS is not conclusively wrong from this text alone. Clarify referent
    if curated; no forced enum or new mechanism."}, {"index": 3, "field": "causal_graphs[0].nodes[3]",
    "node": {"node_id": "potassium_influx", "label": "potassium influx / K+ transport",
    "node_type": "BIOLOGICAL_PROCESS", "description": "Active influx of cations such
    as K+ across the cytoplasmic membrane."}, "status": "supported", "assessment":
    "Explicit influx/transport process, consistent with BIOLOGICAL_PROCESS. Biological
    efficacy is not established by formal fit."}, {"index": 4, "field": "causal_graphs[0].nodes[4]",
    "node": {"node_id": "reversed_membrane_potential", "label": "inside-positive (reversed)
    membrane potential", "node_type": "STATE", "description": "Inside-positive transmembrane
    electrical potential characteristic of extreme acidophiles."}, "status": "supported",
    "assessment": "Explicit inside-positive electrical steady state, consistent with
    STATE and exact maintained migration rationale. It is not the process that establishes
    the potential; this creates edge 3 role conflict."}, {"index": 5, "field": "causal_graphs[0].nodes[5]",
    "node": {"node_id": "proton_influx", "label": "passive proton influx", "node_type":
    "BIOLOGICAL_PROCESS", "description": "Passive entry of protons/hydronium ions
    into the cytoplasm down the steep pH gradient."}, "status": "supported", "assessment":
    "Explicit passive entry process; consistent BIOLOGICAL_PROCESS and compatible
    object of negative process regulation."}, {"index": 6, "field": "causal_graphs[0].nodes[6]",
    "node": {"node_id": "low_proton_permeability", "label": "low passive proton permeability",
    "node_type": "QUALITY", "description": "Low permeability of the cell envelope
    to passive proton flux."}, "status": "supported", "assessment": "Measurable permeability
    property is QUALITY; no mandatory PATO grounding."}, {"index": 7, "field": "causal_graphs[0].nodes[7]",
    "node": {"node_id": "near_neutral_cytoplasmic_ph", "label": "near-neutral cytoplasmic
    pH", "node_type": "STATE", "description": "Maintenance of a near-neutral intracellular
    pH despite strongly acidic external pH."}, "status": "limitation", "assessment":
    "Near-neutral intracellular pH names a state; description uses maintenance language
    that could denote a process. Current state reading is coherent and free predicate
    explicitly says maintenance. No automatic retype finding; scope of near-neutral
    value remains source-specific."}, {"index": 8, "field": "causal_graphs[0].nodes[8]",
    "node": {"node_id": "weak_organic_acids", "label": "protonated weak organic acids",
    "node_type": "CHEMICAL", "description": "Lipophilic protonated weak organic acids
    (e.g., acetic acid) that can permeate the membrane."}, "status": "supported",
    "assessment": "Class of protonated weak organic acids denotes chemical material.
    No compulsory single ChEBI species for an aggregate class."}, {"index": 9, "field":
    "causal_graphs[0].nodes[9]", "node": {"node_id": "cytoplasm", "label": "cytoplasm",
    "node_type": "CELLULAR_LOCALIZATION", "description": "Intracellular cytoplasmic
    compartment.", "grounding": "GO:0005737"}, "status": "supported", "assessment":
    "GO:0005737 is cytoplasm, cellular_component, with actual definition excluding
    plasma membrane/nucleus and including other subcellular structures. Current compartment/localization
    referent fits."}, {"index": 10, "field": "causal_graphs[0].nodes[10]", "node":
    {"node_id": "cytoplasmic_acidification", "label": "cytoplasmic acidification",
    "node_type": "BIOLOGICAL_PROCESS", "description": "Acidification of the cytoplasm
    by influx and dissociation of permeant protons/acids."}, "status": "supported",
    "assessment": "Explicit cytoplasmic acidification process; no formal type defect
    or required additional grounding."}]'
- assessment_id: predicates
  area: consistency
  topic: 'Native checklist: all seven relation roles'
  outcome: concern
  target_ids:
  - METPO:1000459
  summary: RO2212 edge 3 inherits process-subject requirements through 2211 and conflicts
    with the explicit electrical state. Process object is positive; local confers,
    Biolink causes and free predicates have no invented executor restriction.
  evidence_ids:
  - node-edges
  - ro-primary
  - biolink-primary
  - local-authority
  - owners
  - challenge
  - adjudication
  details: '[{"index": 0, "field": "causal_graphs[0].edges[0]", "subject": "extreme_acidophile_envelope",
    "predicate": "confers", "predicate_id": "METPO:2007700", "object": "ph_range_very_low_trait",
    "status": "supported", "assessment": "Local v8 confers takes broad causal-node
    endpoints and presence/activity/state as basis of a trait. Current process-facet
    subject and trait object fit; source efficacy/bin calibration remains separate.",
    "biology_scope": "Generic referents/formal ontology and existing classification
    only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."},
    {"index": 1, "field": "causal_graphs[0].edges[1]", "subject": "ph_range_very_low_trait",
    "predicate": "is a", "predicate_id": "rdfs:subClassOf", "object": "ph_range",
    "status": "supported", "assessment": "RDFS subclass connects current class to
    its explicit raw parent. Literature excerpt does not replace ontology hierarchy
    authority.", "biology_scope": "Generic referents/formal ontology and existing
    classification only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention
    efficacy UNASSESSED_SCOPE."}, {"index": 2, "field": "causal_graphs[0].edges[2]",
    "subject": "potassium_influx", "predicate": "causes", "predicate_id": "biolink:causes",
    "object": "reversed_membrane_potential", "status": "supported", "assessment":
    "Actual Biolink causes inherits named-thing endpoints; process-to-state is formally
    permitted. No material-only endpoint rule is invented.", "biology_scope": "Generic
    referents/formal ontology and existing classification only; detailed pathogen
    acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."}, {"index":
    3, "field": "causal_graphs[0].edges[3]", "subject": "reversed_membrane_potential",
    "predicate": "decreases", "predicate_id": "RO:0002212", "object": "proton_influx",
    "status": "major", "assessment": "RO:0002212 negatively regulates is a subproperty
    of RO:0002211, whose domain and range are BFO:0000015 process. Current steady
    electrical STATE subject fails that role; proton-influx process object fits. Current
    history notes lack of direct domain/range but omits inherited endpoints. One current
    formal-role finding, not a separate biology/sign allegation.", "biology_scope":
    "Generic referents/formal ontology and existing classification only; detailed
    pathogen acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."},
    {"index": 4, "field": "causal_graphs[0].edges[4]", "subject": "low_proton_permeability",
    "predicate": "enables maintenance of", "predicate_id": null, "object": "near_neutral_cytoplasmic_ph",
    "status": "limitation", "assessment": "Free enables maintenance of is not asserted
    RO:0002327. Quality-to-state maintenance wording has no imported executor requirement.
    Source-specific near-neutral range and efficacy remain separate/unassessed.",
    "biology_scope": "Generic referents/formal ontology and existing classification
    only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE."},
    {"index": 5, "field": "causal_graphs[0].edges[5]", "subject": "weak_organic_acids",
    "predicate": "diffuse into", "predicate_id": null, "object": "cytoplasm", "status":
    "unassessed_scope", "assessment": "Free diffuse into connects chemical material
    to cytoplasmic compartment; no imported role or mandatory predicate identifier.
    Literal/source identity may be audited separately; detailed acid-defense/intervention
    efficacy excluded.", "biology_scope": "Generic referents/formal ontology and existing
    classification only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention
    efficacy UNASSESSED_SCOPE."}, {"index": 6, "field": "causal_graphs[0].edges[6]",
    "subject": "weak_organic_acids", "predicate": "cause", "predicate_id": null, "object":
    "cytoplasmic_acidification", "status": "unassessed_scope", "assessment": "Free
    cause connects chemical class to process without an asserted imported predicate.
    No generic chemical exclusion; detailed pathogen/defense/fitness/AMR/intervention
    biology is unassessed.", "biology_scope": "Generic referents/formal ontology and
    existing classification only; detailed pathogen acid-defense/fitness/ROS/AMR/intervention
    efficacy UNASSESSED_SCOPE."}]'
- assessment_id: biology
  area: evidence
  topic: 'Native checklist: bounded environmental support and exclusions'
  outcome: unknown
  target_ids:
  - METPO:1000459
  summary: Existing generic environmental statements receive selected source context.
    Chapter nearest-body attribution remains unknown, near-neutral exception retained,
    and exact-bin universal mechanism calibration is unestablished. Detailed pathogen
    acid-defense/fitness/AMR/ROS and intervention efficacy are UNASSESSED_SCOPE.
  evidence_ids:
  - edge-sources
  - source-reading
  - source-access
  - near-neutral-scope
  - body-organic
  - body-permeability
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: quantitative NONMECHANISTIC applicability'
  outcome: supported
  target_ids:
  - METPO:1000459
  summary: Four components, zero proteins and zero instances are compatible with the
    recorded quantitative NONMECHANISTIC scope. No mandatory connectivity, token protein,
    extra pathway or experimental design is imposed.
  evidence_ids:
  - record
  - node-edges
  - policy
  - ground-reading
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: structured catalog applicability'
  outcome: not_applicable
  target_ids:
  - METPO:1000459
  summary: No exact canonical, current synonym or type alias in the retained 20-organism/28-dataset
    catalog; no substitute organism/module query. Catalog original acquisition remains
    separate from current reading.
  evidence_ids:
  - expression
  - authority-reuse
  - taxon-primary
- assessment_id: ownership
  area: provenance
  topic: 'Native checklist: actual writers and recurrence guards'
  outcome: supported
  target_ids:
  - METPO:1000459
  summary: Record, synonym seeder, mapping/grounder and exact process-quality node-family
    writer are identified. Existing predicate IDs are skipped; node migration retains
    outgoing relation. Historical enables/microbe-domain selectors and sibling review/repair
    are not automatic current repairs.
  evidence_ids:
  - owners
  - ground-reading
  - local-authority
- assessment_id: human
  area: provenance
  topic: 'Native checklist: bounded current acceptance'
  outcome: concern
  target_ids:
  - METPO:1000459
  summary: Eleven AI events plus seed and 14 AI histories do not identify attributable
    current acceptance. Ignored-inclusive 170 paths/67 parsed arrays/zero exact targets
    bound the concern; private/remote review is not ruled out.
  evidence_ids:
  - owners
  - ground-reading
  - playbook
  - challenge
  - adjudication
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: actual checks and provenance chronology'
  outcome: supported
  target_ids:
  - METPO:1000459
  summary: All 136 captured inputs and frozen source/ground/root/challenge bindings
    match. Focused native/strict/snippet checks passed. Reused common failures/skips
    and actual B10 QC retain original times; failed primary accesses remain separate.
  evidence_ids:
  - capture
  - source-capture
  - reuse
  - reuse-postcheck
  - native-checks
  - source-acquisition
  - check-ph-range-very-low-native
  - check-ph-range-very-low-strict
  - check-ph-range-very-low-snippets
findings:
- finding_id: category-and-bin-scope
  issue_key: ph-range-very-low-category-and-bin-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Acidophile category and lower-end reach exceed complete 0–4 scope
  description: Assigned Frontiers Table 1 lists acidophilic growth intervals extending
    above 4, so exact Acidophile alias is not complete 0–4 equivalence. Definition
    and node 0 likewise permit a lower-end reach without confining the complete interval.
    Numeric identity and faithful import remain positive. Other qualitative aliases
    are unverified, not additional confirmed fields.
  target_ids:
  - METPO:1000459
  field_paths:
  - synonyms[1]
  - definition
  - causal_graphs[0].nodes[0].description
  evidence_ids:
  - bin-scope
  - body-permeability
  - metpo-primary
  - identity
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_very_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Faithful synonym import owner; scientific equivalence is separate.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: imported-relation-role
  issue_key: ph-range-very-low-imported-relation-role
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Negative regulation requires a process subject
  description: Edge 3 RO2212 inherits process/process roles from RO2211. Its current
    inside-positive electrical STATE subject is not the process establishing it; proton-influx
    process object fits. The historical direct-domain statement is incomplete, not
    a second finding or biological-sign allegation.
  target_ids:
  - METPO:1000459
  field_paths:
  - causal_graphs[0].edges[3]
  evidence_ids:
  - node-edges
  - ro-primary
  - schema
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_very_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current decreases row; wildcard gates do not waive inherited roles.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Current nonempty IDs are skipped; mapping edits alone do not rewrite current
      assertion.
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_process_quality_consistency.py
    role: Exact reversed-potential node-family owner; STATE decision preserves the
      outgoing relation, not a predicate replacement writer.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: ph-range-very-low-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current local provenance lacks an attributable acceptance link
  description: Eleven AI events plus seed, 14 captured AI histories and REVIEWED status
    do not identify linked current human acceptance. Ignored-inclusive 170 paths/67
    parsed review arrays/zero exact targets bound this traceability concern; no private
    or remote absence claim.
  target_ids:
  - METPO:1000459
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
    path: data/traits/environment/ph_range_very_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-category-and-bin-scope
  description: Reconcile confirmed category and reach-versus-complete-interval wording
    during authorized curation.
  finding_ids:
  - category-and-bin-scope
  target_ids:
  - METPO:1000459
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_very_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Faithful synonym import owner; scientific equivalence is separate.
  acceptance_checks:
  - Preserve numerical identity, related 0–4 alias, faithful import and positive canonical
    upper 4/optimum 0.7.
  - Keep other qualitative aliases and precise canonical lower 0 as explicit follow-ups,
    not already-proven defects.
  - Preserve source-specific conventions and guarded history/validation; no universal
    cutoff or silent source substitution.
- action_id: reconcile-imported-role
  description: Reconcile the current imported relation with the explicitly represented
    electrical state and process referents.
  finding_ids:
  - imported-relation-role
  target_ids:
  - METPO:1000459
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_very_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current decreases row; wildcard gates do not waive inherited roles.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Current nonempty IDs are skipped; mapping edits alone do not rewrite current
      assertion.
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_process_quality_consistency.py
    role: Exact reversed-potential node-family owner; STATE decision preserves the
      outgoing relation, not a predicate replacement writer.
  acceptance_checks:
  - Preserve current STATE interpretation and positive process object.
  - Respect nonempty-ID guard, node-family scope and historical selector limits; mapping
    change alone is insufficient.
  - Do not prescribe an unverified mechanism, new route, perturbation or optimized
    condition.
- action_id: link-human-acceptance
  description: Link attributable current acceptance if available, or clarify status
    while preserving provenance.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000459
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_very_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain actual AI/seed and bounded local search evidence.
  - No contact or automatic status promotion authorized.
limitations:
- Detailed pathogen acid-defense, fitness, AMR, ROS and perturbation efficacy are
  UNASSESSED_SCOPE. Only existing generic environmental context, literal/source identity
  and formal roles were assessed.
- Aliases 0/2/3/4 remain unresolved exact-equivalence questions; extreme 1–3 inside
  0–4 alone is not a confirmed class conflict. Related numeric alias and hierarchy
  remain positive.
- Complete-interval convention comes from the current record/canonical owner; raw
  existential numerical restriction alone is not universal containment.
- Canonical lower growth endpoint approximately 0 is not explicitly established by
  inspected assigned abstract or subscription preview; upper 4/optimum 0.7 and obligacy
  positive. Current P.torridus synonymy does not silently transfer historical named-study
  measurements into that note.
- Near-neutral source phrase is positive generic context with explicit Picrophilus
  intracellular 4.6 exception. No uniform canonical-to-every-branch assignment or
  additional false-mechanism finding.
- Chapter identity resolves but body statements remain unknown after 403/browser failure.
  Organic generic introductory support is supplemental context, not replacement verification
  of chapter wording.
- Springer download returned a client challenge despite 200; separate root browser
  actual abstract/preview is accurately attributed. Frontiers PDF/image/text and organic
  JATS are actual successful snapshots.
- Four disconnected components and zero protein classes/instances are permitted by
  NONMECHANISTIC scope. No compulsory connector, accession, new pathway or optimization.
- Fourteen whole-history reads are grounding-agent work. Root summary/projections
  and source selected readings remain separately attributed. Current report frontmatter
  is a lead, not proof of the exact earlier enrichment version.
- Original publisher 07:56:32–36/BioC 07:57:33, catalog and taxonomy 18:48:17 acquisitions
  remain separate from current metadata/body requests, copies and reading times. Browser
  observation receipts do not invent downloaded-body hashes or unclocked call intervals.
notes:
- Final root adjudication and independent challenge are pinned and verified. Author
  preparation did not import or execute this serializer; the root owns its later single
  execution, native validation and save.
- 'Coverage: six works, ten external placements, three grounding fields, six synonym-source
  placements, eleven nodes/seven edges, one canonical, three snippets: one literal
  and two typography-normalized.'
- No scientific record, native inventory, Git or sweep state mutation by serializer
  preparation.
tags:
- record-review
- ph-range-very-low
- environment
- needs-curation
native_verdict: needs_curation
```
