from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.Integer import Integer
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.Resistance import Resistance
from ..Core.BaseVoltage import BaseVoltage
from ..Core.IdentifiedObject import IdentifiedObject
from ..Core.Terminal import Terminal
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class TransformerEnd(Protocol):
    endNumber: Integer  # metadata: cim='cim:TransformerEnd.endNumber', mult='1'
    grounded: Boolean  # metadata: cim='cim:TransformerEnd.grounded', mult='1'
    BaseVoltage_ref: BaseVoltage  # metadata: cim='cim:TransformerEnd.BaseVoltage', mult='1'
    BaseVoltage_id: str
    Terminal_ref: Terminal  # metadata: cim='cim:TransformerEnd.Terminal', mult='1'
    Terminal_id: str
    rground: Optional[Resistance]  # metadata: cim='cim:TransformerEnd.rground', mult='0..1'
    xground: Optional[Reactance]  # metadata: cim='cim:TransformerEnd.xground', mult='0..1'
