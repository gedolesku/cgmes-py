from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics import AsynchronousMachineDynamics

@dataclass
class AsynchronousMachineUserDefined(AsynchronousMachineDynamics):
    """Asynchronous machine whose dynamic behaviour is described by a user-defined
    model.
    """
    # Behaviour is based on proprietary model as opposed to detailed model.
    # true = user-defined model is proprietary with behaviour mutually understood by
    # sending and receiving applications and parameters passed as general attributes
    # false = user-defined model is explicitly defined in terms of control blocks and
    # their input and output signals.
    proprietary_: bool  = None
     