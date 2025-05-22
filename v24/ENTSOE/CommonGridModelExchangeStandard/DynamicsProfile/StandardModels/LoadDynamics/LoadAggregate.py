from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.LoadDynamics.LoadDynamics import LoadDynamics

@dataclass
class LoadAggregate(LoadDynamics):
    """Standard aggregate load model comprised of static and/or dynamic components.  A
    static load model represents the sensitivity of the real and reactive power
    consumed by the load to the amplitude and frequency of the bus voltage. A
    dynamic load model can used to represent the aggregate response of the motor
    components of the load.
    """
    pass
