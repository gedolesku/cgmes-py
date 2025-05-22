from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.VoltageCompensatorDynamics.VoltageCompensatorDynamics import VoltageCompensatorDynamics

@dataclass
class VCompIEEEType1(VoltageCompensatorDynamics):
    """<font color="#0f0f0f">The class represents the terminal voltage transducer and
    the load compensator as defined in the IEEE Std 421.5-2005, Section 4. This
    model is common to all excitation system models described in the IEEE Standard.
    </font>
    
      Reference: IEEE Standard 421.5-2005 Section 4.
    """
    # <font color="#0f0f0f">Resistive component of compensation of a generator (Rc).
    # </font>
    rc_: PU  = None
 
    # <font color="#0f0f0f">Reactive component of compensation of a generator (Xc).
    # </font>
    xc_: PU  = None
 
    # <font color="#0f0f0f">Time constant which is used for the combined voltage
    # sensing and compensation signal (Tr).</font>
    tr_: Seconds  = None
     