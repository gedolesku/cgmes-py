from __future__ import annotations
from ...StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from ...Wires.EnergySource import EnergySource
from ..DynamicsFunctionBlock import DynamicsFunctionBlock
from .WindPlantDynamics import WindPlantDynamics
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class WindTurbineType3or4Dynamics(DynamicsFunctionBlock, Protocol):
    EnergySource_ref: EnergySource  # metadata: cim='cim:WindTurbineType3or4Dynamics.EnergySource', mult='1'
    EnergySource_id: str
    WindPlantDynamics_ref: Optional[WindPlantDynamics]  # metadata: cim='cim:WindTurbineType3or4Dynamics.WindPlantDynamics', mult='0..1'
    WindPlantDynamics_id: str
    RemoteInputSignal_ref: Optional[RemoteInputSignal]  # metadata: cim='cim:WindTurbineType3or4Dynamics.RemoteInputSignal', mult='0..1'
    RemoteInputSignal_id: str
