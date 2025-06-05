from __future__ import annotations
from ...DomainProfile.ApparentPower import ApparentPower
from ...DomainProfile.Simple_Float import Simple_Float
from ...DomainProfile.Voltage import Voltage
from ..Production.GeneratingUnit import GeneratingUnit
from .RegulatingCondEq import RegulatingCondEq
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class RotatingMachine(RegulatingCondEq, Protocol):
    ratedPowerFactor: Optional[Simple_Float]  # metadata: cim='cim:RotatingMachine.ratedPowerFactor', mult='0..1'
    ratedS: Optional[ApparentPower]  # metadata: cim='cim:RotatingMachine.ratedS', mult='0..1'
    ratedU: Optional[Voltage]  # metadata: cim='cim:RotatingMachine.ratedU', mult='0..1'
    GeneratingUnit_ref: Optional[GeneratingUnit]  # metadata: cim='cim:RotatingMachine.GeneratingUnit', mult='0..1'
    GeneratingUnit_id: str
