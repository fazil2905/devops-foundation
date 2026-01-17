# Phase 1 – Build

## Purpose

The goal of Phase 1 is to create the smallest possible system that can be built and run reliably.

This phase focuses on getting a working baseline before adding complexity.  
Nothing in this phase is optimized, hardened, or production-ready by design.

---

## What Exists

- A simple Python HTTP application
- A Dockerfile to containerize the application
- A CI pipeline that builds the Docker image on every push

This is the minimum required to call the system “deployable”.

---

## Key Decisions

- Chose a very small HTTP server to keep the focus on system behavior, not application logic
- Used a single Dockerfile instead of advanced or multi-stage builds
- CI only validates that the image builds successfully

These decisions reduce moving parts and make failures easier to understand later.

---

## Intentional Omissions

The following were intentionally not implemented in Phase 1:

- No security scanning
- No image registry push
- No deployment automation
- No monitoring or alerting
- No multiple environments

Reason:  
A stable baseline is more valuable than premature optimization.

---

## Completion Criteria

Phase 1 is considered complete when:

- Any code push triggers CI automatically
- The Docker image builds successfully every time
- The application can be run locally or inside a container without manual fixes

All of the above are currently met.

---

## Known Limitations

- The system is not resilient to failures
- Crashes are not handled
- There is no visibility into runtime behavior

These limitations are intentional and will be addressed in later phases.
