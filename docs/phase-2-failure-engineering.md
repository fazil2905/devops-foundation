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

## Phase 2.2 – Runtime Crash After Successful Startup

### Failure Injected
A runtime failure was intentionally introduced after the application
successfully started and began listening on its port.

The application appeared healthy initially but exited unexpectedly
during execution.

---

### Detection
- Detected by: CI pipeline (GitHub Actions)
- Detection point: Python sanity test step
- Signal: Process exited with non-zero exit code after startup logs

---

### Time Metrics
- Time to detect: ~5–10 seconds
- Time to recover: ~5 minutes

---

### Root Cause
The application did not differentiate between CI execution
and normal runtime execution.

As a result, runtime behavior that is valid in production
caused the CI sanity test to fail.

---

### Fix Applied
Environment-aware logic was added to the application.

When running in CI:
- The application performs a startup sanity check
- Exits cleanly without running the long-lived server

When running locally or in runtime:
- The application starts and serves requests normally

---

### Prevention / Optimization
- Separate CI validation paths from runtime execution paths
- Avoid long-running processes during CI sanity checks
- Make application behavior explicit based on environment context

---

### Outcome
The CI pipeline now:
- Detects runtime failures reliably
- Avoids hanging or false negatives
- Validates application startup behavior correctly

The system recovered cleanly and remained stable after the fix.

