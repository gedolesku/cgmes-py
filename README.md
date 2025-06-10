# cgmes‑py – Lightweight CGMES / CIM Toolkit

## 1  What is this project?

A **minimal, code‑generated Python toolkit** for working with ENTSO‑E’s Common Grid Model Exchange Standard (CGMES) and IEC 61970/61968 CIM files exported from Enterprise Architect (EA) in **UML XMI 2.1** format.

Key design choice : Use plain `@dataclass` models whose \*\*fields carry an \*\*`** mapping in **`. A *single, generic* parser and serializer (`parse_dataclass()` / `to_element()`) turn any such dataclass hierarchy into a full XML binding layer without relying on heavyweight frameworks.

---

## 2  Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements2.txt          # lxml + pytest + pylint

python generate_cgmes_project.py          # ▶ writes ./generated/
python examples/roundtrip.py              # ▶ demo: parse + write back
pytest                                    # ▶ all tests incl. pylint
pytest -k smallgrid                       # ▶ integration test on sample model
python -m cgmes.export cgmes-models/v24/SmallGrid/node-breaker out/
# inspect out/*.xml in EA / GridCal
```

```python
from cgmes.runtime import parse_file
from cgmes.generated.topology.topologicalnode import TopologicalNode

for node in parse_file("models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml",
                       TopologicalNode):
    print(node.mRID, node.name, node.BaseVoltage_id)
```

```python
from cgmes.runtime import parse_dataset
from cgmes.generated.topology.voltagelevel import VoltageLevel

data = parse_dataset("models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml",
                     [TopologicalNode, VoltageLevel])
print(len(data[TopologicalNode]))
```

*The generator and runtime are dependency‑light:* only `lxml` and the standard library. Large CGMES instance models (100 MB+) can be streamed with `iterparse` in constant memory.

---

## 3  Directory Layout

```
.
├── generate_cgmes_project.py   ← code‑generator (EA XMI → dataclasses)
├── runtime/
│   ├── base.py                 ← CIMObject + generic parser/serializer
│   └── validation.py           ← optional strict mode helpers
├── generated/                  ← auto‑generated packages (git‑ignored)
├── cgmes‑models/               ← reference XMI + sample instance XMLs
└── tests/
```

---

## 4  How does the binding work?

### 4.1  Field mapping by annotation

```python
@dataclass(kw_only=True)
class TopologicalNode(IdentifiedObject):
    # XML: <cim:TopologicalNode.BaseVoltage rdf:resource="#BV1"/>
    BaseVoltage_id: str | None = field(
        default=None,
        metadata={"xpath": "cim:TopologicalNode.BaseVoltage/@rdf:resource"},
    )
```

* One source of truth –  the `xpath` tells the runtime **where to read / how to write** the value inside the element subtree.
* Elements vs attributes: text nodes use `…/text()`, attributes are denoted with `/@…`.

### 4.2  Generic runtime (excerpt)

```python
for f in fields(cls):
    xp = f.metadata.get("xpath")
    if xp and "/@" in xp:
        path, attr = xp.split("/@")
        child = elem.find(path, NS)
        kwargs[f.name] = child.get(attr) if child is not None else None
```

The same \~30 lines serve every class in the hierarchy – no per‑class ✗ML binding code.

### 4.3  Validation (optional)

Add flags in `metadata`, e.g. `required=True`, `pattern=r"^#.+$"`. Pass `strict=True` to the parser to enable fail‑fast checks.

### 4.4  Caching strategy

```
+--------------+      +-------------+
| dataclass -> | ---> | FieldSpec[] |
+--------------+      +------+------+ 
                       |
                       v
                 [ class cache ]
```

---

## 5  Performance notes

| Parser                           | Objects/s *(≈130 k)* | Notes                                  |
| -------------------------------- | -------------------- | -------------------------------------- |
| Raw dataclass + lxml (this repo) | **≈550 k**           | fastest, zero validation overhead      |
| xsdata‑generated dataclass       | 400 k                | +10–30 % lookup overhead               |
| pydantic‑xml (v2)                | 130 k                | strict runtime validation, \~4× slower |

The generic runtime can fall back to `iterparse` for true streaming, so RAM stays flat even for >500 MB files.

---

## 6  Agent Workflow (Codex / GPT‑powered)

1. **Code‑Gen Agent** – updates generator when UML profile changes.
2. **Runtime Agent** – maintains generic parser/serializer & validators.
3. **Test Agent** – ensures round‑trip + linter pass.
4. **Doc Agent** – keeps `README.md`, `AGENTS.md`, in‑code docs in sync.

> Agents: see *AGENTS.md* for concrete task specs & acceptance criteria.

---

## 7  Roadmap

* Profile‑aware generator (EA stereotypes → Python mixins).
* Bulk streaming transformer for merging CGMES snapshots.
* JSON‑LD exporter for CIM graphs.

Pull requests are welcome – follow the contribution tips in `AGENTS.md`!

## 8  How to add a new CIM element in 3 steps

1. Run `generate_cgmes_project.py` to regenerate models.
2. Extend the generated dataclasses with the new element and its `xpath`.
3. Add a test under `tests/` to validate round‑trip parsing.

