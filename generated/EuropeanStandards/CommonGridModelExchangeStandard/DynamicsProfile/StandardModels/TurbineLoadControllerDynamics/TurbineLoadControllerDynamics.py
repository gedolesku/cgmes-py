from __future__ import annotations
from ..DynamicsFunctionBlock import DynamicsFunctionBlock
from ..TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics
from typing import Protocol, runtime_checkable

@runtime_checkable
class TurbineLoadControllerDynamics(DynamicsFunctionBlock, Protocol):
    TurbineGovernorDynamics_ref: TurbineGovernorDynamics  # metadata: cim='cim:TurbineLoadControllerDynamics.TurbineGovernorDynamics', mult='1'
    TurbineGovernorDynamics_id: str
