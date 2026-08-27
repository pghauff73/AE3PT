#!/usr/bin/env python3
"""Generate the AE3PT conductive-coating method plan library."""

from __future__ import annotations

import argparse
import csv
import html
import io
import textwrap
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Method:
    method_id: str
    slug: str
    title: str
    acronym: str
    accent: str
    difficulty: int
    trial_cost: tuple[int, int]
    capital_cost: tuple[int, int]
    best_geometry: str
    automation_level: str
    recommendation: str
    description: tuple[str, str, str]
    principle: str
    automation_cell: str
    seed_result: str
    equipment: tuple[str, ...]
    materials: tuple[str, ...]
    prerequisites: tuple[str, ...]
    microsteps: tuple[str, ...]
    gates: tuple[tuple[str, str, str, str], ...]
    risks: tuple[tuple[str, str], ...]
    evidence: tuple[str, ...]
    fallback: str
    research: tuple[tuple[str, str], ...]


METHODS = (
    Method(
        "C01",
        "gantry-dispensed-coating",
        "Gantry-Dispensed Conductive Coating",
        "GDC",
        "#1b9e77",
        2,
        (250, 1_000),
        (500, 2_500),
        "Open grooves, flat faces, broad tracks and reachable pads",
        "Student-built two-and-a-half-axis motion",
        "Recommended first automated method",
        (
            "Gantry-dispensed conductive coating uses a computer-controlled syringe, auger or positive-displacement dispenser to place conductive paint, paste or ink onto selected regions of a printed polymer part. The name comes from the bridge-like gantry that moves the tool in the horizontal X and Y directions while the build platform or tool provides a limited vertical Z adjustment. In AE3PT this is the simplest way to turn a digital conductor path into a repeatable seed layer without asking a student to paint every trace by hand.",
            "The method is most suitable for open surfaces, printed grooves and large connection pads. It can reuse an old three-dimensional printer, computer numerical control frame or purpose-built belt gantry, but the original extrusion hot end is replaced or supplemented by a low-pressure liquid dispenser. The deposited seed does not have to carry the final operating current; it only needs continuous conductivity, acceptable adhesion and enough chemical compatibility to begin supervised copper electroplating.",
            "For a third-year student project, the main learning value is the connection between path planning, fluid behaviour, electrical continuity and process evidence. The student can write the path generator, tune speed and flow, inspect line width, measure resistance and create an automatic pass/fail report. The approach is inexpensive and repairable, although it cannot easily coat hidden channels, severe undercuts or the back of a complex part without additional axes or repositioning fixtures.",
        ),
        "A controlled nozzle meters a conductive liquid along a toolpath exported from Computer-Aided Design data.",
        "Reused printer frame, motion controller, syringe or auger dispenser, removable fixture and enclosure",
        "A continuous printed paint or paste trace ready for copper electroplating",
        (
            "reused Cartesian printer or small computer numerical control gantry",
            "stepper controller with emergency stop",
            "syringe pump, auger valve or time-pressure dispenser",
            "disposable needles or tapered nozzles",
            "camera, lighting and dimensional scale",
            "four-wire resistance measurement fixture",
            "local exhaust or enclosed drying area required by the chosen coating",
        ),
        (
            "water-based conductive paint or laboratory-approved conductive paste",
            "printed polymer coupons and final parts",
            "removable masking film and cleaning materials",
            "copper-plating contact tabs",
            "waste containers specified by the laboratory",
        ),
        (
            "approved low-voltage machine modification plan",
            "Safety Data Sheet review for the coating",
            "one flat coupon and one curved coupon geometry",
            "defined minimum seed resistance and adhesion target",
        ),
        (
            "Freeze one seed-track geometry, datum system and contact-pad design.",
            "Measure coating viscosity, drying behaviour and compatibility on scrap polymer.",
            "Build the dispenser mount without disabling printer guarding or emergency stop functions.",
            "Calibrate deposited mass per command using repeated straight-line coupons.",
            "Write a path exporter that limits speed, acceleration, overlap and nozzle clearance.",
            "Print three dry-run paths with a harmless test fluid and inspect registration.",
            "Deposit three conductive seed coupons using the frozen recipe.",
            "Dry or cure under the coating supplier and laboratory limits.",
            "Measure line width, continuity, adhesion and end-to-end resistance.",
            "Electroplate one approved coupon and map copper coverage from contact to far end.",
            "Repeat the complete cycle on three independent parts.",
            "Release the method only when the generator, machine file and evidence package reproduce the result.",
        ),
        (
            ("GDC-G0", "Machine safety", "Emergency stop, guarded motion and spill containment pass inspection.", "Stop modification and use manual coating or an approved service."),
            ("GDC-G1", "Path accuracy", "Ninety-five percent of measured track width and position values meet the frozen tolerance.", "Adjust fixture, nozzle height, speed or flow; do not use conductive material yet."),
            ("GDC-G2", "Seed quality", "All three coupons pass continuity, adhesion and maximum seed resistance.", "Reject the recipe and change surface preparation or coating."),
            ("GDC-G3", "Plating release", "Copper reaches the farthest intended point without bridging isolated regions.", "Redesign contacts or shorten the current path before another supervised plating trial."),
        ),
        (
            ("Solvent or aerosol exposure", "Prefer water-based material; otherwise use laboratory-approved extraction and personal protective equipment."),
            ("Nozzle pressure or sudden release", "Use rated tubing, low pressure, a shield and depressurise before maintenance."),
            ("Interrupted seed trace", "Use camera inspection plus four-wire resistance measurement before plating."),
            ("Copper bridging", "Increase spacing, improve masking and stop at the first unintended deposit."),
        ),
        (
            "frozen Computer-Aided Design and toolpath files",
            "dispenser calibration curve",
            "before-and-after images with scale",
            "seed resistance and adhesion results",
            "plated thickness or mass-gain estimate",
            "three-run repeatability table",
            "cost and operator-time record",
        ),
        "Return to a manual brush-and-mask baseline, or move to robotic spray only if surface coverage rather than trace precision is the main problem.",
        (
            ("Rapid 3D-Plastronics selective metallization", "https://doi.org/10.1016/j.addma.2023.103673"),
            ("Selective electroplating of dual-material printed parts", "https://doi.org/10.1016/j.addma.2018.01.006"),
        ),
    ),
    Method(
        "C02",
        "robotic-spray-coating",
        "Robotic Airbrush or Spray Coating",
        "RSC",
        "#2878c8",
        3,
        (500, 2_000),
        (1_500, 8_000),
        "Broad external surfaces, shells and gently curved parts",
        "Three-axis spray cell with indexed part rotation",
        "Useful second method for area coverage",
        (
            "Robotic spray coating uses a programmed airbrush or low-volume spray gun to apply a thin conductive coating over a selected surface. The acronym RSC means Robotic Spray Coating and describes the automation cell rather than a particular paint chemistry. In AE3PT the process creates a conductive seed film that can later receive thicker copper by electroplating, while masks or removable films protect areas that must remain non-conductive.",
            "Spray deposition is faster than point-by-point dispensing for large areas and can produce a smoother film on broad curves. A low-cost cell can combine a guarded X-Y-Z gantry, an indexed rotary table, a trigger solenoid, a camera and local exhaust ventilation. Coverage is influenced by nozzle distance, angle, overlap, atomising pressure, part rotation, coating viscosity and drying time, so automation is valuable only when those variables are measured and frozen.",
            "The educational challenge is to distinguish apparent visual coverage from verified electrical and plating performance. Students should construct a coupon set with flat, convex and recessed surfaces, then map thickness, sheet resistance and adhesion. The method is not preferred for narrow isolated traces unless masking is precise, and it should never be operated with an unapproved coating or inadequate extraction merely because the spray mechanism itself appears mechanically simple.",
        ),
        "A moving spray cone deposits overlapping passes while a fixture controls surface angle and stand-off distance.",
        "Enclosed gantry, low-volume gun, trigger valve, filtered extraction, rotary fixture and vision check",
        "A broad conductive seed film with masked electrical boundaries",
        (
            "enclosed motion frame or guarded robot",
            "low-volume airbrush or spray gun",
            "regulated clean-air supply",
            "solenoid trigger and flow controller",
            "rotary indexing fixture",
            "filtered local exhaust ventilation",
            "wet-film or dry-film thickness measurement method",
        ),
        (
            "laboratory-approved conductive coating",
            "masking film, plugs and removable resist",
            "flat, convex and recessed coupons",
            "cleaning solvent or water specified by the coating supplier",
            "overspray filters and controlled waste containers",
        ),
        (
            "approved spray-booth or enclosure assessment",
            "coating and cleaning chemical review",
            "air-pressure limit and leak test",
            "defined overspray, adhesion and sheet-resistance acceptance limits",
        ),
        (
            "Design flat, curved and recessed coupons with identical plated areas.",
            "Qualify the spray enclosure, filters, grounding and emergency isolation.",
            "Calibrate gun flow and pattern using water or another harmless surrogate.",
            "Program stand-off distance, angle, pass overlap and indexed part rotation.",
            "Verify masking registration with a dry visual trial.",
            "Spray three coupons at each selected process setting.",
            "Dry or cure without exceeding the polymer temperature limit.",
            "Measure thickness variation, sheet resistance, edge definition and adhesion.",
            "Electroplate the best coupon under the approved laboratory recipe.",
            "Inspect copper coverage, bridging, blistering and masked boundaries.",
            "Repeat the winning recipe on three independently prepared parts.",
            "Release only the geometry classes that passed; keep recess and undercut exclusions explicit.",
        ),
        (
            ("RSC-G0", "Ventilation release", "Extraction, filter loading, grounding and spill controls pass laboratory inspection.", "Do not spray; use dispensing or an external coating service."),
            ("RSC-G1", "Coverage uniformity", "Dry-film thickness and sheet resistance remain within the chosen limits across all measured zones.", "Change spray angle, rotation, overlap or coating dilution."),
            ("RSC-G2", "Boundary control", "Mask edges remain isolated and no unacceptable overspray reaches protected regions.", "Redesign masks or choose a trace-deposition method."),
            ("RSC-G3", "Plating adhesion", "Plated copper passes visual inspection and the selected adhesion test on three samples.", "Stop and improve cleaning, surface texture or seed curing."),
        ),
        (
            ("Inhalation and flammability", "Use only approved materials inside a compliant exhausted enclosure; remove ignition sources."),
            ("Overspray contamination", "Use replaceable filters, enclosed fixtures and documented cleaning."),
            ("Shadowed surfaces", "Rotate the part, add angled passes and define prohibited geometry."),
            ("Mask leakage", "Use witness coupons and electrical isolation checks before plating."),
        ),
        (
            "spray-cell risk assessment",
            "air pressure, flow and path settings",
            "thickness and sheet-resistance maps",
            "mask-boundary photographs",
            "adhesion results before and after plating",
            "filter and waste records",
            "repeatability and cost summary",
        ),
        "Use gantry dispensing for selective tracks, or contract a professional coating service when a compliant spray enclosure is unavailable.",
        (
            ("Rapid 3D-Plastronics selective metallization", "https://doi.org/10.1016/j.addma.2023.103673"),
            ("Direct electroless plating of conductive thermoplastics", "https://doi.org/10.1016/j.addma.2022.102793"),
        ),
    ),
    Method(
        "C03",
        "automated-electroless-seed",
        "Automated Electroless Seed Coating",
        "AESC",
        "#7357b4",
        4,
        (500, 2_500),
        (5_000, 25_000),
        "Complex external surfaces and accessible internal passages",
        "Supervised wet-process line with timed transfers",
        "Shared-laboratory method after coupon success",
        (
            "Automated Electroless Seed Coating, abbreviated AESC, deposits metal through a chemical reduction reaction rather than through current supplied by an external power source. The word electroless distinguishes it from electroplating, where the part is connected as an electrode. Surface preparation and activation allow metal to begin forming on selected regions, creating a continuous seed layer that can be thickened later by conventional copper electroplating.",
            "The process can reach complex external shapes and flowing internal passages that a line-of-sight spray or dispenser cannot reach. Automation normally means controlled bath temperature, agitation, timed immersion, rinsing, solution monitoring and data logging, not unattended chemistry. Selectivity may come from masks, activated surface regions, conductive composite filament, catalyst-loaded material or laser activation, and each route changes the chemical sequence and waste obligations.",
            "For a student project this is an advanced shared-laboratory activity because bath chemistry, ventilation, incompatible chemicals and metal-bearing waste require formal control. The student contribution should focus on fixture design, coupon matrices, timing software, conductivity mapping and evidence capture while trained staff own bath preparation and disposal. Success is defined by uniform, adherent and electrically continuous seed coverage, not simply by a visibly metallic surface.",
        ),
        "Activated regions catalyse metal reduction from solution until a conductive seed layer covers the intended surface.",
        "Covered process tanks, temperature control, agitation, timed lift, rinse cascade, sensors and batch log",
        "Conformal electroless copper or nickel seed suitable for later electroplating",
        (
            "approved wet laboratory with local exhaust ventilation",
            "covered compatible process and rinse tanks",
            "temperature, pH and conductivity measurement",
            "agitation or recirculation system",
            "programmable timed lift or operator-guided transfer aid",
            "secondary containment and emergency wash facilities",
            "solution-analysis and waste-labelling equipment",
        ),
        (
            "approved cleaning, etching and activation chemistry",
            "electroless copper or nickel bath",
            "deionised rinse water",
            "masked, conductive-composite or catalyst-bearing coupons",
            "bath-control standards and metal-bearing waste containers",
        ),
        (
            "institutional chemical-process approval",
            "trained laboratory owner for every bath",
            "material compatibility and coupon plan",
            "documented solution life and waste route",
            "defined coverage, adhesion and bath-stability limits",
        ),
        (
            "Select one activation route and prohibit unreviewed chemistry substitutions.",
            "Create a process flow diagram showing every bath, rinse and waste stream.",
            "Build compatible coupon racks that prevent trapped gas and allow drainage.",
            "Commission temperature, pH, timing and agitation logging with harmless water trials.",
            "Run activation-only coupons and verify selectivity before metal deposition.",
            "Process a three-coupon time series in the electroless bath.",
            "Rinse, dry and record mass, resistance and high-resolution images.",
            "Section or inspect representative features for coverage and voids.",
            "Electroplate only coupons that pass the seed gate.",
            "Measure plated thickness, adhesion and isolation between circuits.",
            "Repeat with a fresh batch or independently controlled run.",
            "Release the method only while bath condition remains inside the approved control window.",
        ),
        (
            ("AESC-G0", "Chemical authority", "Named trained staff approve chemistry, ventilation, storage and waste routes.", "No wet processing; use an external service or a dry deposition method."),
            ("AESC-G1", "Bath control", "Temperature, pH, timing and solution condition remain inside the frozen window.", "Quarantine the run and restore or replace the bath under laboratory authority."),
            ("AESC-G2", "Seed continuity", "Every required zone is conductive and unintended zones remain isolated.", "Reject the activation or masking process."),
            ("AESC-G3", "Repeatability", "Independent runs meet coverage, adhesion and resistance limits.", "Do not scale to full parts; continue coupon investigation."),
        ),
        (
            ("Hazardous or incompatible chemistry", "Use an approved written sequence, segregation, secondary containment and trained supervision."),
            ("Bath decomposition", "Log bath loading, temperature and age; stop on abnormal gas, colour, precipitate or deposition."),
            ("Gas pockets in channels", "Orient fixtures for venting, use flow trials and define drain holes."),
            ("Uncontrolled metal-bearing waste", "Collect every process and rinse stream under the laboratory waste plan."),
        ),
        (
            "approved chemical process sheet",
            "bath and rinse sensor logs",
            "coupon rack and venting drawing",
            "seed resistance and coverage map",
            "mass gain and thickness evidence",
            "adhesion and isolation test",
            "batch identity and waste record",
        ),
        "Use direct conductive-filament electroplating for simpler open features, or purchase an electroless seeding service for complex parts.",
        (
            ("Direct electroless plating of conductive thermoplastics", "https://doi.org/10.1016/j.addma.2022.102793"),
            ("Self-activating metal-polymer composites", "https://doi.org/10.1016/j.jmrt.2022.12.035"),
            ("Self-activating resins for 3D printed parts", "https://doi.org/10.1016/j.addma.2026.105129"),
        ),
    ),
    Method(
        "C04",
        "inkjet-catalyst-seed",
        "Inkjet-Printed Catalyst or Metal Seed",
        "ICS",
        "#d95f02",
        4,
        (1_000, 4_000),
        (20_000, 100_000),
        "Fine planar or gently curved traces",
        "Drop-on-demand digital patterning",
        "Service-first research method",
        (
            "Inkjet-Printed Catalyst or Metal Seed, shortened to ICS, uses digitally controlled droplets to place either a plating catalyst or a thin conductive metal pattern. Unlike office inkjet printing, functional inkjet systems control droplet formation, substrate temperature, waveform, nozzle condition and material compatibility. The printed image becomes the chemical or electrical starting pattern for later electroless deposition or copper electroplating.",
            "The method can create finer tracks than a syringe dispenser and wastes little material because droplets are placed only where required. It performs best on planar or gently curved surfaces with controlled surface energy and limited height variation. Reactive copper inks, nanoparticle inks and catalyst-bearing inks each require different drying, sintering or activation conditions, so the printer, ink, substrate and post-process must be qualified as one system.",
            "A student team should normally begin through a university facility or commercial service rather than purchase a functional inkjet platform. The valuable student work is designing test patterns, controlling files, measuring drop placement, evaluating line breaks and comparing electroless or electrolytic thickening. The main failure modes are nozzle blockage, poor wetting, coffee-ring deposits, thermal damage, oxidation and weak adhesion, all of which must be detected on coupons before a three-dimensional part is attempted.",
        ),
        "Drop-on-demand droplets define a catalyst or metal pattern that is activated, sintered or plated into a continuous conductor.",
        "Functional inkjet printer, controlled substrate stage, printhead maintenance, drying or sintering and inspection",
        "Fine catalyst or metal seed tracks with digital pattern provenance",
        (
            "functional materials inkjet printer or qualified service",
            "temperature-controlled vacuum platen",
            "printhead waveform and cleaning station",
            "drop-watcher or microscope",
            "controlled drying, photonic curing or low-temperature sintering",
            "surface-energy measurement or wetting test",
            "four-wire microtrace resistance fixture",
        ),
        (
            "compatible catalyst, reactive metal or nanoparticle ink",
            "filtered cleaning and flushing fluid",
            "smooth printed polymer coupons",
            "surface-treatment materials approved for the substrate",
            "electroless or electrolytic thickening chemistry",
        ),
        (
            "facility-approved ink and printhead combination",
            "substrate temperature and dimensional stability data",
            "test pattern with line, pad, corner and spacing features",
            "defined droplet, line-width, continuity and adhesion limits",
        ),
        (
            "Choose whether the ink provides catalyst, conductive metal or both.",
            "Design a calibration pattern covering line width, spacing, pads and turns.",
            "Measure substrate flatness, surface energy and allowable heating.",
            "Tune waveform, drop spacing, stage speed and substrate temperature on facility coupons.",
            "Print microscope slides or reference substrates to confirm droplet quality.",
            "Print three polymer coupons with the frozen digital file.",
            "Dry, sinter or activate using the lowest successful thermal budget.",
            "Inspect for missing drops, spreading, satellites, cracks and oxidation.",
            "Measure resistance or verify catalytic activity before thickening.",
            "Electroless plate or electroplate the approved patterns.",
            "Test line resistance, adhesion, minimum spacing and solder-pad suitability.",
            "Archive printhead, ink batch, waveform and file identity with the result.",
        ),
        (
            ("ICS-G0", "Facility compatibility", "Ink, printhead, substrate and post-process are approved as one system.", "Use an external service or a dispenser-based process."),
            ("ICS-G1", "Drop quality", "Drop position, diameter and satellite count meet the frozen inspection limits.", "Clean or retune the printhead before using polymer coupons."),
            ("ICS-G2", "Printed seed", "Three coupons meet line continuity or catalytic-activity requirements.", "Change surface treatment, drop spacing or curing."),
            ("ICS-G3", "Thickened conductor", "The plated trace passes resistance, spacing and adhesion limits.", "Do not transfer the pattern to a functional part."),
        ),
        (
            ("Nanoparticle or reactive-ink exposure", "Use facility controls, closed cartridges and approved cleaning procedures."),
            ("Nozzle clogging", "Filter compatible inks, log idle time and use controlled purge routines."),
            ("Excessive substrate heat", "Use temperature labels or sensors and define a strict thermal ceiling."),
            ("Oxidised or discontinuous copper", "Control atmosphere or chemistry as required and verify continuity before plating."),
        ),
        (
            "test-pattern source file and checksum",
            "ink batch, waveform and printhead record",
            "drop and line microscopy",
            "surface preparation and thermal log",
            "pre- and post-plating resistance",
            "minimum-spacing and adhesion result",
            "service quotation or equipment cost model",
        ),
        "Use gantry dispensing for wider tracks, or aerosol jet printing through a service when non-planar fine features are essential.",
        (
            ("Reactive inkjet copper patterns and electroless plating", "https://doi.org/10.1016/j.apsusc.2016.09.152"),
            ("Inkjet copper-complex patterns on three-dimensional polymers", "https://doi.org/10.1002/admi.201701285"),
        ),
    ),
    Method(
        "C05",
        "aerosol-jet-seed",
        "Aerosol Jet Printed Seed",
        "AJP",
        "#e6ab02",
        5,
        (2_000, 8_000),
        (100_000, 500_000),
        "Fine conformal traces over moderate three-dimensional relief",
        "Commercial aerodynamic direct-write system",
        "External-service or research-facility method",
        (
            "Aerosol Jet Printing, abbreviated AJP, atomises a functional ink into very small droplets and focuses the aerosol with a sheath gas before it exits the nozzle. The focused stream can write fine conductive seed traces without touching the surface. In AE3PT it is considered a high-resolution method for placing silver, copper or catalyst inks on non-planar polymer parts before selective electroplating.",
            "AJP can tolerate more surface relief and a larger nozzle-to-part distance than conventional inkjet printing, and multi-axis motion can produce conformal tracks. The complete process still depends on ink atomisation, gas flow, overspray control, nozzle size, tool orientation, drying and sintering. Published work has shown that electroplating copper onto aerosol-jet-printed silver can greatly reduce resistivity and create more robust solderable features, but the platform and metrology are specialised.",
            "For a low-budget student project, AJP should be evaluated through a facility or service using a small test coupon and a clearly defined evidence contract. The student should not treat a quoted trace width as proof that a three-dimensional route will plate successfully. The project must inspect line thickness, porosity, adhesion, electrical continuity, far-end plating and cost per successful part before comparing AJP against much cheaper dispensing or conductive-filament methods.",
        ),
        "A sheath-gas-focused aerosol writes a fine seed trace that is dried or sintered before copper thickening.",
        "Aerosol atomiser, sheath-gas print head, multi-axis stage, curing system and microscope",
        "Fine conformal nanoparticle or catalyst seed tracks",
        (
            "commercial aerosol jet system or qualified facility",
            "pneumatic or ultrasonic atomiser",
            "controlled carrier and sheath gas",
            "multi-axis motion and part registration",
            "laser or thermal sintering equipment",
            "microscope and thickness metrology",
            "plating fixture for fine contacts",
        ),
        (
            "qualified silver, copper or catalyst ink",
            "compatible solvents and cleaning materials",
            "smooth polymer coupons and shaped demonstrator",
            "gas supplies specified by the process",
            "electroplating contact and masking materials",
        ),
        (
            "service statement covering ink, substrate and geometry limits",
            "digital trace file and registration features",
            "approved curing temperature",
            "minimum line, spacing, resistance and adhesion targets",
        ),
        (
            "Define the minimum feature that has genuine project value.",
            "Obtain a facility design-rule review before ordering samples.",
            "Create a coupon containing lines, turns, pads, slopes and height transitions.",
            "Agree the atomisation, gas, nozzle, motion and curing record to be returned.",
            "Print a reference flat coupon and inspect line morphology.",
            "Print three shaped coupons using the same qualified recipe.",
            "Measure thickness, width, porosity indicators, adhesion and resistance.",
            "Design low-resistance plating contacts that do not damage the fine seed.",
            "Electroplate a staged time series rather than one uncontrolled long run.",
            "Measure resistivity improvement and look for delamination or burning.",
            "Compare yield and cost against gantry dispensing and inkjet alternatives.",
            "Release AJP only when the required geometry cannot be met more simply.",
        ),
        (
            ("AJP-G0", "Design-rule review", "Facility accepts the substrate, three-dimensional path and curing limit.", "Redesign or select a different process before purchase."),
            ("AJP-G1", "Printed morphology", "Line width, continuity and adhesion pass on flat and shaped coupons.", "Retune atomisation, gases, orientation or curing."),
            ("AJP-G2", "Electroplating response", "Copper thickening reduces resistance without unacceptable delamination or bridging.", "Change seed thickness, contact design or plating current."),
            ("AJP-G3", "Value gate", "The geometry or resolution benefit justifies the measured service cost and yield.", "Use a lower-cost deposition method."),
        ),
        (
            ("Aerosol and solvent exposure", "Keep material handling inside the qualified facility and require process records."),
            ("Hidden overspray", "Inspect surrounding insulation and perform isolation tests."),
            ("Fine-trace burnout during plating", "Use staged low-current plating and distributed contacts."),
            ("Vendor lock-in", "Archive neutral geometry, test data and acceptance criteria rather than only machine files."),
        ),
        (
            "facility design-rule response",
            "neutral Computer-Aided Design and trace files",
            "atomiser, gas, nozzle and curing record",
            "microscopy and thickness measurements",
            "pre- and post-plating electrical results",
            "three-part yield",
            "service cost and lead-time comparison",
        ),
        "Use inkjet for planar fine traces, gantry dispensing for wider conformal traces, or a dual-material conductive filament when resolution is not essential.",
        (
            ("Electroplating of Aerosol Jet-Printed Silver Inks", "https://doi.org/10.1002/adem.202100362"),
        ),
    ),
    Method(
        "C06",
        "laser-direct-structuring",
        "Laser Direct Structuring",
        "LDS",
        "#7570b3",
        5,
        (2_000, 10_000),
        (75_000, 300_000),
        "Fine three-dimensional circuits on laser-activatable polymers",
        "Enclosed laser activation and electroless line",
        "Industrial or university-service method",
        (
            "Laser Direct Structuring, abbreviated LDS, uses a focused laser to expose or activate catalyst sites in a compatible polymer surface. The activated path then initiates selective electroless metal deposition. The term originated in three-dimensional moulded interconnect device manufacturing, where electrical circuits are formed directly on shaped plastic rather than assembled as a separate flat printed circuit board.",
            "LDS offers precise digital routing, good three-dimensional integration and strong industrial relevance, but it is a system process rather than a single machine purchase. The polymer must contain or receive a suitable activator, laser wavelength and energy must create active sites without excessive damage, and the subsequent cleaning and electroless baths must preserve selectivity. Multi-axis access, focus, fumes and laser classification become important on complex printed parts.",
            "A student project should normally use an accredited laser and plating facility. The student can design activation coupons, simulate line-of-sight access, prepare safe process files and analyse microscopy, resistance and adhesion results. A pass requires both accurate laser patterning and selective metal growth; a visually darkened line that does not plate, or a plated line surrounded by unintended copper, is a failed process.",
        ),
        "A laser exposes catalytic sites in an activatable polymer, followed by selective electroless metal growth.",
        "Classified laser enclosure, multi-axis positioning, fume extraction, cleaning and electroless plating",
        "Laser-defined catalytic tracks selectively covered by metal",
        (
            "laser direct structuring system or accredited laser facility",
            "wavelength-compatible optics and focus control",
            "multi-axis fixture and registration",
            "fume extraction and laser safety interlocks",
            "cleaning and electroless plating line",
            "microscopy and surface-profile measurement",
            "electrical and adhesion test equipment",
        ),
        (
            "laser-activatable thermoplastic or approved activator coating",
            "reference activation coupons",
            "cleaning and electroless chemistry",
            "masking and handling fixtures",
            "metal-bearing waste containers",
        ),
        (
            "laser safety officer approval",
            "material supplier activation data",
            "facility design rules and file format",
            "defined line width, heat damage, selectivity and adhesion limits",
        ),
        (
            "Select an activatable polymer and obtain its processing window.",
            "Design a coupon with energy, speed, hatch and focus test zones.",
            "Simulate laser access and fixture rotations for the shaped part.",
            "Review the process under the facility laser-safety procedure.",
            "Activate reference coupons across the approved parameter matrix.",
            "Inspect track width, roughness, debris and thermal damage.",
            "Clean and electroless plate the parameter matrix.",
            "Measure selectivity, continuity, adhesion and minimum spacing.",
            "Run the best setting on three shaped coupons.",
            "Map focus and width changes around three-dimensional transitions.",
            "Compare service yield and route freedom against simpler methods.",
            "Release only the material, geometry and laser recipe that passed together.",
        ),
        (
            ("LDS-G0", "Laser and material release", "Facility approves material, wavelength, enclosure, extraction and file.", "Do not expose the material; use a non-laser seed route."),
            ("LDS-G1", "Activation window", "A repeatable parameter window produces active tracks without unacceptable polymer damage.", "Revise energy, speed, focus or material."),
            ("LDS-G2", "Selective metallization", "Metal grows on intended tracks while isolation zones remain below the leakage limit.", "Reject cleaning, activation or bath settings."),
            ("LDS-G3", "Three-dimensional repeatability", "Three shaped coupons pass line width, adhesion and resistance limits.", "Keep LDS at flat-coupon research stage."),
        ),
        (
            ("Laser exposure and fumes", "Use only an interlocked classified enclosure with trained facility operators and extraction."),
            ("Polymer heat damage", "Inspect profile and microscopy; enforce energy and temperature limits."),
            ("Focus loss on curves", "Use calibrated multi-axis motion and focus compensation."),
            ("Non-selective plating", "Use isolation coupons and stop the bath at the first background deposit."),
        ),
        (
            "material and laser approval records",
            "parameter matrix and source file",
            "activation microscopy and surface profile",
            "electroless bath log",
            "selectivity, resistance and adhesion results",
            "three-dimensional registration map",
            "service cost and yield assessment",
        ),
        "Use laser activation of a removable coating, dual-material conductive filament, or a service that accepts ordinary resins if LDS-grade material is unavailable.",
        (
            ("Selective metallization on copper aluminate composite by LDS", "https://doi.org/10.1016/j.compositesb.2016.11.041"),
            ("Hybrid vat printing and laser-activated metallization", "https://doi.org/10.1016/j.addma.2023.103388"),
        ),
    ),
    Method(
        "C07",
        "flash-ablation-metallization",
        "Flash Ablation Metallization",
        "FAM",
        "#e7298a",
        5,
        (2_000, 10_000),
        (20_000, 100_000),
        "Exposed conductive-composite faces and shallow traces",
        "Enclosed high-intensity pulsed-light processing",
        "Research collaboration method",
        (
            "Flash Ablation Metallization, abbreviated FAM, exposes a conductive composite polymer to a short pulse of high-intensity broad-spectrum light. The pulse removes or modifies part of the polymer-rich surface and leaves a denser network of conductive filler near the surface. The name combines flash exposure, surface ablation and metallization because the treatment converts a poorly conductive composite surface into a more useful electrical contact or plating seed.",
            "Published experiments report rapid, non-contact conductivity improvement and show that the method can support later electroless copper deposition on appropriate conductive thermoplastics. The process may be compatible with inline manufacturing, but it is strongly dependent on filler type, film thickness, pulse energy, distance, cooling and the optical response of the polymer. Shadowed or internal surfaces are not treated unless the light can reach them.",
            "This is not a recommended student-built flash lamp because stored electrical energy, intense light, ultraviolet exposure, hot debris and fumes create substantial hazards. A student project should use a qualified research facility and focus on coupon design, energy-response analysis, surface microscopy, resistance mapping and plating verification. The method passes only when conductivity improves without unacceptable warping, burning, cracking, loss of adhesion or damage to neighbouring insulation.",
        ),
        "A high-energy light pulse removes polymer-rich surface material and exposes a metal- or carbon-dense conductive network.",
        "Interlocked pulsed-light enclosure, energy control, cooling, extraction and surface metrology",
        "Ablated conductive-composite surface with lower contact resistance or improved plating activity",
        (
            "qualified photonic-curing or flash-lamp facility",
            "interlocked opaque enclosure and energy monitor",
            "controlled part distance and cooling fixture",
            "local exhaust and debris containment",
            "surface profilometer or microscopy",
            "four-wire resistance mapping",
            "electroless or electrolytic plating capability",
        ),
        (
            "conductive composite filament with documented filler",
            "thickness and colour reference coupons",
            "heat witness labels or embedded temperature sensors",
            "cleaning and plating materials",
            "approved debris and waste containers",
        ),
        (
            "facility photonic-process approval",
            "material-specific optical and thermal review",
            "coupon energy matrix",
            "defined conductance gain and damage limits",
        ),
        (
            "Print a controlled thickness series in the selected conductive composite.",
            "Measure baseline resistance, thickness, mass and surface appearance.",
            "Agree pulse-energy, distance, count and cooling limits with the facility.",
            "Expose sacrificial coupons across a conservative energy matrix.",
            "Inspect immediately for smoke, warping, blistering, cracking and debris.",
            "Measure conductance change and map surface uniformity.",
            "Use microscopy or profiling to relate conductivity to surface modification.",
            "Electroless plate or electroplate only undamaged passing coupons.",
            "Measure plating initiation, coverage, adhesion and final resistance.",
            "Repeat the selected exposure on three independent printed coupons.",
            "Test a shaped coupon with known shadowed regions.",
            "Document geometry exclusions and decide whether the gain justifies facility dependence.",
        ),
        (
            ("FAM-G0", "Facility safety", "Interlocks, optical containment, extraction and stored-energy controls are approved.", "Do not construct or operate a student flash source."),
            ("FAM-G1", "Damage limit", "No passing coupon exceeds the warp, crack, burn or insulation-damage limit.", "Reduce energy or reject the material."),
            ("FAM-G2", "Conductance response", "Three coupons achieve the minimum conductance gain with acceptable variation.", "Change composite, thickness or exposure recipe."),
            ("FAM-G3", "Plating benefit", "Treated coupons plate more reliably or reach the required resistance without new defects.", "Use untreated conductive filament or another seed process."),
        ),
        (
            ("Intense optical radiation", "Use an interlocked opaque facility enclosure; no direct observation."),
            ("Stored electrical energy", "Facility operators own discharge, lockout and maintenance."),
            ("Fumes and ejected debris", "Use extraction and closed debris capture."),
            ("Subsurface damage", "Inspect sectioned coupons and enforce conservative energy limits."),
        ),
        (
            "facility and interlock approval",
            "material batch and print thickness record",
            "pulse energy, count, distance and cooling log",
            "before-and-after surface images",
            "conductance improvement distribution",
            "plating initiation and adhesion result",
            "explicit shadow and geometry limits",
        ),
        "Use direct electroless plating of the conductive composite, mechanical surface preparation, or a lower-energy laser activation service.",
        (
            ("Flash ablation metallization of conductive thermoplastics", "https://doi.org/10.1016/j.addma.2020.101409"),
            ("Direct electroless plating of conductive thermoplastics", "https://doi.org/10.1016/j.addma.2022.102793"),
        ),
    ),
    Method(
        "C08",
        "physical-vapor-deposition",
        "Physical Vapor Deposition Seed Layer",
        "PVD",
        "#66a61e",
        4,
        (1_000, 5_000),
        (75_000, 500_000),
        "Thin external line-of-sight coatings and delicate templates",
        "Vacuum deposition through a facility or service",
        "Service-first method for uniform thin seeds",
        (
            "Physical Vapor Deposition, abbreviated PVD, transfers material from a solid source through a vacuum and condenses it as a thin film on the part. Common PVD families include evaporation and sputtering. In AE3PT a thin titanium, chromium, copper or multilayer film can serve as an adherent conductive seed that is later thickened by electroplating.",
            "PVD can produce clean, thin and well-controlled coatings without immersing the polymer in an activation bath, and published template processes have combined sputtered titanium-copper seed layers with subsequent copper electroplating. However, deposition is mainly line-of-sight. Deep channels, downward-facing surfaces and severe undercuts may receive little metal unless the part is rotated or multiple sources are used, and vacuum compatibility limits polymer choice, part size and trapped volumes.",
            "A student project should use a university vacuum facility or commercial coater. The student should design witness coupons, masks, rotation fixtures and electrical contacts, then compare film continuity before plating and adhesion after plating. The apparent capital cost is not the only concern: pump maintenance, targets, chamber cleaning, fixturing, staff time and contamination policy make ownership unrealistic for most hobby projects.",
        ),
        "Vacuum-transported metal atoms condense on exposed surfaces to form a thin conductive seed film.",
        "Vacuum chamber, evaporation or sputter source, rotation fixture, masks, thickness monitor and pump system",
        "Nanometre- to micrometre-scale metal seed ready for electroplating",
        (
            "qualified evaporation or sputtering facility",
            "vacuum-compatible part fixture and rotation",
            "shadow masks or removable resist",
            "film-thickness monitor",
            "surface cleaning or plasma treatment",
            "four-wire continuity fixture",
            "electroplating contacts designed for a fragile seed",
        ),
        (
            "approved polymer with low outgassing",
            "titanium, chromium, copper or specified target material",
            "witness slides and masked step-height coupons",
            "vacuum-compatible masking and fixturing",
            "clean packaging for transfer to plating",
        ),
        (
            "facility contamination and material approval",
            "vacuum outgassing review",
            "line-of-sight coverage analysis",
            "defined thickness, continuity and adhesion limits",
        ),
        (
            "Choose the adhesion layer, conductive layer and target thickness.",
            "Model or inspect line-of-sight access for every required surface.",
            "Design witness coupons and a fixture that exposes critical orientations.",
            "Clean and dry parts using the facility-approved sequence.",
            "Run a low-risk witness deposition before full shaped parts.",
            "Measure film thickness, continuity and resistance on witness locations.",
            "Deposit three shaped coupons with the frozen fixture and rotation.",
            "Inspect shadowed regions and isolation-mask boundaries.",
            "Attach plating contacts without scratching or burning the thin seed.",
            "Electroplate in staged current increments.",
            "Test plated adhesion, thickness and electrical performance.",
            "Compare service yield and coating access against electroless methods.",
        ),
        (
            ("PVD-G0", "Vacuum compatibility", "Facility approves polymer, adhesives, trapped volumes and cleanliness.", "Choose an electroless or surface-applied seed."),
            ("PVD-G1", "Seed coverage", "All required witness zones meet minimum thickness and continuity.", "Change rotation, source angle, masking or geometry."),
            ("PVD-G2", "Contact survival", "The thin seed accepts plating current without local burnout or peeling.", "Redesign contacts or deposit a thicker seed."),
            ("PVD-G3", "Plated adhesion", "Three plated coupons pass the selected adhesion and resistance limits.", "Change surface preparation or adhesion-layer material."),
        ),
        (
            ("Vacuum-system hazards", "Facility operators own high voltage, vacuum, cooling and maintenance."),
            ("Polymer outgassing", "Pre-dry approved materials and use witness monitoring."),
            ("Shadowed coating", "Use rotation, multiple orientations and explicit geometry exclusions."),
            ("Seed damage in handling", "Use clean carriers, protected contact tabs and minimum handling."),
        ),
        (
            "facility material acceptance",
            "fixture and line-of-sight drawing",
            "target, pressure, power and deposition record",
            "witness thickness measurements",
            "seed continuity and isolation map",
            "post-plating adhesion and resistance",
            "service cost, yield and lead time",
        ),
        "Use electroless seeding for hidden surfaces, or a sprayed and masked conductive coating when vacuum access or budget is unavailable.",
        (
            ("Vapor-deposited seed layers for electrodeposition on printed polymers", "https://digitalcommons.unf.edu/etd/934/"),
        ),
    ),
    Method(
        "C09",
        "laser-induced-graphene",
        "Laser-Induced Graphene Seed",
        "LIG",
        "#a6761d",
        4,
        (1_000, 5_000),
        (10_000, 75_000),
        "Exposed laser-accessible carbon-forming surfaces",
        "Enclosed laser writing followed by copper deposition",
        "Advanced student research with facility laser",
        (
            "Laser-Induced Graphene, abbreviated LIG, is a porous carbon-rich conductive material formed when a suitable polymer or precursor coating is locally converted by a laser. The name describes both the energy source and the graphitic product. In AE3PT the laser-written carbon network can act as a patterned electrode or a seed for later copper electrodeposition, potentially avoiding a separately printed metal ink.",
            "LIG is attractive because the electrical pattern is digitally written and the porous surface can provide many nucleation sites for metal deposition. The process is material-specific: polyimide is widely used in research, while other polymers may need a carbon-forming coating or tailored formulation. Laser wavelength, power, speed, focus, atmosphere and repeat passes affect conductivity, adhesion, pore structure and polymer damage.",
            "A student should undertake LIG only with an approved enclosed laser and a tightly bounded coupon program. The useful questions are whether the selected printable substrate or coating can form a continuous path, whether that path survives bending and handling, and whether copper deposits evenly without delamination. Hidden channels and surfaces outside laser line-of-sight remain unsuitable, and the project must keep carbonisation fumes and fire risk under formal laboratory control.",
        ),
        "A laser locally carbonises a compatible polymer or coating into a conductive porous graphitic path.",
        "Interlocked laser writer, extraction, material fixture, resistance mapping and copper deposition cell",
        "Patterned porous carbon seed that can receive electrodeposited copper",
        (
            "interlocked laser engraver or research laser facility",
            "wavelength and focus control",
            "fume extraction with material-specific filtration",
            "fire-resistant coupon fixture",
            "microscope and surface-profile measurement",
            "four-wire resistance mapping",
            "low-current copper electrodeposition cell",
        ),
        (
            "polyimide or approved carbon-forming precursor coating",
            "printed support or laminate coupons",
            "clean electrical contact materials",
            "copper-plating electrolyte under laboratory control",
            "sealed carbonaceous waste containers",
        ),
        (
            "laser and fume-risk approval",
            "material-specific literature and supplier review",
            "parameter matrix with conservative energy limits",
            "defined resistance, adhesion and fire-damage criteria",
        ),
        (
            "Select one substrate or carbon-forming coating and freeze its thickness.",
            "Design a laser matrix covering power, speed, focus and pass count.",
            "Commission extraction and a fire-safe fixture under facility rules.",
            "Write reference lines and stop immediately on flaming or uncontrolled smoke.",
            "Measure line width, surface profile and end-to-end resistance.",
            "Select a process window that balances conductivity and substrate integrity.",
            "Write three conductor coupons and one shaped coupon.",
            "Test adhesion, bending or handling durability as appropriate.",
            "Attach distributed contacts and begin copper deposition at low current.",
            "Measure copper coverage, mass gain, resistance and adhesion.",
            "Compare the copper-LIG path with painted and conductive-filament seeds.",
            "Release only if material, laser and plating evidence are reproducible.",
        ),
        (
            ("LIG-G0", "Laser and fire safety", "Interlocks, extraction, material approval and fire response pass review.", "Do not laser-carbonise the material."),
            ("LIG-G1", "Conductive conversion", "Three laser-written coupons meet resistance and dimensional limits without unacceptable damage.", "Change precursor, power, speed, focus or pass count."),
            ("LIG-G2", "Mechanical survival", "The seed remains continuous after the defined handling or bending test.", "Change substrate, pattern or protective design."),
            ("LIG-G3", "Copper integration", "Copper deposits continuously and passes adhesion and resistance limits.", "Return to a metal-bearing seed or modify contact distribution."),
        ),
        (
            ("Fire and hot carbon", "Use a fire-resistant fixture, interlocked enclosure and trained operator."),
            ("Carbonisation fumes", "Use material-specific extraction and prohibit unknown polymers."),
            ("Fragile porous trace", "Use protected geometry and perform handling tests before plating."),
            ("Non-uniform copper growth", "Use distributed contacts, staged current and agitation approved by the laboratory."),
        ),
        (
            "material and laser approval",
            "laser parameter matrix",
            "line-width and surface-profile maps",
            "pre-plating resistance distribution",
            "handling or bend-test evidence",
            "copper mass, coverage and resistance",
            "comparison with lower-risk seed routes",
        ),
        "Use a conductive paint, conductive filament or professionally laser-activated metal catalyst when the substrate cannot form stable LIG.",
        (
            ("Laser-induced graphene and copper deposition on printed polyimides", "https://doi.org/10.1002/admt.202401801"),
        ),
    ),
    Method(
        "C10",
        "catalyst-loaded-resin",
        "Catalyst-Loaded Multi-Material Resin",
        "CLMR",
        "#1f9ac7",
        5,
        (2_000, 10_000),
        (25_000, 150_000),
        "Free-form selectively metallised vat-printed structures",
        "Multi-material vat printing plus electroless plating",
        "Research thesis extension, not baseline build",
        (
            "Catalyst-Loaded Multi-Material Resin, abbreviated CLMR, embeds a metal-ion or catalytic precursor inside selected regions of a photocurable resin. A multi-material vat-printing process places catalyst-bearing resin where metal is required and ordinary resin elsewhere. After printing and post-curing, the active regions initiate electroless metal deposition, turning material identity itself into the patterning method.",
            "This approach can create free-form three-dimensional metallised paths without a separate spray, dispenser or line-of-sight activation step. Its difficulty comes from resin formulation, particle or salt dispersion, optical absorption, cure depth, interface bonding, vat contamination, material exchange and bath chemistry. The printed geometry, resin chemistry and exposure settings are tightly coupled, so a successful result cannot be transferred casually to another printer or resin.",
            "CLMR is best treated as an advanced research extension after the simpler AE3PT busbar project is complete. A student with polymer, chemistry and vat-printing supervision can study small interface coupons, catalytic concentration, cure behaviour and plating selectivity. The method fails closed if active resin contaminates inactive regions, if cure quality is uncertain, or if the chemical and uncured-resin waste route is not formally approved.",
        ),
        "Catalytic precursor is printed only in selected resin volumes, which later initiate electroless metal deposition.",
        "Multi-material vat printer, controlled resin exchange, wash and cure stations, electroless line and optical metrology",
        "Material-defined active regions selectively metallised after printing",
        (
            "multi-material Digital Light Processing or stereolithography printer",
            "controlled resin mixing and degassing equipment",
            "separate labelled vats or automated material exchange",
            "exposure calibration and cure-depth measurement",
            "closed washing and post-curing stations",
            "approved electroless plating line",
            "microscopy, resistance and adhesion test equipment",
        ),
        (
            "base photocurable resin",
            "approved metal salt, catalyst or active filler",
            "inactive reference resin",
            "dedicated wash materials and filters",
            "electroless metal bath and controlled waste containers",
        ),
        (
            "chemical and uncured-resin approval",
            "material formulation plan with concentration limits",
            "printer contamination and cleaning procedure",
            "defined cure, interface, selectivity and plating criteria",
        ),
        (
            "Choose one published catalyst family and one compatible base resin.",
            "Prepare a written formulation, labelling, mixing and waste procedure.",
            "Measure optical cure depth across a conservative concentration series.",
            "Print single-material active and inactive reference coupons.",
            "Wash and cure each coupon using a controlled, recorded sequence.",
            "Electroless plate reference coupons to confirm activity and background deposition.",
            "Print two-material interface coupons with wide alignment features.",
            "Inspect interface bonding, cure inhibition and cross-contamination.",
            "Plate three passing interface coupons and map selectivity.",
            "Measure resistance, adhesion, dimensional change and uncured residue.",
            "Attempt one simple three-dimensional route only after all coupon gates pass.",
            "Archive formulation, exposure, cleaning and bath evidence as one inseparable recipe.",
        ),
        (
            ("CLMR-G0", "Chemical and resin authority", "Named staff approve catalyst, resin, washing, exposure and waste routes.", "Do not formulate or print active resin."),
            ("CLMR-G1", "Printability", "Active and inactive coupons meet cure depth, dimensions and mechanical handling limits.", "Change concentration, exposure or resin system."),
            ("CLMR-G2", "Material isolation", "Two-material interfaces remain bonded and background catalyst transfer stays below the limit.", "Stop multi-material work and improve vat exchange or masking."),
            ("CLMR-G3", "Selective plating", "Metal deposits on active regions across three coupons while inactive regions remain isolated.", "Reject the formulation or cleaning process."),
        ),
        (
            ("Uncured resin exposure", "Use closed handling, gloves selected by risk assessment and dedicated wash controls."),
            ("Catalyst or metal-salt toxicity", "Use the minimum quantity in a supervised laboratory and collect all contaminated waste."),
            ("Cross-contamination", "Use separate vats, blank wash checks and contamination witness coupons."),
            ("Incomplete cure", "Measure cure depth, use conservative exposure and reject tacky or uncertain parts."),
        ),
        (
            "approved formulation and batch sheet",
            "cure-depth and dimensional calibration",
            "printer cleaning and contamination checks",
            "interface microscopy",
            "active versus inactive plating map",
            "resistance, adhesion and mechanical handling results",
            "resin, wash and metal-waste record",
        ),
        "Use commercial conductive filament, a surface-applied seed or an external selective-metallization service rather than formulating active resin.",
        (
            ("Self-activating metal-polymer composites", "https://doi.org/10.1016/j.jmrt.2022.12.035"),
            ("Self-activating resins for 3D printed parts", "https://doi.org/10.1016/j.addma.2026.105129"),
        ),
    ),
)


def money(cost: tuple[int, int]) -> str:
    return f"USD ${cost[0]:,}–${cost[1]:,}"


def difficulty_label(value: int) -> str:
    labels = {1: "introductory", 2: "moderate", 3: "intermediate", 4: "advanced", 5: "research-grade"}
    return f"{value}/5 — {labels[value]}"


def bullet_lines(items: tuple[str, ...]) -> str:
    return "\n".join(f"- {item}" for item in items)


def numbered_lines(items: tuple[str, ...]) -> str:
    return "\n".join(f"{index}. {item}" for index, item in enumerate(items, start=1))


def normalize_markdown(rendered: str) -> str:
    """Remove template indentation without changing generated list indentation."""
    lines = rendered.splitlines()
    normalized = [line[8:] if line.startswith("        ") else line for line in lines]
    while normalized and not normalized[-1].strip():
        normalized.pop()
    return "\n".join(normalized).lstrip("\n") + "\n"


def method_markdown(method: Method) -> str:
    gate_rows = "\n".join(
        f"| {code} | {name} | {pass_text} | {fail_text} |"
        for code, name, pass_text, fail_text in method.gates
    )
    risk_rows = "\n".join(f"| {risk} | {control} |" for risk, control in method.risks)
    references = "\n".join(f"- [{label}]({url})" for label, url in method.research)
    return normalize_markdown(
        f"""
        # {method.method_id} — {method.title}

        **Acronym:** {method.acronym} · **Difficulty:** {difficulty_label(method.difficulty)} · **Student trial allowance:** {money(method.trial_cost)} · **Ownership allowance:** {money(method.capital_cost)}

        [← Conductive Coating Methods](index.md)

        ![{method.title} implementation and pass/fail diagram](../diagrams/conductive-coatings/{method.slug}.svg)

        ## Three-Paragraph Description

        {method.description[0]}

        {method.description[1]}

        {method.description[2]}

        ## Student Planning Card

        | Planning field | Project value |
        |---|---|
        | Method identifier | {method.method_id} |
        | Expanded name | {method.title} |
        | Acronym | {method.acronym} |
        | Difficulty | {difficulty_label(method.difficulty)} |
        | Student trial allowance | {money(method.trial_cost)} |
        | Ownership or capital allowance | {money(method.capital_cost)} |
        | Best geometry | {method.best_geometry} |
        | Automation level | {method.automation_level} |
        | Recommended role | {method.recommendation} |

        The allowances are AE3PT planning envelopes in 2026 United States dollars, not supplier quotations. They include representative fixtures, guarding, extraction and qualification work, exclude routine labour and building services, and must be replaced by local written quotations before money is released.

        ## Operating Principle

        **Process principle:** {method.principle}

        **Automation cell:** {method.automation_cell}

        **Required output:** {method.seed_result}

        The coating is a **seed layer**: a thin electrically active starting surface. It is not automatically the final current-carrying conductor. The supervised electroplating stage adds the copper thickness required by the electrical and thermal design.

        ## Required Equipment

        {bullet_lines(method.equipment)}

        ## Required Materials

        {bullet_lines(method.materials)}

        ## Prerequisites

        {bullet_lines(method.prerequisites)}

        ## Complete Implementation Microsteps

        {numbered_lines(method.microsteps)}

        ## Pass/Fail Gates

        | Gate | Decision | Pass condition | Fail action |
        |---|---|---|---|
        {gate_rows}

        A gate is passed only by current evidence from the frozen material, geometry and process recipe. A result from another substrate, previous bath, different machine file or unrecorded operator adjustment cannot release the next stage.

        ## Safety and Process Controls

        | Main risk | Required control |
        |---|---|
        {risk_rows}

        Any abnormal heat, smell, gas, smoke, colour change, electrical behaviour, equipment sound or solution condition is a stop signal. Students make no independent substitutions to coatings, catalysts, plating baths, cleaning agents or laser settings.

        ## Minimum Evidence Package

        {bullet_lines(method.evidence)}

        ## Cost-Control Plan

        1. Buy or book only enough capacity for flat and shaped coupons.
        2. Pass the safety and path-control gate before consuming conductive material.
        3. Pass the seed gate before using copper bath time.
        4. Require three independently prepared results before purchasing upgrades.
        5. Compare cost per passing sample, not cost per machine hour or cost per printed part.
        6. Preserve a lower-cost fallback in the design so one failed process does not end the project.

        ## Fallback

        {method.fallback}

        ## Research Basis

        {references}

        These readings establish technical plausibility and important process variables; they do not certify the student apparatus, chemistry, material combination or final part.

        ## Final Decision Rule

        Adopt {method.acronym} only when it produces repeatable seed continuity, controlled isolation, acceptable adhesion and successful copper thickening at a cost and safety level justified by geometry that a simpler method cannot meet. Otherwise record the result, preserve the evidence and return to the stated fallback.
        """
    )


def overview_markdown() -> str:
    rows = "\n".join(
        f"| [{method.method_id}](./{method.slug}.md) | {method.title} ({method.acronym}) | {method.difficulty}/5 | {money(method.trial_cost)} | {money(method.capital_cost)} | {method.recommendation} |"
        for method in METHODS
    )
    plan_links = "\n".join(
        f"{index}. [{method.method_id} — {method.title}]({method.slug}.md)"
        for index, method in enumerate(METHODS, start=1)
    )
    return normalize_markdown(
        f"""
        # Conductive Coating Methods: Ten Complete Student Plans

        **Library purpose:** compare automated ways to make selected regions of a three-dimensional printed polymer conductive before supervised copper electroplating.

        ![Ten conductive coating methods arranged by cost, difficulty and recommended student path](../diagrams/conductive-coatings/method-selection-map.svg)

        ## Three-Paragraph Description

        This library turns ten conductive-coating suggestions into comparable engineering plans. Every method has the same planning fields: expanded name and acronym, operating principle, equipment, materials, implementation microsteps, pass/fail gates, evidence, safety controls, fallback, difficulty and cost. A student can therefore compare methods by the work and proof they require rather than by promotional claims or a visually impressive machine.

        The methods range from a student-built gantry dispenser to research-grade laser, vacuum, aerosol and multi-material resin systems. The project should start at the lowest complexity capable of reaching the required geometry. Advanced processes are included because they may solve fine-feature, conformal or hidden-surface problems, but they should normally be accessed as shared university equipment or contracted services rather than purchased for one undergraduate demonstrator.

        Each coating is treated as a seed layer for later copper thickening, not as an assumed final power conductor. The common decision loop is design, deposit, inspect, measure, plate, test and either release or return to a fallback. This keeps conductive coating, electroplating, electrical performance, cost, safety and repair evidence inside one traceable AE3PT student workflow.

        ## Recommended Low-Budget Sequence

        1. If a JG MAKER Artist-D is already available, evaluate the [machine-specific dual-material copper electroplating plan](../artist-d-electroplating-plan.md) as a difficulty 4/5 parallel route.
        2. Otherwise begin with **{METHODS[0].method_id} gantry dispensing** for open grooves and pads.
        3. Add **{METHODS[1].method_id} robotic spray** only when broad area coverage is required.
        4. Use **{METHODS[2].method_id} automated electroless seeding** through a supervised laboratory when complex surfaces justify wet processing.
        5. Purchase service coupons for C04–C10 only after a simpler method fails a named geometry or performance requirement.
        6. Never buy advanced equipment merely to increase project novelty.

        The Artist-D route does not create an eleventh coating chemistry. It automates placement of the conductive filament seed before copper electroplating. Its main risks are IDEX alignment, conductive contamination, high and variable seed resistance, plating voltage drop and current crowding near the electrical contact.

        ## Difficulty and Cost Register

        | Plan | Method | Difficulty | Student trial allowance | Ownership allowance | Recommended role |
        |---|---|---:|---:|---:|---|
        {rows}

        The cost values are broad AE3PT planning envelopes in 2026 United States dollars. They are not vendor prices. They include representative fixtures, guarding, extraction and qualification, exclude routine labour and building services, and should be replaced with local written quotations before any purchase decision.

        ## The Ten Plans

        {plan_links}

        ## Common Pass/Fail Architecture

        Every plan applies the same five questions:

        1. **Authority:** Are the equipment, material, chemical and waste controls approved?
        2. **Placement:** Did the automated process place or activate material only where intended?
        3. **Seed:** Is the starting layer continuous, adherent and electrically suitable?
        4. **Copper:** Does supervised electroplating thicken the route without burning, bridging or peeling?
        5. **Value:** Does the method solve a geometry or performance need that a cheaper process cannot solve?

        Failure at any gate returns the project to coupons or to the named fallback. It never authorises an improvised chemical, laser, vacuum, pressure or electrical change.

        ## Machine-Readable Register

        The comparison data are available in [`../data/conductive-coating-methods.csv`](../data/conductive-coating-methods.csv). The Markdown plans, Scalable Vector Graphics diagrams and register are generated by `tools/build_coating_method_plans.py`. Run the generator after changing the method specification and run it with `--check` to detect drift.

        ## Scope Boundary

        This library supports an educational five-volt coupon and low-power busbar demonstrator. It does not certify a production process, pressure vessel, motor winding, medical device, high-voltage component or chemically compliant facility. Professional review remains necessary before industrial scaling.
        """
    )


def xml_text(value: str) -> str:
    return html.escape(value, quote=True)


def wrapped_text(x: int, y: int, text: str, width: int, css_class: str = "body", line_height: int = 24, anchor: str | None = None) -> str:
    words_per_line = max(12, width // 9)
    lines = textwrap.wrap(text, width=words_per_line, break_long_words=False)
    anchor_attribute = f' text-anchor="{anchor}"' if anchor else ""
    spans = []
    for index, line in enumerate(lines):
        dy = "0" if index == 0 else str(line_height)
        spans.append(f'<tspan x="{x}" dy="{dy}">{xml_text(line)}</tspan>')
    return f'<text class="{css_class}" x="{x}" y="{y}"{anchor_attribute}>{"".join(spans)}</text>'


def process_box(x: int, y: int, width: int, height: int, number: str, title: str, detail: str, accent: str) -> str:
    return f'''<g transform="translate({x},{y})">
  <rect width="{width}" height="{height}" rx="18" fill="#ffffff" stroke="{accent}" stroke-width="2"/>
  <circle cx="30" cy="30" r="18" fill="{accent}"/><text class="step" x="30" y="36" text-anchor="middle">{xml_text(number)}</text>
  {wrapped_text(58, 28, title, width - 72, "boxTitle", 21)}
  {wrapped_text(20, 72, detail, width - 40, "body", 23)}
</g>'''


def base_svg(title: str, description: str, body: str, view_box: str = "0 0 1400 900") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" role="img" aria-labelledby="title desc">
<title id="title">{xml_text(title)}</title>
<desc id="desc">{xml_text(description)}</desc>
<defs>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="7" stdDeviation="10" flood-color="#10243d" flood-opacity="0.12"/></filter>
  <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#52657a"/></marker>
  <style>
    .title{{font:700 34px Inter,Arial,sans-serif;fill:#10243d}}
    .subtitle{{font:500 18px Inter,Arial,sans-serif;fill:#52657a}}
    .section{{font:700 18px Inter,Arial,sans-serif;fill:#10243d}}
    .boxTitle{{font:700 17px Inter,Arial,sans-serif;fill:#10243d}}
    .body{{font:500 16px Inter,Arial,sans-serif;fill:#31465d}}
    .small{{font:600 14px Inter,Arial,sans-serif;fill:#52657a}}
    .metric{{font:800 24px Inter,Arial,sans-serif;fill:#10243d}}
    .step{{font:800 16px Inter,Arial,sans-serif;fill:#ffffff}}
    .arrow{{stroke:#52657a;stroke-width:3;fill:none;marker-end:url(#arrow)}}
  </style>
</defs>
<rect width="1400" height="900" fill="#f5f8fc"/>
{body}
</svg>
'''


def method_svg(method: Method) -> str:
    trial = money(method.trial_cost).replace("USD ", "")
    capital = money(method.capital_cost).replace("USD ", "")
    process = (
        ("1", "Digital input", "Frozen geometry, material, path and acceptance limits"),
        ("2", "Automation cell", method.automation_cell),
        ("3", "Seed inspection", "Verify location, continuity, adhesion and isolation"),
        ("4", "Copper thickening", "Supervised staged electroplating with recorded contacts"),
        ("5", "Evidence gate", "Electrical, thermal, repeatability, cost and fallback decision"),
    )
    boxes = []
    x_positions = (40, 310, 580, 850, 1120)
    for x, (number, title, detail) in zip(x_positions, process):
        boxes.append(process_box(x, 252, 240, 208, number, title, detail, method.accent))
    arrows = "".join(f'<path class="arrow" d="M{x + 240} 346H{x + 263}"/>' for x in x_positions[:-1])
    gate = method.gates[-1]
    body = f'''
<rect x="28" y="24" width="1344" height="852" rx="28" fill="#ffffff" filter="url(#shadow)"/>
<rect x="28" y="24" width="14" height="852" rx="7" fill="{method.accent}"/>
<text class="title" x="72" y="76">{xml_text(method.method_id)} — {xml_text(method.title)}</text>
<text class="subtitle" x="72" y="110">Automated conductive seed plan for a supervised copper electroplating workflow</text>

<g transform="translate(72,142)"><rect width="250" height="78" rx="16" fill="#edf8f6"/><text class="small" x="18" y="27">DIFFICULTY</text><text class="metric" x="18" y="57">{method.difficulty}/5</text></g>
<g transform="translate(340,142)"><rect width="300" height="78" rx="16" fill="#eef4ff"/><text class="small" x="18" y="27">STUDENT TRIAL</text><text class="metric" x="18" y="57">{xml_text(trial)}</text></g>
<g transform="translate(658,142)"><rect width="310" height="78" rx="16" fill="#fff6e8"/><text class="small" x="18" y="27">OWNERSHIP ALLOWANCE</text><text class="metric" x="18" y="57">{xml_text(capital)}</text></g>
<g transform="translate(986,142)"><rect width="346" height="78" rx="16" fill="#f4effb"/><text class="small" x="18" y="27">RECOMMENDED ROLE</text>{wrapped_text(18, 53, method.recommendation, 314, "body", 20)}</g>

{''.join(boxes)}
{arrows}

<g transform="translate(54,486)"><rect width="404" height="154" rx="18" fill="#eef8ff" stroke="#2878c8" stroke-width="2"/><text class="section" x="22" y="34">Best geometry</text>{wrapped_text(22, 67, method.best_geometry, 360, "body", 24)}</g>
<g transform="translate(482,486)"><rect width="404" height="154" rx="18" fill="#fff7e9" stroke="#d28b1f" stroke-width="2"/><text class="section" x="22" y="34">Required seed result</text>{wrapped_text(22, 67, method.seed_result, 360, "body", 24)}</g>
<g transform="translate(910,486)"><rect width="436" height="154" rx="18" fill="#fff1f1" stroke="#d84d4d" stroke-width="2"/><text class="section" x="22" y="34">Stop condition</text>{wrapped_text(22, 67, "Any unapproved hazard, misplaced conductor, failed continuity, bridging, peeling, overheating or uncontrolled process change.", 392, "body", 24)}</g>

<g transform="translate(54,672)"><rect width="610" height="164" rx="20" fill="#edf8f2" stroke="#31a56c" stroke-width="2"/><text class="section" x="24" y="36">PASS — {xml_text(gate[0])}: {xml_text(gate[1])}</text>{wrapped_text(24, 72, gate[2], 558, "body", 24)}<text class="small" x="24" y="141">Release only the frozen material + geometry + process recipe.</text></g>
<g transform="translate(692,672)"><rect width="654" height="164" rx="20" fill="#fff1f1" stroke="#d84d4d" stroke-width="2"/><text class="section" x="24" y="36">FAIL — RETURN TO THE FALLBACK</text>{wrapped_text(24, 72, method.fallback, 606, "body", 24)}</g>
'''
    return base_svg(
        f"{method.method_id} {method.title} plan",
        f"Difficulty and cost metrics followed by a five-step process from digital input through seed deposition, inspection, copper electroplating and pass or fallback evidence.",
        body,
    )


def overview_svg() -> str:
    cards = []
    columns = ((54, 286, "STUDENT-BUILT", METHODS[:2], "#1b9e77"), (490, 286, "SHARED LAB", METHODS[2:4], "#7357b4"), (926, 286, "ADVANCED SERVICE / RESEARCH", METHODS[4:], "#d95f02"))
    for x, y, heading, methods, accent in columns:
        row_height = 78
        height = 72 + len(methods) * row_height
        cards.append(f'<g transform="translate({x},{y})"><rect width="420" height="{height}" rx="22" fill="#ffffff" stroke="{accent}" stroke-width="2"/><rect width="420" height="56" rx="22" fill="{accent}"/><text class="step" x="20" y="35">{xml_text(heading)}</text>')
        for index, method in enumerate(methods):
            offset = 70 + index * row_height
            cards.append(f'<circle cx="28" cy="{offset + 22}" r="17" fill="{method.accent}"/><text class="step" x="28" y="{offset + 28}" text-anchor="middle">{xml_text(method.method_id[1:])}</text>')
            cards.append(wrapped_text(58, offset + 10, f"{method.acronym} — {method.title}", 336, "boxTitle", 18))
            cards.append(f'<text class="small" x="58" y="{offset + 60}">Difficulty {method.difficulty}/5 · trial {xml_text(money(method.trial_cost).replace("USD ", ""))}</text>')
        cards.append('</g>')
    body = f'''
<rect x="28" y="24" width="1344" height="852" rx="28" fill="#ffffff" filter="url(#shadow)"/>
<text class="title" x="70" y="76">AE3PT Conductive Coating Method Selection Map</text>
<text class="subtitle" x="70" y="110">Begin with the lowest-complexity process that can reach the required geometry.</text>
<g transform="translate(70,146)"><rect width="1260" height="98" rx="18" fill="#eef5ff"/><text class="section" x="22" y="34">Recommended low-budget progression</text><text class="metric" x="22" y="72">C01 DISPENSE → C02 SPRAY → C03 ELECTROLESS LAB → C04–C10 SERVICE ONLY WHEN JUSTIFIED</text></g>
<path class="arrow" d="M436 264H482"/><path class="arrow" d="M872 264H918"/>
{''.join(cards)}
<text class="small" x="70" y="852">Cost bands are AE3PT 2026 planning allowances, not quotations. Difficulty includes process control, safety, metrology and repeatability—not only machine motion.</text>
'''
    return base_svg(
        "AE3PT conductive coating method selection map",
        "Ten methods grouped as student-built, shared laboratory and advanced service or research routes, with a recommended low-budget progression.",
        body,
    )


def register_csv() -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(
        (
            "method_id",
            "slug",
            "title",
            "acronym",
            "difficulty_1_to_5",
            "student_trial_cost_low_usd",
            "student_trial_cost_high_usd",
            "ownership_cost_low_usd",
            "ownership_cost_high_usd",
            "best_geometry",
            "automation_level",
            "student_recommendation",
            "fallback",
            "svg_file",
            "document_file",
        )
    )
    for method in METHODS:
        writer.writerow(
            (
                method.method_id,
                method.slug,
                method.title,
                method.acronym,
                method.difficulty,
                method.trial_cost[0],
                method.trial_cost[1],
                method.capital_cost[0],
                method.capital_cost[1],
                method.best_geometry,
                method.automation_level,
                method.recommendation,
                method.fallback,
                f"diagrams/conductive-coatings/{method.slug}.svg",
                f"conductive-coatings/{method.slug}.md",
            )
        )
    return stream.getvalue()


def expected_outputs(project_root: Path) -> dict[Path, str]:
    docs_root = project_root / "docs"
    outputs: dict[Path, str] = {
        docs_root / "conductive-coatings" / "index.md": overview_markdown(),
        docs_root / "diagrams" / "conductive-coatings" / "method-selection-map.svg": overview_svg(),
        docs_root / "data" / "conductive-coating-methods.csv": register_csv(),
    }
    for method in METHODS:
        outputs[docs_root / "conductive-coatings" / f"{method.slug}.md"] = method_markdown(method)
        outputs[docs_root / "diagrams" / "conductive-coatings" / f"{method.slug}.svg"] = method_svg(method)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="fail if generated files differ from the current specification")
    arguments = parser.parse_args()
    project_root = arguments.project_root.resolve()
    outputs = expected_outputs(project_root)
    changed: list[str] = []

    for path, content in outputs.items():
        relative = path.relative_to(project_root).as_posix()
        if arguments.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                changed.append(relative)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"generated {relative}")

    if changed:
        print("conductive coating plan generation drift detected:")
        for path in changed:
            print(f"  {path}")
        return 1
    if arguments.check:
        print(f"conductive coating plan set is current: {len(METHODS) + 1} Markdown files, {len(METHODS) + 1} SVG files and one CSV register")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
