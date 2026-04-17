# SAP BTP Service Icon Catalog

This is the catalog of service icons available in the official SAP BTP
shape library. Each icon has a **five-digit ID** and a kebab-case name; both
appear in the library XML and the draw.io shape panel's search box.

The icons come in **three sizes** (S=16px, M=24px, L=48px). Size M is the
recommended default for L2 solution diagrams.

**These libraries are bundled with the skill** at `assets/libraries/`. No
download required. Import any file into draw.io via
`File → Open Library from → File…`.

**Key library files** (paths relative to the skill root):

| Set | Bundled path (Size M shown; also available S and L) | Contains |
|---|---|---|
| All services (recommended) | `assets/libraries/20-02-99-sap-btp-service-icons-all/20-02-99-02-sap-btp-service-icons-all-size-M.xml` | Every service icon in one file |
| Foundational | `assets/libraries/20-02-00-sap-btp-service-icons-foundational-set/20-02-00-02-sap-btp-service-icons-foundational-size-M.xml` | Runtimes, identity, destination, connectivity |
| Integration Suite | `assets/libraries/20-02-01-sap-btp-service-icons-integration-suite-set/20-02-01-02-sap-btp-service-icons-integration_suite-size-M.xml` | Cloud Integration, API Management, Event Mesh, etc. |
| App Dev & Automation | `assets/libraries/20-02-02-sap-btp-service-icons-app-dev-automation-set/20-02-02-02-sap-btp-service-icons-app-dev-automation-size-M.xml` | SAP Build family, Business App Studio, Mobile Services |
| Data & Analytics | `assets/libraries/20-02-04-sap-btp-service-icons-data-analytics-set/20-02-04-02-sap-btp-service-icons-data-analytics-size-M.xml` | HANA Cloud, Datasphere, Analytics Cloud |
| AI | `assets/libraries/20-02-05-sap-btp-service-icons-ai-set/20-02-05-02-sap-btp-service-icons-ai-size-M.xml` | AI Core, AI Launchpad, Document AI services |
| BTP SaaS | `assets/libraries/20-02-06-sap-btp-service-icons-btp-saas-set/20-02-06-02-sap-btp-service-icons-btp-saas-set-size-M.xml` | SaaS solutions running on BTP |
| Generic | `assets/libraries/20-03-generic-icons/sap-generic-icons-size-M-200302.xml` | User, API, App, DB, Mobile, Factory, etc. |

**Helper libraries** (also in `assets/libraries/`): `annotations_and_interfaces.xml`,
`area_shapes.xml`, `connectors.xml`, `numbers.xml`, `sap_brand_names.xml`,
`text_elements.xml`, `default_shapes.xml`, `essentials.xml`.

To refresh the bundle against SAP upstream (e.g. after SAP adds a new service):

```bash
python scripts/download_btp_libraries.py --all --out assets/libraries
```

---

## Complete Service Icon List

Icons are identified by a numeric ID; the name after is what you see as the
default label. To search in draw.io's shape panel, type any word from the name
(e.g. "Task Center", "Cloud Identity", "HANA").

### Foundational (runtime, identity, connectivity)

| ID | Name |
|---|---|
| 10017 | SAP BTP, Cloud Foundry runtime |
| 20065 | SAP BTP, Kyma runtime |
| 20016 | SAP BTP, ABAP environment |
| 32129 | SAP Cloud Identity Services |
| 32071 | Identity Authentication (IAS) |
| 32072 | Identity Provisioning (IPS) |
| 32128 | Identity Directory |
| 32127 | Authorization Management |
| 31015 | SAP Authorization and Trust Management Service (XSUAA) |
| 20070 | OAuth 2.0 on SAP BTP |
| 32148 | Cloud Connector |
| 31113 | SAP Connectivity Service (cross-check 20077) |
| 20077 | SAP Connectivity Service |
| 20080 | SAP Destination Service |
| 10042 | SAP Private Link Service |
| 20074 | SAP Custom Domain Service |
| 10035 | SAP Keystore Service |
| 10037 | SAP Malware Scanning Service |
| 10014 | SAP Audit Log Service |
| 20062 | SAP Application Logging Service for SAP BTP |
| 31112 | Cloud Logging |
| 20092 | SAP Monitoring Service for SAP BTP |
| 31060 | SAP Alert Notification Service for SAP BTP |
| 20051 | Application Autoscaler |
| 20098 | Service Manager |
| 20053 | SAP Cloud Management Service for SAP BTP |
| 20090 | SAP Job Scheduling Service |
| 10028 | SAP Feature Flags Service |
| 31073 | SAP Credential Store |
| 32130 | SAP Secure Login Service for SAP GUI |
| 32156 | SAP PKI Certificate Service |
| 10009 | Object Store on SAP BTP |
| 20064 | SAP BTP Bandwidth |
| 10039 | SAP Master Data Integration |
| 10002 | Cloud Integration Automation |
| 31063 | SAP Automation Pilot |
| 10022 | SAP Continuous Integration and Delivery |
| 20076 | SAP Cloud Transport Management |
| 32021 | SAP Content Agent Service (31021) |
| 31040 | SAP Personal Data Manager |
| 31024 | SAP Data Retention Manager |
| 10023 | SAP Data Privacy Integration |
| 31027 | SAP Document Management Service |
| 31045 | SAP Solution Lifecycle Management Service for SAP BTP |
| 31120 | SAP Software-as-a-Service Provisioning Service |
| 31104 | Landscape Portal for SAP S/4HANA Cloud, ABAP environment |
| 34158 | Application Frontend Service |
| 32082 | SAP Event Broker for SAP Cloud Applications |

### Integration Suite

| ID | Name |
|---|---|
| 32086 | SAP Integration Suite |
| 32134 | Cloud Integration |
| 32133 | API Management |
| 31037 | Event Mesh (legacy) |
| 32032 | Advanced Event Mesh |
| 32141 | Open Connectors |
| 32138 | Integration Advisor |
| 32139 | Integration Assessment |
| 32140 | Migration Assessment |
| 32142 | Trading Partner Management |
| 32135 | Data Space Integration |
| 32136 | Edge Integration Cell |
| 32087 | Graph |
| 32154 | API Business Hub Enterprise |
| 32153 | SAP Business Accelerator Hub |

### Application Development & Automation

| ID | Name |
|---|---|
| 34157 | SAP Build |
| 31066 | SAP Build Apps |
| 31109 | SAP Build Code |
| 31067 | SAP Build Process Automation |
| 31068 | SAP Build Work Zone |
| 31018 | SAP Build Work Zone, advanced edition |
| 31046 | SAP Task Center |
| 20069 | SAP Business Application Studio |
| 33146 | SAP Cloud Application Programming Model (CAP) |
| 33122 | Extensibility Service for SAP BTP |
| 20049 | UI5 Flexibility for Key Users |
| 32147 | SAP UI Theme Designer |
| 20091 | SAP Mobile Services |
| 10030 | SAP HTML5 Application Repository Service for SAP BTP |
| 32150 | SAP Dynamic Forms |
| 35158 | Joule Studio |

### Data & Analytics

| ID | Name |
|---|---|
| 20083 | SAP HANA Cloud |
| 20094 | SAP Persistence Service (ASE) |
| 31085 | SAP HANA Spatial Services |
| 10025 | SAP Datasphere |
| 20061 | SAP Analytics Cloud |
| 10013 | SAP Analytics Cloud, embedded edition |
| 34152 | SAP Business Data Cloud |
| 31114 | SAP Data Enrichment Service |
| 31075 | SAP Cloud Integration for Data Services |
| 31119 | SAP Master Data Governance |
| 31055 | Data Quality Services |

### AI

| ID | Name |
|---|---|
| 20058 | SAP AI Core |
| 20059 | SAP AI Launchpad |
| 32124 | Document Grounding |
| 10004 | Document Information Extraction |
| 20056 | Document Classification |
| 20054 | Data Attribute Recommendation |
| 10010 | Personalized Recommendation |
| 20099 | Service Ticket Intelligence |
| 31052 | Business Entity Recognition |
| 31103 | Invoice Object Recommendation |
| 10007 | Intelligent Situation Automation |
| 31115 | SAP Digital Assistant |
| 20095 | SAP Translation Hub |

### SaaS solutions on BTP

| ID | Name |
|---|---|
| 33126 | SAP Asset Performance Management |
| 34156 | SAP Cloud ALM |
| 33147 | SAP Project and Resource Management |
| 34155 | SAP Logistics Management |
| 34159 | Customer Data Cloud |
| 33149 | SAP S/4HANA for Microsoft Teams |
| 20036 | SAP Landscape Management Cloud |
| 10044 | SAP S/4HANA Cloud for Intelligent Intercompany Reconciliation |
| 32131 | SAP Digital Manufacturing |
| 20096 | SAP Variant Configuration and Pricing |
| 20093 | SAP Omnichannel Promotion Pricing |
| 31117 | SAP Green Token |
| 31118 | SAP Health Data Services for FHIR |
| 32146 | SAP Sustainability Data Exchange |
| 32149 | SAP Collaborative Demand and Capacity Management |
| 32152 | SAP Watch List Screening |
| 31043 | SAP Responsibility Management Service |
| 31026 | SAP Document and Reporting Compliance |
| 31047 | SAP Usage Data Management Service for SAP BTP |
| 31115 | SAP Digital Assistant |
| 10041 | SAP Print Service |
| 33123 | Business Process Model Connector for SAP Signavio Solutions |
| 33145 | SAP Process Visibility Service |
| 34154 | Application Vulnerability Report |
| 33150 | Decentralized Identity Verification |

### Generic Icons (non-service elements)

The `20-03-generic-icons` library contains shapes for things that don't map
to a specific SAP service: users, devices, APIs, documents, factories, etc.
Each icon comes in three variants: **SAP** (blue), **Non-SAP** (grey), and
**Highlight** (accent color).

Available generic shapes (partial list — see the library file for all):

`Adapter`, `Admin`, `AI`, `AI Agent`, `Alert`, `API`, `App`, `Building`,
`Cloud`, `Cloud Connector`, `Collision`, `DA` (data attribute),
`Deploy`, `Desktop`, `Detail-View`, `Devices`, `Document`, `Documents`,
`Event`, `Factory`, `Feature`, `Indent`, `Info`, `Inspect`, `Key`,
`Link`, `Locked`, `Machine`, `Message`, `Mobile`, `On-Premise`,
`Palette`, `Paper-Plane`, `Permission`, `Restart`, `Settings`, `Success`,
`Synchronize`, `Third Party`, `Tree`, `User`, `Web`.

Each is available in S and M sizes with three color variants — use the
SAP variant (blue) for BTP-internal elements, Non-SAP (grey) for external
parties, and Highlight (accent) for elements that need emphasis.

---

## How to Use an Icon

### Option A: Import the library (recommended for editable diagrams)

In draw.io:
1. `File → Open Library from → URL…`
2. Paste the GitHub raw URL of the library XML
3. The icons appear in the left panel; drag one onto the canvas

### Option B: Copy an `<mxCell>` from the library XML directly

Each icon in the library is an `<mxCell>` with a style beginning with
`shape=image;...;image=data:image/svg+xml,<base64>;...`. You can copy the
cell into your diagram and adjust `x`, `y`, `width`, `hei