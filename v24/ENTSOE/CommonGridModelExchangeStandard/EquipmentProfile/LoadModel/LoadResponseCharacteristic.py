from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.IdentifiedObject import IdentifiedObject

@dataclass
class LoadResponseCharacteristic(IdentifiedObject):
    """Models the characteristic response of the load demand due to changes in system
    conditions such as voltage and frequency. This is not related to demand
    response.
    
      If LoadResponseCharacteristic.exponentModel is True, the voltage exponents
    are specified and used as to calculate:
    
      Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage)
    ** cim:LoadResponseCharacteristic.pVoltageExponent
    
      Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.
    nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent
    
      Where  * means "multiply" and ** is "raised to power of".
    """
    # Indicates the exponential voltage dependency model is to be used.   If false,
    # the coefficient model is to be used.
    # The exponential voltage dependency model consist of the attributes
    # - pVoltageExponent
    # - qVoltageExponent.
    # The coefficient model consist of the attributes
    # - pConstantImpedance
    # - pConstantCurrent
    # - pConstantPower
    # - qConstantImpedance
    # - qConstantCurrent
    # - qConstantPower.
    # The sum of pConstantImpedance, pConstantCurrent and pConstantPower shall equal
    # 1.
    # The sum of qConstantImpedance, qConstantCurrent and qConstantPower shall equal
    # 1.
    exponentModel_: bool  = None
 
    # Portion of active power load modeled as constant current.
    pConstantCurrent_: Simple_Float  = None
 
    # Portion of active power load modeled as constant impedance.
    pConstantImpedance_: Simple_Float  = None
 
    # Portion of active power load modeled as constant power.
    pConstantPower_: Simple_Float  = None
 
    # Exponent of per unit frequency effecting active power.
    pFrequencyExponent_: Simple_Float  = None
 
    # Exponent of per unit voltage effecting real power.
    pVoltageExponent_: Simple_Float  = None
 
    # Portion of reactive power load modeled as constant current.
    qConstantCurrent_: Simple_Float  = None
 
    # Portion of reactive power load modeled as constant impedance.
    qConstantImpedance_: Simple_Float  = None
 
    # Portion of reactive power load modeled as constant power.
    qConstantPower_: Simple_Float  = None
 
    # Exponent of per unit frequency effecting reactive power.
    qFrequencyExponent_: Simple_Float  = None
 
    # Exponent of per unit voltage effecting reactive power.
    qVoltageExponent_: Simple_Float  = None
     