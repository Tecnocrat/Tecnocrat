# Application Tracker

Log each application and follow up. This table converts easily to CSV.

| Company | Role | Location | Link | Applied Date | Status | Recruiter | Follow-up Date | Notes |
|---|---|---|---|---|---|---|---|---|
| Example Co | Junior Dev | Remote | https://example.com | 2025-11-23 | Applied | recruiter@example.com | 2025-11-30 | Tailored resume + cover letter |

## Status Labels

- **Interested** — Saved, reviewing fit
- **Applied** — Application submitted
- **Interviewing** — In interview process
- **Offer** — Received offer
- **Rejected** — Application declined
- **Archived** — No longer pursuing

## Conventions

- Date format: `YYYY-MM-DD` (e.g., 2025-11-23)
- Use status values from the list above for consistency
- Keep recruiter contact details minimal — encrypt sensitive info
- Remove personal phone numbers before sharing

## Quick Add (PowerShell)

```powershell
.\scripts\add-tracker-entry.ps1 -Company 'Example Co' -Role 'Junior Dev' -AppliedDate '2025-11-23' -Link 'https://example.com' -Notes 'Tailored resume'
```
