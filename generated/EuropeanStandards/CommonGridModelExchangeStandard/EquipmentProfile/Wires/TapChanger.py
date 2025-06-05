from __future__ import annotations
from ...DomainProfile.Boolean import Boolean
from ...DomainProfile.Integer import Integer
from ...DomainProfile.Voltage import Voltage
from ..Core.PowerSystemResource import PowerSystemResource
from .TapChangerControl import TapChangerControl
from typing import Optional, List
from typing import Protocol, runtime_checkable

@runtime_checkable
class TapChanger(PowerSystemResource, Protocol):
    highStep: Integer  # metadata: cim='cim:TapChanger.highStep', mult='1'
    lowStep: Integer  # metadata: cim='cim:TapChanger.lowStep', mult='1'
    ltcFlag: Boolean  # metadata: cim='cim:TapChanger.ltcFlag', mult='1'
    neutralStep: Integer  # metadata: cim='cim:TapChanger.neutralStep', mult='1'
    neutralU: Voltage  # metadata: cim='cim:TapChanger.neutralU', mult='1'
    normalStep: Integer  # metadata: cim='cim:TapChanger.normalStep', mult='1'
    TapChangerControl_ref: Optional[TapChangerControl]  # metadata: cim='cim:TapChanger.TapChangerControl', mult='0..1'
    TapChangerControl_id: str
