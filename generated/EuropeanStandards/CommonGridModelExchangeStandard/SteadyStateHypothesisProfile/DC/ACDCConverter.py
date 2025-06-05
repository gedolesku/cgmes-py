from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.ReactivePower import ReactivePower
from ...DomainProfile.Voltage import Voltage
from ..Core.ConductingEquipment import ConductingEquipment
from typing import Protocol, runtime_checkable

@runtime_checkable
class ACDCConverter(ConductingEquipment, Protocol):
    p: ActivePower  # metadata: cim='cim:ACDCConverter.p', mult='1'
    q: ReactivePower  # metadata: cim='cim:ACDCConverter.q', mult='1'
    targetPpcc: ActivePower  # metadata: cim='cim:ACDCConverter.targetPpcc', mult='1'
    targetUdc: Voltage  # metadata: cim='cim:ACDCConverter.targetUdc', mult='1'
