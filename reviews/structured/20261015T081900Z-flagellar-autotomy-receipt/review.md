# Oversized flagellar-autotomy provenance receipt

- Review: 20261015T081900Z-flagellar-autotomy-receipt
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-15T08:15:49Z
- Finished UTC: 2026-10-15T08:19:00Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

One confirmed minor provenance-artifact defect; scientific claims are not adjudicated by this bounded observation.

## Scope And Provenance

Source-receipt size and content ownership for the one new trait.

Selection: Exact new trait and its source-verification receipt; no sampling.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 982e7239752041073343fad00e24fbd9474e4776.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000731 | data/traits/physiology/eukaryotic_flagellar_autotomy.yaml | maintained | eukaryotic flagellar autotomy |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Structured receipt inspection | passed | True | traitmech:000731 | Read byte length and parsed owners: 74366222 bytes and 184357 embedded owner objects. This confirms the defect, not acceptance. |

## Scientific And Domain Assessments

### Compact auditable source receipt

provenance: concern. Targets: traitmech:000731.

The receipt duplicates a 184357-owner search inventory and is 74 MB; retain count, scope and hash-linked complete local audit instead.

## Findings

### receipt-inventory: Complete temporary search inventory embedded in tracked summary

minor / open / confirmed; issue key: flagellar-autotomy-receipt-inventory.

74,366,222 bytes and 184,357 owner objects exceed the intended compact provenance summary. No change to biological claims is required. GitHub issue #1944 tracks this prepublication defect.

## Recommended Actions And Acceptance Checks

### compact-receipt

Replace owner objects with their count and hash-linked local audit receipt, preserving all evidence and limits.

- Receipt below 25000 bytes with owners count 184357, complete audit SHA-256 and unchanged source evidence.
- Capture corrected inputs and save a linked successor disposition; run final native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| receipt | research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json; allocation.full_range_check.owners and whole-file byte size | supports | The tracked summary embeds the complete temporary owner inventory instead of the intended count. |

## Limits And Additional Notes

- Author self-review of provenance shape only. Scientific evidence, full QC and merge readiness require the final assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T081900Z-flagellar-autotomy-receipt
kind: record
repository: CultureBotAI/TraitMech
title: Oversized flagellar-autotomy provenance receipt
started_at: '2026-10-15T08:15:49Z'
finished_at: '2026-10-15T08:19:00Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author prepublication review; not independent scientific approval.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: false
summary: One confirmed minor provenance-artifact defect; scientific claims are not
  adjudicated by this bounded observation.
source:
  git_revision: 982e7239752041073343fad00e24fbd9474e4776
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: a9cb4e5e6180e0cd7c62943174af5eb70d558eaa76901b004ac29ca9389f0d90
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
    role: context
  - path: .claude/skills/manage-identifiers/SKILL.md
    sha256: a5c5aaa10943ee6d15423a5878ed2189e4e0b28a5c6e09fda80ba299ab779ebb
    role: context
  - path: .claude/skills/metpo-proposal/SKILL.md
    sha256: 03f008c011e6f0d45cafb7516a01a3383c0a7e8d11bfc5c9cb31efaeca51275f
    role: context
  - path: .claude/skills/metpo-proposal/reference/conventions.md
    sha256: 8f0fb0093a8fad591148a4a72fcac4be3b44d0a1b5e96be5207ba817d07d6cd0
    role: context
  - path: CLAUDE.md
    sha256: 4d328127022388e1affe9b71be24bc93944a971636d0d0ea902f6511e0b405c5
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: README.md
    sha256: ad5edd82e7b3a0f52e76b6b6e31fb5ea97e0bf0503ad2936ae72572d1820beaf
    role: context
  - path: app/dashboard/priority.html
    sha256: ee56ea18f57639736c167fb6caee91308959124642c138ad0e5e3d2a0e133dc9
    role: context
  - path: app/dashboard/priority.json
    sha256: b9aa41fc676be48e11050005f44dc4241a105132407db9cf1e44a19fd374be0e
    role: context
  - path: app/discussions/data.js
    sha256: b9ad8687d3ab1e87d4a3861a005de24c94de4bf99cb1b99010f4e7baaf97cade
    role: context
  - path: app/discussions/index.html
    sha256: f9c315ab6577de4ac4153205d0edf7237ad1ddce769bdd983997f6d332c7850d
    role: context
  - path: app/discussions/theme-toggle.js
    sha256: 8b34063c7251d55e81f74da73bf8ac872f294bfab96acd7095036c7764af4f72
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: cbe5c82379e796446366b292f15194d80625b928119b482a67d857a379ab31a7
    role: context
  - path: conf/record_review.yaml
    sha256: 5adc6244761fb2baf8a059d81f23b0c9b32a33f9426ab84094234c3ec417269d
    role: context
  - path: dashboard/coverage.png
    sha256: 3e23fc5cae5d8b5e75fa071d79216037e6b253c3d0eb8b5a537a390fc223f59d
    role: context
  - path: dashboard/index.html
    sha256: 9b5cabae780d32de2e0da3839fac279ddc900b61e75951945cb9ce1b8613d06f
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
    sha256: e4d4924721768cd6c677b9cdc4781960a0526aa83537b182c7e9df1ba07f3bdc
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
  - path: docs/MERGE_QUEUE.md
    sha256: d3d88b6cb78d755f92e0f72898e75b70ac076cad110f729693fcb9661d27473e
    role: context
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: f795a191e17978454a8bb80da91ed6873a9405a240e6e5758837dd9bdc3b5c07
    role: context
  - path: history/records/eukaryotic_flagellar_autotomy/2026-10-15T080109Z-codex-566021.yaml
    sha256: 0424adcc0f610f47cad9a38d4c5fab405aff579128cdefcaaade57251c547fa5
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: b2ebd44cd55f74b8a3f0d3bed2112ef34dcfc04622d1a0134b8c04ce161d13e0
    role: context
  - path: pages/traits/physiology/eukaryotic_flagellar_autotomy.html
    sha256: d513461af2068cf5f784b79953ff94d7a6de1cbcc93dcdfcb9ec80b8bab58804
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 3fd9e9ea9d0aeaf750dcac81c76b96bbefccee246115a570250224ab63c8285b
    role: context
  - path: proposals/metpo_traitmech_v606/metpo_proposal_classes_robot.tsv
    sha256: 8ed5281bf51e818afa9a78b24582122b1b67cf85e26cc9e95ab5a6e3ea044609
    role: context
  - path: proposals/metpo_traitmech_v607/metpo_proposal_classes_robot.tsv
    sha256: 72af61de0c6d741f00271b48d1656ee47c313fbde38ce953b6cfb81c7a76aae3
    role: context
  - path: proposals/metpo_traitmech_v607/proposal.md
    sha256: 161e52bf8f19987ff2af6e0340e8c303c49816be10adac942e1cbb2525624436
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 59166077243db5e7b686a61842df9613c66771a3f8eda81d9bc713a95e6c8864
    role: context
  - path: research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json
    sha256: c5723db8e742214810ac74f056a9bfa5401b7e75d167cecb08024bacf31158f4
    role: context
  - path: scripts/add_eukaryotic_flagellar_autotomy_trait.py
    sha256: 9fdb337d58a05bc540b59f3a2b3a70df9a857f58dfe8b879155d35b189da58ae
    role: context
  - path: scripts/verify_snippets.py
    sha256: e235ef0a80ba564f929b8255e80ef1265bfdd016f74c627bcb7e7b86e033ddcc
    role: context
  - path: src/traitmech/curate/curation_event.py
    sha256: d9b3e70539bbf13f9130544e18ed7664ff2c3b7c60bcc2cae5185663fe25badd
    role: context
  - path: src/traitmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
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
  - path: tests/test_add_eukaryotic_flagellar_autotomy_trait.py
    sha256: e3cb6e2065b962708044617e8bda01d083048383a72dddce04cf0d3c39abbad2
    role: context
targets:
- target_id: traitmech:000731
  path: data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
  label: eukaryotic flagellar autotomy
  kind: maintained
  record_class: TraitRecord
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
    role: curated_record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_eukaryotic_flagellar_autotomy_trait.py
    role: guarded_writer
scope:
  description: Source-receipt size and content ownership for the one new trait.
  selection: Exact new trait and its source-verification receipt; no sampling.
  population_size: 1
  coverage: partial
  reviewed_target_ids:
  - traitmech:000731
  exclusions:
  - target: Scientific adjudication and complete merge readiness
    reason: Separate final source-based review and full gates are pending.
checks:
- check_id: size-and-content
  name: Structured receipt inspection
  status: passed
  required: true
  target_ids:
  - traitmech:000731
  summary: 'Read byte length and parsed owners: 74366222 bytes and 184357 embedded
    owner objects. This confirms the defect, not acceptance.'
evidence:
- evidence_id: receipt
  kind: record_content
  reference: research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json
  locator: allocation.full_range_check.owners and whole-file byte size
  accessed_at: '2026-10-15T08:19:00Z'
  support: supports
  snapshot_sha256: c5723db8e742214810ac74f056a9bfa5401b7e75d167cecb08024bacf31158f4
  summary: The tracked summary embeds the complete temporary owner inventory instead
    of the intended count.
assessments:
- assessment_id: receipt-size
  area: provenance
  topic: Compact auditable source receipt
  outcome: concern
  target_ids:
  - traitmech:000731
  evidence_ids:
  - receipt
  summary: The receipt duplicates a 184357-owner search inventory and is 74 MB; retain
    count, scope and hash-linked complete local audit instead.
findings:
- finding_id: receipt-inventory
  issue_key: flagellar-autotomy-receipt-inventory
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - traitmech:000731
  field_paths:
  - allocation.full_range_check.owners
  evidence_ids:
  - receipt
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json
    role: maintained_source_receipt
  title: Complete temporary search inventory embedded in tracked summary
  description: '74,366,222 bytes and 184,357 owner objects exceed the intended compact
    provenance summary. No change to biological claims is required. GitHub issue #1944
    tracks this prepublication defect.'
actions:
- action_id: compact-receipt
  description: Replace owner objects with their count and hash-linked local audit
    receipt, preserving all evidence and limits.
  finding_ids:
  - receipt-inventory
  target_ids:
  - traitmech:000731
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json
    role: maintained_source_receipt
  acceptance_checks:
  - Receipt below 25000 bytes with owners count 184357, complete audit SHA-256 and
    unchanged source evidence.
  - Capture corrected inputs and save a linked successor disposition; run final native
    gates.
limitations:
- Author self-review of provenance shape only. Scientific evidence, full QC and merge
  readiness require the final assessment.
links:
- https://github.com/CultureBotAI/TraitMech/issues/1944
```
