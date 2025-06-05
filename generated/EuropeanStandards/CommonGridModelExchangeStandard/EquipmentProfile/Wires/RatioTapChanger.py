from __future__ import annotations
from ...DomainProfile.PerCent import PerCent
from .RatioTapChangerTable import RatioTapChangerTable
from .TapChanger import TapChanger
from .TransformerControlMode import TransformerControlMode
from .TransformerEnd import TransformerEnd
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class RatioTapChanger(TapChanger):
    stepVoltageIncrement: PerCent = field(metadata={'xpath': 'cim:RatioTapChanger.stepVoltageIncrement'})
    tculControlMode: TransformerControlMode = field(metadata={'xpath': 'cim:RatioTapChanger.tculControlMode'})
    TransformerEnd_id: str | None = field(default=None, metadata={"xpath": "cim:RatioTapChanger.TransformerEnd/@rdf:resource", "required": True, "pattern": r"^#.+$"})
    TransformerEnd_ref: TransformerEnd = None
    RatioTapChangerTable_id: str | None = field(default=None, metadata={"xpath": "cim:RatioTapChanger.RatioTapChangerTable/@rdf:resource", "pattern": r"^#.+$"})
    RatioTapChangerTable_ref: RatioTapChangerTable | None = None
