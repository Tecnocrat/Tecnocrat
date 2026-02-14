param (
    [string]$Company,
    [string]$Role,
    [string]$Location = 'Remote',
    [string]$Link = '',
    [string]$AppliedDate,
    [string]$Status = 'Applied',
    [string]$Recruiter = '',
    [string]$FollowUpDate = '',
    [string]$Notes = ''
)

# Build Markdown table row
$line = "| $Company | $Role | $Location | $Link | $AppliedDate | $Status | $Recruiter | $FollowUpDate | $Notes |"

# Append to tracker
$trackerPath = Join-Path $PSScriptRoot "..\templates\application-tracker.md"
Add-Content -Path $trackerPath -Value $line
Write-Output "Added: $line"
