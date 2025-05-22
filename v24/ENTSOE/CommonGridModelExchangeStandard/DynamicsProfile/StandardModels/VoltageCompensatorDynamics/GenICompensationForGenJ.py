from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.VoltageCompensatorDynamics.VCompIEEEType2 import VCompIEEEType2     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics import SynchronousMachineDynamics     

@dataclass
class GenICompensationForGenJ(IdentifiedObject):
    """This class provides the resistive and reactive components of compensation for
    the generator associated with the IEEE Type 2 voltage compensator for current
    flow out of one of the other generators in the interconnection.
    """
    # <font color="#0f0f0f">Resistive component of compensation of generator
    # associated with this IEEE Type 2 voltage compensator for current flow out of
    # another generator (Rcij).</font>
    rcij: PU  = None
 
    # <font color="#0f0f0f">Reactive component of compensation of generator
    # associated with this IEEE Type 2 voltage compensator for current flow out of
    # another generator (Xcij).</font>
    xcij: PU  = None
 
    # The standard IEEE Type 2 voltage compensator of this compensation.
    VcompIEEEType2_ref: Optional[VCompIEEEType2] = None
    VcompIEEEType2: str = None
 
    # Standard synchronous machine out of which current flow is being compensated for.
    SynchronousMachineDynamics_ref: Optional[SynchronousMachineDynamics] = None
    SynchronousMachineDynamics: str = None
     