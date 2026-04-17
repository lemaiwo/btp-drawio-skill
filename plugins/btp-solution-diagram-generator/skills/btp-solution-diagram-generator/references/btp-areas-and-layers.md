# Areas, Layers, and Nesting

Areas group related components. The BTP guideline is specific about how to
color them, how to nest them, and how to show cardinality (multiple instances).

## Area Types

| Type | Border | Fill | Used for |
|---|---|---|---|
| **SAP BTP L0 (primary)** | `#0070F2` | `#EBF8FF` | The BTP subaccount or global BTP area |
| **Non-SAP L0** | `#475E75` | `#F5F6F7` | 3rd-party systems, partner apps, external IdPs |
| **Teal accent** | `#07838F` | `#DAFDF5` | Data/analytics pipelines, emphasis |
| **Indigo accent** | `#5D36FF` | `#F1ECFF` | Authorization paths |
| **Pink accent** | `#CC00DC` | `#FFF0FA` | Trust domains |

Proportions: The BTP area should visually dominate (60–70% of the diagram
area). Accent colors should cover < 10% combined.

**Corner radius: 16px** (`arcSize=16;absoluteArcSize=1;`) for all area rectangles.
This is specified in the guideline — don't use square corners for areas.

---

## Nesting Rules

When you nest areas inside each other (e.g. a runtime area inside the BTP
subaccount), **alternate fill and no-fill** to create contrast:

```
BTP subaccount (filled #EBF8FF)
└── Cloud Foundry runtime (no fill, same blue outline)
    └── Space / app area (filled #EBF8FF again)
```

If two adjacent nested areas both have fill, they blend together and the reader
can't tell where one ends and the next begins.

**XML pattern** (parent area with filled child, inner child with no fill):

```xml
<!-- Parent: BTP subaccount with fill -->
<mxCell id="btp-sub" value="SAP BTP Subaccount"
        style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#0070F2;fillColor=#EBF8FF;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor=#1D2D3E;fontSize=12;fontStyle=1;verticalAlign=top;fontFamily=Helvetica;"
        vertex="1" parent="1">
  <mxGeometry x="60" y="100" width="800" height="500" as="geometry" />
</mxCell>

<!-- Child: Cloud Foundry runtime, NO fill, same blue outline -->
<mxCell id="cf-runtime" value="Cloud Foundry Runtime"
        style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#0070F2;fillColor=#FFFFFF;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor=#1D2D3E;fontSize=12;fontStyle=1;verticalAlign=top;fontFamily=Helvetica;"
        vertex="1" parent="btp-sub">
  <mxGeometry x="40" y="60" width="400" height="300" as="geometry" />
</mxCell>
```

Note `parent="btp-sub"` makes the runtime's coordinates **relative to the
subaccount**, not the page.

---

## Cardinality (Stacked Areas)

To show "multiple instances of this area" (multiple subaccounts, multiple
spaces), stack 2–3 offset rectangles:

```xml
<!-- Back card (shifted down and right) -->
<mxCell id="sub-back" value=""
        style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#0070F2;fillColor=#EBF8FF;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;"
        vertex="1" parent="1">
  <mxGeometry x="68" y="108" width="800" height="500" as="geometry" />
</mxCell>

<!-- Middle card -->
<mxCell id="sub-mid" value=""
        style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#0070F2;fillColor=#EBF8FF;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;"
        vertex="1" parent="1">
  <mxGeometry x="64" y="104" width="800" height="500" as="geometry" />
</mxCell>

<!-- Front card (the primary, labeled one) -->
<mxCell id="sub-front" value="Subaccount"
        style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#0070F2;fillColor=#EBF8FF;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor=#1D2D3E;fontSize=12;fontStyle=1;verticalAlign=top;"
        vertex="1" parent="1">
  <mxGeometry x="60" y="100" width="800" height="500" as="geometry" />
</mxCell>
```

Offset the back cards by 4–6px in x and y. Only the front card carries the
label and contains the child services.

---

## Typical Layer Hierarchy

For an L2 solution diagram, the typical nesting is:

```
Diagram (page)
├── Title + description (top-left)
├── Legend (top-right)
├── SAP BTP Subaccount  [blue, filled]
│   ├── Runtime area (Cloud Foundry / Kyma / ABAP) [blue, no fill]
│   │   └── Services (individual icons inside)
│   ├── Platform services area (optional) [blue, no fill]
│   │   └── Icons for Destination, Connectivity, Identity, etc.
│   └── Business services area (optional) [blue, no fill]
│       └── Icons for Build Work Zone, Task Center, etc.
├── SAP On-Premise area [blue-outline, no fill — it's SAP but NOT BTP]
│   └── S/4HANA icon + label
├── Non-SAP area [grey]
│   └── 3rd-party apps, external IdPs
└── User / Actor (outside all areas, top corner)
```

The runtime layer and the platform/business service layers are optional — use
them when you have enough services to warrant the grouping. For a small
diagram (< 8 services), just put everything directly in the subaccount.

---

## When NOT to Nest

If two areas are logically peers (e.g. two separate subaccounts, or BTP vs
partner system), **don't nest them**. Put them side by side. Nesting implies
containment, which implies one is "inside" the other.

Good: BTP subaccount + partner system, side by side.
Bad: Partner system nested inside the BTP subaccount area.
