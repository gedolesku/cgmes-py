from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePowerPerFrequency import ActivePowerPerFrequency     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RegulatingCondEq import RegulatingCondEq

@dataclass
class ExternalNetworkInjection(RegulatingCondEq):
    """This class represents external network and it is used for IEC 60909
    calculations.
    """
    # Power Frequency Bias. This is the change in power injection divided by the
    # change in frequency and negated.  A positive value of the power frequency bias
    # provides additional power injection upon a drop in frequency.
    governorSCD_: ActivePowerPerFrequency  = None
 
    # Indicates whether initial symmetrical short-circuit current and power have been
    # calculated according to IEC (Ik").
    ikSecond_: bool  = None
 
    #  Maximum initial symmetrical short-circuit currents (Ik" max) in A (Ik" =
    # Sk"/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909
    maxInitialSymShCCurrent_: CurrentFlow  = None
 
    # Maximum active power of the injection.
    maxP_: ActivePower  = None
 
    # Not for short circuit modelling; It is used for modelling of infeed for load
    # flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be
    # used 
    maxQ_: ReactivePower  = None
 
    # Maximum ratio of zero sequence resistance of Network Feeder to its zero
    # sequence reactance (R(0)/X(0) max). Used for short circuit data exchange
    # according to IEC 60909
    maxR0ToX0Ratio_: Simple_Float  = None
 
    # Maximum ratio of positive sequence resistance of Network Feeder to its positive
    # sequence reactance (R(1)/X(1) max). Used for short circuit data exchange
    # according to IEC 60909
    maxR1ToX1Ratio_: Simple_Float  = None
 
    # Maximum ratio of zero sequence impedance to its positive sequence impedance
    # (Z(0)/Z(1) max). Used for short circuit data exchange according to IEC 60909
    maxZ0ToZ1Ratio_: Simple_Float  = None
 
    # Minimum initial symmetrical short-circuit currents (Ik" min) in A (Ik" =
    # Sk"/(SQRT(3) Un)). Used for short circuit data exchange according to IEC 60909
    minInitialSymShCCurrent_: CurrentFlow  = None
 
    # Minimum active power of the injection.
    minP_: ActivePower  = None
 
    # Not for short circuit modelling; It is used for modelling of infeed for load
    # flow exchange. If maxQ and minQ are not used ReactiveCapabilityCurve can be used
    minQ_: ReactivePower  = None
 
    # Indicates whether initial symmetrical short-circuit current and power have been
    # calculated according to IEC (Ik"). Used for short circuit data exchange
    # according to IEC 6090
    minR0ToX0Ratio_: Simple_Float  = None
 
    # Minimum ratio of positive sequence resistance of Network Feeder to its positive
    # sequence reactance (R(1)/X(1) min). Used for short circuit data exchange
    # according to IEC 60909
    minR1ToX1Ratio_: Simple_Float  = None
 
    # Minimum ratio of zero sequence impedance to its positive sequence impedance
    # (Z(0)/Z(1) min). Used for short circuit data exchange according to IEC 60909
    minZ0ToZ1Ratio_: Simple_Float  = None
 
    # Voltage factor in pu, which was used to calculate short-circuit current Ik" and
    # power Sk".
    voltageFactor_: PU  = None
     