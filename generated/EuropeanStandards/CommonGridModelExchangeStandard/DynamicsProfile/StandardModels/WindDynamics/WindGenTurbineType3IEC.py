from __future__ import annotations
from ....DomainProfile.PU import PU
from .WindAeroLinearIEC import WindAeroLinearIEC
from .WindContPType3IEC import WindContPType3IEC
from .WindContPitchAngleIEC import WindContPitchAngleIEC
from .WindMechIEC import WindMechIEC
from .WindTurbineType3or4IEC import WindTurbineType3or4IEC
from typing import Protocol, runtime_checkable

@runtime_checkable
class WindGenTurbineType3IEC(WindTurbineType3or4IEC, Protocol):
    dipmax: PU  # metadata: cim='cim:WindGenTurbineType3IEC.dipmax', mult='1'
    diqmax: PU  # metadata: cim='cim:WindGenTurbineType3IEC.diqmax', mult='1'
    WindMechIEC_ref: WindMechIEC  # metadata: cim='cim:WindGenTurbineType3IEC.WindMechIEC', mult='1'
    WindMechIEC_id: str
    WindContPitchAngleIEC_ref: WindContPitchAngleIEC  # metadata: cim='cim:WindGenTurbineType3IEC.WindContPitchAngleIEC', mult='1'
    WindContPitchAngleIEC_id: str
    WindAeroLinearIEC_ref: WindAeroLinearIEC  # metadata: cim='cim:WindGenTurbineType3IEC.WindAeroLinearIEC', mult='1'
    WindAeroLinearIEC_id: str
    WindContPType3IEC_ref: WindContPType3IEC  # metadata: cim='cim:WindGenTurbineType3IEC.WindContPType3IEC', mult='1'
    WindContPType3IEC_id: str
