from __future__ import annotations
from ...DomainProfile.Simple_Float import Simple_Float
from .RegulatingCondEq import RegulatingCondEq
from typing import Protocol, runtime_checkable

@runtime_checkable
class ShuntCompensator(RegulatingCondEq, Protocol):
    sections: Simple_Float  # metadata: cim='cim:ShuntCompensator.sections', mult='1'
