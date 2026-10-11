# Bounded adversarial source-scope review of swimming motility

- Review: 20261011T182731Z-swimming-source-scope
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-11T18:27:29Z
- Finished UTC: 2026-10-11T18:27:31Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One bounded evidence-note defect confirmed and filed as issue1872. This intermediate observation does not certify the full record or publication gates.

## Scope And Provenance

Strain-background claim in the new record second evidence note.

Selection: One record and its source-scope claim; no sampling.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 029c3bc1383f541a11a1c8ceedf2bdb44998a206.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000702 | data/traits/morphology/swimming_motility.yaml | maintained | swimming motility |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Direct primary-source comparison | passed | True | traitmech:000702 | Main-text claim compared with actual Supplementary Figure11 and its caption. |

## Scientific And Domain Assessments

### Strain-background scope

evidence: concern. Targets: traitmech:000702.

The unqualified draft statement exceeds the complete inspected evidence.

## Findings

### strain-scope: Unqualified strain-background scope

minor / open / confirmed; issue key: swimming-lateral-flagellin-scope-1872.

The curator note overgeneralizes a main-text statement despite a conflicting supplementary experiment. Limit the assertion to the main comparison and retain the discrepancy; the liquid-swimming phenotype itself remains supported.

## Recommended Actions And Acceptance Checks

### repair

Attribute main-text scope, retain supplementary discrepancy, append provenance and regenerate.

- Guarded writer preserves previous curation history.
- Focused test requires the supplementary qualifier.
- New linked review reassesses corrected text and publication gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source | DOI:10.1038/s41467-018-07802-w; Main Results, Characterization of S. putrefaciens FlaA and FlaB; Supplementary Figure11, printed p7 / PDF p8, visually inspected. | refutes | Main text describes a lateral-flagellin-deletion background broadly, whereas Supplementary Figure11 reports an amino-acid-substitution assay retaining lateral flagellins. These source descriptions must be attributed rather than silently harmonized. |
| record | data/traits/morphology/swimming_motility.yaml; evidence[1].notes | supports | The draft generalizes the deletion background to all studied strains, without the supplementary exception. |

## Limits And Additional Notes

- Author self-review limited to one evidence-note claim; full QC, test suite and final artifact review remain pending.
- Snapshot reinspection time is recorded, not a fabricated fresh download time.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T182731Z-swimming-source-scope
kind: record
repository: CultureBotAI/TraitMech
title: Bounded adversarial source-scope review of swimming motility
started_at: '2026-10-11T18:27:29Z'
finished_at: '2026-10-11T18:27:31Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author source cross-check; not an independent review.
skill: .claude/skills/add-trait/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One bounded evidence-note defect confirmed and filed as issue1872. This intermediate
  observation does not certify the full record or publication gates.
source:
  git_revision: 029c3bc1383f541a11a1c8ceedf2bdb44998a206
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: 79196c04273f12305e4da6b842342e190cea45ec1e4f3e8b810fa3133226dfd3
    role: context
  - path: data/traits/morphology/swimming_motility.yaml
    sha256: b5a68c56a1eb61c2baa43d0f83368d02ccb27af6854fc38ba5454c79d06b915a
    role: target
  - path: docs/CURATION_PLAYBOOK.md
    sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
    role: context
  - path: docs/record-review-profile.md
    sha256: 37e37e274e9e884245948242a2b18cee202579ca1f740a7e44a72e0b4817012c
    role: context
  - path: proposals/metpo_traitmech_v578/proposal.md
    sha256: 0b57c3ec4f2dc91b4fc411b0bfeff0ff5278602f8d77cbf024a8ce782d735956
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_swimming_motility_trait.py
    sha256: 093c7d274535203dc88c55d2c75797e6399eb185244ca19e1eb0336556b3472a
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: tests/test_add_swimming_motility_trait.py
    sha256: da98135f28edcb48bf46a375319aa4cebbae176d919554ff62671ffca5f36e41
    role: context
targets:
- target_id: traitmech:000702
  path: data/traits/morphology/swimming_motility.yaml
  label: swimming motility
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/add_swimming_motility_trait.py
    role: guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/swimming_motility.yaml
    role: maintained trait record
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v578/metpo_proposal_classes_robot.tsv
    role: companion METPO proposal
scope:
  description: Strain-background claim in the new record second evidence note.
  selection: One record and its source-scope claim; no sampling.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - traitmech:000702
  exclusions:
  - target: Other traits and full publication gates
    reason: Not assessed by this bounded intermediate review.
checks:
- check_id: source-check
  name: Direct primary-source comparison
  status: passed
  required: true
  target_ids:
  - traitmech:000702
  evidence_ids:
  - source
  - record
  summary: Main-text claim compared with actual Supplementary Figure11 and its caption.
evidence:
- evidence_id: source
  kind: primary_source
  reference: DOI:10.1038/s41467-018-07802-w
  locator: Main Results, Characterization of S. putrefaciens FlaA and FlaB; Supplementary
    Figure11, printed p7 / PDF p8, visually inspected.
  accessed_at: '2026-10-11T18:27:31Z'
  support: refutes
  snapshot_sha256: c48254568659ad4deaba7b89b3dba740eee2ac1b4bf72d873f597489f7854ba5
  summary: Main text describes a lateral-flagellin-deletion background broadly, whereas
    Supplementary Figure11 reports an amino-acid-substitution assay retaining lateral
    flagellins. These source descriptions must be attributed rather than silently
    harmonized.
- evidence_id: record
  kind: record_content
  reference: data/traits/morphology/swimming_motility.yaml
  locator: evidence[1].notes
  accessed_at: '2026-10-11T18:27:31Z'
  support: supports
  summary: The draft generalizes the deletion background to all studied strains, without
    the supplementary exception.
assessments:
- assessment_id: scope
  area: evidence
  topic: Strain-background scope
  outcome: concern
  target_ids:
  - traitmech:000702
  evidence_ids:
  - source
  - record
  summary: The unqualified draft statement exceeds the complete inspected evidence.
findings:
- finding_id: strain-scope
  issue_key: swimming-lateral-flagellin-scope-1872
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Unqualified strain-background scope
  description: The curator note overgeneralizes a main-text statement despite a conflicting
    supplementary experiment. Limit the assertion to the main comparison and retain
    the discrepancy; the liquid-swimming phenotype itself remains supported.
  target_ids:
  - traitmech:000702
  field_paths:
  - evidence[1].notes
  evidence_ids:
  - source
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/add_swimming_motility_trait.py
    role: guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/swimming_motility.yaml
    role: maintained trait record
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/1872
actions:
- action_id: repair
  description: Attribute main-text scope, retain supplementary discrepancy, append
    provenance and regenerate.
  finding_ids:
  - strain-scope
  target_ids:
  - traitmech:000702
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/add_swimming_motility_trait.py
    role: guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/swimming_motility.yaml
    role: maintained trait record
  acceptance_checks:
  - Guarded writer preserves previous curation history.
  - Focused test requires the supplementary qualifier.
  - New linked review reassesses corrected text and publication gates.
limitations:
- Author self-review limited to one evidence-note claim; full QC, test suite and final
  artifact review remain pending.
- Snapshot reinspection time is recorded, not a fabricated fresh download time.
links:
- https://github.com/CultureBotAI/TraitMech/issues/1872
```
