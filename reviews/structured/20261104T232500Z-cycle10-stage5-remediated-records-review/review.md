# Cycle 10 Stage 5 post-remediation verification review of the 14 morphology TraitRecord files in group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS

- Review: 20261104T232500Z-cycle10-stage5-remediated-records-review
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-11-04T23:20:00Z
- Finished UTC: 2026-11-04T23:25:00Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Fresh post-remediation batch review of the 14 morphology TraitRecord YAML files remediated in Cycle 10 Stage 5 (capsule.yaml, carboxysome.yaml, gas_vesicle.yaml, heterocyst.yaml, intracellular_inclusion.yaml, magnetosome.yaml, mycelial_growth.yaml, polyhydroxyalkanoate_granule.yaml, polyphosphate_granule.yaml, prosthecate.yaml, s_layer.yaml, sulfur_globule.yaml, swarming_motility.yaml, and twitching_motility.yaml) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002. All 14 Cycle 10 Stage 4 open findings (F-C10S4-DEF-SRC-001..014) are verified as resolved with contiguous verbatim snippets for their primary definition_source DOI in record-level evidence[0], removal of all 14 baselined MISSING_SNIPPET rows from conf/evidence_snippet_baseline.tsv (2,363 -&gt; 2,349 total baselined findings; MISSING_SNIPPET 2,225 -&gt; 2,211), append-only curation_history provenance, and 0 remaining open findings.

## Scope And Provenance

Focused post-remediation review of all 14 morphology TraitRecord YAML files modified in Cycle 10 Stage 5 (resolve_review_findings) to resolve group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002).

Selection: All 14 records with open findings carried forward from Cycle 10 Stage 4 review 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review.
Coverage: full; 14 reviewed / 14 in the declared population.
Source: working_tree at Git base 013a72e1bdd9d3f5dcaac757e08a5ae1cad881c8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000063 | data/traits/morphology/capsule.yaml | maintained | capsule |
| traitmech:000072 | data/traits/morphology/carboxysome.yaml | maintained | carboxysome |
| traitmech:000070 | data/traits/morphology/gas_vesicle.yaml | maintained | gas vesicle |
| traitmech:000073 | data/traits/morphology/heterocyst.yaml | maintained | heterocyst |
| traitmech:000066 | data/traits/morphology/intracellular_inclusion.yaml | maintained | intracellular inclusion |
| traitmech:000071 | data/traits/morphology/magnetosome.yaml | maintained | magnetosome |
| traitmech:000074 | data/traits/morphology/mycelial_growth.yaml | maintained | mycelial growth |
| traitmech:000067 | data/traits/morphology/polyhydroxyalkanoate_granule.yaml | maintained | polyhydroxyalkanoate granule |
| traitmech:000068 | data/traits/morphology/polyphosphate_granule.yaml | maintained | polyphosphate granule |
| traitmech:000065 | data/traits/morphology/prosthecate.yaml | maintained | prosthecate |
| traitmech:000064 | data/traits/morphology/s_layer.yaml | maintained | S-layer |
| traitmech:000069 | data/traits/morphology/sulfur_globule.yaml | maintained | sulfur globule |
| traitmech:000062 | data/traits/morphology/swarming_motility.yaml | maintained | swarming motility |
| traitmech:000061 | data/traits/morphology/twitching_motility.yaml | maintained | twitching motility |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict LinkML schema and reference validation across all TraitRecord files | passed | True | traitmech:000063, traitmech:000072, traitmech:000070, traitmech:000073, traitmech:000066, traitmech:000071, traitmech:000074, traitmech:000067, traitmech:000068, traitmech:000065, traitmech:000064, traitmech:000069, traitmech:000062, traitmech:000061 | All 1,130 TraitRecord YAML files (including all 14 Cycle 10 Stage 5 remediated morphology records) pass strict closed-mode LinkML validation with 0 errors. |
| Evidence snippet structural and baseline ratchet audit | passed | True | traitmech:000063, traitmech:000072, traitmech:000070, traitmech:000073, traitmech:000066, traitmech:000071, traitmech:000074, traitmech:000067, traitmech:000068, traitmech:000065, traitmech:000064, traitmech:000069, traitmech:000062, traitmech:000061 | All 14 remediated morphology records now carry a contiguous &gt;=16-char verbatim quote for their primary definition_source DOI in record-level evidence[0], passing scripts/audit_evidence_snippets.py with 0 new findings and reducing baselined MISSING_SNIPPET rows in conf/evidence_snippet_baseline.tsv from 2,225 to 2,211 (-14; total baselined findings 2,363 -&gt; 2,349). |
| Stage 5 guarded writer idempotency and postcondition unit tests | passed | True | traitmech:000063, traitmech:000072, traitmech:000070, traitmech:000073, traitmech:000066, traitmech:000071, traitmech:000074, traitmech:000067, traitmech:000068, traitmech:000065, traitmech:000064, traitmech:000069, traitmech:000062, traitmech:000061 | All 5 unit tests in tests/test_curate_stage5_review_findings.py pass, confirming DO_NOT_WORK protection, exact definition_source evidence alignment across all 115 remediated specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4 + 7 Cycle 5 + 13 Cycle 6 + 15 Cycle 7 + 12 Cycle 8 + 9 Cycle 9 + 14 Cycle 10), zero UNQUOTED_DEFINITION_SOURCE or MISSING_DEFINITION_SOURCE_EVIDENCE defects on remediated records, and dry-run/apply idempotency. |
| Guarded YAML writer safeguard audit | passed | True | traitmech:000063, traitmech:000072, traitmech:000070, traitmech:000073, traitmech:000066, traitmech:000071, traitmech:000074, traitmech:000067, traitmech:000068, traitmech:000065, traitmech:000064, traitmech:000069, traitmech:000062, traitmech:000061 | scripts/curate_stage5_review_findings.py satisfies all writer safeguards (appends curation_history, has write safeguard, validates before write, wired into justfile). |

## Scientific And Domain Assessments

### Verification of record-level definition_source evidence[0] verbatim snippet alignment across the 14 remediated morphology records

evidence: supported. Targets: traitmech:000063, traitmech:000072, traitmech:000070, traitmech:000073, traitmech:000066, traitmech:000071, traitmech:000074, traitmech:000067, traitmech:000068, traitmech:000065, traitmech:000064, traitmech:000069, traitmech:000062, traitmech:000061.

All 14 morphology records identified with open findings in Cycle 10 Stage 4 (capsule.yaml, carboxysome.yaml, gas_vesicle.yaml, heterocyst.yaml, intracellular_inclusion.yaml, magnetosome.yaml, mycelial_growth.yaml, polyhydroxyalkanoate_granule.yaml, polyphosphate_granule.yaml, prosthecate.yaml, s_layer.yaml, sulfur_globule.yaml, swarming_motility.yaml, and twitching_motility.yaml) now carry a verified non-elliptical verbatim snippet directly in record-level evidence[0].snippet for their primary definition_source DOI.

Each of the 14 remediated morphology records was re-inspected against .claude/skills/review-yaml-record/SKILL.md: F-C10S4-DEF-SRC-001..014 (capsule.yaml [DOI:10.1146/annurev.micro.50.1.285], carboxysome.yaml [DOI:10.1038/nrmicro.2018.10], gas_vesicle.yaml [DOI:10.1038/nrmicro2834], heterocyst.yaml [DOI:10.1101/cshperspect.a000315], intracellular_inclusion.yaml [DOI:10.1038/s41579-020-0413-0], magnetosome.yaml [DOI:10.1038/nrmicro.2016.99], mycelial_growth.yaml [DOI:10.1038/nrmicro1968], polyhydroxyalkanoate_granule.yaml [DOI:10.1128/mr.54.4.450-472.1990], polyphosphate_granule.yaml [DOI:10.1146/annurev.biochem.77.083007.093039], prosthecate.yaml [DOI:10.1111/j.1365-2958.2007.05633.x], s_layer.yaml [DOI:10.1038/nrmicro3213], sulfur_globule.yaml [DOI:10.1016/S0065-2911(08)00002-7], swarming_motility.yaml [DOI:10.1038/nrmicro2405], and twitching_motility.yaml [DOI:10.1146/annurev.micro.56.012302.160938]) now populate evidence[0].snippet with the verified Europe PMC abstract quote for their declared definition_source DOI and have been removed from conf/evidence_snippet_baseline.tsv.

### Schema validity, curation_history provenance, and writer guardrails on remediated records

provenance: supported. Targets: traitmech:000063, traitmech:000072, traitmech:000070, traitmech:000073, traitmech:000066, traitmech:000071, traitmech:000074, traitmech:000067, traitmech:000068, traitmech:000065, traitmech:000064, traitmech:000069, traitmech:000062, traitmech:000061.

All 14 remediated records pass strict closed-mode LinkML validation, preserve existing canonical_examples, causal_graphs, and UniProtKB protein_examples untouched, and record append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history entries referencing issue #2002.

## Findings

### F-C10S4-DEF-SRC-001: capsule.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1146/annurev.micro.50.1.285

minor / resolved / confirmed; issue key: capsule-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-001 on data/traits/morphology/capsule.yaml (traitmech:000063): populated record-level evidence[0].snippet for definition_source DOI:10.1146/annurev.micro.50.1.285 with the verified Europe PMC abstract quote ('Many bacteria are surrounded by a polysaccharide layer outside the outer membrane of Gram-negative bacteria and the peptidoglycan layer of Gram-positive bacteria.') (Roberts reviews the biochemistry, genetics, group I-IV classification, export/assembly pathways (Wzx/Wzy and ABC transporter systems), and virulence roles of bacterial polysaccharide capsules.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-002: carboxysome.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro.2018.10

minor / resolved / confirmed; issue key: carboxysome-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-002 on data/traits/morphology/carboxysome.yaml (traitmech:000072): populated record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro.2018.10 with the verified Europe PMC abstract quote ('Bacterial microcompartments (BMCs) are self-assembling organelles that consist of an enzymatic core that is encapsulated by a selectively permeable protein shell.') (Kerfeld et al. review bacterial microcompartments, with detailed coverage of alpha- and beta-carboxysome shell architecture (BMC-H, BMC-T, BMC-P), RuBisCO/carbonic anhydrase encapsulation, and CO2-concentrating function.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-003: gas_vesicle.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro2834

minor / resolved / confirmed; issue key: gas-vesicle-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-003 on data/traits/morphology/gas_vesicle.yaml (traitmech:000070): populated record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro2834 with the verified Europe PMC abstract quote ('Gas vesicles are hollow, proteinaceous structures that are filled with gas and allow halophilic and methanogenic archaea as well as photosynthetic and heterotrophic bacteria to thrive at vertical positions with favourable growth conditions in watery environments.') (Pfeifer reviews the structure, gvp gene clusters, GvpA/GvpC shell assembly, regulation, and buoyancy function of bacterial and archaeal gas vesicles.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-004: heterocyst.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1101/cshperspect.a000315

minor / resolved / confirmed; issue key: heterocyst-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-004 on data/traits/morphology/heterocyst.yaml (traitmech:000073): populated record-level evidence[0].snippet for definition_source DOI:10.1101/cshperspect.a000315 with the verified Europe PMC abstract quote ('Heterocysts are terminally differentiated nitrogen-fixing cells formed at semiregular intervals along filaments of certain cyanobacteria, such as Anabaena (Nostoc) sp. strain PCC 7120, when fixed nitrogen is limiting.') (Kumar, Mella-Herrera &amp; Golden review cyanobacterial heterocyst differentiation, NtcA/HetR regulatory control, PatS/HetN spacing, envelope glycolipid/polysaccharide layers, and microoxic nitrogen fixation.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-005: intracellular_inclusion.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1038/s41579-020-0413-0

minor / resolved / confirmed; issue key: intracellular-inclusion-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-005 on data/traits/morphology/intracellular_inclusion.yaml (traitmech:000066): populated record-level evidence[0].snippet for definition_source DOI:10.1038/s41579-020-0413-0 with the verified Europe PMC abstract quote ('Prokaryotes synthesize diverse intracellular nanostructures and bodies to compartmentalize metabolic pathways, store reserves and enhance survival under stress.') (Greening &amp; Lithgow review the biogenesis, classification, and physiological functions of prokaryotic intracellular inclusions, storage granules, and microcompartments across bacteria and archaea.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-006: magnetosome.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro.2016.99

minor / resolved / confirmed; issue key: magnetosome-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-006 on data/traits/morphology/magnetosome.yaml (traitmech:000071): populated record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro.2016.99 with the verified Europe PMC abstract quote ('Magnetotactic bacteria (MTB) orient and navigate along geomagnetic field lines, a behaviour that is enabled by magnetosomes — unique intracellular organelles that consist of magnetic iron mineral crystals enclosed by a specialized membrane bilayer.') (Uebe &amp; Schüler review magnetosome membrane invagination, iron uptake and biomineralization, MamK/MamJ chain assembly, and magnetotactic navigation.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-007: mycelial_growth.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro1968

minor / resolved / confirmed; issue key: mycelial-growth-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-007 on data/traits/morphology/mycelial_growth.yaml (traitmech:000074): populated record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro1968 with the verified Europe PMC abstract quote ('Streptomycetes are filamentous bacteria that grow by tip extension and hyphal branching to form a dense vegetative mycelium.') (Flärdh &amp; Buttner review polar tip extension, DivIVA polarisome function, lateral branching, vegetative vs. aerial mycelium differentiation, and sporulation in Streptomyces.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-008: polyhydroxyalkanoate_granule.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1128/mr.54.4.450-472.1990

minor / resolved / confirmed; issue key: polyhydroxyalkanoate-granule-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-008 on data/traits/morphology/polyhydroxyalkanoate_granule.yaml (traitmech:000067): populated record-level evidence[0].snippet for definition_source DOI:10.1128/mr.54.4.450-472.1990 with the verified Europe PMC abstract quote ('Polyhydroxyalkanoates (PHAs) are polyesters of various hydroxyalkanoates that are synthesized by numerous microorganisms and accumulated as intracellular carbon and energy storage granules.') (Anderson &amp; Dawes review the occurrence, biochemistry, PhaA/PhaB/PhaC biosynthetic pathway, and physiological regulation of bacterial polyhydroxyalkanoate storage granules.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-009: polyphosphate_granule.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1146/annurev.biochem.77.083007.093039

minor / resolved / confirmed; issue key: polyphosphate-granule-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-009 on data/traits/morphology/polyphosphate_granule.yaml (traitmech:000068): populated record-level evidence[0].snippet for definition_source DOI:10.1146/annurev.biochem.77.083007.093039 with the verified Europe PMC abstract quote ('Inorganic polyphosphate (poly P) is a linear polymer of many tens or hundreds of orthophosphate (Pi) residues linked by high-energy phosphoanhydride bonds.') (Rao, Gómez-García &amp; Kornberg review polyphosphate kinases (PPK1, PPK2), exopolyphosphatase (PPX), polyphosphate granule storage, and physiological roles in stress survival, motility, and virulence.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-010: prosthecate.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1111/j.1365-2958.2007.05633.x

minor / resolved / confirmed; issue key: prosthecate-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-010 on data/traits/morphology/prosthecate.yaml (traitmech:000065): populated record-level evidence[0].snippet for definition_source DOI:10.1111/j.1365-2958.2007.05633.x with the verified Europe PMC abstract quote ('Prosthecae are narrow extensions of the bacterial cell wall that contain cytoplasm and are bounded by the cell envelope.') (Wagner &amp; Brun review the structure, peptidoglycan synthesis, developmental regulation, and nutrient-acquisition role of bacterial prosthecae (stalks).), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-011: s_layer.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro3213

minor / resolved / confirmed; issue key: s-layer-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-011 on data/traits/morphology/s_layer.yaml (traitmech:000064): populated record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro3213 with the verified Europe PMC abstract quote ('Surface layers (S-layers) are two-dimensional crystalline arrays of protein or glycoprotein subunits that form the outermost cell envelope component of many bacteria and almost all archaea.') (Fagan &amp; Fairweather review S-layer protein secretion, cell-wall anchoring (SLH and CWB2 domains), self-assembly into paracrystalline lattices, and functional roles across Bacteria and Archaea.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-012: sulfur_globule.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1016/S0065-2911(08)00002-7

minor / resolved / confirmed; issue key: sulfur-globule-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-012 on data/traits/morphology/sulfur_globule.yaml (traitmech:000069): populated record-level evidence[0].snippet for definition_source DOI:10.1016/S0065-2911(08)00002-7 with the verified Europe PMC abstract quote ('Many sulfur-oxidizing bacteria form globules of elemental sulfur as an obligate or facultative intermediate during the oxidation of reduced inorganic sulfur compounds such as sulfide and thiosulfate.') (Frigaard &amp; Dahl review the biogenesis, SgpA/SgpB/SgpC protein envelope, chemical speciation, and Dsr-mediated oxidation of bacterial sulfur globules.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-013: swarming_motility.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro2405

minor / resolved / confirmed; issue key: swarming-motility-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-013 on data/traits/morphology/swarming_motility.yaml (traitmech:000062): populated record-level evidence[0].snippet for definition_source DOI:10.1038/nrmicro2405 with the verified Europe PMC abstract quote ('Swarming motility is a rapid, multicellular movement of bacteria across a surface, powered by rotating flagella.') (Kearns reviews bacterial swarming motility, covering hyperflagellation, biosurfactant wetting agents, cell elongation, and surface sensing.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

### F-C10S4-DEF-SRC-014: twitching_motility.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet for definition_source DOI:10.1146/annurev.micro.56.012302.160938

minor / resolved / confirmed; issue key: twitching-motility-definition-source-snippet.

Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-014 on data/traits/morphology/twitching_motility.yaml (traitmech:000061): populated record-level evidence[0].snippet for definition_source DOI:10.1146/annurev.micro.56.012302.160938 with the verified Europe PMC abstract quote ('Twitching motility is a mode of surface translocation mediated by the extension, tethering, and retraction of type IV pili.') (Mattick reviews the genetics, PilA/PilB/PilT/PilQ machinery, extension-retraction mechanics, and physiological roles of type IV pili-mediated twitching motility.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.

Disposition: Resolved in Cycle 10 Stage 5 (resolve_review_findings) under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via guarded writer scripts/curate_stage5_review_findings.py.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-prior-c10s4-review | reviews/structured/20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review/review.yaml; findings[0..13] | supports | Immutable Cycle 10 Stage 4 review bundle identifying the 14 open definition_source missing-snippet findings (F-C10S4-DEF-SRC-001..F-C10S4-DEF-SRC-014) across data/traits/morphology/ with planned remediation actions ACT-C10S4-DEF-SRC-001..014. |
| ev-c10s5-def-src-001 | DOI:10.1146/annurev.micro.50.1.285; Aligned on data/traits/morphology/capsule.yaml evidence[0] (Roberts reviews the biochemistry, genetics, group I-IV classification, export/assembly pathways (Wzx/Wzy and ABC transporter systems), and virulence roles of bacterial polysaccharide capsules.) | supports | Primary definition_source DOI:10.1146/annurev.micro.50.1.285 on data/traits/morphology/capsule.yaml (traitmech:000063, capsule) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Roberts reviews the biochemistry, genetics, group I-IV classification, export/assembly pathways (Wzx/Wzy and ABC transporter systems), and virulence roles of bacterial polysaccharide capsules.). |
| ev-c10s5-def-src-002 | DOI:10.1038/nrmicro.2018.10; Aligned on data/traits/morphology/carboxysome.yaml evidence[0] (Kerfeld et al. review bacterial microcompartments, with detailed coverage of alpha- and beta-carboxysome shell architecture (BMC-H, BMC-T, BMC-P), RuBisCO/carbonic anhydrase encapsulation, and CO2-concentrating function.) | supports | Primary definition_source DOI:10.1038/nrmicro.2018.10 on data/traits/morphology/carboxysome.yaml (traitmech:000072, carboxysome) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Kerfeld et al. review bacterial microcompartments, with detailed coverage of alpha- and beta-carboxysome shell architecture (BMC-H, BMC-T, BMC-P), RuBisCO/carbonic anhydrase encapsulation, and CO2-concentrating function.). |
| ev-c10s5-def-src-003 | DOI:10.1038/nrmicro2834; Aligned on data/traits/morphology/gas_vesicle.yaml evidence[0] (Pfeifer reviews the structure, gvp gene clusters, GvpA/GvpC shell assembly, regulation, and buoyancy function of bacterial and archaeal gas vesicles.) | supports | Primary definition_source DOI:10.1038/nrmicro2834 on data/traits/morphology/gas_vesicle.yaml (traitmech:000070, gas vesicle) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Pfeifer reviews the structure, gvp gene clusters, GvpA/GvpC shell assembly, regulation, and buoyancy function of bacterial and archaeal gas vesicles.). |
| ev-c10s5-def-src-004 | DOI:10.1101/cshperspect.a000315; Aligned on data/traits/morphology/heterocyst.yaml evidence[0] (Kumar, Mella-Herrera &amp; Golden review cyanobacterial heterocyst differentiation, NtcA/HetR regulatory control, PatS/HetN spacing, envelope glycolipid/polysaccharide layers, and microoxic nitrogen fixation.) | supports | Primary definition_source DOI:10.1101/cshperspect.a000315 on data/traits/morphology/heterocyst.yaml (traitmech:000073, heterocyst) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Kumar, Mella-Herrera &amp; Golden review cyanobacterial heterocyst differentiation, NtcA/HetR regulatory control, PatS/HetN spacing, envelope glycolipid/polysaccharide layers, and microoxic nitrogen fixation.). |
| ev-c10s5-def-src-005 | DOI:10.1038/s41579-020-0413-0; Aligned on data/traits/morphology/intracellular_inclusion.yaml evidence[0] (Greening &amp; Lithgow review the biogenesis, classification, and physiological functions of prokaryotic intracellular inclusions, storage granules, and microcompartments across bacteria and archaea.) | supports | Primary definition_source DOI:10.1038/s41579-020-0413-0 on data/traits/morphology/intracellular_inclusion.yaml (traitmech:000066, intracellular inclusion) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Greening &amp; Lithgow review the biogenesis, classification, and physiological functions of prokaryotic intracellular inclusions, storage granules, and microcompartments across bacteria and archaea.). |
| ev-c10s5-def-src-006 | DOI:10.1038/nrmicro.2016.99; Aligned on data/traits/morphology/magnetosome.yaml evidence[0] (Uebe &amp; Schüler review magnetosome membrane invagination, iron uptake and biomineralization, MamK/MamJ chain assembly, and magnetotactic navigation.) | supports | Primary definition_source DOI:10.1038/nrmicro.2016.99 on data/traits/morphology/magnetosome.yaml (traitmech:000071, magnetosome) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Uebe &amp; Schüler review magnetosome membrane invagination, iron uptake and biomineralization, MamK/MamJ chain assembly, and magnetotactic navigation.). |
| ev-c10s5-def-src-007 | DOI:10.1038/nrmicro1968; Aligned on data/traits/morphology/mycelial_growth.yaml evidence[0] (Flärdh &amp; Buttner review polar tip extension, DivIVA polarisome function, lateral branching, vegetative vs. aerial mycelium differentiation, and sporulation in Streptomyces.) | supports | Primary definition_source DOI:10.1038/nrmicro1968 on data/traits/morphology/mycelial_growth.yaml (traitmech:000074, mycelial growth) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Flärdh &amp; Buttner review polar tip extension, DivIVA polarisome function, lateral branching, vegetative vs. aerial mycelium differentiation, and sporulation in Streptomyces.). |
| ev-c10s5-def-src-008 | DOI:10.1128/mr.54.4.450-472.1990; Aligned on data/traits/morphology/polyhydroxyalkanoate_granule.yaml evidence[0] (Anderson &amp; Dawes review the occurrence, biochemistry, PhaA/PhaB/PhaC biosynthetic pathway, and physiological regulation of bacterial polyhydroxyalkanoate storage granules.) | supports | Primary definition_source DOI:10.1128/mr.54.4.450-472.1990 on data/traits/morphology/polyhydroxyalkanoate_granule.yaml (traitmech:000067, polyhydroxyalkanoate granule) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Anderson &amp; Dawes review the occurrence, biochemistry, PhaA/PhaB/PhaC biosynthetic pathway, and physiological regulation of bacterial polyhydroxyalkanoate storage granules.). |
| ev-c10s5-def-src-009 | DOI:10.1146/annurev.biochem.77.083007.093039; Aligned on data/traits/morphology/polyphosphate_granule.yaml evidence[0] (Rao, Gómez-García &amp; Kornberg review polyphosphate kinases (PPK1, PPK2), exopolyphosphatase (PPX), polyphosphate granule storage, and physiological roles in stress survival, motility, and virulence.) | supports | Primary definition_source DOI:10.1146/annurev.biochem.77.083007.093039 on data/traits/morphology/polyphosphate_granule.yaml (traitmech:000068, polyphosphate granule) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Rao, Gómez-García &amp; Kornberg review polyphosphate kinases (PPK1, PPK2), exopolyphosphatase (PPX), polyphosphate granule storage, and physiological roles in stress survival, motility, and virulence.). |
| ev-c10s5-def-src-010 | DOI:10.1111/j.1365-2958.2007.05633.x; Aligned on data/traits/morphology/prosthecate.yaml evidence[0] (Wagner &amp; Brun review the structure, peptidoglycan synthesis, developmental regulation, and nutrient-acquisition role of bacterial prosthecae (stalks).) | supports | Primary definition_source DOI:10.1111/j.1365-2958.2007.05633.x on data/traits/morphology/prosthecate.yaml (traitmech:000065, prosthecate) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Wagner &amp; Brun review the structure, peptidoglycan synthesis, developmental regulation, and nutrient-acquisition role of bacterial prosthecae (stalks).). |
| ev-c10s5-def-src-011 | DOI:10.1038/nrmicro3213; Aligned on data/traits/morphology/s_layer.yaml evidence[0] (Fagan &amp; Fairweather review S-layer protein secretion, cell-wall anchoring (SLH and CWB2 domains), self-assembly into paracrystalline lattices, and functional roles across Bacteria and Archaea.) | supports | Primary definition_source DOI:10.1038/nrmicro3213 on data/traits/morphology/s_layer.yaml (traitmech:000064, S-layer) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Fagan &amp; Fairweather review S-layer protein secretion, cell-wall anchoring (SLH and CWB2 domains), self-assembly into paracrystalline lattices, and functional roles across Bacteria and Archaea.). |
| ev-c10s5-def-src-012 | DOI:10.1016/S0065-2911(08)00002-7; Aligned on data/traits/morphology/sulfur_globule.yaml evidence[0] (Frigaard &amp; Dahl review the biogenesis, SgpA/SgpB/SgpC protein envelope, chemical speciation, and Dsr-mediated oxidation of bacterial sulfur globules.) | supports | Primary definition_source DOI:10.1016/S0065-2911(08)00002-7 on data/traits/morphology/sulfur_globule.yaml (traitmech:000069, sulfur globule) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Frigaard &amp; Dahl review the biogenesis, SgpA/SgpB/SgpC protein envelope, chemical speciation, and Dsr-mediated oxidation of bacterial sulfur globules.). |
| ev-c10s5-def-src-013 | DOI:10.1038/nrmicro2405; Aligned on data/traits/morphology/swarming_motility.yaml evidence[0] (Kearns reviews bacterial swarming motility, covering hyperflagellation, biosurfactant wetting agents, cell elongation, and surface sensing.) | supports | Primary definition_source DOI:10.1038/nrmicro2405 on data/traits/morphology/swarming_motility.yaml (traitmech:000062, swarming motility) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Kearns reviews bacterial swarming motility, covering hyperflagellation, biosurfactant wetting agents, cell elongation, and surface sensing.). |
| ev-c10s5-def-src-014 | DOI:10.1146/annurev.micro.56.012302.160938; Aligned on data/traits/morphology/twitching_motility.yaml evidence[0] (Mattick reviews the genetics, PilA/PilB/PilT/PilQ machinery, extension-retraction mechanics, and physiological roles of type IV pili-mediated twitching motility.) | supports | Primary definition_source DOI:10.1146/annurev.micro.56.012302.160938 on data/traits/morphology/twitching_motility.yaml (traitmech:000061, twitching motility) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet (Mattick reviews the genetics, PilA/PilB/PilT/PilQ machinery, extension-retraction mechanics, and physiological roles of type IV pili-mediated twitching motility.). |
| ev-remediated-records | data/traits/morphology/capsule.yaml; data/traits/morphology/carboxysome.yaml; data/traits/morphology/gas_vesicle.yaml; data/traits/morphology/heterocyst.yaml; data/traits/morphology/intracellular_inclusion.yaml; data/traits/morphology/magnetosome.yaml; data/traits/morphology/mycelial_growth.yaml; data/traits/morphology/polyhydroxyalkanoate_granule.yaml; data/traits/morphology/polyphosphate_granule.yaml; data/traits/morphology/prosthecate.yaml; data/traits/morphology/s_layer.yaml; data/traits/morphology/sulfur_globule.yaml; data/traits/morphology/swarming_motility.yaml; data/traits/morphology/twitching_motility.yaml; definition_source, evidence[0], curation_history | supports | All 14 remediated morphology TraitRecord YAML files now carry a verified non-elliptical verbatim snippet in record-level evidence[0].snippet for their declared definition_source DOI and record an append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event. |
| ev-stage5-writer | scripts/curate_stage5_review_findings.py; tests/test_curate_stage5_review_findings.py; process_all | supports | Guarded writer script and unit test suite verifying closed-mode LinkML validation, DO_NOT_WORK exclusion, and idempotent remediation across all 115 target specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4 + 7 Cycle 5 + 13 Cycle 6 + 15 Cycle 7 + 12 Cycle 8 + 9 Cycle 9 + 14 Cycle 10). |
| ev-validate-strict | scripts/validate_strict.py; reports/instance_validation_failures.tsv | supports | Closed-mode LinkML schema and identifier validation passes with 0 errors across all 1,130 TraitRecord files. |
| ev-snippet-audit | scripts/audit_evidence_snippets.py; conf/evidence_snippet_baseline.tsv | supports | All 14 remediated record-level evidence[0] entries pass contiguous verbatim quote checks with 0 new warnings, removing 14 baselined MISSING_SNIPPET rows from conf/evidence_snippet_baseline.tsv (2,363 -&gt; 2,349 total baselined findings; MISSING_SNIPPET 2,225 -&gt; 2,211) and eliminating all 14 open definition_source missing-snippet findings from Cycle 10 Stage 4. |

## Limits And Additional Notes

- This batch review covers the 14 morphology records remediated in Cycle 10 Stage 5 under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002); the 5 cohort-level source-limited or upstream-blocked findings from Cycle 10 Stage 4 remain tracked under open GitHub issues #1982, #1983, #1984, #1985, and #364.
- All 14 of the remediated morphology records carry repository-minted traitmech:NNNNNN identifiers (traitmech:000061..000074) backed by validated ROBOT templates awaiting upstream METPO release incorporation (#364, berkeleybop/metpo#535).
- Skills executed: .claude/skills/curate-yaml-record/SKILL.md and .claude/skills/review-yaml-record/SKILL.md.
- Immutable Cycle 10 Stage 4 review bundle preserved untouched at reviews/structured/20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review/review.yaml.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T232500Z-cycle10-stage5-remediated-records-review
kind: batch
repository: CultureBotAI/TraitMech
title: Cycle 10 Stage 5 post-remediation verification review of the 14 morphology
  TraitRecord files in group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
started_at: '2026-11-04T23:20:00Z'
finished_at: '2026-11-04T23:25:00Z'
reviewer:
  identity: antigravity
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Repository-local post-remediation record review verifying resolution
    of the 14 Cycle 10 Stage 4 open findings (F-C10S4-DEF-SRC-001..F-C10S4-DEF-SRC-014)
    under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002); separate
    from independent PR adversarial review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Fresh post-remediation batch review of the 14 morphology TraitRecord YAML
  files remediated in Cycle 10 Stage 5 (capsule.yaml, carboxysome.yaml, gas_vesicle.yaml,
  heterocyst.yaml, intracellular_inclusion.yaml, magnetosome.yaml, mycelial_growth.yaml,
  polyhydroxyalkanoate_granule.yaml, polyphosphate_granule.yaml, prosthecate.yaml,
  s_layer.yaml, sulfur_globule.yaml, swarming_motility.yaml, and twitching_motility.yaml)
  under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002.
  All 14 Cycle 10 Stage 4 open findings (F-C10S4-DEF-SRC-001..014) are verified as
  resolved with contiguous verbatim snippets for their primary definition_source DOI
  in record-level evidence[0], removal of all 14 baselined MISSING_SNIPPET rows from
  conf/evidence_snippet_baseline.tsv (2,363 -> 2,349 total baselined findings; MISSING_SNIPPET
  2,225 -> 2,211), append-only curation_history provenance, and 0 remaining open findings.'
source:
  git_revision: 013a72e1bdd9d3f5dcaac757e08a5ae1cad881c8
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: 27f535d3f057d321c8b87c6506f2f35dd2d37fd005bcd5040b3e17269285075b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: bb03efa3bbd3748ee1dccf57612a6ce8fcc861f20eb57c33eb16e3ac1dd728bd
    role: context
  - path: AGENTS.md
    sha256: 6771ed07ef5ae68deecbf50ae6123e2e3a4834e05b2dbc13faa96ec2329a6f93
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: be3cec885419103ebd08e607c51edb7d32401bd46b35160f7285df615e482862
    role: context
  - path: conf/record_review.yaml
    sha256: 5adc6244761fb2baf8a059d81f23b0c9b32a33f9426ab84094234c3ec417269d
    role: context
  - path: data/traits/morphology/capsule.yaml
    sha256: a01202723c37add15896a3d93972b1579248e8d11e37724e159eef2d259fd476
    role: target
  - path: data/traits/morphology/carboxysome.yaml
    sha256: 08e80c83c10dd41e27d470519aa276a1e1576432487bca39defc90774c2a6752
    role: target
  - path: data/traits/morphology/gas_vesicle.yaml
    sha256: 73689d0f603b573879c5f8942d60ee3ceecea00e5bbec304c5a4b51db6d39b8d
    role: target
  - path: data/traits/morphology/heterocyst.yaml
    sha256: aba174bfeefbb211ad84fc296432d870f6b627df6901ec934a3f23a9f5af9ace
    role: target
  - path: data/traits/morphology/intracellular_inclusion.yaml
    sha256: 044c2fc8562e499f2c46bf68d4149776045f8f0bb6f98dd5501310f10532f415
    role: target
  - path: data/traits/morphology/magnetosome.yaml
    sha256: 84789a7ff755b3d4e48174b52fef9a15323dd3abf9d1eb1c868b305a8724439f
    role: target
  - path: data/traits/morphology/mycelial_growth.yaml
    sha256: 7e6643b29b7af5e880db1a08efb66b0b3fe65a93e59c5a3f49c590c91f99e33f
    role: target
  - path: data/traits/morphology/polyhydroxyalkanoate_granule.yaml
    sha256: 37ddf1be7d4a5a97876c0c66e5c57cabf03a0baca1480e5678ca0cd5693ae695
    role: target
  - path: data/traits/morphology/polyphosphate_granule.yaml
    sha256: 23f27641fb086d537ba21a163e3aa61c982394582603d8918e9a1208ad5ab8e5
    role: target
  - path: data/traits/morphology/prosthecate.yaml
    sha256: 54e4d3cea8a5526cf1ff6e98a2a9216de9a40bc9f8d569c777d0e2c0547dbf40
    role: target
  - path: data/traits/morphology/s_layer.yaml
    sha256: 2d44b1c614d57c36b8fc8b14a5dc9eda776c97708126fc577e113e763650b9a5
    role: target
  - path: data/traits/morphology/sulfur_globule.yaml
    sha256: c11cffdd6704a769778fe7197a34890741da4a196c33fd2c0ae873c0b3a811a1
    role: target
  - path: data/traits/morphology/swarming_motility.yaml
    sha256: 6522c5326c4329d2f84d7dfe32e27b70acff6fc33733606e97195209848165d4
    role: target
  - path: data/traits/morphology/twitching_motility.yaml
    sha256: d79325768f28c81d35a1bd309a092abd54f78f532935c27126a5735ddd82d317
    role: target
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/infrastructure/curate_stage5_review_findings/2026-11-04T232000Z-claude-code-c10a514.yaml
    sha256: 2ebf978e3ec33c47ab9837f5a6fc0a50df9a5fbf89d157c0588b8a13d6bcde8f
    role: context
  - path: reviews/structured/20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review/review.yaml
    sha256: 51ac757cda8db526ed222560f762783e2c72472689ae285b6cb2f96e633e6bb9
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-04/revision-0001/evidence.yaml
    sha256: 38656ba7af735f8ed4c20bc334c2295302b3ed88de4c6e5fde22a86fea30f2f1
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/curate_stage5_review_findings.py
    sha256: 6a4eee55337a5b10cb703b98ef38c1ff0ac5d87efc0ec31231aee1b6609284e4
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: tests/test_curate_stage5_review_findings.py
    sha256: c181b381bb978c744c27fd440df95a0d3b63fb99cd826c0073007abd7e5b728c
    role: context
scope:
  description: Focused post-remediation review of all 14 morphology TraitRecord YAML
    files modified in Cycle 10 Stage 5 (resolve_review_findings) to resolve group
    G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002).
  selection: All 14 records with open findings carried forward from Cycle 10 Stage
    4 review 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review.
  coverage: full
  population_size: 14
  reviewed_target_ids:
  - traitmech:000063
  - traitmech:000072
  - traitmech:000070
  - traitmech:000073
  - traitmech:000066
  - traitmech:000071
  - traitmech:000074
  - traitmech:000067
  - traitmech:000068
  - traitmech:000065
  - traitmech:000064
  - traitmech:000069
  - traitmech:000062
  - traitmech:000061
targets:
- target_id: traitmech:000063
  path: data/traits/morphology/capsule.yaml
  label: capsule
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/capsule.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000072
  path: data/traits/morphology/carboxysome.yaml
  label: carboxysome
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/carboxysome.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000070
  path: data/traits/morphology/gas_vesicle.yaml
  label: gas vesicle
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/gas_vesicle.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000073
  path: data/traits/morphology/heterocyst.yaml
  label: heterocyst
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/heterocyst.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000066
  path: data/traits/morphology/intracellular_inclusion.yaml
  label: intracellular inclusion
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/intracellular_inclusion.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000071
  path: data/traits/morphology/magnetosome.yaml
  label: magnetosome
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/magnetosome.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000074
  path: data/traits/morphology/mycelial_growth.yaml
  label: mycelial growth
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/mycelial_growth.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000067
  path: data/traits/morphology/polyhydroxyalkanoate_granule.yaml
  label: polyhydroxyalkanoate granule
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/polyhydroxyalkanoate_granule.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000068
  path: data/traits/morphology/polyphosphate_granule.yaml
  label: polyphosphate granule
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/polyphosphate_granule.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000065
  path: data/traits/morphology/prosthecate.yaml
  label: prosthecate
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/prosthecate.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000064
  path: data/traits/morphology/s_layer.yaml
  label: S-layer
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/s_layer.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000069
  path: data/traits/morphology/sulfur_globule.yaml
  label: sulfur globule
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/sulfur_globule.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000062
  path: data/traits/morphology/swarming_motility.yaml
  label: swarming motility
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/swarming_motility.yaml
    role: maintained TraitRecord YAML
- target_id: traitmech:000061
  path: data/traits/morphology/twitching_motility.yaml
  label: twitching motility
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/twitching_motility.yaml
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
  - traitmech:000063
  - traitmech:000072
  - traitmech:000070
  - traitmech:000073
  - traitmech:000066
  - traitmech:000071
  - traitmech:000074
  - traitmech:000067
  - traitmech:000068
  - traitmech:000065
  - traitmech:000064
  - traitmech:000069
  - traitmech:000062
  - traitmech:000061
  evidence_ids:
  - ev-validate-strict
  - ev-remediated-records
  summary: All 1,130 TraitRecord YAML files (including all 14 Cycle 10 Stage 5 remediated
    morphology records) pass strict closed-mode LinkML validation with 0 errors.
- check_id: audit-snippets
  name: Evidence snippet structural and baseline ratchet audit
  command: uv run python scripts/audit_evidence_snippets.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000063
  - traitmech:000072
  - traitmech:000070
  - traitmech:000073
  - traitmech:000066
  - traitmech:000071
  - traitmech:000074
  - traitmech:000067
  - traitmech:000068
  - traitmech:000065
  - traitmech:000064
  - traitmech:000069
  - traitmech:000062
  - traitmech:000061
  evidence_ids:
  - ev-snippet-audit
  - ev-c10s5-def-src-001
  - ev-c10s5-def-src-002
  - ev-c10s5-def-src-003
  - ev-c10s5-def-src-004
  - ev-c10s5-def-src-005
  - ev-c10s5-def-src-006
  - ev-c10s5-def-src-007
  - ev-c10s5-def-src-008
  - ev-c10s5-def-src-009
  - ev-c10s5-def-src-010
  - ev-c10s5-def-src-011
  - ev-c10s5-def-src-012
  - ev-c10s5-def-src-013
  - ev-c10s5-def-src-014
  summary: All 14 remediated morphology records now carry a contiguous >=16-char verbatim
    quote for their primary definition_source DOI in record-level evidence[0], passing
    scripts/audit_evidence_snippets.py with 0 new findings and reducing baselined
    MISSING_SNIPPET rows in conf/evidence_snippet_baseline.tsv from 2,225 to 2,211
    (-14; total baselined findings 2,363 -> 2,349).
- check_id: stage5-writer-tests
  name: Stage 5 guarded writer idempotency and postcondition unit tests
  command: uv run pytest tests/test_curate_stage5_review_findings.py -v
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000063
  - traitmech:000072
  - traitmech:000070
  - traitmech:000073
  - traitmech:000066
  - traitmech:000071
  - traitmech:000074
  - traitmech:000067
  - traitmech:000068
  - traitmech:000065
  - traitmech:000064
  - traitmech:000069
  - traitmech:000062
  - traitmech:000061
  evidence_ids:
  - ev-stage5-writer
  summary: All 5 unit tests in tests/test_curate_stage5_review_findings.py pass, confirming
    DO_NOT_WORK protection, exact definition_source evidence alignment across all
    115 remediated specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4 + 7 Cycle
    5 + 13 Cycle 6 + 15 Cycle 7 + 12 Cycle 8 + 9 Cycle 9 + 14 Cycle 10), zero UNQUOTED_DEFINITION_SOURCE
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
  - traitmech:000063
  - traitmech:000072
  - traitmech:000070
  - traitmech:000073
  - traitmech:000066
  - traitmech:000071
  - traitmech:000074
  - traitmech:000067
  - traitmech:000068
  - traitmech:000065
  - traitmech:000064
  - traitmech:000069
  - traitmech:000062
  - traitmech:000061
  evidence_ids:
  - ev-stage5-writer
  summary: scripts/curate_stage5_review_findings.py satisfies all writer safeguards
    (appends curation_history, has write safeguard, validates before write, wired
    into justfile).
evidence:
- evidence_id: ev-prior-c10s4-review
  kind: prior_review
  reference: reviews/structured/20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review/review.yaml
  locator: findings[0..13]
  accessed_at: '2026-11-04T23:21:00Z'
  support: supports
  summary: Immutable Cycle 10 Stage 4 review bundle identifying the 14 open definition_source
    missing-snippet findings (F-C10S4-DEF-SRC-001..F-C10S4-DEF-SRC-014) across data/traits/morphology/
    with planned remediation actions ACT-C10S4-DEF-SRC-001..014.
  snapshot_sha256: 51ac757cda8db526ed222560f762783e2c72472689ae285b6cb2f96e633e6bb9
- evidence_id: ev-c10s5-def-src-001
  kind: primary_source
  reference: DOI:10.1146/annurev.micro.50.1.285
  locator: Aligned on data/traits/morphology/capsule.yaml evidence[0] (Roberts reviews
    the biochemistry, genetics, group I-IV classification, export/assembly pathways
    (Wzx/Wzy and ABC transporter systems), and virulence roles of bacterial polysaccharide
    capsules.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1146/annurev.micro.50.1.285 on data/traits/morphology/capsule.yaml
    (traitmech:000063, capsule) verified with verbatim Europe PMC abstract quote in
    record-level evidence[0].snippet (Roberts reviews the biochemistry, genetics,
    group I-IV classification, export/assembly pathways (Wzx/Wzy and ABC transporter
    systems), and virulence roles of bacterial polysaccharide capsules.).
  quote: Many bacteria are surrounded by a polysaccharide layer outside the outer
    membrane of Gram-negative bacteria and the peptidoglycan layer of Gram-positive
    bacteria.
- evidence_id: ev-c10s5-def-src-002
  kind: primary_source
  reference: DOI:10.1038/nrmicro.2018.10
  locator: Aligned on data/traits/morphology/carboxysome.yaml evidence[0] (Kerfeld
    et al. review bacterial microcompartments, with detailed coverage of alpha- and
    beta-carboxysome shell architecture (BMC-H, BMC-T, BMC-P), RuBisCO/carbonic anhydrase
    encapsulation, and CO2-concentrating function.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/nrmicro.2018.10 on data/traits/morphology/carboxysome.yaml
    (traitmech:000072, carboxysome) verified with verbatim Europe PMC abstract quote
    in record-level evidence[0].snippet (Kerfeld et al. review bacterial microcompartments,
    with detailed coverage of alpha- and beta-carboxysome shell architecture (BMC-H,
    BMC-T, BMC-P), RuBisCO/carbonic anhydrase encapsulation, and CO2-concentrating
    function.).
  quote: Bacterial microcompartments (BMCs) are self-assembling organelles that consist
    of an enzymatic core that is encapsulated by a selectively permeable protein shell.
- evidence_id: ev-c10s5-def-src-003
  kind: primary_source
  reference: DOI:10.1038/nrmicro2834
  locator: Aligned on data/traits/morphology/gas_vesicle.yaml evidence[0] (Pfeifer
    reviews the structure, gvp gene clusters, GvpA/GvpC shell assembly, regulation,
    and buoyancy function of bacterial and archaeal gas vesicles.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/nrmicro2834 on data/traits/morphology/gas_vesicle.yaml
    (traitmech:000070, gas vesicle) verified with verbatim Europe PMC abstract quote
    in record-level evidence[0].snippet (Pfeifer reviews the structure, gvp gene clusters,
    GvpA/GvpC shell assembly, regulation, and buoyancy function of bacterial and archaeal
    gas vesicles.).
  quote: Gas vesicles are hollow, proteinaceous structures that are filled with gas
    and allow halophilic and methanogenic archaea as well as photosynthetic and heterotrophic
    bacteria to thrive at vertical positions with favourable growth conditions in
    watery environments.
- evidence_id: ev-c10s5-def-src-004
  kind: primary_source
  reference: DOI:10.1101/cshperspect.a000315
  locator: Aligned on data/traits/morphology/heterocyst.yaml evidence[0] (Kumar, Mella-Herrera
    & Golden review cyanobacterial heterocyst differentiation, NtcA/HetR regulatory
    control, PatS/HetN spacing, envelope glycolipid/polysaccharide layers, and microoxic
    nitrogen fixation.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1101/cshperspect.a000315 on data/traits/morphology/heterocyst.yaml
    (traitmech:000073, heterocyst) verified with verbatim Europe PMC abstract quote
    in record-level evidence[0].snippet (Kumar, Mella-Herrera & Golden review cyanobacterial
    heterocyst differentiation, NtcA/HetR regulatory control, PatS/HetN spacing, envelope
    glycolipid/polysaccharide layers, and microoxic nitrogen fixation.).
  quote: Heterocysts are terminally differentiated nitrogen-fixing cells formed at
    semiregular intervals along filaments of certain cyanobacteria, such as Anabaena
    (Nostoc) sp. strain PCC 7120, when fixed nitrogen is limiting.
- evidence_id: ev-c10s5-def-src-005
  kind: primary_source
  reference: DOI:10.1038/s41579-020-0413-0
  locator: Aligned on data/traits/morphology/intracellular_inclusion.yaml evidence[0]
    (Greening & Lithgow review the biogenesis, classification, and physiological functions
    of prokaryotic intracellular inclusions, storage granules, and microcompartments
    across bacteria and archaea.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/s41579-020-0413-0 on data/traits/morphology/intracellular_inclusion.yaml
    (traitmech:000066, intracellular inclusion) verified with verbatim Europe PMC
    abstract quote in record-level evidence[0].snippet (Greening & Lithgow review
    the biogenesis, classification, and physiological functions of prokaryotic intracellular
    inclusions, storage granules, and microcompartments across bacteria and archaea.).
  quote: Prokaryotes synthesize diverse intracellular nanostructures and bodies to
    compartmentalize metabolic pathways, store reserves and enhance survival under
    stress.
- evidence_id: ev-c10s5-def-src-006
  kind: primary_source
  reference: DOI:10.1038/nrmicro.2016.99
  locator: Aligned on data/traits/morphology/magnetosome.yaml evidence[0] (Uebe &
    Schüler review magnetosome membrane invagination, iron uptake and biomineralization,
    MamK/MamJ chain assembly, and magnetotactic navigation.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/nrmicro.2016.99 on data/traits/morphology/magnetosome.yaml
    (traitmech:000071, magnetosome) verified with verbatim Europe PMC abstract quote
    in record-level evidence[0].snippet (Uebe & Schüler review magnetosome membrane
    invagination, iron uptake and biomineralization, MamK/MamJ chain assembly, and
    magnetotactic navigation.).
  quote: Magnetotactic bacteria (MTB) orient and navigate along geomagnetic field
    lines, a behaviour that is enabled by magnetosomes — unique intracellular organelles
    that consist of magnetic iron mineral crystals enclosed by a specialized membrane
    bilayer.
- evidence_id: ev-c10s5-def-src-007
  kind: primary_source
  reference: DOI:10.1038/nrmicro1968
  locator: Aligned on data/traits/morphology/mycelial_growth.yaml evidence[0] (Flärdh
    & Buttner review polar tip extension, DivIVA polarisome function, lateral branching,
    vegetative vs. aerial mycelium differentiation, and sporulation in Streptomyces.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/nrmicro1968 on data/traits/morphology/mycelial_growth.yaml
    (traitmech:000074, mycelial growth) verified with verbatim Europe PMC abstract
    quote in record-level evidence[0].snippet (Flärdh & Buttner review polar tip extension,
    DivIVA polarisome function, lateral branching, vegetative vs. aerial mycelium
    differentiation, and sporulation in Streptomyces.).
  quote: Streptomycetes are filamentous bacteria that grow by tip extension and hyphal
    branching to form a dense vegetative mycelium.
- evidence_id: ev-c10s5-def-src-008
  kind: primary_source
  reference: DOI:10.1128/mr.54.4.450-472.1990
  locator: Aligned on data/traits/morphology/polyhydroxyalkanoate_granule.yaml evidence[0]
    (Anderson & Dawes review the occurrence, biochemistry, PhaA/PhaB/PhaC biosynthetic
    pathway, and physiological regulation of bacterial polyhydroxyalkanoate storage
    granules.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1128/mr.54.4.450-472.1990 on data/traits/morphology/polyhydroxyalkanoate_granule.yaml
    (traitmech:000067, polyhydroxyalkanoate granule) verified with verbatim Europe
    PMC abstract quote in record-level evidence[0].snippet (Anderson & Dawes review
    the occurrence, biochemistry, PhaA/PhaB/PhaC biosynthetic pathway, and physiological
    regulation of bacterial polyhydroxyalkanoate storage granules.).
  quote: Polyhydroxyalkanoates (PHAs) are polyesters of various hydroxyalkanoates
    that are synthesized by numerous microorganisms and accumulated as intracellular
    carbon and energy storage granules.
- evidence_id: ev-c10s5-def-src-009
  kind: primary_source
  reference: DOI:10.1146/annurev.biochem.77.083007.093039
  locator: Aligned on data/traits/morphology/polyphosphate_granule.yaml evidence[0]
    (Rao, Gómez-García & Kornberg review polyphosphate kinases (PPK1, PPK2), exopolyphosphatase
    (PPX), polyphosphate granule storage, and physiological roles in stress survival,
    motility, and virulence.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1146/annurev.biochem.77.083007.093039
    on data/traits/morphology/polyphosphate_granule.yaml (traitmech:000068, polyphosphate
    granule) verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet
    (Rao, Gómez-García & Kornberg review polyphosphate kinases (PPK1, PPK2), exopolyphosphatase
    (PPX), polyphosphate granule storage, and physiological roles in stress survival,
    motility, and virulence.).
  quote: Inorganic polyphosphate (poly P) is a linear polymer of many tens or hundreds
    of orthophosphate (Pi) residues linked by high-energy phosphoanhydride bonds.
- evidence_id: ev-c10s5-def-src-010
  kind: primary_source
  reference: DOI:10.1111/j.1365-2958.2007.05633.x
  locator: Aligned on data/traits/morphology/prosthecate.yaml evidence[0] (Wagner
    & Brun review the structure, peptidoglycan synthesis, developmental regulation,
    and nutrient-acquisition role of bacterial prosthecae (stalks).)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1111/j.1365-2958.2007.05633.x on data/traits/morphology/prosthecate.yaml
    (traitmech:000065, prosthecate) verified with verbatim Europe PMC abstract quote
    in record-level evidence[0].snippet (Wagner & Brun review the structure, peptidoglycan
    synthesis, developmental regulation, and nutrient-acquisition role of bacterial
    prosthecae (stalks).).
  quote: Prosthecae are narrow extensions of the bacterial cell wall that contain
    cytoplasm and are bounded by the cell envelope.
- evidence_id: ev-c10s5-def-src-011
  kind: primary_source
  reference: DOI:10.1038/nrmicro3213
  locator: Aligned on data/traits/morphology/s_layer.yaml evidence[0] (Fagan & Fairweather
    review S-layer protein secretion, cell-wall anchoring (SLH and CWB2 domains),
    self-assembly into paracrystalline lattices, and functional roles across Bacteria
    and Archaea.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/nrmicro3213 on data/traits/morphology/s_layer.yaml
    (traitmech:000064, S-layer) verified with verbatim Europe PMC abstract quote in
    record-level evidence[0].snippet (Fagan & Fairweather review S-layer protein secretion,
    cell-wall anchoring (SLH and CWB2 domains), self-assembly into paracrystalline
    lattices, and functional roles across Bacteria and Archaea.).
  quote: Surface layers (S-layers) are two-dimensional crystalline arrays of protein
    or glycoprotein subunits that form the outermost cell envelope component of many
    bacteria and almost all archaea.
- evidence_id: ev-c10s5-def-src-012
  kind: primary_source
  reference: DOI:10.1016/S0065-2911(08)00002-7
  locator: Aligned on data/traits/morphology/sulfur_globule.yaml evidence[0] (Frigaard
    & Dahl review the biogenesis, SgpA/SgpB/SgpC protein envelope, chemical speciation,
    and Dsr-mediated oxidation of bacterial sulfur globules.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1016/S0065-2911(08)00002-7 on data/traits/morphology/sulfur_globule.yaml
    (traitmech:000069, sulfur globule) verified with verbatim Europe PMC abstract
    quote in record-level evidence[0].snippet (Frigaard & Dahl review the biogenesis,
    SgpA/SgpB/SgpC protein envelope, chemical speciation, and Dsr-mediated oxidation
    of bacterial sulfur globules.).
  quote: Many sulfur-oxidizing bacteria form globules of elemental sulfur as an obligate
    or facultative intermediate during the oxidation of reduced inorganic sulfur compounds
    such as sulfide and thiosulfate.
- evidence_id: ev-c10s5-def-src-013
  kind: primary_source
  reference: DOI:10.1038/nrmicro2405
  locator: Aligned on data/traits/morphology/swarming_motility.yaml evidence[0] (Kearns
    reviews bacterial swarming motility, covering hyperflagellation, biosurfactant
    wetting agents, cell elongation, and surface sensing.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1038/nrmicro2405 on data/traits/morphology/swarming_motility.yaml
    (traitmech:000062, swarming motility) verified with verbatim Europe PMC abstract
    quote in record-level evidence[0].snippet (Kearns reviews bacterial swarming motility,
    covering hyperflagellation, biosurfactant wetting agents, cell elongation, and
    surface sensing.).
  quote: Swarming motility is a rapid, multicellular movement of bacteria across a
    surface, powered by rotating flagella.
- evidence_id: ev-c10s5-def-src-014
  kind: primary_source
  reference: DOI:10.1146/annurev.micro.56.012302.160938
  locator: Aligned on data/traits/morphology/twitching_motility.yaml evidence[0] (Mattick
    reviews the genetics, PilA/PilB/PilT/PilQ machinery, extension-retraction mechanics,
    and physiological roles of type IV pili-mediated twitching motility.)
  accessed_at: '2026-11-04T23:22:00Z'
  support: supports
  summary: Primary definition_source DOI:10.1146/annurev.micro.56.012302.160938 on
    data/traits/morphology/twitching_motility.yaml (traitmech:000061, twitching motility)
    verified with verbatim Europe PMC abstract quote in record-level evidence[0].snippet
    (Mattick reviews the genetics, PilA/PilB/PilT/PilQ machinery, extension-retraction
    mechanics, and physiological roles of type IV pili-mediated twitching motility.).
  quote: Twitching motility is a mode of surface translocation mediated by the extension,
    tethering, and retraction of type IV pili.
- evidence_id: ev-remediated-records
  kind: record_content
  reference: data/traits/morphology/capsule.yaml; data/traits/morphology/carboxysome.yaml;
    data/traits/morphology/gas_vesicle.yaml; data/traits/morphology/heterocyst.yaml;
    data/traits/morphology/intracellular_inclusion.yaml; data/traits/morphology/magnetosome.yaml;
    data/traits/morphology/mycelial_growth.yaml; data/traits/morphology/polyhydroxyalkanoate_granule.yaml;
    data/traits/morphology/polyphosphate_granule.yaml; data/traits/morphology/prosthecate.yaml;
    data/traits/morphology/s_layer.yaml; data/traits/morphology/sulfur_globule.yaml;
    data/traits/morphology/swarming_motility.yaml; data/traits/morphology/twitching_motility.yaml
  locator: definition_source, evidence[0], curation_history
  accessed_at: '2026-11-04T23:23:00Z'
  support: supports
  summary: All 14 remediated morphology TraitRecord YAML files now carry a verified
    non-elliptical verbatim snippet in record-level evidence[0].snippet for their
    declared definition_source DOI and record an append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE
    curation_history event.
- evidence_id: ev-stage5-writer
  kind: validation
  reference: scripts/curate_stage5_review_findings.py; tests/test_curate_stage5_review_findings.py
  locator: process_all
  accessed_at: '2026-11-04T23:23:00Z'
  support: supports
  summary: Guarded writer script and unit test suite verifying closed-mode LinkML
    validation, DO_NOT_WORK exclusion, and idempotent remediation across all 115 target
    specs (4 Cycle 1 + 6 Cycle 2 + 17 Cycle 3 + 18 Cycle 4 + 7 Cycle 5 + 13 Cycle
    6 + 15 Cycle 7 + 12 Cycle 8 + 9 Cycle 9 + 14 Cycle 10).
  snapshot_sha256: 6a4eee55337a5b10cb703b98ef38c1ff0ac5d87efc0ec31231aee1b6609284e4
- evidence_id: ev-validate-strict
  kind: validation
  reference: scripts/validate_strict.py
  locator: reports/instance_validation_failures.tsv
  accessed_at: '2026-11-04T23:24:00Z'
  support: supports
  summary: Closed-mode LinkML schema and identifier validation passes with 0 errors
    across all 1,130 TraitRecord files.
- evidence_id: ev-snippet-audit
  kind: validation
  reference: scripts/audit_evidence_snippets.py
  locator: conf/evidence_snippet_baseline.tsv
  accessed_at: '2026-11-04T23:24:00Z'
  support: supports
  summary: All 14 remediated record-level evidence[0] entries pass contiguous verbatim
    quote checks with 0 new warnings, removing 14 baselined MISSING_SNIPPET rows from
    conf/evidence_snippet_baseline.tsv (2,363 -> 2,349 total baselined findings; MISSING_SNIPPET
    2,225 -> 2,211) and eliminating all 14 open definition_source missing-snippet
    findings from Cycle 10 Stage 4.
assessments:
- assessment_id: assess-remediated-evidence-alignment
  area: evidence
  topic: Verification of record-level definition_source evidence[0] verbatim snippet
    alignment across the 14 remediated morphology records
  outcome: supported
  summary: All 14 morphology records identified with open findings in Cycle 10 Stage
    4 (capsule.yaml, carboxysome.yaml, gas_vesicle.yaml, heterocyst.yaml, intracellular_inclusion.yaml,
    magnetosome.yaml, mycelial_growth.yaml, polyhydroxyalkanoate_granule.yaml, polyphosphate_granule.yaml,
    prosthecate.yaml, s_layer.yaml, sulfur_globule.yaml, swarming_motility.yaml, and
    twitching_motility.yaml) now carry a verified non-elliptical verbatim snippet
    directly in record-level evidence[0].snippet for their primary definition_source
    DOI.
  target_ids:
  - traitmech:000063
  - traitmech:000072
  - traitmech:000070
  - traitmech:000073
  - traitmech:000066
  - traitmech:000071
  - traitmech:000074
  - traitmech:000067
  - traitmech:000068
  - traitmech:000065
  - traitmech:000064
  - traitmech:000069
  - traitmech:000062
  - traitmech:000061
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-001
  - ev-c10s5-def-src-002
  - ev-c10s5-def-src-003
  - ev-c10s5-def-src-004
  - ev-c10s5-def-src-005
  - ev-c10s5-def-src-006
  - ev-c10s5-def-src-007
  - ev-c10s5-def-src-008
  - ev-c10s5-def-src-009
  - ev-c10s5-def-src-010
  - ev-c10s5-def-src-011
  - ev-c10s5-def-src-012
  - ev-c10s5-def-src-013
  - ev-c10s5-def-src-014
  - ev-remediated-records
  - ev-snippet-audit
  metrics:
  - name: remediated_open_findings_rate
    value: 1.0
    unit: ratio
    definition: Fraction of Cycle 10 Stage 4 open findings in group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
      verified as resolved with verbatim definition_source evidence.
    denominator: 14
    minimum: 0.0
    maximum: 1.0
  details: 'Each of the 14 remediated morphology records was re-inspected against
    .claude/skills/review-yaml-record/SKILL.md: F-C10S4-DEF-SRC-001..014 (capsule.yaml
    [DOI:10.1146/annurev.micro.50.1.285], carboxysome.yaml [DOI:10.1038/nrmicro.2018.10],
    gas_vesicle.yaml [DOI:10.1038/nrmicro2834], heterocyst.yaml [DOI:10.1101/cshperspect.a000315],
    intracellular_inclusion.yaml [DOI:10.1038/s41579-020-0413-0], magnetosome.yaml
    [DOI:10.1038/nrmicro.2016.99], mycelial_growth.yaml [DOI:10.1038/nrmicro1968],
    polyhydroxyalkanoate_granule.yaml [DOI:10.1128/mr.54.4.450-472.1990], polyphosphate_granule.yaml
    [DOI:10.1146/annurev.biochem.77.083007.093039], prosthecate.yaml [DOI:10.1111/j.1365-2958.2007.05633.x],
    s_layer.yaml [DOI:10.1038/nrmicro3213], sulfur_globule.yaml [DOI:10.1016/S0065-2911(08)00002-7],
    swarming_motility.yaml [DOI:10.1038/nrmicro2405], and twitching_motility.yaml
    [DOI:10.1146/annurev.micro.56.012302.160938]) now populate evidence[0].snippet
    with the verified Europe PMC abstract quote for their declared definition_source
    DOI and have been removed from conf/evidence_snippet_baseline.tsv.'
- assessment_id: assess-remediated-schema-and-provenance
  area: provenance
  topic: Schema validity, curation_history provenance, and writer guardrails on remediated
    records
  outcome: supported
  summary: 'All 14 remediated records pass strict closed-mode LinkML validation, preserve
    existing canonical_examples, causal_graphs, and UniProtKB protein_examples untouched,
    and record append-only ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history
    entries referencing issue #2002.'
  target_ids:
  - traitmech:000063
  - traitmech:000072
  - traitmech:000070
  - traitmech:000073
  - traitmech:000066
  - traitmech:000071
  - traitmech:000074
  - traitmech:000067
  - traitmech:000068
  - traitmech:000065
  - traitmech:000064
  - traitmech:000069
  - traitmech:000062
  - traitmech:000061
  evidence_ids:
  - ev-remediated-records
  - ev-stage5-writer
  - ev-validate-strict
findings:
- finding_id: F-C10S4-DEF-SRC-001
  issue_key: capsule-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: capsule.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet
    for definition_source DOI:10.1146/annurev.micro.50.1.285
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-001 on data/traits/morphology/capsule.yaml
    (traitmech:000063): populated record-level evidence[0].snippet for definition_source
    DOI:10.1146/annurev.micro.50.1.285 with the verified Europe PMC abstract quote
    (''Many bacteria are surrounded by a polysaccharide layer outside the outer membrane
    of Gram-negative bacteria and the peptidoglycan layer of Gram-positive bacteria.'')
    (Roberts reviews the biochemistry, genetics, group I-IV classification, export/assembly
    pathways (Wzx/Wzy and ABC transporter systems), and virulence roles of bacterial
    polysaccharide capsules.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv,
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000063
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-001
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/capsule.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-001
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-002
  issue_key: carboxysome-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: carboxysome.yaml now carries a verified verbatim snippet in record-level
    evidence[0].snippet for definition_source DOI:10.1038/nrmicro.2018.10
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-002 on data/traits/morphology/carboxysome.yaml
    (traitmech:000072): populated record-level evidence[0].snippet for definition_source
    DOI:10.1038/nrmicro.2018.10 with the verified Europe PMC abstract quote (''Bacterial
    microcompartments (BMCs) are self-assembling organelles that consist of an enzymatic
    core that is encapsulated by a selectively permeable protein shell.'') (Kerfeld
    et al. review bacterial microcompartments, with detailed coverage of alpha- and
    beta-carboxysome shell architecture (BMC-H, BMC-T, BMC-P), RuBisCO/carbonic anhydrase
    encapsulation, and CO2-concentrating function.), removed its baselined MISSING_SNIPPET
    row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry
    via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000072
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-002
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/carboxysome.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-002
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-003
  issue_key: gas-vesicle-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gas_vesicle.yaml now carries a verified verbatim snippet in record-level
    evidence[0].snippet for definition_source DOI:10.1038/nrmicro2834
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-003 on data/traits/morphology/gas_vesicle.yaml
    (traitmech:000070): populated record-level evidence[0].snippet for definition_source
    DOI:10.1038/nrmicro2834 with the verified Europe PMC abstract quote (''Gas vesicles
    are hollow, proteinaceous structures that are filled with gas and allow halophilic
    and methanogenic archaea as well as photosynthetic and heterotrophic bacteria
    to thrive at vertical positions with favourable growth conditions in watery environments.'')
    (Pfeifer reviews the structure, gvp gene clusters, GvpA/GvpC shell assembly, regulation,
    and buoyancy function of bacterial and archaeal gas vesicles.), removed its baselined
    MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history
    entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000070
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-003
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/gas_vesicle.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-003
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-004
  issue_key: heterocyst-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: heterocyst.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet
    for definition_source DOI:10.1101/cshperspect.a000315
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-004 on data/traits/morphology/heterocyst.yaml
    (traitmech:000073): populated record-level evidence[0].snippet for definition_source
    DOI:10.1101/cshperspect.a000315 with the verified Europe PMC abstract quote (''Heterocysts
    are terminally differentiated nitrogen-fixing cells formed at semiregular intervals
    along filaments of certain cyanobacteria, such as Anabaena (Nostoc) sp. strain
    PCC 7120, when fixed nitrogen is limiting.'') (Kumar, Mella-Herrera & Golden review
    cyanobacterial heterocyst differentiation, NtcA/HetR regulatory control, PatS/HetN
    spacing, envelope glycolipid/polysaccharide layers, and microoxic nitrogen fixation.),
    removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv,
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000073
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-004
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/heterocyst.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-004
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-005
  issue_key: intracellular-inclusion-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: intracellular_inclusion.yaml now carries a verified verbatim snippet in record-level
    evidence[0].snippet for definition_source DOI:10.1038/s41579-020-0413-0
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-005 on data/traits/morphology/intracellular_inclusion.yaml
    (traitmech:000066): populated record-level evidence[0].snippet for definition_source
    DOI:10.1038/s41579-020-0413-0 with the verified Europe PMC abstract quote (''Prokaryotes
    synthesize diverse intracellular nanostructures and bodies to compartmentalize
    metabolic pathways, store reserves and enhance survival under stress.'') (Greening
    & Lithgow review the biogenesis, classification, and physiological functions of
    prokaryotic intracellular inclusions, storage granules, and microcompartments
    across bacteria and archaea.), removed its baselined MISSING_SNIPPET row from
    conf/evidence_snippet_baseline.tsv, and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000066
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-005
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/intracellular_inclusion.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-005
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-006
  issue_key: magnetosome-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: magnetosome.yaml now carries a verified verbatim snippet in record-level
    evidence[0].snippet for definition_source DOI:10.1038/nrmicro.2016.99
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-006 on data/traits/morphology/magnetosome.yaml
    (traitmech:000071): populated record-level evidence[0].snippet for definition_source
    DOI:10.1038/nrmicro.2016.99 with the verified Europe PMC abstract quote (''Magnetotactic
    bacteria (MTB) orient and navigate along geomagnetic field lines, a behaviour
    that is enabled by magnetosomes — unique intracellular organelles that consist
    of magnetic iron mineral crystals enclosed by a specialized membrane bilayer.'')
    (Uebe & Schüler review magnetosome membrane invagination, iron uptake and biomineralization,
    MamK/MamJ chain assembly, and magnetotactic navigation.), removed its baselined
    MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history
    entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000071
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-006
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/magnetosome.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-006
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-007
  issue_key: mycelial-growth-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: mycelial_growth.yaml now carries a verified verbatim snippet in record-level
    evidence[0].snippet for definition_source DOI:10.1038/nrmicro1968
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-007 on data/traits/morphology/mycelial_growth.yaml
    (traitmech:000074): populated record-level evidence[0].snippet for definition_source
    DOI:10.1038/nrmicro1968 with the verified Europe PMC abstract quote (''Streptomycetes
    are filamentous bacteria that grow by tip extension and hyphal branching to form
    a dense vegetative mycelium.'') (Flärdh & Buttner review polar tip extension,
    DivIVA polarisome function, lateral branching, vegetative vs. aerial mycelium
    differentiation, and sporulation in Streptomyces.), removed its baselined MISSING_SNIPPET
    row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry
    via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000074
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-007
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/mycelial_growth.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-007
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-008
  issue_key: polyhydroxyalkanoate-granule-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: polyhydroxyalkanoate_granule.yaml now carries a verified verbatim snippet
    in record-level evidence[0].snippet for definition_source DOI:10.1128/mr.54.4.450-472.1990
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-008 on data/traits/morphology/polyhydroxyalkanoate_granule.yaml
    (traitmech:000067): populated record-level evidence[0].snippet for definition_source
    DOI:10.1128/mr.54.4.450-472.1990 with the verified Europe PMC abstract quote (''Polyhydroxyalkanoates
    (PHAs) are polyesters of various hydroxyalkanoates that are synthesized by numerous
    microorganisms and accumulated as intracellular carbon and energy storage granules.'')
    (Anderson & Dawes review the occurrence, biochemistry, PhaA/PhaB/PhaC biosynthetic
    pathway, and physiological regulation of bacterial polyhydroxyalkanoate storage
    granules.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv,
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000067
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-008
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/polyhydroxyalkanoate_granule.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-008
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-009
  issue_key: polyphosphate-granule-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: polyphosphate_granule.yaml now carries a verified verbatim snippet in record-level
    evidence[0].snippet for definition_source DOI:10.1146/annurev.biochem.77.083007.093039
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-009 on data/traits/morphology/polyphosphate_granule.yaml
    (traitmech:000068): populated record-level evidence[0].snippet for definition_source
    DOI:10.1146/annurev.biochem.77.083007.093039 with the verified Europe PMC abstract
    quote (''Inorganic polyphosphate (poly P) is a linear polymer of many tens or
    hundreds of orthophosphate (Pi) residues linked by high-energy phosphoanhydride
    bonds.'') (Rao, Gómez-García & Kornberg review polyphosphate kinases (PPK1, PPK2),
    exopolyphosphatase (PPX), polyphosphate granule storage, and physiological roles
    in stress survival, motility, and virulence.), removed its baselined MISSING_SNIPPET
    row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry
    via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000068
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-009
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/polyphosphate_granule.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-009
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-010
  issue_key: prosthecate-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: prosthecate.yaml now carries a verified verbatim snippet in record-level
    evidence[0].snippet for definition_source DOI:10.1111/j.1365-2958.2007.05633.x
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-010 on data/traits/morphology/prosthecate.yaml
    (traitmech:000065): populated record-level evidence[0].snippet for definition_source
    DOI:10.1111/j.1365-2958.2007.05633.x with the verified Europe PMC abstract quote
    (''Prosthecae are narrow extensions of the bacterial cell wall that contain cytoplasm
    and are bounded by the cell envelope.'') (Wagner & Brun review the structure,
    peptidoglycan synthesis, developmental regulation, and nutrient-acquisition role
    of bacterial prosthecae (stalks).), removed its baselined MISSING_SNIPPET row
    from conf/evidence_snippet_baseline.tsv, and appended curation_history entry via
    scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000065
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-010
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/prosthecate.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-010
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-011
  issue_key: s-layer-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: s_layer.yaml now carries a verified verbatim snippet in record-level evidence[0].snippet
    for definition_source DOI:10.1038/nrmicro3213
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-011 on data/traits/morphology/s_layer.yaml
    (traitmech:000064): populated record-level evidence[0].snippet for definition_source
    DOI:10.1038/nrmicro3213 with the verified Europe PMC abstract quote (''Surface
    layers (S-layers) are two-dimensional crystalline arrays of protein or glycoprotein
    subunits that form the outermost cell envelope component of many bacteria and
    almost all archaea.'') (Fagan & Fairweather review S-layer protein secretion,
    cell-wall anchoring (SLH and CWB2 domains), self-assembly into paracrystalline
    lattices, and functional roles across Bacteria and Archaea.), removed its baselined
    MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv, and appended curation_history
    entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000064
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-011
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/s_layer.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-011
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-012
  issue_key: sulfur-globule-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: sulfur_globule.yaml now carries a verified verbatim snippet in record-level
    evidence[0].snippet for definition_source DOI:10.1016/S0065-2911(08)00002-7
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-012 on data/traits/morphology/sulfur_globule.yaml
    (traitmech:000069): populated record-level evidence[0].snippet for definition_source
    DOI:10.1016/S0065-2911(08)00002-7 with the verified Europe PMC abstract quote
    (''Many sulfur-oxidizing bacteria form globules of elemental sulfur as an obligate
    or facultative intermediate during the oxidation of reduced inorganic sulfur compounds
    such as sulfide and thiosulfate.'') (Frigaard & Dahl review the biogenesis, SgpA/SgpB/SgpC
    protein envelope, chemical speciation, and Dsr-mediated oxidation of bacterial
    sulfur globules.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv,
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000069
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-012
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/sulfur_globule.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-012
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-013
  issue_key: swarming-motility-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: swarming_motility.yaml now carries a verified verbatim snippet in record-level
    evidence[0].snippet for definition_source DOI:10.1038/nrmicro2405
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-013 on data/traits/morphology/swarming_motility.yaml
    (traitmech:000062): populated record-level evidence[0].snippet for definition_source
    DOI:10.1038/nrmicro2405 with the verified Europe PMC abstract quote (''Swarming
    motility is a rapid, multicellular movement of bacteria across a surface, powered
    by rotating flagella.'') (Kearns reviews bacterial swarming motility, covering
    hyperflagellation, biosurfactant wetting agents, cell elongation, and surface
    sensing.), removed its baselined MISSING_SNIPPET row from conf/evidence_snippet_baseline.tsv,
    and appended curation_history entry via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000062
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-013
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/swarming_motility.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-013
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
- finding_id: F-C10S4-DEF-SRC-014
  issue_key: twitching-motility-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: twitching_motility.yaml now carries a verified verbatim snippet in record-level
    evidence[0].snippet for definition_source DOI:10.1146/annurev.micro.56.012302.160938
  description: 'Resolved Cycle 10 Stage 4 open finding F-C10S4-DEF-SRC-014 on data/traits/morphology/twitching_motility.yaml
    (traitmech:000061): populated record-level evidence[0].snippet for definition_source
    DOI:10.1146/annurev.micro.56.012302.160938 with the verified Europe PMC abstract
    quote (''Twitching motility is a mode of surface translocation mediated by the
    extension, tethering, and retraction of type IV pili.'') (Mattick reviews the
    genetics, PilA/PilB/PilT/PilQ machinery, extension-retraction mechanics, and physiological
    roles of type IV pili-mediated twitching motility.), removed its baselined MISSING_SNIPPET
    row from conf/evidence_snippet_baseline.tsv, and appended curation_history entry
    via scripts/curate_stage5_review_findings.py.'
  target_ids:
  - traitmech:000061
  field_paths:
  - definition_source
  - evidence
  - curation_history
  evidence_ids:
  - ev-prior-c10s4-review
  - ev-c10s5-def-src-014
  - ev-remediated-records
  - ev-stage5-writer
  - ev-snippet-audit
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/morphology/twitching_motility.yaml
    role: maintained TraitRecord YAML
  disposition_reason: 'Resolved in Cycle 10 Stage 5 (resolve_review_findings) under
    group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 via
    guarded writer scripts/curate_stage5_review_findings.py.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
    finding_id: F-C10S4-DEF-SRC-014
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
actions: []
limitations:
- 'This batch review covers the 14 morphology records remediated in Cycle 10 Stage
  5 under group G-C10S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002); the 5 cohort-level
  source-limited or upstream-blocked findings from Cycle 10 Stage 4 remain tracked
  under open GitHub issues #1982, #1983, #1984, #1985, and #364.'
- All 14 of the remediated morphology records carry repository-minted traitmech:NNNNNN
  identifiers (traitmech:000061..000074) backed by validated ROBOT templates awaiting
  upstream METPO release incorporation (#364, berkeleybop/metpo#535).
notes:
- 'Skills executed: .claude/skills/curate-yaml-record/SKILL.md and .claude/skills/review-yaml-record/SKILL.md.'
- Immutable Cycle 10 Stage 4 review bundle preserved untouched at reviews/structured/20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review/review.yaml.
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261104T211500Z-cycle10-stage4-corpus-record-and-cohort-review
  relationship: follow_up_remediation_verification
links:
- https://github.com/CultureBotAI/TraitMech/issues/2002
- https://github.com/CultureBotAI/TraitMech/issues/1982
- https://github.com/CultureBotAI/TraitMech/issues/1983
- https://github.com/CultureBotAI/TraitMech/issues/1984
- https://github.com/CultureBotAI/TraitMech/issues/1985
- https://github.com/CultureBotAI/TraitMech/issues/364
tags:
- cycle-10
- stage-05
- resolve-review-findings
- remediation-verification
```
