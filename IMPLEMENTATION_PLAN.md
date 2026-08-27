# AE3PT Complete Project Implementation Plan

## Research, Micro-Steps, Binary Gates, Evidence, and Delivery Sequence

**Project:** Adaptive Electroformed 3D Power Topology Simulator<br>
**Document status:** Project execution baseline<br>
**Version:** 0.1<br>
**Date:** 2026-08-27<br>
**Companion architecture:** `AE3PT_SIMULATOR_ROADMAP.md`

---

## 1. Purpose and Authority

This document converts the 20-part AE3PT architecture roadmap into an executable program. It defines:

- the research program;
- the complete work breakdown structure;
- the order and dependencies of work;
- micro-steps and required artifacts;
- binary pass/fail gates;
- numerical, software, manufacturing, safety, and experimental evidence;
- demonstrator and release criteria;
- failure response, rollback, and change control.

`AE3PT_SIMULATOR_ROADMAP.md` remains the architectural intent. This document is the implementation authority for sequencing and acceptance. If a new discovery requires an architectural change, the architecture document must be revised first, then this plan must be updated through change control.

This is a complete planning baseline, not a claim that every future research unknown is already known. Newly discovered work enters the requirements register, receives an owner, dependency, evidence requirement, and gate impact before it becomes part of the accepted program.

---

## 2. Definition of Project Completion

AE3PT is complete at the **Engineering Preview** level only when all of the following are true:

1. all 20 work packages have passed their local exit gates;
2. Master Gates G0-G10 have passed in sequence;
3. the busbar, repairable busbar, hollow conductor, motor winding, and integrated assembly demonstrators have current evidence bundles;
4. every promoted claim maps to source, implementation, deterministic verification, calibration or physical validation, uncertainty, review, and release evidence;
5. the simulator can replay accepted studies from immutable manifests;
6. no unresolved critical safety, data-integrity, numerical-correctness, manufacturing-feasibility, or passport-integrity defect remains;
7. installation and replay succeed on a clean reference environment not used for development;
8. limitations, unsupported conditions, calibration domains, and certification boundaries are published;
9. manufacturing export requires and records explicit human approval;
10. software release status is not represented as physical-product certification.

The following terms are deliberately distinct:

| Status | Meaning |
|---|---|
| Implemented | code or process exists |
| Verified | implementation agrees with analytic, manufactured, or trusted numerical references in a declared domain |
| Calibrated | uncertain model parameters have been fitted using traceable data without hiding residual error |
| Validated | predictions agree with independent physical evidence within pre-approved acceptance criteria |
| Demonstrated | the capability works in an end-to-end representative workflow |
| Approved | an authorized human has accepted the exact evidence bundle and artifact identities |
| Released | the approved version is packaged, documented, reproducible, and available to its intended users |
| Certified | an applicable external authority or accredited process has accepted the product or workflow |

No lower status implies a higher one.

---

## 3. Gate Rules

All formal gates are binary.

### PASS

A gate passes only when:

- every mandatory criterion is satisfied;
- every required artifact exists and has an immutable identity;
- all tests and experiments listed for the gate have completed with recorded exit status;
- evidence uses the candidate source, data, geometry, process, and configuration being approved;
- all critical and high-severity findings are closed or explicitly removed from the claimed scope;
- the reviewer signs the exact gate summary and artifact manifest;
- rollback instructions have been tested where the gate changes a baseline or release.

### FAIL

A gate fails when any mandatory criterion is unsatisfied, evidence is missing or stale, a required test did not execute, an artifact identity is ambiguous, an unexplained discrepancy exceeds its threshold, or safety authorization is absent.

On failure:

1. do not promote the candidate, model, dataset, process, or release;
2. preserve all failed evidence and logs;
3. create a corrective-action record;
4. identify the earliest invalid assumption or artifact;
5. return to that work package;
6. rerun all dependent evidence after correction;
7. never relabel a failed result as a pass by changing thresholds after seeing the result.

“Conditional pass,” “mostly pass,” and “pass with missing evidence” are not formal gate states. A review may remain **open**, but an open gate does not unlock dependent work.

### Threshold Change Rule

Acceptance thresholds may change only when:

- the change is proposed before the affected validation run;
- the physical or statistical rationale is documented;
- the affected requirements and risks are updated;
- the change is independently reviewed;
- the previous threshold and evidence remain visible.

---

## 4. Evidence Classes

Every work package uses the following evidence classes.

| Code | Evidence class | Examples |
|---|---|---|
| E0 | Intent | charter, requirement, hypothesis, planned method |
| E1 | Source evidence | primary research, official standard, supplier record, regulation |
| E2 | Implementation evidence | source, schema, model, process specification, configuration |
| E3 | Deterministic verification | unit, property, analytic, conservation, convergence, replay tests |
| E4 | Cross-model verification | reduced versus reference, mesh refinement, independent solver comparison |
| E5 | Calibration evidence | coupon data, parameter fit, residuals, holdout performance |
| E6 | Physical validation | component experiment, uncertainty budget, as-built measurements |
| E7 | Lifecycle demonstration | operation, damage, inspection, repair, reuse, disassembly, passport transition |
| E8 | Human review | signed gate decision tied to exact artifact identities |
| E9 | Release evidence | package, manifest, clean install, rollback, limitations, release notes |

An evidence record must contain:

- unique identifier;
- creation time;
- responsible person or system;
- source revision and input hashes;
- units and coordinate frame where relevant;
- method and equipment identity;
- raw and processed data identities;
- uncertainty and validity domain;
- pass/fail threshold;
- actual result;
- decision and reviewer;
- supersession link if corrected later.

---

## 5. Initial Quantitative Acceptance Thresholds

These are the starting project thresholds. Gate G1 must confirm or replace them before dependent experiments begin.

### Software and Reproducibility

- identical deterministic inputs produce identical artifact identities;
- stochastic studies reproduce the same population and ranking inputs from recorded seeds;
- all required commands propagate nonzero failures;
- no critical numerical path accepts NaN, infinity, missing units, or out-of-domain material data;
- critical mathematical kernels achieve at least 90% branch coverage and mutation testing of safety-relevant conditions;
- overall automated coverage target is at least 80%, without using coverage as a substitute for numerical verification;
- clean-environment replay reproduces key reported metrics within the solver's declared tolerance.

### Numerical Verification

- analytic electrical and thermal fixtures: relative error no greater than 0.1% unless discretization theory justifies another pre-approved threshold;
- current and energy conservation residuals: no greater than 0.1% of the relevant total for promoted component simulations;
- mesh refinement: less than 1% change in each gate-critical scalar between the final two accepted meshes, or an approved asymptotic error estimate;
- coupled iteration: residual and state-change thresholds defined before execution and satisfied without hidden fallback;
- reduced-to-reference discrepancy: quantified for every promoted fidelity boundary.

### Initial Physical Validation

- four-wire resistance prediction: within 10% of measurement or within the combined precomputed 95% uncertainty interval, whichever is stricter after G1 review;
- hotspot temperature: within 5 °C or the combined 95% uncertainty interval;
- deposited mass: within 5% of measurement;
- local plating thickness: median absolute percentage error no greater than 15%, with no missed safety-critical under-plated region;
- critical under-plating detection: at least 90% recall and no false negative at a terminal, pressure wall, or minimum-current section;
- leak test: zero detectable leakage at maximum operating pressure;
- proof pressure: no leak or permanent deformation that violates requirements at 1.5 times maximum operating pressure;
- repaired conductor: at least 90% of nominal conductance restored and all safety constraints re-passed;
- motor winding: torque and back EMF within 5%, total loss within 10%, and hotspot temperature within 7 °C of independent measurement for the validated operating points.

These thresholds do not override application standards or safety factors. If an applicable standard is stricter, the stricter requirement controls.

---

## 6. Research Program

Research is a continuous workstream, not a one-time literature search. It must produce traceable decisions, model choices, validation methods, and known gaps.

### 6.1 Research Questions

The research register must answer at least the following:

1. Which topology representations support simultaneous electrical, thermal, structural, manufacturing, and repair roles?
2. Which reduced-order conductor models preserve candidate ranking over the intended geometry families?
3. Which 3D electrical formulations are needed for DC, AC, skin, proximity, eddy-current, and contact effects?
4. Which electroplating models are adequate for open surfaces, internal channels, lattices, blind passages, and repair deposition?
5. Which material and interface properties dominate electroformed conductor performance and life?
6. How should print, clean, seed, electrolyte, gas, rinse, inspection, and repair access be represented geometrically?
7. Which ageing modes are credible for each demonstrator and how can they be accelerated without changing the failure mechanism?
8. Which inspection methods can observe thickness loss, delamination, blockage, resistance drift, cracks, or leakage?
9. How can topology optimization include disassembly, local repair, modular replacement, and reuse without reducing them to cosmetic scores?
10. Which lifetime cost, functional mass, circularity, and supply-risk metrics avoid double counting?
11. Which standards apply to additive manufacturing, coating measurement, electrical machines, insulation, environmental testing, LCA, material declaration, digital passports, hazardous chemicals, and wastewater?
12. What experimental evidence is required to move each engine from implemented to verified, calibrated, validated, and demonstrated?
13. Which commercial or open solvers can be legally and reproducibly integrated?
14. Which patents or foreground IP may constrain electroformed internal conductors, repair plating, winding geometry, or digital lifecycle methods?
15. Which capabilities require external specialists, accredited laboratories, or certification bodies?

### 6.2 Research Micro-Steps

- [ ] `RES-001` Create `research/questions.yaml` with one stable identifier per research question.
- [ ] `RES-002` Define keywords, synonyms, exclusions, and date bounds for each question.
- [ ] `RES-003` Define source tiers: primary experiment, primary model, official standard/regulation, validated dataset, review, vendor note, commentary.
- [ ] `RES-004` Define inclusion criteria for geometry, materials, scale, current, temperature, process, repair, and validation relevance.
- [ ] `RES-005` Define exclusion criteria and require a reason for every rejected full-text candidate.
- [ ] `RES-006` Search scholarly databases and publisher indexes using saved query strings.
- [ ] `RES-007` Search standards bodies and regulators using a separate applicability protocol.
- [ ] `RES-008` Search patent databases by inventor, assignee, classification, and claim concept.
- [ ] `RES-009` Record search date, database, query, result count, selected records, and deduplication.
- [ ] `RES-010` Acquire permissible full text or record access limitations.
- [ ] `RES-011` Extract model equations, assumptions, geometry, boundary conditions, material data, mesh, calibration, validation, and error.
- [ ] `RES-012` Extract manufacturing process, bath chemistry, current waveform, flow, temperature, time, seed, cleaning, measurement, and defects for plating studies.
- [ ] `RES-013` Extract lifecycle state, damage mechanism, repair action, restored function, and follow-up life for repair studies.
- [ ] `RES-014` Grade evidence quality and direct applicability to each demonstrator.
- [ ] `RES-015` Reproduce at least one numerical result from every model family selected for implementation.
- [ ] `RES-016` Create an unresolved-question list rather than inferring missing data.
- [ ] `RES-017` Hold a domain review for each engine before freezing its initial model hierarchy.
- [ ] `RES-018` Link each adopted equation, threshold, and test method to its source evidence record.
- [ ] `RES-019` Repeat living searches quarterly and before each master gate.
- [ ] `RES-020` Publish a research delta report listing new sources, changed conclusions, and gate impact.

### 6.3 Initial Research Anchors

The initial evidence library should include and critically reproduce, rather than merely cite:

- the 2025 internal-channel and embedded copper electroplating work supplied with the architecture brief;
- experimentally validated electrothermal busbar topology optimization;
- additively manufactured electric-machine conductors with integrated heat exchange;
- three-dimensional copper electrodeposition models validated against plating-cell geometry;
- coating-uniformity work on additively manufactured lattice electrodes;
- topology optimization for hybrid subtractive-additive remanufacturing;
- integrated product-process additive remanufacturing methods;
- primary research on inspection, accelerated ageing, repaired interfaces, and second-life electrical components.

### 6.4 Standards and Regulatory Research Baseline

At minimum, the applicability register must review current editions and licensing requirements for:

- ISO/ASTM 52910 for additive-manufacturing design requirements and recommendations;
- ISO/ASTM 52920 for qualification principles and quality assurance in industrial additive manufacturing;
- ISO/ASTM 52901 and process-specific standards where the selected manufacturing route requires them;
- ASME V&V 10, V&V 20, and applicable computational-model verification and validation guidance;
- ASTM B193 for resistivity of electrical conductor materials;
- ASTM B487 or an approved equivalent for microscopical coating-thickness measurement;
- IEC 60664 for insulation coordination and clearance/creepage reasoning;
- IEC 60034 series for rotating electrical-machine performance, ratings, test methods, and winding concerns;
- IEC 62474 for material declaration and substance data exchange;
- ISO 14040 and ISO 14044 for lifecycle assessment principles and requirements;
- Regulation (EU) 2024/1781 where digital product passport interoperability or EU market access is relevant;
- applicable electrical, pressure, coolant, environmental, ingress, vibration, and EMC standards for each demonstrator;
- Australian and Queensland hazardous-chemical, electrical, waste, and environmental requirements for any local electroplating laboratory.

The standards register must record title, edition, status, jurisdiction, licensed copy owner, applicable clauses, evidence artifact, and whether the standard is mandatory, contractually required, or voluntarily adopted.

### Research Gate R-GATE

**PASS** when all high-priority research questions have evidence summaries, selected models have reproducibility notes, the standards register has responsible owners, unresolved gaps have planned experiments, and no gate-critical equation or test threshold lacks provenance.

**FAIL** when a selected model is based only on secondary commentary, an applicable standard is unknown, a primary source cannot be inspected, a result cannot be reproduced sufficiently to assess its method, or a known evidence gap is hidden by an assumption.

---

## 7. Program Organization and Responsibilities

The program needs named responsibility even if one person initially fills several roles.

| Role | Principal responsibility |
|---|---|
| Program lead | scope, resources, sequencing, stakeholder decisions |
| Chief systems architect | canonical contracts, dependencies, architecture integrity |
| Research lead | literature, standards, patents, evidence quality |
| Electrical/EM lead | circuit, field, AC, machine, force, loss models |
| Thermal/fluid lead | heat transfer, coolant networks, CFD, calibration |
| Structural/life lead | stress, vibration, pressure, fatigue, damage |
| Manufacturing/process lead | printability, seeding, plating, cleaning, finishing, repair process |
| Materials lead | bulk, interface, process-conditioned, recovered-component data |
| Lifecycle/circularity lead | inspection, repair, reuse, disassembly, LCA, passport |
| Optimization/UQ lead | search, sensitivity, surrogate, uncertainty, robustness |
| Software/platform lead | implementation, packaging, APIs, compute, UI |
| Data/evidence lead | schemas, provenance, manifests, evidence ledger, retention |
| V&V lead | verification plans, experiment independence, discrepancy review |
| Laboratory and EHS lead | risk assessments, training, equipment, chemicals, waste, incidents |
| QA/release lead | gates, audits, defect severity, clean install, release bundle |
| Independent reviewer | challenge assumptions and approve defined gates |

No model owner may be the sole approver of that model's validation gate.

---

## 8. Repository and Artifact Layout

The implementation should converge on the following controlled structure:

```text
AE3PT/
├── README.md
├── AE3PT_SIMULATOR_ROADMAP.md
├── IMPLEMENTATION_PLAN.md
├── CHANGELOG.md
├── pyproject.toml
├── uv.lock or equivalent lock
├── docs/
│   ├── charter/
│   ├── architecture/
│   ├── requirements/
│   ├── research/
│   ├── standards/
│   ├── safety/
│   ├── verification/
│   ├── experiments/
│   ├── demonstrators/
│   └── releases/
├── schemas/
├── data/
│   ├── reference/
│   ├── calibration/
│   ├── validation/
│   └── examples/
├── ae3pt/
│   ├── mission/
│   ├── core/
│   ├── geometry/
│   ├── materials/
│   ├── physics/
│   ├── manufacturing/
│   ├── lifecycle/
│   ├── economics/
│   ├── authority/
│   ├── optimisation/
│   ├── orchestration/
│   ├── applications/
│   └── ui/
├── tests/
│   ├── unit/
│   ├── property/
│   ├── analytic/
│   ├── regression/
│   ├── integration/
│   ├── replay/
│   └── acceptance/
├── experiments/
│   ├── protocols/
│   ├── travelers/
│   ├── raw-manifests/
│   └── analysis/
├── benchmarks/
├── examples/
├── tools/
└── .github/ or equivalent CI configuration
```

Large raw data and solver artifacts may live outside Git, but their immutable manifests and content identities must remain in the controlled project record.

---

## 9. Master Delivery Sequence

| Stage | Indicative window | Master gate | Main result |
|---|---:|---|---|
| S0 | M0-M2 | G0 | charter, research protocol, safety hold, project controls |
| S1 | M1-M6 | G1 | requirements, architecture, standards, evidence and threshold baseline |
| S2 | M3-M10 | G2 | reproducible core platform, data model, geometry, materials |
| S3 | M6-M14 | G3 | reduced-order digital busbar optimization loop |
| S4 | M9-M20 | G4 | calibrated plating coupons and process model |
| S5 | M14-M24 | G5 | physically validated optimized busbar |
| S6 | M20-M32 | G6 | damage, inspection, repair, reuse, passport demonstrator |
| S7 | M26-M40 | G7 | hollow cooled conductor with pressure and life proof |
| S8 | M32-M50 | G8 | 3D motor winding demonstrator |
| S9 | M44-M58 | G9 | integrated assembly and assembly-level lifecycle proof |
| S10 | M52-M60 | G10 | engineering preview release and external replay |

The windows assume parallel work by multiple disciplines. A smaller team must preserve gate order even if the calendar expands.

---

## 10. Master Gates

### G0 — Program Authorization and Safety Hold

**PASS criteria**

- project charter, scope, role assignments, change control, and risk register are approved;
- research protocol and evidence classes are adopted;
- wet-chemistry, high-current, pressure, rotating, and hazardous-material activities have explicit safety holds;
- no physical experiment can start without the relevant hold being released by the EHS lead;
- data retention and incident reporting are defined.

**FAIL criteria**

- missing accountable owner;
- physical procurement or testing begins before hazard review;
- no source/evidence policy;
- no stop-work authority;
- project success is defined only as “software runs.”

### G1 — Requirements, Research, Standards, and Threshold Baseline

**PASS criteria**

- R-GATE passes;
- mission and requirement baselines exist for all five demonstrators;
- standards and jurisdiction applicability are reviewed;
- acceptance thresholds are approved before data collection;
- research gaps have experiments or explicit scope exclusions;
- the requirement-to-evidence matrix covers every roadmap claim.

**FAIL criteria**

- missing mission scenarios;
- unreviewed safety or standards applicability;
- acceptance criteria selected after observing results;
- model selection without inspectable primary evidence.

### G2 — Reproducible Core Platform

**PASS criteria**

- Parts 2-5 and the applicable core of Parts 18 and 20 pass local gates;
- mission, identities, units, provenance, geometry, materials, manifests, and evidence records replay deterministically;
- analytic geometry and property fixtures pass;
- a clean environment reproduces the reference study setup.

**FAIL criteria**

- results depend on hidden local state;
- units or coordinate frames are ambiguous;
- derived facts overwrite authored or measured facts;
- stale results survive invalidating input changes.

### G3 — Reduced-Order Digital Busbar Loop

**PASS criteria**

- topology generation, electrical screening, reduced thermal analysis, manufacturability pre-check, cost, repairability, and Pareto search execute end to end;
- analytic and conservation tests pass;
- at least three topology families survive screening;
- rejected designs have machine-readable reasons;
- a frozen seed reproduces the same candidate population and objective inputs.

**FAIL criteria**

- disconnected or unmanufacturable candidates reach the accepted Pareto set;
- search ranking changes without an input or version change;
- a single hidden weighted score replaces hard constraints and the Pareto vector.

### G4 — Plating Research and Coupon Calibration

**PASS criteria**

- laboratory safety hold is released;
- plating-cell, seed, chemistry, flow, current, temperature, and measurement records are complete;
- coupons span flat, recessed, channel, branch, and difficult-access geometries;
- deposited mass and thickness thresholds pass on holdout coupons;
- model residuals and invalid domains are documented;
- process wastewater and chemical handling comply with the approved site plan.

**FAIL criteria**

- missing raw measurement data;
- calibration and validation use the same specimens without a pre-approved method;
- unsafe or unapproved chemistry/process change;
- under-plated critical regions are missed;
- model predictions are used outside the coupon domain without explicit uncertainty and review.

### G5 — Physical Optimized Busbar

**PASS criteria**

- conventional reference and optimized candidates are manufactured from controlled process travelers;
- as-built geometry and thickness maps replace nominal geometry in final prediction;
- resistance, mass, temperature, and manufacturing feasibility thresholds pass;
- the optimized candidate improves at least one primary lifetime metric without violating any hard constraint;
- all original predictions, discrepancies, and corrected models remain auditable.

**FAIL criteria**

- only the best successful specimen is reported;
- rework is omitted from cost or yield;
- nominal geometry is used despite measured process variation;
- improvement depends on a failed safety, repair, or manufacturing constraint.

### G6 — Damage, Repair, Reuse, and Passport Demonstration

**PASS criteria**

- controlled damage is detected and localized;
- degraded operation is predicted within thresholds;
- a repair plan is generated before repair execution;
- repaired conductance and all applicable thermal, structural, insulation, and leak requirements pass;
- repair is compared with replacement using time, cost, material, risk, and remaining life;
- passport transitions preserve prediction, observation, repair, and requalification history.

**FAIL criteria**

- repair location or method is selected after seeing the outcome without recording the deviation;
- repaired component bypasses requalification;
- passport history is mutable or incomplete;
- repair restores conductivity but creates an unresolved safety defect.

### G7 — Hollow Cooled Conductor

**PASS criteria**

- electrical, thermal, flow, pump, pressure, stress, fatigue, cleanability, plating, and repair models are integrated;
- proof pressure and leak tests pass;
- resistance, temperature, pressure drop, and deformation predictions meet thresholds;
- blocked-flow and loss-of-cooling cases fail safely or meet degraded-operation requirements;
- lifetime comparison against the solid reference includes pump energy and maintenance.

**FAIL criteria**

- cooling benefit ignores pump or system burden;
- plating or cleaning cannot be verified inside the channel;
- proof-pressure or leak requirement fails;
- a blockage creates an unmodelled unsafe state.

### G8 — Three-Dimensional Motor Winding

**PASS criteria**

- DC and AC conductor effects, torque, back EMF, loss, cooling, force, vibration, insulation, manufacturing, and lifecycle models are coupled at the required fidelity;
- predicted torque, back EMF, loss, and hotspot thresholds pass;
- terminal, insulation, and repair access are verified;
- at least one faulted-winding scenario and one repair or module-replacement scenario are demonstrated;
- the design outperforms the conventional reference on an approved Pareto basis.

**FAIL criteria**

- only DC resistance is optimized;
- electromagnetic improvement violates cooling, stress, insulation, process, or repair constraints;
- rotor/stator safety controls or test procedures are incomplete;
- measurement comparison omits uncertainty or as-built geometry.

### G9 — Integrated Assembly Lifecycle Proof

**PASS criteria**

- winding, busbar, coolant, terminals, sensors, mounting, and selected power-electronic interconnects share one mission and passport hierarchy;
- component-level optima are re-evaluated at assembly level;
- fault propagation, maintenance access, disassembly, and recovered-component grading execute end to end;
- assembly metrics, interfaces, and evidence pass;
- at least one complete design-manufacture-operate-inspect-repair-reuse/recover scenario is replayable.

**FAIL criteria**

- component improvements create hidden assembly penalties;
- interface losses, coolant interactions, access, or control effects are omitted;
- passport ancestry breaks when components are replaced or reused.

### G10 — Engineering Preview Release

**PASS criteria**

- all local work-package gates pass;
- external clean installation and study replay pass;
- requirement-to-evidence audit has no uncovered mandatory requirement;
- release bundle includes source, dependency lock, schemas, migrations, benchmark results, validation evidence, limitations, open defects, rollback, and support policy;
- manufacturing export and baseline replacement require exact-hash approval;
- release language does not claim external certification.

**FAIL criteria**

- stale evidence references a different source or model revision;
- known critical defect or unexplained validation failure remains;
- external replay depends on undocumented local software, data, or credentials;
- release claims exceed evidence.

---

# Work Package 1 — Program Charter, Governance, Safety, and Research Control

## Objective

Create the controlled program environment in which every subsequent technical result can be trusted, stopped, reviewed, and reproduced.

## Entry Criteria

- project sponsor or owner identified;
- architecture roadmap available;
- repository write access available.

## Micro-Steps

### Research and Scope

- [ ] `WP01-001` Extract every explicit requirement, objective, metric, engine, demonstrator, and claim from `AE3PT_SIMULATOR_ROADMAP.md`.
- [ ] `WP01-002` Assign a stable requirement identifier to each extracted item.
- [ ] `WP01-003` Separate mandatory project requirements from hypotheses and future options.
- [ ] `WP01-004` Identify the initial target jurisdictions, laboratories, users, and application domains.
- [ ] `WP01-005` Complete the research question register described in Section 6.
- [ ] `WP01-006` Create the standards applicability register.
- [ ] `WP01-007` Create a patent and freedom-to-operate research log; mark it as technical planning, not legal advice.
- [ ] `WP01-008` Identify external laboratories, process specialists, and reviewers needed for unsupported capabilities.

### Governance

- [ ] `WP01-009` Draft and approve `PROJECT_CHARTER.md`.
- [ ] `WP01-010` Define scope, non-goals, success conditions, and cancellation conditions.
- [ ] `WP01-011` Define role assignments and named deputies.
- [ ] `WP01-012` Define decision rights for model selection, data correction, threshold change, manufacturing export, and release.
- [ ] `WP01-013` Define change-control states: proposed, reviewed, approved, implemented, verified, released, rejected.
- [ ] `WP01-014` Define defect severities and stop-ship/stop-test rules.
- [ ] `WP01-015` Define the append-only decision log.
- [ ] `WP01-016` Define data retention, backup, restoration, and access-control policy.
- [ ] `WP01-017` Define publication, supplier confidentiality, and embargo policy.

### Safety and Facilities

- [ ] `WP01-018` Create a hazard inventory for wet chemistry, heavy metals, acids, bases, fumes, electrical current, hot surfaces, pressure, rotating equipment, machining, lasers or imaging, lifting, and waste.
- [ ] `WP01-019` Create separate risk assessments for plating, high-current electrical tests, coolant pressure tests, fatigue/vibration tests, and rotating winding tests.
- [ ] `WP01-020` Identify required engineering controls, PPE, monitoring, ventilation, interlocks, barriers, emergency stops, spill kits, and eyewash/shower facilities.
- [ ] `WP01-021` Define chemical receipt, storage, labeling, SDS, inventory, bath sampling, disposal, and wastewater controls.
- [ ] `WP01-022` Confirm applicable Queensland and Australian licensing, electrical, environmental, hazardous-chemical, and waste requirements with competent professionals.
- [ ] `WP01-023` Define training and authorization matrices for each hazardous activity.
- [ ] `WP01-024` Implement a stop-work and incident-reporting process.
- [ ] `WP01-025` Keep all physical-test safety holds locked until required reviews and training pass.

### Program Controls

- [ ] `WP01-026` Create the master requirement-to-evidence matrix.
- [ ] `WP01-027` Create the integrated schedule and dependency graph.
- [ ] `WP01-028` Create the risk register with probability, consequence, detection, mitigation, owner, and gate impact.
- [ ] `WP01-029` Create procurement, staffing, and external-service registers.
- [ ] `WP01-030` Define monthly technical reviews and pre-gate audits.
- [ ] `WP01-031` Define quarterly research refresh and standards-status review.
- [ ] `WP01-032` Define configuration-baseline naming and archival rules.
- [ ] `WP01-033` Run a tabletop failure exercise covering stale evidence, unsafe test request, solver discrepancy, and corrupted passport history.

## Required Artifacts

- charter;
- requirements register;
- research register;
- standards register;
- patent research log;
- role and authorization matrix;
- safety plans and locked holds;
- risk, procurement, staffing, and change registers;
- requirement-to-evidence matrix;
- decision log.

## Local Gate WP01-G

**PASS** when every mandatory roadmap item has an identifier and owner, all hazardous activities are held pending authorization, research and standards responsibilities are assigned, the tabletop exercise succeeds, and G0 can pass.

**FAIL** when any work begins without scope ownership, physical testing can bypass safety authorization, evidence can be overwritten, or project claims lack mapped acceptance criteria.

---

# Work Package 2 — Mission and Requirements Layer

## Objective

Represent each application as versioned missions, scenarios, hard constraints, soft objectives, uncertainties, maintenance policies, and lifecycle requirements.

## Entry Criteria

- WP01-G passed;
- requirement identifiers and unit policy approved.

## Micro-Steps

### Research

- [ ] `WP02-001` Survey mission-profile representations used in power electronics, electric machines, reliability, fatigue, and lifecycle assessment.
- [ ] `WP02-002` Survey uncertainty representations for measured duty cycles and rare overload events.
- [ ] `WP02-003` Identify applicable mission and rating terminology from the selected electrical-machine and power-system standards.
- [ ] `WP02-004` Define how maintenance policy and degraded operation enter a mission without becoming geometry-specific.

### Schema and Semantics

- [ ] `WP02-005` Define `Mission`, `Scenario`, `TimeSeries`, `Event`, `Requirement`, `Constraint`, `Objective`, and `Assumption` schemas.
- [ ] `WP02-006` Define hard, soft, advisory, and informational requirement classes.
- [ ] `WP02-007` Define scenario probability, frequency, duration, and sequencing semantics.
- [ ] `WP02-008` Define deterministic, interval, distribution, and empirical-sample uncertainty representations.
- [ ] `WP02-009` Define unit and dimensional-analysis requirements.
- [ ] `WP02-010` Define environmental, electrical, thermal, mechanical, coolant, storage, transport, maintenance, damage, and end-of-life fields.
- [ ] `WP02-011` Define failure-consequence and degraded-power requirements.
- [ ] `WP02-012` Define repair-class, repair-cycle, inspection-interval, disassembly, reuse, and recyclability requirements.
- [ ] `WP02-013` Define requirement priority and conflict-resolution policy.
- [ ] `WP02-014` Define provenance for every measured or assumed mission input.

### Implementation

- [ ] `WP02-015` Implement typed schema models.
- [ ] `WP02-016` Implement unit-safe parsing and serialization.
- [ ] `WP02-017` Implement schema versioning and migration tests.
- [ ] `WP02-018` Implement time-series import with sampling, interpolation, and missing-data policy.
- [ ] `WP02-019` Implement scenario composition and mission aggregation.
- [ ] `WP02-020` Implement contradiction detection.
- [ ] `WP02-021` Implement unsupported-fidelity detection.
- [ ] `WP02-022` Implement trace links from requirements to solver inputs and objective terms.
- [ ] `WP02-023` Implement human-readable mission reports.

### Demonstrator Missions

- [ ] `WP02-024` Freeze Busbar Mission v1.
- [ ] `WP02-025` Freeze Repairable Busbar Mission v1.
- [ ] `WP02-026` Freeze Hollow Conductor Mission v1.
- [ ] `WP02-027` Freeze Motor Winding Mission v1.
- [ ] `WP02-028` Freeze Integrated Assembly Mission v1.
- [ ] `WP02-029` Define uncertainty sets and rare-event scenarios for each mission.
- [ ] `WP02-030` Obtain domain review and approval for each mission.

### Verification

- [ ] `WP02-031` Test valid round trips for every schema version.
- [ ] `WP02-032` Test missing units, incompatible dimensions, contradictory limits, invalid probabilities, overlapping events, and unsupported values.
- [ ] `WP02-033` Test deterministic resampling of measured time histories.
- [ ] `WP02-034` Test that every downstream boundary condition has a requirement or assumption source.
- [ ] `WP02-035` Test that a mission change invalidates dependent results.

## Required Artifacts

- mission schemas and migrations;
- unit and time-series library;
- five approved mission baselines;
- validation reports;
- requirement trace report.

## Local Gate WP02-G

**PASS** when all five demonstrator missions parse, validate, replay, expose uncertainty, and trace every solver input and objective to an approved requirement or assumption.

**FAIL** when a mission has missing units, contradictory constraints, hidden nominal assumptions, untraceable boundary conditions, or no defined degraded and lifecycle scenarios.

---

# Work Package 3 — Canonical Data, Provenance, Evidence, and Passport Backbone

## Objective

Build the immutable identity and evidence system that all geometry, simulation, process, experiment, lifecycle, and release work depends on.

## Entry Criteria

- WP01-G passed;
- core entity list approved;
- storage constraints understood.

## Micro-Steps

### Research and Design

- [ ] `WP03-001` Survey scientific artifact formats, content-addressed storage, provenance models, and digital-thread practices.
- [ ] `WP03-002` Review digital product passport interoperability requirements and IEC 62474 data concepts.
- [ ] `WP03-003` Identify privacy, supplier-confidentiality, retention, and export constraints.
- [ ] `WP03-004` Define canonical owners for every authored, derived, measured, calibrated, and approved fact.
- [ ] `WP03-005` Define identity rules for missions, designs, graphs, geometry, meshes, materials, processes, runs, datasets, passport states, and decisions.
- [ ] `WP03-006` Define hash normalization for structured text, arrays, meshes, and binary artifacts.
- [ ] `WP03-007` Define supersession without deletion.
- [ ] `WP03-008` Define validity-domain and uncertainty metadata.
- [ ] `WP03-009` Define access control, signing, and reviewer identity requirements.

### Schemas

- [ ] `WP03-010` Implement `Design` and lineage schema.
- [ ] `WP03-011` Implement `GeometryRevision` and `MeshRevision` schemas.
- [ ] `WP03-012` Implement `MaterialAssignment` and `ProcessPlan` schemas.
- [ ] `WP03-013` Implement `SimulationRun` and solver-log schemas.
- [ ] `WP03-014` Implement `EvidenceRecord` and `PromotionDecision` schemas.
- [ ] `WP03-015` Implement `LifecycleState`, `InspectionEvent`, `RepairEvent`, and `DispositionEvent` schemas.
- [ ] `WP03-016` Implement `ObjectiveVector` and uncertainty result schemas.
- [ ] `WP03-017` Implement `Passport` bundle and component ancestry schema.
- [ ] `WP03-018` Implement schema migrations with loss checks.

### Storage and Services

- [ ] `WP03-019` Select transactional metadata storage.
- [ ] `WP03-020` Select chunked field/array storage.
- [ ] `WP03-021` Implement content-addressed artifact storage.
- [ ] `WP03-022` Implement the append-only evidence ledger.
- [ ] `WP03-023` Implement run manifests with source, dependencies, hardware, seed, inputs, commands, outputs, and exit status.
- [ ] `WP03-024` Implement dependency invalidation rules.
- [ ] `WP03-025` Implement artifact comparison by topology, geometry, mesh, material, process, mission, and solver changes.
- [ ] `WP03-026` Implement backup, restore, and integrity audit commands.
- [ ] `WP03-027` Implement signed approval records tied to exact artifact identities.
- [ ] `WP03-028` Implement export/import for portable passport bundles.

### Verification

- [ ] `WP03-029` Test canonical hashing across supported platforms.
- [ ] `WP03-030` Test that one-bit artifact changes produce new identities.
- [ ] `WP03-031` Test interrupted writes and transaction recovery.
- [ ] `WP03-032` Test corrupted artifact detection.
- [ ] `WP03-033` Test that changed inputs invalidate all dependent results and no unrelated results.
- [ ] `WP03-034` Test supersession while retaining historical records.
- [ ] `WP03-035` Test passport branch, component replacement, reuse, and merge semantics.
- [ ] `WP03-036` Test clean export/import and signature verification.
- [ ] `WP03-037` Execute a disaster-recovery exercise from backup.

## Required Artifacts

- schemas and migrations;
- storage implementation;
- run manifest;
- evidence ledger;
- invalidation graph;
- passport bundle;
- integrity and recovery reports.

## Local Gate WP03-G

**PASS** when any objective can be traced to immutable inputs and evidence, input changes invalidate correctly, corrupted artifacts are detected, backup restoration succeeds, and passport history cannot be silently rewritten.

**FAIL** when identity depends on filenames, measured and simulated values are indistinguishable, stale results survive changes, historical evidence is overwritten, or recovery cannot reconstruct the approved state.

---

# Work Package 4 — Spatial Functional Field and Geometry Kernel

## Objective

Implement the canonical AE3PT graph, spatial functional field, geometry, accessibility, and mesh-mapping representation.

## Entry Criteria

- WP02-G and WP03-G passed;
- coordinate, units, and identity conventions frozen.

## Micro-Steps

### Research and Representation

- [ ] `WP04-001` Compare voxel, octree, signed-distance, boundary-representation, graph, and hybrid geometry approaches.
- [ ] `WP04-002` Benchmark available meshing and geometry libraries against thin walls, channels, branches, and non-manifold failure cases.
- [ ] `WP04-003` Define which functional-field channels are authored and which are derived.
- [ ] `WP04-004` Define categorical, continuous, vector, tensor, probabilistic, and history field types.
- [ ] `WP04-005` Define interpolation, resampling, and conservation rules.
- [ ] `WP04-006` Define graph-to-field, field-to-geometry, and geometry-to-mesh mappings.
- [ ] `WP04-007` Define persistent identities for nodes, edges, ports, subregions, interfaces, and repair zones.

### Core Implementation

- [ ] `WP04-008` Implement `TopologyGraph` with typed nodes, edges, ports, roles, and constraints.
- [ ] `WP04-009` Implement `FunctionalField` with adaptive spatial storage.
- [ ] `WP04-010` Implement sparse voxel or octree indexing.
- [ ] `WP04-011` Implement signed-distance or equivalent implicit geometry operations.
- [ ] `WP04-012` Implement graph-edge sweeps and transitions.
- [ ] `WP04-013` Implement shell, hollow, channel, taper, offset, union, intersection, subtraction, and keep-out operations.
- [ ] `WP04-014` Implement fillet or smooth-transition generation suitable for field and manufacturing analysis.
- [ ] `WP04-015` Implement material and interface assignment.
- [ ] `WP04-016` Implement electrical, coolant, mounting, sensor, repair-electrode, inspection, split-line, and fastener ports.
- [ ] `WP04-017` Implement geometry revisions without mutating parent designs.

### Geometry Queries

- [ ] `WP04-018` Implement connected-component and terminal-connectivity queries.
- [ ] `WP04-019` Implement local thickness and minimum-neck queries.
- [ ] `WP04-020` Implement curvature, branch angle, and transition-gradient queries.
- [ ] `WP04-021` Implement distance-to-exterior and geodesic access queries.
- [ ] `WP04-022` Implement trapped-volume and drain-path detection.
- [ ] `WP04-023` Implement seed-continuity and plating-path queries.
- [ ] `WP04-024` Implement inspection and repair-tool access queries.
- [ ] `WP04-025` Implement disassembly boundary and recoverable-subassembly queries.
- [ ] `WP04-026` Implement coolant inlet-to-outlet path and dead-end classification.

### Meshing and Mapping

- [ ] `WP04-027` Implement surface and volume mesh adapters.
- [ ] `WP04-028` Implement mesh-quality metrics and rejection.
- [ ] `WP04-029` Implement local refinement around terminals, thin walls, corners, interfaces, and high-gradient estimates.
- [ ] `WP04-030` Preserve graph/field identities on mesh entities.
- [ ] `WP04-031` Map solver fields back to graph, functional field, and geometry.
- [ ] `WP04-032` Implement remeshing comparison and field-transfer error reporting.

### Verification

- [ ] `WP04-033` Create canonical bar, taper, branch, hollow tube, channel, lattice, repair window, and separable-joint fixtures.
- [ ] `WP04-034` Test volume, area, length, thickness, and connectivity against analytic values.
- [ ] `WP04-035` Test coordinate transforms and unit changes.
- [ ] `WP04-036` Test graph-field-geometry round trips within declared tolerance.
- [ ] `WP04-037` Test intentional invalid geometries and verify rejection reasons.
- [ ] `WP04-038` Test identity preservation across refinement and remeshing.
- [ ] `WP04-039` Test field conservation during resampling.
- [ ] `WP04-040` Benchmark memory and time for representative candidate populations.

## Required Artifacts

- topology and functional-field APIs;
- geometry kernel;
- query library;
- mesh adapters;
- canonical geometry fixtures;
- geometry verification report;
- performance baseline.

## Local Gate WP04-G

**PASS** when the kernel represents every demonstrator's foundational geometry, rejects invalid topology and access conditions, preserves identity across mesh operations, and meets analytic geometry and mapping tolerances.

**FAIL** when solver results cannot map back to design variables, access or trapped volumes cannot be evaluated, meshing loses topology identity, or authored data are overwritten by derived geometry.

---

# Work Package 5 — Material, Interface, Process, and Recovered-Component Library

## Objective

Create versioned property records with uncertainty and evidence for all bulk materials, interfaces, process-conditioned states, coolants, insulation, and recovered components.

## Entry Criteria

- WP03-G passed;
- unit and provenance systems available;
- initial material scope approved.

## Micro-Steps

### Research

- [ ] `WP05-001` Define the initial material list for Busbar v1.
- [ ] `WP05-002` Define the expanded lists for repair, hollow conductor, and winding stages.
- [ ] `WP05-003` Collect primary or official sources for electrical, thermal, mechanical, magnetic, chemical, and lifecycle properties.
- [ ] `WP05-004` Identify property dependence on temperature, frequency, strain rate, processing, orientation, ageing, and repair.
- [ ] `WP05-005` Research seed-to-substrate, copper-to-seed, coating, insulation, coolant, adhesive, and fastener interfaces.
- [ ] `WP05-006` Research electroformed copper porosity, roughness, residual stress, adhesion, and fatigue behavior.
- [ ] `WP05-007` Research recycled and recovered material property variation.
- [ ] `WP05-008` Research component screening methods for bearings, connectors, magnets, sensors, and semiconductors.
- [ ] `WP05-009` Define evidence tiers and out-of-domain policy.

### Schema and Database

- [ ] `WP05-010` Implement bulk material identity and condition schema.
- [ ] `WP05-011` Implement scalar, curve, surface, tensor, and probabilistic property models.
- [ ] `WP05-012` Implement validity ranges and extrapolation prohibition by default.
- [ ] `WP05-013` Implement interface-property records.
- [ ] `WP05-014` Implement process-conditioned material states.
- [ ] `WP05-015` Implement corrosion, electromigration, fatigue, and insulation-ageing parameter records.
- [ ] `WP05-016` Implement plating compatibility and galvanic-risk rules.
- [ ] `WP05-017` Implement coolant compatibility and contamination rules.
- [ ] `WP05-018` Implement printability, finishing, repair, and separation-method fields.
- [ ] `WP05-019` Implement cost, region, date, recycled fraction, supply risk, and energy fields.
- [ ] `WP05-020` Implement recovered-component identity, test history, grade, derating, and remaining-life fields.

### Initial Records

- [ ] `WP05-021` Create copper records for wrought, plated, electroformed, repaired, and recycled conditions.
- [ ] `WP05-022` Create aluminium, nickel, steel, and selected magnetic-material records.
- [ ] `WP05-023` Create selected printable polymer and recycled-polymer records.
- [ ] `WP05-024` Create insulation and ceramic records.
- [ ] `WP05-025` Create seed, activation, adhesion, and finishing process-interface records.
- [ ] `WP05-026` Create selected coolant records.
- [ ] `WP05-027` Create air, water, electrolyte, and environmental boundary-fluid records.
- [ ] `WP05-028` Create placeholder recovered-component records that fail closed until inspection data exist.

### Verification and Calibration

- [ ] `WP05-029` Test units, interpolation, monotonicity where physically required, and range behavior.
- [ ] `WP05-030` Compare selected handbook/literature values with internal coupons.
- [ ] `WP05-031` Record raw measurements and calibration without replacing source data.
- [ ] `WP05-032` Test solver refusal outside property domains.
- [ ] `WP05-033` Test compatibility rules using known compatible and incompatible pairs.
- [ ] `WP05-034` Test cost and supply records for date and region qualification.
- [ ] `WP05-035` Conduct independent review of all properties used in Gate G3.

## Required Artifacts

- material and interface schemas;
- initial database;
- compatibility rules;
- evidence and uncertainty records;
- coupon-property plan;
- property verification report.

## Local Gate WP05-G

**PASS** when every solver and cost input used by the digital busbar has a versioned, unit-safe, evidence-tiered record with uncertainty and valid range, and unsupported extrapolation fails closed.

**FAIL** when a solver uses an untraceable constant, interface behavior is silently treated as bulk behavior, cost lacks date/region context, or recovered components receive favorable properties without inspection evidence.

---

# Work Package 6 — Topology Grammar and Candidate Generation

## Objective

Generate diverse, reproducible, multifunctional, and initially feasible electrical topologies from mission ports and spatial constraints.

## Entry Criteria

- WP02-G, WP04-G, and WP05-G passed;
- Busbar Mission v1 and process profile selected.

## Micro-Steps

### Research and Search-Space Design

- [ ] `WP06-001` Review graph, density, level-set, implicit, lattice, generative, and grammar-based topology methods.
- [ ] `WP06-002` Reproduce the selected busbar topology-optimization reference case.
- [ ] `WP06-003` Identify which variables are discrete, continuous, categorical, conditional, and derived.
- [ ] `WP06-004` Define protected terminals, keep-outs, mounts, cooling ports, repair zones, and manufacturing directions.
- [ ] `WP06-005` Define topology-family descriptors for diversity measurement.
- [ ] `WP06-006` Define constraints that must be preserved during every mutation.
- [ ] `WP06-007` Define repair-aware and failure-aware topology operators.
- [ ] `WP06-008` Define deterministic random-seed and lineage requirements.

### Grammar and Candidate Representation

- [ ] `WP06-009` Specify terminal-to-terminal conductor seed rules.
- [ ] `WP06-010` Specify branch, merge, parallel path, loop, bypass, and modular split rules.
- [ ] `WP06-011` Specify taper, thickening, thinning, shelling, hollowing, and local reinforcement rules.
- [ ] `WP06-012` Specify coolant-channel and manifold rules.
- [ ] `WP06-013` Specify structural-rib and mount-integration rules.
- [ ] `WP06-014` Specify repair window, inspection port, electrode port, replaceable insert, and sacrificial segment rules.
- [ ] `WP06-015` Specify material substitution and interface rules.
- [ ] `WP06-016` Specify redundant-path and fault-isolation rules.
- [ ] `WP06-017` Implement a normalized candidate encoding.
- [ ] `WP06-018` Implement lineage records with parents, operator, parameters, seed, and rejection history.

### Generators and Operators

- [ ] `WP06-019` Implement deterministic baseline seed generators.
- [ ] `WP06-020` Implement edge split, merge, move, reroute, add, and remove mutations.
- [ ] `WP06-021` Implement thickness, taper, and cross-section mutations.
- [ ] `WP06-022` Implement hollowing and channel mutations.
- [ ] `WP06-023` Implement repair-access and modularity mutations.
- [ ] `WP06-024` Implement redundancy and degraded-operation mutations.
- [ ] `WP06-025` Implement compatible-material and process mutations.
- [ ] `WP06-026` Implement crossover only after lineage and feasibility behavior are verified.
- [ ] `WP06-027` Implement mutation magnitude control and rollback.
- [ ] `WP06-028` Implement novelty metrics across graph, geometry, material, process, and repair strategy.

### Fast Feasibility Screening

- [ ] `WP06-029` Reject disconnected electrical networks.
- [ ] `WP06-030` Reject keep-out and boundary violations.
- [ ] `WP06-031` Reject minimum-thickness, minimum-gap, and minimum-radius violations.
- [ ] `WP06-032` Reject sealed plating or cleaning cavities.
- [ ] `WP06-033` Reject missing seed continuity.
- [ ] `WP06-034` Reject inaccessible required inspection or repair regions.
- [ ] `WP06-035` Reject impossible assembly and disassembly sequences.
- [ ] `WP06-036` Reject singular coolant paths and unclassified dead ends.
- [ ] `WP06-037` Emit one or more stable reason codes for every rejection.

### Verification and Performance

- [ ] `WP06-038` Freeze reference populations for fixed seeds.
- [ ] `WP06-039` Verify exact replay of candidate identities and lineage.
- [ ] `WP06-040` Property-test that every accepted mutation preserves declared invariants.
- [ ] `WP06-041` Measure rejection-stage precision using hand-classified fixtures.
- [ ] `WP06-042` Verify that invalid candidates do not reach physics queues.
- [ ] `WP06-043` Measure population diversity and collapse behavior.
- [ ] `WP06-044` Benchmark candidate generation rate and memory use.
- [ ] `WP06-045` Review whether the search space contains the conventional reference and known good variants.

## Required Artifacts

- topology grammar specification;
- candidate encoding and lineage schema;
- mutation library;
- fast feasibility screen;
- frozen populations;
- diversity and performance report.

## Local Gate WP06-G

**PASS** when fixed seeds reproduce the same populations, accepted mutations preserve all declared invariants, invalid candidates are rejected with reason codes, and the population includes solid, branched, hollow, redundant, modular, and repairable busbar families.

**FAIL** when lineage cannot be replayed, infeasible geometry reaches expensive simulation, diversity collapses without detection, or repair/reuse variables are absent from the generative representation.

---

# Work Package 7 — Reduced-Order Electrical Engine

## Objective

Create Level 0 and Level 1 electrical models that are fast enough for broad search and accurate enough to preserve useful candidate ranking within a declared domain.

## Entry Criteria

- WP02-G, WP04-G, WP05-G, and WP06-G passed;
- analytic fixture set approved.

## Micro-Steps

### Research and Formulation

- [ ] `WP07-001` Review graph resistance, transmission-line, partial-element, distributed conductor, and reduced electrothermal formulations.
- [ ] `WP07-002` Reproduce analytic and published busbar resistance cases.
- [ ] `WP07-003` Define when DC assumptions are valid and when AC promotion is mandatory.
- [ ] `WP07-004` Define contact and joint model families.
- [ ] `WP07-005` Define current-density proxy and bottleneck metrics.
- [ ] `WP07-006` Define conductor-utility sensitivity and its limitations.
- [ ] `WP07-007` Define failure injection at node, edge, joint, and local-thinning levels.

### Level 0 Implementation

- [ ] `WP07-008` Assemble graph conductance matrices from geometry and material records.
- [ ] `WP07-009` Implement voltage, branch-current, power-loss, and equivalent-resistance solution.
- [ ] `WP07-010` Implement fixed-voltage, fixed-current, mixed terminal, and load boundary conditions.
- [ ] `WP07-011` Implement series, parallel, branch, bridge, and multi-terminal networks.
- [ ] `WP07-012` Implement contact resistance and uncertainty.
- [ ] `WP07-013` Implement temperature-dependent segment resistivity.
- [ ] `WP07-014` Implement current and power conservation diagnostics.
- [ ] `WP07-015` Implement singular-network and floating-node diagnostics.

### Level 1 Implementation

- [ ] `WP07-016` Discretize edges into distributed one-dimensional segments.
- [ ] `WP07-017` Derive local effective cross-section from geometry and plating thickness.
- [ ] `WP07-018` Implement tapered and nonuniform segments.
- [ ] `WP07-019` Implement simple transient electrical behavior required by the mission.
- [ ] `WP07-020` Implement optional reduced inductive terms where validated.
- [ ] `WP07-021` Implement local loss and current-density proxy outputs.
- [ ] `WP07-022` Implement current crowding risk indicators at transitions.
- [ ] `WP07-023` Implement mission aggregation across continuous, peak, fault, and degraded scenarios.

### Sensitivity and Faults

- [ ] `WP07-024` Implement finite-difference conductor-utility sensitivity.
- [ ] `WP07-025` Verify sensitivity against analytic derivatives for simple bars.
- [ ] `WP07-026` Implement edge add/remove and thickness perturbation evaluation.
- [ ] `WP07-027` Implement open-circuit, resistance increase, thinning, and bypass faults.
- [ ] `WP07-028` Compute degraded power and survivability proxies.
- [ ] `WP07-029` Expose sensitivity and fault outputs to the topology generator.

### Verification and Benchmarking

- [ ] `WP07-030` Verify uniform bar, tapered bar, series, parallel, bridge, and multi-terminal cases.
- [ ] `WP07-031` Verify temperature coefficient behavior.
- [ ] `WP07-032` Verify contact-resistance fixtures.
- [ ] `WP07-033` Verify current and energy conservation thresholds.
- [ ] `WP07-034` Compare Level 0 and Level 1 on frozen candidates.
- [ ] `WP07-035` Compare both levels with 3D reference results when WP08 becomes available.
- [ ] `WP07-036` Quantify ranking correlation and identify failure domains.
- [ ] `WP07-037` Benchmark throughput for target population sizes.
- [ ] `WP07-038` Verify that out-of-domain cases trigger promotion or rejection.

## Required Artifacts

- Level 0 solver;
- Level 1 solver;
- contact and fault models;
- sensitivity API;
- analytic fixtures;
- ranking and performance report.

## Local Gate WP07-G

**PASS** when analytic error, conservation, deterministic replay, and performance thresholds pass, and the reduced models preserve candidate ranking sufficiently for pre-approved busbar geometry families.

**FAIL** when the solver hides singular networks, violates conservation, uses invalid property ranges, or mis-ranks important candidate families without triggering higher-fidelity promotion.

---

# Work Package 8 — Three-Dimensional Electrical and Electromagnetic Engines

## Objective

Provide verified reference models for three-dimensional conduction, current crowding, AC effects, inductance, eddy currents, force, torque, and back EMF.

## Entry Criteria

- WP03-G through WP07-G passed as applicable;
- solver licensing and reproducibility approach approved;
- mesh mapping available.

## Micro-Steps

### Solver Research and Selection

- [ ] `WP08-001` Compare candidate internal and external FEM/EM solvers for formulations, automation, licensing, meshing, restart, and result export.
- [ ] `WP08-002` Reproduce canonical conduction benchmarks in at least two independent formulations or tools.
- [ ] `WP08-003` Define quasistatic DC, frequency-domain, and transient EM validity domains.
- [ ] `WP08-004` Define terminal, symmetry, periodic, insulation, and far-field boundary-condition semantics.
- [ ] `WP08-005` Define mesh-order and element-family policy.
- [ ] `WP08-006` Define solver convergence and non-convergence evidence requirements.

### 3D Conduction

- [ ] `WP08-007` Implement geometry and material export adapter.
- [ ] `WP08-008` Implement terminal and contact boundary export.
- [ ] `WP08-009` Implement steady conduction solve.
- [ ] `WP08-010` Import voltage, current density, electric field, and loss density.
- [ ] `WP08-011` Map results to geometry, graph, and functional-field identities.
- [ ] `WP08-012` Implement material and thickness inhomogeneity from as-built plating maps.
- [ ] `WP08-013` Implement damaged-region conductivity changes.
- [ ] `WP08-014` Implement current and power conservation reports.

### AC and Electromagnetic Capability

- [ ] `WP08-015` Implement frequency-domain conductor solves.
- [ ] `WP08-016` Resolve skin and proximity effects across the mission frequency set.
- [ ] `WP08-017` Implement self and mutual inductance extraction.
- [ ] `WP08-018` Implement eddy-current loss where required.
- [ ] `WP08-019` Implement magnetic vector-potential formulation for the winding demonstrator.
- [ ] `WP08-020` Implement periodic rotor/stator or equivalent machine boundary handling.
- [ ] `WP08-021` Compute flux linkage, back EMF, torque, harmonic content, and force density.
- [ ] `WP08-022` Transfer force and loss fields to structural and thermal engines.

### Meshing and Numerical Quality

- [ ] `WP08-023` Implement geometry-based initial mesh sizing.
- [ ] `WP08-024` Refine terminals, corners, thin plating, gaps, interfaces, and expected skin-depth regions.
- [ ] `WP08-025` Execute h- or p-refinement studies for gate-critical cases.
- [ ] `WP08-026` Estimate discretization error.
- [ ] `WP08-027` Detect poor elements, disconnected domains, and boundary leakage.
- [ ] `WP08-028` Record solver residuals, iteration counts, warnings, and license/runtime failures.

### Verification and Cross-Checks

- [ ] `WP08-029` Verify uniform 3D bar resistance.
- [ ] `WP08-030` Verify current crowding in a known transition geometry.
- [ ] `WP08-031` Verify inductance against analytic or trusted benchmark cases.
- [ ] `WP08-032` Verify skin-effect trends against analytic solutions.
- [ ] `WP08-033` Verify force, torque, and back EMF on canonical machine cases before using generated windings.
- [ ] `WP08-034` Compare independent solvers or formulations on finalist cases.
- [ ] `WP08-035` Compare Level 0/1 and Level 2/3 results; build discrepancy records.
- [ ] `WP08-036` Freeze benchmark meshes and results with versioned tolerances.

## Required Artifacts

- solver-selection report;
- adapters and field mappings;
- benchmark suite;
- mesh-convergence reports;
- reduced/reference discrepancy records;
- EM verification report.

## Local Gate WP08-G

**PASS** when 3D conduction, AC, and applicable EM benchmarks pass, finalist meshes meet convergence criteria, conservation holds, and reduced-model disagreement is quantified rather than hidden.

**FAIL** when solver warnings are ignored, mesh refinement changes gate-critical outputs beyond tolerance, boundary conditions are untraceable, or winding results are used before canonical machine verification.

---

# Work Package 9 — Thermal and Coolant-Flow Engines

## Objective

Predict steady and transient temperature, heat flow, coolant distribution, pressure drop, pump burden, and cooling failure using accepted electrical loss histories.

## Entry Criteria

- WP02-G through WP05-G passed;
- WP07-G passed for reduced work;
- WP08-G passed before high-fidelity electrothermal promotion.

## Micro-Steps

### Research and Model Hierarchy

- [ ] `WP09-001` Review lumped thermal, 1D conjugate, 3D conduction, coolant-network, and CFD models for conductors and windings.
- [ ] `WP09-002` Identify dominant contact, convection, radiation, and coolant uncertainties for each demonstrator.
- [ ] `WP09-003` Reproduce canonical transient conduction and internal-flow heat-transfer cases.
- [ ] `WP09-004` Define laminar, transitional, turbulent, compressible, boiling, and cavitation scope.
- [ ] `WP09-005` Define promotion triggers from reduced flow to CFD.
- [ ] `WP09-006` Define pump-energy and system-boundary treatment.

### Reduced Thermal Engine

- [ ] `WP09-007` Implement thermal nodes, masses, conductances, and boundaries aligned to topology.
- [ ] `WP09-008` Implement Joule-loss import from accepted electrical states.
- [ ] `WP09-009` Implement temperature-dependent material properties.
- [ ] `WP09-010` Implement contact thermal resistance with uncertainty.
- [ ] `WP09-011` Implement steady-state solve.
- [ ] `WP09-012` Implement transient integration for mission profiles.
- [ ] `WP09-013` Implement thermal limit, time-above-limit, and hotspot outputs.
- [ ] `WP09-014` Implement heat-to-ambient and mounting-interface models.

### Coolant Network

- [ ] `WP09-015` Implement channel geometry extraction.
- [ ] `WP09-016` Implement pressure-drop and local-loss models.
- [ ] `WP09-017` Implement branched flow distribution.
- [ ] `WP09-018` Implement convective heat-transfer correlations within approved ranges.
- [ ] `WP09-019` Implement coolant property dependence on temperature and concentration.
- [ ] `WP09-020` Implement pump power and control assumptions.
- [ ] `WP09-021` Implement blockage, leakage, reduced-flow, and loss-of-pump scenarios.
- [ ] `WP09-022` Implement coolant residence and drainability outputs for maintenance.

### 3D Thermal and CFD Adapters

- [ ] `WP09-023` Implement 3D conduction mesh/material/boundary export.
- [ ] `WP09-024` Import temperature, heat flux, and thermal-gradient fields.
- [ ] `WP09-025` Implement CFD geometry, inlet, outlet, wall, and conjugate heat-transfer export.
- [ ] `WP09-026` Import velocity, pressure, turbulence, temperature, and wall heat-transfer fields.
- [ ] `WP09-027` Map results back to functional-field and topology identities.
- [ ] `WP09-028` Implement mesh independence and energy-balance reports.

### Electrothermal Coupling

- [ ] `WP09-029` Implement one-way electrical-to-thermal coupling.
- [ ] `WP09-030` Implement two-way resistivity-temperature iteration.
- [ ] `WP09-031` Define convergence, relaxation, oscillation, and fallback behavior.
- [ ] `WP09-032` Ensure only accepted BAB-CS histories drive authoritative transients.
- [ ] `WP09-033` Transfer temperature histories to structural and ageing engines.

### Verification and Calibration

- [ ] `WP09-034` Verify analytic steady conduction cases.
- [ ] `WP09-035` Verify analytic transient cases.
- [ ] `WP09-036` Verify pipe-flow pressure drop and heat-transfer cases.
- [ ] `WP09-037` Verify energy conservation.
- [ ] `WP09-038` Compare reduced and 3D thermal results.
- [ ] `WP09-039` Compare coolant network and CFD results.
- [ ] `WP09-040` Calibrate contact and convection uncertainties using dedicated fixtures.
- [ ] `WP09-041` Validate busbar hotspot and transient cooling behavior.
- [ ] `WP09-042` Publish invalid domains and promotion triggers.

## Required Artifacts

- reduced thermal solver;
- coolant network;
- 3D thermal and CFD adapters;
- coupling driver;
- analytic and physical calibration fixtures;
- uncertainty and validation report.

## Local Gate WP09-G

**PASS** when analytic, conservation, convergence, and busbar temperature thresholds pass, cooling system burdens are included, and loss-of-cooling cases are explicitly evaluated.

**FAIL** when heat sources do not come from accepted electrical states, uncertain boundaries are hidden, pump energy is omitted, or CFD results are promoted without mesh and balance evidence.

---

# Work Package 10 — Mechanical, Pressure, Vibration, and Fatigue Engine

## Objective

Verify that initial, manufactured, damaged, and repaired designs survive mechanical loads throughout the mission and maintenance lifecycle.

## Entry Criteria

- WP04-G and WP05-G passed;
- applicable thermal and electromagnetic load interfaces defined;
- mechanical material and interface data available.

## Micro-Steps

### Research and Failure Modes

- [ ] `WP10-001` Review electroformed copper and printed-substrate mechanical-property evidence.
- [ ] `WP10-002` Review pressure-wall, vibration, terminal-fatigue, thermal-strain, electromagnetic-force, and rotating-load methods.
- [ ] `WP10-003` Research repaired-layer adhesion and fatigue knockdown evidence.
- [ ] `WP10-004` Define plausible defect fields: thickness variation, porosity, notch, delamination, residual stress, and misalignment.
- [ ] `WP10-005` Define proof, burst, fatigue, vibration, and rotating-test requirements by demonstrator.
- [ ] `WP10-006` Define allowable-stress and life-factor policy with standards review.

### Reduced Structural Models

- [ ] `WP10-007` Implement beam and shell extraction from graph/field geometry.
- [ ] `WP10-008` Implement mount, terminal, pressure, thermal, acceleration, and distributed-force loads.
- [ ] `WP10-009` Implement linear static screening.
- [ ] `WP10-010` Implement buckling screening where applicable.
- [ ] `WP10-011` Implement simple modal screening.
- [ ] `WP10-012` Implement stress and deformation constraints.
- [ ] `WP10-013` Implement pressure-wall minimum-thickness checks.
- [ ] `WP10-014` Implement cumulative fatigue screening.

### 3D Structural Capability

- [ ] `WP10-015` Implement structural solver geometry and mesh adapter.
- [ ] `WP10-016` Import temperature fields and compute thermal strain.
- [ ] `WP10-017` Import electromagnetic force fields.
- [ ] `WP10-018` Implement pressure, mount, centrifugal, handling, and assembly loads.
- [ ] `WP10-019` Implement contact and interface behavior at joints.
- [ ] `WP10-020` Implement modal and harmonic response.
- [ ] `WP10-021` Implement fatigue damage accumulation.
- [ ] `WP10-022` Implement repaired-region material and interface states.
- [ ] `WP10-023` Implement geometric imperfection and thickness-field sampling.
- [ ] `WP10-024` Map stress, strain, displacement, modes, and life back to topology identities.

### Verification and Physical Tests

- [ ] `WP10-025` Verify beams, plates, shells, cylinders, pressure tubes, and thermal-expansion fixtures.
- [ ] `WP10-026` Execute mesh refinement on critical stress locations.
- [ ] `WP10-027` Verify modal frequencies against analytic or measured fixtures.
- [ ] `WP10-028` Verify load transfer from EM and thermal engines.
- [ ] `WP10-029` Design tensile, adhesion, pressure, fatigue, and vibration coupons.
- [ ] `WP10-030` Measure as-manufactured thickness and defect state before tests.
- [ ] `WP10-031` Calibrate uncertain process-conditioned properties without erasing residuals.
- [ ] `WP10-032` Validate hollow-conductor proof-pressure and deformation predictions.
- [ ] `WP10-033` Validate terminal and winding vibration behavior.
- [ ] `WP10-034` Verify repaired specimens re-pass applicable mechanical constraints.

## Required Artifacts

- reduced and 3D structural models;
- load-transfer contracts;
- fatigue and defect models;
- mechanical test protocols;
- calibration and validation datasets;
- structural acceptance report.

## Local Gate WP10-G

**PASS** when canonical mechanics cases pass, critical meshes converge, process-conditioned uncertainty is included, and each physical demonstrator meets its pre-approved stress, pressure, deformation, vibration, and life requirements.

**FAIL** when nominal bulk properties substitute for unverified electroformed or repaired behavior, peak stress remains mesh-dependent, proof pressure fails, or thermal/EM loads are omitted.

---

# Work Package 11 — Additive Manufacturing, Access, Cleaning, and Printability Engine

## Objective

Determine whether each generated substrate, core, support, channel, access feature, and assembly can be manufactured, cleaned, seeded, plated, inspected, repaired, and disassembled by the selected route.

## Entry Criteria

- WP04-G through WP06-G passed;
- candidate manufacturing processes and local equipment identified;
- physical trials remain under WP01 safety holds.

## Micro-Steps

### Process Research

- [ ] `WP11-001` Compare material extrusion, vat photopolymerization, powder-based, sacrificial-core, machining, and hybrid routes for each demonstrator.
- [ ] `WP11-002` Review ISO/ASTM 52910 and 52920 requirements against the planned process.
- [ ] `WP11-003` Collect printer envelope, resolution, wall, gap, overhang, support, shrinkage, surface, and repeatability data.
- [ ] `WP11-004` Research conductive-seed application, activation, masking, cleaning, and finishing access requirements.
- [ ] `WP11-005` Research trapped resin, powder, support, electrolyte, gas, rinse, and coolant failure modes.
- [ ] `WP11-006` Define process-capability coupons and measurement methods.
- [ ] `WP11-007` Define when supplier data require internal confirmation.

### Process Profiles

- [ ] `WP11-008` Implement process-profile schema with machine, material, orientation, parameters, and capability distributions.
- [ ] `WP11-009` Encode minimum wall, channel, gap, radius, overhang, unsupported span, aspect ratio, and build-envelope constraints.
- [ ] `WP11-010` Encode support-generation and support-removal constraints.
- [ ] `WP11-011` Encode tool, nozzle, brush, spray, probe, camera, electrode, and fixture access envelopes.
- [ ] `WP11-012` Encode drain, vent, purge, and rinse requirements.
- [ ] `WP11-013` Encode dimensional allowance, shrinkage, warpage, and roughness distributions.
- [ ] `WP11-014` Encode post-processing, machining, sealing, and insulation operations.
- [ ] `WP11-015` Encode witness-coupon and traceability requirements.

### Feasibility Analysis

- [ ] `WP11-016` Implement local wall, gap, radius, and overhang checks.
- [ ] `WP11-017` Implement build-envelope and orientation checks.
- [ ] `WP11-018` Implement support volume and removal-path analysis.
- [ ] `WP11-019` Implement trapped-volume detection for each process fluid or loose material.
- [ ] `WP11-020` Implement drain and vent path analysis.
- [ ] `WP11-021` Implement seed and activation access analysis.
- [ ] `WP11-022` Implement electrolyte, gas, rinse, and drying access analysis.
- [ ] `WP11-023` Implement inspection probe and repair tool access analysis.
- [ ] `WP11-024` Implement assembly and disassembly access checks.
- [ ] `WP11-025` Implement feasibility classes F0-F5 with stable reason codes.

### Process-Aware Geometry Changes

- [ ] `WP11-026` Generate drain and vent ports.
- [ ] `WP11-027` Generate temporary supports and sacrificial cores without overwriting authored geometry.
- [ ] `WP11-028` Generate machining allowances and datum features.
- [ ] `WP11-029` Generate electrode, rinse, inspection, and repair access features.
- [ ] `WP11-030` Generate witness coupons linked to the candidate process plan.
- [ ] `WP11-031` Generate orientation and fixture recommendations.
- [ ] `WP11-032` Re-run all geometry and physics invalidation after process-driven changes.

### Cost, Yield, and Validation

- [ ] `WP11-033` Estimate build time, support material, finishing time, labor, energy, and machine occupancy.
- [ ] `WP11-034` Estimate process yield and rework probability from capability data.
- [ ] `WP11-035` Print capability coupons across feature sizes and orientations.
- [ ] `WP11-036` Measure dimensions, roughness, trapped material, support-removal success, and cleaning success.
- [ ] `WP11-037` Compare predicted and observed feasibility classes.
- [ ] `WP11-038` Update process profiles while preserving original predictions.
- [ ] `WP11-039` Validate candidate process plans through dry-run traveler reviews.
- [ ] `WP11-040` Obtain manufacturing-lead approval before releasing geometry to physical build.

## Required Artifacts

- process profiles;
- feasibility and access engine;
- process-aware geometry generator;
- capability coupons and measurements;
- yield/cost model inputs;
- approved process travelers.

## Local Gate WP11-G

**PASS** when known impossible fixtures fail with correct reasons, accepted fixtures are manufactured and cleaned successfully, process variation is quantified, and every candidate sent to plating has verified seed, electrolyte, gas, rinse, drying, inspection, and repair access.

**FAIL** when a candidate contains trapped process material, inaccessible surfaces, unsupported features, unverified minimum dimensions, or requires undocumented manual intervention.

---

# Work Package 12 — Electroplating and Electroforming Process Simulator

## Objective

Predict and optimize deposited thickness, mass, current distribution, transport limitations, defects, and geometry evolution for initial manufacture and repair.

## Entry Criteria

- G0 and G1 passed;
- WP04-G, WP05-G, and WP11-G passed;
- plating laboratory safety hold released before wet experiments;
- approved chemistry and waste route available.

## Micro-Steps

### Research and Model Selection

- [ ] `WP12-001` Reproduce Faraday-law mass predictions for controlled simple cells.
- [ ] `WP12-002` Reproduce at least one published 3D copper-deposition distribution case.
- [ ] `WP12-003` Review primary, secondary, and tertiary current-distribution models.
- [ ] `WP12-004` Review mass-transport, throwing-power, current-efficiency, pulse-plating, and moving-boundary methods.
- [ ] `WP12-005` Review internal-channel, recess, lattice, blind-feature, and repair-plating studies.
- [ ] `WP12-006` Identify chemistry-specific parameters that cannot be transferred from other baths.
- [ ] `WP12-007` Define Level 0, Level 1, and Level 2 plating models and promotion rules.
- [ ] `WP12-008` Define defect outputs: underplate, overgrowth, closure, porosity risk, roughness proxy, stress proxy, adhesion risk, gas trap, and contamination.

### Laboratory and Measurement Readiness

- [ ] `WP12-009` Approve bath chemistry, operating window, ventilation, electrical isolation, spill response, sampling, and disposal plan.
- [ ] `WP12-010` Calibrate current, voltage, mass, temperature, flow, conductivity, pH, and timing instruments.
- [ ] `WP12-011` Qualify four-wire resistance measurement.
- [ ] `WP12-012` Qualify mass-gain measurement.
- [ ] `WP12-013` Qualify coating-thickness measurement using cross-section, imaging, or another approved method.
- [ ] `WP12-014` Define destructive and nondestructive measurement uncertainty budgets.
- [ ] `WP12-015` Define specimen identifiers, process travelers, bath-state sampling, and raw-data capture.
- [ ] `WP12-016` Execute a dry run with water or an approved nonhazardous surrogate where useful.

### Level 0 Process Model

- [ ] `WP12-017` Implement Faraday mass and average-thickness calculation.
- [ ] `WP12-018` Implement exposed-area and time-dependent recipe inputs.
- [ ] `WP12-019` Implement empirical throwing-power factors by geometry class.
- [ ] `WP12-020` Implement current-efficiency uncertainty.
- [ ] `WP12-021` Implement seed sheet-resistance and contact-loss approximation.
- [ ] `WP12-022` Implement entrance-crowding and long-path penalties.
- [ ] `WP12-023` Produce estimated thickness range and infeasibility flags.

### Field and Transport Models

- [ ] `WP12-024` Implement electrolyte-potential and current-density solve.
- [ ] `WP12-025` Implement electrode, auxiliary electrode, shield, and contact representations.
- [ ] `WP12-026` Implement concentration or limiting-current corrections.
- [ ] `WP12-027` Implement temperature-dependent conductivity and kinetics.
- [ ] `WP12-028` Implement simplified flow-dependent mass-transfer coefficients.
- [ ] `WP12-029` Add CFD-derived transport only after reduced transport verification.
- [ ] `WP12-030` Implement gas/wetting risk inputs from access analysis.
- [ ] `WP12-031` Implement seed discontinuity and local resistance.
- [ ] `WP12-032` Implement pulse or waveform controls if supported by evidence and equipment.

### Geometry Evolution and Inverse Design

- [ ] `WP12-033` Implement staged thickness-field updates.
- [ ] `WP12-034` Update surface geometry and local current distribution between stages.
- [ ] `WP12-035` Detect channel closure, loss of access, and unstable overgrowth.
- [ ] `WP12-036` Propagate as-manufactured geometry into electrical, thermal, structural, and cost engines.
- [ ] `WP12-037` Implement target-thickness objective.
- [ ] `WP12-038` Optimize orientation, current, time, flow, shields, and auxiliary electrodes within the validated process domain.
- [ ] `WP12-039` Generate a process recipe and expected uncertainty map.
- [ ] `WP12-040` Prohibit inverse recommendations outside equipment, chemistry, or calibration limits.

### Coupon Campaign

- [ ] `WP12-041` Design flat, edge, recess, branch, open-channel, enclosed-channel, and lattice coupons.
- [ ] `WP12-042` Include deliberately poor seed, poor flow, and gas-trap controls where safe.
- [ ] `WP12-043` Randomize or block experiments to separate geometry, current, time, flow, and bath-state effects.
- [ ] `WP12-044` Pre-register calibration and holdout coupons.
- [ ] `WP12-045` Manufacture substrates and record as-printed geometry.
- [ ] `WP12-046` Apply and verify seed continuity.
- [ ] `WP12-047` Plate under controlled travelers.
- [ ] `WP12-048` Record current/voltage/time/temperature/flow/bath history.
- [ ] `WP12-049` Clean, dry, and record process anomalies.
- [ ] `WP12-050` Measure mass, resistance, dimensions, and thickness fields.
- [ ] `WP12-051` Section selected specimens and characterize defects.
- [ ] `WP12-052` Calibrate model parameters only on the approved calibration set.
- [ ] `WP12-053` Evaluate holdout performance using frozen thresholds.
- [ ] `WP12-054` Publish residual maps and invalid geometry classes.

### Repair Plating Extension

- [ ] `WP12-055` Define aged surface, cleaning, stripping, masking, reseeding, and adjacent-material inputs.
- [ ] `WP12-056` Model local repair electrode placement and current paths.
- [ ] `WP12-057` Model dimensional restoration and overgrowth risk.
- [ ] `WP12-058` Add repaired-layer interface identity and property uncertainty.
- [ ] `WP12-059` Validate repair coupons separately from new-build coupons.

## Required Artifacts

- plating model hierarchy;
- laboratory safety release;
- instrument calibration records;
- coupon designs and travelers;
- raw and processed datasets;
- calibrated parameters and holdout report;
- inverse recipe tool;
- as-manufactured geometry pipeline;
- repair-plating extension.

## Local Gate WP12-G

**PASS** when G4 criteria pass, model predictions meet deposited-mass and thickness thresholds on holdout coupons, critical under-plating is not missed, bath/process evidence is complete, and as-manufactured geometry propagates into downstream analyses.

**FAIL** when calibration leaks into holdout data, unsafe or unrecorded process changes occur, critical underplate is missed, geometry evolution is ignored where material, or downstream solvers continue using nominal thickness after measurement.

---

# Work Package 13 — Coupled Multiphysics, Multi-Fidelity Promotion, and BAB-CS Authority

## Objective

Connect all engines through explicit contracts, invalidation, convergence, fidelity promotion, discrepancy tracking, and authoritative transient acceptance.

## Entry Criteria

- WP03-G passed;
- at least one verified model available on each side of every initial coupling;
- BAB-CS interface and authority expectations documented.

## Micro-Steps

### Coupling Research and Contracts

- [ ] `WP13-001` Inventory every cross-engine quantity, units, coordinate frame, temporal semantics, and uncertainty.
- [ ] `WP13-002` Define electrical-to-thermal loss mapping.
- [ ] `WP13-003` Define thermal-to-electrical property mapping.
- [ ] `WP13-004` Define thermal-to-structural temperature and strain mapping.
- [ ] `WP13-005` Define EM-to-structural force mapping.
- [ ] `WP13-006` Define coolant-to-structural pressure mapping.
- [ ] `WP13-007` Define process-to-geometry thickness and defect mapping.
- [ ] `WP13-008` Define damage-to-property and repair-to-property mapping.
- [ ] `WP13-009` Define mapping conservation and interpolation tolerances.

### Invalidation and State Control

- [ ] `WP13-010` Encode dependency edges among mission, geometry, mesh, material, process, solver, damage, repair, and economics.
- [ ] `WP13-011` Implement stale-result detection.
- [ ] `WP13-012` Implement automatic invalidation on dependency changes.
- [ ] `WP13-013` Require explicit new lifecycle states after damage or repair.
- [ ] `WP13-014` Prevent manual result reuse across incompatible artifacts.
- [ ] `WP13-015` Log every fallback and prohibit silent fallback.

### Coupled Solution Drivers

- [ ] `WP13-016` Implement one-way coupling orchestration.
- [ ] `WP13-017` Implement staggered electrothermal iteration.
- [ ] `WP13-018` Implement thermal-structural and EM-structural sequences.
- [ ] `WP13-019` Implement plating-geometry-electrical update sequence.
- [ ] `WP13-020` Implement damage-property-performance sequence.
- [ ] `WP13-021` Implement repair-process-requalification sequence.
- [ ] `WP13-022` Define convergence, relaxation, iteration cap, and failure status for each loop.
- [ ] `WP13-023` Implement checkpoint, restart, and partial-result retention.

### Multi-Fidelity Promotion

- [ ] `WP13-024` Define Level 0-4 capability matrix for every engine.
- [ ] `WP13-025` Define promotion triggers based on constraint margin, novelty, uncertainty, discrepancy, and Pareto value.
- [ ] `WP13-026` Define demotion or rejection for unresolvable failures.
- [ ] `WP13-027` Implement candidate queues by fidelity and resource class.
- [ ] `WP13-028` Record promotion decisions and supporting metrics.
- [ ] `WP13-029` Build discrepancy models between adjacent levels.
- [ ] `WP13-030` Include discrepancy uncertainty in lower-fidelity ranking.
- [ ] `WP13-031` Audit for systematic elimination of unusual but promising topology families.

### BAB-CS Integration

- [ ] `WP13-032` Define the BAB-CS request and response schema.
- [ ] `WP13-033` Define candidate integration inputs and constraints.
- [ ] `WP13-034` Define reference calculation selection and validity.
- [ ] `WP13-035` Define projection semantics and physical constraint set.
- [ ] `WP13-036` Define replay identity and duplicate handling.
- [ ] `WP13-037` Implement adapter error propagation and cancellation.
- [ ] `WP13-038` Store candidate, reference, projection, replay, discrepancy, and acceptance records separately.
- [ ] `WP13-039` Mark accepted histories immutable.
- [ ] `WP13-040` Reject downstream authoritative ageing or lifecycle runs that reference unaccepted histories.
- [ ] `WP13-041` Test BAB-CS behavior for nominal, stiff, discontinuous, fault, and failed-reference cases.

### Verification

- [ ] `WP13-042` Verify mapping conservation on canonical meshes.
- [ ] `WP13-043` Verify invalidation for every dependency type.
- [ ] `WP13-044` Verify coupled convergence on analytic or manufactured benchmarks.
- [ ] `WP13-045` Verify non-convergence is retained as failure evidence.
- [ ] `WP13-046` Verify checkpoint/restart equivalence.
- [ ] `WP13-047` Verify fidelity promotion replay.
- [ ] `WP13-048` Verify BAB-CS accepted-history enforcement.
- [ ] `WP13-049` Run an adversarial stale-result audit.

## Required Artifacts

- coupling contract registry;
- invalidation engine;
- coupled drivers;
- fidelity matrix and promotion policy;
- BAB-CS adapter and acceptance store;
- discrepancy models;
- convergence, restart, and stale-result reports.

## Local Gate WP13-G

**PASS** when every coupling is typed and traceable, mappings conserve required quantities, stale results cannot be consumed, non-convergence fails closed, checkpoint replay matches, and only BAB-CS-accepted histories drive authoritative transient lifecycle results.

**FAIL** when coupling relies on manual files, fallbacks are silent, results survive invalidating changes, discrepancy is ignored, or unaccepted histories influence promoted decisions.

---

# Work Package 14 — Damage, Ageing, Fault, Reliability, and Survivability

## Objective

Predict evolving damage and degraded function under mission exposure while preserving separate failure mechanisms and uncertainty.

## Entry Criteria

- WP02-G, WP03-G, WP05-G, and applicable WP07-WP13 gates passed;
- mission histories accepted by BAB-CS where required;
- damage modes prioritized by demonstrator.

## Micro-Steps

### Failure-Mode Research

- [ ] `WP14-001` Perform FMEA/FMECA for each demonstrator.
- [ ] `WP14-002` Research electromigration and current-density life models.
- [ ] `WP14-003` Research thermal-cycle and interface-fatigue models.
- [ ] `WP14-004` Research corrosion, galvanic attack, coolant contamination, and conductor thinning.
- [ ] `WP14-005` Research electroform delamination, crack, porosity, and residual-stress evolution.
- [ ] `WP14-006` Research insulation thermal, electrical, mechanical, and environmental degradation.
- [ ] `WP14-007` Research contact and joint resistance growth.
- [ ] `WP14-008` Research bearing, magnet, sensor, and semiconductor remaining-life indicators for later reuse work.
- [ ] `WP14-009` Identify accelerated-test methods and verify that acceleration does not change the mechanism.

### Damage Representation

- [ ] `WP14-010` Define separate damage-state variables by mechanism.
- [ ] `WP14-011` Define local, edge, interface, component, and assembly aggregation.
- [ ] `WP14-012` Define property degradation mappings.
- [ ] `WP14-013` Define uncertainty, correlation, and competing-risk handling.
- [ ] `WP14-014` Define failure, warning, inspection, repair, and safe-shutdown thresholds.
- [ ] `WP14-015` Define remaining-life output and confidence semantics.

### Model Implementation

- [ ] `WP14-016` Implement thermal-cycle counting and accumulation.
- [ ] `WP14-017` Implement current/temperature exposure accumulation.
- [ ] `WP14-018` Implement corrosion/thinning progression.
- [ ] `WP14-019` Implement contact-resistance drift.
- [ ] `WP14-020` Implement insulation-health progression.
- [ ] `WP14-021` Implement fatigue damage import from structural histories.
- [ ] `WP14-022` Implement repaired-interface ageing states.
- [ ] `WP14-023` Implement uncertainty propagation and remaining-life distributions.
- [ ] `WP14-024` Implement time stepping, event stepping, and maintenance resets without erasing history.

### Fault Injection and Survivability

- [ ] `WP14-025` Implement branch removal.
- [ ] `WP14-026` Implement local thinning and conductivity loss.
- [ ] `WP14-027` Implement joint resistance growth and open joint.
- [ ] `WP14-028` Implement coolant blockage, leak, and pump failure.
- [ ] `WP14-029` Implement sensor loss and misreading scenarios where controls depend on sensing.
- [ ] `WP14-030` Implement support detachment and local delamination.
- [ ] `WP14-031` Re-solve electrical, thermal, structural, and control constraints after each fault.
- [ ] `WP14-032` Compute degraded output, grace time, safe isolation, and repair urgency.
- [ ] `WP14-033` Compute survivability and redundancy value.

### Verification and Validation

- [ ] `WP14-034` Verify monotonic and limiting behavior for each model.
- [ ] `WP14-035` Verify zero-damage and immediate-failure edge cases.
- [ ] `WP14-036` Verify accumulation under equivalent reordered histories where the model predicts equivalence.
- [ ] `WP14-037` Compare against published or internal accelerated tests.
- [ ] `WP14-038` Design controlled busbar damage and ageing specimens.
- [ ] `WP14-039` Measure resistance, temperature, thickness, leakage, adhesion, or other relevant health indicators.
- [ ] `WP14-040` Evaluate holdout remaining-life or degraded-performance predictions.
- [ ] `WP14-041` Publish mechanisms not yet calibrated and prohibit authoritative use.

## Required Artifacts

- FMEA/FMECA;
- damage and fault schemas;
- ageing models;
- fault library;
- degraded-operation driver;
- accelerated-test protocols and data;
- remaining-life and uncertainty reports.

## Local Gate WP14-G

**PASS** when prioritized damage mechanisms have source evidence, models pass limiting tests, degraded states re-solve all relevant constraints, controlled damage predictions meet thresholds, and unsupported mechanisms remain visibly non-authoritative.

**FAIL** when separate mechanisms are collapsed into an untraceable health score, acceleration changes the failure mechanism without detection, or remaining life is reported without uncertainty and calibration status.

---

# Work Package 15 — Inspection, Repair, Replating, Remanufacturing, and Requalification

## Objective

Generate and validate executable inspection and repair plans, including local replating and modular replacement, from measured or simulated damage.

## Entry Criteria

- WP11-G, WP12-G, and WP14-G passed for the relevant repair mode;
- repair laboratory safety hold released;
- inspection modalities and equipment available.

## Micro-Steps

### Inspection Research and Qualification

- [ ] `WP15-001` Map each damage mode to candidate inspection methods.
- [ ] `WP15-002` Research four-wire mapping, thermal imaging, visual, microscopy, ultrasound, radiography, computed tomography, pressure decay, impedance, and embedded sensing.
- [ ] `WP15-003` Define detection probability, localization error, measurement uncertainty, access, cost, and specimen constraints.
- [ ] `WP15-004` Design known-defect specimens for inspection qualification.
- [ ] `WP15-005` Calibrate inspection instruments and analysis software.
- [ ] `WP15-006` Execute blind known-defect detection trials.
- [ ] `WP15-007` Approve inspection methods by damage type and size range.

### Observability and Access Engine

- [ ] `WP15-008` Implement line-of-sight, probe, electrode, thermal, acoustic, radiographic, and electrical observability representations.
- [ ] `WP15-009` Compute which regions and damage modes are observable.
- [ ] `WP15-010` Compute expected localization and quantification uncertainty.
- [ ] `WP15-011` Identify inaccessible mandatory health features.
- [ ] `WP15-012` Feed observability deficits back to topology generation.
- [ ] `WP15-013` Generate witness surfaces, test terminals, removable covers, and embedded sensor positions.

### Repair Action Library

- [ ] `WP15-014` Define clean, strip, mask, activate, reseed, replate, patch, machine, replace segment, replace module, re-insulate, seal, and retest actions.
- [ ] `WP15-015` Define required access, equipment, consumables, hazards, time, cost, and process capability for each action.
- [ ] `WP15-016` Define compatible action sequences and prohibited combinations.
- [ ] `WP15-017` Define repair-induced geometry, material, interface, and residual-stress changes.
- [ ] `WP15-018` Define maximum repair cycles and accumulated repair-history effects.
- [ ] `WP15-019` Define repair abort and replacement triggers.

### Repair Planning

- [ ] `WP15-020` Import measured or simulated damage field with uncertainty.
- [ ] `WP15-021` Compute target restoration field.
- [ ] `WP15-022` Generate feasible repair actions and sequences.
- [ ] `WP15-023` Use WP12 inverse plating for replating candidates.
- [ ] `WP15-024` Predict restored geometry and uncertainty.
- [ ] `WP15-025` Re-solve electrical, thermal, structural, insulation, flow, and ageing models.
- [ ] `WP15-026` Estimate repair success, rework, downtime, cost, material, energy, and remaining life.
- [ ] `WP15-027` Compare repair, derated operation, module replacement, full replacement, and retirement.
- [ ] `WP15-028` Produce a pre-repair plan and acceptance checklist.

### Physical Repair Demonstration

- [ ] `WP15-029` Manufacture repairable and non-repairable control specimens.
- [ ] `WP15-030` Record baseline geometry, resistance, thermal, and mechanical state.
- [ ] `WP15-031` Apply controlled damage using a pre-approved method.
- [ ] `WP15-032` Inspect without revealing the known defect record to the operator where practical.
- [ ] `WP15-033` Generate the repair plan before repair execution.
- [ ] `WP15-034` Review and authorize the exact repair traveler.
- [ ] `WP15-035` Execute cleaning, preparation, repair, and finishing.
- [ ] `WP15-036` Record deviations and process history.
- [ ] `WP15-037` Measure as-repaired geometry and material state.
- [ ] `WP15-038` Re-run electrical, thermal, leak, structural, insulation, and life qualification as applicable.
- [ ] `WP15-039` Compare predicted and measured restoration.
- [ ] `WP15-040` Update the passport with immutable damage, inspection, repair, and requalification events.
- [ ] `WP15-041` Repeat repair cycles to the mission requirement or a justified accelerated equivalent.

## Required Artifacts

- inspection-method qualification;
- observability engine;
- repair action and sequence library;
- repair planner;
- pre-repair and as-repaired simulation bundles;
- physical repair data;
- passport transitions;
- repair-versus-replace decision report.

## Local Gate WP15-G

**PASS** when the damage is detected within the approved method range, the repair plan is frozen before execution, repaired conductance and every applicable safety/performance requirement pass, prediction errors meet thresholds, and passport history remains complete.

**FAIL** when damage is not observable, repair is improvised without a recorded deviation, restored conductivity hides a new safety defect, requalification is incomplete, or the history of failed repair attempts is omitted.

---

# Work Package 16 — Disassembly, Reuse, Recycling, and Digital Component Passport

## Objective

Preserve component function and lifecycle evidence through disassembly, second-life grading, remanufacture, material recovery, and final disposition.

## Entry Criteria

- WP03-G passed;
- product structure and repair events represented;
- WP15-G passed before claiming repair/reuse demonstration.

## Micro-Steps

### Research and Policy

- [ ] `WP16-001` Research design-for-disassembly metrics and sequence-planning methods.
- [ ] `WP16-002` Research screening and derating methods for recovered power components.
- [ ] `WP16-003` Research separation, contamination, yield, energy, and value loss for selected material streams.
- [ ] `WP16-004` Review IEC 62474 and applicable digital product passport requirements.
- [ ] `WP16-005` Define passport data ownership, privacy, signing, retention, correction, and sharing policies.
- [ ] `WP16-006` Define which reuse claims require accredited or specialist testing.

### Assembly and Disassembly Model

- [ ] `WP16-007` Implement product, subassembly, component, interface, and fastener graph.
- [ ] `WP16-008` Encode tool, access, orientation, force, temperature, and destructive-step requirements.
- [ ] `WP16-009` Encode disassembly precedence and parallel operations.
- [ ] `WP16-010` Encode probability of damage to the target and neighboring components.
- [ ] `WP16-011` Encode labor, equipment, energy, consumables, and time.
- [ ] `WP16-012` Implement sequence search and comparison.
- [ ] `WP16-013` Identify buried fasteners, inaccessible joints, inseparable materials, and destructive dependencies.
- [ ] `WP16-014` Feed disassembly penalties and redesign suggestions to topology generation.

### Reuse Grading

- [ ] `WP16-015` Define grades A direct reuse, B derated reuse, C repair/remanufacture, and D materials recovery.
- [ ] `WP16-016` Define evidence required for each component type and grade.
- [ ] `WP16-017` Import operating history, peak events, environment, inspections, and repairs.
- [ ] `WP16-018` Import electrical, thermal, mechanical, dimensional, and diagnostic tests.
- [ ] `WP16-019` Estimate remaining-life range and derating.
- [ ] `WP16-020` Reject favorable grading when required history or tests are absent.
- [ ] `WP16-021` Record grade, restrictions, uncertainty, reviewer, and intended second-life mission.
- [ ] `WP16-022` Re-evaluate the component against the second-life mission rather than its original mission only.

### Recycling and Recovery

- [ ] `WP16-023` Define material separation routes for every demonstrator.
- [ ] `WP16-024` Estimate recovered stream mass, purity, yield, energy, cost, and destination.
- [ ] `WP16-025` Distinguish direct reuse, component remanufacture, closed-loop recycling, open-loop recycling, energy recovery, and disposal.
- [ ] `WP16-026` Model contamination caused by adhesives, mixed platings, insulation, coolant, and embedded components.
- [ ] `WP16-027` Record hazardous or regulated waste streams.
- [ ] `WP16-028` Link actual teardown measurements to the recovery model.

### Passport Implementation

- [ ] `WP16-029` Implement product and component passport identities.
- [ ] `WP16-030` Record topology, materials, batches, process plan, as-built map, QA, and initial qualification.
- [ ] `WP16-031` Record accepted operating histories and exceptional events.
- [ ] `WP16-032` Record inspections with measured versus inferred separation.
- [ ] `WP16-033` Record damage, repair, replacement, and requalification events.
- [ ] `WP16-034` Record component removal, reuse grade, second-life mission, and new parent assembly.
- [ ] `WP16-035` Record recycling route and final disposition.
- [ ] `WP16-036` Implement signed append-only updates and correction-by-supersession.
- [ ] `WP16-037` Implement selective disclosure and export.
- [ ] `WP16-038` Implement passport completeness and integrity audit.

### Physical Validation

- [ ] `WP16-039` Create a controlled assembly with representative joints and material interfaces.
- [ ] `WP16-040` Predict disassembly sequence, time, tools, damage risk, and recoverable mass.
- [ ] `WP16-041` Execute disassembly using a controlled traveler.
- [ ] `WP16-042` Measure actual time, tool changes, damage, recovered components, and material purity.
- [ ] `WP16-043` Grade recovered components and record the evidence.
- [ ] `WP16-044` Compare predicted and actual disassembly/recovery outcomes.
- [ ] `WP16-045` Reuse at least one eligible component in a controlled second-life assembly or test fixture.
- [ ] `WP16-046` Verify passport ancestry through removal and reuse.

## Required Artifacts

- assembly/disassembly graph;
- sequence planner;
- reuse grading protocol;
- recycling-route model;
- passport implementation;
- physical teardown and reuse evidence;
- integrity audit.

## Local Gate WP16-G

**PASS** when disassembly predictions are validated, recovered components are graded from required evidence, at least one second-life transition is replayable, recovery streams are measured, and passport ancestry remains signed and complete.

**FAIL** when reuse grades rely on age alone, destructive steps are hidden, measured and inferred passport facts are mixed, or a component changes assemblies without an auditable ancestry transition.

---

# Work Package 17 — Economics, Lifecycle Assessment, Circularity, and Supply Risk

## Objective

Calculate transparent process and lifetime value, material use, environmental flows, circularity, and supply risk without hiding trade-offs in one score.

## Entry Criteria

- WP02-G, WP03-G, and WP05-G passed;
- process plans available from WP11/WP12;
- lifecycle states available as each demonstrator progresses.

## Micro-Steps

### Research and Boundary Definition

- [ ] `WP17-001` Review ISO 14040 and ISO 14044 principles, goal/scope, inventory, impact, interpretation, and reporting needs.
- [ ] `WP17-002` Define study boundaries for cradle-to-gate, use, repair, second life, and end of life.
- [ ] `WP17-003` Define functional units for busbar, cooled conductor, winding, and assembly comparisons.
- [ ] `WP17-004` Define allocation and avoided-burden policy for reuse, remanufacture, and recycling.
- [ ] `WP17-005` Research process cost drivers, yield, batch size, labor, energy, bath maintenance, QA, and rework.
- [ ] `WP17-006` Research supply-risk indicators and data sources.
- [ ] `WP17-007` Define region, currency, date, escalation, discount, and scenario policy.
- [ ] `WP17-008` Define uncertainty and sensitivity reporting.

### Cost Engine

- [ ] `WP17-009` Implement virgin and recycled material cost by mass and process loss.
- [ ] `WP17-010` Implement printing machine time, energy, consumables, supports, labor, and yield.
- [ ] `WP17-011` Implement seeding, plating, bath, electricity, flow, heating, labor, masking, cleaning, and waste cost.
- [ ] `WP17-012` Implement finishing, machining, inspection, QA, assembly, and packaging cost.
- [ ] `WP17-013` Implement operating electrical loss and cooling pump energy.
- [ ] `WP17-014` Implement scheduled inspection, repair, replacement, downtime, logistics, and requalification cost.
- [ ] `WP17-015` Implement disassembly, recovered value, remanufacture, recycling, and disposal cost.
- [ ] `WP17-016` Implement batch-size and learning assumptions as explicit scenarios.
- [ ] `WP17-017` Implement cost uncertainty and correlation.

### Material, Energy, and Circularity Flow

- [ ] `WP17-018` Implement mass balance for virgin, recycled, process scrap, repair, replacement, reuse, and recovered streams.
- [ ] `WP17-019` Implement process and operating energy inventory.
- [ ] `WP17-020` Implement water, chemical, and waste inventory where data exist.
- [ ] `WP17-021` Implement recovery ratio and function-preservation hierarchy.
- [ ] `WP17-022` Compute reused, remanufactured, recycled, lost, and hazardous fractions separately.
- [ ] `WP17-023` Implement circularity weights as study configuration with sensitivity, not universal constants.
- [ ] `WP17-024` Implement supply-risk exposure and substitution scenarios.
- [ ] `WP17-025` Implement missing-data and data-quality scoring.

### Lifetime Metrics

- [ ] `WP17-026` Implement lifetime delivered useful energy or mission function.
- [ ] `WP17-027` Implement `Lambda_m` using virgin plus replacement material.
- [ ] `WP17-028` Implement `Lambda_C` using manufacture, maintenance, repair, and replacement cost.
- [ ] `WP17-029` Implement lifetime loss, downtime, and survivability-adjusted metrics.
- [ ] `WP17-030` Preserve the full objective vector and hard constraints.
- [ ] `WP17-031` Implement scenario, one-way sensitivity, global sensitivity, and break-even analysis.

### Verification and Review

- [ ] `WP17-032` Verify mass and energy conservation.
- [ ] `WP17-033` Verify zero-repair, zero-reuse, and full-reuse limiting cases.
- [ ] `WP17-034` Verify cost calculations against hand-worked reference cases.
- [ ] `WP17-035` Compare predicted process time, material, rework, and energy with demonstrator records.
- [ ] `WP17-036` Independently review functional unit and allocation choices.
- [ ] `WP17-037` Publish data-quality, uncertainty, and excluded-impact statements.
- [ ] `WP17-038` Prevent environmental or circularity claims when supporting data quality is below the approved threshold.

## Required Artifacts

- cost and inventory engine;
- LCA goal/scope records;
- functional-unit definitions;
- circularity and supply-risk models;
- lifetime metric implementation;
- sensitivity and data-quality reports;
- physical process-cost comparison.

## Local Gate WP17-G

**PASS** when cost, mass, and energy balances close, functional units and allocation are independently reviewed, measured demonstrator process data reconcile with the model, uncertainties are visible, and Pareto outputs retain all primary metrics.

**FAIL** when recovered value is double counted, pump or repair burden is excluded, reuse and recycling are treated as equivalent, or a sustainability claim relies on low-quality or untraceable data.

---

# Work Package 18 — Optimization, Uncertainty, Compute Orchestration, and Review Interface

## Objective

Search the mixed topology/process/lifecycle space efficiently while preserving hard constraints, model discrepancy, uncertainty, reproducibility, and human review.

## Entry Criteria

- WP03-G and WP06-G passed;
- at least one verified objective engine available;
- compute and licensing constraints known.

## Micro-Steps

### Optimization Research and Selection

- [ ] `WP18-001` Compare evolutionary, Bayesian, direct-search, mixed-integer, level-set, density, adjoint, and hybrid methods.
- [ ] `WP18-002` Define method suitability for graph, geometry, material, process, repair, and maintenance variables.
- [ ] `WP18-003` Define hard constraints, projections, repair operators, penalties, and unknown feasibility.
- [ ] `WP18-004` Define Pareto dominance with uncertainty and feasibility.
- [ ] `WP18-005` Define diversity preservation and topology-family coverage.
- [ ] `WP18-006` Define surrogate authority limits and reference-evaluation requirements.
- [ ] `WP18-007` Define robust and reliability-based objectives.
- [ ] `WP18-008` Define stopping conditions based on budget, convergence, uncertainty, and evidence sufficiency.

### Search Core

- [ ] `WP18-009` Implement candidate evaluation contracts.
- [ ] `WP18-010` Implement multi-objective evolutionary baseline.
- [ ] `WP18-011` Implement hard feasibility ranking.
- [ ] `WP18-012` Implement Pareto archive with immutable candidate identities.
- [ ] `WP18-013` Implement elitism without losing diversity.
- [ ] `WP18-014` Implement constraint-preserving mutation integration.
- [ ] `WP18-015` Implement restart from a frozen population.
- [ ] `WP18-016` Implement search diagnostics and reason-coded rejection summaries.

### Sensitivity and Local Refinement

- [ ] `WP18-017` Integrate conductor-utility sensitivity.
- [ ] `WP18-018` Integrate local geometry and process sensitivities where verified.
- [ ] `WP18-019` Implement finite-difference checks for gradients or adjoints.
- [ ] `WP18-020` Implement local finalist refinement.
- [ ] `WP18-021` Record every refinement step and accepted/rejected move.

### Surrogates and Active Learning

- [ ] `WP18-022` Define training dataset identity and leakage controls.
- [ ] `WP18-023` Implement baseline regression and classification surrogates.
- [ ] `WP18-024` Implement uncertainty or conformal/error estimates appropriate to the method.
- [ ] `WP18-025` Hold out topology families, not only random samples, during evaluation.
- [ ] `WP18-026` Implement active learning for objective improvement and discrepancy reduction.
- [ ] `WP18-027` Reject surrogate-only promotion to manufacture.
- [ ] `WP18-028` Monitor drift after new process or material data.

### Uncertainty and Robustness

- [ ] `WP18-029` Define uncertain inputs and correlations by engine.
- [ ] `WP18-030` Implement sampling and deterministic seed records.
- [ ] `WP18-031` Implement propagation through reduced models.
- [ ] `WP18-032` Implement selective propagation through high-fidelity finalists.
- [ ] `WP18-033` Compute expected, percentile, worst credible, and reliability metrics as configured.
- [ ] `WP18-034` Implement global sensitivity to identify dominant uncertainty.
- [ ] `WP18-035` Optimize robust performance rather than nominal performance only.

### Compute Orchestration

- [ ] `WP18-036` Implement resource-aware job definitions.
- [ ] `WP18-037` Implement local CPU, accelerator, cluster, and external-solver queues.
- [ ] `WP18-038` Implement deterministic cache keys from all relevant inputs.
- [ ] `WP18-039` Implement concurrency, quotas, timeouts, cancellation, retry, and backoff.
- [ ] `WP18-040` Distinguish transient infrastructure failure from model failure.
- [ ] `WP18-041` Implement checkpoint and resume for long jobs.
- [ ] `WP18-042` Propagate every child-process exit status.
- [ ] `WP18-043` Record runtime, memory, energy proxy, solver license use, and queue wait.
- [ ] `WP18-044` Implement orphan-process detection and cleanup.

### User Workflow and Review

- [ ] `WP18-045` Implement CLI study creation from a mission.
- [ ] `WP18-046` Implement population generation, evaluation, promotion, and resume commands.
- [ ] `WP18-047` Implement candidate comparison and Pareto export.
- [ ] `WP18-048` Implement views for topology roles, constraints, uncertainty, evidence, and lineage.
- [ ] `WP18-049` Explain why material was added or removed.
- [ ] `WP18-050` Explain why a candidate was rejected or promoted.
- [ ] `WP18-051` Show model fidelity, calibration, validity domain, and discrepancy.
- [ ] `WP18-052` Implement exact-artifact human approval for manufacturing export.
- [ ] `WP18-053` Implement approval revocation after artifact change.

### Verification

- [ ] `WP18-054` Verify standard multi-objective benchmark functions.
- [ ] `WP18-055` Verify deterministic population replay.
- [ ] `WP18-056` Verify cache correctness and invalidation.
- [ ] `WP18-057` Verify failed jobs cannot appear successful.
- [ ] `WP18-058` Verify surrogate leakage controls and topology-family holdouts.
- [ ] `WP18-059` Verify approval binds exact artifact identities.
- [ ] `WP18-060` Benchmark scalability at each fidelity tier.

## Required Artifacts

- search coordinator;
- Pareto archive;
- sensitivity and local refinement;
- surrogate/active-learning system;
- uncertainty and robust optimization;
- job orchestration and cache;
- CLI and review UI;
- approval controls;
- scalability report.

## Local Gate WP18-G

**PASS** when searches replay deterministically, hard constraints dominate scoring, failed jobs propagate failure, cache reuse is exact, surrogate uncertainty and holdouts pass, Pareto diversity is retained, and manufacturing export is impossible without exact-artifact approval.

**FAIL** when the optimizer silently converts unknowns to favorable scores, surrogates become manufacturing authority, a stale approval survives an artifact change, or infrastructure failure is mistaken for a valid low objective.

---

# Work Package 19 — Demonstrator and Physical Validation Campaign

## Objective

Close the simulation loop through controlled physical builds that advance from a simple busbar to an integrated, repairable, reusable power topology assembly.

## Entry Criteria

- the applicable engine gates passed;
- G0 and G1 passed;
- experiment-specific safety hold released;
- protocol, thresholds, sample size, calibration, and analysis frozen before data collection.

## Common Experimental Micro-Steps

- [ ] `WP19-001` Assign a demonstrator owner and independent V&V reviewer.
- [ ] `WP19-002` Freeze the mission, requirements, geometry, process, and comparison baseline.
- [ ] `WP19-003` Pre-register hypotheses, primary metrics, secondary metrics, thresholds, exclusions, and failure handling.
- [ ] `WP19-004` Define specimen groups, replicates, controls, randomization, and blocking.
- [ ] `WP19-005` Complete hazard review and release the exact safety hold.
- [ ] `WP19-006` Calibrate instruments and record calibration validity.
- [ ] `WP19-007` Freeze process travelers and test procedures.
- [ ] `WP19-008` Assign immutable specimen, batch, material, geometry, and process identities.
- [ ] `WP19-009` Record as-received material and substrate condition.
- [ ] `WP19-010` Record every process deviation and do not retroactively edit the planned traveler.
- [ ] `WP19-011` Preserve failed and partially completed specimens.
- [ ] `WP19-012` Store immutable raw data before analysis.
- [ ] `WP19-013` Execute analysis from versioned scripts or notebooks with recorded environments.
- [ ] `WP19-014` Separate calibration, validation, and exploratory data.
- [ ] `WP19-015` Compare results with the frozen pre-test predictions before recalibration.
- [ ] `WP19-016` Create discrepancy records and root-cause hypotheses.
- [ ] `WP19-017` Update models only in a new revision.
- [ ] `WP19-018` Re-run dependent studies after model updates.
- [ ] `WP19-019` Conduct an independent requirement-to-evidence audit.
- [ ] `WP19-020` Sign the exact demonstrator evidence bundle or record failure.

## Demonstrator D1 — Current-Adaptive Electroformed Busbar

### Purpose

Prove the initial requirements-to-topology-to-electrothermal-to-manufacture-to-measurement loop.

### Design Micro-Steps

- [ ] `D1-001` Freeze terminal positions, current mission, ambient, mounting, mass, resistance, temperature, cost, and repair-access requirements.
- [ ] `D1-002` Select a conventional sheet/solid reference.
- [ ] `D1-003` Select a simple plated printed reference.
- [ ] `D1-004` Generate a broad topology population with fixed seeds.
- [ ] `D1-005` Screen connectivity, printing, cleaning, seeding, plating, inspection, and assembly access.
- [ ] `D1-006` Evaluate Level 0 electrical and thermal objectives.
- [ ] `D1-007` Promote diverse Pareto families to Level 1 and Level 2.
- [ ] `D1-008` Run plating-process prediction and update as-manufactured geometry distributions.
- [ ] `D1-009` Evaluate robust electrical, thermal, mass, process, cost, and repairability metrics.
- [ ] `D1-010` Select at least three optimized finalists plus one deliberately difficult negative control.
- [ ] `D1-011` Freeze the pre-build prediction bundle.
- [ ] `D1-012` Approve the exact manufacturing exports.

### Manufacturing Micro-Steps

- [ ] `D1-013` Print witness coupons and substrates in controlled batches.
- [ ] `D1-014` Measure as-printed dimensions and defects.
- [ ] `D1-015` Clean and verify all required paths.
- [ ] `D1-016` Apply seed and measure continuity/resistance.
- [ ] `D1-017` Plate using controlled recipes.
- [ ] `D1-018` Record process histories and bath state.
- [ ] `D1-019` Clean, rinse, dry, finish, and inspect.
- [ ] `D1-020` Record yield, rework, failure, time, material, energy, and waste.

### Test Micro-Steps

- [ ] `D1-021` Measure as-built mass and dimensions.
- [ ] `D1-022` Measure coating thickness and critical cross-sections.
- [ ] `D1-023` Measure four-wire resistance at controlled temperature.
- [ ] `D1-024` Execute continuous-current thermal tests.
- [ ] `D1-025` Execute peak-current mission pulses.
- [ ] `D1-026` Record temperature fields, terminal temperatures, voltage drop, current, and environment.
- [ ] `D1-027` Inspect for delamination, overheating, deformation, leakage of any process residue, or inaccessible defects.
- [ ] `D1-028` Recompute performance from measured as-built geometry.
- [ ] `D1-029` Compare all specimen groups and include failed builds in yield and cost.

### D1 Gate

**PASS** when G5 passes; resistance, mass, thickness, and hotspot thresholds pass; the optimized design improves an approved lifetime or Pareto metric; and all hard manufacturing, safety, and repair-access requirements remain satisfied.

**FAIL** when improvement depends on excluding failed specimens, using nominal rather than as-built geometry, or violating a hard requirement.

## Demonstrator D2 — Damage-Aware Repairable Busbar

### Purpose

Prove that repairability changes initial topology and that a measured damaged component can be inspected, repaired, requalified, and compared with replacement.

### Design Micro-Steps

- [ ] `D2-001` Select damage modes relevant to the D1 process and mission.
- [ ] `D2-002` Define detection and repair thresholds before specimen damage.
- [ ] `D2-003` Generate R0-R2 controls and R3-R5 repairable variants.
- [ ] `D2-004` Add repair electrode, inspection, masking, cleaning, and access features.
- [ ] `D2-005` Simulate damage progression and degraded operation.
- [ ] `D2-006` Simulate branch-loss and thinning survivability.
- [ ] `D2-007` Compare added initial mass/cost with expected repair value.
- [ ] `D2-008` Freeze repairable design and control predictions.

### Damage and Inspection Micro-Steps

- [ ] `D2-009` Record new-condition baseline measurements.
- [ ] `D2-010` Apply controlled thinning, corrosion, notch, joint, or delamination damage.
- [ ] `D2-011` Preserve a hidden ground-truth defect record for blind inspection where practical.
- [ ] `D2-012` Execute the approved inspection sequence.
- [ ] `D2-013` Estimate damage location, extent, and uncertainty.
- [ ] `D2-014` Run degraded electrical and thermal predictions before destructive confirmation.
- [ ] `D2-015` Test degraded performance within safety limits.
- [ ] `D2-016` Compare predicted and measured degraded state.

### Repair and Requalification Micro-Steps

- [ ] `D2-017` Generate repair, derate, replace-module, and replace-part alternatives.
- [ ] `D2-018` Freeze the selected repair traveler.
- [ ] `D2-019` Execute cleaning, preparation, masking, reseeding, replating or module replacement.
- [ ] `D2-020` Record repair process and deviations.
- [ ] `D2-021` Measure repaired geometry and thickness.
- [ ] `D2-022` Re-test resistance and thermal performance.
- [ ] `D2-023` Re-test structural, insulation, and leak requirements where applicable.
- [ ] `D2-024` Update remaining-life prediction.
- [ ] `D2-025` Compare actual repair time, cost, material, energy, and downtime with replacement.
- [ ] `D2-026` Repeat the repair cycle to the mission target or approved accelerated equivalent.
- [ ] `D2-027` Complete passport transitions.

### D2 Gate

**PASS** when G6 passes, damage is detected within the qualified range, repaired conductance reaches at least 90% of nominal, every safety constraint re-passes, and repair offers a documented advantage for at least one approved mission scenario.

**FAIL** when the design is called repairable without an executable and validated repair, or when conductivity is restored but life, insulation, pressure, adhesion, or access constraints fail.

## Demonstrator D3 — Hollow Actively Cooled Conductor

### Purpose

Prove the coupled trade between conductor material, channel geometry, plating, coolant flow, pump energy, pressure integrity, cleaning, damage, and repair.

### Design Micro-Steps

- [ ] `D3-001` Freeze pressure, coolant, flow, pump, temperature, leak, mass, and maintenance requirements.
- [ ] `D3-002` Select solid and conventional cooled references.
- [ ] `D3-003` Define channel, manifold, wall, drain, vent, and repair design variables.
- [ ] `D3-004` Generate hollow and multifunctional topology families.
- [ ] `D3-005` Screen print, support, core, cleaning, seed, plating, gas, rinse, and inspection access.
- [ ] `D3-006` Run reduced electrical, thermal, flow, and structural screening.
- [ ] `D3-007` Promote finalists to 3D electrothermal, CFD, pressure, and plating analysis.
- [ ] `D3-008` Evaluate blocked flow, partial blockage, leak, pump loss, freeze/storage, and degraded operation.
- [ ] `D3-009` Evaluate cleaning and fluid-recovery procedures.
- [ ] `D3-010` Evaluate repair of conductor wall and channel-adjacent damage.
- [ ] `D3-011` Freeze finalists and pre-build predictions.

### Manufacturing and Test Micro-Steps

- [ ] `D3-012` Manufacture channel and manifold coupons before full specimens.
- [ ] `D3-013` Verify internal cleanability and dryness.
- [ ] `D3-014` Verify seed continuity through the complete required path.
- [ ] `D3-015` Plate and record internal process evidence.
- [ ] `D3-016` Inspect internal thickness using approved destructive or nondestructive methods.
- [ ] `D3-017` Execute pressure-decay leak test.
- [ ] `D3-018` Execute proof-pressure test at 1.5 times maximum operating pressure.
- [ ] `D3-019` Measure pressure drop and flow distribution.
- [ ] `D3-020` Execute electrothermal tests across flow rates.
- [ ] `D3-021` Execute loss-of-flow and blockage tests within approved safety controls.
- [ ] `D3-022` Measure deformation, temperature, resistance, pump power, and coolant condition.
- [ ] `D3-023` Execute pressure and thermal cycling.
- [ ] `D3-024` Inspect for leakage, delamination, blockage, corrosion, and fatigue.
- [ ] `D3-025` Compare lifetime metrics with solid references.

### D3 Gate

**PASS** when G7 passes, proof pressure and leak tests pass, resistance/temperature/pressure-drop predictions meet thresholds, failure cases are safe, and the complete lifetime comparison includes pump, cleaning, inspection, repair, and coolant burdens.

**FAIL** when the internal channel cannot be inspected or cleaned, plating uniformity is unknown, pressure integrity fails, or the cooling advantage disappears when system burden is counted.

## Demonstrator D4 — Three-Dimensional Motor Winding

### Purpose

Prove mission-driven 3D winding topology with DC and AC electrical behavior, electromagnetic performance, cooling, structural support, insulation, manufacture, fault response, and repair.

### Research and Baseline Micro-Steps

- [ ] `D4-001` Select a bounded motor architecture and conventional winding reference.
- [ ] `D4-002` Freeze electromagnetic, thermal, mechanical, insulation, acoustic, manufacturing, and lifecycle requirements.
- [ ] `D4-003` Confirm applicable IEC 60034 and insulation-coordination requirements.
- [ ] `D4-004` Characterize the reference machine and test stand.
- [ ] `D4-005` Validate canonical motor models before generated winding studies.
- [ ] `D4-006` Define allowable winding design space, terminals, slots, air gap, cooling, supports, and assembly route.

### Design Micro-Steps

- [ ] `D4-007` Generate winding conductor graphs and geometric realizations.
- [ ] `D4-008` Screen DC resistance, fill, clearances, printability, plating access, insulation, and assembly.
- [ ] `D4-009` Evaluate AC resistance, proximity, eddy-current, inductance, back EMF, torque, and harmonics.
- [ ] `D4-010` Evaluate Joule and magnetic losses over the mission.
- [ ] `D4-011` Evaluate thermal and coolant performance.
- [ ] `D4-012` Evaluate electromagnetic force, centrifugal or assembly loads, vibration, and fatigue.
- [ ] `D4-013` Evaluate insulation coordination and thermal life.
- [ ] `D4-014` Evaluate terminal, sensor, inspection, repair, and modular replacement access.
- [ ] `D4-015` Evaluate open branch, turn fault, coolant loss, sensor loss, and degraded operation.
- [ ] `D4-016` Select diverse robust Pareto finalists.
- [ ] `D4-017` Freeze as-designed and as-manufactured uncertainty predictions.

### Prototype and Test Micro-Steps

- [ ] `D4-018` Build subscale conductor and insulation coupons.
- [ ] `D4-019` Qualify plating, insulation application, adhesion, dielectric, and thermal cycling.
- [ ] `D4-020` Build winding segments and terminal transitions.
- [ ] `D4-021` Measure resistance, inductance, AC loss, thermal response, and dimensional variation.
- [ ] `D4-022` Build the controlled winding prototype.
- [ ] `D4-023` Record as-built geometry, thickness, insulation, and assembly state.
- [ ] `D4-024` Execute low-energy electrical and insulation checks.
- [ ] `D4-025` Execute back-EMF and inductance tests.
- [ ] `D4-026` Execute torque and loss mapping.
- [ ] `D4-027` Execute thermal mission tests.
- [ ] `D4-028` Execute vibration and selected endurance tests.
- [ ] `D4-029` Execute a controlled fault/degraded-operation test.
- [ ] `D4-030` Execute one inspection and repair or module-replacement workflow.
- [ ] `D4-031` Compare with the conventional winding reference on the full Pareto vector.

### D4 Gate

**PASS** when G8 passes, torque/back-EMF/loss/hotspot thresholds pass, insulation and mechanical requirements pass, AC effects materially influence design where expected, and one fault plus one repair or module-replacement scenario is demonstrated.

**FAIL** when the winding is optimized only for DC mass, or measured electromagnetic improvement violates insulation, thermal, structural, process, repair, or assembly requirements.

## Demonstrator D5 — Integrated Power Topology Assembly

### Purpose

Prove assembly-level design and lifecycle reasoning across winding, busbar, coolant, terminals, sensors, mounts, and selected power-electronic interconnects.

### Integration Micro-Steps

- [ ] `D5-001` Freeze the assembly mission and interface-control documents.
- [ ] `D5-002` Define component passport hierarchy and replacement semantics.
- [ ] `D5-003` Import qualified component models and uncertainty.
- [ ] `D5-004` Model terminal/contact losses and thermal paths.
- [ ] `D5-005` Model shared coolant flow, heat rejection, pump, and blockage interactions.
- [ ] `D5-006` Model mounts, vibration transfer, thermal expansion, and service access.
- [ ] `D5-007` Model sensors, observability, and control dependencies.
- [ ] `D5-008` Re-optimize component choices at assembly level.
- [ ] `D5-009` Evaluate common-cause faults and fault propagation.
- [ ] `D5-010` Evaluate assembly inspection, repair, replacement, and disassembly sequences.
- [ ] `D5-011` Evaluate recovered-component grading and second-life allocation.
- [ ] `D5-012` Freeze assembly finalists and evidence gaps.

### Assembly Demonstration Micro-Steps

- [ ] `D5-013` Manufacture and assemble using controlled component passports.
- [ ] `D5-014` Execute incoming inspection for every component.
- [ ] `D5-015` Record assembly torque, contacts, seals, coolant fill, sensors, and deviations.
- [ ] `D5-016` Execute low-energy continuity, insulation, leak, and sensor tests.
- [ ] `D5-017` Execute nominal mission tests.
- [ ] `D5-018` Execute peak and selected degraded mission tests.
- [ ] `D5-019` Execute a controlled fault-isolation scenario.
- [ ] `D5-020` Inspect and repair or replace the affected component.
- [ ] `D5-021` Requalify the assembly.
- [ ] `D5-022` Disassemble selected components and grade them for reuse.
- [ ] `D5-023` Install an eligible recovered component into a controlled second-life configuration.
- [ ] `D5-024` Verify passport ancestry and evidence through the complete loop.
- [ ] `D5-025` Compare predicted and observed assembly-level cost, material, energy, downtime, and performance.

### D5 Gate

**PASS** when G9 passes and a complete design-manufacture-operate-inspect-repair-requalify-disassemble-reuse/recover scenario is reproducible from one evidence hierarchy.

**FAIL** when component evidence cannot be composed at assembly level, shared interfaces invalidate component optima, or passport ancestry breaks during replacement and reuse.

## Required Artifacts

- five demonstrator protocols;
- approved safety releases;
- process travelers;
- specimen and assembly passports;
- immutable raw datasets;
- analysis source and environments;
- discrepancy and calibration revisions;
- signed D1-D5 gate records.

## Local Gate WP19-G

**PASS** when D1-D5 pass in sequence, each result uses current evidence, physical failures are retained, and the final lifecycle demonstration is independently replayable.

**FAIL** when any demonstrator gate is skipped, historical evidence is reused after source/process drift, or a system-level claim depends on an unvalidated engine.

---

# Work Package 20 — Productization, Quality, Security, Documentation, and Release

## Objective

Deliver a maintainable engineering-preview simulator with stable contracts, reproducible packaging, controlled extensions, clean-environment replay, transparent limitations, and safe release processes.

## Entry Criteria

- G2 passed for platform productization work;
- G9 passed before final engineering-preview release;
- release scope and supported environments approved.

## Micro-Steps

### Repository and Packaging

- [ ] `WP20-001` Create root project metadata, license decision, contribution policy, and code of conduct as applicable.
- [ ] `WP20-002` Select supported language and runtime versions.
- [ ] `WP20-003` Create reproducible dependency lock and build process.
- [ ] `WP20-004` Define supported operating systems, hardware, accelerators, and external solver versions.
- [ ] `WP20-005` Implement package build, installation, and uninstall tests.
- [ ] `WP20-006` Implement version reporting and source identity.
- [ ] `WP20-007` Implement optional dependency groups by solver and application.
- [ ] `WP20-008` Create container or equivalent clean reference environment where licensing permits.

### API and Extension Governance

- [ ] `WP20-009` Freeze public schema and API stability policy.
- [ ] `WP20-010` Define material, solver, process, damage, objective, and application plugin interfaces.
- [ ] `WP20-011` Require units, validity domain, evidence tier, failure behavior, and version for every extension.
- [ ] `WP20-012` Implement capability discovery and unsupported-feature diagnostics.
- [ ] `WP20-013` Implement schema and API deprecation policy.
- [ ] `WP20-014` Implement migration tooling and migration loss checks.
- [ ] `WP20-015` Create extension conformance tests.

### Continuous Verification

- [ ] `WP20-016` Configure formatting, static analysis, type checking, and dependency vulnerability checks.
- [ ] `WP20-017` Run unit and property tests on every change.
- [ ] `WP20-018` Run analytic and replay tests on every change affecting mathematics or schemas.
- [ ] `WP20-019` Run integration and small multiphysics tests on protected changes.
- [ ] `WP20-020` Run nightly convergence, reference-solver, and benchmark suites.
- [ ] `WP20-021` Run scheduled physical-data regression checks.
- [ ] `WP20-022` Detect performance regressions by model and candidate scale.
- [ ] `WP20-023` Preserve failed logs and artifacts.
- [ ] `WP20-024` Prohibit merge or release when required checks did not execute.

### Security and Data Protection

- [ ] `WP20-025` Threat-model solver adapters, imported models, plugins, passport bundles, credentials, and supplier data.
- [ ] `WP20-026` Sandbox or isolate untrusted external-solver inputs where practical.
- [ ] `WP20-027` Validate imported files, dimensions, schemas, and paths.
- [ ] `WP20-028` Keep credentials out of manifests and artifacts.
- [ ] `WP20-029` Implement least-privilege access to sensitive datasets.
- [ ] `WP20-030` Implement audit logs for approvals, exports, baseline changes, and passport corrections.
- [ ] `WP20-031` Define vulnerability reporting and patch policy.
- [ ] `WP20-032` Test backup confidentiality and restoration integrity.

### Documentation and Training

- [ ] `WP20-033` Write installation and environment documentation.
- [ ] `WP20-034` Write architecture and data-contract documentation.
- [ ] `WP20-035` Write mission, study, optimization, evidence, and passport user guides.
- [ ] `WP20-036` Write solver verification and calibration manuals.
- [ ] `WP20-037` Write manufacturing and experimental safety boundaries.
- [ ] `WP20-038` Write demonstrator tutorials using frozen artifacts.
- [ ] `WP20-039` Write troubleshooting and failure-diagnostic guides.
- [ ] `WP20-040` Train operators, reviewers, and maintainers using role-specific exercises.
- [ ] `WP20-041` Test documentation with users who did not build the system.

### Release Preparation

- [ ] `WP20-042` Freeze release scope and supported claims.
- [ ] `WP20-043` Freeze source, dependencies, schemas, reference data, and benchmark versions.
- [ ] `WP20-044` Run the full automated test and validation discovery.
- [ ] `WP20-045` Run clean build and package creation.
- [ ] `WP20-046` Install on a clean independent environment.
- [ ] `WP20-047` Replay the reference busbar, repair, hollow-conductor, winding, and assembly studies.
- [ ] `WP20-048` Audit requirement-to-evidence coverage.
- [ ] `WP20-049` Audit source, artifact, and evidence hashes.
- [ ] `WP20-050` Audit open defects and scope exclusions.
- [ ] `WP20-051` Audit standards status and calibration validity.
- [ ] `WP20-052` Generate limitations, known issues, migration, support, and rollback documents.
- [ ] `WP20-053` Generate the release evidence bundle.
- [ ] `WP20-054` Obtain independent QA review.
- [ ] `WP20-055` Obtain exact-hash human approval.
- [ ] `WP20-056` Publish the engineering preview.
- [ ] `WP20-057` Execute and document rollback rehearsal.

### Post-Release

- [ ] `WP20-058` Monitor defects, numerical discrepancies, security reports, and invalid-domain use.
- [ ] `WP20-059` Triage incidents by safety and evidence impact.
- [ ] `WP20-060` Revoke affected claims when evidence becomes invalid.
- [ ] `WP20-061` Publish corrections without erasing prior releases.
- [ ] `WP20-062` Maintain release support and data migration windows.
- [ ] `WP20-063` Refresh research, standards, and roadmaps before the next release line.

## Required Artifacts

- reproducible package;
- stable APIs and conformance tests;
- CI and benchmark evidence;
- security model and audit logs;
- complete user and V&V documentation;
- clean-install and replay evidence;
- release bundle, approval, and rollback record.

## Local Gate WP20-G

**PASS** when G10 passes, the release installs and replays independently, all supported claims map to current evidence, critical tests executed successfully, limitations are explicit, and rollback is proven.

**FAIL** when release depends on undocumented local state, missing tests are treated as passes, stale evidence is reused, a critical defect remains, or release wording implies certification not obtained.

---

## 11. Cross-Work-Package Dependency Rules

1. WP01 is mandatory before all other work.
2. WP02-WP05 form the canonical foundation and must not be bypassed by application-specific shortcuts.
3. WP06 and WP07 may begin before every high-fidelity engine, but cannot claim validated ranking until WP08-WP10 discrepancy work exists.
4. WP11 must screen every physical candidate before manufacturing export.
5. WP12 physical work cannot begin until the plating safety hold is released.
6. WP13 controls every coupled authoritative result and all BAB-CS transient acceptance.
7. WP14 cannot consume unaccepted transient histories.
8. WP15 cannot claim repairability without inspection observability, an executable process, and requalification.
9. WP16 cannot assign favorable reuse grades without required inspection and history.
10. WP17 cannot claim lifecycle superiority until process yield, operation, repair, and recovery boundaries are included.
11. WP18 cannot promote surrogate-only results to manufacture.
12. WP19 demonstrators cannot skip failed predecessor gates.
13. WP20 cannot release claims beyond the latest current evidence bundle.

---

## 12. Verification and Test Matrix

| Layer | Mandatory tests | Pass condition |
|---|---|---|
| Schema | round trip, migration, invalid input, units | no silent loss; invalid inputs rejected |
| Geometry | analytic dimensions, connectivity, trapped volumes, identity | tolerance met; invalid geometry rejected |
| Materials | units, interpolation, bounds, evidence | out-of-domain fails closed |
| Reduced physics | analytic, conservation, limiting cases | Section 5 thresholds pass |
| High-fidelity physics | mesh convergence, solver residual, independent comparison | convergence and discrepancy criteria pass |
| Coupling | mapping conservation, invalidation, convergence, restart | no stale state; restart equivalent |
| Optimization | benchmark functions, deterministic replay, feasibility, diversity | expected fronts; exact study replay |
| Surrogates | family holdout, calibration, drift, uncertainty | approved error and coverage thresholds |
| Manufacturing | capability coupons, access, cleaning, yield | predicted feasibility agrees with trials |
| Plating | mass, thickness, defects, holdout coupons | G4 thresholds pass |
| Damage | limiting behavior, controlled defects, holdout degradation | mechanism-specific thresholds pass |
| Repair | blind inspection, frozen plan, restored function, requalification | G6 thresholds pass |
| Passport | append-only, signature, ancestry, selective export | no undetected mutation or broken lineage |
| Economics | hand cases, balance, sensitivity, measured process reconciliation | balances close; assumptions traceable |
| Packaging | clean build/install/uninstall/replay | no undocumented local dependency |
| Security | malformed import, permissions, credential leakage, audit | no critical finding |

---

## 13. Procurement and Facility Plan

All procurement remains conditional on approved scope and safety review.

### Phase P0 — Development and Metrology

- [ ] `PROC-001` Development workstations and reproducible compute environment.
- [ ] `PROC-002` Controlled source and artifact storage with backup.
- [ ] `PROC-003` Calibrated balances for substrate and plating mass.
- [ ] `PROC-004` Four-wire resistance measurement equipment and standards.
- [ ] `PROC-005` Temperature sensors, data acquisition, and thermal imaging access.
- [ ] `PROC-006` Dimensional metrology suitable for printed and plated features.
- [ ] `PROC-007` Microscopy, sectioning, and coating-thickness access, internal or external.

### Phase P1 — Printing and Plating

- [ ] `PROC-008` Selected additive-manufacturing equipment or qualified supplier.
- [ ] `PROC-009` Cleaning, support removal, and drying equipment.
- [ ] `PROC-010` Conductive-seed application and verification equipment.
- [ ] `PROC-011` Controlled plating rectifier with current/voltage logging.
- [ ] `PROC-012` Chemically compatible tanks, pumps, heaters/coolers, filters, flow measurement, fixtures, and electrodes.
- [ ] `PROC-013` Approved ventilation, containment, spill, storage, and emergency facilities.
- [ ] `PROC-014` Bath monitoring and sample-analysis capability.
- [ ] `PROC-015` Approved wastewater and hazardous-waste route.

### Phase P2 — Electrical, Thermal, Flow, and Pressure Test

- [ ] `PROC-016` Protected high-current source/load appropriate to D1 and D2.
- [ ] `PROC-017` Barriers, interlocks, emergency stop, insulated fixtures, and fire response.
- [ ] `PROC-018` Coolant loop with pump, reservoir, heat exchanger, flow, pressure, and temperature measurement.
- [ ] `PROC-019` Pressure-decay and hydrostatic proof-test equipment with shields and remote operation.
- [ ] `PROC-020` Leak detection and controlled drainage.

### Phase P3 — Mechanical, Inspection, and Winding Test

- [ ] `PROC-021` Tensile, adhesion, fatigue, vibration, and modal test access.
- [ ] `PROC-022` Nondestructive inspection access appropriate to chosen damage modes.
- [ ] `PROC-023` Dielectric and insulation test equipment.
- [ ] `PROC-024` Motor dynamometer or bounded winding test stand with guarding and overspeed controls.
- [ ] `PROC-025` Torque, speed, back-EMF, power, vibration, acoustic, and thermal instrumentation.

### Procurement Gate

**PASS** when each item has an approved need, owner, calibration/maintenance plan, safety controls, data interface, supplier or build decision, budget, lead time, and contingency.

**FAIL** when equipment is purchased without a validated requirement, cannot produce traceable data, lacks safe facility support, or creates a proprietary dependency without a reproducibility plan.

---

## 14. Data and Statistical Analysis Plan

- [ ] `DATA-001` Define raw, cleaned, derived, calibration, validation, and publication dataset classes.
- [ ] `DATA-002` Define immutable raw-data ingestion.
- [ ] `DATA-003` Define missing, censored, failed, and anomalous measurement handling before experiments.
- [ ] `DATA-004` Define replicate and sample-size rationale for each physical gate.
- [ ] `DATA-005` Define randomization and blocking where bath, machine, batch, or operator effects matter.
- [ ] `DATA-006` Define calibration-versus-validation splits before specimen manufacture.
- [ ] `DATA-007` Define uncertainty propagation from instruments, geometry, process, boundaries, and model discrepancy.
- [ ] `DATA-008` Define residual analysis and outlier policy; never remove outliers solely to pass a gate.
- [ ] `DATA-009` Define confidence/credible interval and coverage reporting.
- [ ] `DATA-010` Define multiple-comparison control where many candidates are experimentally compared.
- [ ] `DATA-011` Define negative-result and failed-specimen reporting.
- [ ] `DATA-012` Define analysis-code review and exact environment capture.
- [ ] `DATA-013` Define independent reproduction for gate-critical conclusions.
- [ ] `DATA-014` Define publication dataset de-identification and supplier-data restrictions.

### Data Gate

**PASS** when raw data are immutable, calibration and validation are separated, analysis is reproducible, uncertainty is complete enough for the claim, and failed specimens remain represented.

**FAIL** when data are overwritten, subsets are selected after outcomes without disclosure, uncertainty omits dominant sources, or analysis cannot be replayed.

---

## 15. Risk Retirement Order

The program should spend early effort on risks that could invalidate the thesis:

1. inability to seed and plate required internal geometry;
2. uncontrolled plating-thickness variation;
3. reduced-model mis-ranking of topology families;
4. material/interface property uncertainty overwhelming predicted improvement;
5. repair access that is geometrically present but operationally unusable;
6. repaired-layer adhesion or fatigue that prevents repeat repair;
7. cooling gains erased by pump, cleaning, pressure, or maintenance burden;
8. motor AC and insulation constraints eliminating generated winding benefits;
9. lifecycle metrics that are too uncertain to distinguish designs;
10. passport and evidence overhead that cannot be maintained in real workflows.

Each risk-retirement experiment must state what project decision follows from pass and from fail.

---

## 16. Completion Audit Checklist

The project may request G10 review only when every item below is checked.

### Requirements and Research

- [ ] Every roadmap requirement has an owner, implementation, evidence, and status.
- [ ] Every gate-critical model has inspectable primary evidence.
- [ ] Standards and regulatory applicability are current for the release date.
- [ ] Research gaps are either closed or explicitly excluded from claims.

### Source and Reproducibility

- [ ] Source revision and dependency lock are frozen.
- [ ] Generated artifacts identify their generator and inputs.
- [ ] All required tests were discovered and executed.
- [ ] Current hashes match the evidence bundle.
- [ ] Clean-environment installation and replay pass.

### Numerical and Physical Evidence

- [ ] Analytic and conservation tests pass.
- [ ] Mesh and timestep convergence evidence is current.
- [ ] Reduced/reference discrepancy is current.
- [ ] Calibration and validation datasets are separated.
- [ ] D1-D5 physical gates pass.
- [ ] Failed specimens and runs remain in the evidence record.

### Lifecycle and Safety

- [ ] Damage, repair, requalification, disassembly, reuse, and recovery are demonstrated.
- [ ] Passport ancestry and signatures pass integrity audit.
- [ ] Chemical, electrical, pressure, rotating, waste, and environmental controls remain approved.
- [ ] No open critical safety or quality defect exists.

### Release

- [ ] Supported capabilities and invalid domains are documented.
- [ ] Release claims do not exceed evidence.
- [ ] Manufacturing export requires exact-artifact approval.
- [ ] Migration and rollback are tested.
- [ ] Independent reviewer signs G10.

Any unchecked item is a **FAIL** for G10.

---

## 17. Research and Standards Sources for the Initial Evidence Library

The project must retain full bibliographic records and verify the current status of every standard before use. Initial anchors include:

1. Stano et al., “Next Generation of 3D-Printed Electronics: Electroplating Inside Channels to Embed 3D Copper Features within Polymeric Structures Fabricated Through Material Extrusion,” *Advanced Materials Technologies*, 2025. <https://doi.org/10.1002/admt.202401923>
2. Puigdellivol et al., “Thermal Topology Optimization of a Three-Layer Laminated Busbar for Power Converters,” *IEEE Transactions on Power Electronics*, DOI 10.1109/TPEL.2016.2601010. <https://doi.org/10.1109/TPEL.2016.2601010>
3. Pecotich et al., “Additively Manufactured Electric Machine Conductors with Integrated End Turn Heat Exchangers,” ICEM 2022, DOI 10.1109/ICEM51905.2022.9910686. <https://doi.org/10.1109/ICEM51905.2022.9910686>
4. Robison and Free, “Modeling and experimental validation of electroplating deposit distributions from copper sulfate solutions,” DOI 10.1149/06121.0027ECST. <https://doi.org/10.1149/06121.0027ECST>
5. Liu et al., “A Topology Optimization Method for Hybrid Subtractive-Additive Remanufacturing,” DOI 10.1007/S40684-019-00075-8. <https://doi.org/10.1007/S40684-019-00075-8>
6. “Additive remanufacturing (AReM): integrated product-process design for functional upgrades of existing components by directed energy deposition,” DOI 10.1007/s40964-025-01435-4. <https://doi.org/10.1007/s40964-025-01435-4>
7. ISO/ASTM 52910, additive-manufacturing design requirements, guidelines, and recommendations. <https://www.iso.org/standard/67289.html>
8. ISO/ASTM 52920, qualification principles and quality assurance for industrial additive-manufacturing production sites. <https://www.iso.org/standard/76911.html>
9. ASME V&V 10, computational solid-mechanics verification and validation. <https://www.asme.org/codes-standards/find-codes-standards/v-v-10-standard-for-verification-and-validation-in-computational-solid-mechanics>
10. ASME V&V 20, verification and validation in computational fluid dynamics and heat transfer. <https://www.asme.org/codes-standards/find-codes-standards/v-v-20-standard-for-verification-and-validation-in-computational-fluid-dynamics-and-heat-transfer>
11. ASTM B193, resistivity of electrical conductor materials. <https://www.astm.org/b0193-20.html>
12. ASTM B487, measurement of metal and oxide coating thickness by microscopical examination of cross section. <https://www.astm.org/b0487-20.html>
13. IEC 60664 series, insulation coordination for equipment within low-voltage supply systems. <https://webstore.iec.ch/en/publication/596>
14. IEC 60034 series, rotating electrical machines. <https://webstore.iec.ch/en/publication/304>
15. IEC 62474, material declaration for products of and for the electrotechnical industry. <https://webstore.iec.ch/en/publication/67469>
16. ISO 14040, lifecycle assessment principles and framework. <https://www.iso.org/standard/37456.html>
17. ISO 14044, lifecycle assessment requirements and guidelines. <https://www.iso.org/standard/38498.html>
18. Regulation (EU) 2024/1781 establishing a framework for ecodesign requirements and digital product passports. <https://eur-lex.europa.eu/eli/reg/2024/1781/oj>
19. Safe Work Australia, model Code of Practice for managing risks of hazardous chemicals in the workplace. <https://www.safeworkaustralia.gov.au/doc/model-code-practice-managing-risks-hazardous-chemicals-workplace>
20. Queensland environmental legislation and regulator guidance applicable to metal surface treatment, hazardous waste, and wastewater, to be confirmed for the selected facility before wet processing.

---

## 18. Final Program Rule

AE3PT must never optimize only the object that leaves the factory. Every promoted design must be evaluated as a time-dependent chain of physical states:

```text
requirements
  -> design
  -> as-manufactured state
  -> qualified state
  -> operating state
  -> damaged state
  -> inspected state
  -> repaired or replaced state
  -> second-life or recovery state
```

The program succeeds only when the simulator can explain, reproduce, and validate why a particular topology uses less virgin material and lower lifetime cost while still meeting electrical, thermal, magnetic, mechanical, manufacturing, safety, repair, reuse, and recovery requirements.
