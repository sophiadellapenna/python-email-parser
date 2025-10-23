# OLM to MBOX (Conversion Notes)

OLM archives (Outlook for Mac) are proprietary. The recommended approach is to export/convert to `.mbox` and then parse:

## Option A — Outlook for Mac export
1) Open Outlook for Mac → File → Export…  
2) Choose **Mail** → export to **.olm** (if you already have .olm, import it).  
3) Create a new mailbox in Apple Mail → Import `.olm` into Apple Mail (via Outlook/IMAP or intermediate).  
4) From Apple Mail, select the mailbox → **Mailbox > Export Mailbox…** → saves a `.mbox` folder.

## Option B — Use a converter tool
Search for "olm to mbox converter" (CLI/GUI). Verify on a small sample before full conversion.

Record exactly what you did and any errors so we can reproduce.
