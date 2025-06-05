from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.Simple_Float import Simple_Float
from ..Core.PowerSystemResource import PowerSystemResource
from typing import Protocol, runtime_checkable

@runtime_checkable
class TapChanger(PowerSystemResource, Protocol):
    controlEnabled: Boolean  # metadata: cim='cim:TapChanger.controlEnabled', mult='1'
    step: Simple_Float  # metadata: cim='cim:TapChanger.step', mult='1'
