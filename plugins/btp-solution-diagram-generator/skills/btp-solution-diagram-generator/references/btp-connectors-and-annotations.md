# Connectors, Annotations, and Interfaces

Connectors carry most of the meaning in a solution diagram. BTP's guideline
standardizes their semantics so diagrams read consistently across teams.

## Connector Meaning Matrix

| Flow type | Direction | Line style | Color | Notes |
|---|---|---|---|---|
| Direct synchronous data flow (request/response) | One-way | Solid | `#475E75` (grey) or `#0070F2` (blue) | The default. Use grey unless the flow stays entirely within BTP |
| Asynchronous data flow (events, queues) | One-way | **Dashed** | `#475E75` | `dashed=1;` |
| Optional data flow | One-way | **Dotted** | `#475E75` | `dashed=1;dashPattern=1 4;` |
| Mutual trust | Bidirectional | Solid | `#CC00DC` (pink) | Both ends are `blockThin` |
| Authentication | One-way | Solid | `#188918` (green) | From user/actor to IdP |
| Authorization (scope/role) | One-way | Solid | `#5D36FF` (indigo) | From IdP to service |
| Provisioning | One-way | Solid | violet (custom, e.g. `#7F00FF`) | User/role provisioning flows |
| Firewall / network boundary | No arrow | **Thick** (4px) | `#475E75` | `strokeWidth=4;` |

## Arrow Head Style

Always use `blockThin` for arrow heads in BTP diagrams — it's the Horizon
standard. Don't use `block`, `open`, or `classic`.

```
endArrow=blockThin;endFill=1;endSize=4;
```

For bidirectional:
```
endArrow=blockThin;startArrow=blockThin;endFill=1;startFill=1;endSize=4;startSize=4;
```

## Style Strings (copy-paste)

### Synchronous (solid, one-way)
```
endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;
```

### Asynchronous (dashed, one-way)
```
endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;dashed=1;
```

### Optional (dotted, one-way)
```
endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;dashed=1;dashPattern=1 4;
```

### Mutual trust (solid, bi-directional, pink)
```
endArrow=blockThin;startArrow=blockThin;html=1;strokeColor=#CC00DC;strokeWidth=1.5;rounded=0;endFill=1;startFill=1;endSize=4;startSize=4;
```

### Authentication (solid, one-way, green)
```
endArrow=blockThin;html=1;strokeColor=#188918;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;
```

### Authorization (solid, one-way, indigo)
```
endArrow=blockThin;html=1;strokeColor=#5D36FF;strokeWidth=1.5;rounded=0;endFill=1;endSize=4;
```

### Firewall (thick bar, no arrow heads)
```
endArrow=none;startArrow=none;html=1;strokeColor=#475E75;strokeWidth=4;rounded=0;
```

### Edge connecting to a specific side of a shape

Add `entryX`, `entryY`, `exitX`, `exitY` — values between 0 and 1:

```
endArrow=blockThin;html=1;strokeColor=#475E75;strokeWidth=1.5;endFill=1;endSize=4;
exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;
```
(Here the edge exits the right-center of the source and enters the left-center
of the target.)

---

## Annotations

Annotations explain what a line represents. Two patterns:

### 1. Semantic dot on the line
A small colored circle placed on the line indicating its type (green =
authentication, indigo = authorization, pink = trust).

```xml
<mxCell id="anno-auth" value=""
        style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#188918;"
        vertex="1" parent="1">
  <mxGeometry x="430" y="240" width="12" height="12" as="geometry" />
</mxCell>
```

### 2. Label on the line
Draw.io supports edge labels via the `value` attribute on the edge itself — the
label appears mid-line. Keep it short (≤ 3 words).

```xml
<mxCell id="edge-1" value="OAuth2"
        style="endArrow=blockThin;html=1;strokeColor=#188918;strokeWidth=1.5;endFill=1;endSize=4;fontSize=10;fontColor=#1D2D3E;"
        edge="1" source="svc-user" target="svc-ias" parent="1">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

---

## Firewalls

Firewalls are **thick grey lines** (not rectangles with "firewall" inside).
They sit between two areas to indicate a network boundary.

```xml
<!-- Horizontal firewall bar between user zone and BTP -->
<mxCell id="fw-1" value=""
        style="endArrow=none;startArrow=none;html=1;strokeColor=#475E75;strokeWidth=4;rounded=0;"
        edge="1" parent="1">
  <mxGeometry relative="1" as="geometry">
    <mxPoint x="100" y="250" as="sourcePoint" />
    <mxPoint x="900" y="250" as="targetPoint" />
  </mxGeometry>
</mxCell>
```

Add a small "firewall" label next to it if needed, using a text cell.

---

## Interfaces

Interfaces are small labeled circles or half-circles on the edge of a
container, indicating the protocol/API the container exposes.

```xml
<!-- Half-circle showing an OData/REST interface on the right side of a service -->
<mxCell id="iface-1" value="REST"
        style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#475E75;strokeWidth=1.5;fontSize=9;fontColor=#1D2D3E;"
        vertex="1" parent="1">
  <mxGeometry x="580" y="344" width="24" height="24" as="geometry" />
</mxCell>
```

---

## Numbered Paths

To show order of a process, number the steps along the connectors. Use a small
white-fill circle with a black/dark number inside, placed at the midpoint.

```xml
<mxCell id="num-1" value="1"
        style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFFFFF;strokeColor=#475E75;strokeWidth=1.5;fontSize=11;fontColor=#1D2D3E;fontStyle=1;"
        vertex="1" parent="1">
  <mxGeometry x="320" y="200" width="20" height="20" as="geometry" />
</mxCell>
```

Keep numbers 1-based. If you have a complex branch, use sub-numbers (1a, 1b).

---

## Common Mistakes

| Mistake | Why it's wrong | Fix |
|---|---|---|
| Red line for "data flow" | Red = negative/error in Horizon | Use grey `#475E75` for data flows; reserve red for error paths |
| Green for all outgoing arrows | Green means authentication specifically | Use grey; only use green for actual auth flows |
| Dashed = "optional" | In BTP semantics, dashed = asynchronous | Use dotted (`dashPattern=1 4`) for optional |
| Thin line for firewall | Reads as a regular connector | Use `strokeWidth=4` |
| Bidirectional arrow for normal request/response | A request-response is still one direction (you get a reply, not a peer) | Use one-way; only bi-directional for mutual trust/sync |
