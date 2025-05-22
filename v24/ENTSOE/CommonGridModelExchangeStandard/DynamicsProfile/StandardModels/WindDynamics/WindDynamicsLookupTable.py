from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindLookupTableFunctionKind import WindLookupTableFunctionKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindPlantFreqPcontrolIEC import WindPlantFreqPcontrolIEC     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.Core.IdentifiedObject import IdentifiedObject
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindContRotorRIEC import WindContRotorRIEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindContPType3IEC import WindContPType3IEC     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.WindDynamics.WindContCurrLimIEC import WindContCurrLimIEC     

@dataclass
class WindDynamicsLookupTable(IdentifiedObject):
    """The class models a look up table for the purpose of wind standard models.
    """
    # Input value (x) for the lookup table function.
    input_: Simple_Float  = None
 
    # Type of the lookup table function.
    lookupTableFunctionType_: WindLookupTableFunctionKind  = None
 
    # Output value (y) for the lookup table function.
    output_: Simple_Float  = None
 
    # Sequence numbers of the pairs of the input (x) and the output (y) of the lookup
    # table function.
    sequence_: int  = None
 
    # The wind dynamics lookup table associated with this frequency and active power
    # wind plant model.
    WindPlantFreqPcontrolIEC_: Optional[WindPlantFreqPcontrolIEC] = None
 
    # The rotor resistance control model with which this wind dynamics lookup table
    # is associated.
    WindContRotorRIEC_: Optional[WindContRotorRIEC] = None
 
    # The wind dynamics lookup table associated with this P control type 3 model.
    WindContPType3IEC_: Optional[WindContPType3IEC] = None
 
    # The wind dynamics lookup table associated with this current control limitation
    # model.
    WindContCurrLimIEC_: Optional[WindContCurrLimIEC] = None
     