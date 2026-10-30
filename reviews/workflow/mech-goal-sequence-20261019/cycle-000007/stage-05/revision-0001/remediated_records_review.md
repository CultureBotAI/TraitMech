# Cycle 7 Stage 5 post-remediation verification review of the 15 TraitRecord files in group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS

- Review: 20261030T221500Z-cycle7-stage5-remediated-records-review
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-30T22:10:00Z
- Finished UTC: 2026-10-30T22:15:00Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Fresh post-remediation batch review of the 15 DefenseFinder genomics TraitRecord YAML files remediated in Cycle 7 Stage 5 (abia_system.yaml, abib_system.yaml, abic_system.yaml, abid_system.yaml, abii_system.yaml, abir_system.yaml, abiu_system.yaml, lit_system.yaml, card_nlr_endonuclease_system.yaml, card_nlr_gasdermin_system.yaml, card_nlr_phospho_system.yaml, card_nlr_subtilase_system.yaml, card_nlr_system.yaml, nlr_like_bnacht_system.yaml, and pd_t2_1_system.yaml) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002. All 15 Cycle 7 Stage 4 open findings (F-C7S4-DEF-SRC-001..015) are verified as resolved with contiguous verbatim snippets for their primary definition_source DOI in record-level evidence[0], append-only curation_history provenance, and 0 remaining open findings.

## Scope And Provenance

Focused post-remediation review of all 15 TraitRecord YAML files modified in Cycle 7 Stage 5 (resolve_review_findings) to resolve group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002).

Selection: All 15 records with open findings carried forward from Cycle 7 Stage 4 review 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review.
Coverage: full; 15 reviewed / 15 in the declared population.
Source: working_tree at Git base f95c506d07a763bca8241e101536d581dce66799.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000344 | data/traits/genomics/abia_system.yaml | maintained | AbiA system |
| traitmech:000319 | data/traits/genomics/abib_system.yaml | maintained | AbiB system |
| traitmech:000320 | data/traits/genomics/abic_system.yaml | maintained | AbiC system |
| traitmech:000318 | data/traits/genomics/abid_system.yaml | maintained | AbiD system |
| traitmech:000316 | data/traits/genomics/abii_system.yaml | maintained | AbiI system |
| traitmech:000317 | data/traits/genomics/abir_system.yaml | maintained | AbiR system |
| traitmech:000321 | data/traits/genomics/abiu_system.yaml | maintained | AbiU system |
| traitmech:000363 | data/traits/genomics/lit_system.yaml | maintained | Lit system |
| traitmech:000550 | data/traits/genomics/card_nlr_endonuclease_system.yaml | maintained | CARD-NLR endonuclease system |
| traitmech:000555 | data/traits/genomics/card_nlr_gasdermin_system.yaml | maintained | CARD-NLR GasderMIN system |
| traitmech:000551 | data/traits/genomics/card_nlr_phospho_system.yaml | maintained | CARD-NLR phospho system |
| traitmech:000553 | data/traits/genomics/card_nlr_subtilase_system.yaml | maintained | CARD-NLR subtilase system |
| traitmech:000337 | data/traits/genomics/card_nlr_system.yaml | maintained | CARD-NLR system |
| traitmech:000408 | data/traits/genomics/nlr_like_bnacht_system.yaml | maintained | NLR-like bNACHT system |
| traitmech:000476 | data/traits/genomics/pd_t2_1_system.yaml | maintained | PD-T2-1 system |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict LinkML schema and reference validation across all TraitRecord files | passed | True | traitmech:000344, traitmech:000319, traitmech:000320, traitmech:000318, traitmech:000316, traitmech:000317, traitmech:000321, traitmech:000363, traitmech:000550, traitmech:000555, traitmech:000551, traitmech:000553, traitmech:000337, traitmech:000408, traitmech:000476 | All 1,130 TraitRecord YAML files (including all 15 Cycle 7 Stage 5 remediated records) pass strict closed-mode LinkML validation with 0 errors. |
| Evidence snippet structural and baseline ratchet audit | passed | True | traitmech:000344, traitmech:000319, traitmech:000320, traitmech:000318, traitmech:000316, traitmech:000317, traitmech:000321, traitmech:000363, traitmech:000550, traitmech:000555, traitmech:000551, traitmech:000553, traitmech:000337, traitmech:000408, traitmech:000476 | All 15 remediated records now carry a contiguous &gt;=16-char verbatim quote for their primary definition_source DOI in record-level evidence[0], passing scripts/audit_evidence_snippets.py with 0 new findings and reducing MISSING_DEFINITION_SOURCE_EVIDENCE from 44 to 29 (-15). |
| Stage 5 guarded writer idempotency and postcondition unit tests | passed | True | traitmech:000344, traitmech:000319, traitmech:000320, traitmech:000318, traitmech:000316, traitmech:000317, traitmech:000321, traitmech:000363, traitmech:000550, traitmech:000555, traitmech:000551, traitmech:000553, traitmech:000337, traitmech:000408, traitmech:000476 | All 5 unit tests in tests/test_curate_stage5_review_findings.py pass, confirming DO_NOT_WORK protection, exact definition_source evidence alignment across all 80 remediated specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4 + 7 Cycle 5 + 13 Cycle 6 + 15 Cycle 7), zero UNQUOTED_DEFINITION_SOURCE or MISSING_DEFINITION_SOURCE_EVIDENCE defects on remediated records, and dry-run/apply idempotency. |
| Guarded YAML writer safeguard audit | passed | True | traitmech:000344, traitmech:000319, traitmech:000320, traitmech:000318, traitmech:000316, traitmech:000317, traitmech:000321, traitmech:000363, traitmech:000550, traitmech:000555, traitmech:000551, traitmech:000553, traitmech:000337, traitmech:000408, traitmech:000476 | scripts/curate_stage5_review_findings.py satisfies all writer safeguards (appends curation_history, has write safeguard, validates before write, wired into justfile). |

## Scientific And Domain Assessments

### Verification of record-level definition_source evidence[0] CURIE and verbatim snippet alignment across the 15 remediated records

evidence: supported. Targets: traitmech:000344, traitmech:000319, traitmech:000320, traitmech:000318, traitmech:000316, traitmech:000317, traitmech:000321, traitmech:000363, traitmech:000550, traitmech:000555, traitmech:000551, traitmech:000553, traitmech:000337, traitmech:000408, traitmech:000476.

All 15 DefenseFinder genomics records identified with open findings in Cycle 7 Stage 4 (abia_system.yaml, abib_system.yaml, abic_system.yaml, abid_system.yaml, abii_system.yaml, abir_system.yaml, abiu_system.yaml, lit_system.yaml, card_nlr_endonuclease_system.yaml, card_nlr_gasdermin_system.yaml, card_nlr_phospho_system.yaml, card_nlr_subtilase_system.yaml, card_nlr_system.yaml, nlr_like_bnacht_system.yaml, and pd_t2_1_system.yaml) now align record-level evidence[0].reference with their primary definition_source DOI and carry a verified non-elliptical verbatim snippet directly in record-level evidence[0].

Each of the 15 remediated records was re-inspected against .claude/skills/review-yaml-record/SKILL.md: (1) F-C7S4-DEF-SRC-001..008 (abia_system.yaml, abib_system.yaml, abic_system.yaml, abid_system.yaml, abii_system.yaml, abir_system.yaml, abiu_system.yaml, lit_system.yaml) now align evidence[0].reference with their primary lactococcal/E. coli abortive infection definition_source DOIs while preserving their verified verbatim abstract snippets and PMID aliases; (2) F-C7S4-DEF-SRC-009..013 (card_nlr_endonuclease_system.yaml, card_nlr_gasdermin_system.yaml, card_nlr_phospho_system.yaml, card_nlr_subtilase_system.yaml, card_nlr_system.yaml) now align evidence[0].reference with definition_source DOI:10.1101/2023.05.28.542683 (from https://europepmc.org/article/PPR/PPR668921); (3) F-C7S4-DEF-SRC-014 (nlr_like_bnacht_system.yaml) aligns evidence[0].reference with definition_source DOI:10.1016/j.cell.2023.04.015 (from https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/); and (4) F-C7S4-DEF-SRC-015 (pd_t2_1_system.yaml) aligns evidence[0].reference with definition_source DOI:10.1038/s41564-025-02239-6 (from https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/).

### Schema validity, curation_history provenance, and writer guardrails on remediated records

provenance: supported. Targets: traitmech:000344, traitmech:000319, traitmech:000320, traitmech:000318, traitmech:000316, traitmech:000317, traitmech:000321, traitmech:000363, traitmech:000550, traitmech:000555, traitmech:000551, traitmech:000553, traitmech:000337, traitmech:000408, traitmech:000476.

All 15 remediated records pass strict closed-mode LinkML validation, preserve existing canonical_examples, causal_graphs, and UniProtKB protein_examples untouched, and record append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history entries referencing issue #2002.

## Findings

### F-C7S4-DEF-SRC-001: abia_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1128/aem.60.4.1129-1136.1994 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: abia-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-001 on data/traits/genomics/abia_system.yaml (traitmech:000344): aligned record-level evidence[0].reference from PMID:16349225 to definition_source DOI:10.1128/aem.60.4.1129-1136.1994 while preserving the verified verbatim snippet ('The abiA gene (formerly hsp) encodes an abortive phage infection mechanism which inhibits phage DNA replication.') (Dinsmore and Klaenhammer describe abiA as the former hsp abortive-infection determinant and connect AbiA activity to inhibition of phage DNA replication (PMID:16349225 / DOI:10.1128/aem.60.4.1129-1136.1994).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-002: abib_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1046/j.1365-2958.1996.371896.x carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: abib-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-002 on data/traits/genomics/abib_system.yaml (traitmech:000319): aligned record-level evidence[0].reference from PMID:8825768 to definition_source DOI:10.1046/j.1365-2958.1996.371896.x while preserving the verified verbatim snippet ('The abortive infection determinant AbiB prevents growth of the sensitive phage bIL170, but not of the resistant phage bIL41, on Lactococcus lactis strain IL1403') (Parreira et al. place AbiB in the abortive-infection class and show that it blocks the sensitive lactococcal phage bIL170 on Lactococcus lactis IL1403 (PMID:8825768 / DOI:10.1046/j.1365-2958.1996.371896.x).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-003: abic_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1128/jb.174.22.7463-7469.1992 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: abic-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-003 on data/traits/genomics/abic_system.yaml (traitmech:000320): aligned record-level evidence[0].reference from PMID:1429469 to definition_source DOI:10.1128/jb.174.22.7463-7469.1992 while preserving the verified verbatim snippet ('The genetic determinant for Prf (phage resistance five) was subcloned from the conjugative plasmid pTN20') (Durmaz et al. subcloned the Prf determinant from the Lactococcus lactis ME2 conjugative plasmid pTN20 (PMID:1429469 / DOI:10.1128/jb.174.22.7463-7469.1992).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-004: abid_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1128/aem.61.5.2023-2026.1995 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: abid-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-004 on data/traits/genomics/abid_system.yaml (traitmech:000318): aligned record-level evidence[0].reference from PMID:7646042 to definition_source DOI:10.1128/aem.61.5.2023-2026.1995 while preserving the verified verbatim snippet ('A 6.3-kb fragment from pBF61 in Lactococcus lactis subsp. lactis KR5 was cloned and found to confer an abortive phage infection (Abi+) phenotype') (McLandsborough et al. cloned the pBF61-derived fragment from Lactococcus lactis subsp. lactis KR5 and showed that it conferred an Abi phenotype (PMID:7646042 / DOI:10.1128/aem.61.5.2023-2026.1995).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-005: abii_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1016/S0168-1656(97)01692-1 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: abii-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-005 on data/traits/genomics/abii_system.yaml (traitmech:000316): aligned record-level evidence[0].reference from PMID:9195753 to definition_source DOI:10.1016/S0168-1656(97)01692-1 while preserving the verified verbatim snippet ('Plasmid pND852 (56 kb) encodes nisin resistance and was isolated from Lactococcus lactis ssp lactis (L. lactis) M138 by conjugation to L. lactis LM0230') (Su et al. identified plasmid pND852 from Lactococcus lactis M138 as the source of the abiI-associated phage resistance locus (PMID:9195753 / DOI:10.1016/S0168-1656(97)01692-1).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-006: abir_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1128/AEM.66.6.2647-2651.2000 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: abir-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-006 on data/traits/genomics/abir_system.yaml (traitmech:000317): aligned record-level evidence[0].reference from PMID:10831451 to definition_source DOI:10.1128/AEM.66.6.2647-2651.2000 while preserving the verified verbatim snippet ('The native lactococcal plasmid pKR223 encodes two distinct phage resistance mechanisms, a restriction and modification (R/M) system designated LlaKR2I and an abortive infection mechanism (Abi) which affects prolate-headed-phage proliferation') (Twomey et al. identify native Lactococcus lactis plasmid pKR223 as the source of a restriction-modification system and a separate abortive-infection determinant (PMID:10831451 / DOI:10.1128/AEM.66.6.2647-2651.2000).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-007: abiu_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1128/AEM.67.11.5225-5232.2001 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: abiu-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-007 on data/traits/genomics/abiu_system.yaml (traitmech:000321): aligned record-level evidence[0].reference from PMID:11679349 to definition_source DOI:10.1128/AEM.67.11.5225-5232.2001 while preserving the verified verbatim snippet ('This study reports on the identification and characterization of a novel abortive infection system, AbiU, from Lactococcus lactis.') (Dai et al. identify AbiU as a novel Lactococcus lactis abortive-infection system (PMID:11679349 / DOI:10.1128/AEM.67.11.5225-5232.2001).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-008: lit_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1021/bi0495026 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: lit-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-008 on data/traits/genomics/lit_system.yaml (traitmech:000363): aligned record-level evidence[0].reference from PMID:15196039 to definition_source DOI:10.1021/bi0495026 while preserving the verified verbatim snippet ('Bacteriophage exclusion is a suicide response to viral infection. In strains of Escherichia coli K-12 infected with T4 phage this process is mediated by the host-encoded Lit peptidase. Lit is activated by a unique sequence in the major head protein of the T4 phage (the Gol sequence) which then cleaves site-specifically the host translation factor EF-Tu, ultimately leading to cell death.') (Copeland et al. support host Lit as a T4-activated bacteriophage-exclusion peptidase that cleaves EF-Tu and leads to cell death (PMID:15196039 / DOI:10.1021/bi0495026).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-009: card_nlr_endonuclease_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1101/2023.05.28.542683 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: card-nlr-endonuclease-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-009 on data/traits/genomics/card_nlr_endonuclease_system.yaml (traitmech:000550): aligned record-level evidence[0].reference from https://europepmc.org/article/PPR/PPR668921 to definition_source DOI:10.1101/2023.05.28.542683 while preserving the verified verbatim snippet ('Here we show that CARD-like domains are present in defense systems that protect bacteria against phage.') (Wein et al. support bacterial CARD-like domains as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921 / DOI:10.1101/2023.05.28.542683).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-010: card_nlr_gasdermin_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1101/2023.05.28.542683 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: card-nlr-gasdermin-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-010 on data/traits/genomics/card_nlr_gasdermin_system.yaml (traitmech:000555): aligned record-level evidence[0].reference from https://europepmc.org/article/PPR/PPR668921 to definition_source DOI:10.1101/2023.05.28.542683 while preserving the verified verbatim snippet ('Here we show that CARD-like domains are present in defense systems that protect bacteria against phage.') (Wein et al. support bacterial CARD-like domains as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921 / DOI:10.1101/2023.05.28.542683).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-011: card_nlr_phospho_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1101/2023.05.28.542683 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: card-nlr-phospho-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-011 on data/traits/genomics/card_nlr_phospho_system.yaml (traitmech:000551): aligned record-level evidence[0].reference from https://europepmc.org/article/PPR/PPR668921 to definition_source DOI:10.1101/2023.05.28.542683 while preserving the verified verbatim snippet ('Here we show that CARD-like domains are present in defense systems that protect bacteria against phage.') (Wein et al. support bacterial CARD-like domains as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921 / DOI:10.1101/2023.05.28.542683).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-012: card_nlr_subtilase_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1101/2023.05.28.542683 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: card-nlr-subtilase-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-012 on data/traits/genomics/card_nlr_subtilase_system.yaml (traitmech:000553): aligned record-level evidence[0].reference from https://europepmc.org/article/PPR/PPR668921 to definition_source DOI:10.1101/2023.05.28.542683 while preserving the verified verbatim snippet ('Here we show that CARD-like domains are present in defense systems that protect bacteria against phage.') (Wein et al. support bacterial CARD-like domains as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921 / DOI:10.1101/2023.05.28.542683).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-013: card_nlr_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1101/2023.05.28.542683 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: card-nlr-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-013 on data/traits/genomics/card_nlr_system.yaml (traitmech:000337): aligned record-level evidence[0].reference from https://europepmc.org/article/PPR/PPR668921 to definition_source DOI:10.1101/2023.05.28.542683 while preserving the verified verbatim snippet ('Here we show that CARD-like domains are present in defense systems that protect bacteria against phage.') (The Wein et al. abstract supports CARD-like-domain systems as bacterial phage-defense systems (https://europepmc.org/article/PPR/PPR668921 / DOI:10.1101/2023.05.28.542683).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-014: nlr_like_bnacht_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1016/j.cell.2023.04.015 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: nlr-like-bnacht-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-014 on data/traits/genomics/nlr_like_bnacht_system.yaml (traitmech:000408): aligned record-level evidence[0].reference from https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/ to definition_source DOI:10.1016/j.cell.2023.04.015 while preserving the verified verbatim snippet ('Here we show that proteins containing a NACHT module, the central feature of the animal nucleotide-binding domain and leucine-rich repeat-containing gene family (NLRs), are found in bacteria and defend against phages.') (Kibby et al. support NACHT-module proteins as bacterial NLR-related proteins that defend against phages (https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/ / DOI:10.1016/j.cell.2023.04.015).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C7S4-DEF-SRC-015: pd_t2_1_system.yaml now aligns record-level evidence[0].reference with definition_source DOI:10.1038/s41564-025-02239-6 carrying a verified verbatim snippet

minor / resolved / confirmed; issue key: pd-t2-1-system-definition-source-curie-alignment.

Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-015 on data/traits/genomics/pd_t2_1_system.yaml (traitmech:000476): aligned record-level evidence[0].reference from https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/ to definition_source DOI:10.1038/s41564-025-02239-6 while preserving the verified verbatim snippet ('Two phage proteins were further investigated, revealing T7 gp17 and additional tail fiber proteins activated the undescribed antiphage system PD-T2–1 and identifying λ gpE major capsid protein activated the antiphage system Avs8.') (Goedecke et al. report that T7 gp17 and additional tail fiber proteins activated the previously undescribed PD-T2-1 antiphage system (https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/ / DOI:10.1038/s41564-025-02239-6).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 7 Stage 5 (resolve_review_findings) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-prior-c7s4-review | reviews/structured/20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review/review.yaml; findings[0..14] | supports | Immutable Cycle 7 Stage 4 review bundle identifying the 15 open definition_source CURIE alignment findings (F-C7S4-DEF-SRC-001..F-C7S4-DEF-SRC-015) with planned remediation actions ACT-C7S4-DEF-SRC-001..015. |
| ev-c7s5-def-src-001 | DOI:10.1128/aem.60.4.1129-1136.1994; Aligned on evidence[0] (Dinsmore and Klaenhammer describe abiA as the former hsp abortive-infection determinant and connect AbiA activity to inhibition of phage DNA replication (PMID:16349225 / DOI:10.1128/aem.60.4.1129-1136.1994).) | supports | Primary definition_source DOI:10.1128/aem.60.4.1129-1136.1994 verified via existing verbatim quote (Dinsmore and Klaenhammer describe abiA as the former hsp abortive-infection determinant and connect AbiA activity to inhibition of phage DNA replication (PMID:16349225 / DOI:10.1128/aem.60.4.1129-1136.1994).) and aligned in record-level evidence[0]. |
| ev-c7s5-def-src-002 | DOI:10.1046/j.1365-2958.1996.371896.x; Aligned on evidence[0] (Parreira et al. place AbiB in the abortive-infection class and show that it blocks the sensitive lactococcal phage bIL170 on Lactococcus lactis IL1403 (PMID:8825768 / DOI:10.1046/j.1365-2958.1996.371896.x).) | supports | Primary definition_source DOI:10.1046/j.1365-2958.1996.371896.x verified via existing verbatim quote (Parreira et al. place AbiB in the abortive-infection class and show that it blocks the sensitive lactococcal phage bIL170 on Lactococcus lactis IL1403 (PMID:8825768 / DOI:10.1046/j.1365-2958.1996.371896.x).) and aligned in record-level evidence[0]. |
| ev-c7s5-def-src-003 | DOI:10.1128/jb.174.22.7463-7469.1992; Aligned on evidence[0] (Durmaz et al. subcloned the Prf determinant from the Lactococcus lactis ME2 conjugative plasmid pTN20 (PMID:1429469 / DOI:10.1128/jb.174.22.7463-7469.1992).) | supports | Primary definition_source DOI:10.1128/jb.174.22.7463-7469.1992 verified via existing verbatim quote (Durmaz et al. subcloned the Prf determinant from the Lactococcus lactis ME2 conjugative plasmid pTN20 (PMID:1429469 / DOI:10.1128/jb.174.22.7463-7469.1992).) and aligned in record-level evidence[0]. |
| ev-c7s5-def-src-004 | DOI:10.1128/aem.61.5.2023-2026.1995; Aligned on evidence[0] (McLandsborough et al. cloned the pBF61-derived fragment from Lactococcus lactis subsp. lactis KR5 and showed that it conferred an Abi phenotype (PMID:7646042 / DOI:10.1128/aem.61.5.2023-2026.1995).) | supports | Primary definition_source DOI:10.1128/aem.61.5.2023-2026.1995 verified via existing verbatim quote (McLandsborough et al. cloned the pBF61-derived fragment from Lactococcus lactis subsp. lactis KR5 and showed that it conferred an Abi phenotype (PMID:7646042 / DOI:10.1128/aem.61.5.2023-2026.1995).) and aligned in record-level evidence[0]. |
| ev-c7s5-def-src-005 | DOI:10.1016/S0168-1656(97)01692-1; Aligned on evidence[0] (Su et al. identified plasmid pND852 from Lactococcus lactis M138 as the source of the abiI-associated phage resistance locus (PMID:9195753 / DOI:10.1016/S0168-1656(97)01692-1).) | supports | Primary definition_source DOI:10.1016/S0168-1656(97)01692-1 verified via existing verbatim quote (Su et al. identified plasmid pND852 from Lactococcus lactis M138 as the source of the abiI-associated phage resistance locus (PMID:9195753 / DOI:10.1016/S0168-1656(97)01692-1).) and aligned in record-level evidence[0]. |
| ev-c7s5-def-src-006 | DOI:10.1128/AEM.66.6.2647-2651.2000; Aligned on evidence[0] (Twomey et al. identify native Lactococcus lactis plasmid pKR223 as the source of a restriction-modification system and a separate abortive-infection determinant (PMID:10831451 / DOI:10.1128/AEM.66.6.2647-2651.2000).) | supports | Primary definition_source DOI:10.1128/AEM.66.6.2647-2651.2000 verified via existing verbatim quote (Twomey et al. identify native Lactococcus lactis plasmid pKR223 as the source of a restriction-modification system and a separate abortive-infection determinant (PMID:10831451 / DOI:10.1128/AEM.66.6.2647-2651.2000).) and aligned in record-level evidence[0]. |
| ev-c7s5-def-src-007 | DOI:10.1128/AEM.67.11.5225-5232.2001; Aligned on evidence[0] (Dai et al. identify AbiU as a novel Lactococcus lactis abortive-infection system (PMID:11679349 / DOI:10.1128/AEM.67.11.5225-5232.2001).) | supports | Primary definition_source DOI:10.1128/AEM.67.11.5225-5232.2001 verified via existing verbatim quote (Dai et al. identify AbiU as a novel Lactococcus lactis abortive-infection system (PMID:11679349 / DOI:10.1128/AEM.67.11.5225-5232.2001).) and aligned in record-level evidence[0]. |
| ev-c7s5-def-src-008 | DOI:10.1021/bi0495026; Aligned on evidence[0] (Copeland et al. support host Lit as a T4-activated bacteriophage-exclusion peptidase that cleaves EF-Tu and leads to cell death (PMID:15196039 / DOI:10.1021/bi0495026).) | supports | Primary definition_source DOI:10.1021/bi0495026 verified via existing verbatim quote (Copeland et al. support host Lit as a T4-activated bacteriophage-exclusion peptidase that cleaves EF-Tu and leads to cell death (PMID:15196039 / DOI:10.1021/bi0495026).) and aligned in record-level evidence[0]. |
| ev-c7s5-def-src-009 | DOI:10.1101/2023.05.28.542683; Aligned on evidence[0] (Wein et al. support bacterial CARD-like domains as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921 / DOI:10.1101/2023.05.28.542683).) | supports | Primary definition_source DOI:10.1101/2023.05.28.542683 verified via existing verbatim quote (Wein et al. support bacterial CARD-like domains as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921 / DOI:10.1101/2023.05.28.542683).) and aligned in record-level evidence[0]. |
| ev-c7s5-def-src-010 | DOI:10.1016/j.cell.2023.04.015; Aligned on evidence[0] (Kibby et al. support NACHT-module proteins as bacterial NLR-related proteins that defend against phages (https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/ / DOI:10.1016/j.cell.2023.04.015).) | supports | Primary definition_source DOI:10.1016/j.cell.2023.04.015 verified via existing verbatim quote (Kibby et al. support NACHT-module proteins as bacterial NLR-related proteins that defend against phages (https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/ / DOI:10.1016/j.cell.2023.04.015).) and aligned in record-level evidence[0]. |
| ev-c7s5-def-src-011 | DOI:10.1038/s41564-025-02239-6; Aligned on evidence[0] (Goedecke et al. report that T7 gp17 and additional tail fiber proteins activated the previously undescribed PD-T2-1 antiphage system (https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/ / DOI:10.1038/s41564-025-02239-6).) | supports | Primary definition_source DOI:10.1038/s41564-025-02239-6 verified via existing verbatim quote (Goedecke et al. report that T7 gp17 and additional tail fiber proteins activated the previously undescribed PD-T2-1 antiphage system (https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/ / DOI:10.1038/s41564-025-02239-6).) and aligned in record-level evidence[0]. |
| ev-remediated-records | data/traits/genomics/abia_system.yaml; data/traits/genomics/abib_system.yaml; data/traits/genomics/abic_system.yaml; data/traits/genomics/abid_system.yaml; data/traits/genomics/abii_system.yaml; data/traits/genomics/abir_system.yaml; data/traits/genomics/abiu_system.yaml; data/traits/genomics/lit_system.yaml; data/traits/genomics/card_nlr_endonuclease_system.yaml; data/traits/genomics/card_nlr_gasdermin_system.yaml; data/traits/genomics/card_nlr_phospho_system.yaml; data/traits/genomics/card_nlr_subtilase_system.yaml; data/traits/genomics/card_nlr_system.yaml; data/traits/genomics/nlr_like_bnacht_system.yaml; data/traits/genomics/pd_t2_1_system.yaml; definition_source, evidence[0], curation_history | supports | All 15 remediated TraitRecord YAML files now align record-level evidence[0].reference with their declared definition_source DOI, preserve their verified non-elliptical verbatim snippet, and record an append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event. |
| ev-stage5-writer | scripts/curate_stage5_review_findings.py; tests/test_curate_stage5_review_findings.py; process_all | supports | Guarded writer script and unit test suite verifying closed-mode LinkML validation, DO_NOT_WORK exclusion, and idempotent remediation across all 80 target specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4 + 7 Cycle 5 + 13 Cycle 6 + 15 Cycle 7). |
| ev-validate-strict | scripts/validate_strict.py; reports/instance_validation_failures.tsv | supports | Closed-mode LinkML schema and identifier validation passes with 0 errors across all 1,130 TraitRecord files. |
| ev-snippet-audit | scripts/audit_evidence_snippets.py; conf/evidence_snippet_baseline.tsv | supports | All 15 remediated record-level evidence[0] entries pass contiguous verbatim quote checks with 0 new warnings and eliminate all 15 open definition_source CURIE alignment findings from Cycle 7 Stage 4. |

## Limits And Additional Notes

- This batch review covers the 15 records remediated in Cycle 7 Stage 5 under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002); the 5 cohort-level source-limited or upstream-blocked findings from Cycle 7 Stage 4 remain tracked under open GitHub issues #1982, #1983, #1984, #1985, and #364.
- All 15 of the remediated records carry repository-minted traitmech:NNNNNN identifiers (traitmech:000316..000321, traitmech:000337, traitmech:000344, traitmech:000363, traitmech:000408, traitmech:000476, traitmech:000550, traitmech:000551, traitmech:000553, traitmech:000555) backed by validated ROBOT templates awaiting upstream METPO release incorporation (#364, berkeleybop/metpo#535).
- Skills executed: .claude/skills/curate-yaml-record/SKILL.md and .claude/skills/review-yaml-record/SKILL.md.
- Immutable Cycle 7 Stage 4 review bundle preserved untouched at reviews/structured/20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review/review.yaml.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T221500Z-cycle7-stage5-remediated-records-review
kind: batch
repository: CultureBotAI/TraitMech
title: Cycle 7 Stage 5 post-remediation verification review of the 15 TraitRecord
  files in group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
started_at: '2026-10-30T22:10:00Z'
finished_at: '2026-10-30T22:15:00Z'
reviewer:
  identity: antigravity
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Repository-local post-remediation record review verifying resolution
    of the 15 Cycle 7 Stage 4 open findings (F-C7S4-DEF-SRC-001..F-C7S4-DEF-SRC-015)
    under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002); separate from
    independent PR adversarial review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Fresh post-remediation batch review of the 15 DefenseFinder genomics TraitRecord
  YAML files remediated in Cycle 7 Stage 5 (abia_system.yaml, abib_system.yaml, abic_system.yaml,
  abid_system.yaml, abii_system.yaml, abir_system.yaml, abiu_system.yaml, lit_system.yaml,
  card_nlr_endonuclease_system.yaml, card_nlr_gasdermin_system.yaml, card_nlr_phospho_system.yaml,
  card_nlr_subtilase_system.yaml, card_nlr_system.yaml, nlr_like_bnacht_system.yaml,
  and pd_t2_1_system.yaml) under group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
  and GitHub issue #2002. All 15 Cycle 7 Stage 4 open findings (F-C7S4-DEF-SRC-001..015)
  are verified as resolved with contiguous verbatim snippets for their primary definition_source
  DOI in record-level evidence[0], append-only curation_history provenance, and 0
  remaining open findings.'
source:
  git_revision: f95c506d07a763bca8241e101536d581dce66799
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: 27f535d3f057d321c8b87c6506f2f35dd2d37fd005bcd5040b3e17269285075b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: bb03efa3bbd3748ee1dccf57612a6ce8fcc861f20eb57c33eb16e3ac1dd728bd
    role: context
  - path: CLAUDE.md
    sha256: 6771ed07ef5ae68deecbf50ae6123e2e3a4834e05b2dbc13faa96ec2329a6f93
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: conf/record_review.yaml
    sha256: 5adc6244761fb2baf8a059d81f23b0c9b32a33f9426ab84094234c3ec417269d
    role: context
  - path: data/traits/genomics/abia_system.yaml
    sha256: b2946a9c16a6536133931c68bb2750e6ada4afecb03d6feef51d0044486151a3
    role: target
  - path: data/traits/genomics/abib_system.yaml
    sha256: b27679eece391881b5874fccc505a5e59d19d7c945b22783000704c7795e8659
    role: target
  - path: data/traits/genomics/abic_system.yaml
    sha256: 0f8c280c6fe7b44f7e0fd3007fb790cfc7ff1a8ae88cb57b4d338f30c948a998
    role: target
  - path: data/traits/genomics/abid_system.yaml
    sha256: 22ed793d6cf8a82d1b0a26fb0f5e90d1b1fe1b372f51c899a200a30acb674c79
    role: target
  - path: data/traits/genomics/abii_system.yaml
    sha256: 7731249939a3e9e561a9c7dff700f637c099e9f40e72792c2312cde702a1cb8e
    role: target
  - path: data/traits/genomics/abir_system.yaml
    sha256: 1f84d6e09d579c2512781670140fb79e7c689e38ee54491b143314cb5bda06eb
    role: target
  - path: data/traits/genomics/abiu_system.yaml
    sha256: 4632f75dd12183889d30f23f7af4d655a76732b6f01b4139257a182be8b99f29
    role: target
  - path: data/traits/genomics/card_nlr_endonuclease_system.yaml
    sha256: 214ecd01711c91bda2213a79b150d7d55440951b1b39cde8f47f823e8eab6394
    role: target
  - path: data/traits/genomics/card_nlr_gasdermin_system.yaml
    sha256: d210677323156491a50f6b334b4d6bd68e2e38e55a2facb87212897299555851
    role: target
  - path: data/traits/genomics/card_nlr_phospho_system.yaml
    sha256: 0b8c06b41d85ebaa4f7d6671492ebbcf5f563c1e011cf2c90399c3db07135d67
    role: target
  - path: data/traits/genomics/card_nlr_subtilase_system.yaml
    sha256: b7cea39bc2dbe33557af071bb4f738400950262ab874cebdb6c49493985b417c
    role: target
  - path: data/traits/genomics/card_nlr_system.yaml
    sha256: b900692b8a9074e316e1fd8c6937df6cae42a97ee22a99bbe7aece5e7f329c3d
    role: target
  - path: data/traits/genomics/lit_system.yaml
    sha256: 1c0ce6377dae3030cbc89ca2ce27cb2e31a0a675d40eed7d6c6c67c17428f752
    role: target
  - path: data/traits/genomics/nlr_like_bnacht_system.yaml
    sha256: 22dc73b6a7170c2384fea9da0edb43b57167d4af56039cdc2dc941ecad7bcdf3
    role: target
  - path: data/traits/genomics/pd_t2_1_system.yaml
    sha256: 6ad5cdaeae294c6bcd310790e7b3f50886e275ef067b1bd3b85fa07cefb7f974
    role: target
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/infrastructure/curate_stage5_review_findings/2026-10-30T221000Z-claude-code-c7s501.yaml
    sha256: d259bc20c70220680d7b67754f8386ce50d579005b6d9faabf73ba9989248299
    role: context
  - path: reviews/structured/20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review/review.yaml
    sha256: 5b97ed3407f706dfaea68893d8fccec0f5fc86ed14fd7e66baf74635c8a56ec0
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-04/revision-0001/evidence.yaml
    sha256: 222a00d992e5eb786338b7adb358f13677621133be981764b0f2be6fa8fbd47c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/curate_stage5_review_findings.py
    sha256: bc2d52b7f2ecd893006523025b45f44a1edcf8ec7ca4188960c1b4fe94ba283f
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: tests/test_curate_stage5_review_findings.py
    sha256: f8e4f1ab2ca1ce8329ec3d77667100bf37906d4109ce83ac604244aed560a201
    role: context
scope:
  description: Focused post-remediation review of all 15 TraitRecord YAML files modified
    in Cycle 7 Stage 5 (resolve_review_findings) to resolve group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    (#2002).
  selection: All 15 records with open findings carried forward from Cycle 7 Stage
    4 review 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review.
  coverage: full
  population_size: 15
  reviewed_target_ids:
  - traitmech:000344
  - traitmech:000319
  - traitmech:000320
  - traitmech:000318
  - traitmech:000316
  - traitmech:000317
  - traitmech:000321
  - traitmech:000363
  - traitmech:000550
  - traitmech:000555
  - traitmech:000551
  - traitmech:000553
  - traitmech:000337
  - traitmech:000408
  - traitmech:000476
targets:
- target_id: traitmech:000344
  path: data/traits/genomics/abia_system.yaml
  label: AbiA system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abia_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000319
  path: data/traits/genomics/abib_system.yaml
  label: AbiB system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abib_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000320
  path: data/traits/genomics/abic_system.yaml
  label: AbiC system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abic_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000318
  path: data/traits/genomics/abid_system.yaml
  label: AbiD system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abid_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000316
  path: data/traits/genomics/abii_system.yaml
  label: AbiI system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abii_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000317
  path: data/traits/genomics/abir_system.yaml
  label: AbiR system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abir_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000321
  path: data/traits/genomics/abiu_system.yaml
  label: AbiU system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abiu_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000363
  path: data/traits/genomics/lit_system.yaml
  label: Lit system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/lit_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000550
  path: data/traits/genomics/card_nlr_endonuclease_system.yaml
  label: CARD-NLR endonuclease system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/card_nlr_endonuclease_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000555
  path: data/traits/genomics/card_nlr_gasdermin_system.yaml
  label: CARD-NLR GasderMIN system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/card_nlr_gasdermin_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000551
  path: data/traits/genomics/card_nlr_phospho_system.yaml
  label: CARD-NLR phospho system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/card_nlr_phospho_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000553
  path: data/traits/genomics/card_nlr_subtilase_system.yaml
  label: CARD-NLR subtilase system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/card_nlr_subtilase_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000337
  path: data/traits/genomics/card_nlr_system.yaml
  label: CARD-NLR system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/card_nlr_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000408
  path: data/traits/genomics/nlr_like_bnacht_system.yaml
  label: NLR-like bNACHT system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/nlr_like_bnacht_system.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000476
  path: data/traits/genomics/pd_t2_1_system.yaml
  label: PD-T2-1 system
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/pd_t2_1_system.yaml
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
  - traitmech:000344
  - traitmech:000319
  - traitmech:000320
  - traitmech:000318
  - traitmech:000316
  - traitmech:000317
  - traitmech:000321
  - traitmech:000363
  - traitmech:000550
  - traitmech:000555
  - traitmech:000551
  - traitmech:000553
  - traitmech:000337
  - traitmech:000408
  - traitmech:000476
  evidence_ids:
  - ev-validate-strict
  - ev-remediated-records
  summary: All 1,130 TraitRecord YAML files (including all 15 Cycle 7 Stage 5 remediated
    records) pass strict closed-mode LinkML validation with 0 errors.
- check_id: audit-snippets
  name: Evidence snippet structural and baseline ratchet audit
  command: uv run python scripts/audit_evidence_snippets.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000344
  - traitmech:000319
  - traitmech:000320
  - traitmech:000318
  - traitmech:000316
  - traitmech:000317
  - traitmech:000321
  - traitmech:000363
  - traitmech:000550
  - traitmech:000555
  - traitmech:000551
  - traitmech:000553
  - traitmech:000337
  - traitmech:000408
  - traitmech:000476
  evidence_ids:
  - ev-snippet-audit
  - ev-c7s5-def-src-001
  - ev-c7s5-def-src-002
  - ev-c7s5-def-src-003
  - ev-c7s5-def-src-004
  - ev-c7s5-def-src-005
  - ev-c7s5-def-src-006
  - ev-c7s5-def-src-007
  - ev-c7s5-def-src-008
  - ev-c7s5-def-src-009
  - ev-c7s5-def-src-010
  - ev-c7s5-def-src-011
  summary: All 15 remediated records now carry a contiguous >=16-char verbatim quote
    for their primary definition_source DOI in record-level evidence[0], passing scripts/audit_evidence_snippets.py
    with 0 new findings and reducing MISSING_DEFINITION_SOURCE_EVIDENCE from 44 to
    29 (-15).
- check_id: stage5-writer-tests
  name: Stage 5 guarded writer idempotency and postcondition unit tests
  command: uv run pytest tests/test_curate_stage5_review_findings.py -v
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000344
  - traitmech:000319
  - traitmech:000320
  - traitmech:000318
  - traitmech:000316
  - traitmech:000317
  - traitmech:000321
  - traitmech:000363
  - traitmech:000550
  - traitmech:000555
  - traitmech:000551
  - traitmech:000553
  - traitmech:000337
  - traitmech:000408
  - traitmech:000476
  evidence_ids:
  - ev-stage5-writer
  summary: All 5 unit tests in tests/test_curate_stage5_review_findings.py pass, confirming
    DO_NOT_WORK protection, exact definition_source evidence alignment across all
    80 remediated specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4 + 7 Cycle
    5 + 13 Cycle 6 + 15 Cycle 7), zero UNQUOTED_DEFINITION_SOURCE or MISSING_DEFINITION_SOURCE_EVIDENCE
    defects on remediated records, and dry-run/apply idempotency.
- check_id: audit-writers
  name: Guarded YAML writer safeguard audit
  command: uv run python scripts/audit_writers.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000344
  - traitmech:000319
  - traitmech:000320
  - traitmech:000318
  - traitmech:000316
  - traitmech:000317
  - traitmech:000321
  - traitmech:000363
  - traitmech:000550
  - traitmech:000555
  - traitmech:000551
  - traitmech:000553
  - traitmech:000337
  - traitmech:000408
  - traitmech:000476
  evidence_ids:
  - ev-stage5-writer
  summary: scripts/curate_stage5_review_findings.py satisfies all writer safeguards
    (appends curation_history, has write safeguard, validates before write, wired
    into justfile).
evidence:
- evidence_id: ev-prior-c7s4-review
  kind: prior_review
  reference: reviews/structured/20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review/review.yaml
  locator: findings[0..14]
  accessed_at: '2026-10-30T22:11:00Z'
  support: supports
  summary: Immutable Cycle 7 Stage 4 review bundle identifying the 15 open definition_source
    CURIE alignment findings (F-C7S4-DEF-SRC-001..F-C7S4-DEF-SRC-015) with planned
    remediation actions ACT-C7S4-DEF-SRC-001..015.
  snapshot_sha256: 5b97ed3407f706dfaea68893d8fccec0f5fc86ed14fd7e66baf74635c8a56ec0
- evidence_id: ev-c7s5-def-src-001
  kind: primary_source
  reference: DOI:10.1128/aem.60.4.1129-1136.1994
  locator: Aligned on evidence[0] (Dinsmore and Klaenhammer describe abiA as the former
    hsp abortive-infection determinant and connect AbiA activity to inhibition of
    phage DNA replication (PMID:16349225 / DOI:10.1128/aem.60.4.1129-1136.1994).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1128/aem.60.4.1129-1136.1994 verified
    via existing verbatim quote (Dinsmore and Klaenhammer describe abiA as the former
    hsp abortive-infection determinant and connect AbiA activity to inhibition of
    phage DNA replication (PMID:16349225 / DOI:10.1128/aem.60.4.1129-1136.1994).)
    and aligned in record-level evidence[0].
  quote: The abiA gene (formerly hsp) encodes an abortive phage infection mechanism
    which inhibits phage DNA replication.
- evidence_id: ev-c7s5-def-src-002
  kind: primary_source
  reference: DOI:10.1046/j.1365-2958.1996.371896.x
  locator: Aligned on evidence[0] (Parreira et al. place AbiB in the abortive-infection
    class and show that it blocks the sensitive lactococcal phage bIL170 on Lactococcus
    lactis IL1403 (PMID:8825768 / DOI:10.1046/j.1365-2958.1996.371896.x).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1046/j.1365-2958.1996.371896.x verified
    via existing verbatim quote (Parreira et al. place AbiB in the abortive-infection
    class and show that it blocks the sensitive lactococcal phage bIL170 on Lactococcus
    lactis IL1403 (PMID:8825768 / DOI:10.1046/j.1365-2958.1996.371896.x).) and aligned
    in record-level evidence[0].
  quote: The abortive infection determinant AbiB prevents growth of the sensitive
    phage bIL170, but not of the resistant phage bIL41, on Lactococcus lactis strain
    IL1403
- evidence_id: ev-c7s5-def-src-003
  kind: primary_source
  reference: DOI:10.1128/jb.174.22.7463-7469.1992
  locator: Aligned on evidence[0] (Durmaz et al. subcloned the Prf determinant from
    the Lactococcus lactis ME2 conjugative plasmid pTN20 (PMID:1429469 / DOI:10.1128/jb.174.22.7463-7469.1992).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1128/jb.174.22.7463-7469.1992 verified
    via existing verbatim quote (Durmaz et al. subcloned the Prf determinant from
    the Lactococcus lactis ME2 conjugative plasmid pTN20 (PMID:1429469 / DOI:10.1128/jb.174.22.7463-7469.1992).)
    and aligned in record-level evidence[0].
  quote: The genetic determinant for Prf (phage resistance five) was subcloned from
    the conjugative plasmid pTN20
- evidence_id: ev-c7s5-def-src-004
  kind: primary_source
  reference: DOI:10.1128/aem.61.5.2023-2026.1995
  locator: Aligned on evidence[0] (McLandsborough et al. cloned the pBF61-derived
    fragment from Lactococcus lactis subsp. lactis KR5 and showed that it conferred
    an Abi phenotype (PMID:7646042 / DOI:10.1128/aem.61.5.2023-2026.1995).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1128/aem.61.5.2023-2026.1995 verified
    via existing verbatim quote (McLandsborough et al. cloned the pBF61-derived fragment
    from Lactococcus lactis subsp. lactis KR5 and showed that it conferred an Abi
    phenotype (PMID:7646042 / DOI:10.1128/aem.61.5.2023-2026.1995).) and aligned in
    record-level evidence[0].
  quote: A 6.3-kb fragment from pBF61 in Lactococcus lactis subsp. lactis KR5 was
    cloned and found to confer an abortive phage infection (Abi+) phenotype
- evidence_id: ev-c7s5-def-src-005
  kind: primary_source
  reference: DOI:10.1016/S0168-1656(97)01692-1
  locator: Aligned on evidence[0] (Su et al. identified plasmid pND852 from Lactococcus
    lactis M138 as the source of the abiI-associated phage resistance locus (PMID:9195753
    / DOI:10.1016/S0168-1656(97)01692-1).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1016/S0168-1656(97)01692-1 verified via
    existing verbatim quote (Su et al. identified plasmid pND852 from Lactococcus
    lactis M138 as the source of the abiI-associated phage resistance locus (PMID:9195753
    / DOI:10.1016/S0168-1656(97)01692-1).) and aligned in record-level evidence[0].
  quote: Plasmid pND852 (56 kb) encodes nisin resistance and was isolated from Lactococcus
    lactis ssp lactis (L. lactis) M138 by conjugation to L. lactis LM0230
- evidence_id: ev-c7s5-def-src-006
  kind: primary_source
  reference: DOI:10.1128/AEM.66.6.2647-2651.2000
  locator: Aligned on evidence[0] (Twomey et al. identify native Lactococcus lactis
    plasmid pKR223 as the source of a restriction-modification system and a separate
    abortive-infection determinant (PMID:10831451 / DOI:10.1128/AEM.66.6.2647-2651.2000).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1128/AEM.66.6.2647-2651.2000 verified
    via existing verbatim quote (Twomey et al. identify native Lactococcus lactis
    plasmid pKR223 as the source of a restriction-modification system and a separate
    abortive-infection determinant (PMID:10831451 / DOI:10.1128/AEM.66.6.2647-2651.2000).)
    and aligned in record-level evidence[0].
  quote: The native lactococcal plasmid pKR223 encodes two distinct phage resistance
    mechanisms, a restriction and modification (R/M) system designated LlaKR2I and
    an abortive infection mechanism (Abi) which affects prolate-headed-phage proliferation
- evidence_id: ev-c7s5-def-src-007
  kind: primary_source
  reference: DOI:10.1128/AEM.67.11.5225-5232.2001
  locator: Aligned on evidence[0] (Dai et al. identify AbiU as a novel Lactococcus
    lactis abortive-infection system (PMID:11679349 / DOI:10.1128/AEM.67.11.5225-5232.2001).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1128/AEM.67.11.5225-5232.2001 verified
    via existing verbatim quote (Dai et al. identify AbiU as a novel Lactococcus lactis
    abortive-infection system (PMID:11679349 / DOI:10.1128/AEM.67.11.5225-5232.2001).)
    and aligned in record-level evidence[0].
  quote: This study reports on the identification and characterization of a novel
    abortive infection system, AbiU, from Lactococcus lactis.
- evidence_id: ev-c7s5-def-src-008
  kind: primary_source
  reference: DOI:10.1021/bi0495026
  locator: Aligned on evidence[0] (Copeland et al. support host Lit as a T4-activated
    bacteriophage-exclusion peptidase that cleaves EF-Tu and leads to cell death (PMID:15196039
    / DOI:10.1021/bi0495026).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1021/bi0495026 verified via existing verbatim
    quote (Copeland et al. support host Lit as a T4-activated bacteriophage-exclusion
    peptidase that cleaves EF-Tu and leads to cell death (PMID:15196039 / DOI:10.1021/bi0495026).)
    and aligned in record-level evidence[0].
  quote: Bacteriophage exclusion is a suicide response to viral infection. In strains
    of Escherichia coli K-12 infected with T4 phage this process is mediated by the
    host-encoded Lit peptidase. Lit is activated by a unique sequence in the major
    head protein of the T4 phage (the Gol sequence) which then cleaves site-specifically
    the host translation factor EF-Tu, ultimately leading to cell death.
- evidence_id: ev-c7s5-def-src-009
  kind: primary_source
  reference: DOI:10.1101/2023.05.28.542683
  locator: Aligned on evidence[0] (Wein et al. support bacterial CARD-like domains
    as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921
    / DOI:10.1101/2023.05.28.542683).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1101/2023.05.28.542683 verified via existing
    verbatim quote (Wein et al. support bacterial CARD-like domains as parts of anti-phage
    defense systems (https://europepmc.org/article/PPR/PPR668921 / DOI:10.1101/2023.05.28.542683).)
    and aligned in record-level evidence[0].
  quote: Here we show that CARD-like domains are present in defense systems that protect
    bacteria against phage.
- evidence_id: ev-c7s5-def-src-010
  kind: primary_source
  reference: DOI:10.1016/j.cell.2023.04.015
  locator: Aligned on evidence[0] (Kibby et al. support NACHT-module proteins as bacterial
    NLR-related proteins that defend against phages (https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/
    / DOI:10.1016/j.cell.2023.04.015).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1016/j.cell.2023.04.015 verified via existing
    verbatim quote (Kibby et al. support NACHT-module proteins as bacterial NLR-related
    proteins that defend against phages (https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/
    / DOI:10.1016/j.cell.2023.04.015).) and aligned in record-level evidence[0].
  quote: Here we show that proteins containing a NACHT module, the central feature
    of the animal nucleotide-binding domain and leucine-rich repeat-containing gene
    family (NLRs), are found in bacteria and defend against phages.
- evidence_id: ev-c7s5-def-src-011
  kind: primary_source
  reference: DOI:10.1038/s41564-025-02239-6
  locator: Aligned on evidence[0] (Goedecke et al. report that T7 gp17 and additional
    tail fiber proteins activated the previously undescribed PD-T2-1 antiphage system
    (https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/ / DOI:10.1038/s41564-025-02239-6).)
  accessed_at: '2026-10-30T22:12:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/s41564-025-02239-6 verified via existing
    verbatim quote (Goedecke et al. report that T7 gp17 and additional tail fiber
    proteins activated the previously undescribed PD-T2-1 antiphage system (https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/
    / DOI:10.1038/s41564-025-02239-6).) and aligned in record-level evidence[0].
  quote: Two phage proteins were further investigated, revealing T7 gp17 and additional
    tail fiber proteins activated the undescribed antiphage system PD-T2–1 and identifying
    λ gpE major capsid protein activated the antiphage system Avs8.
- evidence_id: ev-remediated-records
  kind: record_content
  reference: data/traits/genomics/abia_system.yaml; data/traits/genomics/abib_system.yaml;
    data/traits/genomics/abic_system.yaml; data/traits/genomics/abid_system.yaml;
    data/traits/genomics/abii_system.yaml; data/traits/genomics/abir_system.yaml;
    data/traits/genomics/abiu_system.yaml; data/traits/genomics/lit_system.yaml; data/traits/genomics/card_nlr_endonuclease_system.yaml;
    data/traits/genomics/card_nlr_gasdermin_system.yaml; data/traits/genomics/card_nlr_phospho_system.yaml;
    data/traits/genomics/card_nlr_subtilase_system.yaml; data/traits/genomics/card_nlr_system.yaml;
    data/traits/genomics/nlr_like_bnacht_system.yaml; data/traits/genomics/pd_t2_1_system.yaml
  locator: definition_source, evidence[0], curation_history
  accessed_at: '2026-10-30T22:13:00Z'
  support: supports
  summary: All 15 remediated TraitRecord YAML files now align record-level evidence[0].reference
    with their declared definition_source DOI, preserve their verified non-elliptical
    verbatim snippet, and record an append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE
    curation_history event.
- evidence_id: ev-stage5-writer
  kind: validation
  reference: scripts/curate_stage5_review_findings.py; tests/test_curate_stage5_review_findings.py
  locator: process_all
  accessed_at: '2026-10-30T22:13:00Z'
  support: supports
  summary: Guarded writer script and unit test suite verifying closed-mode LinkML
    validation, DO_NOT_WORK exclusion, and idempotent remediation across all 80 target
    specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4 + 7 Cycle 5 + 13 Cycle
    6 + 15 Cycle 7).
  snapshot_sha256: bc2d52b7f2ecd893006523025b45f44a1edcf8ec7ca4188960c1b4fe94ba283f
- evidence_id: ev-validate-strict
  kind: validation
  reference: scripts/validate_strict.py
  locator: reports/instance_validation_failures.tsv
  accessed_at: '2026-10-30T22:14:00Z'
  support: supports
  summary: Closed-mode LinkML schema and identifier validation passes with 0 errors
    across all 1,130 TraitRecord files.
- evidence_id: ev-snippet-audit
  kind: validation
  reference: scripts/audit_evidence_snippets.py
  locator: conf/evidence_snippet_baseline.tsv
  accessed_at: '2026-10-30T22:14:00Z'
  support: supports
  summary: All 15 remediated record-level evidence[0] entries pass contiguous verbatim
    quote checks with 0 new warnings and eliminate all 15 open definition_source CURIE
    alignment findings from Cycle 7 Stage 4.
assessments:
- assessment_id: assess-remediated-evidence-alignment
  area: evidence
  topic: Verification of record-level definition_source evidence[0] CURIE and verbatim
    snippet alignment across the 15 remediated records
  outcome: supported
  summary: All 15 DefenseFinder genomics records identified with open findings in
    Cycle 7 Stage 4 (abia_system.yaml, abib_system.yaml, abic_system.yaml, abid_system.yaml,
    abii_system.yaml, abir_system.yaml, abiu_system.yaml, lit_system.yaml, card_nlr_endonuclease_system.yaml,
    card_nlr_gasdermin_system.yaml, card_nlr_phospho_system.yaml, card_nlr_subtilase_system.yaml,
    card_nlr_system.yaml, nlr_like_bnacht_system.yaml, and pd_t2_1_system.yaml) now
    align record-level evidence[0].reference with their primary definition_source
    DOI and carry a verified non-elliptical verbatim snippet directly in record-level
    evidence[0].
  target_ids:
  - traitmech:000344
  - traitmech:000319
  - traitmech:000320
  - traitmech:000318
  - traitmech:000316
  - traitmech:000317
  - traitmech:000321
  - traitmech:000363
  - traitmech:000550
  - traitmech:000555
  - traitmech:000551
  - traitmech:000553
  - traitmech:000337
  - traitmech:000408
  - traitmech:000476
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-001
  - ev-c7s5-def-src-002
  - ev-c7s5-def-src-003
  - ev-c7s5-def-src-004
  - ev-c7s5-def-src-005
  - ev-c7s5-def-src-006
  - ev-c7s5-def-src-007
  - ev-c7s5-def-src-008
  - ev-c7s5-def-src-009
  - ev-c7s5-def-src-010
  - ev-c7s5-def-src-011
  - ev-remediated-records
  - ev-snippet-audit
  metrics:
  - name: remediated_open_findings_rate
    value: 1.0
    unit: ratio
    definition: Fraction of Cycle 7 Stage 4 open findings in group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
      verified as resolved with verbatim definition_source evidence.
    denominator: 15
    minimum: 0.0
    maximum: 1.0
  details: 'Each of the 15 remediated records was re-inspected against .claude/skills/review-yaml-record/SKILL.md:
    (1) F-C7S4-DEF-SRC-001..008 (abia_system.yaml, abib_system.yaml, abic_system.yaml,
    abid_system.yaml, abii_system.yaml, abir_system.yaml, abiu_system.yaml, lit_system.yaml)
    now align evidence[0].reference with their primary lactococcal/E. coli abortive
    infection definition_source DOIs while preserving their verified verbatim abstract
    snippets and PMID aliases; (2) F-C7S4-DEF-SRC-009..013 (card_nlr_endonuclease_system.yaml,
    card_nlr_gasdermin_system.yaml, card_nlr_phospho_system.yaml, card_nlr_subtilase_system.yaml,
    card_nlr_system.yaml) now align evidence[0].reference with definition_source DOI:10.1101/2023.05.28.542683
    (from https://europepmc.org/article/PPR/PPR668921); (3) F-C7S4-DEF-SRC-014 (nlr_like_bnacht_system.yaml)
    aligns evidence[0].reference with definition_source DOI:10.1016/j.cell.2023.04.015
    (from https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/); and (4) F-C7S4-DEF-SRC-015
    (pd_t2_1_system.yaml) aligns evidence[0].reference with definition_source DOI:10.1038/s41564-025-02239-6
    (from https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/).'
- assessment_id: assess-remediated-schema-and-provenance
  area: provenance
  topic: Schema validity, curation_history provenance, and writer guardrails on remediated
    records
  outcome: supported
  summary: 'All 15 remediated records pass strict closed-mode LinkML validation, preserve
    existing canonical_examples, causal_graphs, and UniProtKB protein_examples untouched,
    and record append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history
    entries referencing issue #2002.'
  target_ids:
  - traitmech:000344
  - traitmech:000319
  - traitmech:000320
  - traitmech:000318
  - traitmech:000316
  - traitmech:000317
  - traitmech:000321
  - traitmech:000363
  - traitmech:000550
  - traitmech:000555
  - traitmech:000551
  - traitmech:000553
  - traitmech:000337
  - traitmech:000408
  - traitmech:000476
  evidence_ids:
  - ev-remediated-records
  - ev-stage5-writer
  - ev-validate-strict
findings:
- finding_id: F-C7S4-DEF-SRC-001
  issue_key: abia-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: abia_system.yaml now aligns record-level evidence[0].reference with definition_source
    DOI:10.1128/aem.60.4.1129-1136.1994 carrying a verified verbatim snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-001 on data/traits/genomics/abia_system.yaml
    (traitmech:000344): aligned record-level evidence[0].reference from PMID:16349225
    to definition_source DOI:10.1128/aem.60.4.1129-1136.1994 while preserving the
    verified verbatim snippet (''The abiA gene (formerly hsp) encodes an abortive
    phage infection mechanism which inhibits phage DNA replication.'') (Dinsmore and
    Klaenhammer describe abiA as the former hsp abortive-infection determinant and
    connect AbiA activity to inhibition of phage DNA replication (PMID:16349225 /
    DOI:10.1128/aem.60.4.1129-1136.1994).) and appended curation_history entry via
    scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000344
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-001
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abia_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-001
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-002
  issue_key: abib-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: abib_system.yaml now aligns record-level evidence[0].reference with definition_source
    DOI:10.1046/j.1365-2958.1996.371896.x carrying a verified verbatim snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-002 on data/traits/genomics/abib_system.yaml
    (traitmech:000319): aligned record-level evidence[0].reference from PMID:8825768
    to definition_source DOI:10.1046/j.1365-2958.1996.371896.x while preserving the
    verified verbatim snippet (''The abortive infection determinant AbiB prevents
    growth of the sensitive phage bIL170, but not of the resistant phage bIL41, on
    Lactococcus lactis strain IL1403'') (Parreira et al. place AbiB in the abortive-infection
    class and show that it blocks the sensitive lactococcal phage bIL170 on Lactococcus
    lactis IL1403 (PMID:8825768 / DOI:10.1046/j.1365-2958.1996.371896.x).) and appended
    curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000319
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-002
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abib_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-002
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-003
  issue_key: abic-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: abic_system.yaml now aligns record-level evidence[0].reference with definition_source
    DOI:10.1128/jb.174.22.7463-7469.1992 carrying a verified verbatim snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-003 on data/traits/genomics/abic_system.yaml
    (traitmech:000320): aligned record-level evidence[0].reference from PMID:1429469
    to definition_source DOI:10.1128/jb.174.22.7463-7469.1992 while preserving the
    verified verbatim snippet (''The genetic determinant for Prf (phage resistance
    five) was subcloned from the conjugative plasmid pTN20'') (Durmaz et al. subcloned
    the Prf determinant from the Lactococcus lactis ME2 conjugative plasmid pTN20
    (PMID:1429469 / DOI:10.1128/jb.174.22.7463-7469.1992).) and appended curation_history
    entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000320
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-003
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abic_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-003
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-004
  issue_key: abid-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: abid_system.yaml now aligns record-level evidence[0].reference with definition_source
    DOI:10.1128/aem.61.5.2023-2026.1995 carrying a verified verbatim snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-004 on data/traits/genomics/abid_system.yaml
    (traitmech:000318): aligned record-level evidence[0].reference from PMID:7646042
    to definition_source DOI:10.1128/aem.61.5.2023-2026.1995 while preserving the
    verified verbatim snippet (''A 6.3-kb fragment from pBF61 in Lactococcus lactis
    subsp. lactis KR5 was cloned and found to confer an abortive phage infection (Abi+)
    phenotype'') (McLandsborough et al. cloned the pBF61-derived fragment from Lactococcus
    lactis subsp. lactis KR5 and showed that it conferred an Abi phenotype (PMID:7646042
    / DOI:10.1128/aem.61.5.2023-2026.1995).) and appended curation_history entry via
    scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000318
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-004
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abid_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-004
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-005
  issue_key: abii-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: abii_system.yaml now aligns record-level evidence[0].reference with definition_source
    DOI:10.1016/S0168-1656(97)01692-1 carrying a verified verbatim snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-005 on data/traits/genomics/abii_system.yaml
    (traitmech:000316): aligned record-level evidence[0].reference from PMID:9195753
    to definition_source DOI:10.1016/S0168-1656(97)01692-1 while preserving the verified
    verbatim snippet (''Plasmid pND852 (56 kb) encodes nisin resistance and was isolated
    from Lactococcus lactis ssp lactis (L. lactis) M138 by conjugation to L. lactis
    LM0230'') (Su et al. identified plasmid pND852 from Lactococcus lactis M138 as
    the source of the abiI-associated phage resistance locus (PMID:9195753 / DOI:10.1016/S0168-1656(97)01692-1).)
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000316
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-005
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abii_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-005
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-006
  issue_key: abir-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: abir_system.yaml now aligns record-level evidence[0].reference with definition_source
    DOI:10.1128/AEM.66.6.2647-2651.2000 carrying a verified verbatim snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-006 on data/traits/genomics/abir_system.yaml
    (traitmech:000317): aligned record-level evidence[0].reference from PMID:10831451
    to definition_source DOI:10.1128/AEM.66.6.2647-2651.2000 while preserving the
    verified verbatim snippet (''The native lactococcal plasmid pKR223 encodes two
    distinct phage resistance mechanisms, a restriction and modification (R/M) system
    designated LlaKR2I and an abortive infection mechanism (Abi) which affects prolate-headed-phage
    proliferation'') (Twomey et al. identify native Lactococcus lactis plasmid pKR223
    as the source of a restriction-modification system and a separate abortive-infection
    determinant (PMID:10831451 / DOI:10.1128/AEM.66.6.2647-2651.2000).) and appended
    curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000317
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-006
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abir_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-006
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-007
  issue_key: abiu-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: abiu_system.yaml now aligns record-level evidence[0].reference with definition_source
    DOI:10.1128/AEM.67.11.5225-5232.2001 carrying a verified verbatim snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-007 on data/traits/genomics/abiu_system.yaml
    (traitmech:000321): aligned record-level evidence[0].reference from PMID:11679349
    to definition_source DOI:10.1128/AEM.67.11.5225-5232.2001 while preserving the
    verified verbatim snippet (''This study reports on the identification and characterization
    of a novel abortive infection system, AbiU, from Lactococcus lactis.'') (Dai et
    al. identify AbiU as a novel Lactococcus lactis abortive-infection system (PMID:11679349
    / DOI:10.1128/AEM.67.11.5225-5232.2001).) and appended curation_history entry
    via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000321
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-007
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/abiu_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-007
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-008
  issue_key: lit-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: lit_system.yaml now aligns record-level evidence[0].reference with definition_source
    DOI:10.1021/bi0495026 carrying a verified verbatim snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-008 on data/traits/genomics/lit_system.yaml
    (traitmech:000363): aligned record-level evidence[0].reference from PMID:15196039
    to definition_source DOI:10.1021/bi0495026 while preserving the verified verbatim
    snippet (''Bacteriophage exclusion is a suicide response to viral infection. In
    strains of Escherichia coli K-12 infected with T4 phage this process is mediated
    by the host-encoded Lit peptidase. Lit is activated by a unique sequence in the
    major head protein of the T4 phage (the Gol sequence) which then cleaves site-specifically
    the host translation factor EF-Tu, ultimately leading to cell death.'') (Copeland
    et al. support host Lit as a T4-activated bacteriophage-exclusion peptidase that
    cleaves EF-Tu and leads to cell death (PMID:15196039 / DOI:10.1021/bi0495026).)
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000363
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-008
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/lit_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-008
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-009
  issue_key: card-nlr-endonuclease-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: card_nlr_endonuclease_system.yaml now aligns record-level evidence[0].reference
    with definition_source DOI:10.1101/2023.05.28.542683 carrying a verified verbatim
    snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-009 on data/traits/genomics/card_nlr_endonuclease_system.yaml
    (traitmech:000550): aligned record-level evidence[0].reference from https://europepmc.org/article/PPR/PPR668921
    to definition_source DOI:10.1101/2023.05.28.542683 while preserving the verified
    verbatim snippet (''Here we show that CARD-like domains are present in defense
    systems that protect bacteria against phage.'') (Wein et al. support bacterial
    CARD-like domains as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921
    / DOI:10.1101/2023.05.28.542683).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000550
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/card_nlr_endonuclease_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-009
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-010
  issue_key: card-nlr-gasdermin-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: card_nlr_gasdermin_system.yaml now aligns record-level evidence[0].reference
    with definition_source DOI:10.1101/2023.05.28.542683 carrying a verified verbatim
    snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-010 on data/traits/genomics/card_nlr_gasdermin_system.yaml
    (traitmech:000555): aligned record-level evidence[0].reference from https://europepmc.org/article/PPR/PPR668921
    to definition_source DOI:10.1101/2023.05.28.542683 while preserving the verified
    verbatim snippet (''Here we show that CARD-like domains are present in defense
    systems that protect bacteria against phage.'') (Wein et al. support bacterial
    CARD-like domains as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921
    / DOI:10.1101/2023.05.28.542683).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000555
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/card_nlr_gasdermin_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-010
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-011
  issue_key: card-nlr-phospho-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: card_nlr_phospho_system.yaml now aligns record-level evidence[0].reference
    with definition_source DOI:10.1101/2023.05.28.542683 carrying a verified verbatim
    snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-011 on data/traits/genomics/card_nlr_phospho_system.yaml
    (traitmech:000551): aligned record-level evidence[0].reference from https://europepmc.org/article/PPR/PPR668921
    to definition_source DOI:10.1101/2023.05.28.542683 while preserving the verified
    verbatim snippet (''Here we show that CARD-like domains are present in defense
    systems that protect bacteria against phage.'') (Wein et al. support bacterial
    CARD-like domains as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921
    / DOI:10.1101/2023.05.28.542683).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000551
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/card_nlr_phospho_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-011
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-012
  issue_key: card-nlr-subtilase-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: card_nlr_subtilase_system.yaml now aligns record-level evidence[0].reference
    with definition_source DOI:10.1101/2023.05.28.542683 carrying a verified verbatim
    snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-012 on data/traits/genomics/card_nlr_subtilase_system.yaml
    (traitmech:000553): aligned record-level evidence[0].reference from https://europepmc.org/article/PPR/PPR668921
    to definition_source DOI:10.1101/2023.05.28.542683 while preserving the verified
    verbatim snippet (''Here we show that CARD-like domains are present in defense
    systems that protect bacteria against phage.'') (Wein et al. support bacterial
    CARD-like domains as parts of anti-phage defense systems (https://europepmc.org/article/PPR/PPR668921
    / DOI:10.1101/2023.05.28.542683).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000553
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/card_nlr_subtilase_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-012
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-013
  issue_key: card-nlr-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: card_nlr_system.yaml now aligns record-level evidence[0].reference with definition_source
    DOI:10.1101/2023.05.28.542683 carrying a verified verbatim snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-013 on data/traits/genomics/card_nlr_system.yaml
    (traitmech:000337): aligned record-level evidence[0].reference from https://europepmc.org/article/PPR/PPR668921
    to definition_source DOI:10.1101/2023.05.28.542683 while preserving the verified
    verbatim snippet (''Here we show that CARD-like domains are present in defense
    systems that protect bacteria against phage.'') (The Wein et al. abstract supports
    CARD-like-domain systems as bacterial phage-defense systems (https://europepmc.org/article/PPR/PPR668921
    / DOI:10.1101/2023.05.28.542683).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000337
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/card_nlr_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-013
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-014
  issue_key: nlr-like-bnacht-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: nlr_like_bnacht_system.yaml now aligns record-level evidence[0].reference
    with definition_source DOI:10.1016/j.cell.2023.04.015 carrying a verified verbatim
    snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-014 on data/traits/genomics/nlr_like_bnacht_system.yaml
    (traitmech:000408): aligned record-level evidence[0].reference from https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/
    to definition_source DOI:10.1016/j.cell.2023.04.015 while preserving the verified
    verbatim snippet (''Here we show that proteins containing a NACHT module, the
    central feature of the animal nucleotide-binding domain and leucine-rich repeat-containing
    gene family (NLRs), are found in bacteria and defend against phages.'') (Kibby
    et al. support NACHT-module proteins as bacterial NLR-related proteins that defend
    against phages (https://pmc.ncbi.nlm.nih.gov/articles/PMC10294775/ / DOI:10.1016/j.cell.2023.04.015).)
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000408
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-010
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/nlr_like_bnacht_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-014
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C7S4-DEF-SRC-015
  issue_key: pd-t2-1-system-definition-source-curie-alignment
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: pd_t2_1_system.yaml now aligns record-level evidence[0].reference with definition_source
    DOI:10.1038/s41564-025-02239-6 carrying a verified verbatim snippet
  description: 'Resolved Cycle 7 Stage 4 open finding F-C7S4-DEF-SRC-015 on data/traits/genomics/pd_t2_1_system.yaml
    (traitmech:000476): aligned record-level evidence[0].reference from https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/
    to definition_source DOI:10.1038/s41564-025-02239-6 while preserving the verified
    verbatim snippet (''Two phage proteins were further investigated, revealing T7
    gp17 and additional tail fiber proteins activated the undescribed antiphage system
    PD-T2–1 and identifying λ gpE major capsid protein activated the antiphage system
    Avs8.'') (Goedecke et al. report that T7 gp17 and additional tail fiber proteins
    activated the previously undescribed PD-T2-1 antiphage system (https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/
    / DOI:10.1038/s41564-025-02239-6).) and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000476
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c7s4-review
  - ev-c7s5-def-src-011
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/pd_t2_1_system.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 7 Stage 5 (resolve_review_findings) under
    group G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
    finding_id: F-C7S4-DEF-SRC-015
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
actions: []
limitations:
- 'This batch review covers the 15 records remediated in Cycle 7 Stage 5 under group
  G-C7S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002); the 5 cohort-level source-limited
  or upstream-blocked findings from Cycle 7 Stage 4 remain tracked under open GitHub
  issues #1982, #1983, #1984, #1985, and #364.'
- All 15 of the remediated records carry repository-minted traitmech:NNNNNN identifiers
  (traitmech:000316..000321, traitmech:000337, traitmech:000344, traitmech:000363,
  traitmech:000408, traitmech:000476, traitmech:000550, traitmech:000551, traitmech:000553,
  traitmech:000555) backed by validated ROBOT templates awaiting upstream METPO release
  incorporation (#364, berkeleybop/metpo#535).
notes:
- 'Skills executed: .claude/skills/curate-yaml-record/SKILL.md and .claude/skills/review-yaml-record/SKILL.md.'
- Immutable Cycle 7 Stage 4 review bundle preserved untouched at reviews/structured/20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review/review.yaml.
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261030T112000Z-cycle7-stage4-corpus-record-and-cohort-review
  relationship: follow_up_remediation_verification
links:
- https://github.com/CultureBotAI/TraitMech/issues/2002
- https://github.com/CultureBotAI/TraitMech/issues/1982
- https://github.com/CultureBotAI/TraitMech/issues/1983
- https://github.com/CultureBotAI/TraitMech/issues/1984
- https://github.com/CultureBotAI/TraitMech/issues/1985
- https://github.com/CultureBotAI/TraitMech/issues/364
tags:
- cycle-07
- stage-05
- resolve-review-findings
- remediation-verification
```
