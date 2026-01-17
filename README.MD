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
### Phase 1 – Build (Active)

**Goal:** Create the smallest deployable production system.

### What exists
- Application code
- Dockerfile
- CI pipeline that builds a Docker image

### What is intentionally missing
- Security scanning
- CD automation
- Multiple environments
- Monitoring and alerts

**Reason:** Working software first, improvement later.

---

## Evolution Plan
This system will evolve through four phases:

1. **Build**  
   Establish a minimal, repeatable delivery system.

2. **Inject Failure & Fix**  
   Intentionally break pipelines and runtime to study failure modes, detection, and recovery.

3. **Observe**  
   Add logs, metrics, and alerts to understand normal, degraded, and failure states.

4. **Trade-off Engineering**  
   Make explicit decisions under constraints such as time, cost, and reliability, and document trade-offs.

---

## Final Mindset
DevOps is not about tools.

It is about learning faster, failing safely, and making better decisions under uncertainty.
