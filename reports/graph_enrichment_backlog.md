# Causal-graph enrichment backlog (Edison completeness audit)

> **Historical paid-research snapshot — do not use for prioritization.** This
> artifact has no local regeneration path, and most source graphs have changed
> since the sweep (#443, #480). Use `just trait-priority`, which reads live
> corpus state. After selecting a record, this backlog remains useful as a
> DOI-backed lead, but verify every proposal against the current graph before
> applying it.

Generated from a 353-agent per-trait audit comparing each trait's existing `causal_graphs` against its Edison deep-research report. 351 traits flagged high/medium priority.

**Verdicts:** {'shallow': 228, 'skeletal': 110, 'adequate': 15}  
**Priority:** {'medium': 102, 'high': 249, 'low': 2}


## HIGH priority

### ecology/biofilm_formation  — *skeletal* (2 edges)
- **Missing modules:** c-di-GMP regulatory switch, quorum sensing signaling system, eDNA structural module, functional amyloid fibers, biofilm lifecycle stages (attachment/maturation/dispersal), environmental sensing cascades
- `c-di-GMP —promotes→ planktonic-to-sessile transition`  (DOI:10.3390/w17131944)
- `quorum sensing autoinducers —regulate→ biofilm formation`  (DOI:10.3390/bacteria3030008)
- `extracellular DNA —stabilizes→ biofilm ECM`  (DOI:10.1042/BCJ20210301)
- `extracellular DNA —nucleates→ amyloid-like fiber formation`  (DOI:10.1042/BCJ20210301)
- `extracellular matrix —required_for→ biofilm-defining properties`  (DOI:10.1042/BCJ20210301)
- `nitric oxide —induces→ biofilm dispersal`  (DOI:10.3390/antibiotics13111047)
- _Existing graph captures EPS-biofilm link but misses core generic mechanisms: c-di-GMP switch, QS regulation, eDNA structural biology, multi-stage lifecycle, and dispersal signals documented across diverse bacterial taxa in recent peer-reviewed reviews._

### ecology/biosafety_level_1  — *skeletal* (2 edges)
- **Missing modules:** virulence trait absence mechanism, risk assessment criteria (pathogenicity, transmission, stability, dose, concentration, origin, prophylaxis, experience), risk group 1 agent classification
- `specific virulence traits —enable→ disease causation`  (DOI:10.3390/microorganisms11020344 (Pokharel et al. 2023): ')
- `absence of specific virulence traits —qualifies_for→ biosafety level 1`  (DOI:10.2172/1887109 (Siegel 2022): Virulence-factor review s)
- `risk group 1 agent —aligns_with→ biosafety level 1`  (DOI:10.2172/1887109 (Siegel 2022): 'Risk Group 1: Agents not)
- `pathogenicity —is_risk_assessment_determinant_of→ biosafety level selection`  (DOI:10.2172/1887109 (Siegel 2022): Risk assessment criteria )
- `transmission route —is_risk_assessment_determinant_of→ biosafety level selection`  (DOI:10.2172/1887109 (Siegel 2022): Risk assessment criteria )
- `agent infectious dose —is_risk_assessment_determinant_of→ biosafety level selection`  (DOI:10.2172/1887109 (Siegel 2022): Infectious dose listed am)
- _Existing graph captures the top-level outcome (low hazard → BSL-1) but lacks the mechanistic backbone: virulence traits, risk group classification, and multi-factor risk assessment logic that formally define an agent as BSL-1 candidate._

### ecology/biosafety_level_2  — *skeletal* (2 edges)
- **Missing modules:** risk assessment criteria (pathogenicity, transmission, prophylaxis, community spread), operational containment module (BSC, PPE, training, access control), aerosol-hazard procedure link, waste decontamination controls
- `pathogenicity —influences assignment of→ biosafety level 2`  (Kaufer 2020 specifies pathogenicity as one of four risk-grou)
- `mode/ease of transmission —influences assignment of→ biosafety level 2`  (Kaufer 2020 identifies transmission mode as critical risk cr)
- `aerosol/splash-generating procedure —necessitates use of→ biological safety cabinet (Class I/II)`  (Ta 2018 and Kaufer 2020 mandate BSC use for procedures gener)
- `appropriate PPE (lab coat, gloves, eye/face protection) —mitigates risk in→ biosafety level 2`  (Kaufer 2020 specifies PPE as required BSL-2 control element)
- `restricted laboratory access —is required for→ biosafety level 2`  (Ta 2018 and Kaufer 2020 list restricted access as core BSL-2)
- `autoclave or alternate decontamination capability —reduces exposure from→ infectious materials/waste`  (Ta 2018 and Kaufer 2020 highlight accessible autoclave and r)
- _Existing graph captures top-level classification outcome but misses generic risk-assessment criteria and operational controls that define the BSL-2 mechanism; report identifies 13 generic curatable edges across these dimensions plus procedure-hazard linking._

### ecology/biosafety_level_3  — *skeletal* (2 edges)
- **Missing modules:** aerosol transmission capability, low infectious dose mechanism, environmental persistence (spore stability), laboratory-acquired infection history, negative pressure containment, HEPA filtration
- `aerosol transmission capability —enables→ inhalation exposure risk`  (DOI:10.1089/apb.2022.0038, DOI:10.1089/apb.2022.0042 (Blacks)
- `low inhalational infectious dose —increases_severity_of→ aerosol transmission risk`  (DOI:10.1089/apb.2022.0038 (M. tuberculosis ID50 <10 bacilli)
- `environmental persistence —prolongs_exposure_window_for→ inhalation exposure risk`  (DOI:10.1089/apb.2022.0042 (B. anthracis endospore environmen)
- `inhalation exposure risk —necessitates→ negative pressure airflow`  (DOI:10.64483/jmph-115 (negative pressure 2.5–10 Pa required )
- `inhalation exposure risk —necessitates→ HEPA filtration`  (DOI:10.64483/jmph-115 (HEPA exhaust 99.97% removal for ≥0.3 )
- `serious pathogen hazard —characterized_by→ laboratory-acquired infection history`  (DOI:10.1089/apb.2022.0042 (Brucella 378 LAIs reported 1979–2)
- _Existing graph is a classification stub only; it lacks the mechanistic foundation (infectious dose, aerosol capability, persistence) and engineering-control layer (negative pressure, HEPA) that the report establishes as generic, broadly-applicable drivers of BSL-3 classification._

### ecology/habitat_association  — *skeletal* (2 edges)
- **Missing modules:** environmental factor filtering (pH, salinity, oxygen), microhabitat partitioning (mucosa vs lumen), assembly process framework (selection/drift/dispersal), osmolyte transport/synthesis gene enrichment, carbon metabolism pathway specialization
- `salinity —selects_for→ osmolyte transport and synthesis genes`  (DOI:10.1186/s40168-024-01979-7 — Saline-lake microbiomes pos)
- `pH —selects_for→ Mrp-type Na+:H+ antiporter (mrpABCDEFG)`  (DOI:10.1101/2024.09.17.613589 — pH-associated adaptive trait)
- `environmental stress —increases→ selection in community assembly`  (DOI:10.1038/s41564-023-01573-x — Groundwater stress (pH, cob)
- `freshwater habitat —enriches→ carbon fixation genes`  (DOI:10.1186/s40168-024-01979-7 — Tibetan lake atlas: freshwa)
- `mucosa —differentiates→ lumen microbial community composition`  (DOI:10.1038/s41467-024-44720-6 — Human surface organ atlas ()
- `cooperation genes —increases→ niche breadth`  (DOI:10.1101/2024.10.05.616009 — Broad phylogenetic analysis:)
- _Existing graph captures only the top-level habitat-community link; lacks intermediate mechanistic nodes (environmental factors, assembly processes, functional gene systems) that are well-documented in recent literature._

### ecology/host_associated  — *skeletal* (2 edges)
- **Missing modules:** adhesin-mediated attachment, chemotaxis signaling (MCP/CheA/CheY), c-di-GMP/cAMP second messenger switch, biofilm maturation (irreversible attachment + EPS), host glycan recognition and utilization, mucus-layer niche structure, epithelial shedding/turnover constraint, host exudate-driven nutrient acquisition
- `host_adhesins —enable→ attachment_to_host_surface`  (DOI:10.1093/femsre/fuae008 — flagella, pili, fimbriae, and a)
- `chemotaxis_signaling —enables→ recruitment_toward_host_cues`  (DOI:10.3390/biology13020095)
- `c_di_GMP_cAMP —regulates→ transition_to_irreversible_attachment`  (DOI:10.1093/femsre/fuae008 — c-di-GMP and cAMP regulate tran)
- `host_glycans —serve_as_substrate_for→ microbial_growth_and_persistence`  (DOI:10.1016/j.chom.2023.12.014)
- `mucus_layer_structure —enables→ niche_differentiation_and_persistence`  (DOI:10.1128/ecosalplus.esp-0006-2023 — structured inner (fir)
- `host_exudates —provides_nutrient_and_signal_pool→ rhizobacterial_growth`  (DOI:10.1093/femsre/fuad066 — plant root exudates supply 11–4)
- _The existing host_associated graph captures only the trait-outcome abstraction; it critically lacks mechanistic depth in adhesion, signal sensing, biofilm formation, nutrient utilization, and host structural/temporal factors documented in recent literature._

### ecology/nitrogen_fixing_symbiosis  — *skeletal* (2 edges)
- **Missing modules:** flavonoid-Nod factor initiation, calcium spiking cascade, CCaMK/CYCLOPS/NIN transcriptional hub, infection thread formation, nodule organogenesis, oxygen homeostasis (diffusion barrier + leghemoglobin), microaerobic environment protection, nitrogenase enzymatic mechanism, organic acid exchange, iron cofactor requirement, phosphate requirement for signaling/ATP
- `Flavonoids —induce production of→ Nod factor`  (10.3389/fpls.2023.1284720)
- `Nod factor —activates→ NFR1/NFR5 receptor system`  (10.3389/fpls.2023.1284720)
- `CCaMK/DMI3 —phosphorylates→ CYCLOPS/IPD3`  (10.1093/pcp/pcae128)
- `CYCLOPS/IPD3 —activates transcription of→ NIN`  (10.3389/fpls.2023.1284720)
- `Leghemoglobin —buffers→ oxygen concentration in nodules`  (10.3389/fpls.2023.1284720)
- `Microaerobic environment —enables→ nitrogenase activity`  (10.3389/fpls.2023.1284720)
- _The existing graph misses the entire mechanistic scaffolding (signaling cascade, transcriptional control, developmental processes, oxygen homeostasis, nutrient exchange) that the report well-documents from 2023-2024 peer-reviewed sources; expansion is high-priority to capture generic RNS mechanism._

### ecology/parasitism  — *skeletal* (2 edges)
- **Missing modules:** colonization via adhesin-receptor binding, nutrient acquisition from host metals and hemoglobin, immune evasion and persistence mechanisms, dissemination within host tissues, environmental and transmission-mode modifiers
- `bacterial adhesin activity —promotes→ host colonization`  (DOI:10.1093/femsre/fuae019 — adhesins critical for adherence)
- `host colonization —enables→ host resource exploitation`  (DOI:10.1093/femsre/fuae019, DOI:10.3389/fcimb.2023.1111502 —)
- `hemoglobin uptake mechanism —promotes→ nutrient acquisition from host`  (DOI:10.3389/fcimb.2023.1150054 — Hb/heme utilization by prot)
- `immune evasion via secretion system effectors —enables→ parasite survival within host`  (DOI:10.3389/fimmu.2023.1303072, DOI:10.1128/mbio.00060-23 — )
- `pathogen dissemination via plasminogen activation —exacerbates→ host tissue damage`  (DOI:10.1093/femsre/fuae019 — plasminogen binding/activation )
- `newly acquired facultative endosymbiont state —promotes→ parasitic resource exploitation`  (DOI:10.1002/ece3.11705 — newly acquired endosymbionts often )
- _Existing parasitism graph is a bare definitional stub (3 nodes, 2 edges); report identifies at least 5 major generic mechanistic modules (colonization, nutrient acquisition, immune evasion, dissemination, transmission-mode modifiers) with strong, broadly-applicable evidence — urgent enrichment needed to capture causal mechanisms upstream and parallel to the resource exploitation core._

### ecology/predatory_bacterium  — *skeletal* (2 edges)
- **Missing modules:** prey attachment via T4aP, cell wall modification, bdelloplast formation, intraperiplasmic growth compartment, exit-associated lysis, prey recognition via adhesins
- `Type IV pili/T4aP —mediates attachment to→ prey outer membrane`  (10.1038/s41564-023-01401-2)
- `prey-cell-wall modification enzymes —causes→ bdelloplast formation`  (10.1038/s41467-024-47412-3)
- `bdelloplast —provides environment for→ intraperiplasmic growth and predator replication`  (10.1038/s41564-023-01401-2)
- `exit-associated lytic activity —causes→ prey cell wall lysis and progeny release`  (10.1038/s41564-023-01401-2)
- `MAT adhesin repertoire —enables recognition of→ diverse prey surface epitopes`  (10.1038/s41564-023-01552-2)
- `Bd0875 MIDAS-family adhesin —promotes→ successful prey invasion`  (10.1038/s41467-024-47412-3)
- _Existing graph captures only high-level abstraction; generic research identifies six core mechanistic modules spanning detection, invasion, replication, and exit phases that should be incorporated to reach adequate coverage._

### ecology/saprotrophy  — *skeletal* (2 edges)
- **Missing modules:** extracellular cellulase cascade (CBH+EG+β-glucosidase), lignin oxidation by laccase/peroxidases, carbon catabolite repression logic (glucose/CreA + cellobiose induction), hemicellulose depolymerization (xylanase/mannanase), Mn2+/Mn3+ mediator cycling for lignin attack, bacterial CCR signaling (CRP-cAMP, CcpA-HPr)
- `cellobiohydrolase + endoglucanase + beta-glucosidase —enables_coordinated_depolymerization_of→ cellulose`  (DOI:10.1093/jambio/lxac002)
- `laccase —oxidatively_depolymerizes→ lignin`  (DOI:10.1093/jambio/lxac002)
- `manganese_peroxidase —catalyzes_H2O2_dependent_oxidation_of→ lignin`  (DOI:10.1093/jambio/lxac002)
- `glucose —activates_carbon_catabolite_repression_repressing→ cellulase_genes`  (DOI:10.1093/jambio/lxac002)
- `cellobiose_and_sophorose —induce_transcription_of→ cellulase_genes`  (DOI:10.1093/jambio/lxac002)
- `extracellular_CAZymes —hydrolyze_and_solubilize→ complex_insoluble_organic_matter`  (DOI:10.1093/ismejo/wrae073)
- _The existing graph is a minimal phenotypic sketch; the research report reveals a rich, well-annotated biochemical mechanism (cellulase cascades, lignin oxidation, CCR regulation, hemicellulose breakdown) that is generic across saprotrophic taxa and deserves curation into LayerMech via at least 6 core mechanistic edges and supporting enzyme/chemical nodes."_

### ecology/soil_dwelling  — *skeletal* (2 edges)
- **Missing modules:** flagellar motility response to carbon availability, dormancy/sporulation stress response, oligotrophy adaptation to nutrient limitation, stress-tolerance phenotype under aridity, biogeochemical trait trade-offs (decomposition vs stress-tolerance)
- `high soil carbon availability —selects for→ flagellar motility`  (10.1093/ismejo/wrae067 — Ramoneda et al. quantified flagella)
- `extreme climatic events —induce upregulation of→ dormancy and sporulation genes`  (10.1038/s41586-024-08185-3 — Knight et al. Nature multi-site)
- `low available organic carbon —enriches for→ oligotrophic bacterial phenotype`  (10.1093/ismeco/ycae081 — Dragone et al. show oligotroph-enri)
- `aridity and low precipitation —selects for→ small-genome stress-tolerant soil bacterial communities`  (10.1038/s41564-023-01465-0 — Piton et al. Nature Microbiolog)
- `high soil precipitation —selects for→ large-genome metabolically-versatile soil bacterial communities`  (10.1038/s41564-023-01465-0 — Piton et al. report MCOA1 incre)
- `soil habitat matrix structure —alters expression of→ extracellular enzyme deployment`  (10.1101/2024.10.02.616266 — Rodríguez-Ramos et al. show Stre)
- _The existing soil-dwelling graph captures habitat-trait and trait-biogeochemical links but is missing major generic mechanistic modules (motility, dormancy, oligotrophy, stress-tolerance trait selection) that recent 2023-2024 peer-reviewed evidence strongly supports as universal soil-dwelling adaptations._

### ecology/symbiosis  — *skeletal* (2 edges)
- **Missing modules:** chemosensing and chemotaxis machinery, adhesion and attachment mechanisms, biofilm formation and EPS matrix, c-di-GMP signaling regulation, envelope modifications for immune evasion, two-component systems for host cue sensing, host glycome interface and mucin interactions
- `symbiotic_interaction —requires→ chemotaxis_machinery`  (Wiesmann et al. (2023, DOI:10.1093/femsre/fuac048): 'Chemota)
- `host_metabolites_and_exudates —create_concentration_gradients_sensed_by→ chemotaxis_machinery`  (Liu et al. (2024, DOI:10.1093/femsre/fuad066): 'Plants exude)
- `flagellar_motility —enables→ initial_host_colonization`  (Liu et al. (2024, DOI:10.1093/femsre/fuad066): 'chemotaxis a)
- `bacterial_adhesins —are_prerequisite_for→ persistent_host_colonization`  (Lin et al. (2024, DOI:10.3390/microorganisms12051026): 'Bind)
- `biofilm_formation —supports→ persistent_host_association`  (Wiesmann et al. (2023, DOI:10.1093/femsre/fuac048): 'biofilm)
- `c-di-GMP_upregulation —increases→ biofilm_formation_and_host_association`  (Obeng et al. (2023, DOI:10.1038/s41564-023-01468-x): experim)
- _The existing graph captures only the top-level trait definition but completely omits generic mechanistic modules (chemotaxis, biofilm, adhesion, c-di-GMP signaling, immune evasion) that the research report explicitly frames as conserved prerequisites for colonization and persistence across the mutualism–commensalism–parasitism continuum._

### environment/acidotolerant  — *skeletal* (4 edges)
- **Missing modules:** proton-consuming amino-acid decarboxylation (Gad/Adi/Cad systems), F-type ATP synthase reversal for proton extrusion, periplasmic proteostasis via HdeA/HdeB chaperones, membrane lipid remodeling (cyclopropane fatty acids), cation/H+ antiporter-mediated ion exchange, oxidative stress defense (SodB, KatE)
- `F0F1-ATPase —consumes→ intracellular H+`  (DOI:10.3390/microorganisms12091774 — 'reverses to hydrolyze )
- `glutamate decarboxylase system (GadA/GadB/GadC) —maintains→ intracellular pH homeostasis`  (DOI:10.3390/microorganisms12091774 — 'GadA/B decarboxylate g)
- `cation/H+ antiporter —contributes to→ cytoplasmic pH control`  (DOI:10.1038/nrmicro2549 — 'Na+/H+ and K+/H+ antiporters supp)
- `cyclopropane fatty acid synthesis —reduces→ inward proton leakage`  (DOI:10.3390/microorganisms12091774 — 'conversion of unsatura)
- `periplasmic chaperone HdeA/HdeB —prevents→ protein aggregation at low pH`  (DOI:10.3390/microorganisms12091774 — 'HdeA (pH 1-3) and HdeB)
- `ROS scavengers (SodB, KatE) —contribute to→ acid stress resistance`  (DOI:10.3390/microorganisms12081565 — 'synthetic acid-toleran)
- _Existing graph captures only the high-level homeostasis logic but lacks the mechanistic depth on proton-consuming metabolic cycles, bioenergetic systems, membrane remodeling, and proteostasis documented in the recent literature. Adding 5-6 generic modules would substantially enrich the graph toward the report's evidence base._

### environment/facultatively_aerobic  — *skeletal* (4 edges)
- **Missing modules:** terminal oxidase specificity (cytochrome bd), terminal electron acceptor branching architecture, quinone-redox sensing regulation (ArcAB), electron transport chain intermediates (NADH to menaquinone pool)
- `cytochrome_bd_oxidase —uses_as_terminal_electron_acceptor→ molecular_oxygen`  (DOI:10.1128/jb.00389-22)
- `fumarate_reductase_complex —uses_as_terminal_electron_acceptor→ fumarate`  (DOI:10.1128/jb.00389-22)
- `terminal_electron_acceptor_availability —determines→ terminal_respiratory_branch_choice`  (DOI:10.1128/jb.00389-22)
- `molecular_oxygen —inactivates→ FNR_transcription_factor`  (DOI:10.1093/nar/gkad750)
- `ArcAB_two_component_system —represses→ aerobic_respiration`  (DOI:10.1128/mbio.01448-23)
- `aerobic_respiration —requires→ cytochrome_bd_oxidase`  (DOI:10.1128/mbio.02043-23)
- _The existing graph captures FNR-type oxygen sensing but omits critical mechanistic modules: terminal oxidases (esp. cytochrome bd), alternative electron acceptor branching logic, and ArcAB redox-sensing regulation—together representing ~75% of generic facultative aerobiosis mechanism._

### environment/growth_range_phenotype_with_numerical_limits  — *skeletal* (4 edges)
- **Missing modules:** pH homeostasis / cytoplasmic pH maintenance, ion homeostasis and turgor regulation, compatible solute accumulation and transport, proton-motive-force generation and H+/ion antiporters, osmotic stress response mechanisms, cardinal temperature parameter modeling
- `external pH (environment) —requires→ pH homeostasis (process)`  (DOI:10.1093/femsre/fuad033 - neutralophiles maintain PMF acr)
- `cytoplasmic pH homeostasis (process) —enables→ growth range phenotype with numerical limits (trait)`  (DOI:10.1093/femsre/fuad033 - physicochemical homeostasis (pH)
- `ion/H+ antiporter activity (process) —supports→ growth at alkaline external pH (phenotype)`  (DOI:10.1093/femsre/fuad033 - antiporters acidify cytoplasm w)
- `compatible solute accumulation (process) —counteracts→ osmotic stress from salinity increase (environmental stress)`  (DOI:10.1093/femsre/fuad033, DOI:10.1128/aem.00145-24 - glyci)
- `proton-pumping respiratory chain / F0F1-ATPase (process) —prevents→ cytoplasmic acidification (physiological state)`  (DOI:10.1093/femsre/fuad033 - energy-coupled H+ extrusion pre)
- `hypertonic salinity environment (factor) —causes→ cell shrinkage and turgor loss (physiological state)`  (DOI:10.1093/femsre/fuad033 - osmotic imbalance reduces turgo)
- _Existing graph is a structural scaffold (abstract class hierarchy) with zero mechanistic depth; report identifies 6+ generic homeostasis/adaptation modules (pH/ion/osmotic) missing entirely from the graph, along with the causal edges linking environment→stress→mechanism→growth boundary._

### environment/microaerotolerant  — *skeletal* (5 edges)
- **Missing modules:** O₂-reducing enzyme module (Fdp/revRbr family with tension-specific ranges), sequential ROS reduction pathway (superoxide → H₂O₂ → H₂O), electron donor systems (NADH, thioredoxin, rubredoxin), redox-sensing regulatory network (PerR, OseR, σB control), oxidative damage repair systems (protein chaperones, methionine sulfoxide reductase)
- `low oxygen exposure —generates endogenous→ superoxide`  (DOI:10.1128/mbio.03753-24 (Lotoux et al. 2025): High O₂ gene)
- `superoxide reductase —reduces→ superoxide to hydrogen peroxide`  (DOI:10.1128/IAI.00502-24 (Rose et al. 2025): SOR reduces sup)
- `hydrogen peroxide —detoxified by→ rubrerythrin and peroxiredoxin`  (DOI:10.1128/mbio.03753-24 (Lotoux et al. 2025): Rbr and Bcp )
- `NADH availability —enables function of→ oxygen-reducing and detoxification systems`  (DOI:10.1128/IAI.00502-24 (Rose et al. 2025): SOR/Rbr protect)
- `oxygen tension 0.1-4% —tolerated via→ O₂-reducing enzymes (Fdp/revRbr with complementary ranges)`  (DOI:10.1128/mbio.01591-24 (Caulat et al. 2024): revRbr2 <0.4)
- `oxidative stress regulators (PerR/OseR/σB) —control induction of→ oxygen defense genes upon O₂ exposure`  (DOI:10.1128/mbio.03753-24 (Lotoux et al. 2025): PerR/OseR/σB)
- _The existing graph captures oxygen tolerance phenotype and generic ROS defense concept but misses the quantitative O₂-reducing enzyme module, sequential ROS chemistry (superoxide→H₂O₂→H₂O), electron donor coupling, regulatory networks, and damage repair—all well-supported generic mechanisms from recent literature (Caulat/Lotoux 2024–2025, Rose 2025)._

### environment/nacl_delta_mid2  — *skeletal* (2 edges)
- **Missing modules:** compatible-solute accumulation and transport, osmolality-responsive K+ regulation (kdpFABC), c-di-AMP cell-volume sensing, pH homeostasis (GABA-mediated), EPS matrix water retention
- `compatible-solute accumulation/transport —enables→ osmotic stress response`  (DOI:10.1111/mec.16316 (Rain-Franco 2022))
- `osmolality —upregulates→ kdpFABC expression`  (DOI:10.1128/mmbr.00181-23 (Foster 2024). Broadly conserved o)
- `cyclic di-AMP signaling —modulates→ cell volume regulation`  (DOI:10.1128/mmbr.00181-23 (Foster 2024). Generic master regu)
- `glutamate decarboxylase activity —produces→ GABA accumulation`  (DOI:10.1128/aem.01905-23 (Zou 2024). Generic enzymatic step )
- `GABA accumulation —improves→ pH homeostasis`  (DOI:10.1128/aem.01905-23 (Zou 2024). Mechanistic pathway sup)
- `exopolysaccharide matrix —reduces→ pericellular Na+ toxicity`  (DOI:10.1093/femsre/fuaf020 (Goszcz 2025). Review-backed gene)
- _Existing graph is bare stub; report documents at least 5 distinct GENERIC osmoadaptation modules (compatible solutes, K+ regulation, c-di-AMP sensing, pH homeostasis, EPS protection) absent from the trait, all supported by recent peer-reviewed reviews and experiments._

### environment/nacl_optimum_low  — *skeletal* (3 edges)
- **Missing modules:** c-di-AMP master regulatory switch for osmoadaptation, K+ homeostasis module (Trk/Kdp/Kup uptake systems), compatible solute biosynthesis and uptake (betaine, ectoine, proline), Na+/H+ antiporter ionic export module, osmolyte-responsive transcriptional regulation (riboswitches, KdpDE), ROS/oxidative stress defense coupling to salt response
- `minimal_osmoadaptive_load —activates→ K+ uptake via Trk system`  (DOI:10.3390/microorganisms13071474 (Nie et al., 2025)
- `minimal_osmoadaptive_load —activates→ compatible solute accumulation`  (DOI:10.1128/aem.00619-25 (Thomas et al., 2025)
- `minimal_osmoadaptive_load —activates→ c-di-AMP signaling for osmoadaptation`  (DOI:10.1128/mmbr.00181-23 (Foster et al., 2024)
- `c-di-AMP signaling —inhibits→ K+ uptake via KimA/KUP family`  (DOI:10.1038/s41467-023-38944-1 (Fuss et al., 2023)
- `high salt stress —upregulates→ glycine betaine biosynthetic genes (betA/betB)`  (DOI:10.3390/microorganisms13071474 (Nie et al., 2025)
- `osmotic stress response —activates→ oxidative stress defense (catalases, peroxidases)`  (DOI:10.1186/s12934-024-02358-5 (Yu et al., 2024)
- _The existing graph captures only the high-level osmoadaptive logic but entirely omits the intermediate molecular mechanisms (c-di-AMP regulation, K+ uptake systems, compatible solute pathways, Na+ export) that are universally documented in the research literature and essential for explaining how low ambient salt produces a low NaCl optimum._

### environment/nacl_range_high  — *skeletal* (2 edges)
- **Missing modules:** K+ accumulation and ion homeostasis, acidic proteome and Asp/Glu enrichment, protein stabilization at high ionic strength, compatible-solute biosynthesis and transport (salt-out arm)
- `high external NaCl —induces→ intracellular K+ accumulation`  (DOI:10.1038/s41559-024-02505-6)
- `intracellular K+ accumulation —drives→ proteome acidification`  (DOI:10.1038/s41559-024-02505-6)
- `acidic amino acid enrichment (Asp/Glu) —enables→ protein function at high ionic strength`  (DOI:10.1093/femsre/fuy026)
- `salt-in physiology —requires→ molar intracellular K+`  (DOI:10.1093/femsre/fuy026)
- `high external NaCl —selects for→ compatible-solute biosynthesis`  (DOI:10.1007/978-3-030-18975-4_4)
- `compatible solutes —stabilize→ proteins and enzymes under osmotic stress`  (DOI:10.1007/978-3-030-18975-4_4)
- _Existing graph captures top-level salt-in strategy but misses the molecular cascade (high NaCl → K+ → acidic proteome → protein function) and omits compatible-solute arm entirely; report identifies both as generic mechanisms spanning multiple taxa and environments._

### environment/nacl_range_low  — *skeletal* (2 edges)
- **Missing modules:** osmotic stress sensing, potassium ion uptake cascade, compatible solute accumulation pathway, mechanosensitive channel response (MscL/MscS), c-di-AMP regulatory switch, osmolyte-to-K+ balance feedback
- `increased NaCl concentration —causes→ hyperosmotic stress`  (DOI:10.1093/femsml/uqad020 (Bhowmick 2023) — foundational up)
- `hyperosmotic stress —induces→ potassium uptake`  (DOI:10.1093/femsml/uqad020 (Bhowmick 2023) — strong mechanis)
- `hyperosmotic stress —induces→ compatible solute accumulation`  (DOI:10.1093/femsml/uqad020 (Bhowmick 2023) — broad backbone )
- `c-di-AMP —inhibits→ Ktr potassium uptake systems`  (DOI:10.1128/mmbr.00181-23 (Foster 2024) — strong review synt)
- `hypoosmotic shock —opens→ mechanosensitive channels (MscL/MscS)`  (DOI:10.1093/femsml/uqad020 (Bhowmick 2023) — strong review-s)
- `high intracellular K+ —promotes→ neutral compatible-solute accumulation`  (DOI:10.1128/mmbr.00181-23 (Foster 2024) — bridge edge linkin)
- _Existing graph is a trait stub only; report describes a multi-layer osmoadaptation cascade (stress-sensing → K+ uptake + osmolyte synthesis ← c-di-AMP checkpoint) that is entirely absent and should be prioritized."_

### environment/nacl_range_mid1  — *skeletal* (2 edges)
- **Missing modules:** ectoine biosynthesis operon (ectABC), ion homeostasis (Na+/K+ uptake), compatible-solute transport (ABC/symporters), oxidative stress mitigation, osmolyte switching/modularity
- `NaCl shock —triggers→ Na+/K+ uptake`  (10.1186/s12934-024-02358-5 (Yu et al. 2024, H. elongata temp)
- `ectoine biosynthesis (ectABC) —enables→ sustained growth at 1–3% NaCl`  (10.1128/AEM.01905-23 (Zou et al. 2024: ΔectABC operon deleti)
- `compatible-solute biosynthesis —produces→ ectoine and/or glycine betaine and/or proline`  (10.1186/s12934-024-02358-5)
- `ABC-type osmoprotectant transporters (Opu/ProU families) —mediate_uptake_of→ compatible solutes`  (10.1128/AEM.00145-24 (Xing et al. 2024, N. thermophilus: ABC)
- `osmotic stress (NaCl shock) —induces→ oxidative stress response`  (10.1186/s12934-024-02358-5 (Yu et al. 2024: NaCl shock trigg)
- `ectoine and/or alternative osmolytes —substitute_for→ each other under genetic constraints`  (10.1128/AEM.01905-23)
- _The existing graph misses all five major generic mechanistic modules documented in recent 2024 multi-omics and metabolic-engineering literature; ectABC deletion directly supports the 1–3% boundary, and ion-homeostasis/osmolyte-synthesis/transport mechanisms are well-supported across model organisms._

### environment/nacl_range_mid2  — *skeletal* (2 edges)
- **Missing modules:** osmotic pressure induction, ectoine biosynthesis pathway (ectABC), ectoine accumulation / compatible solute dominance, Na+/K+ ion homeostasis, emergency amino acid pool expansion (Glu/Gln), glycine betaine biosynthesis pathway
- `NaCl 3-8% (w/v) environment —induces→ osmotic pressure`  (DOI:10.1093/femsre/fuy009)
- `osmotic pressure —triggers rapid response via→ Na+/K+ ion uptake and balance`  (DOI:10.1186/s12934-024-02358-5)
- `ectABC operon —enables biosynthesis of→ ectoine`  (DOI:10.3389/fmicb.2023.1192059)
- `ectoine accumulation —sustains growth in→ NaCl range mid2 (3-8%)`  (DOI:10.1186/s12934-024-02358-5)
- `BetA/BetB pathway —enables biosynthesis of→ glycine betaine`  (DOI:10.3389/fmicb.2023.1192059)
- `glutamate/glutamine pools —provide early osmotic buffering during→ NaCl shock response`  (DOI:10.1186/s12934-024-02358-5)
- _The trait graph captures only the phenotypic outcome; the deep-research report identifies six distinct GENERIC mechanistic modules (osmotic pressure, ion homeostasis, ectoine biosynthesis/accumulation, betaine synthesis, amino acid buffering) that together explain sustained growth in the 3–8% NaCl range, none of which are present in the current graph._

### environment/nacl_range  — *skeletal* (4 edges)
- **Missing modules:** potassium homeostasis and uptake regulation, c-di-AMP signaling hub, compatible solutes (glycine betaine, glutamate, proline) uptake/biosynthesis, intracellular ion and osmolyte accumulation, Na+/H+ antiporter-mediated sodium efflux
- `c-di-AMP —inhibits→ Trk/Ktr potassium uptake systems`  (Foster et al. 2024 MMBR (10.1128/MMBR.00181-23) review-level)
- `potassium uptake systems —promote→ intracellular K+ accumulation`  (Foster et al. 2024 MMBR and Xing et al. 2024 AEM (10.1128/AE)
- `compatible-solute accumulation —broadens→ NaCl growth range`  (Xing et al. 2024 AEM multi-omics: glycine betaine rises 52.7)
- `c-di-AMP —binds and regulates→ OpuA-like compatible-solute importers`  (Foster et al. 2024 MMBR (10.1128/MMBR.00181-23))
- `c-di-AMP elevation —causes→ narrower NaCl tolerance`  (Hu et al. 2024 Spectrum (10.1128/SPECTRUM.03786-23) primary )
- `Na+/H+ antiporter —promotes→ Na+ efflux under salt stress`  (Xing et al. 2024 AEM: NhaC antiporters present and upregulat)
- _Existing graph lacks the potassium-homeostasis and c-di-AMP regulatory nodes that the report identifies as the generic mechanistic core controlling NaCl-range boundaries._

### environment/obligately_piezophilic  — *skeletal* (2 edges)
- **Missing modules:** membrane lipid remodeling under pressure, compatible solute/piezolyte accumulation, respiratory/energy metabolism reconfiguration, cell-wall/peptidoglycan biosynthesis, chemotaxis and pressure-responsive signaling
- `high hydrostatic pressure —triggers→ membrane lipid remodeling (increased unsaturation/branching)`  (Tamby 2023 review-level synthesis across marine piezophiles)
- `high hydrostatic pressure —triggers accumulation of→ compatible solutes (glutamate, betaine, proline)`  (Scheffer 2023 (Photobacterium profundum 20–30 MPa) + Qiu 202)
- `membrane lipid remodeling —enables→ obligate piezophilic trait`  (Generic homeoviscous/homeophasic adaptation mechanism)
- `compatible solute accumulation —enables→ obligate piezophilic trait`  (Generic pressure-protective mechanism preventing protein den)
- `high hydrostatic pressure —alters→ respiratory chain components and energy metabolism`  (Generic mechanism: Scheffer 2023 documents pressure-driven s)
- `respiratory/energy metabolism reconfiguration —enables→ obligate piezophilic trait`  (Generic module supporting ATP/NADH balance under pressure)
- _Existing 2-node graph captures trait definition but lacks all major mechanistic modules; needs expansion to membrane adaptation, osmolyte response, energy metabolism, and cell-wall synthesis pathways identified as generic across piezophile lineages in recent literature._

### environment/optimum_phenotype_with_numerical_limits  — *skeletal* (4 edges)
- **Missing modules:** intracellular pH homeostasis via antiporters and ATPase, proton motive force generation and coupling, compatible-solute uptake and osmoadaptation machinery, environmental-to-physiological response pathways connecting external conditions to homeostatic mechanisms
- `external pH —activates→ intracellular pH homeostasis`  (DOI:10.1038/nrmicro2549 — Na+/H+ and K+/H+ antiporters are k)
- `Na+/H+ antiporters —contribute_to→ intracellular pH homeostasis`  (DOI:10.1093/femsre/fuad033 (2023) — Poolman identifies proto)
- `F0F1-ATP synthase —interconverts_with→ proton motive force`  (DOI:10.1093/femsre/fuad033 (2023) — F0F1-ATPase uses proton )
- `hyperosmotic stress —activates→ compatible-solute accumulation`  (DOI:10.1093/femsre/fuad033 (2023) — Hypertonicity triggers a)
- `amino-acid decarboxylation —contributes_to→ proton motive force`  (DOI:10.1093/femsre/fuad033 (2023) — Decarboxylation coupled )
- `membrane potential gradient —constrains→ optimum phenotype with numerical limits`  (DOI:10.1038/nrmicro2549 (2011) — Acidophiles/alkaliphiles ad)
- _Existing graph is a taxonomic scaffold only; research report documents robust generic mechanisms (pH homeostasis, osmoadaptation, PMF coupling) that should be added as mechanistic edges to enrich the causal graph._

### environment/oxygen_preference  — *skeletal* (5 edges)
- **Missing modules:** terminal oxidase switching (bo3/cbb3 to bd), concurrent respiration module management, redox-state sensing and global regulation (ArcAB/FNR/Rex), O2/ROS detoxification enzyme repertoire, electron carrier pool (quinone/menaquinone) regulation
- `declining oxygen availability —shifts terminal oxidase usage from→ bo3-type to bd-type cytochrome oxidase`  (DOI:10.3390/ijms25021277 — Nastasi et al. 2024 demonstrate b)
- `ArcAB two-component system —represses→ respiratory operons and aerobic respiration pathways`  (DOI:10.1128/mbio.01448-23 — Brown et al. 2023 show ArcAB is )
- `low oxygen tension —enables concurrent activity of→ fumarate reductase and cytochrome bd-mediated respiration`  (DOI:10.1128/jb.00389-22 — Butler et al. 2023 show B. fragili)
- `ArcA and FNR regulators —are required for peak expression of→ cyd operon under microaerobic conditions`  (DOI:10.1042/ebc20230012 — Mele et al. 2023 cite conserved co)
- `O2 exposure —induces expression of→ flavodiiron proteins and rubrerythrin detoxification enzymes with O2-range specialization`  (DOI:10.1128/mbio.01591-24 — Caulat et al. 2024 demonstrate m)
- `menaquinone electron carrier pool —supplies electrons to→ terminal oxidases and terminal reductases enabling respiratory flexibility`  (DOI:10.1128/jb.00389-22 — Butler et al. 2023 quantify menaqu)
- _Existing graph is a phenotypic taxonomy stub with zero mechanistic depth; the report describes five generic, well-supported modules (terminal oxidase switching, concurrent respiration, redox sensing, detoxification, electron carriers) that should form the core of an enriched causal graph."_

### environment/ph_delta_mid3  — *skeletal* (2 edges)
- **Missing modules:** proton motive force (PMF) with Δψ and ΔpH, proton-pumping respiratory complexes, Na+/H+ and K+/H+ antiporter systems, F0F1-ATPase proton extrusion, cytoplasmic phosphate buffering, amino-acid decarboxylation pathways
- `Proton-pumping respiratory complexes —contribute_to→ Proton motive force (PMF)`  (DOI:10.1038/nrmicro2549 (Krulwich et al. 2011, pages 1-3) de)
- `Proton motive force (PMF) —maintains→ Cytoplasmic pH homeostasis across broad external pH`  (DOI:10.1038/nrmicro2549 (Krulwich et al. 2011) describes PMF)
- `Na+/H+ antiporter activity —enables_proton_extrusion_under→ Alkaline pH conditions`  (DOI:10.1038/nrmicro2549 (Krulwich et al. 2011, pages 5-6) id)
- `F0F1-ATPase —extrudes_protons_to_support→ Acid stress homeostasis`  (DOI:10.1038/nrmicro2549 (Krulwich et al. 2011) and DOI:10.10)
- `Cytoplasmic phosphate buffering capacity —stabilizes→ Intracellular pH`  (DOI:10.1093/femsre/fuad033 (Poolman 2023, pages 1-2) emphasi)
- `Amino-acid decarboxylation pathways —consume_protons_and_contribute_to→ Acid stress tolerance and PMF generation`  (DOI:10.1093/femsre/fuad033 (Poolman 2023, pages 1-2) describ)
- _The existing graph captures only the trait and a generic 'wide pH-homeostasis' process but omits all six major generic mechanistic modules (PMF, respiratory chains, antiporters, ATP synthase, buffering, decarboxylation) that the report identifies as universal to mid-3 pH-delta breadth; enrichment is high priority."_

### environment/ph_delta  — *skeletal* (2 edges)
- **Missing modules:** proton motive force generation and utilization, F0F1-ATPase / oxidative phosphorylation, monovalent cation/H+ antiporter classes, membrane lipid remodeling for acid tolerance, amino-acid decarboxylase acid-resistance pathways
- `proton motive force generation —supports→ external pH homeostasis`  (10.1093/femsre/fuad033)
- `F0F1-ATPase activity —supports→ external pH homeostasis`  (10.1093/femsre/fuad033)
- `external pH homeostasis —enables→ broader external pH growth breadth`  (10.1093/femsre/fuad033)
- `monovalent cation:H+ antiporter activity —supports→ external pH homeostasis`  (10.1093/femsre/fuad033)
- `membrane lipid remodeling —decreases→ proton permeability`  (10.3389/fmicb.2022.1034164)
- `glutamate-dependent acid resistance pathway —consumes→ intracellular protons`  (10.1128/aem.00569-24)
- _Existing graph is a bare two-node skeleton (homeostasis flexibility → tolerance breadth → trait); report documents five generic mechanistic modules (PMF, ATPase, antiporters, lipid remodeling, acid-resistance pathways) entirely missing from the causal graph, with strong review-level or experimental evidence in Poolman 2023 and ecophysiology studies._

### environment/ph_optimum_mid1  — *skeletal* (3 edges)
- **Missing modules:** proton pumping via F0F1-ATPase, amino-acid decarboxylation (proton-consuming), ammonia-based pH buffering (NH3/NH4+ chemistry), cell envelope permeability control (dlt operon)
- `F0F1-ATPase —exports→ H+`  (10.1371/journal.ppat.1011927 (beetham2024) — classic pH-home)
- `amino-acid decarboxylation pathways —consume→ H+`  (10.1371/journal.ppat.1011927 (beetham2024) — good general ac)
- `NH3 —binds→ H+ forming NH4+`  (10.1128/aem.00569-24 (jiang2024) — direct acid-buffering che)
- `dlt operon-mediated D-alanylation —reduces→ cell envelope proton permeability`  (10.1371/journal.ppat.1011927 (beetham2024) — relevant bounda)
- `cytoplasmic pH homeostasis —results from→ coordinated F0F1-ATPase and decarboxylation`  (10.1007/s12602-024-10273-9 (bustos2025) + 10.1371/journal.pp)
- `minimal pH-homeostasis load —depends on→ functional proton export and consumption pathways`  (10.1038/nrmicro2549 (review cited in YAML) — neutr pH requir)
- _Existing graph captures the phenotype outcome but omits the cell-intrinsic pH-homeostasis machinery (pumps, decarboxylases, buffering chemistry, envelope modifications) that actually implement minimal homeostasis load at neutral pH._

### environment/ph_optimum_mid2  — *skeletal* (3 edges)
- **Missing modules:** Na+/H+ antiporter regulation, K+/H+ antiporter regulation, proton motive force (PMF) and membrane potential, proton-pumping respiratory chain, F0F1-ATP synthase, cytoplasmic buffering capacity, metabolite decarboxylation pathways
- `external pH ~7–8 —determines magnitude of→ ΔpH contribution to proton motive force`  (DOI:10.1093/femsre/fuad033 (Poolman 2023): 'Since cells main)
- `Na+/H+ antiporters —acidify cytoplasm to regulate→ intracellular pH homeostasis`  (DOI:10.1093/femsre/fuad033 (Poolman 2023): 'Proton-sensing i)
- `cytoplasmic buffering capacity —stabilizes→ intracellular pH against fluctuations`  (DOI:10.1093/femsre/fuad033 (Poolman 2023): 'The buffering ca)
- `proton motive force magnitude —constrains→ external pH range for pHi homeostasis`  (DOI:10.1103/PRXLife.2.043015 (Terradot et al. 2024): 'the ab)
- `NhaB-like antiporter —minimizes homeostatic cost at→ external pH 5–9 range (includes optimum 7–8)`  (DOI:10.1103/PRXLife.2.043015 (Terradot et al. 2024): 'cells )
- `proton-ion antiporters —generate and maintain→ membrane potential (Δψ) and proton motive force`  (DOI:10.1103/PRXLife.2.043015 (Terradot et al. 2024): 'proton)
- _Existing graph lacks all core mechanistic determinants: antiporter families, PMF/membrane potential framework, respiratory proton pumping, ATP synthase, buffering, and decarboxylation pathways identified in recent (2023–2024) generic literature as broadly applicable to neutrophiles and alkalitolerant growth near pH 7–8._

### environment/ph_phenotype_with_numerical_limits  — *skeletal* (4 edges)
- **Missing modules:** intracellular pH homeostasis mechanism, proton motive force (PMF) maintenance, ion antiporter regulation (Na+/H+, K+/H+), amino-acid decarboxylase-mediated proton consumption, membrane lipid composition adaptation, cell-surface charge modulation (S-layer/SCWP)
- `external pH (CHEBI:33996) —perturbs→ intracellular pH homeostasis (GO:0006885)`  (DOI:10.1093/femsre/fuad033)
- `external pH (CHEBI:33996) —modulates→ proton motive force across cell envelope (GO:0098869)`  (DOI:10.1093/femsre/fuad033)
- `F-type H+-ATPase (GO:0046933) —hydrolyzes ATP to consume→ intracellular H+ (CHEBI:15378)`  (DOI:10.3390/microorganisms12091774)
- `Na+/H+ and K+/H+ antiporter activity (GO:0015385) —regulates→ intracellular pH and PMF (label-only)`  (DOI:10.1093/femsre/fuad033)
- `amino-acid decarboxylase + antiporter systems (label-only) —consume→ intracellular H+ via coupled proton pumping (CHEBI:15378)`  (DOI:10.1093/femsre/fuad033)
- `membrane lipid composition (saturated vs unsaturated fatty acids) —modulates→ proton permeability of cytoplasmic membrane (label-only)`  (DOI:10.3389/fmicb.2022.1034164, DOI:10.1128/aem.00569-24)
- _Existing graph captures only phenotype taxonomy (optimum/range/delta), missing all six core mechanistic modules (homeostasis, PMF, antiporters, decarboxylases, lipid adaptation, surface charge) that the report identifies as generic pH-limit determinants._

### environment/ph_range_mid1  — *skeletal* (2 edges)
- **Missing modules:** proton motive force (PMF) bioenergetic control, Na+/H+ antiporter families and pH-range boundary determination, respiratory proton-pumping complexes and acid/alkali stress response, F1Fo-ATP synthase regulation in pH homeostasis, oxygen availability impact on PMF and pH maintenance
- `proton motive force —enables→ cytoplasmic pH homeostasis`  (DOI:10.1103/PRXLife.2.043015)
- `Na+/H+ antiporter activity —determines→ external pH range for pH homeostasis`  (DOI:10.1103/PRXLife.2.043015)
- `respiratory proton-pumping complexes —enables→ baseline pH homeostasis`  (DOI:10.1038/nrmicro2549)
- `F1Fo-ATP synthase —enables→ baseline pH homeostasis`  (DOI:10.1038/nrmicro2549)
- `oxygen availability —influences→ proton motive force`  (DOI:10.1103/PRXLife.2.043015)
- `acid challenge —triggers→ upregulation of respiratory proton pumping and downregulation of ATP synthase`  (DOI:10.1038/nrmicro2549)
- _The existing graph is a minimal scaffold capturing the phenotype-trait hierarchy and one enabling process; it lacks the mechanistic depth of PMF, antiporters, bioenergetic enzyme regulation, and oxygen coupling that the literature establishes as generic, broadly-applicable mechanisms for neutrophilic pH range mid1."_

### environment/ph_range_mid2  — *skeletal* (2 edges)
- **Missing modules:** cytoplasmic pH homeostasis, proton motive force maintenance, membrane potential/ΔpH rebalancing, cytoplasmic buffering, Na+/H+ antiport activity, K+/H+ antiport activity, respiratory electron transport / proton pumps
- `external pH 7-8 —permits maintenance of→ cytoplasmic pH 7.0-7.5`  (DOI:10.1093/femsre/fuad033 (Poolman 2023))
- `cytoplasmic pH homeostasis —depends on→ cytoplasmic buffering`  (DOI:10.1093/femsre/fuad033 (Poolman 2023))
- `Na+/H+ antiport activity —enables→ cytoplasmic acidification during alkaline stress`  (DOI:10.1093/femsre/fuad033 (Poolman 2023))
- `membrane potential / ΔpH rebalancing —maintains→ proton motive force across external pH 5-8`  (DOI:10.1093/femsre/fuad033 (Poolman 2023))
- `respiratory proton pumps —generate→ proton motive force`  (DOI:10.1093/femsre/fuad033 (Poolman 2023))
- `proton motive force —enables→ ATP synthesis via F0F1-ATPase`  (DOI:10.1093/femsre/fuad033 (Poolman 2023))
- _Existing graph lacks the mechanistic backbone connecting ion transport, PMF regulation, and buffering to the trait; Poolman 2023 provides high-consensus framework for generic pH 7-8 homeostasis that should anchor enrichment._

### environment/ph_range_very_low  — *skeletal* (2 edges)
- **Missing modules:** cation/K+ influx and inside-positive membrane potential, low passive proton permeability, cytoplasmic pH homeostasis as intermediate state, F1Fo-ATPase proton extrusion, weak organic acid inhibition boundary
- `Cation influx / K+ transport —causes→ Inside-positive membrane potential`  (DOI:10.1128/9781555818821.ch4.3.1)
- `Inside-positive membrane potential —reduces→ Proton influx`  (DOI:10.1038/nrmicro2549)
- `Low passive proton permeability —enables maintenance of→ Near-neutral cytoplasmic pH`  (DOI:10.3389/frbis.2023.1338019)
- `F1Fo-ATPase —exports protons increasing→ Intracellular pH`  (DOI:10.1038/nrmicro2549)
- `Near-neutral cytoplasmic pH —enables→ pH range very low growth`  (DOI:10.1038/nrmicro2549)
- `Weak organic acids —cause→ Cytoplasmic acidification`  (DOI:10.1128/AEM.04031-15)
- _Existing graph captures only high-level envelope concept; lacks decomposition into the well-supported PMF architecture (cation influx, reversed membrane potential, reduced proton influx, pH homeostasis intermediates) and F1Fo-ATPase extrusion that form the generic mechanistic backbone across acidophiles._

### environment/ph_range  — *skeletal* (4 edges)
- **Missing modules:** cytoplasmic pH homeostasis (central regulator), proton motive force / Δψ compensation, membrane proton impermeability / lipid remodeling, Mrp/NhaA antiporter-mediated H+ uptake, decarboxylase-based acid resistance (glutamate/arginine), F1F0-ATP synthase pH adaptation, buffering compound production
- `external_ph —creates→ proton_gradient_stress`  (DOI:10.1038/nrmicro2549 — PMF architecture determines whethe)
- `cytoplasmic_pH_homeostasis —enables→ bounded_growth_window`  (DOI:10.1038/nrmicro2549 — bacteria maintain distinct cytopla)
- `proton_impermeability —extends→ acid_tolerance`  (DOI:10.3389/fmicb.2020.556140 — reduced proton leak via memb)
- `mrp_antiporter_activity —mediates→ alkaline_tolerance`  (DOI:10.1038/nrmicro2549 — Na+/H+ exchange is principal strat)
- `decarboxylase_system —consumes_H+_to_support→ acid_tolerance`  (DOI:10.3389/fmicb.2017.00206 — glutamate/arginine decarboxyl)
- `ATP_synthase_adaptation —enhances→ alkaline_tolerance`  (DOI:10.1038/nrmicro2549 — F1F0-ATP synthase motif mutations )
- _The existing graph is a high-level scaffold; it lacks the well-documented generic mechanistic modules (PMF, homeostasis, antiporters, decarboxylases, ATP synthase) that the report identifies as the basis of acid and alkaline tolerance._

### environment/piezophilic  — *skeletal* (3 edges)
- **Missing modules:** osmolyte/piezolyte accumulation, ion homeostasis and pH regulation, protein folding and stress-response proteins, DNA repair and genome maintenance, porin-mediated nutrient transport, respiratory chain rewiring, lipid biosynthesis gene regulation
- `high hydrostatic pressure —increases→ unsaturated and branched-chain fatty acid abundance`  (DOI:10.3389/fmolb.2022.1058381 — broad review support for pr)
- `high hydrostatic pressure —accumulates→ piezolytes (glutamate, betaine, TMAO, β-hydroxybutyrate)`  (DOI:10.3390/microorganisms11071629 and DOI:10.3389/fmicb.202)
- `pfa operon —enables→ ω-3 polyunsaturated fatty acid production`  (DOI:10.3390/microorganisms11071629 — strong gene-to-function)
- `high hydrostatic pressure —upregulates→ protein folding / stress-response proteins (heat-shock, cold-shock)`  (DOI:10.3389/fmicb.2024.1293928 — transcriptomic evidence fro)
- `high hydrostatic pressure —upregulates→ ion homeostasis genes (nhaA, ktrA/ktrB, kefC, cusA)`  (DOI:10.3389/fmicb.2024.1293928 — Na+/H+ exchangers and K+ tr)
- `polyunsaturated fatty acids (EPA C20:5, DHA C22:6) —enables→ membrane homeoviscous adaptation`  (DOI:10.3389/fmolb.2022.1058381 — specific lipid species stre)
- _Existing graph captures only the membrane-lipid backbone; six well-documented generic mechanistic modules (osmolyte accumulation, ion homeostasis, stress-response proteins, gene regulation, PUFA-specific lipid adaptation) are missing and should be prioritized for enrichment to reflect the literature consensus._

### environment/pressure_range  — *skeletal* (2 edges)
- **Missing modules:** membrane lipid homeoviscous adaptation, oxidative stress response and antioxidant defense, compatible solute / osmolyte stabilization, cell-division machinery (FtsZ) pressure tolerance, nitrate respiration alternative electron acceptor pathway, protein/proteome stability mechanisms
- `high hydrostatic pressure —induces→ oxidative stress response`  (DOI:10.1128/aem.01304-22 — Li et al. 2023 demonstrate upregu)
- `unsaturated membrane lipids —enables→ cell membrane fluidity under pressure`  (DOI:10.3389/fmolb.2022.1058381 & DOI:10.1021/acs.chemrev.3c0)
- `cell membrane fluidity under pressure —supports→ pressure range`  (DOI:10.1021/acs.chemrev.3c00432 — Peters et al. 2023 establi)
- `TorRS two-component system —activates→ TMAO reductase (torA)`  (DOI:10.3389/fmicb.2023.1291578 — Liu et al. 2023 show TorRS )
- `compatible solutes (betaine, glutamate, TMAO) —stabilize→ protein function via preferential hydration`  (DOI:10.3389/fmolb.2022.1058381 & DOI:10.1021/acs.chemrev.3c0)
- `FtsZ N-terminal GTPase domain —maintains→ cell-division septum assembly under high pressure`  (DOI:10.3389/fmicb.2024.1441398 — Cui et al. 2024 identify cr)
- _The existing graph is a minimal stub (2 edges) capturing only the physical constraint (pressure defines bounded range) but entirely lacking the mechanistic substrate layers (lipid adaptation, redox control, osmolyte stabilization, cell-division adaptation) that the research identifies as generic, broadly-supported mechanisms underlying pressure tolerance and growth range expansion._

### environment/salinity_phenotype_with_numerical_limits  — *skeletal* (4 edges)
- **Missing modules:** osmoadaptation strategy selection (salt-in vs salt-out), compatible solute accumulation pathway, ion homeostasis module (K+ uptake and regulation), proline biosynthesis pathway, environmental modifiers (water activity, salt composition)
- `salt-in strategy —maintains→ intracellular osmotic balance across salinity`  (DOI:10.3389/frmbi.2023.1329925 — general mechanistic edge fr)
- `compatible-solute strategy —maintains→ intracellular osmotic balance across salinity`  (DOI:10.3389/frmbi.2023.1329925 — broad review-style statemen)
- `L-proline accumulation —increases→ salinity phenotype with numerical limits`  (DOI:10.1128/aem.01195-24 — strong causal perturbation)
- `proB/proA/proC proline biosynthesis pathway —produces→ L-proline`  (DOI:10.1128/aem.01195-24 — strong biochemical edge, general )
- `water activity —constrains→ salinity phenotype with numerical limits`  (DOI:10.1038/s41559-024-02505-6 — general abiotic edge for tr)
- `hybrid salt-in/salt-out strategy —is_selected_by→ extreme salinity fluctuations`  (DOI:10.3389/frmbi.2023.1329925 — strong ecological selection)
- _Existing graph captures only trait definition and numerical descriptors; report describes detailed mechanistic backbone (osmoadaptation pathways, metabolite/ion homeostasis, environmental context) entirely absent from current graph._

### environment/temperature_delta_high  — *skeletal* (2 edges)
- **Missing modules:** membrane fluidity homeostasis / homoviscous adaptation, lipid desaturation / unsaturated fatty acid biosynthesis, thermostable enzyme proteostasis, membrane physical state temperature sensing
- `decreased growth temperature —increases→ unsaturated fatty acid biosynthesis`  (Core homoviscous adaptation mechanism expanding low-temperat)
- `homoviscous adaptation —maintains→ membrane fluidity homeostasis`  (Membrane physical homeostasis proximal mechanism for sustain)
- `lipid desaturase activity —increases→ membrane fluidity`  (Desaturation creates packing defects that preserve bilayer f)
- `cis-trans isomerase activity —increases→ membrane viscosity`  (Rapid remodeling of existing UFAs counters excess fluidity d)
- `thermostable enzyme machinery —resists→ irreversible protein inactivation`  (Protein intrinsic stability extends upper growth temperature)
- `maximal thermal-adaptation flexibility —consists of→ membrane remodeling and protein thermostability`  (Synthesis of lipid remodeling and proteostasis as dual mecha)
- _Existing graph is a stub capturing only the outcome node; report documents five generic mechanistic modules (membrane sensing/remodeling, lipid desaturation, thermostable proteins, cold-shock factors, regulatory signaling) that should be integrated as a multi-pathway network downstream of maximal-thermal-adaptation._

### environment/temperature_delta_mid1  — *skeletal* (2 edges)
- **Missing modules:** temperature-induced membrane rigidification sensing, membrane fluidity homeostasis via UFA remodeling, two-component cold signaling pathway
- `low temperature —causes→ membrane rigidification`  (DOI:10.1128/spectrum.03925-23)
- `membrane rigidification —triggers→ increased unsaturated fatty acid biosynthesis`  (DOI:10.1007/s42770-023-01057-4)
- `increased unsaturated fatty acids —restores→ membrane fluidity`  (DOI:10.1128/spectrum.03925-23)
- `membrane fluidity —enables→ growth at moderate temperature range`  (DOI:10.1007/s42770-023-01057-4)
- `membrane state change —activates→ two-component cold signaling`  (DOI:10.1007/s42770-023-01057-4)
- `Tmin and Tmax —define→ temperature growth breadth`  (DOI:10.3390/pr8010121)
- _Existing graph captures only the trait-parent relationship and an abstract "moderate thermal adaptation" node, missing the entire membrane-fluidity homeostasis mechanism that literature identifies as the core generic basis for Td_10_20 breadth._

### environment/temperature_delta_mid2  — *skeletal* (2 edges)
- **Missing modules:** homeoviscous adaptation via desaturation, DesK/DesR membrane-sensing cascade, trehalose biosynthesis pathway (otsAB/RpoS), chaperone-mediated stress response, BR-body/RNP condensate formation, branched-chain fatty-acid remodeling, temperature as environmental driver node
- `decreased temperature —triggers→ broad thermal-adaptation flexibility`  (Generic cold-stress trigger supported across multiple bacter)
- `broad thermal-adaptation flexibility —upregulates→ fatty-acid desaturation`  (Rapid desaturation-mediated homeoviscous adaptation upon col)
- `decreased temperature —induces→ trehalose biosynthesis (otsAB operon)`  (RpoS-dependent cold-shock induction of otsAB is a generic ba)
- `trehalose —improves→ cold tolerance`  (Compatible solute function in cold-shock tolerance)
- `decreased temperature —upregulates→ chaperone proteins (GroEL, DnaK, Hsp family)`  (Generic cold-response upregulation of conserved chaperones d)
- `unsaturated fatty acids —maintains→ membrane fluidity`  (Desaturation-mediated membrane fluidization is the core home)
- _Existing graph captures only the high-level phenotype and broad adaptation label, missing six distinct generic mechanistic modules (sensing, signaling, lipid remodeling, compatible solutes, proteostasis, stress-condensates) that the deep-research report documents as broadly supported across multiple bacterial taxa."_

### environment/temperature_delta_very_low  — *skeletal* (2 edges)
- **Missing modules:** membrane homeoviscous adaptation (UFAs and fluidity sensing), heat-shock proteostasis (RpoH/DnaK/RpoE pathways), cold-shock translation control (CspA/CsdA), stringent-response division buffering ((p)ppGpp/RelA/SpoT), compatible solutes and osmo-ion homeostasis (c-di-AMP/K+)
- `unsaturated fatty acids —increases→ membrane fluidity`  (10.1146/annurev-micro-091313-103612)
- `RpoH (sigma-32) —induces→ heat-shock chaperone and protease program`  (10.1007/s12275-023-00031-x — 'RpoH (sigma-32) controlled by )
- `cold shock —induces→ CspA (cold-shock protein)`  (10.1007/s12275-023-00031-x — 'Cold-shock proteins (notably C)
- `RelA/SpoT enzymes —synthesize→ (p)ppGpp stringent-response alarmone`  (10.1111/mmi.15323 — 'the (p)ppGpp stringent-response system )
- `(p)ppGpp —buffers→ cell division under reduced membrane fluidity`  (10.1111/mmi.15323 — '(p)ppGpp-dependent adaptive response re)
- `compatible solutes (glycine betaine, proline) —protect→ cells from thermal stress`  (10.3390/biology13121088 — 'Compatible solutes (glycine–betai)
- _Existing graph captures only the highest-level trait-mechanism relationship (limited thermal adaptation → stenothermal breadth) but omits all five major generic mechanistic modules the report documents: membrane homeoviscous adaptation, heat-shock proteostasis, cold-shock translation control, (p)ppGpp stringent response, and compatible solutes. All six suggested edges are explicitly flagged as HIGH confidence or broad-spectrum in the report and are not marked taxon-specific/assay-specific/uncertain per the audit rules."_

### environment/temperature_optimum_high  — *skeletal* (3 edges)
- **Missing modules:** DNA topology (reverse gyrase, positive supercoiling), genome organization (nucleoid-associated proteins, histones, SMC), proteostasis (chaperones, chaperonins, proteases), membrane lipid remodeling, intrinsic protein thermostability (hydrophobic/charged amino acid enrichment)
- `reverse gyrase —positively regulates→ positive DNA supercoiling`  (DOI:10.1264/jsme2.me23087 (Takemata 2024): reverse gyrase in)
- `nucleoid-associated proteins —increase→ genome thermostability`  (DOI:10.1264/jsme2.me23087 (Takemata 2024): NAPs enhance DNA )
- `small heat shock proteins —prevent→ heat-induced protein aggregation`  (DOI:10.1128/mbio.03593-22 (Baes et al. 2023): sHSPs bind den)
- `prefoldin —shuttles substrates to→ thermosome`  (DOI:10.1128/mbio.03593-22 (Baes et al. 2023): prefoldin targ)
- `altered membrane lipid composition —stabilizes→ cytoplasmic membrane at high temperature`  (DOI:10.1128/mbio.03593-22 (Baes et al. 2023): heat shock ind)
- `thermophile protein thermostability —reflects→ enrichment in hydrophobic and charged amino acids`  (DOI:10.1128/mbio.02174-23 (Grünberger et al. 2023): thermoph)
- _Existing graph treats thermophile thermostability as atomic; report decomposes it into four major generic mechanistic modules (DNA topology, genome organization, proteostasis, membrane remodeling) with substantial 2023–2024 evidence; minimal overlap risks silent underrepresentation of causal mechanisms driving the phenotype."_

### environment/temperature_optimum_mid1  — *skeletal* (3 edges)
- **Missing modules:** membrane physical state sensing, homeoviscous adaptation process, fatty acid remodeling module, protein folding stress-response module
- `lower-mesophilic environment —causes→ membrane thickening / rigidification`  (DOI:10.1007/s42770-023-01057-4 (Ramón et al. 2023): 'At low )
- `membrane physical state —is sensed as input to→ homeoviscous adaptation`  (DOI:10.1039/d4cc03114h (Maiti et al. 2024): 'HVA was first o)
- `homeoviscous adaptation —remodels toward increased→ low-melting lipids (MUFAs, PUFAs, branched FAs)`  (DOI:10.1039/d4cc03114h (Maiti et al. 2024): 'Adaptive change)
- `unsaturated fatty acids —increases→ membrane fluidity`  (DOI:10.1007/s42770-023-01057-4 (Ramón et al. 2023): 'The Des)
- `elevated temperature stress —induces upregulation of→ chaperones`  (DOI:10.1101/2024.07.23.604647 (Karmann et al. 2024): 'The mo)
- `chaperone upregulation —promotes→ correct protein folding / protein conformational stability`  (DOI:10.1101/2024.07.23.604647 (Karmann et al. 2024): 'stabil)
- _The existing 3-edge graph captures only environment→process→phenotype abstraction; it omits the mechanistic internals (membrane-state sensing, HVA remodeling, lipid composition, protein folding) that the report identifies as generic, broadly-applicable foundation for the 22–27 °C mesophilic optimum."_

### environment/temperature_optimum_very_low  — *skeletal* (3 edges)
- **Missing modules:** membrane fluidity maintenance (homeoviscous adaptation), cold-shock proteins and RNA chaperones, molecular chaperones (GroEL/DnaK/GroES), protein quality control (Clp proteases), compatible solutes (trehalose, glycine betaine), exopolysaccharides (EPS) for cryoprotection, ice-binding proteins (AFPs), antioxidant enzyme systems (SOD, catalase)
- `low_temperature —decreases_fluidity_of→ cell_membrane`  (DOI:10.3389/fmicb.2023.1215837)
- `fatty_acid_desaturases —increase_abundance_of→ unsaturated_fatty_acids`  (DOI:10.17159/sajs.2018/20170254)
- `unsaturated_fatty_acids —maintain→ membrane_fluidity_at_low_temperature`  (DOI:10.1128/AEM.01928-22)
- `cold_shock_proteins —support→ translation_at_low_temperature`  (DOI:10.17159/sajs.2018/20170254)
- `molecular_chaperones —restore→ transcription_and_translation_under_cold`  (DOI:10.3389/fmicb.2023.1215837)
- `antifreeze_proteins —inhibit→ ice_recrystallization`  (DOI:10.37256/amtt.5220244537)
- _The existing 3-edge graph is a high-level stub capturing only environment-to-machinery-to-trait; it omits 8+ well-supported generic mechanistic modules and detailed causal chains documented in the report, warranting substantial expansion to achieve adequate coverage._

### environment/temperature_range_low  — *skeletal* (2 edges)
- **Missing modules:** membrane fluidity homeostasis (lipid desaturation/branching), RNA/translation cold-shock response (CSPs, helicases, RbfA), protein folding/proteostasis (chaperone system), cryoprotection/compatible solutes (glycine betaine, trehalose, glycerol), extracellular polymeric substance biosynthesis
- `low temperature —decreases→ membrane fluidity`  (10.37256/amtt.5220244537)
- `fatty acid desaturase —increases→ unsaturated fatty acid proportion`  (10.37256/amtt.5220244537)
- `unsaturated fatty acids —increases→ membrane fluidity`  (10.1128/aem.01928-22 (yang2023insightintothe pages 1-2, page)
- `cold-shock proteins (CspA/CspC) —enables→ translation at low temperature`  (10.1186/s12864-023-09638-1)
- `compatible solutes (glycine betaine, trehalose, glycerol) —provides→ cryoprotection`  (10.3389/fmicb.2023.1197797)
- `extracellular polymeric substances —provides→ cryoprotection`  (10.37256/amtt.5220244537)
- _Existing graph is a bare stub capturing only psychrotolerant adaptation as an opaque process; report describes four distinct generic mechanistic modules (membrane homeostasis, RNA/translation, proteostasis, cryoprotection) with strong evidence for specific edges that should replace or expand the current single enabling relationship._

### environment/temperature_range_mid2  — *skeletal* (2 edges)
- **Missing modules:** membrane fluidity homeostasis, fatty acid desaturation pathway, DNA supercoiling thermosensing, RNA thermometer translational control, proteostasis (chaperone/heat-shock response)
- `temperature change —alters→ DNA supercoiling`  (DOI:10.1007/s12275-023-00031-x)
- `homeoviscous adaptation —maintains→ membrane lipid viscosity`  (DOI:10.1007/s42770-023-01057-4)
- `increased unsaturated fatty acid fraction —increases→ membrane fluidity`  (DOI:10.1007/s12275-023-00031-x)
- `temperature shift —induces→ heat-shock proteins and chaperones`  (DOI:10.1007/s12275-023-00031-x)
- `heat-shock proteins and chaperones —counteract→ protein denaturation and aggregation`  (DOI:10.1007/s12275-023-00031-x)
- `elevated temperature —opens→ RNA thermometer 5' UTR structure`  (DOI:10.1007/s12551-025-01290-1)
- _The existing graph captures only a vague top-level edge (baseline mesophile adaptation → trait); the research report identifies at least 5 core generic mechanistic modules (membrane homeostasis, lipid desaturation, DNA/RNA thermosensing, proteostasis) that are absent and critical to understanding mesophilic temperature tolerance at 27–30 °C._

### environment/temperature_range_very_low  — *skeletal* (2 edges)
- **Missing modules:** membrane homeoviscous adaptation, cold-shock RNA chaperone system, protein folding and proteostasis (DnaK/GroEL/Clp), compatible solutes (osmolyte accumulation), antifreeze and ice-binding proteins, oxidative stress detoxification (SOD/peroxidases), DNA repair and SOS response, cold-induced metabolic rewiring (glycolysis/beta-oxidation upregulation), ABC transporter upregulation, two-component cold sensing (generic pathway level)
- `membrane_fluidity —maintained_by→ fatty_acid_desaturation`  (DOI:10.1007/s42770-023-01057-4)
- `cold_shock_proteins —enables→ translation_at_low_temperature`  (DOI:10.1007/s42770-023-01057-4)
- `DnaK_GroEL_proteostasis_system —preserves→ protein_folding_in_cold`  (DOI:10.37256/amtt.5220244537)
- `compatible_solutes —stabilizes→ proteins_and_membranes`  (DOI:10.3389/fmicb.2023.1197797)
- `antifreeze_proteins —inhibits→ ice_crystal_growth`  (DOI:10.3389/fmicb.2023.1197797)
- `oxidative_stress_response_system —detoxifies→ cold_induced_ROS`  (DOI:10.3389/fmicb.2024.1465627)
- _Existing graph captures only the trait phenotype and vague "machinery" abstraction; report documents ~10 generic mechanistic modules (membrane adaptation, RNA chaperones, proteostasis, osmolytes, ice-binding, oxidative stress, DNA repair, metabolic rewiring) entirely absent from current graph._

### environment/xerophilic  — *skeletal* (2 edges)
- **Missing modules:** compatible solute accumulation and biosynthesis, glycerol biosynthesis pathway and glycerol-3-phosphate dehydrogenase, HOG osmotic stress signaling (HogA MAPK), membrane fluidity and composition remodeling, cell wall strengthening (chitin and alpha-glucan remodeling), osmolyte secretion (extracellular compatible solutes), environmental modifiers (relative humidity, time-of-wetness)
- `xerophilic trait —increases→ compatible solute accumulation`  (DOI:10.34293/sijash.v7i3.473)
- `compatible solute accumulation —enables→ osmotic adjustment`  (DOI:10.1007/978-3-031-81904-9_3)
- `low water activity —activates→ HOG osmotic stress signaling pathway`  (DOI:10.3390/jof10040290)
- `HOG pathway —increases→ glycerol biosynthesis`  (DOI:10.1007/s00253-024-13338-5)
- `glycerol —enables→ osmotic adjustment`  (DOI:10.1007/978-3-031-81904-9_3)
- `low water activity —increases→ plasma membrane fluidity adjustment`  (DOI:10.3390/jof10040290)
- _Existing graph captures definition-level trait-environment link and generic osmotic adaptation but misses at least 7 major mechanistic modules (compatible solutes, glycerol biosynthesis, HOG signaling, membrane/cell wall remodeling, environmental modifiers) well-supported in 2024 fungal reviews._

### genomics/codon_usage_bias  — *skeletal* (2 edges)
- **Missing modules:** mutational bias and GC-content evolution, natural selection for translational efficiency, growth-condition-dependent selection, tRNA pool and abundance, tRNA anticodon-loop modifications, mRNA secondary structure effects on initiation, stress-responsive tRNA reprogramming
- `mutational bias —shapes→ codon usage bias`  (DOI:10.1038/nrg2899)
- `natural selection for translational efficiency —shapes→ codon usage bias`  (DOI:10.1146/annurev.genet.42.110807.091442)
- `gene expression level —strengthens selection for→ codon usage bias`  (DOI:10.1146/annurev.genet.42.110807.091442)
- `tRNA pool —influences→ codon adaptation`  (DOI:10.1038/nrg2899)
- `tRNA anticodon-loop modifications —alter→ codon-anticodon decoding efficiency`  (DOI:10.1021/acs.accounts.3c00572)
- `strong 5' mRNA secondary structure —inhibits→ translation initiation`  (DOI:10.1038/nrg2899)
- _Existing graph captures only expression-output phenotypes and misses upstream drivers (mutational/selective), mechanistic mediators (tRNA systems, mRNA structure), and stress-response integration that the report flags as generic, well-supported mechanism across taxa._

### genomics/gc_high  — *skeletal* (2 edges)
- **Missing modules:** DNA repair loss (BER/UDG/Nei/MutT pathways), Cytosine deamination and oxidative lesion accumulation, Hypermutator phenotype, Genome reduction and deletional bias, Host-associated reductive evolution context
- `Loss of base-excision repair pathway —causally_promotes→ hypermutator state`  (DOI:10.1038/s41467-026-71228-y — Moncadas et al. (2026) demo)
- `Hypermutator state —causally_promotes→ AT-biased mutation spectrum`  (DOI:10.1038/s41467-026-71228-y — Laboratory analogues of rep)
- `Cytosine deamination —contributes_to→ AT-biased substitutions`  (DOI:10.1038/s41467-026-71228-y — Spontaneous deamination pro)
- `Genome reduction —precedes_and_promotes→ GC_<=42.65 phenotype`  (DOI:10.1038/s41467-026-71228-y — Genome reduction precedes G)
- `Host-associated obligate endosymbiosis —associated_with→ genetic drift and fixation of deleterious mutations`  (DOI:10.1264/jsme2.me24041 — Yasuda et al. (2024) show host-r)
- `Loss of uracil-DNA glycosylase —causally_promotes→ GC_<=42.65 phenotype`  (DOI:10.1038/s41467-026-71228-y — Absence of UDG family glyco)
- _The existing graph captures mutation pressure as final cause but omits the mechanistic chain (repair loss → lesions → hypermutation → GC erosion) and ecological context (host-associated drift) supported generically across 2024-2026 literature; enrichment with repair-pathway nodes and hypermutator intermediates is high priority._

### genomics/genomic_island  — *skeletal* (2 edges)
- **Missing modules:** integration machinery (integrase/recombinase/transposase modules), conjugation and type IV secretion system (for self-transmissible ICEs), integrative mobilizable element helper-element dependency, regulatory mobilization trigger (SOS response pathway), defense and fitness cargo phenotypes
- `genomic island —carries→ integrase/recombinase/transposase mobility module`  (DOI:10.1093/nar/gkad644 (Bioteau et al. 2023) — 'Intracellul)
- `integrative conjugative element —requires→ type IV secretion system`  (DOI:10.1093/nar/gkad644 (Bioteau et al. 2023) — 'ICEs dissem)
- `integrative mobilizable element —requires helper→ conjugative plasmid or helper ICE`  (DOI:10.1093/nar/gkad644 (Bioteau et al. 2023) — 'IMEs… sprea)
- `conjugative plasmid entry —triggers→ SOS response`  (DOI:10.1128/spectrum.02201-22 (Pons et al. 2023) — 'conjugat)
- `SOS response activation —promotes→ genomic island mobilization and excision`  (DOI:10.1128/spectrum.02201-22 (Pons et al. 2023) — 'SOS resp)
- `genomic island —encodes→ defense systems (restriction-modification and anti-phage)`  (DOI:10.1093/nar/gkad282 (Botelho 2023) + DOI:10.1128/jb.0014)
- _Existing graph captures only the broadest HGT-acquisition and accessory-function payload edges; it misses five key generic mechanistic modules: integration machinery, conjugation/T4SS transfer, IME helper-dependency, SOS-regulated mobilization, and encoded defense cargo that are all well-supported across 2023-2024 literature and not taxon-specific._

### genomics/mobile_genetic_element  — *skeletal* (2 edges)
- **Missing modules:** conjugative transfer machinery (relaxase-oriT-T4SS), ICE excision and circularization, integron cassette capture mechanism, transposition (IS/transposon mobility), phage-mediated transduction, AMR and defense cargo enrichment and selective pressure
- `integrase AND excisionase —enable→ ICE excision and circularization`  (10.1128/AEM.01360-24)
- `relaxase —enables→ oriT nicking and rolling-circle transfer`  (10.1128/AEM.01360-24)
- `VirB4/VirD4-containing T4SS —enables→ cell-to-cell conjugative DNA transfer`  (10.1093/nar/gkad024)
- `IntI1 integron integrase —enables→ site-specific cassette insertion at attI/attC`  (10.1111/1751-7915.14408)
- `phage infection or predation —triggers→ ICE excision and conjugative transfer`  (10.1093/nar/gkad282)
- `transposon or insertion sequence —enables→ intracellular DNA transposition`  (10.1146/annurev-micro-032521-022006)
- _Existing graph captures only top-level HGT outcome; missing 6 major generic mechanistic modules that describe intermediate machinery, phage transduction, integron operation, transposition, and environmental drivers well-documented in recent literature._

### genomics/pangenome_openness  — *skeletal* (2 edges)
- **Missing modules:** gene gain/loss dynamics, mobile genetic element vectors (plasmid, prophage, ICE/IME, transposon), integrase/transfer machinery abundance, genome stability proxies (recombinase, DNA repair, endonuclease gene counts), core/rare gene fraction proxies
- `gene gain and loss dynamics —shapes→ pangenome openness`  (DOI:10.1099/mgen.0.001021 (Tonkinhill 2023: 'HGT and the res)
- `plasmid —enables→ horizontal gene transfer`  (DOI:10.1099/mgen.0.001021 (Tonkinhill 2023: plasmids listed )
- `integrase abundance —positively_associated_with→ pangenome openness`  (DOI:10.3390/microorganisms12050986 (Wang 2024: integrase Spe)
- `DNA repair system gene count —positively_associated_with→ pangenome openness`  (DOI:10.3390/microorganisms12050986 (Wang 2024: repair system)
- `core gene fraction —negatively_associated_with→ pangenome openness`  (DOI:10.3390/microorganisms12050986 (Wang 2024: strong invers)
- `rare gene fraction —positively_associated_with→ pangenome openness`  (DOI:10.3390/microorganisms12050986 (Wang 2024: positive corr)
- _Existing graph captures primary HGT mechanism but omits 5 generic mechanistic modules (gene dynamics, mobile vectors, machinery abundance, stability proxies, gene-fraction correlates) documented as strong/moderate and non-taxon-specific in the 2023–2024 literature._

### genomics/plasmid_carriage  — *skeletal* (2 edges)
- **Missing modules:** plasmid partition/segregation system, toxin-antitoxin addiction, fitness cost, compensatory evolution, restriction-modification barriers and countermeasures
- `plasmid partition/segregation system —enables→ faithful plasmid segregation`  (10.1093/nar/gkae018)
- `plasmid carriage —imposes→ fitness cost`  (10.1080/22221751.2024.2352432)
- `toxin-antitoxin system —stabilizes→ plasmid vertical inheritance`  (10.1093/nar/gkae018)
- `compensatory mutations —reduce→ plasmid fitness cost`  (10.1002/ece3.70121)
- `restriction-modification systems —reduce→ conjugative plasmid transfer`  (10.1093/nar/gkae896)
- `antibiotic selective pressure —promotes retention of→ plasmid carriage`  (10.1080/22221751.2024.2352432)
- _Existing graph captures conjugation and accessory function but omits core GENERIC maintenance mechanisms (partition, addiction, fitness costs, compensatory evolution, RM barriers) documented in 2023-2024 literature._

### genomics/prophage  — *skeletal* (2 edges)
- **Missing modules:** master repressor (CI) and lytic gene repression, DNA damage sensing and SOS response coupling, RecA-mediated CI repressor inactivation, prophage induction to lytic cycle transition
- `CI master repressor —represses→ lytic gene expression`  (DOI:10.1038/s41586-023-06376-y — 'maintained by a phage-enco)
- `DNA damage / replication stress —activates→ RecA-LexA SOS response`  (DOI:10.1073/pnas.2407832121 + DOI:10.1128/aem.01716-22 — AZT)
- `RecA nucleoprotein filament —promotes autocleavage of→ CI master repressor`  (DOI:10.1038/s41586-023-06376-y — 'RecA activation leads to a)
- `prophage induction —enables→ viral release and virion production`  (DOI:10.1038/s41586-023-06376-y + DOI:10.1038/ismej.2017.16 —)
- `temperate phage genome —requires maintenance by→ CI repressor-mediated gene silencing`  (DOI:10.1038/s41586-023-06376-y — structural requirement for )
- `prophage carriage —can trigger→ lysogenic conversion of host phenotype`  (DOI:10.1038/ismej.2017.16 — Howard-Varona review — generic m)
- _Existing graph is a trait-label stub with no mechanistic detail; missing canonical CI repressor maintenance logic and SOS-RecA induction cascade that are well-supported as generic across 2023-2024 literature and should anchor a complete graph._

### metabolism/anaerobic_oxidation_of_methane  — *skeletal* (2 edges)
- **Missing modules:** reverse methanogenesis core pathway, MCR/mcrABCD methane activation step, DIET-mediated syntrophy (ANME-SRB electron bridge), denitrifying AOM pathways (nitrate/nitrite/NO dismutation), metal-dependent AOM with multiheme cytochromes, electrode-coupled AOM with OmcZ nanowires
- `anaerobic oxidation of methane —has_core_pathway→ reverse methanogenesis`  (DOI:10.3390/fermentation9070645)
- `methyl-coenzyme M reductase (MCR) —catalyzes_first_step_of→ anaerobic oxidation of methane`  (DOI:10.1021/acs.est.3c07197)
- `ANME archaea —forms_obligate_syntrophy_with→ sulfate-reducing bacteria`  (DOI:10.1371/journal.pbio.3002292)
- `direct interspecies electron transfer complexes —mediate_electron_flow_from→ ANME to SRB outer membrane`  (DOI:10.1371/journal.pbio.3002292)
- `nitrate —serves_as_terminal_electron_acceptor_for→ methane oxidation by Methanoperedens`  (DOI:10.1021/acs.est.3c07197)
- `multiheme c-type cytochromes —mediate_electron_transfer_to→ Fe(III) and Mn(IV) oxides in metal-dependent AOM`  (DOI:10.5194/egusphere-2024-1829)
- _Existing graph captures only terminal chemistry (methane + sulfate); misses generic mechanistic modules (reverse methanogenesis, MCR, DIET syntrophy, alternative acceptors) that are well-supported across all AOM modes and should form the core graph scaffold."_

### metabolism/biopolymer_degradation  — *skeletal* (2 edges)
- **Missing modules:** multi-enzyme cellulose degradation cascade, crystalline cellulose accessibility via LPMO, hemicellulose backbone and side-chain cleavage, hemicellulose-lignin cross-link breaking, outer membrane oligosaccharide capture and import, periplasmic depolymerization and transport, chitin degradation pathway, lignin oxidative attack, intracellular sugar metabolism
- `Endoglucanase / Exoglucanase / β-Glucosidase —form_degradation_cascade_for→ cellulose saccharification`  (10.1101/2024.11.06.622210)
- `AA10 LPMO —oxidatively_cleaves→ crystalline cellulose`  (10.1128/aem.01742-24)
- `Xylanase / Debranching enzymes / CE1 esterase —degrade→ hemicellulose backbone and decorations`  (10.1128/aem.01742-24)
- `CE15 glucuronoyl esterase —cleaves→ hemicellulose-lignin ester bonds`  (10.1128/aem.01742-24)
- `SusC/D transporter complex —imports→ oligosaccharides from degraded biopolymers`  (10.1128/msphere.00278-24)
- `Endo-chitinase / Exochitinase / AA10 LPMO —catalyze→ chitin depolymerization to assimilable units`  (10.1128/spectrum.00886-24)
- _Existing graph captures only entry-level mechanism; report documents rich polymer-specific pathways (cellulose, hemicellulose, chitin, lignin), transport systems, and periplasmic processing absent from current curation._

### metabolism/calvin_benson_bassham_cycle  — *skeletal* (3 edges)
- **Missing modules:** carboxysome assembly and RuBisCO sequestration, DIC transporter system (HCO3- import and regulation), CO2 conversion machinery (carbonic anhydrase, NDH complexes), RuBP regeneration (PRK pathway), CP12 regulatory protein and CBB inhibition, transcriptional regulation by CbbR, RbcR, CcmR, CmpR, metabolite sensing (RuBP, 2-phosphoglycolate)
- `carboxysome —contains→ RuBisCO`  (DOI:10.1111/ppl.14140)
- `carboxysomal carbonic anhydrase (CsoSCA/ιCA) —converts→ HCO3− to CO2`  (DOI:10.1111/ppl.14140)
- `RuBP (ribulose-1,5-bisphosphate) —regenerated by→ phosphoribulokinase (PRK)`  (DOI:10.3389/fpls.2024.1417680)
- `CP12 protein —inhibits→ phosphoribulokinase (PRK)`  (DOI:10.3389/fpls.2024.1417680)
- `CbbR transcriptional regulator —activates expression of→ cbb operon`  (DOI:10.1128/JB.00442-15)
- `RuBP —activates→ CsoSCA (α-carboxysome carbonic anhydrase)`  (DOI:10.1126/sciadv.adk7283)
- _The existing graph captures only the top-level enzyme-pathway-trait relation; it misses 7 generic mechanistic modules including carboxysome architecture, CCM/DIC import, CO2 conversion, transcriptional control, and metabolite-based regulatory feedback—all documented in 2023–2024 peer-reviewed sources."_

### metabolism/carbon_fixation  — *skeletal* (2 edges)
- **Missing modules:** DIC transport and speciation control, carbonic anhydrase and carboxysome-based CCM, non-CBB carbon fixation pathways (rTCA, Wood-Ljungdahl, 3HP bicycle, etc.), enzyme substrate specificity (CO2 vs HCO3-), ATP and NADPH/ferredoxin cofactor supply, metabolic pathway module structure
- `carbonic anhydrase —accelerates interconversion of→ CO2 and bicarbonate`  (DOI:10.1128/aem.01557-23 (Scott 2024, section 2.2))
- `bicarbonate transporters (SbtA, BicA, CmpABCD) —increase intracellular availability of→ bicarbonate`  (DOI:10.1128/aem.01557-23 (Scott 2024, section 2.2))
- `carboxysome compartment —localizes Rubisco and carboxysomal CA for→ CBB pathway`  (DOI:10.1128/aem.01557-23 (Scott 2024, section 2.2))
- `Wood-Ljungdahl pathway —fixes CO2 to produce→ acetyl-CoA`  (DOI:10.3390/bioengineering10121357 (Kurt 2023, section 4.1))
- `reverse TCA cycle —requires cofactors→ ATP and reduced ferredoxin`  (DOI:10.4014/jmb.2306.06005 (Kang 2023, section 3.4))
- `pH environment —governs speciation of→ dissolved inorganic carbon (CO2 vs HCO3- availability)`  (DOI:10.1128/aem.01557-23 (Scott 2024, section 2.1))
- _Existing graph captures only trait-level entry point; report describes six recognized natural pathways, DIC toolkit (transport/CA/carboxysome), cofactor requirements, and enzyme substrate specificity—none curated yet. Immediate gaps: multi-pathway architecture, CCM components, cofactor nodes, environmental pH constraint."_

### metabolism/cellulolysis  — *skeletal* (2 edges)
- **Missing modules:** cellulose substrate node, cellobiose/cellodextrin intermediates, cellulosome multienzyme architecture (scaffoldin-cohesin-dockerin assembly), LPMO oxidative pathway, carbon catabolite repression regulatory control, transport/uptake modules (PTS/ABC transporters), synergistic action of enzyme classes
- `cellulose —is substrate for→ cellulolysis`  (DOI:10.1093/jambio/lxac002)
- `cellulose —is degraded by concerted action of→ endoglucanase`  (DOI:10.1093/jambio/lxac002)
- `cellulose —is degraded by concerted action of→ cellobiohydrolase`  (DOI:10.1093/jambio/lxac002)
- `cellulosome —has non-catalytic backbone→ scaffoldin`  (DOI:10.1093/jambio/lxac002)
- `LPMO —oxidatively cleaves→ cellulose`  (DOI:10.1007/s00253-024-13240-0)
- `carbon catabolite repression —represses transcription of→ cellulolytic genes`  (DOI:10.1093/jambio/lxac002)
- _The existing graph captures only the terminal step (cellulase → glucose); it lacks the substrate, intermediate metabolites, cellulosome assembly architecture, oxidative pathway, and regulatory controls that literature establishes as generic mechanisms in cellulolysis across diverse microbial taxa._

### metabolism/chitinolysis  — *skeletal* (2 edges)
- **Missing modules:** exo-chitinase product module (diacetylchitobiose), monomer-production by N-acetylglucosaminidase, LPMO oxidative auxiliary pathway, product-based regulation of chitinase expression
- `exochitinase / chitobiosidase —hydrolyzes_to→ diacetylchitobiose ((GlcNAc)2)`  (DOI:10.3389/fmicb.2013.00149)
- `β-N-acetylhexosaminidase —hydrolyzes_to→ N-acetyl-D-glucosamine (GlcNAc)`  (DOI:10.3390/toxins16010026)
- `chitooligosaccharides —induces_expression_of→ chitinase genes`  (DOI:10.3389/fmicb.2013.00149)
- `lytic polysaccharide monooxygenase (LPMO) —oxidatively_cleaves→ chitin`  (DOI:10.15407/microbiolj86.04.053)
- `chitinase (GH18/GH19) —produces→ chitooligosaccharides`  (DOI:10.3389/fmicb.2013.00149)
- `diacetylchitobiose —acts_as_substrate_for→ cytoplasmic GlcNAc catabolism`  (DOI:10.3389/fmicb.2013.00149)
- _The existing chitinolysis graph captures only the entry point (chitinase) and terminal product (GlcNAc) but omits intermediate hydrolytic steps, enzyme-type specialization, oxidative auxiliary pathway, and generic product-based regulation—all well-supported by non-taxon-specific evidence."_

### metabolism/denitrification  — *skeletal* (2 edges)
- **Missing modules:** nitrate-to-nitrite reduction enzymatic step (Nar/Nap), nitrite-to-NO reduction enzymatic step (NirK/NirS), NO-to-N2O reduction enzymatic step (Nor cNor/qNor), O2 repression of denitrification activity, pathway modularity causing transient intermediate accumulation
- `respiratory nitrate reductase NarGHI —enables→ nitrate reduction to nitrite`  (DOI:10.3389/fmicb.2023.1218207 (Xiang 2023))
- `copper nitrite reductase NirK —enables→ nitrite reduction to nitric oxide`  (DOI:10.1093/ismeco/ycae020 (Pold 2024))
- `nitric oxide reductase Nor —enables→ nitric oxide reduction to nitrous oxide`  (DOI:10.3389/fmicb.2023.1218207 (Xiang 2023))
- `nitrous oxide reductase NosZ —enables→ nitrous oxide reduction to dinitrogen`  (DOI:10.3389/fmicb.2023.1218207 (Xiang 2023))
- `molecular oxygen (O2) —negatively_regulates→ denitrification`  (DOI:10.1038/s41467-024-51688-w (Sennett 2024))
- `denitrification pathway modularity —causes→ transient accumulation of denitrification intermediates`  (DOI:10.1038/s41467-024-51688-w (Sennett 2024))
- _Existing graph captures only the gross stoichiometry (NO3→N2) and trait classification, but omits all five enzymatic reaction steps, oxygen regulation, and the mechanistic link between modularity and intermediate accumulation—the core generic mechanistic scaffolding well-supported in recent literature."_

### metabolism/dissimilatory_metal_reduction  — *skeletal* (2 edges)
- **Missing modules:** extracellular electron transfer (EET) machinery, periplasmic-to-outer-membrane cytochrome relay, outer-membrane porin-cytochrome conduit complexes, nanowire-mediated long-range electron conduction, redox shuttle (flavin) production and secretion
- `extracellular_electron_transfer —enables→ dissimilatory_metal_reduction`  (Portela et al. 2024 DOI:10.1038/s41467-024-46192-0)
- `nanowire_structures —enable→ long_range_electron_conduction_to_metal_oxides`  (Portela et al. 2024 DOI:10.1038/s41467-024-46192-0 lines 292)
- `periplasmic_cytochromes —transfer_electrons_to→ outer_membrane_electron_conduits`  (Portela et al. 2024 DOI:10.1038/s41467-024-46192-0 lines 284)
- `mediated_electron_transfer_via_flavins —facilitates→ reduction_of_distant_metal_substrates`  (Soares et al. 2025 DOI:10.3390/fermentation11070381 lines 28)
- `direct_electron_transfer —alternative_to→ mediated_electron_transfer`  (Hou et al. 2025 DOI:10.1128/spectrum.01226-24)
- `outer_membrane_conduit_complexes —create_pathway_for→ electron_transfer_to_extracellular_acceptor`  (Hsu et al. 2024 DOI:10.1128/aem.00044-24 line 283: MtrCAB cr)
- _The existing graph captures only top-level respiratory coupling (metal acceptor enables trait) but completely omits the mechanistic substrate: extracellular electron transfer machinery (EET) and its modular architecture (periplasmic relays, outer-membrane conduits, nanowires, shuttles)—the defining innovation of dissimilatory metal reduction versus other anaerobic respiration."_

### metabolism/dissimilatory_sulfate_reduction  — *skeletal* (2 edges)
- **Missing modules:** sulfate transport entry step, sulfate activation via Sat, APS reduction via AprAB with QmoABC electron input, sulfite reduction via DsrAB-DsrC complex, terminal DsrC-trisulfide reduction via DsrMKJOP, energy conservation coupling
- `sulfate —is activated by→ Sat (sulfate adenylyltransferase)`  (DOI:10.3390/antiox12030767)
- `Sat —produces→ APS (adenosine-5-phosphosulfate)`  (DOI:10.3390/antiox12030767)
- `AprAB —reduces→ APS to sulfite`  (DOI:10.1038/s41396-023-01477-y)
- `QmoABC —transfers electrons to→ AprAB`  (DOI:10.1038/s41396-023-01477-y)
- `DsrAB and DsrC —produces→ DsrC-trisulfide from sulfite`  (DOI:10.1038/s41396-023-01477-y)
- `DsrMKJOP —reduces→ DsrC-trisulfide to sulfide`  (DOI:10.1038/s41396-023-01477-y)
- _The existing graph captures only the coarse trait participation frame (trait→anaerobic respiration, sulfate→sulfide) but lacks the six core generic mechanistic modules (transport, activation, APS reduction, sulfite reduction, terminal reduction, energy coupling) that are universally required and well-supported across the 2023-2024 literature._

### metabolism/electron_transfer  — *skeletal* (7 edges)
- **Missing modules:** intracellular electron transport chain cascade (Complex I → quinone → bc1 → cytochrome c → terminal oxidase), proton motive force coupling and energy conservation, EET pathway architecture (outer-membrane conduit → periplasmic carriers → quinone pool), direct vs mediated extracellular electron transfer mechanisms
- `Complex I / NADH dehydrogenase —oxidizes and reduces→ ubiquinone`  (DOI:10.3390/ijms252413421 — 'Complex I… oxidizes NADH using )
- `ubiquinol —donates electrons to→ cytochrome bc1 complex`  (DOI:10.1073/pnas.2307093120 — electrons flow 'into the quino)
- `cytochrome bc1 complex —transfers electrons to→ cytochrome c`  (DOI:10.1073/pnas.2307093120 — 'then to the bc1 complex… and )
- `cytochrome c —transfers electrons to→ terminal oxidase`  (DOI:10.1073/pnas.2307093120 — 'onward via cytochrome c to te)
- `terminal oxidase —reduces→ oxygen to water`  (DOI:10.1073/pnas.2307093120 — 'terminal oxidases (Complex IV)
- `membrane electron transport chain —couples electron transfer to→ proton translocation and proton motive force`  (DOI:10.3390/ijms252413421 — 'coupling this redox reaction to)
- _Existing graph captures donor-acceptor framing and nanowire structures but entirely omits the intracellular ETC cascade (Complex I through terminal oxidases), energy-conservation coupling, and EET pathway topology — core generic mechanisms emphasized throughout the report._

### metabolism/ethanol_fermentation  — *skeletal* (2 edges)
- **Missing modules:** glycolysis as upstream pyruvate/NADH source, pyruvate decarboxylation to acetaldehyde + CO2 step, acetaldehyde reduction to ethanol by ADH step, NAD+ regeneration from NADH redox cofactor cycling
- `glycolysis —produces→ pyruvate`  (Yan 2024 (DOI:10.5376/be.2024.14.0025) establishes glycolysi)
- `pyruvate —is substrate for→ pyruvate decarboxylase (PDC) reaction`  (Yan 2024 (DOI:10.5376/be.2024.14.0025, pages 2-5): 'Pyruvate)
- `pyruvate decarboxylase activity —produces→ acetaldehyde`  (Yan 2024 (DOI:10.5376/be.2024.14.0025) describes PDC-catalyz)
- `acetaldehyde —is reduced by→ alcohol dehydrogenase (ADH)`  (Yan 2024 (DOI:10.5376/be.2024.14.0025, pages 2-5): 'acetalde)
- `ADH reaction —regenerates→ NAD+ from NADH`  (Yan 2024 (DOI:10.5376/be.2024.14.0025, pages 2-5): 'regenera)
- `ethanol fermentation —requires→ NAD+ cycling for glycolysis continuation`  (Yan 2024 and Bao 2023 (DOI:10.3390/fermentation9020113) both)
- _Existing graph captures trait classification and product but omits the entire generic enzymatic pathway (glycolysis→pyruvate→PDC→acetaldehyde→ADH→ethanol + NAD+ regeneration) that the report identifies as the core canonical mechanism universally supported by 2023–2024 literature._

### metabolism/iron_oxidation  — *skeletal* (2 edges)
- **Missing modules:** outer-membrane electron uptake (Cyc2, MtoA entry points), multiheme cytochrome electron transfer networks, terminal oxidase diversity (cbb3, bd for microaerobic), reactive nitrogen species inhibition, substrate form specialization (aqueous vs mineral-bound Fe2+)
- `iron_oxidation_trait —requires_protein_for_electron_uptake→ Cyc2`  (10.1128/msystems.00720-23 and 10.1128/msystems.00038-23 (bro)
- `iron_oxidation_trait —requires_protein_for_electron_uptake→ MtoA/MtoAB`  (10.1128/aem.00599-24 and 10.1128/msystems.00038-23 (substrat)
- `iron_oxidation_trait —requires_terminal_oxidase→ cbb3-type cytochrome oxidase`  (10.1128/aem.00599-24 (high-affinity terminal oxidase enablin)
- `multiheme_cytochromes —enables_electron_transfer_across→ minerals_and_long_distances`  (10.1128/msystems.00038-23 (EET capability in FeOB-enriched M)
- `nitrite_and_NO —inhibits→ cytochrome_c_activity`  (10.1128/msystems.00038-23 (generic environmental constraint:)
- `ferrous_iron —substrate_availability_depends_on→ substrate_form_aqueous_vs_mineral`  (10.1128/aem.00599-24 (Cyc2 associated with aqueous Fe2+)
- _The existing graph captures only the top-level reaction; the report describes multiple generic mechanistic modules (electron uptake proteins, terminal oxidase diversity, EET capability, regulatory inhibition, substrate specialization) that must be added to reflect the well-supported generic FeOB iron oxidation mechanism._

### metabolism/lactic_acid_fermentation  — *skeletal* (2 edges)
- **Missing modules:** glycolysis/EMP pathway, pyruvate-to-lactate enzymatic conversion (LDH), heterolactic branching via phosphoketolase, substrate-level ATP generation, anaerobic/redox environmental determinants
- `glucose —is fermented via→ glycolysis/EMP pathway`  (DOI:10.3390/fermentation10030168 (Aguirre-Garcia 2024))
- `pyruvate —is reduced by→ lactate dehydrogenase to form lactate`  (DOI:10.3390/foods12152850 (Hakim 2023))
- `homolactic pathway —produces→ 2 lactate + 2 ATP per glucose`  (DOI:10.3390/foods12152850 (Hakim 2023))
- `heterolactic LAB —use→ phosphoketolase pathway`  (DOI:10.3390/fermentation10030168 (Aguirre-Garcia 2024))
- `phosphoketolase pathway —yields→ lactate + ethanol/acetate + CO2`  (DOI:10.3390/fermentation10030168 (Aguirre-Garcia 2024))
- `anaerobic conditions —promote→ heterolactic stoichiometry with equimolar lactate/ethanol/CO2`  (Christofi 2023 (mixed-culture fermentation))
- _Existing graph captures phenotype (trait produces lactate) but omits core enzymatic machinery (LDH), substrate pathways (glycolysis), heterolactic branching, ATP generation, and environmental modifiers; at least 3 generic mechanistic modules are absent._

### metabolism/mixed_acid_fermentation  — *skeletal* (2 edges)
- **Missing modules:** glycolytic pyruvate hub, pyruvate formate lyase (PFL) branch, formate hydrogenlyase (FHL) complex, environmental anoxia control, acid-stress feedback (pH lowering)
- `glycolysis —produces→ pyruvate`  (Taggar et al. 2024 DOI:10.35812/cellulosechemtechnol.2024.58)
- `pyruvate —converted_by→ pyruvate formate lyase (PFL)`  (Brothwell et al. 2023 DOI:10.1128/iai.00176-23 and Taggar et)
- `acetyl-CoA —converted_to_by→ phosphotransacetylase (Pta) + acetate kinase (AckA)`  (Brothwell et al. 2023 DOI:10.1128/iai.00176-23 states Pta/Ac)
- `formate —disproportionated_by→ formate hydrogenlyase (FHL) complex`  (Li et al. 2024 DOI:10.1128/aem.01472-24 provides Figure 1 an)
- `mixed-acid products —lowers_pH_of→ cytoplasm`  (Brothwell et al. 2023 DOI:10.1128/iai.00176-23 explicitly st)
- `oxygen —inhibits→ formate hydrogenlyase activity`  (Li et al. 2024 DOI:10.1128/aem.01472-24 and Taggar et al. 20)
- _Existing graph misses all generic enzymatic branch structure, FHL complex, and environmental controls; report describes well-supported enterobacterial mechanism (2023–2024 primary literature) with clear pathway topology ready for curation._

### metabolism/nitrogen_fixation  — *skeletal* (4 edges)
- **Missing modules:** electron transfer chain (Fd/Fld to NifH to P-cluster to FeMo-co), FeMo-cofactor biosynthesis (NifS/U, K-cluster, NifB, L-cluster, NifEN, M-cluster assembly), oxygen inhibition of nitrogenase, ATP requirement and stoichiometry, proton and electron cofactors
- `ferredoxin (Fd) —transfers_electron_to→ NifH`  (DOI:10.34133/bdr.0005)
- `NifH —transfers_electron_to→ P-cluster`  (DOI:10.1128/aem.00378-23)
- `P-cluster —transfers_electron_to→ FeMo-cofactor`  (DOI:10.1128/aem.00378-23)
- `NifS and NifU —assembles→ [Fe4S4] clusters`  (DOI:10.1126/sciadv.adw6785)
- `NifB —assembles→ L-cluster`  (DOI:10.1038/s41929-024-01229-x)
- `oxygen —inhibits→ nitrogenase`  (DOI:10.1128/aem.00378-23)
- _Graph captures only trait-process-substrate-product skeleton; entirely missing generic electron-transfer and cofactor-assembly pathways that are universal across diazotrophs._

### metabolism/oxygenic_photosynthesis  — *skeletal* (2 edges)
- **Missing modules:** PSII water-oxidizing complex and Kok S-state cycle, linear electron transport chain (PSII→Cyt b6f→PSI→ferredoxin→NADPH), cyclic electron transport and NDH-1-mediated electron recycling, proton motive force generation and ATP synthase coupling, carbon concentrating mechanism (CCM: bicarbonate transporters, NDH-mediated CO2 hydration, carboxysome, Rubisco)
- `Photosystem II (PSII) —oxidizes→ water (H2O)`  (Shevela et al. 2023, DOI:10.1007/s11120-022-00991-y)
- `Mn4CaO5 oxygen-evolving complex (OEC) —is catalytic site for→ water oxidation`  (Shevela et al. 2023, DOI:10.1007/s11120-022-00991-y)
- `plastoquinol (PQH2) —donates electrons to→ cytochrome b6f complex`  (Milrad et al. 2024, DOI:10.3390/plants13152103)
- `linear electron transport —generates→ proton motive force (pmf)`  (Milrad et al. 2024, DOI:10.3390/plants13152103)
- `SbtA/BicA transporters —import→ bicarbonate (HCO3−)`  (Kurkela & Tyystjärvi 2024, DOI:10.1111/ppl.14140)
- `carboxysomal carbonic anhydrase —converts→ HCO3− to CO2`  (Kurkela & Tyystjärvi 2024, DOI:10.1111/ppl.14140)
- _Graph captures oxygen-evolution headline but misses the entire electron transport backbone, pmf generation, and carbon-concentrating mechanisms that form the generic mechanistic core documented across five recent 2023-2024 synthesis reviews._

### metabolism/photosynthesis  — *skeletal* (2 edges)
- **Missing modules:** oxygenic light reactions chain (PSII→PQ→Cyt b6f→PSI→FNR→NADPH), water oxidation complex (Mn4CaO5 oxygen evolution), anoxygenic type I reaction center electron transfer, antenna systems (phycobilisomes/chlorosomes/FMO), cyclic electron transfer pathway, ferredoxin–NADP reductase coupling
- `light energy —enables→ chlorophyll excitation`  (Grettenberger 2024, 10.1111/1751-7915.14519: 'Cyanobacteria )
- `water —oxidized by→ oxygen evolving complex (Mn4CaO5)`  (Grettenberger 2024, 10.1111/1751-7915.14519: 'electrons and )
- `photochemical charge separation —generates→ electron transport chain`  (Niederman 2024, 10.3390/biom14030311: 'light-driven charge s)
- `electron transport chain —creates→ proton motive force`  (Niederman 2024, 10.3390/biom14030311: 'powers cyclic electro)
- `proton motive force —drives→ ATP synthesis`  (Niederman 2024, 10.3390/biom14030311: 'electrochemical proto)
- `light energy —reduces→ ferredoxin`  (Grettenberger 2024, 10.1111/1751-7915.14519: 'PSI catalyses )
- _Existing graph captures trait-level definition but entirely lacks detailed electron-transport mechanisms for both oxygenic and anoxygenic photosynthesis; high-priority enrichment with antenna systems, reaction-center charge separation, and electron carriers recommended._

### metabolism/phototrophy  — *skeletal* (2 edges)
- **Missing modules:** light-driven photocycle activation (rhodopsin), visible light → ion transport (phototrophy mechanism), photochemical electron transport (chlorophyll), ATP synthase coupling to PMF, antenna pigment systems, environmental photodamage inhibitors
- `light —activates→ microbial rhodopsin photocycle`  (DOI:10.1093/ismejo/wrae175 (Hasegawa-Takano et al. 2024) — ')
- `rhodopsin photocycle —enables→ ion transport`  (DOI:10.1093/ismejo/wrae175 (Hasegawa-Takano et al. 2024) — ')
- `proton-pumping rhodopsin —generates→ proton motive force`  (DOI:10.1128/spectrum.02177-23 (Li et al. 2024) — 'pump proto)
- `proton motive force —drives→ ATP synthesis`  (DOI:10.1128/spectrum.02177-23 (Li et al. 2024) — 'creating a)
- `light —damages→ photosystem II`  (DOI:10.1111/1751-7915.14519 (Grettenberger et al. 2024) — 'H)
- `phycobilisome —transfers energy to→ photosystem`  (DOI:10.1111/1751-7915.14519 (Grettenberger et al. 2024) — 'P)
- _Graph captures light-in and PMF-out but omits 6+ generic mechanistic modules connecting them (photocycle activation, ion/electron transport, ATP synthase coupling, environmental photodamage); high-priority for enrichment with recent 2023-2024 research._

### metabolism/propionic_acid_fermentation  — *skeletal* (2 edges)
- **Missing modules:** Wood-Werkman cycle pathway scaffolding, succinate pathway (Bacteroidia), acrylate pathway (lactate-to-propionate), biotin/B12 cofactor nodes, NAD regeneration/redox balancing, intermediate enzymatic steps (methylmalonyl-CoA carboxytransferase, succinyl-CoA synthetase, methylmalonyl-CoA mutase)
- `propionic acid fermentation —has_major_pathway→ Wood-Werkman cycle`  (DOI:10.3390/molecules31020333 — Wood-Werkman methylmalonyl-C)
- `pyruvate —causally_upstream_of→ oxaloacetate`  (DOI:10.3390/molecules31020333 — Pyruvate carboxylated to oxa)
- `biotin —cofactor_for→ methylmalonyl-CoA carboxytransferase`  (DOI:10.3390/molecules31020333 — Transcarboxylation convertin)
- `vitamin B12 —cofactor_for→ methylmalonyl-CoA mutase`  (DOI:10.3390/molecules31020333 — Methylmalonyl-CoA mutase rea)
- `propionyl-CoA —causally_upstream_of→ propionate`  (DOI:10.3390/molecules31020333 — Propionyl-CoA converted to p)
- `propionic acid fermentation —has_byproduct→ acetate`  (DOI:10.3390/molecules31020333 — Propionate fermentation char)
- _Existing graph captures trait definition and output phenotype but lacks the entire mechanistic scaffolding (pathways, enzymatic steps, cofactors, redox balancing) that the report identifies as generic, well-supported, and curatable._

### metabolism/proteorhodopsin_phototrophy  — *skeletal* (2 edges)
- **Missing modules:** retinal biogenesis and scavenging, spectral tuning (Leu105/Gln105 depth adaptation), ATP synthesis coupling, ecological marker gene expression, acid stress and membrane homeostasis
- `all-trans retinal —required for→ proteorhodopsin`  (DOI:10.1038/s41467-024-50960-3)
- `beta-carotene dioxygenase —catalyzes synthesis of→ all-trans retinal`  (DOI:10.34133/2022/9782712)
- `proton motive force —drives→ ATP synthesis`  (DOI:10.4014/jmb.2410.10034)
- `Leu105 residue variant —enables→ green-shifted light absorption`  (DOI:10.1126/sciadv.adj0384)
- `Gln105 residue variant —enables→ blue-shifted light absorption`  (DOI:10.1126/sciadv.adj0384)
- `proteorhodopsin phototrophy —does not generate→ NAD(P)H`  (DOI:10.4014/jmb.2410.10034)
- _Existing graph captures only the core light-to-PMF step; report describes five major generic mechanistic modules (retinal biogenesis, spectral adaptation, ATP coupling, ecological markers, physiological constraints) with strong recent evidence (2022-2024) that should be integrated._

### metabolism/sulfur_oxidation  — *skeletal* (3 edges)
- **Missing modules:** SQR sulfide entry point, PDO persulfide dioxygenase pathway, rDSR alternative sulfur oxidation module, S4I tetrathionate intermediate pathway, terminal electron acceptor (O2) dependency
- `sulfide:quinone oxidoreductase (SQR) —oxidizes→ hydrogen sulfide to sulfane sulfur`  (10.3390/ijms252010962)
- `glutathione persulfide (GSSH) —is substrate of→ persulfide dioxygenase (PDO)`  (10.3390/ijms252010962)
- `persulfide dioxygenase (PDO) —produces→ sulfite`  (10.3390/ijms252010962)
- `reverse dissimilatory sulfite reductase (rDSR) —enables→ sulfur oxidation`  (10.1093/ismejo/wrae110)
- `thiosulfate dehydrogenase (TsdA) —oxidizes→ thiosulfate to tetrathionate`  (10.3389/fmicb.2024.1426584)
- `oxygen (O2) —required for→ complete sulfur oxidation pathway`  (10.1007/s10230-024-01016-x)
- _Existing graph captures trait → Sox → product skeleton only; misses generic intracellular/entry-point pathways (SQR/PDO), alternative oxidation systems (rDSR, S4I), and explicit TEA dependency well-documented in recent literature._

### metabolism/three_hydroxypropionate_bicycle  — *skeletal* (2 edges)
- **Missing modules:** diagnostic enzyme set (Acc, Pcc, Mcr, Pcs, MMC/Mcl), intermediary metabolite nodes (malonyl-CoA, 3-hydroxypropionate, propionyl-CoA, glyoxylate, pyruvate), ATP/NADPH cofactor dependency nodes, two-cycle process decomposition (first cycle vs. second cycle), pyruvate output as net product
- `bicarbonate —is_substrate_of→ acetyl-CoA carboxylase`  (10.17192/z2022.0467 (mclean2022invitrorealisation))
- `acetyl-CoA carboxylase —catalyzes_production_of→ malonyl-CoA`  (10.17192/z2022.0467 (mclean2022invitrorealisation))
- `malonyl-CoA reductase —catalyzes_production_of→ 3-hydroxypropionate`  (10.1146/annurev-marine-120709-142712 (hugler2011beyondthecal)
- `propionyl-CoA synthase —catalyzes_production_of→ propionyl-CoA`  (10.1146/annurev-marine-120709-142712 (hugler2011beyondthecal)
- `MMC lyase —catalyzes_production_of→ pyruvate`  (10.1146/annurev-marine-120709-142712 (hugler2011beyondthecal)
- `3-hydroxypropionate bicycle —requires_cofactor→ ATP`  (10.17192/z2022.0467 (mclean2022invitrorealisation))
- _Existing graph is a bare stub (bicarbonate → trait → carbon fixation) missing all internal enzyme catalysis, metabolite intermediates, cofactor dependencies, and the second cycle that produces net pyruvate; report describes a detailed 13-enzyme, 19-reaction mechanism suitable for substantial graph enrichment._

### metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle  — *skeletal* (2 edges)
- **Missing modules:** enzymatic carboxylation step (accA/acetyl-CoA carboxylase), 4-hydroxybutyrate intermediate processing (dehydratase, crotonyl-CoA recycling), cofactor requirements (NADPH, ATP), carbonic anhydrase substrate-supply context, aerobic environmental niche specification
- `3-hydroxypropionate/4-hydroxybutyrate cycle —forms intermediate→ succinyl-CoA`  (DOI:10.1186/s40643-023-00705-9 (2023))
- `succinyl-CoA —is reduced to→ 4-hydroxybutyrate`  (DOI:10.1186/s40643-023-00705-9 (2023))
- `4-hydroxybutyryl-CoA dehydratase —dehydrates→ 4-hydroxybutyryl-CoA to crotonyl-CoA`  (DOI:10.1038/s42003-024-06432-x (2024))
- `acetyl-CoA/propionyl-CoA carboxylase —mediates carboxylation in→ 3-hydroxypropionate/4-hydroxybutyrate cycle`  (DOI:10.1038/s42003-024-06432-x (2024))
- `NADPH —is required by→ 3-hydroxypropionate/4-hydroxybutyrate cycle reactions`  (DOI:10.1186/s40643-023-00705-9 (2023))
- `carbonic anhydrase —supplies substrate for→ 3-hydroxypropionate/4-hydroxybutyrate cycle via HCO3−`  (Cornell 2024 thesis (2024))
- _Existing graph captures only the outer boundary (CO2 fixation); the report describes a 10-step generic mechanism with enzymatic, chemical-intermediate, and cofactor nodes that are entirely absent from the current graph structure._

### metabolism/wood_ljungdahl_pathway  — *skeletal* (2 edges)
- **Missing modules:** methyl-branch C1 carrier and corrinoid-mediated methyl transfer network, carbonyl-branch CO reduction and CODH/ACS terminal condensation, ferredoxin-mediated electron transfer to CODH, energy conservation modules (Rnf/Ech chemiosmotic coupling)
- `Wood-Ljungdahl pathway —has_part→ methyl branch`  (10.3389/fbioe.2024.1395540)
- `methyl branch —requires→ tetrahydrofolate (THF) as C1 carrier`  (10.1039/d4cb00099d)
- `formyl-THF synthetase (Fhs/FTS) —catalyzes→ formate to formyl-THF formation`  (10.3389/fbioe.2024.1395540)
- `CODH/ACS complex —catalyzes→ CO + methyl-CoFeSP + CoA to acetyl-CoA condensation`  (10.3389/fbioe.2024.1395540)
- `Rnf or Ech complex —conserves_energy_via→ ion gradient to drive ATP synthase`  (10.1039/d4cb00099d)
- `Wood-Ljungdahl pathway —net_substrate_level_ATP_yield→ zero ATP (requires chemiosmotic coupling)`  (10.3389/fbioe.2024.1395540)
- _Existing graph captures only trait-level substrate/product; entirely missing the branched enzymatic pathway architecture, THF/corrinoid cofactor network, CODH/ACS terminal condensation, and critical energy-conservation modules that distinguish WLP mechanistically from other carbon fixation pathways._

### metabolism/xylan_degradation  — *skeletal* (2 edges)
- **Missing modules:** accessory debranching enzymes (arabinofuranosidase, glucuronidase, esterase), transport module (SusC/SusD or ABC importers), intracellular deacylation and decoration removal, regulatory systems (HTCS, ECF-sigma, CCR), accessory ester cleavage (CE15 synergy with xylanases)
- `debranching enzyme systems (arabinofuranosidases, glucuronidases, esterases) —enables→ arabinoxylan and glucuronoxylan depolymerization`  (DOI:10.3390/microorganisms12112271)
- `oligosaccharide transport systems (SusC/SusD, ABC importers) —enables→ xylan-oligosaccharide uptake and periplasmic/cytoplasmic processing`  (DOI:10.1007/s00253-023-12977-4)
- `intracellular hydrolases and esterases (GH51, GH43, GH8, GH39, CE deacylases) —enables→ debranching and deacylation of imported arabinoxylodextrins`  (DOI:10.1186/s12934-024-02423-z)
- `HTCS and ECF-sigma/anti-sigma regulatory systems —regulates→ hemicellulase and transport gene expression`  (DOI:10.1007/s00253-023-12977-4)
- `carbon catabolite repression (CCR / glucose-dependent mechanism) —represses→ hemicellulase gene expression during glucose availability`  (DOI:10.1007/s00253-023-12977-4)
- `CE15 glucuronoyl esterases —increases_effectiveness_of→ xylanase backbone hydrolysis on lignocellulose substrates`  (DOI:10.1186/s13068-025-02639-0)
- _Existing graph captures only xylanase backbone hydrolysis; report describes three generic mechanistic modules (polymer deconstruction, transport, intracellular completion) plus regulation and accessory cooperation—all absent from current graph."_

### morphology/amphitrichous  — *skeletal* (2 edges)
- **Missing modules:** FlhF polar localization and GTPase activity, FipA licensing of FlhF membrane targeting, HubP/FimV polar landmark recruitment cascade, FlhG antagonism and number restriction, FliG/FliF binding and MS-ring assembly, Flagellar assembly intermediate checkpoints
- `FipA —facilitates_localization_of→ FlhF to cell pole`  (DOI:10.7554/eLife.93004.3 — multi-species evidence (Vibrio, )
- `FlhF —binds→ FliG`  (DOI:10.1038/s41467-024-50274-4 — strong biochemical evidence)
- `FlhF_bound_FliG —recruits→ FliF MS-ring`  (DOI:10.1038/s41467-024-50274-4 — FlhF-bound FliG captures Fl)
- `HubP_FimV —recruits_to_pole→ FlhF_FliG complex`  (DOI:10.7554/eLife.93004.3 — polar landmark protein HubP recr)
- `FlhG —antagonizes_GTPase_activity_of→ FlhF`  (DOI:10.7554/eLife.93004.3 — FlhG stimulates FlhF GTP hydroly)
- `FlhG —restricts→ number of polar flagella`  (DOI:10.7554/eLife.93004.3 — FlhG links flagella synthesis wi)
- _Existing graph captures only morphological definition; 2023-2024 literature reveals sophisticated FlhF/FlhG/FipA/HubP patterning module as core generic mechanism, entirely absent from current TraitMech representation._

### morphology/capsule  — *skeletal* (3 edges)
- **Missing modules:** Wzx/Wzy-dependent capsule biosynthesis pathway, ABC transporter-dependent export pathway, Tyrosine phosphoregulatory control (CpsBCD system), Rcs envelope-stress phosphorelay signaling
- `Wzx flippase —flips→ lipid-linked capsule repeat unit`  (10.1038/s41522-024-00497-6 — 'the complete repeat unit is tu)
- `Wzy polymerase —polymerizes→ capsule polymer`  (10.1038/s41522-024-00497-6 — 'the Wzy polymerase attaches th)
- `KpsMT ABC transporter —exports→ polysaccharide chains across inner membrane`  (10.1038/s41522-024-00497-6 — 'the ABC transporter (KpsMT) pl)
- `Wza outer-membrane protein —enables→ translocation across outer membrane`  (10.1038/s41522-024-00497-6 — 'The polymer translocates acros)
- `Rcs phosphorelay —activates→ capsule synthesis genes`  (10.1371/journal.pgen.1011408 — 'The Rcs phosphorelay signali)
- `high osmolarity —increases→ capsule synthesis`  (10.1038/s41522-024-00497-6 — 'exposed to a 0.15 M sodium chl)
- _The existing graph captures only the terminal phenotype (assembly→polysaccharide→trait→immune evasion) and omits the three major generic biosynthesis pathways (Wzx/Wzy, ABC transporter, and envelope-stress regulation modules) that the report identifies as conserved across bacterial taxa._

### morphology/carboxysome  — *skeletal* (3 edges)
- **Missing modules:** shell diffusion barrier for CO2, bicarbonate transport and carboxysome entry, carbonic anhydrase enzymatic conversion, shell architecture and pore structure, local CO2 concentration around RuBisCO, carboxylation versus oxygenation selectivity
- `carboxysome_shell —prevents_loss_of→ carbon_dioxide`  (DOI:10.1038/nrmicro.2018.10)
- `carboxysomal_carbonic_anhydrase —converts→ bicarbonate_to_CO2`  (DOI:10.1128/aem.01075-24)
- `carboxysome_shell —permits_passage_of→ bicarbonate`  (DOI:10.1093/plphys/kiae438)
- `carbonic_anhydrase_activity —elevates_local_concentration_of→ CO2_around_Rubisco`  (DOI:10.1093/plphys/kiae438)
- `carboxysome_shell —limits_influx_of→ oxygen`  (DOI:10.1093/plphys/kiae438)
- `elevated_CO2_around_Rubisco —enhances→ Rubisco_carboxylation`  (DOI:10.1093/plphys/kiae438)
- _Existing graph covers only trait identity and broad function; the report reveals six well-supported generic mechanistic modules (shell permeability, bicarbonate transport, carbonic anhydrase action, local CO2 concentration, oxygen exclusion, carboxylation enhancement) that should be added to complete a core CCM causal graph._

### morphology/dumbbell_shaped  — *skeletal* (3 edges)
- **Missing modules:** septal peptidoglycan hydrolysis process, FtsEX-RipC regulatory complex, SteAB cell separation regulator, trehalose glycolipid septal infiltration structural state, outer envelope layer mechanical rupture module
- `septal peptidoglycan hydrolysis —enables→ daughter-cell separation`  (10.1073/pnas.2214599119)
- `FtsEX complex —regulates→ RipC-family cell division hydrolase`  (10.1038/s41467-023-43770-6)
- `RipC peptidoglycan endopeptidase activity —promotes→ septal peptidoglycan remodeling`  (10.1371/journal.pgen.1008284)
- `SteAB complex —promotes→ cell separation via RipC-FtsEX module`  (10.1371/journal.pgen.1008284)
- `septal peptidoglycan cleavage with outer layer continuity —leads to→ mechanical snapping separation`  (10.1128/mmbr.00028-07)
- `trehalose glycolipid infiltration of septum —precedes→ V-snapping`  (10.1371/journal.pgen.1008284)
- _Existing graph captures only the immediate morphological endpoint and two direct-acting processes; it omits the upstream FtsEX-RipC-SteAB regulatory module, peptidoglycan hydrolysis control, and outer envelope mechanics that the report identifies as generic, universal mechanisms for incomplete separation—all supported by strong primary evidence and quantitative phenotypes (31.7–45 min V-snap delays in regulatory mutants)."_

### morphology/gas_vesicle  — *skeletal* (2 edges)
- **Missing modules:** protein shell assembly (GvpA/GvpC), physical-chemical barrier mechanism (hydrophobic surface, gas diffusion, pressure collapse), transcriptional regulation (GvpE/GvpD), accessory protein interactions
- `GvpA —forms→ gas_vesicle_shell`  (DOI:10.1186/s13036-024-00426-3)
- `GvpA —self_assembles_into→ helical_half_shells`  (DOI:10.1186/s13036-024-00426-3)
- `hydrophobic_inner_surface —prevents→ water_condensation`  (DOI:10.1038/s44318-024-00178-2)
- `GvpC —strengthens→ gas_vesicle_shell`  (DOI:10.1186/s13036-024-00426-3)
- `pressure —irreversibly_collapses→ gas_vesicle`  (DOI:10.1186/s13036-024-00426-3)
- `GvpE —activates_transcription_of→ gvp_structural_genes`  (DOI:10.1186/s13036-024-00426-3)
- _Existing graph captures phenotypic outcome (buoyancy→positioning) but omits the entire molecular assembly, physical-chemical mechanism, and regulatory backbone documented in 2024 primary literature._

### morphology/intracellular_inclusion  — *skeletal* (2 edges)
- **Missing modules:** PHA biosynthesis and phasin coating, glycogen synthesis and N-limitation regulation, polyphosphate kinase/phosphatase balance, gas vesicle protein assembly (GvpA/GvpC structure), BMC shell assembly and cargo targeting via encapsulation peptides, magnetosome chain organization via MamJ/MamK/MamY
- `phaABC pathway —produces→ PHA granule`  (10.3390/molecules29102293 (Fukala 2024): direct evidence tha)
- `PhaP phasin —coats surface of→ PHA granule`  (10.3390/molecules29102293 (Fukala 2024): 'granules largely c)
- `nitrogen limitation —increases accumulation of→ glycogen granule`  (10.3390/fermentation10050265 (But 2024): Methylococcus capsu)
- `GvpA + GvpC —assemble into→ gas vesicle shell`  (10.1186/s13036-024-00426-3 (Feng 2024): 'shell primarily Gvp)
- `BMC-H/BMC-T/BMC-P —assemble into→ BMC shell`  (10.1042/bst20230229 (Doron 2024): core shell proteins form s)
- `MamJ/MamK/MamY magnetoskeleton —arranges→ magnetosome chain`  (10.1038/s41467-024-55121-0 (Paulus 2024): 'MamJ/MamK/MamY ar)
- _The existing graph captures only abstract compartmentalization but misses all generic mechanistic modules (biosynthesis, assembly, regulation) for 7 inclusion subtypes; report provides 53 well-cited edges suitable for expansion into module-based causal architecture._

### morphology/irregular_shaped  — *skeletal* (3 edges)
- **Missing modules:** MreB-mediated rod shape sensing and maintenance, RodZ-MreB complex assembly and organization, peptidoglycan synthase-hydrolase coordination, polar growth control (DivIVA/FilP/Scy axis), septal vs. sidewall synthesis balance, membrane microdomain organization at growth poles
- `MreB polymerization —enables→ rod shape maintenance`  (DOI:10.1101/2024.11.22.624946 (Kale et al.): MreB filaments )
- `RodZ-MreB complex organization —maintains→ rod shape`  (DOI:10.3389/fmicb.2024.1400434 (Ojima et al.): RodZ is neede)
- `peptidoglycan synthase-hydrolase imbalance —destabilizes→ rod shape`  (DOI:10.1038/s41467-023-41082-3 (Zhang et al.): Dysregulation)
- `polar growth organization —enables→ uniform apical growth`  (DOI:10.21203/rs.3.rs-3811693/v1 (Claessen et al.): DivIVA an)
- `loss of septal wall synthesis capability —enables→ amoeboid morphology`  (DOI:10.1038/s42003-024-07279-y (Hayashi et al.): Wall-less L)
- `reduced lateral wall patterning —increases→ morphological heterogeneity`  (DOI:10.1101/2024.07.30.605496 (Zambri et al.) and DOI:10.114)
- _Existing graph captures endpoint but lacks mechanistic depth; report identifies 6+ generic, transferable modules (cytoskeletal sensing, complex assembly, synthesis-hydrolase balance, polar growth control) absent from current 3-edge scaffold._

### morphology/lophotrichous  — *skeletal* (2 edges)
- **Missing modules:** FlhF-FlhG polar patterning module, pole landmark recruitment (HubP/FimV), FipA licensing factor, basal body assembly checkpoint (FliF/FliG/FliM/FliN), FlhG-mediated number control via GTPase stimulation, transcriptional regulation (FleQ/FlrA repression)
- `FlhF —localizes_to_and_recruits_basal_body_components_at→ cell pole`  (DOI:10.7554/eLife.93004.3)
- `FlhF —recruits→ FliG`  (DOI:10.7554/eLife.93004.3)
- `FlhG —negatively_regulates→ flagellar_number`  (DOI:10.1093/femsre/fuv034)
- `HubP_or_FimV —recruits→ FlhG_to_cell_pole`  (DOI:10.7554/eLife.93004.3)
- `FipA —required_for→ normal_polar_flagellar_synthesis`  (DOI:10.7554/eLife.93004.3)
- `FlhG —stimulates_GTPase_activity_of→ FlhF`  (DOI:10.1038/s41467-024-50274-4)
- _Existing graph captures only phenotypic boundary (flagella→lophotrichous) but omits the robust, generic FlhF/FlhG/pole-landmark mechanism universally conserved in polar-flagellated bacteria across 2024–2015 primary sources._

### morphology/mycelial_growth  — *skeletal* (2 edges)
- **Missing modules:** polarisome polarity complex (DivIVA/Scy/FilP assembly), branching via polarisome splitting, AfsK/SppA-mediated DivIVA phosphorylation stress control, CglA-mediated cell-wall glycopolymer attachment and septation coupling, surfactant/hydrophobic coating system (SapB/chaplins/rodlins), FtsZ Z-ladder sporulation scaffold
- `DivIVA polarisome —directs→ apical hyphal growth`  (10.1128/JB.00153-23)
- `polarisome splitting —causes→ daughter polarisomes and new branch emergence`  (10.1093/femsml/uqad020)
- `AfsK-mediated DivIVA phosphorylation —promotes→ hyperbranching`  (10.1093/femsml/uqad020)
- `CglA ligase —mediates→ wall glycopolymer attachment to peptidoglycan`  (10.1128/mbio.01492-24)
- `SapB and chaplins —promote→ aerial hyphae emergence`  (10.1093/femsml/uqad020)
- `FtsZ Z-ladders —drive→ sporulation septation and spore-chain formation`  (10.1128/mbio.01492-24)
- _Existing graph captures phenotypic differentiation but omits five major generic mechanistic modules (polarity complex, branching control, phosphorylation signaling, wall biogenesis, aerial-development surfactant system, sporulation architecture) that are well-supported by peer-reviewed literature; all six suggested edges are from peer-reviewed or strong review sources."_

### morphology/polyhydroxyalkanoate_granule  — *skeletal* (2 edges)
- **Missing modules:** environmental accumulation trigger (C/N, nutrient limitation), PHA biosynthetic enzyme cascade (PhaA/B/C pathway), granule coat protein assembly (PhaP phasin), transcriptional regulation (PhaR repression switch), mobilization/degradation response (PhaZ, starvation trigger)
- `high carbon-to-nitrogen ratio —increases→ polyhydroxyalkanoate accumulation`  (doi:10.3390/molecules29102293 (Fukala 2024))
- `PhaC (PHB synthase) —catalyzes→ polyhydroxyalkanoate polymerization`  (doi:10.3390/polym15143027 (Martinez 2023))
- `PhaP (phasin) —stabilizes→ polyhydroxyalkanoate granule`  (doi:10.3390/polym15143027 (Martinez 2023))
- `PhaR (repressor) —represses_transcription_of→ phaP`  (doi:10.1016/j.jbc.2024.107523 (Santolin 2024))
- `carbon starvation —increases→ PHB mobilization`  (doi:10.1101/2023.07.06.548030 (Koning 2023))
- `PhaZ (depolymerase) —mediates→ polyhydroxyalkanoate degradation`  (doi:10.3390/polym15143027 (Martinez 2023))
- _The existing graph captures only the trait phenotype and end-stage storage function, missing five generic mechanistic modules (environmental triggers, biosynthetic pathway, coat proteins, transcriptional regulation, mobilization) supported by peer-reviewed 2023–2024 sources; prioritize environmental and enzymatic edges first._

### morphology/s_layer  — *skeletal* (2 edges)
- **Missing modules:** Gram-positive teichoic acid anchoring (TAB domain binding), Gram-positive SCWP-anchoring via SLH domains, Archaeal glycosylation (AglB-mediated N-glycosylation), Archaeal two-component SlaA/SlaB assembly, Diderm envelope coordination (PG turnover + LPS dependence)
- `S-layer (glyco)protein subunits —requires for assembly→ Ca2+ / divalent cation binding`  (DOI:10.1038/s41467-024-47529-5 (Herdman et al. 2024): Purifi)
- `TAB (teichoic-acid-binding) domain —binds→ lipoteichoic acid (LTA) / wall teichoic acid (WTA)`  (DOI:10.1073/pnas.2401686121 (Sagmeister et al. 2024): ITC/NM)
- `SLH (S-layer homology) domains —bind→ secondary cell wall polysaccharide (SCWP) with ketal-pyruvylated N-acetylmannosamine`  (DOI:10.1038/s41467-023-42826-x (Sogues et al. 2023): Sap/EA1)
- `Archaeal AglB oligosaccharyltransferase —glycosylates→ S-layer protein (SlaA)`  (DOI:10.7554/eLife.84617 (Gambelli et al. 2024): AglB is esse)
- `SlaA (outer glycoprotein) —assembles with→ SlaB (inner membrane-bound component)`  (DOI:10.7554/eLife.84617 (Gambelli et al. 2024): Two-componen)
- `LPS (lipopolysaccharide) —is required for→ S-layer insertion in diderm bacteria`  (DOI:10.1038/s41467-024-47529-5 (Herdman et al. 2024): Locali)
- _Existing graph captures self-assembly backbone but lacks mechanistic detail on attachment (teichoic acids vs SLH vs archaeal two-component), post-translational modification (glycosylation), and envelope-context dependencies; report recommends curating these as alternative lineage-specific pathways per section 8.1._

### morphology/sarcina_arrangement  — *skeletal* (2 edges)
- **Missing modules:** FtsZ polymerization and Z-ring assembly, Divisome recruitment (DivIB-DivIC-FtsL-MurJ pathway), Septal peptidoglycan synthesis and remodeling, Autolysin-mediated daughter-cell separation, Division-plane placement regulation (Noc nucleoid occlusion), Incomplete septum splitting control
- `Noc-bound DNA —inhibits→ FtsZ Z-ring assembly over nucleoid`  (DOI:10.1002/mbo3.1338)
- `FtsZ —polymerizes_to_form→ Z-ring`  (DOI:10.1002/mbo3.1338)
- `DivIB-DivIC-FtsL complex —recruits→ MurJ to divisome`  (DOI:10.1002/mbo3.1338)
- `Peptidoglycan hydrolases —degrade→ peripheral peptidoglycan bridge`  (DOI:10.1002/mbo3.1338)
- `FtsZ-dependent cell wall synthesis —drives→ division septum formation`  (DOI:10.1111/j.1574-6976.2007.00098.x)
- `Delayed autolysin activity —enables→ retention of cells as cubic packets`  (DOI:10.1111/j.1574-6976.2007.00098.x)
- _Existing graph is a direct phenotype edge only; the report describes a rich mechanistic backbone (FtsZ assembly, PG remodeling, autolysin regulation, and placement control) that explains both perpendicular-plane selection and incomplete separation, none of which are represented in the causal graph._

### morphology/twitching_motility  — *skeletal* (2 edges)
- **Missing modules:** PilB extension motor ATPase, PilT retraction motor ATPase, pilus secretion/surface exposure (PilQ), pilus alignment complex, cAMP-mediated T4P gene transcription
- `PilB extension ATPase —drives→ type IV pilus extension`  (DOI:10.1128/jb.00359-24)
- `PilT retraction ATPase —drives→ type IV pilus retraction`  (DOI:10.1128/jb.00359-24)
- `type IV pilus retraction —enables→ twitching motility`  (DOI:10.1128/jb.00442-23)
- `PilQ secretin —enables_surface_exposure_of→ type IV pilus filament`  (DOI:10.1099/mic.0.001311)
- `cAMP —promotes_transcription_of→ type IV pilus genes`  (DOI:10.1128/jb.00359-24)
- `PilM/N/O/P alignment complex —forms_part_of→ type IV pilus machine`  (DOI:10.1038/s41467-024-53638-y)
- _Existing graph captures trait definition but omits the pilus motor cycle (extension/retraction ATPases), secretion barrier (PilQ), and upstream cAMP regulation that the report identifies as generic, well-supported mechanistic modules._

### morphology/yellow_pigmented  — *skeletal* (4 edges)
- **Missing modules:** isoprenoid precursor hierarchy (IPP/DMAPP→GGPP→lycopene), β-carotene as canonical yellow carotenoid, xanthomonadin/aryl polyene alternative mechanism, flexirubin-type pigment alternative mechanism, lycopene→β-carotene cyclization (crtY specificity)
- `IPP/DMAPP —precursor_of→ GGPP`  (DOI:10.1038/s41598-024-58700-9 — foundational isoprenoid cas)
- `GGPP —precursor_of→ lycopene`  (DOI:10.1038/s41598-024-58700-9 — C40 backbone formation, uni)
- `lycopene —precursor_of→ beta-carotene`  (DOI:10.1038/s41598-024-58700-9 — crtY-catalyzed cyclization )
- `3-hydroxybenzoic_acid —precursor_of→ xanthomonadin`  (DOI:10.1016/j.heliyon.2024.e34275 — generic aryl polyene pat)
- `acetyl-CoA_polyene_elongation —produces→ flexirubin_chromophore`  (DOI:10.1038/s41467-024-54112-5 — fatty-acid-like polyene bio)
- `beta-carotene —causes→ yellow_phenotype`  (DOI:10.4014/jmb.2404.04018 — β-carotene explicitly documente)
- _Existing graph captures only the final output chain (enzyme → biosynthesis → pigment → color); missing precursor cascade, canonical yellow intermediate (β-carotene), and alternative pigment pathways (xanthomonadin, flexirubin) that are well-documented as generic mechanisms across taxa._

### physiology/antibiotic_resistance  — *skeletal* (2 edges)
- **Missing modules:** enzymatic drug inactivation (beta-lactamase), target modification via QRDR mutations, target modification via rRNA methylation, reduced permeability via porin loss/modification, R plasmid-mediated dissemination
- `beta-lactamase —enables→ antibiotic resistance to beta-lactams`  (DOI:10.1038/s43856-024-00591-y)
- `outer membrane porin modification —decreases→ antibiotic influx`  (DOI:10.3390/pharmaceutics16020170)
- `QRDR mutation in DNA gyrase —confers resistance to→ fluoroquinolone`  (DOI:10.3389/fphar.2024.1444781)
- `23S rRNA methyltransferase (erm/cfr) —decreases binding of→ macrolide antibiotic`  (DOI:10.3389/fphar.2024.1444781)
- `R plasmid —carries→ antibiotic resistance gene`  (DOI:10.3389/fphar.2024.1444781)
- `intracellular antibiotic concentration —affected by→ reduced permeability and efflux`  (DOI:10.3390/pharmaceutics16020170)
- _Existing graph captures only efflux among four canonical mechanisms; skeletal structure lacks enzymatic inactivation, target modification, permeability reduction, and dissemination pathways essential to generic antibiotic resistance phenotype._

### physiology/chemotaxis  — *skeletal* (2 edges)
- **Missing modules:** chemoreceptor ligand sensing, CheA autophosphorylation, two-component phosphorelay (CheA→CheY), motor control via CheY-P, signal reset (CheZ phosphatase), sensory adaptation (CheR/CheB methylation cycle), flagellar motor output node
- `chemoreceptor —modulates→ CheA autophosphorylation`  (DOI:10.1146/annurev-micro-032421-110850)
- `CheA —phosphorylates→ CheY`  (DOI:10.1146/annurev-micro-032421-110850)
- `CheY-P —induces→ flagellar rotation`  (DOI:10.1146/annurev-micro-032421-110850)
- `CheZ —dephosphorylates→ CheY-P`  (DOI:10.1146/annurev-micro-032421-110850)
- `CheR —methylates→ chemoreceptors`  (DOI:10.1146/annurev-micro-032421-110850)
- `CheW —scaffolds→ CheA-receptor complex`  (DOI:10.1146/annurev-micro-032421-110850)
- _Existing graph captures trait definition and environmental stimulus but entirely omits the canonical two-component phosphorelay, motor control, and adaptation modules that define the chemotaxis mechanism._

### physiology/dormancy  — *skeletal* (2 edges)
- **Missing modules:** stringent response (p)ppGpp cascade, toxin-antitoxin TA induction and translation arrest, ribosome hibernation machinery (RMF/HPF/RaiA), energetic state control (ATP depletion, PMF disruption), NAD+ resuscitation pathway, oxidative stress tolerance
- `nutrient limitation/starvation —activates→ stringent response ((p)ppGpp alarmone pathway)`  (10.1186/s12866-024-03628-3 (yuan2024molecularmechanismand pa)
- `stringent response ((p)ppGpp) —upregulates→ toxin-antitoxin (TA) modules`  (10.1186/s12866-024-03628-3 (yuan2024molecularmechanismand pa)
- `TA toxins (TisB/HokB/RelE/MazF) —inhibit→ translation and ATP synthesis`  (10.1186/s12866-024-03628-3 (yuan2024molecularmechanismand pa)
- `ribosome hibernation factors (RMF/HPF/RaiA) —inhibit→ protein synthesis / 70S ribosome activity`  (10.3389/fmicb.2024.1386179 (helena-bueno2024ripplinglifeon p)
- `rewetting/hydration —triggers→ resuscitation / ATP-driven NAD+ synthesis`  (10.1038/s41467-024-46920-6 (imminger2024survivalandrapid pag)
- `ATP depletion / low energetic state —induces / maintains→ dormancy phenotype`  (10.1128/msystems.01060-24 (leinberger2024proteinaggregationi)
- _Existing graph captures only top-level entry trigger; report details generic energy-allocation and translation-shutdown machinery absent from current curation, representing >=4 distinct mechanistic modules (stringent response, TA cascade, hibernation factors, resuscitation pathways)._

### physiology/lithoautotrophic  — *skeletal* (6 edges)
- **Missing modules:** multiple electron acceptors (O2 vs nitrate), explicit electron transport chain + PMF + ATP nodes, reverse electron flow → reducing equivalents mechanism, DIC acquisition toolkit (transporters + carbonic anhydrase), pH-dependent DIC speciation (CO2 vs HCO3-), alternative carbon fixation pathways (rTCA, Wood-Ljungdahl), generic sulfur oxidation modules (Sox/rDsr systems)
- `inorganic_electron_donor —oxidized by→ electron_transport_chain`  (Jahn et al. DOI:10.1128/aem.00748-24: membrane-bound dehydro)
- `electron_transport_chain —generates→ proton_motive_force`  (Jahn et al. DOI:10.1128/aem.00748-24: ETC drives PMF buildup)
- `proton_motive_force —powers→ ATP_synthase`  (Gupta et al. DOI:10.1007/s10295-020-02309-0: PMF drives ATP )
- `electron_transport_chain —enables_via_reverse→ reducing_power`  (Gupta et al. DOI:10.1007/s10295-020-02309-0: reverse electro)
- `dissolved_inorganic_carbon —speciation_depends_on→ pH`  (Scott et al. DOI:10.1128/aem.01557-23: CO2 dominates at low )
- `DIC_transport_toolkit —facilitates→ autotrophic_co2_fixation`  (Scott et al. DOI:10.1128/aem.01557-23: carbonic anhydrase + )
- _The existing graph captures the minimal energy-fixation backbone but misses generic mechanistic layers (ETC/PMF/ATP separation, reverse electron flow, DIC toolkit, alternative fixation pathways, sulfur modules) that report identifies as widely reusable across taxa and environments._

### physiology/oxidase_activity  — *skeletal* (3 edges)
- **Missing modules:** Electron-transfer chain through heme-copper cofactor architecture, CuA/CuB copper centers and heme cofactors, Reduced cytochrome c as electron-donor specification, Cofactor availability and copper metalation dependency
- `reduced_cytochrome_c —donates_electrons_to→ CuA_center`  (DOI:10.3390/microorganisms10050926 — canonical electron-entr)
- `CuA_center —transfers_electrons_to→ heme_a`  (DOI:10.3390/microorganisms10050926 — core electron-flow step)
- `heme_a —transfers_electrons_to→ heme_a3_CuB_binuclear_center`  (DOI:10.3390/microorganisms10050926 — penultimate electron-fl)
- `cytochrome_c_oxidase —has_cofactor→ heme_a`  (DOI:10.3390/microorganisms10050926 — essential prosthetic gr)
- `cytochrome_c_oxidase —has_cofactor→ CuA_dicopper_center`  (DOI:10.3390/microorganisms10050926 — electron-entry metal ce)
- `copper_ion_availability —positively_regulates→ cytochrome_c_oxidase_activity`  (DOI:10.3389/fmicb.2021.683260 — generic principle: copper li)
- _The existing graph shows only the terminal scaffold (protein → activity → O2 reduction) but omits the detailed generic electron-transfer chain, cofactor architecture, and cofactor-availability regulation that constitute the biochemical mechanism in the literature report._

### physiology/persister_cell_formation  — *skeletal* (2 edges)
- **Missing modules:** stringent response signaling (ppGpp), toxin-antitoxin systems, ATP/energy state depletion, NAD+/NADP+ metabolic regulation, proton motive force maintenance, electron transport chain/oxidative phosphorylation
- `stringent response alarmone (p)ppGpp —positively_regulates→ toxin-antitoxin system activity`  (DOI:10.3389/fmicb.2024.1395504)
- `toxin-antitoxin system activity —decreases→ intracellular ATP level`  (DOI:10.3389/fmicb.2024.1395504 (Brucella))
- `nutrient limitation / stationary phase —triggers→ persister cell formation`  (DOI:10.3389/fmicb.2024.1395504)
- `decreased intracellular ATP level —enables→ persister cell formation`  (DOI:10.3389/fmicb.2024.1395504 (explicit ATP association wit)
- `persister cell formation —requires→ proton motive force generation`  (DOI:10.1111/1751-7915.70042 (persisters actively generate PM)
- `antibiotic stress / phage attack / starvation —triggers→ stringent response activation`  (DOI:10.1128/ecosalplus.esp-0025-2022 (multiple stress trigge)
- _Existing graph captures only dormancy-tolerance bookend; misses central mechanistic modules (ppGpp signaling, TA systems, metabolic state changes, PMF maintenance) documented as generic across multiple species and stress contexts in 2023-2024 literature._

### physiology/spore_germination  — *skeletal* (2 edges)
- **Missing modules:** germinant receptor sensing as nutrient-gated ion channels, early cation efflux from spore core, SpoVA-mediated DPA/CaDPA release, cortex peptidoglycan hydrolysis (CwlJ/SleB enzymes), core rehydration and outgrowth
- `GerA-family germinant receptor —mediates release of→ cations from spore core (K+, Na+, H+, Ca2+)`  (10.1126/science.adg9829)
- `cation efflux from spore core —triggers→ SpoVA-mediated DPA/CaDPA release`  (10.1126/science.adg9829)
- `DPA/CaDPA release —activates→ CwlJ-catalyzed cortex peptidoglycan hydrolysis`  (10.1101/gad.351353.123)
- `SleB —redundantly contributes to→ cortex peptidoglycan hydrolysis`  (10.1128/mbio.02220-23)
- `cortex peptidoglycan hydrolysis —enables→ spore core rehydration and outgrowth`  (10.1128/mbio.02220-23)
- `germinant binding to GerA receptor —initiates→ cation-release cascade`  (10.1126/science.adg9829)
- _Existing graph is a bare stub capturing only top-level concept; modern literature (2023–2024) has revealed mechanistic detail (nutrient-gated ion channels, ion-flux-triggered DPA release, ordered cortex-lysis cascade) that should anchor the graph for generic germination across Bacillus and related endospore formers._

### physiology/stress_response  — *skeletal* (2 edges)
- **Missing modules:** RpoS sigma-factor hub, stringent response / (p)ppGpp alarmone signaling, sRNA-Hfq mediated translational control, RpoS proteolysis regulation (RssB/ClpXP/anti-adaptors), RpoS recovery feedback loop, oxidative stress response (ROS/OxyR) module
- `nutrient deprivation / starvation —increases accumulation of→ RpoS (sigma-S factor)`  (DOI:10.1146/annurev-micro-090110-102946)
- `RpoS —induces expression of→ general stress resistance genes`  (DOI:10.1146/annurev-micro-090110-102946)
- `nutrient limitation —triggers synthesis of→ (p)ppGpp alarmone`  (DOI:10.1099/mic.0.001483)
- `(p)ppGpp —positively regulates→ RpoS accumulation`  (DOI:10.1016/j.isci.2024.108818)
- `reactive oxygen species (ROS) —activates→ OxyR transcription factor`  (DOI:10.1099/mic.0.001481)
- `OxyR —induces→ oxidative defense genes`  (DOI:10.1099/mic.0.001481)
- _The existing graph captures only the outermost stimulus-response arc; it entirely omits RpoS (the canonical sigma factor), (p)ppGpp stringent signaling, and multi-layer regulatory mechanisms that are generic, broadly conserved, and essential to stress-response phenotype._

### physiology/viable_but_nonculturable_state  — *skeletal* (2 edges)
- **Missing modules:** stringent response / (p)ppGpp regulatory switch, ATP-mediated NAD+ resuscitation pathway, oxidative stress defense module gating resuscitation, Rpf-mediated peptidoglycan remodeling and reanimation, DnaK-ClpB proteostasis system, toxin-antitoxin metabolic dampening
- `relA/spoT activity —increases→ (p)ppGpp accumulation`  (DOI:10.3390/foods12061179)
- `ATP availability —promotes→ VBNC resuscitation efficiency`  (DOI:10.1016/j.jare.2023.08.002)
- `ATP —drives→ NAD+ biosynthesis during resuscitation lag phase`  (DOI:10.1016/j.jare.2023.08.002)
- `NAD+ availability —restores→ TCA cycle flux and oxidative phosphorylation`  (DOI:10.1016/j.jare.2023.08.002)
- `oxidative stress / ROS —inhibits→ VBNC resuscitation`  (DOI:10.1186/s13213-022-01703-6)
- `Rpf peptidoglycan hydrolase —triggers→ reanimation / resuscitation from VBNC`  (DOI:10.3390/microorganisms12122662 and DOI:10.3390/microorga)
- _The existing graph captures only the initial stress-to-dormancy trigger; the report describes 5+ generic mechanistic modules (stringent response, ATP-NAD+ resuscitation, oxidative stress gating, Rpf reanimation, proteostasis) that are well-supported and should be curated in."_

### ecology/biosafety_level_5  — *skeletal* (2 edges)
- **Missing modules:** hazard property decomposition (infectivity, severity, transmissibility), aerosol/inhalation risk escalation, vaccine/treatment-unavailability linkage to containment
- `infectivity —defines→ biosafety level assignment`  (Pavone et al. 2024 DOI:10.3390/ani14030454)
- `disease severity —defines→ biosafety level assignment`  (Pavone et al. 2024 DOI:10.3390/ani14030454)
- `transmissibility —defines→ biosafety level assignment`  (Pavone et al. 2024 DOI:10.3390/ani14030454)
- `aerosol transmissibility —increases need for→ biosafety level 4`  (Gao et al. 2024 DOI:10.3390/laboratories1030013)
- `lack of vaccines or treatments —motivates→ biosafety level 4`  (Gao et al. 2024 DOI:10.3390/laboratories1030013)
- _Existing graph captures only a vague \"enhanced hazard\" umbrella; report identifies five well-supported generic hazard-property-to-containment edges that should decompose the mechanism but are entirely absent."_

### ecology/commensalism  — *skeletal* (2 edges)
- **Missing modules:** host immune tolerance signaling (IgA/IL-22), microbial attachment/adhesion to host substrates, host-derived nutrient/resource availability (mucins), environmental gradient regulation (oxygen limitation), host protective barriers (bile acid shielding, antimicrobial peptides)
- `secretory IgA —promotes colonization of→ bacteria in mucus layer`  (doi:10.1126/science.adi3338)
- `mucus/mucins —provides niche and resources for→ mucin-foraging bacteria`  (doi:10.1126/science.adi3338)
- `bacterial glycan-binding proteins —mediate attachment to→ mucin`  (doi:10.1126/science.adi3338)
- `secretory IgA —protects from→ bile acids`  (doi:10.1126/science.adi3338)
- `oxygen limitation —favors→ fermentation-capable bacteria`  (doi:10.1126/science.adi3338)
- _Current graph is a bare definition scaffold; report documents 10+ generic mechanistic pathways (immune tolerance, attachment, nutrient provisioning, environmental gradients) with strong peer-reviewed support that are entirely absent from causal structure._

### morphology/magnetosome  — *skeletal* (2 edges)
- **Missing modules:** membrane invagination and protein targeting (MamF-like system), magnetosome chain assembly and positioning (MamK-centered magnetoskeleton), iron transport infrastructure (FeoB1/FeoB2 and CDF-family transporters)
- `mamAB operon —sufficient for→ rudimentary biomineralization`  (DOI:10.1111/mmi.15330)
- `MamB —promotes→ membrane invagination`  (DOI:10.1111/mmi.15330)
- `MamF-like proteins —enable targeting of→ MamD and Mms5 to magnetosome membrane`  (DOI:10.1038/s41467-024-55121-0)
- `MamK —organizes→ magnetosome chain assembly`  (DOI:10.1128/mbio.01649-23)
- `MamJ —tethers→ magnetosomes to MamK filaments`  (DOI:10.1128/mbio.01649-23)
- _Existing graph captures only phenotypic endpoints; report details at least five generic, curation-ready mechanistic edges spanning early organelle biogenesis (membrane/targeting), chain assembly, and supporting infrastructure._

### morphology/tetrad_arrangement  — *skeletal* (2 edges)
- **Missing modules:** FtsZ/divisome-driven septation, cell wall hydrolase-mediated daughter-cell splitting, division-plane memory/DivIVA-guided perpendicular orientation
- `FtsZ Z-ring assembly —initiates→ septation`  (DOI:10.1042/bst20240956 + DOI:10.1101/2024.11.18.624142)
- `septation —enables→ tetrad arrangement`  (DOI:10.1038/ncomms4842 + DOI:10.1042/bst20240956)
- `cell wall hydrolases —mediate→ daughter-cell splitting`  (DOI:10.1042/bst20240956)
- `incomplete daughter-cell separation —results_in→ tetrad attachment`  (DOI:10.1038/ncomms4842 + DOI:10.1042/bst20240956)
- `two perpendicular division planes —combined_with→ incomplete daughter-cell separation`  (DOI:10.1042/bst20240956 line 248)
- _Existing graph captures phenotype-level division-plane edge but misses foundational septation (FtsZ) and splitting (hydrolase) modules that are generically essential; report flags *D. radiodurans*-specific DivIVA/RqkA pathway and *S. aureus* morphology cues as uncertain/taxon-specific and correctly excludes them from generic graph."_

### environment/ph_delta_very_low  — *skeletal* (2 edges)
- **Missing modules:** PMF partitioning and ΔpH/Δψ remodeling, energetic cost-breadth trade-off constraint, external pH as environmental trigger
- `external pH —alters→ transmembrane proton gradient`  (DOI:10.1038/nrmicro2549 (Krulwich et al. 2011, pages 3-5): f)
- `constitutive pH-homeostasis machinery expression —imposes energetic cost on→ growth near neutral pH`  (DOI:10.1038/nrmicro2549 (Krulwich et al. 2011, pages 3-5): e)
- `proton motive force partitioning —enables→ pH homeostasis`  (DOI:10.1038/nrmicro2549 (Krulwich et al. 2011, pages 3-5): Δ)
- `energetic cost of constitutive specialization —contributes to→ narrow growth breadth`  (DOI:10.1038/nrmicro2549 (Krulwich et al. 2011, pages 3-5): c)
- _The trait graph captures the high-level phenotype (very limited pH-homeostasis flexibility produces narrow breadth) but lacks the mechanistic intermediate layer: how external pH triggers PMF remodeling, what energetic trade-off actually drives stenotopy, and which proteins/processes sustain that tradeoff—all documented as generic, broadly-applicable mechanisms in the research literature._

### morphology/peritrichous  — *skeletal* (2 edges)
- **Missing modules:** flagellar assembly regulation (master regulators, hierarchical sigma factors), basal body insertion and envelope-based localization mechanism, FlhF/FlhG cytoplasmic patterning control (conserved placement/number regulators), cell-wall/peptidoglycan spatial constraints on basal body distribution
- `bacterial flagellar assembly —required_for→ peritrichous flagellar arrangement`  (DOI:10.1093/femsre/fuv034 and DOI:10.3390/biom9070279 establ)
- `FlhF/FlhG family regulators —regulate→ flagellar basal body number and placement`  (DOI:10.1038/s41467-024-50274-4 (Dornes et al. 2024) mechanis)
- `basal body insertion through cell envelope —determines→ flagellar spatial distribution`  (DOI:10.1128/mbio.00530-25 (Dunn et al. 2025) shows rod assem)
- `peptidoglycan and cell-wall structure —constrains→ basal body insertion sites`  (DOI:10.1128/mbio.00530-25 describes 'permissive holes' in PG)
- _Existing graph captures trait definition but omits all mechanistic layers (assembly, localization, regulation); report identifies generic modules but emphasizes taxon-specificity (B. subtilis rod/PG model, polar-specific FlhF anchoring) and warns against overgeneralization, limiting truly universal curable edges."_

### ecology/biosafety_level_4  — *shallow* (2 edges)
- **Missing modules:** disease severity hazard driver, countermeasure absence hazard driver, aerosol transmission risk hazard driver, positive-pressure suit containment control, airlock containment control, decontamination shower containment control, specialized waste disposal containment control
- `life-threatening disease severity —requires containment level→ biosafety level 4`  (DOI:10.1016/j.pathol.2020.09.006)
- `absence of effective prevention or treatment —requires containment level→ biosafety level 4`  (DOI:10.1016/j.pathol.2020.09.006)
- `high risk of aerosol-transmitted laboratory infection —requires containment level→ biosafety level 4`  (DOI:10.1016/j.pathol.2020.09.006)
- `biosafety level 4 —necessitates use of→ positive-pressure air-supplied suit`  (DOI:10.1016/j.pathol.2020.09.006)
- `biosafety level 4 —requires→ airlock`  (DOI:10.3390/laboratories1030013)
- `biosafety level 4 —requires→ specialized waste disposal`  (DOI:10.3390/laboratories1030013)
- _Existing graph captures only a vague "extreme pathogen hazard" node without decomposing the three generic hazard drivers (severity, countermeasure absence, aerosol risk) or representing BSL-4 engineering/procedural containment controls._

### ecology/endosymbiosis  — *shallow* (2 edges)
- **Missing modules:** host immune tolerance (PGRP-mediated peptidoglycan control of IMD pathway), metabolic complementation (host-symbiont amino acid & nutrient exchange), host developmental control (NIN-mediated intracellular infection signaling), host nutrient homeostasis (phosphate & iron limitation feedback on symbiosis stability), DNA repair complementation (inter-symbiont MMR assembly), vertical transmission mechanisms (ovarian tropism, transovarial transmission)
- `host immune peptidoglycan recognition —controls→ endosymbiont proliferation`  (PGRP-LB amidase cleaves peptidoglycan to prevent IMD pathway)
- `host nutrient limitation (phosphate, iron) —constrains→ symbiosis stability and nitrogen fixation`  (Pi and Fe deficiency significantly reduce nodule formation a)
- `host-symbiont metabolic complementarity —enables→ intracellular symbiont survival`  (Amino acid pathway complementarity between host and Tremblay)
- `DNA mismatch repair assembly (Serratia MutH + Buchnera MutL/S) —preserves→ endosymbiont genome stability`  (Inter-symbiont protein translocation enables active MMR)
- `intracellular symbiont abundance —signals_to→ host mTOR pathway`  (Altering Tremblaya abundance activates host mTOR, consistent)
- `ovarian enrichment of symbionts —enables→ transovarial vertical transmission`  (Symbiodolus high abundance in female ovaries across life sta)
- _Existing graph captures the intracellular localization–genome reduction backbone but misses six major generic mechanistic modules documented in recent literature: immune tolerance, metabolic complementation, nutrient homeostasis feedback, host developmental signaling, DNA repair complementation, and transmission mechanisms._

### ecology/free_living  — *shallow* (2 edges)
- **Missing modules:** nutrient acquisition (phosphorus), motility and chemotaxis, osmotic stress tolerance, metabolic biosynthetic completeness
- `phosphorus acquisition genes (pst/ugp/pho/phn) —enables→ environmental nutrient acquisition`  (10.1128/aem.00601-23, 10.1111/1755-0998.13889 — Free-living )
- `flagellar assembly genes (fli/flg) —enables→ motility`  (10.1128/aem.00601-23 — Free-living Leisingera genome encodes)
- `chemotaxis genes (che) —promotes→ free-living lifestyle`  (10.1128/aem.00601-23 — Free-living cells upregulate chemotax)
- `ectoine biosynthetic pathway —enables→ osmotic stress tolerance`  (10.48550/arxiv.2302.00582, 10.1371/journal.pone.0287947 — Ma)
- `osmotic stress tolerance —promotes→ free-living lifestyle`  (10.48550/arxiv.2302.00582 — Salinity transitions (salt barri)
- `metabolic biosynthetic completeness (carbon/nitrogen/sulfur/cofactors) —required_for→ free-living lifestyle`  (10.1186/s12915-024-02013-w, 10.1128/aem.01900-23 — Reversion)
- _Existing graph captures ecological framing (habitat enables trait) but lacks mechanistic depth; report identifies four convergent generic mechanistic modules (nutrient acquisition, motility, osmoadaptation, metabolic breadth) via 2023-2024 comparative genomics with broad cross-taxa support."_

### ecology/gut_associated  — *shallow* (2 edges)
- **Missing modules:** adhesion entry step, environmental filtering (bile/antimicrobials in proximal GI), oxygen homeostasis / niche shelter, bile acid metabolism regulatory loop
- `Adhesins —enables adhesion to→ intestinal mucus / epithelial receptors`  (DOI:10.3390/microorganisms12051026 (Lin 2024): 'adhesion is )
- `Adhesion to mucus/epithelium —prerequisite_for→ long-term gut colonization`  (DOI:10.3390/microorganisms12051026 (Lin 2024): 'adhesion → g)
- `Small-intestinal bile salts and Paneth-cell antimicrobials —inhibits growth of→ many bacteria in small intestine`  (DOI:10.1016/j.chom.2024.05.011 (Muramatsu & Winter 2024): pr)
- `Homeostatic limitation of oxygen diffusion into colonic lumen —shelters→ community dominated by primary fermenters`  (DOI:10.1128/iai.00302-24 (Lee 2024): distinguishes healthy g)
- `Bile acid-altering enzymes (bshA, bshB, hsdhA) —alters→ gut bile acid pool`  (DOI:10.1128/spectrum.03576-23 (McMillan 2024): strong enzyme)
- `Peristalsis and proximal-GI antimicrobials —contributes to→ low colonization / retention in duodenum and proximal small intestine`  (DOI:10.3390/microorganisms12051026 (Lin 2024): habitat bound)
- _Existing graph captures trait-to-host metabolic outcome but misses foundational generic mechanisms of colonization (adhesion, environmental filters, redox/oxygen niches, bile metabolism) that are emphasized across multiple 2024 reviews as universal drivers of gut-associated persistence._

### ecology/human_pathogen  — *shallow* (4 edges)
- **Missing modules:** adhesion/attachment entry step, secretion systems (T3SS/T4SS) as virulence platforms, nutrient acquisition (host-specific metal/heme scavenging), genome plasticity and HGT-mediated virulence acquisition, within-host evolution and hypermutation enabling persistence
- `bacterial adhesins —enables→ host epithelial colonization`  (DOI:10.1093/femsre/fuae019 (barber2024mechanismsofhost pages)
- `type III/IV secretion systems —enables→ host cell manipulation via effector translocation`  (DOI:10.1093/femsre/fuae019 & DOI:10.1038/s41579-023-00974-3 )
- `host-adapted nutrient acquisition receptors —enables→ scavenging of host-specific nutrients (metal/heme)`  (DOI:10.1093/femsre/fuae019 (barber2024mechanismsofhost pages)
- `mobile genetic elements (transposons, IS elements, phages) —enables→ horizontal gene transfer of virulence genes`  (DOI:10.1093/femsre/fuae019 (barber2024mechanismsofhost pages)
- `surface modifications (e.g., dltB pathway) —enables→ antimicrobial peptide resistance and immune evasion`  (DOI:10.1093/femsre/fuae019 (barber2024mechanismsofhost pages)
- `within-host mutation and hypermutation —enables→ genetic diversity for adaptation and chronic infection`  (DOI:10.1146/annurev-pathmechdis-051122-111408 (dekker2024wit)
- _Existing graph captures virulence-factors-to-disease backbone but omits five major generic mechanistic modules (adhesion entry, secretion systems, nutrient acquisition, genome plasticity/HGT, within-host evolution) that report identifies as broadly-supported and non-taxon-specific._

### ecology/opportunistic_pathogen  — *shallow* (2 edges)
- **Missing modules:** barrier breach and epithelial integrity, dysbiosis and microbial overgrowth, adhesion and invasion cascade, secreted enzymes and tissue damage, iron/nutrient limitation sensing and acquisition, biofilm formation and persistence
- `barrier breach / epithelial disruption —enables→ infection by opportunists`  (Uberoi 2024 (10.1038/s41579-024-01035-z): barrier breach exp)
- `antimicrobial dysbiosis —increases→ colonization by opportunistic commensals`  (Jacobsen 2023 (10.1007/s40588-023-00190-w), Jensen 2024 (10.)
- `adhesion to epithelium —enables→ invasion of host tissue`  (Jacobsen 2023 (10.1007/s40588-023-00190-w): adhesion as prer)
- `secreted degradative enzymes —causes→ host tissue damage`  (Pfeilmeier 2024 (10.1038/s41564-023-01555-z): T2SS-secreted )
- `nutritional immunity / iron limitation —triggers→ microbial iron acquisition systems`  (Sánchez-Jiménez 2023 (10.1111/1751-7915.14241): under iron l)
- `biofilm formation —promotes→ pathogenic persistence and infection`  (Sangiorgio 2024 (10.3390/pathogens13050409), Uberoi 2024 (10)
- _Existing graph captures the definitional frame (compromised defense → disease) but lacks mechanistic depth; missing >=4 major generic pathways (barrier/dysbiosis/adhesion-invasion/nutrient sensing/biofilm) that differentiate opportunistic pathogenesis from binary host-pathogen models._

### ecology/pathogenic_to_host  — *shallow* (4 edges)
- **Missing modules:** quorum sensing regulation of virulence and biofilm, metabolic state coupling to virulence gene expression, biofilm formation and persistence, immune evasion via capsule and complement antagonism, horizontal gene transfer of virulence determinants
- `quorum sensing —activates→ virulence gene expression`  (10.3390/ijms25052655 (Juszczuk-Kubiak 2024))
- `quorum sensing —enables→ biofilm formation and maturation`  (10.3390/antibiotics13070619 (D'Aquila 2024))
- `biofilm extracellular matrix —provides→ antibiotic tolerance and immune evasion`  (10.3390/bacteria3030008 (Erkihun 2024))
- `horizontal gene transfer —enables→ acquisition of virulence determinants`  (10.1093/femsre/fuae019 (Barber & Fitzgerald 2024))
- `capsule —resists→ phagocytosis`  (10.58532/nbennurmmch1 (Pandey 2024))
- `bacterial surface protein variant —modulates→ host receptor binding affinity`  (10.1093/femsre/fuae019 (Barber & Fitzgerald 2024))
- _The existing graph captures the central secretion-colonization-damage axis but omits generic regulatory (QS, metabolic coupling), persistence (biofilm), and immune-evasion modules that the report identifies as broadly applicable across pathogens._

### ecology/rhizosphere_association  — *shallow* (2 edges)
- **Missing modules:** chemotaxis-flagellum system (MCP-CheA/CheW/CheY-flagella cascade), biofilm formation pathway, exudate-chemotaxis coupling
- `methyl-accepting chemotaxis protein —positively_regulates→ bacterial chemotaxis`  (10.3389/fpls.2024.1491495 (yang2024mechanismsofrhizosphere) )
- `bacterial chemotaxis —enables→ rhizosphere association`  (10.3390/biology13020095 (chen2024thefunctionof pages 3-4) - )
- `CheA/CheW/CheY signaling —positively_regulates→ flagellum-dependent cell motility`  (10.3389/fpls.2024.1491495 (yang2024mechanismsofrhizosphere p)
- `flagellum-dependent cell motility —positively_regulates→ rhizosphere association`  (10.1093/femsre/fuad066 (liu2024rootcolonizationby pages 2-3))
- `root exudates —positively_regulates→ biofilm formation`  (10.3389/fpls.2024.1491495 (yang2024mechanismsofrhizosphere p)
- `biofilm formation —positively_regulates→ rhizosphere association`  (10.3390/biology13020095 (chen2024thefunctionof pages 3-4) - )
- _Existing graph captures only habitat-level ecology; is missing core generic microbial machinery (chemotaxis cascade, biofilm formation) that are well-supported across multiple 2023-2024 reviews and would strengthen trait grounding._

### environment/aerobic  — *shallow* (4 edges)
- **Missing modules:** ETC electron transfer (dehydrogenases to quinone pool), terminal oxidase mechanism (quinol oxidation), PMF generation, ATP synthesis (energy conservation), ROS generation and detoxification, oxygen-sensitive enzyme inactivation (negative constraint)
- `aerobic_respiration —transfers electrons through→ quinone pool`  (Electrons are transferred from substrate-specific dehydrogen)
- `terminal_oxidases —oxidize→ quinol and reduce O2 to H2O`  (Quinol-to-O2 oxidation is catalyzed by quinol oxidases (bo3,)
- `terminal_oxidases —generate→ proton motive force`  (Terminal oxidases catalyze four-electron reduction of O2 to )
- `proton_motive_force —powers→ ATP synthesis`  (The transmembrane electrochemical gradient powers the membra)
- `aerobic_respiration —generates→ ROS (superoxide and H2O2)`  (ROS are formed endogenously during aerobic respiration due t)
- `molecular_oxygen —inactivates→ oxygen-sensitive enzymes (Fe-S clusters in fumarase, aconitase; pyruvate formate-lyase)`  (Even low levels of O2 inactivate PFL in seconds)
- _Existing graph captures oxygen-dependent respiration core but omits energy conservation (PMF→ATP), oxidative stress management (ROS generation and detoxification), and negative constraints; report emphasizes generic ETC structure, branched terminal oxidases, and obligate ROS detoxification as trait hallmarks._

### environment/aerotolerant  — *shallow* (4 edges)
- **Missing modules:** O2-scavenging/O2-reduction enzymes (flavodiiron proteins, rubrerythrins, Roo/NorV), catalase H2O2 detoxification, regulatory gating (sigma factors, redox-responsive repressors), protein repair and iron-sequestration systems
- `molecular_oxygen —is_consumed_by→ flavodiiron_protein`  (DOI:10.1128/mbio.01591-24 — FdpA and FdpF enable tolerance a)
- `catalase —mitigates→ hydrogen_peroxide`  (DOI:10.1038/s43705-023-00251-7 — Catalase degrades H2O2 rapi)
- `reactive_oxygen_species —is_detoxified_by→ peroxidase`  (DOI:10.3389/fmicb.2023.1253114 — Cytochrome c peroxidase (Ma)
- `molecular_oxygen —is_reduced_by→ rubredoxin_oxygen_oxidoreductase`  (DOI:10.1186/s40168-024-01909-7 — Roo/NorV and cytochrome bd )
- `oxidative_stress_response —is_regulated_by→ sigma_factor_B`  (DOI:10.1128/mbio.01591-24 — σB controls O2-reductase gene ex)
- `hydrogen_peroxide —is_detoxified_by→ peroxiredoxin`  (DOI:10.1038/s43705-023-00251-7 — Peroxiredoxins identified a)
- _The existing graph captures ROS detoxification (SOD) but misses the equally critical O2-reduction module and catalase detoxification; both modules are documented as generic across disparate anaerobic taxa (C. difficile, anammox, SRB, Geobacter) and should be integrated for an adequate representation of mechanistic aerotolerance."_

### environment/alkaphilic  — *shallow* (5 edges)
- **Missing modules:** ATP synthase c-subunit adaptation for high-pH proton binding, K+ uptake and intracellular K+ accumulation, Na+/solute symporter-mediated Na+ cycling, Membrane potential maintenance via K+ regulation, Surface proton retention via acidic cell envelope
- `ATP synthase c-subunit alkaline-adaptive motifs —increases→ proton binding affinity at high pH`  (10.1038/nrmicro2549 — foundational Krulwich 2011 Nat Rev Mic)
- `Na+/solute symporters —supplies→ cytoplasmic sodium for Na+/H+ antiporter cycling`  (10.1038/nrmicro2549 — Krulwich et al. identify Na+/solute sy)
- `TrkAH K+ uptake system —increases→ intracellular K+ concentration`  (10.1128/aem.00145-24 — Xing et al. 2024 provide quantitative)
- `intracellular K+ accumulation —supports→ membrane potential and ion homeostasis`  (10.1128/aem.00145-24 — Xing et al. measure coupled Δψ = −124)
- `acidic S-layer and cell-wall proteins —retains→ protons at cell surface for bioenergetic compensation`  (10.3389/fmicb.2022.842785 — Goto et al. 2022 identify acidic)
- `ectoine biosynthesis —supports→ osmotic and haloalkaline adaptation`  (10.3389/fmicb.2023.1233691 — Khomyakova et al. 2023 identify)
- _Existing graph captures the core Na+/H+ antiporter-mediated pH homeostasis principle but lacks bioenergetic compensation mechanisms (ATP synthase adaptation, K+ regulation, surface proton retention) and Na+ entry pathways (symporters) that are generic, well-supported, and present across diverse alkaliphile lineages in the research literature._

### environment/arsenic_tolerant  — *shallow* (3 edges)
- **Missing modules:** arsenate reduction (ArsC), ars operon transcriptional regulation (ArsR), arsenate uptake (Pit/Pst), arsenite uptake (GlpF), alternative efflux pump (Acr3), ArsA/ArsD ATP energization and chaperoning, arsenic methylation (ArsM)
- `arsC —reduces→ arsenate`  (DOI:10.3390/antibiotics12091474)
- `arsR —represses→ ars_promoter`  (DOI:10.3390/antibiotics12091474)
- `arsenite —relieves_repression_of→ ars_operon_transcription`  (DOI:10.3389/fmicb.2024.1494872)
- `pit_pst_transporters —imports→ arsenate`  (DOI:10.3390/antibiotics12091474)
- `glpf —imports→ arsenite`  (DOI:10.3390/antibiotics12091474)
- `acr3 —exports→ arsenite`  (DOI:10.3390/microorganisms12010074)
- _Existing graph captures only ars operon efflux backbone but omits ArsC reduction, ArsR regulation, arsenate as distinct substrate, and uptake routes — missing >=2 core generic modules that are well-supported by recent reviews and unambiguously part of canonical arsenic tolerance mechanism._

### environment/copper_tolerant  — *shallow* (3 edges)
- **Missing modules:** periplasmic copper oxidation (multicopper oxidases), transenvelope efflux system (CusCBA), metallochaperone copper delivery, sensory/regulatory network (CueR, CusRS), extracellular copper sequestration (EPS)
- `cytoplasmic copper(1+) —exported_by→ P1B-ATPase (CopA/CupA)`  (DOI:10.1128/aem.00567-23)
- `periplasmic copper(1+) —oxidized_to_less_toxic_form_by→ multicopper oxidase (CueO/CopA/PcoA)`  (DOI:10.3390/antibiotics12091474)
- `periplasmic copper(1+) —exported_by→ RND transenvelope complex (CusCBA)`  (DOI:10.1128/aem.00567-23)
- `periplasmic copper —sensed_by→ CusS sensor histidine kinase`  (DOI:10.1128/spectrum.00291-23)
- `CusS/CusR signal —activates→ cusCFBA transporter operon`  (DOI:10.1128/spectrum.00291-23)
- `copper exposure —induces_synthesis_of→ extracellular polymeric substances (EPS)`  (DOI:10.3389/fmicb.2024.1390451)
- _Existing graph captures initial efflux step but omits periplasmic oxidation, transenvelope export, metallochaperone delivery, regulatory sensing (CusS/CueR), and EPS sequestration—all generic, well-supported mechanisms in the literature."_

### environment/delta_phenotype_with_numerical_limits  — *shallow* (4 edges)
- **Missing modules:** homeoviscous adaptation (lipidome remodeling), compatible solute biosynthesis and accumulation, stress protein regulatory networks (sigma factors, chaperones, proteases), antioxidant defense and redox management, transcriptomic buffering of core metabolism, energy metabolism rewiring (anaerobic respiration, fermentation)
- `homeoviscous adaptation —maintains→ membrane fluidity across temperature and osmotic stress`  (DOI:10.1039/d4cc03114h (Maiti et al. 2024): 'HVA involves re)
- `compatible solute accumulation —stabilizes→ proteins and membranes under cold and osmotic stress`  (DOI:10.37256/amtt.5220244537 (Purwar & Srivastava 2024): tre)
- `membrane lipid remodeling —prevents→ fluid-to-gel phase transition`  (DOI:10.1039/d4cc03114h (Maiti et al. 2024): enrichment of MU)
- `RpoH and RpoE sigma factors —induce→ heat-shock and envelope-protection gene programs`  (DOI:10.1007/s12275-023-00031-x (Moon et al. 2023): 'RpoH ind)
- `antioxidant defenses (SOD, catalase) —mitigate→ reactive oxygen species under high pressure and multiple stresses`  (DOI:10.1128/aem.01304-22 (Li et al. 2023): 'antioxidant defe)
- `transcriptomic regulatory rewiring —maintains→ core metabolite pools across wide temperature range`  (DOI:10.1128/msystems.01124-22 (Riccardi et al. 2023): 'broad)
- _Existing graph captures only structural taxonomy (environmental axis definition, trait hierarchy); lacks mechanistic substrate. Report identifies 6+ generic, well-supported modules (HVA, osmolytes, stress-response networks, antioxidant defense, metabolic buffering, energy rewiring) absent from existing graph; these are broadly applicable across taxa and parameters, not strain/assay-specific."_

### environment/desiccation_tolerant  — *shallow* (3 edges)
- **Missing modules:** oxidative stress defense, trehalose/compatible solutes pathway, heat shock protein proteostasis, desiccation priming/acclimation, LEA/CAHS + cosolute synergy
- `Desiccation (ENVO:desiccation) —causes→ Oxidative stress / ROS (GO:0006979)`  (10.1021/acs.chemrev.2c00659, 2023 — Low hydration below wate)
- `Trehalose (CHEBI:16551) —stabilizes→ Plasma membrane integrity (GO:0005886)`  (10.1007/s00203-023-03683-w, 2023 — Trehalose interacts with )
- `Heat shock proteins / chaperone activity (GO:0051082) —negatively_regulates→ Protein aggregation / denaturation (GO:0035966)`  (10.1007/s00203-023-03683-w, 2023 — HSPs bind denatured prote)
- `Superoxide dismutase activity (GO:0004784) —negatively_regulates→ Reactive oxygen species level (GO:1903409)`  (10.1021/acs.chemrev.2c00659, 2023 — SOD upregulation is cons)
- `Desiccation priming / acclimation (label) —positively_regulates→ Desiccation survival (traitmech:000010)`  (10.1021/acs.chemrev.2c00659, 2023 — Priming/acclimation is o)
- `LEA/CAHS intrinsically disordered proteins (label) —synergizes_with→ Trehalose / compatible solutes (CHEBI:16551)`  (10.7554/eLife.97231, 2024 — Desiccation-related IDPs synergi)
- _Existing graph captures anhydrobiosis framework and DNA repair but omits conserved stress-response and molecular-protection modules identified as critical in expert Chemical Reviews synthesis; expert consensus stresses desiccation tolerance is a systems phenotype requiring both classical stress responses (antioxidants/chaperones) and cytoplasmic materials strategies (vitrification/gels)._

### environment/extreme_hyperthermophilic  — *shallow* (4 edges)
- **Missing modules:** DNA topology protection via reverse gyrase and positive supercoiling, Temperature-dependent GDGT remodeling and cyclization
- `reverse gyrase —introduces positive supercoils into→ DNA positive supercoiling`  (DOI:10.1264/jsme2.me23087 (Takemata 2024))
- `DNA positive supercoiling —decreases risk of→ DNA thermal denaturation`  (DOI:10.1264/jsme2.me23087 (Takemata 2024))
- `very high temperature —increases proportion of→ membrane-spanning GDGTs`  (DOI:10.1007/s00792-023-01330-2 (Rao & Driessen 2024))
- `GrsA/GrsB cyclization enzymes —increase→ membrane packing and stability`  (DOI:10.1007/s00792-023-01330-2 (Rao & Driessen 2024))
- `thermosome chaperonin complex —enables→ protein folding at extreme temperature`  (DOI:10.1186/2046-0481-57-6-348 (Irwin & Baird 2004))
- `reverse gyrase knockout —causes loss of growth at→ 95-100°C temperature`  (DOI:10.1007/s00792-017-0929-z (Lipscomb et al. 2017))
- _Existing graph captures generic membrane lipid and bioenergetics roles but overlooks hallmark DNA topology protection (reverse gyrase) and temperature-dependent lipid remodeling mechanisms documented in 2024 reviews and primary literature."_

### environment/facultative_psychrophilic  — *shallow* (5 edges)
- **Missing modules:** two-component cold-sensing system, fatty acid desaturase enzyme activity, exopolysaccharide (EPS) cryoprotection, compatible solute transport and osmoprotectant accumulation, trehalose and glycogen metabolism pathways
- `low_temperature —induces→ two_component_system`  (DOI:10.1007/s42770-023-01057-4 - membrane physical-state sen)
- `low_temperature —upregulates→ fatty_acid_desaturase`  (DOI:10.37256/amtt.5220244537 - genes for fatty acid desatura)
- `fatty_acid_desaturase —increases→ unsaturated_fatty_acids`  (DOI:10.1016/B978-0-12-809633-8.02282-2 - desaturase increase)
- `exopolysaccharides —protects_against→ freeze_thaw_damage`  (DOI:10.37256/amtt.5220244537 - EPS provides protection again)
- `compatible_solute_transport —imports→ glycine_betaine`  (DOI:10.3389/fmicb.2023.1197797 - accumulation of glycine bet)
- `trehalose_metabolism —supports→ low_temperature_survival`  (DOI:10.1038/s41598-023-41323-x - trehalose biosynthesis path)
- _Existing graph captures trait phenotype and membrane fluidity core, but lacks 5 major generic mechanisms: cold-sensing regulation, desaturase enzyme, EPS cryoprotection, compatible solute system, and carbohydrate metabolism pathways — all high-certainty in report._

### environment/facultatively_acidophilic  — *shallow* (6 edges)
- **Missing modules:** inside-positive membrane potential via potassium accumulation, hopanoid and membrane composition adaptation (first-line passive defense), specific proton antiporters (NhaA, Mrp, ClcA), proton-consuming decarboxylase pathways (Gad, SpeA, urease)
- `potassium ions —generate→ internal positive membrane potential`  (DOI:10.3389/fmicb.2021.822229)
- `Kdp potassium uptake system —supports→ acid tolerance`  (DOI:10.3389/fmicb.2023.1149903)
- `hopanoid biosynthesis —reduces→ membrane proton permeability`  (DOI:10.3389/fmicb.2021.822229)
- `NhaA sodium/proton antiporter —exports→ excess intracellular protons`  (DOI:10.13343/j.cnki.wsxb.20230336)
- `glutamate decarboxylase system —consumes→ intracellular protons`  (DOI:10.3389/fmicb.2021.822229)
- `urease system —neutralizes→ intracellular acid stress`  (DOI:10.3389/fmicb.2023.1149903)
- _Existing graph captures trait-homeostasis backbone but misses >=2 generic mechanistic layers (membrane defense, specific antiporters, and metabolic proton-consuming pathways) that are consistently supported across multiple 2020-2024 sources and reused across diverse acidophilic taxa._

### environment/facultatively_alkaphilic  — *shallow* (6 edges)
- **Missing modules:** Mrp multi-subunit antiporter complex, membrane electrical potential (ΔΨ), proton motive force, F1Fo-ATP synthase energy coupling, cell-envelope acidity/buffering (acidic polymers/S-layers), NhaC antiporter family module, sodium availability as environmental factor
- `Mrp Na+/H+ antiporter complex (mrpABCDEFG) —enables→ facultatively alkaphilic growth`  (10.3389/fbioe.2015.00075 - essential for electrogenic antipo)
- `Na+/H+ antiport activity —maintains→ cytoplasmic pH homeostasis`  (10.1007/978-981-19-1573-4_3 - antiport keeps cytoplasm 2-2.3)
- `acidic cell-wall polymers (teichuronic acid) —buffers→ cell surface microenvironment`  (10.1007/978-981-19-1573-4_3 - anionic polymers help maintain)
- `high membrane potential (ΔΨ) —increases→ ATP synthase driving force`  (10.3389/fmicb.2018.02331 - elevated ΔΨ enhances driving forc)
- `F1Fo-ATP synthase —enables→ ATP production at alkaline pH`  (10.3389/fbioe.2015.00075 - alkaliphiles use proton-coupled A)
- `sodium availability —enables→ cytoplasmic pH below 9 at external pH 10.5`  (10.1007/978-981-19-1573-4_3 - without Na+, internal pH rose )
- _Existing graph captures only sodium-cycle and cytoplasmic pH homeostasis backbone; report documents rich multi-module mechanism (Mrp complex, membrane potential, ATP synthesis coupling, cell-envelope acidity, NhaC family) with strong generic and 2023-2024 evidence lacking in current graph._

### environment/haloalkaliphilic  — *shallow* (6 edges)
- **Missing modules:** salt-in (K+ accumulation) strategy, Na+/H+ antiporter (Na+ efflux and pH regulation), compatible-solute biosynthesis pathways (ectoine, glycine betaine), K+ uptake systems (Trk/Ktr), intracellular Na+ homeostasis mechanism
- `high_salt_environment —enables→ salt-in_strategy`  (DOI:10.1128/aem.00145-24)
- `salt-in_strategy —involves→ K_plus_accumulation`  (DOI:10.1128/aem.00145-24 - intracellular K+ increases (227.2)
- `high_salt_environment —contributes to→ intracellular_Na_plus_stress`  (DOI:10.1128/aem.00145-24)
- `Na_plus_H_plus_antiporter —enables→ intracellular_Na_homeostasis`  (DOI:10.1128/aem.00145-24 - Na+/H+ antiporters (nhaA/B/C) mai)
- `compatible-solute_strategy —involves→ glycine_betaine_biosynthesis`  (DOI:10.3389/fmicb.2025.1550346)
- `high_salt_environment —induces→ compatible-solute_biosynthesis`  (DOI:10.1128/aem.00145-24)
- _The existing graph has backbone structure but lacks 5+ generic mechanistic modules (salt-in strategy, Na+/H+ antiporters, ion homeostasis details, biosynthesis pathways) that are well-supported across the recent literature; upgrading would capture the dual osmoadaptation mechanisms central to the trait._

### environment/mesophilic  — *shallow* (4 edges)
- **Missing modules:** heat-shock sigma factor (σ32/RpoH) regulatory cascade, cold-shock protein (CspA) induction and function, chaperone-mediated negative regulation of heat-shock response (DnaK), trehalose biosynthesis and membrane/protein stabilization
- `temperature stress —induces→ sigma32 RpoH expression`  (Moon 2023, DOI:10.1007/s12275-023-00031-x)
- `sigma32 RpoH —activates transcription of→ heat shock genes`  (Moon 2023, DOI:10.1007/s12275-023-00031-x)
- `DnaK chaperone —negatively regulates via sequestration→ sigma32 RpoH`  (Moon 2023, DOI:10.1007/s12275-023-00031-x)
- `cold shock —induces→ CspA cold shock protein`  (Moon 2023, DOI:10.1007/s12275-023-00031-x)
- `CspA —promotes→ translation under cold stress`  (Moon 2023, DOI:10.1007/s12275-023-00031-x)
- `RpoS sigma S —activates transcription of→ trehalose biosynthesis genes otsAB`  (Moon 2023, DOI:10.1007/s12275-023-00031-x)
- _Existing graph captures homoviscous adaptation backbone but lacks heat-shock/cold-shock regulatory cascades and trehalose protection; all suggested edges are generic, broadly-applicable mechanisms excluding taxon-specific (DesK/DesR), species-specific (cis-vaccenic), and assay-specific (denitrification ABC transporter) edges from the report."_

### environment/metal_tolerant  — *shallow* (3 edges)
- **Missing modules:** metal-sensing regulation (two-component systems), enzymatic detoxification/redox transformation, metal sequestration/buffering
- `metal_sensing_two_component_system —enables→ efflux_pump_expression`  (10.1128/spectrum.00291-23)
- `detoxification_enzyme —enables→ metal_detoxification_process`  (10.1128/aem.00567-23)
- `metal_detoxification_process —enables→ metal_tolerant_trait`  (10.1128/aem.00567-23)
- `metal_sequestration_molecule —modulates→ intracellular_metal_pool`  (10.1128/jb.00080-24)
- `periplasmic_metal_pool —challenges→ metal_tolerant_trait`  (10.1128/spectrum.00291-23)
- `metal_stressor —activates→ metal_sensing_two_component_system`  (10.1128/spectrum.00291-23)
- _Existing graph captures efflux export pathway but omits three major generic mechanistic modules (regulation, detoxification, sequestration) that the 2023–2024 literature emphasizes as integrated, interdependent contributors to metal tolerance across diverse taxa."_

### environment/moderately_halophilic  — *shallow* (5 edges)
- **Missing modules:** ectoine biosynthesis pathway (ectABC genes + precursor supply), glycine betaine biosynthesis (BetA/BetB from choline), ectoine hydroxylation to hydroxyectoine (EctD), compatible-solute transporter families (ProU, BCCT, TeaABC), oxidative stress co-response, ion homeostasis (Na+/K+ early-phase uptake)
- `NaCl salinity —causes→ oxidative stress`  (10.1186/s12934-024-02358-5 (Yu 2024): NaCl shock induces osm)
- `aspartate —serves as precursor for→ ectoine biosynthetic process`  (10.1186/s12934-021-01567-6 (Liu 2021): aspartate feeds ectoi)
- `ectoine biosynthetic process —produces→ ectoine`  (10.1128/AEM.01195-24 (Khanh 2024): ectABC-encoded enzymes ca)
- `ectoine —can be converted to→ 5-hydroxyectoine`  (10.1186/s12934-021-01567-6 (Liu 2021): EctD hydroxylase tran)
- `ProU ABC transporter —imports→ glycine betaine`  (10.58088/07hg-r941 (Lichty 2024): ProU family mediates high-)
- `TeaABC TRAP transporter —imports→ ectoine`  (10.58088/07hg-r941 (Lichty 2024): TeaABC/UehABC TRAP system )
- _Existing graph captures trait-level osmoadaptation logic but lacks GENERIC biosynthetic, transport, and co-stress modules documented in the report; high-priority enrichment recommended to enable mechanistic reasoning about osmolyte synthesis/import control and oxidative defense coupling._

### environment/nacl_delta_high  — *shallow* (2 edges)
- **Missing modules:** compatible-solute uptake and biosynthesis (glycine betaine, proline, ectoine), K+ accumulation via TrkH and related transporters (salt-in strategy), Na+/H+ antiporter-mediated ion homeostasis (NhaC), acidic proteome / low pI adaptation signature, environmental high-salinity driving force
- `high external salinity —increases→ compatible-solute accumulation`  (10.1128/aem.00145-24)
- `glycine betaine ABC transporters (Opu/ProU) —enables→ adaptation to high salinity`  (10.1128/aem.00145-24)
- `TrkH potassium uptake system —increases intracellular→ K+`  (10.1128/aem.00145-24)
- `intracellular K+ accumulation —supports→ salt-in osmoadaptation`  (10.1128/aem.00145-24)
- `nhaC Na+/H+ antiporter upregulation —facilitates→ Na+ homeostasis at high salinity`  (10.1128/aem.00145-24)
- `salt-in strategy —associated with→ acidic proteome / low pI proteome`  (10.1038/s41559-024-02505-6)
- _Existing graph is a single 2-edge scaffold; report describes rich generic dual-strategy mechanism (compatible solutes + K+ accumulation + transporter machinery + proteome remodeling) across multiple taxa with strong 2023-2024 evidence, but graph captures none of this mechanistic depth._

### environment/nacl_delta_low  — *shallow* (2 edges)
- **Missing modules:** osmolyte biosynthesis pathways (ectoine, proline, GABA), compatible-solute transporter systems, ion homeostasis (K+/Na+ transport), osmoadaptation regulatory network
- `ectoine biosynthesis —supports→ NaCl delta phenotype breadth`  (DOI:10.1128/aem.01905-23)
- `compatible-solute uptake systems (OpuA/ProU) —supports→ NaCl delta phenotype breadth`  (DOI:10.1128/aem.00145-24 — Proteomics across salinity steps )
- `potassium ion transport (TrkH) —supports→ osmoadaptation`  (DOI:10.1128/aem.00145-24 — TrkH upregulation across salinity)
- `sodium ion export (NhaC antiporters) —supports→ osmoadaptation`  (DOI:10.1128/aem.00145-24 — NhaC-family Na+/H+ antiporters sh)
- `osmoadaptation —requires→ compatible solute accumulation`  (DOI:10.1128/aem.01905-23)
- `limited osmoadaptive flexibility —manifests as→ stenohaline organism phenotype`  (DOI:10.4490/algae.2023.38.6.12 — Geminocystis urbisnovae exh)
- _Existing graph captures the top-level concept (osmoadaptation → phenotype) but lacks mechanistic depth; key osmolyte biosynthesis/uptake, ion-transport, and regulatory edges are supported by 2023–2024 causal evidence (knockouts, rescues, omics) and are curatable as generic, non-taxon-specific mechanism._

### environment/nacl_delta_mid1  — *shallow* (2 edges)
- **Missing modules:** K+ uptake systems (Trk/Ktr), compatible solute accumulation mechanism (glycine betaine, trehalose, ectoine), c-di-AMP regulatory control, mechanosensitive channels (MscL/MscS)
- `osmotic upshift —induces→ potassium import`  (DOI:10.1128/MMBR.00181-23)
- `potassium ion —is replaced by→ compatible solute accumulation`  (DOI:10.1128/MMBR.00181-23)
- `cyclic di-AMP —regulates→ potassium homeostasis`  (DOI:10.1128/MMBR.00181-23)
- `cyclic di-AMP —regulates→ OpuA compatible solute transporter`  (DOI:10.1128/MMBR.00181-23)
- `compatible solute accumulation —supports→ osmoadaptation under NaCl stress`  (DOI:10.1093/femsre/fuaf020)
- `Trk potassium uptake system —mediates→ potassium accumulation after osmotic upshift`  (DOI:10.1093/femsre/fuaf020)
- _Existing graph is a vague umbrella node; report details four generic mechanistic modules (K+ uptake, solute replacement, c-di-AMP regulation, mechanosensitive relief) supported by 2024 reviews and taxon-independent evidence."_

### environment/nacl_delta  — *shallow* (3 edges)
- **Missing modules:** ion homeostasis (Na+/H+ antiporters, K+ uptake systems), compatible solute biosynthesis and accumulation (glycine betaine, ectoine, trehalose), c-di-AMP regulatory control of ion transport, mechanosensitive channels (safety valves for osmotic shock)
- `hyperosmotic_stress —causes→ K_plus_uptake`  (DOI:10.1128/MMBR.00181-23 — cells rapidly import large amoun)
- `K_plus_uptake —enables→ osmoadaptive_flexibility`  (DOI:10.1128/MMBR.00181-23 — quantitative evidence shows cyto)
- `compatible_solute_accumulation —enables→ osmoadaptive_flexibility`  (DOI:10.1128/MMBR.00181-23 — compatible solutes (glycine beta)
- `c_di_AMP —regulates→ K_plus_uptake`  (DOI:10.1128/MMBR.00181-23 — c-di-AMP acts as master regulato)
- `Na_plus_H_plus_antiporters —enables→ osmoadaptive_flexibility`  (DOI:10.3390/biology13060404 — Na+ export via antiporters (e.)
- `salt_out_strategy —produces→ broad_NaCl_tolerance_range`  (DOI:10.3390/microorganisms12081738 — compatible-solute strat)
- _Existing graph has the macro-pathway backbone but lacks meso-level mechanistic modules (ion regulation, compatible solute synthesis, c-di-AMP control, mechanosensitive channels) that the report extensively documents as generic, well-supported mechanisms of NaCl-delta breadth across diverse bacteria."_

### environment/nacl_optimum_high  — *shallow* (3 edges)
- **Missing modules:** intracellular KCl accumulation (ion homeostasis), potassium uptake system (K+ transport), Na+/H+ antiporter (Na+ exclusion), bioenergetic coupling (bacteriorhodopsin, proton motive force), acidic proteome adaptation (amino acid composition, protein solubility)
- `salt-in osmoadaptation strategy —increases→ intracellular KCl concentration`  (DOI:10.1002/pro.5003 (Herrero-Alfonso 2024))
- `intracellular high KCl —selects for→ acidic proteome`  (DOI:10.1093/femsre/fuy026 (Lee 2018))
- `acidic proteome —enables→ protein function at high salinity`  (DOI:10.1038/s41559-024-02505-6 (Gutiérrez-Preciado 2024))
- `Na+/H+ antiporter activity —supports→ salt-in osmoadaptation strategy`  (DOI:10.3390/microorganisms12081738 (Bonnaud 2024))
- `bacteriorhodopsin proton pump —generates→ proton motive force`  (DOI:10.3390/microorganisms12081738 (Bonnaud 2024))
- `proton motive force —powers→ Na+/H+ antiporter activity`  (DOI:10.3390/microorganisms12081738 (Bonnaud 2024))
- _Existing graph captures environmental selection and phenotypic output but omits the 5 major generic mechanistic modules (ion homeostasis, K+ transport, Na+ antiport, bioenergetics, proteome adaptation) that 2023-2024 reviews identify as core to extreme-halophile physiology._

### environment/neutrophilic  — *shallow* (4 edges)
- **Missing modules:** cytoplasmic buffering capacity, amino-acid decarboxylation systems (GAD/ADI/CAD), F1F0-ATPase proton pumps, metabolic proton efflux coupling to antiporters
- `cytoplasmic buffering capacity —enables→ cytoplasmic pH homeostasis`  (Proton sequestration by proteins, phosphates, polyamines dam)
- `external acidic pH —enables→ proton influx into cytoplasm`  (Low external pH increases H+ entry via multiple routes (perm)
- `amino-acid decarboxylation —enables→ proton consumption`  (Decarboxylation is enzyme-catalyzed and directly removes H+ )
- `proton efflux from central metabolism —enables→ proton-ion antiporter function`  (Metabolic proton export provides energy input to antiporters)
- `F1F0-ATPase —enables→ proton pumping against gradient`  (ATP-dependent proton transport helps restore cytoplasmic pH )
- `proton motive force strength —determines→ extracellular pH range for pHi homeostasis`  (PMF strength sets maximal rate of antiporter work and determ)
- _The existing neutrophilic graph captures external pH and pHi homeostasis but misses generic buffering, amino-acid decarboxylation systems, F1F0-ATPase pumps, and metabolic-to-antiporter coupling that the report identifies as broadly supported mechanisms._

### environment/ph_delta_high  — *shallow* (2 edges)
- **Missing modules:** Na+/H+ antiporter system, K+/H+ antiporter system, respiratory proton pumps, F0F1-ATPase, decarboxylation pathways (proton-consuming), cytoplasmic buffering capacity, membrane lipid/porin remodeling, proton motive force (PMF) stability, glutamate decarboxylase (Gad) system
- `Na+/H+ antiporters —contributes_to→ maximal pH-homeostasis flexibility`  (DOI:10.1093/femsre/fuad033)
- `K+/H+ antiporters —contributes_to→ maximal pH-homeostasis flexibility`  (DOI:10.1093/femsre/fuad033)
- `respiratory proton-pumping enzymes —helps_maintain→ maximal pH-homeostasis flexibility`  (DOI:10.1093/femsre/fuad033)
- `F0F1-ATPase —contributes_to→ maximal pH-homeostasis flexibility`  (DOI:10.1093/femsre/fuad033)
- `metabolite decarboxylation pathways —contributes_to→ maximal pH-homeostasis flexibility`  (DOI:10.1093/femsre/fuad033)
- `constant proton motive force (PMF) —enables→ pH delta high`  (DOI:10.1093/femsre/fuad033)
- _Existing graph captures only the abstract output (pH homeostasis → broad breadth) but entirely omits six core mechanistic modules (antiporters, pumps, decarboxylation, buffering, membrane remodeling, PMF stability) that Poolman 2023 and Krulwich 2011 identify as generic determinants of euryphilic breadth; enrichment is high-priority to expose functional modularity._

### environment/ph_delta_low  — *shallow* (2 edges)
- **Missing modules:** proton motive force (PMF) as mechanistic bottleneck, external pH stress as environmental driver, membrane proton permeability control, cytoplasmic pH regulation as intermediate state
- `external pH stress —challenges→ cytoplasmic pH homeostasis`  (DOI:10.1038/nrmicro2549)
- `proton motive force (PMF) architecture —constrains→ limited pH-homeostasis flexibility`  (DOI:10.1038/nrmicro2549)
- `membrane proton permeability —determines→ passive proton leak rate`  (DOI:10.3389/frbis.2023.1338019)
- `cytoplasmic pH homeostasis —maintains→ cytoplasmic pH within growth range`  (DOI:10.1038/nrmicro2549)
- `F1Fo-ATPase —contributes to→ proton efflux during acid stress`  (DOI:10.3390/microorganisms12091774)
- `envelope lipid composition —reduces→ membrane proton permeability`  (DOI:10.3389/fmicb.2022.1034164)
- _Existing graph captures trait taxonomy and high-level homeostasis constraint but lacks the mechanistic scaffolding (PMF, external pH stress, membrane permeability, transporter activity) that the report identifies as generic, broadly-applicable components of narrow pH-breadth mechanism; no taxon-specific edges wrongly included, but curation is incomplete at the generic module level."_

### environment/ph_delta_mid1  — *shallow* (2 edges)
- **Missing modules:** glutamate decarboxylase / Gad proton-consuming pathway, F0F1-ATPase ATP-driven proton export, YbaS glutaminase ammonia-neutralization, oxidative phosphorylation / electron-transport proton maintenance, urease ammonia-generation module, membrane lipid saturation / proton-permeability reduction
- `glutamate decarboxylase system (GadA/GadB/GadC) —enables→ survival/growth at low external pH`  (Li et al. 2024, doi:10.3390/microorganisms12091774, pages 2-)
- `F0F1-ATPase —consumes ATP to export H+→ cytoplasmic pH homeostasis under acid stress`  (Li et al. 2024, doi:10.3390/microorganisms12091774, pages 2-)
- `YbaS glutaminase —produces ammonia from glutamine→ intracellular proton neutralization`  (Li et al. 2024, doi:10.3390/microorganisms12091774, pages 2-)
- `oxidative phosphorylation / ETC genes (nuo, cyo, ndh, sdh) —maintains→ proton-motive force under mild acid stress`  (Qin et al. 2024, doi:10.3390/microorganisms12081565, pages 1)
- `urease pathway —produces ammonia→ pH neutralization`  (Ramoneda et al. 2023, doi:10.1126/sciadv.adf8998, pages 3-5)
- `increased saturated membrane fatty acids —reduce→ proton diffusion across membrane`  (Jiang et al. 2024, doi:10.1128/aem.00569-24, pages 1-2)
- _The existing graph captures high-level pH homeostasis concept but lacks mechanistic decomposition into acid-resistance pathways, proton-export systems, and metabolic modules that literature describes generically; six core generic mechanisms are unsupported in the current graph."_

### environment/ph_delta_mid2  — *shallow* (2 edges)
- **Missing modules:** external pH stress transduction, respiratory chain PMF generation, ATP synthase-mediated proton translocation, Na+/H+ antiporter alkaline tolerance, acid-resistance decarboxylase (GDAR) pathway
- `external pH stress —alters→ proton motive force (PMF) component balance`  (DOI:10.1038/nrmicro2549)
- `respiratory chain proton pumps —generate→ proton motive force`  (DOI:10.1038/nrmicro2549)
- `F1Fo ATP synthase activity —contributes to→ cytoplasmic pH homeostasis`  (DOI:10.1038/nrmicro2549, DOI:10.3390/antibiotics12091474)
- `Na+/H+ antiporter activity —supports→ alkaline pH homeostasis`  (DOI:10.1038/nrmicro2549)
- `glutamate decarboxylase system —consumes→ cytoplasmic H+`  (DOI:10.1038/nrmicro2549, DOI:10.3390/antibiotics12091474)
- `membrane lipid remodeling —reduces→ proton diffusion across membrane`  (DOI:10.1128/AEM.00569-24)
- _Existing graph is minimal (2 edges, high-level output only); report identifies 6+ generic mechanistic modules (bioenergetics, stress transduction, transporters, acid resistance) absent from current curation; high-priority enrichment to capture Krulwich-style integrated mechanistic architecture."_

### environment/ph_range_low  — *shallow* (2 edges)
- **Missing modules:** buffering systems (glutamate decarboxylase, arginine decarboxylase, lysine decarboxylase), cyclopropane fatty acid membrane adaptation, weak organic acid uncoupling (undissociated entry + intracellular dissociation), proton export pumps (P-type H+-ATPase, F0F1 ATPase), K+ uptake and inside-positive membrane potential
- `P-type H+-ATPase —exports→ H+`  (10.3390/microorganisms12030625 (S. cerevisiae) and 10.3389/f)
- `H+-ATPase activity —maintains→ intracellular pH homeostasis`  (10.3390/microorganisms12030625)
- `glutamate decarboxylase system (gadABC) —buffers→ cytoplasmic pH`  (10.3389/fmicb.2023.1149903 and 10.4014/jmb.2303.03009)
- `cyclopropane-fatty-acyl-phospholipid synthase (cfa) —decreases→ membrane proton permeability`  (10.4014/jmb.2303.03009 and 10.3389/fmicb.2023.1149903)
- `weak organic acids (undissociated) —diffuse_into→ cell`  (10.1111/1758-2229.70019)
- `intracellular dissociation of weak organic acids —lowers→ internal pH`  (10.1111/1758-2229.70019)
- _Existing graph captures the high-level enabling role of pH homeostasis but lacks explicit mechanistic detail on proton pumps, buffering systems, membrane adaptations, and weak-acid boundary conditions that define acidophile physiology at pH 4–6."_

### environment/ph_range_mid3  — *shallow* (2 edges)
- **Missing modules:** Mrp/NhaC Na+/H+ antiporter complex specifics, Na+-dependent ATP synthesis/bioenergetics adaptation, Compatible-solute transport and accumulation module, Cell envelope acidic polymer reinforcement
- `Mrp Na+/H+ antiporter complex —maintains→ intracellular pH homeostasis under alkaline stress`  (DOI:10.1038/s41467-022-33640-y (Lee 2022, cryo-EM + MD showi)
- `External Na+ availability —supports→ growth across pH 8-10 range`  (DOI:10.1007/s13205-021-02938-x (Krishna 2021, Alkalihalobaci)
- `NhaC-family Na+/H+ antiporter —increases→ alkaline pH tolerance`  (DOI:10.3390/ijms241310786 (Wang 2023, archaeal NhaC expressi)
- `Compatible-solute transport and accumulation —assists in→ maintaining near-neutral internal pH under alkaline stress`  (DOI:10.3389/fmicb.2023.1228266 (de Jong 2023, thermoalkaliph)
- `Na+-translocating F1Fo-ATPase —enables→ ATP synthesis under high alkaline pH with low external proton availability`  (DOI:10.1128/AEM.00145-24 (Xing 2024, Natranaerobius thermoph)
- `Teichuronic acid and acidic cell-wall polymers —contribute to→ alkaline pH tolerance through OH- repulsion and cation binding`  (DOI:10.1007/s13205-021-02938-x (Krishna 2021, comparative ge)
- _The existing graph captures generic pH homeostasis but lacks specificity on molecular actors (Mrp/NhaC antiporters), bioenergetic adaptations (Na+-coupled ATP synthase), osmoadaptation (compatible solutes), and structural reinforcement (acidic cell-wall polymers) — all well-supported generic mechanisms in the report."_

### environment/pressure_delta  — *shallow* (2 edges)
- **Missing modules:** membrane lipid unsaturation & fluidity regulation, ribosome dissociation / translation suppression, respiratory energy conservation (nuo complex I), osmolyte/cosolute stabilization, basic & hydrophobic proteome composition
- `hydrostatic_pressure —causes_loss_of→ membrane_fluidity`  (DOI:10.1038/s43247-023-01045-4)
- `unsaturated_fatty_acid_production —enables→ membrane_fluidity_maintenance`  (DOI:10.1186/s12864-020-07102-y)
- `hydrostatic_pressure —induces→ ribosome_dissociation`  (DOI:10.1038/s43247-023-01045-4)
- `ribosome_dissociation —restricts→ growth_supported_pressure_range`  (DOI:10.1038/s43247-023-01045-4)
- `nuo_nadh_dehydrogenase_I —supports→ high_pressure_respiratory_energy`  (DOI:10.1186/s12864-020-07102-y)
- `intracellular_osmolytes —stabilize→ proteins_under_pressure`  (DOI:10.1021/acs.chemrev.3c00432)
- _The existing graph captures trait definition but lacks 4+ generic mechanistic modules (membrane adaptation, translation suppression, energy conservation, protein stabilization) that are strongly supported across 2023-2024 literature and flagged as curation-ready by the report._

### environment/pressure_optimum  — *shallow* (2 edges)
- **Missing modules:** membrane_lipid_unsaturation_homeoviscous_adaptation, compatible_solute_osmolyte_accumulation, cation_transport_and_intracellular_osmotic_pressure, protein_stabilization_via_preferential_hydration
- `unsaturated_fatty_acid —enables→ pressure_optimum`  (10.3389/fmolb.2022.1058381 — Tamby et al. 2023 review: homeo)
- `hydrostatic_pressure —induces→ membrane_lipid_remodeling`  (10.3389/fmolb.2022.1058381, 10.1128/mbio.00958-23 — foundati)
- `cation_transport_system —increases→ intracellular_osmotic_pressure`  (10.1128/mbio.00958-23 — Zheng et al. 2023: metal ABC transpo)
- `intracellular_osmotic_pressure —enables→ HHP_tolerance`  (10.1128/mbio.00958-23 — explicitly proposed osmotic pressure)
- `compatible_solutes —promotes→ protein_stabilization`  (10.3390/microorganisms11071629 — Scheffer & Gieg 2023 review)
- `compatible_solute_accumulation —enables→ HHP_tolerance`  (10.3390/microorganisms11071629, 10.1007/s00253-023-12906-5 —)
- _Existing graph captures trait definition (hydrostatic_pressure defines optimum; optimum associated with maximal_growth_rate) but omits 4 major generic mechanistic modules that the literature review identifies as the backbone of pressure adaptation across piezophiles: membrane homeostasis, osmolyte protection, cation transport regulation, and protein stabilization. All 16 candidate edges from the report were evaluated; 10 were excluded as taxon-specific, strain-specific, correlational-only, or measuring acute stress response rather than genuine optimum shift (following Section 7 warnings)."_

### environment/temperature_delta_low  — *shallow* (2 edges)
- **Missing modules:** membrane rigidification sensing, homeoviscous adaptation cascade, fatty acid desaturation pathway, membrane fluidity biophysics, adaptation capacity constraints
- `temperature decrease —causes→ membrane rigidification`  (DOI:10.1128/spectrum.03925-23)
- `membrane rigidification —triggers→ homeoviscous adaptation`  (DOI:10.1146/annurev-micro-091313-103612)
- `homeoviscous adaptation —involves increased synthesis of→ unsaturated fatty acids`  (DOI:10.1146/annurev-micro-091313-103612)
- `increased unsaturated fatty acids —restores→ membrane fluidity`  (DOI:10.1101/2023.10.13.562271)
- `limited remodeling capacity —constrains→ homeoviscous adaptation effectiveness`  (DOI:10.1101/2023.11.10.566608)
- `adaptation system impairment under harsh cold —limits→ thermal adaptation breadth`  (DOI:10.1128/spectrum.03925-23)
- _Existing graph captures only high-level limitation concept; report establishes a detailed generic membrane-centric cascade (temperature → rigidification → sensing → fatty acid remodeling → fluidity recovery) that should form the backbone, with adaptation-failure constraints explaining narrow breadth._

### environment/temperature_delta  — *shallow* (2 edges)
- **Missing modules:** membrane lipid remodeling (unsaturated/branched fatty acids), membrane fluidity/transition temperature control, cold-shock response (CspA, RNA chaperones), heat-shock response proteostasis (RpoH, DnaK, GroEL, ClpB), protective molecule biosynthesis (compatible solutes)
- `unsaturated fatty acids —decreases→ membrane transition temperature`  (DOI:10.1146/annurev-micro-091313-103612 (Mendoza 2014, found)
- `membrane fluidity —enables→ growth across wider temperature range`  (DOI:10.1146/annurev-micro-091313-103612 (Mendoza 2014, homov)
- `cold shock —induces→ CspA cold-shock protein`  (DOI:10.1128/mbio.02174-23 (Grünberger 2023, strong for bacte)
- `CspA cold-shock protein —facilitates→ transcription and translation at low temperature`  (DOI:10.1128/mbio.02174-23 (Grünberger 2023, generic for low-)
- `RpoH sigma factor —positively regulates expression of→ DnaK and GroEL chaperones`  (DOI:10.1128/mbio.02174-23, DOI:10.1007/s12275-023-00031-x (G)
- `DnaK chaperone system —recruits→ ClpB disaggregase`  (DOI:10.1007/s12275-023-00031-x (Moon 2023, strong bacterial )
- _Existing graph captures trait endpoint and abstract thermal-adaptation flexibility but omits concrete mechanistic modules (membrane lipid sensing/remodeling, cold/heat-shock regulons, proteostasis cascades) that literature identifies as generic and broadly applicable across microbes._

### environment/temperature_optimum_low  — *shallow* (3 edges)
- **Missing modules:** cold shock proteins (CSP) induction and RNA protection, molecular chaperones (GroEL/GroES/DnaK/Clp), compatible solutes accumulation and cryoprotection, extracellular polymeric substances (EPS) production, antifreeze/ice-binding protein systems, RNA processing and ribosomal maturation under cold, antioxidant enzyme upregulation
- `cool_environment —induces→ cold shock protein expression`  (10.37256/amtt.5220244537)
- `cool_environment —upregulates→ molecular chaperone expression (GroEL/GroES/DnaK/Clp)`  (10.37256/amtt.5220244537)
- `cool_environment —promotes accumulation→ compatible solutes (glycine betaine, trehalose, glycerol)`  (10.37256/amtt.5220244537)
- `compatible solutes —stabilizes→ proteins and membranes`  (10.37256/amtt.5220244537)
- `cool_environment —increases→ extracellular polymeric substances (EPS) production`  (10.37256/amtt.5220244537)
- `antifreeze/ice-binding proteins —inhibits→ ice crystal growth and recrystallization`  (10.37256/amtt.5220244537)
- _Existing graph captures only membrane fluidity via unsaturated lipids; report identifies 7 additional generic protective modules (cold shock proteins, chaperones, compatible solutes, EPS, antifreeze proteins, RNA support, antioxidants) as broadly conserved across psychrophilic/psychrotolerant taxa."_

### environment/temperature_optimum_mid2  — *shallow* (3 edges)
- **Missing modules:** membrane rigidification/thickening sensing, fatty acid saturation/unsaturation remodeling, membrane fluidity recovery via desaturase/flux allocation, two-component temperature sensing (generic archetype), lipid composition feedback control
- `mesophilic environment —causes→ membrane rigidification`  (DOI:10.1128/spectrum.03925-23 (Sidarta et al. 2024) describe)
- `membrane rigidification —triggers→ homeoviscous adaptation`  (DOI:10.1128/spectrum.03925-23 (Sidarta et al. 2024) and DOI:)
- `homeoviscous adaptation —increases→ unsaturated fatty acids`  (DOI:10.1128/spectrum.03925-23 and DOI:10.1007/s42770-023-010)
- `unsaturated fatty acids —increases→ membrane fluidity`  (DOI:10.1128/spectrum.03925-23 (Sidarta et al. 2024) and DOI:)
- `membrane fluidity —supports→ cell division`  (DOI:10.1111/mmi.15323 (Singh & Harinarayanan 2024) demonstra)
- `baseline mesophile adaptation —maintains→ membrane homeostasis through lipid remodeling`  (DOI:10.1007/s42770-023-01057-4 (Ramón et al. 2023) describes)
- _Existing graph captures the phenotypic outcome but omits the mechanistic cascade: temperature → membrane physical state change → sensing/remodeling → fluidity restoration → growth; all generic, well-supported modules present in report."_

### environment/temperature_optimum_mid4  — *shallow* (3 edges)
- **Missing modules:** homeoviscous adaptation (membrane lipid remodeling), RNA thermometer regulation, heat-shock proteostasis axis (RpoH/DnaK/proteases), DNA supercoiling and gyrase-mediated topology control
- `temperature change —alters→ unsaturated fatty acid proportion`  (Foundational homoviscous adaptation mechanism)
- `unsaturated fatty acids —maintains→ membrane fluidity homeostasis`  (Direct mechanistic outcome of cold-induced FA remodeling)
- `temperature upshift —melts→ RNA thermometer secondary structure`  (ROSE and FourU RNATs form inhibitory hairpins at low T and m)
- `RNA thermometer melting —exposes→ Shine-Dalgarno ribosome binding site`  (Direct consequence of RNAT structural change)
- `heat-denatured proteins —displace→ DnaK from RpoH`  (Core heat-shock regulatory mechanism)
- `ATP-dependent DNA gyrase —mediates→ temperature-sensitive DNA supercoiling adjustments`  (Generic bacterial topology regulator)
- _Existing graph has bare scaffolding (environment + adaptation phenotype) but misses four generic mechanistic modules (membrane remodeling, RNA thermometers, proteostasis, DNA topology) that literature strongly supports as core warm-mesophile physiology._

### environment/temperature_phenotype_with_numerical_limits  — *shallow* (4 edges)
- **Missing modules:** homeoviscous adaptation pathway, membrane fluidity maintenance, fatty acid unsaturation induction, protein quality control and chaperone response, DNA topology and supercoiling thermosensing
- `membrane rigidification during cooling —activates→ DesK/DesR two-component signaling`  (DOI:10.1007/s42770-023-01057-4)
- `fatty acid desaturase activity —increases→ unsaturated fatty acid biosynthesis`  (DOI:10.1007/s42770-023-01057-4)
- `unsaturated fatty acid content —maintains→ membrane fluidity`  (DOI:10.37256/amtt.5220244537)
- `membrane fluidity maintenance —supports→ growth at low temperature`  (DOI:10.1039/d4cc03114h)
- `DNA gyrase activity —changes→ DNA supercoiling`  (DOI:10.1007/s12275-023-00031-x)
- `DNA supercoiling change —modulates→ transcription during temperature response`  (DOI:10.1007/s12275-023-00031-x)
- _Existing graph is taxonomic only (trait class hierarchy); report describes five major generic mechanistic modules (membrane adaptation, protein quality control, DNA topology sensing, RNA maintenance, cryoprotection) almost entirely absent from the causal graph._

### environment/temperature_range_high  — *shallow* (2 edges)
- **Missing modules:** DNA genome-stability via reverse gyrase and positive supercoiling, Proteostasis maintenance via heat-shock chaperones and proteases
- `reverse gyrase (TopR/rgy) —introduces→ positive DNA supercoils`  (takemata2024howdothermophiles (pages 1-2, 2-3))
- `positive DNA supercoils —limits→ DNA melting`  (takemata2024howdothermophiles (pages 1-2))
- `reverse gyrase —maintains→ genome integrity at high temperature`  (takemata2024howdothermophiles (pages 1-2))
- `heat-shock chaperones (DnaK/GroEL/HtpG) —assist→ protein folding under heat stress`  (moon2023temperaturemattersbacterial (pages 6-7))
- `proteases (Lon/Clp/HslUV/FtsH) —degrade→ misfolded proteins at high temperature`  (moon2023temperaturemattersbacterial (pages 6-7))
- `proteostasis at high temperature —supports→ growth at high temperature`  (grunberger2023uncoveringthetemporal (pages 1-2))
- _Existing graph captures thermostability generically but misses two major generic mechanistic modules from recent literature: DNA genome-stability via reverse gyrase and proteostasis via heat-shock machinery; membrane-adaptation edges are correctly absent (taxon-specific to archaea/thermoacidophiles with pH coupling)._

### environment/temperature_range_mid1  — *shallow* (2 edges)
- **Missing modules:** membrane physical-state sensing and signaling, fatty-acid biosynthesis and lipid remodeling (desaturation and BCFA precursor pathways), cold-shock and stress-responsive gene expression (sigma factors, RNA thermometers, CspA)
- `temperature decrease to ~25 °C —causes→ membrane rigidification/thickening`  (DOI:10.1007/s42770-023-01057-4)
- `membrane rigidification —initiates→ fatty-acid desaturation pathway`  (DOI:10.1128/spectrum.03925-23)
- `fatty-acid desaturation —increases→ membrane fluidity`  (DOI:10.1128/spectrum.03925-23)
- `cooling —increases→ cis-vaccenic acid synthesis`  (DOI:10.1007/s42770-023-01057-4)
- `cold shock —induces→ CspA RNA-binding protein`  (DOI:10.1007/s12275-023-00031-x)
- `branched-chain amino acids —precursors for→ anteiso-branched fatty acids`  (DOI:10.1007/s42770-023-01057-4)
- _Existing graph captures only high-level abstraction; report reveals rich mechanistic detail on membrane sensing, lipid remodeling, and stress response that are broadly conserved across mesophiles and should be incorporated as intermediate nodes and edges._

### environment/temperature_range_mid3  — *shallow* (2 edges)
- **Missing modules:** membrane thickness sensing (DesK two-component system), fatty acid desaturation and UFA synthesis pathway, homeoviscous adaptation negative feedback
- `temperature decrease —causes→ membrane rigidification and increased thickness`  (DOI:10.1007/s42770-023-01057-4)
- `membrane rigidification —activates→ DesK kinase state`  (DOI:10.1128/spectrum.03925-23)
- `DesK —phosphorylates→ DesR`  (DOI:10.1128/spectrum.03925-23)
- `phosphorylated DesR —activates transcription of→ des (Δ5 desaturase)`  (DOI:10.1128/spectrum.03925-23)
- `des desaturase —increases→ unsaturated fatty acids`  (DOI:10.1128/spectrum.03925-23)
- `unsaturated fatty acids —decreases→ membrane thickness and order`  (DOI:10.1007/s42770-023-01057-4)
- _Existing graph captures upper-mesophile adaptation concept but lacks the well-documented membrane-sensing (DesK/DesR), UFA synthesis, and feedback-regulation modules that enable 30–34 °C growth across diverse mesophiles._

### environment/temperature_range_mid4  — *shallow* (2 edges)
- **Missing modules:** homeoviscous adaptation via FabI/FabB metabolic valve, membrane fluidity homeostasis, fatty acid composition control (saturated vs unsaturated balance), FabR/FadR transcriptional feedback regulation, heat shock response system (σ32/RpoH and chaperones), protein quality control/proteostasis
- `warm_mesophile_adaptation —regulates→ homeoviscous adaptation`  (Hoogerland 2024 (DOI:10.1038/s41467-024-53677-5) demonstrate)
- `homeoviscous adaptation —maintains→ membrane fluidity`  (Hoogerland 2024 (DOI:10.1038/s41467-024-53677-5) quantifies )
- `FabI/FabB branchpoint metabolic valve —shifts_flux_between→ saturated vs unsaturated fatty acids`  (Hoogerland 2024 (DOI:10.1038/s41467-024-53677-5) identifies )
- `saturated fatty acids —stiffen→ membrane fluidity`  (McGuire 2023 (DOI:10.1186/s12864-023-09266-9) and Hoogerland)
- `heat stress —triggers→ heat shock response (σ32 regulon)`  (Berdejo 2024 (DOI:10.1128/mbio.03105-23) documents that σ32/)
- `heat shock response (σ32 regulon) —protects→ protein folding and stability`  (Berdejo 2024 (DOI:10.1128/mbio.03105-23) and McGuire 2023 (D)
- _Existing graph captures only high-level warm-mesophile adaptation phenotype but misses all major mechanistic modules; report describes rich, generic homeoviscous adaptation backbone (membrane-lipid valve + transcriptional feedback) and proteostasis pathways that are universally applicable across bacteria and should be added as core nodes and edges._

### environment/temperature_range  — *shallow* (4 edges)
- **Missing modules:** membrane lipid homeostasis / unsaturation, compatible solutes accumulation, heat-shock protein / chaperone systems, oxidative stress response & protection, two-component thermosensing
- `cold ambient temperature —triggers homeostatic response→ increased membrane lipid unsaturation`  (DOI:10.1007/s12275-023-00031-x: broad bacterial mechanism li)
- `cold stress —induces accumulation of→ compatible solutes (glycine betaine, trehalose, glycerol)`  (DOI:10.37256/amtt.5220244537: cross-taxa cryoprotection mech)
- `heat stress —upregulates→ heat-shock protein chaperone systems (DnaK, GroEL)`  (DOI:10.1007/s12275-023-00031-x: universal bacterial heat-tol)
- `thermal stress (cold or heat) —increases→ reactive oxygen species (ROS)`  (DOI:10.37256/amtt.5220244537: oxidative stress is a measurab)
- `oxidative stress response systems —support→ thermal tolerance / growth under extreme temperature`  (DOI:10.1371/journal.pone.0310595: antioxidant/oxidative-dama)
- `membrane physical state changes (fluidity / lipid packing) —activate→ two-component signal transduction cascades`  (DOI:10.1007/s42770-023-01057-4: generic cold-sensing mechani)
- _Existing graph captures phenotype endpoints but lacks mechanistic depth; report identifies 5+ generic, peer-reviewed molecular modules (membrane adaptation, solutes, chaperones, oxidative protection, thermosensing) absent from the current causal graph, warranting expansion to adequately reflect the generic literature consensus."_

### environment/thermophilic  — *shallow* (5 edges)
- **Missing modules:** protein homeostasis via heat shock proteins (sHSPs/prefoldin/thermosome), DNA topology protection via reverse gyrase, nucleoid-associated protein (NAP) driven chromatin organization, heat-triggered expression of chaperone system
- `high_temperature —induces→ small_heat_shock_proteins`  (DOI:10.1128/mbio.03593-22 — Baes 2023 demonstrates heat shoc)
- `small_heat_shock_proteins —delivers_to→ thermosome_chaperonin`  (DOI:10.1128/mbio.03593-22 — sHSPs and prefoldin shuttle unfo)
- `reverse_gyrase —introduces→ positive_DNA_supercoils`  (DOI:10.1264/jsme2.me23087 — Takemata 2024 establishes revers)
- `high_temperature —activates→ reverse_gyrase`  (DOI:10.1128/mbio.03593-22 — Baes 2023 shows heat shock cause)
- `nucleoid_associated_proteins —reorganizes→ chromosome_organization`  (DOI:10.1264/jsme2.me23087 — Takemata 2024 frames NAPs and ch)
- `positive_DNA_supercoils —limits→ DNA_melting`  (DOI:10.1264/jsme2.me23087 — Takemata 2024 review establishes)
- _Existing graph captures membrane permeability and thermostable proteins but critically misses three major generic modules: heat-inducible protein folding machinery (sHSPs→thermosome pathway), reverse gyrase-mediated DNA topology protection, and NAP-driven genome organization—all supported by 2023–2024 literature as core thermophily mechanisms."_

### environment/uv_radiation_tolerant  — *shallow* (3 edges)
- **Missing modules:** DNA lesion formation (CPD/6-4PP), lesion-induced transcription/replication block, ROS generation and oxidative damage pathway, antioxidant detoxification (catalase/SOD), photoreactivating light requirement
- `ultraviolet radiation —causes→ cyclobutane pyrimidine dimer`  (10.3390/life14070822)
- `cyclobutane pyrimidine dimer —inhibits→ transcription and replication`  (10.3390/microorganisms13040756)
- `nucleotide excision repair —repairs→ cyclobutane pyrimidine dimer`  (10.3390/life14070822)
- `ultraviolet radiation —generates→ reactive oxygen species`  (10.3390/microorganisms13040756)
- `reactive oxygen species —causes→ DNA strand breaks and oxidative base damage`  (10.3390/microorganisms13040756)
- `catalase —detoxifies→ reactive oxygen species`  (10.3390/microorganisms13040756)
- _Existing graph captures two repair pathways but omits lesion formation, lesion consequences, ROS pathway, antioxidants, and light activation—representing generic mechanisms firmly supported across taxa."_

### environment/zinc_tolerant  — *shallow* (3 edges)
- **Missing modules:** ZntA primary inner-membrane efflux, ZntR regulatory activation layer, environmental trigger (Zn threshold sensing), backup CDF-family exporter (CdfX), cytoplasmic metal buffering (glutathione/polyphosphate)
- `zinc(II) ion (CHEBI:29105) —upregulates→ zntA expression`  (Schulz et al. (2024): 'At external zinc concentrations above)
- `ZntR MerR-family regulator —required_for→ zntA expression`  (Schulz et al. (2024): 'ZntR was essential for zntA expressio)
- `ZntA PIB2-type P-type ATPase —exports→ zinc(II) ion (CHEBI:29105)`  (Nies et al. (2024): 'Efflux of zinc ions is mediated by the )
- `ZntR MerR-family regulator —upregulates→ cdfX expression`  (Schulz et al. (2024): 'ZntR was responsible for zinc- and ca)
- `CdfX CDF-family exporter —exports→ zinc(II) ion (CHEBI:29105)`  (Schulz et al. (2024): 'The efflux system CdfX exports zinc t)
- `glutathione (CHEBI:16856) —contributes_to→ zinc flow equilibrium / buffering`  (Nies et al. (2024): 'The absence of... glutathione... influe)
- _Existing graph captures only plasmid-borne CzcCBA pathway; 2024 literature reveals a layered homeostasis model integrating ZntA-ZntR regulation, backup CdfX exporter, and cytoplasmic buffering (GSH, polyP) that are generic, well-supported mechanisms absent from current curation."_

### genomics/crispr_cas_system  — *shallow* (2 edges)
- **Missing modules:** spacer integration/acquisition, crRNA biogenesis and processing, effector complex target recognition and cleavage
- `Cas1–Cas2 complex —integrates into→ CRISPR array spacers`  (10.5483/bmbrep.2023-0050)
- `CRISPR array —is transcribed and processed to produce→ crRNA`  (10.1016/j.heliyon.2024.e39538)
- `crRNA —forms complex with→ Cas effector proteins`  (10.5483/bmbrep.2023-0050)
- `crRNA–Cas effector complex —enables cleavage of→ invading nucleic acid target`  (10.5483/bmbrep.2023-0050)
- `Type I/II/IV/V CRISPR-Cas systems —target→ DNA`  (10.5483/bmbrep.2023-0050)
- `Type III/VI CRISPR-Cas systems —target→ RNA`  (10.5483/bmbrep.2023-0050)
- _Existing graph captures trait-level defense participation but omits generic molecular steps (spacer integration, crRNA maturation, target recognition/cleavage) essential to mechanism representation._

### genomics/gc_content  — *shallow* (8 edges)
- **Missing modules:** DNA replication/repair/damage (DRR) system, cytosine deamination process, oxidative guanine lesions (8-oxoG) formation, error-prone translesion synthesis (TLS), amino-acid metabolic cost coupling, environmental temperature/pH/resource selection
- `cytosine deamination —decreases→ gc_content_trait`  (DOI:10.1128/spectrum.02145-22 (Teng 2023))
- `guanine oxidation (8-oxoG) —alters mutational spectrum toward AT→ gc_content_trait`  (DOI:10.1128/spectrum.02145-22 (Teng 2023))
- `translesion synthesis (TLS) —increases→ gc_content_trait`  (DOI:10.1128/spectrum.02145-22 (Teng 2023))
- `codon usage (GC-rich) —shifts proteome toward→ lower amino-acid metabolic cost`  (DOI:10.1111/1462-2920.16511 (Aliperti 2023))
- `high temperature (optimal growth) —positively associated with→ gc_content_trait`  (DOI:10.1186/s12864-022-08353-7 (Hu 2022))
- `soil pH —positively associated with→ community-average gc_content`  (DOI:10.1038/s41467-023-43297-w (Wang 2023))
- _Existing graph captures mutation bias and codon-usage selection but lacks DNA damage/repair intermediates (cytosine deamination, 8-oxoG, TLS), proteome-cost coupling, and environmental selection drivers explicitly described in the literature as generic mechanisms._

### genomics/gc_mid1  — *shallow* (2 edges)
- **Missing modules:** NHEJ/Ku pathway (DSB repair module), DRR-system composition framework (replication/repair systems), DnaE2 TLS polymerase positive correlate, MutS2 and MMR/HR proteins negative correlates, DSB damage/repair selection pressure
- `Ku/bacterial NHEJ pathway —positively_correlated_with→ high genomic GC content >66.3% (METPO:1000430)`  (Pearson r=0.54 (p<2.2×10−16))
- `DnaE2 translesion synthesis polymerase —positively_correlated_with→ high genomic GC content >66.3% (METPO:1000430)`  (Strongest positive GC correlate among DRR genes in 11,083-ge)
- `MutS2 mismatch repair protein —negatively_correlated_with→ high genomic GC content >66.3% (METPO:1000430)`  (Strongest negative GC correlate)
- `MutS, MutL, RecJ, RecU MMR/HR proteins —negatively_correlated_with→ high genomic GC content >66.3% (METPO:1000430)`  (Negative correlates in DRR-system model)
- `high double-strand break formation rate —selects_for→ high genomic GC content >66.3% (METPO:1000430)`  (Mechanistic hypothesis: DSB-inducing environments (soils, ae)
- `DNA replication and repair (DRR) system composition —strongly_correlated_with→ genomic GC state (METPO:1000430)`  (Linear model using 217 DRR-related KEGG orthologs explains 8)
- _Existing graph relies on gBGC, which the report flags as insufficiently supported for prokaryotes; major recent 2023-2024 literature emphasizes DNA replication/repair systems (DRR) as the primary generic mechanism, with multiple quantified, taxon-agnostic correlates (NHEJ/Ku, DnaE2, MutS2, MMR/HR) that can enrich the graph substantially."}
</invoke>_

### genomics/gc_mid2  — *shallow* (2 edges)
- **Missing modules:** homologous recombination → gBGC upstream link, DNA double-strand break repair pathway (Ku/NHEJ), mutation bias (AT enrichment) counterforce, GC3 / recombination-associated GC signature
- `homologous recombination —positively influences→ GC-biased gene conversion`  (DOI:10.1101/011023 — Lassalle et al. 2015 foundational mecha)
- `Ku protein / NHEJ —positively associated with→ genome-wide GC content`  (DOI:10.1371/journal.pgen.1008493 — Weissman et al. 2019)
- `DNA double-strand break rate —positively influences→ selection for high GC content`  (DOI:10.1371/journal.pgen.1008493 — Weissman et al. 2019)
- `mutation bias toward AT —negatively influences→ genome-wide GC content`  (DOI:10.1101/011023 — Lassalle et al. 2015)
- `cytosine deamination —positively influences→ mutation bias toward AT`  (DOI:10.63635/mrj.v1i4.188 — Deka et al. 2025)
- `recombining genes —has increased attribute→ GC3`  (DOI:10.1101/011023 — Lassalle et al. 2015)
- _Existing graph captures gBGC→GC pathway but omits 4 generic mechanistic modules: upstream recombination coupling, DSB repair selection axis, AT-biased mutation counterforce, and GC3/recombination signature; report flagged Ku–GC as association/uncertain (mark carefully in YAML)._

### genomics/genome_size  — *shallow* (2 edges)
- **Missing modules:** abiotic environmental drivers (ocean depth, temperature, soil pH), lifestyle/ecological strategy (particle-associated vs free-living), nutrient/resource limitation as selective pressure, horizontal gene transfer & prophage integration (genome expansion), CRISPR-Cas defence systems (inhibition of HGT), metabolic versatility as correlate of genome size
- `seawater temperature —negatively associated with→ genome size`  (DOI:10.1038/s41467-023-36988-x)
- `soil pH —negatively associated with→ genome size`  (DOI:10.1101/2021.11.17.469016)
- `horizontal gene transfer —increases→ genome size`  (DOI:10.1038/s41559-024-02357-0)
- `gene loss —decreases→ genome size`  (DOI:10.1038/s41467-024-50368-z)
- `CRISPR-Cas defence system —decreases→ gene gain rate`  (DOI:10.1111/1462-2920.16630)
- `metabolic versatility —positively associated with→ genome size`  (DOI:10.1038/s41564-023-01465-0)
- _Existing graph captures reductive evolution pathway but omits major generic mechanisms: abiotic drivers (ocean depth/temp/soil pH), HGT/prophage integration, and defence-system-mediated constraints on genome expansion documented across 2023-2024 literature (Ngugi, Chuckran, Dmitrijeva, Kogay et al.)._

### genomics/ploidy  — *shallow* (2 edges)
- **Missing modules:** phosphate-buffering nutrient storage, environmental phosphate-starvation response, segregational drift (population-genetic consequence)
- `ploidy_trait —enables→ growth without external phosphate`  (Polyploidy enables growth in phosphate-free media by mobiliz)
- `phosphate starvation —decreases→ ploidy_trait`  (All characterized polyploid prokaryotes reduce genome copy n)
- `ploidy_trait —increases→ segregational drift`  (Higher chromosome copy number increases stochastic allele se)
- `polyploidy —enables→ nucleotide/phosphate mobilization during nutrient stress`  (Redundant genome copies can be degraded and metabolized to r)
- `segregational drift —decreases→ beneficial allele fixation on polyploid replicons`  (Stochastic allele segregation on multicopy replicons reduces)
- `genome copy number variation —contributes to→ within-cell genetic heterogeneity`  (Polyploid cells maintain heterozygous states across multiple)
- _Existing graph captures DNA repair pathway but misses two major generic mechanisms: phosphate-nutrient buffering (supported across five polyploid species) and segregational drift (fundamental population-genetic consequence); both are central to recent literature and warrant high-priority enrichment."_

### genomics/restriction_modification_system  — *shallow* (2 edges)
- **Missing modules:** methyltransferase activity and host-site methylation, restriction endonuclease cleavage of unmethylated DNA, plasmid-encoded counter-defenses (methylases, anti-restriction proteins), phage counter-defenses (DNA modification, encoded methylases)
- `cognate DNA methyltransferase —methylates→ host recognition sites`  (DOI:10.1093/nar/gkad452 (Shaw et al. 2023) — MTase protects )
- `host-site methylation —protects from→ cognate restriction endonuclease cleavage`  (DOI:10.1093/nar/gkad452 (Shaw et al. 2023) — core mechanisti)
- `restriction endonuclease —cleaves→ unmethylated foreign double-stranded DNA`  (DOI:10.1093/nar/gkad452 (Shaw et al. 2023) — REase destroys )
- `plasmid-encoded methylase —protects plasmid from→ host restriction activity`  (DOI:10.1093/nar/gkae896 (Dimitriu et al. 2024) — plasmids ev)
- `anti-restriction genes on plasmids —inhibit→ RM-mediated restriction during conjugation`  (DOI:10.1093/nar/gkae896 (Dimitriu et al. 2024) — ArdA/ArdB/O)
- `phage-encoded DNA methyltransferase —reduces→ host RM restriction of phage genome`  (DOI:10.1128/MMBR.00044-12 (Vasu & Nagaraja 2013) — phages en)
- _Existing graph captures high-level self/non-self discrimination but lacks enzymatic details, plasmid/phage counter-defenses, and mechanistic depth; generic backbone present, but 4+ core mechanistic modules are missing and should be added as nodes/edges at the core trait level (distinct from type-specific or assay-specific edges)._

### metabolism/acetogenesis  — *shallow* (6 edges)
- **Missing modules:** energy conservation via Rnf/Ech and ATP synthase, electron bifurcation/confurcation module (HydABC), detailed methyl-branch enzymatic resolution (FDH, Fhs, FolD, MTHFR, methyltransferase), detailed carbonyl-branch resolution (CODH, ACS)
- `hydrogen —oxidized by→ HydABC electron-bifurcating hydrogenase`  (doi:10.1038/s41467-024-49680-5)
- `reduced ferredoxin —drives ion pumping in→ Rnf complex`  (doi:10.3389/fbioe.2024.1395540)
- `Rnf-generated ion gradient —drives→ ATP synthase-catalyzed ATP production`  (doi:10.3389/fbioe.2024.1395540)
- `carbon dioxide —reduced by formate dehydrogenase to→ formate`  (doi:10.34726/hss.2024.114566)
- `formate —activated and converted by formyl-THF synthetase to→ formyl-THF`  (doi:10.3389/fbioe.2024.1395540)
- `acetyl-CoA —converted via substrate-level phosphorylation by PTA/ACK to→ acetate and ATP`  (doi:10.3389/fbioe.2024.1395540)
- _Existing graph has carbon-fixation backbone but lacks two GENERIC mechanistic modules essential for functioning acetogenesis: energy conservation (Rnf/Ech chemiosmosis) and electron bifurcation; also lacks fine-grained WLP resolution (currently a black box with single node)._

### metabolism/aerobic_respiration  — *shallow* (6 edges)
- **Missing modules:** NADH oxidoreductase (Complex I) entry point, quinone electron carrier pathway, cytochrome bc1 complex (Complex III) step, cytochrome c as electron shuttle to terminal oxidases, bo3 quinol oxidase pathway (oxygen-dependent), cytochrome bd oxidase pathway and its PMF mechanism
- `NADH:quinone oxidoreductase (Complex I, NDH-1) —reduces→ quinone pool / ubiquinone`  (DOI:10.12938/bmfh.2024-002)
- `quinone pool / ubiquinol —donates electrons to→ cytochrome bc1 complex (Complex III)`  (DOI:10.1089/ars.2020.8039)
- `cytochrome bc1 complex (Complex III) —reduces→ cytochrome c`  (DOI:10.12938/bmfh.2024-002)
- `cytochrome c —donates electrons to→ heme-copper terminal oxidase family (Complex IV)`  (DOI:10.3389/fmicb.2024.1468929)
- `quinol / ubiquinol —donates electrons to→ cytochrome bd oxidase`  (DOI:10.3390/ijms25021277)
- `cytochrome bd oxidase —generates→ proton motive force`  (DOI:10.3390/antiox13030383)
- _The existing graph captures the trait phenotype (O2 reduction, ATP synthesis) but omits the generic prokaryotic electron transport chain architecture (Complexes I–IV, electron carriers, alternative terminal oxidases), making it adequate for high-level overview but shallow for mechanistic completeness._

### metabolism/anaerobic_respiration  — *shallow* (5 edges)
- **Missing modules:** fumarate respiration pathway, sulfoxide/sulfoxide-compound respiration (DMSO/MetSO), electron shuttle systems (quinone pool, phenazine oxidation), alternative nitrite reduction mechanisms (non-NirK/NirS)
- `anaerobic respiration —exemplified by→ fumarate respiration`  (DOI:10.1101/2023.11.14.567096 shows FrdA-dependent fumarate )
- `anaerobic respiration —exemplified by→ sulfoxide respiration`  (DOI:10.1016/j.chom.2024.01.004 demonstrates DmsABC-mediated )
- `terminal electron acceptor availability —increases activity of→ anaerobic respiration`  (DOI:10.1101/2023.11.14.567096 reports any respirable termina)
- `oxygen limitation —increases activity of→ anaerobic respiratory reductases`  (DOI:10.1038/s41467-024-51688-w shows early transcription of )
- `quinone pool —transfers electrons to→ terminal electron acceptor reductases`  (DOI:10.1101/2023.11.14.567096 pages 9-16 describes quinone-m)
- `fumarate reductase —uses→ fumarate`  (DOI:10.1101/2023.11.14.567096 pages 26-31 demonstrates FrdA )
- _The existing anaerobic respiration graph captures only denitrification with nitrogen oxides; it misses at least 4 major GENERIC anaerobic respiratory pathways (fumarate, sulfoxide compounds, alternative reductases, electron shuttles) that are well-supported in 2024 peer-reviewed and preprint literature and represent universal mechanistic capacity across facultative anaerobes._

### metabolism/anoxygenic_photosynthesis  — *shallow* (2 edges)
- **Missing modules:** reaction center architecture (Type I and Type II), alternative electron donors (Fe(II) photoferrotrophy), primary product (elemental sulfur oxidation)
- `Type I reaction center —enables→ anoxygenic photosynthesis`  (DOI:10.1038/s41586-024-07180-y, DOI:10.3390/biom14030311)
- `Type II reaction center —enables→ anoxygenic photosynthesis`  (DOI:10.3390/biom14030311)
- `Fe(II) —is_electron_donor_for→ anoxygenic photosynthesis`  (DOI:10.1073/pnas.2322120121)
- `anoxygenic photosynthesis —produces→ elemental sulfur`  (DOI:10.3389/fmicb.2024.1417714)
- `Light —enables→ anoxygenic photosynthesis`  (DOI:10.1038/s41586-024-07180-y)
- `sulfide —oxidized_to→ elemental sulfur`  (DOI:10.3389/fmicb.2024.1417714)
- _Existing graph captures sulfide electron donation backbone but lacks reaction center types (RCI/RCII), alternative donors (Fe(II)), and primary products (S0), representing 3 generic mechanistic modules core to anoxygenic photosynthesis._

### metabolism/cable_bacteria_metabolism  — *shallow* (9 edges)
- **Missing modules:** nickel-cofactor-mediated conduction, nickel homeostasis system, nitrate reduction as terminal acceptor, cytochrome-mediated electron loading
- `conductive_fiber_network —contains→ nickel_cofactor`  (DOI:10.3389/fmicb.2024.1208033)
- `nickel_cofactor —mediates→ long_distance_electron_transport`  (DOI:10.3389/fmicb.2024.1208033 — Orientation-dependent Raman)
- `nitrate —serves_as_terminal_electron_acceptor_for→ electrogenic_sulfur_oxidation`  (DOI:10.7554/eLife.91097)
- `nickel_ion_homeostasis —enables→ nickel_cofactor`  (DOI:10.1186/s12864-024-10594-7 — Comparative genomics reveal)
- `periplasmic_cytochromes —facilitate_electron_loading_unloading_at→ conductive_fiber_network`  (DOI:10.3389/fmicb.2024.1208033 — Raman analysis indicates cy)
- `intact_filament_continuity —required_for→ long_distance_electron_transport`  (DOI:10.1073/pnas.1800367115 — Laser-cutting filaments or rem)
- _The existing graph captures the sulfide-oxygen redox couple and basic fiber conductivity well, but misses the nickel-cofactor mechanism (now central to 2024 literature) and nitrate-reduction capacity; high-priority enrichment targets are the Ni system (3 convergent papers) and alternative electron acceptors._

### metabolism/dicarboxylate_four_hydroxybutyrate_cycle  — *shallow* (2 edges)
- **Missing modules:** oxygen sensitivity constraint, pyruvate synthase carboxylation step, PEPC carboxylation step, succinyl-CoA reductase step, succinic semialdehyde reductase step, 4-hydroxybutyryl-CoA dehydratase hallmark enzyme, beta-oxidation closure (crotonyl-CoA to acetyl-CoA)
- `molecular oxygen (CHEBI:15379) —negatively_regulates→ dicarboxylate/4-hydroxybutyrate cycle (traitmech:000025)`  (DOI:10.1128/AEM.02473-10 (Berg 2011) — oxygen sensitivity of)
- `pyruvate synthase / pyruvate:ferredoxin oxidoreductase (EC:1.2.7.1) —catalyzes_reductive_carboxylation_of→ acetyl-CoA (CHEBI:15351) to pyruvate (CHEBI:15361)`  (DOI:10.1002/9783527629916 (Berg et al. 2010) — first carboxy)
- `phosphoenolpyruvate carboxylase (EC:4.1.1.31) —catalyzes_carboxylation_of→ phosphoenolpyruvate (CHEBI:18021) to oxaloacetate (CHEBI:16452)`  (DOI:10.1002/9783527629916 (Berg et al. 2010) — second carbox)
- `4-hydroxybutyryl-CoA dehydratase (GO:0018798) —catalyzes_radical_dehydration_of→ 4-hydroxybutyryl-CoA to crotonyl-CoA (CHEBI:37554)`  (DOI:10.1073/pnas.0801043105 (Huber et al. 2008) — hallmark r)
- `crotonyl-CoA (CHEBI:37554) —is_oxidized_via_beta_oxidation_to→ acetyl-CoA (CHEBI:15351)`  (DOI:10.1073/pnas.0801043105 (Huber et al. 2008) — beta-oxida)
- `succinyl-CoA (CHEBI:15380) —is_reduced_via_enzyme_cascade_to→ 4-hydroxybutyrate (CHEBI:30830)`  (DOI:10.1146/annurev-micro-090110-102801 (Fuchs 2011) — succi)
- _Existing graph captures trait-level CO2 fixation but lacks the detailed generic pathway mechanism—nine catalytic steps, oxygen sensitivity, and substrate specificity—all well-supported by canonical biochemistry literature (Huber, Berg, Fuchs)._

### metabolism/dissimilatory_iron_reduction  — *shallow* (2 edges)
- **Missing modules:** anaerobic respiration classification, electron donor coupling, Fe(III) speciation effects on kinetics, extracellular electron transfer (EET) mechanism, hydrogen oxidation coupling
- `dissimilatory iron reduction —is_a→ energy-conserving anaerobic respiration`  (DOI:10.1128/mr.55.2.259-287.1991 — Lovley 1991 establishes D)
- `organic matter oxidation —coupled_to→ ferric iron reduction`  (DOI:10.1128/mr.55.2.259-287.1991 — Core mechanistic principl)
- `hydrogen oxidation —can_be_coupled_to→ ferric iron reduction`  (DOI:10.1128/mr.55.2.259-287.1991 — Lovley review: H2 oxidati)
- `dissolved Fe(III)-organic matter complexes —have_higher_reduction_rates_than→ solid Fe(III) oxide minerals`  (DOI:10.1007/s10533-024-01186-4 — Shi et al. 2024: Fe(III) sp)
- `extracellular electron transfer —enables→ reduction of insoluble Fe(III) oxides`  (DOI:10.1128/mbio.00690-24 — Schwarz et al. 2024: EET (via co)
- `dissimilatory iron reduction —requires→ anaerobic conditions`  (DOI:10.1128/mbio.02589-22 — Norman et al. 2023: oxygen expos)
- _Existing graph captures the core redox chemistry (Fe(III)→Fe(II)) but misses generic mechanistic scaffolding: anaerobic respiration context, electron donors, Fe(III) speciation logic, and EET as a universal module for particulate substrates—all well-supported across multiple recent papers and absent taxon-specificity constraints._

### metabolism/dissimilatory_manganese_reduction  — *shallow* (2 edges)
- **Missing modules:** electron donor coupling (organic matter, hydrogen), anoxia/anaerobic requirement, extracellular electron transfer (EET) as core mechanistic constraint, mediated EET conduit module (quinol-to-quinone entry + cytochrome transfer), direct EET conduit module (outer-membrane complex + extracellular cytochrome + e-pili)
- `organic matter —enables→ dissimilatory manganese reduction`  (DOI:10.1128/mr.55.2.259-287.1991 - 'organisms can completely)
- `hydrogen —enables→ dissimilatory manganese reduction`  (DOI:10.1128/mr.55.2.259-287.1991 - 'organisms...can complete)
- `anoxia —enables→ dissimilatory manganese reduction`  (DOI:10.1128/mr.55.2.259-287.1991 - DMR is defined as 'anaero)
- `dissimilatory manganese reduction —requires_process→ extracellular electron transfer`  (DOI:10.3389/fmicb.2012.00050 (Shi 2012) and DOI:10.1128/aem.)
- `quinol oxidation —initiates→ extracellular electron transfer`  (DOI:10.3389/fmicb.2012.00050 - inner-membrane quinone pool e)
- `extracellular cytochromes —enable→ terminal reduction of external metal oxides`  (DOI:10.1128/aem.03109-20 - outer-membrane cytochromes (OmcS,)
- _Existing graph captures core chemistry (Mn(IV) reduction to Mn(II)) but lacks the generic electron-transfer mechanistic modules (donor coupling, EET pathways) that explain how organisms actually perform this anaerobic respiration; the report identifies two distinct EET paradigms (mediated via quinone-cytochrome transfer, direct via e-pili) that should be represented at the trait level, not just the biochemical transformation."_

### metabolism/dissimilatory_nitrate_reduction_to_ammonium  — *shallow* (2 edges)
- **Missing modules:** nitrite intermediate node (canonical NO3→NO2→NH4+ pathway), nitrate reductase catalysts (NarGHI, NapAB), nitrite reductase (NrfA) canonical enzyme, regulatory sensing layer (FNR, NarX/NarL nitrate/O2 control), electron donor/DOC-NO3 ratio environmental driver
- `nitrate —is reduced to→ nitrite via NarGHI`  (DOI:10.1128/msystems.00967-23)
- `nitrite —is reduced to→ ammonium via NrfA`  (DOI:10.1128/aem.00292-25)
- `nrfA gene abundance —positively correlates with→ DNRA potential rate`  (DOI:10.3389/fmicb.2024.1411753)
- `high DOC/NO3 ratio —promotes→ DNRA-associated community (Anaeromyxobacter, Geobacter)`  (DOI:10.3390/land13101557)
- `anaerobic conditions with nitrate —activates expression of→ nrf operon via NarX/NarL`  (DOI:10.1128/aem.00292-25)
- `anaerobic conditions —activate→ FNR-mediated DNRA pathway activation`  (DOI:10.1128/aem.00292-25)
- _The existing graph captures the trait, final product, and one environmental factor, but misses the canonical two-step enzymatic pathway (NO3→NO2→NH4), core enzymes (NarGHI/NapAB, NrfA), regulatory control (FNR, NarX/NarL), and refined environmental drivers (DOC/NO3 ratio); these are all well-supported by 2024-2025 literature."_

### metabolism/fermentative_hydrogen_production  — *shallow* (2 edges)
- **Missing modules:** pyruvate → ferredoxin electron transfer (PFOR), reduced ferredoxin electron donation to hydrogenase, NADH → ferredoxin electron transfer (redox balancing), bifurcating [FeFe] hydrogenase electron coupling module, acetate-H2 product coupling (end-product-driven redox balance), H2 partial pressure feedback regulation (global inhibition mechanism)
- `pyruvate:ferredoxin oxidoreductase (PFOR) —reduces→ ferredoxin`  (10.1007/s00253-023-12974-7 — mechanistically central for pyr)
- `reduced ferredoxin —is electron donor to→ [FeFe] hydrogenase`  (DOI:10.3390/en16083321 — core mechanistic step)
- `[FeFe] hydrogenase —oxidizes→ reduced ferredoxin`  (DOI:10.3390/en16083321 — generic broad edge for dark ferment)
- `bifurcating [FeFe] hydrogenase —couples electron transfer from→ NADH and reduced ferredoxin`  (10.1007/s00253-023-12974-7 — strongly supported in thermophi)
- `acetate formation pathway —is tightly coupled to→ H2 production`  (10.1007/s00253-023-12974-7 — generic redox-balancing relatio)
- `high H2 partial pressure —inhibits→ H2 production`  (10.1128/aem.00634-23 — generic feedback mechanism likely bro)
- _The existing graph is skeletal (2 edges) and misses the mechanistic core: PFOR-driven ferredoxin reduction, ferredoxin-to-hydrogenase electron transfer, NADH-ferredoxin redox coupling, bifurcating hydrogenase modules, and product-coupling logic that the report identifies as generic and broadly supported._

### metabolism/lignin_degradation  — *shallow* (2 edges)
- **Missing modules:** manganese peroxidase oxidation module (Mn2+/Mn3+ cycling), β-O-4 and β-5 bond-cleavage specificity, diffusible mediator system (Mn3+, lignin-derived aromatics), downstream aromatic funneling (β-ketoadipate pathway), auxiliary ROS-handling enzymes (superoxide dismutase)
- `manganese peroxidase —oxidizes→ Mn2+`  (DOI:10.3390/polym16172388 — MnP converts Mn2+ to Mn3+)
- `Mn3+ —acts_as_diffusible_oxidant→ lignin polymer`  (DOI:10.1039/d3cc05298b — Mn3+ diffuses into lignin structure)
- `manganese peroxidase —cleaves→ β-O-4 ether linkage`  (DOI:10.1186/s13068-024-02583-5 — MnP from Irpex lacteus clea)
- `DyP-type peroxidase —cleaves→ β-5 C-C linkage`  (DOI:10.1186/s13068-023-02447-4 — Bacterial DyPB attacks both)
- `aromatic monomers —funneled_to→ β-ketoadipate pathway`  (DOI:10.1126/sciadv.adj0053 — Werner et al. show convergent c)
- `superoxide dismutase —regulates→ lignin degradation`  (DOI:10.1186/s13068-024-02470-z — SOD knockouts reduce activi)
- _The existing 2-edge graph captures basic enzyme-enabling but omits 5+ generic mechanistic modules that report details: mediator chemistry, specific bond cleavage, enzyme subtypes, ROS support, and critical downstream funneling—all METPO-grounded, cross-taxon mechanisms that belong in a mature causal graph._

### metabolism/metabolism  — *shallow* (5 edges)
- **Missing modules:** oxidative phosphorylation (electron transport chain + proton motive force + ATP synthase), substrate-level phosphorylation
- `catabolism —generates→ proton_motive_force`  (Williams 2024: reduced cofactors oxidized at membrane pumps/)
- `proton_motive_force —drives→ ATP_synthase_activity`  (Williams 2024: proton binding to ATP synthase converts elect)
- `electron_transport_chain —generates→ proton_gradient`  (Althaher 2023 DOI:10.1016/j.heliyon.2023.e22459: standard me)
- `reduced_cofactors —feeds→ electron_transport_chain`  (Williams 2024: NADH, FADH2, ferredoxin oxidized at membrane )
- `substrate_level_phosphorylation —produces→ ATP`  (Williams 2024: fewer than ten biological reactions directly )
- `electron_bifurcation —couples→ endergonic_exergonic_electron_transfer`  (Williams 2024: conserved auxiliary mechanism wherein endergo)
- _Existing graph lacks the mechanistic detail of ATP generation pathways (oxidative phosphorylation via proton motive force, substrate-level phosphorylation); these are well-supported generic mechanisms conserved across bacterial phyla, not taxon-specific uncertainties._

### metabolism/methanogenesis  — *shallow* (5 edges)
- **Missing modules:** pathway differentiation (hydrogenotrophic/acetoclastic/methylotrophic), mcrABG gene encoding, methyl-CoM reduction chemistry, coenzyme B catalytic role, coenzyme M C1-carrier role, coenzyme F420 electron donation
- `mcrABG gene cluster —enables→ methyl-coenzyme M reductase complex`  (DOI:10.1128/mmbr.00024-22 (de Mesquita 2023, pages 2-4): 'A )
- `methyl-CoM —is_reduced_by→ methyl-coenzyme M reductase complex`  (DOI:10.1128/mmbr.00024-22 (de Mesquita 2023, pages 8-11): 'm)
- `coenzyme M —carries_methyl_group_in→ methanogenesis`  (DOI:10.3389/fmicb.2023.1296008 (Khairunisa 2023, pages 10-11)
- `coenzyme B —participates_in_terminal_reduction_of→ methyl-CoM`  (DOI:10.1128/mmbr.00024-22 (de Mesquita 2023, pages 8-11): 'm)
- `coenzyme F420 —donates_electrons_to→ carbon dioxide reduction intermediate steps`  (DOI:10.3389/fmicb.2023.1296008 (Khairunisa 2023, pages 10-11)
- `acetate —serves_as_substrate_for→ acetoclastic methanogenesis`  (DOI:10.1007/s00253-023-12700-3 (Szuhaj 2023, pages 1-2): 'ac)
- _Existing graph is mechanistically skeletal: lacks gene-level representation, pathway differentiation (only hydrogenotrophic captured implicitly), and the critical Mcr cofactor chemistry (CoM, CoB, F420 participation) that is generic across all methanogenic pathways._

### metabolism/proteolysis  — *shallow* (2 edges)
- **Missing modules:** protein-to-peptide hydrolysis step, peptide import (Opp/Dpp systems), intracellular peptidase processing, size constraint rationale
- `secreted proteases —hydrolyzes→ intact extracellular proteins`  (DOI:10.1186/s43014-024-00265-1 — 'hydrolyse intact proteins )
- `extracellular proteases —produces→ peptides (oligopeptides)`  (DOI:10.1186/s43014-023-00165-w — 'producing peptides of roug)
- `peptide transporters (Opp/Dpp) —imports→ peptides`  (DOI:10.1186/s43014-023-00165-w — 'oligopeptide permease (Opp)
- `intracellular peptidases —hydrolyzes→ imported peptides`  (DOI:10.1186/s43014-023-00165-w — 'Inside the cell, multiple )
- `amino acid pool —enables→ bacterial growth on protein substrates`  (DOI:10.1186/s43014-023-00165-w — 'free amino acids used for )
- `large extracellular proteins —cannot be imported by→ prokaryotic transport systems`  (DOI:10.1128/spectrum.03036-23 — 'proteins are too large for )
- _Current graph captures only the initial enablement and final product (amino acids), missing the critical multi-step mechanism: protein hydrolysis → peptide generation → peptide import → intracellular peptidolysis. The research explicitly frames this as a coordinated four-stage system; the existing graph skips all intermediate machinery."_

### metabolism/syntrophy  — *shallow* (6 edges)
- **Missing modules:** interspecies formate transfer mechanism, direct interspecies electron transfer (DIET) pathway, DIET structural conduits (pili, multiheme cytochromes), enzymatic machinery (hydrogenase, formate dehydrogenase complexes), cell aggregation and physical proximity requirements
- `syntrophic_product_formation —transfers electrons via→ formate`  (DOI:10.1093/femsre/fuab057 (Westerholm 2022) notes formate-m)
- `direct interspecies electron transfer —bypasses→ low_hydrogen_condition`  (DOI:10.3390/fermentation9100884 (Kong 2023) reviews DIET as )
- `conductive pili —mediates→ direct interspecies electron transfer`  (DOI:10.1134/S0026261720020101 (Nozhevnikova 2020) identifies)
- `multiheme c-type cytochromes —mediates→ direct interspecies electron transfer`  (DOI:10.3390/life14050591 (Zhuang 2024) reviews outer-surface)
- `formate dehydrogenase complex —mediates→ interspecies formate transfer`  (DOI:10.1186/s40168-020-00885-y (Nobu 2020) documents formate)
- `hydrogenase complex —mediates→ interspecies hydrogen transfer`  (DOI:10.1038/s41396-023-01504-y (Singh 2023) shows hydrogenas)
- _Existing graph captures H2-mediated MIET backbone but misses formate-mediated transfer, DIET mechanisms, enzymatic machinery, and thermodynamic energy-conservation pathways that are generic, well-supported mechanisms in modern syntrophy research._

### morphology/axially_filamented  — *shallow* (6 edges)
- **Missing modules:** cell-pole anchoring of periplasmic flagella, flagellar basal body structure and collar scaffold, stator complex recruitment by collar/FlbB, filament assembly regulation (FlgV dosage control), flagellar filament composition (FlaB/FlaA), wavy/helical morphology phenotype
- `periplasmic flagella —anchored_at→ cell pole`  (DOI:10.1038/s41467-024-54806-w (Zamba-Campero 2024) — direct)
- `FlbB —forms_ring_around→ flagellar rotor`  (DOI:10.1371/journal.ppat.1012812 (Botting 2025) — cryo-ET st)
- `FlbB ring / collar —recruits→ stator complexes`  (DOI:10.1371/journal.ppat.1012812 (Botting 2025) — direct mec)
- `FlaB —is_core_component_of→ periplasmic flagellar filament`  (DOI:10.3390/biom10040550 (Nakamura 2020) — broad review cons)
- `FlgV —modulates→ flagellar filament assembly`  (DOI:10.1038/s41467-024-54806-w (Zamba-Campero 2024) — dosage)
- `periplasmic flagella —enables→ wavy/helical cell morphology`  (DOI:10.3390/biom10040550 (Nakamura 2020) — PF rotation estab)
- _Graph captures basic trait definition and simple motor-to-motility chain but omits critical generic mechanistic modules: polar anchoring, basal body collar scaffold, stator recruitment, filament assembly regulation, and morphology phenotype. High priority for enrichment with collar/FlbB-stator pathway and filament composition/assembly control._

### morphology/bacillus_shaped  — *shallow* (5 edges)
- **Missing modules:** RodA (SEDS polymerase), PBP2/MrdA (class B transpeptidase partner), RodZ (elongasome accessory factor), RodA-PBP2 conformational regulatory activation, Elongasome processivity control via RodA abundance, Peptidoglycan structure as distinct shape-determining entity
- `RodA —enables→ rod_complex`  (DOI:10.1038/s41467-023-39037-9)
- `PBP2 —enables→ rod_complex`  (DOI:10.1038/s41467-023-39037-9)
- `RodZ —maintains→ bacillus_shaped_trait`  (DOI:10.3389/fmicb.2024.1400434)
- `peptidoglycan_cell_wall —determines→ bacillus_shaped_trait`  (DOI:10.1038/s41467-023-39037-9)
- `RodA_abundance —regulates→ elongasome_processivity`  (DOI:10.1038/s41467-024-49785-x)
- `mreB —regulates→ elongasome_processivity`  (DOI:10.1038/s41467-024-49785-x)
- _The existing graph captures elongation backbone but misses RodA, PBP2, and RodZ components; regulatory layers (conformational activation, processivity control); and PG structure as distinct from synthesis—all well-supported by 2023-2024 literature and GENERIC across rod-shaped bacteria."_

### morphology/black_pigmented  — *shallow* (5 edges)
- **Missing modules:** DHN-melanin biosynthetic pathway via polyketide synthase and laccase, pyomelanin biosynthetic pathway via HppD/HmgA axis and HGA auto-oxidation, detailed DOPA pathway intermediates (dopaquinone, dopachrome, DHI, DHICA), copper cofactor requirement for tyrosinase activity
- `tyrosinase_laccase_oxidases —catalyzes conversion of→ L-tyrosine to L-DOPA`  (10.3390/ijms25053013)
- `polyketide synthase —synthesizes precursor for→ DHN-melanin pathway`  (10.3390/microorganisms12071352)
- `laccase —oxidizes and polymerizes→ DHN to melanin`  (10.3390/microorganisms12071352)
- `HppD enzyme —converts→ 4-hydroxyphenylpyruvate to homogentisic acid`  (10.1128/spectrum.00410-24)
- `accumulated homogentisic acid —auto-oxidizes and polymerizes into→ pyomelanin`  (10.1128/spectrum.00410-24)
- `copper ion —required cofactor for→ tyrosinase activity`  (10.3390/microorganisms12071352)
- _Existing graph captures only the generic DOPA/eumelanin pathway skeleton; completely missing the equally well-supported DHN-melanin and pyomelanin biosynthetic routes, which account for substantial microbial dark pigmentation mechanisms across diverse taxa._

### morphology/branched_shaped  — *shallow* (5 edges)
- **Missing modules:** DivIVA phosphorylation regulation (AfsK/SppA stress switch), membrane microdomain organization (StlP), cell-wall glycopolymer integrity (CglA), exocyst-mediated vesicle tethering (fungi), Spitzenkörper-directed secretory trafficking (fungi), septin-marked branch-site specification (fungi)
- `AfsK-mediated DivIVA phosphorylation —stimulates→ polarisome splitting and multiple new polarity centers`  (DOI:10.1093/femsml/uqad020 — constitutive AfsK activity prod)
- `cell-wall stress (bacitracin/vancomycin) —activates→ AfsK-dependent DivIVA phosphorylation`  (DOI:10.1093/femsml/uqad020 — AfsK phosphorylates DivIVA in r)
- `StlP membrane microdomain formation —enables→ normal branch spacing and polar growth fidelity`  (DOI:10.1038/s41467-025-58093-x — loss of StlP leads to branc)
- `CglA glycopolymer ligase activity —maintains→ normal hyphal cell-wall integrity and shape`  (DOI:10.1128/mbio.01492-24 — cglA deletion causes enlarged hy)
- `Cdc42/Rho GTPase signaling —targets→ exocyst complex to polarized growth sites`  (DOI:10.3390/jof10090614 — Cdc42 directs Sec3/Exo70 exocyst t)
- `exocyst-mediated vesicle tethering —enables→ directional hyphal growth and branching`  (DOI:10.3390/jof10090614 — exocyst phosphoregulation and Cdc4)
- _The existing graph captures the core Streptomyces DivIVA-polarisome-cell-wall pathway but lacks three major bacterial regulatory modules (phosphorylation control, membrane organization, glycopolymer integrity) and all conserved fungal branching machinery; enrichment with stress-response and post-translational regulation layers is warranted._

### morphology/brown_pigmented  — *shallow* (5 edges)
- **Missing modules:** HmgA regulatory branch (homogentisate 1,2-dioxygenase cataplerosis), 4-hydroxyphenylpyruvate intermediate node, oxidative intermediate (benzoquinoneacetic acid)
- `L-tyrosine —converted_to→ 4-hydroxyphenylpyruvate`  (DOI:10.1038/s41564-023-01517-5 — tyrosine aminotransferases )
- `4-hydroxyphenylpyruvate —converted_by→ hppD`  (DOI:10.1128/spectrum.00410-24 — explicit intermediate in Hpp)
- `homogentisate_1_2_dioxygenase —catabolizes→ homogentisic_acid`  (DOI:10.1128/spectrum.00410-24 — HmgA diverts HGA to maleylac)
- `homogentisic_acid —auto_oxidizes_to→ benzoquinoneacetic_acid`  (DOI:10.1128/spectrum.00410-24 — intermediate oxidation step )
- `hmgA_loss_of_function —enables_accumulation_of→ homogentisic_acid`  (DOI:10.1128/spectrum.00410-24 — G378R mutation renders HmgA )
- `benzoquinoneacetic_acid —self_polymerizes_to→ pyomelanin`  (DOI:10.1128/spectrum.00410-24 — direct polymerization after )
- _Existing graph captures phenotype cascade (HGA → pigment → color) but critically omits HmgA cataplerotic control—the genetic/regulatory lever explaining WHY HGA accumulates in pigmented strains, making the mechanism incomplete for predictive modeling or strain engineering._

### morphology/carotenoid_pigmentation  — *shallow* (5 edges)
- **Missing modules:** individual crt gene catalytic functions (crtE GGPP synthase, crtB phytoene synthase, crtI desaturase, crtY cyclase), environmental drivers of carotenoid biosynthesis (UV/light and oxidative stress → gene expression), chemical pathway intermediates (GGPP, phytoene, lycopene, β-carotene as distinct nodes), functional phenotype outcome (carotenoid-mediated oxidative stress resistance)
- `UV/light exposure —upregulates transcription of→ crtI`  (Tobin et al. 2024 (DOI:10.1007/s00253-024-13379-w) — qPCR sh)
- `oxidative stress (H2O2) —upregulates transcription of→ crtE and isoprenoid biosynthetic genes`  (Tobin et al. 2024 (DOI:10.1007/s00253-024-13379-w) — qPCR sh)
- `crtE (GGPP synthase) —catalyzes synthesis of→ GGPP`  (Li et al. 2023 (DOI:10.1038/s41467-023-42193-7) + Liu et al.)
- `crtB (phytoene synthase) —catalyzes condensation of→ GGPP to phytoene`  (Liu et al. 2024 (DOI:10.3390/molecules29174235) + Raman et a)
- `crtI (phytoene desaturase) —catalyzes sequential desaturation of→ phytoene to lycopene`  (Li et al. 2023 (DOI:10.1038/s41467-023-42193-7) — heterologo)
- `carotenoid biosynthesis products —provide antioxidant protection against→ oxidative stress (ROS)`  (Nirmala et al. 2024 (DOI:10.7759/cureus.59892) + Ma et al. 2)
- _Existing graph captures linear biosynthetic backbone but lacks mechanistic depth on individual crt gene catalytic roles, environmental sensing, and carotenoid's functional phenotype (oxidative stress resistance), missing 2+ generic modules present in 2023-2024 literature._

### morphology/cell_length_small  — *shallow* (3 edges)
- **Missing modules:** FtsZ rate-limiting divisome assembly, Min system spatial regulation of FtsZ, FtsN-mediated late divisome checkpoint, septal PG synthesis positive feedback on Z-ring, division-growth allocation dynamic, sizer-like division strategy as size-control alternative
- `FtsZ protein —rate_limiting_for→ division timing and constriction onset`  (Männik et al. 2024, DOI:10.1038/s41467-024-54242-w - FtsZ nu)
- `Min system proteins —regulates→ FtsZ ring positioning and initiation`  (Vashistha et al. 2023, DOI:10.1038/s41467-023-41487-0 - Min )
- `FtsN protein —activates→ FtsWI septal peptidoglycan synthase`  (Gong et al. 2024, DOI:10.1038/s41467-024-52217-5 - FtsN allo)
- `septal peptidoglycan synthesis —positively_feedback_to→ Z ring condensation and stability`  (Gong et al. 2024, DOI:10.1038/s41467-024-52217-5 - septal ce)
- `division-growth allocation parameter —shifts_during→ nutrient limitation to increase division relative to growth`  (Nieto et al. 2024, DOI:10.1101/2024.09.24.614723 - lambda sh)
- `sizer-like division strategy —enables→ small cell phenotype under poor media`  (Nieto et al. 2024, DOI:10.1038/s41540-024-00383-z - under po)
- _Existing graph captures only adder control mechanism; research reveals rich divisome assembly cascade (FtsZ→Min→FtsN→septal synthesis feedback) and sizer-like alternative as generic, broadly-applicable regulators of cell-length setpoints missing from current curation._

### morphology/cell_length_very_small  — *shallow* (3 edges)
- **Missing modules:** core morphogenetic machinery (FtsZ, MreB, RodZ, peptidoglycan synthesis), phosphorus limitation as selective pressure on cell miniaturization, nutrient constraint biophysics (genome+envelope fractions in very small cells)
- `FtsZ treadmilling —organizes→ septal peptidoglycan synthesis`  (DOI:10.1128/aem.02807-16 and Page 2022 (unavailable DOI) — m)
- `peptidoglycan biosynthesis machinery —constrains→ cell length`  (DOI:10.1128/mbio.03222-19 — MreB/RodZ/PBP3 system controls m)
- `phosphorus limitation —selects for→ small cell size`  (DOI:10.1128/mbio.01415-23 and DOI:10.1038/ismej.2014.60 — ol)
- `very small cell volume —increases→ genome plus envelope fraction`  (Grant 2014 (unavailable DOI, pages 115-119) — biophysical co)
- `nutrient limitation —selects for→ genome streamlining`  (DOI:10.1128/mSphereDirect.00011-19 — broad ecological associ)
- `genome streamlining —enables→ very small cell length`  (DOI:10.1038/s41467-024-48591-9 — streamlined oligotrophs (SA)
- _Existing graph captures oligotrophy-driven streamlining but lacks morphogenesis machinery and phosphorus-economy selective pressures; both are generic, well-supported mechanisms in the literature._

### morphology/cell_length  — *shallow* (5 edges)
- **Missing modules:** Min system temporal control of FtsZ ring timing and cell size, Elongasome/rod complex (MreB/RodZ/PBP2) sidewall peptidoglycan synthesis and elongation, Divisome recruitment cascade and FtsWI septal peptidoglycan synthesis machinery
- `Min_system —delays→ FtsZ_ring_initiation`  (DOI:10.1038/s41467-023-41487-0 (Vashistha 2023)
- `FtsZ_ring —recruits_and_organizes→ divisome_proteins`  (DOI:10.1038/s41579-023-00942-x (Cameron 2024 Nature Rev Micr)
- `FtsZ_membrane_tethers (FtsA/ZipA) —attach→ FtsZ_ring`  (DOI:10.1038/s41579-023-00942-x (Cameron 2024)
- `divisome_recruitment_cascade —activates→ FtsWI_septal_PG_synthases`  (DOI:10.1038/s41579-023-00942-x (Cameron 2024)
- `elongasome (MreB/RodZ/PBP2) —drives→ sidewall_peptidoglycan_synthesis`  (DOI:10.1038/s42003-024-07279-y (Hayashi 2024 Commun Biol)
- `sidewall_peptidoglycan_synthesis —promotes→ cell_length_trait`  (DOI:10.3389/fcimb.2023.1205488 (Harpring 2023)
- _Existing graph captures abstract growth → adder → division → reset backbone but omits three generic mechanistic modules highlighted in the report's expert synthesis as curation-ready: Min system temporal control, elongasome-mediated elongation, and divisome assembly-to-septal-synthesis pathway._

### morphology/cell_shape  — *shallow* (6 edges)
- **Missing modules:** elongasome Rod complex (RodZ, RodA, PBP2, MreC/MreD coordination), septal divisome synthase-driven constriction module, membrane-cell wall feedback (lipid order, cardiolipin, flotillins)
- `rod_complex —organizes→ peptidoglycan_architecture`  (10.1002/mbo3.1385 — rod complex as determinant of whole-cell)
- `septal_peptidoglycan_synthesis —drives→ septum_constriction`  (10.1126/sciadv.ade9023 — peptidoglycan synthesis as essentia)
- `membrane_lipid_order —interferes_with→ mreB_assembly`  (10.1128/jb.00433-22 — increased lipid order and cardiolipin )
- `flotillins —promote→ mreB_activity`  (10.1128/jb.00433-22 — flotillin absence downregulates MreB a)
- `rodZ —coordinates_with→ mreB`  (10.1002/mbo3.1385 — RodZ links MreB to PG synthesis and main)
- `penicillin_binding_proteins —catalyzes→ septal_peptidoglycan_synthesis`  (10.1126/sciadv.ade9023 — septal PBPs (PBP1, PBP2B) drive sep)
- _Existing graph captures peptidoglycan-MreB-FtsZ backbone but misses elongasome architecture details and membrane-wall feedback layer, both well-supported generic mechanisms in recent literature._

### morphology/cell_width_medium  — *shallow* (3 edges)
- **Missing modules:** RodA-PBP2 allosteric activation during elongasome, MreC and MreD modulatory control of PBP2, RodZ scaffolding and Rod complex integrity, Environmental stress responses (osmotic, ionic) affecting MreB filaments
- `rod_complex_pg —requires_allosteric_activation_of→ RodA-PBP2 complex`  (10.1038/s41467-023-39037-9)
- `MreC —positively_regulates→ PBP2 activation`  (10.1002/mbo3.1385)
- `MreD —modulates_activity_of→ PBP2`  (10.1002/mbo3.1385)
- `RodZ —scaffolds→ rod_complex_pg`  (10.1002/mbo3.1385)
- `environmental_stress —destabilizes→ MreB filaments`  (10.3390/microorganisms12071309)
- `potassium_influx —required_for→ MreB filament disassembly and reassembly`  (10.3390/microorganisms12071309)
- _Existing graph captures high-level MreB→PG→width pathway but omits peer-reviewed mechanistic details on RodA-PBP2 allosteric regulation, MreC/D modulation, RodZ scaffolding, and stress-responsive MreB dynamics documented across 2023–2024 literature._

### morphology/cell_width  — *shallow* (4 edges)
- **Missing modules:** class A PBP balance module, cell-wall hydrolase activity control, elongasome processivity regulation, envelope bending rigidity mechanical constraint
- `RodA-PBP2 complex —activates→ peptidoglycan polymerization and crosslinking`  (DOI:10.1038/s41467-023-39037-9 — Shlosman et al. show struct)
- `class A PBPs —balances_with→ Rod complex elongasome`  (DOI:10.1128/mbio.00475-23 — Willdigg et al. state balanced a)
- `CwlO hydrolase activity —regulates→ cell width`  (DOI:10.1128/mbio.01760-23 — Wilson et al. show ΔcwlO cells 1)
- `cell envelope bending rigidity —constrains→ cell width homeostasis`  (DOI:10.1101/2024.11.22.624946 — Kale et al. show width contr)
- `RodA abundance —regulates→ elongasome processivity`  (DOI:10.1038/s41467-024-49785-x — Middlemiss et al. show RodA)
- `MreC/MreD/RodZ accessories —regulate→ RodA-PBP2 activity`  (DOI:10.1038/s41467-023-39037-9 — Shlosman et al. identify Ro)
- _Existing graph captures the MreB-PG wall backbone, but misses recent high-confidence mechanisms for aPBP balance, hydrolase control, processivity regulation, and biophysical envelope mechanics—all generic, well-supported modules that should enrich the graph._

### morphology/curved_shaped  — *shallow* (4 edges)
- **Missing modules:** asymmetric peptidoglycan editing (Bd1075-class LD-carboxypeptidase mechanism), outer-membrane porin-lipoprotein elongasome caging (Por39/Por41/PapS module)
- `LD-carboxypeptidase activity —generates asymmetric peptidoglycan remodeling at→ outer cell curve`  (DOI:10.1038/s41467-022-29007-y (Banks et al. 2022: 'Bd1075 g)
- `asymmetric outer-curve localization —required for→ cell body curvature`  (DOI:10.1038/s41467-022-29007-y (Banks et al. 2022: 'this spe)
- `porin-PapS complex —entraps→ elongasome complexes`  (DOI:10.1038/s41467-024-51790-z (Pöhl et al. 2024: 'porin-Pap)
- `entrapped elongasome —biases growth towards→ outer cell curve`  (DOI:10.1038/s41467-024-51790-z (Pöhl et al. 2024: 'thus bias)
- `porin-PapS assembly at outer curve —stabilizes→ RodZ/elongasome localization`  (DOI:10.1038/s41467-024-51790-z (Pöhl et al. 2024: 'mNG-RodZ )
- `asymmetric outer-curve elongasome bias —generates→ curved shaped trait`  (DOI:10.1038/s41467-024-51790-z (Pöhl et al. 2024: 'promote e)
- _Existing graph captures inner-curve scaffold pathway (Caulobacter crescentin) but omits two equally generic and well-supported mechanisms: Bd1075 asymmetric PG-editing (Bdellovibrio) and porin-PapS outer-membrane caging (Rhodospirillum), published in Nature Communications 2022/2024 with quantitative evidence; adding 2-3 edges per missing pathway would complete a balanced 3-mechanism core graph._

### morphology/diplococcus_shaped  — *shallow* (4 edges)
- **Missing modules:** spatial localization machinery (LysM domains, membrane adaptors), envelope polymer substrate recognition (WTA binding), kinase-mediated regulatory coordination (StkP-LytB coupling)
- `septal peptidoglycan hydrolase —requires localization to→ septal cell division site`  (DOI:10.1038/s42003-023-04808-z - AtlA/LysM domain localizati)
- `wall teichoic acid —enables binding and positioning of→ septal peptidoglycan hydrolase`  (DOI:10.1016/j.celrep.2023.112756 - LytB C-subdomain specific)
- `membrane adaptor protein —recruits→ septal peptidoglycan hydrolase`  (DOI:10.1038/s42003-023-04808-z - AdmA deletion abolishes Atl)
- `serine threonine kinase —coordinates septal localization of→ peptidoglycan hydrolase`  (DOI:10.1016/j.celrep.2023.112756 - StkP PASTA4 domain binds )
- `loss of septal hydrolase activity —causes→ long cell chains or clumps`  (DOI:10.1016/j.celrep.2023.112756, DOI:10.1128/iai.00485-21 -)
- `regulated septal cross wall cleavage —yields→ daughter cell pair attachment`  (DOI:10.1038/ncomms4842 - emphasizes incomplete/regulated sep)
- _Existing graph captures the basic synthesis-hydrolysis-incomplete-separation backbone but omits GENERIC localization and regulatory modules (envelope polymers, adaptors, kinases) that literature identifies as critical to achieving diplococcus morphology without lysis; all suggested edges are peer-reviewed, non-taxon-specific mechanistic principles well-supported by 2023-2024 publications._

### morphology/disc_shaped  — *shallow* (3 edges)
- **Missing modules:** CetZ1-mediated cytoskeletal regulation of rod formation, S-layer glycoprotein processing and lipid anchoring (ArtA/PssA/PssD), Trace element availability and environmental sensing, Growth-phase-dependent morphological switching
- `CetZ1 —required for→ rod cell formation`  (10.1038/nature13983 (Duggin et al. 2015))
- `loss of CetZ1 function —promotes→ disc shaped`  (10.1099/mic.0.001012 (de Silva et al. 2021) — CetZ1 knockout)
- `archaeosortase A (ArtA) activity —required for→ stable plate-shaped cell formation`  (10.1099/mic.0.001012 (de Silva et al. 2021) — ArtA is requir)
- `S-layer glycoprotein processing and lipid anchoring —enables→ disc shaped`  (10.1099/mic.0.001012 (de Silva et al. 2021) — S-layer glycop)
- `trace element availability —promotes→ disc shaped`  (10.1099/mic.0.001012 (de Silva et al. 2021) — Trace element )
- `late log/stationary phase growth —promotes dominance of→ disc shaped`  (10.1099/mic.0.001012 (de Silva et al. 2021))
- _Existing graph captures anisotropic envelope growth but omits the strongest generic mechanisms: CetZ1-mediated cytoskeletal regulation (foundational for disc-vs-rod switching), S-layer biogenesis via ArtA/PssA/PssD, and environmental/developmental drivers (trace elements, growth phase). Report explicitly warns against taxon-specific confounders (plasmids, selection markers, hdrB) which are correctly excluded._

### morphology/filament_shaped  — *shallow* (5 edges)
- **Missing modules:** division-arrest filamentation (SOS/SulA/FtsZ inhibition), cell-wall glycopolymer control (CglA), polarisome phosphorylation regulation (AfsK/SppA), c-di-AMP osmotic signaling
- `DNA damage —activates→ SOS response`  (DOI:10.1002/advs.202203260 (yu2023plasmidscanshift))
- `SOS response —induces→ SulA`  (DOI:10.1002/advs.202203260 — SOS response upregulates SulA e)
- `SulA —inhibits→ FtsZ polymerization`  (DOI:10.1002/advs.202203260 + DOI:10.1073/pnas.2317322121 — S)
- `FtsZ inhibition —causes→ filament shaped`  (DOI:10.1002/advs.202203260 — Blocked septation leads to non-)
- `CglA —mediates→ cell-wall glycopolymer attachment`  (DOI:10.1128/mbio.01492-24 (bhowmick2024cellshapeand) — CglA )
- `AfsK —phosphorylates→ DivIVA`  (DOI:10.1093/femsml/uqad020 (bhowmick2023osmoticstressrespons)
- _Existing graph captures Streptomyces polar-growth mechanism well (5 edges) but omits the entire generic division-arrest filamentation pathway (SOS/SulA/FtsZ), glycopolymer control, and polarisome phosphorylation regulation—all documented as broadly-applicable in the report._

### morphology/flagellar_arrangement  — *shallow* (2 edges)
- **Missing modules:** landmark-mediated polar anchoring (HubP/FimV-FlhF), direct rotor component recruitment (FliF/FliG/FliM/FliN assembly ordering), FlhG negative regulation of FlhF GTPase activity, c-di-GMP-TipF signaling (Caulobacter landmark pathway), domain-level mechanistic detail (FlhF NG/B-domain interactions)
- `FlhF —anchors to→ HubP/FimV polar landmark protein`  (DOI:10.1038/s41467-024-50274-4)
- `FlhF B-domain/FID —binds→ FliG`  (DOI:10.1038/s41467-024-50274-4)
- `FlhF-bound FliG —recruits→ FliF MS-ring protein`  (DOI:10.1038/s41467-024-50274-4)
- `FlhG —stimulates GTPase activity of→ FlhF`  (DOI:10.1038/s41467-024-50274-4)
- `c-di-GMP —stabilizes→ TipF`  (DOI:10.1093/femsre/fuv034)
- `TipF —recruits→ basal-body building blocks (FliF/FliG/FliM)`  (DOI:10.1093/femsre/fuv034)
- _Existing graph captures high-level FlhF/FlhG regulation but lacks mechanistic detail on polar landmark anchoring, rotor recruitment chain, GTPase feedback, and the alternative Caulobacter landmark pathway—generic mechanisms well-documented in recent literature._

### morphology/gram_variable  — *shallow* (4 edges)
- **Missing modules:** stress-response regulation module, autolysin-mediated peptidoglycan degradation pathway, VBNC / cell-wall-deficient state as mechanistic intermediate
- `nutrient starvation —induces→ VBNC state`  (Carvalho et al. 2024 Nature Communications 10.1038/s41467-02)
- `stress response regulator —promotes→ autolysin activity`  (Carvalho et al. 2024 Nature Communications 10.1038/s41467-02)
- `autolysin activity —causes→ peptidoglycan degradation`  (Carvalho et al. 2024 Nature Communications 10.1038/s41467-02)
- `peptidoglycan layer thickness —determines→ crystal violet-iodide complex retention`  (Choi et al. 2024 Microbiology Spectrum 10.1128/spectrum.0073)
- `VBNC state —manifests as→ cell wall-deficient morphology`  (Carvalho et al. 2024 Nature Communications 10.1038/s41467-02)
- `cell wall-deficient population —produces→ mixed gram staining phenotype`  (Carvalho et al. 2024 Nature Communications 10.1038/s41467-02)
- _Existing graph captures aging-driven peptidoglycan thinning backbone but lacks stress-response regulation, autolysin degradation, and VBNC state as mechanistic intermediates; recent 2024 peer-reviewed literature (Carvalho Nature Comms, Choi Microbiology Spectrum) provides strong generic evidence for these modules warranting enrichment."_

### morphology/green_pigmented  — *shallow* (4 edges)
- **Missing modules:** quorum sensing regulatory layer (las/rhl/pqs), pyoverdine fluorescent siderophore biosynthesis, iron limitation environmental trigger, NahK upstream regulator of phenazine output
- `las_quorum_sensing_system —positively_regulates→ phz1_operon`  (DOI:10.1128/jb.00276-23)
- `pyoverdine —exhibits_fluorescence→ blue_green_to_yellow_green_under_UV_excitation`  (DOI:10.1101/2024.04.26.591271)
- `pvdL_pvdI_pvdJ_pvdD —catalyze→ pyoverdine_biosynthesis`  (DOI:10.3390/ijms25116013)
- `iron_limitation —induces_expression_of→ pyoverdine_biosynthetic_enzymes`  (DOI:10.3390/ijms25116013)
- `nahk —represses_or_modulates→ pyocyanin_production`  (DOI:10.1128/jb.00276-23)
- `pqsR —activates→ pqsA_pqsE_operon`  (DOI:10.1128/jb.00138-24)
- _Existing graph captures only the pyocyanin biosynthetic chain; literature reports green pigmentation as a composite phenotype requiring both pyocyanin (phz pathway) and pyoverdine (NRPS fluorescence), with substantial quorum-sensing and environmental regulation that is nearly absent from the current graph structure._

### morphology/heterocyst  — *shallow* (3 edges)
- **Missing modules:** environmental trigger (nitrogen deprivation), regulatory hierarchy (NtcA/HetR/FurC), envelope structure (Hgl/Hep layers), oxygen protection mechanisms (PSII suppression, respiratory oxidases, Flv3B, Hup), heterocyst spacing/patterning control (PatS/HetN)
- `combined nitrogen deprivation —triggers→ heterocyst differentiation`  (Heterocysts are terminally differentiated N2-fixing cells th)
- `2-oxoglutarate —signals_to→ NtcA transcription factor`  (2-OG is a C/N-status signal that activates NtcA-dependent N )
- `HetR —positively_regulates→ heterocyst differentiation`  (HetR is the master regulator of heterocyst development (DOI:)
- `FurC/PerR —binds_and_regulates→ hetR promoter`  (EMSA assays detected FurC binding to both distal (S1) and pr)
- `heterocyst glycolipid layer (Hgl) —reduces_diffusion_of→ oxygen`  (The inner heterocyst-specific glycolipid layer (HGL) reduces)
- `respiratory terminal oxidases (Cox/Cyd) —consume→ oxygen`  (Heterocysts establish microoxic conditions using respiratory)
- _Existing graph captures the core functional chain but omits essential regulatory inputs (NtcA/HetR/FurC), structural determinants (envelope layers), and oxygen-scavenging mechanisms well-documented in recent primary literature; these are generic, broadly-applicable mechanistic modules._

### morphology/monotrichous  — *shallow* (2 edges)
- **Missing modules:** polar landmark-mediated basal-body recruitment, FlhF-FlhG polar placement and number control module, assembly checkpoint mechanism (FlhF-bound FliG progression)
- `FlhF —recruits→ FliG to polar flagellar basal body`  (10.1038/s41467-024-50274-4)
- `FlhG —regulates numerosity of→ polar flagella per cell`  (10.1128/jb.00110-23)
- `HubP/FimV polar landmark —anchors→ FlhF at cell pole`  (10.1038/s41467-024-50274-4)
- `FlhF-bound FliG —prevents assembly of→ C-ring FliM/FliN interaction`  (10.1038/s41467-024-50274-4)
- `FlhG —stimulates GTPase activity of→ FlhF`  (10.1038/s41467-024-50274-4)
- `polar flagellar basal body —localized by→ HubP/FimV-FlhF-FlhG module`  (10.1093/femsre/fuv034)
- _Existing graph captures phenotypic definition but lacks the conserved FlhF-FlhG-HubP-FliG regulatory module that controls polar placement and restricts numerosity to one flagellum; high-confidence mechanism from 2024 Nature Communications and consistent with 2015 and 2023 peer-reviewed sources, generic across polar-flagellated bacteria."_

### morphology/motility  — *shallow* (5 edges)
- **Missing modules:** T4P extension/retraction motors (PilB, PilT, PilU), Pil-Chp chemosensory coupling to cAMP/Vfr, c-di-GMP second-messenger regulation, Gliding mechanistic detail (GldLM, SprB, Myxococcus bFACs), Archaeal motility systems (archaellum, Aap pili)
- `PilB —drives_extension_of→ type IV pilus`  (DOI:10.1128/jb.00359-24 (Roberge & Burrows 2024: PilB as hex)
- `PilT —drives_retraction_of→ type IV pilus`  (DOI:10.1128/jb.00359-24 (Roberge & Burrows 2024: PilT as ant)
- `type IV pilus retraction —generates→ twitching motility`  (DOI:10.1128/jb.00442-23 (Geiger et al. 2024: T4P retraction )
- `Pil-Chp system —increases→ cAMP`  (DOI:10.1128/jb.00359-24 (Roberge & Burrows 2024: PilG→CyaB→c)
- `elevated c-di-GMP —reduces→ motility`  (DOI:10.1038/s41467-024-46149-3 (Zhan et al. 2024: iron-IsmP-)
- `archaellum —enables→ archaeal swimming motility`  (DOI:10.1038/s41467-024-50277-1 (Sofer et al. 2024: archaellu)
- _Existing graph captures three locomotory modes and ion-motive-force coupling but misses T4P mechanics, chemosensory integration, c-di-GMP regulation, and archaeal systems; high-priority enrichment with 13+ generic edges from 2023-2024 literature._

### morphology/non_motile  — *shallow* (3 edges)
- **Missing modules:** c-di-GMP regulatory repression switch, transcriptional regulator repression (FleQ, OmpR, CdsR), FlhF-mediated flagellar localization coupling to c-di-GMP, motor/stator protein (MotAB) structural loss
- `high c-di-GMP levels —represses→ flagellar gene expression`  (DOI:10.1128/jb.00365-23 (Oladosu 2024) demonstrates FleQ-med)
- `OmpR response regulator —represses→ flhDC master operon`  (DOI:10.1038/s41598-024-76694-2 (Zhang 2024) and DOI:10.3390/)
- `STM0435 c-di-GMP effector —inhibits→ flagellar biogenesis`  (DOI:10.1080/21505594.2024.2331265 (Dai 2024) demonstrates me)
- `WspR diguanylate cyclase activity —increases→ c-di-GMP levels`  (DOI:10.1128/aem.01548-23 (Guan 2024) shows WspR phosphorylat)
- `absent motor proteins (MotAB/MotC) —prevents→ flagellar rotation and propulsion`  (DOI:10.3389/fmicb.2024.1456637 (Carter 2024) implicates motB)
- `flhF deletion or mutation —causes→ flagellar mislocalization and diminished motility`  (DOI:10.1128/aem.01548-23 (Guan 2024) demonstrates flhF-knock)
- _The existing graph captures structural apparatus absence but lacks three major generic regulatory modules: c-di-GMP switching, transcriptional repression, and flagellar localization-to-regulation coupling that 2024 literature emphasizes as broadly-applicable mechanisms for non-motile phenotypes."_

### morphology/orange_pigmented  — *shallow* (5 edges)
- **Missing modules:** isoprenoid precursor supply (FPP/GGPP), intermediate carotenoid metabolites (phytoene, lycopene, β-carotene), individual Crt enzyme steps (CrtE, CrtB, CrtI, CrtY, CrtZ), C30 vs C40 pathway distinction, carotenoid protective function (ROS/UV stress response)
- `isoprenoid precursor pathways —supplies→ farnesyl diphosphate (FPP)`  (DOI:10.1080/1040841X.2025.2526423)
- `farnesyl diphosphate —is_substrate_for→ crtM (dehydrosqualene synthase)`  (DOI:10.7759/cureus.59892)
- `phytoene —is_converted_by→ crtI (phytoene desaturase)`  (DOI:10.3390/pathogens12010086)
- `lycopene —is_converted_by→ crtY (lycopene cyclase)`  (DOI:10.3390/microorganisms11030614)
- `beta-carotene —is_substrate_for→ crtZ (beta-carotene hydroxylase)`  (DOI:10.3390/microorganisms11030614)
- `orange carotenoid accumulation —provides_protection_against→ oxidative stress and UV radiation`  (DOI:10.7759/cureus.59892, DOI:10.3389/fmicb.2024.1447785)
- _Existing graph captures assay readout but lacks mechanistic scaffolding; missing isoprenoid precursor supply, intermediate metabolites (phytoene/lycopene/β-carotene), individual Crt enzyme steps, and protective function—all documented as generic mechanisms in literature."_

### morphology/oval_shaped  — *shallow* (5 edges)
- **Missing modules:** DivIVA-STK-MltG regulatory cascade for peripheral PG synthesis termination, GpsB-mediated PBP spatial localization control (taxon: S. aureus), MreC/Pbp2B/RodA peripheral elongasome-like system, MltG hydrolase coordination
- `DivIVA —positively regulates→ peripheral peptidoglycan synthesis`  (DOI:10.1128/spectrum.04750-22)
- `STK serine/threonine kinase —phosphorylates→ DivIVA`  (DOI:10.1128/spectrum.04750-22)
- `phosphorylated DivIVA —mislocalizes→ MltG`  (DOI:10.1128/spectrum.04750-22)
- `MltG —negatively regulates→ peripheral peptidoglycan synthesis`  (DOI:10.1128/spectrum.04750-22)
- `MreC —enables→ peripheral peptidoglycan synthesis`  (DOI:10.1038/s41467-023-38904-9)
- `RodA —enables→ peptidoglycan synthesis at septal sidewall`  (DOI:10.1128/mbio.03235-23)
- _Existing graph captures PG dichotomy and divisome backbone but omits 4 critical generic mechanistic modules: DivIVA-STK-MltG regulatory cascade (strong primary evidence in S. suis), GpsB-PBP localization control, extended PBP/RodA system, and MltG hydrolase coordination._

### morphology/pleomorphic_shaped  — *shallow* (3 edges)
- **Missing modules:** Excess membrane synthesis driving pleomorphic L-form proliferation, Peptidoglycan/cell-wall precursor inhibition as primary trigger to L-form state, Oxidative stress as major negative constraint on wall-free growth
- `Peptidoglycan precursor synthesis inhibition —causes transition to→ L-form / cell-wall-deficient state`  (DOI:10.1098/rstb.2015.0494 (Errington et al. 2016): 'repress)
- `Excess membrane synthesis —drives proliferation of→ pleomorphic wall-free L-forms via blebbing/vesiculation`  (DOI:10.1098/rstb.2015.0494 (Errington et al. 2016): 'increas)
- `Increased surface area-to-volume ratio from elevated membrane synthesis —enables→ blebbing-tubulation-scission proliferation of pleomorphic L-forms`  (DOI:10.1042/bst20160435 (Errington 2017): 'This proliferatio)
- `Oxidative stress / ROS from respiratory chain —limits growth of→ wall-deficient protoplasts / L-forms`  (DOI:10.1016/j.tim.2019.07.008 (Claessen & Errington 2019): ')
- `Loss of cell wall —causes→ spherical or pleomorphic morphology in bacteria`  (DOI:10.3390/bioengineering11010081 (Tian et al. 2024): 'rod-)
- `Osmoprotective / high-osmolarity growth medium —enables survival and growth of→ pleomorphic L-forms`  (DOI:10.1042/bst20160435 (Errington 2017): 'They grow robustl)
- _Existing graph captures the broad principle (shape-control loss → variable geometry → pleomorphism) but lacks mechanistic depth: missing are the membrane-synthesis drive for L-form proliferation, upstream PG-precursor inhibition, oxidative-stress constraint, and osmoprotective-environment enablement—all well-supported across diverse bacteria in the literature._

### morphology/polyphosphate_granule  — *shallow* (2 edges)
- **Missing modules:** PPK1 synthesis pathway, PPX degradation pathway, starvation-induced accumulation trigger, phosphate mobilization/release mechanism, environmental/redox modulation of polyP cycling
- `polyphosphate kinase 1 (PPK1) —synthesizes→ inorganic polyphosphate`  (DOI:10.1371/journal.pbio.3002558 — Baijal et al. (2024) PLOS)
- `exopolyphosphatase (PPX) —degrades→ inorganic polyphosphate`  (DOI:10.1371/journal.pbio.3002558 — Baijal et al. (2024) PLOS)
- `nutrient downshift / starvation —increases→ PPK-dependent polyP accumulation`  (DOI:10.1371/journal.pbio.3002558 — Baijal et al. (2024): 'sh)
- `aerobic conditions in EBPR biofilms —increases→ phosphate uptake and polyP synthesis`  (DOI:10.2166/wst.2024.314 — Villard et al. (2024): 'PAOs take)
- `anaerobic conditions in EBPR biofilms —increases→ polyP hydrolysis and phosphate release`  (Retrieved without stable DOI — Ruiz-Haddad et al. (2024) Env)
- `inorganic polyphosphate —mobilizes phosphate→ orthophosphate (Pi)`  (DOI:10.1146/annurev.biochem.77.083007.093039 — Rao et al. (2)
- _Graph captures trait and basic storage function but lacks the core enzymatic pathways (PPK synthesis, PPX degradation), environmental triggers (starvation, EBPR redox cycling), and phosphate mobilization mechanism—all generic, canonical mechanisms well-supported across the literature._

### morphology/prosthecate  — *shallow* (2 edges)
- **Missing modules:** phosphate starvation sensing and signal transduction, peptidoglycan synthesis machinery (BacA/BacB/PbpC/MreB/RodA), stalk crossband structure (StpABCD), developmental differentiation state (swarmer-to-stalked transition)
- `phosphate starvation —triggers differentiation to→ stalked cell state`  (DOI:10.1371/journal.pgen.1010882 (Hallgren et al., 2023))
- `cytoplasmic phosphate level —controls→ stalk elongation`  (DOI:10.1038/s42003-024-06469-y (Billini et al., 2024))
- `BacA/BacB bactofilins —recruit→ PbpC cell wall synthase`  (DOI:10.1128/jb.00384-22 (Barrows & Goley, 2023))
- `MreB cytoskeleton —required for→ stalk formation`  (DOI:10.1128/jb.00384-22 (Barrows & Goley, 2023))
- `(p)ppGpp alarmone level —permits→ swarmer-to-stalked differentiation`  (DOI:10.1371/journal.pgen.1010882 (Hallgren et al., 2023))
- `stalk crossbands (StpABCD) —limit→ diffusion along stalk`  (DOI:10.1128/jb.00384-22 (Barrows & Goley, 2023))
- _Existing graph captures headline trait→function but misses the nutrient-sensing regulatory scaffold and core cell-envelope synthesis machinery that drive stalk morphogenesis in oligotrophic environments; taxon-specific edges (e.g., NtrC, holdfast attachment) correctly excluded from generic graph._

### morphology/red_pigmented  — *shallow* (4 edges)
- **Missing modules:** prodiginine gene cluster (Pig/Red) enablement, precursor biosynthesis (MBC and MAP pathways), carotenoid alternative mechanism (GGPP→phytoene→lycopene), CpxA/CpxR negative regulation, environmental modulation (light/ROS stress)
- `prodiginine gene cluster —enables→ prodiginine biosynthesis`  (10.3390/microorganisms11122920 (barreto2023: gene clusters l)
- `MBC + MAP condensation —produces→ prodigiosin`  (10.20944/preprints202310.0121.v1 (barreto2023: bifurcated pa)
- `GGPP —substrate_for→ carotenoid biosynthesis`  (10.3390/microorganisms11122920 (barreto2023: phytoene syntha)
- `lycopene —confers_color→ red pigmentation`  (10.3390/microorganisms11122920 (barreto2023: lycopene is a r)
- `CpxA/CpxR system —inhibits_transcription_of→ prodiginine gene cluster`  (10.3389/fmicb.2024.1412776 (lu2024: CpxA/CpxR activation inh)
- `oxidative stress (ROS) —increases→ carotenoid synthesis`  (10.3389/ffunb.2024.1378590 (mosqueda2024: oxidative metaboli)
- _Existing prodiginine path is accurate but incomplete; entirely missing carotenoid mechanism (equally generic), upstream gene cluster + precursor nodes, and regulatory control points that are broadly applicable across taxa._

### morphology/spiral_shaped  — *shallow* (4 edges)
- **Missing modules:** outer membrane porin-lipoprotein caging module, periplasmic flagella cell-body distortion module, specific PG-remodeling enzymes (Pgp1/Pgp2/bactofilin/M23 peptidases), LPS envelope biosynthesis secondary stabilization
- `PG_hydrolases_Pgp1_Pgp2 —alters→ muropeptide_crosslinking_profile`  (DOI:10.3389/fmicb.2023.1162806 - Frirdich et al. show Pgp1/P)
- `outer_membrane_porin_PapS_complex —entraps_and_concentrates→ elongasome_RodZ_complexes`  (DOI:10.1038/s41467-024-51790-z - Pöhl et al. 2024 Nature Com)
- `elongasome_outer_curve_localization_bias —produces→ anisotropic_cell_wall_growth_curvature`  (DOI:10.1038/s41467-024-51790-z - ~15% outer-curve growth bia)
- `periplasmic_endoflagella —distorts_and_shapes→ spiral_cell_body`  (DOI:10.1038/s41467-024-54806-w - Zamba-Campero et al. 2024 N)
- `FlgV_flagellar_assembly_component —required_for→ periplasmic_flagellar_filament_assembly`  (DOI:10.1038/s41467-024-54806-w - FlgV deletion causes fewer/)
- `LPS_glycosyltransferase_activity —maintains→ helical_morphology_stability`  (DOI:10.3390/ijms241411381 - Tang et al. 2023: LPS gene delet)
- _Existing graph captures core PG-scaffold mechanism but is incomplete: misses 2024 outer-membrane patterning module (novel curvature-caging mechanism), spirochete flagellar pathway, and LPS envelope contribution; report flags spirochetes as mechanistically distinct but worth including as separate sub-module per curation guidance._

### morphology/spirochete_shaped  — *shallow* (4 edges)
- **Missing modules:** flagellar hook mechanical integrity (FlgE + Lal crosslink), FlgV-mediated flagellar assembly regulation, flagellar basal body organizing assembly, motility as functional intermediate between flagella rotation and morphology
- `FlgE —stabilized_by→ Lal_crosslink`  (Lynch et al. 2023, DOI:10.1093/pnasnexus/pgad349 — Lal cross)
- `Lal_crosslink —required_for→ motility`  (Lynch et al. 2023, DOI:10.1093/pnasnexus/pgad349 — Direct mu)
- `FlgV —modulates→ periplasmic_flagella_assembly`  (Zamba-Campero et al. 2024, DOI:10.1038/s41467-024-54806-w — )
- `flagellar_basal_body —organizes→ periplasmic_flagella_assembly`  (Zamba-Campero et al. 2024, DOI:10.1038/s41467-024-54806-w)
- `FlgE —transmits_force→ periplasmic_flagella_rotation`  (Nakamura & Minamino 2024, DOI:10.3390/biom14121488 — Hook is)
- `periplasmic_flagella_rotation —enables→ spirochete_shaped_morphology`  (Lynch et al. 2023, DOI:10.1093/pnasnexus/pgad349)
- _Existing graph captures core flagella-body-morphology principle but misses 2024 discoveries (FlgV regulation) and 2023 hook mechanics (Lal crosslink); adding hook and FlgV nodes would elevate from skeletal to adequate._

### morphology/spore_forming  — *shallow* (5 edges)
- **Missing modules:** sporulation initiation and phosphorelay (Spo0A master regulator and sensor kinases), sigma-factor developmental cascade (σF→σE→σG→σK), forespore engulfment regulation (spoIID/spoIIM/spoIIP genes and mother-cell membrane dynamics), nutrient limitation sensing upstream of sporulation initiation
- `Spo0A~P (phosphorylated Spo0A) —positively regulates→ sporulation initiation program`  (DOI:10.3390/microbiolres14020035 (Guerrero 2023))
- `sporulation sensor kinases —phosphorylate→ Spo0F`  (DOI:10.3390/microbiolres14020035 (Guerrero 2023))
- `Spo0F~P —transfers phosphoryl group to→ Spo0B`  (DOI:10.3390/microbiolres14020035 (Guerrero 2023))
- `Spo0B —phosphorylates→ Spo0A`  (DOI:10.3390/microbiolres14020035 (Guerrero 2023))
- `sigma factor σF —precedes and enables stage leading to→ sigma factor σE`  (DOI:10.3390/microbiolres14020035 (Guerrero 2023))
- `spoIID protein —required for→ forespore engulfment`  (DOI:10.3390/microbiolres14020035 (Guerrero 2023))
- _Existing graph captures final morphogenetic assembly (forespore → cortex/coat/DPA → resistant spore) but entirely omits the foundational regulatory initiation network (master regulator Spo0A, phosphorelay, sigma cascade) that controls whether sporulation occurs; high-priority expansion needed to represent complete generic mechanism._

### morphology/spore_shaped  — *shallow* (5 edges)
- **Missing modules:** sporulation entry control (Spo0A-driven phosphorelay), sigma factor cascade (σE, σF, σG, σK regulatory phases), coat morphogenetic protein scaffolds (SpoIVA tether, SafA/CotE organizers, SpoVM/SpoVID encasement drivers), encasement process (distinct from generic coat assembly)
- `Spo0A phosphorylation —positively regulates→ sporulation initiation`  (10.1371/journal.ppat.1012507)
- `sporulation initiation —enables→ forespore engulfment`  (10.1038/nrmicro2921 — Spo0A-driven sigma cascade controls mo)
- `SpoIVA —anchors→ coat to forespore membrane`  (10.1038/nrmicro2921)
- `SafA —required for assembly of→ inner coat layer`  (10.1038/nrmicro2921)
- `CotE —required for assembly of→ outer coat layer`  (10.1038/nrmicro2921)
- `SpoVM and SpoVID —required for→ spore encasement`  (10.1038/nrmicro2921 — morphological transition from cap to f)
- _Existing graph captures structural outcome (layers → mature spore) but omits upstream sporulation entry control (Spo0A phosphorelay) and critical coat morphogenetic protein scaffolds (SpoIVA, SafA, CotE, SpoVM, SpoVID), which the report emphasizes as generic, broadly-conserved mechanisms._

### morphology/sporulation  — *shallow* (7 edges)
- **Missing modules:** phosphorelay cascade (KinA/B→Spo0F→Spo0B→Spo0A~P), translational control (EF-P upstream regulator), forespore engulfment step, sigma-cascade compartmentalization (SigH entry, SigG/SigK late functions), spore structural maturation (coat/cortex deposition)
- `EF-P —positively regulates expression of→ spo0a_phosphorelay`  (10.1128/jb.00370-22 — shows lower spo0A expression in Δefp m)
- `spo0a_phosphorelay —activates→ compartment_sigma_factors (SigH)`  (10.1128/jb.00370-22 — Spo0A in conjunction with stationary-p)
- `asymmetric_septation —produces→ forespore_engulfment`  (10.1038/s41467-024-51654-6 — asymmetric division followed by)
- `compartment_sigma_factors (SigG) —drives→ spore_DNA_protection`  (10.1038/s41467-024-51654-6 — σG drives spore maturation and )
- `compartment_sigma_factors (SigK) —controls→ spore_coat_cortex_maturation`  (10.1038/s41467-024-51654-6 — σK controls spore coat and cort)
- `spore_coat_cortex_maturation —confers→ heat_and_chemical_resistance`  (10.1038/s42003-024-06521-x — deposition of cortex, coat, and)
- _Existing graph captures the developmental backbone (stress→Spo0A→septation→sigma→forespore→spore) but lacks phosphorelay detail, translational control entry, forespore engulfment sequence, sigma-cascade specificity (SigH/SigG/SigK roles), and structural-to-phenotype linkage; enrichment should prioritize generic, universally-supported modules while respecting taxon constraints noted in the report._

### morphology/staphylococcus_arrangement  — *shallow* (2 edges)
- **Missing modules:** FacZ-GpsB division-site regulation, Atl-mediated daughter-cell separation, Noc-driven nucleoid occlusion in perpendicular Z-ring placement
- `FacZ —prevents aberrant placement of→ FtsZ cytokinetic rings`  (DOI:10.1038/s41564-024-01607-y (Bartlett et al. 2024 Nature )
- `FacZ —interacts with→ GpsB`  (DOI:10.1038/s41564-024-01607-y (Bartlett et al. 2024))
- `GpsB —promotes lateral interactions between→ FtsZ filaments`  (DOI:10.1038/s41564-024-01607-y (Bartlett et al. 2024))
- `Atl autolysin —promotes→ daughter-cell separation`  (DOI:10.1146/annurev-micro-102215-095657 (Eswara & Ramamurthi)
- `Noc —promotes perpendicular placement of→ FtsZ Z-rings`  (Monteiro 2018, Kent 2013 (peer-reviewed synthesis/thesis))
- `FtsZ Z-ring —organizes→ divisome peptidoglycan synthesis machinery`  (DOI:10.1038/s41564-024-01607-y (Bartlett et al. 2024))
- _Existing graph has bare 3-node backbone (division planes + trait); reports identifies four well-supported generic modules (FacZ-GpsB, Atl separation, Noc occlusion, FtsZ divisome) absent from current model._

### morphology/star_shaped  — *shallow* (3 edges)
- **Missing modules:** bactofilin cytoskeleton (BacA-family) spatial organizer, BacA–LmdC module (bactofilin–M23 endopeptidase conserved pair), zonal peptidoglycan insertion zones (constrained growth at stalk base, tip, bud neck), apical/tip growth and PG incorporation, SpmX-mediated developmental positioning of PG synthesis, PG remodeling/hydrolysis step (M23 endopeptidases, LD-transpeptidases), PbpC bifunctional PBP recruitment by bactofilins
- `bactofilin BacA —localizes_to→ stalk base`  (DOI:10.7554/eLife.86577.2 — direct experimental evidence in )
- `BacA —interacts_with→ LmdC (M23 endopeptidase)`  (DOI:10.7554/eLife.86577.2 — direct biochemical binding)
- `BacA–LmdC module —promotes→ local peptidoglycan remodeling`  (DOI:10.7554/eLife.86577.2 — explicit mechanistic synthesis)
- `zonal peptidoglycan insertion —occurs_at→ stalk base and stalk tip and bud neck`  (DOI:10.32469/10355/79574 — four distinct PG insertion zones )
- `loss of BacA —causes→ unconstrained peptidoglycan incorporation and bulging extensions`  (DOI:10.1101/2023.02.27.530196 — direct mutant phenotype in H)
- `PG incorporation —localizes_to→ hyphal tips (apical growth)`  (DOI:10.1371/journal.pgen.1010788 — HADA labeling in Rhodomic)
- _The existing graph captures the phenotypic endpoint (radiating projections → star shape) and acknowledges multi-site polar growth, but omits all the generic, conserved mechanistic machinery (bactofilin scaffolds, spatial positioning, zonal growth zones, PG remodeling enzymes) that the 2023–2024 literature shows are essential and applicable across prosthecate alphaproteobacteria, making the graph too phenotypic and incomplete for mechanistic curation._

### morphology/streptococcus_arrangement  — *shallow* (2 edges)
- **Missing modules:** incomplete septum splitting / daughter-cell separation failure (central mechanistic step), peptidoglycan hydrolase activation and remodeling (FtsEX-PcsB and autolysins), lipoteichoic acid (LTA) and its role in septa placement
- `incomplete septum splitting / daughter-cell separation —causes→ streptococcus arrangement`  (DOI:10.1128/mSphere.00119-21 (Tan et al. 2021, pages 11-13):)
- `FtsEX complex —enables→ PG hydrolase-mediated septum splitting`  (DOI:10.1128/mSphere.00119-21 (Tan et al. 2021, pages 11-13):)
- `PG hydrolase activity (including FtsEX-PcsB) —promotes→ daughter-cell separation`  (DOI:10.3389/fmicb.2021.737396 (Briggs et al. 2021, pages 7-9)
- `lipoteichoic acid (LTA) —promotes→ proper septa placement and cell division`  (DOI:10.1186/s13567-024-01287-w (Payen et al. 2024, pages 239)
- `residual septal peptidoglycan —increases→ chain length`  (DOI:10.1128/mSphere.00119-21 (Tan et al. 2021, pages 11-13):)
- `secretion chaperones (PrsA/SlrA/HtrA) —affects abundance of→ cell wall remodeling proteins (LytA/LytB, MapZ, EzrA)`  (DOI:10.1128/iai.00490-23 (George et al. 2024, pages 7-11): T)
- _Existing graph captures parallel division planes but misses the critical incomplete-septum-splitting mechanism and the cell-wall-polymer controls (LTA, PG hydrolases) that gate separation; recent high-quality evidence (2021-2024) supports enrichment toward a mechanistic backbone linking division-plane geometry to PG remodeling to separation failure to chains."_

### morphology/tailed_shaped  — *shallow* (3 edges)
- **Missing modules:** bactofilin cytoskeletal scaffolding and localization, stalk-base spatial confinement of PG synthesis, M23 endopeptidase-bactofilin conserved module, elongasome (MreB/RodA) localization to stalk base
- `bactofilin polymers —localize_to→ stalk base`  (DOI:10.7554/eLife.86577 (2024))
- `bactofilin —limits→ peptidoglycan biosynthesis to stalk base`  (DOI:10.7554/eLife.86577 (2024))
- `MreB —required_for→ stalk formation`  (DOI:10.1128/jb.00384-22 (2023))
- `bactofilin polymers —act_as_barrier_retaining→ cell wall biosynthetic machinery at growth zones`  (DOI:10.7554/eLife.86577 (2024))
- `phosphate limitation —induces→ stalk elongation`  (DOI:10.1128/jb.00384-22 (2023))
- `bactofilin —interacts_directly_with→ M23 endopeptidase (LmdC)`  (DOI:10.7554/eLife.86577 (2024))
- _The existing graph captures the core PG-growth-to-stalk-morphology backbone but omits critical mechanistic modules (bactofilin scaffolding, spatial confinement, M23 module) that the 2024 deep-research report identifies as generic and conserved across multiple alphaproteobacterial clades; enrichment would integrate spatial and protein-machinery details to explain HOW unipolar PG growth is organized."_

### morphology/vibrio_shaped  — *shallow* (4 edges)
- **Missing modules:** envelope-stress regulatory module (VxrAB-VadR), c-di-GMP signaling antagonism module, CrvB cofactor assembly step
- `VadR sRNA —post-transcriptionally represses→ crvA mRNA`  (DOI:10.1038/s41467-020-19890-8 — strong direct regulatory co)
- `VxrAB two-component system —activates transcription of→ VadR`  (DOI:10.1038/s41467-020-19890-8 — strong upstream regulatory )
- `cyclic di-GMP —decreases→ cell curvature`  (DOI:10.1073/pnas.2010199117 — strong direct antagonistic con)
- `CrvB —promotes higher-order assembly of→ CrvA filament`  (DOI:10.1101/2020.02.20.954503 — strong mechanistic link (pre)
- `VpsT transcription factor —inhibits→ vibrio shaped`  (DOI:10.1073/pnas.2010199117 — strong sufficiency claim for c)
- `periplasmic filament —requires→ CrvB for stable assembly`  (DOI:10.1101/2020.02.20.954503 — supports cofactor relationsh)
- _Existing graph captures only the core CrvA filament assembly mechanism; report identifies three additional GENERIC modules (envelope-stress regulation, c-di-GMP antagonism, CrvB cofactor assembly) that are broadly supported and mechanistically central to vibrio-shape control across conditions."_

### physiology/autotrophic  — *shallow* (8 edges)
- **Missing modules:** pH-dependent DIC speciation, carbon concentrating mechanism (CCM), bicarbonate transporter and uptake, carbonic anhydrase function, carboxysome compartmentalization, alternative CO2-fixation pathways, electron donor energy coupling
- `environmental_pH —determines_speciation_of→ dissolved_inorganic_carbon`  (DOI:10.1128/AEM.01557-23)
- `bicarbonate —transported_via→ bicarbonate_transporters`  (DOI:10.1111/ppl.14140)
- `carbonic_anhydrase —converts→ HCO3_to_CO2`  (DOI:10.1128/AEM.01075-24)
- `carboxysome —compartmentalizes→ CO2_fixation`  (DOI:10.1111/ppl.14140)
- `carbon_concentrating_mechanism —enhances_catalytic_efficiency_of→ RuBisCO`  (DOI:10.1128/AEM.01557-23)
- `wood_ljungdahl_pathway —example_of→ CO2_fixation_pathway`  (DOI:10.1039/D4CB00099D)
- _Existing graph captures core CO2→biomass spine but misses 7 generic mechanistic modules including pH-DIC coupling, CCM dynamics, alternative fixation pathways, and electron donor integration; excludes only taxon-specific (ιCA in Thiomicrospira), ecological (paddy soil), and engineered edges per critical rule._

### physiology/bioluminescence  — *shallow* (3 edges)
- **Missing modules:** flavin reduction module (LuxG/NADPH/FMN↔FMNH2), aldehyde substrate synthesis (LuxCDE complex with ATP/NADPH), quorum sensing regulatory circuit (LuxI/LuxR/autoinducer/density sensing)
- `LuxG flavin reductase —converts→ FMN to FMNH2`  (DOI:10.1016/j.csbj.2018.11.003 — Brodl et al. establish LuxG)
- `LuxCDE fatty acid reductase complex —supplies→ long-chain aldehyde substrate`  (DOI:10.1016/j.csbj.2018.11.003 — Brodl et al. identify LuxCD)
- `LuxI —synthesizes→ 3-oxo-C6-HSL autoinducer`  (DOI:10.1128/jb.00035-24 — Septer & Visick (2024) identify Lu)
- `LuxR bound to autoinducer —activates transcription of→ lux operon`  (DOI:10.1128/jb.00035-24 — Septer & Visick confirm LuxR-autoi)
- `cell density / autoinducer accumulation —enables sensing of→ sufficient population threshold`  (DOI:10.1128/jb.00035-24 — Septer & Visick establish autoindu)
- `NADPH —required for→ LuxC aldehyde formation`  (DOI:10.1016/j.csbj.2018.11.003 — Brodl et al. detail NADPH r)
- _Existing graph captures oxygen dependency and luciferase catalysis but lacks three generic mechanistic modules: substrate supply (flavin reduction, aldehyde synthesis) and quorum-sensing regulation, all strongly supported by peer-reviewed literature as universal in luminous bacteria._

### physiology/carboxydotrophic  — *shallow* (8 edges)
- **Missing modules:** CODH class diversity (Ni,Fe anaerobic vs Cu,Mo aerobic), Operon architecture and gene organization (cox/coo operons), CO-sensing transcriptional regulation (CooA/RcoM), Anaerobic hydrogenogenic pathway (Ni-CODH + ECH to H2), Explicit ATP synthase coupling from pmf, Electron acceptor branching (quinones/cytochrome for aerobic; H+ for anaerobic)
- `Ni,Fe-CODH —has property→ oxygen sensitive`  (Dent et al. 10.1128/jb.00332-22 (2023) — defines anaerobic c)
- `Cu,Mo-CODH —has property→ O2-tolerant`  (Dent et al. 10.1128/jb.00332-22 (2023) — distinguishes aerob)
- `coo operon —encodes→ Ni,Fe-CODH for anaerobic CO metabolism`  (Dent et al. 10.1128/jb.00332-22 (2023) — core anaerobic path)
- `cox operon —encodes→ coxMSL Mo-CODH for aerobic CO metabolism`  (Dent et al. 10.1128/jb.00332-22 (2023) — core aerobic pathwa)
- `CooA —activates transcription of→ coo operon`  (Dent et al. 10.1128/jb.00332-22 (2023) — CO-sensing regulato)
- `proton motive force —powers→ ATP synthase`  (Bährle et al. 10.1186/s40643-023-00705-9 (2023) — generic en)
- _Graph captures aerobic CO-oxidation backbone but lacks generic modules for anaerobic pathway, operon/regulatory organization, and CODH class diversity; research report emphasizes dual-mechanism carboxydotrophy (aerobic Mo-CODH vs anaerobic Ni-CODH with hydrogenogenic coupling) not fully reflected in current graph._

### physiology/catalase_activity  — *shallow* (5 edges)
- **Missing modules:** OxyR-mediated transcriptional regulation of catalase genes, KatG and KatE gene/protein nodes, AhpCF (alkyl hydroperoxide reductase) alternative scavenging system, PerR H2O2-sensing regulation, Heme biosynthesis cofactor prerequisite (HemF, ferrochelatase), H2O2 degradation capacity as measurable phenotype, Concentration-dependent switching (low vs high H2O2 enzyme preference)
- `hydrogen peroxide —activates→ OxyR`  (Intracellular H2O2 concentration ~200 nM drives OxyR into di)
- `OxyR —RO:0002212 (regulates transcription of)→ katG`  (OxyR induces katG (catalase G / catalase-peroxidase) >10-fol)
- `OxyR —RO:0002212 (regulates transcription of)→ ahpCF`  (OxyR induces ahpCF (alkyl hydroperoxide reductase system) >1)
- `katG —RO:0002327 (enables)→ catalase_activity`  (KatG protein product is catalase HPI)
- `heme biosynthesis —BFO:0000051 (has part / supports)→ KatG activation`  (Heme synthesis (HemF/ferrochelatase-dependent) is prerequisi)
- `catalase activity —RO:0002307 (contributes to)→ pathogen intracellular survival`  (Antioxidant capacity (including catalase/SOD activity) linke)
- _Existing graph captures only the direct catalase enzymatic reaction; report documents at least 4 generic, broadly-applicable mechanistic modules missing: OxyR regulation, gene-level catalase nodes, cofactor prerequisites (heme), and functional phenotypic outcomes (H2O2 degradation capacity + downstream survival), all supported by primary literature and reviews as non-taxon-specific mechanisms."_

### physiology/chemoautolithotrophic  — *shallow* (8 edges)
- **Missing modules:** CO2 fixation pathway variants (CBB, rTCA, 3HP/4HB), nitrification module (ammonia oxidation → nitrite oxidation coupling), hydrogen oxidation system (H2 → hydrogenase), sulfur oxidation pathways (sox, sqr, S4I), terminal electron acceptors beyond O2 (Fe3+, nitrate), iron oxidation specific chain (Cyc2-Rus-Cyc1-Cox), high-temperature respiration (cytochrome bd)
- `Calvin-Benson-Bassham cycle —enables→ chemoautolithotrophic carbon fixation`  (DOI:10.3390/microorganisms12030590 — Wang et al. show CBB as)
- `reverse tricarboxylic acid cycle —enables→ carbon dioxide fixation`  (DOI:10.1186/s40168-023-01712-w — Deng et al. document rTCA a)
- `inorganic electron donor —feeds electrons into→ hydrogen oxidation pathway`  (DOI:10.1186/s40168-023-01712-w — H2 described as significant)
- `molecular hydrogen —example of→ inorganic electron donor`  (DOI:10.1186/s40168-023-01712-w — Deng et al. identify H2 as )
- `thiosulfate —example of→ inorganic electron donor`  (DOI:10.3389/fmicb.2024.1426584 — Twible et al. show thiosulf)
- `respiratory chain —can accept electrons from→ nitrate`  (DOI:10.1038/s41467-024-47392-4 — Han et al. report denitrifi)
- _Existing graph captures the definitional spine (inorganic donor → respiration → ATP, CO2 fixation) but omits ~7 major generic mechanistic modules: alternative CO2-fixation pathways (CBB, rTCA, 3HP/4HB), nitrification coupling, hydrogen oxidation, sulfur-oxidation systems, iron-oxidation specifics, multiple terminal electron acceptors, and high-temperature oxidase variants—all well-supported by recent literature and broadly applicable across chemoautolithotrophic taxa._

### physiology/chemoautotrophic  — *shallow* (9 edges)
- **Missing modules:** carbon-concentrating mechanism (carboxysome + carbonic anhydrase + DIC transporters), alternative carbon fixation pathways (rTCA cycle, 3HP/4HB cycle), differentiated electron donor metabolic modules (sulfur oxidation, hydrogen oxidation, ammonia oxidation), electron transfer cofactors and ferredoxins
- `reduced_inorganic_compound —enables→ respiratory_energy_conservation`  (DOI:10.1128/AEM.01075-24)
- `carbon_dioxide —fixed_by→ carboxysome`  (DOI:10.1128/AEM.01075-24)
- `carboxysome —encapsulates→ carbonic_anhydrase`  (DOI:10.1128/AEM.01075-24)
- `dic_transporter —supplies_substrate_for→ carbon_concentrating_mechanism`  (DOI:10.1128/AEM.01075-24)
- `reverse_tca_cycle —enables→ inorganic_carbon_assimilation`  (DOI:10.3390/life13030627)
- `3hp_4hb_cycle —enables→ inorganic_carbon_assimilation`  (DOI:10.1038/s42003-024-06432-x)
- _Graph captures basic energy-to-Calvin-Benson scaffold but lacks carbon-concentrating mechanism structure, alternative pathways (rTCA, 3HP/4HB), and differentiated electron donor metabolisms—all generic, well-supported mechanisms in 2023-2024 literature._

### physiology/chemolithoheterotrophic  — *shallow* (9 edges)
- **Missing modules:** sulfur oxidation pathway (Sox/Sqr/SoeABC), denitrification electron acceptor pathway, sulfur intermediate cycling (S0/thiosulfate/sulfate), acetyl-CoA metabolic hub, organic uptake transporters specificity
- `acetate —converted to via acetyl-CoA synthetase→ acetyl-CoA`  (DOI:10.1128/AEM.01344-19 (Callbeck 2019): Arcobacter peruens)
- `sulfide —oxidized by→ Sox pathway (soxCDYZAXB)`  (DOI:10.3389/fmicb.2023.1182497 (Trutschel 2023): Serpentiniz)
- `nitrate —serves as electron acceptor for→ denitrification pathway`  (DOI:10.1128/AEM.01344-19 (Callbeck 2019): Arcobacter peruens)
- `elemental sulfur —oxidized to→ thiosulfate and sulfate`  (DOI:10.3390/ijms252010962 (Rudenko 2024) and DOI:10.3389/fmi)
- `organic uptake transporters —enable import of→ acetate and other organic acids`  (DOI:10.1038/s41396-021-01163-x (Taubert 2022): Abundance of )
- `Sqr enzyme —catalyzes initial oxidation of→ sulfide to quinone-bound intermediates`  (DOI:10.3389/fmicb.2023.1182497 (Trutschel 2023): All Rhodoba)
- _Existing graph captures electron donor abstraction and energy conservation core (respiratory chain, PMF, ATP, carbon heterotrophy) but misses sulfur-specific oxidation machinery (Sox/Sqr pathways), denitrification as electron acceptor, sulfur intermediate cycling, and transporter-level organic uptake specificity—five generic mechanistic modules present in multi-taxa report evidence but absent from graph._

### physiology/chemolithotrophic  — *shallow* (7 edges)
- **Missing modules:** iron oxidation electron transport chain, CO2 fixation pathways (Calvin/rTCA/Wood-Ljungdahl), nitrite oxidation completing nitrification cycle, anaerobic lithotrophy with alternative electron acceptors (NO3-, NO2-)
- `ferrous iron —oxidized by→ outer membrane cytochrome (Cyc2)`  (DOI:10.3390/microorganisms12030590 (Fe2+ oxidation chain in )
- `inorganic electron donor oxidation —feeds into→ Calvin-Benson-Bassham cycle`  (DOI:10.3390/microorganisms12030590 (CBB cycle carbon fixatio)
- `ammonia oxidation —coupled with→ bicarbonate/CO2 fixation`  (DOI:10.1038/s41467-023-37104-9 (ammonia oxidizers couple nit)
- `thiosulfate oxidation —yields→ sulfate via complete Sox pathway`  (DOI:10.3389/fmicb.2024.1426584 (csox complete oxidation with)
- `nitrite —oxidized to→ nitrate`  (DOI:10.1146/annurev.micro.55.1.485 (nitrification completion)
- `inorganic donor oxidation —enables→ chemolithotrophic growth with CO2 as primary carbon source`  (DOI:10.1016/B978-0-12-378630-2.00219-X (chemolithotroph trai)
- _Existing graph captures ammonia and sulfur oxidation cascades plus generic respiratory energy conservation but lacks iron oxidation (a major chemolithotrophic type), CO2 fixation pathways (essential to trait autotrophy definition), and anaerobic alternative electron acceptors._

### physiology/chemoorganotrophic  — *shallow* (7 edges)
- **Missing modules:** fermentation with substrate-level phosphorylation, environmental conditioning (O2 presence enabling aerobic vs. NO3-/NO2- enabling anaerobic vs. absence triggering fermentation), glycolysis and TCA cycle entry points, redox cofactor intermediates (NADH, ferredoxin, quinone pools), membrane-linked anaerobic energy conservation (Rnf and Ech complexes), terminal oxidase and NADH dehydrogenase entry points in respiratory chain
- `chemoorganotrophic_trait —has_two_main_energy_paths→ respiration and fermentation`  (Hackmann 2024 doi:10.1093/femsre/fuae016: ~25% of prokaryote)
- `oxygen_present —enables→ aerobic respiration`  (Weissbrodt 2023 doi:10.2166/9781789062304_0009: 'electron ac)
- `nitrate_or_nitrite_present —enables→ anaerobic respiration`  (Weissbrodt 2023 doi:10.2166/9781789062304_0009: 'anoxic (abs)
- `no_external_terminal_acceptor —triggers→ fermentation`  (Weissbrodt 2023 doi:10.2166/9781789062304_0009: 'In fermenta)
- `fermentation —generates_ATP_via→ substrate_level_phosphorylation`  (Hackmann 2024 doi:10.1093/femsre/fuae016: 'ATP is generated )
- `substrate_oxidation —produces_reduced_cofactors→ NADH and ferredoxin`  (Hackmann 2024 doi:10.1093/femsre/fuae016: 'At several points)
- _Existing graph biases heavily toward aerobic respiration and omits fermentation (~25% of prokaryotes), environmental triggers, and redox intermediates—meeting only the respiration backbone of the generic mechanism._

### physiology/heterotrophic  — *shallow* (6 edges)
- **Missing modules:** glycolysis (Embden-Meyerhof pathway), TCA cycle, glyoxylate cycle for acetate/C2 assimilation, aerobic respiration with electron transport chain, anaerobic respiration (fumarate as alternative electron acceptor), explicit ATP/NAD(P)H energy currency production
- `organic_molecule —catabolized via→ glycolysis_pathway`  (DOI:10.1111/raq.12700 - 'Glucose is highlighted as the most )
- `pyruvate —oxidized by→ TCA_cycle`  (DOI:10.3389/fmicb.2024.1441865 - 'both strains encode comple)
- `acetyl_CoA —routed through→ glyoxylate_cycle`  (DOI:10.1111/raq.12700 - 'Acetate... routed into the glyoxyla)
- `catabolism —enables_aerobic_energy_via→ respiration_with_O2`  (DOI:10.3389/fmicb.2024.1441865 - 'Glucose, fructose, or sucr)
- `catabolism —enables_anaerobic_energy_via→ fumarate_respiration`  (DOI:10.3389/fmicb.2024.1441865 - 'Both genomes encode fumara)
- `organic_substrate —metabolized_via→ fermentation`  (DOI:10.1016/j.chom.2024.05.011 - anaerobic heterotrophs use )
- _Existing graph captures substrate-uptake-catabolism-anabolism-biomass backbone but misses at least 3 major generic mechanistic modules: specific central carbon pathways (glycolysis, TCA, glyoxylate cycle), electron acceptor options (aerobic, anaerobic, fermentation), and explicit energy (ATP/NAD(P)H) vs. biomass distinction; report identifies these as core, broadly-reusable, cultivation-backed mechanisms."_

### physiology/hydrogenotrophic  — *shallow* (7 edges)
- **Missing modules:** electron bifurcation (anaerobic H2-coupled CO2 reduction), Wood-Ljungdahl pathway (acetogenesis), hydrogenotrophic methanogenesis (H2+CO2→CH4), ATP synthase coupling, ferredoxin electron carrier, multiple electron acceptors (O2, NO3, SO4, Fe(III)), oxygen concentration environmental constraint
- `H2 oxidation —generates→ proton motive force`  (DOI:10.2138/gselements.16.1.39 — 'Splitting H2 yields electr)
- `proton gradient —drives→ ATP synthase`  (DOI:10.1128/spectrum.01385-22 — 'transmembrane electrochemic)
- `HydABC electron-bifurcating hydrogenase —reduces→ ferredoxin and NAD(P)+`  (DOI:10.1021/jacs.2c11683 — 'HydABC... catalyze electron bifu)
- `electron bifurcation —essential_for→ Wood-Ljungdahl pathway operation`  (DOI:10.1021/jacs.2c11683 — 'electron bifurcation is essentia)
- `H2 oxidation —coupled_to_reduction_of→ multiple electron acceptors (O2, nitrate, sulfate, Fe(III))`  (DOI:10.2138/gselements.16.1.39 — 'hydrogen oxidation can be )
- `H2 and CO2 availability —supports→ hydrogenotrophic methanogenesis`  (DOI:10.1007/s00253-023-12700-3 — 'hydrogenotrophic methanoge)
- _Existing graph captures aerobic H2-oxidation backbone but severely under-represents anaerobic acetogenic and methanogenic hydrogenotrophy, which report treats as equally generic. Major modules absent: electron bifurcation, ferredoxin coupling, Wood-Ljungdahl, methanogenesis, ATP synthase, and multi-acceptor respiration._

### physiology/methanotrophic  — *shallow* (8 edges)
- **Missing modules:** copper availability regulation (copper switch), copper acquisition via methanobactin, gene-to-protein grounding (pmoCAB, mmoXYZ operons)
- `copper_availability —positively_regulates_expression_of→ pMMO`  (10.1039/d3cy00737e — canonical copper switch controlling MMO)
- `copper_availability —negatively_regulates_expression_of→ sMMO`  (10.1039/d3cy00737e — high copper represses soluble MMO expre)
- `methanobactin —enables→ copper_acquisition`  (10.1039/d3cy00737e — methanobactin-mediated copper chelation)
- `pmoCAB_operon —encodes→ pMMO_complex_subunits`  (10.1039/d3cy00737e — gene-level grounding for particulate MM)
- `mmoXYZ_genes —encodes→ soluble_MMO_hydroxylase`  (10.1039/d3cy00737e — gene-level grounding for soluble MMO hy)
- `copper_acquisition —positively_regulates→ pMMO_activity`  (10.1021/acs.chemrev.3c00727 — copper as essential cofactor f)
- _Existing graph captures methane-formaldehyde-CO2 oxidation backbone but omits the copper-switch regulatory hub and gene-level architecture controlling MMO phenotype switching."_

### physiology/mixotrophic  — *shallow* (6 edges)
- **Missing modules:** iron oxidation energy metabolism, electron transport chain bioenergetic hub, proton gradient as universal energy coupling principle, explicit Calvin-Benson-Bassham cycle detail, transporter-mediated organic substrate uptake specificity
- `Fe(II) oxidation —feeds electrons to→ electron transport chain`  (10.1128/aem.00599-24: 'validated iron oxidases (Cyc2 cluster)
- `electron transport chain —drives→ ATP synthesis`  (10.1128/aem.00599-24: 'complete ETC complexes… and F-type AT)
- `RuBisCO (rbcL/cbbM) —enables→ Calvin-Benson-Bassham cycle`  (10.1128/aem.00599-24: 'all MAGs encode Form II RuBisCO (rbcL)
- `proton-pump rhodopsin —generates→ proton gradient`  (10.1128/spectrum.02177-23: 'PPR (rhodopsin) is proposed as a)
- `proton gradient —drives→ ATP synthesis`  (10.1128/spectrum.02177-23: 'creates a proton gradient to dri)
- `sugar ABC transporters (gtsABC/frcABC) —imports→ sugars`  (10.1128/aem.00599-24: 'sugar transporters (gtsABC, frcABC)… )
- _Existing graph lacks major energy-generation pathways (iron oxidation, ETC, proton gradients) and mechanistic depth on carbon fixation and substrate uptake; these are well-supported as generic modules applicable across multiple mixotrophic taxa (not taxon-specific), primarily from Tothero 2024 (L. ochracea genomes) and Li 2024 (community transcriptomics)._

### physiology/natural_competence  — *shallow* (2 edges)
- **Missing modules:** DNA capture by competence pilus, pilus retraction-driven DNA transport, ComEA/ComEC-mediated membrane translocation, RecA-mediated homologous recombination, DprA-RecA handoff and ssDNA processing
- `competence pilus —binds→ extracellular DNA`  (DOI:10.1128/mmbr.00125-23)
- `pilus retraction —promotes→ extracellular DNA uptake`  (DOI:10.1128/mmbr.00125-23)
- `ComEA —mediates_transfer_to→ periplasm / inner membrane uptake machinery`  (DOI:10.1101/2024.02.06.579203)
- `ComEC —required_for→ cytoplasmic DNA uptake`  (DOI:10.1101/2024.02.06.579203)
- `DprA —recruits→ RecA`  (DOI:10.1371/journal.pbio.3002814)
- `RecA —mediates→ homologous recombination of transforming DNA`  (DOI:10.1371/journal.pbio.3002814)
- _The existing graph captures only the phenotype and high-level process but omits the core mechanistic steps (pilus-mediated uptake, membrane translocation, and recombination machinery) that are universally conserved across naturally competent bacteria._

### physiology/nutrient_adaptation  — *shallow* (6 edges)
- **Missing modules:** genome streamlining selection, rrn copy number growth proxy, growth-acquisition trade-off, motility/sensing investment contrast, high-affinity transporter uptake systems, regulatory proteome reallocation (ppGpp/DksA/cAMP-CRP)
- `ambient_nutrient_concentration —selects_for→ genome_streamlining`  (DOI:10.1038/ismej.2014.60 — chronic nutrient limitation sele)
- `genome_streamlining —correlates_with→ lower_rrn_operon_copy_number`  (DOI:10.1093/ismeco/ycae081, DOI:10.1038/ismej.2014.60 — stre)
- `rrn_operon_copy_number —positively_associates_with→ maximum_growth_rate`  (DOI:10.1038/s41564-023-01465-0, DOI:10.1038/s41467-024-53753)
- `copiotrophic_strategy —enriches→ chemotaxis_and_motility_genes`  (DOI:10.1073/pnas.0903507106, DOI:10.1038/s41467-024-50382-1 )
- `oligotrophic_adaptation —depends_on→ high_affinity_ABC_transporter_systems`  (DOI:10.1073/pnas.0903507106 — oligotrophic bacteria rely on )
- `high_growth_rate_strategy —trades_off_with→ carbohydrate_acquisition_gene_abundance`  (DOI:10.1038/s41467-024-50382-1 — maximum growth potential ne)
- _Existing graph captures the sensing→resource allocation→phenotype backbone but misses six generic mechanistic modules: genome streamlining selection, rrn-growth coupling, growth-acquisition trade-offs, motility/sensing investment contrast, high-affinity transporter systems, and regulatory proteome reallocation nodes."_

### physiology/oligotrophic  — *shallow* (6 edges)
- **Missing modules:** high-affinity solute-binding proteins (SBPs), phosphate acquisition and utilization pathways, dissolved organic phosphorus (DOP) scavenging, alternative nitrogen source utilization (urea/cyanate), substrate uptake at picomolar-nanomolar concentrations
- `oligotrophic_environment —favors→ high_affinity_solute_binding_proteins`  (DOI:10.1038/s41586-024-07924-w — SAR11 SBPs show extreme bin)
- `high_affinity_solute_binding_proteins —enables→ substrate_uptake_at_picomolar_nanomolar_concentrations`  (DOI:10.1038/s41586-024-07924-w — Characterized SBP binding a)
- `low_phosphate_concentration —selects_for→ phosphate_acquisition_and_storage_genes`  (DOI:10.1128/msystems.00898-23 — At <0.05 µM phosphate, cells)
- `nutrient_limitation —favors→ alkaline_phosphatase_and_DOP_scavenging`  (DOI:10.1128/msystems.00898-23 — Oligotrophy-associated genom)
- `low_inorganic_nitrogen_availability —selects_for→ urease_and_urea_utilization`  (DOI:10.3389/fmars.2024.1386686 — SAR11 ureC prevalence negat)
- `low_nutrient_availability —selects_for→ streamlined_genome`  (DOI:10.1038/s41467-023-36988-x — Nutrient limitation drives )
- _Existing graph captures phenotypic outcomes but misses molecular mechanistic details; high-affinity SBPs and nutrient-specific acquisition pathways are generic, broadly-supported modules absent from current curation._

### physiology/organotrophic  — *shallow* (7 edges)
- **Missing modules:** NADH dehydrogenase entry (NDH-1/NDH-2 branching), quinone pool electron carrier, Complex III / cytochrome bc1 intermediate coupling, terminal oxidase / Complex IV O2 reduction, ATP synthase as distinct catalytic complex
- `organic_compound —oxidation generates→ NADH and FADH2`  (DOI:10.1186/s13213-024-01761-y (Garimella 2024: 'Catabolic p)
- `NADH —donates electrons to→ NADH dehydrogenase`  (DOI:10.1186/s13213-024-01761-y (Garimella 2024: 'NADH dehydr)
- `NADH dehydrogenase —transfers electrons to→ quinone pool`  (Giordano 2024 (mechanistic excerpt: 'NDH-1/NDH-2 transfer el)
- `quinone pool —donates electrons to→ Complex III / cytochrome bc1`  (Giordano 2024 (generic ETC mechanism: 'reduced quinone pool )
- `Complex III / cytochrome bc1 —transfers electrons to and generates→ proton motive force`  (Giordano 2024 (canonical mechanism: 'Complex III generates P)
- `proton_motive_force —drives→ ATP synthase`  (Giordano 2024 (energy conservation: 'ATP synthase uses elect)
- _Generic mechanism well-described in report, but existing graph oversimplifies electron-transport-chain architecture, merging dehydrogenases, quinone, Complex III, and terminal oxidase into single 'respiratory_chain' node; detailed ETC intermediate nodes needed._

### physiology/oxidative_stress_response  — *shallow* (2 edges)
- **Missing modules:** catalase/peroxidase scavenging enzymes, superoxide dismutase (Sod), OxyR redox-responsive regulator and target genes, RpoS/sigma factors for stress regulation, DNA exonuclease repair (xthA), thioredoxin/glutaredoxin thiol-repair systems
- `OxyR —activates transcription of→ oxidative-stress defense genes (katG, ahpCF, dps, gorA, grxA)`  (DOI:10.1099/mic.0.001481 — Bientz 2024: 'The transcriptional)
- `catalase/peroxidase enzymes (KatE, KatG, AhpC/AhpF) —reduces→ hydrogen peroxide`  (DOI:10.1038/nrmicro3032 (existing ref))
- `superoxide dismutase (Sod) —reduces→ superoxide radical`  (DOI:10.1128/mmbr.00151-22 — Bouillet 2024: sodA listed as co)
- `RpoS (sigma factor) —regulates transcription of→ dps, catalase, sodA, osmC`  (DOI:10.1128/mmbr.00151-22 — Bouillet 2024: 'RpoS controls...)
- `xthA (exonuclease III) —repairs→ oxidatively damaged DNA`  (DOI:10.3389/fcimb.2023.1290508 — Wang 2023: xthA 'repairs ox)
- `thioredoxin system (TrxA/TrxB) —repairs→ oxidative protein disulfides`  (DOI:10.1371/journal.ppat.1012001 — Anjou 2024: 'The thioredo)
- _Existing graph captures only stimulus and trait outcome, missing six major generic mechanistic modules (regulators, enzyme classes, repair systems) explicitly documented in the report as broadly conserved and functionally essential to oxidative stress defense._

### physiology/photoheterotrophic  — *shallow* (7 edges)
- **Missing modules:** proteorhodopsin-driven proton pumping pathway, membrane potential as energetic intermediate, photophosphorylation as unifying ATP-generation process, NAD(P)H boundary (PR cannot generate reducing power)
- `light —activates→ proteorhodopsin proton pumping`  (Lee & Oh 2024, https://doi.org/10.1007/s12275-024-00125-0, p)
- `proteorhodopsin proton pumping —generates→ proton motive force`  (Lee & Oh 2024, https://doi.org/10.1007/s12275-024-00125-0, p)
- `proton motive force —enables→ atp`  (Lee & Oh 2024, https://doi.org/10.1007/s12275-024-00125-0, p)
- `photosynthetic_reaction_center —participates in→ photophosphorylation`  (Stojan et al. 2024, https://doi.org/10.1186/s40793-024-00573)
- `photoheterotrophic_trait —cannot generate→ nadph`  (Oh et al. 2024, https://doi.org/10.4014/jmb.2410.10034, page)
- `aerobic anoxygenic phototroph —relies primarily on→ organic_carbon`  (Stojan et al. 2024, https://doi.org/10.1186/s40793-024-00573)
- _Existing graph captures only the bacteriochlorophyll-AAP pathway; lacks the equally-generic proteorhodopsin route documented as widespread in recent (2024) literature, plus the proton motive force intermediate and boundary edge distinguishing photoheterotrophy from photoautotrophy."_

### physiology/photolithoautotrophic  — *shallow* (8 edges)
- **Missing modules:** CO2-concentrating mechanism (DIC toolkit: carbonic anhydrase, DIC transporters, carboxysomes), sulfur oxidation machinery (SQR, SoxAX linking to electron transport)
- `carbonic anhydrase —interconverts→ carbon dioxide and bicarbonate`  (DOI:10.1128/aem.01557-23 Scott 2024 reviews CA-mediated CO2/)
- `DIC transporters —imports→ inorganic carbon`  (DOI:10.1128/aem.01557-23 Scott 2024 tabulates SbtA/BicA/CmpA)
- `carboxysome —concentrates→ carbon dioxide near RuBisCO`  (DOI:10.1128/aem.01557-23 Scott 2024 details carboxysomes as )
- `photosynthetic electron transport —generates→ NADPH`  (DOI:10.1038/s44222-023-00093-x Lawrence 2023 tabulates ferre)
- `RuBisCO —catalyzes→ carbon dioxide fixation`  (DOI:10.1128/aem.01557-23 Scott 2024 identifies RuBisCO as CO)
- `SQR —oxidizes→ sulfide to electron carrier pool`  (DOI:10.1038/s44222-023-00093-x Lawrence 2023 details sulfide)
- _Existing graph captures the core energy → electron transport → reducing power → CO2 fixation → biomass chain but lacks the CO2-concentrating mechanism (DIC toolkit) and explicit sulfur oxidation enzymes, both emphasized in recent generic reviews as universal/near-universal modules in photolithoautotrophic systems._

### physiology/phototrophic  — *shallow* (6 edges)
- **Missing modules:** carotenoid light-harvesting extension, primary charge separation, quinone/cytochrome electron transport chain, proton motive force formation, light-inhibition regulatory constraint on BChl synthesis, retinalophototrophy/rhodopsin-based ion pumping pathway
- `carotenoids —extends absorption into→ blue-green light spectrum`  (DOI:10.1093/femsre/fuv032)
- `carotenoid excited energy —is transferred to→ bacteriochlorophyll`  (DOI:10.1093/femsre/fuv032)
- `bacteriochlorophyll —enables→ primary charge separation`  (DOI:10.1093/femsre/fuv032)
- `photosynthetic electron transport —forms→ proton motive force`  (DOI:10.1128/aem.00863-24)
- `proton motive force —powers→ ATP synthase`  (DOI:10.1128/aem.00863-24)
- `light —inhibits→ bacteriochlorophyll biosynthesis`  (DOI:10.1093/femsre/fuv032)
- _Existing graph captures initial light→ATP backbone but omits the intermediate generic modules (carotenoid antenna, charge separation, electron transport details, proton gradient, light regulation) that contextualize how light energy is actually converted to usable forms._

### upper/biological_process  — *shallow* (3 edges)
- **Missing modules:** cellular localization context (occurs_in), molecular activity chaining (MF-to-MF causality), chemical inputs and outputs, GO-CAM relation predicates (RO/BFO grounding)
- `molecular_function —part_of→ biological_process`  (DOI:10.1186/s40708-023-00208-5 (Prakash et al. 2023) — GO-CA)
- `molecular_function —enabled_by→ gene_product`  (DOI:10.1186/s40708-023-00208-5 (Prakash et al. 2023) — Essen)
- `molecular_function —occurs_in→ cellular_component`  (DOI:10.1186/s40708-023-00208-5 (Prakash et al. 2023) — GO-CA)
- `molecular_function —has_input→ chemical_entity`  (DOI:10.1186/s40708-023-00208-5 (Prakash et al. 2023) — Gener)
- `molecular_function —has_output→ chemical_entity`  (DOI:10.1186/s40708-023-00208-5 (Prakash et al. 2023) — Gener)
- `molecular_function —causally_upstream_of_or_within→ molecular_function`  (DOI:10.1186/s40708-023-00208-5 (Prakash et al. 2023) — GO-CA)
- _Existing graph has backbone (gene-function-process) but omits four generic mechanistic modules: cellular localization, activity chaining, chemical I/O, and proper RO/BFO predicate grounding endorsed by the report as broadly applicable to microbial trait curation._

### environment/cadmium_tolerant  — *shallow* (3 edges)
- **Missing modules:** zinc-induced CzcRS regulatory activation, cadA/P-type ATPase alternate efflux pathway, biofilm/EPS-mediated community tolerance, thiol/metallothionein cytoplasmic sequestration
- `zinc(2+) ion —induces→ CzcRS two-component system`  (DOI:10.1038/s41598-024-80754-y (Chatterjee et al. 2024, page)
- `CzcRS two-component system —activates transcription of→ czc_efflux_system`  (DOI:10.1038/s41598-024-80754-y (Chatterjee et al. 2024, page)
- `CadA P-type ATPase —enables→ cadmium ion transport across cytoplasmic membrane`  (DOI:10.1007/s40201-023-00887-6 (Sharma et al. 2024, pages 12)
- `biofilm formation —increases tolerance to→ cadmium ion`  (DOI:10.1038/s41598-024-80754-y (Chatterjee et al. 2024, page)
- `metallothionein/thiol-rich proteins —sequester→ cadmium(2+) ion`  (DOI:10.1038/s41598-024-80754-y (Chatterjee et al. 2024, page)
- _Existing graph captures czc efflux core well (3 edges) but misses 4 generic mechanistic modules: zinc-regulated CzcRS activation, alternate P-type ATPase efflux, community-level biofilm protection, and thiol-based sequestration._

### environment/ph_range_high  — *shallow* (2 edges)
- **Missing modules:** membrane potential (Δψ) bioenergetic coupling, F1Fo-ATP synthase proton uptake cycle, Na+/solute symporter Na+ recycling, MrpA–G operon gene organization
- `membrane potential —drives→ extreme_alkaliphile_antiport`  (DOI:10.1038/nrmicro2549 (Krulwich 2011, pages 5-6): large tr)
- `MrpA–G operon —encodes→ Mrp hetero-oligomeric antiporter complex`  (DOI:10.1038/nrmicro2549 (Krulwich 2011, pages 12-14): Bacill)
- `F1Fo-ATP synthase —contributes_to→ alkaliphile pH homeostasis`  (DOI:10.1038/nrmicro2549 (Krulwich 2011, pages 12-14): proton)
- `Na+/solute symporters —supplies→ extreme_alkaliphile_antiport`  (DOI:10.1038/nrmicro2549 (Krulwich 2011, pages 12-14): ongoin)
- `ATP synthase subunit-a/c motifs —enables→ ATP synthase function at high pH`  (DOI:10.1038/nrmicro2549 (Krulwich 2011, pages 12-14): alkali)
- _Existing graph captures only the core Na+/H+ antiporter node and immediate enablement edge; misses 4+ generic mechanistic modules including bioenergetic coupling, ATP synthase cycling, Na+ recycling, and gene-level organization that are all well-supported in Krulwich 2011._

### genomics/gc_low  — *shallow* (2 edges)
- **Missing modules:** DNA repair pathway (MMR/BER/HR) as upstream driver, mutational spectrum intermediate node, cytosine deamination and AT-enriching transitions as mechanistic step, spectrum-to-GC-composition correlation
- `DNA repair defects (mismatch repair or base excision repair) —creates distinctive→ bacterial mutational spectrum`  (Ruis 2023, DOI:10.1038/s41467-023-42916-w: 'defects in DNA r)
- `cytosine deamination —drives→ C→T transition enrichment in mutation spectrum`  (Ruis 2023, DOI:10.1038/s41467-023-42916-w: 'C→T was typicall)
- `AT-enriching mutation spectrum (C→T, G:C→A:T dominant) —shifts genomic composition toward→ lower GC content`  (Ruis 2023, DOI:10.1038/s41467-023-42916-w: 'Genomic G+C cont)
- `mutational spectrum composition (C>A/T enrichment, C>G depletion) —associates with→ genomic G+C content in mid-range (42.65-57.0%)`  (Ruis 2023, DOI:10.1038/s41467-023-42916-w: direct quantitati)
- `DNA replication or repair enzyme bias —shapes→ genomic GC composition`  (Delgado 2024, DOI:10.3389/fmicb.2024.1412318: 'The GC% of ge)
- _The existing graph captures mutation bias → GC low but skips the critical intermediate (mutational spectrum) and upstream drivers (DNA repair pathways); report prescribes a two-step architecture (repair → spectrum → GC) strongly supported by Ruis 2023 multi-clade study; all flagged taxon-specific edges (MutL, UV, oxygen, nutrient limitation habitat-scoped) were correctly excluded."_

### metabolism/starch_degradation  — *shallow* (2 edges)
- **Missing modules:** surface binding/recognition step, maltooligosaccharide intermediate product, periplasmic hydrolysis finishing step, debranching module for amylopectin branch-points, transport/import across membrane
- `starch —is_hydrolyzed_to→ maltooligosaccharides`  (Brown et al. 2024)
- `maltooligosaccharides —is_further_hydrolyzed_to→ glucose`  (Brown et al. 2024 (DOI:10.1128/mbio.01506-24) documents peri)
- `amylase —produces→ maltooligosaccharides`  (Brown et al. 2024)
- `type_I_pullulanase —degrades→ alpha-1,6-branch-points`  (Pickens & Cockburn 2024 (DOI:10.1128/msphere.00566-23) demon)
- `starch_binding_protein —binds→ starch`  (Brown et al. 2024 (DOI:10.1128/mbio.01506-24) describes oute)
- _Existing graph captures only direct amylase→trait edge; misses critical intermediate (maltooligosaccharides), periplasmic finishing step, branching enzymes, and substrate-binding entry point—five distinct generic mechanistic modules described in recent literature as universal across starch-degrading bacteria."_

### morphology/cell_length_medium  — *shallow* (3 edges)
- **Missing modules:** Rod complex (elongasome) structural integrity and regulation, Divisome and septation coordination with elongation
- `RodZ —physically interacts with→ MreB/MreC/MreD/RodA/PBP2 complex`  (doi:10.1002/mbo3.1385 (Ago et al. 2023) establishes RodZ as )
- `RodA-PBP2 elongasome —enables→ peptidoglycan insertion during cell elongation`  (doi:10.1002/mbo3.1385 (Ago et al. 2023) shows RodA (glycosyl)
- `intact Rod complex —maintains→ dense peptidoglycan structure and rod shape`  (doi:10.1002/mbo3.1385 (Ago et al. 2023) demonstrates Rod com)
- `FtsZ divisome —coordinates with→ MreB elongation machinery`  (doi:10.1128/mbio.00631-23 (Lakey et al. 2023) in R. sphaeroi)
- `cell elongation rate —is balanced by→ cell division rate`  (Report consensus across Lakey, Castanheira, Singh sources (2)
- _Existing graph captures growth-rate size law but misses well-evidenced Rod complex and divisome coordination mechanisms needed to explain maintenance of 2–3 µm rod morphology; high priority for enrichment with generic (non-taxon-specific) mechanistic edges from 2023–2024 literature._


## MEDIUM priority

### ecology/animal_pathogen  — *shallow* (4 edges)
- **Missing modules:** adhesion entry step, secretion system machinery (T3SS/T4SS/T5SS), iron acquisition and siderophore biosynthesis, complement/antibody-targeted immune evasion
- `metazoan_virulence_factors —enables→ bacterial_adhesion_to_host`  (DOI:10.1093/femsre/fuae019 — bacterial adhesins expression i)
- `bacterial_secretion_systems —enables→ effector_translocation_into_host_cell`  (DOI:10.1128/spectrum.02224-23 — T3SS form syringe-like struc)
- `siderophore_biosynthesis —enables→ animal_tissue_colonization`  (DOI:10.1080/19490976.2024.2369339 — yersiniabactin enhances )
- `immune_evasion —includes→ complement_regulatory_protein_binding`  (DOI:10.1093/femsre/fuae019 — surface proteins bind fH/C4BP t)
- `metazoan_virulence_factors —enables→ biofilm_formation`  (DOI:10.1093/femsre/fuae019 — adhesion promotes biofilm/absce)
- `Fur_low_iron_derepression —enables→ siderophore_biosynthesis_gene_expression`  (DOI:10.1039/d4cb00175c — core iron-responsive regulatory mec)
- _The existing graph captures disease-progression linearity but misses three major generic mechanistic modules (adhesion entry, secretion-system effector delivery, iron-acquisition physiology) that are well-supported across diverse animal pathogens in the literature._

### ecology/biosafety_level  — *shallow* (7 edges)
- **Missing modules:** virulence determinants (secretion systems, effectors, toxins), infectious dose input to risk assessment, route of transmission / aerosolization potential, treatment and vaccine availability as BSL determinants, host damage mechanisms (cytoskeleton manipulation, immune evasion)
- `type III secretion system —contributes_to→ pathogen_hazard_properties`  (DOI:10.1128/cmr.00013-07: Type III secretion systems are a d)
- `effector protein translocation —causes→ host cell damage`  (DOI:10.1038/nature06247: Secreted effectors alter host pathw)
- `aerosol generation potential —increases_requirement_for→ bsl3`  (DOI:10.3390/laboratories1030013 (2024): BSL-3 is specified f)
- `infectious dose —is_input_to→ risk_assessment`  (DOI:10.1089/apb.2022.0040 (2023): Infectious dose is identif)
- `availability_of_vaccines —influences→ biosafety_level_trait`  (DOI:10.3390/laboratories1030013 (2024): BSL-4 covers agents )
- `toxin_production —contributes_to→ pathogen_hazard_properties`  (DOI:10.2903/j.efsa.2025.9169 (2025): Bacterial toxins like h)
- _Existing graph captures hazard-to-containment logic but omits biological mechanism: secretion systems, toxins, infectious dose, and transmission route are generic, well-supported hazard inputs that should connect upstream of pathogen_hazard_properties node._

### ecology/mutualism  — *shallow* (2 edges)
- **Missing modules:** host control and partner selection, cross-partner signaling (flavonoid/Nod-factor dialogue), community assembly and microbiota structuring, obligate mutual dependence (syntrophy), diverse metabolite exchange modules (carbon, nitrogen, vitamins, micronutrients)
- `host control mechanisms —select for→ microbial traits beneficial to host`  (DOI:10.1126/science.adi3338 (Wilde et al. 2024: hosts exert )
- `plant root exudate composition —shapes→ symbiotic microbiota assembly`  (DOI:10.1038/s41467-024-47752-0 (Tao et al. 2024: Nod factor )
- `co-auxotrophic cross-feeding —creates→ obligate mutualism`  (DOI:10.1038/s41564-023-01596-4 (Peng et al. 2024: syntrophy/)
- `multi-strain microbial community —increases→ host growth and fitness`  (DOI:10.1128/mbio.00972-24 (Laurich et al. 2024: 10-strain co)
- `plant carbon supply —enables→ fungal nutrient acquisition from soil`  (DOI:10.1007/s00253-024-13298-w (Pena & Tibbett 2024: mycorrh)
- `metabolite secretion profile —determines→ mutualism versus antagonism outcome`  (DOI:10.3390/plants13060829 (Burgunter-Delamare et al. 2024: )
- _The existing graph is a bare minimum (nutrient exchange → reciprocal benefit) and lacks mechanistic depth on host control, partner signaling, community assembly, obligate syntrophy, and the diversity of exchange types documented across plant–rhizobium, plant–fungal, and microbe–microbe mutualisms in the 2024 literature._

### ecology/plant_pathogen  — *shallow* (6 edges)
- **Missing modules:** biofilm formation and QS regulatory system, xylem colonization and EPS-mediated vessel occlusion pathway, c-di-GMP signaling as virulence regulator
- `quorum sensing —positively regulates→ biofilm formation`  (DOI:10.3390/plants12112207 - 'QS is required for cooperative)
- `quorum sensing / c-di-GMP —positively regulates→ exopolysaccharide production`  (DOI:10.3390/plants12112207 - 'EPS such as amylovoran, levan,)
- `EPS-rich biofilm —causes→ xylem vessel obstruction`  (DOI:10.3390/plants12112207 - 'travels to the xylem where it )
- `xylem vessel obstruction —causes→ wilting disease phenotype`  (DOI:10.3390/plants12112207 - vascular biofilms 'cause wiltin)
- `type III effectors —suppresses→ plant PTI (pattern-triggered immunity) defenses`  (DOI:10.1094/PHYTO-08-22-0292-KD - 'a primary function of phy)
- `plant cell-wall-degrading enzymes —facilitates→ pathogen invasion and tissue maceration`  (DOI:10.21608/mb.2024.307263.1134 - 'secretion of cell-wall-d)
- _Existing graph has core T3SS/effector backbone (6 edges covering T3SS delivery → immune suppression → colonization → disease) but misses biofilm/QS/EPS regulatory system and xylem occlusion consequence pathway; both are generic, cross-taxon mechanisms well-supported in recent literature._

### environment/acidophilic  — *shallow* (5 edges)
- **Missing modules:** proton-coupled ATPase (active export via ATP synthase), cation/proton antiporter secondary transport (H+ for K+/Na+), urease-mediated cytoplasmic buffering, proton-consuming amino acid decarboxylation (Adi/Gad pathways), hopanoid lipid membrane adaptation
- `proton-coupled ATPase —catalyzes active transport of→ proton`  (DOI:10.1038/nrmicro2549 (lines 260: Krulwich et al. 2011 ide)
- `cation/proton antiporter —exchanges→ proton for cation (Na+ or K+)`  (DOI:10.1038/nrmicro2549 (line 261: Krulwich et al. 2011 desc)
- `urease system —contributes to→ cytoplasmic buffering`  (DOI:10.3389/fmicb.2023.1149903 (line 269: Dopson et al. 2023)
- `amino acid decarboxylase (Adi/Gad pathway) —consumes→ proton`  (DOI:10.3389/fmicb.2023.1149903 (lines 267-268: Dopson et al.)
- `hopanoid lipids —decrease→ membrane proton permeability`  (DOI:10.3389/fmicb.2023.1149903 and DOI:10.1111/1758-2229.700)
- `cation uptake (K+ and Na+) —reduces→ proton influx`  (DOI:10.1111/1758-2229.70019 (line 275: Valdez-Nuñez et al. 2)
- _Existing graph captures pH homeostasis backbone and passive defenses (membrane impermeability, reversed potential) but omits active mechanisms (ATPases, antiporters, decarboxylation buffering, hopanoid adaptation) documented across multiple acidophile lineages._

### environment/alkalotolerant  — *shallow* (5 edges)
- **Missing modules:** cell-envelope acidic polymers module, sodium motive force (Na+-based bioenergetics), compatible solute and osmolyte regulation, K+ homeostasis maintenance
- `alkaline pH stress —requires→ acidic cell-surface polymers`  (DOI:10.1128/MMBR.63.4.735-750.1999)
- `acidic nonpeptidoglycan cell-surface polymers —assists→ growth in alkaline environments`  (DOI:10.1128/MMBR.63.4.735-750.1999)
- `sodium motive force —enables→ cytoplasmic pH homeostasis`  (DOI:10.1007/s11244-024-01919-7)
- `compatible solute accumulation —supports→ alkalotolerant growth`  (DOI:10.1128/AEM.00145-24)
- `intracellular K+ maintenance —contributes to→ ion homeostasis under alkaline stress`  (DOI:10.1128/AEM.00145-24)
- `Na+/K+/H+ antiporter activity —maintains→ intracellular cation balance`  (DOI:10.3390/ijms23169156)
- _Existing graph captures pH homeostasis and cation/proton antiport backbone, but lacks three generic mechanistic modules (cell-envelope polymers, sodium motive force, osmolyte/K+ regulation) that the literature identifies as core alkaline-stress adaptations across diverse taxa._

### environment/cobalt_tolerant  — *shallow* (3 edges)
- **Missing modules:** cobalt sensing and transcriptional regulation (CzcRS-like system), alternative efflux determinants (cnr, rcnA operons), homeostasis vs. stress-defense framing
- `CzcS/CzcR two-component system —senses periplasmic metal and activates transcription of→ czcCBA operon`  (10.3390/ijms26125716 (Oleńska et al. 2025) — CzcRS detects Z)
- `cnr determinant (cnrCBAYXHT operon) —confers resistance to→ cobalt tolerant trait`  (10.1007/s44274-025-00301-y (Siunova et al. 2025) — C. metall)
- `rcnA (yohM nickel/cobalt resistance gene) —enables cobalt efflux and increases resistance to→ cobalt(2+)`  (10.1128/JB.187.8.2912-2916.2005 (Rodrigue et al. 2005) — rcn)
- `cobalt(2+) ion —requires efflux-mediated homeostasis for→ cytoplasmic metal balance`  (10.1093/mtomcs/mfae058 (Galea et al. 2024) — Proteomics show)
- `czcCBA operon —confers resistance to→ cobalt tolerant trait`  (10.1007/s44274-025-00301-y (Siunova et al. 2025) — C. metall)
- `DmeF (CDF-family metal exporter) —preferentially exports→ cobalt(2+)`  (10.1007/s44274-025-00301-y (Siunova et al. 2025) — DmeF show)
- _Existing graph captures core efflux-mediated detoxification but omits regulatory control layer, alternative determinants (cnr, rcnA), and homeostasis framing; all omitted edges are generic and well-supported across organisms or strains._

### environment/euryhaline  — *shallow* (6 edges)
- **Missing modules:** salt-in inorganic ion uptake (K+, Na+, Cl−), compatible-solute biosynthesis pathways (glycine betaine, ectoine), mechanosensitive ion-channel osmotic-downshock response, water-channel regulation / aquaporin transport, proteome remodeling / acidic amino-acid adaptation
- `salinity_gradient —selects for→ salt_in_strategy`  (10.1186/s40168-024-01817-w: COG0168 and inorganic-ion transp)
- `salt_in_strategy —depends on→ potassium_transport_system`  (10.1186/s40168-024-01817-w: Trk-type K+ transport (COG0168) )
- `betA_betB_enzymes —catalyze→ glycine_betaine`  (10.3389/fmicb.2023.1192059: Choline converted to glycine bet)
- `ectoine_biosynthesis_pathway —produces→ ectoine`  (10.3389/fmicb.2023.1192059: Five-step biosynthesis from L-as)
- `mechanosensitive_channels —enables→ osmotic_downshock_response`  (10.3389/fmicb.2023.1192059 + 10.3390/microorganisms12081738:)
- `water_channel_proteins —regulates→ osmotic_water_flux`  (10.1186/s40168-024-01817-w: COG0580-linked water channels (G)
- _Existing graph captures osmotic-imbalance backbone and compatible-solute uptake but omits generic mechanistic modules: salt-in ion-transport strategies, compatible-solute biosynthesis pathways, mechanosensitive-channel downshock response, and proteome remodeling—all well-supported as generic euryhaline mechanisms across 2023–2024 literature. Prioritize salt-in K+ transport and compatible-solute biosynthesis pathways as highest-impact gaps."_

### environment/extremely_halophilic  — *shallow* (5 edges)
- **Missing modules:** ionic transport specificity (Na+/H+ antiporters, K+ uniport, halorhodopsin, Cl−/Na+ symport), salinity-responsive cell-envelope glycosylation (S-layer and archaellum N-glycosylation), osmotic stress sensing and ion homeostasis feedback
- `hypersaline_brine —triggers→ osmotic stress response`  (Yu et al. 2024, DOI:10.1186/s12934-024-02358-5)
- `osmotic stress response —induces→ intracellular K+ accumulation`  (Yu et al. 2024, DOI:10.1186/s12934-024-02358-5)
- `Na+/H+ antiporter —mediates→ sodium efflux`  (Bonnaud et al. 2024, DOI:10.3390/microorganisms12081738)
- `halorhodopsin —drives→ chloride uptake`  (Bonnaud et al. 2024, DOI:10.3390/microorganisms12081738)
- `external salinity —alters→ S-layer N-glycosylation pathways`  (Gebhard et al. 2023, DOI:10.3390/v15071469)
- `archaellin N-glycosylation —prevents→ filament bundling and enables cell motility`  (Sofer et al. 2024, DOI:10.1038/s41467-024-50277-1)
- _Graph captures salt-in and acidic-proteome backbone but misses ionic transporter specificity and salinity-responsive cell-envelope remodeling, which are generic and well-evidenced mechanisms in recent literature._

### environment/facultative_oxygen_preference  — *shallow* (4 edges)
- **Missing modules:** oxygen-sensing regulatory switching (ArcA/ArcAB, FNR), alternative terminal electron acceptors (nitrate, fumarate), fermentation pathway and regulation, redox/quinone-based sensor kinase signaling
- `oxygen_sensing_regulation —represses→ aerobic_respiration`  (Brown 2023 (10.1128/mbio.01448-23): ArcA represses respirato)
- `oxygen_sensing_regulation —promotes→ fermentation`  (Brown 2023 (10.1128/mbio.01448-23): ArcA activation promotes)
- `molecular_oxygen —affects activation of→ oxygen_sensing_regulation`  (Villamizar 2023 (10.1128/aem.01491-23): Anaerobiosis activat)
- `nitrate —enables→ anaerobic_respiration_or_fermentation`  (Baker 2024 (10.1128/msphere.00774-23): Nitrate as terminal e)
- `facultative_oxygen_trait —depends on→ electron_transport_chain_sensing`  (Brown 2023 (10.1128/mbio.01448-23): ArcB senses respiratory/)
- `fumarate —enables→ anaerobic_respiration_or_fermentation`  (Butler 2023 (10.1128/jb.00389-22): Fumarate serves as termin)
- _Graph captures phenotypic outcome but lacks regulatory mechanisms and alternative electron acceptor flexibility that define facultative oxygen preference mechanistically._

### environment/facultatively_anaerobic  — *shallow* (4 edges)
- **Missing modules:** ArcAB redox-sensing two-component system, quinone/quinol pool as redox signal integrator, alternative terminal electron acceptors (nitrate/fumarate/DMSO/TMAO), fermentation as oxygen-independent energy metabolism fallback, NarX/NarQ-NarL/NarP nitrate-sensing regulatory cascade
- `molecular_oxygen limitation / reducing conditions —activates→ ArcB/ArcBA two-component system`  (DOI:10.1128/mbio.02370-24 (Whittle et al., 2024): ArcBA is ')
- `quinone/quinol pool redox state —regulates→ ArcB sensor kinase activity`  (DOI:10.1128/mbio.02370-24 (Whittle et al., 2024): Oxidized q)
- `ArcA/ArcAB —represses→ aerobic respiration program`  (DOI:10.1128/mbio.01448-23 (Brown et al., 2023): ArcAB, a two)
- `alternative anaerobic electron acceptors (nitrate, fumarate, DMSO, TMAO) —enable→ anaerobic electron transport chain operation`  (DOI:10.1038/s41467-024-51029-x (Schulz-Mirbach et al., 2024))
- `nitrate / nitrite —activates via sensing by→ NarX/NarQ → NarL/NarP`  (DOI:10.1101/2025.01.08.631794 (Ricciardelli et al., 2025): N)
- `molybdenum availability —enables→ nitrate reductase-dependent anaerobic respiration`  (DOI:10.1101/2025.01.08.631794 (Ricciardelli et al., 2025): M)
- _Existing graph captures oxygen-FNR sensing pathway but misses ArcAB (cross-taxon redox regulator), alternative electron acceptors, and fermentation fallback—all flagged as generic mechanisms in the report's expert synthesis._

### environment/halophily_preference  — *shallow* (6 edges)
- **Missing modules:** Na+/H+ antiporter-mediated sodium expulsion, proton gradient driving Na+ antiporter, ectoine biosynthesis and accumulation, acidified proteome for protein solubility, mechanosensitive channel response to downshock
- `osmotic_stress —induces→ Na+/H+ antiporter-mediated Na+ expulsion`  (10.3390/microorganisms12081738 (Bonnaud et al. 2024) — 'sodi)
- `proton electrochemical gradient —drives→ Na+/H+ antiporter activity`  (10.3390/microorganisms12081738 (Bonnaud et al. 2024) — 'sodi)
- `salt_stress —induces→ ectoine biosynthesis`  (10.1186/s12934-024-02515-w (Chen et al. 2024) — 'expression )
- `environmental_salinity —favors→ acidified proteome`  (10.3390/microorganisms12081738 (Bonnaud et al. 2024) — 'micr)
- `osmotic_downshock —activates→ mechanosensitive channels`  (10.3390/microorganisms12081738 (Bonnaud et al. 2024) — 'Msc )
- `acute_osmotic_stress —induces→ K+ uptake`  (10.3390/microorganisms12081738 (Bonnaud et al. 2024) — 'It s)
- _Existing graph captures core osmotic-stress-to-solute logic but misses at least 5 generic mechanistic modules: sodium antiporter system, proton gradient coupling, ectoine pathway, proteome acidification (extreme halophiles), and downshock recovery valves."_

### environment/halotolerant  — *shallow* (6 edges)
- **Missing modules:** salt-out strategy / salt exclusion module, Na+ homeostasis / antiporter-mediated Na+ extrusion, compatible solute biosynthesis pathways (ectABC, betA/betB), specific compatible solute identities (glycine betaine, ectoine, proline)
- `high_salt_exposure —triggers→ salt-out strategy`  (DOI:10.1038/s41598-024-63581-z)
- `salt-out strategy —relies on→ compatible_solute_accumulation`  (DOI:10.1038/s41598-024-63581-z)
- `ectABC_operon —enables→ ectoine_biosynthesis`  (DOI:10.58088/07hg-r941)
- `betA_betB —enables→ glycine_betaine_biosynthesis`  (DOI:10.58088/07hg-r941)
- `Na_H_antiporter_NhaA —extrudes→ sodium_ion`  (DOI:10.3390/biology13060404)
- `osmotic_stress —increases→ compatible_solute_accumulation`  (DOI:10.58088/07hg-r941)
- _Existing graph captures osmotic-stress and compatible-solute abstraction but lacks the salt-out strategy context, Na+ extrusion mechanisms, specific biosynthetic pathways (ectABC, betA/betB), and chemical specificity (ectoine, glycine betaine); all are generic, broadly-supported in recent literature._

### environment/ionizing_radiation_tolerant  — *shallow* (3 edges)
- **Missing modules:** ssDNA-mediated damage sensing, ROS detoxification via catalase pathway, clustered DNA lesion repair (vs simple DSB)
- `ionizing radiation —generates→ clustered DNA lesions`  (Lourenço et al. 2023, DOI:10.1007/978-3-031-18810-7_9 — ioni)
- `ionizing radiation —generates→ reactive oxygen species (ROS)`  (Lourenço et al. 2023, DOI:10.1007/978-3-031-18810-7_9)
- `DNA strand breaks (single-stranded DNA) —triggers→ DNA damage response / repair gene induction`  (Lu et al. 2024, DOI:10.1038/s41467-024-46208-9 — ssDNA serve)
- `catalase (KatA) —detoxifies→ reactive oxygen species`  (Rai & Dutta 2024, DOI:10.1128/aem.01538-23 — DrsS-regulated )
- `intracellular Mn2+ (elevated) —protects→ proteome from oxidative carbonylation`  (Rai & Dutta 2024, DOI:10.1128/aem.01538-23)
- `reactive oxygen species —causes_damage_to→ proteome (protein carbonylation)`  (Rai & Dutta 2024, DOI:10.1128/aem.01538-23 — oxidative stres)
- _Existing graph captures the two major arms (DSB repair + Mn-antioxidant defense) but lacks intermediate mechanistic detail: explicit ROS damage pathway, catalase induction module, and ssDNA as generic damage signal. Report flags Mn/Fe correlation as not universally causal across taxa, so recommend marking edges 5-6 as correlation if added."_

### environment/mercury_tolerant  — *shallow* (3 edges)
- **Missing modules:** MerR mercury sensing and regulation, MerP/MerT transport chain (periplasmic capture to cytoplasm), MerB organomercurial cleavage (broad-spectrum pathway), Mer operon inducibility under Hg stress
- `Hg(II) ion —activates transcription via MerR of→ mer operon`  (DOI:10.21203/rs.3.rs-3854515/v1 (paape2024adaptationtomercur)
- `MerB —cleaves→ organomercury (e.g., methylmercury) to Hg(II)`  (DOI:10.21203/rs.3.rs-3854515/v1 (paape2024adaptationtomercur)
- `MerP —binds and transfers→ Hg(II) to MerT`  (DOI:10.1128/spectrum.00553-23 (biełło2023quantitativeproteom)
- `MerT —transports→ Hg(II) to cytoplasm for MerA reduction`  (DOI:10.1128/spectrum.00553-23 (biełło2023quantitativeproteom)
- `Complete mer operon —enables→ high-level mercury tolerance (10-fold MIC increase vs stand-alone merA)`  (DOI:10.1186/s12866-024-03391-5 (bhat2024horizontalgenetransf)
- `Mercury exposure —upregulates→ mer operon gene expression`  (DOI:10.1186/s12866-024-03391-5 (bhat2024horizontalgenetransf)
- _Existing graph captures core detoxification chemistry but lacks regulation, transport, broad-spectrum MerB pathway, and operon-level causal logic; all six missing modules are generic, well-supported by review and multi-strain evidence, not taxon/assay-specific."_

### environment/microaerophilic  — *shallow* (4 edges)
- **Missing modules:** cytochrome bd-type oxidase respiratory module, ROS detoxification and oxidative stress defense system, branched respiratory chain adaptation to fluctuating oxygen
- `cytochrome bd oxidase —enables→ respiration under low oxygen`  (DOI:10.3390/ijms24076428 — 'bd-type quinol oxidases are wide)
- `branched respiratory chain —enables→ adaptation to fluctuating oxygen`  (DOI:10.3389/fmicb.2024.1468929 — 'branched respiratory chain)
- `ahpC alkyl hydroperoxide reductase —scavenges→ hydrogen peroxide`  (DOI:10.1186/s12866-024-03201-y — 'AhpC is considered the pre)
- `katA catalase —detoxifies→ hydrogen peroxide`  (DOI:10.3390/pathogens13100842 — 'katA encodes catalase that )
- `sodB superoxide dismutase —protects against→ reactive oxygen species`  (DOI:10.3390/pathogens13100842 — 'sodB encodes superoxide dis)
- `high-affinity terminal oxidase —increases→ respiratory flexibility during oxygen depletion`  (DOI:10.1128/spectrum.02767-23 — 'high-affinity oxidases cont)
- _Graph captures cbb3-mediated low-oxygen respiration backbone but misses the equally critical bd-oxidase module and the ROS-defense system, which the report identifies as mechanistically central to microaerophilic growth boundaries and oxygen sensitivity; adding these three modules would lift the graph to adequate coverage._

### environment/nacl_optimum_mid1  — *shallow* (3 edges)
- **Missing modules:** compatible-solute accumulation, salt-in vs salt-out strategy branching, major osmolytes (proline, ectoine, glycine betaine) as causal mediators, osmolyte biosynthesis and transport pathways
- `seawater_nacl —induces_synthesis_or_uptake_of→ compatible_solutes`  (Report establishes that elevated external NaCl universally t)
- `compatible_solutes —enables→ osmotic_balance`  (Direct mechanistic evidence: compatible solutes accumulate i)
- `modest_osmoadaptation —includes_both→ salt_in_and_salt_out_strategies`  (Report explicitly identifies two canonical strategies: salt-)
- `proline_biosynthesis_pathway —produces→ L_proline`  (Report identifies proB/proA/proC pathway as generic proline )
- `elevated_external_NaCl —selects_for_accumulation_of→ glycine_betaine`  (Report shows glycine betaine intracellular levels increase w)
- `ectoine_biosynthesis —produces→ ectoine`  (Report documents ectoine synthase gene presence and ectoine )
- _Graph captures high-level mechanism (external NaCl → osmoadaptation → phenotype) but lacks mechanistic depth: missing decomposition of 'modest osmoadaptation' into distinct salt-in/salt-out branches and absent specific osmolyte nodes (proline, ectoine, glycine betaine) and their biosynthetic/transport pathways, which the report identifies as universal, well-supported generic mechanisms."_

### environment/nacl_optimum_mid2  — *shallow* (3 edges)
- **Missing modules:** ectoine biosynthesis pathway regulation (ectABC operon upregulation), ectoine accumulation as specific mediator of salt tolerance, glycine betaine and proline as alternative compatible solutes
- `elevated_nacl —induces→ ectoine_biosynthesis_operon_ectABC`  (DOI:10.1128/aem.01905-23 (Zou et al. 2024 on H. elongata))
- `ectoine_biosynthesis_operon_ectABC —produces→ ectoine`  (DOI:10.1128/aem.01905-23)
- `ectoine —increases→ intracellular_osmolyte_concentration`  (DOI:10.1128/aem.01905-23 (H. elongata accumulates ectoine as)
- `elevated_nacl —induces→ compatible_solute_strategy`  (DOI:10.3390/biotech14020049 (Neagu & Stancu 2025))
- `compatible_solute_strategy —includes→ ectoine`  (DOI:10.3390/biotech14020049)
- `intracellular_osmolyte_concentration —enables→ nacl_optimum_mid2_trait`  (DOI:10.1093/femsre/fuy009 (osmoadaptation review)
- _Existing graph captures the high-level generic mechanism (NaCl → compatible solutes → trait) but abstracts away ectoine as the specific, well-supported mechanistic mediator across multiple Halomonas species; recommend granularizing the compatible-solute node into explicit ectoine biosynthesis pathway (ectABC) induction and accumulation steps._

### environment/nacl_optimum  — *shallow* (5 edges)
- **Missing modules:** salt-in strategy (K+ accumulation), acidic proteome adaptation, Na+ homeostasis (specificity beyond osmotic balance)
- `ambient_nacl —induces→ salt_in_strategy`  (DOI:10.1186/1746-1448-4-2 — Oren (2008) reviews salt-in as o)
- `salt_in_strategy —increases→ intracellular_K_accumulation`  (DOI:10.1186/1746-1448-4-2 — Oren (2008) establishes that sal)
- `acidic_proteome —enables→ protein_function_at_high_salt`  (DOI:10.1186/1746-1448-4-2 — Oren (2008) shows acidic proteom)
- `compatible_solute_accumulation —increases→ maximal_growth_rate`  (DOI:10.1099/acmi.0.000359 — Abosamaha et al. (2022) demonstr)
- `na_h_antiporters —maintains→ cytoplasmic_na_homeostasis`  (DOI:10.1128/aem.00145-24 — Xing et al. (2024) document Na+/H)
- `cytoplasmic_na_homeostasis —enables→ osmotic_balance`  (DOI:10.1186/1746-1448-4-2 — Oren (2008) links ion homeostasi)
- _Existing graph captures compatible-solute/salt-out pathway but omits equally canonical salt-in (K+ accumulation + acidic proteome) module; graph has structural backbone but misses full mechanistic breadth covering both major osmoadaptation strategies documented in 2024 literature._

### environment/obligately_aerobic  — *shallow* (4 edges)
- **Missing modules:** ROS detoxification (SOD/catalase/peroxidases), O₂-dependent cofactor biosynthesis (NAD+/PLP/heme), Fe-S cluster oxidation damage and repair, detailed anoxia→ETC-interruption→PMF-failure cascade
- `superoxide dismutase (SOD) —mitigates→ superoxide stress`  (Khademian 2021, https://doi.org/10.1016/j.tim.2020.10.001: a)
- `catalase activity —mitigates→ hydrogen peroxide stress`  (Khademian 2021 / Mrnjavac 2024, https://doi.org/10.1016/j.ti)
- `absence of O2 —interrupts flux through→ electron transport chain`  (Ciemniecki 2020, https://doi.org/10.1128/JB.00797-19: interr)
- `protoporphyrinogen oxidase —enables→ heme biosynthesis`  (Mrnjavac 2024, https://doi.org/10.1002/1873-3468.14906: O₂-d)
- `superoxide or H2O2 —oxidizes/inactivates→ Fe-S cluster enzymes`  (Khademian 2021, https://doi.org/10.1016/j.tim.2020.10.001: r)
- `oxygen-dependent terminal oxidases —support colonization of→ oxic niches`  (Mrnjavac 2024, https://doi.org/10.1002/1873-3468.14906: O₂-d)
- _Existing graph captures core obligate aerobe-O₂ dependency and terminal oxidase function, but omits three well-supported generic modules: ROS defense (SOD/catalase), O₂-dependent cofactor synthesis (NAD+/PLP/heme), and Fe-S cluster vulnerability—all necessary to explain why obligate aerobes cannot survive anoxia. The report explicitly flags taxon-specific edges (E. coli MFS transporters for bo3, P. aeruginosa CIO tolerance) and universal cofactor-synthesis uncertainty to avoid; medium-priority enrichment should focus on ROS machinery._

### environment/obligately_alkaphilic  — *shallow* (6 edges)
- **Missing modules:** potassium uptake system (TrkAH) for membrane potential and pH homeostasis, cell envelope proton capture mechanism (S-layer/secondary cell wall polymers), compatible solute osmoprotection (ectoine, glycine betaine)
- `TrkAH transport system —contributes to→ cytoplasmic pH homeostasis`  (DOI:10.1128/AEM.00145-24 (Xing et al. 2024): 'The TrkAH tran)
- `secondary cell wall polymers —increases→ net negative surface charge`  (DOI:10.3389/fmicb.2022.1034164 (Yao et al. 2023): alkaliphil)
- `net negative surface charge —increases attraction to→ proton`  (DOI:10.3389/fmicb.2022.1034164 (Yao et al. 2023): net charge)
- `alkaline external pH —causes→ acetate dissociation to anion`  (DOI:10.3389/fmicb.2023.1233691 (Khomyakova et al. 2023): hig)
- `ectoine biosynthesis —provides→ osmoprotection`  (DOI:10.3389/fmicb.2023.1233691 (Khomyakova et al. 2023): ect)
- `monovalent cation/proton antiporters —are essential for→ growth under halophilic and alkaliphilic stress`  (DOI:10.1128/AEM.00145-24 (Xing et al. 2024): antiporters ess)
- _Existing graph captures the core Na+/H+ antiporter–ATP synthase sodium cycle but lacks 3 generic mechanistic modules (K+ uptake, cell-envelope proton capture, compatible-solute osmoprotection) supported by 2023–2024 literature; K+ uptake and S-layer mechanisms are broadly documented across alkaliphiles and not flagged as assay-specific, making them valid enrichment targets._

### environment/obligately_anaerobic  — *shallow* (4 edges)
- **Missing modules:** ROS cascade/Fenton chemistry, DNA damage pathway, glycyl-radical enzyme inactivation, ROS detoxification defenses, protein oxidation repair module
- `molecular_oxygen —inactivates→ pyruvate formate-lyase`  (DOI:10.1038/s41579-021-00583-y — PFL is rapidly inactivated )
- `superoxide —oxidizes→ Fe-S cluster`  (DOI:10.1038/s41579-021-00583-y)
- `hydrogen_peroxide —reacts_with→ Fe(II)`  (DOI:10.1038/s41579-021-00583-y — Fe(II) + H2O2 generates hyd)
- `hydroxyl_radical —damages→ DNA`  (DOI:10.1038/s41579-021-00583-y — Hydroxyl radicals create ir)
- `ROS_detoxification_module —protects_from→ oxidative_damage`  (DOI:10.1186/s40168-024-01909-7 — Catalase-peroxidase (KatG),)
- `protein_repair_module —enables_recovery_from→ oxidized_protein_damage`  (DOI:10.1186/s40168-024-01909-7 — Thioredoxin (TrxA/B) and me)
- _Existing graph captures core oxygen toxicity but lacks well-supported generic mechanisms for ROS cascade, DNA damage, specific enzyme inactivation (PFL), and defenses/repair systems documented in recent comprehensive literature."_

### environment/ph_growth_preference  — *shallow* (5 edges)
- **Missing modules:** F1F0-ATPase proton-export bioenergetics, amino-acid decarboxylase proton-consuming metabolism, Na+/H+ antiporter alkaline homeostasis mechanism, ion homeostasis (K+/Na+ balance), membrane fatty-acid composition regulation
- `cytoplasmic_ph_homeostasis —depends_on→ F1F0-ATPase_proton_pump`  (DOI:10.1093/femsre/fuad062 (Atasoy 2024: strong review suppo)
- `acidic_external_ph —activates→ amino_acid_decarboxylase_systems`  (DOI:10.1093/femsre/fuad062 (Atasoy 2024: strong review suppo)
- `alkaline_external_ph —activates→ Na_H_antiporter_system`  (DOI:10.1038/nrmicro2549 (Krulwich 2011: foundational and str)
- `Na_H_antiporter_system —enables→ cytoplasmic_ph_homeostasis`  (DOI:10.1038/nrmicro2549 (Krulwich 2011: Na+/H+ antiporters a)
- `amino_acid_decarboxylation —consumes→ proton_H_plus`  (DOI:10.1093/femsre/fuad062 (Atasoy 2024: good generic mechan)
- `ion_homeostasis —supports→ cytoplasmic_ph_homeostasis`  (DOI:10.3389/fmicb.2022.1034164 (Yao 2023: good mechanistic e)
- _Existing graph captures foundational trait scope and homeostasis requirement but lacks explicit molecular effectors; report documents 4+ generic mechanistic modules (F1F0-ATPase, decarboxylases, antiporters, ion transport) not yet integrated._

### environment/ph_optimum_high  — *shallow* (4 edges)
- **Missing modules:** sodium bioenergetics (Na+ gradient &amp; Na+-ATPase coupling), K+ homeostasis (TrkAH uptake system), compatible solute accumulation (Opu/ProU), respiratory chain context (branched terminal oxidases)
- `Na+/H+ antiporters —establish→ transmembrane Na+ gradient`  (DOI:10.1128/AEM.00145-24 (Xing et al. 2024) describes antipo)
- `transmembrane Na+ gradient —powers→ Na+-translocating ATPase`  (DOI:10.1128/AEM.00145-24 explicitly names Na+-translocating )
- `TrkAH K+ uptake system —maintains→ membrane potential`  (DOI:10.1128/AEM.00145-24 (Xing et al. 2024 p. 19-21): 'The T)
- `K+ homeostasis —contributes to→ alkaliphile pH homeostasis`  (DOI:10.1128/AEM.00145-24 (Xing et al. 2024): TrkAH is descri)
- `Compatible solute uptake (Opu/ProU) —supports→ growth in haloalkaline conditions`  (DOI:10.1128/AEM.00145-24 (Xing et al. 2024): 'N. thermophilu)
- `Branched respiratory chain terminal oxidases —pump→ protons across membrane`  (DOI:10.3389/fmicb.2024.1468929 (Jong et al. 2024): quantifie)
- _Graph captures core pH-homeostasis backbone but misses sodium-cycle bioenergetics and K+/compatible-solute modules that are generic, broadly supported in 2024 literature and not taxon-specific._

### environment/ph_optimum_low  — *shallow* (3 edges)
- **Missing modules:** electrochemical proton barrier via reversed membrane potential, membrane passive proton impermeability barrier, active proton export via ATP-driven and respiratory-chain pumps
- `large transmembrane ΔpH —drives establishment of→ reversed membrane potential (inside-positive Δψ)`  (10.1038/nrmicro2549)
- `reversed membrane potential —counteracts→ proton influx`  (10.1038/nrmicro2549)
- `rigid proton-impermeable membrane —decreases→ passive proton permeability`  (10.3389/fmicb.2023.1149903)
- `proton-pumping respiratory complexes —exports→ protons from cytoplasm`  (10.1038/nrmicro2549)
- `maintained cytoplasmic pH (~6) —enables→ growth at acidic external pH`  (10.1038/nrmicro2549)
- `low external pH —establishes→ large transmembrane pH gradient`  (10.1038/nrmicro2549)
- _Existing graph is a foundational stub; research report identifies 5 mechanistic strategies, of which 3 (electrochemistry, impermeability, active export) are generic and broadly supported but absent from graph._

### environment/ph_optimum  — *shallow* (4 edges)
- **Missing modules:** ATP synthesis by F0F1-ATP synthase, Ion antiporter activity (Na+/H+, K+/H+), Metabolite decarboxylation (PMF generation and pH homeostasis), Cytoplasmic buffering capacity
- `proton_motive_force —drives→ ATP_synthesis_by_F0F1_ATPase`  (Poolman 2023 DOI:10.1093/femsre/fuad033: 'Protons participat)
- `cytoplasmic_pH_homeostasis —enabled_by→ Na_H_antiporter_activity`  (Poolman 2023 DOI:10.1093/femsre/fuad033: 'Key regulators of )
- `metabolite_decarboxylation_pathways —contributes_to→ cytoplasmic_pH_homeostasis`  (Poolman 2023 DOI:10.1093/femsre/fuad033: 'the chemistry of t)
- `metabolite_decarboxylation_pathways —generates→ proton_motive_force`  (Poolman 2023 DOI:10.1093/femsre/fuad033: 'the free energy ch)
- `cytoplasmic_buffering_capacity —stabilizes→ cytoplasmic_pH`  (Poolman 2023 DOI:10.1093/femsre/fuad033: 'The buffering capa)
- `external_pH —contributes_to→ ΔpH_component_of_PMF`  (Poolman 2023 DOI:10.1093/femsre/fuad033: 'The proton motive )
- _Existing graph captures external pH-PMF-growth spine but misses 4 generic mechanistic modules (ATP synthase, ion antiporters, decarboxylation, buffering) that are well-supported and universal across microbes; report's expert synthesis emphasizes these as central to the homeostatic balance determining pH optimum."_

### environment/piezotolerant  — *shallow* (2 edges)
- **Missing modules:** stress-proteostasis circuitry (heat-shock regulon, rpoH/rpoE/dnaK/groEL), compatible-solute accumulation (piezolytes: glutamate, betaine), respiration remodeling (pressure-conditional metabolism), detailed membrane fluidity mechanism (pressure → fluidity loss → unsaturated/branched fatty acid synthesis)
- `hydrostatic pressure —decreases→ membrane fluidity`  (DOI:10.3390/microorganisms11071629 — 'HHP reduces membrane f)
- `membrane fluidity reduction —triggers increase in→ unsaturated fatty acids`  (DOI:10.3390/microorganisms11071629 — 'organisms counter HHP )
- `hydrostatic pressure —induces transcription of→ heat-shock regulon (rpoH, rpoE, dnaK, groEL)`  (DOI:10.3389/fmicb.2024.1470617 — 'key heat shock genes trans)
- `hydrostatic pressure —triggers accumulation of→ piezolytes (glutamate, betaine, β-hydroxybutyrate)`  (DOI:10.3390/microorganisms11071629 — 'molecules accumulate i)
- `piezolyte accumulation —protects proteins via→ preferential hydration`  (DOI:10.3390/microorganisms11071629 — 'compatible solutes act)
- `hydrostatic pressure —upregulates→ outer membrane protein OmpH`  (DOI:10.3390/microorganisms11071629 — 'OmpH abundance increas)
- _Existing graph captures membrane adaptation but lacks stress proteostasis, compatible-solute chemistry, and mechanistic detail on fatty-acid remodeling; all omitted mechanisms are generic and well-supported across 2023–2024 literature._

### environment/psychrophilic  — *shallow* (6 edges)
- **Missing modules:** cryoprotective solutes (trehalose, compatible solutes), nucleic acid maintenance / cold-induced translation constraints (RNA helicases), oxidative stress / ROS management
- `low_temperature —increases→ reactive_oxygen_species`  (DOI:10.1002/embr.201338170)
- `cold_shock_proteins —regulates→ transcription_and_translation`  (DOI:10.1002/embr.201338170)
- `trehalose —prevents→ protein_denaturation_and_aggregation`  (DOI:10.1038/sj.embor.7400662)
- `compatible_solutes —lowers→ freezing_point_of_intracellular_environment`  (DOI:10.3389/fmicb.2023.1215837)
- `RNA_helicases —restores→ normal_transcription_and_translation`  (DOI:10.3389/fmicb.2023.1215837)
- `compatible_solutes —stabilizes→ proteins_and_membranes`  (DOI:10.37256/amtt.5220244537)
- _Existing graph has core backbone (membrane fluidity, cold enzymes, cryoprotection) but misses 3 GENERIC modules: cryoprotective solutes, cold-induced translation constraints, and ROS management—all well-supported in literature as universal mechanisms not strain-specific._

### environment/psychrotolerant  — *shallow* (4 edges)
- **Missing modules:** compatible solute osmoprotection (glycine betaine, trehalose, glycerol, etc.), extracellular polymeric substances (EPS) cryoprotection, membrane rigidification as initiating stressor / detection
- `low_temperature —causes→ membrane_rigidification`  (DOI:10.1128/spectrum.03925-23)
- `compatible_solutes —protects→ proteins_and_membranes`  (DOI:10.37256/amtt.5220244537)
- `compatible_solute_accumulation —enables→ psychrotolerant_trait`  (DOI:10.37256/amtt.5220244537)
- `extracellular_polymeric_substances —provides_cryoprotection_against→ freeze_thaw_stress`  (DOI:10.37256/amtt.5220244537)
- `eps_accumulation —improves_survival_in→ cold_environments`  (DOI:10.1016/j.femsec.2004.12.003)
- `unsaturated_hopanoids —increases_with→ decreasing_temperature`  (DOI:10.1007/s42770-023-01057-4)
- _Existing graph captures low-temp → membrane stress → lipid remodeling → trait pathway but omits two major generic modules: compatible solute osmoprotection and EPS cryoprotection, both appearing broadly in the literature across multiple organisms._

### environment/radiotolerant  — *shallow* (3 edges)
- **Missing modules:** ROS as damage mediator, enzymatic ROS detoxification, non-enzymatic antioxidants (carotenoids), UV-damage repair module
- `ionizing radiation —causes→ reactive oxygen species (ROS)`  (DOI:10.1371/journal.pone.0304810 — 'Another aftermath of irr)
- `Mn2+ —scavenges→ reactive oxygen species (ROS)`  (DOI:10.1128/spectrum.03838-23 — 'manganese is an antioxidant)
- `catalase —detoxifies→ reactive oxygen species (ROS)`  (DOI:10.1128/aem.01538-23 — 'catalase-mediated detoxification)
- `carotenoids —scavenge→ reactive oxygen species (ROS)`  (DOI:10.3390/su17177864 — 'deinoxanthin scavenges ROS quantit)
- `ultraviolet radiation —damages→ DNA`  (DOI:10.3390/genes14091803 — UV causes helix-distorting lesio)
- `ROS —causes→ protein damage (carbonylation)`  (DOI:10.1128/aem.01538-23 — 'increased protein carbonylation')
- _The existing 3-node graph captures DNA repair and Mn-antioxidant protection but misses ROS as a damage intermediate and enzymatic+non-enzymatic antioxidant diversification, warranting expansion to reflect the multi-modal antioxidant architecture documented in recent literature."_

### environment/slightly_halophilic  — *shallow* (4 edges)
- **Missing modules:** ectoine biosynthesis operon activation by osmotic stress, glycine betaine biosynthesis pathway, ion homeostasis regulatory coordination
- `osmotic_stress —upregulates→ ectoine_biosynthesis_operon`  (Huang 2022 (DOI:10.1038/s42003-022-04319-3) and Zou 2024 (DO)
- `ectoine_biosynthesis_operon —enables→ ectoine_accumulation`  (Zou 2024 (DOI:10.1128/aem.01905-23) demonstrates ectABC knoc)
- `ectoine_accumulation —mitigates→ osmotic_stress`  (Zou 2024 (DOI:10.1128/aem.01905-23) shows ectABC-deficient m)
- `osmotic_stress —upregulates→ proline_glycine_betaine_transporter_proWXV`  (Huang 2022 (DOI:10.1038/s42003-022-04319-3) identifies proWX)
- `proline_glycine_betaine_transporter_proWXV —mediates_uptake_of→ glycine_betaine`  (Huang 2022 (DOI:10.1038/s42003-022-04319-3) annotates proWXV)
- `glycine_betaine_accumulation —mitigates→ osmotic_stress`  (Xing 2024 (DOI:10.1128/aem.00145-24) shows intracellular gly)
- _Graph captures core osmotic-stress-to-compatible-solutes pathway but abstracts away the specific ectoine-biosynthesis and glycine-betaine-biosynthesis modules that recur across multiple taxa in the literature, making the mechanistic detail shallow despite adequate scaffolding."_

### environment/stenohaline  — *shallow* (5 edges)
- **Missing modules:** salt-in K+ uptake strategy, salt-out compatible-solute accumulation, c-di-AMP master regulation of osmoadaptation, mechanosensitive channel-mediated shock response, ion homeostasis molecules (K+, Na+, metabolites)
- `osmotic_imbalance —triggers→ K_plus_import`  (DOI:10.1093/femsml/uqad020 — canonical osmoadaptation respon)
- `K_plus_import_systems —mediates→ salt_in_osmoadaptation`  (DOI:10.1186/s40168-024-01817-w — Wu 2024 identifies COG0168 )
- `c_di_AMP —inhibits→ K_plus_import_systems`  (DOI:10.1128/mmbr.00181-23 — Foster 2024 identifies c-di-AMP )
- `compatible_solute_uptake_synthesis —mediates→ salt_out_osmoadaptation`  (DOI:10.1186/s40168-024-01817-w)
- `c_di_AMP —inhibits→ compatible_solute_importers`  (DOI:10.1128/mmbr.00181-23 — Foster 2024 describes c-di-AMP b)
- `mechanosensitive_channels —enables_rapid_release_of→ osmolytes`  (DOI:10.1128/mmbr.00181-23 — Foster 2024 identifies mechanose)
- _Existing graph captures osmotic imbalance cascade but omits 5 major generic mechanistic modules (salt-in/K+, salt-out/compatible solutes, c-di-AMP regulation, mechanosensitive response, ion homeostasis molecules); report strongly supports enrichment with Foster 2024 c-di-AMP framework and Wu 2024 K+ transporter associations, while excluding taxon-specific edges (Streptomyces genes, Natranaerobius quantitatives, Pearl River estuary markers)._

### environment/temperature_optimum_mid3  — *shallow* (3 edges)
- **Missing modules:** homeoviscous adaptation (desaturation and lipid remodeling), proteostasis machinery (DnaK/GroEL chaperone system required above ~30 °C)
- `upper_mesophilic_environment —triggers→ homeoviscous adaptation`  (DOI:10.1007/s42770-023-01057-4 (ramon2023ageneraloverview))
- `homeoviscous adaptation —includes→ membrane desaturation and UFA incorporation`  (DOI:10.1128/spectrum.03925-23 (sidarta2024lipidphaseseparati)
- `membrane rigidification —triggers→ response to cold`  (DOI:10.1128/spectrum.03925-23 (sidarta2024lipidphaseseparati)
- `upper_mesophilic_environment —requires→ DnaK chaperone system`  (DOI:10.1007/s12275-023-00031-x (moon2023temperaturemattersba)
- `proteostasis machinery —maintains→ protein stability at upper mesophilic temperatures`  (DOI:10.1007/s12275-023-00031-x (moon2023temperaturemattersba)
- `monounsaturated fatty acid incorporation —increases→ membrane fluidity`  (DOI:10.1007/s42770-023-01057-4 (ramon2023ageneraloverview))
- _Existing graph captures high-level adaptation concept but lacks mechanistic detail on the two core generic mechanisms: membrane lipid homeoviscous adaptation (desaturation, UFA remodeling) and the DnaK/GroEL proteostasis system that becomes essential above ~30 °C in mesophiles._

### environment/temperature_optimum  — *shallow* (5 edges)
- **Missing modules:** lipid_biosynthetic_regulation_FadR_FabR, membrane_thickness_sensing_and_response, cell_division_fluidity_coupling, unsaturated_vs_saturated_fatty_acid_balance
- `ambient_temperature —regulates→ fatty_acid_desaturase_activity`  (10.1128/spectrum.03925-23)
- `temperature_decrease —activates→ membrane_fluidity_sensing_machinery`  (10.1007/s42770-023-01057-4)
- `FadR_transcriptional_regulator —activates→ unsaturated_fatty_acid_biosynthesis`  (10.1111/mmi.15323)
- `reduced_membrane_fluidity —triggers→ ppGpp-mediated_growth_modulation`  (10.1111/mmi.15323)
- `unsaturated_fatty_acid_proportion —maintains→ membrane_fluidity`  (10.1039/d3sc04523d)
- `ambient_temperature —sets_homeostatic_target_for→ membrane_physical_state`  (10.1007/s42770-023-01057-4)
- _Existing graph captures backbone (temperature→fluidity→growth) but misses lipid biosynthetic regulation, membrane-sensing cascade, division coupling, and explicit UFA/SFA balance; these are GENERIC and well-supported across literature; archaeal GMGT edges excluded as taxon-specific/uncertain per report warnings._

### environment/temperature_preference  — *shallow* (6 edges)
- **Missing modules:** homeoviscous adaptation (fatty-acid desaturase pathway), RNA thermometer sensing and translation control, cold-shock protein machinery (CspA/CsdA/RNase R), compatible solute synthesis (RpoS-trehalose pathway), DNA topology remodeling (thermophile reverse gyrase)
- `low_temperature —activates→ fatty_acid_desaturase_expression`  (DOI:10.1007/s42770-023-01057-4 (Ramon 2023, pages 5-7) descr)
- `fatty_acid_desaturase_expression —increases→ unsaturated_membrane_fatty_acids`  (DOI:10.1007/s42770-023-01057-4 (Ramon 2023, pages 5-7) estab)
- `unsaturated_membrane_fatty_acids —increases→ membrane_fluidity`  (DOI:10.1007/s42770-023-01057-4 (Ramon 2023, pages 5-7) core )
- `temperature_upshift —denatures→ RNA_thermometer`  (DOI:10.1007/s12275-023-00031-x (Moon 2023, pages 3-5) FourU )
- `cold_shock —induces→ CspA_mediated_translation_control`  (DOI:10.1007/s12275-023-00031-x (Moon 2023, pages 3-5) generi)
- `high_temperature —increases_activity_of→ reverse_gyrase`  (DOI:10.1264/jsme2.me23087 (Takemata 2024) and DOI:10.1111/mm)
- _Graph correctly frames temperature and membrane/protein endpoints but lacks the key GENERIC mechanistic intermediates (desaturase pathway, RNA sensing, cold-shock proteins) that literature identifies as universal bacterial temperature-response systems._

### environment/thermotolerant  — *shallow* (3 edges)
- **Missing modules:** RpoH regulatory cascade (sigma-32), RpoE envelope stress response, oxidative stress mitigation (ROS/antioxidant defense), compatible solutes accumulation (trehalose/mannitol)
- `elevated_temperature —activates→ RpoH (sigma-32)`  (DOI:10.1186/s12934-024-02602-y: RpoH regulates groEL, dnaK, )
- `RpoH (sigma-32) —positively_regulates→ GroESL-DnaK-ClpB expression`  (DOI:10.1186/s12934-024-02602-y: 'The expression of groEL, dn)
- `RpoE (sigma-24) —positively_regulates→ membrane_protein_folding`  (DOI:10.1007/s12275-023-00031-x: RpoE activates HtrA, DegP pr)
- `heat_shock_response —activates→ antioxidant_defense (SOD/GPx/thioredoxin_reductase)`  (DOI:10.1186/s12934-024-02602-y: Antioxidant genes upregulate)
- `trehalose_accumulation —enables→ thermotolerant_growth`  (DOI:10.3390/jof10030185: Trehalose synthesis upregulated und)
- `membrane_lipid_remodeling —maintains→ membrane_integrity_under_heat`  (DOI:10.1128/spectrum.01627-23: HsfA controls sdeA (Δ9-fatty )
- _Existing graph is adequate as a minimal skeleton but misses 4 generic mechanistic modules (RpoH cascade, envelope stress, ROS defense, compatible solutes) that span multiple organisms and are well-supported in the 2023–2024 literature."_

### genomics/gc_skew  — *shallow* (2 edges)
- **Missing modules:** cytosine deamination at replication fork, gene strand bias / leading-strand enrichment, strand-specific DNA repair (MMR/TC-NER), translational selection and codon-position bias, cumulative GC skew extrema inference (ori/ter localization)
- `lagging strand single-stranded DNA exposure —increases→ cytosine deamination`  (DOI:10.1101/2023.11.15.567178)
- `cytosine deamination at replication forks —contributes_to→ GC skew`  (DOI:10.3389/fmicb.2026.1727296)
- `leading-strand gene density / gene strand bias —contributes_to→ GC skew`  (DOI:10.1101/2023.11.15.567178)
- `strand-specific DNA repair (MutSL-dependent MMR / TC-NER) —contributes_to→ GC skew`  (DOI:10.3389/fmicb.2026.1727296)
- `cumulative GC skew global minimum —indicates→ replication origin (ori)`  (DOI:10.1093/nar/26.10.2286)
- `cumulative GC skew global maximum —indicates→ replication terminus (ter)`  (DOI:10.1093/nar/26.10.2286)
- _Existing graph captures the core replication link but misses five generic mechanistic modules (deamination cascade, gene strand bias, repair mechanisms, coding constraints, and ori/ter inference) that the literature identifies as major contributors._

### genomics/genome_streamlining  — *shallow* (2 edges)
- **Missing modules:** metabolic auxotrophy and cross-feeding consequences, shortened gene length and compact genomic architecture as streamlining signatures, cofactor/vitamin biosynthesis reduction leading to community dependence
- `oligotrophic_environment —selects for→ shorter_coding_genes`  (DOI:10.1038/s41467-023-36988-x)
- `genome_streamlining —leads to→ metabolic_auxotrophy_for_vitamins_and_cofactors`  (DOI:10.1038/s41467-024-46374-w)
- `metabolic_auxotrophy —promotes→ metabolic_cross_feeding`  (DOI:10.1038/s41467-024-46374-w)
- `reduced_cofactor_biosynthesis —increases_dependence_on→ exogenous_b_vitamins_and_precursors`  (DOI:10.1038/s41467-024-46374-w)
- `streamlining_trait —is_characterized_by→ short_intergenic_spacers_and_compact_genome`  (DOI:10.1128/msystems.00898-23)
- `oligotrophic_environment —selects_for→ reduced_two_component_regulatory_systems`  (DOI:10.21203/rs.3.rs-4258556/v1)
- _Existing graph captures classical streamlining theory (oligotrophic selection → reductive evolution) but omits generic peer-reviewed modules on auxotrophy/cross-feeding (Giordano 2024, ocean-wide) and genomic signatures (Ngugi 2023, 364 metagenomes); drift-mechanism alternatives (Zhang/Wang 2024) are lineage-specific and preprint-derived, flagged but not essential for completeness."_

### genomics/transposable_element  — *shallow* (2 edges)
- **Missing modules:** transposase as catalytic participant, gene disruption as direct transposition consequence, regulatory control of transposase expression/mobility, target site duplication structural mechanism
- `transposable element —has_participant→ transposase`  (DOI:10.1128/MMBR.00119-22 — IS26 encodes DDE-family transpos)
- `transposase —enables→ transposition`  (DOI:10.1128/MMBR.00119-22 — transposase activity is required)
- `DNA transposition —causes→ gene disruption`  (DOI:10.1038/s41467-023-39964-7 — IS movement directly disrup)
- `DNA transposition —causes→ target site duplication`  (DOI:10.1038/s41467-023-39964-7 — IS insertion typically crea)
- `homologous recombination between IS copies —causes→ genome rearrangement`  (DOI:10.1038/s41467-023-39964-7 — recombination between ident)
- `stress (DNA damage, oxidative) —increases→ transposase activity`  (DOI:10.1038/s41467-023-39964-7 + DOI:10.3390/microorganisms1)
- _Existing graph captures the core transposition → rearrangement spine but lacks explicit transposase participation, gene disruption as direct mechanism, regulatory inputs, and structural intermediates described as generic in the report._

### metabolism/disproportionation  — *shallow* (7 edges)
- **Missing modules:** S4I (tetrathionate intermediate) pathway with TsdA and TetH steps, thiosulfate-specific disproportionation stoichiometry, elemental sulfur solubility constraint and activation bottleneck, sulfide-scavenging enabling condition for S0 disproportionation
- `thiosulfate —disproportionated via→ TsdA to tetrathionate`  (DOI:10.3389/fmicb.2024.1426584 (Twible 2024: tsdA catalyzes )
- `tetrathionate —hydrolyzed and disproportionated by→ TetH to sulfate + sulfide + elemental sulfur`  (DOI:10.3389/fmicb.2024.1426584 (Twible 2024: TetH produces S)
- `elemental sulfur —disproportionation enabled by→ sulfide removal via iron minerals`  (DOI:10.1128/msystems.00954-22 (Wang 2023: S0 disproportionat)
- `low elemental sulfur solubility —constrains→ sulfur activation and uptake mechanisms`  (DOI:10.1128/msystems.00954-22 (Wang 2023: elemental sulfur ~)
- `SOR (sulfur oxygenase reductase) —catalyzes O2-dependent disproportionation of→ elemental sulfur to sulfite and sulfide`  (DOI:10.1007/978-3-031-54306-7_15 (D'Ermo 2024: SOR catalyzes)
- `sulfite —is more energetically favorable for disproportionation than→ elemental sulfur`  (DOI:10.1128/msystems.00954-22 and Yan 2024 thesis (sulfite Δ)
- _The existing graph captures the core redox-split trait definition and basic substrate/product logic, but lacks the recent mechanistically detailed pathways (especially S4I tetrathionate intermediate pathway with TsdA/TetH) and critical physical/bioenergetic constraints documented as generic mechanisms across 2023-2024 literature."_

### metabolism/fermentation  — *shallow* (5 edges)
- **Missing modules:** entry pathways (glycolysis, pentose phosphate pathway), pyruvate:ferredoxin oxidoreductase (PFOR) enzyme node, electron bifurcation mechanism, ferredoxin reoxidation alternatives, ion-gradient ATP synthesis (Rnf/Ech supplementary modules)
- `organic substrate —catabolized via→ glycolysis`  (DOI:10.1093/femsre/fuae016 (Hackmann 2024, lines 276-277): ')
- `glycolysis —produces→ pyruvate`  (DOI:10.1093/femsre/fuae016 (Hackmann 2024, lines 4-5): glyco)
- `pyruvate —oxidized by→ pyruvate:ferredoxin oxidoreductase`  (DOI:10.1093/femsre/fuae016 (Hackmann 2024, lines 283, 313): )
- `electron bifurcation —couples→ reduced ferredoxin and NAD(H)`  (DOI:10.1038/s41467-023-41212-x (Kumar 2023, line 316): 'FBEB)
- `Rnf complex —pumps ions driving→ ion-motive force for ATP synthesis`  (DOI:10.1093/femsre/fuae016 (Hackmann 2024, lines 321-322): ')
- `ferredoxin:NAD+ oxidoreductase —transfers electrons from→ reduced ferredoxin to NAD+`  (DOI:10.1093/femsre/fuae016 (Hackmann 2024, line 315): 'ferre)
- _Graph captures redox-balance backbone and SLP but misses entry pathways, PFOR enzyme, electron bifurcation module, and ion-gradient ATP systems documented as generic across diverse fermenters in the Hackmann 2024 synthesis; Rnf/Ech presence and directionality are taxon-dependent so treated as supplementary rather than core-defining edges._

### metabolism/manganese_oxidation  — *shallow* (2 edges)
- **Missing modules:** Mn oxidation intermediate cascade (Mn(II)→Mn(III)→Mn(IV) pathway), O2 as direct electron acceptor, Multicopper oxidase subunit architecture (MnxG, MnxE, MnxF complex), Enzyme-substrate binding/catalytic mechanism
- `multicopper_oxidase —uses→ O2`  (10.1021/jacs.3c06537 (Novikova et al. 2024): Mnx can use O2 )
- `Mn(II) —oxidizes_via→ Mn(III) intermediate`  (10.1021/jacs.3c06537 (Novikova et al. 2024): Cryo-EM structu)
- `Mn(III) intermediate —disproportionates_to→ Mn(IV) oxide`  (10.1021/jacs.3c06537 (Novikova et al. 2024): Mn(III)(OH)Mn(I)
- `manganese_oxidation_trait —requires→ dissolved_oxygen`  (10.1038/s41598-023-36348-1 (Earle et al. 2023): Dissolved ox)
- `multicopper_oxidase —composes_with→ MnxE accessory_subunit`  (10.1021/jacs.3c06537 (Novikova et al. 2024): Cryo-EM structu)
- `multicopper_oxidase —produces→ biogenic_MnOx`  (10.1021/acscatal.3c06119 (Fu et al. 2024): MnxE3F3G complex )
- _Existing graph captures only the entry enzyme and gross product; lacks intermediate oxidation cascade, cofactor requirement (O2), and structural subunit details that the 2024 cryo-EM literature now enables. The omission of the Mn(II)→Mn(III)→Mn(IV) intermediate pathway is the most significant gap, as it obscures the actual catalytic mechanism."_

### metabolism/oxidative_phosphorylation  — *shallow* (5 edges)
- **Missing modules:** electron entry point branching (Complex I vs Complex II), quinone pool mediation and redox cycling, terminal oxidase mechanistic diversity (proton pumping vs electrogenic), oxygen reduction coupling
- `electron_transport_chain —accepts electrons via→ Complex I / NDH-1`  (10.3390/ijms252413421 (grivennikova2024): complex I catalyze)
- `electron_transport_chain —accepts electrons via→ succinate dehydrogenase`  (10.1007/s10863-024-10041-y (uriberamirez2024): succinate deh)
- `electron_transport_chain —transfers electrons via→ quinone pool`  (10.3390/ijms252413421 (grivennikova2024): NADH oxidation by )
- `terminal_oxidases —reduces→ oxygen`  (10.3390/ijms25021277 (nastasi2024): terminal oxidases cataly)
- `heme_copper_oxidase —pumps protons during→ proton_motive_force`  (10.3390/ijms25021277 (nastasi2024): heme-copper oxidases are)
- `cytochrome_bd_oxidase —contributes to via electrogenic transfer→ proton_motive_force`  (10.3390/ijms25021277 (nastasi2024): cytochromes bd generate )
- _Existing graph captures chemiosmotic backbone but lacks explicit electron entry branching, quinone intermediation, terminal oxidase heterogeneity (proton pumping vs electrogenic), and oxygen reduction—all generic modules well-supported by literature._

### metabolism/reductive_tca_cycle  — *shallow* (2 edges)
- **Missing modules:** citrate cleavage module (ACL or CCS/CCL), ferredoxin-dependent carboxylations (PFOR/OGOR/KOR enzymes), reduced ferredoxin electron carrier, energy metabolism coupling (sulfur oxidation via Sox)
- `ATP citrate lyase complex aclAB (EC:2.3.3.8) —enables→ reductive tricarboxylic acid cycle (traitmech:000021)`  (DOI:10.1101/2022.10.25.513756)
- `reduced ferredoxin (CHEBI:57925) —electron_donor_for→ pyruvate:ferredoxin oxidoreductase PFOR (EC:1.2.7.1)`  (DOI:10.3390/life13030627)
- `reduced ferredoxin (CHEBI:57925) —electron_donor_for→ 2-oxoglutarate:ferredoxin oxidoreductase OGOR (EC:1.2.7.3)`  (DOI:10.3390/life13030627)
- `pyruvate:ferredoxin oxidoreductase PFOR (EC:1.2.7.1) —part_of→ reductive tricarboxylic acid cycle (traitmech:000021)`  (DOI:10.3390/life13030627)
- `2-oxoglutarate:ferredoxin oxidoreductase OGOR (EC:1.2.7.3) —part_of→ reductive tricarboxylic acid cycle (traitmech:000021)`  (DOI:10.3390/life13030627)
- `sulfur oxidation via Sox system —provides_energy_for→ reductive tricarboxylic acid cycle (traitmech:000021)`  (DOI:10.1371/journal.pone.0310595)
- _Existing graph captures CO2 entry and citrate output but omits key generic mechanistic modules: citrate-cleavage enzyme(s), ferredoxin-dependent carboxylations (PFOR/OGOR), ferredoxin carrier, and energy-source coupling; prioritize adding enzyme pathway components and electron-carrier relationships._

### metabolism/respiration  — *shallow* (7 edges)
- **Missing modules:** quinone pool mediation of electron flow, terminal oxidase (Complex IV) specificity and water production, Fe(III)/Mn(IV)/sulfate as alternative terminal acceptors, environmental regulation via anoxic microsites, NDH-1/Complex I to quinone pool electron input
- `membrane_electron_transport_chain —transfers electrons through→ quinone_pool`  (Line 317-318: quinone pool links dehydrogenases to terminal )
- `quinone_pool —transfers electrons to→ terminal_oxidases`  (Line 318: ubiquinone/menaquinone connect to terminal oxidase)
- `terminal_oxidases —reduces→ oxygen`  (Line 319: Complex IV uses O2 as terminal electron acceptor f)
- `iron_oxide —serves_as→ terminal_electron_acceptor`  (Section 6 node Fe(III), Line 252: dissimilatory Fe(III) resp)
- `sulfate —serves_as→ terminal_electron_acceptor`  (Section 6 node SO42-, Line 253: dissimilatory sulfate respir)
- `anoxic_microsites —control_availability_of→ terminal_electron_acceptor`  (Line 327: anoxic microsites control local TEA ordering (Lacr)
- _Existing graph captures core donor-to-acceptor-to-energy principle but misses quinone-pool architecture, multiple generic terminal acceptors (Fe/Mn/SO4), and environmental modulation—all generic, universally applicable mechanisms supported by literature._

### morphology/cell_length_large  — *shallow* (3 edges)
- **Missing modules:** SOS response activation pathway, SulA-mediated FtsZ polymerization inhibition, FtsZ availability as rate-limiting factor for division timing
- `SOS response —induces→ SulA expression`  (DOI:10.1101/2025.05.13.653778)
- `SulA protein —inhibits→ FtsZ polymerization`  (DOI:10.1101/2025.05.13.653778)
- `FtsZ abundance —rate-limiting-for→ division timing onset`  (DOI:10.1038/s41467-024-54242-w — E. coli quantitative pertur)
- `DNA damage stimulus —activates→ SOS response`  (DOI:10.1101/2025.05.13.653778)
- `division timing delay —mechanistic basis includes→ SulA-mediated FtsZ inhibition`  (DOI:10.1101/2025.05.13.653778)
- `constriction onset checkpoint —depends on→ FtsZ assembly competence`  (DOI:10.1038/s41467-024-54242-w)
- _Existing graph captures the two-layer backbone (elongation + division delay), but lacks explicit representation of SOS/SulA and FtsZ-dosage mechanisms that the report identifies as generic, well-supported routes to division delay; antibiotic and stress-condition context is noted but correctly marked as application-specific rather than core generic mechanism._

### morphology/cell_width_large  — *shallow* (3 edges)
- **Missing modules:** RodA–PBP2 allosteric activation coupling synthesis activation, MreB-guided circumferential peptidoglycan insertion geometry, MreC/MreD balance regulating PBP2 activity, RodZ structural organization of Rod complex
- `rod_complex_pg —depends_on→ mreb_filament_orientation`  (DOI:10.1038/s41467-024-49785-x — Middlemiss et al. (2024) qu)
- `mreB_filaments —directs→ circumferential_pg_insertion`  (DOI:10.1038/s41467-024-49785-x, DOI:10.1073/pnas.2301987120 )
- `roda_pbp2_complex —requires_activation→ rod_complex_pg`  (DOI:10.1038/s41467-023-39037-9 — Shlosman et al. show RodA–P)
- `mrec_mred_balance —regulates→ pbp2_activity`  (DOI:10.1002/mbo3.1385 — Ago et al. directly state balance be)
- `roda_abundance —modulates→ elongasome_processivity_and_width`  (DOI:10.1038/s41467-024-49785-x — Middlemiss et al. quantify )
- `outer_membrane_fortification —suppresses→ rod_complex_morphology_defects`  (DOI:10.1073/pnas.2301987120 — Fivenson et al. show OM streng)
- _Existing graph captures nutrient-rich setpoint shift but misses mechanistic depth: RodA–PBP2 activation, MreB-directed geometry, accessory regulation (MreC/MreD/RodZ), and OM compensation represent generic, multi-organism-validated modules absent from current curation._

### morphology/cell_width_small  — *shallow* (3 edges)
- **Missing modules:** RodZ bridging / Rod complex assembly, MreC/MreD allosteric activation of RodA-PBP2, PG hydrolase balance (synthesis-degradation coupling), Conformational regulation of RodA-PBP2
- `MreC —activates→ RodA-PBP2 complex`  (DOI:10.1038/s41467-023-39037-9 (Shlosman 2023): MreC favors )
- `RodZ —required_for→ Rod complex integrity`  (DOI:10.1002/mbo3.1385 (Ago 2023): RodZ interacts with MreB c)
- `Rod complex integrity —enables→ ordered peptidoglycan architecture`  (DOI:10.1002/mbo3.1385 (Ago 2023): Rod complex defects yield )
- `peptidoglycan hydrolase activity —negatively_regulates→ rod width control`  (DOI:10.1038/s41598-021-04294-5 (Tesson 2022, Bacillus/generi)
- `magnesium ion —inhibits→ peptidoglycan hydrolase activity`  (DOI:10.1038/s41598-021-04294-5 (Tesson 2022): Exogenous Mg2+)
- `RodA-PBP2 conformational opening —increases→ peptidoglycan polymerization and crosslinking`  (DOI:10.1038/s41467-023-39037-9 (Shlosman 2023): Structural o)
- _Graph captures MreB-elongasome-width backbone but omits RodZ bridging, MreC/MreD allosteric control, hydrolase balance, and RodA-PBP2 conformational gating—all generic mechanisms in recent literature."_

### morphology/cell_width_very_small  — *shallow* (3 edges)
- **Missing modules:** peptidoglycan-insertion-mode balance (Rod vs aPBP), MreB-directed cell-width homeostasis, nutrient-uptake efficiency as selective advantage
- `Rod complex —regulates→ cell width`  (Juillot 2021 (DOI:10.1128/msystems.01017-21) describes Rod-c)
- `high surface-to-volume ratio —increases→ nutrient uptake efficiency`  (Belykh 2024 (DOI:10.31951/2658-3518-2024-a-4-795) frames thi)
- `peptidoglycan biosynthetic process —regulates→ cell morphology`  (Juillot 2021 (DOI:10.1128/msystems.01017-21) shows diameter )
- `MreB cytoskeleton —determines→ cell width and curvature`  (Juillot 2021 (DOI:10.1128/msystems.01017-21) identifies MreB)
- `oligotrophs —employ→ reduced transcriptional regulation`  (Noell 2023 (DOI:10.1128/mmbr.00124-22) identifies this as ge)
- `oligotrophic environment —selects for→ high surface-to-volume ratio`  (Implicit in Belykh 2024 and Giovannoni 2014 linkage of small)
- _Existing graph captures ecological selection level (streamlining) but entirely lacks cell-biological width-control machinery (Rod complex, peptidoglycan insertion mode, MreB); latter is generic and peer-reviewed in model systems and essential for achieving ≤0.5 µm phenotype._

### morphology/coccobacillus_shaped  — *shallow* (4 edges)
- **Missing modules:** FtsZ/divisome-mediated elongation control, PBP localization/septal targeting regulation, PBP2 structural cofactor requirements (zinc-binding)
- `ftsZ —regulates→ peptidoglycan_synthesis`  (FtsZ divisome geometry directs PG insertion pattern)
- `rodA —required_for→ peptidoglycan_synthesis`  (RodA (SEDS partner of PBP2) is core to elongasome-mediated r)
- `pbp2_zinc_binding_site —required_for→ mreB`  (PBP2 zinc-binding site integrity required for protein stabil)
- `gpsB —regulates_localization_of→ pbp2`  (GpsB controls PBP2/PBP4 septal/peripheral localization)
- `ftsZ_filament_geometry —directs→ helical_pg_insertion`  (Altered FtsZ geometry generates helical/asymmetric PG insert)
- `septal_growth —requires→ rodA`  (RodA participates in both elongation and septal/divisional P)
- _Existing graph captures elongasome basics but lacks divisome/FtsZ module and PBP regulatory/structural requirements; both are documented as generic mechanisms across multiple taxa and are high-priority additions._

### morphology/ellipsoidal  — *shallow* (5 edges)
- **Missing modules:** DivIVA phosphorylation-mediated aspect ratio control, MltG-dependent peripheral PG remodeling, Undecaprenyl phosphate precursor supply system, RodA/MreD elongasome assembly and cooperation, StkP kinase-DivIVA phosphorylation signaling
- `DivIVA —promotes→ peripheral_peptidoglycan`  (DOI:10.1128/Spectrum.04750-22)
- `RodA —cooperates_with→ PBP2b`  (DOI:10.1111/mmi.13543)
- `MltG —regulates→ ellipsoid_geometry`  (DOI:10.1128/Spectrum.04750-22)
- `mevalonate_pathway —supplies→ undecaprenyl_phosphate`  (DOI:10.7554/eLife.75607)
- `undecaprenyl_phosphate —preferentially_limits→ septal_peptidoglycan`  (DOI:10.7554/eLife.75607)
- `StkP —phosphorylates→ DivIVA`  (DOI:10.1371/journal.pgen.1004275)
- _Existing graph captures the 2-ring septal+peripheral backbone and PBP2b-peripheral link, but misses well-supported generic modules: phosphorylation-control via DivIVA-MltG, elongasome assembly cooperation, precursor-supply constraint, and kinase signaling—all non-taxon-specific and documented across multiple ovococci._

### morphology/flagellated  — *shallow* (5 edges)
- **Missing modules:** flagellar type III secretion system (fT3SS) export pathway, transcriptional hierarchy with anti-sigma regulation (flhDC → FliA/FlgM → class 3 genes), stator-rotor torque generation coupling (H+ conduction through MotA-MotB → FliG electrostatic interaction), flagellar protein assembly and substrate specificity switching (FliK-mediated hook-to-filament checkpoint), detailed chemotactic signal transduction cascade (Tar/Tsr → CheA → CheY-P → FliM binding → rotational switching)
- `flagellar type III secretion system —exports→ flagellar structural subunits`  (DOI:10.1128/ecosalplus.esp-0011-2023)
- `flhDC operon —activates_expression_of→ class 2 flagellar genes`  (DOI:10.1128/ecosalplus.esp-0011-2023)
- `FlgM —inhibits→ FliA sigma factor`  (DOI:10.1128/ecosalplus.esp-0011-2023)
- `hook completion —enables_secretion_of→ FlgM`  (DOI:10.1128/ecosalplus.esp-0011-2023)
- `H+ conduction through MotA-MotB —generates_torque_via→ electrostatic interaction with FliG`  (DOI:10.3390/biom14121488)
- `FliK —triggers_switch_to→ filament assembly`  (DOI:10.3390/biom14121488)
- _Existing graph captures structural phenotype and gross energetics but lacks export machinery, transcriptional checkpoint control, molecular-level stator-rotor coupling, and detailed chemotactic cascade—all generic, well-supported mechanisms in current literature."_

### morphology/fusiform_shaped  — *shallow* (3 edges)
- **Missing modules:** elongasome assembly and MreB orientation, pole-enriched lipid-driven MreB exclusion, spatial gradient of peptidoglycan insertion rate
- `MreB filament —guides→ lateral peptidoglycan synthesis`  (DOI:10.1038/s41579-020-0366-3 — MreB filaments orient PG syn)
- `cardiolipin and phosphatidylglycerol —inhibit→ assembled MreB filaments`  (DOI:10.1007/978-3-030-18768-2_5 — Pole-enriched anionic lipi)
- `RodZ protein —regulates→ MreB polymer localization`  (DOI:10.1186/s12964-025-02373-y — RodZ modulates geometric lo)
- `graded polar peptidoglycan growth —depends_on→ MreB-directed elongasome`  (DOI:10.1038/s41579-020-0366-3 — Elongasome (MreB/RodZ/MreC/M)
- `RodA and cognate PBPs —execute→ lateral peptidoglycan incorporation`  (DOI:10.1016/j.mib.2021.01.011 — SEDS protein RodA + class B )
- `FtsW with divisome —executes→ septal peptidoglycan incorporation`  (DOI:10.1016/j.mib.2021.01.011 — FtsW mediates septal PG synt)
- _Existing graph has correct high-level causal spine but lacks mechanistic scaffold (elongasome, lipid inhibition, SEDS partitioning); all suggested edges are generic, cross-taxon mechanisms, excluding Spiroplasma-specific and assay-specific claims per report warnings."_

### morphology/gliding  — *shallow* (5 edges)
- **Missing modules:** GldLM motor complex, SprB adhesin secretion, Multirail track structure / GldJ, Motor-to-translocon energy transduction
- `proton_gradient —powers→ GldLM_motor`  (DOI:10.1371/journal.pbio.3001443)
- `GldLM_motor —enables→ type_ix_secretion_system`  (DOI:10.1371/journal.pbio.3001443)
- `type_ix_secretion_system —secretes→ SprB_adhesin`  (DOI:10.1371/journal.pbio.3001443)
- `GldJ_protein —component_of→ multirail_track`  (DOI:10.1038/s42003-023-04472-3)
- `SprB_translocation —causes→ cell_propulsion`  (DOI:10.1371/journal.pbio.3001443)
- `GldK_GldN_ring —transduces_energy_from→ SprA_translocon`  (DOI:10.1021/acsomega.3c05155)
- _Existing graph captures energy and adhesin roles but lacks explicit motors, adhesins, and structural tracks; Bacteroidota T9SS mechanism well-supported in 2023-2024 literature but underrepresented in graph nodes/edges._

### morphology/gram_negative  — *shallow* (5 edges)
- **Missing modules:** LPS asymmetry / Lpt-mediated transport, β-barrel OMP biogenesis (SecYEG, BAM, chaperones), Tol-Pal envelope connectivity maintenance, Mla retrograde lipid transport / OM asymmetry homeostasis, Ionic stabilization of LPS packing (Mg2+/Ca2+)
- `lipopolysaccharide —occupies_outer_leaflet_of→ outer_membrane`  (10.1146/annurev-micro-032521-014507)
- `Lpt_pathway —transports→ lipopolysaccharide`  (10.1007/s12275-024-00137-w)
- `BAM_complex —inserts_and_folds→ β-barrel_outer_membrane_proteins`  (10.3390/pathogens13100889)
- `Tol-Pal_system —maintains_connectivity→ outer_membrane_peptidoglycan_inner_membrane_layers`  (10.1038/s44259-024-00065-0)
- `magnesium_ion —stabilizes→ lipopolysaccharide_packing`  (10.3390/pathogens13100889)
- `Mla_pathway —maintains→ outer_membrane_lipid_asymmetry`  (10.3390/pathogens13100889)
- _Existing graph captures the phenotype mechanism (dye loss, counterstain uptake) but omits the generic mechanistic backbone: LPS asymmetry/transport, OMP biogenesis/BAM, envelope-layer connectivity (Tol-Pal), and OM homeostasis (Mla), all well-supported by 2024 reviews (Tan, Bisht, Szczepaniak, Yoon)._

### morphology/gram_positive  — *shallow* (5 edges)
- **Missing modules:** iodine mordant chemistry and CV-iodine complex formation, peptidoglycan mesh porosity determinism, D-alanylation pathway (DltA/DltB/DltC proteins), teichoic acid charge neutralization by D-alanine, LPS/outer-membrane negative effect (comparative mechanism)
- `iodine —causes→ crystal violet-iodine complex formation`  (DOI:10.52403/ijrr.20230934 (Paray 2023) - Iodine interacts w)
- `peptidoglycan mesh porosity —increases→ crystal violet-iodine complex retention`  (DOI:10.1038/s42003-026-10072-8 (García-Miranda 2026) - Low-p)
- `D-alanine —neutralizes→ teichoic acid negative charge`  (DOI:10.1038/s41564-023-01411-0 (Schultz 2023) - D-alanine es)
- `dltA protein —required_for→ D-alanylation of teichoic acids`  (DOI:10.1038/s41564-023-01411-0 (Schultz 2023) - DltA adenyla)
- `outer membrane with lipopolysaccharide —decreases→ crystal violet-iodine complex retention`  (DOI:10.1038/s42003-026-10072-8 (García-Miranda 2026) - LPS-r)
- `dltB membrane protein —enables→ D-alanylation of teichoic acids`  (DOI:10.1038/s41564-023-01411-0 (Schultz 2023) - DltB MBOAT-f)
- _The existing graph captures staining outcome and basic teichoic acid/peptidoglycan architecture but omits iodine-dependent dye chemistry, porosity determinism, and the conserved D-alanylation pathway that are described as generic mechanisms in the research report."_

### morphology/helical_shaped  — *shallow* (4 edges)
- **Missing modules:** bactofilin-M23 peptidase module interaction, Pgp1 PG carboxypeptidase pathway (C. jejuni generic parallel), muropeptide-specific inhibition (tetrapentapeptide accumulation opposes helicity)
- `ccmA —cooperates_with→ M23_peptidase_complex`  (DOI:10.7554/eLife.86577.2 — bactofilin-M23 module conserved )
- `pgp1 —promotes→ peptidoglycan_monomeric_trimeric_conversion`  (DOI:10.1371/journal.ppat.1002602 — Pgp1 DL-carboxypeptidase )
- `tetrapentapeptide_crosslinked_dimer —negatively_regulates→ helical_curvature_twist`  (DOI:10.1016/j.cell.2010.03.046 — quantified 20-50% increase )
- `M23_peptidase_domain_proteins —contributes_to→ peptidoglycan_crosslink_relaxation`  (DOI:10.3389/fmicb.2023.1162806 (2023) and DOI:10.1016/j.cell)
- `Csd4 —promotes→ peptidoglycan_crosslink_relaxation`  (DOI:10.1016/j.cell.2010.03.046 — M14 carboxypeptidase (Csd4))
- `pgp1_overexpression —produces→ straight_or_kinked_nonhelical_morphology`  (DOI:10.1371/journal.ppat.1002602 — dose-sensitive control: e)
- _Existing graph captures H. pylori PG relaxation backbone but misses bactofilin-M23 modular organization, C. jejuni Pgp1 parallel pathway as generic validation, and specific muropeptide inhibition roles._

### morphology/motile  — *shallow* (5 edges)
- **Missing modules:** stator complex H+ channel and torque generation, chemotaxis signal transduction cascade (CheA-CheY-FliM/FliN), gliding motility pathway (GldL/GldM-SprB), T4P extension-retraction cycle details, archaeal flagellar motility
- `MotA-MotB stator complex —acts_as→ transmembrane H+ channel`  (DOI:10.3390/biom14121488)
- `H+ flux through MotA-MotB —generates_torque_via→ electrostatic interaction with FliG`  (DOI:10.3390/biom14121488)
- `CheA —autophosphorylates_and_phosphorylates→ CheY`  (DOI:10.3390/biom14121488)
- `CheY-P —binds→ C-ring flagellar switch complex`  (DOI:10.3390/biom14121488)
- `GldL/GldM motor complex —powers_via_proton_gradient→ gliding motility`  (DOI:10.1128/jb.00068-24)
- `cycles of T4P extension and retraction —enable→ twitching motility`  (DOI:10.1128/msphere.00390-24)
- _Existing graph captures flagellum-centric energy transduction and chemotaxis regulation but lacks stator mechanics, chemotaxis cascade details, non-flagellar mechanisms (gliding, detailed T4P cycles), and archaeal motility that are generic and well-supported in the literature._

### morphology/non_spore_forming  — *shallow* (3 edges)
- **Missing modules:** gene loss of sporulation machinery pathway, phosphorelay initiation sub-pathway (KinA/KinB → Spo0F → Spo0B → Spo0A), Spo0A activity/phosphorylation level distinction from total absence
- `loss_of_sporulation_gene_set —causes→ non_spore_forming_phenotype`  (DOI:10.1111/1462-2920.16145 (Fatton et al. 2022) and DOI:10.)
- `absent_spo0a —predicts→ non_spore_forming_phenotype`  (DOI:10.1128/jb.00079-22 (Galperin et al. 2022) — spo0A absen)
- `low_spo0a_activity —prevents→ endospore_formation`  (DOI:10.3389/fmicb.2021.630573 (Beskrovnaya et al. 2021) — in)
- `sporulation_phosphorelay_disruption —arrests→ sporulation_initiation`  (DOI:10.3390/microorganisms11081928 (Jun et al. 2023) — KinA/)
- `rap_phosphatases —dephosphorylate→ spo0f`  (DOI:10.1038/s41522-024-00594-6 (Xiong et al. 2024) — Rap pho)
- `reduced_spo0f_phosphorylation —decreases_activation_of→ spo0a`  (DOI:10.3390/microorganisms11081928 + DOI:10.1038/s41522-024-)
- _Existing graph captures the Spo0A regulatory bottleneck and downstream morphogenesis pathway but lacks two major generic mechanisms: (1) gene-loss-independent asporogenesis via sporulation machinery deletions, and (2) phosphorelay architecture detail (initiation kinases and Spo0F as intermediate regulator). Recommended priority: medium — add gene-loss pathway and phosphorelay sub-pathway to achieve adequate mechanistic coverage."_

### morphology/ovoid_shaped  — *shallow* (5 edges)
- **Missing modules:** FtsZ treadmilling and septal PG synthesis coupling, RodA-PBP2b elongasome and peripheral PG synthesis module, FtsW-PBP2x septal synthase complex, Phosphorylation regulatory hub (GpsB) coordinating synthesis modes, Concentric ring spatial organization of division/elongation machinery
- `FtsZ treadmilling —drives→ septal peptidoglycan synthesis`  (10.1042/BSR20221664 (2023) - Direct mechanistic statement: F)
- `FtsW-PBP2x complex —synthesizes→ septal peptidoglycan`  (10.1042/BSR20221664 (2023) - Core pneumococcal mechanism for)
- `RodA-PBP2b pair —drives→ peripheral peptidoglycan synthesis`  (10.1042/BSR20221664 (2023) - Generic elongasome module for o)
- `septal peptidoglycan synthesis —occurs_at→ concentric midcell rings`  (10.1042/BSR20221664 (2023) - Spatial organization principle )
- `peripheral peptidoglycan synthesis —maintains→ ovoid aspect ratio`  (10.1128/SPECTRUM.04750-22 (2023) - Deletion/impairment of pe)
- `GpsB —regulates→ septal vs peripheral PG synthesis balance`  (10.1111/MMI.15122 (2023) - Pneumococcal phosphorylation hub )
- _Existing graph captures MapZ/DivIVA pathway but lacks peripheral PG synthesis machinery (RodA-PBP2b), FtsZ-septal coupling, and phosphorylation regulatory hub—all generic, well-supported modules."_

### morphology/pigmentation  — *shallow* (4 edges)
- **Missing modules:** carotenoid biosynthesis pathway, phenazine/pyocyanin biosynthesis, violacein biosynthesis (vio operon), prodigiosin biosynthesis (pig/red clusters), melanin/pyomelanin biosynthesis, intracellular vs extracellular pigment localization distinction
- `carotenoid biosynthesis —enabled_by→ MVA or MEP pathway`  (DOI:10.3390/microorganisms11122920 - provides C5 precursors )
- `crtE/crtB/crtI/crtY gene set —enables→ beta-carotene biosynthesis`  (DOI:10.3390/microorganisms11030614 - core carotenoid biosynt)
- `phzE/phzD/phzF/phzB/phzG gene set —enables→ phenazine biosynthesis`  (DOI:10.3390/microorganisms11030614 - core phenazine pathway )
- `shikimate pathway —provides_precursor_for→ phenazine biosynthesis`  (DOI:10.3390/microorganisms11122920 - phenazines (including p)
- `intracellular pigment accumulation —contributes_to→ pigmentation phenotype`  (DOI:10.3390/microorganisms11030614 - cell-confined insoluble)
- `extracellular pigment secretion —contributes_to→ pigmentation phenotype`  (DOI:10.3390/microorganisms11030614 - soluble pigments diffus)
- _Existing graph captures phenotype-level biosynthesis and visible color outcome but lacks major pigment-class pathways (carotenoids, phenazines, violacein, prodigiosin, melanin) and pigment localization distinctions—generic mechanistic modules reported as widespread across diverse taxa."_

### morphology/pink_pigmented  — *shallow* (5 edges)
- **Missing modules:** lycopene precursor branch-point, retinal biosynthetic competitor branch, growth-phase coupling of pigment synthesis, mevalonate pathway for isoprenoid supply, oxygen regulation of crt operons
- `lycopene —substrate_branch_point_for→ bacterioruberin_biosynthesis`  (DOI:10.1128/aem.00540-24 identifies lycopene as central prec)
- `retinal_biosynthetic_pathway —competes_with→ bacterioruberin_biosynthesis`  (DOI:10.1128/aem.00540-24 documents blh/crtY/brp genes as com)
- `logarithmic_growth_phase —enables→ bacterioruberin_synthesis`  (DOI:10.1128/aem.00540-24 shows BR synthesis is growth-couple)
- `mevalonate_pathway —supplies_substrate_for→ carotenoid_biosynthetic_process`  (DOI:10.1128/aem.00540-24 places haloarchaeal BR biosynthesis)
- `oxygen —upregulates→ crtI_crtB_operon`  (DOI:10.3390/biology12101346 (Sandmann 2023) documents oxygen)
- `lyeJ —catalyzes_key_step_in→ bacterioruberin_biosynthesis`  (DOI:10.1128/aem.00540-24 identifies lyeJ as key gene in de n)
- _The existing graph captures the basic isoprenoid-to-carotenoid-to-color pathway but misses at least 5 generic mechanistic modules (lycopene branching, retinal competition, growth-phase coupling, MVA supply, oxygen regulation) that are well-documented and non-taxon-specific in the literature."_

### morphology/ring_shaped  — *shallow* (3 edges)
- **Missing modules:** MreB-mediated wall synthesis control, bactofilin-LmdC localized remodeling module, elongasome circumferential processivity, osmotic/environmental stress sensing pathway
- `MreB filament —correlates with→ lateral cell wall growth rate`  (DOI:10.1038/s41467-024-49785-x (Middlemiss et al. 2024))
- `bactofilin polymers —spatially regulate→ peptidoglycan biosynthetic sites`  (DOI:10.7554/eLife.86577.2 (Pöhl et al. 2024))
- `bactofilin-LmdC module —promotes→ local cell wall remodeling`  (DOI:10.7554/eLife.86577.2 (Pöhl et al. 2024))
- `osmotic upshift —triggers→ MreB filament disassembly`  (DOI:10.3390/microorganisms12071309 (Dersch & Graumann 2024))
- `MreB disassembly —leads to→ disorganized peptidoglycan synthesis pattern`  (DOI:10.3390/microorganisms12071309 (Dersch & Graumann 2024))
- `RodA elongasome complex —inserts→ circumferential glycan strands`  (DOI:10.1038/s41467-024-49785-x (Middlemiss et al. 2024))
- _Existing graph captures backbone (curvature→closure→trait) but misses generic molecular machinery: MreB dynamics, bactofilin-LmdC remodeling, and environmental sensors—all 2024 peer-reviewed, non-assay-specific. Report cautions against in vitro/preprint edges (ZapD–FtsZ), recommending 'core mechanistic subgraph' approach instead of full whole-cell toroid mechanisms._

### morphology/rod_shaped  — *shallow* (5 edges)
- **Missing modules:** RodA–PBP2 allosteric activation, MreC upstream regulation of elongasome, MreD regulatory module, RodZ complex integrity, Elongasome processivity reinforcement
- `mreC —activates→ rod_complex`  (DOI:10.1038/s41467-023-39037-9 (2023))
- `rod_complex —enables→ peptidoglycan_synthesis`  (DOI:10.1038/s41467-023-39037-9 (2023))
- `mreD —modulates→ rod_complex`  (DOI:10.1002/mbo3.1385 (2023))
- `rodZ —maintains→ rod_complex`  (DOI:10.1002/mbo3.1385 (2023))
- `peptidoglycan_synthesis —contributes to→ lateral_cell_wall_elongation`  (DOI:10.1038/s41467-024-49785-x (2024))
- `mreB —directs→ lateral_cell_wall_elongation`  (DOI:10.1038/s41467-024-49785-x (2024))
- _Existing graph captures rod-shape backbone but abstracts away RodA–PBP2 allosteric activation and upstream MreC/MreD regulation; adding explicit mechanistic nodes and edges would lift coverage from backbone to nearly-complete generic mechanism._

### morphology/sphere_shaped  — *shallow* (4 edges)
- **Missing modules:** MreB-mediated elongation suppression, FtsZ treadmilling distributive mechanism, lipid II precursor translocation pool, divisome/PBP recruitment coordination
- `loss_of_MreB_activity —causes→ loss_of_elongation_capacity`  (DOI:10.1038/nrmicro3088 (pinho2013howtoget pages 11-11): los)
- `loss_of_elongation_capacity —contributes_to→ sphere_shaped_trait`  (DOI:10.1038/nrmicro3088 (pinho2013howtoget pages 11-11): pre)
- `ftsZ_treadmilling —organizes→ septal_peptidoglycan_synthesis`  (DOI:10.1042/bsr20221664 (battaje2023modelsversuspathogens pa)
- `ftsW_translocation —enables→ lipid_II_availability_at_septum`  (DOI:10.1038/nrmicro3088 (pinho2013howtoget pages 2-3): lipid)
- `lipid_II_availability_at_septum —substrate_for→ septal_peptidoglycan_synthesis`  (DOI:10.1038/nrmicro3088 (pinho2013howtoget pages 2-3): PG sy)
- `ftsZ_division_ring —recruits→ divisome_PBP_complex`  (DOI:10.1038/nrmicro3088 (pinho2013howtoget pages 5-6): FtsZ )
- _Existing graph captures FtsZ-septal PG-wall geometry backbone but omits generic cocci mechanisms for MreB loss, FtsZ treadmilling, lipid II transport, and divisome recruitment; filtering excluded S. aureus-specific edges (PBP2/4/GpsB, Atl) and ovococci boundary cases per curation rules._

### morphology/spindle_shaped  — *shallow* (3 edges)
- **Missing modules:** bactofilin cytoskeleton (BacA) localized growth control, M23 endopeptidase (LmdC) PG-remodeling module, spatial growth-zone confinement logic, localized vs. dispersed PG insertion contrast
- `bactofilin —required_for→ spatial confinement of peptidoglycan biosynthesis`  (DOI:10.7554/eLife.86577 (Pöhl 2024) — broad mechanistic prin)
- `BacA —interacts_with→ LmdC`  (DOI:10.7554/eLife.86577 (Pöhl 2024) — direct biochemical int)
- `LmdC —decreases→ peptidoglycan cross-linkage`  (DOI:10.7554/eLife.86577 (Pöhl 2024) — enzymatic mechanism li)
- `spatial confinement of peptidoglycan biosynthesis —enables→ localized peptidoglycan insertion`  (DOI:10.7554/eLife.86577 (Pöhl 2024) + DOI:10.3389/fmicb.2017)
- `localized peptidoglycan insertion —enables→ reduced end-cap radius`  (DOI:10.3389/fmicb.2017.01264 (van Teeseling 2017) — localize)
- `LmdC —required_for→ proper cell shape`  (DOI:10.7554/eLife.86577 (Pöhl 2024) — knockout/knockdown lea)
- _Existing graph captures phenotypic flow (polar growth → taper → trait) but omits the generic bactofilin-LmdC-PG remodeling backbone documented in 2023-2024 mechanistic studies; two or more core modules (cytoskeleton control, enzymatic remodeling, spatial confinement logic) are absent._

### morphology/square_shaped  — *shallow* (3 edges)
- **Missing modules:** cytoskeletal guidance of division axis, local growth coordination, envelope-environment water-activity feedback, S-layer integrity as dynamic property
- `cytoskeletal filaments —guides→ right_angle_growth`  (10.1038/s41564-022-01215-8)
- `local growth —enables→ right_angle_growth`  (10.1038/s41564-022-01215-8)
- `S-layer integrity —enables→ cell_shape_maintenance`  (10.1038/s41586-024-07462-5 (2024 Nature))
- `division axis control —determines→ right_angle_growth`  (10.1038/s41564-022-01215-8)
- `water activity limitation —selects for→ envelope architecture`  (10.1371/journal.pone.0018653)
- `S-layer lattice periodicity —constrains→ cell geometry`  (10.1371/journal.pone.0018653)
- _Existing graph captures S-layer → shape backbone but omits cytoskeletal coordination, local-growth dynamics, and envelope-stress coupling that the report explicitly identifies as the generic archaeal mechanism for geometric morphologies."_

### morphology/sulfur_globule  — *shallow* (2 edges)
- **Missing modules:** sulfur globule envelope proteins (SgpA/B/C/D), intracellular sulfur oxidation pathway (SQR→persulfides→rDsrAB), periplasmic/extracytoplasmic localization constraint
- `SgpA/B/C/D sulfur globule proteins —surrounds→ elemental_sulfur`  (10.3390/microorganisms12020391)
- `SQR (sulfide:quinone oxidoreductase) —produces→ persulfide sulfur / sulfane sulfur`  (10.3390/ijms252010962)
- `persulfide_sulfur / sulfane_sulfur —precursor_of→ elemental_sulfur_globule`  (10.1128/aem.01941-21)
- `rDsrAB (reverse dissimilatory sulfite reductase) —oxidizes→ elemental_sulfur_globule`  (10.20944/preprints202306.1429.v1)
- `elemental_sulfur_globule —located_in→ periplasmic_space`  (10.3390/microorganisms12020391)
- `sulfide_or_thiosulfate_availability —positively_regulates→ sulfur_globule_formation`  (10.1007/978-3-319-51365-2_2)
- _Existing graph captures only substrate → elemental sulfur → storage localization; missing envelope proteins, sulfur consumption pathway, and periplasmic specificity—all well-supported by generic mechanisms across Chromatiaceae, Allochromatium, and Beggiatoa."_

### morphology/triangular_shaped  — *shallow* (3 edges)
- **Missing modules:** rod-determining protein complex (RdfA/Sph3), disk-determining factors (DdfA/Volactin), growth-phase transition trigger, ParA/MinD spatial organization system, cytoskeletal scaffolding proteins (CetZ1), envelope glycosylation pathway
- `disk-determining factors (DdfA, Volactin) —promote→ flat polygonal disk-state morphogenesis`  (DOI:10.1038/s41467-024-45196-0 (Schiller 2024): reverse gene)
- `rod-determining factor complex (RdfA, Sph3, CetZ1) —suppresses→ polygonal disk morphology`  (DOI:10.1038/s41467-024-45196-0: deletion of rdfA/sph3/cetZ1 )
- `growth phase progression (increasing OD600) —triggers→ rod-to-disk morphological transition`  (DOI:10.3389/fmicb.2023.1270665 (Patro 2023): quantitative tr)
- `MinD2 (ParA/MinD-family ATPase) —maintains→ rod morphology through spatial localization`  (DOI:10.3389/fmicb.2024.1474570 (Patro 2024): MinD2 loss caus)
- `cytoskeletal actin-homolog (Volactin) —assembles into→ dynamic filaments constraining cell shape`  (DOI:10.1038/s41467-024-45196-0: Volactin forms dynamic filam)
- `Agl15-dependent N-glycosylation pathway —enriched in→ disk-forming envelope conditions`  (DOI:10.1038/s41467-024-45196-0: proteomics shows Agl11/Agl12)
- _Existing graph captures S-layer structural determinism but omits the genetic/regulatory rod-vs-disk switch (RdfA/DdfA/MinD2) and growth-phase triggers that drive pleomorphic triangular phenotype emergence in haloarchaea; these are well-supported generic mechanisms in recent high-impact literature (Nature Communications, Frontiers 2023-2024) and suitable for curation once confirmed to apply across multiple triangular-forming taxa._

### morphology/white_pigmented  — *shallow* (5 edges)
- **Missing modules:** SigB-mediated transcriptional regulation of staphyloxanthin biosynthesis, Fungal melanin biosynthesis pathway (pks-dependent), Alternative pigment systems (prodigiosin)
- `sigB —positively_regulates→ staphyloxanthin_biosynthesis`  (DOI:10.1128/mbio.00346-24)
- `glmS —positively_regulates→ sigB`  (DOI:10.1080/21505594.2024.2352476)
- `pksA —encodes→ melanin_biosynthesis`  (DOI:10.1080/21501203.2023.2249010)
- `reduced_melanin_accumulation —causes→ white_pigmented_trait`  (DOI:10.1080/21501203.2023.2249010)
- `pig_operon —positively_regulates→ prodigiosin_biosynthesis`  (DOI:10.1038/s41598-024-68747-3)
- `reduced_prodigiosin_accumulation —causes→ white_pigmented_trait`  (DOI:10.1038/s41598-024-68747-3)
- _Existing S. aureus staphyloxanthin backbone is adequate, but graph lacks generic regulatory layer (SigB/GlmS) and omits entire fungal melanin and bacterial prodigiosin mechanisms documented in 2023-2024 literature; SigB regulatory edges are well-supported and broadly applicable to staphylococci."_

### physiology/chemoheterotrophic  — *shallow* (9 edges)
- **Missing modules:** glycolysis (EMP) as explicit pathway node, TCA cycle as explicit pathway node, fermentation overflow products (acetate, lactate, formate), extracellular electron transfer (EET) and metal-based terminal electron acceptors, non-oxidative pentose phosphate pathway
- `organic_molecule —catabolized via→ glycolysis`  (DOI:10.3390/microorganisms12112271 - Rakitin et al. (2024) e)
- `glycolysis —produces→ pyruvate`  (DOI:10.1021/acsomega.3c02205 - Stebegg et al. (2023) note py)
- `pyruvate —can be converted to→ acetate`  (DOI:10.3390/microorganisms12112271 - Rakitin et al. (2024) d)
- `fermentation —produces→ short_chain_fatty_acids`  (DOI:10.1016/j.chom.2024.05.011 - Muramatsu & Winter (2024) d)
- `catabolism —can proceed through→ extracellular_electron_transfer`  (DOI:10.1128/mbio.00992-24 - Su et al. (2024) identify EET-en)
- `extracellular_electron_transfer —transfers electrons to→ metal_acceptors`  (DOI:10.1128/mbio.00992-24 - Su et al. (2024) describe multih)
- _Existing graph captures trait-to-substrate and core energy/biomass synthesis, but lacks explicit glycolytic and TCA nodes, fermentation product diversity beyond ATP, and anaerobic/EET respiration mechanisms now recognized as generic in modern genome-centric definitions._

### physiology/chemolithoautotrophic  — *shallow* (9 edges)
- **Missing modules:** specific CO2 fixation pathways (CBB, rTCA, WL), DIC acquisition toolkit (carbonic anhydrase, transporters, bicarbonate), specific inorganic donors (H2, thiosulfate, sulfide, Fe(II), ammonia), key enzymatic steps (RuBisCO, aclAB/oorABCD, PFOR/OGOR, ferredoxins), electron acceptors/terminal processes (oxygen, nitrate, DNRA)
- `inorganic_electron_donor —includes→ molecular hydrogen`  (DOI:10.1093/ismejo/wrae173)
- `inorganic_electron_donor —includes→ thiosulfate`  (DOI:10.1093/ismejo/wrae173)
- `co2_fixation_pathway —includes module→ Calvin-Benson-Bassham cycle`  (DOI:10.1128/aem.01557-23)
- `co2_fixation_pathway —includes module→ reverse tricarboxylic acid cycle`  (DOI:10.1128/msystems.00148-24)
- `carbon_dioxide —converted by→ carbonic anhydrase`  (DOI:10.1128/aem.01557-23)
- `reducing_power —can be supplied by→ reduced ferredoxin`  (DOI:10.3390/life13030627)
- _Existing graph captures core energy-coupling backbone (donor→ETC→PMF→ATP→fixation) but lacks generic mechanistic depth in specific fixation pathways, DIC handling, enzymatic detail, and electron acceptor diversity; report emphasizes these modules as universal across chemolithoautotrophs._

### physiology/chemotrophic  — *shallow* (8 edges)
- **Missing modules:** NADH/NADPH electron carrier intermediate, Alternative PMF generation mechanisms (quinone/quinol cycling and redox loops), Fermentation pathway (chemotrophic variant bypassing ETC)
- `reduced_chemical_substrate —electrons captured in→ NADH/NADPH`  (DOI:10.1016/j.bbabio.2008.09.008 / Yousavich 2024: electrons)
- `NADH/NADPH —transfers electrons to→ respiratory_chain`  (Yousavich 2024 pages 21-25: NADPH transfers electrons to fir)
- `respiratory_chain —can generate proton_motive_force via→ quinone/quinol cycling`  (DOI:10.1016/j.bbabio.2008.09.008: pmf built by quinone/quino)
- `respiratory_chain —can generate proton_motive_force via→ redox loop`  (DOI:10.1016/j.bbabio.2008.09.008: pmf built by redox loop me)
- `fermentation —provides alternative ATP in→ chemotrophic_trait`  (Yousavich 2024 pages 21-25: fermentation does not involve ET)
- `redox_reaction —is transduced via→ proton_motive_force`  (DOI:10.1016/j.bbabio.2008.09.008: free energy of membrane re)
- _Existing graph captures substrate-to-ATP backbone but omits NADH/NADPH carrier intermediate, alternative PMF mechanisms (quinone/redox loops), and fermentation as universal chemotrophic variant; these are generic mechanisms attested in Simon 2008 and Yousavich 2024._

### physiology/copiotrophic  — *shallow* (6 edges)
- **Missing modules:** chemotaxis and motility genes, two-component regulatory systems, outer-membrane and secreted proteins, carbohydrate-active enzyme enrichment, ribosome biogenesis regulatory mechanism
- `copiotrophic genomes —enriched in→ motility functions`  (DOI:10.1073/pnas.0903507106)
- `copiotrophic genomes —enriched in→ chemotaxis genes`  (DOI:10.1093/ismeco/ycae081)
- `copiotrophic genomes —enriched in→ two-component signal transduction systems`  (DOI:10.1186/s40168-025-02182-y)
- `copiotrophic genomes —enriched in→ membrane transport functions`  (DOI:10.1038/s41467-023-43297-w)
- `copiotrophic genomes —enriched in→ outer membrane and secreted proteins`  (DOI:10.1073/pnas.0903507106)
- `ribosome biogenesis —enables→ rapid growth under nutrient-rich conditions`  (DOI:10.1038/s41467-024-48591-9)
- _Existing graph captures nutrient environment and growth phenotype skeleton but misses 5+ generic genomic-enrichment modules that literature identifies as core copiotrophic adaptations; recommend adding chemotaxis, motility, two-component systems, and membrane-protein edges from marine-genomics and recent soil studies._

### physiology/lithoheterotrophic  — *shallow* (9 edges)
- **Missing modules:** sulfur compound oxidation pathways (Sox, Dsr, sulfide/thiosulfate/S0), denitrification module (nitrate/nitrite reduction), nitrate/nitrite as alternative electron acceptors, microaerobic oxygen conditions as environmental requirement
- `sulfide —can serve as electron donor for→ chemolithoheterotrophic growth`  (DOI:10.1038/s41467-025-56588-1 — sulfide oxidation coupled t)
- `thiosulfate —can serve as electron donor for→ chemolithoheterotrophic growth`  (DOI:10.3390/life14050591 — sulfur-cycle review treats thiosu)
- `inorganic_electron_donor —feeds electrons into→ denitrification pathway`  (DOI:10.1038/s41467-025-56588-1 — sulfide oxidation coupled t)
- `denitrification pathway —reduces→ nitrate`  (DOI:10.1038/s41467-025-56588-1 & thesis context — generic de)
- `microaerobic conditions —enable→ Fe(II) oxidation by preventing abiotic oxidation`  (DOI:10.1038/s41598-021-81412-3 — low O2 required because hig)
- `sulfide —inhibits→ copper-dependent denitrification enzymes (NirK, NosZ)`  (DOI:10.1038/s41467-025-56588-1 — sulfide inhibits NirK and N)
- _Existing graph covers Fe(II)-O2 lithoheterotrophy backbone but omits generic sulfur pathways and denitrification alternatives that the report documents across multiple taxa; sulfur-based mechanisms are curable and broadly applicable."_

### physiology/lithotrophic  — *shallow* (6 edges)
- **Missing modules:** terminal oxidase catalytic step, explicit F-type ATP synthase node, sulfur oxidation pathways (Sox/SQR/SoeABC), ammonia oxidation pathway, quinone redox intermediates, alternative electron acceptor coupling (O2, nitrate)
- `menaquinol —oxidized_by→ terminal_oxidase`  (Soom et al., 2025, https://doi.org/10.1101/2025.03.14.643271)
- `terminal_oxidase —generates→ proton_motive_force`  (Soom et al., 2025, https://doi.org/10.1101/2025.03.14.643271)
- `thiosulfate —oxidized_by→ sox_multienzyme_system`  (Nosalova et al., 2023, https://doi.org/10.3390/microorganism)
- `sulfide —oxidized_by→ sulfide_quinone_oxidoreductase`  (Nosalova et al., 2023, https://doi.org/10.3390/microorganism)
- `ammonia —oxidized_by→ ammonia_monooxygenase`  (Kong et al., 2026, https://doi.org/10.1186/s40168-025-02290-)
- `nitrite —oxidized_by→ nitrite_oxidoreductase`  (Laso-Pérez et al., 2025, https://doi.org/10.1128/mbio.00749-)
- _Existing graph captures respiratory backbone (donor–ETC–PMF–ATP) but omits 4+ generic mechanistic modules: terminal oxidase catalysis, sulfur/ammonia oxidation pathways, and quinone redox intermediates; recent literature (Soom 2025, Nosalova 2023, Laso-Pérez 2025) provides strong peer-reviewed support for enrichment._

### physiology/methylotrophic  — *shallow* (8 edges)
- **Missing modules:** RuMP pathway enzymes (Hps, Phi), serine cycle enzymes (GlyA/SHMT, SgaA/SGT, HprA/HPR), MDH isoforms with cofactor logic (MxaFI vs XoxF; PQQ, lanthanides, Ca2+), formaldehyde oxidation pathways (H4MPT, H4F/THF)
- `methanol_dehydrogenase —has_two_isoforms→ MxaFI methanol dehydrogenase`  (DOI:10.1128/msphere.00685-24)
- `methanol_dehydrogenase —has_two_isoforms→ XoxF methanol dehydrogenase`  (DOI:10.1128/msystems.00248-24)
- `XoxF methanol dehydrogenase —requires_cofactor→ lanthanides`  (DOI:10.1128/msphere.00685-24)
- `GlyA serine hydroxymethyltransferase —catalyzes→ serine_pathway`  (DOI:10.1128/msystems.00248-24)
- `Hps 3-hexulose-6-phosphate synthase —catalyzes→ rump_cycle`  (DOI:10.1038/s41467-023-43610-7)
- `formaldehyde —oxidized_by→ H4MPT pathway`  (DOI:10.1038/s41467-024-48197-1)
- _Existing graph captures basic methanol-formaldehyde-assimilation backbone but misses generic pathway enzyme specificity, cofactor requirements, MDH isoform diversity (MxaFI vs XoxF), and formaldehyde oxidation routes reported in 2023–2024 literature._

### physiology/organoheterotrophic  — *shallow* (7 edges)
- **Missing modules:** tricarboxylic acid cycle (TCA) pathway node, anaerobic respiration / nitrate reduction branch, electron acceptor alternatives (O2, NO3-, fumarate)
- `central_carbon_metabolism —includes pathway→ tricarboxylic acid cycle`  (Liu et al. 2023 (10.1128/spectrum.04110-22) documents comple)
- `central_carbon_metabolism —includes pathway→ glycolytic process`  (Liu et al. 2023 (10.1128/spectrum.04110-22) documents comple)
- `central_carbon_metabolism —includes pathway→ pentose phosphate pathway`  (Liu et al. 2023 (10.1128/spectrum.04110-22) documents pentos)
- `respiratory_chain —can use electron acceptor→ nitrate`  (Liu et al. 2023 (10.1128/spectrum.04110-22) documents narGHI)
- `anaerobic_respiration —enabled by→ nitrate reductase complex`  (Liu et al. 2023 (10.1128/spectrum.04110-22) demonstrates nar)
- `catabolic_redox_reaction —coupled to→ anabolic biosynthesis`  (Slowinski 2019 establishes that organoheterotrophs 'couple a)
- _Existing graph captures trait-defining core (organic donor/carbon sources, central metabolism, respiratory ATP, biomass) but lacks explicit central-metabolism pathway differentiation (TCA, glycolysis, PPP) and anaerobic respiration branch—both well-documented in 2023–2024 literature and mechanistically generic rather than taxon-specific._

### physiology/photoautotrophic  — *shallow* (8 edges)
- **Missing modules:** photosystem I and ferredoxin-NADPH pathway, carbon-concentrating mechanism (CCM) with transporters and carboxysomes, inorganic carbon chemistry (CO2/HCO3- interconversion), CCM regulatory feedback (CmpR/CcmR metabolite signaling)
- `photosystem I —transfers electrons to→ ferredoxin-dependent NADPH formation`  (Grettenberger et al. 2024 (10.1111/1751-7915.14519): electro)
- `carbon-concentrating mechanism —reduces→ RuBisCO oxygenase activity`  (Lucius & Hagemann 2024 (10.3389/fpls.2024.1417680): CCM supp)
- `BCT1 bicarbonate transporter —imports→ bicarbonate`  (Kurkela & Tyystjärvi 2024 (10.1111/ppl.14140): BCT1 is ATP-d)
- `carboxysome —compartmentalizes and elevates→ CO2 concentration near RuBisCO`  (Kurkela & Tyystjärvi 2024 (10.1111/ppl.14140): carboxysomes )
- `2-phosphoglycolate —activates→ CmpR transcription factor`  (Kurkela & Tyystjärvi 2024 (10.1111/ppl.14140): 2-PG and RuBP)
- `CmpR transcription factor —activates expression of→ BCT1 and cmp operon`  (Kurkela & Tyystjärvi 2024 (10.1111/ppl.14140): CmpR activate)
- _Existing graph captures core light→ATP/NADPH→fixation backbone but omits the carbon-concentrating mechanism (transporters, carboxysomes, regulatory feedback) documented as essential in 2024 cyanobacteria reviews; addition of CCM module would elevate verdict to adequate._

### physiology/photolithotrophic  — *shallow* (8 edges)
- **Missing modules:** photosynthetic reaction centers (Type I/II), light-harvesting antenna structures (chlorosomes), reverse tricarboxylic acid cycle (rTCA) pathway, sulfur oxidation intermediate module with Dsr system
- `light —excites→ photosynthetic reaction center`  (DOI:10.3389/fmicb.2024.1417714 - 'capture of a light quantum)
- `photosynthetic reaction center —initiates→ photosynthetic electron transport chain`  (DOI:10.3389/fmicb.2024.1417714 - core mechanism for anoxygen)
- `chlorosome —enables→ efficient light harvesting`  (DOI:10.3389/fmicb.2024.1417714 - 'most efficient light-harve)
- `hydrogen_sulfide —oxidized_to→ elemental_sulfur`  (DOI:10.3389/fmicb.2024.1417714 - 'GSB oxidize H2S to element)
- `dissimilatory_sulfite_reductase_system —required_for→ sulfur oxidation`  (DOI:10.3390/life14050591 - 'Sulfur globule oxidation depende)
- `reverse_tricarboxylic_acid_cycle —pathway_for→ CO2_fixation`  (DOI:10.3389/fmicb.2024.1417714 - 'carbon dioxide assimilated)
- _Existing graph captures light and inorganic donors as energy/electron sources and anoxygenic photosynthesis as pathway, but lacks mechanistic depth on reaction centers, antenna structures, sulfur-oxidation intermediates, and specific carbon-fixation pathways (rTCA vs Calvin) that distinguish anoxygenic from oxygenic phototrophy."_

### physiology/photoorganoheterotrophic  — *shallow* (8 edges)
- **Missing modules:** detailed reaction-center electron transfer chain, rhodopsin vs reaction-center photoheterotrophy distinction, photosynthesis gene cluster (PGC) genetic basis, cytochrome-mediated electron donation for RC re-reduction
- `photosynthetic_reaction_center —transfers electrons to→ iron-sulfur_cluster_FX`  (DOI:10.3390/biom14030311 describes Type I RC structure where)
- `iron-sulfur_cluster_FX —transfers electrons to→ iron-sulfur_clusters_FA_FB`  (DOI:10.3390/biom14030311 reports terminal FA/FB [4Fe-4S] clu)
- `cytochrome_bc1_complex —supplies electrons to→ cytochrome_cZ_donors`  (DOI:10.3390/biom14030311 describes how cytochrome bc1 comple)
- `photosynthesis_gene_cluster —encodes_genes_for→ bacteriochlorophyll_synthesis`  (DOI:10.1128/spectrum.01112-23 documents that PGCs containing)
- `reaction_center_photoheterotrophy —generates→ reducing_power_NADPH`  (DOI:10.4014/jmb.2410.10034 establishes that reaction-center-)
- `diurnal_light_dark_cycle —drives→ rhythmic_transcription`  (DOI:10.1038/s43705-023-00334-5 demonstrates that light-dark )
- _Existing graph captures broad light-PMF-ATP pathway and organic substrate roles, but omits electron transfer chain details, mechanistic pathway distinction (reaction-center vs rhodopsin), genetic basis (PGC operons), and regulatory environmental response—all generic modules in the literature._

### physiology/quorum_sensing  — *shallow* (2 edges)
- **Missing modules:** autoinducer synthesis by synthase (LuxI/AgrB/AgrD proteolytic maturation), positive feedback loop (activated receptor promotes synthase transcription), two-component signaling pathway (sensor kinase / response regulator cascade, Gram-positive), signal degradation / quorum quenching (enzymatic inactivation of autoinducers), threshold-dependent receptor activation mechanism
- `autoinducer synthase (e.g., LuxI) —synthesizes→ autoinducer (e.g., OHHL)`  (DOI:10.3390/synbio1020010 — Li et al. 2024 describe LuxI syn)
- `autoinducer —binds→ cognate receptor/sensor protein (e.g., LuxR, AgrC, LuxQ)`  (DOI:10.3390/ijms25052655 — Juszczuk-Kubiak 2024 review defin)
- `activated receptor-autoinducer complex (e.g., LuxR-OHHL) —promotes transcription of→ autoinducer synthase gene(s) (e.g., luxI)`  (DOI:10.3390/ijms25052655 — Juszczuk-Kubiak 2024 explicitly f)
- `activated sensor kinase (e.g., AgrC phosphorylated by AIP) —phosphorylates→ response regulator (e.g., AgrA)`  (DOI:10.1128/jb.00195-24 — Fang et al. 2024 describe AgrC aut)
- `quorum-quenching enzyme (e.g., AiiA lactonase) —degrades / inactivates→ autoinducer`  (DOI:10.3390/ijms25052655 — Juszczuk-Kubiak 2024 review ident)
- `high cell density / accumulation of autoinducer to threshold —enables detection by→ quorum sensing process`  (DOI:10.3390/ijms25052655 — Juszczuk-Kubiak 2024 emphasizes t)
- _Existing graph captures autoinducer-as-central-node but omits mechanistic branches (synthesis, positive feedback, two-component signaling, signal degradation) that distinguish QS from generic chemical communication; report identifies 5+ generic modules across 2023–2024 primary and review literature warranting enrichment._

### upper/observation  — *shallow* (3 edges)
- **Missing modules:** metadata modeling, environmental conditions context, measurement process distinction, FAIR identifier infrastructure, sample entity, data provenance/recording standard
- `assay_measurement —has_output→ measurement_datum`  (DOI:10.3233/sw-223096 (Dooley et al. 2024, pages 16-19) maps)
- `observation_trait —has_context→ metadata`  (DOI:10.3233/sw-223096 (Dooley et al. 2024, pages 11-14) stat)
- `metadata —includes→ environmental_conditions`  (DOI:10.1007/978-1-0716-3838-5_20 (Eloe-Fadrosh et al. 2024) )
- `metadata —recorded_in→ MIxS_standard`  (DOI:10.1007/978-1-0716-3838-5_20 (Eloe-Fadrosh et al. 2024) )
- `sample —requires_metadata→ environmental_conditions`  (DOI:10.1007/978-1-0716-3838-5_20 (Eloe-Fadrosh et al. 2024) )
- `metadata —enables→ data_reuse`  (DOI:10.1007/978-1-0716-3838-5_20 (Eloe-Fadrosh et al. 2024) )
- _The existing graph captures only the assay→data→quality spine; the report describes a richer metadata-and-context substrate (environmental conditions, FAIR identifiers, provenance standards) that is generic and broadly applicable across microbiome observations but entirely absent from the current graph._

### upper/quality  — *shallow* (3 edges)
- **Missing modules:** EQ entity-quality binding (characteristic_of/inheres_in), process quality class and bearer relations, relational quality patterns (toward sensitivity/tolerance), temporal/context qualifiers (during), comparative phenotype reference (altered_relative_to)
- `quality_trait —inheres_in→ material_entity`  (DOI:10.1186/2041-1480-3-s2-s6 (Gkoutos 2012): canonical EQ r)
- `process_quality —is_a→ quality_trait`  (DOI:10.1186/s12866-014-0294-3 (Chibucos 2014): PATO:0001236 )
- `relational_quality —is_a→ quality_trait`  (DOI:10.1093/bib/bbx035 (Gkoutos 2018): unary vs relational q)
- `quality_trait —toward→ environmental_entity`  (DOI:10.1093/bib/bbx035 (Gkoutos 2018): relational quality te)
- `phenotype_trait —during→ biological_process`  (DOI:10.1093/genetics/iyaf027 (Matentzoglu 2025): temporal co)
- `dependent_phenotype —altered_relative_to→ reference_genotype_or_condition`  (DOI:10.1186/s12866-014-0294-3 (Chibucos 2014): OMP dependent)
- _Existing graph captures trait taxonomy but misses 5+ generic mechanistic modules (EQ binding, process quality, relational/directional qualities, temporal context, comparative reference patterns) that the report emphasizes as foundational to upper-level phenotype modeling._

### morphology/coccus_shaped  — *shallow* (4 edges)
- **Missing modules:** divisome complex assembly and organization, spatial regulation of PBP activity (septal vs peripheral localization), primacy of active peptidoglycan synthesis in driving constriction mechanics
- `FtsZ division ring —organizes→ divisome complex`  (DOI:10.1038/nrmicro3088 and DOI:10.1042/BSR20221664 — FtsZ i)
- `divisome complex —recruits→ FtsW/PBP1 septal synthase module`  (DOI:10.1038/s41564-024-01629-6 (Schäper 2024) — FtsW/PBP1 an)
- `active peptidoglycan synthesis —drives→ septum constriction`  (DOI:10.1038/s41564-024-01629-6 (Schäper 2024) — septal synth)
- `GpsB regulator —spatially_restricts→ penicillin-binding proteins`  (DOI:10.1128/mbio.03235-23 (Costa 2024) — GpsB maintains PBP2)
- `peripheral peptidoglycan synthesis —negatively_associated_with→ coccus shaped`  (DOI:10.1038/nrmicro3088 (Pinho 2013) — peripheral synthesis )
- _Existing graph captures septal-synthesis backbone but lacks divisome organization layer and spatial PBP-regulation mechanisms that the report identifies as generic refinements to coccal morphogenesis; adding divisome node and spatial-regulation edges would strengthen mechanistic depth to adequate._

### morphology/cream_pigmented  — *shallow* (3 edges)
- **Missing modules:** transcriptional repression of carotenoid operons (CrtR/MarR regulatory layer), isoprenoid precursor supply (MEP pathway and GGPP synthesis), carotenoid biosynthesis gene nodes (crtE, crtB, crtI)
- `crtR —represses→ carotenoid_biosynthesis`  (CrtR overexpression reduced crtE expression by ≥500-fold, yi)
- `MEP_pathway —produces→ isopentenyl_diphosphate`  (MEP pathway supplies IPP precursor for carotenoid synthesis )
- `crtE_disruption —decreases→ carotenoid_production`  (Insertions in crtE associated with off-white WW phenotype)
- `isoprenoid_biosynthesis —produces→ geranylgeranyl_diphosphate`  (GGPP is direct precursor for phytoene synthesis)
- `crtB_crtI_disruption —decreases→ carotenoid_production`  (crtB (phytoene synthase) and crtI (phytoene desaturase) knoc)
- _Existing graph captures phenotypic causality but omits regulatory layer (CrtR) and precursor-supply pathway (MEP/GGPP) that are generic, well-documented mechanisms across Mycobacterium and Corynebacterium; light-driven photochromogenicity and S. aureus STX regulation were correctly excluded as taxon-specific._

### morphology/flask_shaped  — *shallow* (3 edges)
- **Missing modules:** bactofilin cytoskeletal scaffolding, PG hydrolase remodeling (M23 endopeptidase module), bactofilin-LmdC interaction coupling, growth zone repositioning mechanism, zonal PG synthesis localization
- `bactofilin cytoskeleton —constrains→ polar growth compartment`  (DOI:10.7554/elife.86577.2 — loss of bactofilins causes 'unco)
- `M23 endopeptidase (LmdC-type) —interacts_with→ bactofilin`  (DOI:10.7554/elife.86577.2 — direct in vitro interaction betw)
- `bactofilin-LmdC module —promotes_local_changes_in→ cell wall biosynthesis`  (DOI:10.7554/elife.86577.2 — conserved module drives local PG)
- `zonal peptidoglycan synthesis —produces→ polar neck-like extension`  (DOI:10.1371/journal.pbio.1002565 — spatially restricted PG i)
- `polar growth zone localization —determines→ neck position and morphology`  (DOI:10.1371/journal.pbio.1002565 — repositioning of polar PG)
- _The existing graph captures unipolar PG growth as a backbone but omits the conserved scaffold-hydrolase (bactofilin-LmdC) regulatory module and growth-zone-positioning logic that the report identifies as generic mechanisms for walled bacteria producing flask-like polar morphology; Mycoplasma attachment-organelle pathway is taxon-specific and correctly not included."_

### physiology/urease_activity  — *shallow* (4 edges)
- **Missing modules:** hydroxide production, carbon dioxide production, pH alkalinization, carbonic anhydrase coupling, bicarbonate chemistry
- `urease_function —produces→ hydroxide (CHEBI:16234)`  (DOI:10.24263/2304-974x-2024-13-2-10 — Core ureolysis reactio)
- `urease_function —produces→ carbon dioxide (CHEBI:16526)`  (DOI:10.24263/2304-974x-2024-13-2-10 — Core ureolysis reactio)
- `urease_function —increases→ pH (PATO:0000196)`  (DOI:10.1021/acs.est.3c06617 — Generic consequence of urea hy)
- `carbon dioxide (CHEBI:16526) —is hydrated by→ carbonic anhydrase (EC:4.2.1.1)`  (DOI:10.1021/acs.est.3c06617 — Widespread coupling: 'CA hydra)
- `carbonic anhydrase (EC:4.2.1.1) —produces→ bicarbonate (CHEBI:17544)`  (DOI:10.1021/acs.est.3c06617 — Direct product of CA activity)
- _Existing graph captures urea hydrolysis core but omits generic products (hydroxide, CO2) and pH mechanism; carbonic anhydrase coupling and Ni-maturation are mechanistically important but marked taxon-specific or application-specific in literature and should remain pending further generic evidence._

### environment/anaerobic  — *shallow* (4 edges)
- **Missing modules:** ROS detoxification enzymes module, alternative electron acceptor respiration pathway
- `reactive oxygen species —detoxified by→ superoxide dismutase, catalase, and peroxidases`  (Okabe et al. 2023)
- `respiratory reductases —enables utilization of→ alternative anaerobic terminal electron acceptors`  (Little et al. 2024)
- `alternative anaerobic terminal electron acceptors —enables→ anaerobic growth`  (Little et al. 2024)
- _Existing graph captures oxygen exclusion and ROS stress but omits two generic mechanistic modules reported as universal: active ROS detoxification (Sod/Cat/peroxidases) and alternative anaerobic respiration via terminal electron acceptors."_

### environment/halophilic  — *adequate* (5 edges)
- **Missing modules:** oxidative stress response, ectoine biosynthesis pathway (ectABC), salt-in proteome adaptation, ion transporter mechanisms (Na+/H+ antiport, K+ uptake)
- `sodium_chloride —induces→ oxidative_stress`  (https://doi.org/10.1186/s12934-024-02358-5 (Yu et al. 2024: )
- `compatible_solutes —includes→ ectoine`  (https://doi.org/10.1128/aem.00479-23 (Lichty et al. 2023: ec)
- `ectoine_biosynthesis —is_catalyzed_by→ ectABC_operon`  (https://doi.org/10.1128/aem.00479-23 (Lichty et al. 2023: 'B)
- `salt_in_strategy —requires→ acidified_proteome`  (https://doi.org/10.3390/microorganisms12081738 (Bonnaud et a)
- `sodium_chloride —causes→ oxidative_stress`  (https://doi.org/10.1186/s12934-024-02358-5 (Yu et al. 2024 H)
- `high_salt_environment —induces→ osmotic_stress`  (https://doi.org/10.3390/microorganisms12081738 (Bonnaud et a)
- _The existing graph captures the core osmotic-adaptation skeleton but misses oxidative stress response coupling and specific pathway details (ectoine biosynthesis, ion transporters, proteome adaptation) that are well-supported generically across multiple recent sources (2023–2024)."_

### environment/hyperthermophilic  — *adequate* (5 edges)
- **Missing modules:** compatible solutes/extremolytes biosynthesis (DIP, cDPG), GMGT lipid biosynthesis and modification (Gms, Gmm), heat shock regulatory cascade (Phr, transcriptional control)
- `increased growth temperature —triggers biosynthesis of→ compatible solutes (cDPG, DIP)`  (DOI:10.3389/fmicb.2023.1267570 (Rose 2023))
- `compatible solutes (cDPG, DIP) —stabilizes→ archaeal proteins and DNA`  (DOI:10.3389/fmicb.2023.1267570 (Rose 2023))
- `elevated growth temperature —increases production of→ GMGT membrane lipids`  (DOI:10.1073/pnas.2318761121 (Garcia 2024))
- `Gms and Gmm enzymes —catalyze cross-linking and modification of→ GDGT to form GMGT`  (DOI:10.1038/s41467-024-49650-x (Li 2024))
- `small HSPs and prefoldin —shuttle substrates to→ thermosome (archaeal chaperonin)`  (DOI:10.1128/mbio.03593-22 (Baes 2023))
- `heat shock (temperature upshift) —triggers→ proteostasis response (HSP20, VAT1, thermosome upregulation)`  (DOI:10.1128/mbio.02174-23 (Grünberger 2023))
- _Existing graph covers core mechanisms (thermostable enzymes, chaperonins, DNA topology, membrane lipids) but omits generic extremolyte biosynthesis, detailed lipid remodeling enzymes (Gms/Gmm), and heat shock regulatory scaffolding—three well-supported mechanistic modules present in 2023-2024 literature."_

### environment/obligately_acidophilic  — *adequate* (6 edges)
- **Missing modules:** K+ transport systems (Kdp/Kef) and inside-positive membrane potential, Na+/H+ antiporter proton export, P-type ATPase proton pumping, Hopanoid and lipid-based membrane impermeability, Glutamate decarboxylase and cytoplasmic proton consumption
- `K+ uptake system (Kdp/Kef) —creates→ inside-positive membrane potential`  (DOI:10.3389/fmicb.2023.1149903)
- `Na+/H+ antiporter (NhaA/NhaB) —exports→ proton`  (DOI:10.3389/fmicb.2023.1149903 + 10.1101/2023.07.13.548807)
- `P-type ATPase (proton-translocating) —increases→ proton efflux`  (DOI:10.3389/fmicb.2023.1149903)
- `hopanoid-containing membrane —decreases→ proton permeability`  (DOI:10.1111/1758-2229.70019)
- `glutamate decarboxylase (Gad) —consumes→ cytoplasmic proton`  (DOI:10.3389/fmicb.2023.1149903)
- `urease system (UreABCDEFGHJ) —increases→ cytoplasmic buffering`  (DOI:10.3389/fmicb.2023.1149903)
- _Existing graph captures pH homeostasis backbone; generic mechanistic modules from 2023–2024 consensus literature (K+ systems, Na+/H+ antiporters, P-type ATPases, hopanoids, decarboxylases) are documented but absent from the trait graph._

### metabolism/homoacetogenesis  — *adequate* (9 edges)
- **Missing modules:** WLP methyl-branch intermediates (formate, formyl-THF) and their enzymes (Fdh, Fhs), electron-bifurcating hydrogenase + reduced ferredoxin/NADH coupling, membrane-potential energy conservation (Rnf or Ech complex detail)
- `carbon_dioxide —is reduced by formate dehydrogenase to→ formate`  (DOI:10.1039/d4cb00099d (Bae et al. 2024, pages 2-3))
- `formate —is converted by formyl-THF synthetase to→ formyl_tetrahydrofolate`  (DOI:10.1039/d4cb00099d (Bae et al. 2024, pages 2-3))
- `molecular_hydrogen —oxidized by electron-bifurcating hydrogenase yields→ reduced_ferredoxin_and_nadh`  (DOI:10.1039/d4cb00099d (Bae et al. 2024, pages 1-2,2-3))
- `carbon_monoxide —oxidized by CODH produces→ reduced_ferredoxin`  (DOI:10.1039/d4cb00099d (Bae et al. 2024, pages 2-3))
- `rnf_complex —generates transmembrane ion gradient driving→ atp_synthase`  (DOI:10.3389/fmicb.2023.1185739 (Frolov et al. 2023, pages 1-)
- `ech_complex —generates transmembrane ion gradient driving→ atp_synthase`  (DOI:10.3389/fmicb.2023.1185739 (Frolov et al. 2023, pages 1-)
- _The existing graph captures the trait's backbone (WLP, substrates, acetyl-CoA→acetate, ATP) but misses formate/formyl-THF pathway intermediates, enzyme nodes (Fdh, Fhs), electron-bifurcating hydrogenase, and explicit Rnf/Ech membrane-potential coupling—all generic, well-supported mechanisms in the literature."_

### morphology/crescent_shaped  — *adequate* (4 edges)
- **Missing modules:** elongasome coordination / MreB-guided peptidoglycan insertion, envelope biosynthesis prerequisite (LPS/envelope assembly), inner-membrane localization specificity
- `MreB —coordinates→ peptidoglycan insertion`  (Cabeen et al. 2009 doi:10.1038/emboj.2009.61)
- `LPS biosynthesis —enables→ crescentin envelope association`  (Cabeen et al. 2010 doi:10.1128/jb.01371-09 — mutations in LP)
- `inner membrane —localizes_to→ crescentin filament`  (Liu et al. 2024 doi:10.1073/pnas.2309984121 — cryo-ET shows )
- `peptidoglycan insertion —driven_by→ differential growth rate around cell circumference`  (Cabeen et al. 2009 doi:10.1038/emboj.2009.61 — 'differential)
- `elongasome —guided_by→ MreB-crescentin complex`  (Cabeen et al. 2009 doi:10.1038/emboj.2009.61 and Pöhl et al.)
- `cell envelope structure —required_for→ crescentin localization and curvature function`  (Cabeen et al. 2010 doi:10.1128/jb.01371-09)
- _Existing graph captures the generic asymmetric-growth abstraction unifying all four taxon-specific morphogenesis pathways (crescentin, CrvA/CrvB, Bd1075, Por39/Por41–PapS); misses generic supporting context on elongasome coordination and envelope prerequisites, but core mechanism is sound for a generic trait graph."_

### morphology/swarming_motility  — *adequate* (3 edges)
- **Missing modules:** quorum sensing regulation of surfactant, c-di-GMP signaling switch, flagellar gene regulation (FliA pathway), biosurfactant production/secretion, semi-solid substrate environmental context
- `quorum sensing signaling —positively_regulates→ biosurfactant production`  (DOI:10.1063/5.0128140 (Bru et al. 2023) and DOI:10.1128/spec)
- `c-di-GMP signaling —negatively_regulates→ flagellar motor stator recruitment`  (DOI:10.1128/mbio.03322-23 (de Anda et al. 2024) describes Fl)
- `flagellar gene regulatory factors —positively_regulates→ flagellar assembly and function`  (DOI:10.1128/spectrum.00166-24 (Pastora et al. 2024) shows Fl)
- `biosurfactant production —enables→ swarming motility`  (DOI:10.1063/5.0128140 (Bru et al. 2023) and DOI:10.1128/spec)
- `semi-solid agar substrate —enables→ swarming motility`  (DOI:10.1016/j.mex.2024.102622 (Pozo et al. 2024) optimized 0)
- `Gac/Rsm pathway —positively_regulates→ biosurfactant production`  (DOI:10.1128/spectrum.00166-24 (Pastora et al. 2024) shows Rs)
- _Existing graph captures the minimal core (flagella + surfactant) but misses regulatory checkpoints (QS, c-di-GMP, Gac/Rsm) and the critical intermediate step of biosurfactant production/secretion; adding 4-5 generic regulatory edges would elevate to 'complete' coverage of well-supported mechanism."_

### physiology/chemoorganoheterotrophic  — *adequate* (10 edges)
- **Missing modules:** substrate transport/import step, NAD(P)H / reducing power generation
- `organic_molecule —imported via→ substrate_transporter`  (10.1021/acsomega.3c02205 (stebegg 2023, pages 2-4): 'heterot)
- `catabolism —produces→ nadph`  (10.1021/acsomega.3c02205 (stebegg 2023, pages 2-4): 'the ent)
- `respiration —requires→ terminal_electron_acceptor`  (10.1134/S0026261724605608 (pavlova 2024, pages 1-2) and 10.1)
- `substrate_transporter —enables→ catabolism`  (10.1021/acsomega.3c02205 (stebegg 2023, pages 2-4): 'heterot)
- `nadph —required for→ biomass`  (10.1016/B978-012373944-5.00083-3 (encyclopedic reference in )
- `organic_carbon —provides→ catabolism`  (10.1111/gcb.16925 (wang 2023, pages 1-2): 'microorganisms us)
- _Graph captures core trait-defining mechanism (C, electron, energy from organics; catabolism-ATP-biomass pathway) but omits mechanistically generic modules for substrate transport and NAD(P)H/reducing power production; these are broadly applicable rather than taxon/assay-specific, warranting addition for a complete generic mechanism."_

### physiology/trophic_type  — *adequate* (8 edges)
- **Missing modules:** carbon-fixation pathways (CBB, rTCA), inorganic electron-donor substrates (Fe(II), H2, S), respiratory electron transport chains, heterotrophic substrate catabolism (sugar transporters, CAZymes)
- `Calvin-Benson-Bassham cycle —realizes→ autotrophic carbon assimilation`  (DOI:10.1128/AEM.00599-24 (Tothero et al. 2024: universal mar)
- `reductive TCA cycle —realizes→ autotrophic carbon assimilation`  (DOI:10.1128/mSystems.00148-24 (Wang et al. 2024: alternative)
- `Fe(II) oxidation pathway —enables→ chemolithotrophic energy metabolism`  (DOI:10.1128/AEM.00599-24 (Tothero et al. 2024: cyc2/mtoA mar)
- `sulfur/thiosulfate oxidation (sox genes) —enables→ chemolithotrophic energy metabolism`  (DOI:10.1128/AEM.00599-24 (Tothero et al. 2024: soxABXYZ clus)
- `organic carbon transporters and catabolic enzymes —enable→ heterotrophic metabolism`  (DOI:10.1128/AEM.00599-24 (Tothero et al. 2024: gtsABC/frcABC)
- `terminal oxidases (cbb3, bd, aa3) —enable→ aerobic electron transport`  (DOI:10.1128/AEM.00599-24 (Tothero et al. 2024: high-affinity)
- _Existing graph captures the three classification axes (carbon, energy, electron donor) abstractly; mechanistic report reveals deeper pathways and substrates that realize trophic phenotypes but are absent from the current causal structure._

### environment/non_halophilic  — *adequate* (6 edges)
- **Missing modules:** osmotic upshift-triggered water efflux / cytoplasmic volume decrease (initial physical trigger), glutamate counterion balancing to support K+ accumulation (ionic homeostasis)
- `high_osmolarity —causes→ water_efflux`  (DOI:10.1128/mmbr.00181-23 — Foster et al., 2024, pages 6-8: )
- `water_efflux —reduces→ turgor_pressure`  (DOI:10.1128/mmbr.00181-23 — Foster et al., 2024, pages 6-8: )
- `potassium_ion —requires_counterion_from→ glutamate_accumulation`  (DOI:10.1128/mmbr.00181-23 — Foster et al., 2024, pages 6-8: )
- `high_intracellular_K_and_ionic_strength —triggers→ compatible_solute_accumulation`  (DOI:10.1128/mmbr.00181-23 — Foster et al., 2024, pages 10-12)
- _The existing graph captures the core generic non-halophilic osmostress pathway (K+ and compatible solute accumulation) but omits two foundational generic modules: the initial water-efflux trigger and the glutamate counterion mechanism; wisely excludes taxon-limited c-di-AMP regulation."_

### genomics/rrna_operon_copy_number  — *adequate* (2 edges)
- **Missing modules:** rRNA transcription initiation capacity step, growth efficiency trade-off (inverse relationship), transcriptional RNAP allocation/redistribution mechanism
- `rRNA operon copy number —increases capacity for→ rRNA transcription initiation`  (Multiple rrn operons raise the ceiling for rRNA transcriptio)
- `rRNA transcription initiation —enables→ ribosome biogenesis`  (Higher rRNA transcription capacity directly supports ribosom)
- `rRNA operon copy number —inversely associated with→ growth efficiency`  (Growth efficiency is inversely related to maximal growth rat)
- `rRNA operon copy number —increases→ maximal growth rate`  (Maximum reproductive rate doubles with doubling of rrn copy )
- _Existing graph captures the foundational rrn copy-to-growth-rate skeleton but lacks intermediate rRNA transcription capacity node and inverse growth-efficiency trade-off; adding these two modules would strengthen mechanistic specificity without departing from generic, well-supported mechanism."_

### metabolism/substrate_level_phosphorylation  — *adequate* (6 edges)
- **Missing modules:** anaerobic environmental conditioning, phosphotransacetylase-catalyzed acetyl-CoA activation, fermentation-to-ATP direct linking
- `low oxygen / anaerobiosis —enables→ fermentation`  (10.1093/femsre/fuae016 (Hackmann 2024): foundational conditi)
- `fermentation —produces ATP via→ substrate-level phosphorylation`  (10.1093/femsre/fuae016 (Hackmann 2024): definitional bridge )
- `phosphotransacetylase —catalyzes→ acetyl-CoA to acetyl-phosphate conversion`  (10.1042/ETLS20220092 (Hosmer 2023): central acetate-switch e)
- `AckA-Pta pathway —allows ATP production via→ substrate-level phosphorylation`  (10.1042/ETLS20220092 (Hosmer 2023): strong review-level supp)
- _Existing graph captures acetate kinase branch well but lacks the anaerobic context, explicit PTA catalytic step, and direct fermentation-to-ATP bridge; all missing elements are generic and supported by peer-reviewed reviews (Hackmann 2024, Hosmer 2023)._

### upper/phenotype  — *adequate* (4 edges)
- **Missing modules:** entity-quality formalization (phenotype has_participant entity; has_quality quality), environmental context constraint pattern (context constrains phenotype)
- `phenotype_trait —has_participant→ affected_entity`  (10.1186/gb-2010-11-1-r2 — 'a phenotype description minimally)
- `phenotype_trait —has_quality→ quality_parent`  (10.1186/gb-2010-11-1-r2 — 'a phenotype description minimally)
- `environmental_context —constrains→ phenotype_trait`  (10.1242/dmm.002790 — 'phenotype denotes the actual observabl)
- `phenotype_quality —towards→ secondary_entity`  (10.1186/gb-2010-11-1-r2 — 'EQ descriptions may also include )
- _Existing graph correctly captures upper-ontology structure; research report's mechanistic edges are predominantly taxon/assay-specific, appropriately excluded. Four GENERIC representation-pattern edges from Mungall 2010 could strengthen entity-quality formalization and environmental context modeling._

### environment/strictly_anaerobic  — *adequate* (4 edges)
- **Missing modules:** iron-sulfur cluster inactivation, glycyl radical enzyme incompatibility, PFOR/PFL oxygen sensitivity
- `molecular oxygen / reactive oxygen species —oxidizes / inactivates→ iron-sulfur cluster enzymes`  (10.1128/IAI.00502-24 (Rose et al. 2025): oxygen directly oxi)
- `molecular oxygen —inactivates→ glycyl radical enzymes`  (10.1128/IAI.00502-24 (Rose et al. 2025): Certain enzyme clas)
- `molecular oxygen / reactive oxygen species —inactivates→ pyruvate formate-lyase (PFL) and pyruvate:ferredoxin oxidoreductase (PFOR)`  (10.1038/s43705-023-00251-7 (Okabe et al. 2023): key anaerobi)
- _The existing graph captures the oxygen-inhibition backbone and ROS damage, but conflates distinct enzyme-specific toxicity mechanisms under a generic 'oxygen-sensitive enzymes' node; adding edges for Fe-S cluster, glycyl radical, and PFOR/PFL vulnerability would provide mechanistic depth while remaining generic across anaerobic lineages."_
