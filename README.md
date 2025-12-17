# Vlad Translator (CLI)

A simple yet growing **Command Line Translator** built with **Python**.
This project is intentionally developed step by step to practice real-world Python skills.

This repository represents a **learning journey**, not just a finished tool.

---

## Current Features

* CLI-based translator
* Interactive text translation
* Supported languages:

  * Indonesia (`id`)
  * English (`en`)
  * Japanese (`ja`)
  * Korean (`ko`)
  * Russian (`ru`)
* Input validation:

  * No empty input
  * No same source & target language
* Translation history feature

  * Stores every translation session
  * Prevents history overwrite using incremental keys
  * Displays history in a clean, table-like format
* Clean, readable, and procedural code
* Lightweight & beginner-friendly

---

## Latest Update

* Fixed translation history overwrite issue
* Implemented incremental counter-based history storage (temporary solution)
* Added formatted history display with word wrapping
* Code structure prepared for future refactor (list-based history)

---

## Tech Stack

* Python 3
* `deep-translator`
* Python standard library:

  * `textwrap`
  * `itertools`

---

## How to Run

```bash
pip install deep-translator
python translator.py
```

---

## Planned Improvements

* Refactor history storage to `list of dict`
* Add timestamp to translation history
* Export / clear translation history
* Auto-detect source language

---

> This project is continuously updated as part of a hands-on Python learning process.
