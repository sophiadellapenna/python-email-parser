# Tech Spike: Email Parsing Libraries

**Owner:** Sophia DellaPenna  
**Date started:** 2025-10-23

## Goal
Find the best Python approach to parse local email archives into structured data. Verify feasibility for `.mbox` now and document the path for `.olm` (conversion to mbox).

## Deliverable (Success Criteria)
- A short **README.md** (this file) summarizing which Python libraries to use and why.
- A minimal working script that can open a sample **.mbox** and extract basic fields.

## Recommendation (TL;DR)
- Use Python stdlib **`mailbox`** + **`email`** for parsing `.mbox`/`.eml`.
- Add helpers: **`python-dateutil`** (dates), **`beautifulsoup4`** (HTML→text), **`chardet`** (encoding).
- Optional convenience: **`mail-parser`**.
- **`.olm`** is proprietary → **export/convert to `.mbox`** using Outlook for Mac or a converter, then parse.

## Install
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the tiny demo
```bash
python scripts/mbox_to_csv.py /path/to/input.mbox out.csv
```

## Notes to capture while you spike
- Which libraries worked well and why
- Any `.olm` → `.mbox` steps you followed (screenshots helpful)
- Edge cases: encodings, HTML-only messages, attachments
- Performance observations on larger mailboxes
