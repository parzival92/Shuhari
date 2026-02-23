# CKA Mentor AI - Component Overview

## System Overview
The platform follows a linear but iterative flow with human checkpoints:

1. Trainee Assessment
2. Plan Generation (trainer approval)
3. Training Execution with Hint Bot
4. Evaluation (trainer verification)
5. Sprint loop (reassess, adapt, repeat)
6. Final evaluation and certification-readiness sign-off

Two user roles exist: Trainer (human reviewer) and Trainee (CKA candidate). Each trainee is assigned a trainer. Each trainer can manage multiple trainees. All intelligence is powered by scoped AI agents, with the trainer acting as the human-in-the-loop at critical decision points. Plan approval uses a two-phase gate: consolidated AI review via diffed model outputs, followed by final human approval.

## Goal and Success Criteria
Goal: produce a CKA-ready engineer who can perform to expert-level Kubernetes standards without shortcuts.

Primary success criteria (external outcome):
- Candidate achieves a strong CKA result that meets internal quality thresholds (not shown to the trainee).
- Demonstrate hands-on proficiency across core CKA domains in live demos.
- Trainer signs off on readiness using a structured rubric.

Internal note: the quality threshold is used as a mentorship quality signal and is not surfaced to trainees.

Readiness gates (internal, before scheduling the exam):
- Two consecutive, full-length mock exams under timed conditions meeting the internal quality threshold.
- Capstone and live demo passed with trainer approval.

The system is designed to build real capability, not just test-taking tricks.

## Timeline and Pacing (User-Specific)
Timeline is computed per trainee based on baseline assessment and weekly time budget.

Default pacing assumptions (adjust after baseline):
- Strong baseline (daily Kubernetes users): 6-8 weeks
- Mid baseline (some production exposure): 10-14 weeks
- Early baseline (labs only): 16-20 weeks

Each plan uses 2-week sprints with adaptive scope based on sprint reviews.

## Component 1: CKA Baseline Assessment
Purpose: Evaluate the trainee's current Kubernetes and Linux skills to establish a baseline competency profile that drives the training plan, difficulty calibration, and evaluation targets.

How it works (layered and adaptive):
- Layer 1: Self-declaration (2-3 minutes)
  - Trainee selects proficiency band: beginner, intermediate, or advanced.
  - Skill matrix covering CKA domains (cluster architecture, workloads, services/networking, storage, security, troubleshooting, Linux fundamentals).
- Layer 2: Scenario spot-checks (5-10 minutes)
  - One targeted scenario per domain rated "hands-on" or above.
  - Example: "Your pods are CrashLoopBackOff and logs show OOMKilled. What is your diagnosis and remediation?"
- Layer 3: Quick hands-on diagnostic (15-25 minutes)
  - Short live tasks on a sandbox cluster to validate key skills (kubectl workflow, YAML editing, debugging, core resource management).
- Layer 4: Mismatch deep-dive (only if triggered)
  - 1-2 focused questions when self-rating and performance diverge.

Outputs:
- Competency profile (scores per domain + radar chart data)
- Raw responses and hands-on results for trainer review
 - Baseline accuracy signal (self-rating vs spot-check performance)

Trainer touchpoint:
- Review profile and trainee responses
- Add annotations and adjust scores with mandatory justification (audit trail)

## Onboarding and Exam-Compatibility Check
Purpose: Ensure the trainee's workflow and artifacts are compatible with the exam environment.

How it works:
- Trainee selects proficiency band (beginner/intermediate/advanced).
- Trainee uploads a helper file or script they intend to use during practice.
- System validates that the file and commands align with CKA exam constraints and supported tooling.
- Any unsupported tooling or patterns are flagged and replaced with approved alternatives.

## Component 2: Training Plan Generation
Purpose: Produce a personalized, structured learning path aligned to the current CKA curriculum and the trainee's goals and constraints.

Inputs:
- Competency profile from assessment
- Trainee goal (CKA target date, desired pace, weekly time budget)
- Trainer adjustments and notes

Plan structure:
- Organized into 2-week sprints with 3-5 learning modules per sprint
- Each module includes:
  - Objective (clear, measurable)
  - Theory (30%): short readings and docs
  - Hands-on (50%): concrete tasks with deliverables
  - Mini-quiz/reflection (10%): scenario questions
  - Stretch goal (10%): optional advanced challenge

Difficulty calibration:
- Low score domains: fundamentals-first, more theory
- Mid score domains: practical focus
- High score with gaps: targeted deep-dives
- Strong domains: skipped or stretch-only

Measurable outputs per module:
- YAML manifests
- Runbooks or troubleshooting notes
- Scripts or CLI command logs
- Architecture diagrams for complex tasks

Trainer touchpoint:
- Approve as-is
- Edit modules and sequencing
- Add custom assignments relevant to real work
- Flag modules for live demo evaluation

## Component 3: Training Execution and Hint Bot
Purpose: Guide the trainee through the plan with an always-available AI mentor that teaches without giving away answers.

Trainee experience:
- Current sprint and module list
- Progress indicators (not started, in progress, completed, evaluated)
- Module detail view with resources and deliverables
- Hint Bot side panel

Hint Bot principles:
- Socratic by default (asks guiding questions)
- Hint ladder when stuck:
  - Level 1: abstract direction
  - Level 2: narrowed focus
  - Level 3: near-answer concept clarification (still no full solution)
- Never provides complete solutions, working code, or step-by-step exam answers

Per-module Training Agent:
- Scope: single module only
- Context: module objectives, trainee interaction log, and module-specific memory
- Responsibilities: provide hints, evaluate quizzes, track struggle points

Deliverable submission:
1. Trainee submits artifacts
2. Training Agent checks completeness and flags obvious issues
3. Trainee revises and marks "ready for evaluation"
4. Evaluation Agent scores the deliverable
5. Trainer reviews every module deliverable (per-module human review)
6. Modules flagged for demo go to trainer scheduling

## Component 4: Evaluation and Feedback
Purpose: Assess real learning and CKA readiness with a blend of AI evaluation and human judgment.

Level 1: Module evaluation (continuous)
- Quiz performance
- Deliverable quality (rubric-based)
- Hint usage and struggle metrics
- Trainer scores for live demos
- Trainer review required on every module (approve or request revisions)

Level 2: Sprint review (end of sprint)
- Topics mastered vs weak areas
- Competency deltas
- Recommendation: proceed, revisit, or adjust plan
- Trainer verification required

Level 3: Final evaluation (end of plan)
- Part A: Full-length mock exam (timed, no hints)
- Part B: Capstone challenge (multi-domain scenario)
- Part C: Live demo with trainer using structured rubric
- Part D: Competency delta report (baseline vs final)

Readiness rule:
- Two consecutive mocks meeting the internal quality threshold
- Trainer sign-off on capstone and live demo

Feedback style:
- Direct and blunt feedback is allowed and encouraged.
- Feedback must be actionable and tied to evidence from deliverables and rubrics.

## Supporting Component: Memory System
Purpose: Maintain learning continuity and personalized guidance without leaking context or enabling shortcuts.

Memory layers:
- Short-term (session): current task, recent errors, hints used
- Sprint-level: module progress, persistent misconceptions, time-on-task
- Long-term: baseline profile, domain scores, recurring weaknesses, learning preferences

Memory controls:
- Trainer can view and annotate
- Trainee can request corrections to memory
- Audit trail for major profile changes

## Supporting Component: Orchestrator
Purpose: Manage workflow state, transitions, notifications, and escalation.

Examples:
- Assessment complete -> trigger plan generation -> notify trainer
- Trainer approves plan -> unlock modules
- Sprint complete -> trigger sprint review -> regenerate plan
- Final submission -> trigger evaluation -> notify trainer

## Agent Architecture Summary
- Assessment Agent: initial evaluation per trainee
- Plan Agent: sprint plan creation and adaptation
- Training Agent: module-level mentor and evaluator
- Evaluation Agent: deliverable scoring, sprint reviews, final evaluation
- Orchestrator: workflow coordination and alerts

## Dashboard Views
Trainer dashboard:
- Trainee list with status and progress
- Pending actions: plan reviews, demos, evaluations
- Alerts: stuck trainees, overdue reviews
- Per-trainee deep dive: assessment, plan, scores, notes

Trainee dashboard:
- Competency radar chart
- Sprint plan and module progress
- Active module detail with Hint Bot
- Mock exam scores and readiness tracker
- Final report upon completion
