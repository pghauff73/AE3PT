# Adaptive Electroformed 3D Power Topology Lite (AE3PT-Lite): Classroom Demonstration Overview

## A Small, Low-Power Engineering Project for Students, Lecturers, and Business Funders

> **One-sentence explanation:** Students design three small three-dimensional (3D)-printed electrical paths, coat them with copper in a supervised laboratory, test them at five volts, deliberately damage one, repair it, and compare the technical and financial results.

This is the public overview of the **Adaptive Electroformed 3D Power Topology Lite** project, shortened to **AE3PT-Lite**. The name is explained in full before the abbreviation is used:

- **Adaptive** means the design changes after calculations or measurements show a weakness.
- **Electroformed** refers to making metal shapes by electrically depositing metal. In this classroom project, **electroplating** is the more exact word because copper is deposited as a coating on a printed base.
- **3D** means three-dimensional.
- **Power topology** means the arrangement of connected paths that carry electrical power.
- **Lite** means the research idea has been reduced to a safe, affordable teaching demonstration.

The project is designed for first-year engineering students and readers without an engineering background. Every important technical term is explained when it first appears. The separate [Student Glossary and Acronym Guide](student-glossary.md) provides a second reference.

---

## 1. What Students Actually Build

Students build three types of copper-coated conductor on a 3D-printed plastic base. A **conductor** is a material path that allows electric current to flow. A **busbar** is a conductor used to distribute current between connection points.

Each sample is approximately:

- 100 millimetres long;
- 30 millimetres wide;
- 3–6 millimetres thick before plating;
- operated from a **current-limited** five-volt supply, meaning the supply automatically restricts excessive current;
- tested at approximately 0.5, 1.0, and 1.8 amperes.

An **ampere**, written A, is the unit of electric current. A **volt**, written V, is the unit of electrical potential difference. The project uses five volts of **direct current**, abbreviated 5 VDC, meaning the current keeps one direction rather than reversing periodically.

### Design A — Simple strip

A straight strip with constant width. It is the reference design used for comparison.

### Design B — Material-saving path

A shaped path that removes material from low-value regions while keeping enough copper near the terminals and narrow sections.

### Design C — Repair-ready path

A path with a clearly marked inspection and repair zone. It includes space for measurement probes and a mask used during local replating.

Students normally manufacture three copies of each design, giving nine functional samples. Additional small coupons are used to practise printing, conductive coating, and plating before the functional samples are made.

---

## 2. Why the Project Matters

Most student projects stop after proving that a device works once. AE3PT-Lite also asks:

- How much material was used?
- How accurately did the simple **model**, meaning a simplified calculation of the real object, predict performance?
- Can the damaged item be restored?
- Is repair cheaper than replacement?
- Which records would a future user need?

This creates a complete learning loop:

```text
need
→ idea
→ calculation
→ printed sample
→ copper coating
→ measurement
→ controlled damage
→ repair
→ business comparison
```

For a business reader, the project is a small experiment in reducing technical and financial **uncertainty**, meaning what is not yet known well enough to make a confident decision. It does not promise a commercial product. It demonstrates whether a repairable manufacturing idea deserves further investment.

---

## 3. The Common Demonstration Baseline

Every document in this site uses the same baseline. **USD** means **United States dollars** and is used only as a common planning currency.

| Item | Classroom baseline |
|---|---|
| Student level | first-year engineering or mixed technical/business team |
| Project duration | 24 teaching weeks |
| Supply | certified or laboratory-approved 5 VDC supply |
| Maximum current | 2 A, with normal test point near 1.8 A |
| Electrical protection | 2.5 A fuse and current-limited source |
| Temperature stop | 50 °C measured surface temperature |
| Functional designs | simple strip, material-saving path, repair-ready path |
| Repeated samples | three independently made samples per design |
| Required repair | one supervised local copper repair |
| Required software | small Python calculation and report package |
| Required electronics | low-voltage voltage/current logger and digital temperature logger |
| Chemical work | approved supervised laboratory or approved external service only |
| Baseline direct budget | approximately USD $1,500 when a printer, computer, and laboratory are available |

Local purchasing should use current quotations and local currency.

> **Safety note:** Low voltage reduces electrical shock risk, but current, heat, sharp tools, chemicals, and waste still require supervision and institutional controls.

---

## 4. What Is Being Demonstrated

The project tests five connected ideas.

### 4.1 Electrical performance

Students measure **resistance**, which describes how strongly a path opposes current. Lower resistance usually means less electrical energy is lost as heat.

### 4.2 Thermal performance

**Thermal** means related to heat. Students record temperature while current flows and compare the three designs.

### 4.3 Manufacturing repeatability

**Repeatability** means getting similar results when the same method is repeated. Three copies of each design show whether one excellent sample is typical or merely lucky.

### 4.4 Repair recovery

Students compare a repair-ready sample in three states:

1. original;
2. deliberately damaged;
3. repaired.

The repair is successful only if both resistance and temperature return to the agreed range.

### 4.5 Basic business value

Students calculate:

- cost per sample;
- copper and plastic mass;
- time required for printing, plating, testing, and repair;
- cost of repair;
- cost of replacement;
- number of successful samples;
- technical risk still remaining.

This introduces **engineering economics**, the use of economic reasoning to compare engineering choices.

---

## 5. What the Project Does Not Claim

AE3PT-Lite is not:

- a certified electrical product;
- a high-voltage experiment;
- a motor or inverter project;
- proof of industrial-scale production;
- proof that repair is always better;
- a replacement for professional electroplating controls;
- a complete environmental lifecycle assessment;
- a commercial investment guarantee.

The project produces educational evidence. Further development requires additional testing, standards review, safety engineering, and commercial validation.

---

## 6. Student Learning Path

The [Student Learning and Project Guide](student-project.md) is the main course document.

Students move through six stages:

1. **Understand:** learn the words, simple electrical equations, and project limits.
2. **Predict:** calculate expected resistance and heating.
3. **Build tools:** assemble a low-voltage logger and temperature sensors.
4. **Manufacture:** print, prepare, and plate supervised samples.
5. **Test and repair:** collect repeatable evidence across original, damaged, and repaired states.
6. **Explain value:** present technical results, cost, risk, and next-step recommendation.

The [Student Reading and Study Guide](student-reading-guide.md) recommends short, applied readings. The [Student Glossary](student-glossary.md) explains acronyms, units, and named scientific laws.

---

## 7. Lecturer View

The [Lecturer Guide](lecturer-guide.md) provides:

- lesson sequence;
- expected prior knowledge;
- suggested team roles;
- laboratory release gates;
- assessment rubric;
- common misconceptions;
- questions for oral examination;
- options for mixed engineering and business classes.

Lecturers are encouraged to reward traceable evidence and honest failure analysis. A simple project with excellent records is stronger than a complicated project with unsupported claims.

---

## 8. Business Funder View

The [Business Funder Brief](business-funder-brief.md) explains:

- what funding buys;
- what evidence is produced;
- the difference between a teaching demonstration and commercial readiness;
- financial decision gates;
- risks that remain after the course;
- reasonable next investments.

The first funding question is not “Can this become a large company?” It is:

> Can a small, controlled experiment produce enough evidence to justify the next, slightly larger experiment?

---

## 9. Construction and Budget Documents

The [Low-Power Construction Plan](low-budget-construction-plan.md) describes the student-built logger, digital temperature measurement, printed fixtures, supervised plating workflow, and software package.

The [Student Bill of Materials](bill-of-materials.md) lists required and optional parts, specifications, approximate costs, purchase gates, and lower-cost substitutions. The machine-readable registers are:

- [`data/ae3pt-low-budget-bom.csv`](data/ae3pt-low-budget-bom.csv) for one student team;
- [`data/ae3pt-bom.csv`](data/ae3pt-bom.csv) for a small teaching cohort.

The [JG MAKER Artist-D Dual-Material Copper Electroplating Plan](artist-d-electroplating-plan.md) describes the 300 mm × 300 mm × 340 mm direct-drive IDEX route, its difficulty 4/5 rating, non-conductive and conductive 1.75 mm filament assignment, resistance problems, copper-plating gates and USD $90–$365 optional allowance.

---

## 10. Conductive Coating Method Library

The [Conductive Coating Methods library](conductive-coatings/index.md) converts ten automated seed-layer suggestions into complete student engineering plans. Each plan includes a three-paragraph introduction, expanded acronym, required equipment and materials, implementation microsteps, difficulty, student trial cost, ownership cost, pass/fail gates, safety controls, evidence package, fallback and an accessible Scalable Vector Graphics diagram.

The recommended low-budget route begins with gantry dispensing, then considers robotic spray and supervised electroless seeding. Inkjet, aerosol jet, laser, vacuum and catalyst-loaded resin methods are treated as shared-facility or service options that must solve a named geometry or performance problem before extra spending is justified.

The comparison register is [`data/conductive-coating-methods.csv`](data/conductive-coating-methods.csv). The costs are planning allowances rather than quotations and must be replaced by current local prices before purchase.

---

## 11. Evidence and Decision Gates

A **gate** is a decision point that must pass before the next stage begins.

| Gate | Decision | Required evidence |
|---|---|---|
| G0 | Is the project safe and understandable? | approved scope, risk controls, explained terms |
| G1 | Do the measurement tools work? | reference measurements and fault tests |
| G2 | Does the simple model work? | hand calculations and automated software tests |
| G3 | Are the designs ready to make? | drawings, dimensions, print and plating access review |
| G4 | Are the samples traceable? | sample identifiers, photos, mass, process records |
| G5 | Are the measurements repeatable? | three samples per design and uncertainty notes |
| G6 | Did repair restore useful performance? | original, damaged, and repaired comparison |
| G7 | Is the result ready to communicate? | student report, lecturer review, and funder summary |

The letter **G** means Gate. The number gives the sequence.

---

## 12. Success Measures

The teaching demonstration succeeds when:

- all tests remain within the approved 5 V and 2 A envelope;
- the negative or deliberately weakened condition is detectable;
- resistance and temperature are recorded for every functional sample;
- the simple software correctly predicts the order from best to worst for most samples;
- one repair cycle is completed and evaluated honestly;
- the direct cost remains within the approved student budget;
- a non-engineering reader can explain what was built, what was learned, and what remains uncertain.

The project can still receive a strong result if the repair fails, provided the failure is measured, explained, and used to improve the next plan.

---

## 13. Document Tree

### Start Here

- [Classroom Demonstration Overview](index.md)
- [Student Learning and Project Guide](student-project.md)

### Student Study Support

- [Student Glossary and Acronym Guide](student-glossary.md)
- [Student Reading and Study Guide](student-reading-guide.md)

### Build and Budget

- [Low-Power Construction Plan](low-budget-construction-plan.md)
- [Student Bill of Materials](bill-of-materials.md)
- [JG MAKER Artist-D Dual-Material Copper Electroplating Plan](artist-d-electroplating-plan.md)

### Conductive Coating Methods

- [Ten Complete Conductive Coating Method Plans](conductive-coatings/index.md)
- [C01 Gantry-Dispensed Conductive Coating](conductive-coatings/gantry-dispensed-coating.md)
- [C02 Robotic Airbrush or Spray Coating](conductive-coatings/robotic-spray-coating.md)
- [C03 Automated Electroless Seed Coating](conductive-coatings/automated-electroless-seed.md)
- [C04 Inkjet-Printed Catalyst or Metal Seed](conductive-coatings/inkjet-catalyst-seed.md)
- [C05 Aerosol Jet Printed Seed](conductive-coatings/aerosol-jet-seed.md)
- [C06 Laser Direct Structuring](conductive-coatings/laser-direct-structuring.md)
- [C07 Flash Ablation Metallization](conductive-coatings/flash-ablation-metallization.md)
- [C08 Physical Vapor Deposition Seed Layer](conductive-coatings/physical-vapor-deposition.md)
- [C09 Laser-Induced Graphene Seed](conductive-coatings/laser-induced-graphene.md)
- [C10 Catalyst-Loaded Multi-Material Resin](conductive-coatings/catalyst-loaded-resin.md)

### Teaching and Funding

- [Lecturer Guide](lecturer-guide.md)
- [Business Funder Brief](business-funder-brief.md)

### Improvement Record

- [Project Rewrite, Problem, and Fix Log](project-rewrite-plan.md)
- [Project Diagram Implementation and Coverage Plan](diagram-implementation-plan.md)

---

## 14. Final Plain-Language Summary

AE3PT-Lite is a small classroom experiment about whether a copper-coated printed electrical path can be designed with less material and repaired after damage. Students learn the science, build low-power tools, make samples, collect evidence, and explain the financial meaning.

The project is deliberately modest. Its value comes from completing the whole loop and making each claim understandable to students, lecturers, and business decision-makers.
