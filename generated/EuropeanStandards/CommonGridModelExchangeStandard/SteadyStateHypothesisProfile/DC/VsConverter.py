from __future__ import annotations
from ...DomainProfile.PU import PU
from ...DomainProfile.PerCent import PerCent
from ...DomainProfile.ReactivePower import ReactivePower
from ...DomainProfile.Resistance import Resistance
from ...DomainProfile.Voltage import Voltage
from .ACDCConverter import ACDCConverter
from .VsPpccControlKind import VsPpccControlKind
from .VsQpccControlKind import VsQpccControlKind
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class VsConverter(ACDCConverter):
    droop: PU = field(metadata={'xpath': 'cim:VsConverter.droop'})
    droopCompensation: Resistance = field(metadata={'xpath': 'cim:VsConverter.droopCompensation'})
    pPccControl: VsPpccControlKind = field(metadata={'xpath': 'cim:VsConverter.pPccControl'})
    qPccControl: VsQpccControlKind = field(metadata={'xpath': 'cim:VsConverter.qPccControl'})
    qShare: PerCent = field(metadata={'xpath': 'cim:VsConverter.qShare'})
    targetQpcc: ReactivePower = field(metadata={'xpath': 'cim:VsConverter.targetQpcc'})
    targetUpcc: Voltage = field(metadata={'xpath': 'cim:VsConverter.targetUpcc'})
