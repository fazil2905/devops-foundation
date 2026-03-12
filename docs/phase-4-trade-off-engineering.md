## Phase 4.1 – Rate Limiting Trade-off

### Problem
The application currently accepts every incoming request.

Under high traffic bursts, even a simple service can become unstable due to:
- excessive CPU usage
- request queue buildup
- degraded response time
- potential application failure

A decision needed to be made on how the system should behave under heavy load.

---

### Options Considered

**Option 1 – Accept all requests**

Pros:
- No request rejection
- Maximum availability to users

Cons:
- High risk of system overload
- Unpredictable latency
- Potential full service failure

---

**Option 2 – Introduce rate limiting (Chosen)**

Pros:
- Protects system stability
- Prevents resource exhaustion
- Predictable system behavior under load

Cons:
- Some legitimate requests may be rejected
- Reduced short-term availability

---

### Decision
A simple rate limiting mechanism was implemented.

The system now:
- tracks request timestamps
- limits the number of requests allowed in a short time window
- returns **HTTP 429 (Too Many Requests)** when the limit is exceeded

This prioritizes **system stability over accepting unlimited traffic**.

---

### Trade-off
The chosen design intentionally sacrifices:

**Immediate availability**

in favor of:

**System reliability and predictable performance**

Rejecting some requests early prevents the system from degrading
or crashing under excessive load.

---

### Implementation
A sliding window rate limiter was implemented using:

- request timestamp tracking
- configurable request window
- maximum request threshold

When the request limit is exceeded:

HTTP 429 is returned.

---

### Outcome
The system now behaves predictably during traffic bursts.

Instead of slowing down or failing completely, the application
protects itself by rejecting excess requests.

This demonstrates a common production trade-off in distributed systems:

**controlled rejection is often better than uncontrolled failure.**