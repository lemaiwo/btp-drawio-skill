# BTP Solution Diagram Generator

Generate, edit, and validate SAP BTP solution diagrams as `.drawio` files — following the official [SAP BTP Solution Diagram Guidelines](https://sap.github.io/btp-solution-diagrams/).

## What it does

Claude authors `.drawio` files that match SAP's own reference style: the Fiori Horizon color palette, the grey-circle BTP service icons, correct area/nesting rules for the BTP subaccount vs non-SAP systems, and connector semantics for authentication (green), authorization (indigo), trust (pink), async flows (dashed), optional flows (dotted), and firewalls (thick grey bars). Files open directly in draw.io (web, desktop, or the `hediet.vscode-drawio` VS Code extension).

## Components

| Component | Name | Purpose |
|---|---|---|
| Skill | `btp-solution-diagram-generator` | Core knowledge: Horizon palette, area/connector rules, diagram levels L0–L3, mxGraph XML schema, icon catalog |

The skill bundles:

- **6 reference files** with the complete design system, connector semantics, icon catalog, XML schema, and diagram-level guidance
- **3 Python helper scripts** (`validate_drawio.py`, `generate_btp_diagram.py`, `download_btp_libraries.py`) — no third-party dependencies
- **4 starter `.drawio` templates** (solution, process flow, data flow, legend)
- **The full official SAP BTP shape library** — 22 XML files × icon sets × sizes S/M/L, plus generics and annotation helpers
- **11 editable reference `.drawio` examples** from SAP (Task Center, Build Work Zone, Cloud Identity, Private Link, SAP Start, Build Process Automation)

## How it triggers

The skill loads when you ask for anything involving a BTP architecture diagram. Examples:

- "Draw an architecture diagram for our SAP Build Work Zone setup"
- "Visualize how SAP Cloud Identity Services authenticates users into our CAP app"
- "Show the subaccount structure with Kyma runtime and HANA Cloud"
- "Make a data-flow diagram from S/4HANA to SAP Datasphere via Cloud Integration"
- "I need a solution diagram for SAP Task Center at L2"

The skill triggers even when "drawio" or "BTP" isn't spelled out — as long as the request is clearly about SAP BTP architecture visualization.

## Usage

Once the plugin is installed, just ask Claude for the diagram you want. The skill guides Claude through:

1. Clarifying intent (diagram type, level L0–L3, scenario, SAP/non-SAP systems involved)
2. Picking a starter template or building from scratch
3. Applying the Horizon palette and correct connector semantics
4. Validating the output structurally and against BTP conventions
5. Handing off the `.drawio` file with open/edit instructions

To import the bundled SAP BTP icon library into draw.io, point it at any file in `skills/btp-solution-diagram-generator/assets/libraries/`:

> File → Open Library from → File…

The all-in-one Size M library is the recommended default.

## Setup

No environment variables or external services required. The Python scripts use only the standard library.

## Customization

None required. The plugin works out of the box.

## License

MIT. The bundled SAP icon library is Apache-2.0 (see the repo's REUSE metadata for the original source at [SAP/btp-solution-diagrams](https://github.com/SAP/btp-solution-diagrams)).
