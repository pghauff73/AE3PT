(() => {
  "use strict";

  const bundle = window.AE3PT_DOCS;
  const DEFAULT_DOCUMENT_PATH = "student-project.md";
  const STUDY_PROGRESS_KEY = "ae3pt-study-progress-v1";
  const documentProfiles = {
    "index.md": {
      group: "Start Here",
      order: 0,
      label: "Classroom Demonstration Overview",
      kind: "Classroom overview",
      short: "Plain-language project, scale, outcomes, and document map",
      stage: "Understand what is being built and why",
      guidance: "Use this overview for students, lecturers, and non-technical reviewers before opening detailed construction or assessment material.",
    },
    "student-project.md": {
      group: "Start Here",
      order: 1,
      label: "First-Year Student Project Guide",
      kind: "Core project guide",
      short: "First-year 24-week learn–build–measure pathway",
      stage: "Learn → build → measure → decide",
      guidance: "Complete each lesson with evidence, then mark the section finished. Safety and supervisor approval always override website progress.",
    },
    "student-glossary.md": {
      group: "Student Course",
      order: 0,
      label: "First-Year Glossary",
      kind: "Glossary and terminology",
      short: "Technical, business, safety, and project terms",
      stage: "Understand the language before using it",
      guidance: "Spell out every acronym on first use and return here whenever a term, unit, or project-created name is unclear.",
    },
    "student-reading-guide.md": {
      group: "Student Course",
      order: 1,
      label: "Reading and Activity Guide",
      kind: "Reading curriculum",
      short: "Textbooks, official resources, and applied notes",
      stage: "Read only what the next engineering task needs",
      guidance: "Turn every reading into a calculation, test, diagram, risk control, or design decision rather than collecting an unused bibliography.",
    },
    "low-budget-construction-plan.md": {
      group: "Build and Budget",
      order: 0,
      label: "Low-Power Construction Plan",
      kind: "Laboratory construction plan",
      short: "Five-volt tools, sensors, fixtures, and software",
      stage: "Plan equipment before purchasing it",
      guidance: "Use the student guide as the active scope and this document as a deeper construction reference. Release spending only after the relevant gate passes.",
    },
    "bill-of-materials.md": {
      group: "Build and Budget",
      order: 1,
      label: "Student Bill of Materials",
      kind: "Student procurement plan",
      short: "$1,555 team BOM and $7,700 cohort package",
      stage: "Buy only what produces required classroom evidence",
      guidance: "Use purchase gates and recomputed totals. Borrow shared equipment and protect testing and repair funds from optional features.",
    },
    "artist-d-electroplating-plan.md": {
      group: "Build and Budget",
      order: 2,
      label: "Artist-D Copper Electroplating Plan",
      kind: "Machine-specific construction plan",
      short: "Difficulty 4/5 · 300 × 300 × 340 mm IDEX · conductive seed plus copper",
      stage: "Qualify the printer, two materials, seed path, contacts, and copper coverage",
      guidance: "Treat conductive filament as a high-resistance plating seed. Release functional samples only after alignment, isolation, numerical resistance, contact, and supervised plating gates pass.",
    },
    "conductive-coatings/index.md": {
      group: "Conductive Coating Methods",
      order: 0,
      label: "Ten Coating Method Plans",
      kind: "Method selection library",
      short: "Ten automated seed routes compared by difficulty, cost, geometry, gates, and fallback",
      stage: "Choose the simplest process that reaches the required surface",
      guidance: "Start with C01, compare cost per passing coupon, and move to shared-laboratory or service methods only when a named geometry or performance requirement justifies them.",
    },
    "conductive-coatings/gantry-dispensed-coating.md": {
      group: "Conductive Coating Methods",
      order: 1,
      label: "C01 Gantry-Dispensed Coating",
      kind: "Complete method plan",
      short: "Difficulty 2/5 · trial $250–$1,000 · recommended first automation build",
      stage: "Digitally dispense a continuous seed into open grooves and pads",
      guidance: "Qualify harmless-fluid motion first, then seed continuity, adhesion, isolation, copper coverage, and three-run repeatability.",
    },
    "conductive-coatings/robotic-spray-coating.md": {
      group: "Conductive Coating Methods",
      order: 2,
      label: "C02 Robotic Spray Coating",
      kind: "Complete method plan",
      short: "Difficulty 3/5 · trial $500–$2,000 · broad external surface coverage",
      stage: "Control stand-off, overlap, rotation, masking, and extraction",
      guidance: "Use only an approved exhausted enclosure and release only the geometry classes that pass coverage, boundary, adhesion, and plating gates.",
    },
    "conductive-coatings/automated-electroless-seed.md": {
      group: "Conductive Coating Methods",
      order: 3,
      label: "C03 Automated Electroless Seed",
      kind: "Complete method plan",
      short: "Difficulty 4/5 · trial $500–$2,500 · supervised conformal wet process",
      stage: "Control activation, baths, rinses, coverage, and waste",
      guidance: "Students design fixtures and evidence; trained laboratory staff retain authority over chemistry, bath condition, ventilation, and waste.",
    },
    "conductive-coatings/inkjet-catalyst-seed.md": {
      group: "Conductive Coating Methods",
      order: 4,
      label: "C04 Inkjet Catalyst or Metal Seed",
      kind: "Complete method plan",
      short: "Difficulty 4/5 · trial $1,000–$4,000 · fine planar digital traces",
      stage: "Qualify ink, drops, substrate, activation, and thickening as one system",
      guidance: "Use a facility or service first and retain the print file, waveform, ink batch, microscopy, and plated electrical evidence.",
    },
    "conductive-coatings/aerosol-jet-seed.md": {
      group: "Conductive Coating Methods",
      order: 5,
      label: "C05 Aerosol Jet Seed",
      kind: "Complete method plan",
      short: "Difficulty 5/5 · trial $2,000–$8,000 · fine conformal service method",
      stage: "Prove that resolution and three-dimensional access justify specialised equipment",
      guidance: "Purchase only shaped test coupons with a facility evidence contract; compare yield and cost against dispensing and inkjet alternatives.",
    },
    "conductive-coatings/laser-direct-structuring.md": {
      group: "Conductive Coating Methods",
      order: 6,
      label: "C06 Laser Direct Structuring",
      kind: "Complete method plan",
      short: "Difficulty 5/5 · trial $2,000–$10,000 · laser-activated three-dimensional circuits",
      stage: "Match activatable polymer, laser window, focus, and electroless selectivity",
      guidance: "Use an accredited laser and plating facility; a darkened laser path is not a pass until selective metal growth and isolation are proven.",
    },
    "conductive-coatings/flash-ablation-metallization.md": {
      group: "Conductive Coating Methods",
      order: 7,
      label: "C07 Flash Ablation Metallization",
      kind: "Complete method plan",
      short: "Difficulty 5/5 · trial $2,000–$10,000 · pulsed-light research route",
      stage: "Improve a conductive-composite surface without heat or insulation damage",
      guidance: "Do not construct a student flash source. Use a qualified research facility and require damage, conductance, plating, and geometry evidence.",
    },
    "conductive-coatings/physical-vapor-deposition.md": {
      group: "Conductive Coating Methods",
      order: 8,
      label: "C08 Physical Vapor Deposition",
      kind: "Complete method plan",
      short: "Difficulty 4/5 · trial $1,000–$5,000 · vacuum-deposited thin metal seed",
      stage: "Control vacuum compatibility, line-of-sight coverage, handling, and contacts",
      guidance: "Use witness coupons and a facility service; release only surfaces with measured seed continuity and post-plating adhesion.",
    },
    "conductive-coatings/laser-induced-graphene.md": {
      group: "Conductive Coating Methods",
      order: 9,
      label: "C09 Laser-Induced Graphene",
      kind: "Complete method plan",
      short: "Difficulty 4/5 · trial $1,000–$5,000 · laser-written carbon seed",
      stage: "Convert an approved precursor into a durable seed, then deposit copper",
      guidance: "Keep laser, fire, fumes, precursor identity, seed durability, and copper adhesion inside one approved coupon process.",
    },
    "conductive-coatings/catalyst-loaded-resin.md": {
      group: "Conductive Coating Methods",
      order: 10,
      label: "C10 Catalyst-Loaded Resin",
      kind: "Complete method plan",
      short: "Difficulty 5/5 · trial $2,000–$10,000 · multi-material research extension",
      stage: "Couple resin formulation, cure, material isolation, and selective plating",
      guidance: "Treat this as a thesis extension after the baseline project; fail closed on uncured resin, contamination, uncertain chemistry, or background plating.",
    },
    "lecturer-guide.md": {
      group: "Teaching and Funding",
      order: 0,
      label: "Lecturer Guide",
      kind: "Lecturer delivery guide",
      short: "Lessons, gates, assessment, misconceptions, and review",
      stage: "Teach the complete loop without unsupported complexity",
      guidance: "Release practical work only after students can explain the activity and its evidence requirements in ordinary language.",
    },
    "business-funder-brief.md": {
      group: "Teaching and Funding",
      order: 1,
      label: "Business Funder Brief",
      kind: "Business funder brief",
      short: "Funding stages, evidence, risk, and next decisions",
      stage: "Fund learning and uncertainty reduction in stages",
      guidance: "Judge the project by evidence, technical yield, cost visibility, student capability, and the quality of the next decision—not by premature commercial claims.",
    },
    "project-rewrite-plan.md": {
      group: "Improvement Record",
      order: 0,
      label: "Rewrite Problem and Fix Log",
      kind: "Problem and fix log",
      short: "Tree audit, corrections, verification, and second loop",
      stage: "Make document problems and corrections visible",
      guidance: "A correction is complete only when current source, generated data, and rendered pages prove that the conflict is removed.",
    },
    "diagram-implementation-plan.md": {
      group: "Improvement Record",
      order: 1,
      label: "Diagram Implementation Plan",
      kind: "Visual coverage and maintenance plan",
      short: "Eleven accessible phase SVGs plus the coating-method diagram library",
      stage: "Verify every project step has complete visual evidence",
      guidance: "Use the coverage matrix and generated manifest to keep project steps, diagrams, gates, and student evidence synchronized.",
    },
  };
  const groupOrder = ["Start Here", "Student Course", "Build and Budget", "Conductive Coating Methods", "Teaching and Funding", "Improvement Record", "Other Resources"];

  const elements = {
    root: document.documentElement,
    body: document.body,
    sidebar: document.getElementById("document-sidebar"),
    sidebarToggle: document.getElementById("sidebar-toggle"),
    sidebarScrim: document.getElementById("sidebar-scrim"),
    documentTree: document.getElementById("document-tree"),
    documentCount: document.getElementById("document-count"),
    buildStatus: document.getElementById("build-status"),
    documentPath: document.getElementById("document-path"),
    documentTitle: document.getElementById("document-title"),
    documentSummary: document.getElementById("document-summary"),
    documentKind: document.getElementById("document-kind"),
    wordCount: document.getElementById("word-count"),
    readingTime: document.getElementById("reading-time"),
    markdownBody: document.getElementById("markdown-body"),
    pageOutline: document.getElementById("page-outline"),
    globalSearch: document.getElementById("global-search"),
    searchResults: document.getElementById("search-results"),
    copyLink: document.getElementById("copy-link"),
    printDocument: document.getElementById("print-document"),
    themeToggle: document.getElementById("theme-toggle"),
    focusMode: document.getElementById("focus-mode"),
    studyGuideLink: document.getElementById("study-guide-link"),
    startLearning: document.getElementById("start-learning"),
    backToTop: document.getElementById("back-to-top"),
    progressBar: document.getElementById("reading-progress-bar"),
    learningDashboard: document.getElementById("learning-dashboard"),
    learningStage: document.getElementById("learning-stage"),
    learningGuidance: document.getElementById("learning-guidance"),
    studyProgressPanel: document.getElementById("study-progress-panel"),
    studyProgressText: document.getElementById("study-progress-text"),
    studyProgressBar: document.getElementById("study-progress-bar"),
    resetStudyProgress: document.getElementById("reset-study-progress"),
    toast: document.getElementById("toast"),
  };

  const state = {
    documents: Array.isArray(bundle?.documents) ? bundle.documents : [],
    documentByPath: new Map(),
    currentDocument: null,
    currentSection: "",
    outlineObserver: null,
    searchSelection: -1,
    searchItems: [],
    toastTimer: null,
    completedSections: new Set(),
  };

  state.documents.forEach((documentRecord) => state.documentByPath.set(documentRecord.path, documentRecord));

  function defaultDocumentPath() {
    return state.documentByPath.has(DEFAULT_DOCUMENT_PATH) ? DEFAULT_DOCUMENT_PATH : state.documents[0]?.path || "";
  }

  function profileFor(documentPath) {
    return documentProfiles[documentPath] || {
      group: "Other Resources",
      order: 99,
      kind: "Project reference",
      short: humanizePath(documentPath),
      stage: "Use this resource as supporting evidence",
      guidance: "Connect each reference back to the active student scope, its requirements, and its pass/fail gates.",
    };
  }

  function sectionProgressKey(documentPath, sectionId) {
    return `${documentPath}#${sectionId}`;
  }

  function loadStudyProgress() {
    try {
      const stored = JSON.parse(window.localStorage.getItem(STUDY_PROGRESS_KEY) || "[]");
      if (Array.isArray(stored)) state.completedSections = new Set(stored.filter((value) => typeof value === "string"));
    } catch {
      state.completedSections = new Set();
    }
  }

  function saveStudyProgress() {
    window.localStorage.setItem(STUDY_PROGRESS_KEY, JSON.stringify([...state.completedSections].sort()));
  }

  function escapeSelector(value) {
    if (window.CSS?.escape) return window.CSS.escape(value);
    return value.replace(/[^a-zA-Z0-9_-]/g, (character) => `\\${character}`);
  }

  function parseRoute() {
    const hash = window.location.hash.startsWith("#") ? window.location.hash.slice(1) : window.location.hash;
    const params = new URLSearchParams(hash);
    return {
      documentPath: params.get("doc") || defaultDocumentPath(),
      section: params.get("section") || "",
    };
  }

  function routeFor(documentPath, section = "") {
    const params = new URLSearchParams();
    params.set("doc", documentPath);
    if (section) params.set("section", section);
    return `#${params.toString()}`;
  }

  function navigate(documentPath, section = "", replace = false) {
    const target = routeFor(documentPath, section);
    if (replace) window.history.replaceState(null, "", target);
    else if (window.location.hash !== target) window.location.hash = target;
    else loadRoute();
  }

  function humanizePath(path) {
    return path
      .replace(/\.md$/i, "")
      .split("/")
      .map((part) => part.replace(/[-_]+/g, " ").replace(/\b\w/g, (letter) => letter.toUpperCase()))
      .join(" / ");
  }

  function createTreeModel() {
    const root = { folders: new Map(), documents: [] };
    state.documents.forEach((documentRecord) => {
      const segments = documentRecord.path.split("/");
      const filename = segments.pop();
      let cursor = root;
      segments.forEach((segment) => {
        if (!cursor.folders.has(segment)) cursor.folders.set(segment, { folders: new Map(), documents: [] });
        cursor = cursor.folders.get(segment);
      });
      cursor.documents.push({ ...documentRecord, filename });
    });
    return root;
  }

  function renderDocumentButton(documentRecord) {
    const item = document.createElement("li");
    const profile = profileFor(documentRecord.path);
    const button = document.createElement("button");
    button.type = "button";
    button.className = "tree-document-button";
    button.dataset.documentPath = documentRecord.path;
    button.title = documentRecord.path;

    const title = document.createElement("span");
    title.className = "tree-document-title";
    title.textContent = profile.label || documentRecord.title;
    const description = document.createElement("small");
    description.textContent = profile.short;
    button.append(title, description);

    const majorHeadings = documentRecord.headings.filter((heading) => heading.level === 2);
    if (majorHeadings.length) {
      const completed = majorHeadings.filter((heading) => state.completedSections.has(sectionProgressKey(documentRecord.path, heading.id))).length;
      const badge = document.createElement("span");
      badge.className = "tree-progress-badge";
      badge.textContent = `${completed}/${majorHeadings.length}`;
      badge.title = `${completed} of ${majorHeadings.length} major sections marked complete`;
      button.appendChild(badge);
    }

    button.addEventListener("click", () => {
      navigate(documentRecord.path);
      closeSidebar();
    });
    item.appendChild(button);

    if (state.currentDocument?.path === documentRecord.path) {
      button.classList.add("active");
      button.setAttribute("aria-current", "page");
      if (majorHeadings.length) {
        const headingList = document.createElement("ul");
        headingList.className = "tree-document-headings";
        majorHeadings.forEach((heading) => {
          const headingItem = document.createElement("li");
          const headingButton = document.createElement("button");
          headingButton.type = "button";
          headingButton.className = `tree-heading-link level-${heading.level}`;
          headingButton.textContent = heading.text;
          if (state.completedSections.has(sectionProgressKey(documentRecord.path, heading.id))) {
            headingButton.classList.add("completed");
          }
          headingButton.addEventListener("click", () => {
            navigate(documentRecord.path, heading.id);
            closeSidebar();
          });
          headingItem.appendChild(headingButton);
          headingList.appendChild(headingItem);
        });
        item.appendChild(headingList);
      }
    }

    return item;
  }

  function renderTreeBranch(model, label = "") {
    const list = document.createElement("ul");
    list.className = "tree-list";

    [...model.folders.entries()]
      .sort(([left], [right]) => left.localeCompare(right))
      .forEach(([folderName, folderModel]) => {
        const item = document.createElement("li");
        item.className = "tree-folder";
        const details = document.createElement("details");
        details.open = true;
        const summary = document.createElement("summary");
        summary.textContent = humanizePath(folderName);
        details.appendChild(summary);
        details.appendChild(renderTreeBranch(folderModel, folderName));
        item.appendChild(details);
        list.appendChild(item);
      });

    [...model.documents]
      .sort((left, right) => left.path.localeCompare(right.path))
      .forEach((documentRecord) => list.appendChild(renderDocumentButton(documentRecord)));

    if (!label && !list.children.length) {
      const emptyItem = document.createElement("li");
      emptyItem.className = "search-empty";
      emptyItem.textContent = "No Markdown documents were generated.";
      list.appendChild(emptyItem);
    }
    return list;
  }

  function renderDocumentTree() {
    const grouped = new Map(groupOrder.map((groupName) => [groupName, []]));
    state.documents.forEach((documentRecord) => {
      const groupName = profileFor(documentRecord.path).group;
      if (!grouped.has(groupName)) grouped.set(groupName, []);
      grouped.get(groupName).push(documentRecord);
    });

    const fragment = document.createDocumentFragment();
    [...grouped.entries()].forEach(([groupName, documents]) => {
      if (!documents.length) return;
      const section = document.createElement("section");
      section.className = "tree-learning-group";
      const heading = document.createElement("h3");
      heading.textContent = groupName;
      const list = document.createElement("ul");
      list.className = "tree-list";
      documents
        .sort((left, right) => {
          const leftProfile = profileFor(left.path);
          const rightProfile = profileFor(right.path);
          return leftProfile.order - rightProfile.order || left.title.localeCompare(right.title);
        })
        .forEach((documentRecord) => list.appendChild(renderDocumentButton(documentRecord)));
      section.append(heading, list);
      fragment.appendChild(section);
    });

    elements.documentTree.replaceChildren(fragment);
    elements.documentCount.textContent = String(state.documents.length);
    elements.buildStatus.textContent = `${state.documents.length} learning resource${state.documents.length === 1 ? "" : "s"} indexed`;
  }

  function renderOutline(documentRecord) {
    const headings = documentRecord.headings.filter((heading) => heading.level >= 2 && heading.level <= 4);
    const list = document.createElement("ul");
    list.className = "outline-list";
    headings.forEach((heading) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.className = `outline-link level-${heading.level}`;
      link.href = routeFor(documentRecord.path, heading.id);
      link.dataset.sectionId = heading.id;
      link.textContent = heading.text;
      if (heading.level === 2 && state.completedSections.has(sectionProgressKey(documentRecord.path, heading.id))) {
        link.classList.add("completed");
      }
      link.addEventListener("click", (event) => {
        event.preventDefault();
        navigate(documentRecord.path, heading.id);
      });
      item.appendChild(link);
      list.appendChild(item);
    });
    elements.pageOutline.replaceChildren(list);
  }

  function updateStudyProgress(documentRecord = state.currentDocument) {
    if (!documentRecord) return;
    const sections = documentRecord.headings.filter((heading) => heading.level === 2);
    const completed = sections.filter((heading) => state.completedSections.has(sectionProgressKey(documentRecord.path, heading.id))).length;
    const percentage = sections.length ? Math.round((completed / sections.length) * 100) : 0;
    elements.studyProgressText.textContent = `${completed} of ${sections.length}`;
    elements.studyProgressBar.style.width = `${percentage}%`;
    elements.studyProgressPanel.hidden = !sections.length;
  }

  function toggleSectionCompletion(documentPath, sectionId) {
    const key = sectionProgressKey(documentPath, sectionId);
    if (state.completedSections.has(key)) state.completedSections.delete(key);
    else state.completedSections.add(key);
    saveStudyProgress();
    renderDocumentTree();
    renderOutline(state.currentDocument);
    updateStudyProgress();

    const heading = elements.markdownBody.querySelector(`#${escapeSelector(sectionId)}`);
    if (heading) {
      const completed = state.completedSections.has(key);
      heading.classList.toggle("study-complete", completed);
      const button = heading.querySelector(".section-complete-button");
      if (button) {
        button.classList.toggle("completed", completed);
        button.setAttribute("aria-pressed", String(completed));
        button.textContent = completed ? "Completed" : "Mark complete";
      }
    }
    showToast(state.completedSections.has(key) ? "Lesson marked complete" : "Lesson returned to in progress");
  }

  function decorateHeadings(documentRecord) {
    elements.markdownBody.querySelectorAll("h2[id], h3[id], h4[id]").forEach((heading) => {
      const headingText = heading.textContent.trim();
      const anchor = document.createElement("a");
      anchor.className = "heading-anchor";
      anchor.href = routeFor(documentRecord.path, heading.id);
      anchor.setAttribute("aria-label", `Link to ${headingText}`);
      anchor.textContent = "#";
      heading.prepend(anchor);

      if (heading.tagName === "H2") {
        const completed = state.completedSections.has(sectionProgressKey(documentRecord.path, heading.id));
        const button = document.createElement("button");
        button.type = "button";
        button.className = "section-complete-button";
        button.classList.toggle("completed", completed);
        button.setAttribute("aria-pressed", String(completed));
        button.setAttribute("aria-label", `${completed ? "Mark in progress" : "Mark complete"}: ${headingText}`);
        button.textContent = completed ? "Completed" : "Mark complete";
        button.addEventListener("click", () => toggleSectionCompletion(documentRecord.path, heading.id));
        heading.classList.toggle("study-complete", completed);
        heading.appendChild(button);
      }
    });
  }

  function decorateEducationalContent(documentRecord) {
    const calloutTypes = [
      { pattern: /^start here:/i, className: "callout-start", label: "Start here" },
      { pattern: /^(practical|study|budget) tip:/i, className: "callout-tip", label: "Practical tip" },
      { pattern: /^safety (gate|note):/i, className: "callout-safety", label: "Safety note" },
      { pattern: /^learning principle:/i, className: "callout-concept", label: "Learning principle" },
      { pattern: /^lecturer (note|principle):/i, className: "callout-concept", label: "Lecturer note" },
      { pattern: /^(teaching purpose|construction objective|purpose):/i, className: "callout-start", label: "Purpose" },
      { pattern: /^(one-sentence explanation|plain-language proposal):/i, className: "callout-start", label: "Plain-language summary" },
      { pattern: /^(reading|writing) rule:/i, className: "callout-tip", label: "Learning rule" },
      { pattern: /^budget basis:/i, className: "callout-tip", label: "Budget basis" },
      { pattern: /^common mistake:/i, className: "callout-warning", label: "Common mistake" },
    ];

    elements.markdownBody.querySelectorAll("blockquote").forEach((blockquote) => {
      const text = blockquote.textContent.trim();
      const type = calloutTypes.find((candidate) => candidate.pattern.test(text));
      if (!type) return;
      blockquote.classList.add("learning-callout", type.className);
      blockquote.dataset.calloutLabel = type.label;
    });

    elements.markdownBody.querySelectorAll("table").forEach((table) => {
      const firstHeading = table.querySelector("th")?.textContent.trim().toLowerCase() || "";
      if (["term", "symbol"].includes(firstHeading)) table.classList.add("glossary-table");
    });

    elements.body.dataset.documentGroup = profileFor(documentRecord.path).group.toLowerCase().replace(/\s+/g, "-");
  }

  function updateLearningDashboard(documentRecord) {
    const profile = profileFor(documentRecord.path);
    elements.documentKind.textContent = profile.kind;
    elements.learningStage.textContent = profile.stage;
    elements.learningGuidance.textContent = profile.guidance;
    elements.learningDashboard.classList.toggle("core-guide", documentRecord.path === DEFAULT_DOCUMENT_PATH);
    updateStudyProgress(documentRecord);
  }

  function decorateReferences() {
    const referenceHeading = elements.markdownBody.querySelector("#references");
    const referenceList = referenceHeading?.nextElementSibling;
    if (!(referenceList instanceof HTMLOListElement)) return;
    [...referenceList.children].forEach((item, index) => {
      item.id = `reference-${index + 1}`;
    });

    const walker = document.createTreeWalker(elements.markdownBody, NodeFilter.SHOW_TEXT);
    const candidateNodes = [];
    while (walker.nextNode()) {
      const node = walker.currentNode;
      if (!node.parentElement?.closest("a, code, pre, #references + ol")) candidateNodes.push(node);
    }

    candidateNodes.forEach((node) => {
      const value = node.nodeValue || "";
      if (!/\[\d+\]/.test(value)) return;
      const fragment = document.createDocumentFragment();
      let cursor = 0;
      value.replace(/\[(\d+)\]/g, (match, number, offset) => {
        fragment.append(value.slice(cursor, offset));
        const link = document.createElement("a");
        link.href = routeFor(state.currentDocument.path, `reference-${number}`);
        link.className = "citation-link";
        link.textContent = match;
        fragment.append(link);
        cursor = offset + match.length;
        return match;
      });
      fragment.append(value.slice(cursor));
      node.replaceWith(fragment);
    });
  }

  function decorateLinks() {
    elements.markdownBody.querySelectorAll("a[href]").forEach((link) => {
      const href = link.getAttribute("href") || "";
      if (/^https?:\/\//i.test(href)) {
        link.target = "_blank";
        link.rel = "noopener noreferrer";
      }
    });
  }

  function setupOutlineObserver() {
    state.outlineObserver?.disconnect();
    const headings = [...elements.markdownBody.querySelectorAll("h2[id], h3[id], h4[id]")];
    if (!("IntersectionObserver" in window) || !headings.length) return;

    state.outlineObserver = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((left, right) => left.boundingClientRect.top - right.boundingClientRect.top);
        if (!visible.length) return;
        setActiveOutline(visible[0].target.id);
      },
      { rootMargin: "-82px 0px -72% 0px", threshold: [0, 1] },
    );
    headings.forEach((heading) => state.outlineObserver.observe(heading));
  }

  function setActiveOutline(sectionId) {
    elements.pageOutline.querySelectorAll(".outline-link").forEach((link) => {
      link.classList.toggle("active", link.dataset.sectionId === sectionId);
    });
  }

  function scrollToSection(sectionId, behavior = "smooth") {
    if (!sectionId) {
      window.scrollTo({ top: 0, behavior });
      return;
    }
    const target = document.getElementById(sectionId);
    if (!target) return;
    target.scrollIntoView({ behavior, block: "start" });
    target.classList.add("citation-jump");
    window.setTimeout(() => target.classList.remove("citation-jump"), 1200);
    setActiveOutline(sectionId);
  }

  function loadDocument(documentRecord, section = "") {
    state.currentDocument = documentRecord;
    state.currentSection = section;
    elements.documentPath.textContent = documentRecord.path;
    elements.documentTitle.textContent = documentRecord.title;
    elements.documentTitle.classList.toggle("long-title", documentRecord.title.length > 72);
    elements.documentSummary.textContent = documentRecord.summary;
    elements.wordCount.textContent = `${documentRecord.wordCount.toLocaleString()} words`;
    elements.readingTime.textContent = `${Math.max(1, Math.ceil(documentRecord.wordCount / 230))} min read`;
    elements.markdownBody.innerHTML = documentRecord.html;
    elements.markdownBody.querySelector(":scope > h1:first-child")?.remove();
    document.title = `${documentRecord.title} · AE3PT Student Engineering Studio`;

    decorateHeadings(documentRecord);
    decorateLinks();
    decorateReferences();
    decorateEducationalContent(documentRecord);
    updateLearningDashboard(documentRecord);
    renderDocumentTree();
    renderOutline(documentRecord);
    setupOutlineObserver();
    updateReadingProgress();

    window.requestAnimationFrame(() => scrollToSection(section, "auto"));
  }

  function loadRoute() {
    if (!state.documents.length) {
      elements.markdownBody.innerHTML = '<div class="error-state">No generated Markdown documents are available. Run <code>python tools/build_docs_site.py</code>.</div>';
      renderDocumentTree();
      return;
    }

    const route = parseRoute();
    const documentRecord = state.documentByPath.get(route.documentPath) || state.documents[0];
    if (route.documentPath !== documentRecord.path) {
      navigate(documentRecord.path, route.section, true);
      return;
    }

    if (state.currentDocument?.path !== documentRecord.path) loadDocument(documentRecord, route.section);
    else if (route.section !== state.currentSection) {
      state.currentSection = route.section;
      scrollToSection(route.section);
    }
  }

  function searchSnippet(text, query) {
    const lowerText = text.toLowerCase();
    const position = lowerText.indexOf(query);
    if (position < 0) return text.slice(0, 120) + (text.length > 120 ? "…" : "");
    const start = Math.max(0, position - 52);
    const end = Math.min(text.length, position + query.length + 72);
    return `${start > 0 ? "…" : ""}${text.slice(start, end)}${end < text.length ? "…" : ""}`;
  }

  function collectSearchResults(query) {
    const normalizedQuery = query.trim().toLowerCase();
    if (!normalizedQuery) return [];
    const results = [];

    state.documents.forEach((documentRecord) => {
      const titleMatch = documentRecord.title.toLowerCase().includes(normalizedQuery);
      const pathMatch = documentRecord.path.toLowerCase().includes(normalizedQuery);
      const textMatch = documentRecord.text.toLowerCase().includes(normalizedQuery);
      if (titleMatch || pathMatch || textMatch) {
        results.push({
          type: "document",
          documentPath: documentRecord.path,
          section: "",
          title: documentRecord.title,
          detail: searchSnippet(documentRecord.text, normalizedQuery),
          score: titleMatch ? 100 : pathMatch ? 80 : 30,
        });
      }

      documentRecord.headings.forEach((heading) => {
        if (heading.text.toLowerCase().includes(normalizedQuery)) {
          results.push({
            type: "section",
            documentPath: documentRecord.path,
            section: heading.id,
            title: heading.text,
            detail: documentRecord.title,
            score: heading.level === 1 ? 95 : heading.level === 2 ? 90 : 70,
          });
        }
      });
    });

    return results
      .sort((left, right) => right.score - left.score || left.title.localeCompare(right.title))
      .slice(0, 14);
  }

  function renderSearchResults(query) {
    state.searchItems = collectSearchResults(query);
    state.searchSelection = -1;
    elements.searchResults.replaceChildren();

    if (!query.trim()) {
      elements.searchResults.hidden = true;
      return;
    }

    if (!state.searchItems.length) {
      const empty = document.createElement("div");
      empty.className = "search-empty";
      empty.textContent = "No matching documents or sections.";
      elements.searchResults.appendChild(empty);
      elements.searchResults.hidden = false;
      return;
    }

    state.searchItems.forEach((result, index) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "search-result";
      button.dataset.resultIndex = String(index);
      const title = document.createElement("strong");
      title.textContent = result.title;
      const detail = document.createElement("span");
      detail.textContent = result.detail;
      button.append(title, detail);
      button.addEventListener("click", () => activateSearchResult(index));
      elements.searchResults.appendChild(button);
    });
    elements.searchResults.hidden = false;
  }

  function activateSearchResult(index) {
    const result = state.searchItems[index];
    if (!result) return;
    elements.globalSearch.value = "";
    elements.searchResults.hidden = true;
    navigate(result.documentPath, result.section);
  }

  function moveSearchSelection(direction) {
    if (!state.searchItems.length) return;
    state.searchSelection = (state.searchSelection + direction + state.searchItems.length) % state.searchItems.length;
    elements.searchResults.querySelectorAll(".search-result").forEach((element, index) => {
      element.setAttribute("aria-selected", String(index === state.searchSelection));
      if (index === state.searchSelection) element.scrollIntoView({ block: "nearest" });
    });
  }

  function updateReadingProgress() {
    if (!state.currentDocument) return;
    const articleTop = elements.markdownBody.getBoundingClientRect().top + window.scrollY;
    const articleHeight = elements.markdownBody.offsetHeight;
    const viewportAnchor = window.scrollY + 92;
    const available = Math.max(1, articleHeight - window.innerHeight + 92);
    const progress = Math.min(1, Math.max(0, (viewportAnchor - articleTop) / available));
    elements.progressBar.style.width = `${progress * 100}%`;
  }

  function openSidebar() {
    elements.body.classList.add("sidebar-open");
    elements.sidebarToggle.setAttribute("aria-expanded", "true");
    elements.sidebarScrim.hidden = false;
  }

  function closeSidebar() {
    elements.body.classList.remove("sidebar-open");
    elements.sidebarToggle.setAttribute("aria-expanded", "false");
    elements.sidebarScrim.hidden = true;
  }

  function currentThemePreference() {
    return window.localStorage.getItem("ae3pt-docs-theme") || "system";
  }

  function applyTheme(preference) {
    const resolved = preference === "system"
      ? (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light")
      : preference;
    elements.root.dataset.theme = resolved;
    elements.themeToggle.dataset.preference = preference;
    elements.themeToggle.title = `Theme: ${preference}. Activate to change.`;
    elements.themeToggle.setAttribute("aria-label", `Color theme is ${preference}; change color theme`);
  }

  function cycleTheme() {
    const sequence = ["system", "light", "dark"];
    const current = elements.themeToggle.dataset.preference || "system";
    const next = sequence[(sequence.indexOf(current) + 1) % sequence.length];
    window.localStorage.setItem("ae3pt-docs-theme", next);
    applyTheme(next);
    showToast(`Theme set to ${next}`);
  }

  function toggleFocusMode() {
    const active = elements.body.classList.toggle("focus-mode");
    elements.focusMode.setAttribute("aria-pressed", String(active));
    elements.focusMode.textContent = active ? "Exit focus" : "Focus";
    elements.focusMode.title = active ? "Restore project navigation" : "Hide navigation for focused reading";
    showToast(active ? "Focus mode enabled" : "Project navigation restored");
    window.requestAnimationFrame(updateReadingProgress);
  }

  function resetCurrentStudyProgress() {
    if (!state.currentDocument) return;
    const prefix = `${state.currentDocument.path}#`;
    state.completedSections = new Set([...state.completedSections].filter((key) => !key.startsWith(prefix)));
    saveStudyProgress();
    loadDocument(state.currentDocument, state.currentSection);
    showToast("Lesson progress reset for this resource");
  }

  function showToast(message) {
    window.clearTimeout(state.toastTimer);
    elements.toast.textContent = message;
    elements.toast.hidden = false;
    state.toastTimer = window.setTimeout(() => {
      elements.toast.hidden = true;
    }, 2200);
  }

  async function copyCurrentLink() {
    const url = window.location.href;
    try {
      await navigator.clipboard.writeText(url);
      showToast("Document link copied");
    } catch {
      const input = document.createElement("textarea");
      input.value = url;
      input.style.position = "fixed";
      input.style.opacity = "0";
      document.body.appendChild(input);
      input.select();
      document.execCommand("copy");
      input.remove();
      showToast("Document link copied");
    }
  }

  function bindEvents() {
    window.addEventListener("hashchange", loadRoute);
    window.addEventListener("scroll", updateReadingProgress, { passive: true });
    window.addEventListener("resize", updateReadingProgress, { passive: true });
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener?.("change", () => {
      if (currentThemePreference() === "system") applyTheme("system");
    });

    elements.sidebarToggle.addEventListener("click", () => {
      if (elements.body.classList.contains("sidebar-open")) closeSidebar();
      else openSidebar();
    });
    elements.sidebarScrim.addEventListener("click", closeSidebar);
    elements.themeToggle.addEventListener("click", cycleTheme);
    elements.focusMode.addEventListener("click", toggleFocusMode);
    elements.studyGuideLink.addEventListener("click", () => navigate(DEFAULT_DOCUMENT_PATH));
    elements.startLearning.addEventListener("click", () => {
      navigate(DEFAULT_DOCUMENT_PATH);
      closeSidebar();
    });
    elements.resetStudyProgress.addEventListener("click", resetCurrentStudyProgress);
    elements.printDocument.addEventListener("click", () => window.print());
    elements.copyLink.addEventListener("click", copyCurrentLink);
    elements.backToTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));

    document.querySelectorAll("[data-learning-doc]").forEach((button) => {
      button.addEventListener("click", () => {
        navigate(button.dataset.learningDoc, button.dataset.learningSection || "");
      });
    });

    elements.globalSearch.addEventListener("input", (event) => renderSearchResults(event.target.value));
    elements.globalSearch.addEventListener("keydown", (event) => {
      if (event.key === "ArrowDown") {
        event.preventDefault();
        moveSearchSelection(1);
      } else if (event.key === "ArrowUp") {
        event.preventDefault();
        moveSearchSelection(-1);
      } else if (event.key === "Enter" && state.searchSelection >= 0) {
        event.preventDefault();
        activateSearchResult(state.searchSelection);
      } else if (event.key === "Escape") {
        elements.globalSearch.value = "";
        elements.searchResults.hidden = true;
        elements.globalSearch.blur();
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "/" && !/input|textarea|select/i.test(document.activeElement?.tagName || "")) {
        event.preventDefault();
        elements.globalSearch.focus();
      }
      if (event.key === "Escape") closeSidebar();
    });

    document.addEventListener("click", (event) => {
      if (!elements.searchResults.contains(event.target) && event.target !== elements.globalSearch) {
        elements.searchResults.hidden = true;
      }
    });
  }

  function initialize() {
    applyTheme(currentThemePreference());
    loadStudyProgress();
    bindEvents();
    renderDocumentTree();

    if (!bundle || !state.documents.length) {
      elements.markdownBody.innerHTML = '<div class="error-state">The documentation data bundle is missing or empty. Run <code>python tools/build_docs_site.py</code> from the project root.</div>';
      elements.documentSummary.textContent = "No generated document data are available.";
      elements.buildStatus.textContent = "Document data unavailable";
      return;
    }

    if (!window.location.hash) navigate(defaultDocumentPath(), "", true);
    loadRoute();
  }

  initialize();
})();
