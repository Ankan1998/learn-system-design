/**
 * Mermaid rendering for the curriculum site: eager, resilient, zoomable.
 *
 * - Eager: Material's built-in Mermaid support mounts diagrams lazily when
 *   they scroll into view, which fails in background tabs and when printing.
 *   Here every diagram is rendered up front and re-rendered when the reader
 *   toggles light/dark.
 * - Resilient: if the renderer cannot be loaded (offline, CDN blocked) or a
 *   diagram fails to parse, the page shows the diagram source and the reason
 *   instead of a blank gap.
 * - Zoomable: wide diagrams are scaled down to fit the column, so clicking
 *   (or pressing Enter on) a diagram opens it full-screen.
 *
 * The ```mermaid fences are emitted as <div class="mermaid-diagram"> holding
 * the escaped diagram source (see mkdocs.yml -> superfences custom_fences).
 */

const MERMAID_URL = "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs";
const SELECTOR = ".mermaid-diagram";
let mermaid = null;
let counter = 0;

/** Material flags dark mode with data-md-color-scheme="slate" on <body>. */
function currentTheme() {
  return document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "default";
}

/** Stash the original source so theme switches can re-render from it. */
function cacheSources() {
  for (const el of document.querySelectorAll(SELECTOR)) {
    if (el.dataset.source === undefined) {
      el.dataset.source = el.textContent.trim();
    }
  }
}

/** Replace a diagram with its source text and a one-line explanation. */
function showSource(el, reason) {
  const note = document.createElement("p");
  note.textContent = reason;
  const code = document.createElement("code");
  code.textContent = el.dataset.source ?? "";
  const pre = document.createElement("pre");
  pre.append(code);
  el.replaceChildren(note, pre);
  el.classList.remove("mermaid-rendered");
  el.classList.add("mermaid-failed");
  el.removeAttribute("role");
  el.removeAttribute("tabindex");
}

async function renderAll() {
  cacheSources();

  mermaid.initialize({
    startOnLoad: false,
    theme: currentTheme(),
    // Diagram sources are authored in this repo, so HTML labels (<br/>) are safe.
    securityLevel: "loose",
    fontFamily: "inherit",
    flowchart: { htmlLabels: true, useMaxWidth: true, curve: "basis" },
    sequence: { useMaxWidth: true, wrap: true },
    er: { useMaxWidth: true },
    gantt: { useMaxWidth: true }
  });

  for (const el of document.querySelectorAll(SELECTOR)) {
    const source = el.dataset.source;
    if (!source) continue;

    try {
      const { svg } = await mermaid.render(`mermaid-svg-${counter++}`, source);
      el.innerHTML = svg;
      el.classList.remove("mermaid-failed");
      el.classList.add("mermaid-rendered");
      el.setAttribute("role", "button");
      el.setAttribute("tabindex", "0");
      el.setAttribute("title", "Click to enlarge");
      el.setAttribute("aria-label", "Diagram. Press Enter to enlarge.");
    } catch (error) {
      const message = error && error.message ? error.message.split("\n")[0] : String(error);
      showSource(el, `This diagram could not be rendered (${message}). Its source:`);
    }
  }
}

/* ---------- click-to-enlarge ---------- */

let overlay = null;
let lastFocused = null;

function closeZoom() {
  if (!overlay) return;
  overlay.remove();
  overlay = null;
  document.documentElement.style.removeProperty("overflow");
  if (lastFocused) lastFocused.focus({ preventScroll: true });
}

function openZoom(el) {
  const original = el.querySelector("svg");
  if (!original) return;

  lastFocused = el;
  overlay = document.createElement("div");
  overlay.className = "mermaid-zoom";
  overlay.setAttribute("role", "dialog");
  overlay.setAttribute("aria-modal", "true");
  overlay.setAttribute("aria-label", "Enlarged diagram. Press Escape or click to close.");
  overlay.tabIndex = -1;

  const svg = original.cloneNode(true);
  const natural = original.viewBox && original.viewBox.baseVal ? original.viewBox.baseVal.width : 0;
  svg.removeAttribute("height");
  svg.style.maxWidth = "none";
  svg.style.height = "auto";
  // Fill the screen, but never blow a small diagram up past 2x its natural size.
  svg.style.width = natural ? `min(96vw, ${Math.round(natural * 2)}px)` : "96vw";

  const hint = document.createElement("div");
  hint.className = "mermaid-zoom__hint";
  hint.textContent = "Click anywhere or press Esc to close";

  overlay.append(svg, hint);
  overlay.addEventListener("click", closeZoom);
  document.body.append(overlay);
  document.documentElement.style.overflow = "hidden";
  overlay.focus({ preventScroll: true });
}

document.addEventListener("click", (event) => {
  if (overlay) return;
  const el = event.target.closest(`${SELECTOR}.mermaid-rendered`);
  if (el && !window.getSelection().toString()) openZoom(el);
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && overlay) {
    closeZoom();
  } else if ((event.key === "Enter" || event.key === " ") && !overlay) {
    const el = document.activeElement;
    if (el && el.matches && el.matches(`${SELECTOR}.mermaid-rendered`)) {
      event.preventDefault();
      openZoom(el);
    }
  }
});

/* ---------- boot ---------- */

cacheSources();
try {
  mermaid = (await import(MERMAID_URL)).default;
} catch (error) {
  for (const el of document.querySelectorAll(SELECTOR)) {
    showSource(el, "The diagram renderer could not be loaded (are you offline?). Diagram source:");
  }
}

if (mermaid) {
  await renderAll();

  // Re-render when the reader toggles light/dark so diagram colours follow.
  new MutationObserver((mutations) => {
    if (mutations.some((m) => m.attributeName === "data-md-color-scheme")) {
      closeZoom();
      renderAll();
    }
  }).observe(document.body, { attributes: true });
}
