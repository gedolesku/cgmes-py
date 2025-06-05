from __future__ import annotations
from ..DynamicsFunctionBlock import DynamicsFunctionBlock
from ..ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics
from typing import Protocol, runtime_checkable

@runtime_checkable
class PFVArControllerType1Dynamics(DynamicsFunctionBlock, Protocol):
    ExcitationSystemDynamics_ref: ExcitationSystemDynamics  # metadata: cim='cim:PFVArControllerType1Dynamics.ExcitationSystemDynamics', mult='1'
    ExcitationSystemDynamics_id: str
