from __future__ import annotations
from ...DomainProfile.CurrentFlow import CurrentFlow
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.Voltage import Voltage
from .EarthFaultCompensator import EarthFaultCompensator
from .PetersenCoilModeKind import PetersenCoilModeKind
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass(kw_only=True)
class PetersenCoil(EarthFaultCompensator):
    mode: PetersenCoilModeKind = field(metadata={'xpath': 'cim:PetersenCoil.mode'})
    nominalU: Voltage = field(metadata={'xpath': 'cim:PetersenCoil.nominalU'})
    xGroundMax: Reactance = field(metadata={'xpath': 'cim:PetersenCoil.xGroundMax'})
    xGroundMin: Reactance = field(metadata={'xpath': 'cim:PetersenCoil.xGroundMin'})
    xGroundNominal: Reactance = field(metadata={'xpath': 'cim:PetersenCoil.xGroundNominal'})
    offsetCurrent: Optional[CurrentFlow] = field(default=None, metadata={'xpath': 'cim:PetersenCoil.offsetCurrent'})
    positionCurrent: Optional[CurrentFlow] = field(default=None, metadata={'xpath': 'cim:PetersenCoil.positionCurrent'})
