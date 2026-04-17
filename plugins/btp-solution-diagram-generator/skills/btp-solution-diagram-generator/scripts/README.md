# Scripts

Python 3.8+ helper scripts for the BTP Solution Diagram Generator skill.
No third-party dependencies — only the standard library.

## validate_drawio.py

Validate a `.drawio` file for structural correctness *and* BTP guideline
conformance (Horizon palette usage, title cell, legend presence).

```bash
python scripts/validate_drawio.py my-diagram.drawio
python scripts/validate_drawio.py my-diagram.drawio --strict
```

Exit codes:
- `0` — passed all checks (or only has BTP warnings in non-strict mode)
- `1` — structural error (file won't render correctly in draw.io)
- `2` — `--strict` mode and BTP warnings were raised

## generate_btp_diagram.py

Scaffold a new diagram file with correct BTP styling applied.

```bash
# Default: L2 solution diagram with a BTP subaccount, non-SAP area, and legend
python scripts/generate_btp_diagram.py task-center.drawio \
    --title "SAP Task Center" \
    --description "Unified task inbox across SAP systems via BTP." \
    --level L2

# Process-flow variant
python scripts/generate_btp_diagram.py onboarding-flow.drawio \
    --title "User Onboarding" \
    --level L1 \
    --type process-flow

# Data-flow variant on a 1080p canvas
python scripts/generate_btp_diagram.py s4-to-datasphere.drawio \
    --title "S/4HANA to Datasphere" \
    --description "Nightly extract via Cloud Integration." \
    --level L2 \
    --type data-flow \
    --page 1080p
```

The output is a valid `.drawio` file you can open directly and then extend by
dragging service icons from the imported SAP BTP shape library.

## download_btp_libraries.py

**You probably don't need this script.** The skill already ships with the
full SAP BTP shape library bundled at `assets/libraries/` (all sets in
sizes S/M/L, plus generics and annotation/area/connector/text helpers).

Use it only to **refresh** the bundle against SAP upstream — e.g. when SAP
adds a new service icon. To overwrite the bundled copies:

```bash
python scripts/download_btp_libraries.py --all --out assets/libraries
```

Other usage:

```bash
# See what's available
python scripts/download_btp_libraries.py --list

# Download everything to ./btp-libraries/ (default output dir)
python scripts/download_btp_libraries.py --all

# Just one set
python scripts/download_btp_libraries.py --set foundational
```

I