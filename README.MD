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
- Observability implemented incrementally
- Health and degradation states simulated

---

## Current Phase

### Phase 4 – Trade-off Engineering (Active)

The focus now shifts from building and observing the system to making deliberate engineering decisions under constraints.

This phase will introduce:
- performance vs reliability trade-offs
- cost vs stability considerations
- operational decision documentation
- controlled system changes with measurable impact

Goal:
Engineer decisions, not just features.

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

This phase established a stable baseline.

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

Each failure was:
- detected
- analyzed
- documented
- resolved
- optimized for prevention

This phase built reliability intuition.

---

## Phase 3 – Observe (Completed)

**Goal:** Understand system behavior before optimizing or scaling.

Observability improvements included:
- Structured logging with timestamps and levels
- Request counter metric
- Uptime tracking
- Dedicated `/health` endpoint
- Degradation detection via load thresholds
- Automatic unhealthy state transition

The system can now distinguish:
- Healthy
- Busy
- Degrading
- Unhealthy

This phase established behavioral visibility.

---

## Evolution Plan

This system evolves through four structured phases:

1. **Build (Completed)**  
   Established a minimal, repeatable delivery system.

2. **Inject Failure & Fix (Completed)**  
   Studied failure modes and recovery behavior.

3. **Observe (Completed)**  
   Implemented logs, metrics, health signals, and degradation detection.

4. **Trade-off Engineering (Active)**  
   Introduce constraints and document engineering decisions.

---

## Documentation Approach
Each phase includes structured documentation covering:
- what changed
- why it changed
- how it was detected
- impact on the system
- trade-offs introduced
- lessons learned

The repository is designed as a learning artifact, not just a codebase.

---

## Final Mindset
DevOps is not about tools.  
It is about understanding systems, failing safely, observing clearly, and making better decisions under uncertainty.