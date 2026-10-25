# Cycle 4 Stage 5 post-remediation verification review of the 18 TraitRecord files in group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS

- Review: 20261025T130000Z-cycle4-stage5-remediated-records-review
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-25T12:55:00Z
- Finished UTC: 2026-10-25T13:00:00Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Fresh post-remediation batch review of the 18 TraitRecord YAML files remediated in Cycle 4 Stage 5 across ecology (habitat_association.yaml), environment (neutrophilic.yaml), metabolism (reductive_tca_cycle.yaml), morphology (cell_shape.yaml, flagellar_arrangement.yaml, orange_pigmented.yaml, spirochete_shaped.yaml), physiology (chemolithoautotrophic.yaml), and genomics (gao_her_system.yaml, gao_hhe_system.yaml, gao_iet_system.yaml, gao_mza_system.yaml, gao_ppl_system.yaml, gao_qat_system.yaml, gao_rl_system.yaml, gao_tery_system.yaml, gao_tmn_system.yaml, gao_upx_system.yaml) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002. All 18 Cycle 4 Stage 4 open findings (F-C4S4-DEF-SRC-001..018) are verified as resolved with contiguous verbatim snippets from their primary definition_source in record-level evidence[0], append-only curation_history provenance, and 0 remaining open findings.

## Scope And Provenance

Focused post-remediation review of all 18 TraitRecord YAML files modified in Cycle 4 Stage 5 (resolve_review_findings) to resolve group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002).

Selection: All 18 records with open findings carried forward from Cycle 4 Stage 4 review 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review.
Coverage: full; 18 reviewed / 18 in the declared population.
Source: working_tree at Git base eb6d17c7e248633240ec49bf3b8529f4f82cc81f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000047 | data/traits/ecology/habitat_association.yaml | maintained | habitat association |
| METPO:1003001 | data/traits/environment/neutrophilic.yaml | maintained | neutrophilic |
| traitmech:000021 | data/traits/metabolism/reductive_tca_cycle.yaml | maintained | reductive tricarboxylic acid cycle |
| METPO:1000666 | data/traits/morphology/cell_shape.yaml | maintained | cell shape |
| traitmech:000056 | data/traits/morphology/flagellar_arrangement.yaml | maintained | flagellar arrangement |
| METPO:1003026 | data/traits/morphology/orange_pigmented.yaml | maintained | orange pigmented |
| METPO:1000693 | data/traits/morphology/spirochete_shaped.yaml | maintained | spirochete shaped |
| METPO:1000637 | data/traits/physiology/chemolithoautotrophic.yaml | maintained | chemolithoautotrophic |
| traitmech:000409 | data/traits/genomics/gao_her_system.yaml | maintained | Gao-Her system |
| traitmech:000353 | data/traits/genomics/gao_hhe_system.yaml | maintained | Gao-Hhe system |
| traitmech:000354 | data/traits/genomics/gao_iet_system.yaml | maintained | Gao-Iet system |
| traitmech:000355 | data/traits/genomics/gao_mza_system.yaml | maintained | Gao-Mza system |
| traitmech:000356 | data/traits/genomics/gao_ppl_system.yaml | maintained | Gao-Ppl system |
| traitmech:000359 | data/traits/genomics/gao_qat_system.yaml | maintained | Gao-Qat system |
| traitmech:000352 | data/traits/genomics/gao_rl_system.yaml | maintained | Gao-RL system |
| traitmech:000360 | data/traits/genomics/gao_tery_system.yaml | maintained | Gao-TerY system |
| traitmech:000357 | data/traits/genomics/gao_tmn_system.yaml | maintained | Gao-Tmn system |
| traitmech:000358 | data/traits/genomics/gao_upx_system.yaml | maintained | Gao-Upx system |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict LinkML schema and reference validation across all TraitRecord files | passed | True | traitmech:000047, METPO:1003001, traitmech:000021, METPO:1000666, traitmech:000056, METPO:1003026, METPO:1000693, METPO:1000637, traitmech:000409, traitmech:000353, traitmech:000354, traitmech:000355, traitmech:000356, traitmech:000359, traitmech:000352, traitmech:000360, traitmech:000357, traitmech:000358 | All 1,130 TraitRecord YAML files (including all 18 Cycle 4 Stage 5 remediated records) pass strict closed-mode LinkML validation with 0 errors. |
| Evidence snippet structural and baseline ratchet audit | passed | True | traitmech:000047, METPO:1003001, traitmech:000021, METPO:1000666, traitmech:000056, METPO:1003026, METPO:1000693, METPO:1000637, traitmech:000409, traitmech:000353, traitmech:000354, traitmech:000355, traitmech:000356, traitmech:000359, traitmech:000352, traitmech:000360, traitmech:000357, traitmech:000358 | All 18 remediated records now carry a contiguous &gt;=12-char verbatim quote for their primary definition_source in record-level evidence[0], passing scripts/audit_evidence_snippets.py with 0 new findings and reducing MISSING_SNIPPET from 2,254 to 2,251, ELLIPTICAL_SNIPPET from 57 to 52, UNQUOTED_DEFINITION_SOURCE from 102 to 94, and MISSING_DEFINITION_SOURCE_EVIDENCE from 69 to 59. |
| Stage 5 guarded writer idempotency and postcondition unit tests | passed | True | traitmech:000047, METPO:1003001, traitmech:000021, METPO:1000666, traitmech:000056, METPO:1003026, METPO:1000693, METPO:1000637, traitmech:000409, traitmech:000353, traitmech:000354, traitmech:000355, traitmech:000356, traitmech:000359, traitmech:000352, traitmech:000360, traitmech:000357, traitmech:000358 | All 5 unit tests in tests/test_curate_stage5_review_findings.py pass, confirming DO_NOT_WORK protection, exact definition_source evidence alignment across all 45 remediated specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4), zero UNQUOTED_DEFINITION_SOURCE or MISSING_DEFINITION_SOURCE_EVIDENCE defects on remediated records, and dry-run/apply idempotency. |
| Guarded YAML writer safeguard audit | passed | True | traitmech:000047, METPO:1003001, traitmech:000021, METPO:1000666, traitmech:000056, METPO:1003026, METPO:1000693, METPO:1000637, traitmech:000409, traitmech:000353, traitmech:000354, traitmech:000355, traitmech:000356, traitmech:000359, traitmech:000352, traitmech:000360, traitmech:000357, traitmech:000358 | scripts/curate_stage5_review_findings.py satisfies all writer safeguards (appends curation_history, has write safeguard, validates before write, wired into justfile). |

## Scientific And Domain Assessments

### Verification of record-level definition_source evidence[0] verbatim snippets across the 18 remediated records

evidence: supported. Targets: traitmech:000047, METPO:1003001, traitmech:000021, METPO:1000666, traitmech:000056, METPO:1003026, METPO:1000693, METPO:1000637, traitmech:000409, traitmech:000353, traitmech:000354, traitmech:000355, traitmech:000356, traitmech:000359, traitmech:000352, traitmech:000360, traitmech:000357, traitmech:000358.

All 18 records identified with open findings in Cycle 4 Stage 4 (habitat_association.yaml, neutrophilic.yaml, reductive_tca_cycle.yaml, cell_shape.yaml, flagellar_arrangement.yaml, orange_pigmented.yaml, spirochete_shaped.yaml, chemolithoautotrophic.yaml, and the 10 Gao-* defense system records gao_{her,hhe,iet,mza,ppl,qat,rl,tery,tmn,upx}_system.yaml) now carry a verified non-elliptical verbatim snippet for their primary definition_source directly in record-level evidence[0].

Each of the 18 remediated records was re-inspected against .claude/skills/review-yaml-record/SKILL.md: (1) F-C4S4-DEF-SRC-001..008 (habitat_association.yaml, neutrophilic.yaml, reductive_tca_cycle.yaml, cell_shape.yaml, flagellar_arrangement.yaml, orange_pigmented.yaml, spirochete_shaped.yaml, chemolithoautotrophic.yaml) now quote their declared definition_source with a contiguous non-elliptical verbatim snippet in evidence[0] promoted from intra-record causal_graphs[0].edges[*] or linked parent/child/sibling TraitRecords; and (2) F-C4S4-DEF-SRC-009..018 (gao_her_system.yaml, gao_hhe_system.yaml, gao_iet_system.yaml, gao_mza_system.yaml, gao_ppl_system.yaml, gao_qat_system.yaml, gao_rl_system.yaml, gao_tery_system.yaml, gao_tmn_system.yaml, gao_upx_system.yaml) now align evidence[0].reference with definition_source DOI:10.1126/science.aba0372 (from PMID alias PMID:32855333) while preserving the verified verbatim abstract snippet from Gao et al. 2020 (Science).

### Schema validity, curation_history provenance, and writer guardrails on remediated records

provenance: supported. Targets: traitmech:000047, METPO:1003001, traitmech:000021, METPO:1000666, traitmech:000056, METPO:1003026, METPO:1000693, METPO:1000637, traitmech:000409, traitmech:000353, traitmech:000354, traitmech:000355, traitmech:000356, traitmech:000359, traitmech:000352, traitmech:000360, traitmech:000357, traitmech:000358.

All 18 remediated records pass strict closed-mode LinkML validation, preserve existing canonical_examples, causal_graphs, and UniProtKB protein_examples untouched, and record append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history entries referencing issue #2002.

## Findings

### F-C4S4-DEF-SRC-001: habitat_association.yaml now includes a verified verbatim snippet for definition_source DOI:10.1038/nrmicro1341 in record-level evidence[0]

minor / resolved / confirmed; issue key: habitat-association-definition-source-snippet.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-001 on data/traits/ecology/habitat_association.yaml (traitmech:000047): aligned/promoted verified verbatim snippet ('free-living microbial taxa') from child data/traits/ecology/free_living.yaml (traitmech:000048) evidence[0] to record-level evidence[0] for definition_source DOI:10.1038/nrmicro1341 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-002: neutrophilic.yaml now includes a verified verbatim snippet for definition_source DOI:10.1038/nrmicro2549 in record-level evidence[0]

minor / resolved / confirmed; issue key: neutrophilic-definition-source-snippet.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-002 on data/traits/environment/neutrophilic.yaml (METPO:1003001): aligned/promoted verified verbatim snippet ('external pH values outside the cytoplasmic pH') from causal_graphs[0].edges[0].evidence[0] on the same record (near_neutral_external_ph -&gt; neutrophilic_trait) to record-level evidence[0] for definition_source DOI:10.1038/nrmicro2549 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-003: reductive_tca_cycle.yaml now includes a verified verbatim snippet for definition_source DOI:10.1128/AEM.02473-10 in record-level evidence[0]

minor / resolved / confirmed; issue key: reductive-tca-cycle-definition-source-snippet.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-003 on data/traits/metabolism/reductive_tca_cycle.yaml (traitmech:000021): aligned/promoted verified verbatim snippet ('the second autotrophic CO2 fixation cycle (the reductive citric acid cycle) had been discovered') from parent data/traits/metabolism/carbon_fixation.yaml (traitmech:000019) causal_graphs[0].edges[12].evidence[0] (rtca_cycle -&gt; carbon_fixation_process) to record-level evidence[0] for definition_source DOI:10.1128/AEM.02473-10 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-004: cell_shape.yaml now includes a verified verbatim snippet for definition_source DOI:10.1038/nrmicro1205 in record-level evidence[0]

minor / resolved / confirmed; issue key: cell-shape-definition-source-snippet.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-004 on data/traits/morphology/cell_shape.yaml (METPO:1000666): aligned/promoted verified verbatim snippet ('primary role in maintaining cell shape') from causal_graphs[0].edges[0].evidence[0] on the same record (peptidoglycan_cell_wall -&gt; cell_shape_trait) to record-level evidence[0] for definition_source DOI:10.1038/nrmicro1205 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-005: flagellar_arrangement.yaml now includes a verified verbatim snippet for definition_source DOI:10.1093/femsre/fuv034 in record-level evidence[0]

minor / resolved / confirmed; issue key: flagellar-arrangement-definition-source-snippet.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-005 on data/traits/morphology/flagellar_arrangement.yaml (traitmech:000056): aligned/promoted verified verbatim snippet ('Bacteria differ in number and location of their flagella that appear in regular patterns at the cell surface (flagellation pattern).') from child data/traits/morphology/polar_flagellation.yaml (METPO:1005032), amphitrichous.yaml (traitmech:000059), lophotrichous.yaml (traitmech:000058), and monotrichous.yaml (traitmech:000057) evidence[0] to record-level evidence[0] for definition_source DOI:10.1093/femsre/fuv034 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-006: orange_pigmented.yaml now includes a verified verbatim snippet for definition_source DOI:10.1080/1040841X.2025.2526423 in record-level evidence[0]

minor / resolved / confirmed; issue key: orange-pigmented-definition-source-snippet.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-006 on data/traits/morphology/orange_pigmented.yaml (METPO:1003026): aligned/promoted verified verbatim snippet ('red, pink, orange, and yellow pigmentation in bacteria') from parent data/traits/morphology/carotenoid_pigmentation.yaml (traitmech:000116) and siblings pink_pigmented.yaml (METPO:1003027) and yellow_pigmented.yaml (METPO:1003029) evidence[0] to record-level evidence[0] for definition_source DOI:10.1080/1040841X.2025.2526423 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-007: spirochete_shaped.yaml now includes a verified verbatim snippet for definition_source DOI:10.1073/pnas.200221797 in record-level evidence[0]

minor / resolved / confirmed; issue key: spirochete-shaped-definition-source-snippet.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-007 on data/traits/morphology/spirochete_shaped.yaml (METPO:1000693): aligned/promoted verified verbatim snippet ('cell morphology is either a helix, a flat wave, or an irregularly shaped helix') from causal_graphs[0].edges[3].evidence[0] on the same record (flat_wave_morphology -&gt; spirochete_shaped_trait) to record-level evidence[0] for definition_source DOI:10.1073/pnas.200221797 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-008: chemolithoautotrophic.yaml now includes a verified verbatim snippet for definition_source DOI:10.1146/annurev.micro.52.1.191 in record-level evidence[0]

minor / resolved / confirmed; issue key: chemolithoautotrophic-definition-source-snippet.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-008 on data/traits/physiology/chemolithoautotrophic.yaml (METPO:1000637): aligned/promoted verified verbatim snippet ('Carbon Dioxide Fixation in Chemoautotrophs') from causal_graphs[0].edges[5].evidence[0] on the same record (carbon_dioxide -&gt; co2_fixation_pathway) and parent chemoautotrophic.yaml (METPO:1000626) evidence[0] to record-level evidence[0] for definition_source DOI:10.1146/annurev.micro.52.1.191 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-009: gao_her_system.yaml now includes a verified verbatim snippet for definition_source DOI:10.1126/science.aba0372 in record-level evidence[0]

minor / resolved / confirmed; issue key: gao-her-system-definition-source-curie-alignment.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-009 on data/traits/genomics/gao_her_system.yaml (traitmech:000409): aligned/promoted verified verbatim snippet ('By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages.') from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-010: gao_hhe_system.yaml now includes a verified verbatim snippet for definition_source DOI:10.1126/science.aba0372 in record-level evidence[0]

minor / resolved / confirmed; issue key: gao-hhe-system-definition-source-curie-alignment.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-010 on data/traits/genomics/gao_hhe_system.yaml (traitmech:000353): aligned/promoted verified verbatim snippet ('By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages.') from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-011: gao_iet_system.yaml now includes a verified verbatim snippet for definition_source DOI:10.1126/science.aba0372 in record-level evidence[0]

minor / resolved / confirmed; issue key: gao-iet-system-definition-source-curie-alignment.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-011 on data/traits/genomics/gao_iet_system.yaml (traitmech:000354): aligned/promoted verified verbatim snippet ('By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages.') from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-012: gao_mza_system.yaml now includes a verified verbatim snippet for definition_source DOI:10.1126/science.aba0372 in record-level evidence[0]

minor / resolved / confirmed; issue key: gao-mza-system-definition-source-curie-alignment.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-012 on data/traits/genomics/gao_mza_system.yaml (traitmech:000355): aligned/promoted verified verbatim snippet ('By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages.') from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-013: gao_ppl_system.yaml now includes a verified verbatim snippet for definition_source DOI:10.1126/science.aba0372 in record-level evidence[0]

minor / resolved / confirmed; issue key: gao-ppl-system-definition-source-curie-alignment.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-013 on data/traits/genomics/gao_ppl_system.yaml (traitmech:000356): aligned/promoted verified verbatim snippet ('By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages.') from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-014: gao_qat_system.yaml now includes a verified verbatim snippet for definition_source DOI:10.1126/science.aba0372 in record-level evidence[0]

minor / resolved / confirmed; issue key: gao-qat-system-definition-source-curie-alignment.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-014 on data/traits/genomics/gao_qat_system.yaml (traitmech:000359): aligned/promoted verified verbatim snippet ('By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages.') from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-015: gao_rl_system.yaml now includes a verified verbatim snippet for definition_source DOI:10.1126/science.aba0372 in record-level evidence[0]

minor / resolved / confirmed; issue key: gao-rl-system-definition-source-curie-alignment.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-015 on data/traits/genomics/gao_rl_system.yaml (traitmech:000352): aligned/promoted verified verbatim snippet ('By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages.') from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-016: gao_tery_system.yaml now includes a verified verbatim snippet for definition_source DOI:10.1126/science.aba0372 in record-level evidence[0]

minor / resolved / confirmed; issue key: gao-tery-system-definition-source-curie-alignment.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-016 on data/traits/genomics/gao_tery_system.yaml (traitmech:000360): aligned/promoted verified verbatim snippet ('By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages.') from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-017: gao_tmn_system.yaml now includes a verified verbatim snippet for definition_source DOI:10.1126/science.aba0372 in record-level evidence[0]

minor / resolved / confirmed; issue key: gao-tmn-system-definition-source-curie-alignment.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-017 on data/traits/genomics/gao_tmn_system.yaml (traitmech:000357): aligned/promoted verified verbatim snippet ('By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages.') from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C4S4-DEF-SRC-018: gao_upx_system.yaml now includes a verified verbatim snippet for definition_source DOI:10.1126/science.aba0372 in record-level evidence[0]

minor / resolved / confirmed; issue key: gao-upx-system-definition-source-curie-alignment.

Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-018 on data/traits/genomics/gao_upx_system.yaml (traitmech:000358): aligned/promoted verified verbatim snippet ('By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages.') from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372 and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 4 Stage 5 (resolve_review_findings) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-prior-c4s4-review | reviews/structured/20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review/review.yaml; findings[0..17] | supports | Immutable Cycle 4 Stage 4 review bundle identifying the 18 open definition_source evidence snippet / CURIE alignment findings (F-C4S4-DEF-SRC-001..F-C4S4-DEF-SRC-018) with planned remediation actions ACT-C4S4-DEF-SRC-001..018. |
| ev-c4s5-def-src-001 | DOI:10.1038/nrmicro1341; Promoted/aligned on evidence[0] from child data/traits/ecology/free_living.yaml (traitmech:000048) evidence[0] | supports | Primary definition_source DOI:10.1038/nrmicro1341 verified via existing verbatim quote in child data/traits/ecology/free_living.yaml (traitmech:000048) evidence[0] and populated/aligned in record-level evidence[0]. |
| ev-c4s5-def-src-002 | DOI:10.1038/nrmicro2549; Promoted/aligned on evidence[0] from causal_graphs[0].edges[0].evidence[0] on the same record (near_neutral_external_ph -&gt; neutrophilic_trait) | supports | Primary definition_source DOI:10.1038/nrmicro2549 verified via existing verbatim quote in causal_graphs[0].edges[0].evidence[0] on the same record (near_neutral_external_ph -&gt; neutrophilic_trait) and populated/aligned in record-level evidence[0]. |
| ev-c4s5-def-src-003 | DOI:10.1128/AEM.02473-10; Promoted/aligned on evidence[0] from parent data/traits/metabolism/carbon_fixation.yaml (traitmech:000019) causal_graphs[0].edges[12].evidence[0] (rtca_cycle -&gt; carbon_fixation_process) | supports | Primary definition_source DOI:10.1128/AEM.02473-10 verified via existing verbatim quote in parent data/traits/metabolism/carbon_fixation.yaml (traitmech:000019) causal_graphs[0].edges[12].evidence[0] (rtca_cycle -&gt; carbon_fixation_process) and populated/aligned in record-level evidence[0]. |
| ev-c4s5-def-src-004 | DOI:10.1038/nrmicro1205; Promoted/aligned on evidence[0] from causal_graphs[0].edges[0].evidence[0] on the same record (peptidoglycan_cell_wall -&gt; cell_shape_trait) | supports | Primary definition_source DOI:10.1038/nrmicro1205 verified via existing verbatim quote in causal_graphs[0].edges[0].evidence[0] on the same record (peptidoglycan_cell_wall -&gt; cell_shape_trait) and populated/aligned in record-level evidence[0]. |
| ev-c4s5-def-src-005 | DOI:10.1093/femsre/fuv034; Promoted/aligned on evidence[0] from child data/traits/morphology/polar_flagellation.yaml (METPO:1005032), amphitrichous.yaml (traitmech:000059), lophotrichous.yaml (traitmech:000058), and monotrichous.yaml (traitmech:000057) evidence[0] | supports | Primary definition_source DOI:10.1093/femsre/fuv034 verified via existing verbatim quote in child data/traits/morphology/polar_flagellation.yaml (METPO:1005032), amphitrichous.yaml (traitmech:000059), lophotrichous.yaml (traitmech:000058), and monotrichous.yaml (traitmech:000057) evidence[0] and populated/aligned in record-level evidence[0]. |
| ev-c4s5-def-src-006 | DOI:10.1080/1040841X.2025.2526423; Promoted/aligned on evidence[0] from parent data/traits/morphology/carotenoid_pigmentation.yaml (traitmech:000116) and siblings pink_pigmented.yaml (METPO:1003027) and yellow_pigmented.yaml (METPO:1003029) evidence[0] | supports | Primary definition_source DOI:10.1080/1040841X.2025.2526423 verified via existing verbatim quote in parent data/traits/morphology/carotenoid_pigmentation.yaml (traitmech:000116) and siblings pink_pigmented.yaml (METPO:1003027) and yellow_pigmented.yaml (METPO:1003029) evidence[0] and populated/aligned in record-level evidence[0]. |
| ev-c4s5-def-src-007 | DOI:10.1073/pnas.200221797; Promoted/aligned on evidence[0] from causal_graphs[0].edges[3].evidence[0] on the same record (flat_wave_morphology -&gt; spirochete_shaped_trait) | supports | Primary definition_source DOI:10.1073/pnas.200221797 verified via existing verbatim quote in causal_graphs[0].edges[3].evidence[0] on the same record (flat_wave_morphology -&gt; spirochete_shaped_trait) and populated/aligned in record-level evidence[0]. |
| ev-c4s5-def-src-008 | DOI:10.1146/annurev.micro.52.1.191; Promoted/aligned on evidence[0] from causal_graphs[0].edges[5].evidence[0] on the same record (carbon_dioxide -&gt; co2_fixation_pathway) and parent chemoautotrophic.yaml (METPO:1000626) evidence[0] | supports | Primary definition_source DOI:10.1146/annurev.micro.52.1.191 verified via existing verbatim quote in causal_graphs[0].edges[5].evidence[0] on the same record (carbon_dioxide -&gt; co2_fixation_pathway) and parent chemoautotrophic.yaml (METPO:1000626) evidence[0] and populated/aligned in record-level evidence[0]. |
| ev-c4s5-def-src-009 | DOI:10.1126/science.aba0372; Promoted/aligned on evidence[0] from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] | supports | Primary definition_source DOI:10.1126/science.aba0372 verified via existing verbatim quote in record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0] and populated/aligned in record-level evidence[0]. |
| ev-remediated-records | data/traits/ecology/habitat_association.yaml; data/traits/environment/neutrophilic.yaml; data/traits/metabolism/reductive_tca_cycle.yaml; data/traits/morphology/cell_shape.yaml; data/traits/morphology/flagellar_arrangement.yaml; data/traits/morphology/orange_pigmented.yaml; data/traits/morphology/spirochete_shaped.yaml; data/traits/physiology/chemolithoautotrophic.yaml; data/traits/genomics/gao_her_system.yaml; data/traits/genomics/gao_hhe_system.yaml; data/traits/genomics/gao_iet_system.yaml; data/traits/genomics/gao_mza_system.yaml; data/traits/genomics/gao_ppl_system.yaml; data/traits/genomics/gao_qat_system.yaml; data/traits/genomics/gao_rl_system.yaml; data/traits/genomics/gao_tery_system.yaml; data/traits/genomics/gao_tmn_system.yaml; data/traits/genomics/gao_upx_system.yaml; definition_source, evidence[0], curation_history | supports | All 18 remediated TraitRecord YAML files now include a verified non-elliptical verbatim snippet for their declared definition_source in record-level evidence[0] and an append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event. |
| ev-stage5-writer | scripts/curate_stage5_review_findings.py; tests/test_curate_stage5_review_findings.py; process_all | supports | Guarded writer script and unit test suite verifying closed-mode LinkML validation, DO_NOT_WORK exclusion, and idempotent remediation across all 45 target specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4). |
| ev-validate-strict | scripts/validate_strict.py; reports/instance_validation_failures.tsv | supports | Closed-mode LinkML schema and identifier validation passes with 0 errors across all 1,130 TraitRecord files. |
| ev-snippet-audit | scripts/audit_evidence_snippets.py; conf/evidence_snippet_baseline.tsv | supports | All 18 remediated record-level evidence[0] entries pass contiguous verbatim quote checks with 0 new warnings and eliminate all 18 open definition_source findings from Cycle 4 Stage 4. |

## Limits And Additional Notes

- This batch review covers the 18 records remediated in Cycle 4 Stage 5 under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002); the 5 cohort-level source-limited or upstream-blocked findings from Cycle 4 Stage 4 remain tracked under open GitHub issues #1982, #1983, #1984, #1985, and #364.
- 13 of the 18 remediated records carry repository-minted traitmech:NNNNNN identifiers backed by validated ROBOT templates awaiting upstream METPO release incorporation (#364, berkeleybop/metpo#535); the remaining 5 records carry active METPO: identifiers (METPO:1003001, METPO:1000666, METPO:1003026, METPO:1000693, METPO:1000637).
- Skills executed: .claude/skills/curate-yaml-record/SKILL.md and .claude/skills/review-yaml-record/SKILL.md.
- Immutable Cycle 4 Stage 4 review bundle preserved untouched at reviews/structured/20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review/review.yaml.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T130000Z-cycle4-stage5-remediated-records-review
kind: batch
repository: CultureBotAI/TraitMech
title: Cycle 4 Stage 5 post-remediation verification review of the 18 TraitRecord
  files in group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
started_at: '2026-10-25T12:55:00Z'
finished_at: '2026-10-25T13:00:00Z'
reviewer:
  identity: antigravity
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Repository-local post-remediation record review verifying resolution
    of the 18 Cycle 4 Stage 4 open findings (F-C4S4-DEF-SRC-001..F-C4S4-DEF-SRC-018)
    under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002); separate from
    independent PR adversarial review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Fresh post-remediation batch review of the 18 TraitRecord YAML files remediated
  in Cycle 4 Stage 5 across ecology (habitat_association.yaml), environment (neutrophilic.yaml),
  metabolism (reductive_tca_cycle.yaml), morphology (cell_shape.yaml, flagellar_arrangement.yaml,
  orange_pigmented.yaml, spirochete_shaped.yaml), physiology (chemolithoautotrophic.yaml),
  and genomics (gao_her_system.yaml, gao_hhe_system.yaml, gao_iet_system.yaml, gao_mza_system.yaml,
  gao_ppl_system.yaml, gao_qat_system.yaml, gao_rl_system.yaml, gao_tery_system.yaml,
  gao_tmn_system.yaml, gao_upx_system.yaml) under group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
  and GitHub issue #2002. All 18 Cycle 4 Stage 4 open findings (F-C4S4-DEF-SRC-001..018)
  are verified as resolved with contiguous verbatim snippets from their primary definition_source
  in record-level evidence[0], append-only curation_history provenance, and 0 remaining
  open findings.'
source:
  git_revision: eb6d17c7e248633240ec49bf3b8529f4f82cc81f
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: 27f535d3f057d321c8b87c6506f2f35dd2d37fd005bcd5040b3e17269285075b
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
  - path: conf/record_review.yaml
    sha256: 5adc6244761fb2baf8a059d81f23b0c9b32a33f9426ab84094234c3ec417269d
    role: context
  - path: data/traits/ecology/habitat_association.yaml
    sha256: 6c4ad53b8aa891b286f220b46c32c475af3902898ef7f2e60fb4500b4a178e2b
    role: target
  - path: data/traits/environment/neutrophilic.yaml
    sha256: 37d9ec732f032629e3508fa01a414a2e4eda61c6cd354ace747a82e1de6d41c7
    role: target
  - path: data/traits/genomics/gao_her_system.yaml
    sha256: 8dd4a4427e9f7b56f42a00dbfa7afa393fe3ec88481aaa430a30ae7d8ae13de1
    role: target
  - path: data/traits/genomics/gao_hhe_system.yaml
    sha256: 07dc8a8550e6bce77346d29d4f3ef2f985fd96bdcbb1693b5e88551f8b94f26e
    role: target
  - path: data/traits/genomics/gao_iet_system.yaml
    sha256: 6d7d08dc6f109d48485c28a9bb95cacc5d4287257d17186de1d0712804d6218c
    role: target
  - path: data/traits/genomics/gao_mza_system.yaml
    sha256: 1d6c57417d3cda51899c780e115f234efcee2fa649db4383f0a0e1d59d86ca92
    role: target
  - path: data/traits/genomics/gao_ppl_system.yaml
    sha256: 8d5a5325bdeb216bdcf6953a01f542e9219d3718c5a2934b6ba41d4b07169b77
    role: target
  - path: data/traits/genomics/gao_qat_system.yaml
    sha256: e30291b69baaa9077e02b1e0c25cdae34f6eddabd705792862309074394b9e4b
    role: target
  - path: data/traits/genomics/gao_rl_system.yaml
    sha256: 752a0ddbdbbe0f5b45c5b7c3af8c10fda720458b41a65a21aa6c717c15704553
    role: target
  - path: data/traits/genomics/gao_tery_system.yaml
    sha256: a2c09c6957d93327f709df84286c7ec8a99b0128909e566e6325cb4e3dd65435
    role: target
  - path: data/traits/genomics/gao_tmn_system.yaml
    sha256: 8fa1e1ceaca47fd4779509ff7bfd6f9cadee3636003ddf73baf1c4885cb8a241
    role: target
  - path: data/traits/genomics/gao_upx_system.yaml
    sha256: 7f8489a9153d49c02affcd30faac061db08ccd21cd9709feba2acee56522283b
    role: target
  - path: data/traits/metabolism/reductive_tca_cycle.yaml
    sha256: 625990eee2d87d012ad83cb413cc8704e0b7e18a32bdb5e4dfcd25d632b262e6
    role: target
  - path: data/traits/morphology/cell_shape.yaml
    sha256: 066e3a824510b3a7813423d13d8e4c32d3607b9369346ac3517d844fd16c8b0e
    role: target
  - path: data/traits/morphology/flagellar_arrangement.yaml
    sha256: fe99189f2585c43987741ae0c25ccb966c1f04bdb4df504ac8017e0ae6776758
    role: target
  - path: data/traits/morphology/orange_pigmented.yaml
    sha256: d4afc1189e331c2cb0a805ced8dd60355672b355d5a794c39bbb0bc27fbbd16e
    role: target
  - path: data/traits/morphology/spirochete_shaped.yaml
    sha256: 148fa028a9ff72253bf52311bad0150b78a9cc1f11d884cfb34d0ca0eea96710
    role: target
  - path: data/traits/physiology/chemolithoautotrophic.yaml
    sha256: 5ec906c105bdadc314f0af92525d71fc03263f5abba0d0b57fa3deb2869308b4
    role: target
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/infrastructure/curate_stage5_review_findings/2026-10-25T125500Z-claude-code-c4s501.yaml
    sha256: 1070875ffebc0de7f01f66176ad293ff6de1b4c52ea29f4f847a8b6c42ca554c
    role: context
  - path: reviews/structured/20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review/review.yaml
    sha256: 60af7ae02bedcfd3c03619781b662ea7ed172be00b41bb1bac67dde07ec168d5
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml
    sha256: 77587f0d4a85d9f82f21f338d1253096f6c34047375ba925d9c441341f0dddbd
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/curate_stage5_review_findings.py
    sha256: 985e5c2a85d2300b7045fdec0013a194de68ed26345f59dbb85844cf0ca445b2
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: tests/test_curate_stage5_review_findings.py
    sha256: 6a2b59fa3912a463f8c701fa638e6db37c7d032767fef48fd661a5c1dbc1a005
    role: context
scope:
  description: Focused post-remediation review of all 18 TraitRecord YAML files modified
    in Cycle 4 Stage 5 (resolve_review_findings) to resolve group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    (#2002).
  selection: All 18 records with open findings carried forward from Cycle 4 Stage
    4 review 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review.
  coverage: full
  population_size: 18
  reviewed_target_ids:
  - traitmech:000047
  - METPO:1003001
  - traitmech:000021
  - METPO:1000666
  - traitmech:000056
  - METPO:1003026
  - METPO:1000693
  - METPO:1000637
  - traitmech:000409
  - traitmech:000353
  - traitmech:000354
  - traitmech:000355
  - traitmech:000356
  - traitmech:000359
  - traitmech:000352
  - traitmech:000360
  - traitmech:000357
  - traitmech:000358
targets:
- target_id: traitmech:000047
  path: data/traits/ecology/habitat_association.yaml
  label: habitat association
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/habitat_association.yaml
    role: maintained TraitRecord YAML
- target_id: METPO:1003001
  path: data/traits/environment/neutrophilic.yaml
  label: neutrophilic
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/neutrophilic.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000021
  path: data/traits/metabolism/reductive_tca_cycle.yaml
  label: reductive tricarboxylic acid cycle
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/metabolism/reductive_tca_cycle.yaml
    role: maintained TraitRecord YAML
- target_id: METPO:1000666
  path: data/traits/morphology/cell_shape.yaml
  label: cell shape
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/cell_shape.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000056
  path: data/traits/morphology/flagellar_arrangement.yaml
  label: flagellar arrangement
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/flagellar_arrangement.yaml
    role: maintained TraitRecord YAML
- target_id: METPO:1003026
  path: data/traits/morphology/orange_pigmented.yaml
  label: orange pigmented
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/orange_pigmented.yaml
    role: maintained TraitRecord YAML
- target_id: METPO:1000693
  path: data/traits/morphology/spirochete_shaped.yaml
  label: spirochete shaped
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/spirochete_shaped.yaml
    role: maintained TraitRecord YAML
- target_id: METPO:1000637
  path: data/traits/physiology/chemolithoautotrophic.yaml
  label: chemolithoautotrophic
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/chemolithoautotrophic.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000409
  path: data/traits/genomics/gao_her_system.yaml
  label: Gao-Her system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_her_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000353
  path: data/traits/genomics/gao_hhe_system.yaml
  label: Gao-Hhe system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_hhe_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000354
  path: data/traits/genomics/gao_iet_system.yaml
  label: Gao-Iet system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_iet_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000355
  path: data/traits/genomics/gao_mza_system.yaml
  label: Gao-Mza system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_mza_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000356
  path: data/traits/genomics/gao_ppl_system.yaml
  label: Gao-Ppl system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_ppl_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000359
  path: data/traits/genomics/gao_qat_system.yaml
  label: Gao-Qat system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_qat_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000352
  path: data/traits/genomics/gao_rl_system.yaml
  label: Gao-RL system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_rl_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000360
  path: data/traits/genomics/gao_tery_system.yaml
  label: Gao-TerY system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_tery_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000357
  path: data/traits/genomics/gao_tmn_system.yaml
  label: Gao-Tmn system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_tmn_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000358
  path: data/traits/genomics/gao_upx_system.yaml
  label: Gao-Upx system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_upx_system.yaml
    role: maintained TraitRecord YAML
checks:
- check_id: validate-strict
  name: Strict LinkML schema and reference validation across all TraitRecord files
  command: uv run python scripts/validate_strict.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000047
  - METPO:1003001
  - traitmech:000021
  - METPO:1000666
  - traitmech:000056
  - METPO:1003026
  - METPO:1000693
  - METPO:1000637
  - traitmech:000409
  - traitmech:000353
  - traitmech:000354
  - traitmech:000355
  - traitmech:000356
  - traitmech:000359
  - traitmech:000352
  - traitmech:000360
  - traitmech:000357
  - traitmech:000358
  evidence_ids:
  - ev-validate-strict
  - ev-remediated-records
  summary: All 1,130 TraitRecord YAML files (including all 18 Cycle 4 Stage 5 remediated
    records) pass strict closed-mode LinkML validation with 0 errors.
- check_id: audit-snippets
  name: Evidence snippet structural and baseline ratchet audit
  command: uv run python scripts/audit_evidence_snippets.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000047
  - METPO:1003001
  - traitmech:000021
  - METPO:1000666
  - traitmech:000056
  - METPO:1003026
  - METPO:1000693
  - METPO:1000637
  - traitmech:000409
  - traitmech:000353
  - traitmech:000354
  - traitmech:000355
  - traitmech:000356
  - traitmech:000359
  - traitmech:000352
  - traitmech:000360
  - traitmech:000357
  - traitmech:000358
  evidence_ids:
  - ev-snippet-audit
  - ev-c4s5-def-src-001
  - ev-c4s5-def-src-002
  - ev-c4s5-def-src-003
  - ev-c4s5-def-src-004
  - ev-c4s5-def-src-005
  - ev-c4s5-def-src-006
  - ev-c4s5-def-src-007
  - ev-c4s5-def-src-008
  - ev-c4s5-def-src-009
  summary: All 18 remediated records now carry a contiguous >=12-char verbatim quote
    for their primary definition_source in record-level evidence[0], passing scripts/audit_evidence_snippets.py
    with 0 new findings and reducing MISSING_SNIPPET from 2,254 to 2,251, ELLIPTICAL_SNIPPET
    from 57 to 52, UNQUOTED_DEFINITION_SOURCE from 102 to 94, and MISSING_DEFINITION_SOURCE_EVIDENCE
    from 69 to 59.
- check_id: stage5-writer-tests
  name: Stage 5 guarded writer idempotency and postcondition unit tests
  command: uv run pytest tests/test_curate_stage5_review_findings.py -v
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000047
  - METPO:1003001
  - traitmech:000021
  - METPO:1000666
  - traitmech:000056
  - METPO:1003026
  - METPO:1000693
  - METPO:1000637
  - traitmech:000409
  - traitmech:000353
  - traitmech:000354
  - traitmech:000355
  - traitmech:000356
  - traitmech:000359
  - traitmech:000352
  - traitmech:000360
  - traitmech:000357
  - traitmech:000358
  evidence_ids:
  - ev-stage5-writer
  summary: All 5 unit tests in tests/test_curate_stage5_review_findings.py pass, confirming
    DO_NOT_WORK protection, exact definition_source evidence alignment across all
    45 remediated specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4), zero UNQUOTED_DEFINITION_SOURCE
    or MISSING_DEFINITION_SOURCE_EVIDENCE defects on remediated records, and dry-run/apply
    idempotency.
- check_id: audit-writers
  name: Guarded YAML writer safeguard audit
  command: uv run python scripts/audit_writers.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000047
  - METPO:1003001
  - traitmech:000021
  - METPO:1000666
  - traitmech:000056
  - METPO:1003026
  - METPO:1000693
  - METPO:1000637
  - traitmech:000409
  - traitmech:000353
  - traitmech:000354
  - traitmech:000355
  - traitmech:000356
  - traitmech:000359
  - traitmech:000352
  - traitmech:000360
  - traitmech:000357
  - traitmech:000358
  evidence_ids:
  - ev-stage5-writer
  summary: scripts/curate_stage5_review_findings.py satisfies all writer safeguards
    (appends curation_history, has write safeguard, validates before write, wired
    into justfile).
evidence:
- evidence_id: ev-prior-c4s4-review
  kind: prior_review
  reference: reviews/structured/20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review/review.yaml
  locator: findings[0..17]
  accessed_at: '2026-10-25T12:55:00Z'
  support: supports
  summary: Immutable Cycle 4 Stage 4 review bundle identifying the 18 open definition_source
    evidence snippet / CURIE alignment findings (F-C4S4-DEF-SRC-001..F-C4S4-DEF-SRC-018)
    with planned remediation actions ACT-C4S4-DEF-SRC-001..018.
  snapshot_sha256: 60af7ae02bedcfd3c03619781b662ea7ed172be00b41bb1bac67dde07ec168d5
- evidence_id: ev-c4s5-def-src-001
  kind: primary_source
  reference: DOI:10.1038/nrmicro1341
  locator: Promoted/aligned on evidence[0] from child data/traits/ecology/free_living.yaml
    (traitmech:000048) evidence[0]
  accessed_at: '2026-10-25T12:56:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/nrmicro1341 verified via existing
    verbatim quote in child data/traits/ecology/free_living.yaml (traitmech:000048)
    evidence[0] and populated/aligned in record-level evidence[0].
  quote: free-living microbial taxa
- evidence_id: ev-c4s5-def-src-002
  kind: primary_source
  reference: DOI:10.1038/nrmicro2549
  locator: Promoted/aligned on evidence[0] from causal_graphs[0].edges[0].evidence[0]
    on the same record (near_neutral_external_ph -> neutrophilic_trait)
  accessed_at: '2026-10-25T12:56:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/nrmicro2549 verified via existing
    verbatim quote in causal_graphs[0].edges[0].evidence[0] on the same record (near_neutral_external_ph
    -> neutrophilic_trait) and populated/aligned in record-level evidence[0].
  quote: external pH values outside the cytoplasmic pH
- evidence_id: ev-c4s5-def-src-003
  kind: primary_source
  reference: DOI:10.1128/AEM.02473-10
  locator: Promoted/aligned on evidence[0] from parent data/traits/metabolism/carbon_fixation.yaml
    (traitmech:000019) causal_graphs[0].edges[12].evidence[0] (rtca_cycle -> carbon_fixation_process)
  accessed_at: '2026-10-25T12:56:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1128/AEM.02473-10 verified via existing
    verbatim quote in parent data/traits/metabolism/carbon_fixation.yaml (traitmech:000019)
    causal_graphs[0].edges[12].evidence[0] (rtca_cycle -> carbon_fixation_process)
    and populated/aligned in record-level evidence[0].
  quote: the second autotrophic CO2 fixation cycle (the reductive citric acid cycle)
    had been discovered
- evidence_id: ev-c4s5-def-src-004
  kind: primary_source
  reference: DOI:10.1038/nrmicro1205
  locator: Promoted/aligned on evidence[0] from causal_graphs[0].edges[0].evidence[0]
    on the same record (peptidoglycan_cell_wall -> cell_shape_trait)
  accessed_at: '2026-10-25T12:56:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/nrmicro1205 verified via existing
    verbatim quote in causal_graphs[0].edges[0].evidence[0] on the same record (peptidoglycan_cell_wall
    -> cell_shape_trait) and populated/aligned in record-level evidence[0].
  quote: primary role in maintaining cell shape
- evidence_id: ev-c4s5-def-src-005
  kind: primary_source
  reference: DOI:10.1093/femsre/fuv034
  locator: Promoted/aligned on evidence[0] from child data/traits/morphology/polar_flagellation.yaml
    (METPO:1005032), amphitrichous.yaml (traitmech:000059), lophotrichous.yaml (traitmech:000058),
    and monotrichous.yaml (traitmech:000057) evidence[0]
  accessed_at: '2026-10-25T12:56:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1093/femsre/fuv034 verified via existing
    verbatim quote in child data/traits/morphology/polar_flagellation.yaml (METPO:1005032),
    amphitrichous.yaml (traitmech:000059), lophotrichous.yaml (traitmech:000058),
    and monotrichous.yaml (traitmech:000057) evidence[0] and populated/aligned in
    record-level evidence[0].
  quote: Bacteria differ in number and location of their flagella that appear in regular
    patterns at the cell surface (flagellation pattern).
- evidence_id: ev-c4s5-def-src-006
  kind: primary_source
  reference: DOI:10.1080/1040841X.2025.2526423
  locator: Promoted/aligned on evidence[0] from parent data/traits/morphology/carotenoid_pigmentation.yaml
    (traitmech:000116) and siblings pink_pigmented.yaml (METPO:1003027) and yellow_pigmented.yaml
    (METPO:1003029) evidence[0]
  accessed_at: '2026-10-25T12:56:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1080/1040841X.2025.2526423 verified via
    existing verbatim quote in parent data/traits/morphology/carotenoid_pigmentation.yaml
    (traitmech:000116) and siblings pink_pigmented.yaml (METPO:1003027) and yellow_pigmented.yaml
    (METPO:1003029) evidence[0] and populated/aligned in record-level evidence[0].
  quote: red, pink, orange, and yellow pigmentation in bacteria
- evidence_id: ev-c4s5-def-src-007
  kind: primary_source
  reference: DOI:10.1073/pnas.200221797
  locator: Promoted/aligned on evidence[0] from causal_graphs[0].edges[3].evidence[0]
    on the same record (flat_wave_morphology -> spirochete_shaped_trait)
  accessed_at: '2026-10-25T12:56:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1073/pnas.200221797 verified via existing
    verbatim quote in causal_graphs[0].edges[3].evidence[0] on the same record (flat_wave_morphology
    -> spirochete_shaped_trait) and populated/aligned in record-level evidence[0].
  quote: cell morphology is either a helix, a flat wave, or an irregularly shaped
    helix
- evidence_id: ev-c4s5-def-src-008
  kind: primary_source
  reference: DOI:10.1146/annurev.micro.52.1.191
  locator: Promoted/aligned on evidence[0] from causal_graphs[0].edges[5].evidence[0]
    on the same record (carbon_dioxide -> co2_fixation_pathway) and parent chemoautotrophic.yaml
    (METPO:1000626) evidence[0]
  accessed_at: '2026-10-25T12:56:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1146/annurev.micro.52.1.191 verified via
    existing verbatim quote in causal_graphs[0].edges[5].evidence[0] on the same record
    (carbon_dioxide -> co2_fixation_pathway) and parent chemoautotrophic.yaml (METPO:1000626)
    evidence[0] and populated/aligned in record-level evidence[0].
  quote: Carbon Dioxide Fixation in Chemoautotrophs
- evidence_id: ev-c4s5-def-src-009
  kind: primary_source
  reference: DOI:10.1126/science.aba0372
  locator: Promoted/aligned on evidence[0] from record-level evidence[0] on the same
    record (cited under PMID alias PMID:32855333) and sibling avast_system.yaml /
    drt_system.yaml / dsr_system.yaml evidence[0]
  accessed_at: '2026-10-25T12:56:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1126/science.aba0372 verified via existing
    verbatim quote in record-level evidence[0] on the same record (cited under PMID
    alias PMID:32855333) and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml
    evidence[0] and populated/aligned in record-level evidence[0].
  quote: By systematic defense gene prediction and heterologous reconstitution, here
    we discover 29 widespread antiviral gene cassettes, collectively present in 32%
    of all sequenced bacterial and archaeal genomes, that mediate protection against
    specific bacteriophages.
- evidence_id: ev-remediated-records
  kind: record_content
  reference: data/traits/ecology/habitat_association.yaml; data/traits/environment/neutrophilic.yaml;
    data/traits/metabolism/reductive_tca_cycle.yaml; data/traits/morphology/cell_shape.yaml;
    data/traits/morphology/flagellar_arrangement.yaml; data/traits/morphology/orange_pigmented.yaml;
    data/traits/morphology/spirochete_shaped.yaml; data/traits/physiology/chemolithoautotrophic.yaml;
    data/traits/genomics/gao_her_system.yaml; data/traits/genomics/gao_hhe_system.yaml;
    data/traits/genomics/gao_iet_system.yaml; data/traits/genomics/gao_mza_system.yaml;
    data/traits/genomics/gao_ppl_system.yaml; data/traits/genomics/gao_qat_system.yaml;
    data/traits/genomics/gao_rl_system.yaml; data/traits/genomics/gao_tery_system.yaml;
    data/traits/genomics/gao_tmn_system.yaml; data/traits/genomics/gao_upx_system.yaml
  locator: definition_source, evidence[0], curation_history
  accessed_at: '2026-10-25T12:57:00Z'
  support: supports
  summary: All 18 remediated TraitRecord YAML files now include a verified non-elliptical
    verbatim snippet for their declared definition_source in record-level evidence[0]
    and an append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history
    event.
- evidence_id: ev-stage5-writer
  kind: validation
  reference: scripts/curate_stage5_review_findings.py; tests/test_curate_stage5_review_findings.py
  locator: process_all
  accessed_at: '2026-10-25T12:58:00Z'
  support: supports
  summary: Guarded writer script and unit test suite verifying closed-mode LinkML
    validation, DO_NOT_WORK exclusion, and idempotent remediation across all 45 target
    specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4).
  snapshot_sha256: 985e5c2a85d2300b7045fdec0013a194de68ed26345f59dbb85844cf0ca445b2
- evidence_id: ev-validate-strict
  kind: validation
  reference: scripts/validate_strict.py
  locator: reports/instance_validation_failures.tsv
  accessed_at: '2026-10-25T12:59:00Z'
  support: supports
  summary: Closed-mode LinkML schema and identifier validation passes with 0 errors
    across all 1,130 TraitRecord files.
- evidence_id: ev-snippet-audit
  kind: validation
  reference: scripts/audit_evidence_snippets.py
  locator: conf/evidence_snippet_baseline.tsv
  accessed_at: '2026-10-25T12:59:00Z'
  support: supports
  summary: All 18 remediated record-level evidence[0] entries pass contiguous verbatim
    quote checks with 0 new warnings and eliminate all 18 open definition_source findings
    from Cycle 4 Stage 4.
assessments:
- assessment_id: assess-remediated-evidence-alignment
  area: evidence
  topic: Verification of record-level definition_source evidence[0] verbatim snippets
    across the 18 remediated records
  outcome: supported
  summary: All 18 records identified with open findings in Cycle 4 Stage 4 (habitat_association.yaml,
    neutrophilic.yaml, reductive_tca_cycle.yaml, cell_shape.yaml, flagellar_arrangement.yaml,
    orange_pigmented.yaml, spirochete_shaped.yaml, chemolithoautotrophic.yaml, and
    the 10 Gao-* defense system records gao_{her,hhe,iet,mza,ppl,qat,rl,tery,tmn,upx}_system.yaml)
    now carry a verified non-elliptical verbatim snippet for their primary definition_source
    directly in record-level evidence[0].
  target_ids:
  - traitmech:000047
  - METPO:1003001
  - traitmech:000021
  - METPO:1000666
  - traitmech:000056
  - METPO:1003026
  - METPO:1000693
  - METPO:1000637
  - traitmech:000409
  - traitmech:000353
  - traitmech:000354
  - traitmech:000355
  - traitmech:000356
  - traitmech:000359
  - traitmech:000352
  - traitmech:000360
  - traitmech:000357
  - traitmech:000358
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-001
  - ev-c4s5-def-src-002
  - ev-c4s5-def-src-003
  - ev-c4s5-def-src-004
  - ev-c4s5-def-src-005
  - ev-c4s5-def-src-006
  - ev-c4s5-def-src-007
  - ev-c4s5-def-src-008
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-snippet-audit
  metrics:
  - name: remediated_open_findings_rate
    value: 1.0
    unit: ratio
    definition: Fraction of Cycle 4 Stage 4 open findings in group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
      verified as resolved with verbatim definition_source evidence.
    denominator: 18
    minimum: 0.0
    maximum: 1.0
  details: 'Each of the 18 remediated records was re-inspected against .claude/skills/review-yaml-record/SKILL.md:
    (1) F-C4S4-DEF-SRC-001..008 (habitat_association.yaml, neutrophilic.yaml, reductive_tca_cycle.yaml,
    cell_shape.yaml, flagellar_arrangement.yaml, orange_pigmented.yaml, spirochete_shaped.yaml,
    chemolithoautotrophic.yaml) now quote their declared definition_source with a
    contiguous non-elliptical verbatim snippet in evidence[0] promoted from intra-record
    causal_graphs[0].edges[*] or linked parent/child/sibling TraitRecords; and (2)
    F-C4S4-DEF-SRC-009..018 (gao_her_system.yaml, gao_hhe_system.yaml, gao_iet_system.yaml,
    gao_mza_system.yaml, gao_ppl_system.yaml, gao_qat_system.yaml, gao_rl_system.yaml,
    gao_tery_system.yaml, gao_tmn_system.yaml, gao_upx_system.yaml) now align evidence[0].reference
    with definition_source DOI:10.1126/science.aba0372 (from PMID alias PMID:32855333)
    while preserving the verified verbatim abstract snippet from Gao et al. 2020 (Science).'
- assessment_id: assess-remediated-schema-and-provenance
  area: provenance
  topic: Schema validity, curation_history provenance, and writer guardrails on remediated
    records
  outcome: supported
  summary: 'All 18 remediated records pass strict closed-mode LinkML validation, preserve
    existing canonical_examples, causal_graphs, and UniProtKB protein_examples untouched,
    and record append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history
    entries referencing issue #2002.'
  target_ids:
  - traitmech:000047
  - METPO:1003001
  - traitmech:000021
  - METPO:1000666
  - traitmech:000056
  - METPO:1003026
  - METPO:1000693
  - METPO:1000637
  - traitmech:000409
  - traitmech:000353
  - traitmech:000354
  - traitmech:000355
  - traitmech:000356
  - traitmech:000359
  - traitmech:000352
  - traitmech:000360
  - traitmech:000357
  - traitmech:000358
  evidence_ids:
  - ev-remediated-records
  - ev-stage5-writer
  - ev-validate-strict
findings:
- finding_id: F-C4S4-DEF-SRC-001
  issue_key: habitat-association-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: habitat_association.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1038/nrmicro1341 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-001 on data/traits/ecology/habitat_association.yaml
    (traitmech:000047): aligned/promoted verified verbatim snippet (''free-living
    microbial taxa'') from child data/traits/ecology/free_living.yaml (traitmech:000048)
    evidence[0] to record-level evidence[0] for definition_source DOI:10.1038/nrmicro1341
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000047
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-001
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/habitat_association.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-001
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-002
  issue_key: neutrophilic-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: neutrophilic.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1038/nrmicro2549 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-002 on data/traits/environment/neutrophilic.yaml
    (METPO:1003001): aligned/promoted verified verbatim snippet (''external pH values
    outside the cytoplasmic pH'') from causal_graphs[0].edges[0].evidence[0] on the
    same record (near_neutral_external_ph -> neutrophilic_trait) to record-level evidence[0]
    for definition_source DOI:10.1038/nrmicro2549 and appended curation_history entry
    via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - METPO:1003001
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-002
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/neutrophilic.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-002
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-003
  issue_key: reductive-tca-cycle-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: reductive_tca_cycle.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1128/AEM.02473-10 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-003 on data/traits/metabolism/reductive_tca_cycle.yaml
    (traitmech:000021): aligned/promoted verified verbatim snippet (''the second autotrophic
    CO2 fixation cycle (the reductive citric acid cycle) had been discovered'') from
    parent data/traits/metabolism/carbon_fixation.yaml (traitmech:000019) causal_graphs[0].edges[12].evidence[0]
    (rtca_cycle -> carbon_fixation_process) to record-level evidence[0] for definition_source
    DOI:10.1128/AEM.02473-10 and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000021
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-003
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/metabolism/reductive_tca_cycle.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-003
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-004
  issue_key: cell-shape-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: cell_shape.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1038/nrmicro1205 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-004 on data/traits/morphology/cell_shape.yaml
    (METPO:1000666): aligned/promoted verified verbatim snippet (''primary role in
    maintaining cell shape'') from causal_graphs[0].edges[0].evidence[0] on the same
    record (peptidoglycan_cell_wall -> cell_shape_trait) to record-level evidence[0]
    for definition_source DOI:10.1038/nrmicro1205 and appended curation_history entry
    via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - METPO:1000666
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-004
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/cell_shape.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-004
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-005
  issue_key: flagellar-arrangement-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: flagellar_arrangement.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1093/femsre/fuv034 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-005 on data/traits/morphology/flagellar_arrangement.yaml
    (traitmech:000056): aligned/promoted verified verbatim snippet (''Bacteria differ
    in number and location of their flagella that appear in regular patterns at the
    cell surface (flagellation pattern).'') from child data/traits/morphology/polar_flagellation.yaml
    (METPO:1005032), amphitrichous.yaml (traitmech:000059), lophotrichous.yaml (traitmech:000058),
    and monotrichous.yaml (traitmech:000057) evidence[0] to record-level evidence[0]
    for definition_source DOI:10.1093/femsre/fuv034 and appended curation_history
    entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000056
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-005
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/flagellar_arrangement.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-005
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-006
  issue_key: orange-pigmented-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: orange_pigmented.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1080/1040841X.2025.2526423 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-006 on data/traits/morphology/orange_pigmented.yaml
    (METPO:1003026): aligned/promoted verified verbatim snippet (''red, pink, orange,
    and yellow pigmentation in bacteria'') from parent data/traits/morphology/carotenoid_pigmentation.yaml
    (traitmech:000116) and siblings pink_pigmented.yaml (METPO:1003027) and yellow_pigmented.yaml
    (METPO:1003029) evidence[0] to record-level evidence[0] for definition_source
    DOI:10.1080/1040841X.2025.2526423 and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - METPO:1003026
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-006
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/orange_pigmented.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-006
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-007
  issue_key: spirochete-shaped-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: spirochete_shaped.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1073/pnas.200221797 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-007 on data/traits/morphology/spirochete_shaped.yaml
    (METPO:1000693): aligned/promoted verified verbatim snippet (''cell morphology
    is either a helix, a flat wave, or an irregularly shaped helix'') from causal_graphs[0].edges[3].evidence[0]
    on the same record (flat_wave_morphology -> spirochete_shaped_trait) to record-level
    evidence[0] for definition_source DOI:10.1073/pnas.200221797 and appended curation_history
    entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - METPO:1000693
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-007
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/spirochete_shaped.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-007
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-008
  issue_key: chemolithoautotrophic-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: chemolithoautotrophic.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1146/annurev.micro.52.1.191 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-008 on data/traits/physiology/chemolithoautotrophic.yaml
    (METPO:1000637): aligned/promoted verified verbatim snippet (''Carbon Dioxide
    Fixation in Chemoautotrophs'') from causal_graphs[0].edges[5].evidence[0] on the
    same record (carbon_dioxide -> co2_fixation_pathway) and parent chemoautotrophic.yaml
    (METPO:1000626) evidence[0] to record-level evidence[0] for definition_source
    DOI:10.1146/annurev.micro.52.1.191 and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - METPO:1000637
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-008
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/chemolithoautotrophic.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-008
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-009
  issue_key: gao-her-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gao_her_system.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1126/science.aba0372 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-009 on data/traits/genomics/gao_her_system.yaml
    (traitmech:000409): aligned/promoted verified verbatim snippet (''By systematic
    defense gene prediction and heterologous reconstitution, here we discover 29 widespread
    antiviral gene cassettes, collectively present in 32% of all sequenced bacterial
    and archaeal genomes, that mediate protection against specific bacteriophages.'')
    from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333)
    and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0]
    to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000409
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_her_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-009
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-010
  issue_key: gao-hhe-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gao_hhe_system.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1126/science.aba0372 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-010 on data/traits/genomics/gao_hhe_system.yaml
    (traitmech:000353): aligned/promoted verified verbatim snippet (''By systematic
    defense gene prediction and heterologous reconstitution, here we discover 29 widespread
    antiviral gene cassettes, collectively present in 32% of all sequenced bacterial
    and archaeal genomes, that mediate protection against specific bacteriophages.'')
    from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333)
    and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0]
    to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000353
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_hhe_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-010
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-011
  issue_key: gao-iet-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gao_iet_system.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1126/science.aba0372 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-011 on data/traits/genomics/gao_iet_system.yaml
    (traitmech:000354): aligned/promoted verified verbatim snippet (''By systematic
    defense gene prediction and heterologous reconstitution, here we discover 29 widespread
    antiviral gene cassettes, collectively present in 32% of all sequenced bacterial
    and archaeal genomes, that mediate protection against specific bacteriophages.'')
    from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333)
    and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0]
    to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000354
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_iet_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-011
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-012
  issue_key: gao-mza-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gao_mza_system.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1126/science.aba0372 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-012 on data/traits/genomics/gao_mza_system.yaml
    (traitmech:000355): aligned/promoted verified verbatim snippet (''By systematic
    defense gene prediction and heterologous reconstitution, here we discover 29 widespread
    antiviral gene cassettes, collectively present in 32% of all sequenced bacterial
    and archaeal genomes, that mediate protection against specific bacteriophages.'')
    from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333)
    and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0]
    to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000355
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_mza_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-012
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-013
  issue_key: gao-ppl-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gao_ppl_system.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1126/science.aba0372 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-013 on data/traits/genomics/gao_ppl_system.yaml
    (traitmech:000356): aligned/promoted verified verbatim snippet (''By systematic
    defense gene prediction and heterologous reconstitution, here we discover 29 widespread
    antiviral gene cassettes, collectively present in 32% of all sequenced bacterial
    and archaeal genomes, that mediate protection against specific bacteriophages.'')
    from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333)
    and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0]
    to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000356
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_ppl_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-013
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-014
  issue_key: gao-qat-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gao_qat_system.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1126/science.aba0372 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-014 on data/traits/genomics/gao_qat_system.yaml
    (traitmech:000359): aligned/promoted verified verbatim snippet (''By systematic
    defense gene prediction and heterologous reconstitution, here we discover 29 widespread
    antiviral gene cassettes, collectively present in 32% of all sequenced bacterial
    and archaeal genomes, that mediate protection against specific bacteriophages.'')
    from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333)
    and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0]
    to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000359
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_qat_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-014
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-015
  issue_key: gao-rl-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gao_rl_system.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1126/science.aba0372 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-015 on data/traits/genomics/gao_rl_system.yaml
    (traitmech:000352): aligned/promoted verified verbatim snippet (''By systematic
    defense gene prediction and heterologous reconstitution, here we discover 29 widespread
    antiviral gene cassettes, collectively present in 32% of all sequenced bacterial
    and archaeal genomes, that mediate protection against specific bacteriophages.'')
    from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333)
    and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0]
    to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000352
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_rl_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-015
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-016
  issue_key: gao-tery-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gao_tery_system.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1126/science.aba0372 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-016 on data/traits/genomics/gao_tery_system.yaml
    (traitmech:000360): aligned/promoted verified verbatim snippet (''By systematic
    defense gene prediction and heterologous reconstitution, here we discover 29 widespread
    antiviral gene cassettes, collectively present in 32% of all sequenced bacterial
    and archaeal genomes, that mediate protection against specific bacteriophages.'')
    from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333)
    and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0]
    to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000360
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_tery_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-016
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-017
  issue_key: gao-tmn-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gao_tmn_system.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1126/science.aba0372 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-017 on data/traits/genomics/gao_tmn_system.yaml
    (traitmech:000357): aligned/promoted verified verbatim snippet (''By systematic
    defense gene prediction and heterologous reconstitution, here we discover 29 widespread
    antiviral gene cassettes, collectively present in 32% of all sequenced bacterial
    and archaeal genomes, that mediate protection against specific bacteriophages.'')
    from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333)
    and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0]
    to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000357
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_tmn_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-017
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C4S4-DEF-SRC-018
  issue_key: gao-upx-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gao_upx_system.yaml now includes a verified verbatim snippet for definition_source
    DOI:10.1126/science.aba0372 in record-level evidence[0]
  description: 'Resolved Cycle 4 Stage 4 open finding F-C4S4-DEF-SRC-018 on data/traits/genomics/gao_upx_system.yaml
    (traitmech:000358): aligned/promoted verified verbatim snippet (''By systematic
    defense gene prediction and heterologous reconstitution, here we discover 29 widespread
    antiviral gene cassettes, collectively present in 32% of all sequenced bacterial
    and archaeal genomes, that mediate protection against specific bacteriophages.'')
    from record-level evidence[0] on the same record (cited under PMID alias PMID:32855333)
    and sibling avast_system.yaml / drt_system.yaml / dsr_system.yaml evidence[0]
    to record-level evidence[0] for definition_source DOI:10.1126/science.aba0372
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000358
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c4s4-review
  - ev-c4s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gao_upx_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 4 Stage 5 (resolve_review_findings) under
    group G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
    finding_id: F-C4S4-DEF-SRC-018
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
actions: []
limitations:
- 'This batch review covers the 18 records remediated in Cycle 4 Stage 5 under group
  G-C4S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002); the 5 cohort-level source-limited
  or upstream-blocked findings from Cycle 4 Stage 4 remain tracked under open GitHub
  issues #1982, #1983, #1984, #1985, and #364.'
- '13 of the 18 remediated records carry repository-minted traitmech:NNNNNN identifiers
  backed by validated ROBOT templates awaiting upstream METPO release incorporation
  (#364, berkeleybop/metpo#535); the remaining 5 records carry active METPO: identifiers
  (METPO:1003001, METPO:1000666, METPO:1003026, METPO:1000693, METPO:1000637).'
notes:
- 'Skills executed: .claude/skills/curate-yaml-record/SKILL.md and .claude/skills/review-yaml-record/SKILL.md.'
- Immutable Cycle 4 Stage 4 review bundle preserved untouched at reviews/structured/20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review/review.yaml.
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261025T111000Z-cycle4-stage4-corpus-record-and-cohort-review
  relationship: follow_up_remediation_verification
links:
- https://github.com/CultureBotAI/TraitMech/issues/2002
- https://github.com/CultureBotAI/TraitMech/issues/1982
- https://github.com/CultureBotAI/TraitMech/issues/1983
- https://github.com/CultureBotAI/TraitMech/issues/1984
- https://github.com/CultureBotAI/TraitMech/issues/1985
- https://github.com/CultureBotAI/TraitMech/issues/364
tags:
- cycle-04
- stage-05
- resolve-review-findings
- remediation-verification
```
