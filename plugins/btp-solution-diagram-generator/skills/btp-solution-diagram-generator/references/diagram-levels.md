# Diagram Levels (L0, L1, L2, L3)

SAP's guideline defines four levels of detail. Picking the wrong level is a
common mistake: an executive asking for "an architecture diagram" probably
wants L0 or L1, not L2. A developer asking the same question usually wants L2
or L3.

## Level Overview

| Level | Audience | Fits on one page? | Typical width |
|---|---|---|---|
| L0 | Business / C-suite | Yes, comfortably | 800–1000px of content |
| L1 | Solution overview | Yes | 1000–1200px of content |
| L2 | Technical stakeholders | Usually yes | 1200–1600px of content |
| L3 | Implementation team | Rarely — often 2 pages | 1600–2400px of content |

Default to **L2** if the user doesn't specify. Most "draw my architecture"
requests are L2-appropriate.

---

## L0 — Capability View

**Purpose**: Communicate *what* BTP does for the business, not *how*.

**Contents**:
- 1 big blue BTP area, maybe labeled "SAP BTP"
- 2–4 capability boxes inside (e.g. "App Dev & Automation", "Integration",
  "Data & Analytics", "AI")
- 1–2 outside systems (S/4HANA, external partners) as large grey boxes
- A user/actor on one side
- NO individual service icons, NO technical annotations
- Short, punchy labels

**Example subjects**: "How BTP supports our digital strategy", "BTP capability
overview for executive kickoff"

```
┌─────────────────────────────────────────────┐
│              SAP BTP                         │
│  ┌─────────────┐  ┌──────────────────┐      │
│  │ Integration │  │ App Dev & Auto.  │      │
│  └─────────────┘  └──────────────────┘      │
│  ┌─────────────┐  ┌──────────────────┐      │
│  │ Data & Ana. │  │ AI               │      │
│  └─────────────┘  └──────────────────┘      │
└─────────────────────────────────────────────┘
    ↕                    ↕
[S/4HANA]          [3rd-Party SaaS]
```

---

## L1 — Solution Overview

**Purpose**: Show the major components and the outline of flows between them.

**Contents**:
- BTP area with 3–7 grouped service clusters (NOT individual services)
  - e.g. "Identity & Access", "User Experience (Build Work Zone + Task Center)",
    "Integration (Cloud Integration)", "Data (HANA Cloud)"
- User/actor with primary access flows
- Key non-SAP systems
- 1–2 semantic flow colors (e.g. authentication in green) to hint at the flow
- Minimal legend (3–5 entries)

**Example subjects**: "SAP Task Center solution overview", "BTP architecture
for Sales extensions"

---

## L2 — Technical Blueprint (default)

**Purpose**: Show the services, their relationships, and how traffic flows.
This is what most architects mean by "BTP architecture diagram".

**Contents**:
- BTP subaccount with its runtime (CF / Kyma / ABAP) as a nested area
- Individual SAP BTP service icons (with the **grey background circle**)
- Each service labeled with its full product name
- Connectors with correct semantic colors (auth=green, authz=indigo, trust=pink,
  data=grey, async=dashed, optional=dotted)
- Full legend
- Title, description, "Diagram Level: L2" label
- Firewall bars between network zones if relevant

**What NOT to include at L2**:
- Protocol details ("OAuth 2.0 / SAML 2.0 / OIDC")
- Endpoint URLs
- Destination names
- Specific scopes or roles

**Example subjects**: "SAP Task Center L2", "CAP on CF extending S/4HANA L2",
"Datasphere → Analytics Cloud pipeline"

This is what `assets/templates/solution-diagram-l2.drawio` produces.

---

## L3 — Implementation Detail

**Purpose**: Give the team everything they need to implement. Usually read
by developers and operators.

**Contents** (everything from L2, plus):
- Protocol + version on each connector (e.g. "OAuth 2.0 Client Credentials")
- Principal propagation arrows
- Destinations and connectivity config annotations
- Instance/plan identifiers for services
- Ports, firewall rules
- Specific scopes, roles, role-collections on authorization flows
- Data volumes / throughput if relevant
- API versions

L3 diagrams often spill onto a second page or require 1920×1080 canvas.

**Example subjects**: "L3 detail — Task Center auth flow including IAS → IPS
provisioning", "L3 detail — CAP service deployment on CF with SAP Destination
Service and Cloud Connector"

---

## Tips for Choosing a Level

| User says… | Probably wants… |
|---|---|
| "Architecture diagram" | L2 |
| "High-level overview" | L1 |
| "Executive / board slide" | L0 |
| "For my design doc" | L2 |
| "For the implementation team" | L3 |
| "For my boss" | L1 |
| "I need to understand how auth works end-to-end" | L3 (auth-focused) |
| "What does our landscape look like" | L1 or L2 |

If the user says "as detailed as possible", offer L3 but warn them it will be
dense and may need 2 pages. Many users walk it back to L2 once they see what
L3 entails.

## Transitioning Between Levels

A single solution often needs diagrams at multiple levels. Structure them so
the reader can jump between:
- L0 has a block labeled "Build Work Zone Area" → L1 shows a cluster with
  Build Work Zone + Task Center → L2 shows each service icon → L3 adds the
  OAuth flow between them
- Use the same title prefix ("SAP Task Center — L0", "… — L1", "… — L2", "… — L3")
- Use the same color palette — the BTP area stays blue at every level
