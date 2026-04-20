# Copilot instructions — SAP BTP Solution Diagram Generator

This repo is a knowledge base for authoring **SAP BTP solution diagrams as `.drawio` files**
that follow the official [SAP BTP Solution Diagram Guidelines](https://sap.github.io/btp-solution-diagrams/).

When the user asks for anything that involves visualizing SAP BTP architecture, follow the
rules below. The goal isn't "a diagram that opens" — it's a diagram that looks like it came
out of SAP's own guideline: **SAP Fiori Horizon** palette, **grey-circle BTP service icons**,
and the area/connector conventions SAP architects expect.

Skill source of truth: `plugins/btp-solution-diagram-generator/skills/btp-solution-diagram-generator/SKILL.md`.
If this file and `SKILL.md` disagree, `SKILL.md` wins.

---

## When to apply

Trigger for any request like:

- "Draw an architecture diagram for our SAP Build Work Zone setup"
- "Visualize how SAP Cloud Identity Services authenticates users into our CAP app"
- "Show the subaccount structure with Kyma runtime and HANA Cloud"
- "Data-flow diagram from S/4HANA to Datasphere via Cloud Integration"
- "Solution diagram for SAP Task Center at L2"
- Any `.drawio` file that mentions BTP services or running on the BTP landscape

For non-BTP diagrams (pure flowchart/UML/ER), don't apply this guidance.

---

## Diagram levels

Pick the right level up front. Users often say "architecture diagram" when they mean L1 or L2.

| Level | Audience | Shows |
|---|---|---|
| **L0** | Executive / business | BTP as a single block, 2–4 capability areas, no service icons |
| **L1** | Solution overview | Areas and groups, minimal service names, logical flows |
| **L2** | Technical (default) | Individual BTP services with icons, auth/trust/data flows, legend |
| **L3** | Deep technical | L2 + protocols, ports, adapters, destinations, principal propagation |

If the user doesn't specify, default to **L2** and say so.

---

## Workflow

1. **Clarify only if ambiguous** — level, diagram type (solution / process flow / data flow),
   central BTP scenario, SAP systems involved, non-SAP systems. Skip questions the prompt
   already answered.
2. **Start from a template.** Copy one of:
   - `plugins/btp-solution-diagram-generator/skills/btp-solution-diagram-generator/assets/templates/solution-diagram-l2.drawio`
   - `.../assets/templates/process-flow.drawio`
   - `.../assets/templates/data-flow.drawio`
   - `.../assets/templates/legend.drawio` (drop-in legend)
3. **Or start from a real SAP example.** 11 editable `.drawio` files in
   `.../assets/reference-examples/` — Task Center L0/L1/L2, Build Work Zone L2, Cloud
   Identity Authentication/Authorization/Lifecycle, Private Link, SAP Start, Build Process
   Automation L2.
4. **Apply Horizon styles** (see palette below). Never use draw.io's default pastel colors.
5. **Use the right connector semantics** (see table below).
6. **Use the grey-circle BTP service icons** — bundled in `.../assets/libraries/`.
7. **Add scaffolding:** title (16pt, bold, `#0070F2`), 2–3 line description (`#475E75`, 12pt),
   diagram level indicator, and a legend.
8. **Hand off:** write the `.drawio` file, summarize in one line, tell the user to open it
   in draw.io (`app.diagrams.net`), desktop, or VS Code `hediet.vscode-drawio`.

Minimal skeleton (A4 landscape, 1169×827) — cells `id="0"` and `id="1"` are mandatory,
first, in that order:

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

---

## Horizon palette (mandatory)

**Primary**

| Purpose | strokeColor | fillColor |
|---|---|---|
| SAP / BTP area | `#0070F2` | `#EBF8FF` |
| Non-SAP area | `#475E75` | `#F5F6F7` |
| Title text | `#1D2D3E` | — |
| Body text | `#556B82` | — |

**Semantic (lines, status)**

| Purpose | Color |
|---|---|
| Authentication / positive | `#188918` (fill `#F5FAE5`) |
| Warning / critical | `#C35500` (fill `#FFF8D6`) |
| Error / negative | `#D20A0A` (fill `#FFEAF4`) |

**Accents (use sparingly)**

| Purpose | Color |
|---|---|
| Teal emphasis | `#07838F` (fill `#DAFDF5`) |
| Authorization (indigo) | `#5D36FF` (fill `#F1ECFF`) |
| Trust (pink) | `#CC00DC` (fill `#FFF0FA`) |

Full reference: `plugins/btp-solution-diagram-generator/skills/btp-solution-diagram-generator/references/btp-colors-and-styles.md`.

---

## Connector semantics

| Meaning | Line style | Color |
|---|---|---|
| Sync request-response | solid, one-directional | grey `#475E75` or blue `#0070F2` |
| Async / indirect | **dashed** | same |
| Optional | **dotted** (`dashPattern=1 4`) | same |
| Mutual trust | solid, bi-directional | pink `#CC00DC` |
| Authentication | solid or dashed | green `#188918` |
| Authorization | solid | indigo `#5D36FF` |
| Firewall | **thick** (`strokeWidth=4`) | grey `#475E75` |

Base edge style:
```
endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;
```
Add `dashed=1;` for async; `dashed=1;dashPattern=1 4;` for optional.

**Dashed ≠ optional in BTP — dashed means asynchronous.** Use dotted for optional.

Full reference: `plugins/btp-solution-diagram-generator/skills/btp-solution-diagram-generator/references/btp-connectors-and-annotations.md`.

---

## BTP service icons

Use the **grey-circle** version, not the old flat icons. The full library is bundled at
`plugins/btp-solution-diagram-generator/skills/btp-solution-diagram-generator/assets/libraries/`.

Two ways to use them:

- **Import into draw.io**: `File → Open Library from → File…` and pick e.g.
  `.../assets/libraries/20-02-99-sap-btp-service-icons-all/20-02-99-02-sap-btp-service-icons-all-size-M.xml`
- **Inline in the `.drawio` XML**: copy the `<mxCell>` with
  `shape=image;image=data:image/svg+xml,<base64>;...` directly from the library file into
  your diagram. Adjust `x`, `y`, `width`, `height`, `value`. No library import required.

Size **M** (24px) is the default. **S** (16px) for dense L3, **L** (48px) for L0/L1.

Searchable icon names: `.../references/btp-icons.md`.

---

## mxGraph XML essentials

**Vertex:**
```xml
<mxCell id="unique-id" value="Label"
        style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EBF8FF;strokeColor=#0070F2;"
        vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="320" height="200" as="geometry" />
</mxCell>
```

**Edge:**
```xml
<mxCell id="edge-1" value=""
        style="endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;endFill=1;endSize=4;"
        edge="1" source="a" target="b" parent="1">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**BTP service icon:**
```xml
<mxCell id="svc-wz" value="SAP Build Work Zone"
        style="shape=image;verticalLabelPosition=bottom;verticalAlign=top;imageAspect=0;aspect=fixed;image=data:image/svg+xml,<BASE64>;fontColor=#556B82;fontSize=10;"
        vertex="1" parent="1">
  <mxGeometry x="240" y="160" width="48" height="48" as="geometry" />
</mxCell>
```

**Hard rules** (diagrams won't render otherwise):

- `id="0"` and `id="1"` exist, first two cells, in that order; `id="1"` has `parent="0"`
- Every other cell has a `parent` pointing at an existing id
- All ids unique on a page
- Every vertex has an `<mxGeometry as="geometry">` child
- Every edge has `source`+`target` on real ids, OR `<mxPoint as="sourcePoint">` and
  `<mxPoint as="targetPoint">` in its geometry
- Escape XML in labels: `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`
- Coordinates of children of a group are **relative to the group**, not the page

Full reference: `plugins/btp-solution-diagram-generator/skills/btp-solution-diagram-generator/references/drawio-xml-schema.md`.

---

## Layout & labels

- Snap to 10px grid (x/y divisible by 10)
- ~16px whitespace around icons
- BTP subaccount is the dominant blue rounded rectangle (`arcSize=16`, `absoluteArcSize=1`)
- Non-SAP systems: grey container, outside the BTP area
- Service labels **below** the icon, 10pt, `#556B82`, Arial
- Title top-left, 16pt, bold, `#0070F2`
- ≤15 services per L2 page; split into L2a/L2b if more
- Arrow direction: caller → callee for sync flows

---

## File naming

Kebab-case with level suffix:
- `task-center-l2.drawio`
- `cap-on-cf-extension-l2.drawio`
- `s4-datasphere-data-flow-l2.drawio`

---

## Output handoff

Deliver three things:

1. The `.drawio` file at the requested path
2. A one-line summary of what it shows
3. How to open and edit it — draw.io web (`app.diagrams.net`), desktop, or the VS Code
   extension `hediet.vscode-drawio`. To add more services, `File → Open Library from → File…`
   and pick any file under `.../assets/libraries/`.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| File opens blank | Missing `id=0` / `id=1` | Add both at top of `<root>` |
| Icon renders as red X | Truncated SVG base64 | Re-copy the entire `image=data:image/svg+xml,...` blob |
| Shape in wrong place | Child of a group, page coords used | Convert to relative coords or set `parent="1"` |
| Pastel/off-brand look | draw.io defaults | Swap to Horizon palette above |
| Edges dangling after edit | Endpoint id deleted | Re-point `source`/`target` to a real id |
