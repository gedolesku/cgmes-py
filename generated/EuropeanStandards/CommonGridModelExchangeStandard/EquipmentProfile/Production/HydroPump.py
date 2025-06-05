from __future__ import annotations
from ..Core.Equipment import Equipment
from ..Wires.RotatingMachine import RotatingMachine
from .HydroPowerPlant import HydroPowerPlant
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class HydroPump(Equipment):
    RotatingMachine_id: str | None = field(default=None, metadata={"xpath": "cim:HydroPump.RotatingMachine/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    RotatingMachine_ref: RotatingMachine = None
    HydroPowerPlant_id: str | None = field(default=None, metadata={"xpath": "cim:HydroPump.HydroPowerPlant/@rdf:resource", "pattern": r"^#.+$"})
    HydroPowerPlant_ref: HydroPowerPlant | None = None
