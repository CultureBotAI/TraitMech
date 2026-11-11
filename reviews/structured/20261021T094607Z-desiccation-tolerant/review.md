# Definition, evidence and relation review of desiccation tolerance

- Review: 20261021T094607Z-desiccation-tolerant
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T09:33:09Z
- Finished UTC: 2026-10-21T09:46:07Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The definition, related synonym and genus-level desiccation example are supported, and both quotations are exact. One major finding concerns edge5: process-only RO:0002213 is assigned to chemical trehalose, with recurrence possible through the wildcard mapping. Three minor findings concern nearest repair-evidence placement, ancillary radiation/endolithic details in the canonical note, and a bounded missing human-acceptance link. All thirteen nodes, ten edges, seven references and fifteen citation placements were assessed using seven complete article bodies. Positive contextual biology, eLife version-of-record status and source-specific limits are preserved.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: One complete maintained TraitRecord, read before native capture. All thirteen nodes, ten edges, one canonical example, seven references, fifteen citation placements, two snippets and nine history events are included. Contextual ontology, source, parent and writer inputs are not additional review targets; the excluded spore-germination record remains untouched.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000010 | data/traits/environment/desiccation_tolerant.yaml | maintained | desiccation tolerant |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000010 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000010 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000010 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000010 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | traitmech:000010 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000010 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000010 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000010 | Passed at 09:34:03–06Z; structural validity does not establish external relation roles or scientific source support. |
| Focused strict validation | passed | True | traitmech:000010 | Passed at 09:34:03–09Z with zero strict errors. The external process-role mismatch is assessed separately. |
| Focused abstract snippet check | passed | True | traitmech:000010 | Passed at 09:34:05–09Z: both occurrences are NOT_IN_ABSTRACT, an inconclusive retrieval result. Subsequent actual complete article bodies verify both quotations exactly. |
| Reused native full-corpus QC | passed | True | traitmech:000010 | Actual B4 execution 09:19:10–09:21:17Z passed. B5 byte comparison supports reuse for unchanged scientific and common-check inputs. Original baselines and warnings remain; this is not a fresh B5 execution or semantic certification. |
| Live UniProt instance audit | not_applicable | False | traitmech:000010 | No protein instance or UniProt accession is asserted. The explicit label-only aggregate and contextual graph do not require a token accession. |
| Structured-source runner discovery | unavailable | False | traitmech:000010 | Hash-verified reuse of bounded discovery with original execution times; official catalog fallback inspected. |
| Canonical-organism dataset applicability | not_applicable | False | traitmech:000010 | No matching canonical Chroococcidiopsis dataset in the inspected catalog; no organism substitution or module query. |

## Scientific And Domain Assessments

### Native checklist: identifier, label, polarity, synonym and term kind

identity: supported. Targets: traitmech:000010.

The justified local fallback denotes a positive environmental survival class, not an organism, assay or molecular object. The RELATED_SYNONYM anhydrobiotic is conservative and source-backed. A local METPO proposal exists but is not represented as an already active upstream class.

### Native checklist: noncircular survival/recovery definition and attribution

evidence: supported. Targets: traitmech:000010.

The definition distinguishes extreme drying and subsequent growth recovery. The bacterial review supports reversible anhydrobiosis, retaining suspended-or-undetectable metabolism as source context. A broad environmental class does not require one universal molecular route.

### Native checklist: strictly broader parent and environmental category

identity: supported. Targets: traitmech:000010.

Phenotype is strictly broader than environmental desiccation tolerance; ENVIRONMENT and CLASS are coherent. The maintained v5 proposal retains the same definition and parent.

### Native checklist: canonical genus and ancillary note scope

evidence: concern. Targets: traitmech:000010.

Current Chroococcidiopsis genus identity is exact. The cited CCMEE029 strain supplies a valid desiccation/desert/lithic example without asserting the phenotype for every genus member. Radiation and specifically endolithic wording exceed the directly inspected supporting statements and need bounded precision.

### Native checklist: graph scope, all thirteen node kinds and optional fields

representation: supported. Targets: traitmech:000010.

The contextual NONMECHANISTIC classification and reviewed-label-only IDP aggregate are coherent. Activity nodes remain activities, oxidative stress denotes accumulation/damage, and vitrification denotes formation. No token protein, extra pathway link, optional domain/range, priority/subset, discussion or dataset is required solely to fill an optional field.

### Native checklist: all node identities, proposal status and label-only aggregate

grounding: supported. Targets: traitmech:000010.

The four GO node identifiers are active and exact in meaning/aspect. The trait fallback and local confers proposal retain their status. Source context supports the label-only aggregate; no single-protein instance or irrelevant live UniProt audit is introduced.

### Native checklist: all ten edge roles and directions

consistency: concern. Targets: traitmech:000010.

Edge5 assigns process-only RO:0002213 to a chemical subject. Other current role assignments are compatible, including molecular-function activities on edges6–8. Biolink permits the existing broad endpoint kinds, local confers accepts state/process to trait, and unassigned stabilizes/synergizes predicates are not automatically invalid.

### Native checklist: seven references and fifteen nearest placements

evidence: concern. Targets: traitmech:000010.

All references resolve and all bodies are accessible. The repair branch has positive support in the definition review, while the attached Genes citation primarily supplies an exact organism background quote and a different-species radiation study; align the stronger notes with their actual source. The other edge claims have positive contextual support with the recorded yeast, cross-kingdom and protein/cosolute limits.

### Native checklist: both snippets against actual article text

evidence: supported. Targets: traitmech:000010.

Both quotations are exact after XML element-boundary/whitespace normalization. The Genes quotation genuinely names D.radiodurans, so its different own-study species is not a quote or citation-identity error. The initial abstract misses are superseded by actual full-text verification.

### Native checklist: bare eLife DOI publication status

evidence: supported. Targets: traitmech:000010.

Official publisher and registration records confirm a published version of record. Preprint-version relationships do not invalidate the cited bare DOI.

### Native checklist: whole-record and contextual mechanism coverage

completeness: supported. Targets: traitmech:000010.

All thirteen nodes and ten edges have an assessment. The sources support reasonable contextual causal explanations without requiring new experiments, exhaustive mechanisms or all-taxon necessity. Formal ontology and nearest-placement defects remain distinct from supported biology.

### Native checklist: optional structured sources and canonical applicability

evidence: supported. Targets: traitmech:000010.

The inspected catalog has no canonical Chroococcidiopsis dataset. Reused bounded runner discovery retains original times; no replacement organism query or negative biological inference follows.

### Native checklist: history, human acceptance, maintained owners and native checks

provenance: concern. Targets: traitmech:000010.

All nine history events disclose AI assistance, including the REVIEWED promotion. No explicit local human-acceptance link was found within the retained ignored-inclusive scope. Wildcard promotes can restore the formal error after an ID-only correction. Native checks pass within their stated execution/reuse limits.

## Findings

### chemical-subject-process-regulation: Process regulation is assigned to a chemical subject

major / open / confirmed; issue key: desiccation-tolerant-chemical-subject-process-regulation.

Edge5 links trehalose CHEMICAL to vitrification BIOLOGICAL_PROCESS using RO:0002213 positively regulates. The relation inherits the explicit process domain/range of RO:0002211 and concerns process execution; the chemical subject does not satisfy that represented role. The literature positively supports trehalose-related glass formation, so this is a grounding mismatch rather than false biology. Wildcard promotes row63 can restore the mismatch if only the identifier is cleared. This is not an asserted reasoner result or native-validation failure.

### repair-evidence-placement: The repair interpretation needs its nearest supporting citation

minor / open / confirmed; issue key: desiccation-tolerant-repair-evidence-placement.

The Genes14091803 quotation exactly supports introductory D.radiodurans desiccation context, but its own study concerns D.irradiatisoli17bor-2 radiation/genome work. The current top-level note and edge2 use it for shared DNA-repair and post-rehydration restoration claims that are not directly established in the inspected body. The separately cited anhydrobiosis review §4.2 positively supports post-rehydration repair and desiccation-induced DNA damage. Align the stronger interpretation and nearest citation with that evidence, preserving the valid quotation and repair branch instead of calling the biology unsupported.

### canonical-ancillary-scope: The canonical note adds ancillary details beyond its cited support

minor / open / confirmed; issue key: desiccation-tolerant-canonical-ancillary-scope.

PMID34122375 supports Chroococcidiopsis desiccation tolerance through CCMEE029 and describes desert strains and lithic provenance. The note also asserts radiation tolerance and specifically endolithic habitat, which are not directly established by the inspected main-body statements about this organism. Retain the supported genus example and strain-limited context, and narrow or directly source these ancillary details. This does not assert that those details are false or that every member of the genus has been tested.

### human-acceptance-link: Human scientific acceptance is not linked locally

minor / open / confirmed; issue key: desiccation-tolerant-human-acceptance-link.

All nine events disclose AI assistance and one explicitly promotes the record to REVIEWED. Ignored-inclusive local target searches and matching review target-list inspection found no explicit human-acceptance link for this revision. The native status gate requires that acceptance; the bounded documentary gap does not establish that no human reviewed the record privately or remotely.

## Recommended Actions And Acceptance Checks

### reconcile-relation

In separately authorized curation, reconcile edge5 with its chemical/process endpoints and the maintained wildcard mapping.

- Retained relation grounding agrees with both endpoint identities and the authority definition; do not relabel the chemical as a process solely to preserve the current relation.
- Address whether unchanged promotes wording can reacquire the rejected grounding after an ID is cleared; do not guess a replacement identifier.
- Preserve the supported generic vitrification explanation and compatible activity/process edges6–8.
- After authorized edits use guarded writes, append-only history, focused strict/term/graph and mapping checks, just qc and maintained derived-product regeneration.

### align-repair-attribution

Align repair notes and nearest evidence with the actual supporting passages already available.

- Preserve the exact Genes introductory quotation and distinguish D.radiodurans background from the D.irradiatisoli own-study context.
- Place support for repair after rehydration beside the claim, with the definition review §4.2 as available positive evidence; retain only source-supported shared-repair wording.
- No new mechanism, molecular target, protocol or experiment is proposed; validate the bibliography and nearest placement through the native guarded curation workflow.

### bound-canonical-note

Retain the valid genus example while narrowing or directly supporting its ancillary note details.

- Keep Chroococcidiopsis genus identity and the cited CCMEE029 desiccation/desert/lithic context.
- Separate directly supported habitat wording from the specifically endolithic and radiation asides; any retained ancillary statement has an actual inspected supporting citation.
- Do not convert strain evidence into a claim about every genus member or misclassify the genus identifier as erroneous.

### link-acceptance

Locate and link existing human scientific acceptance or obtain it through the established process, preserving history and reassessing status if needed.

- Acceptance identifies the reviewed revision and scientific scope.
- AI disclosure, validator success and this review do not substitute for human acceptance; retain append-only provenance.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-005.klfwsp1f/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-desiccation-validate | /private/tmp/traitmech-record-sweep-005.klfwsp1f/desiccation-validate.log; Executed 2026-10-21T09:34:03Z through 2026-10-21T09:34:06Z; metadata desiccation-validate.json | context_only | Passed at 09:34:03–06Z; structural validity does not establish external relation roles or scientific source support. |
| check-desiccation-strict | /private/tmp/traitmech-record-sweep-005.klfwsp1f/desiccation-strict.log; Executed 2026-10-21T09:34:03Z through 2026-10-21T09:34:09Z; metadata desiccation-strict.json | context_only | Passed at 09:34:03–09Z with zero strict errors. The external process-role mismatch is assessed separately. |
| check-desiccation-snippets | /private/tmp/traitmech-record-sweep-005.klfwsp1f/desiccation-snippets.log; Executed 2026-10-21T09:34:05Z through 2026-10-21T09:34:09Z; metadata desiccation-snippets.json | context_only | Passed at 09:34:05–09Z: both occurrences are NOT_IN_ABSTRACT, an inconclusive retrieval result. Subsequent actual complete article bodies verify both quotations exactly. |
| check-batch004-qc | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/batch004-qc.log; Executed 2026-10-21T09:19:10Z through 2026-10-21T09:21:17Z; metadata batch004-qc.json | context_only | Actual B4 execution 09:19:10–09:21:17Z passed. B5 byte comparison supports reuse for unchanged scientific and common-check inputs. Original baselines and warnings remain; this is not a fresh B5 execution or semantic certification. |
| reuse | B5 common-input byte comparison and original execution receipts; 1130 trait files, history and common-check inputs versus B4; unchanged 8eee scientific base | supports | Original f25 diagnostics and B3 history validation retain their execution dates, failed product attempts and adapter skips. The receipt also preserves B4 QC execution. Unchanged-input reuse does not certify later ontology releases. |
| reuse-independent | Independent B5 setup/reuse inspection; Original diagnostics and byte-comparison scope | supports | Independent verification confirmed the reuse basis and original check counts, failures and limits without rerunning scientific validators or current external releases. |
| capture | Native selected-record inspection; 55 inputs captured 09:33:09–11Z after entire target read; grounding review confirmed all hashes | supports | The native capture includes the target, parent, schema, ontology snapshots, review rules, proposals, mappings, maintained writers and research lead. Provider content is not treated as primary scientific proof. |
| record | data/traits/environment/desiccation_tolerant.yaml; Entire identity, definition, synonym, graph, canonical example and history | partial | The record denotes survival of extreme water loss with recovery after rehydration. NONMECHANISTIC classification context and a reviewed label-only protein aggregate do not require a token UniProt example. |
| identity | Pinned METPO and v5 class proposal; Complete active/deprecated label and synonym inspection; v5 classes row12; parent METPO:1000059 | supports | No exact desiccation/anhydrobiosis class was found among the 1631 inspected label elements in the pinned snapshot. The maintained v5 proposal explicitly associates the same label, definition and parent with traitmech:000010 and proposed METPO:1007609. The fallback is justified for this snapshot, not claimed necessary in every unseen later release. |
| local-authority | Native schema/checklist, v5/v8 proposals and maintained mappings; Node kinds; provisional confers roles; REVIEWED human-acceptance gate | supports | STATE and process subjects fit local confers with a TRAIT object. CELLULAR_LOCALIZATION includes components. Provisional identifiers retain proposal status; missing optional groundings or token instances are not automatic defects. The native status rule distinguishes human scientific acceptance from AI assistance and structural validation. |
| ro | RO:0002213 positively regulates; RO:0002212 negatively regulates; RO:0002211 regulates; Original authority inspection 08:04:46.869674Z; hash-verified reuse 09:36:11.317209Z | supports | Both directional regulation properties inherit the explicit process domain/range of regulates. Edge 5 has a chemical subject, whereas edges 6–8 represent molecular activities acting on processes. The former is an intended-role mismatch; the latter are not excluded merely because their subjects are molecular functions. |
| biolink | Biolink Model 4.4.0 causes and inherited slots; Original authority inspection 09:19:29.572066Z; byte-identical reuse 09:36:11.319782Z | supports | The inspected causes chain inherits broad named-thing endpoints. Environmental water loss, physiological state and oxidative-damage process are not formally excluded. Specific causal context is assessed using the literature. |
| go-taxonomy | Official QuickGO and NCBI Taxonomy authorities; GO:0006302, GO:0005886, GO:0003674; NCBITaxon:54298; reused activity terms | supports | Repair, membrane and activity identities/aspects match. The molecular-function root explicitly denotes a molecular process/action, supporting the processual roles of activity nodes. Chroococcidiopsis is the exact current genus, not a species; source scope remains strain-specific. Fresh authority calls ran 09:35:04–05Z; SOD/catalase responses retain their original 08:25:48 acquisition. |
| live-receipts | Fresh official authority response receipts; NCBI 09:35:04.449318–09:35:04.720804Z; QuickGO 09:35:04.453158–09:35:05.132886Z | supports | URLs, actual request times, raw response paths and SHA256 hashes are retained. These identity checks do not establish a desiccation assay or genus-wide phenotype. |
| ledger | Independent complete grounding, source-owner and history review; Thirteen nodes, ten edges, one label-only protein node, no protein examples; nine AI events; all55 capture hashes match | partial | All node and relation roles were assessed. The material-subject regulation error is isolated to edge 5. The other grounded activity/process and local confers roles are coherent. Literature support is independently assessed below. |
| node-edges | Complete independent node/edge ledger; Each of thirteen nodes and ten edges, zero-based | partial | The oxidative-stress description represents accumulation/damage, and vitrification represents glass formation rather than the formed material. Reviewed-label-only IDP scope is explicit. Neither slash labels nor a broad aggregate justify additional automatic type findings. |
| owners | mappings/predicate_grounding.tsv:63; scripts/ground_causal_predicates.py:138–179; Wildcard promotes mapping; populated-ID skip; node, fallback and confers owners | supports | The writer skips existing IDs. Clearing edge 5’s ID alone leaves wildcard promotes row63 able to restore process-only RO:0002213 for a chemical subject. Static inspection establishes recurrence risk; no writer run occurred. Negative-regulation row100 is broad too, but the present activity/process endpoints fit and are not additional findings. |
| provenance | Entire target history and ignored-inclusive local provenance search; 172 matching files; nine events all llm_assisted=true; no target-specific repository history/review link found | partial | An AI-assisted event explicitly promoted the record to REVIEWED. The examined local target matches contain no explicit human-acceptance link. This documents a bounded linkage gap, not an assertion that no human reviewed the record elsewhere. |
| provenance-independent | Independent provenance-applicability inspection; Same retained search receipt; 67 matching review YAML files independently parsed | supports | No target-specific review bundle or human-acceptance link emerged from the matching local review target lists. This was an independent reading of the retained scope, not a new global search. |
| expression | https://imodulondb.org/api/datasets; Original catalog 07:36:12.732638–07:36:12.858149Z; hash-verified reuse and target applicability | context_only | The 20-organism, 28-dataset catalog contains no matching canonical Chroococcidiopsis entry. No module query or replacement organism was used, including the contextual Deinococcus example. Catalog noncoverage is not evidence of absent phenotype/function. |
| runner | Structured-source runner discovery and explicit reuse provenance; Original fresh PATH/B5 search 09:27:57.380287–09:27:57.542053Z; earlier external bounds 08:17:15; reused09:35:23Z | context_only | No runner was found within the documented PATH/B5 filenames and pyproject search. External search bounds retain their earlier original times. Desiccation applicability reused these hashes rather than claiming another execution. |
| bibliography | Complete source/claim and acquisition ledger; Seven references, fifteen placements, two snippets, thirteen nodes and ten edge claims | partial | All seven identities resolve and all seven complete publisher-deposited article bodies are saved locally. Relevant passages were actually inspected; this does not claim a full methods/supplement audit. Both snippets are exact. Sixteen successful acquisitions comprise seven metadata responses, seven bodies and two version-authority responses, with real URLs, UTC bounds and hashes. |
| source-receipts | Europe PMC publisher-deposited full-text XML acquisition receipts; Seven complete article XML files acquired09:37:42.073112–09:37:46.277419Z | supports | Each successful response has an actual request/finish time, content type, size and SHA256. Earlier browser challenge/DOI failures are retained separately; source conclusions use the successfully inspected XML, not search-result snippets. |
| definition-source | https://doi.org/10.3390/microorganisms10020432; PMID35208886; PMC8874559; §1/body1, §2/body10,12,14, §4.2/body35–36 | supports | The review supports reversible extreme dehydration, recovery and anhydrobiosis while distinguishing drought tolerance. The first quotation is exact. Section4.2 separately supports repair after rehydration and double-strand damage during desiccation, providing existing-source support for the repair branch even though the record does not attach this reference at edge2. |
| genes-source | https://doi.org/10.3390/genes14091803; PMID37761943; PMC10531146; Intro/body0–3; Discussion/body19–21; Conclusions/body22 | partial | The second snippet exactly quotes introductory D.radiodurans desiccation context. The own study is D.irradiatisoli17bor-2 radiation/genome work. In the complete main-body extraction desiccation appears only in that introductory background and no rehydration passage occurs. The stronger shared-repair/post-rehydration interpretation in the notes and edge2 is not directly established by this nearest citation; separate definition-review support prevents a false unsupported-biology conclusion. |
| canonical-source | https://pubmed.ncbi.nlm.nih.gov/34122375/; DOI10.3389/fmicb.2021.660050; PMC8193680; Intro/sec1/body0–1; Organism provenance/sec3/body6 first sentence | partial | The article concerns Chroococcidiopsis sp.CCMEE029 and directly supports desiccation tolerance, desert strains and lithic growth in the Negev Desert. This supports the genus example through an identified strain. The note’s more specific endolithic habitat and radiation-tolerance aside are not directly established by these main-body passages; the main-body radiation mention concerns D.radiodurans. Genus identity and desiccation phenotype remain supported. |
| crosskingdom-source | https://doi.org/10.1021/acs.chemrev.2c00659; PMID37132487; PMC10375483; §1.2/body8 and §1.3/body13–16 | supports | The review discusses the hydration-monolayer threshold, dehydration-associated oxidative damage and explicitly conserved SOD/catalase defense context. It distinguishes tolerant from sensitive organisms. These passages support the contextual edges without establishing a measured ROS-onset threshold or every taxon’s response; the graph does not expressly require those broader claims. |
| protectants-source | https://doi.org/10.1007/s00203-023-03683-w; PMID37782422; PMC10545650; Sec6 Plasma membrane/body10 including final sentences; Sec8/body23; Sec9/body27 | supports | The yeast review expressly supports trehalose interaction with phospholipid polar groups. The end of body10 directly states that heat-shock proteins can bind denatured proteins, prevent aggregation and aid rehydration repair. Preserve the yeast/review and may/can context; broad contextual nodes do not automatically assert all-taxon necessity. |
| vitrification-source | https://doi.org/10.1038/s41598-023-31586-9; PMID36941331; PMC10027729; Introduction/Sec1/body2,4 | supports | Natural-desiccation background directly supports trehalose-mediated glass formation, reduced molecular motion and prevention of damaging crystals. The paper’s own application concerns a human protein, so this is background support rather than a microbial growth experiment. That evidence type fits the generic explanatory claim; the separate RO role error does not negate it. |
| idps-source | https://doi.org/10.7554/eLife.97231; PMID39560655; PMC11575898; Abstract; s1/body4–7; s2-1/body9–10; s2-3/body25,36 | supports | Selected full-length representatives from two LEA families and the CAHS family, from four eukaryotic organisms, show positive endogenous-cosolute synergy in enzyme-protection readouts. Pair/family differences and distinctions from short motifs are explicit. This supports the existing contextual synergy claim without asserting that every IDP cooperates with every solute or that the study measured microbial survival. |
| elife-version | Official eLife article API and Crossref DOI registration; https://api.elifesciences.org/articles/97231 and DOI10.7554/eLife.97231 registration;09:39:06.556857–09:39:06.833026Z | supports | The API identifies published version-of-record status with publication date2024-11-19; Crossref registers a journal article and relates the bare DOI to its reviewed-preprint versions. The API object version is not the preprint revision number. The bare DOI is valid and is not an unresolved preprint-only citation. |

## Limits And Additional Notes

- All seven article bodies were acquired, but inspection focused on relevant definition, introduction, results and discussion passages. No exhaustive method, supplement or cited-reference audit is claimed.
- The Genes quotation is exact and its D.radiodurans background context is valid. The nearest repair interpretation needs citation precision; the separately cited definition review positively supports repair after rehydration, so no false-mechanism finding is asserted.
- The canonical genus is valid through a specified strain. Radiation and specifically endolithic details remain unsupported by the inspected nearest-source statements, not demonstrated false; no genus-wide phenotype inference is made.
- Cross-kingdom and yeast reviews provide contextual support. The monolayer discussion is not a measured ROS-onset threshold, and may/can wording is retained without inventing an all-taxon necessity claim or new endpoint requirement.
- The vitrification article supports natural-desiccation background while studying a human protein application. The eLife study supports selected full-length eukaryotic IDP/cosolute pairs with enzyme-protection readouts and pair-specific differences; neither is recast as a microbial survival experiment.
- The local METPO fallback and confers proposal are assessed against the pinned snapshot and maintained proposals. No claim is made about unseen newer ontology releases. The external relation mismatch is an intended-role assessment, not a reasoner result.
- Common checks and B4 QC retain original execution times, failures, skips and warnings and are reused on documented unchanged inputs. No fresh full-corpus execution or latest-release certification is implied.
- No protein instance is asserted. Live UniProt instance validation is inapplicable; dataset noncoverage and bounded reused runner discovery do not imply missing biological function.
- Human acceptance outside the declared ignored-inclusive local search remains unknown. This review is not human scientific sign-off.
- No record, mapping, history or generated product was edited. No paid provider call, protocol design, organism optimization or new biological mechanism was performed.
- All node, edge and extracted body-paragraph indices are zero-based.
- Native capture retained55 inputs at09:33:09–11Z, and independent grounding inspection confirmed every captured hash. Nine history events all disclose AI assistance.
- One major and three minor findings. Source access and publication-version receipts retain their actual acquisition times and hashes; abstract misses are superseded only where exact full text was inspected.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094607Z-desiccation-tolerant
kind: record
repository: CultureBotAI/TraitMech
title: Definition, evidence and relation review of desiccation tolerance
started_at: '2026-10-21T09:33:09Z'
finished_at: '2026-10-21T09:46:07Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Current review session did not author or change the captured
    trait. Supporting agents inspected sources and prepared draft observations; root
    reviewer integrates and validates the final review. Historical Codex/Claude curation
    events are disclosed and are not human sign-off.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'The definition, related synonym and genus-level desiccation example are
  supported, and both quotations are exact. One major finding concerns edge5: process-only
  RO:0002213 is assigned to chemical trehalose, with recurrence possible through the
  wildcard mapping. Three minor findings concern nearest repair-evidence placement,
  ancillary radiation/endolithic details in the canonical note, and a bounded missing
  human-acceptance link. All thirteen nodes, ten edges, seven references and fifteen
  citation placements were assessed using seven complete article bodies. Positive
  contextual biology, eLife version-of-record status and source-specific limits are
  preserved.'
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
  - path: data/traits/environment/desiccation_tolerant.yaml
    sha256: e5044ef67c4cf892aafe03b7da222c267aea1fdeeb546c3d95f57c13d4122e97
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
  - path: reports/ontology_snapshot_manifest.tsv
    sha256: 4a157279a8c4e3fc2afb5382a45c31961991bbd1f330f26d0061b0cfd0b4d213
    role: context
  - path: research/traits/environment/desiccation_tolerant-deep-research-falcon.md
    sha256: d3a5a3352f99083f91ae85276c81e033439e1aae27b369b2d8a785727c94abef
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
- target_id: traitmech:000010
  path: data/traits/environment/desiccation_tolerant.yaml
  label: desiccation tolerant
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/desiccation_tolerant.yaml
    role: Maintained TraitRecord; scientific changes require guarded curation
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: METPO-first identifier comparison; target was curator proposed
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: One complete maintained TraitRecord, read before native capture. All
    thirteen nodes, ten edges, one canonical example, seven references, fifteen citation
    placements, two snippets and nine history events are included. Contextual ontology,
    source, parent and writer inputs are not additional review targets; the excluded
    spore-germination record remains untouched.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000010
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000010
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - traitmech:000010
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - traitmech:000010
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - traitmech:000010
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - traitmech:000010
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - traitmech:000010
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - traitmech:000010
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    005 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: desiccation-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000010
  command: just validate data/traits/environment/desiccation_tolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at 09:34:03–06Z; structural validity does not establish external
    relation roles or scientific source support.
  evidence_ids:
  - check-desiccation-validate
- check_id: desiccation-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000010
  command: just validate-strict data/traits/environment/desiccation_tolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at 09:34:03–09Z with zero strict errors. The external process-role
    mismatch is assessed separately.
  evidence_ids:
  - check-desiccation-strict
- check_id: desiccation-snippets
  name: Focused abstract snippet check
  status: passed
  required: true
  target_ids:
  - traitmech:000010
  command: just verify-snippets --record data/traits/environment/desiccation_tolerant.yaml
    --out /private/tmp/traitmech-record-sweep-005.klfwsp1f/desiccation-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed at 09:34:05–09Z: both occurrences are NOT_IN_ABSTRACT, an inconclusive
    retrieval result. Subsequent actual complete article bodies verify both quotations
    exactly.'
  evidence_ids:
  - check-desiccation-snippets
- check_id: batch004-qc
  name: Reused native full-corpus QC
  status: passed
  required: true
  target_ids:
  - traitmech:000010
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual B4 execution 09:19:10–09:21:17Z passed. B5 byte comparison supports
    reuse for unchanged scientific and common-check inputs. Original baselines and
    warnings remain; this is not a fresh B5 execution or semantic certification.
  evidence_ids:
  - check-batch004-qc
- check_id: live-uniprot
  name: Live UniProt instance audit
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000010
  summary: No protein instance or UniProt accession is asserted. The explicit label-only
    aggregate and contextual graph do not require a token accession.
  evidence_ids:
  - record
  - ledger
- check_id: structured-source-runner
  name: Structured-source runner discovery
  status: unavailable
  required: false
  target_ids:
  - traitmech:000010
  summary: Hash-verified reuse of bounded discovery with original execution times;
    official catalog fallback inspected.
  evidence_ids:
  - runner
- check_id: expression-context
  name: Canonical-organism dataset applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000010
  summary: No matching canonical Chroococcidiopsis dataset in the inspected catalog;
    no organism substitution or module query.
  evidence_ids:
  - expression
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-desiccation-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/desiccation-validate.log
  locator: Executed 2026-10-21T09:34:03Z through 2026-10-21T09:34:06Z; metadata desiccation-validate.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: Passed at 09:34:03–06Z; structural validity does not establish external
    relation roles or scientific source support.
  snapshot_sha256: 32804899efe2a4b36e9c2e17ed0092434fcff694c2cd4aaa943c402919cacb6e
- evidence_id: check-desiccation-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/desiccation-strict.log
  locator: Executed 2026-10-21T09:34:03Z through 2026-10-21T09:34:09Z; metadata desiccation-strict.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: Passed at 09:34:03–09Z with zero strict errors. The external process-role
    mismatch is assessed separately.
  snapshot_sha256: c4b58b77454a0f583400615eddf652d5b017a93b14ab251e8cc2bf1b9b6e300b
- evidence_id: check-desiccation-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/desiccation-snippets.log
  locator: Executed 2026-10-21T09:34:05Z through 2026-10-21T09:34:09Z; metadata desiccation-snippets.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: 'Passed at 09:34:05–09Z: both occurrences are NOT_IN_ABSTRACT, an inconclusive
    retrieval result. Subsequent actual complete article bodies verify both quotations
    exactly.'
  snapshot_sha256: 741c0212c29a21229a4ab8543ed1ef19f3ea7762014ddee9670121535d9f00e0
- evidence_id: check-batch004-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/batch004-qc.log
  locator: Executed 2026-10-21T09:19:10Z through 2026-10-21T09:21:17Z; metadata batch004-qc.json
  accessed_at: '2026-10-21T09:46:07Z'
  support: context_only
  summary: Actual B4 execution 09:19:10–09:21:17Z passed. B5 byte comparison supports
    reuse for unchanged scientific and common-check inputs. Original baselines and
    warnings remain; this is not a fresh B5 execution or semantic certification.
  snapshot_sha256: 41a3fbd2beadf60e039992274e868de70b6ade8cf4b5d6028d6df932e0cfb2e5
- evidence_id: reuse
  kind: validation
  reference: B5 common-input byte comparison and original execution receipts
  locator: 1130 trait files, history and common-check inputs versus B4; unchanged
    8eee scientific base
  accessed_at: '2026-10-21T09:46:07Z'
  support: supports
  summary: Original f25 diagnostics and B3 history validation retain their execution
    dates, failed product attempts and adapter skips. The receipt also preserves B4
    QC execution. Unchanged-input reuse does not certify later ontology releases.
  snapshot_sha256: ce111d70655cdee3528b3c85ca4a71468c47d96e84ff4b28c0932389aee61313
- evidence_id: reuse-independent
  kind: validation
  reference: Independent B5 setup/reuse inspection
  locator: Original diagnostics and byte-comparison scope
  accessed_at: '2026-10-21T09:25:47.749251Z'
  support: supports
  summary: Independent verification confirmed the reuse basis and original check counts,
    failures and limits without rerunning scientific validators or current external
    releases.
  snapshot_sha256: 4279ad9f488f187dd2f118a9b6274a60e5f79019225d24b33ce8b25f4ea2ca9f
- evidence_id: capture
  kind: validation
  reference: Native selected-record inspection
  locator: 55 inputs captured 09:33:09–11Z after entire target read; grounding review
    confirmed all hashes
  accessed_at: '2026-10-21T09:33:11Z'
  support: supports
  summary: The native capture includes the target, parent, schema, ontology snapshots,
    review rules, proposals, mappings, maintained writers and research lead. Provider
    content is not treated as primary scientific proof.
  snapshot_sha256: e8f6a407b890943e7dd8392abed04b198314d482fdf25c075bbc862e07e0b2ef
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/desiccation_tolerant.yaml
  locator: Entire identity, definition, synonym, graph, canonical example and history
  accessed_at: '2026-10-21T09:33:09Z'
  support: partial
  summary: The record denotes survival of extreme water loss with recovery after rehydration.
    NONMECHANISTIC classification context and a reviewed label-only protein aggregate
    do not require a token UniProt example.
  snapshot_sha256: e5044ef67c4cf892aafe03b7da222c267aea1fdeeb546c3d95f57c13d4122e97
- evidence_id: identity
  kind: authority
  reference: Pinned METPO and v5 class proposal
  locator: Complete active/deprecated label and synonym inspection; v5 classes row12;
    parent METPO:1000059
  accessed_at: '2026-10-21T09:34:35.112136Z'
  support: supports
  summary: No exact desiccation/anhydrobiosis class was found among the 1631 inspected
    label elements in the pinned snapshot. The maintained v5 proposal explicitly associates
    the same label, definition and parent with traitmech:000010 and proposed METPO:1007609.
    The fallback is justified for this snapshot, not claimed necessary in every unseen
    later release.
  snapshot_sha256: 9891dc2dda6e24a2d802b3a4d7b205d1976b509655a20bc84a5b1de94e0a4e6e
- evidence_id: local-authority
  kind: authority
  reference: Native schema/checklist, v5/v8 proposals and maintained mappings
  locator: Node kinds; provisional confers roles; REVIEWED human-acceptance gate
  accessed_at: '2026-10-21T09:37:32.219494Z'
  support: supports
  summary: STATE and process subjects fit local confers with a TRAIT object. CELLULAR_LOCALIZATION
    includes components. Provisional identifiers retain proposal status; missing optional
    groundings or token instances are not automatic defects. The native status rule
    distinguishes human scientific acceptance from AI assistance and structural validation.
  snapshot_sha256: c957a0e6997bdddfcd930ad1f953b1a8877a465a5d78e23a9dbce782cb6f1736
- evidence_id: ro
  kind: authority
  reference: RO:0002213 positively regulates; RO:0002212 negatively regulates; RO:0002211
    regulates
  locator: Original authority inspection 08:04:46.869674Z; hash-verified reuse 09:36:11.317209Z
  accessed_at: '2026-10-21T09:36:11.317209Z'
  support: supports
  summary: Both directional regulation properties inherit the explicit process domain/range
    of regulates. Edge 5 has a chemical subject, whereas edges 6–8 represent molecular
    activities acting on processes. The former is an intended-role mismatch; the latter
    are not excluded merely because their subjects are molecular functions.
  snapshot_sha256: 87cbb71ada08152acfe29bef96d1c4686ada7b7e44ac56c4d59b2f51da905314
- evidence_id: biolink
  kind: authority
  reference: Biolink Model 4.4.0 causes and inherited slots
  locator: Original authority inspection 09:19:29.572066Z; byte-identical reuse 09:36:11.319782Z
  accessed_at: '2026-10-21T09:36:11.319782Z'
  support: supports
  summary: The inspected causes chain inherits broad named-thing endpoints. Environmental
    water loss, physiological state and oxidative-damage process are not formally
    excluded. Specific causal context is assessed using the literature.
  snapshot_sha256: c2180f415a8587d7a9bd7259e066047efdade477db2c75bdef3ea76f8653f8d1
- evidence_id: go-taxonomy
  kind: database
  reference: Official QuickGO and NCBI Taxonomy authorities
  locator: GO:0006302, GO:0005886, GO:0003674; NCBITaxon:54298; reused activity terms
  accessed_at: '2026-10-21T09:36:11.310937Z'
  support: supports
  summary: Repair, membrane and activity identities/aspects match. The molecular-function
    root explicitly denotes a molecular process/action, supporting the processual
    roles of activity nodes. Chroococcidiopsis is the exact current genus, not a species;
    source scope remains strain-specific. Fresh authority calls ran 09:35:04–05Z;
    SOD/catalase responses retain their original 08:25:48 acquisition.
  snapshot_sha256: f4274b8fc29a2c5ef5702a937dbf1aeca97009afdebfacc37bb5c73fffe5ed6d
- evidence_id: live-receipts
  kind: database
  reference: Fresh official authority response receipts
  locator: NCBI 09:35:04.449318–09:35:04.720804Z; QuickGO 09:35:04.453158–09:35:05.132886Z
  accessed_at: '2026-10-21T09:35:05.132886Z'
  support: supports
  summary: URLs, actual request times, raw response paths and SHA256 hashes are retained.
    These identity checks do not establish a desiccation assay or genus-wide phenotype.
  snapshot_sha256: 23714ed18c729459ce5496d0e3847cbef9c948256295c8169382247cc973d3bc
- evidence_id: ledger
  kind: validation
  reference: Independent complete grounding, source-owner and history review
  locator: Thirteen nodes, ten edges, one label-only protein node, no protein examples;
    nine AI events; all55 capture hashes match
  accessed_at: '2026-10-21T09:37:32.228982Z'
  support: partial
  summary: All node and relation roles were assessed. The material-subject regulation
    error is isolated to edge 5. The other grounded activity/process and local confers
    roles are coherent. Literature support is independently assessed below.
  snapshot_sha256: 564f3865a37593a994776898f21a8bff7b33f10be056519bbb7c756f7fe19744
- evidence_id: node-edges
  kind: validation
  reference: Complete independent node/edge ledger
  locator: Each of thirteen nodes and ten edges, zero-based
  accessed_at: '2026-10-21T09:37:32.219494Z'
  support: partial
  summary: The oxidative-stress description represents accumulation/damage, and vitrification
    represents glass formation rather than the formed material. Reviewed-label-only
    IDP scope is explicit. Neither slash labels nor a broad aggregate justify additional
    automatic type findings.
  snapshot_sha256: 0994429e0155f2cc448188fc608906ff3c68b533b48454feb925fdef778137d0
- evidence_id: owners
  kind: search
  reference: mappings/predicate_grounding.tsv:63; scripts/ground_causal_predicates.py:138–179
  locator: Wildcard promotes mapping; populated-ID skip; node, fallback and confers
    owners
  accessed_at: '2026-10-21T09:37:32.219494Z'
  support: supports
  summary: The writer skips existing IDs. Clearing edge 5’s ID alone leaves wildcard
    promotes row63 able to restore process-only RO:0002213 for a chemical subject.
    Static inspection establishes recurrence risk; no writer run occurred. Negative-regulation
    row100 is broad too, but the present activity/process endpoints fit and are not
    additional findings.
  snapshot_sha256: e7fa291a004a56581caefeca03ce8fe73aa6982bdad410142161c06071283b45
  search_scope: Ignored-inclusive target label/ID/slug search excluding .git and .venv,
    with supplementary bounded mappings/scripts/proposals search. Exact commands and
    file results are retained; no global absence claim.
- evidence_id: provenance
  kind: search
  reference: Entire target history and ignored-inclusive local provenance search
  locator: 172 matching files; nine events all llm_assisted=true; no target-specific
    repository history/review link found
  accessed_at: '2026-10-21T09:34:48.704690Z'
  support: partial
  summary: An AI-assisted event explicitly promoted the record to REVIEWED. The examined
    local target matches contain no explicit human-acceptance link. This documents
    a bounded linkage gap, not an assertion that no human reviewed the record elsewhere.
  snapshot_sha256: 580a3c16f30da31ca259b5f2151f3c066f639ac648c95dbced685573d8e9f7d4
  search_scope: rg --hidden --no-ignore over repository target ID, label and slug,
    excluding .git/** and .venv/**. Matching local histories and review target lists
    inspected; private and remote acceptance are outside the search.
- evidence_id: provenance-independent
  kind: validation
  reference: Independent provenance-applicability inspection
  locator: Same retained search receipt; 67 matching review YAML files independently
    parsed
  accessed_at: '2026-10-21T09:35:25.946151Z'
  support: supports
  summary: No target-specific review bundle or human-acceptance link emerged from
    the matching local review target lists. This was an independent reading of the
    retained scope, not a new global search.
  snapshot_sha256: b32ff084c12f4b932cf2f6db2d190776f0565f8f6fd2b4cd7e0fad70c2c1dc34
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Original catalog 07:36:12.732638–07:36:12.858149Z; hash-verified reuse
    and target applicability
  accessed_at: '2026-10-21T09:35:25.946673Z'
  support: context_only
  summary: The 20-organism, 28-dataset catalog contains no matching canonical Chroococcidiopsis
    entry. No module query or replacement organism was used, including the contextual
    Deinococcus example. Catalog noncoverage is not evidence of absent phenotype/function.
  snapshot_sha256: 9178bd8dc8c1a93bed84b83ebb0d60c30663e8d2474c4489a7ba0c4a5efb13da
- evidence_id: runner
  kind: search
  reference: Structured-source runner discovery and explicit reuse provenance
  locator: Original fresh PATH/B5 search 09:27:57.380287–09:27:57.542053Z; earlier
    external bounds 08:17:15; reused09:35:23Z
  accessed_at: '2026-10-21T09:35:23.130236Z'
  support: context_only
  summary: No runner was found within the documented PATH/B5 filenames and pyproject
    search. External search bounds retain their earlier original times. Desiccation
    applicability reused these hashes rather than claiming another execution.
  snapshot_sha256: b872de08b82960bd56870779264757643934b7f6dc2b7635451c0c43cb6c5a99
  search_scope: Retained B5 discovery includes ignored/hidden and virtual-environment
    contents, excluding Git internals. Earlier external roots remain bounded; no exhaustive
    filesystem absence claim.
- evidence_id: bibliography
  kind: database
  reference: Complete source/claim and acquisition ledger
  locator: Seven references, fifteen placements, two snippets, thirteen nodes and
    ten edge claims
  accessed_at: '2026-10-21T09:41:29.212548Z'
  support: partial
  summary: All seven identities resolve and all seven complete publisher-deposited
    article bodies are saved locally. Relevant passages were actually inspected; this
    does not claim a full methods/supplement audit. Both snippets are exact. Sixteen
    successful acquisitions comprise seven metadata responses, seven bodies and two
    version-authority responses, with real URLs, UTC bounds and hashes.
  snapshot_sha256: 011ae39dc5d92adbfb6d40a8798ea8e7e286ac087ef17a3de5aeb3a8b56ca0e3
- evidence_id: source-receipts
  kind: primary_source
  reference: Europe PMC publisher-deposited full-text XML acquisition receipts
  locator: Seven complete article XML files acquired09:37:42.073112–09:37:46.277419Z
  accessed_at: '2026-10-21T09:37:46.277419Z'
  support: supports
  summary: Each successful response has an actual request/finish time, content type,
    size and SHA256. Earlier browser challenge/DOI failures are retained separately;
    source conclusions use the successfully inspected XML, not search-result snippets.
  snapshot_sha256: e70bf0f4a26c5336e05c542ad8d267ef73e66b1d9c0f8625e14ceba3cd5ce7cc
- evidence_id: definition-source
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms10020432
  locator: PMID35208886; PMC8874559; §1/body1, §2/body10,12,14, §4.2/body35–36
  accessed_at: '2026-10-21T09:37:46.277419Z'
  support: supports
  summary: The review supports reversible extreme dehydration, recovery and anhydrobiosis
    while distinguishing drought tolerance. The first quotation is exact. Section4.2
    separately supports repair after rehydration and double-strand damage during desiccation,
    providing existing-source support for the repair branch even though the record
    does not attach this reference at edge2.
  snapshot_sha256: 90d4e7a487b83d3baf1bd9c9bdd9a88a86d0478414cbf861e731136ff24be722
- evidence_id: genes-source
  kind: primary_source
  reference: https://doi.org/10.3390/genes14091803
  locator: PMID37761943; PMC10531146; Intro/body0–3; Discussion/body19–21; Conclusions/body22
  accessed_at: '2026-10-21T09:37:43.175723Z'
  support: partial
  summary: The second snippet exactly quotes introductory D.radiodurans desiccation
    context. The own study is D.irradiatisoli17bor-2 radiation/genome work. In the
    complete main-body extraction desiccation appears only in that introductory background
    and no rehydration passage occurs. The stronger shared-repair/post-rehydration
    interpretation in the notes and edge2 is not directly established by this nearest
    citation; separate definition-review support prevents a false unsupported-biology
    conclusion.
  snapshot_sha256: 2564113369503820a669b56961713e37baa11fe6096dd4cf10c7945c2704f48e
- evidence_id: canonical-source
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/34122375/
  locator: DOI10.3389/fmicb.2021.660050; PMC8193680; Intro/sec1/body0–1; Organism
    provenance/sec3/body6 first sentence
  accessed_at: '2026-10-21T09:37:44.495211Z'
  support: partial
  summary: The article concerns Chroococcidiopsis sp.CCMEE029 and directly supports
    desiccation tolerance, desert strains and lithic growth in the Negev Desert. This
    supports the genus example through an identified strain. The note’s more specific
    endolithic habitat and radiation-tolerance aside are not directly established
    by these main-body passages; the main-body radiation mention concerns D.radiodurans.
    Genus identity and desiccation phenotype remain supported.
  snapshot_sha256: 8275ca5b4d3002f31031d1ec70980727b4e1a1abe718c87d43f5d9b6b0af01b7
- evidence_id: crosskingdom-source
  kind: primary_source
  reference: https://doi.org/10.1021/acs.chemrev.2c00659
  locator: PMID37132487; PMC10375483; §1.2/body8 and §1.3/body13–16
  accessed_at: '2026-10-21T09:37:44.776067Z'
  support: supports
  summary: The review discusses the hydration-monolayer threshold, dehydration-associated
    oxidative damage and explicitly conserved SOD/catalase defense context. It distinguishes
    tolerant from sensitive organisms. These passages support the contextual edges
    without establishing a measured ROS-onset threshold or every taxon’s response;
    the graph does not expressly require those broader claims.
  snapshot_sha256: 8a844d39f98ac5e991794e0ff8d8d70d775a973aabfabee807e6141505b68d79
- evidence_id: protectants-source
  kind: primary_source
  reference: https://doi.org/10.1007/s00203-023-03683-w
  locator: PMID37782422; PMC10545650; Sec6 Plasma membrane/body10 including final
    sentences; Sec8/body23; Sec9/body27
  accessed_at: '2026-10-21T09:37:43.280276Z'
  support: supports
  summary: The yeast review expressly supports trehalose interaction with phospholipid
    polar groups. The end of body10 directly states that heat-shock proteins can bind
    denatured proteins, prevent aggregation and aid rehydration repair. Preserve the
    yeast/review and may/can context; broad contextual nodes do not automatically
    assert all-taxon necessity.
  snapshot_sha256: f4a1416ff4621eceae28cbc5cd5cdcf4bb4dfdf674f09410c9f179491168e137
- evidence_id: vitrification-source
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-023-31586-9
  locator: PMID36941331; PMC10027729; Introduction/Sec1/body2,4
  accessed_at: '2026-10-21T09:37:44.387661Z'
  support: supports
  summary: Natural-desiccation background directly supports trehalose-mediated glass
    formation, reduced molecular motion and prevention of damaging crystals. The paper’s
    own application concerns a human protein, so this is background support rather
    than a microbial growth experiment. That evidence type fits the generic explanatory
    claim; the separate RO role error does not negate it.
  snapshot_sha256: c7d7b370a5f69b0fa8b8048e99ea880f0b00d7c8d6ff55b7ab8dbaee6141f096
- evidence_id: idps-source
  kind: primary_source
  reference: https://doi.org/10.7554/eLife.97231
  locator: PMID39560655; PMC11575898; Abstract; s1/body4–7; s2-1/body9–10; s2-3/body25,36
  accessed_at: '2026-10-21T09:37:43.376934Z'
  support: supports
  summary: Selected full-length representatives from two LEA families and the CAHS
    family, from four eukaryotic organisms, show positive endogenous-cosolute synergy
    in enzyme-protection readouts. Pair/family differences and distinctions from short
    motifs are explicit. This supports the existing contextual synergy claim without
    asserting that every IDP cooperates with every solute or that the study measured
    microbial survival.
  snapshot_sha256: 3e4a813f0f2ddaf22056bfa5e8f410cb6abdc5d3de6ec3850aaf46f41bd53a5d
- evidence_id: elife-version
  kind: database
  reference: Official eLife article API and Crossref DOI registration
  locator: https://api.elifesciences.org/articles/97231 and DOI10.7554/eLife.97231
    registration;09:39:06.556857–09:39:06.833026Z
  accessed_at: '2026-10-21T09:39:06.833026Z'
  support: supports
  summary: The API identifies published version-of-record status with publication
    date2024-11-19; Crossref registers a journal article and relates the bare DOI
    to its reviewed-preprint versions. The API object version is not the preprint
    revision number. The bare DOI is valid and is not an unresolved preprint-only
    citation.
  snapshot_sha256: 82a8ba776afbc28fa0d42eef0495a28a03a78e6cbaa84f0ec61a426c93b78ac5
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, label, polarity, synonym and term kind'
  outcome: supported
  target_ids:
  - traitmech:000010
  summary: The justified local fallback denotes a positive environmental survival
    class, not an organism, assay or molecular object. The RELATED_SYNONYM anhydrobiotic
    is conservative and source-backed. A local METPO proposal exists but is not represented
    as an already active upstream class.
  evidence_ids:
  - identity
  - record
  - definition-source
  - local-authority
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: noncircular survival/recovery definition and attribution'
  outcome: supported
  target_ids:
  - traitmech:000010
  summary: The definition distinguishes extreme drying and subsequent growth recovery.
    The bacterial review supports reversible anhydrobiosis, retaining suspended-or-undetectable
    metabolism as source context. A broad environmental class does not require one
    universal molecular route.
  evidence_ids:
  - definition-source
  - record
- assessment_id: hierarchy
  area: identity
  topic: 'Native checklist: strictly broader parent and environmental category'
  outcome: supported
  target_ids:
  - traitmech:000010
  summary: Phenotype is strictly broader than environmental desiccation tolerance;
    ENVIRONMENT and CLASS are coherent. The maintained v5 proposal retains the same
    definition and parent.
  evidence_ids:
  - identity
  - local-authority
  - record
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: canonical genus and ancillary note scope'
  outcome: concern
  target_ids:
  - traitmech:000010
  summary: Current Chroococcidiopsis genus identity is exact. The cited CCMEE029 strain
    supplies a valid desiccation/desert/lithic example without asserting the phenotype
    for every genus member. Radiation and specifically endolithic wording exceed the
    directly inspected supporting statements and need bounded precision.
  evidence_ids:
  - go-taxonomy
  - canonical-source
  - bibliography
- assessment_id: model
  area: representation
  topic: 'Native checklist: graph scope, all thirteen node kinds and optional fields'
  outcome: supported
  target_ids:
  - traitmech:000010
  summary: The contextual NONMECHANISTIC classification and reviewed-label-only IDP
    aggregate are coherent. Activity nodes remain activities, oxidative stress denotes
    accumulation/damage, and vitrification denotes formation. No token protein, extra
    pathway link, optional domain/range, priority/subset, discussion or dataset is
    required solely to fill an optional field.
  evidence_ids:
  - record
  - node-edges
  - local-authority
  - idps-source
- assessment_id: grounding
  area: grounding
  topic: 'Native checklist: all node identities, proposal status and label-only aggregate'
  outcome: supported
  target_ids:
  - traitmech:000010
  summary: The four GO node identifiers are active and exact in meaning/aspect. The
    trait fallback and local confers proposal retain their status. Source context
    supports the label-only aggregate; no single-protein instance or irrelevant live
    UniProt audit is introduced.
  evidence_ids:
  - go-taxonomy
  - identity
  - ledger
  - idps-source
  - owners
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all ten edge roles and directions'
  outcome: concern
  target_ids:
  - traitmech:000010
  summary: Edge5 assigns process-only RO:0002213 to a chemical subject. Other current
    role assignments are compatible, including molecular-function activities on edges6–8.
    Biolink permits the existing broad endpoint kinds, local confers accepts state/process
    to trait, and unassigned stabilizes/synergizes predicates are not automatically
    invalid.
  evidence_ids:
  - ro
  - biolink
  - ledger
  - node-edges
  - owners
  - local-authority
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: seven references and fifteen nearest placements'
  outcome: concern
  target_ids:
  - traitmech:000010
  summary: All references resolve and all bodies are accessible. The repair branch
    has positive support in the definition review, while the attached Genes citation
    primarily supplies an exact organism background quote and a different-species
    radiation study; align the stronger notes with their actual source. The other
    edge claims have positive contextual support with the recorded yeast, cross-kingdom
    and protein/cosolute limits.
  evidence_ids:
  - bibliography
  - definition-source
  - genes-source
  - crosskingdom-source
  - protectants-source
  - vitrification-source
  - idps-source
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: both snippets against actual article text'
  outcome: supported
  target_ids:
  - traitmech:000010
  summary: Both quotations are exact after XML element-boundary/whitespace normalization.
    The Genes quotation genuinely names D.radiodurans, so its different own-study
    species is not a quote or citation-identity error. The initial abstract misses
    are superseded by actual full-text verification.
  evidence_ids:
  - check-desiccation-snippets
  - definition-source
  - genes-source
  - bibliography
- assessment_id: versioning
  area: evidence
  topic: 'Native checklist: bare eLife DOI publication status'
  outcome: supported
  target_ids:
  - traitmech:000010
  summary: Official publisher and registration records confirm a published version
    of record. Preprint-version relationships do not invalidate the cited bare DOI.
  evidence_ids:
  - elife-version
  - idps-source
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole-record and contextual mechanism coverage'
  outcome: supported
  target_ids:
  - traitmech:000010
  summary: All thirteen nodes and ten edges have an assessment. The sources support
    reasonable contextual causal explanations without requiring new experiments, exhaustive
    mechanisms or all-taxon necessity. Formal ontology and nearest-placement defects
    remain distinct from supported biology.
  evidence_ids:
  - ledger
  - node-edges
  - bibliography
  - record
- assessment_id: datasets
  area: evidence
  topic: 'Native checklist: optional structured sources and canonical applicability'
  outcome: supported
  target_ids:
  - traitmech:000010
  summary: The inspected catalog has no canonical Chroococcidiopsis dataset. Reused
    bounded runner discovery retains original times; no replacement organism query
    or negative biological inference follows.
  evidence_ids:
  - expression
  - runner
- assessment_id: audit
  area: provenance
  topic: 'Native checklist: history, human acceptance, maintained owners and native
    checks'
  outcome: concern
  target_ids:
  - traitmech:000010
  summary: All nine history events disclose AI assistance, including the REVIEWED
    promotion. No explicit local human-acceptance link was found within the retained
    ignored-inclusive scope. Wildcard promotes can restore the formal error after
    an ID-only correction. Native checks pass within their stated execution/reuse
    limits.
  evidence_ids:
  - provenance
  - provenance-independent
  - local-authority
  - owners
  - capture
  - reuse
  - reuse-independent
  - check-batch004-qc
findings:
- finding_id: chemical-subject-process-regulation
  issue_key: desiccation-tolerant-chemical-subject-process-regulation
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Process regulation is assigned to a chemical subject
  description: Edge5 links trehalose CHEMICAL to vitrification BIOLOGICAL_PROCESS
    using RO:0002213 positively regulates. The relation inherits the explicit process
    domain/range of RO:0002211 and concerns process execution; the chemical subject
    does not satisfy that represented role. The literature positively supports trehalose-related
    glass formation, so this is a grounding mismatch rather than false biology. Wildcard
    promotes row63 can restore the mismatch if only the identifier is cleared. This
    is not an asserted reasoner result or native-validation failure.
  target_ids:
  - traitmech:000010
  field_paths:
  - causal_graphs[0].edges[5].predicate_id
  - causal_graphs[0].nodes[5]
  evidence_ids:
  - ro
  - node-edges
  - owners
  - vitrification-source
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/desiccation_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard promotes row63 owner
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing-ID skip and endpoint type-policy owner
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: repair-evidence-placement
  issue_key: desiccation-tolerant-repair-evidence-placement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The repair interpretation needs its nearest supporting citation
  description: The Genes14091803 quotation exactly supports introductory D.radiodurans
    desiccation context, but its own study concerns D.irradiatisoli17bor-2 radiation/genome
    work. The current top-level note and edge2 use it for shared DNA-repair and post-rehydration
    restoration claims that are not directly established in the inspected body. The
    separately cited anhydrobiosis review §4.2 positively supports post-rehydration
    repair and desiccation-induced DNA damage. Align the stronger interpretation and
    nearest citation with that evidence, preserving the valid quotation and repair
    branch instead of calling the biology unsupported.
  target_ids:
  - traitmech:000010
  field_paths:
  - evidence[1].notes
  - causal_graphs[0].edges[2].description
  - causal_graphs[0].edges[2].evidence[0]
  evidence_ids:
  - genes-source
  - definition-source
  - bibliography
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/desiccation_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: canonical-ancillary-scope
  issue_key: desiccation-tolerant-canonical-ancillary-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The canonical note adds ancillary details beyond its cited support
  description: PMID34122375 supports Chroococcidiopsis desiccation tolerance through
    CCMEE029 and describes desert strains and lithic provenance. The note also asserts
    radiation tolerance and specifically endolithic habitat, which are not directly
    established by the inspected main-body statements about this organism. Retain
    the supported genus example and strain-limited context, and narrow or directly
    source these ancillary details. This does not assert that those details are false
    or that every member of the genus has been tested.
  target_ids:
  - traitmech:000010
  field_paths:
  - canonical_examples[0].note
  evidence_ids:
  - canonical-source
  - go-taxonomy
  - bibliography
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/desiccation_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: desiccation-tolerant-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked locally
  description: All nine events disclose AI assistance and one explicitly promotes
    the record to REVIEWED. Ignored-inclusive local target searches and matching review
    target-list inspection found no explicit human-acceptance link for this revision.
    The native status gate requires that acceptance; the bounded documentary gap does
    not establish that no human reviewed the record privately or remotely.
  target_ids:
  - traitmech:000010
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - provenance-independent
  - local-authority
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/desiccation_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-relation
  description: In separately authorized curation, reconcile edge5 with its chemical/process
    endpoints and the maintained wildcard mapping.
  finding_ids:
  - chemical-subject-process-regulation
  target_ids:
  - traitmech:000010
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/desiccation_tolerant.yaml
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
  - Retained relation grounding agrees with both endpoint identities and the authority
    definition; do not relabel the chemical as a process solely to preserve the current
    relation.
  - Address whether unchanged promotes wording can reacquire the rejected grounding
    after an ID is cleared; do not guess a replacement identifier.
  - Preserve the supported generic vitrification explanation and compatible activity/process
    edges6–8.
  - After authorized edits use guarded writes, append-only history, focused strict/term/graph
    and mapping checks, just qc and maintained derived-product regeneration.
- action_id: align-repair-attribution
  description: Align repair notes and nearest evidence with the actual supporting
    passages already available.
  finding_ids:
  - repair-evidence-placement
  target_ids:
  - traitmech:000010
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/desiccation_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve the exact Genes introductory quotation and distinguish D.radiodurans
    background from the D.irradiatisoli own-study context.
  - Place support for repair after rehydration beside the claim, with the definition
    review §4.2 as available positive evidence; retain only source-supported shared-repair
    wording.
  - No new mechanism, molecular target, protocol or experiment is proposed; validate
    the bibliography and nearest placement through the native guarded curation workflow.
- action_id: bound-canonical-note
  description: Retain the valid genus example while narrowing or directly supporting
    its ancillary note details.
  finding_ids:
  - canonical-ancillary-scope
  target_ids:
  - traitmech:000010
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/desiccation_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Keep Chroococcidiopsis genus identity and the cited CCMEE029 desiccation/desert/lithic
    context.
  - Separate directly supported habitat wording from the specifically endolithic and
    radiation asides; any retained ancillary statement has an actual inspected supporting
    citation.
  - Do not convert strain evidence into a claim about every genus member or misclassify
    the genus identifier as erroneous.
- action_id: link-acceptance
  description: Locate and link existing human scientific acceptance or obtain it through
    the established process, preserving history and reassessing status if needed.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - traitmech:000010
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/desiccation_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies the reviewed revision and scientific scope.
  - AI disclosure, validator success and this review do not substitute for human acceptance;
    retain append-only provenance.
limitations:
- All seven article bodies were acquired, but inspection focused on relevant definition,
  introduction, results and discussion passages. No exhaustive method, supplement
  or cited-reference audit is claimed.
- The Genes quotation is exact and its D.radiodurans background context is valid.
  The nearest repair interpretation needs citation precision; the separately cited
  definition review positively supports repair after rehydration, so no false-mechanism
  finding is asserted.
- The canonical genus is valid through a specified strain. Radiation and specifically
  endolithic details remain unsupported by the inspected nearest-source statements,
  not demonstrated false; no genus-wide phenotype inference is made.
- Cross-kingdom and yeast reviews provide contextual support. The monolayer discussion
  is not a measured ROS-onset threshold, and may/can wording is retained without inventing
  an all-taxon necessity claim or new endpoint requirement.
- The vitrification article supports natural-desiccation background while studying
  a human protein application. The eLife study supports selected full-length eukaryotic
  IDP/cosolute pairs with enzyme-protection readouts and pair-specific differences;
  neither is recast as a microbial survival experiment.
- The local METPO fallback and confers proposal are assessed against the pinned snapshot
  and maintained proposals. No claim is made about unseen newer ontology releases.
  The external relation mismatch is an intended-role assessment, not a reasoner result.
- Common checks and B4 QC retain original execution times, failures, skips and warnings
  and are reused on documented unchanged inputs. No fresh full-corpus execution or
  latest-release certification is implied.
- No protein instance is asserted. Live UniProt instance validation is inapplicable;
  dataset noncoverage and bounded reused runner discovery do not imply missing biological
  function.
- Human acceptance outside the declared ignored-inclusive local search remains unknown.
  This review is not human scientific sign-off.
- No record, mapping, history or generated product was edited. No paid provider call,
  protocol design, organism optimization or new biological mechanism was performed.
notes:
- All node, edge and extracted body-paragraph indices are zero-based.
- Native capture retained55 inputs at09:33:09–11Z, and independent grounding inspection
  confirmed every captured hash. Nine history events all disclose AI assistance.
- One major and three minor findings. Source access and publication-version receipts
  retain their actual acquisition times and hashes; abstract misses are superseded
  only where exact full text was inspected.
tags:
- record-review
- desiccation-tolerant
- environment
- needs-curation
```
