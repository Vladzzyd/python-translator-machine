# Vlad Translator (CLI)

A growing **Command Line Translator** built with **Python**, designed as a real-world learning project.
This repository documents not just features, but **progressive improvements in code structure and design**.

---

## Version

**v5.0 – Class-based Refactor & Detection Mode**

This version focuses on **code structure improvement** while keeping all previous features intact.

---

## Current Features

* CLI-based interactive translator
* Translate text continuously without restarting the app
* Supported languages:

  * Indonesia (`id`)
  * English (`en`)
  * Japanese (`ja`)
  * Korean (`ko`)
  * Russian (`ru`)
  * Auto language detection (`deteksi`)
* Translation history with incremental ID
* Well-formatted history display (wrapped text)
* ANSI-colored terminal output
* delete history with two delete options
* Input validation:

  * No empty input
  * No invalid language
  * No same source & target language

---

## What’s New in v5

* delete history with two delete options

---

## Tech Stack

* Python 3
* [`deep-translator`](https://pypi.org/project/deep-translator/)
* Built-in modules:

  * `textwrap`
  * `itertools`

---

## Project Philosophy

This project is intentionally built step-by-step:

* Prioritizing **clarity over complexity**
* Applying improvements incrementally
* Avoiding premature optimization

The goal is to simulate how a small real-world CLI app **naturally evolves** over time.

---

## Planned Improvements

* Implement delete history feature
* Save history to file (`.json` or `.txt`)
* Configuration persistence
* Unit testing


> Built as part of a personal Python learning journey 
