from __future__ import annotations
from ..Core.Substation import Substation
from .DCConverterOperatingModeKind import DCConverterOperatingModeKind
from .DCEquipmentContainer import DCEquipmentContainer
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class DCConverterUnit(DCEquipmentContainer):
    operationMode: DCConverterOperatingModeKind = field(metadata={'xpath': 'cim:DCConverterUnit.operationMode'})
    Substation_id: str | None = field(default=None, metadata={"xpath": "cim:DCConverterUnit.Substation/@rdf:resource", "pattern": r"^#.+$"})
    Substation_ref: Substation | None = None
