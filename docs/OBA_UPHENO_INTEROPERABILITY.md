# OBA and uPheno for microbial traits: fit with METPO and TraitMech

Assessment date: 2026-11-07; revised 2026-11-15 when it moved here from
[CultureBotAI/XMechBay#51](https://github.com/CultureBotAI/XMechBay/pull/51) after review. This is a research and modeling
assessment, not an implemented ontology mapping or schema migration.

## Papers and scope

The two works considered are their published versions:

- Stefancsik et al. (2023), [The Ontology of Biological Attributes
  (OBA)—computational traits for the life sciences](https://doi.org/10.1007/s00335-023-09992-1).
  [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10382347/).
- Matentzoglu et al. (2025), [The Unified Phenotype Ontology: a framework for
  cross-species integrative phenomics](https://doi.org/10.1093/genetics/iyaf027).
  [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11912833/).

OBA provides neutral biological attributes through Entity–Quality definitions,
design patterns, and logical classification. It distinguishes attributes from
phenotype states and measurement methods. Its formal design is species-independent,
but the paper describes its coverage focus as Metazoan traits. The framework is
applicable beyond that focus; the paper does not establish comprehensive microbial
coverage.

uPheno provides shared phenotype patterns, species-neutral grouping classes, and
cross-ontology mappings. Its reported integrations include fission yeast,
ascomycetes, Dictyostelium, and pathogen–host phenotypes (PHIPO, whose taxon
scope the paper lists as general), with varying integration depth. Microbes
therefore already participate, mainly as eukaryotic model organisms and as
pathogens. This does not demonstrate comprehensive bacterial or archaeal
ecophysiological coverage. The paper explicitly
leaves actual comparators and effect sizes to annotation metadata.

Two microbial ontologies matter here and neither paper discusses them: OMP
(Ontology of Microbial Phenotypes) and MicrO (Ontology of Prokaryotic Phenotypic
and Metabolic Characters). The METPO snapshot cites OMP 116 times and MicrO 61
times, every one as a definition source (`IAO:0000119` on a definition). The uPheno paper does not list
OMP among its integrated ontologies; whether current uPheno releases import or
map OMP was not checked. Any OBA or uPheno alignment for prokaryotic traits should
state its relation to OMP and MicrO terms that METPO already cites.

These statements describe the publications, not an exhaustive audit of subsequent
OBA or uPheno releases. The recommendations below are proposed applications to
microbial data, not experimental results reported by either paper.

## Complementary roles

| Resource or layer | Role | Microbial example |
|---|---|---|
| OBA | Neutral attribute: what varies | Cell length or a precisely defined growth rate |
| uPheno | Comparable phenotype state | Increased cell length relative to a reference |
| METPO | Microbial ecophysiological concepts and relations | Halophily, oxygen requirements, substrate use, growth optima |
| Observation/profile data | Organism-specific evidence and context | Strain, medium, assay, conditions, value, unit, comparator |
| TraitMech | Definitions, provenance, organism examples, and mechanism evidence | Supported processes and proteins associated with a trait |

The architecture should connect these layers without conflating them. A neutral
attribute is not equivalent to its increased or decreased state. An assay measures
an attribute but is not the attribute. A semantic mapping does not establish a
causal mechanism.

## What METPO already cites

Alignment does not start from nothing. The METPO `2026-06-12` snapshot used by
TraitMech (`data/raw/metpo.owl`) already gives OBA and uPheno classes as
definition sources (`IAO:0000119` on the definition) of five terms, alongside
other sources on the same axiom. The labels below are from OLS:

| METPO term | OBA or uPheno source (label) | Other ontology sources on the same definition |
|---|---|---|
| `METPO:1000881` cell length | `OBA:2040145` cell length ("The length of a cell.") | none |
| `METPO:1000882` cell width | `OBA:2040146` cell width ("The width of a cell.") | none |
| `METPO:1000601` oxygen preference | `UPHENO:0049673` response to oxygen levels phenotype ("Changed response to oxygen levels.") | none (plus the DSMZ OxygenTolerance schema and trait databases) |
| `METPO:1000703` non motile | `UPHENO:0034076` absent cell motility ("Lack of cell motility.") | `OMP:0000133` absence of motility; `OMP:0007488`, `OMP:0007489`, `OMP:0007490` |
| `METPO:1000872` non-spore forming | `UPHENO:0083394` absent sporulation ("Lack of sporulation.") | `OMP:0000018` absence of endospore formation; `OMP:0007232`, `OMP:0007236`, `OMP:0007434` |

These citations show exactly the boundaries this assessment is about:

- **Intraspecific phenotype versus neutral attribute.** METPO defines cell length
  as "a phenotype that inheres in a cell by virtue of its longer dimension when
  viewed on a plane". Its parent, `METPO:1000059` phenotype, is a quality that
  differentiates instances of a species from other instances of the same species.
  OBA defines cell length as "the length of a cell", a species-neutral biological
  attribute. OBA can inform the definition, but an equivalence would carry METPO's
  intraspecific-phenotype parent and its planar wording over to OBA. That needs
  the axiom-level review in pilot step 1 (berkeleybop/metpo#657).
- **Normal adaptation versus abnormal phenotype.** In uPheno this is axiomatic, not
  a matter of reading: all three uPheno classes above carry
  `has_modifier PATO:0000460` (abnormal). The uPheno paper states that every
  phenotype term represents a deviation from a reference phenotype. Oxygen
  preference is a normal adaptation (aerobe, anaerobe, microaerophile), so citing
  an abnormal "changed response" phenotype is the conflation the table below warns
  against, already present in METPO. For non-motile and non-spore-forming
  *species* there is no wild-type reference to deviate from. For a non-motile
  *mutant strain* there is, and METPO 1000703 can describe either case. The OMP
  sources on the same definitions model capability absence ("lacks the ability"),
  which fits species-level traits better.
- **Scope.** METPO 1000872 concerns endospores, while `UPHENO:0083394` covers all
  sporulation (GO:0043934). An exospore-forming organism such as *Streptomyces*
  is non-spore-forming in METPO's sense but not "absent sporulation".
  `OMP:0000018` (absence of endospore formation), already co-cited, is the precise
  match.

At revision `0c20b4c`, TraitMech did not carry these ontology sources through. The
[cell length](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/data/traits/morphology/cell_length.yaml),
[cell width](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/data/traits/morphology/cell_width.yaml),
[oxygen preference](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/data/traits/environment/oxygen_preference.yaml),
[non motile](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/data/traits/morphology/non_motile.yaml) and
[non-spore forming](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/data/traits/morphology/non_spore_forming.yaml)
records each cite a paper as `definition_source` instead. For the three uPheno
cases, leaving out the uPheno class may be the right outcome; the OMP sources are
closer ([#2090](https://github.com/CultureBotAI/TraitMech/issues/2090)).

## Concrete microbial modeling choices

| Concept | Recommended treatment | Boundary to preserve |
|---|---|---|
| Cell length and width | First candidates for OBA alignment; METPO already cites OBA as their definition source | Review bearer, quality, and logical axioms before asserting equivalence |
| Increased cell length after perturbation | Relative phenotype linked to the neutral attribute and an explicit control | Do not equate it with neutral cell length |
| Growth rate | Specify elongation, biomass increase, cell-count increase, or colony expansion | Different readouts are not interchangeable |
| Growth temperature optimum | Preserve the growth-response and ambient-temperature interpretation | It is not automatically cell/body temperature |
| Halophily or anaerobiosis | Preserve METPO's microbial definitions; revisit the oxygen-preference definition source | Normal adaptations are not abnormal phenotypes |
| Substrate use | Preserve the organism-level relation and chemical object | Chemical-use capability is not a chemical-amount measurement |

The existing [cell length record](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/data/traits/morphology/cell_length.yaml)
uses `METPO:1000881`; cell width uses `METPO:1000882`. The
[temperature optimum record](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/data/traits/environment/temperature_optimum.yaml)
uses `METPO:1000304`. No OBA or uPheno exact-match identifier is asserted here.
Label similarity alone is insufficient, especially where one source models a
quality and another models a phenotype containing that quality.

Keep single-cell, culture/population, and community scales distinct. A function
observed in a community need not be a capability of every member organism. Likewise,
isolation from an acidic environment does not by itself establish acidophily, and
failure to grow in one assay does not establish universal inability to grow.
The [METPO source snapshot](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/data/raw/metpo.owl)
already makes the environment/phenotype and conditional growth distinctions. The
uPheno definition sources discussed above raise a different issue, normal versus
abnormal.

## Fit with the existing implementation

This assessment inspected TraitMech commit
`0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a` and its METPO `2026-06-12` snapshot.
It does not assert that these are the latest upstream versions.

The [TraitMech schema](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/src/traitmech/schema/traitmech.yaml)
already separates several relevant concerns:

- Trait records preserve METPO identifiers, definitions, synonym scope, and parents,
  but not always METPO's definition source (see above).
- Cross-references are intended for true equivalents; broader/narrower or
  attribute-to-state relations need appropriately typed mappings.
- Causal edges require supporting evidence.
- Protein examples pair organism-specific protein instances with source taxa,
  separately from generic mechanism concepts.
- Graph scope distinguishes mechanisms from measurement/classification context.

Both the cell-length and temperature-optimum records explicitly label their graphs
`NONMECHANISTIC`. Ontology integration should respect these reviewed dispositions.
Phenotype similarity can prioritize candidate mechanisms for investigation, but
cannot by itself establish conserved machinery, homology, or causality.

Measured observations are out of scope for TraitMech itself. The
[deprecated-replacement proposal](DEPRECATED_REPLACEMENT_PROPOSAL.md#observation-value-records-stay-deprecated)
keeps observation-value records deprecated and places observations downstream in
KG-Microbe. A future `traitmech:Observation` class, if ever needed, would align to
STATO, OBI and QUDT. An OBA alignment is still useful for those downstream
observations: strain, versioned genome, genotype or perturbation, medium, assay,
growth phase, conditions, value and unit, uncertainty, comparator, and
measured-versus-predicted status can then be found through a shared attribute
concept. This assessment does not propose reopening that decision.
See the [curation playbook](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/docs/CURATION_PLAYBOOK.md)
and [grounding policy](https://github.com/CultureBotAI/TraitMech/blob/0c20b4c82a8b5ae4a883cbc536abfd6fdca6380a/docs/GROUNDING_POLICY.md).

## Recommended pilot and acceptance criteria

Start with one cell-dimension attribute before expanding to growth traits:

1. Review `METPO:1000881` and `OBA:2040145`, already linked as definition
   source, at the axiom level, including bearer, quality, and
   class-versus-property distinctions. The METPO-side discussion is
   [berkeleybop/metpo#657](https://github.com/berkeleybop/metpo/issues/657).
2. Record the appropriate mapping relation, evidence, source versions, and curator
   rationale in SSSOM. Use exact equivalence only when justified.
3. Outside TraitMech's records, in the pilot's own example packet or downstream,
   link one measured observation and one comparator-dependent phenotype, retaining
   strain, medium, growth phase, value/unit, and control metadata. The worked
   packet is being ported in [#2092](https://github.com/CultureBotAI/TraitMech/issues/2092).
4. Run logical classification checks. Verify the intended parent relationships and
   that neutral cell length does not become equivalent to increased cell length.
5. Confirm that mapping creates no unsupported causal edge in TraitMech, then assess
   expansion to additional dimensions and ecophysiological traits.

Success means that measurements and comparative phenotypes can be found through
shared attribute concepts while their experimental and biological scope remains
recoverable. This proposal changes no scientific data or ontology axioms.
