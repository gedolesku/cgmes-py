from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.RotatingMachineDynamics import RotatingMachineDynamics
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Wires.AsynchronousMachine import AsynchronousMachine     

@dataclass
class AsynchronousMachineDynamics(RotatingMachineDynamics):
    """Asynchronous machine whose behaviour is described by reference to a standard
    model expressed in either time constant reactance form or equivalent circuit
    form <font color="#0f0f0f">or by definition of a user-defined model.</font>
    
      <b>Parameter Notes:</b>
      <ol>
      	<li>Asynchronous machine parameters such as <b>Xl, Xs</b> etc. are actually
    used as inductances (L) in the model, but are commonly referred to as
    reactances since, at nominal frequency, the per unit values are the same.
    However, some references use the symbol L instead of X. </li>
      </ol>
    """
    # Asynchronous machine to which this asynchronous machine dynamics model applies.
    AsynchronousMachine_ref: Optional[AsynchronousMachine] = None
    AsynchronousMachine: str = None
     