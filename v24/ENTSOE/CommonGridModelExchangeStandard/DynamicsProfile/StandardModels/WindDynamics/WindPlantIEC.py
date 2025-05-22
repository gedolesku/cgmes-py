from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindPlantReactiveControlIEC import WindPlantReactiveControlIEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindPlantDynamics import WindPlantDynamics
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindPlantFreqPcontrolIEC import WindPlantFreqPcontrolIEC     

@dataclass
class WindPlantIEC(WindPlantDynamics):
    """Simplified IEC type plant level model.
    
      Reference: IEC 61400-27-1, AnnexE.
    """
    # Wind plant reactive control model associated with this wind plant.
    WindPlantReactiveControlIEC_: Optional[WindPlantReactiveControlIEC] = None
 
    # Wind plant frequency and active power control model associated with this wind
    # plant.
    WindPlantFreqPcontrolIEC_: Optional[WindPlantFreqPcontrolIEC] = None
     