# BTP Draw.io Skill — Claude Plugin Marketplace

A Claude plugin marketplace hosting the **BTP Solution Diagram Generator** — a skill that helps Claude author SAP BTP solution diagrams as `.drawio` files, following the official [SAP BTP Solution Diagram Guidelines](https://sap.github.io/btp-solution-diagrams/).

## Install

In Claude Code or Cowork, add this marketplace and install the plugin:

```
/plugin marketplace add lemaiwo/btp-drawio-skill
/plugin install btp-solution-diagram-generator
```

Or use the Discover tab in the `/plugin` UI.

## What you get

| Plugin | Description |
|---|---|
| [`btp-solution-diagram-generator`](./plugins/btp-solution-diagram-generator) | Generate, edit, and validate SAP BTP solution diagrams (.drawio) following SAP Fiori Horizon guidelines — the full official BTP icon library bundled. |

## Example prompts that trigger the skill

Once installed, Claude loads the skill automatically when you say things like:

- *"Draw an architecture diagram for our SAP Build Work Zone setup"*
- *"Show me how SAP Cloud Identity Services authenticates users into our CAP app"*
- *"Diagram the subaccount with Kyma runtime, HANA Cloud, and SAP Datasphere"*
- *"I need a solution diagram for SAP Task Center at L2"*
- *"Visualize the data flow from S/4HANA to Datasphere via Cloud Integration"*

The skill produces a ready-to-open `.drawio` file using the SAP Fiori Horizon color palette, the grey-circle BTP service icons, and correct connector semantics (authentication in green, authorization in indigo, trust in pink, async flows dashed, firewalls thick grey).

## What's inside the plugin

- A core skill (`SKILL.md`) with the design system, diagram-level model (L0–L3), and workflow
- 6 reference files covering Horizon colors/styles, area/nesting rules, connector semantics, the icon catalog, the mxGraph XML schema, and diagram levels
- 3 Python helper scripts (`validate_drawio.py`, `generate_btp_diagram.py`, `download_btp_libraries.py`) — zero third-party dependencies
- 4 starter `.drawio` templates (solution, process flow, data flow, legend)
- The **full official SAP BTP shape library** (22 XML files × three sizes + generics + annotation helpers) bundled at `assets/libraries/` — no network needed
- 11 editable SAP reference `.drawio` examples

## Sources

- [SAP BTP Solution Diagrams (upstream)](https://github.com/SAP/btp-solution-diagrams)
- [SAP BTP Solution Diagram Guidelines (rendered)](https://sap.github.io/btp-solution-diagrams/)
- [Claude plugin marketplace docs](https://code.claude.com/docs/en/plugin-marketplaces)

## License

MIT for the skill content, manifest, and scripts. The bundled SAP icon assets are Apache-2.0 — see [SAP/btp-solution-diagrams](https://github.com/SAP/btp-solution-diagrams) for the upstream license and REUSE metadata.

## Contributing

Issues and PRs welcome. To refresh the bundled SAP icon library against upstream:

```bash
python plugins/btp-solution-diagram-generator/skills/btp-solution-diagram-generator/scripts/download_btp_libraries.py \
    --all \
    --out plugins/btp-solution-diagram-generator/skills/btp-solution-diagram-generator/assets/libraries
```
