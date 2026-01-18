# DevOps Systems Engineering Portfolio

## Core Philosophy
This repository evolves a single production-like system over time.

The goal is not to build isolated DevOps projects, but to learn through:
- automation
- failure
- observability
- decision-making

DevOps here is treated as systems thinking, not tool usage.

---

## System Overview
- Simple HTTP application
- Containerized using Docker
- CI pipeline builds a Docker image on every push

---

## Current Phase
### Phase 2 – Inject Failure & Fix (Active)

The system is intentionally broken to understand how failures are detected,
how long recovery takes, and what changes prevent recurrence.

---

### Phase 1 – Build (Completed)

**Goal:** Create the smallest deployable production system.

**Status:** Completed

**Outcome:**
- A simple Python HTTP application
- Dockerfile to containerize the application
- CI pipeline that:
  - checks out source code
  - runs a sanity test
  - builds a Docker image
- Clear repository structure and documentation

This phase established a stable baseline that can now be safely broken and improved.

---

## Evolution Plan
This system evolves through four phases:

1. **Build (Completed)**  
   Established a minimal, repeatable delivery system.

2. **Inject Failure & Fix (Active)**  
   Intentionally break pipelines and runtime to study failure modes, detection, and recovery.

3. **Observe**  
   Add logs, metrics, and alerts to understand normal, degraded, and failure behavior.

4. **Trade-off Engineering**  
   Make explicit decisions under constraints such as time, cost, and reliability, and document trade-offs.

---

## Next Focus: Phase 2

The system will now be intentionally broken to study:
- how failures are detected
- time to detect and recover (MTTR)
- root causes
- changes that prevent similar failures

Failures and fixes will be documented before moving forward.

---

## Final Mindset
DevOps is not about tools.  
It is about learning faster, failing safely, and making better decisions under uncertainty.
