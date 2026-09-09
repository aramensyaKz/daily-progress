# Daily Progress

This repository records small, meaningful learning and development improvements.

## Structure

- `journal/` contains dated progress notes.
- `notes/` contains reusable explanations and guidelines.
- `tools/new_entry.py` creates a structured journal entry without overwriting an existing one.
- `tests/` verifies the journal tooling.
- Each entry describes what was learned, built, fixed, or verified.

Automated updates must contain useful content. Empty commits and backdated activity are not allowed.

## Create an entry

Run the generator from the repository root:

```powershell
python tools/new_entry.py `
  --topic "Python file safety" `
  --summary "Explored exclusive file creation and verified overwrite protection."
```

The command creates a dated Markdown template in `journal/`. Complete its
Result and Verification sections before committing it. The command fails if an
entry with the same date and topic already exists.

## Run checks

```powershell
python -m unittest discover -s tests -v
```
