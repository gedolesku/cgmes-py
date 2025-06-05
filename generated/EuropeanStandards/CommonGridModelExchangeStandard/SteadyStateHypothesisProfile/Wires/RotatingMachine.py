from __future__ import annotations
from ...DomainProfile.ActivePower import ActivePower
from ...DomainProfile.ReactivePower import ReactivePower
from .RegulatingCondEq import RegulatingCondEq
from typing import Protocol, runtime_checkable

@runtime_checkable
class RotatingMachine(RegulatingCondEq, Protocol):
    p: ActivePower  # metadata: cim='cim:RotatingMachine.p', mult='1'
    q: ReactivePower  # metadata: cim='cim:RotatingMachine.q', mult='1'
