#!/usr/bin/env python3
"""Generate the complete AE3PT-Lite student project SVG diagram set."""

from __future__ import annotations

import argparse
import csv
import html
import io
import textwrap
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Phase:
    diagram_id: str
    slug: str
    title: str
    weeks: str
    section: str
    accent: str
    purpose: str
    inputs: tuple[str, ...]
    tools: tuple[str, ...]
    safety: tuple[str, ...]
    actions: tuple[tuple[str, str], ...]
    evidence: tuple[str, ...]
    gate_code: str
    gate_text: str
    handoff: str
    detail_kind: str


PHASES = (
    Phase(
        "D01",
        "step-01-understand-approve",
        "Understand and approve",
        "Weeks 1–2",
        "weeks-1-2-understand-and-approve",
        "#18a79e",
        "Turn the idea into one safe, shared and explainable classroom mission before any building begins.",
        ("plain-language project brief", "5 V / 2 A / 50 °C limits", "laboratory and course rules"),
        ("scope worksheet", "risk-assessment template", "team-role record"),
        ("no construction before approval", "no chemical work by students alone", "unknown hazards stop the phase"),
        (
            ("Explain", "Describe the project without specialist language."),
            ("Fix limits", "Agree voltage, current, temperature and budget boundaries."),
            ("Assign roles", "Name design, measurement, software and business leads."),
            ("Assess risk", "Identify hazards, consequences and controls."),
            ("Review", "Present scope and controls for Gate G0."),
        ),
        ("one-paragraph mission", "approved risk assessment", "named team roles", "baseline limits table"),
        "G0",
        "Every student can explain the purpose and controls; lecturer and laboratory approve the scope.",
        "Proceed to calculations and printer coupons.",
        "approval",
    ),
    Phase(
        "D02",
        "step-02-calculate-coupons",
        "Calculate and print coupons",
        "Weeks 3–5",
        "weeks-3-5-hand-calculations-and-coupons",
        "#2f78db",
        "Use simple electrical calculations and small prints to learn before committing material to nine samples.",
        ("trial length, width and thickness", "copper resistivity", "printer and material choice"),
        ("calculator or Python", "Computer-Aided Design software", "3D printer and calliper"),
        ("convert units before calculating", "guard hot printer surfaces", "record failed coupons rather than hiding them"),
        (
            ("Calculate area", "Area equals width multiplied by copper thickness."),
            ("Predict resistance", "Use resistivity, length and area."),
            ("Predict heating", "Estimate power at the planned current."),
            ("Print coupons", "Make small dimensional and coating test pieces."),
            ("Update rules", "Measure coupons and revise allowable dimensions."),
        ),
        ("checked calculation sheet", "three measured coupons", "printer capability table", "revised design rules"),
        "Preparation gate",
        "Calculations are unit-consistent and repeated coupons meet the lecturer-approved dimensional range.",
        "Use measured rules to build the loggers and freeze designs.",
        "calculate",
    ),
    Phase(
        "D03",
        "step-03-build-loggers",
        "Build the measurement tools",
        "Weeks 4–7",
        "weeks-4-7-build-loggers",
        "#7659d7",
        "Build low-voltage instruments that measure current, sample voltage and four temperatures with traceable checks.",
        ("5 V current-limited supply", "current shunt and voltage converter", "four digital temperature sensors"),
        ("microcontroller", "breadboard then stripboard", "trusted comparison meter"),
        ("2.5 A fuse and main switch", "guard load resistors", "invalid sensor or 50 °C reading stops the test"),
        (
            ("Build fixture", "Wire supply, fuse, switch, load and sample terminals."),
            ("Measure current", "Read voltage across the known current shunt."),
            ("Measure sample", "Use separate current and voltage-sense leads."),
            ("Add temperature", "Identify and position four sensor channels."),
            ("Calibrate", "Compare references and prove every stop condition."),
        ),
        ("wiring diagram", "firmware and channel map", "calibration table", "fault and stop test record"),
        "G1",
        "Current and temperature readings are repeatable, labelled and within the agreed classroom tolerance.",
        "Provide verified measurements to the software phase.",
        "logger",
    ),
    Phase(
        "D04",
        "step-04-write-software",
        "Write simple calculation software",
        "Weeks 6–9",
        "weeks-6-9-write-simple-software",
        "#4d8cf2",
        "Turn equations and raw measurements into transparent, tested calculations and one repeatable report.",
        ("mission limits", "geometry and material values", "Comma-Separated Values measurement format"),
        ("Python", "code editor", "pytest automated checks"),
        ("software never replaces the physical stop", "retain original raw data", "failed tests block later analysis"),
        (
            ("Store inputs", "Keep mission, geometry and material values in clear modules."),
            ("Calculate", "Implement resistance, power and temperature estimates."),
            ("Read data", "Import logger tables without editing the originals."),
            ("Test code", "Check units, limits and hand-calculation examples."),
            ("Report", "Create one comparison table and one figure."),
        ),
        ("readable source files", "automated test results", "example input dataset", "reproducible report output"),
        "G2",
        "Software agrees with approved hand calculations and fails clearly when inputs or limits are invalid.",
        "Use the verified model during design freeze and testing.",
        "software",
    ),
    Phase(
        "D05",
        "step-05-freeze-print-designs",
        "Freeze and print three designs",
        "Weeks 8–11",
        "weeks-8-11-freeze-and-print-designs",
        "#18a98f",
        "Create a fair three-design comparison with common terminals, traceable samples and an approved seed route.",
        ("coupon-derived print rules", "electrical predictions", "common 100 mm × 30 mm envelope"),
        ("Computer-Aided Design software", "Artist-D IDEX or approved printer", "calliper, scale and camera"),
        ("qualify both nozzles on coupons", "do not change frozen geometry silently", "inspect sharp or failed prints before use"),
        (
            ("Design A", "Straight reference path with constant width."),
            ("Design B", "Material-saving path with shaped width or branch."),
            ("Design C", "Repair-ready path with access and sense pads."),
            ("Freeze", "Review terminals, seed route, plating access and repair mask."),
            ("Print and label", "Make A01–A03, B01–B03 and C01–C03."),
        ),
        ("three frozen design files", "nine labelled bases", "dimension and mass record", "failed-print and change log"),
        "G3 / G4 preparation",
        "Designs share test interfaces; the chosen print and seed route passes coupons; every physical sample is traceable.",
        "Release identified samples to supervised seeding and plating.",
        "designs",
    ),
    Phase(
        "D06",
        "step-06-seed-plate",
        "Apply conductive seed and copper",
        "Weeks 11–14",
        "weeks-11-14-seed-and-plate",
        "#f28d3c",
        "Use an approved seed and coupon-first laboratory process to make traceable copper-coated conductors.",
        ("clean labelled bases and coupons", "approved printed or applied seed", "approved copper-plating process"),
        ("masks and hanging fixtures", "resistance and voltage-drop check", "scale, camera and process traveller"),
        ("laboratory owns chemistry and waste", "approved Personal Protective Equipment", "no student bath changes or unsupervised plating"),
        (
            ("Clean and mask", "Expose only the intended conductive route."),
            ("Apply seed", "Print or apply one continuous conductive route."),
            ("Check coupons", "Verify isolation, resistance, voltage drop and plating access."),
            ("Plate copper", "Laboratory controls current, time, flow and chemistry."),
            ("Rinse and inspect", "Record mass, appearance, defects and continuity."),
        ),
        ("completed process travellers", "seed resistance and voltage-drop record", "before/after mass and photographs", "defect and continuity map"),
        "G4",
        "Coupon plating covers the full intended route before samples proceed; all samples retain identities, records and visible defects.",
        "Release plated samples only after laboratory and traceability review.",
        "plating",
    ),
    Phase(
        "D07",
        "step-07-test-samples",
        "Test all nine samples",
        "Weeks 15–18",
        "weeks-15-18-test",
        "#55bd70",
        "Measure every design at the same low-voltage conditions so electrical, thermal and manufacturing differences are comparable.",
        ("nine plated samples", "verified fixture and loggers", "randomized sample order"),
        ("four-wire sample connection", "four temperature channels", "raw-data and observation forms"),
        ("stop above 2 A or at 50 °C", "stop on invalid sensor or loose connection", "stop for smoke, smell or unexpected heating"),
        (
            ("Inspect", "Check identity, surface, terminals and room temperature."),
            ("Connect", "Use repeatable clamps and separate sense leads."),
            ("Run levels", "Test approximately 0.5 A, 1.0 A and 1.8 A."),
            ("Repeat", "Retest enough to estimate measurement variation."),
            ("Compare", "Analyse resistance, temperature, yield and model error."),
        ),
        ("raw time-series tables", "resistance and temperature plots", "uncertainty note", "three-design comparison and yield"),
        "G5",
        "All samples, including failures, are represented and repeated results are stable enough for an honest comparison.",
        "Select one repair-ready sample for controlled damage.",
        "testing",
    ),
    Phase(
        "D08",
        "step-08-damage-repair",
        "Damage, repair and retest",
        "Weeks 19–21",
        "weeks-19-21-damage-and-repair",
        "#e6538d",
        "Create a controlled local defect, restore copper under supervision and measure whether useful performance returns.",
        ("tested repair-ready sample", "approved damage location", "repair mask and laboratory access"),
        ("controlled abrasion or cut fixture", "inspection camera", "same electrical and temperature test system"),
        ("contain sharp edges and particles", "record damage before repair", "repair plating remains laboratory controlled"),
        (
            ("Original", "Save baseline resistance, temperature and photographs."),
            ("Damage", "Remove copper only in the approved local zone."),
            ("Measure", "Quantify the defect before changing it again."),
            ("Repair", "Clean, mask and locally restore copper."),
            ("Retest", "Repeat the original current and temperature sequence."),
        ),
        ("original/damaged/repaired dataset", "matched photographs", "repair time and material cost", "electrical and thermal recovery result"),
        "G6",
        "Repair is evaluated against declared electrical and thermal criteria; an unsuccessful repair is reported rather than hidden.",
        "Send the complete evidence package to business comparison and reporting.",
        "repair",
    ),
    Phase(
        "D09",
        "step-09-explain-present",
        "Explain, present and decide",
        "Weeks 22–24",
        "weeks-22-24-explain-and-present",
        "#6f4cb8",
        "Turn calculations, physical evidence, costs and limitations into a decision another person can understand and reproduce.",
        ("source code and calculations", "manufacturing and test evidence", "Bill of Materials and actual costs"),
        ("report and chart templates", "demonstration poster or video", "lecturer and non-technical review"),
        ("separate facts from interpretation", "do not hide failures or uncertainty", "do not claim industrial or commercial proof"),
        (
            ("Validate", "Check identifiers, files, units, totals and missing data."),
            ("Compare value", "Calculate cost per success, repair and replacement."),
            ("Explain limits", "State uncertainty and what the project does not prove."),
            ("Review", "Use lecturer and non-technical translation checks."),
            ("Recommend", "Choose stop, repeat or one specific expansion."),
        ),
        ("first-year engineering report", "one-page business summary", "reproducible data and code package", "final presentation and decision"),
        "G7",
        "An independent reader can trace the evidence, reproduce the calculations and understand the recommended next decision.",
        "Archive the project passport and approved next-step recommendation.",
        "present",
    ),
)


def escape(value: str) -> str:
    return html.escape(value, quote=True)


def wrap_lines(value: str, width: int) -> list[str]:
    return textwrap.wrap(value, width=width, break_long_words=False, break_on_hyphens=False) or [""]


def text_block(x: float, y: float, value: str, width: int, css_class: str, line_height: int = 18, anchor: str = "start") -> str:
    lines = wrap_lines(value, width)
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if index == 0 else line_height}">{escape(line)}</tspan>'
        for index, line in enumerate(lines)
    )
    return f'<text class="{css_class}" x="{x}" y="{y}" text-anchor="{anchor}">{spans}</text>'


def bullet_list(x: float, y: float, values: tuple[str, ...], width: int, css_class: str = "body", line_height: int = 17) -> str:
    parts: list[str] = []
    cursor = y
    for value in values:
        lines = wrap_lines(value, width)
        parts.append(f'<circle cx="{x}" cy="{cursor - 5}" r="3.5" fill="currentColor"/>')
        parts.append(text_block(x + 12, cursor, value, width, css_class, line_height))
        cursor += line_height * len(lines) + 8
    return "".join(parts)


def card(x: int, y: int, width: int, height: int, title: str, body: tuple[str, ...], accent: str, kind: str = "normal") -> str:
    fill = "#ffffff" if kind == "normal" else "#fff8ef" if kind == "safety" else "#edf8f6"
    stroke = accent if kind != "safety" else "#dd6b35"
    return (
        f'<g transform="translate({x},{y})"><rect width="{width}" height="{height}" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
        f'<text class="section" x="18" y="28">{escape(title)}</text>{bullet_list(20, 56, body, max(18, width // 9))}</g>'
    )


def mini_box(x: int, y: int, width: int, height: int, title: str, subtitle: str, accent: str, fill: str = "#ffffff") -> str:
    return (
        f'<g transform="translate({x},{y})"><rect width="{width}" height="{height}" rx="13" fill="{fill}" stroke="{accent}" stroke-width="1.4"/>'
        f'{text_block(width / 2, 27, title, max(10, width // 10), "miniTitle", 15, "middle")}'
        f'{text_block(width / 2, 52, subtitle, max(12, width // 8), "miniBody", 14, "middle")}</g>'
    )


def arrow(x1: int, y1: int, x2: int, y2: int, css_class: str = "arrow") -> str:
    return f'<path class="{css_class}" d="M{x1} {y1}L{x2} {y2}"/>'


def action_flow(phase: Phase) -> str:
    parts = ['<text class="detailHeading" x="302" y="190">Student action flow</text>']
    x_positions = (300, 470, 640, 810, 980)
    for index, ((title, detail), x) in enumerate(zip(phase.actions, x_positions, strict=True), 1):
        parts.append(f'<g transform="translate({x},210)"><rect width="150" height="125" rx="15" fill="#ffffff" stroke="{phase.accent}" stroke-width="1.4"/>')
        parts.append(f'<circle cx="22" cy="22" r="14" fill="{phase.accent}"/><text class="stepNumber" x="22" y="27" text-anchor="middle">{index}</text>')
        parts.append(text_block(75, 51, title, 17, "actionTitle", 15, "middle"))
        parts.append(text_block(75, 79, detail, 22, "actionBody", 14, "middle"))
        parts.append("</g>")
        if index < len(x_positions):
            parts.append(arrow(x + 151, 272, x + 168, 272))
    return "".join(parts)


def detail_approval(accent: str) -> str:
    parts = [mini_box(320, 420, 175, 82, "Mission", "one paragraph anyone can explain", accent)]
    parts += [arrow(495, 461, 530, 461), mini_box(530, 420, 175, 82, "Team roles", "named owners and responsibilities", accent)]
    parts += [arrow(705, 461, 740, 461), mini_box(740, 420, 175, 82, "Risk controls", "hazard, consequence and control", accent)]
    parts += [arrow(915, 461, 950, 461), mini_box(950, 420, 175, 82, "Gate G0", "lecturer and laboratory approval", accent, "#edf8f6")]
    for index, label in enumerate(("5 volts", "2 amperes", "50 °C stop", "24 weeks")):
        x = 365 + index * 190
        parts.append(f'<g transform="translate({x},540)"><rect width="150" height="42" rx="21" fill="{accent}" opacity="0.12"/><text class="badgeText" x="75" y="27" text-anchor="middle">{escape(label)}</text></g>')
    return "".join(parts)


def detail_calculate(accent: str) -> str:
    parts: list[str] = [
        f'<g transform="translate(330,405)"><rect width="220" height="82" rx="13" fill="#fff" stroke="{accent}" stroke-width="1.4"/><text class="miniTitle" x="110" y="27" text-anchor="middle">Copper area</text><text class="miniBody" x="110" y="56" text-anchor="middle"><tspan>A</tspan><tspan baseline-shift="sub" font-size="8">Cu</tspan><tspan> = w</tspan><tspan baseline-shift="sub" font-size="8">Cu</tspan><tspan> × t</tspan><tspan baseline-shift="sub" font-size="8">Cu</tspan></text></g>',
        f'<g transform="translate(590,405)"><rect width="220" height="82" rx="13" fill="#fff" stroke="{accent}" stroke-width="1.4"/><text class="miniTitle" x="110" y="27" text-anchor="middle">Resistance</text><text class="miniBody" x="110" y="56" text-anchor="middle"><tspan>R = ρL / A</tspan><tspan baseline-shift="sub" font-size="8">Cu</tspan></text></g>',
        f'<g transform="translate(850,405)"><rect width="220" height="82" rx="13" fill="#fff" stroke="{accent}" stroke-width="1.4"/><text class="miniTitle" x="110" y="27" text-anchor="middle">Heating</text><text class="miniBody" x="110" y="56" text-anchor="middle"><tspan>P = I</tspan><tspan baseline-shift="super" font-size="8">2</tspan><tspan>R</tspan></text></g>',
    ]
    loop = (("CAD", "draw"), ("Print", "coupon"), ("Measure", "dimensions"), ("Update", "design rules"))
    for index, (title, subtitle) in enumerate(loop):
        x = 335 + index * 205
        parts.append(mini_box(x, 530, 165, 70, title, subtitle, accent, "#f5f9fd"))
        if index < 3:
            parts.append(arrow(x + 165, 565, x + 198, 565))
    parts.append('<path class="returnArrow" d="M1115 600C1115 630 330 630 330 600"/>')
    return "".join(parts)


def detail_logger(accent: str) -> str:
    parts = ['<text class="miniLabel" x="320" y="415">POWER PATH</text>']
    chain = (("5 V supply", 130), ("Fuse + switch", 145), ("Sample", 130), ("Load", 115), ("Shunt", 115))
    x = 320
    centres: list[int] = []
    for index, (title, width) in enumerate(chain):
        parts.append(mini_box(x, 430, width, 62, title, "current path", accent))
        centres.append(x + width // 2)
        if index < len(chain) - 1:
            parts.append(arrow(x + width, 461, x + width + 24, 461))
        x += width + 25
    parts.append(mini_box(430, 545, 155, 62, "Voltage converter", "sample + shunt sensing", accent, "#f4f0ff"))
    parts.append(mini_box(625, 545, 145, 62, "Microcontroller", "timestamp and limits", accent, "#f4f0ff"))
    parts.append(mini_box(810, 545, 125, 62, "CSV data", "raw readings", accent, "#edf8f6"))
    parts.append(mini_box(965, 525, 150, 82, "4 temperature sensors", "ambient + three sample points", accent, "#fff8ef"))
    parts += [arrow(585, 576, 625, 576), arrow(770, 576, 810, 576), arrow(935, 576, 965, 566)]
    parts.append('<path class="signal" d="M645 492V530H510V545"/><path class="signal" d="M955 492V515H510V545"/>')
    return "".join(parts)


def detail_software(accent: str) -> str:
    parts: list[str] = []
    for index, (title, subtitle) in enumerate((("Mission limits", "5 V · 2 A · 50 °C"), ("Geometry", "length · width · thickness"), ("Raw CSV", "logger measurements"))):
        parts.append(mini_box(320, 405 + index * 72, 165, 58, title, subtitle, accent, "#f5f9fd"))
    modules = (("geometry.py", "dimensions"), ("electrical.py", "R and P"), ("thermal.py", "ΔT estimate"), ("analysis.py", "compare"), ("reporting.py", "table + figure"))
    for index, (title, subtitle) in enumerate(modules):
        x = 520 + index * 122
        parts.append(mini_box(x, 440, 108, 76, title, subtitle, accent))
        if index < len(modules) - 1:
            parts.append(arrow(x + 108, 478, x + 119, 478))
    parts.append('<path class="signal" d="M485 434H520M485 506H520M485 578H500V500H520"/>')
    parts.append(mini_box(600, 555, 260, 62, "Automated tests", "hand examples · units · limits · invalid data", accent, "#edf8f6"))
    parts.append('<path class="returnArrow" d="M730 555V532C730 525 680 525 680 516"/>')
    return "".join(parts)


def detail_designs(accent: str) -> str:
    parts: list[str] = []
    panels = ((330, "Design A", "straight reference"), (610, "Design B", "material-saving"), (890, "Design C", "repair-ready"))
    for x, title, subtitle in panels:
        parts.append(f'<g transform="translate({x},402)"><rect width="230" height="200" rx="16" fill="#fff" stroke="{accent}" stroke-width="1.4"/><text class="miniTitle" x="115" y="28" text-anchor="middle">{title}</text><text class="miniBody" x="115" y="49" text-anchor="middle">{subtitle}</text>')
        parts.append('<rect x="22" y="82" width="25" height="54" rx="5" fill="#d6e2ea"/><rect x="183" y="82" width="25" height="54" rx="5" fill="#d6e2ea"/>')
        if title == "Design A":
            parts.append(f'<rect x="42" y="96" width="146" height="26" rx="8" fill="{accent}"/>')
        elif title == "Design B":
            parts.append(f'<path d="M42 95H88L112 82H142L166 95H188V123H166L142 136H112L88 123H42Z" fill="{accent}"/>')
        else:
            parts.append(f'<rect x="42" y="96" width="146" height="26" rx="8" fill="{accent}"/><rect x="101" y="91" width="30" height="36" rx="5" fill="#fff" stroke="#e6538d" stroke-width="4"/><circle cx="71" cy="109" r="5" fill="#17364a"/><circle cx="160" cy="109" r="5" fill="#17364a"/>')
        ids = "A01 · A02 · A03" if title == "Design A" else "B01 · B02 · B03" if title == "Design B" else "C01 · C02 · C03"
        parts.append(f'<text class="badgeText" x="115" y="176" text-anchor="middle">{ids}</text></g>')
    parts.append(f'<g transform="translate(410,612)"><rect width="630" height="24" rx="12" fill="{accent}" opacity=".14"/><text class="badgeText" x="315" y="17" text-anchor="middle">Artist-D option: left PLA body · right conductive seed · coupons before nine samples</text></g>')
    return "".join(parts)


def detail_plating(accent: str) -> str:
    parts = ['<g transform="translate(320,405)"><rect width="210" height="200" rx="16" fill="#fff" stroke="#ccdbe6"/><text class="miniTitle" x="105" y="28" text-anchor="middle">Coating cross-section</text><rect x="34" y="132" width="142" height="38" rx="7" fill="#d6e2ea"/><rect x="34" y="116" width="142" height="12" rx="4" fill="#34495e"/><rect x="34" y="82" width="142" height="30" rx="6" fill="#d98632"/><text class="miniBody" x="105" y="101" text-anchor="middle" fill="#fff">copper</text><text class="miniBody" x="105" y="126" text-anchor="middle" fill="#fff">printed or applied seed</text><text class="miniBody" x="105" y="154" text-anchor="middle">printed polymer</text></g>']
    process = (("Clean + mask", "route exposed"), ("Seed", "continuous route"), ("Coupon gate", "R + drop + coverage"), ("Copper plate", "lab controlled"), ("Inspect", "mass + defects"))
    for index, (title, subtitle) in enumerate(process):
        x = 565 + (index % 3) * 185
        y = 410 if index < 3 else 520
        if index >= 3:
            x = 660 + (index - 3) * 220
        parts.append(mini_box(x, y, 160, 72, title, subtitle, accent, "#fff8ef" if title == "Copper plate" else "#ffffff"))
        if index in (0, 1):
            parts.append(arrow(x + 160, y + 36, x + 180, y + 36))
    parts.append('<path class="arrow" d="M1035 446V505H820V520"/><path class="arrow" d="M820 556H870"/>')
    return "".join(parts)


def detail_testing(accent: str) -> str:
    parts = ['<text class="miniLabel" x="320" y="413">REPEATABLE TEST PATH</text>']
    process = (("Randomized ID", 145), ("Inspect", 105), ("4-wire connect", 145), ("Run current", 130), ("Save raw data", 145))
    x = 320
    for index, (title, width) in enumerate(process):
        parts.append(mini_box(x, 430, width, 66, title, "same method", accent))
        if index < len(process) - 1:
            parts.append(arrow(x + width, 463, x + width + 18, 463))
        x += width + 20
    for index, label in enumerate(("≈ 0.5 A", "≈ 1.0 A", "≈ 1.8 A")):
        parts.append(f'<g transform="translate({490 + index * 150},535)"><rect width="125" height="44" rx="22" fill="{accent}" opacity="0.16"/><text class="badgeText" x="62" y="28" text-anchor="middle">{label}</text></g>')
    parts.append(mini_box(955, 525, 165, 70, "STOP", ">2 A · ≥50 °C · invalid sensor", "#d84d4d", "#fff1f1"))
    parts.append('<path class="signal" d="M875 496V550H955"/>')
    return "".join(parts)


def detail_repair(accent: str) -> str:
    parts: list[str] = []
    states = ((330, "Original", "baseline"), (610, "Damaged", "local copper loss"), (890, "Repaired", "local copper restored"))
    for index, (x, title, subtitle) in enumerate(states):
        parts.append(f'<g transform="translate({x},402)"><rect width="230" height="200" rx="16" fill="#fff" stroke="{accent}" stroke-width="1.4"/><text class="miniTitle" x="115" y="30" text-anchor="middle">{title}</text><text class="miniBody" x="115" y="52" text-anchor="middle">{subtitle}</text><rect x="25" y="95" width="180" height="28" rx="10" fill="#d98632"/>')
        if index == 1:
            parts.append('<rect x="98" y="87" width="34" height="44" fill="#fff"/><path d="M98 87L132 131M132 87L98 131" stroke="#d84d4d" stroke-width="4"/>')
        if index == 2:
            parts.append('<rect x="96" y="89" width="38" height="40" rx="6" fill="#f0a45a" stroke="#e6538d" stroke-width="3"/>')
        parts.append('<text class="badgeText" x="115" y="166" text-anchor="middle">same test sequence</text></g>')
        if index < 2:
            parts.append(arrow(x + 230, 502, x + 270, 502))
    parts.append('<text class="miniLabel" x="600" y="630" text-anchor="middle">COMPARE RESISTANCE · TEMPERATURE · TIME · MATERIAL · COST</text>')
    return "".join(parts)


def detail_present(accent: str) -> str:
    parts: list[str] = []
    evidence = (("Calculations", "prediction"), ("Samples", "physical evidence"), ("Data", "measurement"), ("Costs", "business evidence"))
    for index, (title, subtitle) in enumerate(evidence):
        parts.append(mini_box(320, 395 + index * 56, 150, 46, title, subtitle, accent, "#f5f9fd"))
    parts.append(mini_box(555, 440, 220, 120, "Evidence package", "report · code · raw data · charts · limits", accent, "#ffffff"))
    for index in range(4):
        parts.append(f'<path class="signal" d="M470 {418 + index * 56}H520V500H555"/>')
    decisions = (("STOP", "evidence rejects the idea", "#d84d4d"), ("REPEAT", "correct one known weakness", "#e18a2d"), ("EXPAND", "test one larger question", "#42a963"))
    for index, (title, subtitle, color) in enumerate(decisions):
        parts.append(mini_box(850, 395 + index * 75, 250, 60, title, subtitle, color, "#ffffff"))
        parts.append(arrow(775, 500, 835, 425 + index * 75, "decisionArrow"))
    return "".join(parts)


DETAIL_RENDERERS = {
    "approval": detail_approval,
    "calculate": detail_calculate,
    "logger": detail_logger,
    "software": detail_software,
    "designs": detail_designs,
    "plating": detail_plating,
    "testing": detail_testing,
    "repair": detail_repair,
    "present": detail_present,
}


def phase_svg(phase: Phase) -> str:
    description = (
        f"{phase.title}, {phase.weeks}. The diagram shows required inputs, tools, safety controls, "
        f"five student actions, phase-specific system detail, evidence, {phase.gate_code}, and the handoff."
    )
    action_markup = action_flow(phase)
    detail_markup = DETAIL_RENDERERS[phase.detail_kind](phase.accent)
    if len(phase.gate_code) > 8:
        gate_badge = text_block(1054, 85, phase.gate_code, 12, "gateValueLong", 16, "middle")
    else:
        gate_badge = f'<text class="gateValue" x="1054" y="101" text-anchor="middle">{escape(phase.gate_code)}</text>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="920" viewBox="0 0 1200 920" role="img" aria-labelledby="title desc">
  <title id="title">{escape(phase.diagram_id)} — {escape(phase.title)}</title>
  <desc id="desc">{escape(description)}</desc>
  <defs>
    <linearGradient id="header" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{phase.accent}"/><stop offset="1" stop-color="#304e83"/></linearGradient>
    <filter id="shadow" x="-20%" y="-30%" width="140%" height="170%"><feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="#17364a" flood-opacity="0.13"/></filter>
    <marker id="arrowhead" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0 0L0 8L9 4Z" fill="#54728a"/></marker>
    <style>
      .ui{{font-family:Inter,Segoe UI,Arial,sans-serif}}.title{{font:800 31px Inter,Segoe UI,Arial,sans-serif;fill:#fff}}.subtitle{{font:500 15px Inter,Segoe UI,Arial,sans-serif;fill:#e9f3ff}}.gateValue{{font:800 28px Inter,Segoe UI,Arial,sans-serif;fill:#fff}}.gateValueLong{{font:800 15px Inter,Segoe UI,Arial,sans-serif;fill:#fff}}.section{{font:800 14px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.08em;fill:#214158}}.body{{font:500 13px Inter,Segoe UI,Arial,sans-serif;fill:#48657a}}.detailHeading{{font:800 17px Inter,Segoe UI,Arial,sans-serif;fill:#18384d}}.stepNumber{{font:800 13px Inter,Segoe UI,Arial,sans-serif;fill:#fff}}.actionTitle{{font:800 13px Inter,Segoe UI,Arial,sans-serif;fill:#17384d}}.actionBody{{font:500 10.5px Inter,Segoe UI,Arial,sans-serif;fill:#5a7487}}.miniTitle{{font:800 13px Inter,Segoe UI,Arial,sans-serif;fill:#18384d}}.miniBody{{font:500 10.5px Inter,Segoe UI,Arial,sans-serif;fill:#5a7487}}.miniLabel{{font:800 11px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.08em;fill:#567388}}.badgeText{{font:750 12px Inter,Segoe UI,Arial,sans-serif;fill:#26485d}}.gateTitle{{font:850 18px Inter,Segoe UI,Arial,sans-serif;fill:#fff}}.gateBody{{font:550 12px Inter,Segoe UI,Arial,sans-serif;fill:#eaf4ff}}.handoff{{font:750 13px Inter,Segoe UI,Arial,sans-serif;fill:#24475d}}.arrow{{stroke:#54728a;stroke-width:2;fill:none;marker-end:url(#arrowhead)}}.returnArrow{{stroke:#6a8090;stroke-width:1.8;fill:none;stroke-dasharray:6 5;marker-end:url(#arrowhead)}}.signal{{stroke:#7659d7;stroke-width:1.8;fill:none;stroke-dasharray:4 4;marker-end:url(#arrowhead)}}.decisionArrow{{stroke:#6f4cb8;stroke-width:1.8;fill:none;marker-end:url(#arrowhead)}}
    </style>
  </defs>
  <rect width="1200" height="920" rx="28" fill="#edf3f8"/>
  <rect x="28" y="28" width="1144" height="112" rx="22" fill="url(#header)"/>
  <g class="ui"><rect x="54" y="52" width="78" height="56" rx="15" fill="#fff" opacity=".18"/><text class="title" x="93" y="90" text-anchor="middle" font-size="23">{escape(phase.diagram_id)}</text>
  <text class="title" x="155" y="76">{escape(phase.title)}</text><text class="subtitle" x="155" y="106">{escape(phase.weeks)} · Adaptive Electroformed 3D Power Topology Lite student project</text>
  <rect x="968" y="52" width="172" height="56" rx="14" fill="#153758" opacity=".86"/><text class="subtitle" x="1054" y="72" text-anchor="middle">Phase gate</text>{gate_badge}</g>
  <g class="ui" transform="translate(28,156)"><rect width="1144" height="64" rx="16" fill="#fff" stroke="#cbdce8"/>{text_block(26, 27, "WHY THIS PHASE EXISTS", 28, "section")}{text_block(26, 50, phase.purpose, 125, "body", 17)}</g>
  <g class="ui">{card(28, 238, 240, 158, "INPUTS", phase.inputs, phase.accent)}{card(28, 410, 240, 144, "TOOLS AND MATERIALS", phase.tools, phase.accent)}{card(28, 568, 240, 176, "SAFETY / STOP", phase.safety, phase.accent, "safety")}</g>
  <g class="ui">{action_markup}<rect x="288" y="362" width="884" height="280" rx="20" fill="#f8fbfd" stroke="#cbdce8"/>{detail_markup}</g>
  <g class="ui" transform="translate(288,660)"><rect width="430" height="154" rx="18" fill="#fff" stroke="{phase.accent}" stroke-width="1.5"/><text class="section" x="20" y="29">EVIDENCE PRODUCED</text>{bullet_list(22, 58, phase.evidence, 45)}</g>
  <g class="ui" transform="translate(736,660)"><rect width="436" height="154" rx="18" fill="#294d75"/><text class="gateTitle" x="22" y="34">PASS / FAIL — {escape(phase.gate_code)}</text>{text_block(22, 62, phase.gate_text, 55, "gateBody", 18)}</g>
  <g class="ui" transform="translate(288,832)"><rect width="884" height="60" rx="16" fill="#edf8f6" stroke="{phase.accent}"/><text class="section" x="20" y="25">HANDOFF TO THE NEXT PHASE</text>{text_block(260, 36, phase.handoff, 85, "handoff", 17)}</g>
</svg>
'''


def coverage_map_svg() -> str:
    cards: list[str] = []
    for index, phase in enumerate(PHASES):
        row, column = divmod(index, 3)
        x = 48 + column * 448
        y = 180 + row * 218
        gate_label = "Prep gate" if phase.gate_code == "Preparation gate" else "G3/G4 prep" if phase.gate_code == "G3 / G4 preparation" else phase.gate_code
        cards.append(
            f'<g class="ui" transform="translate({x},{y})"><rect width="400" height="178" rx="19" fill="#fff" stroke="{phase.accent}" stroke-width="2" filter="url(#shadow)"/>'
            f'<rect width="82" height="178" rx="19" fill="{phase.accent}"/><text class="code" x="41" y="73" text-anchor="middle">{phase.diagram_id}</text><text class="week" x="41" y="102" text-anchor="middle">{escape(phase.weeks)}</text>'
            f'{text_block(105, 37, phase.title, 26, "cardTitle", 20)}{text_block(105, 86, phase.purpose, 49, "cardBody", 16)}'
            f'<rect x="104" y="132" width="104" height="28" rx="14" fill="{phase.accent}" opacity=".14"/><text class="gate" x="156" y="151" text-anchor="middle">{escape(gate_label)}</text>'
            f'<text class="coverage" x="224" y="150">inputs · actions · safety · evidence</text></g>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="940" viewBox="0 0 1400 940" role="img" aria-labelledby="title desc">
  <title id="title">AE3PT-Lite complete project-step diagram coverage map</title>
  <desc id="desc">Nine linked teaching phases from scope approval to final decision. Every phase diagram covers inputs, actions, tools, safety controls, evidence, a pass or fail gate, and a handoff.</desc>
  <defs><linearGradient id="header" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#147c88"/><stop offset=".55" stop-color="#346bb9"/><stop offset="1" stop-color="#704ab5"/></linearGradient><filter id="shadow" x="-20%" y="-30%" width="140%" height="170%"><feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="#17364a" flood-opacity=".12"/></filter><style>.ui{{font-family:Inter,Segoe UI,Arial,sans-serif}}.title{{font:800 34px Inter,Segoe UI,Arial,sans-serif;fill:#fff}}.subtitle{{font:500 16px Inter,Segoe UI,Arial,sans-serif;fill:#e6f2ff}}.code{{font:850 26px Inter,Segoe UI,Arial,sans-serif;fill:#fff}}.week{{font:650 11px Inter,Segoe UI,Arial,sans-serif;fill:#eef7ff}}.cardTitle{{font:800 18px Inter,Segoe UI,Arial,sans-serif;fill:#18384d}}.cardBody{{font:500 11px Inter,Segoe UI,Arial,sans-serif;fill:#587286}}.gate{{font:800 11px Inter,Segoe UI,Arial,sans-serif;fill:#23465d}}.coverage{{font:650 10px Inter,Segoe UI,Arial,sans-serif;fill:#6b8292}}.legendTitle{{font:800 14px Inter,Segoe UI,Arial,sans-serif;fill:#214158}}.legend{{font:500 12px Inter,Segoe UI,Arial,sans-serif;fill:#587286}}</style></defs>
  <rect width="1400" height="940" rx="28" fill="#edf3f8"/><rect x="28" y="28" width="1344" height="116" rx="22" fill="url(#header)"/>
  <g class="ui"><text class="title" x="62" y="76">Complete project-step diagram coverage</text><text class="subtitle" x="62" y="108">Adaptive Electroformed 3D Power Topology Lite · nine phases · 24 weeks · Gate G0 to Gate G7</text><rect x="1140" y="52" width="196" height="66" rx="15" fill="#18395d" opacity=".88"/><text class="subtitle" x="1238" y="78" text-anchor="middle">Coverage requirement</text><text class="title" x="1238" y="104" text-anchor="middle" font-size="19">9 of 9 phases</text></g>
  {''.join(cards)}
  <g class="ui" transform="translate(48,852)"><rect width="1304" height="60" rx="17" fill="#fff" stroke="#c9d9e5"/><text class="legendTitle" x="22" y="26">EVERY PHASE SVG MUST SHOW</text><text class="legend" x="250" y="27">purpose · inputs · tools/materials · five actions · phase-specific system detail · safety/stop controls · evidence · pass/fail gate · handoff</text><text class="legend" x="22" y="48">Select any embedded diagram in the student guide to open its full-size SVG.</text></g>
</svg>
'''


def artist_d_workflow_svg() -> str:
    """Return the machine-specific optional IDEX printing and plating workflow."""

    machine_points = (
        "Independent Dual Extruder: two direct-drive toolheads",
        "300 × 300 × 340 mm nominal build volume",
        "1.75 mm filament and 0.4 mm standard nozzles",
        "substantially preassembled; final setup and calibration remain",
    )
    warnings = (
        "conductive filament is the plating seed, not the final power path",
        "generic conductive PLA may be too resistive for a long seed route",
        "voltage drop and current crowding can starve the far end of copper",
        "a continuity beep does not prove acceptable plating distribution",
        "a failed seed coupon returns to surface-applied seed",
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="980" viewBox="0 0 1400 980" role="img" aria-labelledby="title desc">
  <title id="title">JG MAKER Artist-D dual-material printing and copper-electroplating workflow</title>
  <desc id="desc">An educational workflow showing the difficulty four out of five Artist-D independent dual extruder route, a non-conductive PLA body, a high-resistance conductive PLA seed track, voltage-drop and current-crowding checks, supervised copper plating, and the fallback to a surface-applied seed.</desc>
  <defs>
    <linearGradient id="header" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#126d78"/><stop offset=".55" stop-color="#386fb5"/><stop offset="1" stop-color="#6c4db1"/></linearGradient>
    <marker id="arrowhead" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0L10 4L0 8Z" fill="#58768d"/></marker>
    <filter id="shadow" x="-20%" y="-30%" width="140%" height="170%"><feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="#17364a" flood-opacity=".12"/></filter>
    <style>.ui{{font-family:Inter,Segoe UI,Arial,sans-serif}}.title{{font:800 34px Inter,Segoe UI,Arial,sans-serif;fill:#fff}}.subtitle{{font:500 16px Inter,Segoe UI,Arial,sans-serif;fill:#e8f4ff}}.statusLabel{{font:500 13px Inter,Segoe UI,Arial,sans-serif;fill:#e8f4ff}}.statusValue{{font:800 18px Inter,Segoe UI,Arial,sans-serif;fill:#fff}}.section{{font:800 16px Inter,Segoe UI,Arial,sans-serif;fill:#1f435b;letter-spacing:.02em}}.body{{font:500 12px Inter,Segoe UI,Arial,sans-serif;fill:#526f82}}.small{{font:500 11px Inter,Segoe UI,Arial,sans-serif;fill:#5a7487}}.label{{font:800 12px Inter,Segoe UI,Arial,sans-serif;fill:#24475d;letter-spacing:.05em}}.gateTitle{{font:850 18px Inter,Segoe UI,Arial,sans-serif;fill:#fff}}.resultTitle{{font:850 18px Inter,Segoe UI,Arial,sans-serif;fill:#1f435b}}.gateBody{{font:550 12px Inter,Segoe UI,Arial,sans-serif;fill:#eaf4ff}}.badge{{font:800 12px Inter,Segoe UI,Arial,sans-serif;fill:#24475d}}.arrow{{stroke:#58768d;stroke-width:2.2;fill:none;marker-end:url(#arrowhead)}}.dash{{stroke:#58768d;stroke-width:2;fill:none;stroke-dasharray:7 6;marker-end:url(#arrowhead)}}</style>
  </defs>
  <rect width="1400" height="980" rx="28" fill="#edf3f8"/>
  <rect x="28" y="28" width="1344" height="116" rx="22" fill="url(#header)"/>
  <g class="ui"><text class="title" x="62" y="76">Artist-D IDEX selective-plating option</text><text class="subtitle" x="62" y="108">Non-conductive printed body + conductive printed seed + laboratory-controlled copper electroplating</text><rect x="900" y="52" width="188" height="66" rx="15" fill="#214f79" opacity=".92"/><text class="statusLabel" x="994" y="77" text-anchor="middle">Overall difficulty</text><text class="statusValue" x="994" y="103" text-anchor="middle">4 / 5</text><rect x="1104" y="52" width="232" height="66" rx="15" fill="#18395d" opacity=".88"/><text class="statusLabel" x="1220" y="77" text-anchor="middle">Project status</text><text class="statusValue" x="1220" y="103" text-anchor="middle">OPTIONAL ROUTE</text></g>

  <g class="ui" transform="translate(40,174)"><rect width="370" height="316" rx="20" fill="#fff" stroke="#2f78db" stroke-width="1.7" filter="url(#shadow)"/><text class="section" x="22" y="32">1 · PRINTER ROLE</text><rect x="24" y="54" width="322" height="90" rx="14" fill="#edf5ff" stroke="#80aee8"/><path d="M86 72H284L314 112V130H56V112Z" fill="#d7e8fa" stroke="#2f78db"/><rect x="120" y="84" width="34" height="42" rx="6" fill="#f3a14a"/><rect x="218" y="84" width="34" height="42" rx="6" fill="#18a79e"/><text class="badge" x="137" y="107" text-anchor="middle">L</text><text class="badge" x="235" y="107" text-anchor="middle">R</text><text class="small" x="185" y="161" text-anchor="middle">two parked, independently moving direct-drive heads</text>{bullet_list(26, 182, machine_points, 40, "body", 16)}</g>

  <g class="ui" transform="translate(436,174)"><rect width="426" height="316" rx="20" fill="#fff" stroke="#18a79e" stroke-width="1.7" filter="url(#shadow)"/><text class="section" x="22" y="32">2 · MATERIAL ASSIGNMENT</text><g transform="translate(22,56)"><rect width="182" height="112" rx="15" fill="#fff7ec" stroke="#e69038"/><text class="label" x="91" y="29" text-anchor="middle">LEFT EXTRUDER</text><text class="section" x="91" y="55" text-anchor="middle">Natural PLA</text><text class="small" x="91" y="78" text-anchor="middle">insulating body</text><text class="small" x="91" y="96" text-anchor="middle">lands · masks · labels</text></g><g transform="translate(222,56)"><rect width="182" height="112" rx="15" fill="#edf8f6" stroke="#18a79e"/><text class="label" x="91" y="29" text-anchor="middle">RIGHT EXTRUDER</text><text class="section" x="91" y="55" text-anchor="middle">Conductive PLA</text><text class="small" x="91" y="78" text-anchor="middle">exposed seed route</text><text class="small" x="91" y="96" text-anchor="middle">large contact pads</text></g><path class="arrow" d="M113 181V211H213"/><path class="arrow" d="M313 181V211H213"/><g transform="translate(85,216)"><rect width="256" height="73" rx="14" fill="#f5f9fd" stroke="#7ca4c4"/><rect x="28" y="39" width="200" height="22" rx="7" fill="#dce7ee"/><rect x="50" y="27" width="156" height="12" rx="5" fill="#34495e"/><text class="small" x="128" y="18" text-anchor="middle">co-printed seed exposed above PLA body</text></g></g>

  <g class="ui" transform="translate(888,174)"><rect width="472" height="316" rx="20" fill="#fff8ef" stroke="#dd6b35" stroke-width="1.7" filter="url(#shadow)"/><text class="section" x="22" y="32">3 · NON-NEGOTIABLE LIMITS</text>{bullet_list(26, 64, warnings, 49, "body", 19)}<g transform="translate(24,240)"><rect width="424" height="52" rx="14" fill="#fff1f1" stroke="#d84d4d"/><text class="label" x="212" y="22" text-anchor="middle">DO NOT SOLVE A FAILED COUPON BY</text><text class="small" x="212" y="41" text-anchor="middle">raising bath voltage, changing chemistry or bypassing laboratory approval</text></g></g>

  <text class="section ui" x="40" y="532">COUPON-FIRST QUALIFICATION — ALL THREE GATES MUST PASS</text>
  <g class="ui" transform="translate(40,554)"><rect width="394" height="154" rx="19" fill="#fff" stroke="#2f78db" stroke-width="1.6"/><circle cx="34" cy="34" r="20" fill="#2f78db"/><text class="gateTitle" x="34" y="41" text-anchor="middle">A</text><text class="section" x="68" y="32">Alignment and isolation</text>{bullet_list(28, 68, ("calibrate XY and Z offset", "no gap along the intended interface", "no conductive bridge across insulation"), 38, "body", 17)}</g>
  <path class="arrow" d="M434 631H468"/>
  <g class="ui" transform="translate(470,554)"><rect width="394" height="154" rx="19" fill="#fff" stroke="#7659d7" stroke-width="1.6"/><circle cx="34" cy="34" r="20" fill="#7659d7"/><text class="gateTitle" x="34" y="41" text-anchor="middle">B</text><text class="section" x="68" y="32">Electrical seed check</text>{bullet_list(28, 68, ("measure numerical seed resistance", "calculate plating voltage drop", "map near, middle and far electrical access"), 38, "body", 17)}</g>
  <path class="arrow" d="M864 631H898"/>
  <g class="ui" transform="translate(900,554)"><rect width="460" height="154" rx="19" fill="#fff" stroke="#f28d3c" stroke-width="1.6"/><circle cx="34" cy="34" r="20" fill="#f28d3c"/><text class="gateTitle" x="34" y="41" text-anchor="middle">C</text><text class="section" x="68" y="32">Supervised plating coupon</text>{bullet_list(28, 68, ("copper starts at every intended region", "coverage reaches the farthest point", "adhesion and isolation remain acceptable"), 45, "body", 17)}</g>

  <g class="ui" transform="translate(40,752)"><rect width="610" height="164" rx="20" fill="#edf8f6" stroke="#31a56c" stroke-width="2"/><text class="resultTitle" x="24" y="38">PASS — RELEASE THE OPTION</text><text class="body" x="24" y="68">Print labelled samples in normal dual-material mode.</text><text class="body" x="24" y="91">Use multiple seed contacts if the approved coupon requires them.</text><text class="body" x="24" y="114">Copper plate under laboratory control, then test at 0.5 A, 1.0 A and 1.8 A.</text><text class="badge" x="24" y="144">Final power performance comes from copper, not from the polymer seed.</text></g>
  <g class="ui" transform="translate(684,752)"><rect width="676" height="164" rx="20" fill="#fff1f1" stroke="#d84d4d" stroke-width="2"/><text class="resultTitle" x="24" y="38">FAIL — RETURN TO A SAFER BASELINE</text><text class="body" x="24" y="68">Use normal PLA or approved PETG with a laboratory-approved surface-applied seed.</text><text class="body" x="24" y="91">Or redesign the seed path: shorter route, wider track, larger pads or approved extra contacts.</text><text class="body" x="24" y="114">Record the failure as evidence; do not print or plate the nine functional samples.</text><text class="badge" x="24" y="144">The IDEX method is optional; the project can succeed without it.</text></g>
  <path class="arrow" d="M1130 708V730H345V752"/><path class="dash" d="M1130 708V730H1022V752"/><text class="small ui" x="965" y="726">any gate fails</text>
  <text class="small ui" x="700" y="956" text-anchor="middle">Teaching boundary: printer work is student-operated after approval; copper chemistry, ventilation, process settings, rinsing and waste remain laboratory-controlled.</text>
</svg>
'''


def manifest_csv() -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(("diagram_id", "project_step", "weeks", "gate", "svg_file", "student_section", "inputs", "actions", "safety", "evidence", "handoff"))
    for phase in PHASES:
        writer.writerow(
            (
                phase.diagram_id,
                phase.title,
                phase.weeks,
                phase.gate_code,
                f"diagrams/{phase.slug}.svg",
                phase.section,
                " | ".join(phase.inputs),
                " | ".join(title for title, _ in phase.actions),
                " | ".join(phase.safety),
                " | ".join(phase.evidence),
                phase.handoff,
            )
        )
    return stream.getvalue()


def expected_outputs(project_root: Path) -> dict[Path, str]:
    docs_root = project_root / "docs"
    outputs = {docs_root / "diagrams" / f"{phase.slug}.svg": phase_svg(phase) for phase in PHASES}
    outputs[docs_root / "diagrams" / "student-project-step-map.svg"] = coverage_map_svg()
    outputs[docs_root / "diagrams" / "artist-d-dual-material-plating-workflow.svg"] = artist_d_workflow_svg()
    outputs[docs_root / "data" / "student-diagram-manifest.csv"] = manifest_csv()
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
        print("diagram generation drift detected:")
        for path in changed:
            print(f"  {path}")
        return 1
    if arguments.check:
        print(f"diagram set is current: {len(outputs) - 1} SVG files and one manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
