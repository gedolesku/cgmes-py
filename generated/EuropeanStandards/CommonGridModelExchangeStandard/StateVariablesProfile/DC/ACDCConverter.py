from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.CurrentFlow import CurrentFlow
from ...DomainProfile.Voltage import Voltage
from ..Core.ConductingEquipment import ConductingEquipment
from typing import Protocol, runtime_checkable

@runtime_checkable
class ACDCConverter(ConductingEquipment, Protocol):
    idc: CurrentFlow  # metadata: cim='cim:ACDCConverter.idc', mult='1'
    poleLossP: ActivePower  # metadata: cim='cim:ACDCConverter.poleLossP', mult='1'
    uc: Voltage  # metadata: cim='cim:ACDCConverter.uc', mult='1'
    udc: Voltage  # metadata: cim='cim:ACDCConverter.udc', mult='1'
