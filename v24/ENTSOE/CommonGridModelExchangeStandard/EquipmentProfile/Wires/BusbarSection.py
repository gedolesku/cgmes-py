from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.Connector import Connector

@dataclass
class BusbarSection(Connector):
    """A conductor, or group of conductors, with negligible impedance, that serve to
    connect other conducting equipment within a single substation.
      Voltage measurements are typically obtained from VoltageTransformers that are
    connected to busbar sections. A bus bar section may have many physical
    terminals but for analysis is modelled with exactly one logical terminal.
    """
    # Maximum allowable peak short-circuit current of busbar (Ipmax in the IEC 60909-
    # 0).
    # Mechanical limit of the busbar in the substation itself. Used for short circuit
    # data exchange according to IEC 60909
    ipMax_: CurrentFlow  = None
     