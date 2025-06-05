# Project Guidelines for cgmes-py

This repository contains utilities for working with the Common Grid Model Exchange Standard (CGMES) models.

## Key Files
- `generate_cgmes_project.py` – converts the CGMES 2.4 Enterprise Architect XMI export into Python dataclasses.
- `cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml` – XMI file used as the generator's input.
- `cgmes-models/v24/SmallGrid/node-breaker/*.xml` – sample instance models.
- `.codex/setup.sh` – installs minimal dependencies from `requirements2.txt`.


# 🤖 cgmes‑py Agent Handbook

> *Everything an AI (or human) agent needs to know to deliver a pull‑request that «just works».*

---

## 1  Mission Statement

Deliver a **lean, type‑safe and performant** Python toolkit that can:

1. **Generate** dataclass models from EA’s UML XMI.
2. **Round‑trip** CGMES / CIM instance XMLs via the *metadata‑driven* binding layer.
3. Remain **dependency‑light** (only `lxml` + stdlib) and **tool‑friendly** (mypy, pylint, pytest).

---

## 2  System Architecture Snapshot

```
                 +-----------------------+
                 |  cgmes-models/       |
EA XMI  ➜  +---->+  (reference models)  |
           |     +-----------+----------+
           |                 |
           |   generate_cgmes_project.py
           |                 |
           |     +-----------v----------+
           +---->+  generated/  (code)  |
                 +-----------+----------+
                             |
            runtime/base.py  |  runtime/validation.py
                             |
                 +-----------v----------+
                 |  Your scripts/tests |
                 +---------------------+
```

* **Binding layer**: Plain `@dataclass` + `field(metadata={"xpath": …})`.
* **Runtime**: `parse_dataclass()` + `to_element()` + optional validation.
* **Streaming**: use `lxml.iterparse` when handling >100 MB instance files.

---

## 3  Agent Roles & Responsibilities

| Agent ID     | Role                | Key files                                    | Acceptance tests                                                |
| ------------ | ------------------- | -------------------------------------------- | --------------------------------------------------------------- |
| **GEN‑101**  | *Code‑Gen Agent*    | `generate_cgmes_project.py`<br>`templates/`  | *tests/test\_generator\_output.py* – must compile, lint pass    |
| **RT‑201**   | *Runtime Agent*     | `runtime/base.py`<br>`runtime/validation.py` | *tests/test\_roundtrip.py* – parse ➜ write ➜ diff ≅ 0           |
| **VAL‑202**  | *Validation Agent*  | same as RT                                   | *tests/test\_validation.py* – fail‑fast on required/regex rules |
| **PERF‑301** | *Performance Agent* | benchmarks/                                  | `pytest -k perf` must stay below 1.2× baseline                  |
| **DOC‑401**  | *Doc Agent*         | `README.md`, `AGENTS.md`                     | Markdown lint + reviewer approval                               |

> **Note:** A single PR may involve multiple agents; tag the checklist accordingly in the PR description.

---

## 4  Guidelines for Implementing Tasks

### 4.1  Coding Standards

* **PEP 8** + black (line = 120). Use type hints everywhere.
* No external deps beyond `lxml` and `python‑dateutil` (if ISO‑dates needed).
* Keep generic runtime under **150 LoC** and free of reflection magic.

### 4.2  Dataclass ↔ XML Mapping Rules

| Rule                                                          | Rationale                                        |
| ------------------------------------------------------------- | ------------------------------------------------ |
| Use absolute XPath rooted in the *current element* (no `..`)  | Simpler & faster lookup.                         |
| Attributes are denoted with `/@attr`                          | Clear distinction element vs attribute.          |
| Prefixes must exist in global `NS` dict                       | Centralised URI management.                      |
| Omit `xpath` ⇒ field is **RAM‑only** (refs, caches, computed) | Keeps XML clean while allowing enriched objects. |
| Add `required=True` in `metadata` for multiplicity 1‥1        | Validated in strict mode.                        |
| Use `pattern="^#.+$"` for `rdf:resource` IDs                  | Basic sanity guard.                              |

### 4.3  Validation Strategy

* **Strict mode** is optional but enabled in CI – keep parse cost low in default mode.
* ID dereference (`*_id` ➜ `*_ref`) happens in a post‑pass inside `runtime/validation.py`.

### 4.4  Performance

* Parser must reach **≥ 500 k objects/s** on the 130 k‑node sample grid (M1 Pro).
* Use `iterparse` + `elem.clear()` for streaming; memory ≤ 400 MB on the 500 MB test file.

### 4.5  Documentation

* Each public function ↔ one docstring with example.
* Update **both** this handbook and `README.md` when behaviour changes.

---

## 5  Contributor Checklist (for humans & LLMs)

* [ ] My code is typed, formatted, and passes `pytest`.<br>
* [ ] I updated or added tests relevant to my changes.<br>
* [ ] I updated docs (`README.md`, `AGENTS.md`).<br>
* [ ] I ran `python -m benchmarks.perf` and stayed within budget.

---

## 6  FAQs for Agents

**Q 1:** *Šta ako UML profil doda novi atribut?*  ➜ Regeneriši model (GEN‑101) + dodaj `xpath` + test.

**Q 2:** *Mogu li da koristim pydantic?* ➜ Ne; zadržavamo samo `dataclasses` radi nulte zavisnosti i brзине.

**Q 3:** *Šta ako se `xpath` promeni?* ➜ Izmeni polje u modelu + test\_roundtrip mora proći.

---

*Srećan rad – neka objave prolaze na **prvi review**!*
