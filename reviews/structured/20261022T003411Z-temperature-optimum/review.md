# Whole-record review of temperature optimum

- Review: 20261022T003411Z-temperature-optimum
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T00:28:32.226478Z
- Finished UTC: 2026-10-22T00:34:11Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review finds one grouped imported-role major and bounded composition-facet, quoted-note and human-acceptance minors; reported optimum 30 °C and seven literal schema snippets are positive. Operational-definition, optimum-setting and Arrhenius interpretations remain unknown.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Eighth record of the actual local batch 013 queue. Whole 271-line target and 97 captured inputs verified before judgment; local review does not assert remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000304 | data/traits/environment/temperature_optimum.yaml | maintained | temperature optimum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000304 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000304 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000304 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000304 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000304 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000304 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000304 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000304 | Native record validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000304 | The actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000304 | All seven schema snippets over two references were VERIFIED. The native checker does not test quoted notes. Two separately quoted note spans were reviewed manually: one bounded nonverbatim note and one unresolved note. |
| Qualified batch-twelve QC | passed | True | METPO:1000304 | Actual prior QC qualified against B13 bytes; this is not a new B13 QC execution or publication. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000304 | Zero protein classes or instances in this quantitative NONMECHANISTIC optimum overview; no token protein requirement. |

## Scientific And Domain Assessments

### Native checklist: active identity and hierarchy

identity: supported. Targets: METPO:1000304.

Active METPO:1000304 and both direct parents 1000533/1000536 match the optimum measurement concept. Local v3 fluidity, v85 homeoviscous adaptation and v2 manifests-as retain separate proposal status.

### Native checklist: operational-definition support

quantity: unknown. Targets: METPO:1000304.

Ordinary temperature-at-maximal-growth meaning is coherent. Inspected generic thermophile and membrane sources do not establish the stronger best-maintained membrane/enzyme operational equivalence or unique joint optimum-setting claim. Body access limits do not refute those claims.

### Native checklist: reported optimum point

quantity: supported. Targets: METPO:1000304.

Oceanimonas pelagia NTOU-MSR1T has a reported optimum of 30 °C, separate from growth at 10–45 °C. The parent placement retains the local boundary policy without attributing TraitMech bins to the paper. Official taxonomy verifies identity separately.

### Native checklist: five works and twelve placements

evidence: unknown. Targets: METPO:1000304.

Source identities and generic membrane physics are positive; exact optimum-setting and Arrhenius diagnostic interpretations remain unknown. The positive Crossref identity and two HTTP403 body failures are separate. Detailed host/pathogen stress, fitness and intervention efficacy remain UNASSESSED_SCOPE.

### Native checklist: snippets and quoted notes

evidence: concern. Targets: METPO:1000304.

All seven schema snippets are literal and native-verified. The edge 5 Ramón quoted note is nonverbatim on the inspected whole HTML surface while its concept is positive. The edge 7 Arrhenius quotation remains unknown because adequate body text was unavailable.

### Native checklist: all nine current referents

representation: concern. Targets: METPO:1000304.

Node 3 composition versus CELLULAR_LOCALIZATION requires bounded facet clarification without a forced exact retype. Fluidity and maximal growth rate remain qualities; homeoviscous adaptation is a process. Enzyme-kinetics and Arrhenius-factor nuances remain qualifications.

{
  "grounding": [
    {
      "index": 0,
      "node_id": "temperature_optimum_trait",
      "label": "temperature optimum",
      "node_type": "TRAIT",
      "grounding": "METPO:1000304",
      "outcome": "supported",
      "assessment": "Active temperature-optimum trait identity and both direct parents fit."
    },
    {
      "index": 1,
      "node_id": "ambient_temperature",
      "label": "ambient temperature",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Actual imposed ambient temperature is a condition/value, not an explicitly described change event; environmental enum is appropriate and not the basis of relation failure alone."
    },
    {
      "index": 2,
      "node_id": "membrane_fluidity",
      "label": "membrane fluidity",
      "node_type": "QUALITY",
      "grounding": "METPO:1007505",
      "outcome": "supported",
      "assessment": "Explicit membrane physical attribute is QUALITY with exact local v3 identity."
    },
    {
      "index": 3,
      "node_id": "homoviscous_lipid_composition",
      "label": "homoviscous lipid composition",
      "node_type": "CELLULAR_LOCALIZATION",
      "grounding": null,
      "outcome": "concern",
      "assessment": "Lipid composition tuned to fluidity denotes composition rather than a location. CELLULAR_LOCALIZATION may intend membrane material/component shorthand, but that is not explicit. Bounded facet precision minor; no forced replacement type or chemical identity invented."
    },
    {
      "index": 4,
      "node_id": "enzyme_kinetics",
      "label": "enzyme kinetics",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "unknown",
      "assessment": "Enzyme turnover can be processual; temperature dependence of its rate can be a quality. Current kinetics wording remains qualified; role major does not require forcing this ambiguity."
    },
    {
      "index": 5,
      "node_id": "maximal_growth_rate",
      "label": "maximal growth rate",
      "node_type": "QUALITY",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Peak specific growth rate is a measurable QUALITY, not the ambient temperature that attains it."
    },
    {
      "index": 6,
      "node_id": "homeoviscous_adaptation",
      "label": "homeoviscous adaptation",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": "METPO:1016200",
      "outcome": "supported",
      "assessment": "Explicit lipid-remodeling process agrees with captured v85 homeoviscous-adaptation definition, distinct from fluidity quality."
    },
    {
      "index": 7,
      "node_id": "arrhenius_plot_deviation",
      "label": "Arrhenius plot deviation from linearity",
      "node_type": "EXPERIMENTAL_FACTOR",
      "grounding": null,
      "outcome": "unknown",
      "assessment": "Deviation in an Arrhenius plot is an observational measurement feature used for interpretation; EXPERIMENTAL_FACTOR is broad and no forced additional facet finding is made."
    },
    {
      "index": 8,
      "node_id": "stress_growth_regime",
      "label": "stress / non-physiological growth regime",
      "node_type": "STATE",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Non-physiological growth condition is a state/regime; detailed biological support belongs to source audit."
    }
  ],
  "source": [
    {
      "index": 0,
      "node_id": "temperature_optimum_trait",
      "label": "temperature optimum",
      "node_type": "TRAIT",
      "outcome": "SUPPORTED_MEASUREMENT_CONCEPT",
      "assessment": "Maximum growth-rate temperature is the current measurement concept; canonical abstract provides a reported optimum. General definition-source sufficiency remains unknown."
    },
    {
      "index": 1,
      "node_id": "ambient_temperature",
      "label": "ambient temperature",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Ambient growth temperature is the measured environmental variable; no claim of a particular universal value."
    },
    {
      "index": 2,
      "node_id": "membrane_fluidity",
      "label": "membrane fluidity",
      "node_type": "QUALITY",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Mendoza and Ramón support membrane fluidity as a physical property. Detailed bioenergetic efficacy is not assessed."
    },
    {
      "index": 3,
      "node_id": "homoviscous_lipid_composition",
      "label": "homoviscous lipid composition",
      "node_type": "CELLULAR_LOCALIZATION",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Lipid composition is relevant to physical state in the selected abstracts; the declared CELLULAR_LOCALIZATION facet is a grounding concern, not source identity."
    },
    {
      "index": 4,
      "node_id": "enzyme_kinetics",
      "label": "enzyme kinetics",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "UNKNOWN_EXACT_SCOPE",
      "assessment": "Thermophile enzyme adaptation is generic context; whole-network turnover and its precise optimum effects are not established by the selected Tolner text."
    },
    {
      "index": 5,
      "node_id": "maximal_growth_rate",
      "label": "maximal growth rate",
      "node_type": "QUALITY",
      "outcome": "SUPPORTED_MEASUREMENT_CONCEPT",
      "assessment": "Peak growth rate is distinguishable from the temperature at which the peak is measured. No direct assay/formula is reconstructed."
    },
    {
      "index": 6,
      "node_id": "homeoviscous_adaptation",
      "label": "homeoviscous adaptation",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Selected abstracts and Ramón paragraph support generic homeoviscous remodeling. No novel pathway or intervention is inferred."
    },
    {
      "index": 7,
      "node_id": "arrhenius_plot_deviation",
      "label": "Arrhenius plot deviation from linearity",
      "node_type": "EXPERIMENTAL_FACTOR",
      "outcome": "UNKNOWN_BODY_UNAVAILABLE",
      "assessment": "Arrhenius deviation representation refers to a cited review whose body could not be acquired; exact diagnostic interpretation is unverified."
    },
    {
      "index": 8,
      "node_id": "stress_growth_regime",
      "label": "stress / non-physiological growth regime",
      "node_type": "STATE",
      "outcome": "UNKNOWN_BODY_UNAVAILABLE",
      "assessment": "Stress/non-physiological regime as inferred from nonlinearity remains unknown from the accessible citation abstract."
    }
  ]
}

### Native checklist: all eight current relations

consistency: concern. Targets: METPO:1000304.

Edges 0/1/2/3/5/6 form one inherited-process-role major based on actual condition, composition and quality referents. Edge 4 distinguishes the dependent peak rate from the temperature attaining it, but broad manifests-as roles do not establish a hard violation. Lexical indicates receives no invented imported constraints.

{
  "grounding": [
    {
      "index": 0,
      "subject": "ambient_temperature",
      "predicate": "regulates",
      "predicate_id": "RO:0002211",
      "object": "membrane_fluidity",
      "outcome": "concern",
      "assessment": "RO2211 requires process domain and range. Ambient temperature is an imposed condition/value, and fluidity is an explicit quality; no event description supplies a process reading."
    },
    {
      "index": 1,
      "subject": "homoviscous_lipid_composition",
      "predicate": "regulates",
      "predicate_id": "RO:0002211",
      "object": "membrane_fluidity",
      "outcome": "concern",
      "assessment": "RO2211 process endpoints conflict with composition/material-or-quality subject and explicit fluidity QUALITY object; node3 type clarification alone would not fix this relation."
    },
    {
      "index": 2,
      "subject": "ambient_temperature",
      "predicate": "regulates",
      "predicate_id": "RO:0002211",
      "object": "enzyme_kinetics",
      "outcome": "concern",
      "assessment": "RO2211 process domain conflicts with ambient temperature condition/value. Enzyme-turnover process interpretation of object remains possible; subject mismatch independently decisive."
    },
    {
      "index": 3,
      "subject": "enzyme_kinetics",
      "predicate": "promotes",
      "predicate_id": "RO:0002213",
      "object": "maximal_growth_rate",
      "outcome": "concern",
      "assessment": "RO2213 inherits process range from RO2211; peak specific growth rate is an explicit quality. Enzyme-kinetics process/attribute nuance does not remove this object conflict."
    },
    {
      "index": 4,
      "subject": "maximal_growth_rate",
      "predicate": "manifests as",
      "predicate_id": "METPO:2007400",
      "object": "temperature_optimum_trait",
      "outcome": "unknown",
      "assessment": "Local manifests-as broad formal endpoints do not force a domain failure. Subject is peak growth-rate value, while description refers to the temperature attaining that peak. Retain dependent-rate versus independent-condition distinction as a qualification; criterion shorthand may be intended, no replacement predicate/retype dictated."
    },
    {
      "index": 5,
      "subject": "homeoviscous_adaptation",
      "predicate": "regulates",
      "predicate_id": "RO:0002211",
      "object": "membrane_fluidity",
      "outcome": "concern",
      "assessment": "Homeoviscous-adaptation process fits RO2211 domain; fluidity QUALITY object conflicts with process range."
    },
    {
      "index": 6,
      "subject": "membrane_fluidity",
      "predicate": "promotes",
      "predicate_id": "RO:0002213",
      "object": "maximal_growth_rate",
      "outcome": "concern",
      "assessment": "RO2213 inherited process/process roles conflict with explicit fluidity and maximal-growth-rate qualities."
    },
    {
      "index": 7,
      "subject": "arrhenius_plot_deviation",
      "predicate": "indicates",
      "predicate_id": null,
      "object": "stress_growth_regime",
      "outcome": "unknown",
      "assessment": "Lexical indicates has no predicate_id; no imported domain/range invented. Observational inference from deviation to regime remains source-dependent, not a biological causal claim established by ontology."
    }
  ],
  "source": [
    {
      "index": 0,
      "subject": "ambient_temperature",
      "predicate": "regulates",
      "object": "membrane_fluidity",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Mendoza abstract explicitly links lower growth temperature with membrane remodeling/fluidity. The wording that ambient temperature sets a target remains interpretive; no measured optimum follows.",
      "source_locator": "mendoza-metadata.json; abstract first two sentences"
    },
    {
      "index": 1,
      "subject": "homoviscous_lipid_composition",
      "predicate": "regulates",
      "object": "membrane_fluidity",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Lipid composition and fluidity adaptation are supported as generic context. A particular optimal growth temperature is not demonstrated by this abstract.",
      "source_locator": "mendoza-metadata.json; abstract first two sentences"
    },
    {
      "index": 2,
      "subject": "ambient_temperature",
      "predicate": "regulates",
      "object": "enzyme_kinetics",
      "outcome": "UNKNOWN_EXACT_SCOPE",
      "assessment": "Tolner supplies thermophile enzyme-function context, not a direct whole-cell-network temperature-scaling or optimum determination in the inspected abstract. Detailed transport/host interventions are unassessed.",
      "source_locator": "tolner-metadata.json; abstract opening adaptation sentence and supplied short phrase only"
    },
    {
      "index": 3,
      "subject": "enzyme_kinetics",
      "predicate": "promotes",
      "object": "maximal_growth_rate",
      "outcome": "UNKNOWN_EXACT_SCOPE",
      "assessment": "Adaptation and enzyme turnover context do not independently establish the asserted peak-growth causal link in inspected text. Unavailable body is not a refutation.",
      "source_locator": "tolner-metadata.json; selected abstract context"
    },
    {
      "index": 4,
      "subject": "maximal_growth_rate",
      "predicate": "manifests as",
      "object": "temperature_optimum_trait",
      "outcome": "UNKNOWN_NEAREST_SOURCE",
      "assessment": "The Tolner short supplied phrase is literal, but exact rate-to-temperature-at-peak measurement semantics are not directly established by this abstract. Formal endpoint semantics belong to grounding.",
      "source_locator": "tolner-metadata.json; supplied short phrase"
    },
    {
      "index": 5,
      "subject": "homeoviscous_adaptation",
      "predicate": "regulates",
      "object": "membrane_fluidity",
      "outcome": "SUPPORTED_GENERIC_CONTEXT_WITH_QUOTATION_CONCERN",
      "assessment": "Ramón generic membrane-phase paragraph supports composition changes maintaining physical state at low temperature. The note puts a paraphrase in quotation marks; the supplied complete span is absent from the inspected HTML. No biological falsity is inferred.",
      "source_locator": "cold-pmc.html; zero-based HTML &lt;p&gt; ordinal 17, selected first seven sentences; quoted-note-literal-check.json"
    },
    {
      "index": 6,
      "subject": "membrane_fluidity",
      "predicate": "promotes",
      "object": "maximal_growth_rate",
      "outcome": "UNKNOWN_EXACT_SCOPE",
      "assessment": "Ramón generic membrane functionality context is positive, but the specific peak-growth proximal determinant and full transport/signaling/division formulation are not directly established by the selected paragraph.",
      "source_locator": "cold-pmc.html; selected generic paragraph 17"
    },
    {
      "index": 7,
      "subject": "arrhenius_plot_deviation",
      "predicate": "indicates",
      "object": "stress_growth_regime",
      "outcome": "UNKNOWN_BODY_UNAVAILABLE",
      "assessment": "Crossref confirms the psychrophile review. Its abstract does not contain the quoted Arrhenius sentence; two official PDF routes returned 403, so exact quotation and linearity-to-stress interpretation remain unknown, not false.",
      "source_locator": "arrhenius-crossref.json; abstract and official link; actual PDF access receipts"
    }
  ]
}

### Native checklist: quantitative overview and biological limits

scope: unknown. Targets: METPO:1000304.

Two components and zero protein classes/instances are compatible with the quantitative NONMECHANISTIC overview. No forced connector or token protein is required. Formal representation and literal checks do not establish detailed pathogen stress/survival/fitness/ROS/AMR/intervention efficacy, which remains UNASSESSED_SCOPE.

### Native checklist: bounded catalog applicability

evidence: unknown. Targets: METPO:1000304.

Canonical species/type-strain aliases have no exact match in the retained 20-organism / 28-dataset catalog. Broad source context and incidental E. coli/Bacillus host mentions do not justify exact-strain or detailed module transfer; source-species coverage is not globally absent.

### Native checklist: current writers and historical conditions

consistency: supported. Targets: METPO:1000304.

Process-quality migration preserves the correct maximal-rate QUALITY, but its old enables-object branch would recreate promotes/RO2213; current promotes edges skip that branch. Shared grounders skip populated IDs. The homeoviscous normalizer targets siblings only. Composition facet and quoted-note corrections have record-only ownership.

### Native checklist: attributable current acceptance

provenance: concern. Targets: METPO:1000304.

Fifteen AI events plus a seed and the ignored-inclusive 282-path / 73-array search do not establish current human acceptance. Sixteen captured projections include ten current whole bodies and six byte-qualified prior readings; seven uncaptured histories remain matching-line context. Private/remote acceptance remains unknown.

### Native checklist: checks and evidence chronology

consistency: supported. Targets: METPO:1000304.

All 97 captured inputs and frozen audits match. Three focused native checks passed. B13 qualified common diagnostics retain historical optional failures and 123 no-adapter skips; no B14 fresh diagnostics or new B13 QC/publication claim is introduced. Acquisitions, copies and readings remain distinct.

## Findings

### imported-process-roles: Imported relation roles conflict with current referents

major / open / confirmed; issue key: temperature-optimum-imported-process-roles.

Six edges conflict with imported process roles. RO:0002211 requires process subjects and objects, and RO:0002213 inherits both constraints. Edges 0/1/2 use an ambient-temperature condition or composition as subject; edges 0/1/5 have an explicit fluidity-quality object; edges 3/6 have a maximal-growth-rate quality object and edge 6 also has a quality subject. The turnover-process reading of enzyme kinetics cannot repair the independently decisive other endpoints. This formal representation evidence is separate from biological causal efficacy.

### composition-localization-facet: Composition and localization facets need clarification

minor / open / confirmed; issue key: temperature-optimum-composition-localization-facet.

The label and description name lipid composition, while CELLULAR_LOCALIZATION denotes a component or location. A lipid mixture/component shorthand may be intended but is not explicit. Clarify that referent; the evidence does not justify prescribing one replacement type or chemical identity. This bounded facet issue is independent of the relation-role conflict.

### nonverbatim-source-note: Quoted note differs from inspected primary wording

minor / open / confirmed; issue key: temperature-optimum-nonverbatim-source-note.

The Ramon note encloses a paraphrase in quotation marks. The complete supplied span is absent from the retained primary HTML under exact and casefolded whitespace-normalized searches. The selected nearby generic membrane paragraph supports the concept with different wording. This is quotation precision, not biological refutation; all seven schema snippet fields remain literal positive controls.

### human-acceptance-link: Reviewed status lacks locally attributable acceptance

minor / open / confirmed; issue key: temperature-optimum-human-acceptance-link.

Current REVIEWED status lacks attributable human acceptance of the present assertions in the inspected local evidence. The ignored- and hidden-inclusive search, excluding .git and .venv, found 282 matching paths and 73 actual review target arrays with no exact target. Sixteen embedded events comprise fifteen AI events and one seed; the one exact-target repository history has an AI actor. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### resolve-imported-process-roles

In separately authorized curation, reconcile affected predicates with their actual condition, composition, process or quality referents. Preserve growth-rate QUALITY. Update the process-quality writer rationale and old-enables transform so historical inputs cannot recreate RO:0002213 on a quality object. Current promotes edges skip that transform; shared grounding skips populated IDs, so a rerun alone is not a current fix.

- Demonstrate compatible actual endpoint roles without inventing mechanisms or numerical optima.
- Retain unknown source calibration, the rate-versus-temperature distinction and NONMECHANISTIC scope; no required protein instances or component connectors.
- Run focused strict validation, relevant graph/predicate audits, full QC and required curation history/product gates.

### resolve-composition-localization-facet

Clarify whether the node denotes composition as an attribute or a specific material component, then reconcile its label, description and type. Do not guess a replacement grounding.

- The stated referent fits the schema type and nearest source scope.
- Do not retype merely to make an incompatible predicate appear valid; run native strict and graph checks after authorized curation.

### resolve-nonverbatim-source-note

Mark the note as paraphrase or replace it with a short exact primary-source quotation with a precise locator. Preserve the generic evidence scope.

- Quoted text is exact and interpretation is separate.
- Retain the seven verified snippet results and keep the inaccessible Arrhenius quotation UNKNOWN unless adequate primary text is inspected.
- Run focused snippet checking and native curation history/QC gates; document that native snippet verification does not check quoted note fields.

### resolve-human-acceptance-link

Link attributable human acceptance of current assertions or reconcile REVIEWED through the native status workflow in separately authorized curation. Preserve existing actors.

- Human reviewer and accepted scope are attributable, or status accurately reflects available evidence.
- Per-record and repository history validates and AI assistance remains explicit.

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
| check-temperature-optimum-validate | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-validate.log; Executed 2026-10-22T00:28:48.767134+00:00 through 2026-10-22T00:28:49.307749+00:00; metadata temperature-optimum-validate.json | context_only | Native record validation passed; scientific interpretation is assessed separately. |
| check-temperature-optimum-strict | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-strict.log; Executed 2026-10-22T00:28:48.767149+00:00 through 2026-10-22T00:28:49.739728+00:00; metadata temperature-optimum-strict.json | context_only | The actual validate-strict command passed. |
| check-temperature-optimum-snippets-network | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-snippets-network.log; Executed 2026-10-22T00:29:12.030851+00:00 through 2026-10-22T00:29:15.555699+00:00; metadata temperature-optimum-snippets-network.json | context_only | All seven schema snippets over two references were VERIFIED. The native checker does not test quoted notes. Two separately quoted note spans were reviewed manually: one bounded nonverbatim note and one unresolved note. |
| check-batch012-qc | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log; Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00; metadata batch012-qc.json | context_only | Actual prior QC qualified against B13 bytes; this is not a new B13 QC execution or publication. |
| record | data/traits/environment/temperature_optimum.yaml; Whole 271-line current record | supports | Nine nodes, eight edges and sixteen embedded events; one canonical example, zero protein classes and zero instances. |
| reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json; Actual B12-to-B13 qualification | supports | Current byte comparisons retain original diagnostic failures, retries and skips. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json; Independent actual-output verification | supports | Qualification verification, not new QC. |
| local-init | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Actual local initialization; publication remains a separate action. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Actual referents and optional protein applicability. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source scope and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current facets and NONMECHANISTIC scope. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Shared mapping for future empty fields; populated IDs are skipped. |
| local-v2 | proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv; Captured maintained authority | supports | Manifests-as has broad formal endpoints and state-to-trait prose. |
| local-v3 | proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv; Captured maintained authority | supports | Exact membrane-fluidity quality. |
| local-v85 | proposals/metpo_traitmech_v85/metpo_proposal_classes_robot.tsv; Captured maintained authority | supports | Exact homeoviscous-adaptation process, distinct from fluidity quality. |
| capture | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/capture-verification.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | All 97 captured inputs and whole target verified. |
| identity | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/identity-assessment.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Active exact optimum and both direct parents; local proposal identities separate. |
| nodes-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/node-edge-grounding-ledger.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | All nine nodes and eight edges, including positives and measurement qualifications. |
| owners | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/owner-provenance-assessment.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Current owners, conditional migration and sibling-only context. |
| owner-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/owner-primary-reading.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Whole process-quality migration and normalizer, selected canonical and shared grounding guards. |
| writer-shape | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/writer-current-shape-check.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Current promotes edges skip the old enables conversion; correct rate QUALITY is retained. |
| human-search | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/search-and-provenance.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | 282 ignored-inclusive paths; 73 actual target arrays, zero exact current target. |
| histories | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/history-reading-provenance.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Sixteen current projections: ten current whole bodies and six byte-qualified prior readings. |
| discovery | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/discovery-disposition.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Seven uncaptured histories and two scripts remain matching-line-only context. |
| expression | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/expression-and-readiness.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | No exact canonical catalog match; source species coverage not globally absent. |
| local-authority | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/local-authority-reading.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Actual local proposal/mapping rows; lexical indicates has no invented imported constraints. |
| ground-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/evidence-manifest.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Twenty-nine frozen grounding artifacts verified. |
| metpo-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl; Retained primary authority, locally read at the recorded time | supports | Active 1000304 with both direct parents 1000533/1000536. |
| metpo-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/metpo-authority.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Selected primary statements and exact-byte provenance. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Retained primary authority, locally read at the recorded time | supports | Actual inherited process domain/range for regulates and positively-regulates. |
| ro-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/selected-ro-primary-reading.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Selected primary statements and exact-byte provenance. |
| tolner | DOI:10.1016/s0300-9629(97)00003-0; Indexed abstract | supports | Generic adaptation and literal snippets; operational-definition and precise optimum inference unknown. |
| tolner-author | DOI:10.1016/s0300-9629(97)00003-0; Institutional abstract page | supports | Abstract context only; not a full primary body. |
| mendoza | DOI:10.1146/annurev-micro-091313-103612; Indexed abstract | supports | Generic membrane context and current literal snippets; exact optimum-setting inference unknown. |
| mendoza-browser | DOI:10.1146/annurev-micro-091313-103612; Actual publisher abstract tool export; origin/cache-fetch time unknown | supports | Generic membrane physics, not a full article or raw HTML. |
| cold-metadata | DOI:10.1007/s42770-023-01057-4; Indexed metadata and abstract | supports | Identity and broad review context only. |
| cold-body | DOI:10.1007/s42770-023-01057-4; Zero-based HTML paragraph 17, selected first seven generic sentences; whole surface literal search only | supports | Generic composition/physical-state context is positive; the quoted edge 5 note differs from inspected wording. |
| canonical-primary | DOI:10.1007/s10482-024-01948-y; Indexed abstract temperature and type-strain sentences | supports | NTOU-MSR1T optimum is 30 °C; growth range 10–45 °C is separate. |
| arrhenius-primary | DOI:10.37256/amtt.5220244537; Current Crossref identity and abstract; no body claim | supports | Citation identity is positive; exact Arrhenius note and diagnostic interpretation remain unknown. |
| arrhenius-zero-hit | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.37256/amtt.5220244537&amp;format=json&amp;resultType=core; Current Europe PMC zero-hit response | context_only | Index noncoverage is retrieval context, not a missing DOI or source refutation. |
| arrhenius-publisher.pdf | https://wiserpub.com/uploads/1/20241105/29fd7fa9dab36af843bb14d851dbb31c.pdf; Actual HTTP403 request and retained error bytes, not article PDF | context_only | Body unavailable; exact quoted note remains unknown. Neither failure is a failed required native review check. |
| arrhenius-vor.pdf | https://ojs.wiserpub.com/index.php/AMTT/article/download/4537/2677; Actual HTTP403 request and retained error bytes, not article PDF | context_only | Body unavailable; exact quoted note remains unknown. Neither failure is a failed required native review check. |
| taxonomy | NCBITaxon:3028314; Whole retained official taxonomy XML | supports | Oceanimonas pelagia and NTOU-MSR1 type material match; identity is separate from optimum phenotype. |
| taxonomy-reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/taxonomy-reuse.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Original successful response and separate failed request are distinguished from present copy/read. |
| taxonomy-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/taxonomy-identity.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Whole current identity reading and aliases, without phenotype inference. |
| sources | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-assessment.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Five works; overall source support UNKNOWN and one bounded quoted-note minor. |
| source-identities | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-identities-status.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Exact identities and bounded notice observations. |
| placements | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-placement-ledger.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Twelve external placements accounted for. |
| snippets | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/snippet-ledger.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | All seven schema snippets are literal. |
| notes | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-note-ledger.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Ten notes, including one nonverbatim quoted note and one unresolved quotation. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/node-edge-source-ledger.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Complete current source judgments for nine nodes and eight edges. |
| source-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/primary-reading-scope.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Selected generic abstracts and membrane paragraph; not full scientific article review. |
| source-access | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-access-limits.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Unavailable bodies, zero-hit index and HTTP errors are not source refutations. |
| source-reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-reuse-receipt.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Original requests, current copies and current readings remain distinct. |
| canonical | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/canonical-assessment.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Reported optimum 30 °C is distinct from growth interval 10–45 °C. |
| source-native | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/native-check-context.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Seven native verified snippets; quoted notes assessed separately. |
| quote-check | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/quoted-note-literal-check.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Whole HTML machine search and selected generic context support bounded quotation precision. |
| source-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/evidence-manifest.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Thirty-three frozen source artifacts verified. |
| root-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-root/root-reading.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Independent root science, source and selected primary/owner/history readings. |
| root-literal | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-root/literal-check.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Independent quoted-note check, bounded generic source context. |
| root-browser | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-root/browser-primary-export.json; Actual root browser response; origin/cache-fetch time unknown | context_only | Selected primary browser surfaces retain access and reading qualifications. |
| adjudication | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-root-adjudication.json; Final root adjudication | supports | Final findings, fields, owners and actions control serialization. |

## Limits And Additional Notes

- Overall source support is UNKNOWN for the definition-source calibration, precise optimum-setting interpretations and Arrhenius note. No unavailable-body absence or falsehood is inferred.
- Tolner author-repository HTML and indexed metadata expose abstract context, not a full primary body. Detailed transport/host intervention mechanisms incidentally present in the full abstract display were not adopted.
- Mendoza retained publisher browser export is an actual tool-response snapshot, not raw HTML or full article. Original browser/cache fetch time is not independently known; recorded tool-call bounds remain distinct from current copy/read times.
- Ramón complete retained PMC HTML was machine-searched for the one supplied quote, but scientific reading was confined to the generic membrane-phase paragraph and source identity. No full-article scientific audit is claimed.
- Arrhenius Europe PMC zero-hit JSON is retrieval context only. Positive Crossref identity/abstract is primary metadata. Both arrhenius-publisher.pdf and arrhenius-vor.pdf contain HTTP403 error bytes and are not article PDFs.
- Canonical Preprint-in metadata annotation is linkage, not a retraction/correction. Notice status is bounded to inspected response fields and selected publisher/author surfaces.
- Detailed dangerous pathogen stress/survival/fitness, ROS/defense, AMR and intervention efficacy remain UNASSESSED_SCOPE. No source audit action recommends a biological improvement.
- Catalog relevance is limited to named source contexts: canonical O. pelagia; selected generic Bacteria/Archaea context; Tolner also mentions E. coli as a historical host and two Bacillus species, without adopting detailed transport findings or exact strain/module coverage.
- Edge4 dependent maximal-growth-rate value versus independent temperature-at-peak is qualified; broad local manifests-as endpoints do not establish a hard formal violation.
- Enzyme-kinetics process/rate nuance and observational Arrhenius factor wording remain qualified rather than forced extra findings.
- Formal role checks do not establish source operational-definition or joint-membrane/enzyme causal sufficiency. Detailed pathogen survival/fitness/ROS/AMR/intervention efficacy UNASSESSED_SCOPE.
- Seven uncaptured histories and two scripts are matching-line-only contexts, not whole-body authority.
- Retained catalog canonical absence does not imply all source organisms are absent.
- Private/remote human acceptance remains unknown.
- Root read one exact-target history whole and all sixteen actor/target/event projections; agent ten current whole and six qualified prior histories are separately attributed.
- A verified literal span is not proof of the adjacent exact optimum-setting causal interpretation.
- Original acquisition, current reuse and current reading times remain distinct.
- Actual browser responses are tool exports, not raw HTML; unknown origin/cache-fetch times are not invented. Original requests differ from current copies/readings.
- Qualified B12 QC is not new B13 QC or publication; historical optional failures/retries and 123 no-adapter skips remain explicit.
- Whole 271-line target, 97 captured inputs, five works, twelve external placements, ten grounding fields, nine nodes and eight edges reviewed.
- Sixteen current history projections: ten current whole bodies and six byte-qualified prior readings. Seven uncaptured histories and two scripts remain matching-line context.
- One scratch serializer execution follows root FINAL and explicit permission; root owns actual YAML review, native validation and save.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T003411Z-temperature-optimum
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature optimum
started_at: '2026-10-22T00:28:32.226478Z'
finished_at: '2026-10-22T00:34:11Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits plus independent root primary,
    owner and final adjudication readings. No additional semantic challenge was required.
    Detailed cold-fitness or intervention mechanisms remain UNASSESSED_SCOPE.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole-record review finds one grouped imported-role major and bounded composition-facet,
  quoted-note and human-acceptance minors; reported optimum 30 °C and seven literal
  schema snippets are positive. Operational-definition, optimum-setting and Arrhenius
  interpretations remain unknown.
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
  - path: data/traits/environment/optimum_phenotype_with_numerical_limits.yaml
    sha256: 85423dbaa018cc557495fec708cde21decddd7f0fc0d674f62b09c510d2309ad
    role: context
  - path: data/traits/environment/temperature_optimum.yaml
    sha256: e419e363fd4b2e26f2ce3f092b117fba3103e5155e6dafb95bb5ce5c76644a0d
    role: target
  - path: data/traits/environment/temperature_phenotype_with_numerical_limits.yaml
    sha256: 0eb92c52b7672f072e404d18a007ad19c381367e07601c5cf9cf8445a8562591
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
  - path: history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    sha256: 21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T010000Z-codex-60bca2.yaml
    sha256: 44f328d3f4735a641a33e6f5823a043ccc87594971cfdd9b58be134f3ea70106
    role: context
  - path: history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    sha256: c938f2928f2eb41505d58c2fb72d8de01d99534d766de9af400010e8778988a4
    role: context
  - path: history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml
    sha256: 23be5f6ab519511e3e23feffa85813eec4fa3c7e6b900e77fd4a3adc0c26da0e
    role: context
  - path: history/records/homeoviscous_adaptation/2026-09-15T070756Z-codex-24f768.yaml
    sha256: e813ec0f62859a2d04d6964a082ac78eea8966e44b8224a3fe49eff8552bd778
    role: context
  - path: history/records/homeoviscous_adaptation/2026-09-15T071638Z-codex-eab563.yaml
    sha256: a0aaa509360e1b845bc09a6a0c598a4e9f1a1b31c63be1907dda97293cf605cd
    role: context
  - path: history/records/homeoviscous_adaptation/2026-09-15T072704Z-codex-6cb554.yaml
    sha256: f82d94646e70fd82a5d3f6939339efae8ce0fe5e80fe6f50aab994de6c409fa8
    role: context
  - path: history/records/temperature_optimum/2026-09-15T070759Z-codex-e0d923.yaml
    sha256: 05e6ac08e579e45031473bc1b2ebd8089d18d639534ac5db409d705943882b86
    role: context
  - path: history/records/temperature_optimum_high/2026-09-04T032000Z-codex-f0b8c3.yaml
    sha256: fea3d657cff8ef0b7a7fe783991943f1248f163f2a8ca59ddb218a4183649772
    role: context
  - path: history/records/temperature_optimum_high/2026-09-04T200000Z-codex-183.yaml
    sha256: 10cd203cb37e56abd0f36721b0cdb857bd1f0c769d200d4df963028bb1ab0761
    role: context
  - path: history/records/temperature_optimum_high/2026-09-08T033000Z-codex-506e08.yaml
    sha256: d7aa33a420444c86380ce26aa63c3a77950a19306f3b9bd3692bf2f5be0be999
    role: context
  - path: history/records/temperature_optimum_mid1/2026-09-15T070759Z-codex-35d0a7.yaml
    sha256: c10f51ae7c1806d27cf51df19d9b2e8a601cbdae078a9cf1de8ffab49f339a53
    role: context
  - path: history/records/temperature_optimum_mid3/2026-09-15T070800Z-codex-44b4c3.yaml
    sha256: 410c667e0f7988e3f8df1319c4e42326130b5ee46b34854009b8a744b67ab5e7
    role: context
  - path: history/records/temperature_optimum_very_low/2026-09-04T034000Z-codex-1f380e.yaml
    sha256: 86baac0f11d45ba1989ba43c4c8a43294c652ebd6298f98cccdbb3cd9b32b198
    role: context
  - path: history/records/temperature_optimum_very_low/2026-09-04T210000Z-codex-183.yaml
    sha256: d2dff988a235fc27369f305585f4e865266f3dabf23fa06670a6e30a415f2f6e
    role: context
  - path: history/records/temperature_optimum_very_low/2026-09-08T032500Z-codex-77dafe.yaml
    sha256: dfa857844cb78f8fbb905a762242c0671701caf54fe35c81da0c38422142cab3
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
  - path: proposals/metpo_traitmech_v3/proposal.md
    sha256: 37be7b2c2efe0d1598d62b8df04f08262ba74b9d8068e010df6ee48069449067
    role: context
  - path: proposals/metpo_traitmech_v85/metpo_proposal_classes_robot.tsv
    sha256: 6f32bf183eda67697a4d4c9920416473b0d09b78fab4f1d8d67140db68fb8550
    role: context
  - path: proposals/metpo_traitmech_v85/proposal.md
    sha256: b41cf306750f63743bf9d7c465f3e9ad8b4ec75f19a383d64e2187331d721f05
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
  - path: research/traits/environment/temperature_optimum-deep-research-falcon.md
    sha256: b72cf3545cb53caec432c81c4f8774cc7ec64d86df11384c7f30d0659a74c005
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_homeoviscous_adaptation_trait.py
    sha256: 1c757fd67bda18d2f4afb2fbf63d899844d416d084e2b9d53e298182ae2e4d09
    role: context
  - path: scripts/add_thermotaxis_trait.py
    sha256: 37ed0df3824199c227ed98f79d17dbbcce3aff5ea4aea3103444c9c13a6fcf5a
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
  - path: scripts/connect_mesophilic_graph_183.py
    sha256: 3f1fa78321d7aa98dc2fedde9784e71ed60624a94f825bf3af1674753af56f85
    role: context
  - path: scripts/connect_temperature_delta_high_graph_183.py
    sha256: ccbb1e6bb0e050d2975425914d6412fb3eb5812720407e1d143fbaae5a548bb7
    role: context
  - path: scripts/connect_temperature_delta_very_low_graph_183.py
    sha256: 19eb2722de2fae0c76bf4c83b5f5b13f09841b17def22cdccb86d373711bf879
    role: context
  - path: scripts/connect_temperature_optimum_high_graph_183.py
    sha256: 7d2c6bee0f2af46cec82afe93b93b5a993ffb6042f953e7793b2bbc6ea713504
    role: context
  - path: scripts/connect_temperature_optimum_very_low_graph_183.py
    sha256: 4749be5b5aacc87817ea013e587c41096e8a213c93dde74546f4906a0a08dc7e
    role: context
  - path: scripts/connect_temperature_range_mid3_graph_183.py
    sha256: 0b72a42532f79c8efef52aaec4e60e0b58a7c8b9bc7ec288b9fa21a4c0e25656
    role: context
  - path: scripts/connect_temperature_range_mid4_graph_183.py
    sha256: dd4b85888e88346adb515170c8fa37d542c7c7d9307d8a9fc63b22bdd6fb8b70
    role: context
  - path: scripts/connect_temperature_range_very_low_graph_183.py
    sha256: 71755acb7ce3311fd473c8bef9a71dfed5fc6b8089b79cf33ea95cd5d1dad0a1
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
  - path: scripts/normalize_homeoviscous_nodes.py
    sha256: 9b219161570aff3ca48bf79d7fac0fe0da0a629a32ce6ca60bee9b4b9d0f4bc9
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_pr664_adversarial_review.py
    sha256: 5717a89bee383aa0e12aec9bf30434ccff74efcbe64684d13ef9b290b1accf96
    role: context
  - path: scripts/review_mesophilic_graph_183.py
    sha256: 46f9548808936268217a5e078fc1fa64d74cc2eeb69863ab6f3bb0da21e2b59c
    role: context
  - path: scripts/review_obligately_piezophilic_graph_183.py
    sha256: d8fcbbb725162212cfce96bed9800e2cf08374170b7d929a1928248178111efb
    role: context
  - path: scripts/review_temperature_delta_high_graph_183.py
    sha256: dcade5d2fdf07c76e06cd5d8abca898af95a8faabf70e45a62bebf951f2ae31b
    role: context
  - path: scripts/review_temperature_delta_very_low_graph_183.py
    sha256: 1ac23973b6cf54861f6ae79afefe93e39cc9382a93c73c36a8daa37b376334d0
    role: context
  - path: scripts/review_temperature_optimum_high_graph_183.py
    sha256: ed7b046129400db1fa4352250d27569e0844ef837000577f1448e565a0e60576
    role: context
  - path: scripts/review_temperature_optimum_very_low_graph_183.py
    sha256: 17e41b0426e6c41a43e7624799cf35db9737ef372d3aeb3ea40ac0a2dce20869
    role: context
  - path: scripts/review_temperature_range_mid3_graph_183.py
    sha256: 623668a7f0f2cd487c096c2b786471fe986f64cfd5c34edad30422299f03794a
    role: context
  - path: scripts/review_temperature_range_mid4_graph_183.py
    sha256: 51611a8200146f1887831e5b2a49800151dc0b112d177853c3055dd442852a5a
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
- target_id: METPO:1000304
  path: data/traits/environment/temperature_optimum.yaml
  label: temperature optimum
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum.yaml
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
  selection: Eighth record of the actual local batch 013 queue. Whole 271-line target
    and 97 captured inputs verified before judgment; local review does not assert
    remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000304
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000304
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000304
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000304
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot.
  evidence_ids:
  - check-check-pathway-links
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000304
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000304
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000304
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000304
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: temperature-optimum-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000304
  command: just validate data/traits/environment/temperature_optimum.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  evidence_ids:
  - check-temperature-optimum-validate
- check_id: temperature-optimum-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000304
  command: just validate-strict data/traits/environment/temperature_optimum.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The actual validate-strict command passed.
  evidence_ids:
  - check-temperature-optimum-strict
- check_id: temperature-optimum-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000304
  command: just verify-snippets --record data/traits/environment/temperature_optimum.yaml
    --out /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'All seven schema snippets over two references were VERIFIED. The native
    checker does not test quoted notes. Two separately quoted note spans were reviewed
    manually: one bounded nonverbatim note and one unresolved note.'
  evidence_ids:
  - check-temperature-optimum-snippets-network
- check_id: batch012-qc
  name: Qualified batch-twelve QC
  status: passed
  required: true
  target_ids:
  - METPO:1000304
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual prior QC qualified against B13 bytes; this is not a new B13 QC execution
    or publication.
  evidence_ids:
  - check-batch012-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000304
  summary: Zero protein classes or instances in this quantitative NONMECHANISTIC optimum
    overview; no token protein requirement.
  evidence_ids:
  - record
  - policy
  - expression
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
- evidence_id: check-temperature-optimum-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-validate.log
  locator: Executed 2026-10-22T00:28:48.767134+00:00 through 2026-10-22T00:28:49.307749+00:00;
    metadata temperature-optimum-validate.json
  accessed_at: '2026-10-22T00:28:49.307749Z'
  support: context_only
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  snapshot_sha256: 55eb25356bd46d1122299692cbae0ef148240b1bc908af55fffa32f86cecb645
- evidence_id: check-temperature-optimum-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-strict.log
  locator: Executed 2026-10-22T00:28:48.767149+00:00 through 2026-10-22T00:28:49.739728+00:00;
    metadata temperature-optimum-strict.json
  accessed_at: '2026-10-22T00:28:49.739728Z'
  support: context_only
  summary: The actual validate-strict command passed.
  snapshot_sha256: 5821324b5f54ac4706aa8f0ed6a70197c5ff4bfe2834428ba37b8be4b98dd5d5
- evidence_id: check-temperature-optimum-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-snippets-network.log
  locator: Executed 2026-10-22T00:29:12.030851+00:00 through 2026-10-22T00:29:15.555699+00:00;
    metadata temperature-optimum-snippets-network.json
  accessed_at: '2026-10-22T00:29:15.555699Z'
  support: context_only
  summary: 'All seven schema snippets over two references were VERIFIED. The native
    checker does not test quoted notes. Two separately quoted note spans were reviewed
    manually: one bounded nonverbatim note and one unresolved note.'
  snapshot_sha256: e24c822975cab3c8c8b05867a31b3b9dbf4c1d3b8cbd3eb62f0389c562caa56f
- evidence_id: check-batch012-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log
  locator: Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00;
    metadata batch012-qc.json
  accessed_at: '2026-10-21T23:04:01.628423Z'
  support: context_only
  summary: Actual prior QC qualified against B13 bytes; this is not a new B13 QC execution
    or publication.
  snapshot_sha256: 8ab67b821055863ce13616ed79a0acacaf61b632dcb80f6aa63fd45f0485c52b
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_optimum.yaml
  locator: Whole 271-line current record
  accessed_at: '2026-10-22T00:28:32.921206Z'
  support: supports
  summary: Nine nodes, eight edges and sixteen embedded events; one canonical example,
    zero protein classes and zero instances.
  snapshot_sha256: e419e363fd4b2e26f2ce3f092b117fba3103e5155e6dafb95bb5ce5c76644a0d
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json
  locator: Actual B12-to-B13 qualification
  accessed_at: '2026-10-21T23:05:39.165510Z'
  support: supports
  summary: Current byte comparisons retain original diagnostic failures, retries and
    skips.
  snapshot_sha256: e1fa58cb626ef76e2b2066404078b9893b069a5b53a0cffbc3a184e68f0cd9f1
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Independent actual-output verification
  accessed_at: '2026-10-21T23:07:53.187524Z'
  support: supports
  summary: Qualification verification, not new QC.
  snapshot_sha256: 42a5580991e7251963a9b83d0817facda019de29d9e13208e870c27e1c62ad7d
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-21T23:09:00.804479Z'
  support: supports
  summary: Actual local initialization; publication remains a separate action.
  snapshot_sha256: cda5c0d3753e7a2a3ceb9ba723261fa79d4f760aad1713ff2d33b08def3577f7
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:31:21.613297Z'
  support: supports
  summary: Actual referents and optional protein applicability.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:31:21.613297Z'
  support: supports
  summary: Source scope and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:31:21.613297Z'
  support: supports
  summary: Current facets and NONMECHANISTIC scope.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:31:21.613297Z'
  support: supports
  summary: Shared mapping for future empty fields; populated IDs are skipped.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: local-v2
  kind: authority
  reference: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:31:21.613297Z'
  support: supports
  summary: Manifests-as has broad formal endpoints and state-to-trait prose.
  snapshot_sha256: 4ab5ca37ff8595210254b1099563b4425ecd737ed375dc5a932b44e2ad5c332e
- evidence_id: local-v3
  kind: authority
  reference: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:31:21.613297Z'
  support: supports
  summary: Exact membrane-fluidity quality.
  snapshot_sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
- evidence_id: local-v85
  kind: authority
  reference: proposals/metpo_traitmech_v85/metpo_proposal_classes_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:31:21.613297Z'
  support: supports
  summary: Exact homeoviscous-adaptation process, distinct from fluidity quality.
  snapshot_sha256: 6f32bf183eda67697a4d4c9920416473b0d09b78fab4f1d8d67140db68fb8550
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/capture-verification.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:29:09.999665Z'
  support: supports
  summary: All 97 captured inputs and whole target verified.
  snapshot_sha256: f25eb852cae8c7ecd783c7628e7d76b242a7c0ce26c1db715cc19b9d54f6e514
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/identity-assessment.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.580035Z'
  support: supports
  summary: Active exact optimum and both direct parents; local proposal identities
    separate.
  snapshot_sha256: 888d5913c259212d0f0b65b5079e4388d7a7ba540a76638d00b0d08572bb837c
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/node-edge-grounding-ledger.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.610081Z'
  support: supports
  summary: All nine nodes and eight edges, including positives and measurement qualifications.
  snapshot_sha256: 01a4a3def2f46c852454888498db87575a9ded1e17a4242837305ce0fe87c472
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/owner-provenance-assessment.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.612421Z'
  support: supports
  summary: Current owners, conditional migration and sibling-only context.
  snapshot_sha256: 58ca640ed6504c15622d8672f5f00727a597aba0c62b5e2597999d6092b89c25
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/owner-primary-reading.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.580191Z'
  support: supports
  summary: Whole process-quality migration and normalizer, selected canonical and
    shared grounding guards.
  snapshot_sha256: ebc7026190227e58bc07b2fec48b896aaaebeeb8e44ec858c3104a49ec2977bb
- evidence_id: writer-shape
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/writer-current-shape-check.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.580950Z'
  support: supports
  summary: Current promotes edges skip the old enables conversion; correct rate QUALITY
    is retained.
  snapshot_sha256: 9f2dd9b22227ae5da8740937c38e0e1425e74eee085f7790082480ac667cfd76
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/search-and-provenance.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:29:10.197909Z'
  support: supports
  summary: 282 ignored-inclusive paths; 73 actual target arrays, zero exact current
    target.
  snapshot_sha256: 701f0f515d09b617ee028f7ed96d43610ff94b1ba633350b5312949a19fbc747
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/history-reading-provenance.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.612112Z'
  support: supports
  summary: 'Sixteen current projections: ten current whole bodies and six byte-qualified
    prior readings.'
  snapshot_sha256: 2aa3c7489663875476c9d273356c1337ada8b9e5b7a9f5047adc6689a88e31ca
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/discovery-disposition.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.609845Z'
  support: supports
  summary: Seven uncaptured histories and two scripts remain matching-line-only context.
  snapshot_sha256: 358a51691bc64ab64f257eb6e569e0ab3d55e06b1328e8edb1e27e645d4460f0
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/expression-and-readiness.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.612922Z'
  support: supports
  summary: No exact canonical catalog match; source species coverage not globally
    absent.
  snapshot_sha256: 503cb2b3bb309d9c1bcd079d55011431f95231b1f8cd4ed2b00bd4521c9ad9e7
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/local-authority-reading.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.545692Z'
  support: supports
  summary: Actual local proposal/mapping rows; lexical indicates has no invented imported
    constraints.
  snapshot_sha256: a24bd0d690e668394c83bf5bbeae021a5f7e6fc37ba5ee28d4e7ba72b3f125c2
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/evidence-manifest.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.616834Z'
  support: supports
  summary: Twenty-nine frozen grounding artifacts verified.
  snapshot_sha256: 412173bc7552ca29020249bead1fbaa0d15195e3b7faad0965a2551a88239091
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl
  locator: Retained primary authority, locally read at the recorded time
  accessed_at: '2026-10-22T00:29:10.075566Z'
  support: supports
  summary: Active 1000304 with both direct parents 1000533/1000536.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: metpo-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/metpo-authority.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:29:10.075566Z'
  support: supports
  summary: Selected primary statements and exact-byte provenance.
  snapshot_sha256: 72a1e9ced561a4da6821a3405ccd353a209867374e6b8aed3eaa7848858b4587
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Retained primary authority, locally read at the recorded time
  accessed_at: '2026-10-22T00:29:10.040413Z'
  support: supports
  summary: Actual inherited process domain/range for regulates and positively-regulates.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: ro-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/selected-ro-primary-reading.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:29:10.040413Z'
  support: supports
  summary: Selected primary statements and exact-byte provenance.
  snapshot_sha256: 9a99d4d353437722dc98444e29be1dab9e7158226cd2667ff96d1e8421399645
- evidence_id: tolner
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Indexed abstract
  accessed_at: '2026-10-21T09:29:01.331044Z'
  support: supports
  summary: Generic adaptation and literal snippets; operational-definition and precise
    optimum inference unknown.
  snapshot_sha256: 56f69a7ce2e69822ef753fec5c43716583184e45fc1a2c0cae98aa9bdb841265
- evidence_id: tolner-author
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Institutional abstract page
  accessed_at: '2026-10-21T09:29:00.791083Z'
  support: supports
  summary: Abstract context only; not a full primary body.
  snapshot_sha256: 3c475aae5c42532ff36e66a262fe2d6a9c6fc8b64aa6576d93efdc96cada4134
- evidence_id: mendoza
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Indexed abstract
  accessed_at: '2026-10-21T10:00:02.042457Z'
  support: supports
  summary: Generic membrane context and current literal snippets; exact optimum-setting
    inference unknown.
  snapshot_sha256: 801da630644a181211f991a6f21c49b178e42a65f615c4eebd8196bc29244588
- evidence_id: mendoza-browser
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Actual publisher abstract tool export; origin/cache-fetch time unknown
  accessed_at: '2026-10-21T23:38:35Z'
  support: supports
  summary: Generic membrane physics, not a full article or raw HTML.
  snapshot_sha256: b8635235ad5e362d0b33ef4834f84eb25fe7ff6b1bd1321affb2b61cecbc66fc
- evidence_id: cold-metadata
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Indexed metadata and abstract
  accessed_at: '2026-10-21T22:07:08.865512Z'
  support: supports
  summary: Identity and broad review context only.
  snapshot_sha256: da5cffab81fe0e039c6fcec8f318b2715f5604eaf8722ea6f63f944178ed447b
- evidence_id: cold-body
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Zero-based HTML paragraph 17, selected first seven generic sentences; whole
    surface literal search only
  accessed_at: '2026-10-21T22:07:50.938485Z'
  support: supports
  summary: Generic composition/physical-state context is positive; the quoted edge
    5 note differs from inspected wording.
  snapshot_sha256: bb09a59c07f43ff0af177f89b624c8b5d4841e513ed0d478120954a016342889
- evidence_id: canonical-primary
  kind: primary_source
  reference: DOI:10.1007/s10482-024-01948-y
  locator: Indexed abstract temperature and type-strain sentences
  accessed_at: '2026-10-21T19:34:30.779057Z'
  support: supports
  summary: NTOU-MSR1T optimum is 30 °C; growth range 10–45 °C is separate.
  snapshot_sha256: 73ea00102769ce9782573737fb2b62eb6d86b441a248b0a55c045bb6a3c64a9e
- evidence_id: arrhenius-primary
  kind: primary_source
  reference: DOI:10.37256/amtt.5220244537
  locator: Current Crossref identity and abstract; no body claim
  accessed_at: '2026-10-22T00:29:26.281512Z'
  support: supports
  summary: Citation identity is positive; exact Arrhenius note and diagnostic interpretation
    remain unknown.
  snapshot_sha256: 9f5ed8f0f9d07aface3f482bc888a6c47a4d9683abf51f76b16bf56412857cf7
- evidence_id: arrhenius-zero-hit
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.37256/amtt.5220244537&format=json&resultType=core
  locator: Current Europe PMC zero-hit response
  accessed_at: '2026-10-22T00:29:26.622156Z'
  support: context_only
  summary: Index noncoverage is retrieval context, not a missing DOI or source refutation.
  snapshot_sha256: d0eef7c61f38fab3f0b2a3d73127915d63da077e0617bff6ac487ec290045df3
- evidence_id: arrhenius-publisher.pdf
  kind: validation
  reference: https://wiserpub.com/uploads/1/20241105/29fd7fa9dab36af843bb14d851dbb31c.pdf
  locator: Actual HTTP403 request and retained error bytes, not article PDF
  accessed_at: '2026-10-22T00:29:26.719413Z'
  support: context_only
  summary: Body unavailable; exact quoted note remains unknown. Neither failure is
    a failed required native review check.
  snapshot_sha256: ab237907ceb462d30eabf4e1f5fac11b03b409aa667ff2382d4cde73af272928
- evidence_id: arrhenius-vor.pdf
  kind: validation
  reference: https://ojs.wiserpub.com/index.php/AMTT/article/download/4537/2677
  locator: Actual HTTP403 request and retained error bytes, not article PDF
  accessed_at: '2026-10-22T00:30:07.641227Z'
  support: context_only
  summary: Body unavailable; exact quoted note remains unknown. Neither failure is
    a failed required native review check.
  snapshot_sha256: 708a4e897aab21f52285f7c14de3ff59007873e38af17e6db259f86462573807
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:3028314
  locator: Whole retained official taxonomy XML
  accessed_at: '2026-10-21T16:43:16.762138Z'
  support: supports
  summary: Oceanimonas pelagia and NTOU-MSR1 type material match; identity is separate
    from optimum phenotype.
  snapshot_sha256: 17213af06e1b89f10c93a152bc8cfe6553b0ada3d5bb9a3d8a4c578b5f379a10
- evidence_id: taxonomy-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/taxonomy-reuse.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:29:57.849250Z'
  support: supports
  summary: Original successful response and separate failed request are distinguished
    from present copy/read.
  snapshot_sha256: e878c69ee1b57bd42e48aefb92f3ac6612d10d17181b37b4b039b2445c658b26
- evidence_id: taxonomy-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-ground-agent/taxonomy-identity.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:31:21.579884Z'
  support: supports
  summary: Whole current identity reading and aliases, without phenotype inference.
  snapshot_sha256: 138d6a36605daf18ca2bd69c8c46989ae9a95ecdacc41bee3d05f96da3827249
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-assessment.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.254064Z'
  support: supports
  summary: Five works; overall source support UNKNOWN and one bounded quoted-note
    minor.
  snapshot_sha256: 73a53627a4dfa978cbe1e9682561257610caba29ed5abd63a260efbb44ca475f
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-identities-status.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.254064Z'
  support: supports
  summary: Exact identities and bounded notice observations.
  snapshot_sha256: d8c118fb90aaf4ec3d415c62ef21f614cda5669c1f4f3ff47c74fa32388d7bb9
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-placement-ledger.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.254064Z'
  support: supports
  summary: Twelve external placements accounted for.
  snapshot_sha256: e9e08a4feab5fad635eaed83f266f44979c778107ff7689d2d34cea07fb6d9f7
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/snippet-ledger.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.254064Z'
  support: supports
  summary: All seven schema snippets are literal.
  snapshot_sha256: bbb9b89bed9563772168a764f82ef3c660544afb8ce13c65626cebf4aad7d318
- evidence_id: notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-note-ledger.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.254064Z'
  support: supports
  summary: Ten notes, including one nonverbatim quoted note and one unresolved quotation.
  snapshot_sha256: d610d816dd00af108e4f7e2349e78962b2e730a4c34961c0f3f4a898f729b797
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/node-edge-source-ledger.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.254064Z'
  support: supports
  summary: Complete current source judgments for nine nodes and eight edges.
  snapshot_sha256: f22b7185fdbc4d0f93c135aa1bfe2c8e492fc7da14f8a22b901d8ce0a00f74b6
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/primary-reading-scope.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.254064Z'
  support: supports
  summary: Selected generic abstracts and membrane paragraph; not full scientific
    article review.
  snapshot_sha256: c12ef98ab47fdcb2c96c88c88527d72c1c5e3b11de20dcc1c379c674e1105638
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-access-limits.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.254064Z'
  support: supports
  summary: Unavailable bodies, zero-hit index and HTTP errors are not source refutations.
  snapshot_sha256: 476df77ba8b72db94439bbdcc1c9c13d2c8699deeef33c861d88dcc5284876f0
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/source-reuse-receipt.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:29:18.065659Z'
  support: supports
  summary: Original requests, current copies and current readings remain distinct.
  snapshot_sha256: c3e184148dc3bd096570d80a78419a01f30da89d99edd99306fc49af4436f86f
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/canonical-assessment.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.254064Z'
  support: supports
  summary: Reported optimum 30 °C is distinct from growth interval 10–45 °C.
  snapshot_sha256: 3be19b17241ba5713caa0b6018ef4a731f8bc27c5beac618e7dca81406bac014
- evidence_id: source-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/native-check-context.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.254064Z'
  support: supports
  summary: Seven native verified snippets; quoted notes assessed separately.
  snapshot_sha256: 6ca11105f9d721682c0a5ae45044c76695483ef5e8ef31cb1e9981c96ff98d43
- evidence_id: quote-check
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/quoted-note-literal-check.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:30:36.766725Z'
  support: supports
  summary: Whole HTML machine search and selected generic context support bounded
    quotation precision.
  snapshot_sha256: 101d87f0953f57767c7dd3c54164494b99f37583e330c6960201a2c06052c363
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-agent/evidence-manifest.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:32:17.277512Z'
  support: supports
  summary: Thirty-three frozen source artifacts verified.
  snapshot_sha256: 46983809f544b89e4a18b37481cd3699c4c2fa3c27854c8c60eb466b08c1cfa7
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-root/root-reading.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:33:23.267440Z'
  support: supports
  summary: Independent root science, source and selected primary/owner/history readings.
  snapshot_sha256: 5b5dc633b2bc24eba08f807976e1357c068d277368474c13f90027105ee2a275
- evidence_id: root-literal
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-root/literal-check.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:30:54.821992Z'
  support: supports
  summary: Independent quoted-note check, bounded generic source context.
  snapshot_sha256: a1984a7c8a270cc69049795c9972d075b09b6ae07bc841b7d7a8c4d651a2c302
- evidence_id: root-browser
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-source-root/browser-primary-export.json
  locator: Actual root browser response; origin/cache-fetch time unknown
  accessed_at: '2026-10-22T00:29:18Z'
  support: context_only
  summary: Selected primary browser surfaces retain access and reading qualifications.
  snapshot_sha256: 33b0f17d0e11cdb9e3c1436fd0066b608dca5eb129fb68b118edf6ee2ae1ec60
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-22T00:33:23.267749Z'
  support: supports
  summary: Final findings, fields, owners and actions control serialization.
  snapshot_sha256: 2ecf107fe3e51520d5e2631b96567ef1ff1f8e0aa49d7aa56583bf3334577721
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active identity and hierarchy'
  outcome: supported
  target_ids:
  - METPO:1000304
  summary: Active METPO:1000304 and both direct parents 1000533/1000536 match the
    optimum measurement concept. Local v3 fluidity, v85 homeoviscous adaptation and
    v2 manifests-as retain separate proposal status.
  evidence_ids:
  - identity
  - metpo-primary
  - local-v2
  - local-v3
  - local-v85
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: operational-definition support'
  outcome: unknown
  target_ids:
  - METPO:1000304
  summary: Ordinary temperature-at-maximal-growth meaning is coherent. Inspected generic
    thermophile and membrane sources do not establish the stronger best-maintained
    membrane/enzyme operational equivalence or unique joint optimum-setting claim.
    Body access limits do not refute those claims.
  evidence_ids:
  - sources
  - placements
  - notes
  - mendoza
  - tolner
- assessment_id: canonical-example
  area: quantity
  topic: 'Native checklist: reported optimum point'
  outcome: supported
  target_ids:
  - METPO:1000304
  summary: Oceanimonas pelagia NTOU-MSR1T has a reported optimum of 30 °C, separate
    from growth at 10–45 °C. The parent placement retains the local boundary policy
    without attributing TraitMech bins to the paper. Official taxonomy verifies identity
    separately.
  evidence_ids:
  - canonical
  - canonical-primary
  - taxonomy
  - owner-primary
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: five works and twelve placements'
  outcome: unknown
  target_ids:
  - METPO:1000304
  summary: Source identities and generic membrane physics are positive; exact optimum-setting
    and Arrhenius diagnostic interpretations remain unknown. The positive Crossref
    identity and two HTTP403 body failures are separate. Detailed host/pathogen stress,
    fitness and intervention efficacy remain UNASSESSED_SCOPE.
  evidence_ids:
  - sources
  - source-identities
  - placements
  - notes
  - source-access
  - source-reading
  - arrhenius-primary
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: snippets and quoted notes'
  outcome: concern
  target_ids:
  - METPO:1000304
  summary: All seven schema snippets are literal and native-verified. The edge 5 Ramón
    quoted note is nonverbatim on the inspected whole HTML surface while its concept
    is positive. The edge 7 Arrhenius quotation remains unknown because adequate body
    text was unavailable.
  evidence_ids:
  - snippets
  - notes
  - quote-check
  - cold-body
  - root-literal
  - source-native
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all nine current referents'
  outcome: concern
  target_ids:
  - METPO:1000304
  summary: Node 3 composition versus CELLULAR_LOCALIZATION requires bounded facet
    clarification without a forced exact retype. Fluidity and maximal growth rate
    remain qualities; homeoviscous adaptation is a process. Enzyme-kinetics and Arrhenius-factor
    nuances remain qualifications.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - schema
  - identity
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"node_id\":\
    \ \"temperature_optimum_trait\",\n      \"label\": \"temperature optimum\",\n\
    \      \"node_type\": \"TRAIT\",\n      \"grounding\": \"METPO:1000304\",\n  \
    \    \"outcome\": \"supported\",\n      \"assessment\": \"Active temperature-optimum\
    \ trait identity and both direct parents fit.\"\n    },\n    {\n      \"index\"\
    : 1,\n      \"node_id\": \"ambient_temperature\",\n      \"label\": \"ambient\
    \ temperature\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n      \"grounding\"\
    : null,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Actual imposed\
    \ ambient temperature is a condition/value, not an explicitly described change\
    \ event; environmental enum is appropriate and not the basis of relation failure\
    \ alone.\"\n    },\n    {\n      \"index\": 2,\n      \"node_id\": \"membrane_fluidity\"\
    ,\n      \"label\": \"membrane fluidity\",\n      \"node_type\": \"QUALITY\",\n\
    \      \"grounding\": \"METPO:1007505\",\n      \"outcome\": \"supported\",\n\
    \      \"assessment\": \"Explicit membrane physical attribute is QUALITY with\
    \ exact local v3 identity.\"\n    },\n    {\n      \"index\": 3,\n      \"node_id\"\
    : \"homoviscous_lipid_composition\",\n      \"label\": \"homoviscous lipid composition\"\
    ,\n      \"node_type\": \"CELLULAR_LOCALIZATION\",\n      \"grounding\": null,\n\
    \      \"outcome\": \"concern\",\n      \"assessment\": \"Lipid composition tuned\
    \ to fluidity denotes composition rather than a location. CELLULAR_LOCALIZATION\
    \ may intend membrane material/component shorthand, but that is not explicit.\
    \ Bounded facet precision minor; no forced replacement type or chemical identity\
    \ invented.\"\n    },\n    {\n      \"index\": 4,\n      \"node_id\": \"enzyme_kinetics\"\
    ,\n      \"label\": \"enzyme kinetics\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"grounding\": null,\n      \"outcome\": \"unknown\",\n      \"assessment\"\
    : \"Enzyme turnover can be processual; temperature dependence of its rate can\
    \ be a quality. Current kinetics wording remains qualified; role major does not\
    \ require forcing this ambiguity.\"\n    },\n    {\n      \"index\": 5,\n    \
    \  \"node_id\": \"maximal_growth_rate\",\n      \"label\": \"maximal growth rate\"\
    ,\n      \"node_type\": \"QUALITY\",\n      \"grounding\": null,\n      \"outcome\"\
    : \"supported\",\n      \"assessment\": \"Peak specific growth rate is a measurable\
    \ QUALITY, not the ambient temperature that attains it.\"\n    },\n    {\n   \
    \   \"index\": 6,\n      \"node_id\": \"homeoviscous_adaptation\",\n      \"label\"\
    : \"homeoviscous adaptation\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n\
    \      \"grounding\": \"METPO:1016200\",\n      \"outcome\": \"supported\",\n\
    \      \"assessment\": \"Explicit lipid-remodeling process agrees with captured\
    \ v85 homeoviscous-adaptation definition, distinct from fluidity quality.\"\n\
    \    },\n    {\n      \"index\": 7,\n      \"node_id\": \"arrhenius_plot_deviation\"\
    ,\n      \"label\": \"Arrhenius plot deviation from linearity\",\n      \"node_type\"\
    : \"EXPERIMENTAL_FACTOR\",\n      \"grounding\": null,\n      \"outcome\": \"\
    unknown\",\n      \"assessment\": \"Deviation in an Arrhenius plot is an observational\
    \ measurement feature used for interpretation; EXPERIMENTAL_FACTOR is broad and\
    \ no forced additional facet finding is made.\"\n    },\n    {\n      \"index\"\
    : 8,\n      \"node_id\": \"stress_growth_regime\",\n      \"label\": \"stress\
    \ / non-physiological growth regime\",\n      \"node_type\": \"STATE\",\n    \
    \  \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Non-physiological growth condition is a state/regime; detailed biological\
    \ support belongs to source audit.\"\n    }\n  ],\n  \"source\": [\n    {\n  \
    \    \"index\": 0,\n      \"node_id\": \"temperature_optimum_trait\",\n      \"\
    label\": \"temperature optimum\",\n      \"node_type\": \"TRAIT\",\n      \"outcome\"\
    : \"SUPPORTED_MEASUREMENT_CONCEPT\",\n      \"assessment\": \"Maximum growth-rate\
    \ temperature is the current measurement concept; canonical abstract provides\
    \ a reported optimum. General definition-source sufficiency remains unknown.\"\
    \n    },\n    {\n      \"index\": 1,\n      \"node_id\": \"ambient_temperature\"\
    ,\n      \"label\": \"ambient temperature\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\",\n      \"assessment\": \"\
    Ambient growth temperature is the measured environmental variable; no claim of\
    \ a particular universal value.\"\n    },\n    {\n      \"index\": 2,\n      \"\
    node_id\": \"membrane_fluidity\",\n      \"label\": \"membrane fluidity\",\n \
    \     \"node_type\": \"QUALITY\",\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\"\
    ,\n      \"assessment\": \"Mendoza and Ramón support membrane fluidity as a physical\
    \ property. Detailed bioenergetic efficacy is not assessed.\"\n    },\n    {\n\
    \      \"index\": 3,\n      \"node_id\": \"homoviscous_lipid_composition\",\n\
    \      \"label\": \"homoviscous lipid composition\",\n      \"node_type\": \"\
    CELLULAR_LOCALIZATION\",\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\",\n\
    \      \"assessment\": \"Lipid composition is relevant to physical state in the\
    \ selected abstracts; the declared CELLULAR_LOCALIZATION facet is a grounding\
    \ concern, not source identity.\"\n    },\n    {\n      \"index\": 4,\n      \"\
    node_id\": \"enzyme_kinetics\",\n      \"label\": \"enzyme kinetics\",\n     \
    \ \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"outcome\": \"UNKNOWN_EXACT_SCOPE\"\
    ,\n      \"assessment\": \"Thermophile enzyme adaptation is generic context; whole-network\
    \ turnover and its precise optimum effects are not established by the selected\
    \ Tolner text.\"\n    },\n    {\n      \"index\": 5,\n      \"node_id\": \"maximal_growth_rate\"\
    ,\n      \"label\": \"maximal growth rate\",\n      \"node_type\": \"QUALITY\"\
    ,\n      \"outcome\": \"SUPPORTED_MEASUREMENT_CONCEPT\",\n      \"assessment\"\
    : \"Peak growth rate is distinguishable from the temperature at which the peak\
    \ is measured. No direct assay/formula is reconstructed.\"\n    },\n    {\n  \
    \    \"index\": 6,\n      \"node_id\": \"homeoviscous_adaptation\",\n      \"\
    label\": \"homeoviscous adaptation\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\",\n      \"assessment\": \"\
    Selected abstracts and Ramón paragraph support generic homeoviscous remodeling.\
    \ No novel pathway or intervention is inferred.\"\n    },\n    {\n      \"index\"\
    : 7,\n      \"node_id\": \"arrhenius_plot_deviation\",\n      \"label\": \"Arrhenius\
    \ plot deviation from linearity\",\n      \"node_type\": \"EXPERIMENTAL_FACTOR\"\
    ,\n      \"outcome\": \"UNKNOWN_BODY_UNAVAILABLE\",\n      \"assessment\": \"\
    Arrhenius deviation representation refers to a cited review whose body could not\
    \ be acquired; exact diagnostic interpretation is unverified.\"\n    },\n    {\n\
    \      \"index\": 8,\n      \"node_id\": \"stress_growth_regime\",\n      \"label\"\
    : \"stress / non-physiological growth regime\",\n      \"node_type\": \"STATE\"\
    ,\n      \"outcome\": \"UNKNOWN_BODY_UNAVAILABLE\",\n      \"assessment\": \"\
    Stress/non-physiological regime as inferred from nonlinearity remains unknown\
    \ from the accessible citation abstract.\"\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all eight current relations'
  outcome: concern
  target_ids:
  - METPO:1000304
  summary: Edges 0/1/2/3/5/6 form one inherited-process-role major based on actual
    condition, composition and quality referents. Edge 4 distinguishes the dependent
    peak rate from the temperature attaining it, but broad manifests-as roles do not
    establish a hard violation. Lexical indicates receives no invented imported constraints.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ro-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"subject\":\
    \ \"ambient_temperature\",\n      \"predicate\": \"regulates\",\n      \"predicate_id\"\
    : \"RO:0002211\",\n      \"object\": \"membrane_fluidity\",\n      \"outcome\"\
    : \"concern\",\n      \"assessment\": \"RO2211 requires process domain and range.\
    \ Ambient temperature is an imposed condition/value, and fluidity is an explicit\
    \ quality; no event description supplies a process reading.\"\n    },\n    {\n\
    \      \"index\": 1,\n      \"subject\": \"homoviscous_lipid_composition\",\n\
    \      \"predicate\": \"regulates\",\n      \"predicate_id\": \"RO:0002211\",\n\
    \      \"object\": \"membrane_fluidity\",\n      \"outcome\": \"concern\",\n \
    \     \"assessment\": \"RO2211 process endpoints conflict with composition/material-or-quality\
    \ subject and explicit fluidity QUALITY object; node3 type clarification alone\
    \ would not fix this relation.\"\n    },\n    {\n      \"index\": 2,\n      \"\
    subject\": \"ambient_temperature\",\n      \"predicate\": \"regulates\",\n   \
    \   \"predicate_id\": \"RO:0002211\",\n      \"object\": \"enzyme_kinetics\",\n\
    \      \"outcome\": \"concern\",\n      \"assessment\": \"RO2211 process domain\
    \ conflicts with ambient temperature condition/value. Enzyme-turnover process\
    \ interpretation of object remains possible; subject mismatch independently decisive.\"\
    \n    },\n    {\n      \"index\": 3,\n      \"subject\": \"enzyme_kinetics\",\n\
    \      \"predicate\": \"promotes\",\n      \"predicate_id\": \"RO:0002213\",\n\
    \      \"object\": \"maximal_growth_rate\",\n      \"outcome\": \"concern\",\n\
    \      \"assessment\": \"RO2213 inherits process range from RO2211; peak specific\
    \ growth rate is an explicit quality. Enzyme-kinetics process/attribute nuance\
    \ does not remove this object conflict.\"\n    },\n    {\n      \"index\": 4,\n\
    \      \"subject\": \"maximal_growth_rate\",\n      \"predicate\": \"manifests\
    \ as\",\n      \"predicate_id\": \"METPO:2007400\",\n      \"object\": \"temperature_optimum_trait\"\
    ,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Local manifests-as\
    \ broad formal endpoints do not force a domain failure. Subject is peak growth-rate\
    \ value, while description refers to the temperature attaining that peak. Retain\
    \ dependent-rate versus independent-condition distinction as a qualification;\
    \ criterion shorthand may be intended, no replacement predicate/retype dictated.\"\
    \n    },\n    {\n      \"index\": 5,\n      \"subject\": \"homeoviscous_adaptation\"\
    ,\n      \"predicate\": \"regulates\",\n      \"predicate_id\": \"RO:0002211\"\
    ,\n      \"object\": \"membrane_fluidity\",\n      \"outcome\": \"concern\",\n\
    \      \"assessment\": \"Homeoviscous-adaptation process fits RO2211 domain; fluidity\
    \ QUALITY object conflicts with process range.\"\n    },\n    {\n      \"index\"\
    : 6,\n      \"subject\": \"membrane_fluidity\",\n      \"predicate\": \"promotes\"\
    ,\n      \"predicate_id\": \"RO:0002213\",\n      \"object\": \"maximal_growth_rate\"\
    ,\n      \"outcome\": \"concern\",\n      \"assessment\": \"RO2213 inherited process/process\
    \ roles conflict with explicit fluidity and maximal-growth-rate qualities.\"\n\
    \    },\n    {\n      \"index\": 7,\n      \"subject\": \"arrhenius_plot_deviation\"\
    ,\n      \"predicate\": \"indicates\",\n      \"predicate_id\": null,\n      \"\
    object\": \"stress_growth_regime\",\n      \"outcome\": \"unknown\",\n      \"\
    assessment\": \"Lexical indicates has no predicate_id; no imported domain/range\
    \ invented. Observational inference from deviation to regime remains source-dependent,\
    \ not a biological causal claim established by ontology.\"\n    }\n  ],\n  \"\
    source\": [\n    {\n      \"index\": 0,\n      \"subject\": \"ambient_temperature\"\
    ,\n      \"predicate\": \"regulates\",\n      \"object\": \"membrane_fluidity\"\
    ,\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\",\n      \"assessment\": \"\
    Mendoza abstract explicitly links lower growth temperature with membrane remodeling/fluidity.\
    \ The wording that ambient temperature sets a target remains interpretive; no\
    \ measured optimum follows.\",\n      \"source_locator\": \"mendoza-metadata.json;\
    \ abstract first two sentences\"\n    },\n    {\n      \"index\": 1,\n      \"\
    subject\": \"homoviscous_lipid_composition\",\n      \"predicate\": \"regulates\"\
    ,\n      \"object\": \"membrane_fluidity\",\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\"\
    ,\n      \"assessment\": \"Lipid composition and fluidity adaptation are supported\
    \ as generic context. A particular optimal growth temperature is not demonstrated\
    \ by this abstract.\",\n      \"source_locator\": \"mendoza-metadata.json; abstract\
    \ first two sentences\"\n    },\n    {\n      \"index\": 2,\n      \"subject\"\
    : \"ambient_temperature\",\n      \"predicate\": \"regulates\",\n      \"object\"\
    : \"enzyme_kinetics\",\n      \"outcome\": \"UNKNOWN_EXACT_SCOPE\",\n      \"\
    assessment\": \"Tolner supplies thermophile enzyme-function context, not a direct\
    \ whole-cell-network temperature-scaling or optimum determination in the inspected\
    \ abstract. Detailed transport/host interventions are unassessed.\",\n      \"\
    source_locator\": \"tolner-metadata.json; abstract opening adaptation sentence\
    \ and supplied short phrase only\"\n    },\n    {\n      \"index\": 3,\n     \
    \ \"subject\": \"enzyme_kinetics\",\n      \"predicate\": \"promotes\",\n    \
    \  \"object\": \"maximal_growth_rate\",\n      \"outcome\": \"UNKNOWN_EXACT_SCOPE\"\
    ,\n      \"assessment\": \"Adaptation and enzyme turnover context do not independently\
    \ establish the asserted peak-growth causal link in inspected text. Unavailable\
    \ body is not a refutation.\",\n      \"source_locator\": \"tolner-metadata.json;\
    \ selected abstract context\"\n    },\n    {\n      \"index\": 4,\n      \"subject\"\
    : \"maximal_growth_rate\",\n      \"predicate\": \"manifests as\",\n      \"object\"\
    : \"temperature_optimum_trait\",\n      \"outcome\": \"UNKNOWN_NEAREST_SOURCE\"\
    ,\n      \"assessment\": \"The Tolner short supplied phrase is literal, but exact\
    \ rate-to-temperature-at-peak measurement semantics are not directly established\
    \ by this abstract. Formal endpoint semantics belong to grounding.\",\n      \"\
    source_locator\": \"tolner-metadata.json; supplied short phrase\"\n    },\n  \
    \  {\n      \"index\": 5,\n      \"subject\": \"homeoviscous_adaptation\",\n \
    \     \"predicate\": \"regulates\",\n      \"object\": \"membrane_fluidity\",\n\
    \      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT_WITH_QUOTATION_CONCERN\",\n  \
    \    \"assessment\": \"Ramón generic membrane-phase paragraph supports composition\
    \ changes maintaining physical state at low temperature. The note puts a paraphrase\
    \ in quotation marks; the supplied complete span is absent from the inspected\
    \ HTML. No biological falsity is inferred.\",\n      \"source_locator\": \"cold-pmc.html;\
    \ zero-based HTML <p> ordinal 17, selected first seven sentences; quoted-note-literal-check.json\"\
    \n    },\n    {\n      \"index\": 6,\n      \"subject\": \"membrane_fluidity\"\
    ,\n      \"predicate\": \"promotes\",\n      \"object\": \"maximal_growth_rate\"\
    ,\n      \"outcome\": \"UNKNOWN_EXACT_SCOPE\",\n      \"assessment\": \"Ramón\
    \ generic membrane functionality context is positive, but the specific peak-growth\
    \ proximal determinant and full transport/signaling/division formulation are not\
    \ directly established by the selected paragraph.\",\n      \"source_locator\"\
    : \"cold-pmc.html; selected generic paragraph 17\"\n    },\n    {\n      \"index\"\
    : 7,\n      \"subject\": \"arrhenius_plot_deviation\",\n      \"predicate\": \"\
    indicates\",\n      \"object\": \"stress_growth_regime\",\n      \"outcome\":\
    \ \"UNKNOWN_BODY_UNAVAILABLE\",\n      \"assessment\": \"Crossref confirms the\
    \ psychrophile review. Its abstract does not contain the quoted Arrhenius sentence;\
    \ two official PDF routes returned 403, so exact quotation and linearity-to-stress\
    \ interpretation remain unknown, not false.\",\n      \"source_locator\": \"arrhenius-crossref.json;\
    \ abstract and official link; actual PDF access receipts\"\n    }\n  ]\n}"
- assessment_id: scope-completeness
  area: scope
  topic: 'Native checklist: quantitative overview and biological limits'
  outcome: unknown
  target_ids:
  - METPO:1000304
  summary: Two components and zero protein classes/instances are compatible with the
    quantitative NONMECHANISTIC overview. No forced connector or token protein is
    required. Formal representation and literal checks do not establish detailed pathogen
    stress/survival/fitness/ROS/AMR/intervention efficacy, which remains UNASSESSED_SCOPE.
  evidence_ids:
  - record
  - policy
  - source-reading
  - expression
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: bounded catalog applicability'
  outcome: unknown
  target_ids:
  - METPO:1000304
  summary: Canonical species/type-strain aliases have no exact match in the retained
    20-organism / 28-dataset catalog. Broad source context and incidental E. coli/Bacillus
    host mentions do not justify exact-strain or detailed module transfer; source-species
    coverage is not globally absent.
  evidence_ids:
  - expression
  - source-reading
- assessment_id: recurrence
  area: consistency
  topic: 'Native checklist: current writers and historical conditions'
  outcome: supported
  target_ids:
  - METPO:1000304
  summary: Process-quality migration preserves the correct maximal-rate QUALITY, but
    its old enables-object branch would recreate promotes/RO2213; current promotes
    edges skip that branch. Shared grounders skip populated IDs. The homeoviscous
    normalizer targets siblings only. Composition facet and quoted-note corrections
    have record-only ownership.
  evidence_ids:
  - owners
  - owner-primary
  - writer-shape
  - discovery
  - predicate-mapping
  - adjudication
- assessment_id: human
  area: provenance
  topic: 'Native checklist: attributable current acceptance'
  outcome: concern
  target_ids:
  - METPO:1000304
  summary: Fifteen AI events plus a seed and the ignored-inclusive 282-path / 73-array
    search do not establish current human acceptance. Sixteen captured projections
    include ten current whole bodies and six byte-qualified prior readings; seven
    uncaptured histories remain matching-line context. Private/remote acceptance remains
    unknown.
  evidence_ids:
  - human-search
  - histories
  - owners
  - playbook
  - root-reading
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: checks and evidence chronology'
  outcome: supported
  target_ids:
  - METPO:1000304
  summary: All 97 captured inputs and frozen audits match. Three focused native checks
    passed. B13 qualified common diagnostics retain historical optional failures and
    123 no-adapter skips; no B14 fresh diagnostics or new B13 QC/publication claim
    is introduced. Acquisitions, copies and readings remain distinct.
  evidence_ids:
  - capture
  - reuse
  - reuse-postcheck
  - local-init
  - source-reuse
  - root-reading
findings:
- finding_id: imported-process-roles
  issue_key: temperature-optimum-imported-process-roles
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Imported relation roles conflict with current referents
  description: Six edges conflict with imported process roles. RO:0002211 requires
    process subjects and objects, and RO:0002213 inherits both constraints. Edges
    0/1/2 use an ambient-temperature condition or composition as subject; edges 0/1/5
    have an explicit fluidity-quality object; edges 3/6 have a maximal-growth-rate
    quality object and edge 6 also has a quality subject. The turnover-process reading
    of enzyme kinetics cannot repair the independently decisive other endpoints. This
    formal representation evidence is separate from biological causal efficacy.
  target_ids:
  - METPO:1000304
  field_paths:
  - causal_graphs[0].edges[0].predicate_id
  - causal_graphs[0].edges[1].predicate_id
  - causal_graphs[0].edges[2].predicate_id
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[5].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  evidence_ids:
  - nodes-edges
  - ro-primary
  - owners
  - owner-primary
  - predicate-mapping
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum.yaml
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_process_quality_consistency.py
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: composition-localization-facet
  issue_key: temperature-optimum-composition-localization-facet
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Composition and localization facets need clarification
  description: The label and description name lipid composition, while CELLULAR_LOCALIZATION
    denotes a component or location. A lipid mixture/component shorthand may be intended
    but is not explicit. Clarify that referent; the evidence does not justify prescribing
    one replacement type or chemical identity. This bounded facet issue is independent
    of the relation-role conflict.
  target_ids:
  - METPO:1000304
  field_paths:
  - causal_graphs[0].nodes[3].node_type
  evidence_ids:
  - nodes-edges
  - schema
  - owners
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum.yaml
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: nonverbatim-source-note
  issue_key: temperature-optimum-nonverbatim-source-note
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Quoted note differs from inspected primary wording
  description: The Ramon note encloses a paraphrase in quotation marks. The complete
    supplied span is absent from the retained primary HTML under exact and casefolded
    whitespace-normalized searches. The selected nearby generic membrane paragraph
    supports the concept with different wording. This is quotation precision, not
    biological refutation; all seven schema snippet fields remain literal positive
    controls.
  target_ids:
  - METPO:1000304
  field_paths:
  - causal_graphs[0].edges[5].evidence[0].notes
  evidence_ids:
  - notes
  - quote-check
  - cold-body
  - root-literal
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum.yaml
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-optimum-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Reviewed status lacks locally attributable acceptance
  description: Current REVIEWED status lacks attributable human acceptance of the
    present assertions in the inspected local evidence. The ignored- and hidden-inclusive
    search, excluding .git and .venv, found 282 matching paths and 73 actual review
    target arrays with no exact target. Sixteen embedded events comprise fifteen AI
    events and one seed; the one exact-target repository history has an AI actor.
    Private or remote acceptance remains unknown.
  target_ids:
  - METPO:1000304
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - human-search
  - histories
  - owners
  - playbook
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum.yaml
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: resolve-imported-process-roles
  description: In separately authorized curation, reconcile affected predicates with
    their actual condition, composition, process or quality referents. Preserve growth-rate
    QUALITY. Update the process-quality writer rationale and old-enables transform
    so historical inputs cannot recreate RO:0002213 on a quality object. Current promotes
    edges skip that transform; shared grounding skips populated IDs, so a rerun alone
    is not a current fix.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000304
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum.yaml
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_process_quality_consistency.py
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  acceptance_checks:
  - Demonstrate compatible actual endpoint roles without inventing mechanisms or numerical
    optima.
  - Retain unknown source calibration, the rate-versus-temperature distinction and
    NONMECHANISTIC scope; no required protein instances or component connectors.
  - Run focused strict validation, relevant graph/predicate audits, full QC and required
    curation history/product gates.
- action_id: resolve-composition-localization-facet
  description: Clarify whether the node denotes composition as an attribute or a specific
    material component, then reconcile its label, description and type. Do not guess
    a replacement grounding.
  finding_ids:
  - composition-localization-facet
  target_ids:
  - METPO:1000304
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum.yaml
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  acceptance_checks:
  - The stated referent fits the schema type and nearest source scope.
  - Do not retype merely to make an incompatible predicate appear valid; run native
    strict and graph checks after authorized curation.
- action_id: resolve-nonverbatim-source-note
  description: Mark the note as paraphrase or replace it with a short exact primary-source
    quotation with a precise locator. Preserve the generic evidence scope.
  finding_ids:
  - nonverbatim-source-note
  target_ids:
  - METPO:1000304
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum.yaml
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  acceptance_checks:
  - Quoted text is exact and interpretation is separate.
  - Retain the seven verified snippet results and keep the inaccessible Arrhenius
    quotation UNKNOWN unless adequate primary text is inspected.
  - Run focused snippet checking and native curation history/QC gates; document that
    native snippet verification does not check quoted note fields.
- action_id: resolve-human-acceptance-link
  description: Link attributable human acceptance of current assertions or reconcile
    REVIEWED through the native status workflow in separately authorized curation.
    Preserve existing actors.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000304
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum.yaml
    role: Current assertion or documented conditional recurrence; preserve recorded
      replay guards.
  acceptance_checks:
  - Human reviewer and accepted scope are attributable, or status accurately reflects
    available evidence.
  - Per-record and repository history validates and AI assistance remains explicit.
limitations:
- Overall source support is UNKNOWN for the definition-source calibration, precise
  optimum-setting interpretations and Arrhenius note. No unavailable-body absence
  or falsehood is inferred.
- Tolner author-repository HTML and indexed metadata expose abstract context, not
  a full primary body. Detailed transport/host intervention mechanisms incidentally
  present in the full abstract display were not adopted.
- Mendoza retained publisher browser export is an actual tool-response snapshot, not
  raw HTML or full article. Original browser/cache fetch time is not independently
  known; recorded tool-call bounds remain distinct from current copy/read times.
- Ramón complete retained PMC HTML was machine-searched for the one supplied quote,
  but scientific reading was confined to the generic membrane-phase paragraph and
  source identity. No full-article scientific audit is claimed.
- Arrhenius Europe PMC zero-hit JSON is retrieval context only. Positive Crossref
  identity/abstract is primary metadata. Both arrhenius-publisher.pdf and arrhenius-vor.pdf
  contain HTTP403 error bytes and are not article PDFs.
- Canonical Preprint-in metadata annotation is linkage, not a retraction/correction.
  Notice status is bounded to inspected response fields and selected publisher/author
  surfaces.
- Detailed dangerous pathogen stress/survival/fitness, ROS/defense, AMR and intervention
  efficacy remain UNASSESSED_SCOPE. No source audit action recommends a biological
  improvement.
- 'Catalog relevance is limited to named source contexts: canonical O. pelagia; selected
  generic Bacteria/Archaea context; Tolner also mentions E. coli as a historical host
  and two Bacillus species, without adopting detailed transport findings or exact
  strain/module coverage.'
- Edge4 dependent maximal-growth-rate value versus independent temperature-at-peak
  is qualified; broad local manifests-as endpoints do not establish a hard formal
  violation.
- Enzyme-kinetics process/rate nuance and observational Arrhenius factor wording remain
  qualified rather than forced extra findings.
- Formal role checks do not establish source operational-definition or joint-membrane/enzyme
  causal sufficiency. Detailed pathogen survival/fitness/ROS/AMR/intervention efficacy
  UNASSESSED_SCOPE.
- Seven uncaptured histories and two scripts are matching-line-only contexts, not
  whole-body authority.
- Retained catalog canonical absence does not imply all source organisms are absent.
- Private/remote human acceptance remains unknown.
- Root read one exact-target history whole and all sixteen actor/target/event projections;
  agent ten current whole and six qualified prior histories are separately attributed.
- A verified literal span is not proof of the adjacent exact optimum-setting causal
  interpretation.
- Original acquisition, current reuse and current reading times remain distinct.
- Actual browser responses are tool exports, not raw HTML; unknown origin/cache-fetch
  times are not invented. Original requests differ from current copies/readings.
- Qualified B12 QC is not new B13 QC or publication; historical optional failures/retries
  and 123 no-adapter skips remain explicit.
notes:
- Whole 271-line target, 97 captured inputs, five works, twelve external placements,
  ten grounding fields, nine nodes and eight edges reviewed.
- 'Sixteen current history projections: ten current whole bodies and six byte-qualified
  prior readings. Seven uncaptured histories and two scripts remain matching-line
  context.'
- One scratch serializer execution follows root FINAL and explicit permission; root
  owns actual YAML review, native validation and save.
tags:
- record-review
- temperature-optimum
- environment
- needs-curation
```
