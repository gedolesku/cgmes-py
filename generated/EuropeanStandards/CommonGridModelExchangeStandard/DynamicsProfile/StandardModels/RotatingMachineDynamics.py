from __future__ import annotations
from ...DomainProfile.PU import PU
from ...DomainProfile.Seconds import Seconds
from ...DomainProfile.Simple_Float import Simple_Float
from .DynamicsFunctionBlock import DynamicsFunctionBlock
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class RotatingMachineDynamics(DynamicsFunctionBlock, Protocol):
    damping: Optional[Simple_Float]  # metadata: cim='cim:RotatingMachineDynamics.damping', mult='0..1'
    inertia: Optional[Seconds]  # metadata: cim='cim:RotatingMachineDynamics.inertia', mult='0..1'
    saturationFactor: Optional[Simple_Float]  # metadata: cim='cim:RotatingMachineDynamics.saturationFactor', mult='0..1'
    saturationFactor120: Optional[Simple_Float]  # metadata: cim='cim:RotatingMachineDynamics.saturationFactor120', mult='0..1'
    statorLeakageReactance: Optional[PU]  # metadata: cim='cim:RotatingMachineDynamics.statorLeakageReactance', mult='0..1'
    statorResistance: Optional[PU]  # metadata: cim='cim:RotatingMachineDynamics.statorResistance', mult='0..1'
