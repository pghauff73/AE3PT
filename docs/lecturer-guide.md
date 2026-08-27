# Adaptive Electroformed 3D Power Topology Lite (AE3PT-Lite): Lecturer Guide

## Teaching a 24-Week, Five-Volt, Repairable-Conductor Demonstration

> **Teaching purpose:** Introduce first-year students to the complete engineering cycle without requiring high power, advanced mathematics, or uncontrolled chemical work.

**AE3PT-Lite** means **Adaptive Electroformed 3D Power Topology Lite**, the reduced classroom demonstration.

AE3PT-Lite combines electrical basics, 3D printing, simple software, measurement, repair, and business reasoning. The learning outcome is not a commercially ready conductor. It is a **traceable** demonstration, meaning each claim can be followed back to a calculation, sample, measurement, cost, or approval.

---

## 1. Recommended Student Cohort

Suitable for:

- first-year electrical, mechanical, mechatronic, manufacturing, or general engineering;
- mixed engineering and business innovation classes;
- maker-experienced students needing stronger experimental discipline;
- teams of three or four students.

Students need only introductory algebra, basic spreadsheet or Python exposure, simple **Computer-Aided Design (CAD)** familiarity, and supervised workshop practice.

---

## 2. Teaching Model

Use the repeating sequence:

```text
explain
→ calculate
→ build
→ measure
→ interpret
→ communicate
```

Each lesson should produce evidence. For example:

- a circuit lesson produces a labelled circuit and calculation;
- a CAD lesson produces a dimensional coupon;
- a measurement lesson produces a calibration record;
- an economics lesson produces a repair-versus-replacement comparison.

> **Lecturer principle:** Students should never perform a practical activity containing a term they cannot explain in ordinary language.

---

## 3. Suggested Team Roles

Rotate roles so every student experiences technical and communication work.

### Design lead

Maintains CAD files, dimensions, sample identifiers, and print records.

### Measurement lead

Maintains the fixture, logger, calibration, sensor placement, and raw data.

### Software and analysis lead

Maintains calculations, automated tests, **Comma-Separated Values (CSV)** import, charts, and report generation.

### Business and evidence lead

Maintains actual costs, decision gates, risk summary, repair comparison, and plain-language explanation.

For teams of three, combine business/evidence with design or analysis but rotate after Gate G3.

---

## 4. Course Entry Activity

Ask every team to explain, without acronyms:

1. what the object does;
2. why copper is used;
3. why plastic is printed;
4. why three shapes are compared;
5. why one shape is repaired;
6. what evidence would justify a larger project.

Students who cannot yet answer should use the [Classroom Overview](index.md) and [Glossary](student-glossary.md) before proceeding.

---

## 5. Twenty-Four-Week Teaching Sequence

**Calibration** means comparing an instrument with a reference. **Measurement uncertainty** means reasonable doubt about a measured value.

| Weeks | Topic | Student output | Gate |
|---|---|---|---|
| 1–2 | language, purpose, limits, risk | one-page explanation and approved risk boundary | G0 |
| 3–5 | circuits, resistance, power, CAD coupons | hand calculations and measured coupons | — |
| 4–7 | logger and fixture | calibration and fault-test record | G1 |
| 6–9 | Python calculations and tests | reproducible example report | G2 |
| 8–11 | final design and print preparation | frozen CAD and process review | G3 |
| 11–14 | seed and supervised plating | nine traceable samples | G4 |
| 15–18 | electrical and thermal test | repeated data and uncertainty notes | G5 |
| 19–21 | damage, repair, and retest | recovery and cost comparison | G6 |
| 22–24 | report, demonstration, and decision | technical report and funder brief | G7 |

---

## 6. Laboratory Release Gates

### G0 — Scope and safety

Pass when:

- supply is limited to 5 **Volts Direct Current (VDC)** and 2 amperes;
- a 2.5 A fuse and physical switch are specified;
- 50 °C is the maximum measured surface temperature;
- chemical responsibilities are assigned to an approved laboratory or service;
- students can explain each hazard and stop condition.

### G1 — Measurement tools

Pass when:

- the fixture has been tested with a safe reference link;
- current remains below 2 A;
- temperature channels are correctly labelled;
- the automatic or supervised stop rule works;
- raw voltage, current, and temperature are retained.

### G2 — Calculation software

Pass when:

- the straight-path hand calculation and Python result agree;
- invalid dimensions fail clearly;
- units are visible;
- automated tests pass from a clean environment.

### G3 — Design freeze

Pass when:

- all three designs use the same terminal spacing and test length;
- probe pads are accessible;
- Design C has a practical repair zone;
- sample identifiers are built into or permanently added to the part;
- any later change creates a new version.

### G4 — Manufacturing evidence

Pass when every sample has print, seed, plating, mass, photograph, and defect records.

### G5 — Measurement evidence

Pass when all nine samples are tested, repeated measurements are stable enough to compare designs, and failed samples remain in the dataset.

### G6 — Repair evidence

Pass when original, damaged, and repaired states are measured and both electrical and thermal criteria are evaluated.

### G7 — Communication

Pass when a non-engineering reviewer can summarize the experiment, evidence, cost, and remaining risk.

---

## 7. Assessment Rubric

| Area | Weight |
|---|---:|
| clear explanation and correct terminology | 12% |
| safe scope and disciplined gate use | 12% |
| hand calculations and simple software | 15% |
| measurement-tool construction and calibration | 15% |
| printing and manufacturing records | 12% |
| experimental method and data quality | 14% |
| damage, repair, and economics | 10% |
| report, demonstration, and teamwork | 10% |

Award marks for visible reasoning and traceability. Do not reward unsupported complexity.

---

## 8. Common Misconceptions to Correct

### “Low voltage means no hazard”

Correct response: low voltage reduces shock risk, but current can heat resistors, wires, contacts, and samples.

### “The software answer is the true answer”

Correct response: the simple **model**, meaning a simplified calculation of the real object, is a prediction based on assumptions. Measurement tests whether it is useful.

### “Three readings are three samples”

Correct response: three readings from one sample test measurement variation. Three independently manufactured samples test manufacturing variation.

### “Copper mass gain proves uniform coating”

Correct response: total mass gives average deposition but cannot prove local thickness.

### “The repair looks complete”

Correct response: visual appearance is not enough. Resistance and temperature must be retested.

### “Cheaper material means cheaper product”

Correct response: process time, failed samples, inspection, repair, and delay also affect cost.

---

## 9. Questions for Oral Examination

1. Explain voltage, current, resistance, and power without using an equation.
2. Why does Design A exist?
3. Why are three samples of each design required?
4. What does the current shunt do?
5. Why are separate voltage-sense wires used?
6. Which assumption most affects the simple resistance calculation?
7. Why can total copper mass hide a local defect?
8. What result would cause the 1.8 A test to be cancelled?
9. Why could resistance recover while temperature remains poor?
10. Which cost is shared equipment and which cost is consumed by one sample?
11. What does this project prove?
12. What does it not prove?

---

## 10. Mixed Engineering and Business Delivery

Pair students for “translation reviews.” The engineering student explains one technical result; the business student restates it as a decision with cost, benefit, and uncertainty. Roles then reverse.

Suggested business outputs:

- unit cost of each design;
- cost per successful sample;
- repair and replacement cost;
- simple payback estimate;
- **risk matrix**, meaning a table comparing the likelihood and consequence of risks;
- stop/repeat/expand recommendation.

Suggested engineering outputs:

- calculation and assumptions;
- design drawing;
- calibration result;
- measured comparison;
- defect explanation;
- repair recovery result.

---

## 11. Inclusive Teaching Notes

- Provide a plain-language glossary before equations.
- Show a physical resistor, wire, printed coupon, and plated sample.
- Use colour-coded current and voltage-sense wiring.
- Allow spreadsheet calculation before Python where needed.
- Pair code with a hand calculation.
- provide labelled example data before students collect their own.
- assess explanation, not only speed of construction.
- avoid assuming prior electronics hobby experience.

---

## 12. Lecturer Preparation Checklist

- approved five-volt supply and fuse arrangement;
- guarded load-resistor fixture;
- one trusted multimeter;
- current-shunt reference calculation;
- temperature-sensor comparison setup;
- printer capability coupon;
- approved seed and plating route;
- approved damage method;
- sample storage and waste route;
- starter Python repository;
- example CSV file;
- assessment and gate sheets;
- non-technical review panel or business guest.

---

## 13. Lecturer Stop Rules

Stop or pause the project when:

- students cannot explain the activity;
- a gate lacks evidence;
- sample identity is lost;
- current exceeds 2 A;
- a required temperature channel fails;
- any temperature reaches 50 °C;
- chemical work is attempted outside the approved process;
- a design change is not versioned;
- reported results exclude unexplained failures;
- commercial claims exceed the evidence.

---

## 14. Recommended Final Review Panel

Include:

- one engineering lecturer;
- one laboratory or workshop representative;
- one non-engineering business or economics reader;
- optionally one student from another team.

Ask each reviewer to identify one clear strength, one unsupported claim, one missing cost, and one recommended next experiment.

---

## 15. Lecturer Completion Standard

The course is complete when students can connect every final claim to a calculation, software test, sample, measurement, cost record, or stated limitation—and a non-technical reviewer can understand that chain.
