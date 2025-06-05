from __future__ import annotations
from ...DomainProfile.String import String
from ...DomainProfile.UnitMultiplier import UnitMultiplier
from ...DomainProfile.UnitSymbol import UnitSymbol
from ..Core.ACDCTerminal import ACDCTerminal
from ..Core.IdentifiedObject import IdentifiedObject
from ..Core.PhaseCode import PhaseCode
from ..Core.PowerSystemResource import PowerSystemResource
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class Measurement(Protocol):
    measurementType: String  # metadata: cim='cim:Measurement.measurementType', mult='1'
    unitMultiplier: UnitMultiplier  # metadata: cim='cim:Measurement.unitMultiplier', mult='1'
    unitSymbol: UnitSymbol  # metadata: cim='cim:Measurement.unitSymbol', mult='1'
    PowerSystemResource_ref: PowerSystemResource  # metadata: cim='cim:Measurement.PowerSystemResource', mult='1'
    PowerSystemResource_id: str
    phases: Optional[PhaseCode]  # metadata: cim='cim:Measurement.phases', mult='0..1'
    Terminal_ref: Optional[ACDCTerminal]  # metadata: cim='cim:Measurement.Terminal', mult='0..1'
    Terminal_id: str
