# Adaptive Electroformed 3D Power Topology Lite (AE3PT-Lite): Student Bill of Materials

## Parts, Materials, Equipment, Specifications, Costs, and Purchase Gates

> **Budget basis:** Approximately 1,500 United States dollars (USD) for one student team when a computer, 3D printer, ordinary hand tools, and supervised copper-coating access are already available.

**AE3PT-Lite** means **Adaptive Electroformed 3D Power Topology Lite**, the small classroom version of the project. **Electroplating** means using an approved electrical and chemical process to deposit copper as a coating.

A **Bill of Materials**, abbreviated BOM, is a controlled list of what must be bought, borrowed, made, or supplied. Costs are planning estimates, not quotations. Verify local prices, taxes, shipping, and laboratory charges before purchase.

Purchase-gate labels use **P** for **Purchase** followed by the order number. For example, P1 is the first purchase decision. These are project-created labels, not external standards.

The machine-readable one-team register is [`data/ae3pt-low-budget-bom.csv`](data/ae3pt-low-budget-bom.csv). A small-class register is [`data/ae3pt-bom.csv`](data/ae3pt-bom.csv).

The optional JG MAKER Artist-D dual-material register is [`data/ae3pt-artist-d-option-bom.csv`](data/ae3pt-artist-d-option-bom.csv). It is separate because the $1,555 baseline does not require a conductive-filament seed route. The complete machine and plating procedure is the [Artist-D Dual-Material Copper Electroplating Plan](artist-d-electroplating-plan.md).

---

## 1. Budget Summary

**Contingency** means money reserved for uncertain costs and failures.

| Group | One-team allowance |
|---|---:|
| Printing and sample materials | $170 |
| Low-voltage electrical fixture | $235 |
| Voltage/current logger | $190 |
| Temperature logger | $105 |
| Inspection and measurement | $145 |
| Supervised seed and plating | $360 |
| Safety and containment | $105 |
| Data, display, and documentation | $65 |
| Contingency | $180 |
| **Planned total** | **$1,555** |

The contingency protects the project from failed prints, damaged sensors, extra plating coupons, replacement connectors, and shipping variation.

---

## 2. Existing Equipment Assumptions

The baseline cost assumes free or shared access to:

- one ordinary laptop capable of running Python;
- one material-extrusion 3D printer;
- soldering iron and basic electronics tools;
- approved electroplating laboratory or service infrastructure;
- trusted multimeter for comparison;
- normal workshop ventilation and supervision.

If these are not available, use the optional-equipment section rather than hiding the missing cost.

---

## 3. Printing and Sample Materials

**PETG** means **Polyethylene Terephthalate Glycol-modified**. **PLA** means **Polylactic Acid**.

| Item | Quantity | Minimum specification | Approximate cost |
|---|---:|---|---:|
| PETG or approved functional filament | 2 kg | known supplier and batch; suitable for printer and approved process | $55 |
| PLA practice filament | 1 kg | general-purpose dimensional coupons | $25 |
| spare brass nozzles | 3 | match printer diameter and thread | $18 |
| build-surface consumables | 1 set | compatible adhesive or sheet | $20 |
| sample labels and paint marker | 1 set | chemical-resistant where required | $12 |
| failed-print allowance | 1 | material reserve | $25 |
| repair-mask and fixture material | 1 kg equivalent | printable and process-compatible | $15 |

**Purchase gate P1:** Buy only after the printer, selected material, and dimensional coupon plan are approved.

---

## 4. Low-Voltage Electrical Fixture

**VDC** means **Volts Direct Current**.

A **current-limited supply** automatically restricts excessive current.

| Item | Quantity | Minimum specification | Approximate cost |
|---|---:|---|---:|
| certified 5 VDC supply | 1 | 3 A minimum; current limited or protected | $35 |
| 2.5 A fuse holders and fuses | 1 set | low-voltage direct-current rated | $18 |
| main power switch | 1 | 5 A at low-voltage direct current | $12 |
| 10 Ω load resistor | 2 | 10 W minimum | $12 |
| 4.7 Ω load resistor | 2 | 10 W minimum | $14 |
| 2.7 Ω load resistor | 2 | 15 W minimum | $18 |
| load-selection switches | 3 | guarded or enclosed | $20 |
| 0.1 Ω current shunt | 2 | 1%, 3 W minimum | $16 |
| sample terminals and clamps | 1 set | repeatable pressure; insulated covers | $45 |
| wire, ferrules, heat-shrink | 1 set | suitable for 2 A continuous service | $25 |
| enclosure and printed hot-part guard | 1 set | non-conductive enclosure and guarded hot surfaces | $20 |

**Purchase gate P2:** Buy after the circuit diagram, fuse position, load power, and enclosure plan pass lecturer review.

---

## 5. Voltage and Current Logger

**ADC** means **Analog-to-Digital Converter**. **USB** means **Universal Serial Bus**. **PCB** means **Printed Circuit Board**.

| Item | Quantity | Minimum specification | Approximate cost |
|---|---:|---|---:|
| Arduino-compatible microcontroller | 2 | one working unit plus spare | $35 |
| ADS1115 ADC module | 3 | 16-bit; one spare | $35 |
| resistor and protection kit | 1 | 1% resistors; small signal protection parts | $20 |
| solderless breadboard | 2 | full-size, labelled rails | $20 |
| stripboard or simple PCB materials | 1 set | verified circuit transfer | $25 |
| screw terminals and connectors | 1 set | separate current and voltage-sense connections | $25 |
| plastic instrument enclosure | 1 | strain relief and ventilation where needed | $20 |
| USB cables and serial adapter allowance | 1 set | data and low-voltage power only | $10 |

**Purchase gate P3:** Buy after one hand calculation defines the expected sample-voltage range and ADC input range.

---

## 6. Temperature Logger

| Item | Quantity | Minimum specification | Approximate cost |
|---|---:|---|---:|
| DS18B20 digital temperature sensors | 8 | four working channels plus spares | $32 |
| sensor cable and connectors | 1 set | labelled and replaceable | $18 |
| attachment tape or approved adhesive | 1 set | repeatable below 50 °C | $15 |
| small controller enclosure | 1 | labelled channels | $20 |
| warm-reference materials | 1 set | safe container and trusted comparison thermometer | $20 |

**Purchase gate P4:** Buy after the sample sensor locations and automatic stop rule are documented.

---

## 7. Inspection and Measurement

A **resistance reference** is a component or metal link with a known or independently checked resistance. **Calibration** means comparing an instrument with a reference.

| Item | Quantity | Minimum specification | Approximate cost |
|---|---:|---|---:|
| digital calliper | 1 | 0.01 mm display; checked against reference | $35 |
| digital scale | 1 | 0.01 g resolution; suitable capacity | $35 |
| USB microscope or camera stand | 1 | repeatable lighting and scale reference | $45 |
| resistance references | 1 set | values covering expected sample range | $20 |
| steel rule and photograph scale | 1 set | metric | $10 |

**Purchase gate P5:** Buy only items not already available in the teaching laboratory.

---

## 8. Supervised Seed and Plating

**Consumables** are items used up by the project, such as conductive seed, masks, and plating materials.

| Item or service | Quantity | Minimum specification | Approximate cost |
|---|---:|---|---:|
| laboratory or service access | 1 allowance | approved copper-plating process and waste route | $180 |
| approved conductive seed materials | 1 allowance | compatible with selected polymer and process | $75 |
| copper anode and process consumables | 1 allowance | supplied or approved by laboratory | $40 |
| masks, contacts, and hanging fixtures | 1 set | reusable where possible | $35 |
| coupon and failed-run allowance | 1 | additional supervised process time/material | $30 |

**Purchase gate P6:** No chemical purchase occurs before laboratory approval, Safety Data Sheets, storage, and waste responsibilities are assigned.

---

## 9. Safety and Containment

**PPE** means **Personal Protective Equipment**.

A **risk assessment** identifies hazards, possible consequences, and the controls required before work begins.

| Item | Quantity | Minimum specification | Approximate cost |
|---|---:|---|---:|
| electrical safety glasses | 2 | impact-rated | $20 |
| laboratory-approved chemical PPE allowance | 1 | selected by laboratory risk assessment | $30 |
| low-profile containment trays | 2 | compatible with supervised process | $20 |
| labels and storage containers | 1 set | clear sample and hazard identification | $15 |
| spill and cleanup contribution | 1 | laboratory-approved materials | $20 |

PPE selection remains a laboratory responsibility.

---

## 10. Data, Display, and Documentation

| Item | Quantity | Minimum specification | Approximate cost |
|---|---:|---|---:|
| external storage | 1 | 256 GB or larger, encrypted where required | $25 |
| sample storage boxes | 2 | labelled compartments | $15 |
| poster and demonstration printing | 1 allowance | final review material | $25 |

Use free and open-source Python, scientific, plotting, and testing software where permitted.

---

## 11. Optional Equipment

These items are not part of the $1,555 baseline.

| Optional item | Reason | Approximate cost |
|---|---|---:|
| entry-level enclosed 3D printer | needed only if no printer is available | $450–$900 |
| refurbished laptop | needed only if no suitable computer is available | $400–$700 |
| trusted bench multimeter | improves comparison and teaching | $250–$600 |
| small fume extraction or enclosure upgrade | only if specified by the approved process | $300–$1,000 |
| commercial four-wire meter rental | independent verification | $100–$300 |
| thermal camera rental | optional visualization | $100–$250 |

### JG MAKER Artist-D IDEX option

Use this option when the Artist-D is already owned, borrowed, or available in the teaching laboratory. **IDEX** means **Independent Dual Extrusion**: one head can print the non-conductive body and the other can print an exposed conductive seed route.

**Difficulty:** 4/5 for the complete route. The printer is substantially preassembled, but the project must still prove two-head calibration, material isolation, seed resistance, plating contacts and full-route copper coverage. The nominal 300 mm × 300 mm × 340 mm build volume and “98% assembled” retail description do not reduce these qualification requirements.

| Optional item | Quantity | Minimum specification | Approximate cost |
|---|---:|---|---:|
| existing Artist-D printer access | 1 | both heads operational; bed, brushes, guards, firmware, and manual checked | $0–$100 service allowance |
| natural PLA for dedicated left tool | 1 kg | compatible with conductive PLA and approved coupon plan | $20–$35 |
| conductive PLA development material | 50–500 g | published electrical data and supplier print settings; not decorative copper-coloured filament | $15–$100 |
| dedicated or replacement 0.4 mm nozzles | 2–4 | verified fit; abrasion-resistant nozzle when required by the conductive-filament supplier | $15–$35 |
| purge brushes, collection cups, and labels | 1 set | separate left/right material-control areas | $10–$25 |
| dry storage and desiccant | 1 set | sealed containers for both filaments | $15–$30 |
| IDEX alignment, resistance, and plating coupons | 1 allowance | at least three geometries and one supervised plating trial | $15–$40 |
| **Dedicated option allowance** |  | excludes printer purchase and laboratory plating already budgeted | **$90–$365** |

Several items overlap the baseline printing allowance. The incremental cost can therefore be much lower when PLA, nozzles, storage, and coupon material are already available.

Do not buy an unsupported or used Artist-D solely because it has a large build volume or is advertised as mostly assembled. Before purchase, obtain a current quotation, confirm electrical compliance for the installation location, download the official files, inspect replacement-part availability, and verify that both independent heads can be calibrated. If no suitable machine is owned, compare a currently supported IDEX printer against the existing $450–$900 optional-printer allowance.

**Purchase gate P1-IDEX:** Buy conductive filament only after the lecturer approves the dual-material coupon drawing, the laboratory accepts the proposed seed material for a coupon plating trial, and a surface-applied seed remains available as the fallback.

---

## 12. Small-Class Funding Package

For a class of 12 students working in four teams, share the printer, inspection tools, supervised plating access, and reference equipment.

Suggested funding envelope:

| Group | Allowance |
|---|---:|
| team electronics and fixtures | $1,680 |
| printing materials and process allowance | $650 |
| shared inspection and reference tools | $750 |
| supervised plating access and materials | $1,200 |
| shared printer maintenance | $650 |
| safety and containment | $350 |
| laboratory and teaching support | $1,200 |
| data, storage, and display | $400 |
| contingency and failed builds | $820 |
| **Cohort total** | **$7,700** |

The cohort machine-readable BOM contains more exact line items and assumptions.

---

## 13. Cost Controls for Business Review

### Track actual cost

Record ordered cost, delivered cost, tax, shipping, quantity used, quantity left, and whether the item is reusable.

### Separate capital and consumable cost

- **Capital equipment** can serve future projects, such as a printer or multimeter.
- **Consumables** are used by this project, such as filament, masks, and plating materials.

### Record cost per successful sample

$$
C_{successful}=\frac{C_{consumed}}{N_{samples\ passing}}
$$

where \(C_{consumed}\) is consumed cost and \(N_{samples\ passing}\) is the number of samples meeting the classroom criteria.

### Record repair cost

Include inspection, cleaning, masking, replating, retesting, labour time, and failed attempts. Do not call repair cheaper until the same cost categories are included for repair and replacement.

---

## 14. Procurement Pass/Fail Rules

**PASS** a purchase when:

- it supports a named lesson, sample, measurement, or gate;
- its specification matches the 5 V/2 A baseline;
- an existing item cannot meet the need;
- storage, safety, calibration, and disposal are defined;
- the remaining budget still covers required stages.

**FAIL** or defer a purchase when:

- it is intended for motors, high voltage, or industrial scale;
- it duplicates available equipment;
- it is bought before the relevant design passes;
- it has no owner or storage plan;
- it consumes repair/testing funds for an optional feature.

---

## 15. Final BOM Rule

Buy the smallest safe item that produces the required evidence. Borrow or share rarely used equipment. Spend first on reliable measurement and supervised process access, not on impressive but unnecessary machinery.
