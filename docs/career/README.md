# 🎯 Career Intelligence — Tecnocrat

> **Absorbed from:** `Tecnocrat/Job-Hunting-Workflow` (Nov 23, 2025)
> **Architecture:** Part of Tecnocrat Intelligence Layer
> **Status:** Active — Career tooling for entry-level remote dev positions

---

## Purpose

Career intelligence tooling for systematic job application tracking,
interview preparation, and professional outreach. Integrated into the
Tecnocrat profile ecosystem alongside Portfolio, AIOS API, and the
LinkedIn touchpoint.

## Structure

```
docs/career/
├── README.md               ← This file (career hub)
├── workflow.md             ← Step-by-step job-hunting workflow
├── focus.md                ← Strategic focus areas and targeting
├── next-steps.md           ← Immediate action items
├── tips.md                 ← Best practices and privacy guidance
├── templates/
│   ├── application-tracker.md   ← Application log (markdown table)
│   ├── resume-template.md       ← Resume scaffold
│   ├── cover-letter-template.md ← Cover letter scaffold
│   ├── interview-prep.md        ← Interview preparation checklist
│   └── job-post-capture.md      ← Job posting analysis template
└── scripts/
    └── add-tracker-entry.ps1    ← PowerShell tracker automation
```

## Integration Points

| Surface | Connection |
|---------|-----------|
| **docs/cv/** | Actual CV PDFs (source of truth) |
| **ROADMAP Step 20** | Resume/CV auto-generation pipeline |
| **Portfolio** | Live website showcasing projects |
| **LinkedIn** | Professional network touchpoint |
| **aios-trader** | Financial independence complement |

## Workflow

1. **Discover** → Capture job post using `templates/job-post-capture.md`
2. **Prepare** → Tailor resume/cover letter from templates
3. **Apply** → Log in `templates/application-tracker.md`
4. **Interview** → Use `templates/interview-prep.md` checklist
5. **Track** → Update status (Applied → Interviewing → Offer/Rejected)

## Privacy Rules

- Keep this repo **private** — never commit PII
- Store recruiter contacts in encrypted vault, not git
- Use redacted versions for any public sharing
- Prefer `YYYY-MM-DD` date format for consistency

---

*Absorbed into Tecnocrat ecosystem — OS0.6.7.4*
