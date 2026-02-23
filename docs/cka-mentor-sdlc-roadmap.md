# CKA Mentor AI - SDLC Roadmap and Tech Stack

## Scope and Assumptions
- Team: 4-8 engineers, 1 PM, 1 designer, 1 QA
- Cloud: AWS (swapable)
- AI: multi-model LLM gateway with evals and guardrails
- Human review: per-module and two-phase plan approval

## Roadmap (Phased)

### Phase 0 - Product Definition (1-2 weeks)
Deliverables:
- PRD with success metrics and internal quality thresholds
- User journey and requirements
- Threat model and compliance baseline

Exit criteria:
- PRD approved
- KPIs and milestones locked

### Phase 1 - Architecture and Prototype (2-4 weeks)
Deliverables:
- System architecture and data model
- Agent boundaries and orchestration design
- Clickable UX prototype for trainee and trainer flows
- LLM evaluation harness (prompt tests and regression tests)

Exit criteria:
- Architecture approved
- Prototype validated with 3-5 users

### Phase 2 - MVP Build (6-8 weeks)
Deliverables:
- Baseline assessment and plan generation
- Training modules and Hint Bot
- Trainer dashboard with per-module review
- Orchestrator for state transitions
- Audit trail for approvals and adjustments
- Basic observability

Exit criteria:
- End-to-end internal demo
- One sprint completed by a pilot trainee

### Phase 3 - Alpha (2-4 weeks)
Deliverables:
- Two-phase plan approval (AI gatepass + human approval)
- Blunt feedback style support
- Exam-compatibility checker for uploaded helper files
- Real-user pilot (5-10 trainees)

Exit criteria:
- 70%+ sprint completion
- No critical workflow blockers

### Phase 4 - Beta (4-6 weeks)
Deliverables:
- Capstone and mock exam flows
- Evaluation rubrics and trainer scoring
- Sprint review and plan adaptation tuning
- Performance and UX polish

Exit criteria:
- Readiness gates stable
- Trainer review loop under 48 hours

### Phase 5 - GA (4-6 weeks)
Deliverables:
- Security hardening and privacy controls
- Rate limits and SLOs
- Full QA and automated test suites
- Support playbooks

Exit criteria:
- Stable uptime
- Support-ready operations

### Phase 6 - Scale (Ongoing)
Deliverables:
- Additional certification profiles (CKAD, CKS)
- Team analytics and cohort insights
- Model routing and cost optimization
- Advanced personalization

## Recommended Tech Stack

### Frontend
- Next.js (React + TypeScript)
- Tailwind CSS
- React Query or Zustand
- Storybook

### Backend and API
- Node.js (TypeScript) or Python (FastAPI)
- REST API + event-driven workers
- Prisma (Node) or SQLAlchemy (Python)

### Data Layer
- Postgres
- Redis
- Object storage (S3)

### AI and Agents
- LLM gateway with model diffing
- Prompt versioning and eval harness
- Vector DB: pgvector or Pinecone
- Safety and policy enforcement layer

### Orchestration
- Temporal or queue-based workers (BullMQ / Celery / SQS)

### Exam Compatibility Checker
- Static analysis for uploaded files
- Optional sandbox execution (Firecracker or gVisor)
- Rule-based allowlist for exam-safe tooling

### Observability
- OpenTelemetry
- Prometheus + Grafana
- Sentry

### CI/CD and Infra
- GitHub Actions
- Terraform
- Docker
- Kubernetes (optional)

### Auth
- OIDC provider (Auth0 or Clerk)

## Non-Negotiable Product Gates
- Two-phase plan approval (AI gatepass + human approval)
- Trainer review required for every module
- Internal quality threshold not shown to trainees
- Exam-compatibility checker for uploaded helper files
