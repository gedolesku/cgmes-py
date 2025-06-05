from __future__ import annotations
from .WindMechIEC import WindMechIEC
from .WindProtectionIEC import WindProtectionIEC
from .WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics
from typing import Protocol, runtime_checkable

@runtime_checkable
class WindTurbineType1or2IEC(WindTurbineType1or2Dynamics, Protocol):
    WindProtectionIEC_ref: WindProtectionIEC  # metadata: cim='cim:WindTurbineType1or2IEC.WindProtectionIEC', mult='1'
    WindProtectionIEC_id: str
    WindMechIEC_ref: WindMechIEC  # metadata: cim='cim:WindTurbineType1or2IEC.WindMechIEC', mult='1'
    WindMechIEC_id: str
