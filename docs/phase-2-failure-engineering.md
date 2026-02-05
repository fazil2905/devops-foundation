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

---

## Phase 2.3 – Slow CI Pipeline (Artificial Delay)

### Failure Injected
An artificial delay was intentionally introduced into the CI pipeline
to simulate a slow build process.

The pipeline continued to succeed, but feedback to developers
was significantly delayed.

---

### Detection
- Detected by: Manual observation
- Detection point: CI execution duration in GitHub Actions
- Signal: Pipeline step taking significantly longer than expected

---

### Time Metrics
- Time to detect: Immediate
- Time to recover: ~2 minutes

---

### Root Cause
A non-essential blocking step was added to the CI workflow,
introducing latency without providing validation or safety benefits.

This increased pipeline duration while delivering no additional value.

---

### Fix Applied
The artificial delay was removed from the CI workflow.

Pipeline execution time returned to normal without
impacting build correctness or reliability.

---

### Prevention / Optimization
- Treat slow pipelines as reliability issues
- Keep CI feedback fast to encourage frequent commits
- Review pipeline steps for unnecessary blocking behavior

---

### Outcome
CI feedback speed was restored.

Developer feedback loops improved, and the pipeline
returned to a fast, predictable execution time.

---

## Phase 2.4 – Broken Docker Build (Invalid Build Context)

### Failure Injected
The Docker build was intentionally broken by modifying the `Dockerfile`
to reference a non-existent file during the `COPY` step.

This caused the Docker image build to fail during the CI pipeline.

---

### Detection
- Detected by: CI pipeline (GitHub Actions)
- Detection point: Docker build step
- Signal: Docker build error indicating missing file in build context

---

### Time Metrics
- Time to detect: ~5–10 seconds
- Time to recover: ~5 minutes

---

### Root Cause
The Dockerfile assumed the presence of a file (`app/main.py`)
that did not exist in the repository.

This created a mismatch between the application structure
and the Docker build context.

---

### Fix Applied
The Dockerfile was updated to reference the correct application path.

The build context and Dockerfile were aligned with
the actual repository structure.

The CI pipeline was re-run and completed successfully.

---

### Prevention / Optimization
- Keep Dockerfiles tightly aligned with repository structure
- Treat Docker build failures as first-class CI failures
- Prefer explicit paths over assumptions in build steps

---

### Outcome
The CI pipeline correctly detected the broken Docker build
and prevented an invalid image from being produced.

After the fix, Docker builds became reliable and predictable.

---

## Phase 2.5 – Flaky CI Behaviour

### Failure Injected
Non-deterministic behavior was intentionally introduced into the CI pipeline,
causing the same code to sometimes pass and sometimes fail without changes.

This resulted in inconsistent CI outcomes across multiple runs.

---

### Detection
- Detected by: Re-running the same CI workflow
- Detection point: Python sanity test step
- Signal: Identical commits producing different CI results (pass/fail)

---

### Time Metrics
- Time to detect: Immediate after re-runs
- Time to recover: ~5 minutes

---

### Root Cause
The CI sanity test contained non-deterministic logic.

Pipeline success depended on runtime conditions rather than
explicit, repeatable validation rules.

This made CI behavior unreliable and unpredictable.

---

### Fix Applied
The non-deterministic logic was removed.

CI validation was made deterministic so that:
- The same code always produces the same result
- CI outcomes depend only on code changes

---

### Prevention / Optimization
- Ensure CI tests are deterministic
- Avoid randomness or timing-based logic in pipelines
- Treat flaky CI as a reliability incident, not a minor bug
- Prefer clear failures over intermittent ones

---

### Outcome
CI behavior became stable and predictable.

Developer trust in the pipeline was restored,
and failures once again reliably indicated real problems.

---

## Phase 2.6 – Incorrect Port Configuration

### Failure Injected
The application was configured to listen on one port
while logging a different port number at startup.

The server was running, but users could not access it
using the logged port.

---

### Detection
- Detected by: Manual testing in browser
- Detection point: Attempting to access logged port
- Signal: Service unreachable despite app running

---

### Time Metrics
- Time to detect: ~2 minutes
- Time to recover: ~5 minutes

---

### Root Cause
Mismatch between the configured server port
and the port printed in application logs.

This created misleading observability.

---

### Fix Applied
The server port configuration and log message
were aligned to use the same port.

Application became accessible immediately.

---

### Prevention / Optimization
- Keep configuration and logs consistent
- Treat logs as part of system reliability
- Validate port bindings during testing

---

### Outcome
Application accessibility restored.

This highlighted that incorrect logging
can be an operational failure even
when the system is technically running.

---

## Phase 2.7 – Container Crash on Startup

### Failure Injected
The application was intentionally forced to exit
immediately at startup using `sys.exit(1)`.

This simulated a container that starts and
crashes instantly.

---

### Detection
- Detected by: CI pipeline
- Detection point: Python sanity test
- Signal: Immediate exit with code 1

---

### Time Metrics
- Time to detect: Immediate
- Time to recover: ~3 minutes

---

### Root Cause
Application terminated itself during initialization,
preventing the server from starting.

---

### Fix Applied
The forced exit was removed.

The application resumed normal startup behavior.

---

### Prevention / Optimization
- Avoid early exits in startup logic
- Validate startup paths in CI
- Treat crash loops as critical failures

---

### Outcome
Application stability restored.

This demonstrated how startup crashes
lead to container restart loops in production.
