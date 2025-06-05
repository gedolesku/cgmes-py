from __future__ import annotations
from ...DomainProfile.CurrentFlow import CurrentFlow
from ...DomainProfile.Simple_Float import Simple_Float
from .ACDCConverter import ACDCConverter
from .VsCapabilityCurve import VsCapabilityCurve
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class VsConverter(ACDCConverter):
    maxModulationIndex: Optional[Simple_Float] = field(default=None, metadata={'xpath': 'cim:VsConverter.maxModulationIndex'})
    maxValveCurrent: Optional[CurrentFlow] = field(default=None, metadata={'xpath': 'cim:VsConverter.maxValveCurrent'})
    CapabilityCurve_id: str | None = field(default=None, metadata={"xpath": "cim:VsConverter.CapabilityCurve/@rdf:resource", "pattern": r"^#.+$"})
    CapabilityCurve_ref: VsCapabilityCurve | None = None
