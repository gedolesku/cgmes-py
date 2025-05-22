from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.VoltageCompensatorDynamics.VoltageCompensatorDynamics import VoltageCompensatorDynamics

@dataclass
class VCompIEEEType2(VoltageCompensatorDynamics):
    """<font color="#0f0f0f">The class represents the terminal voltage transducer and
    the load compensator as defined in the IEEE Std 421.5-2005, Section 4. This
    model is designed to cover the following types of compensation: </font>
      <ul>
      	<li><font color="#0f0f0f">reactive droop</font></li>
      	<li><font color="#0f0f0f">transformer-drop or line-drop
    compensation</font></li>
      	<li><font color="#0f0f0f">reactive differential compensation known also as
    cross-current compensation.</font></li>
      </ul>
      <font color="#0f0f0f">
      </font><font color="#0f0f0f">Reference: IEEE Standard 421.5-2005, Section 4.
    </font>
    """
    # <font color="#0f0f0f">Time constant which is used for the combined voltage
    # sensing and compensation signal (Tr).</font>
    tr: Seconds  = None
     