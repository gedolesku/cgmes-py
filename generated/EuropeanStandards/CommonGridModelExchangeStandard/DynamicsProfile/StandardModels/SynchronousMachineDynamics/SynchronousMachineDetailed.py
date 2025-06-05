from __future__ import annotations
from ....DomainProfile.CurrentFlow import CurrentFlow
from ....DomainProfile.Simple_Float import Simple_Float
from .IfdBaseKind import IfdBaseKind
from .SynchronousMachineDynamics import SynchronousMachineDynamics
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class SynchronousMachineDetailed(SynchronousMachineDynamics, Protocol):
    efdBaseRatio: Optional[Simple_Float]  # metadata: cim='cim:SynchronousMachineDetailed.efdBaseRatio', mult='0..1'
    ifdBaseType: Optional[IfdBaseKind]  # metadata: cim='cim:SynchronousMachineDetailed.ifdBaseType', mult='0..1'
    ifdBaseValue: Optional[CurrentFlow]  # metadata: cim='cim:SynchronousMachineDetailed.ifdBaseValue', mult='0..1'
    saturationFactor120QAxis: Optional[Simple_Float]  # metadata: cim='cim:SynchronousMachineDetailed.saturationFactor120QAxis', mult='0..1'
    saturationFactorQAxis: Optional[Simple_Float]  # metadata: cim='cim:SynchronousMachineDetailed.saturationFactorQAxis', mult='0..1'
