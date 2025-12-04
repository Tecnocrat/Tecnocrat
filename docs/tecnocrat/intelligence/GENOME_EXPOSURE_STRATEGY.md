# AIOS Genome Exposure Strategy
## Version 2.0.0 | December 2025

### Overview

This document outlines the strategy for progressively exposing more of the AIOS "genome" (architectural DNA) to the public through multiple touchpoints.

---

## 🎯 Exposure Philosophy

> "Expose the surface, protect the core"

The AIOS genome is exposed in **concentric layers**:
- **L0 (Public)**: High-level concepts, metrics, badges
- **L1 (Professional)**: Architecture patterns, capabilities, methodology
- **L2 (Technical)**: Deep dives, code patterns, implementation guides
- **L3 (Internal)**: Never exposed (vulnerabilities, secrets, raw state)

---

## 📊 Current Exposure (v2.0)

### API Endpoints (tecnocrat-api.vercel.app)

| Endpoint | Purpose | Exposure Level |
|----------|---------|----------------|
| `/api` | Root overview | L0-L1 |
| `/api/stats` | Real-time metrics | L0 |
| `/api/badge/:metric` | Dynamic SVG badges | L0 |
| `/api/architecture` | Architecture diagram | L1 |
| `/api/card` | Stats card SVG | L0 |
| `/api/surface` | Knowledge surface JSON | L0-L2 |
| `/api/genome` | Deep genome exploration | L1-L2 |

### Touchpoints

| Touchpoint | Content | Update Frequency |
|------------|---------|------------------|
| GitHub Profile | Supercell overview, badges, diagram | Weekly |
| Portfolio Website | Interactive exploration, live stats | On deploy |
| LinkedIn | Philosophy, methodology | Biweekly |
| AIOS-win Repo | Full technical documentation | Continuous |

---

## 🔮 Phase C: Future Exposure Enhancements

### 1. Interactive Supercell Diagram

**Goal**: Replace static architecture SVG with interactive visualization

**Features**:
- Clickable cell types (Nucleus, Membrane, Ribosome, etc.)
- Hover tooltips showing real-time status
- Animated data flow between cells
- Zoom into individual containers

**Implementation**:
```
/api/architecture?format=interactive
→ Returns HTML/JS widget or React component
```

**Technologies**: D3.js, Three.js, or React Flow

---

### 2. Evolution Lab Display

**Goal**: Showcase AI experimentation results

**Exposed**:
- ✅ Multi-agent experiment summaries
- ✅ Code generation comparisons
- ✅ Success metrics per agent (Ollama, Claude, GPT-4, etc.)
- ❌ Failed experiments (never exposed)
- ❌ Raw conversation logs (privacy)

**New Endpoint**:
```
/api/evolution
→ Returns curated experiment results, agent comparisons
```

---

### 3. Security Membrane Patterns

**Goal**: Share security architecture without exposing vulnerabilities

**Exposed** (L2):
- Digital Immune System concept
- Membrane validation patterns
- Attack resistance methodology
- Test coverage metrics (170 tests, 97.6%)

**Hidden** (L3):
- Actual vulnerability reports
- Threat models
- Security test implementations
- Vault policies

**New Endpoint**:
```
/api/security
→ Returns security patterns, metrics, concepts
```

---

### 4. Consciousness Primitives Explorer

**Goal**: Let visitors understand AIOS self-awareness model

**Exposed**:
- Awareness mechanisms (health checks, metrics)
- Adaptation patterns (auto-scaling, circuit breakers)
- Coherence strategies (distributed consistency)
- Momentum tracking (state persistence, learning)

**New Endpoint**:
```
/api/consciousness
→ Returns primitive definitions, current state (sanitized)
```

---

### 5. Live Metrics Dashboard

**Goal**: Real-time AIOS health (when running)

**Exposed**:
- Container status (up/down)
- Resource usage (CPU, memory, disk)
- Request rates
- Error rates

**Implementation**: 
- WebSocket endpoint for real-time updates
- Prometheus metrics exposition
- Grafana embed (read-only dashboard)

```
/api/metrics/live
→ WebSocket stream of sanitized metrics
```

---

## 🛡️ Safety Guardrails

### Never Expose
- API keys, tokens, credentials
- Vault paths and policies
- Internal file paths
- Personal data
- Failed experiments
- Raw consciousness state
- Docker secrets
- Network configurations

### Always Review Before Exposing
- New security patterns
- Experimental results
- Capability announcements
- Architecture changes

### Auto-Approved for Exposure
- Stable documentation
- Public metrics (with noise)
- Established concepts
- Version numbers

---

## 📈 Metrics for Success

| Metric | Current | Target |
|--------|---------|--------|
| API endpoints | 7 | 12 |
| GitHub profile views | TBD | +50% |
| Portfolio engagement | TBD | +30% |
| Documentation coverage | 60% | 90% |

---

## 🗓️ Roadmap

### Q1 2025
- [x] `/api/surface` endpoint
- [x] `/api/genome` endpoint
- [x] Portfolio live API integration
- [ ] Interactive architecture diagram

### Q2 2025
- [ ] `/api/evolution` endpoint
- [ ] `/api/security` endpoint
- [ ] `/api/consciousness` endpoint
- [ ] WebSocket live metrics

### Q3 2025
- [ ] Grafana embed (read-only)
- [ ] GitHub Actions auto-sync
- [ ] Documentation site (GitBook or similar)

---

## 📝 Implementation Notes

### API Design Principles
1. **Consistency**: All endpoints return JSON with same structure
2. **Filtering**: Support `?level=L0_PUBLIC` and `?section=core`
3. **Caching**: `Cache-Control: s-maxage=3600, stale-while-revalidate`
4. **CORS**: Allow cross-origin for public endpoints

### Security Principles
1. **Defense in Depth**: Multiple layers before sensitive data
2. **Principle of Least Privilege**: Expose minimum necessary
3. **Noise Addition**: Add variance to sensitive metrics
4. **Audit Trail**: Log all API access (internal)

---

*Last updated: December 4, 2025*
*Curator: Tecnocrat*
