from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.DateTime import DateTime
from ...DomainProfile.Integer import Integer
from ...DomainProfile.Seconds import Seconds
from ...DomainProfile.Voltage import Voltage
from ...DomainProfile.VoltagePerReactivePower import VoltagePerReactivePower
from .RegulatingCondEq import RegulatingCondEq
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class ShuntCompensator(RegulatingCondEq, Protocol):
    maximumSections: Integer  # metadata: cim='cim:ShuntCompensator.maximumSections', mult='1'
    nomU: Voltage  # metadata: cim='cim:ShuntCompensator.nomU', mult='1'
    normalSections: Integer  # metadata: cim='cim:ShuntCompensator.normalSections', mult='1'
    aVRDelay: Optional[Seconds]  # metadata: cim='cim:ShuntCompensator.aVRDelay', mult='0..1'
    grounded: Optional[Boolean]  # metadata: cim='cim:ShuntCompensator.grounded', mult='0..1'
    switchOnCount: Optional[Integer]  # metadata: cim='cim:ShuntCompensator.switchOnCount', mult='0..1'
    switchOnDate: Optional[DateTime]  # metadata: cim='cim:ShuntCompensator.switchOnDate', mult='0..1'
    voltageSensitivity: Optional[VoltagePerReactivePower]  # metadata: cim='cim:ShuntCompensator.voltageSensitivity', mult='0..1'
