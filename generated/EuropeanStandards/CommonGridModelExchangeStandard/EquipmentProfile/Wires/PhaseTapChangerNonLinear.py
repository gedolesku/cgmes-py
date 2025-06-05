from __future__ import annotations
from ...DomainProfile.PerCent import PerCent
from ...DomainProfile.Reactance import Reactance
from .PhaseTapChanger import PhaseTapChanger
from typing import Protocol, runtime_checkable

@runtime_checkable
class PhaseTapChangerNonLinear(PhaseTapChanger, Protocol):
    voltageStepIncrement: PerCent  # metadata: cim='cim:PhaseTapChangerNonLinear.voltageStepIncrement', mult='1'
    xMax: Reactance  # metadata: cim='cim:PhaseTapChangerNonLinear.xMax', mult='1'
    xMin: Reactance  # metadata: cim='cim:PhaseTapChangerNonLinear.xMin', mult='1'
