from __future__ import annotations
from ..DynamicsFunctionBlock import DynamicsFunctionBlock
from ..ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics
from typing import Protocol, runtime_checkable

@runtime_checkable
class PowerSystemStabilizerDynamics(DynamicsFunctionBlock, Protocol):
    ExcitationSystemDynamics_ref: ExcitationSystemDynamics  # metadata: cim='cim:PowerSystemStabilizerDynamics.ExcitationSystemDynamics', mult='1'
    ExcitationSystemDynamics_id: str
