# draw.io (mxGraph) XML Schema Reference

This reference covers the essentials needed to hand-author valid `.drawio` XML
for BTP solution diagrams. For the full mxGraph spec see
[jgraph/mxgraph](https://github.com/jgraph/mxgraph).

## Document Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="Electron" modified="2026-04-17T00:00:00.000Z" agent="..." version="27.0.0">
  <diagram id="page-1" name="Page-1">
    <mxGraphModel ...>
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- your cells -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## mxfile

The root element.

| Attribute | Meaning |
|---|---|
| `host` | Free-form — "Electron", "app.diagrams.net", etc. Not used by the renderer |
| `modified` | ISO 8601 timestamp (optional) |
| `version` | draw.io version string (optional) |

## diagram

One page of the file. A file can contain multiple pages.

| Attribute | Meaning |
|---|---|
| `id` | Unique page id (any string, not required to be a number) |
| `name` | Tab label shown in draw.io |

## mxGraphModel

The page's canvas settings.

| Attribute | Typical value | Meaning |
|---|---|---|
| `dx`, `dy` | `1422`, `762` | Initial scroll offset |
| `grid` | `1` | Show grid |
| `gridSize` | `10` | Grid spacing (10px is standard for BTP) |
| `guides` | `1` | Show alignment guides |
| `tooltips` | `1` | Show tooltips |
| `connect` | `1` | Allow creating edges by dragging |
| `arrows` | `1` | Show edge arrows by default |
| `fold` | `1` | Allow collapsing groups |
| `page` | `1` | Show page boundary |
| `pageScale` | `1` | Page scale factor |
| `pageWidth` | `1169` | A4 landscape default |
| `pageHeight` | `827` | A4 landscape default |
| `math` | `0` | Enable MathJax rendering |
| `shadow` | `0` | Global shadow effect |
| `background` | `none` | Page background color |

For BTP solution diagrams, the A4 landscape default (1169×827) is almost always
correct. For dense L3 diagrams, bump to 1920×1080.

## root

Container for all `mxCell` elements. No attributes needed.

## mxCell — Reserved Cells

The first two cells must exist, in this order:

```xml
<mxCell id="0" />                    <!-- page root -->
<mxCell id="1" parent="0" />         <!-- default layer -->
```

Everything else lives under id `1` (or a group/container cell that itself
parents to `1`). **Never reuse ids `0` and `1` for other cells**.

## mxCell — Vertex (Shape)

Any shape on the canvas.

```xml
<mxCell id="svc-1"
        value="SAP Build Work Zone"
        style="shape=image;image=data:image/svg+xml,...;verticalLabelPosition=bottom;verticalAlign=top;fontColor=#556B82;fontSize=10;"
        vertex="1"
        parent="1">
  <mxGeometry x="100" y="200" width="48" height="48" as="geometry" />
</mxCell>
```

| Attribute | Required | Meaning |
|---|---|---|
| `id` | yes | Globally unique within the diagram page |
| `value` | no | Label (HTML if `html=1` is in the style, else plain) |
| `style` | no | Semi-colon separated key=value pairs (see style reference) |
| `vertex="1"` | yes | Marks this as a shape |
| `parent` | yes | Id of parent cell. `1` for top-level; another cell id to nest |

Inside the vertex, an `mxGeometry` child is **required**:
```xml
<mxGeometry x="100" y="200" width="48" height="48" as="geometry" />
```

Coordinates: `x`, `y` are the top-left corner of the shape. If the vertex's
parent is not `1`, they are **relative to the parent**, not the page.

## mxCell — Edge (Connector)

A line between two shapes.

```xml
<mxCell id="edge-1"
        value=""
        style="endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;endFill=1;endSize=4;"
        edge="1"
        source="svc-1"
        target="svc-2"
        parent="1">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

| Attribute | Required | Meaning |
|---|---|---|
| `id` | yes | Unique id |
| `edge="1"` | yes | Marks this as an edge |
| `source` | one of source/sourcePoint | Id of the source vertex |
| `target` | one of target/targetPoint | Id of the target vertex |
| `parent` | yes | Usually `1` |
| `value` | no | Label text (appears mid-line) |
| `style` | no | Edge styling |

### Floating Edges

An edge can "float" — its source or target is a fixed point on the canvas
instead of a vertex. Use this for:
- Firewalls (a bar between two areas, not between two vertices)
- Sequence-diagram-style lifelines
- Any line that shouldn't move when vertices move

```xml
<mxCell id="fw-1" value=""
        style="endArrow=none;startArrow=none;html=1;strokeColor=#475E75;strokeWidth=4;"
        edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="100" y="300" as="sourcePoint" />
    <mxPoint x="900" y="300" as="targetPoint" />
  </mxGeometry>
</mxCell>
```

### Edge Waypoints

For an edge that bends at specific points:

```xml
<mxGeometry relative="1" as="geometry">
  <Array as="points">
    <mxPoint x="400" y="200" />
    <mxPoint x="400" y="400" />
  </Array>
</mxGeometry>
```

## mxCell — Group

A group is a vertex whose children move with it. Use groups to bundle
several shapes into a single moveable object.

```xml
<mxCell id="group-btp" value="" style="group" vertex="1" connectable="0" parent="1">
  <mxGeometry x="100" y="100" width="400" height="300" as="geometry" />
</mxCell>
<!-- children of the group -->
<mxCell id="svc-a" value="..." style="..." vertex="1" parent="group-btp">
  <mxGeometry x="20" y="40" width="48" height="48" as="geometry" />  <!-- coords relative to group -->
</mxCell>
```

`connectable="0"` on the group itself prevents users from accidentally
attaching edges to the group rectangle.

## Coordinate System

- Origin is **top-left** of the page
- x increases rightward, y increases downward (standard screen coordinates)
- For a **nested** vertex (parent is not id `1`), x/y are relative to the parent
- For an **edge**, x/y in mxGeometry are ignored when source/target are set
- Page size (default A4 landscape): `0, 0` to `1169, 827`

## Common Style Keys

All style values go in the `style` attribute as `key=value;key=value;...`.

### Shape type
- `rounded=1` — rounded rectangle
- `ellipse` — ellipse
- `rhombus` — diamond
- `shape=image;image=<url-or-data-uri>` — SVG/PNG image (BTP icons use this)
- `swimlane` — container with a header
- `group` — moveable group container
- `text` — pure text cell (no fill/stroke)

### Fill and stroke
- `fillColor=#EBF8FF`
- `strokeColor=#0070F2`
- `strokeWidth=1.5`
- `fillColor=none` or `strokeColor=none` to disable

### Rounded corners
- `arcSize=16` — corner radius
- `absoluteArcSize=1` — interpret arcSize as pixels (otherwise it's a percent)

### Text
- `html=1` — render `<b>`, `<i>`, `<br>` in labels
- `fontColor=#1D2D3E`
- `fontSize=12`
- `fontStyle=1` (bold), `=2` (italic), `=3` (bold+italic), `=4` (underline)
- `fontFamily=Helvetica`
- `align=left|center|right`
- `verticalAlign=top|middle|bottom`
- `whiteSpace=wrap` — wrap long labels
- `labelBackgroundColor=none`

### Geometry / layout
- `verticalLabelPosition=bottom` — label under the shape (used for icons)
- `imageAspect=0` — image can stretch
- `aspect=fixed` — shape maintains its aspect ratio

### Arrows (edges only)
- `endArrow=blockThin|block|classic|open|none`
- `startArrow=...` (default `none`)
- `endFill=0|1` — filled or hollow arrow head
- `endSize=4` — arrow size in pixels
- `dashed=1` — dashed line
- `dashPattern=1 4` — pattern for dashed lines (dotted: `1 4`)
- `rounded=0|1` — rounded corners on orthogonal edges

### Connection points
- `exitX=0..1`, `exitY=0..1` — where the edge leaves the source (normalized)
- `entryX=0..1`, `entryY=0..1` — where it enters the target
- `exitPerimeter=0|1`, `entryPerimeter=0|1`

## Validation Rules

A file that violates any of these will fail to render or will render incorrectly:

1. Every diagram page must contain `<mxCell id="0" />` as the **first** cell
2. Every diagram page must contain `<mxCell id="1" parent="0" />` as the **second** cell
3. Every other cell must have a `parent` attribute referencing an existing cell id
4. Cell ids must be unique **within a diagram page** (ids can be reused across pages)
5. Vertex cells (`vertex="1"`) must have `<mxGeometry as="geometry">` as a direct child
6. Edge cells (`edge="1"`) must have **either**:
   - `source` AND `target` attributes pointing to existing vertex ids, OR
   - `<mxPoint as="sourcePoint">` AND `<mxPoint as="targetPoint">` inside the `<mxGeometry>`
7. XML special characters in labels must be escaped: `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`
8. If a label contains HTML, the style must include `html=1`

Run `scripts/validate_drawio.py` to catch all of these automatically.

## Compressed Diagrams

Older draw.io versions sometimes save diagrams base64-encoded and deflate-compressed
inside `<diagram>`. These look like:

```xml
<diagram id="..." name="...">
  xV1bc5s4FP4teez...  <!-- base64 gibberish -->
</diagram>
```

The validator and generator assume **uncompressed** diagrams. If you encounter
a compressed file, open it in draw.io and `File → Export → XML (uncompressed)`.

## Multi-page Files

Add multiple `<diagram>` elements for complex architectures:

```xml
<mxfile>
  <diagram id="overview" name="Overview">
    <mxGraphModel>...</mxGraphModel>
  </diagram>
  <diagram id="l3" name="L3 Detail">
    <mxGraphModel>...</mxGraphModel>
  </diagram>
</mxfile>
```

Each page has its own cell id namespace — the same id can appear on different
pages without conflict.
