from __future__ import annotations
from ..Core.PowerSystemResource import PowerSystemResource
from ..LoadModel.EnergyArea import EnergyArea
from .ControlAreaTypeKind import ControlAreaTypeKind
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class ControlArea(PowerSystemResource):
    type: ControlAreaTypeKind = field(metadata={'xpath': 'cim:ControlArea.type'})
    EnergyArea_id: str | None = field(default=None, metadata={"xpath": "cim:ControlArea.EnergyArea/@rdf:resource", "pattern": r"^#.+$"})
    EnergyArea_ref: EnergyArea | None = None
