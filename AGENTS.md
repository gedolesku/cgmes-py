# Project Guidelines for cgmes-py

This repository contains utilities for working with the Common Grid Model Exchange Standard (CGMES) models.

## Key Files
- `generate_cgmes_project.py` – converts the CGMES 2.4 Enterprise Architect XMI export into Python dataclasses.
- `cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml` – XMI file used as the generator's input.
- `cgmes-models/v24/SmallGrid/node-breaker/*.xml` – sample instance models.
- `.codex/setup.sh` – installs minimal dependencies from `requirements2.txt`.

## Running the Generator
Use the CLI to generate dataclasses:
```bash
python generate_cgmes_project.py cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml -o generated
```
The output directory (`generated/` in the example) is ignored by Git via `.gitignore` and should not be committed.

## Notes about the Script
- The script traverses each `uml:Model` element and writes a dataclass for every UML class it finds.
- Multiplicities are respected so attributes may become `Optional` or `list` types.
- A minimal runtime (`base.py`) with the `CIMObject` class is written automatically.
- Enumerations and custom datatypes are not yet supported.

## Contribution Tips
- Install dependencies with `pip install -r requirements2.txt` (or run `.codex/setup.sh`).
- Do not commit generated code or large XML model files.
- Keep docstrings and CLI help messages up to date when modifying `generate_cgmes_project.py`.

