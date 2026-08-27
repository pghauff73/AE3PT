# AE3PT

**Adaptive Electroformed 3D Power Topology** is a closed-loop design and lifecycle simulation concept for lightweight, low-cost, repairable and reusable electrical systems.

This repository contains:

- the complete simulator architecture and development roadmap;
- a phased implementation plan with research tasks and pass/fail gates;
- an undergraduate-scale AE3PT-Lite project;
- low-budget measurement and construction plans;
- Bills of Materials and machine-readable cost registers;
- ten automated conductive-coating method plans;
- a JG MAKER Artist-D dual-material copper-electroplating plan;
- generated Scalable Vector Graphics diagrams;
- a self-contained HTML documentation browser.

## Start Here

- [`AE3PT_SIMULATOR_ROADMAP.md`](AE3PT_SIMULATOR_ROADMAP.md) — research-scale architecture and roadmap.
- [`IMPLEMENTATION_PLAN.md`](IMPLEMENTATION_PLAN.md) — complete implementation phases, microsteps and release gates.
- [`docs/index.md`](docs/index.md) — student-focused project and documentation map.
- [`docs/artist-d-electroplating-plan.md`](docs/artist-d-electroplating-plan.md) — Independent Dual Extrusion conductive-filament and copper-plating route.
- [`docs/conductive-coatings/index.md`](docs/conductive-coatings/index.md) — ten conductive seed automation plans with difficulty and cost.

## Build the Documentation Bundle

The HTML documentation is generated from every Markdown file under `docs/`.

```bash
python tools/build_project_diagrams.py --check
python tools/build_coating_method_plans.py --check
python tools/build_docs_site.py
```

Open `docs/index.html` directly, or run a local server:

```bash
python -m http.server 8765 --directory docs
```

Then open `http://127.0.0.1:8765/`.

## Project Boundary

AE3PT-Lite is a supervised low-voltage educational demonstrator. Copper chemistry, process ventilation, exposure control, rinsing, storage and waste remain under an approved laboratory or qualified service. The repository does not certify a production electrical product or an electroplating facility.

## Generated Assets

- `tools/build_project_diagrams.py` owns the student phase and Artist-D diagrams.
- `tools/build_coating_method_plans.py` owns the coating-method Markdown, SVG and CSV files.
- `tools/build_docs_site.py` owns `docs/assets/document-data.js`.

Run the two diagram generators with `--check` before publication to detect drift.
