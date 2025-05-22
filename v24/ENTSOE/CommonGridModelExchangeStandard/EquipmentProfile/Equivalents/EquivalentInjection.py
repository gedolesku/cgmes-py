from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Equivalents.EquivalentEquipment import EquivalentEquipment
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.ReactiveCapabilityCurve import ReactiveCapabilityCurve     

@dataclass
class EquivalentInjection(EquivalentEquipment):
    """This class represents equivalent injections (generation or load).  Voltage
    regulation is allowed only at the point of connection.
    """
    # Maximum active power of the injection.
    maxP: ActivePower  = None
 
    # Used for modeling of infeed for load flow exchange. Not used for short circuit
    # modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used.   
    maxQ: ReactivePower  = None
 
    # Minimum active power of the injection.
    minP: ActivePower  = None
 
    # Used for modeling of infeed for load flow exchange. Not used for short circuit
    # modeling.  If maxQ and minQ are not used ReactiveCapabilityCurve can be used.
    minQ: ReactivePower  = None
 
    # Positive sequence resistance. Used to represent Extended-Ward (IEC 60909).
    # Usage : Extended-Ward is a result of network reduction prior to the data
    # exchange. 
    r: Resistance  = None
 
    # Zero sequence resistance. Used to represent Extended-Ward (IEC 60909).
    # Usage : Extended-Ward is a result of network reduction prior to the data
    # exchange. 
    r0: Resistance  = None
 
    # Negative sequence resistance. Used to represent Extended-Ward (IEC 60909).
    # Usage : Extended-Ward is a result of network reduction prior to the data
    # exchange. 
    r2: Resistance  = None
 
    # Specifies whether or not the EquivalentInjection has the capability to regulate
    # the local voltage.
    regulationCapability: bool  = None
 
    # Positive sequence reactance. Used to represent Extended-Ward (IEC 60909).
    # Usage : Extended-Ward is a result of network reduction prior to the data
    # exchange. 
    x: Reactance  = None
 
    # Zero sequence reactance. Used to represent Extended-Ward (IEC 60909).
    # Usage : Extended-Ward is a result of network reduction prior to the data
    # exchange. 
    x0: Reactance  = None
 
    # Negative sequence reactance. Used to represent Extended-Ward (IEC 60909).
    # Usage : Extended-Ward is a result of network reduction prior to the data
    # exchange. 
    x2: Reactance  = None
 
    # The equivalent injection using this reactive capability curve.
    ReactiveCapabilityCurve_ref: Optional[ReactiveCapabilityCurve] = None
    ReactiveCapabilityCurve: str = None
     