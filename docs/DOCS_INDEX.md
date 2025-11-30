# 📚 Tecnocrat Documentation Index
## Navigation Hub for All Documentation

> **Last Updated:** 2025-11-30  
> **Version:** 1.0.0

---

## 🗂️ Repository Structure

```
Tecnocrat/
├── README.md                        ← GitHub Profile (public landing page)
├── DOCS_INDEX.md                    ← This file (documentation hub)
├── .gitignore
├── Tecnocrat.code-workspace
│
├── docs/
│   ├── sources/                     ← External project documentation
│   │   └── AIOS/                    ← AIOS project references
│   │       ├── AIOS_CORE.hydro      ← Hydrolang core definition
│   │       └── AIOS_README.md       ← AIOS full documentation
│   │
│   └── tecnocrat/                   ← Tecnocrat intelligence system
│       ├── ARCHITECTURE.md          ← System design (formerly blueprint)
│       ├── ROADMAP.md               ← Implementation tasks (formerly tasklist)
│       │
│       └── intelligence/            ← Intelligence layer definitions
│           ├── TECNOCRAT_CORE.hydro ← Hydrolang definition of Tecnocrat
│           │
│           ├── manifests/           ← Declarative configurations
│           │   ├── exposed_surface.yaml
│           │   ├── content_pipeline.yaml
│           │   └── touchpoints.yaml
│           │
│           └── context/             ← Runtime state & guidelines
│               ├── persona.md
│               └── current_surface.md
│
└── media/
    ├── icons/                       ← SVG/PNG icons
    ├── banners/                     ← Profile banners
    └── diagrams/                    ← Architecture diagrams
```

---

## 🧭 Quick Navigation

### Core Documents

| Document | Purpose | Path |
|----------|---------|------|
| **GitHub Profile** | Public landing page | [`README.md`](../README.md) |
| **Architecture** | Tecnocrat system design | [`docs/tecnocrat/ARCHITECTURE.md`](tecnocrat/ARCHITECTURE.md) |
| **Roadmap** | Implementation tasks | [`docs/tecnocrat/ROADMAP.md`](tecnocrat/ROADMAP.md) |

### Intelligence Layer

| Document | Purpose | Path |
|----------|---------|------|
| **Tecnocrat Core** | Hydrolang definition | [`TECNOCRAT_CORE.hydro`](tecnocrat/intelligence/TECNOCRAT_CORE.hydro) |
| **Persona** | Voice & identity guide | [`persona.md`](tecnocrat/intelligence/context/persona.md) |
| **Knowledge Surface** | Current exposure state | [`current_surface.md`](tecnocrat/intelligence/context/current_surface.md) |

### Manifests

| Manifest | Purpose | Path |
|----------|---------|------|
| **Exposed Surface** | What AIOS knowledge is public | [`exposed_surface.yaml`](tecnocrat/intelligence/manifests/exposed_surface.yaml) |
| **Content Pipeline** | Transformation rules | [`content_pipeline.yaml`](tecnocrat/intelligence/manifests/content_pipeline.yaml) |
| **Touchpoints** | Platform configurations | [`touchpoints.yaml`](tecnocrat/intelligence/manifests/touchpoints.yaml) |

### Source References

| Document | Purpose | Path |
|----------|---------|------|
| **AIOS Core** | Hydrolang v0.3.0 reference | [`AIOS_CORE.hydro`](sources/AIOS/AIOS_CORE.hydro) |
| **AIOS README** | Full AIOS documentation | [`AIOS_README.md`](sources/AIOS/AIOS_README.md) |

---

## 📁 Folder Purposes

### `docs/sources/`
External project documentation that Tecnocrat **references but doesn't own**. These are copies/mirrors of docs from other repositories (like AIOS) that inform Tecnocrat's knowledge surface.

### `docs/tecnocrat/`
The **Tecnocrat intelligence system** itself—architecture, roadmap, and the intelligence layer that manages public exposure of AIOS.

### `docs/tecnocrat/intelligence/`
The **core intelligence infrastructure**:
- **Hydrolang definition** of Tecnocrat as Observer
- **Manifests** that declare what's exposed, how content transforms, and platform configs
- **Context** files that track persona and current state

### `media/`
Visual assets for GitHub profile and documentation:
- **icons/** - Favicons, logos
- **banners/** - Profile headers
- **diagrams/** - Architecture visualizations

---

## 🔄 Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| **Folders** | lowercase, hyphenated | `docs/tecnocrat/` |
| **Documents** | UPPERCASE for major docs | `ARCHITECTURE.md` |
| **Configs** | snake_case | `exposed_surface.yaml` |
| **Hydrolang** | UPPERCASE_CORE.hydro | `TECNOCRAT_CORE.hydro` |

---

## 🎯 Document Lifecycle

```
AIOS (source) → docs/sources/AIOS/ → Tecnocrat reads
                                           ↓
                              docs/tecnocrat/intelligence/
                                           ↓
                              manifests define exposure
                                           ↓
                              README.md, Portfolio, LinkedIn
```

---

*"Documentation is the knowledge surface of the codebase."*
