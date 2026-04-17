---
name: btp-solution-diagram-generator
description: Use when creating, editing, or generating SAP BTP (Business Technology Platform) solution diagrams as draw.io (.drawio) files — solution architectures, process flows, data flows, deployment topologies, or any visual showing SAP BTP services, subaccounts, runtimes, integrations, identity flows, or hybrid SAP/non-SAP landscapes. Covers the official SAP BTP Solution Diagram Guidelines (SAP Fiori Horizon colors, area/layer conventions, connector semantics for auth/trust/authorization, the SAP BTP Service Icon library, diagram levels L0–L3), mxGraph XML authoring, and the end-to-end workflow from request to a ready-to-open .drawio file. Trigger on phrases like "BTP architecture diagram", "SAP solution diagram", "draw the subaccount layout", "diagram my CAP/SAP Build app", "show the Cloud Identity Services flow", "visualize the BTP landscape" — even when the user doesn't say the word "drawio" explicitly.
---

# SAP BTP Solution Diagram Generator

Generate, edit, and validate `.drawio` diagrams that follow the official
[SAP BTP Solution Diagram Guidelines](https://sap.github.io/btp-solution-diagrams/).
Output files open directly in [draw.io](https://drawio.com/) (web, desktop, or VS Code
extension `hediet.vscode-drawio`) without any manual fixes.

The goal isn't just "a diagram that opens" — it's a diagram that looks like it came
out of SAP's own guideline, using the **SAP Fiori Horizon** palette, the **grey-circle
BTP service icons**, and the area/connector conventions SAP architects expect.

---

## 1. When to Use This Skill

Trigger this skill for any request that involves visualizing SAP BTP architecture.
Examples — load this skill even if "drawio" or "BTP" isn't spelled out:

- "Draw an architecture diagram for our SAP Build Work Zone setup"
- "Visualize how SAP Cloud Identity Services authenticates users into our CAP app"
- "Show the subaccount structure with Kyma runtime and HANA Cloud"
- "Make a data-flow diagram from S/4HANA to SAP Datasphere via Cloud Integration"
- "I need a solution diagram for SAP Task Center at L2"
- "Diagram how we extend S/4HANA with BTP"
- Any `.drawio` file mentioning BTP services or running on the BTP landscape

If the user wants a *non-BTP* diagram (pure flowchart, UML, ER), fall back to the
generic draw.io approach. This skill is specifically for BTP-flavored diagrams.

---

## 2. Supported Diagram Types

| Type | Starter template | What it shows |
|---|---|---|
| Solution / Architecture (L0–L3) | `assets/templates/solution-diagram-l2.drawio` | BTP subaccount with services, runtimes, identity, and integrations |
| Process flow | `assets/templates/process-flow.drawio` | Numbered sequence of steps across BTP and external systems |
| Data flow | `assets/templates/data-flow.drawio` | Direction and shape of data movement between services |
| Reusable legend | `assets/templates/legend.drawio` | Drop-in legend for connectors and semantic colors |

### Diagram Levels (granularity)

SAP's guideline defines four levels of detail. Pick the right one up front — users
often ask for "an architecture diagram" when what they need is L1 or L2.

| Level | Audience | Shows |
|---|---|---|
| **L0** | Executive / business | BTP as a single block, 2–4 high-level capability areas, no service icons |
| **L1** | Solution overview | Major components grouped into areas; minimal service names; logical flows |
| **L2** | Technical stakeholders (default) | Individual BTP services with icons, clear auth/trust/data flows, legend |
| **L3** | Deep technical | L2 plus protocols, ports, adapters, destinations, principal propagation details |

If the user doesn't specify, default to **L2** and mention you did.

---

## 3. Prerequisites

- **draw.io** — web (`app.diagrams.net`), desktop, or the VS Code extension
  `hediet.vscode-drawio`. All three render the same `.drawio` XML.
- **Python 3.8+** (optional) — for the helper scripts in `scripts/`:
  - `validate_drawio.py` — structural validation + BTP-specific checks
  - `generate_btp_diagram.py` — scaffold a new BTP diagram with defaults applied
  - `download_btp_libraries.py` — fetch the official SAP BTP icon libraries
    (`.xml`) from GitHub so the user can import them into draw.io

No other dependencies. The scripts use only the Python standard library.

---

## 4. Step-by-Step Workflow

Follow this order for every BTP diagram request.

### Step 1 — Clarify intent (only if ambiguous)

You want to pin down five things. If the user's prompt already covers them, skip
ahead; don't ask for the sake of asking.

1. **Diagram level** (L0/L1/L2/L3) — default L2 if unspecified
2. **Diagram type** (solution, process flow, data flow)
3. **Central BTP scenario** (e.g. SAP Build Work Zone, Task Center, CAP on Cloud
   Foundry, extension on Kyma, Datasphere pipeline)
4. **SAP systems involved** (S/4HANA on-prem / Cloud, SuccessFactors, Ariba, etc.)
5. **Non-SAP / external systems** (identity providers, 3rd-party apps, databases)

### Step 2 — Choose a starting template

- **Solution diagram** → copy `assets/templates/solution-diagram-l2.drawio`
- **Process flow** → copy `assets/templates/process-flow.drawio`
- **Data flow** → copy `assets/templates/data-flow.drawio`

If none fits, start fresh with this minimal skeleton (A4 landscape, 1169×827):

```xml
<mxfile host="Electron" modified="" version="27.0.0">
  <diagram id="page-1" name="BTP Solution Diagram">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="1169" pageHeight="827"
                  math="0" shadow="0" background="none">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- your cells -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Cells `id="0"` and `id="1"` are mandatory and must be first, in that order. `id="1"`
must have `parent="0"`. Never reuse those ids for anything else.

### Step 3 — Plan the layout

Before writing any XML, sketch mentally (or in a comment):

1. **The BTP subaccount area** is the dominant container — a blue rounded
   rectangle (`strokeColor=#0070F2`, `fillColor=#EBF8FF`, `arcSize=16`,
   `absoluteArcSize=1`). It's usually the largest single element and sits
   center/upper-left.
2. **Non-SAP systems** sit outside the BTP area in grey containers
   (`strokeColor=#475E75`, `fillColor=#F5F6F7`).
3. **SAP on-premise / other SAP cloud solutions** get their own blue-outlined
   containers, separate from the BTP area.
4. **User/actor** top-left or top-right as a user icon.
5. **Identity & trust flows** are pink (`#CC00DC`), authentication is green
   (`#188918`), authorization is indigo (`#5D36FF`) — use these sparingly.
6. **Firewalls** are thick grey bars, not thin lines.
7. **Leave ~16px of whitespace** around icons. Good breathing room matters.

### Step 4 — Apply BTP-correct styles

Never use draw.io's default fillColor/strokeColor palette (the pale pastel blue, etc.).
Always use the SAP Horizon values below. Everything else will look off-brand.

**Primary colors**

| Purpose | strokeColor | fillColor | Notes |
|---|---|---|---|
| SAP / BTP area | `#0070F2` | `#EBF8FF` | The default container for anything BTP-owned |
| Non-SAP area | `#475E75` | `#F5F6F7` | 3rd-party apps, external IdPs, partner systems |
| Title text | `#1D2D3E` | — | Used for headers and labels |
| Body text | `#556B82` | — | Used for descriptions and secondary labels |

**Semantic colors (for lines and status indicators)**

| Purpose | Color |
|---|---|
| Positive / Authentication flow | `#188918` (fill `#F5FAE5`) |
| Critical / Warning | `#C35500` (fill `#FFF8D6`) |
| Negative / Error | `#D20A0A` (fill `#FFEAF4`) |

**Accent colors (use sparingly to highlight)**

| Purpose | Color |
|---|---|
| Teal (emphasis) | `#07838F` (fill `#DAFDF5`) |
| Indigo / Authorization flow | `#5D36FF` (fill `#F1ECFF`) |
| Pink / Trust flow | `#CC00DC` (fill `#FFF0FA`) |

> Full reference: `references/btp-colors-and-styles.md`

### Step 5 — Pick the right connector semantics

Connector meaning in BTP diagrams is standardized. Stick to these and the reader
can understand the flow without you having to over-explain in the legend.

| Meaning | Line style | Color |
|---|---|---|
| Direct, synchronous data flow (request-response) | solid, one-directional | grey `#475E75` or blue `#0070F2` |
| Indirect / asynchronous data flow | **dashed**, one-directional | same |
| Optional data flow | **dotted** | same |
| Mutual trust | solid, bi-directional | pink `#CC00DC` |
| Authentication | solid or dashed | green `#188918` |
| Authorization | solid | indigo `#5D36FF` |
| Firewall / network barrier | **thick** (`strokeWidth=4`) | grey `#475E75` |

Edge style string pattern:

```
endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;
```

For a dashed line add `dashed=1;` and for dotted add `dashed=1;dashPattern=1 4;`.

> Full reference: `references/btp-connectors-and-annotations.md`

### Step 6 — Use the official BTP service icons

The guideline is emphatic: **use the icon version with the grey background circle**,
not the older flat icons.

**The full SAP BTP icon library is bundled inside this skill** at
`assets/libraries/`. You don't need to fetch anything — the XML files are
already here, mirroring the structure from `SAP/btp-solution-diagrams`.

**Three approaches:**

**(a) Import a bundled library into draw.io (recommended for editable files).**
In draw.io (web / desktop / VS Code):
1. `File → Open Library from → File…`
2. Pick the library you want from `assets/libraries/` — e.g. for every
   service in one file (Size M):
   `assets/libraries/20-02-99-sap-btp-service-icons-all/20-02-99-02-sap-btp-service-icons-all-size-M.xml`
3. Icons appear in the left-hand panel; drag them onto the canvas

Size **M** (24px) is the default. Size **S** (16px) is useful for dense L3
diagrams; size **L** (48px) for L0/L1 overviews.

**(b) Copy an `<mxCell>` directly from the bundled library XML.**
Each icon in the library is a fully-formed `<mxCell>` with a
`shape=image;image=data:image/svg+xml,<base64>;...` style. For fully
self-contained `.drawio` files, copy the cell into your diagram and
adjust `x`, `y`, `width`, `height`, and `value` (the label). No library
import required afterwards.

**(c) Start from a real SAP reference example.**
`assets/reference-examples/` contains 11 editable `.drawio` files from the
SAP repo (Task Center L0/L1/L2, Build Work Zone L2, Cloud Identity
Authentication/Authorization/Lifecycle, Private Link Service, SAP Start,
Build Process Automation L2). These are great if the user wants something
close to an existing SAP scenario.

> Searchable icon catalog (names and IDs): see `references/btp-icons.md`
>
> The bundled libraries are a snapshot of the SAP repo. To refresh them
> against upstream, run `python scripts/download_btp_libraries.py --all --out assets/libraries`.

### Step 7 — Add the mandatory diagram scaffolding

Every BTP solution diagram should include:

1. **A title** — top-left, fontSize 16, fontColor `#0070F2`, bold, Arial or Helvetica
2. **A short description** — ~2–3 lines under the title, fontColor `#475E75`,
   fontSize 12, non-bold
3. **A diagram level indicator** — e.g. "Diagram Level: L2", bold, fontColor `#1D2D3E`
4. **A legend** — white-fill rounded rectangle (`fillColor=#FFFFFF`,
   `strokeColor=#eaecee`, `arcSize=16`, `absoluteArcSize=1`) containing one entry
   per connector type and per access/color used. See `assets/templates/legend.drawio`

### Step 8 — Write, validate, and hand off

1. **Write** the file to the requested path with `.drawio` extension.
2. **Validate**:
   ```bash
   python scripts/validate_drawio.py <path-to-file.drawio>
   ```
   This checks XML well-formedness, required root cells, unique ids, parent
   references, vertex geometry, edge endpoints, plus BTP-specific guidance
   (presence of title, presence of legend, use of BTP palette).
3. **Tell the user** how to open it — point to draw.io web, desktop, or the VS
   Code extension. Mention they can also import the SAP BTP icon library if they
   want to add more services.
4. **Summarize** what the diagram contains in 1–2 sentences (what the user
   gains from opening it).

---

## 5. Anatomy of a Correct BTP Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ [Title: "SAP Task Center - BTP Solution Diagram"]            │  <-- #0070F2, bold, 16pt
│ Short description (2–3 lines)                                │  <-- #475E75, 12pt
│ Diagram Level: L2                                            │
│                                                              │
│  ┌──────────────────────────────┐   ┌───────────────────┐    │
│  │  SAP BTP Subaccount (blue)   │   │ Non-SAP System    │    │
│  │                              │   │ (grey)            │    │
│  │  ┌──[Cloud Foundry runtime]  │   │                   │    │
│  │  │  [icon]  SAP Build WZ      │  │                   │    │
│  │  │  [icon]  SAP Task Center   │  │                   │    │
│  │  └────────────────────────┘   │                   │    │
│  │                              │   └───────────────────┘    │
│  │  [icon] Cloud Identity Svc   │                            │
│  │  [icon] Destination Service  │                            │
│  └──────────────────────────────┘                            │
│                                                              │
│   ┌─ Legend ─────────────────┐                               │
│   │ ● Access       ─► Service │                              │
│   │ ● Authentication ══► MTrust│                              │
│   │ ● Authorization  ··► Opt. │                              │
│   └──────────────────────────┘                               │
└─────────────────────────────────────────────────────────────┘
```

The blue BTP subaccount dominates; internal services nest inside with alternating
fill to provide contrast; non-SAP systems are grey, outside; identity/trust
flows use semantic colors; a legend explains the connector semantics.

---

## 6. mxGraph XML Essentials

Full reference: `references/drawio-xml-schema.md`. The highlights:

**Vertex cell** (any shape, container, or icon):
```xml
<mxCell id="unique-id" value="Label"
        style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EBF8FF;strokeColor=#0070F2;"
        vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="320" height="200" as="geometry" />
</mxCell>
```

**Edge cell** (any connector):
```xml
<mxCell id="edge-1" value=""
        style="endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;endFill=1;endSize=4;"
        edge="1" source="a" target="b" parent="1">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**BTP service icon** (grey-circle version — the important bit is
`shape=image;...image=data:image/svg+xml,<BASE64>`):
```xml
<mxCell id="svc-wz" value="SAP Build Work Zone"
        style="shape=image;verticalLabelPosition=bottom;verticalAlign=top;imageAspect=0;aspect=fixed;image=data:image/svg+xml,<BASE64>;fontColor=#556B82;fontSize=10;"
        vertex="1" parent="1">
  <mxGeometry x="240" y="160" width="48" height="48" as="geometry" />
</mxCell>
```

**Rules** (every file must satisfy these or draw.io won't render):
- Cells `id="0"` and `id="1"` exist, are first and second, in that order
- All other cells have a `parent` pointing at an existing id
- All ids are unique within a diagram page
- Every vertex has an `<mxGeometry as="geometry">` child
- Every edge has either `source`+`target` attributes pointing at real vertex
  ids, or `<mxPoint as="sourcePoint">` + `<mxPoint as="targetPoint">` in its
  `<mxGeometry>` (floating edges)
- XML special characters in labels are escaped: `&` → `&amp;`, `<` → `&lt;`,
  `>` → `&gt;`

---

## 7. Editing Existing BTP Diagrams

1. **Read the file first.** Understand existing ids, the subaccount container's
   id, the group hierarchy. Services nested inside a group use coordinates
   **relative to the group**, not the page.
2. **Reuse the existing palette.** If the file already uses `#0070F2` / `#EBF8FF`,
   stay consistent. Don't mix Horizon with draw.io defaults.
3. **Generate non-colliding ids.** A short prefix like `btp-` plus a random
   suffix is safest.
4. **After moving shapes, re-check edges.** Edges use ids, not positions, so
   they survive moves — but they'll dangle if you deleted an endpoint.
5. **Run the validator** after editing. Same command as Step 8 above.

---

## 8. Best Practices

**Layout**
- Align shapes to the 10px grid (all x/y divisible by 10)
- Leave ~16px of whitespace around icons (Horizon guideline: "rule of thumb —
  spacing = height of the SAP logo")
- Group related services inside a swimlane or rounded-rectangle area
- For L2 diagrams, aim for ≤ 15 services on one page — split into L2a/L2b if more

**Labels**
- Service labels are **below** the icon, not inside it, fontSize 10,
  fontColor `#556B82`, Arial
- Title is top-left, fontSize 16, bold, fontColor `#0070F2`
- Keep labels concise. "SAP Cloud Identity Services" is fine; don't add "(SAP
  BTP service for authentication)" — the reader knows.

**Colors**
- Don't color every area differently. Blue (BTP) + grey (non-SAP) carries most
  diagrams. Accent colors (teal/indigo/pink) are for specific highlights only.
- Never color-code services by *type* with custom colors — that fights the
  guideline. Use the standard palette and let icons differentiate services.

**Connector direction**
- Arrow points **from caller to callee** for synchronous flows
- For mutual trust, use a bidirectional arrow with both ends as blockThin
- Dashed ≠ optional in BTP semantics; dashed means **asynchronous**. Use
  **dotted** (`dashPattern=1 4`) for optional.

**File naming**
- Kebab-case, describe the scenario: `task-center-l2.drawio`,
  `cap-on-cf-extension.drawio`, `s4-datasphere-data-flow.drawio`
- Append the level: `-l1`, `-l2`, `-l3` so readers know the granularity up front

---

## 9. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| File opens blank | Missing `id=0` or `id=1` cell | Add both at the top of `<root>` |
| Icon shows as a red X | SVG base64 is truncated or corrupted | Re-copy from library XML — the whole `image=data:image/svg+xml,...` blob must be intact |
| Shape appears far away | Child of a group, but x/y given in page coords | Convert to relative coords, or set `parent="1"` if you want page coords |
| Lines look flat pastel | Using draw.io's default colors | Replace with Horizon palette from §4 |
| "Diagram looks off" but no specific issue | Palette mixing, inconsistent fonts, too many accent colors | Audit against `references/btp-colors-and-styles.md` |
| Validator complains "no title cell" | No 16pt header at top of page | Add a `text;...fontSize=16;fontStyle=1;fontColor=#0070F2;` cell |
| Can't find a service icon | Service may be under a different naming in the library | Search the icon catalog in `references/btp-icons.md` |

---

## 10. Output Handoff

Deliver three things with every generated file:

1. **The `.drawio` file** at the requested path
2. **A one-line summary** of what it shows (for the reader's context)
3. **How to open and edit it**:
   > Open the file in draw.io (`app.diagrams.net`) or the VS Code extension
   > `hediet.vscode-drawio`. To add more SAP BTP services, load the official icon
   > library: `File → Open Library from → URL…`, paste
   > `https://github.com/SAP/btp-solution-diagrams/blob/main/assets/shape-libraries-and-editable-presets/draw.io/20-02-99-sap-btp-service-icons-all/20-02-99-02-sap-btp-service-icons-all-size-M.xml`

---

## 11. Reference Files

| File | What's in it |
|---|---|
| `references/btp-colors-and-styles.md` | Complete Horizon palette, text styles, spacing rules, ready-to-paste style strings |
| `references/btp-areas-and-layers.md` | Area types (BTP, non-SAP, accent), nesting rules, cardinality (stacked areas), layer proportions |
| `references/btp-connectors-and-annotations.md` | Connector semantics, authentication/authorization/trust color mapping, firewall style, interface annotations |
| `references/btp-icons.md` | Catalog of all ~200 SAP BTP service icons with their library titles — search by service name |
| `references/drawio-xml-schema.md` | mxfile/mxGraphModel/mxCell attribute reference, coordinate system, reserved cells |
| `references/diagram-levels.md` | When to use L0 vs L1 vs L2 vs L3, and the contents expected at each |
| `assets/templates/solution-diagram-l2.drawio` | Ready-to-edit L2 solution diagram with BTP subaccount, 3rd-party area, legend |
| `assets/templates/process-flow.drawio` | Numbered process-flow starter |
| `assets/templates/data-flow.drawio` | Data-flow starter with two systems and a BTP area |
| `assets/templates/legend.drawio` | Drop-in legend you can copy into any diagram |
| `assets/libraries/` | **Bundled** — the full SAP BTP icon library (all 22 XML files: foundational / integration-suite / app-dev-automation / data-analytics / AI / BTP-SaaS / all-in-one, in sizes S/M/L, plus generics and annotation helpers) |
| `assets/reference-examples/` | **Bundled** — 11 editable `.drawio` files from SAP (Task Center L0/L1/L2, Build Work Zone L2, Cloud Identity flows, Private Link, SAP Start, Build Process Automation L2) |
| `scripts/validate_drawio.py` | 