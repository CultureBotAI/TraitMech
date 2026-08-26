# TraitMech Protein and Taxon Exemplar Research

## Target

- Trait: {trait_label} ({trait_identifier})
- Definition: {definition}
- Existing canonical examples: {canonical_examples_summary}
- Existing gene/protein nodes: {protein_node_summary}
- Existing graph summary: {causal_graph_summary}

## Objective

Determine whether the existing graph for **{trait_label}** is mechanistic and,
if so, identify at least one exact protein instance whose experimentally
supported role and organism match one existing canonical example. The result is
research input for `data/traits/{trait_category_slug}/{trait_slug}.yaml`.

## Required Analysis

1. Decide `MECHANISTIC`, `NONMECHANISTIC`, or `REVIEW_NEEDED`, with a concise
   source-backed rationale. Do not add a token protein to a measurement,
   classification, numeric bin, hazard class, or upper-ontology context.
2. For each existing gene/protein node, decide whether it denotes a molecular
   function, protein family, named protein, or multisubunit complex. Recommend
   an exact GO, InterPro, NCBIfam, or Complex Portal grounding only when its
   definition matches. Explicitly flag broad labels that must remain label-only
   or be split.
3. Select one existing canonical taxon for which a primary paper identifies a
   concrete protein, gene, or complex component that causally supports the
   graph. Prefer direct genetic, biochemical, structural, or physiological
   evidence over genome annotation or review inference.
4. Report the current UniProtKB primary accession for that exact protein in the
   same taxon. Distinguish a complex from its components: a single subunit
   accession is an example component and must not be described as the entire
   complex.
5. For every proposed protein example, provide:
   - protein name and gene symbol;
   - UniProtKB primary accession;
   - NCBITaxon identifier and scientific name;
   - reviewed/unreviewed status, and reference-proteome accession if unreviewed;
   - exact role or complex-component role;
   - primary DOI (PMID only if no DOI exists);
   - a short contiguous verbatim snippet from the source; and
   - notes explaining how the snippet supports this protein in this taxon.

## Evidence Rules

- Prefer primary experimental papers with DOI citations.
- UniProt proves identity and taxonomy, not the causal role; cite the paper for
  the role and use UniProt only to verify the current accession and metadata.
- Never infer a taxon-protein pair from two unrelated sources.
- Mark family-only, taxon-mismatched, annotation-only, or review-only evidence
  uncertain and do not recommend it for direct curation.

## Output

Return a compact scope decision, a node-grounding review table, a protein/taxon
example table, DOI-first bibliography, and a final list of claims safe to
curate versus findings that remain uncertain.
