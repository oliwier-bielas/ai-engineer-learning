# Python Basics 01 – Inbox
 
First exercise of **Phase 1 (Python)** of my AI Engineer learning path.
A small command-line program that loads emails from a JSON file, validates them and filters them.
 
## Task
 
Load a list of emails from `data/emails.json`, turn them into objects and answer three questions:
 
1. How many valid emails are in the inbox?
2. Which emails are urgent (`"pilne"` in the subject, case-insensitive)?
3. Who sent the unread emails?
Requirements:
 
- `Email` as a `@dataclass` with type hints
- loading emails from a JSON file passed as a path
- filtering by topic, case-insensitive
- unread emails selected with a list comprehension
- invalid emails (missing field or empty value) are skipped with a warning instead of crashing the program
- unit tests with `pytest`
`data/emails.json` contains 6 emails, 2 of them invalid on purpose to show validation at work.
 
Expected output:
 
```
Warning: skipping invalid email (missing field: tresc)
Warning: skipping invalid email (missing field: nadawca)
All emails: 4
Urgent: ['Pilne: spotkanie jutro', 'Pilne: poprawka faktury']
Unread emails from: ['anna@firma.pl', 'sklep@promo.pl', 'anna@firma.pl']
```
 
## Learning goals
 
| Topic | What I practised |
| --- | --- |
| Python syntax | coming from JS/TS: indentation, `None`, truthiness, snake_case (PEP 8) |
| Data structures | lists, dicts, iterating with `.items()`, the `in` operator |
| List comprehensions | replacing `filter` + `lambda` + `append` loops |
| Classes | `__init__`, `self`, "private" `_attributes`, read-only `@property` returning a copy |
| Dataclasses | `@dataclass` as a typed data model |
| Type hints | annotating arguments and return types, `-> None` |
| Modules | splitting code into `models`, `inbox`, `exceptions` and `app` |
| Files and JSON | `with open(..., encoding="utf-8")`, `json.load`, `pathlib.Path` |
| Exceptions | a custom `InvalidEmailError`, `raise`, `try/except` inside a loop |
| Testing | `pytest`, fixtures, separate test data, isolated tests |
| Tooling | virtual environments (`venv`), `requirements.txt`, git and Conventional Commits |
 
## Project structure
 
```
python-basics-01/
├── data/
│   └── emails.json         # input data
├── tests/
│   ├── data/
│   │   └── test_emails.json
│   └── test_inbox.py
├── app.py                  # entry point
├── models.py               # Email dataclass
├── inbox.py                # Inbox: loading, validation, filtering
├── exceptions.py           # InvalidEmailError
├── pytest.ini
└── requirements.txt
```
 
## How to run
 
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
 
python app.py
```
 
## How to test
 
```bash
python -m pytest
```
 
The test data in `tests/data/test_emails.json` contains 6 emails: 4 valid and 2 invalid (one with an empty value, one with a missing field). Uppercase and lowercase urgent subjects are mixed to check that filtering is case-insensitive.
 
## Data format
 
```json
{
  "nadawca": "anna@firma.pl",
  "temat": "Pilne: poprawka faktury",
  "tresc": "Błąd w kwocie.",
  "przeczytany": false
}
```
 
All four fields are required. An email with a missing field or an empty value is skipped.
 