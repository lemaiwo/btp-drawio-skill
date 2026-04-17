# BTP Colors and Styles (SAP Fiori Horizon)

The SAP BTP solution diagram guideline is built on the SAP Fiori Horizon design
system. Every color you pick should come from this page. Mixing Horizon with
draw.io's default palette is the #1 cause of diagrams "looking wrong" despite
having correct content.

## Table of Contents
- [Primary Colors](#primary-colors)
- [Semantic Colors](#semantic-colors)
- [Accent / Emphasized Colors](#accent--emphasized-colors)
- [Text Styles](#text-styles)
- [Spacing](#spacing)
- [Ready-to-Paste Style Strings](#ready-to-paste-style-strings)

---

## Primary Colors

The foundation. Most elements in a BTP diagram use these.

| Role | Border (strokeColor) | Fill (fillColor) | Notes |
|---|---|---|---|
| SAP / BTP area | `#0070F2` | `#EBF8FF` | The default container color for anything BTP-owned |
| Non-SAP area | `#475E75` | `#F5F6F7` | 3rd-party apps, external systems, partner landscapes |
| Title text | `#1D2D3E` | — | Fontcolor for headings and titles |
| Body text | `#556B82` | — | Fontcolor for descriptions, icon labels, notes |

Rule of thumb: If you're in doubt whether to use blue (BTP) or grey (non-SAP),
use grey. The BTP area is a specific thing, not a synonym for "SAP".

---

## Semantic Colors

Used for connector lines and status indicators. Apply sparingly — one semantic
color per flow type.

| Role | Border | Fill |
|---|---|---|
| Positive / Authentication | `#188918` | `#F5FAE5` |
| Critical / Warning | `#C35500` | `#FFF8D6` |
| Negative / Error | `#D20A0A` | `#FFEAF4` |

Don't use these for regular containers. Green fill on a box reads as "positive
status" — confusing if it's actually a service area.

---

## Accent / Emphasized Colors

For highlighting specific paths or elements that deserve attention. Over-use
drowns the diagram in color.

| Role | Border | Fill |
|---|---|---|
| Teal (emphasis, data/analytics flows) | `#07838F` | `#DAFDF5` |
| Indigo (authorization flows) | `#5D36FF` | `#F1ECFF` |
| Pink (trust flows) | `#CC00DC` | `#FFF0FA` |

The guideline specifically assigns semantic meaning to some of these:
- **Pink**: trust relationships (mutual trust, SAML federation)
- **Indigo**: authorization (scopes, role assignment)
- **Teal**: general accent, often used to highlight data pipelines

---

## Text Styles

Four styles, derived from Fiori Horizon's type scale.

| Style | Size | Weight | Color | Use |
|---|---|---|---|---|
| Diagram title | 16pt | Bold | `#0070F2` | Top-left header, e.g. "SAP Task Center – BTP Solution Diagram" |
| Section header | 14pt | Bold | `#1D2D3E` | Subsection titles inside an area |
| Area title | 12pt or 16pt | Bold | `#1D2D3E` | "SAP BTP Subaccount", "Non-SAP Systems" |
| Service label | 10pt | Regular | `#556B82` | Text below an icon |
| Body / description | 12pt | Regular | `#475E75` | Paragraph description under the title |

Font family: **Arial** or **Helvetica** (use `fontFamily=Helvetica;` in the
style — draw.io renders Helvetica as Arial on most systems).

---

## Spacing

From the guideline: "Spacing around objects should be even and roughly the
height of the SAP Logo." In practice that's ~16px on all sides of an icon.

Concrete rules:

- Service icons: **48×48** (Size M) or **24×24** (Size S)
- Whitespace between icons in the same row: **40–60px**
- Vertical whitespace between tier rows: **60–100px**
- Area inner padding: **20px**
- Canvas: **A4 landscape = 1169 × 827px** (default) or **1920 × 1080** for L3

Grid: align all coordinates to a **10px grid** (x and y divisible by 10).

---

## Ready-to-Paste Style Strings

Copy these directly into `style="..."` attributes.

### Containers / Areas

```
# SAP BTP area (primary)
rounded=1;whiteSpace=wrap;html=1;strokeColor=#0070F2;fillColor=#EBF8FF;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor=#1D2D3E;fontFamily=Helvetica;fontSize=12;fontStyle=1;verticalAlign=top;

# SAP BTP area (nested, no fill — alternate with filled parent)
rounded=1;whiteSpace=wrap;html=1;strokeColor=#0070F2;fillColor=#FFFFFF;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor=#1D2D3E;fontFamily=Helvetica;fontSize=12;fontStyle=1;verticalAlign=top;

# Non-SAP area
rounded=1;whiteSpace=wrap;html=1;strokeColor=#475E75;fillColor=#F5F6F7;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor=#1D2D3E;fontFamily=Helvetica;fontSize=12;fontStyle=1;verticalAlign=top;

# Teal accent area
rounded=1;whiteSpace=wrap;html=1;strokeColor=#07838F;fillColor=#DAFDF5;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor=#1D2D3E;fontFamily=Helvetica;fontSize=12;fontStyle=1;verticalAlign=top;

# Indigo accent area
rounded=1;whiteSpace=wrap;html=1;strokeColor=#5D36FF;fillColor=#F1ECFF;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor=#1D2D3E;fontFamily=Helvetica;fontSize=12;fontStyle=1;verticalAlign=top;

# Pink accent area
rounded=1;whiteSpace=wrap;html=1;strokeColor=#CC00DC;fillColor=#FFF0FA;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor=#1D2D3E;fontFamily=Helvetica;fontSize=12;fontStyle=1;verticalAlign=top;
```

### Stacked Area (cardinality > 1, "multiple instances")

Use a `group` containing two or three identical rounded rectangles offset by
4–6px on both axes.

### Text labels

```
# Diagram title (top of page)
text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=16;fontStyle=1;fontColor=#0070F2;fontFamily=Helvetica;

# Diagram description
text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;fontSize=12;fontColor=#475E75;fontFamily=Helvetica;

# Area/group title (inside a container)
text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=12;fontStyle=1;fontColor=#1D2D3E;fontFamily=Helvetica;

# Service label below an icon
text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=10;fontColor=#556B82;fontFamily=Helvetica;
```

### Legend box

```
rounded=0;whiteSpace=wrap;html=1;strokeColor=#eaecee;strokeWidth=1.5;fillColor=#FFFFFF;arcSize=16;absoluteArcSize=1;
```

### Small annotation dots (used in legends)

```
# Green (authentication)
ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#188918;

# Indigo (authorization)
ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#5D36FF;

# Pink (trust)
ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#CC00DC;

# Grey (access/service)
ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#475E75;
```

### Connector templates

See `btp-connectors-and-annotations.md` for the complete list.

```
# Standard solid arrow (synchronous flow)
endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;

# Dashed arrow (asynchronous)
endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;dashed=1;

# Dotted arrow (optional)
endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;dashed=1;dashPattern=1 4;

# Authentication (green, solid)
endArrow=blockThin;html=1;strokeColor=#188918;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;

# Trust (pink, bi-directional, dashed)
endArrow=blockThin;startArrow=blockThin;html=1;strokeColor=#CC00DC;strokeWidth=1.5;rounded=0;endFill=1;startFill=1;endSize=4;startSize=4;dashed=1;

# Firewall (thick grey bar, often no arrow)
endArrow=none;startArrow=none;html=1;strokeColor=#475E75;strokeWidth=4;rounded=0;
```

---

## Why the palette matters

SAP architects recognize the Horizon palette on sight. A diagram that uses
`#dae8fc` (draw.io's default pale blue) instead of `#EBF8FF` reads as
"cobbled together", even if the architecture is correct. The hex values in
this file are the single most important thing to copy verbatim.
