#!/usr/bin/env python3
"""
generate_btp_diagram.py — Scaffold a new BTP solution diagram (.drawio file)
with the required header, legend, BTP subaccount area, and a placeholder for
services. Output follows the SAP BTP Solution Diagram Guidelines.

Usage:
    python scripts/generate_btp_diagram.py <output.drawio> \
        --title "SAP Task Center" \
        --description "Access to tasks across SAP systems via BTP." \
        --level L2

Options:
    --title TEXT           Diagram title (required)
    --description TEXT     1–3 line description shown under the title
    --level {L0,L1,L2,L3}  Diagram level (default L2)
    --page {A4,1080p}      Page size: A4 landscape (1169x827) or 1080p (1920x1080). Default A4
    --type {solution,process-flow,data-flow}  Base template type (default solution)

The resulting file is a valid, BTP-styled skeleton. Add service icons by
dragging them from the imported SAP BTP icon library, or by copying cells
from the library XML.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path


# ---------- Horizon palette shortcuts ----------
C_BTP_STROKE = "#0070F2"
C_BTP_FILL = "#EBF8FF"
C_NONSAP_STROKE = "#475E75"
C_NONSAP_FILL = "#F5F6F7"
C_TITLE = "#1D2D3E"
C_BODY = "#556B82"
C_LEGEND_BORDER = "#eaecee"

# ---------- Style building blocks ----------
S_TITLE = f"text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=16;fontStyle=1;fontColor={C_BTP_STROKE};fontFamily=Helvetica;"
S_DESC = f"text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=top;fontSize=12;fontColor={C_BODY};fontFamily=Helvetica;"
S_LEVEL = f"text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=12;fontStyle=1;fontColor={C_TITLE};fontFamily=Helvetica;"
S_BTP_AREA = f"rounded=1;whiteSpace=wrap;html=1;strokeColor={C_BTP_STROKE};fillColor={C_BTP_FILL};strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor={C_TITLE};fontFamily=Helvetica;fontSize=14;fontStyle=1;verticalAlign=top;"
S_NONSAP_AREA = f"rounded=1;whiteSpace=wrap;html=1;strokeColor={C_NONSAP_STROKE};fillColor={C_NONSAP_FILL};strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor={C_TITLE};fontFamily=Helvetica;fontSize=14;fontStyle=1;verticalAlign=top;"
S_RUNTIME_AREA = f"rounded=1;whiteSpace=wrap;html=1;strokeColor={C_BTP_STROKE};fillColor=#FFFFFF;strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor={C_TITLE};fontFamily=Helvetica;fontSize=12;fontStyle=1;verticalAlign=top;"
S_LEGEND_BOX = f"rounded=0;whiteSpace=wrap;html=1;strokeColor={C_LEGEND_BORDER};strokeWidth=1.5;fillColor=#FFFFFF;arcSize=16;absoluteArcSize=1;"
S_LEGEND_TITLE = f"text;html=1;strokeColor=none;fillColor=none;fontSize=12;fontStyle=1;fontColor={C_TITLE};fontFamily=Helvetica;align=left;verticalAlign=top;"
S_LEGEND_LABEL = f"text;html=1;strokeColor=none;fillColor=none;fontSize=10;fontColor={C_TITLE};fontFamily=Helvetica;align=left;verticalAlign=middle;"

S_DOT_ACCESS = f"ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor={C_NONSAP_STROKE};"
S_DOT_AUTH = "ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#188918;"
S_DOT_AUTHZ = "ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#5D36FF;"
S_DOT_TRUST = "ellipse;whiteSpace=wrap;html=1;aspect=fixed;strokeColor=none;fillColor=#CC00DC;"

S_ARROW_SYNC = f"endArrow=blockThin;html=1;strokeColor={C_NONSAP_STROKE};strokeWidth=1.5;rounded=0;endFill=1;endSize=4;"
S_ARROW_DASH = f"endArrow=blockThin;html=1;strokeColor={C_NONSAP_STROKE};strokeWidth=1.5;rounded=0;endFill=1;endSize=4;dashed=1;"
S_ARROW_DOT = f"endArrow=blockThin;html=1;strokeColor={C_NONSAP_STROKE};strokeWidth=1.5;rounded=0;endFill=1;endSize=4;dashed=1;dashPattern=1 4;"
S_ARROW_TRUST = "endArrow=blockThin;startArrow=blockThin;html=1;strokeColor=#CC00DC;strokeWidth=1.5;rounded=0;endFill=1;startFill=1;endSize=4;startSize=4;"


def _esc(s: str) -> str:
    """Escape for XML text/attribute content."""
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def build_solution_diagram(title: str, description: str, level: str, page_w: int, page_h: int) -> str:
    """Return the XML string for an L2-style solution diagram skeleton."""
    ts = _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

    # Geometry constants (A4 landscape layout)
    title_y = 20
    btp_x, btp_y, btp_w, btp_h = 40, 130, int(page_w * 0.55), int(page_h * 0.72)
    nonsap_x = btp_x + btp_w + 40
    nonsap_w = page_w - nonsap_x - 40
    nonsap_h = int(page_h * 0.35)
    nonsap_y = btp_y
    # Legend top-right
    leg_w, leg_h = 240, 110
    leg_x = page_w - leg_w - 30
    leg_y = title_y + 0

    # Runtime area inside BTP subaccount
    rt_x, rt_y = 30, 50
    rt_w, rt_h = btp_w - 60, int(btp_h * 0.4)

    cells = []

    def add(cell_xml: str) -> None:
        cells.append(cell_xml)

    # Mandatory root cells
    add('<mxCell id="0" />')
    add('<mxCell id="1" parent="0" />')

    # Title
    add(
        f'<mxCell id="t-title" value="{_esc(title)} - SAP BTP Solution Diagram" '
        f'style="{S_TITLE}" vertex="1" parent="1">'
        f'<mxGeometry x="30" y="{title_y}" width="800" height="30" as="geometry" />'
        f"</mxCell>"
    )
    # Description
    if description:
        add(
            f'<mxCell id="t-desc" value="{_esc(description)}" '
            f'style="{S_DESC}" vertex="1" parent="1">'
            f'<mxGeometry x="30" y="{title_y + 30}" width="800" height="40" as="geometry" />'
            f"</mxCell>"
        )
    # Level label
    add(
        f'<mxCell id="t-level" value="Diagram Level: {_esc(level)}" '
        f'style="{S_LEVEL}" vertex="1" parent="1">'
        f'<mxGeometry x="30" y="{title_y + 70}" width="300" height="24" as="geometry" />'
        f"</mxCell>"
    )

    # BTP subaccount area
    add(
        f'<mxCell id="a-btp" value="SAP BTP Subaccount" '
        f'style="{S_BTP_AREA}" vertex="1" parent="1">'
        f'<mxGeometry x="{btp_x}" y="{btp_y}" width="{btp_w}" height="{btp_h}" as="geometry" />'
        f"</mxCell>"
    )
    # Runtime area nested inside BTP
    add(
        f'<mxCell id="a-runtime" value="Cloud Foundry Runtime" '
        f'style="{S_RUNTIME_AREA}" vertex="1" parent="a-btp">'
        f'<mxGeometry x="{rt_x}" y="{rt_y}" width="{rt_w}" height="{rt_h}" as="geometry" />'
        f"</mxCell>"
    )
    # Placeholder note inside BTP area
    add(
        f'<mxCell id="a-btp-note" value="[drag SAP BTP service icons here — see references/btp-icons.md]" '
        f'style="{S_DESC}" vertex="1" parent="a-btp">'
        f'<mxGeometry x="30" y="{rt_y + rt_h + 20}" width="{rt_w}" height="40" as="geometry" />'
        f"</mxCell>"
    )

    # Non-SAP area
    add(
        f'<mxCell id="a-nonsap" value="Non-SAP Systems" '
        f'style="{S_NONSAP_AREA}" vertex="1" parent="1">'
        f'<mxGeometry x="{nonsap_x}" y="{nonsap_y}" width="{nonsap_w}" height="{nonsap_h}" as="geometry" />'
        f"</mxCell>"
    )
    add(
        f'<mxCell id="a-nonsap-note" value="[external IdP / 3rd-party apps]" '
        f'style="{S_DESC}" vertex="1" parent="a-nonsap">'
        f'<mxGeometry x="20" y="40" width="{nonsap_w - 40}" height="30" as="geometry" />'
        f"</mxCell>"
    )

    # Legend box
    add(
        f'<mxCell id="leg-box" value="" '
        f'style="{S_LEGEND_BOX}" vertex="1" parent="1">'
        f'<mxGeometry x="{leg_x}" y="{leg_y}" width="{leg_w}" height="{leg_h}" as="geometry" />'
        f"</mxCell>"
    )
    add(
        f'<mxCell id="leg-title" value="Legend" style="{S_LEGEND_TITLE}" vertex="1" parent="1">'
        f'<mxGeometry x="{leg_x + 10}" y="{leg_y + 5}" width="60" height="20" as="geometry" />'
        f"</mxCell>"
    )
    # Legend entries: dot + label
    leg_entries = [
        (S_DOT_ACCESS, "Access"),
        (S_DOT_AUTH, "Authentication"),
        (S_DOT_AUTHZ, "Authorization"),
        (S_DOT_TRUST, "Trust"),
    ]
    for i, (dot_style, lab) in enumerate(leg_entries):
        dy = leg_y + 28 + i * 18
        add(
            f'<mxCell id="leg-dot-{i}" value="" style="{dot_style}" vertex="1" parent="1">'
            f'<mxGeometry x="{leg_x + 14}" y="{dy}" width="12" height="12" as="geometry" />'
            f"</mxCell>"
        )
        add(
            f'<mxCell id="leg-lab-{i}" value="{lab}" style="{S_LEGEND_LABEL}" vertex="1" parent="1">'
            f'<mxGeometry x="{leg_x + 34}" y="{dy - 4}" width="140" height="20" as="geometry" />'
            f"</mxCell>"
        )

    # Compose the file
    inner = "\n        ".join(cells)
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="cowork-btp-skill" modified="{ts}" version="27.0.0">
  <diagram id="p1" name="{_esc(title)}">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" math="0" shadow="0" background="none">
      <root>
        {inner}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""
    return xml


def build_process_flow(title: str, description: str, level: str, page_w: int, page_h: int) -> str:
    """Generate a simple numbered process-flow diagram skeleton."""
    ts = _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    cells = ['<mxCell id="0" />', '<mxCell id="1" parent="0" />']

    # Title + description + level
    cells.append(
        f'<mxCell id="t-title" value="{_esc(title)} - BTP Process Flow" '
        f'style="{S_TITLE}" vertex="1" parent="1"><mxGeometry x="30" y="20" width="900" height="30" as="geometry" /></mxCell>'
    )
    if description:
        cells.append(
            f'<mxCell id="t-desc" value="{_esc(description)}" style="{S_DESC}" vertex="1" parent="1">'
            f'<mxGeometry x="30" y="50" width="900" height="40" as="geometry" /></mxCell>'
        )
    cells.append(
        f'<mxCell id="t-level" value="Diagram Level: {_esc(level)}" style="{S_LEVEL}" vertex="1" parent="1">'
        f'<mxGeometry x="30" y="90" width="300" height="24" as="geometry" /></mxCell>'
    )

    # 4 process steps in a row + arrows between them
    y = 260
    step_w, step_h, gap = 200, 100, 40
    x0 = 60
    prev_id = None
    for i, label in enumerate(["Step 1", "Step 2", "Step 3", "Step 4"], start=1):
        x = x0 + (i - 1) * (step_w + gap)
        cid = f"step-{i}"
        cells.append(
            f'<mxCell id="{cid}" value="{label}" '
            f'style="rounded=1;whiteSpace=wrap;html=1;strokeColor={C_BTP_STROKE};fillColor={C_BTP_FILL};'
            f'strokeWidth=1.5;arcSize=16;absoluteArcSize=1;fontColor={C_TITLE};fontSize=12;fontFamily=Helvetica;" '
            f'vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="{step_w}" height="{step_h}" as="geometry" />'
            f"</mxCell>"
        )
        # Number badge at top-left of each step
        cells.append(
            f'<mxCell id="num-{i}" value="{i}" '
            f'style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFFFFF;strokeColor={C_NONSAP_STROKE};'
            f'strokeWidth=1.5;fontSize=11;fontStyle=1;fontColor={C_TITLE};" vertex="1" parent="1">'
            f'<mxGeometry x="{x - 10}" y="{y - 10}" width="22" height="22" as="geometry" />'
            f"</mxCell>"
        )
        if prev_id is not None:
            cells.append(
                f'<mxCell id="e-{i}" value="" style="{S_ARROW_SYNC}" edge="1" '
                f'source="{prev_id}" target="{cid}" parent="1">'
                f'<mxGeometry relative="1" as="geometry" /></mxCell>'
            )
        prev_id = cid

    inner = "\n        ".join(cells)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="cowork-btp-skill" modified="{ts}" version="27.0.0">
  <diagram id="p1" name="{_esc(title)}">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" math="0" shadow="0" background="none">
      <root>
        {inner}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""


def build_data_flow(title: str, description: str, level: str, page_w: int, page_h: int) -> str:
    """Generate a simple two-side data-flow diagram skeleton."""
    ts = _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    cells = ['<mxCell id="0" />', '<mxCell id="1" parent="0" />']
    cells.append(
        f'<mxCell id="t-title" value="{_esc(title)} - BTP Data Flow" '
        f'style="{S_TITLE}" vertex="1" parent="1"><mxGeometry x="30" y="20" width="900" height="30" as="geometry" /></mxCell>'
    )
    if description:
        cells.append(
            f'<mxCell id="t-desc" value="{_esc(description)}" style="{S_DESC}" vertex="1" parent="1">'
            f'<mxGeometry x="30" y="50" width="900" height="40" as="geometry" /></mxCell>'
        )
    cells.append(
        f'<mxCell id="t-level" value="Diagram Level: {_esc(level)}" style="{S_LEVEL}" vertex="1" parent="1">'
        f'<mxGeometry x="30" y="90" width="300" height="24" as="geometry" /></mxCell>'
    )

    # Left: source area (non-SAP or SAP on-prem)
    cells.append(
        f'<mxCell id="a-src" value="Source System" style="{S_NONSAP_AREA}" vertex="1" parent="1">'
        f'<mxGeometry x="50" y="160" width="300" height="380" as="geometry" /></mxCell>'
    )
    # Middle: BTP area
    cells.append(
        f'<mxCell id="a-btp" value="SAP BTP" style="{S_BTP_AREA}" vertex="1" parent="1">'
        f'<mxGeometry x="420" y="160" width="340" height="380" as="geometry" /></mxCell>'
    )
    # Right: target area
    cells.append(
        f'<mxCell id="a-tgt" value="Target System" style="{S_NONSAP_AREA}" vertex="1" parent="1">'
        f'<mxGeometry x="830" y="160" width="300" height="380" as="geometry" /></mxCell>'
    )
    # Two flows: source -> BTP (solid), BTP -> target (dashed async)
    cells.append(
        f'<mxCell id="flow-1" value="extract" style="{S_ARROW_SYNC}fontSize=10;fontColor={C_TITLE};" edge="1" source="a-src" target="a-btp" parent="1">'
        f'<mxGeometry relative="1" as="geometry" /></mxCell>'
    )
    cells.append(
        f'<mxCell id="flow-2" value="publish (async)" style="{S_ARROW_DASH}fontSize=10;fontColor={C_TITLE};" edge="1" source="a-btp" target="a-tgt" parent="1">'
        f'<mxGeometry relative="1" as="geometry" /></mxCell>'
    )

    inner = "\n        ".join(cells)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="cowork-btp-skill" modified="{ts}" version="27.0.0">
  <diagram id="p1" name="{_esc(title)}">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" math="0" shadow="0" background="none">
      <root>
        {inner}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a BTP-styled .drawio diagram.")
    parser.add_argument("output", help="Path to write the .drawio file")
    parser.add_argument("--title", required=True, help="Diagram title")
    parser.add_argument("--description", default="", help="Short description (1-3 lines)")
    parser.add_argument("--level", choices=["L0", "L1", "L2", "L3"], default="L2", help="Diagram level (default L2)")
    parser.add_argument("--page", choices=["A4", "1080p"], default="A4", help="Page size")
    parser.add_argument("--type", choices=["solution", "process-flow", "data-flow"], default="solution", help="Diagram type")
    args = parser.parse_args()

    if args.page == "A4":
        page_w, page_h = 1169, 827
    else:
        page_w, page_h = 1920, 1080

    if args.type == "solution":
        xml = build_solution_diagram(args.title, args.description, args.level, page_w, page_h)
    elif args.type == "process-flow":
        xml = build_process_flow(args.title, args.description, args.level, page_w, page_h)
    else:
        xml = build_data_flow(args.title, args.description, args.level, page_w, page_h)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(xml, encoding="utf-8")
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
