from __future__ import annotations
from ...DomainProfile.Reactance import Reactance
from ...DomainProfile.Voltage import Voltage
from ...DomainProfile.VoltagePerReactivePower import VoltagePerReactivePower
from .RegulatingCondEq import RegulatingCondEq
from .SVCControlMode import SVCControlMode
from dataclasses import dataclass, field

@dataclass(kw_only=True)
class StaticVarCompensator(RegulatingCondEq):
    capacitiveRating: Reactance = field(metadata={'xpath': 'cim:StaticVarCompensator.capacitiveRating'})
    inductiveRating: Reactance = field(metadata={'xpath': 'cim:StaticVarCompensator.inductiveRating'})
    slope: VoltagePerReactivePower = field(metadata={'xpath': 'cim:StaticVarCompensator.slope'})
    sVCControlMode: SVCControlMode = field(metadata={'xpath': 'cim:StaticVarCompensator.sVCControlMode'})
    voltageSetPoint: Voltage = field(metadata={'xpath': 'cim:StaticVarCompensator.voltageSetPoint'})
