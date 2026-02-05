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
- Failures intentionally injected and documented
- Observability being added incrementally

---

## Current Phase

### Phase 3 – Observe (Active)

The focus is now on understanding system behavior before automating decisions.

This phase introduces:
- meaningful application logs
- basic health signals
- simple metrics
- awareness of normal vs abnormal behavior

Goal:
Understand the system before trying to optimize or scale it.

---

## Phase 1 – Build (Completed)

**Goal:** Create the smallest deployable production system.

**Outcome:**
- A simple Python HTTP application
- Dockerfile to containerize the application
- CI pipeline that:
  - checks out source code
  - runs a sanity test
  - builds a Docker image
- Clear repository structure and documentation

This phase established a stable baseline that could be safely evolved.

---

## Phase 2 – Inject Failure & Fix (Completed)

**Goal:** Learn how the system fails and reduce recovery pain.

Failures intentionally introduced included:
- application startup failures
- runtime crashes
- slow CI pipelines
- flaky CI behavior
- broken Docker builds
- configuration and port mismatches
- container crash scenarios

For each failure:
- detection method was observed
- time to detect and recover was noted
- root cause was identified
- fixes and prevention ideas were documented

This phase built intuition around reliability and recovery.

---

## Evolution Plan

This system evolves through four phases:

1. **Build (Completed)**  
   Established a minimal, repeatable delivery system.

2. **Inject Failure & Fix (Completed)**  
   Studied failure modes, detection, and recovery.

3. **Observe (Active)**  
   Add logs, metrics, and simple signals to understand behavior.

4. **Trade-off Engineering (Planned)**  
   Make explicit decisions under constraints such as time, cost, and reliability.

---

## Documentation Approach
Each phase includes written documentation covering:
- what changed
- what failed
- how it was detected
- how it was fixed
- what was learned

The focus is on learning, not just building.

---

## Final Mindset
DevOps is not about tools.  
It is about learning faster, failing safely, and making better decisions under uncertainty.
