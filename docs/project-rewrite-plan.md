# Adaptive Electroformed 3D Power Topology Lite (AE3PT-Lite): Document Rewrite, Problem, and Fix Log

## Plan Based on the Existing HyperText Markup Language (HTML) Document Tree

> **Purpose:** Record the problems found in the original tree, the correction plan, the implementation loops, and the evidence required before declaring the rewrite complete.

**AE3PT-Lite** means **Adaptive Electroformed 3D Power Topology Lite**. A **Bill of Materials (BOM)** is the controlled parts-and-cost list. **CSV** means **Comma-Separated Values**. **Scalable Vector Graphics (SVG)** is the text-based format used for the timeline. **HyperText Markup Language (HTML)** structures the website. **Markdown** is the plain-text writing format converted into HTML. **USD** means **United States dollars**.

This log is written so students, lecturers, and funders can see how document quality was improved. It is not a marketing document.

Problem labels use **P** for **Problem** followed by a sequence number. Correction labels use **F** for **Fix** followed by a sequence number. These labels belong only to this audit record.

---

## 1. Original Tree Audited

The generated HTML site originally indexed six Markdown documents:

1. complete project essays;
2. full bill of materials;
3. low-budget construction plan;
4. student project guide;
5. student glossary;
6. student reading guide.

The HTML interface also provided search, navigation, reading progress, lesson completion, and a timeline image.

---

## 2. Problems Found in Audit Loop 1

### Problem P1 — Scale conflict

The tree mixed a small student guide with research-scale motor, inverter, high-current, computational fluid dynamics, and multi-year plans.

**Evidence found:** the low-budget plan described 60 months and approximately $184,530; the full BOM exceeded $1 million; the student guide used 24 V and 10 A.

### Problem P2 — Audience conflict

The main guide targeted third-year or graduate hobby users, while the new audience is first-year students and non-technical business readers.

### Problem P3 — Budget conflict

The website displayed three incompatible budget levels without one active classroom baseline.

### Problem P4 — Schedule conflict

The timeline used 36 teaching weeks, which did not match a normal 24-week two-semester teaching plan.

### Problem P5 — Vocabulary burden

Advanced concepts appeared before a first-year reader had a physical picture of the demonstration.

### Problem P6 — Missing audience documents

There was no dedicated lecturer delivery guide and no funder decision brief.

### Problem P7 — No visible correction loop

Problems and fixes were not recorded as a document-tree artifact.

---

## 3. Correction Plan from Audit Loop 1

### Fix F1 — One baseline

Use one baseline across every generated document:

- 5 **Volts Direct Current (VDC)** supply;
- maximum 2 A;
- approximately 0.5, 1.0, and 1.8 A test points;
- 50 °C stop;
- three designs;
- three samples per design;
- one repair cycle;
- 24 teaching weeks;
- approximately USD $1,555 direct team budget.

### Fix F2 — One audience ladder

Write in this order:

1. everyday explanation;
2. first-year technical meaning;
3. calculation or build activity;
4. evidence gate;
5. business meaning.

### Fix F3 — Explain at first encounter

Spell out acronyms and define terms before use. Add a plain-language glossary including technical, experimental, safety, and business terms.

### Fix F4 — Replace research-scale documents

Rewrite the full essays, full BOM, and low-budget plan rather than placing a small disclaimer above them.

### Fix F5 — Add role-specific notes

Create lecturer and business-funder documents in the same HTML tree.

### Fix F6 — Align data and graphics

Replace both machine-readable BOM files and the 36-week timeline so they agree with the active baseline.

### Fix F7 — Audit again

Search all generated source documents for conflicting voltage, current, budget, schedule, and research-scale terms. Render desktop and mobile views and correct discovered problems.

---

## 4. Implementation Loop 1

Completed changes:

- replaced research-scale overview with classroom overview;
- replaced million-dollar BOM with one-team and cohort student BOMs;
- replaced 60-month construction plan with low-voltage tools and fixtures;
- rewrote student guide for first-year entry;
- expanded glossary to include business terms;
- changed reading path to short applied activities;
- added lecturer guide;
- added business-funder brief;
- created this audit and fix log.

Pending at the end of Loop 1:

- replace machine-readable BOM registers;
- replace 36-week SVG timeline;
- update HTML document grouping and descriptions;
- run conflict searches;
- inspect rendered pages;
- correct Loop 2 problems.

---

## 5. Acceptance Requirements for Audit Loop 2

| Requirement | Evidence needed |
|---|---|
| all generated documents use student scale | no active research-scale specification remains |
| low power is consistent | 5 VDC and maximum 2 A in overview, guide, construction, BOM, lecturer, and funder documents |
| first-year organization | concepts precede equations and builds |
| non-technical readability | plain-language summaries and business meanings |
| acronyms explained | first-use expansions plus glossary |
| lecturer notes exist | lecturer guide indexed and rendered |
| funder notes exist | funder brief indexed and rendered |
| plan/fix loop exists | this document records problems, fixes, and second audit |
| costs align | Markdown and CSV totals match stated budgets |
| schedule aligns | Markdown and SVG use 24 teaching weeks |
| website works | build, JavaScript, links, SVG, desktop, and mobile checks pass |

---

## 6. Rules for Reporting Problems

Every problem record must contain:

- identifier;
- source file or rendered page;
- observed conflict;
- effect on student, lecturer, or funder;
- correction;
- verification result.

Do not report “fixed” until the current source and rendered output have been checked.

---

## 7. Loop 2 Record

The second audit tested current source, generated data, JavaScript, local links, budget totals, the SVG timeline, desktop rendering, mobile rendering, and audience-specific pages.

### Problem P8 — Acronym first-use defects

Several standalone documents displayed AE3PT-Lite in the title before showing the full name. Some tables used VDC, ADC, USB, PPE, PLA, PETG, or USD before expansion.

**Correction:** Expand the project name in every document title; place full names before shortened forms; remove unexplained shorthand from the standalone timeline.

**Verification:** All nine document titles contain “Adaptive Electroformed 3D Power Topology Lite”; the glossary and first-use audit cover the remaining abbreviations.

### Problem P9 — Obsolete HTML shortcut

The “Project gates” button still targeted the removed 36-week section.

**Correction:** Point the shortcut to the current “Twenty-Four-Week Plan” section.

**Verification:** The generated heading identifier exists and local navigation resolves to it.

### Problem P10 — Long educational titles in navigation

Full first-use titles made the document tree difficult to scan.

**Correction:** Keep full titles in document heroes while providing short, audience-friendly labels in the navigation profile.

**Verification:** Desktop screenshots show clear short labels and complete expanded hero titles.

### Problem P11 — Budget and data drift risk

Narrative totals could differ from machine-readable data.

**Correction:** Replace both BOM files and recompute totals from their `extended_cost_usd` columns.

**Verification:** The one-team file totals $1,555 and the four-team cohort file totals $7,700 exactly.

### Problem P12 — Timeline and course mismatch

The former 36-week timeline conflicted with the current course.

**Correction:** Replace it with a 24-week, 5-volt, maximum-2-ampere timeline and full plain-language labels.

**Verification:** SVG **Extensible Markup Language (XML)** validation and a 1500 × 920 browser screenshot pass.

### Problem P13 — Secondary terms remained unexplained

The first rewrite expanded major acronyms but still used several teaching, measurement, manufacturing, and business terms before defining them. Examples included current-limited supply, model, firmware, stripboard, one-wire data bus, infill, process traveller, resistance reference, control, cash flow, direct cost, and risk matrix.

**Correction:** Add short everyday definitions at the first meaningful use of each term, while keeping the detailed glossary as a second reference.

**Verification:** The final source audit finds the added definitions in the overview, construction plan, Bill of Materials, reading guide, lecturer guide, and funder brief. Generated pages are rebuilt and visually checked after the correction.

### Problem P14 — Mathematical notation displayed as raw markup

Display equations used dollar-sign delimiters and LaTeX commands such as `\\frac`, `\\times`, and `\\rho`. The basic Markdown renderer displayed those commands as text instead of mathematical notation. Markdown also misread the superscript in `I^2R`, causing the exponent to include the following symbol.

**Correction:** Add an offline build-time converter for the mathematical subset used by the course. It converts display and inline notation to native **Mathematical Markup Language (MathML)**, adds spoken accessibility labels, and gives display equations a responsive educational card style. Replace the long word-based thermal expression with the compact standard form \(\Delta T\approx P\times R_{\theta}\), followed immediately by definitions of every symbol.

**Verification:** The regenerated bundle contains 10 display equations and 18 inline mathematical expressions. Every expression is valid MathML with a non-empty accessibility label; no raw mathematical delimiters or LaTeX commands remain in generated HTML; desktop and mobile formula previews pass visual inspection without horizontal overflow.

### Loop 2 status

**PASS.** No active research-scale voltage, current, schedule, budget, motor, inverter, or computational-fluid-dynamics specification remains outside this historical problem record. The nine documents present at the end of this loop were represented in the generated HTML tree.

---

## 8. Final Verification Record

The final correction loop produced the following evidence:

- the Markdown-to-HTML build completed for all ten current documents;
- both JavaScript files passed syntax checks;
- the student timeline and the original ten project-step SVGs passed SVG/XML validation;
- all local document, data, and diagram links resolved;
- all 32 HTML identifiers used by JavaScript existed;
- all ten documents had navigation profiles and expanded project titles;
- the one-team data file contained 50 rows and totalled exactly USD $1,555;
- the four-team data file contained 29 rows and totalled exactly USD $7,700;
- the active-document scale scan found no research-scale values or methods;
- desktop, mobile, lecturer, funder, timeline, coverage-map, and representative phase-diagram screenshots passed visual review;
- all mathematical expressions were converted to accessible native MathML and checked on desktop and mobile;
- ten recommended reading links were checked: nine returned a successful page response, while the Wiley *Modern Electroplating* page rejected the automated request but was independently confirmed by its exact title and Digital Object Identifier.

### Final known limitations

- prices remain planning estimates rather than supplier quotations;
- the copper process still requires an approved laboratory or external service;
- the constructed meters are teaching instruments, not certified instruments;
- the experiment does not prove industrial durability, environmental superiority, or commercial return;
- a lecturer must still approve local safety controls, facilities, and assessment rules.

### Final rewrite gate

**PASS.** The active HTML document tree now describes one small, low-power, testable first-year project; explains the project name, important concepts, acronyms, units, and internal code origins; includes lecturer and business-funder guidance; supplies readings and practical activities; provides complete visual coverage of every teaching phase; and preserves a visible problem–fix–verification loop.

---

## 9. Diagram Coverage Implementation Loop

### Problem P15 — The timeline did not fully represent each project step

The existing timeline showed when work occurred but did not explain the complete inputs, tools, actions, safety stops, evidence, gate, and handoff for each of the nine student phases. Other SVG files in the directory belonged to the earlier research-scale concept and were not linked to the active first-year guide.

### Implementation plan

1. derive nine authoritative phases from the Twenty-Four-Week Plan;
2. require every phase diagram to show purpose, inputs, tools, five actions, phase-specific detail, safety, evidence, gate, and handoff;
3. generate D01–D09, one complete coverage map, and one Artist-D equipment-reference workflow from one controlled specification;
4. generate a machine-readable manifest from the same source;
5. embed every SVG under its matching student phase with a full-size link and caption;
6. add a diagram implementation and maintenance plan to the HTML tree;
7. validate XML, accessibility, source-to-manifest coverage, generated links, drift, desktop rendering, and mobile embedding.

### Correction

Add `tools/build_project_diagrams.py`, nine detailed phase SVGs, `student-project-step-map.svg`, `artist-d-dual-material-plating-workflow.svg`, and `data/student-diagram-manifest.csv`. Add the [Project Diagram Implementation and Coverage Plan](diagram-implementation-plan.md) as the tenth document. Keep the timeline as the schedule view, use the phase set as the operational view, and use the Artist-D diagram as the optional equipment workflow supporting D05 and D06.

### Verification requirements

- generator check mode reports no drift;
- the manifest has D01–D09 exactly once;
- every manifest section exists in the student guide;
- every phase section references its matching SVG exactly once as an image and once as a full-size link;
- all eleven generated SVGs are valid XML with accessible titles and descriptions;
- the coverage map reports nine of nine phases;
- representative electrical, manufacturing, testing, repair, decision, coverage, and Artist-D diagrams pass full-size visual review;
- the complete Markdown, JavaScript, MathML, link, budget, and active-scope regression gates still pass.

### Diagram coverage gate

**PASS only when all verification requirements above are proved from current generated artifacts.**

---

## 10. Artist-D Selective-Plating Option Loop

### Problem P16 — Dual extrusion could be mistaken for a finished conductor

The Artist-D can place conductive and non-conductive filament in one print, but ordinary conductive PLA remains far more resistive than copper. Without a machine-specific explanation, students could treat a continuity beep as proof that a 100 mm seed route will plate uniformly or carry the final sample current.

### Implementation plan

1. record official machine limits without implying that every material pairing is approved;
2. define Independent Dual Extrusion, direct drive, conductive filament, selective electroplating, and tool offset;
3. assign non-conductive PLA and conductive PLA to separate labelled extruders;
4. add alignment, isolation, resistance, voltage-drop, and supervised-plating coupon checks;
5. preserve the surface-applied seed as the project baseline and fallback;
6. add a separate optional Bill of Materials register rather than changing the baseline cost;
7. link the equipment workflow from the construction and student guides.

### Correction

Add the Artist-D setup, material-selection reasoning, 15 preparation micro-steps, mode guidance, seed equations, pass/fail gates, optional cost allowance, machine-readable option register, glossary definitions, generated workflow SVG, and a dedicated machine-specific HTML document. Explain the 300 mm × 300 mm × 340 mm build volume, substantially preassembled construction, 1.75 mm direct-drive IDEX arrangement, overall difficulty 4/5, and the voltage-drop and current-crowding problems of conductive filament. Update D05 and D06 so the phase diagrams require an approved seed route and record seed resistance and voltage drop.

### Verification requirements

- the baseline $1,555 project remains possible without conductive filament;
- the Artist-D option register is separate and internally consistent;
- the student and construction guides link the generated workflow SVG;
- the dedicated Artist-D plan appears in the Build and Budget HTML tree;
- conductive filament is described as a seed rather than the final power conductor;
- the difficulty rating separates simple mechanical setup from advanced IDEX, seed and plating work;
- a continuity beep is explicitly rejected as evidence of uniform plating-current distribution;
- failed IDEX coupons return to surface-applied seed rather than uncontrolled chemistry changes;
- the revised mathematical area notation defines copper width, thickness, and cross-sectional area explicitly;
- generator, XML, accessibility, document-build, MathML, and link checks pass.

### Artist-D option gate

**PASS only when the optional route is technically bounded, coupon-first, laboratory-controlled, cost-separated, and visibly fail-closed.**

---

## 11. Automated Conductive-Coating Method Loop

### Problem P17 — Ten coating suggestions were not yet complete engineering plans

The project identified multiple ways to automate conductive seed deposition, but a short suggestion list did not tell a student what to build or book, what each acronym meant, how much to budget, what evidence to collect, when to stop, or how to return to a lower-cost method. Advanced laser, vacuum, aerosol, inkjet and catalyst-resin ideas also risked appearing equivalent to a student-built dispenser even though their safety authority, cost and process difficulty are substantially different.

### Implementation plan

1. define one comparable schema for all ten methods;
2. write exactly three introductory teaching paragraphs for every method;
3. spell out and explain every method acronym on first use;
4. include equipment, materials, prerequisites and complete implementation microsteps;
5. add method-specific safety controls, evidence packages and pass/fail gates;
6. give each method a difficulty score, student trial allowance and ownership allowance;
7. preserve a named lower-cost fallback for every advanced process;
8. generate one accessible SVG per method and one method-selection map;
9. generate one machine-readable cost and difficulty register;
10. add all eleven documents to a dedicated HTML navigation group;
11. verify research links, generated drift, XML, accessibility, links, JavaScript and representative rendering.

### Correction

Add the [Conductive Coating Methods library](conductive-coatings/index.md), ten complete method plans, eleven accessible SVG files under `diagrams/conductive-coatings/`, the machine-readable `data/conductive-coating-methods.csv` register and the authoritative `tools/build_coating_method_plans.py` generator. Add the method acronyms and origins to the glossary, link the library from the overview, and expose cost and difficulty directly in the HTML document tree.

### Verification requirements

- the generator reports eleven Markdown files, eleven SVG files and one CSV register with no drift;
- every method contains exactly three paragraphs in its description section;
- every method has a unique identifier from C01 to C10;
- every method contains difficulty, trial cost, ownership cost, microsteps, pass/fail gates, evidence and fallback;
- every SVG is valid XML and contains a title, description and accessible image role;
- all research and local documentation links resolve;
- the HTML navigation shows a dedicated Conductive Coating Methods group in C01–C10 order;
- advanced methods are described as facility or service routes unless current safety and ownership evidence supports local operation;
- the full documentation build and existing phase-diagram generator remain green.

### Coating-method library gate

**PASS only when all ten suggestions are individually actionable, cost-visible, difficulty-rated, research-grounded, visually explained, fail-closed and discoverable in the generated HTML tree.**
