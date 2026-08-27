# Adaptive Electroformed 3D Power Topology Lite (AE3PT-Lite): Low-Power Construction Plan

## Student-Built Tools, Printed Samples, Software, and Safe Test Fixtures

> **Construction objective:** Build only the tools needed to test 100 millimetre copper-coated samples at 5 volts direct current and no more than 2 amperes.

**AE3PT-Lite** means **Adaptive Electroformed 3D Power Topology Lite**, the reduced classroom version of the project.

This plan assumes access to a computer, a 3D printer that melts filament and builds layer by layer, called **material extrusion**, and an approved copper-coating process called **electroplating**. **Calibration** means comparing an instrument with a reference. The equipment is educational and not intended for certified calibration work, mains electricity, vehicle batteries, or industrial busbars.

---

## 1. System at a Glance

```text
5 V current-limited supply
        ↓
2.5 A fuse and switch
        ↓
student sample
        ↓
selectable load resistor
        ↓
known current-measurement resistor
        ↓
return to supply

sample voltage + shunt voltage + temperatures
        ↓
small controller and data logger
        ↓
measurement data file and Python report
```

A **current shunt** is a known low resistance used to measure current. A **microcontroller** is a small programmable computer used to read sensors and send data. A **data logger** records sensor readings with time. **CSV** means **Comma-Separated Values**, a simple table stored as text.

---

## 2. Safety Boundary

### Electrical limits

- 5 **Volts Direct Current (VDC)** normal supply;
- 2 A maximum test current;
- 2.5 A fuse at the supply output;
- insulated connectors;
- covered load resistors;
- physical power switch;
- automatic stop at 50 °C;
- no connection to mains wiring inside student-built equipment.

A **current-limited supply** automatically restricts excessive current rather than allowing the test circuit to draw without control.

### Chemical limits

Students may design masks, fixtures, labels, and recording forms. They may perform plating only under the approved laboratory procedure or use an approved external service. Students must not formulate chemical baths, change chemical concentrations, or dispose of plating waste independently.

### Mechanical limits

Cutting or abrading plated copper can create sharp edges and particles. Use the approved tool, local containment, eye protection, and cleanup method.

> **Lecturer note:** Treat failure of a sensor, fuse, switch, or data connection as a stop condition. The exercise teaches controlled testing, not endurance.

---

## 3. Student Sample Geometry

Create three approximately 100 mm × 30 mm bases.

### Sample A — Straight reference

- one 10 mm-wide central conductive route;
- enlarged terminal pads;
- two small voltage-sense pads inside the current terminals.

### Sample B — Material-saving route

- wider near terminals;
- narrower in low-current or low-risk regions;
- optional second branch through the middle;
- same terminal locations as Sample A.

### Sample C — Repair-ready route

- same test length as the reference;
- a clearly marked 15 mm repair zone;
- flat mask land around the repair zone;
- probe pads before and after the zone;
- sample identifier moulded or embossed into the print.

### Practice coupons

Print at least six small coupons before functional samples:

- two dimensional coupons;
- two conductive-seed coupons;
- two plating-access coupons.

Coupons are inexpensive test pieces used to learn a process without risking a complete sample.

---

## 4. Low-Voltage Test Fixture

### Function

The fixture sends a known, limited current through the sample and measures voltage and temperature.

### Current steps

Use switchable power resistors to create approximate test points:

| Load resistor | Approximate current from 5 V | Purpose |
|---:|---:|---|
| 10 Ω, 10 W | 0.5 A | first functional check |
| 4.7 Ω, 10 W | 1.0 A | normal comparison |
| 2.7 Ω, 15 W | 1.8 A | short peak comparison |

An **ohm**, written Ω, is the unit of resistance. A **watt**, written W, is the unit of power.

Actual current must be measured because supply voltage, resistor tolerance, wiring, and sample resistance change the result.

### Construction steps

1. Mount the three load resistors on a ventilated non-combustible base.
2. Add a rotary switch or individual covered switches so only one load is selected.
3. Add the 2.5 A fuse and main power switch.
4. Use touch-safe or covered terminals for the student sample.
5. Mount the current shunt away from the sample temperature sensors.
6. Add a clear polycarbonate guard over hot resistors.
7. Label current settings as approximate, not exact.
8. Test the fixture first with a metal reference link.
9. Verify that opening the main switch removes current.
10. Record a photograph and wiring diagram.

### Pass gate

The fixture passes when each switch position produces a stable current below 2 A, the fuse is correctly installed, hot surfaces are guarded, and the main switch reliably removes current.

---

## 5. Voltage and Current Logger

### Purpose

The logger measures:

- voltage across the student sample;
- voltage across the current shunt;
- calculated current;
- calculated sample resistance;
- test time.

### Recommended parts

- Arduino-compatible or similar microcontroller;
- one or two ADS1115 16-bit Analog-to-Digital Converter modules;
- 0.1 Ω, 1%, 3 W current shunt;
- screw terminals;
- fuse-status input if desired;
- Universal Serial Bus cable for data transfer.

An **Analog-to-Digital Converter**, abbreviated ADC, changes an analogue voltage into a digital number. **USB** means Universal Serial Bus.

### Measurement equations

Current is calculated from the shunt:

$$
I=\frac{V_{shunt}}{R_{shunt}}
$$

Sample resistance is calculated from:

$$
R_{sample}=\frac{V_{sample}}{I}
$$

### Four-wire sample connection

Use two thick wires to carry current and two separate thin wires to measure sample voltage. This is called a **four-wire** or **Kelvin** measurement. It reduces the effect of lead and contact resistance.

### Construction steps

1. Assemble the microcontroller and ADC on a solderless breadboard.
2. Read a known low voltage from a resistor divider.
3. Read the shunt voltage at approximately 0.5 A.
4. Compare current with a trusted multimeter.
5. Add separate sample-voltage sense leads.
6. Add input protection recommended by the module documentation.
7. Write **firmware**, meaning software stored on the microcontroller, that records raw ADC counts and converted volts.
8. Calculate current and resistance in the host Python program.
9. Move the verified circuit to **stripboard**, a board with pre-made copper strips, or a simple **Printed Circuit Board**, a custom board connecting components, if required.
10. Place it in a labelled plastic enclosure.

### Calibration checks

Use at least three reference resistors or metal links covering the expected range. Record five repeated measurements at each level.

### Pass gate

The logger passes when raw voltages are retained, current agrees with the reference meter within the agreed classroom tolerance, and repeated sample-resistance readings remain stable enough to separate the three designs.

---

## 6. Digital Temperature Logger

### Purpose

Measure ambient temperature and three sample locations without using an expensive thermal camera.

### Recommended design

Use four DS18B20 digital temperature sensors:

- one ambient sensor;
- one near the input terminal;
- one at the centre or narrowest point;
- one near the output terminal.

DS18B20 is a manufacturer part number, not an acronym.

### Construction steps

1. Connect one sensor and verify its digital address.
2. Add the remaining sensors on the same **one-wire data bus**, a shared communication wire used by several addressed sensors.
3. Label every physical sensor and software channel.
4. Attach all sensors together at room temperature.
5. record their differences for ten minutes.
6. Place them together on a warm, stable reference below 50 °C.
7. Record channel differences again.
8. Attach them to the sample using the same tape, pressure, and location method.
9. Add a software stop when any valid sensor reaches 50 °C.
10. Stop the test if any required sensor becomes invalid.

### Pass gate

The logger passes when channels are correctly identified, readings are repeatable, the stop rule works, and the attachment method is documented.

---

## 7. Printing Tools and Process

Use an available material-extrusion printer. Material extrusion pushes softened filament through a nozzle and builds the part layer by layer.

### JG MAKER Artist-D suitability

The **JG MAKER Artist-D** is a practical machine for the project when it is already owned or can be borrowed. Its most useful feature is **Independent Dual Extrusion**, abbreviated **IDEX**. IDEX means that the left and right print heads move independently rather than sharing one fixed carriage position. For this project, one head can print the insulating body while the other prints a conductive seed route that is intended to receive copper.

The manufacturer documentation identifies a nominal 300 mm × 300 mm × 340 mm build volume, 1.75 mm filament, 0.4 mm nozzles, direct-drive extrusion, a 0.05–0.30 mm layer range, a bed temperature up to 90 °C, and support for materials including Polylactic Acid (PLA), Acrylonitrile Butadiene Styrene (ABS), Thermoplastic Polyurethane (TPU), and Polyvinyl Alcohol (PVA). The manual recommends 30–60 mm/s as the normal printing-speed range. Retail descriptions may say “98% assembled,” but the manual still requires gantry installation, spool-holder installation, cable connection, leveling and calibration. These are machine capabilities and sales descriptions, not automatic approval for every filament pairing or plating process.

**Overall route difficulty: 4/5.** Mechanical completion and ordinary PLA printing are relatively straightforward. The difficulty comes from calibrating two independent nozzles, preventing conductive contamination, proving a stable low-resistance seed, designing plating contacts and obtaining copper at the far end without bridging or peeling.

[![Artist-D dual-material printing and copper-electroplating workflow](diagrams/artist-d-dual-material-plating-workflow.svg)](diagrams/artist-d-dual-material-plating-workflow.svg)

*Machine-specific workflow — the Independent Dual Extruder route is optional and must pass alignment, electrical-seed, and supervised-plating coupon gates.*

The [complete Artist-D Dual-Material Copper Electroplating Plan](artist-d-electroplating-plan.md) consolidates the machine specification, difficulty breakdown, conduction problems, geometry rules, coupon matrix, microsteps and five release gates.

### Recommended material assignment

Use a simple first pairing:

- **left extruder:** natural or light-coloured non-conductive PLA for the sample body, insulating lands, labels, and masking features;
- **right extruder:** carbon-filled conductive PLA for the exposed seed route and enlarged electrical contact pads;
- **final conductor:** laboratory-deposited copper over the accepted seed route.

Conductive PLA is many orders of magnitude more resistive than copper. Published research describes even the best conductive composite thermoplastic filaments as approximately four orders of magnitude less conductive than bulk copper. It should therefore be treated as a temporary distributed electrode or **seed**, not as the final 0.5–1.8 A classroom conductor. A commercial carbon-black conductive PLA, for example, can behave more like a resistor than a wire, and only a sufficiently conductive printed path can distribute plating current over several centimetres.

High seed resistance creates three linked problems. First, voltage is lost along the printed route. Second, current crowds near the plating contact. Third, copper growth near that contact lowers local resistance and can further starve the unplated far end. A continuity beep cannot detect this distribution problem; record numerical resistance and inspect near, middle and far regions during the supervised coupon trial.

Do not assume that a copper-coloured or copper-filled decorative filament is electrically conductive. The material record must state its measured resistance and intended technical function.

### Material combinations to avoid initially

- Do not begin with an ABS body and a PLA-based conductive track. Their different temperatures, shrinkage, and interface behaviour create unnecessary variables.
- Do not begin with a flexible TPU plated sample. TPU is useful for flexible guards, seals, or cable-management fixtures, but bending can crack or delaminate a rigid copper coating.
- Do not pair PETG and conductive PLA for the functional samples until small interface coupons prove adhesion and dimensional stability.
- Do not use soluble PVA as a permanent base beneath the conductive route. PVA is useful only as a removable support where the approved process allows it.

The recommended sequence is PLA plus conductive PLA for the IDEX experiment, while normal PLA or approved PETG with a laboratory-approved surface seed remains the robust baseline.

### Artist-D preparation micro-steps

1. Record the machine serial number, firmware version, nozzle size, and maintenance state.
2. Inspect belts, wiring, fans, hot-end insulation, build surface, filament sensors, and both nozzle brushes.
3. Fit clean 0.4 mm nozzles. Keep spare nozzles available and dedicate the right material path to conductive filament during the trial.
4. Label the left and right spools, extruders, purge areas, and generated tool paths.
5. Dry or condition each filament only according to its supplier instructions.
6. Load ordinary PLA in the left extruder and conductive PLA in the right extruder.
7. Purge each head separately until the previous material is removed. Conductive material in the insulating tool path is a contamination failure.
8. Level the bed using the manufacturer procedure.
9. Calibrate left and right nozzle height so neither nozzle scrapes a previously printed material.
10. Print a two-colour alignment coupon and correct the X and Y tool offsets in the slicer or printer configuration.
11. Print interface coupons with 2 mm, 4 mm, and 8 mm seed widths and at least two seed thicknesses.
12. Record nozzle temperatures, bed temperature, layer height, speeds, cooling, retraction, wiping, purge amount, and visible ooze.
13. Measure the insulating gap, seed width, interface continuity, warping, and dimensional error.
14. Measure end-to-end seed resistance before any chemical work.
15. Release one accepted coupon for supervised plating; do not print the nine functional samples yet.

Use the official PLA and PLA-plus-soluble-support profiles only as starting references. Conductive filament settings come from the actual material supplier and must be requalified on this machine.

### Normal, duplication, and mirror modes

- Use **normal dual-material mode** for a single part containing an insulating body and conductive seed.
- Use **duplication mode** to accelerate setup coupons only when both heads use the same approved material and the slicer output has been checked.
- Use **mirror mode** only for a deliberate left/right geometry experiment.

Two coupons printed simultaneously on one bed are useful process checks, but they are not fully independent manufacturing replicates. Final evidence should include separately started print jobs and more than one bed position so machine position and batch effects can be observed.

### Conductive-seed calculations

Measure the printed seed resistance at a low, safe test current:

$$
R_{seed}=\frac{V_{seed}}{I_{test}}
$$

Use the laboratory-approved estimated plating current to calculate a simple pre-screening voltage drop:

$$
\Delta V_{seed}=I_{plate}R_{seed}
$$

Here, \(R_{seed}\) is the measured end-to-end resistance of the printed seed, \(I_{test}\) is the low measurement current, and \(I_{plate}\) is an estimate supplied or approved by the plating laboratory. This calculation does not replace a plating trial. It helps identify a seed path that is too resistive to distribute plating current to its far end.

### Artist-D pass/fail gates

**Gate A — print and isolation**

**PASS** when the two materials meet continuously, the seed remains exposed, intended insulating gaps remain open, and no conductive ooze bridges separate regions.

**FAIL** when the nozzles are offset, the materials separate during handling, the seed is buried, or unwanted conductive bridges appear.

**Gate B — electrical seed**

**PASS** when every intended seed region is electrically reachable, measured resistance is stable, the calculated seed voltage drop is accepted by the laboratory, and contact pads can be connected without damaging the print.

**FAIL** when the far end is open circuit, resistance changes when the coupon is handled, or the laboratory predicts unacceptable current crowding. The correction is a shorter or wider seed path, larger pads, approved additional contact points, or the surface-applied seed baseline.

**Gate C — supervised plating coupon**

**PASS** when copper begins and continues over the full intended route, the farthest point receives acceptable coverage, insulating regions remain unplated, adhesion is acceptable, and the process record is complete.

**FAIL** when deposition remains near the electrical contact, isolated areas do not plate, copper bridges insulation, the coating lifts, or the laboratory stops the run. Do not raise voltage or change chemistry independently.

Only after Gates A, B, and C pass may the IDEX route be used for A01–C03. A failure does not fail the whole project; it selects the normal polymer plus surface-applied seed route.

Recommended starting material:

- **Polylactic Acid (PLA)** for simple dimensional coupons; or
- **Polyethylene Terephthalate Glycol-modified (PETG)** for functional fixtures when approved for the selected plating process.

Record printer, nozzle, material batch, layer height, wall count, **infill**, meaning the internal printed pattern, orientation, support, print time, actual dimensions, and failed prints.

### Print gate

The print process passes when three repeated coupons remain within the lecturer-approved dimensional range, terminal and repair features are accessible, and any IDEX seed route has passed Gates A and B above.

---

## 8. Conductive Seed and Supervised Plating

Plastic does not normally conduct electricity. A **conductive seed layer** is a thin first coating that allows electroplating current to reach the intended surface.

The seed may be surface-applied to an ordinary print or selectively printed using the Artist-D. The same plating evidence is required for both routes. The printed route does not receive a lower-quality gate merely because two materials were placed automatically.

Use the [Conductive Coating Methods library](conductive-coatings/index.md) when automation is required. It compares ten routes by geometry, difficulty, student trial allowance, ownership allowance, equipment, materials, microsteps, pass/fail gates and fallback. C01 gantry dispensing is the preferred student-built extension; advanced chemistry, laser, vacuum, inkjet and aerosol routes remain controlled by approved facilities or services.

### Student responsibilities

- prepare drawings and masks;
- identify samples;
- inspect seed continuity using the approved low-voltage method;
- record pre-plating mass;
- prepare **process travellers**, meaning records that stay with each sample through manufacturing;
- observe and record the approved plating run;
- record post-plating mass and defects.

### Laboratory responsibilities

- approve chemistry;
- control ventilation and exposure;
- approve electrical settings;
- control storage and waste;
- supervise cleaning, plating, rinsing, and emergency response.

### Plating record

Record sample identifier, process identifier, date, operator, current, voltage, time, permitted bath temperature, pre/post mass, interruptions, photographs, and disposition.

### Pass gate

Plating passes when the selected seed method first passes a coupon, every functional sample then has continuous coating between terminals, the process record is complete, no liquid is trapped, and no visible defect makes electrical testing unsafe.

---

## 9. Controlled Damage and Repair Fixture

### Damage purpose

Create a visible, repeatable increase in resistance at the marked repair zone.

### Method

Use a lecturer-approved guide that limits abrasion or machining to a defined 5 mm-wide region. Collect particles and record the damaged dimensions. The student does not choose an uncontrolled cutting method.

### Repair mask

3D print a clip-on mask exposing only the repair zone. The mask should:

- locate from fixed sample features;
- protect adjacent areas;
- allow approved cleaning and replating access;
- be removable without damaging the sample.

### Repair gate

Repair passes when the sample is measured in original, damaged, and repaired states; the repair history is complete; resistance returns within 15% of original; temperature rise returns within 20% of original; and no unsafe local heating or delamination is observed.

These are classroom criteria, not industrial standards.

---

## 10. Student Software

Use a small Python package rather than a large application.

### Required modules

```text
mission.py       project limits and test settings
geometry.py      lengths, widths, and copper thickness
electrical.py    resistance and power calculations
thermal.py       simple temperature-rise estimate
data_io.py       CSV import and validation
analysis.py      comparisons and uncertainty notes
reporting.py     tables and figures
```

### Minimum automated tests

- a straight conductor matches a hand calculation;
- two series sections add correctly;
- two parallel paths reduce total resistance;
- zero current produces zero electrical heating;
- invalid negative dimensions are rejected;
- a missing temperature channel fails the test record;
- repaired-state calculations use the correct sample identifier;
- the same input produces the same report.

### Pass gate

Software passes when a new student can install it, run one example, and reproduce one figure using the documented command.

---

## 11. Data Record

Minimum fields:

```text
time_s
sample_id
design
state
load_setting
sample_voltage_v
shunt_voltage_v
current_a
resistance_ohm
ambient_temperature_c
input_temperature_c
centre_temperature_c
output_temperature_c
operator_note
software_version
```

The **state** field is one of `original`, `damaged`, or `repaired`.

Raw files are never edited by hand. Processing scripts create separate cleaned files.

---

## 12. Construction Sequence

1. Approve project and safety boundary.
2. Print and measure dimensional coupons.
3. Build the 0.5 A test-fixture setting.
4. Build and calibrate the voltage/current logger.
5. Build and check the temperature logger.
6. Complete the simple Python calculations.
7. Print seed and plating coupons.
8. Review results before printing functional samples.
9. Print three copies of each functional design.
10. Seed and plate under the approved process.
11. Test at 0.5 A, then 1 A, then approximately 1.8 A.
12. Damage one repair-ready sample.
13. Measure the damaged state.
14. Repair under supervision.
15. Measure the repaired state.
16. Generate technical and business summaries.

Never purchase or build later-stage equipment before the earlier gate passes.

---

## 13. Common Problems and Fixes

| Problem | Likely cause | First correction |
|---|---|---|
| current is unstable | loose terminal or unsuitable load switch | repair fixture before testing samples |
| resistance changes when probes move | poor four-wire probe location | add fixed probe pads and clamp |
| one temperature channel differs | sensor identity or attachment error | recheck labels and common-reference test |
| coating is discontinuous | seed access or continuity problem | return to coupon stage |
| edge is heavily plated | electrical field concentration | discuss geometry/current with lab supervisor |
| sample overheats at 1 A | narrow path, poor coating, or bad terminal | stop, inspect, and do not continue to 1.8 A |
| repair looks good but remains hot | local thin region or contact defect | fail repair and inspect cross-section/coupon evidence |
| software predicts impossible values | unit conversion error | check millimetres, metres, square area, and test cases |

---

## 14. Completion Evidence

The construction work is complete only when the project contains:

- wiring diagrams;
- instrument photographs;
- calibration records;
- sensor identification table;
- fixture fault tests;
- sample drawings;
- print and plating travellers;
- raw CSV files;
- tested Python code;
- original/damaged/repaired evidence;
- cost record;
- plain-language explanation.

---

## 15. Artist-D and Conductive-Filament References

- [JG MAKER documentation downloads](https://www.jgmaker3d.com/pages/documents-download) — manufacturer manual, profiles, firmware, and source files.
- [Protopasta Conductive PLA](https://proto-pasta.com/products/conductive-pla) — example carbon-black conductive PLA properties and print guidance.
- [One-step electrodeposition of copper on conductive 3D printed objects](https://doi.org/10.1016/j.addma.2019.03.016) — research on the relationship between printed-seed conductivity and copper deposition.

Product availability, prices, profiles, and supplier claims can change. Download the current manual and material data before the project purchase gate.
