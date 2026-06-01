# Candidate missing ENVIRONMENT traits — literature-backed proposal

**Date:** 2026-05-28 · **Curator:** claude (LLM-assisted) · **Status of all entries:** `PROPOSED`

## Why these traits

The ENVIRONMENT category (103 reviewed traits) is densely built out along four axes —
pH (27), temperature (28), salinity/NaCl (26), and oxygen (12) — but a survey of
`data/traits/environment/` found **no coverage** of several well-established environmental
microbial trait dimensions. This proposal adds **18 candidate traits** across the four
genuinely-absent axes below, each backed by **≥ 2 distinct literature citations** spread
across `definition_source` and `evidence[].reference`.

Each candidate is authored as a normal `TraitRecord` YAML in `data/traits/environment/`
with `mapping_status: PROPOSED`, so it flows through the existing closed-mode LinkML
validation. The ≥ 2-citation bar is enforced for every PROPOSED record by
`scripts/audit_proposals.py` (wired into `just qc` / CI →
`reports/proposal_citation_audit.tsv`).

### Identifiers
All 18 are new to METPO (verified: 0 hits for piezo/pressure/radiation/desiccation/xerophil/
metal/mercury/cadmium/arsenic/copper/zinc in `data/raw/metpo.owl`), so they are minted under
the reserved synthetic prefix `traitmech:000001`–`traitmech:000018` per
`.claude/skills/manage-identifiers/SKILL.md`. Qualitative traits parent to `METPO:1000059`
(*phenotype*) — the same upper class `oxygen preference` uses — and the metal-specific and
radiation-specific sub-variants parent to their family head (`traitmech:000012` /
`traitmech:000007`) to form small hierarchies.

### Already in METPO (not proposed here)
`oligotrophic` (METPO:1000654) and `copiotrophic` (METPO:1000642) **already exist in METPO**
but are not yet seeded into the corpus. They are intentionally excluded from this proposal —
they are a *seeding* gap, not a vocabulary gap — and should be imported via `seed_from_metpo`.

---

## Proposed traits

### Pressure / piezophily (deep-sea, deep-subsurface)
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000001 | piezophilic | METPO:1000059 | DOI:10.3389/fmolb.2022.1058381; DOI:10.1099/ijsem.0.001671 |
| traitmech:000002 | obligately piezophilic | traitmech:000001 | DOI:10.1038/srep27289; DOI:10.1099/ijsem.0.001671 |
| traitmech:000003 | piezotolerant | METPO:1000059 | DOI:10.3389/fmolb.2022.1058381; DOI:10.1099/ijsem.0.001671 |
| traitmech:000004 | pressure optimum | METPO:1000059 | DOI:10.1099/ijsem.0.001671; DOI:10.3389/fmolb.2022.1058381 |
| traitmech:000005 | pressure range | METPO:1000059 | DOI:10.1099/ijsem.0.001671; DOI:10.3389/fmolb.2022.1058381 |
| traitmech:000006 | pressure delta | METPO:1000059 | DOI:10.3389/fmolb.2022.1058381; DOI:10.1099/ijsem.0.001671 |

Key evidence: *"Microorganisms adapted to HHP are usually known as piezophiles, referring to
their preference for high pressure"* (DOI:10.3389/fmolb.2022.1058381). Organism example —
*Colwellia marinimaniae* MTCD1, the most piezophilic organism described: *"growth range of
80–140 MPa (optimum, 120 MPa) at 6 °C"* (DOI:10.1099/ijsem.0.001671). Obligate example —
*Pyrococcus yayanosii* (DOI:10.1038/srep27289).

### Radiation tolerance
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000007 | radiotolerant | METPO:1000059 | DOI:10.1101/cshperspect.a012765; DOI:10.3390/genes14091803 |
| traitmech:000008 | ionizing radiation tolerant | traitmech:000007 | DOI:10.3390/genes14091803; DOI:10.1101/cshperspect.a012765 |
| traitmech:000009 | UV radiation tolerant | traitmech:000007 | DOI:10.3390/genes14091803; DOI:10.1101/cshperspect.a012765 |

Key evidence: *"Deinococcus radiodurans … showcasing an impressive resistance to a wide array
of stressors, including ionizing radiation, desiccation, UV radiation, and oxidizing agents"*
and *"D10 values exceeding 12 kGy for gamma radiation and 700 J/m2 for UV-C radiation"*
(DOI:10.3390/genes14091803); manganese-antioxidant mechanism (DOI:10.1101/cshperspect.a012765).

### Desiccation / water activity
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000010 | desiccation tolerant | METPO:1000059 | DOI:10.3390/microorganisms10020432; DOI:10.3390/genes14091803 |
| traitmech:000011 | xerophilic | METPO:1000059 | DOI:10.1098/rstb.2004.1502; DOI:10.3390/microorganisms10020432 |

Key evidence: anhydrobiosis = *"the ability of some organisms to lose all or almost all water
and enter a state of suspension where the metabolism comes to a reversible standstill"*
(DOI:10.3390/microorganisms10020432); xerophile growth *"at a water activity (aw) of 0.61, the
lowest aw value for growth recorded to date"* (DOI:10.1098/rstb.2004.1502).

### Heavy-metal / metalloid tolerance
| ID | Label | Parent | Citations |
|----|-------|--------|-----------|
| traitmech:000012 | metal tolerant | METPO:1000059 | PMID:12829273; DOI:10.3389/fmicb.2020.00047 |
| traitmech:000013 | cadmium tolerant | traitmech:000012 | DOI:10.1111/j.1365-2958.2009.06792.x; DOI:10.3389/fmicb.2020.00047 |
| traitmech:000014 | zinc tolerant | traitmech:000012 | DOI:10.1111/j.1365-2958.2009.06792.x; DOI:10.3389/fmicb.2020.00047 |
| traitmech:000015 | cobalt tolerant | traitmech:000012 | DOI:10.1111/j.1365-2958.2009.06792.x; DOI:10.3389/fmicb.2020.00047 |
| traitmech:000016 | mercury tolerant | traitmech:000012 | DOI:10.1016/S0168-6445(03)00046-9; PMID:12829273 |
| traitmech:000017 | arsenic tolerant | traitmech:000012 | DOI:10.3389/fmicb.2018.02473; DOI:10.3389/fmicb.2020.00047 |
| traitmech:000018 | copper tolerant | traitmech:000012 | DOI:10.1007/s10565-013-9262-1; DOI:10.3389/fmicb.2020.00047 |

Key evidence: efflux-mediated resistance via *"CBA efflux pumps … P-type ATPases, cation
diffusion facilitator and chromate proteins"* (PMID:12829273); model metallophile
*Cupriavidus metallidurans* BS1 — *"resistance to Zn2+ … MIC of 20 mM, Cd2+ (2.5 mM), Co2+
(20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 µM) and Pb2+ (1.7 mM)"*
(DOI:10.3389/fmicb.2020.00047); mercury *mer*/MerA (DOI:10.1016/S0168-6445(03)00046-9);
arsenic *ars*/ArsB (DOI:10.3389/fmicb.2018.02473); copper ATPase efflux
(DOI:10.1007/s10565-013-9262-1); czc cobalt-zinc-cadmium efflux
(DOI:10.1111/j.1365-2958.2009.06792.x).

---

## Citation index
| Reference | Work |
|-----------|------|
| DOI:10.3389/fmolb.2022.1058381 (PMID:36685280) | Microbial membrane lipid adaptations to high hydrostatic pressure |
| DOI:10.1099/ijsem.0.001671 (PMID:27902293) | *Colwellia marinimaniae* sp. nov., hyperpiezophile, Challenger Deep |
| DOI:10.1038/srep27289 (PMID:27250364) | HHP adaptive strategies in obligate piezophile *Pyrococcus yayanosii* |
| DOI:10.1101/cshperspect.a012765 (PMID:23818498) | Biology of Extreme Radiation Resistance: *Deinococcus radiodurans* |
| DOI:10.3390/genes14091803 (PMID:37761943) | NER/Rec-dependent UV-radiation resistance in *Deinococcus* |
| DOI:10.3390/microorganisms10020432 (PMID:35208886) | Introduction to Bacterial Anhydrobiosis |
| DOI:10.1098/rstb.2004.1502 (PMID:15306390) | Grant, "Life at low water activity" |
| PMID:12829273 | Nies, "Efflux-mediated heavy metal resistance in prokaryotes" |
| DOI:10.3389/fmicb.2020.00047 (PMID:32117100) | *Cupriavidus metallidurans* BS1 genome, metal MICs |
| DOI:10.1016/S0168-6445(03)00046-9 (PMID:12829275) | Barkay et al., "Bacterial mercury resistance from atoms to ecosystems" |
| DOI:10.3389/fmicb.2018.02473 (PMID:30405552) | Distribution of Arsenic Resistance Genes in Prokaryotes |
| DOI:10.1007/s10565-013-9262-1 (PMID:24072389) | Molecular basis of active copper resistance in Gram-negative bacteria |
| DOI:10.1111/j.1365-2958.2009.06792.x (PMID:19602147) | CzcP efflux (cobalt-zinc-cadmium) in *C. metallidurans* CH34 |

## How this is validated
- **Schema:** `MappingStatusEnum` gained a `PROPOSED` value (`src/traitmech/schema/traitmech.yaml`).
- **Citation bar:** `scripts/audit_proposals.py` requires ≥ 2 distinct, well-formed citations
  (PMID/DOI/URL) per PROPOSED record, counted across `definition_source` ∪ `evidence[].reference`.
  Wired into `just qc` and the `qc` CI workflow; report at `reports/proposal_citation_audit.tsv`.
- **Tests:** `tests/test_audit_proposals.py` locks the rule (pass ≥2, fail single/placeholder/malformed).
- **Result:** `just validate-strict` → 0 errors over 375 files; `audit-proposals` → 18/18 passing.

## Follow-ups (out of scope here)
- Add evidence-backed `causal_graphs` once a candidate is promoted `PROPOSED` → `REVIEWED`.
- Mint intermediate METPO axis classes (e.g. "pressure preference", "radiation tolerance") and
  re-parent, rather than parenting directly to `METPO:1000059` (phenotype).
- Upstream the `traitmech:` IDs into METPO via the `metpo-proposal` skill.
- Seed the existing METPO `oligotrophic` / `copiotrophic` classes into the corpus.
