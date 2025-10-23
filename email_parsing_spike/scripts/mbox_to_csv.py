# scripts/mbox_to_csv.py
import mailbox, csv, sys
from email import policy
from email.message import EmailMessage
from bs4 import BeautifulSoup
from dateutil import parser as dateparser

def body_text(msg: EmailMessage) -> str:
    if msg.is_multipart():
        # Prefer text/plain; fall back to HTML
        for part in msg.walk():
            if part.get_content_disposition() == 'attachment':
                continue
            ctype = part.get_content_type()
            if ctype == 'text/plain':
                return part.get_content().strip()
        for part in msg.walk():
            if part.get_content_disposition() != 'attachment' and part.get_content_type() == 'text/html':
                return BeautifulSoup(part.get_content(), 'html.parser').get_text(' ', strip=True)
        return ""
    # Single part
    payload = msg.get_content()
    if msg.get_content_type() == 'text/html':
        return BeautifulSoup(payload, 'html.parser').get_text(' ', strip=True)
    return payload or ""

def addresses(msg, header):
    from email.utils import getaddresses
    vals = msg.get_all(header, [])
    return ", ".join([addr for _name, addr in getaddresses(vals)])

def run(mbox_path, out_csv):
    mbox = mailbox.mbox(mbox_path, factory=lambda f: EmailMessage(policy=policy.default))
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["date","from","to","cc","bcc","subject","body_chars"])
        w.writeheader()
        for msg in mbox:
            try:
                date_iso = dateparser.parse(msg.get("Date")).isoformat()
            except Exception:
                date_iso = ""
            w.writerow({
                "date": date_iso,
                "from": msg.get("From",""),
                "to": addresses(msg,"To"),
                "cc": addresses(msg,"Cc"),
                "bcc": addresses(msg,"Bcc"),
                "subject": msg.get("Subject",""),
                "body_chars": len(body_text(msg))
            })
    print(f"Wrote {out_csv}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scripts/mbox_to_csv.py INPUT.mbox OUTPUT.csv")
        sys.exit(1)
    run(sys.argv[1], sys.argv[2])
