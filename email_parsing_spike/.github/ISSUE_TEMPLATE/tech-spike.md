---
name: Tech Spike — Email Parsing
about: Use this for the 'Tech Spike: Email Parsing Libraries' work
title: "[Spike] Email Parsing Libraries"
labels: spike, emails
assignees: ''
---

## Purpose
As a developer, I want to know which Python libraries and approaches exist to parse and extract information from email data (mbox/olm).

## Tasks
- [ ] Survey libraries (`mailbox`, `email`, `mail-parser`, `beautifulsoup4`, `chardet`, `dateutil`)
- [ ] Verify `.mbox` parsing on a small sample
- [ ] Document `.olm` → `.mbox` conversion path
- [ ] Note risks/mitigations (encodings, HTML-only, large files)
- [ ] Write findings in README
- [ ] Commit and push results

## Acceptance Criteria
- [ ] README lists chosen libs and why
- [ ] Minimal script runs on sample `.mbox` and produces a CSV
- [ ] Clear instructions for `.olm` conversion
