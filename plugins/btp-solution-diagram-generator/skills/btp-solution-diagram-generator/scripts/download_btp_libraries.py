#!/usr/bin/env python3
"""
download_btp_libraries.py — Refresh the SAP BTP draw.io shape libraries from
github.com/SAP/btp-solution-diagrams.

NOTE: The skill already bundles these libraries at assets/libraries/ (full set,
sizes S/M/L, plus generics and annotation helpers). You only need this script
to update the bundle against SAP upstream — e.g. when SAP adds a new service.

To overwrite the bundled libraries in-place:
    python scripts/download_btp_libraries.py --all --out assets/libraries

Usage:
    python scripts/download_btp_libraries.py --list                # list available sets
    python scripts/download_btp_libraries.py --all                 # download all (Size M)
    python scripts/download_btp_libraries.py --set foundational    # just one set

Files are saved to ./btp-libraries/ by default (override with --out DIR).

Nothing is installed system-wide — these are plain XML files. Drag them into
draw.io (File → Open Library from → File…) to make the icons available in the
left-hand shape panel.
"""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from pathlib import Path


BASE = "https://raw.githubusercontent.com/SAP/btp-solution-diagrams/main/assets/shape-libraries-and-editable-presets/draw.io"

# Short names → GitHub path. Size M (24px) is the recommended default.
LIBRARIES: dict[str, str] = {
    "all": f"{BASE}/20-02-99-sap-btp-service-icons-all/20-02-99-02-sap-btp-service-icons-all-size-M.xml",
    "foundational": f"{BASE}/20-02-00-sap-btp-service-icons-foundational-set/20-02-00-02-sap-btp-service-icons-foundational-size-M.xml",
    "integration-suite": f"{BASE}/20-02-01-sap-btp-service-icons-integration-suite-set/20-02-01-02-sap-btp-service-icons-integration_suite-size-M.xml",
    "app-dev-automation": f"{BASE}/20-02-02-sap-btp-service-icons-app-dev-automation-set/20-02-02-02-sap-btp-service-icons-app-dev-automation-size-M.xml",
    "data-analytics": f"{BASE}/20-02-04-sap-btp-service-icons-data-analytics-set/20-02-04-02-sap-btp-service-icons-data-analytics-size-M.xml",
    "ai": f"{BASE}/20-02-05-sap-btp-service-icons-ai-set/20-02-05-02-sap-btp-service-icons-ai-size-M.xml",
    "btp-saas": f"{BASE}/20-02-06-sap-btp-service-icons-btp-saas-set/20-02-06-02-sap-btp-service-icons-btp-saas-set-size-M.xml",
    "generic": f"{BASE}/20-03-generic-icons/sap-generic-icons-size-M-200302.xml",
    # Extras from the root of draw.io/ folder — non-service elements
    "annotations": f"{BASE}/annotations_and_interfaces.xml",
    "areas": f"{BASE}/area_shapes.xml",
    "connectors": f"{BASE}/connectors.xml",
    "text-elements": f"{BASE}/text_elements.xml",
    "numbers": f"{BASE}/numbers.xml",
    "sap-brand-names": f"{BASE}/sap_brand_names.xml",
}


def download_one(name: str, url: str, out_dir: Path) -> bool:
    """Download a single library file. Returns True on success."""
    filename = url.rsplit("/", 1)[-1]
    dest = out_dir / filename
    try:
        print(f"  {name:20s} -> {dest}")
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = resp.read()
        dest.write_bytes(data)
        return True
    except urllib.error.URLError as exc:
        print(f"  FAILED {name}: {exc}", file=sys.stderr)
        return False
    except Exception as exc:  # noqa: BLE001
        print(f"  FAILED {name}: {exc}", file=sys.stderr)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Download official SAP BTP draw.io shape libraries.")
    parser.add_argument("--all", action="store_true", help="Download every library")
    parser.add_argument("--set", dest="set_name", help="Download a single set by short name (e.g. 'foundational')")
    parser.add_argument("--list", action="store_true", help="List available sets and exit")
    parser.add_argument("--out", default="./btp-libraries", help="Output directory (default ./btp-libraries)")
    args = parser.parse_args()

    if args.list:
        print("Available libraries (short name → URL):\n")
        for name, url in LIBRARIES.items():
            print(f"  {name:20s} {url}")
        return 0

    if not args.all and not args.set_name:
        parser.print_help()
        return 1

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.set_name:
        if args.set_name not in LIBRARIES:
            print(f"Unknown set '{args.set_name}'. Run with --list to see available sets.", file=sys.stderr)
            return 1
        ok = download_one(args.set_name, LIBRARIES[args.set_name], out_dir)
        return 0 if ok else 1

    # --all
    print(f"Downloading {len(LIBRARIES)} libraries to {out_dir}/")
    successes = 0
    for name, url in LIBRARIES.items():
        if download_one(name, url, out_dir):
            successes += 1
  