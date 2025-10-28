# Tech Spike: Email Parsing Libraries
<hr>
**Owner:** Sophia DellaPenna  
**Date started:** 2025-10-23

## Goal
Find the best Python approach to parse local email archives into structured data. Verify feasibility for `.mbox` now and document the path for `.olm` (conversion to mbox).

<hr>

## Python Libraries to Parse Emails and Inboxes
Below are Python packages and standard libraries that can parse and extract email data.

- **email** – Standard library for parsing headers, subjects, body text, and attachments.
- **mailbox** – Can read `.mbox` and `.Maildir` files; returns email messages as objects.
- **mailparser** – Third-party package that simplifies extracting metadata (To/From/Date).
- **extract-msg** – Reads `.msg` files (Outlook).
- **olmreader** or **pyolm** – Open-source tools for parsing `.olm` (Mac Outlook) files.
- **chardet** – Detects character encodings for mixed email data.

<hr>

## Data You Can Expect to Extract
Typical data fields accessible from these libraries:

- Date and time the message was sent or received  
- Sender and recipient addresses (`To`, `From`, `Cc`, `Bcc`)  
- Subject line and body text  
- Attachments (filename, size, type)  
- Message-ID, reply chain, or thread information  
- Character encoding and content type  

<hr>

## How to Parse Email Files (High-Level Overview)
```python
import mailbox
```
<hr>

##Open an .mbox file and read its contents
mbox = mailbox.mbox('inbox.mbox')
for message in mbox:
    print("From:", message['from'])
    print("Subject:", message['subject'])

<hr>

## To handle .olm Files, use: 
pip install pyolm

<hr> ```

## Findings
- `.mbox` parsing works well with the built-in `mailbox` + `email` libraries.
- `.olm` files are proprietary — best path is **convert `.olm` → `.mbox`** first.
- Key helper packages improve reliability:
  - `chardet` for encoding
  - `BeautifulSoup` for HTML-to-text
  - `dateutil` for date normalization

## Limitations
- `.olm` parsing is less mature and may require conversion to `.mbox`.
- Large mailbox files (>1GB) can slow processing.
- Some emails may contain malformed headers or unusual encodings.

<hr>


## Next Steps
- Run `scripts/mbox_to_csv.py` on a small `.mbox` test file.
- Document conversion steps for `.olm` in `docs/olm-to-mbox.md`.
- Write a short “Prototype” script to extract more fields.

<hr>

## Example of Working Command
```bash
python scripts/mbox_to_csv.py sample.mbox output.csv
```

<hr>

## Deliverable (Success Criteria)
- A short **README.md** (this file) summarizing which Python libraries to use and why.
- A minimal working script that can open a sample **.mbox** and extract basic fields.

<hr>

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

<hr>

## This was generated with the help of ChatGPT
