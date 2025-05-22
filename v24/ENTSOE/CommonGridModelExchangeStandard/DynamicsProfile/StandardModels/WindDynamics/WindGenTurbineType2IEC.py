from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindPitchContEmulIEC import WindPitchContEmulIEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindTurbineType1or2IEC import WindTurbineType1or2IEC
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindContRotorRIEC import WindContRotorRIEC     

@dataclass
class WindGenTurbineType2IEC(WindTurbineType1or2IEC):
    """Wind turbine IEC Type 2.
    
      Reference: IEC Standard 61400-27-1, section 6.5.3.
    """
    # Pitch control emulator model associated with this wind turbine type 2 model.
    WindPitchContEmulIEC_ref: Optional[WindPitchContEmulIEC] = None
    WindPitchContEmulIEC: str = None
 
    # Wind control rotor resistance model associated with wind turbine type 2 model.
    WindContRotorRIEC_ref: Optional[WindContRotorRIEC] = None
    WindContRotorRIEC: str = None
     