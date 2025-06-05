from __future__ import annotations
from ....DomainProfile.PU import PU
from ....DomainProfile.Seconds import Seconds
from .WindTurbineType3or4IEC import WindTurbineType3or4IEC
from typing import Protocol, runtime_checkable

@runtime_checkable
class WindGenType4IEC(WindTurbineType3or4IEC, Protocol):
    dipmax: PU  # metadata: cim='cim:WindGenType4IEC.dipmax', mult='1'
    diqmax: PU  # metadata: cim='cim:WindGenType4IEC.diqmax', mult='1'
    diqmin: PU  # metadata: cim='cim:WindGenType4IEC.diqmin', mult='1'
    tg: Seconds  # metadata: cim='cim:WindGenType4IEC.tg', mult='1'
