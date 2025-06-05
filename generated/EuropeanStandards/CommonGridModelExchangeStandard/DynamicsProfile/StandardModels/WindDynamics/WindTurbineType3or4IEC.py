from __future__ import annotations
from .WindContCurrLimIEC import WindContCurrLimIEC
from .WindContQIEC import WindContQIEC
from .WindProtectionIEC import WindProtectionIEC
from .WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics
from typing import Protocol, runtime_checkable

@runtime_checkable
class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics, Protocol):
    WindProtectionIEC_ref: WindProtectionIEC  # metadata: cim='cim:WindTurbineType3or4IEC.WindProtectionIEC', mult='1'
    WindProtectionIEC_id: str
    WindContCurrLimIEC_ref: WindContCurrLimIEC  # metadata: cim='cim:WindTurbineType3or4IEC.WindContCurrLimIEC', mult='1'
    WindContCurrLimIEC_id: str
    WIndContQIEC_ref: WindContQIEC  # metadata: cim='cim:WindTurbineType3or4IEC.WIndContQIEC', mult='1'
    WIndContQIEC_id: str
