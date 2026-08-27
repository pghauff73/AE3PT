# Conductive Coating Methods: Ten Complete Student Plans

**Library purpose:** compare automated ways to make selected regions of a three-dimensional printed polymer conductive before supervised copper electroplating.

![Ten conductive coating methods arranged by cost, difficulty and recommended student path](../diagrams/conductive-coatings/method-selection-map.svg)

## Three-Paragraph Description

This library turns ten conductive-coating suggestions into comparable engineering plans. Every method has the same planning fields: expanded name and acronym, operating principle, equipment, materials, implementation microsteps, pass/fail gates, evidence, safety controls, fallback, difficulty and cost. A student can therefore compare methods by the work and proof they require rather than by promotional claims or a visually impressive machine.

The methods range from a student-built gantry dispenser to research-grade laser, vacuum, aerosol and multi-material resin systems. The project should start at the lowest complexity capable of reaching the required geometry. Advanced processes are included because they may solve fine-feature, conformal or hidden-surface problems, but they should normally be accessed as shared university equipment or contracted services rather than purchased for one undergraduate demonstrator.

Each coating is treated as a seed layer for later copper thickening, not as an assumed final power conductor. The common decision loop is design, deposit, inspect, measure, plate, test and either release or return to a fallback. This keeps conductive coating, electroplating, electrical performance, cost, safety and repair evidence inside one traceable AE3PT student workflow.

## Recommended Low-Budget Sequence

1. If a JG MAKER Artist-D is already available, evaluate the [machine-specific dual-material copper electroplating plan](../artist-d-electroplating-plan.md) as a difficulty 4/5 parallel route.
2. Otherwise begin with **C01 gantry dispensing** for open grooves and pads.
3. Add **C02 robotic spray** only when broad area coverage is required.
4. Use **C03 automated electroless seeding** through a supervised laboratory when complex surfaces justify wet processing.
5. Purchase service coupons for C04–C10 only after a simpler method fails a named geometry or performance requirement.
6. Never buy advanced equipment merely to increase project novelty.

The Artist-D route does not create an eleventh coating chemistry. It automates placement of the conductive filament seed before copper electroplating. Its main risks are IDEX alignment, conductive contamination, high and variable seed resistance, plating voltage drop and current crowding near the electrical contact.

## Difficulty and Cost Register

| Plan | Method | Difficulty | Student trial allowance | Ownership allowance | Recommended role |
|---|---|---:|---:|---:|---|
| [C01](./gantry-dispensed-coating.md) | Gantry-Dispensed Conductive Coating (GDC) | 2/5 | USD $250–$1,000 | USD $500–$2,500 | Recommended first automated method |
| [C02](./robotic-spray-coating.md) | Robotic Airbrush or Spray Coating (RSC) | 3/5 | USD $500–$2,000 | USD $1,500–$8,000 | Useful second method for area coverage |
| [C03](./automated-electroless-seed.md) | Automated Electroless Seed Coating (AESC) | 4/5 | USD $500–$2,500 | USD $5,000–$25,000 | Shared-laboratory method after coupon success |
| [C04](./inkjet-catalyst-seed.md) | Inkjet-Printed Catalyst or Metal Seed (ICS) | 4/5 | USD $1,000–$4,000 | USD $20,000–$100,000 | Service-first research method |
| [C05](./aerosol-jet-seed.md) | Aerosol Jet Printed Seed (AJP) | 5/5 | USD $2,000–$8,000 | USD $100,000–$500,000 | External-service or research-facility method |
| [C06](./laser-direct-structuring.md) | Laser Direct Structuring (LDS) | 5/5 | USD $2,000–$10,000 | USD $75,000–$300,000 | Industrial or university-service method |
| [C07](./flash-ablation-metallization.md) | Flash Ablation Metallization (FAM) | 5/5 | USD $2,000–$10,000 | USD $20,000–$100,000 | Research collaboration method |
| [C08](./physical-vapor-deposition.md) | Physical Vapor Deposition Seed Layer (PVD) | 4/5 | USD $1,000–$5,000 | USD $75,000–$500,000 | Service-first method for uniform thin seeds |
| [C09](./laser-induced-graphene.md) | Laser-Induced Graphene Seed (LIG) | 4/5 | USD $1,000–$5,000 | USD $10,000–$75,000 | Advanced student research with facility laser |
| [C10](./catalyst-loaded-resin.md) | Catalyst-Loaded Multi-Material Resin (CLMR) | 5/5 | USD $2,000–$10,000 | USD $25,000–$150,000 | Research thesis extension, not baseline build |

The cost values are broad AE3PT planning envelopes in 2026 United States dollars. They are not vendor prices. They include representative fixtures, guarding, extraction and qualification, exclude routine labour and building services, and should be replaced with local written quotations before any purchase decision.

## The Ten Plans

1. [C01 — Gantry-Dispensed Conductive Coating](gantry-dispensed-coating.md)
2. [C02 — Robotic Airbrush or Spray Coating](robotic-spray-coating.md)
3. [C03 — Automated Electroless Seed Coating](automated-electroless-seed.md)
4. [C04 — Inkjet-Printed Catalyst or Metal Seed](inkjet-catalyst-seed.md)
5. [C05 — Aerosol Jet Printed Seed](aerosol-jet-seed.md)
6. [C06 — Laser Direct Structuring](laser-direct-structuring.md)
7. [C07 — Flash Ablation Metallization](flash-ablation-metallization.md)
8. [C08 — Physical Vapor Deposition Seed Layer](physical-vapor-deposition.md)
9. [C09 — Laser-Induced Graphene Seed](laser-induced-graphene.md)
10. [C10 — Catalyst-Loaded Multi-Material Resin](catalyst-loaded-resin.md)

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
