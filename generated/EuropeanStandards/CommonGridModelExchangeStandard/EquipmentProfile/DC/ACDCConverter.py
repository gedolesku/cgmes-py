from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.ActivePowerPerCurrentFlow import ActivePowerPerCurrentFlow
from ...DomainProfile.ApparentPower import ApparentPower
from ...DomainProfile.Integer import Integer
from ...DomainProfile.Resistance import Resistance
from ...DomainProfile.Voltage import Voltage
from ..Core.ConductingEquipment import ConductingEquipment
from ..Core.Terminal import Terminal
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class ACDCConverter(ConductingEquipment, Protocol):
    baseS: Optional[ApparentPower]  # metadata: cim='cim:ACDCConverter.baseS', mult='0..1'
    idleLoss: Optional[ActivePower]  # metadata: cim='cim:ACDCConverter.idleLoss', mult='0..1'
    maxUdc: Optional[Voltage]  # metadata: cim='cim:ACDCConverter.maxUdc', mult='0..1'
    minUdc: Optional[Voltage]  # metadata: cim='cim:ACDCConverter.minUdc', mult='0..1'
    numberOfValves: Optional[Integer]  # metadata: cim='cim:ACDCConverter.numberOfValves', mult='0..1'
    ratedUdc: Optional[Voltage]  # metadata: cim='cim:ACDCConverter.ratedUdc', mult='0..1'
    resistiveLoss: Optional[Resistance]  # metadata: cim='cim:ACDCConverter.resistiveLoss', mult='0..1'
    switchingLoss: Optional[ActivePowerPerCurrentFlow]  # metadata: cim='cim:ACDCConverter.switchingLoss', mult='0..1'
    valveU0: Optional[Voltage]  # metadata: cim='cim:ACDCConverter.valveU0', mult='0..1'
    PccTerminal_ref: Optional[Terminal]  # metadata: cim='cim:ACDCConverter.PccTerminal', mult='0..1'
    PccTerminal_id: str
