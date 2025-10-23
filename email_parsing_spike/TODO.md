# Tech Spike — Execution Checklist

## Local setup
- [ ] Create/activate venv
- [ ] `pip install -r requirements.txt`
- [ ] Place a tiny sample `input.mbox` locally (10–50 emails)

## Run
- [ ] `python scripts/mbox_to_csv.py input.mbox out.csv`
- [ ] Inspect `out.csv` — confirm headers & rows
- [ ] Record timing (# msgs processed / seconds)

## Research notes
- [ ] What worked well / pain points
- [ ] OLM → MBOX steps you actually used
- [ ] Edge cases (attachments, HTML-only, encodings)
- [ ] Next steps for Prototype
