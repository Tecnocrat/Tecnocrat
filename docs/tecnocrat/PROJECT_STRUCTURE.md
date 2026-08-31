# 🏗️ Project Structure Guide

> **Purpose:** Maintain coherence across Tecnocrat ecosystem repositories  
> **Last Updated:** 2025-12-01

---

## ⚠️ Critical Warning: Repository Separation

### The Problem (December 2025)

An accidental `git clone` inside the Tecnocrat repo created a **nested repository**:

```
❌ WRONG STRUCTURE (caused confusion)
c:\dev\Tecnocrat\           ← Profile repo
    └── Portfolio\          ← Cloned INSIDE (nested repo!)
        └── .git\           ← Separate git history
```

**Symptoms:**
- Backup created in wrong location
- Risk of accidentally committing Portfolio files to Tecnocrat
- Git submodule confusion
- Workspace path ambiguity

### The Solution

```
✅ CORRECT STRUCTURE
c:\dev\
    ├── Tecnocrat\          ← GitHub Profile repo (Tecnocrat/Tecnocrat)
    │   ├── README.md       ← Profile landing page
    │   ├── docs\           ← Documentation
    │   ├── Tecnocrat.code-workspace ← Multi-root workspace definition
    │   └── .gitignore      ← Excludes Portfolio/, aios-api/, aios-public/
    │
    ├── Portfolio\          ← Portfolio repo (Tecnocrat/Portfolio)
    │   ├── index.html      ← Main website
    │   ├── styles.css
    │   └── script.js
    │
    ├── aios-api\           ← Vercel API repo (Tecnocrat/aios-api)
    │   ├── app/            ← Next.js API routes
    │   └── lib/            ← Metrics & SVG generators
    │
    └── aios-public\        ← Public Genome repo (Tecnocrat/AIOS-Public-Genome)
        ├── genome/         ← Consciousness axioms
        └── architecture/   ← Public architectural layer
```

### Prevention Rules

1. **Never clone repos inside other repos** unless using git submodules
2. **Always verify working directory** before `git clone`
3. **Check `.gitignore`** includes any local project folders
4. **Use absolute paths** when unsure: `cd c:\dev\Portfolio` not `cd Portfolio`

---

## 📦 Repository Ecosystem

### 1. Tecnocrat/Tecnocrat (Profile)
**Location:** `c:\dev\Tecnocrat\`  
**Purpose:** GitHub profile README and documentation  
**Deploys to:** github.com/Tecnocrat (profile landing)

**Contents:**
- `README.md` - Profile with stats, badges, AIOS architecture
- `docs/` - Technical documentation
- `media/` - Images, icons, diagrams

**References (external, not included):**
- Portfolio badges → `tecnocrat.github.io/Portfolio/`
- Architecture SVG → `tecnocrat-api.vercel.app/api/architecture`
- Dynamic badges → `tecnocrat-api.vercel.app/api/badge/*`

---

### 2. Tecnocrat/Portfolio (Website)
**Location:** `c:\dev\Portfolio\`  
**Purpose:** Personal portfolio website  
**Deploys to:** tecnocrat.github.io/Portfolio/

**Contents:**
- `index.html` - Single-page application
- `styles.css` - Styling with animations
- `script.js` - 3D cube, card stack, interactions
- `surface.js` - Tecnocrat intelligence layer connection

**References (external):**
- Stats cards → Self-hosted github-readme-stats
- Connection indicator → `tecnocrat-api.vercel.app`

---

### 3. Tecnocrat/aios-api (Vercel Infrastructure)
**Location:** `c:\dev\Tecnocrat\aios-api\` or `c:\dev\aios-api\`  
**Purpose:** Dynamic SVG/badge generation API  
**Deploys to:** tecnocrat-api.vercel.app

**Contents:**
- `app/api/` - Next.js API routes
- `lib/config.ts` - Central metrics configuration
- `lib/svg-generator.ts` - Dynamic SVG generation

**Endpoints:**
| Path | Output |
|------|--------|
| `/api` | JSON status + metrics |
| `/api/architecture` | Architecture diagram SVG |
| `/api/badge/[metric]` | Dynamic badge SVG |
| `/api/stats` | Statistics card SVG |

---

### 4. Tecnocrat/AIOS-win (Main Project)
**Location:** Separate development environment  
**Purpose:** Supercell architecture - Windows 11 containerized AI platform  
**Reference:** Architecture terminology source

---

## 🔗 Dependency Graph

```
┌─────────────────────────────────────────────────────────────┐
│                     TECNOCRAT ECOSYSTEM                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌──────────────┐         ┌──────────────────┐            │
│   │  AIOS-win    │────────▶│   aios-api       │            │
│   │  (source)    │ metrics │   (Vercel)       │            │
│   └──────────────┘         └────────┬─────────┘            │
│                                     │                       │
│         ┌───────────────────────────┼───────────────┐      │
│         │                           │               │      │
│         ▼                           ▼               ▼      │
│   ┌──────────────┐         ┌──────────────┐  ┌──────────┐ │
│   │  Tecnocrat   │         │  Portfolio   │  │ External │ │
│   │  (Profile)   │◀───────▶│  (Website)   │  │ Services │ │
│   └──────────────┘  link   └──────────────┘  └──────────┘ │
│         │                         │                │       │
│         ▼                         ▼                ▼       │
│   github.com/         tecnocrat.github.io/   shields.io   │
│   Tecnocrat           Portfolio/             capsule-render│
│                                              github-stats  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛡️ .gitignore Patterns

### Tecnocrat/.gitignore
```gitignore
# Nested repos - keep separate
Portfolio/
aios-api/

# Large files
media/Library/cpp-standard-library-msvc-170.pdf
```

### Portfolio/.gitignore
```gitignore
# Backups
backups/

# OS files
.DS_Store
Thumbs.db
```

---

## ✅ Verification Checklist

Before making changes, verify:

- [ ] Am I in the correct repository? (`git remote -v`)
- [ ] Is this folder at the right level? (sibling to other repos, not nested)
- [ ] Does `.gitignore` exclude local project folders?
- [ ] Will this change affect other repos unintentionally?

---

## 📝 Workspace Configuration

The VS Code / Antigravity workspace (`Tecnocrat.code-workspace`) references all 4 sibling repositories:

```json
{
  "folders": [
    { "name": "⚛ Tecnocrat (GitHub Profile)", "path": "." },
    { "name": "🚀 AIOS API (Vercel Infrastructure)", "path": "../aios-api" },
    { "name": "🌐 Portfolio (Website)", "path": "../Portfolio" },
    { "name": "🧬 AIOS Public (Genome Layer)", "path": "../aios-public" }
  ]
}
```

This way, each repo maintains its independence while being accessible in one workspace.
