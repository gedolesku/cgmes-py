from __future__ import annotations
from ..DynamicsFunctionBlock import DynamicsFunctionBlock
from ..PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import PFVArControllerType1Dynamics
from typing import Protocol, runtime_checkable

@runtime_checkable
class VoltageAdjusterDynamics(DynamicsFunctionBlock, Protocol):
    PFVArControllerType1Dynamics_ref: PFVArControllerType1Dynamics  # metadata: cim='cim:VoltageAdjusterDynamics.PFVArControllerType1Dynamics', mult='1'
    PFVArControllerType1Dynamics_id: str
