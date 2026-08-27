# Adaptive Electroformed 3D Power Topology Lite (AE3PT-Lite): First-Year Reading and Activity Guide

## Short Readings That Lead Directly to Calculations, Builds, or Decisions

> **Reading rule:** Read a small section, use it immediately, and produce evidence. A long unused reading list is not project progress.

**AE3PT-Lite** means **Adaptive Electroformed 3D Power Topology Lite**, the five-volt classroom project supported by this reading path.

---

## 1. How to Study Each Topic

For every reading, answer:

1. What problem is being explained?
2. Which new words must be defined?
3. What simple equation or diagram is useful?
4. What assumption is being made?
5. What activity will check the idea?
6. What result would show the idea is wrong or incomplete?

Write a one-page note and link it to a calculation, software test, sample, risk control, or business decision.

---

## 2. Week 1 — Electricity Without Jargon

Read an introductory circuit chapter covering voltage, current, resistance, power, series paths, and parallel paths.

Recommended accessible starting point:

- OpenStax, *University Physics Volume 2*, sections on current, resistance, and direct-current circuits.[1]

Activity:

- draw the five-volt test circuit;
- label where current flows;
- identify where voltage is measured;
- calculate current through a 10 Ω resistor.

---

## 3. Week 2 — Engineering Calculations

Read the introductory resistance and node-voltage sections of a circuits textbook such as Nilsson and Riedel, *Electric Circuits*.[2]

Activity:

- calculate one straight copper section by hand;
- calculate two sections in series;
- calculate two equal branches in parallel;
- turn each result into an automated software test.

> **Practical tip:** A correct one-page hand calculation is more valuable than copying a large simulation you cannot explain.

---

## 4. Week 3 — 3D Printing for Function

Read introductory material-extrusion and Design for Additive Manufacturing sections from Gibson and co-authors, *Additive Manufacturing Technologies*.[3] **Computer-Aided Design (CAD)** means using software to create and dimension the part.

Activity:

- print a width-and-hole coupon;
- measure it with a calliper;
- record which dimensions are consistently too large or too small;
- update the CAD design rules.

---

## 5. Week 4 — Measurement and Uncertainty

Read the National Institute of Standards and Technology introduction to **measurement uncertainty**, meaning reasonable doubt associated with a measured value.[4]

Activity:

- measure the same resistor five times;
- calculate the mean and range;
- list at least four reasons the value could vary;
- write the result with units and sensible decimal places.

---

## 6. Week 5 — Four-Wire Resistance Measurement

Read the Keithley/Tektronix low-resistance measurement guide.[5] A **four-wire measurement** uses one pair of wires to carry current and another pair to measure voltage.

Activity:

- draw thick current wires in red;
- draw thin voltage-sense wires in blue;
- explain why the voltage-sense wires are placed inside the current contacts;
- compare two-wire and four-wire readings if a suitable reference is available.

---

## 7. Week 6 — Temperature and Heat

Read introductory energy-balance and thermal-resistance material from Bergman and co-authors, *Fundamentals of Heat and Mass Transfer*.[6] **Thermal resistance** describes how difficult it is for heat to leave an object.

Activity:

- calculate electrical power at 0.5 A, 1 A, and 1.8 A;
- predict which test should heat fastest;
- draw arrows showing heat leaving the sample;
- state why the temperature model will be approximate.

---

## 8. Week 7 — Python and Automated Tests

Use the official Python tutorial and pytest getting-started guide.[7][8] **Python** is the programming language used for the project. An **automated test** is code that checks other code.

Activity:

- create a project environment;
- run one Python file;
- write one passing calculation test;
- write one test that confirms negative dimensions are rejected;
- record the command needed to run all tests.

---

## 9. Week 8 — Copper Electroplating

Read selected introductory chapters from *Modern Electroplating* under lecturer guidance.[9]

**Electrodeposition** is electrically driven metal deposition. **Electroplating** deposits a coating that stays on the base. **Electroforming** builds a more substantial metal form. Read for mechanism and process variables, not for unsupervised chemical recipes.

Activity:

- draw the approved process flow;
- identify which responsibilities belong to students and which belong to the laboratory;
- create the plating process traveller;
- explain why edges may receive more deposit than hidden regions.

### Optional conductive-coating comparison

Open the [Conductive Coating Methods library](conductive-coatings/index.md) and compare C01, C03 and one advanced service method. For each route, identify the full acronym, geometry advantage, main safety authority, trial cost, ownership cost, first pass/fail gate and lower-cost fallback. The activity is complete only when the student can explain why the most technically advanced machine is not automatically the best project choice.

---

## 10. Week 9 — Experimental Comparison

Read an introductory source on experiments, controls, replicates, and randomization supplied by the lecturer. A **control** is a comparison condition. An **independent variable** is deliberately changed; a **dependent variable** is measured; a **controlled variable** is held as constant as practical. A **replicate** is a separately manufactured copy. **Randomization** means mixing test order to reduce time-order bias.

Activity:

- identify the independent variable: design;
- identify dependent variables: resistance and temperature;
- list controlled variables;
- create a randomized sample test order;
- explain why three separate samples are used.

---

## 11. Week 10 — Repair and Circular Design

Use the Circular Design Guide to map repair, reuse, replacement, and recovery.[10]

Activity:

```text
plastic and copper
→ manufacture
→ test
→ use
→ inspect
→ damage
→ repair or replace
→ reuse or recover
```

Mark where money, material, time, and information are lost.

---

## 12. Week 11 — Engineering Economics

Read a first-year introduction to **engineering economics**, meaning financial comparison of engineering choices. Cover cost, **cash flow**, meaning money entering or leaving over time, payback, and uncertainty. **Payback** asks how many uses or repairs are needed to recover extra initial cost. Lecturer-selected library texts are appropriate.

Activity:

- separate capital equipment from consumables;
- calculate cost per successful sample;
- calculate direct repair and replacement cost;
- estimate the number of repairs needed to recover extra repair-ready design cost;
- list reasons the estimate may change at larger scale.

---

## 13. Week 12 — Communicating to Business Readers

Read a short guide on executive summaries and evidence-based recommendations supplied by the lecturer. An **executive summary** is a short decision-focused explanation written for a reader who may not read the full technical report.

Activity:

Write one page containing:

- the problem;
- what was built;
- what was measured;
- the most important technical result;
- the direct cost;
- the main remaining risk;
- the recommended next decision.

Avoid unexplained acronyms and marketing claims.

---

## 14. Reading Notes for Lecturers

- Provide page or section ranges rather than whole-book assignments.
- Ask students to bring one calculation or diagram from each reading.
- Use short quizzes on meaning and units, not memorized history.
- Pair engineering and business students for explanation exercises.
- Ask students to identify assumptions and limitations.
- Accept library editions when the same fundamental topic is covered.
- Do not require students to purchase all recommended books.

---

## 15. Reading Notes for Business Funders

Funders do not need to study circuit theory. Useful reading outputs are:

- one-page plain-language project overview;
- cost categories and assumptions;
- repair-versus-replacement calculation;
- risk register;
- gate results;
- recommendation for stop, repeat, or expand.

The reading programme is valuable because it connects technical learning to measurable decisions.

---

## 16. Reading Evidence Gate

The reading programme passes when students produce:

- one circuit diagram;
- three hand calculations;
- one print-capability table;
- one measurement uncertainty note;
- one four-wire diagram;
- one heat-flow sketch;
- at least five automated tests;
- one approved plating process map;
- one randomized experiment table;
- one lifecycle map;
- one repair-versus-replacement calculation;
- one plain-language executive summary.

---

## References

1. OpenStax, [University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2).
2. Pearson, [Electric Circuits, Twelfth Edition](https://www.pearson.com/en-ca/subject-catalog/p/electric-circuits/P200000003451/9780137648276).
3. Springer Nature, [Additive Manufacturing Technologies, Third Edition](https://link.springer.com/book/10.1007/978-3-030-56127-7).
4. National Institute of Standards and Technology, [NIST Technical Note 1297: Measurement Uncertainty](https://www.nist.gov/pml/nist-technical-note-1297).
5. Tektronix/Keithley, [Accurate Low-Resistance Measurements Start with Identifying Sources of Error](https://www.tek.com/en/documents/whitepaper/accurate-low-resistance-measurements-start-identifying-sources-error).
6. Wiley, [Fundamentals of Heat and Mass Transfer, Eighth Edition](https://www.wileyplus.com/engineering-and-materials-science/bergman-fundamentals-heat-mass-transfer-8e-eprof18094/).
7. Python Software Foundation, [Python Tutorial](https://docs.python.org/3/tutorial/).
8. pytest contributors, [pytest Get Started](https://docs.pytest.org/en/stable/getting-started.html).
9. Wiley Online Library, [Modern Electroplating, Fifth Edition](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470602638).
10. Ellen MacArthur Foundation and IDEO, [The Circular Design Guide](https://www.circular.design/).
