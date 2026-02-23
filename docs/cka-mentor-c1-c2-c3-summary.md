# CKA Mentor AI - C4 C1/C2/C3 Summary (What’s Covered and How They Differ)

## Purpose of Each Diagram
**C1 - System Context**
- Shows the platform as a single box and its external actors/systems.
- Defines the scope and external dependencies.

**C2 - Container Diagram**
- Zooms into the platform to show deployable containers (microservices, UI, data stores).
- Clarifies technology choices and responsibilities.

**C3 - Component Diagram**
- Zooms into a single container (the Backend API) and shows internal components.
- Explains how requests flow inside the container.

## What Each Diagram Covers (This Product)

**C1 - System Context**
- Users: Trainee and Trainer
- External systems: LLM providers, notification service, identity provider, sandbox/cluster provider

**C2 - Container Diagram**
- Web UI (Next.js)
- Backend API (microservices, Docker-ready)
- LLM Gateway
- Orchestrator and workers
- Sandbox runner
- Data stores: Postgres, Redis, object storage

**C3 - Component Diagram (Backend API Container)**
- API controllers and routing
- Auth/RBAC
- Assessment, Plan, Training, Evaluation services
- Hint Bot component
- File/Artifact service
- Event publisher and audit logging
- Data access layer

## Key Differences
- C1 defines the boundary of the system and its external dependencies.
- C2 defines the deployable building blocks and their responsibilities.
- C3 defines internal structure of one container and its components.

## Diagram Files
- C1 PNG: /Users/parzival/Documents/Developer/ai-mentor/docs/diagrams/c1.png
- C2 PNG: /Users/parzival/Documents/Developer/ai-mentor/docs/diagrams/c2.png
- C3 PNG: /Users/parzival/Documents/Developer/ai-mentor/docs/diagrams/c3.png
