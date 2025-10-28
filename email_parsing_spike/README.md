# Tech Spike: Email Parsing Libraries

**Owner:** Sophia DellaPenna  
**Date started:** 2025-10-23

## Goal
Find the best Python approach to parse local email archives into structured data. Verify feasibility for `.mbox` now and document the path for `.olm` (conversion to mbox).

## Libraries Reviewed
| Library | Purpose | Pros | Cons | Verdict |
|----------|----------|------|------|----------|
| `mailbox` (stdlib) | Read `.mbox` files | Built-in, stable, easy to use | Low-level API | ✅ Use |
| `email` (stdlib) | Handle message structure | Robust, standard | Needs helpers for HTML | ✅ Use |
| `mail-parser` | Convenience wrapper | Fast for attachments/body | Adds dependency | Optional helper |
| `beautifulsoup4` | Strip HTML → text | Cleans body text | Needs parser library | ✅ Use |
| `chardet` | Detect encodings | Fixes bad charsets | Not perfect | ✅ Use |
| `python-dateutil` | Parse dates | Timezone-safe | — | ✅ Use |
| `extract-msg` | Parse Outlook `.msg` | Handles .msg files | Not `.olm`/`.mbox` | ❌ Skip for now |

## Findings
- `.mbox` parsing works well with the built-in `mailbox` + `email` libraries.
- `.olm` files are proprietary — best path is **convert `.olm` → `.mbox`** first.
- Key helper packages improve reliability:
  - `chardet` for encoding
  - `BeautifulSoup` for HTML-to-text
  - `dateutil` for date normalization

## Next Steps
- Run `scripts/mbox_to_csv.py` on a small `.mbox` test file.
- Document conversion steps for `.olm` in `docs/olm-to-mbox.md`.
- Write a short “Prototype” script to extract more fields.

---

### Example of Working Command
```bash
python scripts/mbox_to_csv.py sample.mbox output.csv




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

## This was generated using ChatGPT
