from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.UnitMultiplier import UnitMultiplier     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.Core.PowerSystemResource import PowerSystemResource

@dataclass
class RegulatingControl(PowerSystemResource):
    """Specifies a set of equipment that works together to control a power system
    quantity such as voltage or flow.
      Remote bus voltage control is possible by specifying the controlled terminal
    located at some place remote from the controlling equipment.
      In case multiple equipment, possibly of different types, control same
    terminal there must be only one RegulatingControl at that terminal. The most
    specific subtype of RegulatingControl shall be used in case such equipment
    participate in the control, e.g. TapChangerControl for tap changers.
      For flow control  load sign convention is used, i.e. positive sign means flow
    out from a TopologicalNode (bus) into the conducting equipment.
    """
    # The regulation is performed in a discrete mode. This applies to equipment with
    # discrete controls, e.g. tap changers and shunt compensators.
    discrete_: bool  = None
 
    # The flag tells if regulation is enabled.
    enabled_: bool  = None
 
    # This is a deadband used with discrete control to avoid excessive update of
    # controls like tap changers and shunt compensator banks while regulating.
    # The units of those appropriate for the mode.
    targetDeadband_: Simple_Float  = None
 
    # The target value specified for case input.   This value can be used for the
    # target value without the use of schedules. The value has the units appropriate
    # to the mode attribute.
    targetValue_: Simple_Float  = None
 
    # Specify the multiplier for used for the targetValue.
    targetValueUnitMultiplier_: UnitMultiplier  = None
     