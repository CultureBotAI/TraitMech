---
provider: gpt-rosalind
model: GPT "Rosalind" (external, not a configured TraitMech provider)
pipeline_run: false
cached: false
supplied_on: '2026-08-31'
supplied_by: maintainer (pasted into the session; not produced by scripts/research_trait_edison.py)
manifest_row: none
manifest_row_reason: >-
  reports/trait_graph_audit_manifest.tsv is an APPEND-ONLY SPEND RECORD of calls
  this repository's pipeline actually made. This result was produced outside the
  pipeline and cost this repository nothing through it, so writing an `ok` row
  would assert a run that never happened. Deliberately omitted rather than
  overlooked -- this is the #245 question answered in the honest direction.
  The file is outside the resume namespace (`<slug>-deep-research-falcon.md`),
  so it cannot suppress a future call and `just audit-research-artifacts`
  does not flag it.
answers_hypothesis:
  record: data/traits/ecology/free_living.yaml
  trait_identifier: traitmech:000048
  discussion_prompt: >-
    Ectoine and glycine betaine both enable osmotic stress tolerance here, but
    trehalose is wired instead to environmental stress tolerance -- a node with
    no outgoing edge. Is that split a real distinction, or does trehalose belong
    on the osmotic route too?
  experiment_id: x-compatible-solute-partitioning
  would_support: >-
    trehalose loss costs nothing osmotically and only shows under desiccation or
    heat -- the split in the graph is real
  would_refute: >-
    the trehalose knockout is osmotically impaired -- it belongs on the osmotic
    route with the other two
verdict: REFUTED (high confidence, per the supplied analysis)
citations_resolvable: 0
citations_recovered_by_hand:
  - reference: DOI:10.1128/mBio.00390-21
    pmid: 33785618
    citation: >-
      Ledermann R, Emmenegger B, Couzigou J-M, Zamboni N, Kiefer P, Vorholt JA,
      Fischer H-M. Bradyrhizobium diazoefficiens Requires Chemical Chaperones To
      Cope with Osmotic Stress during Soybean Infection. mBio 2021.
    covers: >-
      The 400 mM sorbitol / 27 mM NaCl / 50 mM MgCl2 / 75 mM MgSO4 free-living
      phenotype, the TreF-1 trehalase phenocopy, the OtsC-dependent trehalose
      rescue, and the ectoine/hydroxyectoine-vs-glycine-betaine metabolomics.
  - reference: DOI:10.1128/AEM.02483-09
    pmid: 20023090
    citation: >-
      Sugawara M, Cytryn EJ, Sadowsky MJ. Functional Role of Bradyrhizobium
      japonicum Trehalose Biosynthesis and Metabolism Genes during Physiological
      Stress and Nodulation. Appl Environ Microbiol 2010;76(4):1071-1081.
    covers: >-
      The 60 mM NaCl growth inhibition, the absent desiccation defect for the
      low-trehalose otsA mutants at 50% RH, and the osmoprotectant conclusion.
corrections_to_this_artifact:
  - claim: >-
      "Adding 5 mM exogenous trehalose restored the delta-otsA mutant to nearly
      wild-type tolerance under sorbitol stress."
    status: UNVERIFIED CONCENTRATION
    detail: >-
      The rescue and its OtsC dependence are confirmed -- "While the otsA mutant
      was rescued to almost wild-type stress tolerance, trehalose did not enhance
      osmotolerance of the (otsCB-otsA) and otsCB mutants" -- but the source does
      not state a trehalose concentration for the free-living sorbitol experiment.
      The 5 mM figure could not be confirmed and was NOT carried into the record
      (PR #615). Treat it as unsupported.
citation_caveat: >-
  CRITICAL AS SUPPLIED, now partly discharged -- see citations_recovered_by_hand
  above, and PR #615 which applies the correction. As supplied, this artifact
  names organisms, genotypes and
  phenotypes but carries NO DOI, PMID, or other resolvable reference, and no
  verbatim source snippet. `CausalEdge.evidence` requires a `reference`, and
  docs/GROUNDING_POLICY.md requires an edge-specific snippet. The graph
  correction below therefore CANNOT be applied from this artifact alone: the
  two primary studies must be identified and cited first. Treat this as a
  reviewed lead, not as evidence.
---

# free-living: is the trehalose / osmotic-tolerance split real?

Verdict: **Refuted — high confidence.**

The matching experimental system is *Bradyrhizobium diazoefficiens* USDA 110. In this
organism, trehalose is directly required for free-living osmotic-stress tolerance. Its
placement only under a terminal `environmental_stress_tolerance` node is therefore not a
biologically meaningful separation from ectoine-mediated osmoprotection.

## Decisive falsification

A mutant lacking the OtsAB trehalose-biosynthesis pathway, Δ(otsCB-otsA), showed reduced
survival under:

- 400 mM sorbitol, a nonionic osmotic challenge;
- 27 mM NaCl;
- 50 mM MgCl₂;
- 75 mM MgSO₄.

The sorbitol phenotype is particularly decisive because it separates general osmotic
pressure from salt-specific ion toxicity. The same mutant was not equivalently defective
under alkaline-pH or oxidative-stress tests, making the phenotype more specifically
osmotic rather than merely "general environmental stress."

That directly meets the refutation criterion: the trehalose knockout is osmotically
impaired.

## The phenotype is causally attributable to trehalose

Several controls make a deletion artifact unlikely:

- Single-pathway mutants affecting `otsA` or `otsB` were also impaired across a sorbitol
  gradient.
- Introducing a cytoplasmic trehalase into otherwise wild-type cells depleted
  intracellular trehalose and reproduced the osmotic-stress phenotype.
- Adding 5 mM exogenous trehalose restored the ΔotsA mutant to nearly wild-type tolerance
  under sorbitol stress.
- Rescue depended on the trehalose transporter OtsC, as expected for genuine intracellular
  trehalose complementation.

Together, knockout, biochemical depletion, and metabolite rescue establish a direct causal
chain:

    trehalose accumulation → free-living osmotic-stress tolerance

## Independent replication

An earlier USDA 110 study, published under the name *Bradyrhizobium japonicum*, reached
the same conclusion using independently constructed mutants. Strains disrupted in the
OtsA pathway were inhibited by 60 mM NaCl, while mutants simultaneously lacking the OtsAB
and TreYZ routes either grew extremely poorly or failed to grow. The severity tracked the
loss of trehalose accumulation, leading the authors to identify trehalose as an
osmoprotectant during salt-induced osmotic stress.

This independent result reduces the chance that the newer phenotype depends on one
particular construct or assay.

## The desiccation result points in the opposite direction from the proposed split

In the earlier study, low-trehalose `otsA` and `otsA treY` mutants were not detectably
worse than wild type during the tested desiccation exposure at 50% relative humidity. Some
`treS`-pathway mutants were desiccation-sensitive, but that sensitivity did not correlate
cleanly with cellular trehalose abundance and was interpreted as a pathway-specific
metabolic effect rather than proof that trehalose accumulation itself was the desiccation
determinant.

So, in the available USDA 110 data, the clean phenotype is almost the reverse of the
proposed categorization:

- **Osmotic stress:** clear trehalose-loss phenotype.
- **Desiccation:** no corresponding defect for the principal low-trehalose `otsA` mutants
  in the cited assay.
- **Heat:** not needed to decide the hypothesis, because the osmotic phenotype already
  falsifies the proposed exclusive split.

## Ectoine and glycine-betaine nuance

The later study engineered a combined pathway intended to produce glycine betaine,
ectoine, and hydroxyectoine. This construct restored salt tolerance and partially restored
sorbitol tolerance in the trehalose-deficient strain, showing that another compatible
solute can substitute for trehalose-mediated osmoprotection. However, metabolomics
detected substantial ectoine/hydroxyectoine, while glycine betaine remained only at minute
levels also seen in parental strains. Thus, the experiment directly supports functional
replacement by ectoine/hydroxyectoine; it does not cleanly isolate glycine betaine as the
rescuing molecule.

## Recommended graph correction

The evidence supports adding or restoring:

    free_living
      └─ trehalose biosynthesis / accumulation
           └─ osmotic_stress_tolerance

`environmental_stress_tolerance` may remain as a broader parent category, but it should
not be a terminal branch that prevents trehalose from reaching `osmotic_stress_tolerance`.
A biologically faithful representation would treat osmotic tolerance as a subtype of
environmental-stress tolerance, not as a category reserved for ectoine and glycine
betaine.

A useful additional relation would be:

    ectoine / hydroxyectoine
      └─ functionally substitutes for trehalose
           └─ osmotic_stress_tolerance

**Bottom line:** the proposed split is not real for this system. Trehalose has a directly
demonstrated, rescue-validated role in free-living osmotic tolerance, while the available
desiccation evidence does not support restricting it to a desiccation/heat-only branch.
