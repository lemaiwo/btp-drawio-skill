#!/usr/bin/env python3
"""
validate_drawio.py — Validate the structure of a .drawio file plus BTP-specific
conventions from the SAP BTP Solution Diagram Guideline.

Structural checks (match the generic drawio validator):
  - XML is well-formed
  - Root element is <mxfile>
  - Every diagram page has <mxCell id="0" /> as first cell
  - Every diagram page has <mxCell id="1" parent="0" /> as second cell
  - All cell ids are unique within a page
  - Every non-root cell has a parent pointing to an existing id
  - Every vertex has <mxGeometry as="geometry">
  - Every edge has source+target (both existing) OR sourcePoint+targetPoint

BTP-specific checks (warnings, not errors):
  - A title cell exists (text style, fontSize>=14)
  - A BTP-colored area exists (fillColor=#EBF8FF or strokeColor=#0070F2)
  - The diagram uses Horizon palette colors (warns on draw.io default colors)
  - A legend area exists

Usage:
    python scripts/validate_drawio.py <file.drawio> [--strict]

Exit codes:
    0  All structural checks passed (warnings may still print)
    1  Structural error found
    2  --strict and a BTP warning was raised
"""
from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


# Horizon palette (approximations used as style hints)
BTP_COLORS = {
    "#0070F2", "#EBF8FF", "#475E75", "#F5F6F7", "#1D2D3E", "#556B82",
    "#188918", "#F5FAE5", "#C35500", "#FFF8D6", "#D20A0A", "#FFEAF4",
    "#07838F", "#DAFDF5", "#5D36FF", "#F1ECFF", "#CC00DC", "#FFF0FA",
    "#FFFFFF", "#EAECEE",
}
# Draw.io default palette — presence of these suggests the author didn't apply BTP styling
DRAWIO_DEFAULTS = {
    "#dae8fc", "#6c8ebf", "#d5e8d4", "#82b366", "#fff2cc", "#d6b656",
    "#f8cecc", "#b85450", "#e1d5e7", "#9673a6",
}


def _err(errors: list, msg: str) -> None:
    errors.append(msg)
    print(f"  ERROR: {msg}")


def _warn(warnings: list, msg: str) -> None:
    warnings.append(msg)
    print(f"  WARN:  {msg}")


def _style_to_dict(style: str | None) -> dict[str, str]:
    """Parse a draw.io style string like 'rounded=1;fillColor=#EBF8FF;' into a dict."""
    out: dict[str, str] = {}
    if not style:
        return out
    for part in style.split(";"):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            k, _, v = part.partition("=")
            out[k.strip()] = v.strip()
        else:
            # bare key like "rounded" or "ellipse" — record with empty value
            out[part] = ""
    return out


def _iter_colors_in_style(style_dict: dict[str, str]) -> list[str]:
    """Return all hex colors that appear in fillColor/strokeColor/fontColor values."""
    out = []
    for key in ("fillColor", "strokeColor", "fontColor"):
        v = style_dict.get(key, "")
        if v.startswith("#"):
            out.append(v.upper())
    return out


def validate_file(path: Path) -> tuple[list[str], list[str]]:
    """Validate one .drawio file. Returns (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        return [f"XML parse error: {exc}"], []

    root = tree.getroot()
    if root.tag != "mxfile":
        _err(errors, f"Root element must be <mxfile>, got <{root.tag}>")
        return errors, warnings

    diagrams = root.findall("diagram")
    if not diagrams:
        _err(errors, "No <diagram> elements found inside <mxfile>")
        return errors, warnings

    for d_idx, diagram in enumerate(diagrams):
        d_name = diagram.get("name", f"page-{d_idx}")
        prefix = f"[diagram '{d_name}']"

        graph_model = diagram.find("mxGraphModel")
        if graph_model is None:
            # Compressed diagram — not supported for structural validation
            _warn(warnings, f"{prefix} mxGraphModel not direct child (may be compressed). Skipping structural checks.")
            continue

        root_elem = graph_model.find("root")
        if root_elem is None:
            _err(errors, f"{prefix} Missing <root> element inside <mxGraphModel>")
            continue

        cells = root_elem.findall("mxCell")
        cell_ids: dict[str, ET.Element] = {}

        # Collect ids, check uniqueness
        for cell in cells:
            cid = cell.get("id")
            if cid is None:
                _err(errors, f"{prefix} <mxCell> without 'id' attribute")
                continue
            if cid in cell_ids:
                _err(errors, f"{prefix} Duplicate cell id='{cid}'")
            cell_ids[cid] = cell

        # Structural rules for the first two cells:
        #   - First cell is the "root": it has NO parent attribute (or an empty one)
        #   - Second cell is the "default layer": its parent = first cell's id
        # Draw.io's convention is ids "0" and "1", but any ids are valid as long
        # as the parent relationship holds. SAP's own reference files use
        # prefixed ids like "WXxtYBOuJOK_NInGcJ7v-0" / "-1".
        root_id: str | None = None
        if len(cells) >= 1:
            first = cells[0]
            root_id = first.get("id")
            if first.get("parent") not in (None, ""):
                _err(errors, f"{prefix} First <mxCell> (the root, id='{root_id}') must have no 'parent' attribute, got parent='{first.get('parent')}'")
        if len(cells) >= 2:
            second = cells[1]
            layer_parent = second.get("parent")
            if layer_parent != root_id:
                _err(errors, f"{prefix} Second <mxCell> (the default layer, id='{second.get('id')}') must have parent='{root_id}', got parent='{layer_parent}'")

        # Every cell's parent must exist, except the root cell
        for cell in cells:
            cid = cell.get("id", "?")
            if cid == root_id:
                continue
            parent = cell.get("parent")
            if parent is None:
                _err(errors, f"{prefix} Cell id='{cid}' missing 'parent' attribute")
            elif parent not in cell_ids:
                _err(errors, f"{prefix} Cell id='{cid}' references unknown parent='{parent}'")

        # Vertex cells must have mxGeometry
        for cell in cells:
            if cell.get("vertex") == "1":
                if cell.find("mxGeometry") is None:
                    _err(errors, f"{prefix} Vertex id='{cell.get('id')}' missing <mxGeometry>")

        # Edge cells must have source+target OR sourcePoint+targetPoint
        for cell in cells:
            if cell.get("edge") != "1":
                continue
            cid = cell.get("id", "?")
            src = cell.get("source")
            tgt = cell.get("target")
            geom = cell.find("mxGeometry")
            has_src_pt = geom is not None and any(
                p.get("as") == "sourcePoint" for p in geom.findall("mxPoint")
            )
            has_tgt_pt = geom is not None and any(
                p.get("as") == "targetPoint" for p in geom.findall("mxPoint")
            )
            if src is None and not has_src_pt:
                _err(errors, f"{prefix} Edge id='{cid}' missing 'source' (and no sourcePoint)")
            elif src is not None and src not in cell_ids:
                _err(errors, f"{prefix} Edge id='{cid}' references unknown source='{src}'")
            if tgt is None and not has_tgt_pt:
                _err(errors, f"{prefix} Edge id='{cid}' missing 'target' (and no targetPoint)")
            elif tgt is not None and tgt not in cell_ids:
                _err(errors, f"{prefix} Edge id='{cid}' references unknown target='{tgt}'")

        # --- BTP-specific warnings ---
        _btp_checks(prefix, cells, warnings)

    return errors, warnings


def _btp_checks(prefix: str, cells: list[ET.Element], warnings: list[str]) -> None:
    """Check for BTP guideline conformance. Emits warnings, not errors."""
    found_title = False
    found_btp_area = False
    found_legend = False
    drawio_default_hits: list[tuple[str, str]] = []

    for cell in cells:
        cid = cell.get("id", "?")
        style_dict = _style_to_dict(cell.get("style"))
        colors = [c.upper() for c in _iter_colors_in_style(style_dict)]

        # Title: a vertex with 'text' style and fontSize >= 14
        is_text = (
            "text" in style_dict
            or style_dict.get("verticalLabelPosition") is None
            and cell.get("value")
        )
        font_size = 0
        try:
            font_size = int(style_dict.get("fontSize", "0"))
        except ValueError:
            font_size = 0
        if cell.get("vertex") == "1" and font_size >= 14 and "text" in style_dict:
            found_title = True

        # BTP area: a vertex with Horizon blue stroke OR fill
        fill = style_dict.get("fillColor", "").upper()
        stroke = style_dict.get("strokeColor", "").upper()
        if stroke == "#0070F2" or fill == "#EBF8FF":
            found_btp_area = True

        # Legend: a vertex with fillColor=#FFFFFF, strokeColor=#EAECEE (light grey)
        if fill == "#FFFFFF" and stroke in ("#EAECEE", "#EAECEE".upper()):
            found_legend = True

        # Draw.io default palette (warn)
        for color in colors:
            if color.lower() in {c.lower() for c in DRAWIO_DEFAULTS}:
                drawio_default_hits.append((cid, color))

    if not found_title:
        _warn(warnings, f"{prefix} No title cell found (expected a text cell with fontSize>=14 — usually 16pt blue #0070F2)")
    if not found_btp_area:
        _warn(warnings, f"{prefix} No BTP-styled area found (no cell uses #0070F2 stroke or #EBF8FF fill)")
    if not found_legend:
        _warn(warnings, f"{prefix} No legend detected (expected a white-fill container with stroke #EAECEE)")
    for cid, color in drawio_default_hits[:5]:  # cap output
        _warn(warnings, f"{prefix} Cell id='{cid}' uses draw.io default color {color} — replace with Horizon palette (see references/btp-colors-and-styles.md)")
    if len(drawio_default_hits) > 5:
        _warn(warnings, f"{prefix} ... and {len(drawio_default_hits) - 5} more non-Horizon color(s)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a .drawio file for structure and BTP guideline conformance.")
    parser.add_argument("path", help="Path to the .drawio file")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on BTP warnings, not just errors")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"File not found: {path}")
        return 1
    if not path.is_file():
        print(f"Not a file: {path}")
        return 1

    print(f"Validating: {path}")
    errors, warnings = validate_file(path)

    print()
    if errors:
        print(f"FAIL — {len(errors)} structural error(s), {len(warnings)} BTP warning(s).")
        return 1
    if warnings and args.strict:
        print(f"STRICT FAIL — {len(warnings)} BTP warning(s) (no structural errors).")
        return 2
    if warnings:
        print(f"PASS structure, {len(warnings)} BTP warning(s) — review above.")
    else:
        print("PASS — no errors, no BTP warnings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
