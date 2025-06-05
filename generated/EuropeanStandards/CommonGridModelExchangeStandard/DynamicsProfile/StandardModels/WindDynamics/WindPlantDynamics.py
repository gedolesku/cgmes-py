from __future__ import annotations
from ...StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from ..DynamicsFunctionBlock import DynamicsFunctionBlock
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class WindPlantDynamics(DynamicsFunctionBlock, Protocol):
    RemoteInputSignal_ref: Optional[RemoteInputSignal]  # metadata: cim='cim:WindPlantDynamics.RemoteInputSignal', mult='0..1'
    RemoteInputSignal_id: str
