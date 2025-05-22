from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RegulatingControlModeKind import RegulatingControlModeKind     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.PowerSystemResource import PowerSystemResource
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Terminal import Terminal     

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
    # The regulating control mode presently available.  This specification allows for
    # determining the kind of regulation without need for obtaining the units from a
    # schedule.
    mode_: RegulatingControlModeKind  = None
 
    # The controls regulating this terminal.
    Terminal_: Optional[Terminal] = None
     