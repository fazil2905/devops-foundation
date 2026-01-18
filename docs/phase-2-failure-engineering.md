# Phase 2 – Inject Failure, Fix, Optimize

## Purpose
The goal of Phase 2 is to intentionally introduce failures into the system
to understand how it behaves under stress, how quickly failures are detected,
and how painful recovery is.

This phase focuses on learning from failure, not avoiding it.

---

## Phase 2.1 – Application Startup Failure

### Failure Injected
An intentional startup error was introduced into the application by referencing
an undefined variable during application initialization.

This caused the application to crash immediately on execution.

---

### Detection
- Detected by: CI pipeline (GitHub Actions)
- Detection point: Python sanity test step
- Signal: Python traceback and non-zero exit code

---

### Time Metrics
- Time to detect: ~5 seconds
- Time to recover: ~5 minutes

---

### Root Cause
Invalid application code caused a runtime exception during startup,
preventing the process from initializing successfully.

---

### Fix Applied
The invalid startup code was removed.
The application was restored to a clean startup path.
CI was re-run and passed successfully.

---

### Prevention / Optimization
- Keep fast startup sanity checks in CI
- Fail early before Docker build or deployment stages

---

### Outcome
The CI pipeline successfully detected the failure and prevented
a broken build from progressing further.

---

## Phase 2.2 – (Planned)
Future experiments will include:
- Broken Docker builds
- CI misconfigurations
- Slow pipelines
- Container crash loops
- Resource exhaustion scenarios
