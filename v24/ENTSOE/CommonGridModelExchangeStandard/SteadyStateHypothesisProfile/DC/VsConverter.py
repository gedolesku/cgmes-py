from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.DC.VsPpccControlKind import VsPpccControlKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.DC.VsQpccControlKind import VsQpccControlKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PerCent import PerCent     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Voltage import Voltage     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.DC.ACDCConverter import ACDCConverter

@dataclass
class VsConverter(ACDCConverter):
    """DC side of the voltage source converter (VSC).
    """
    # Droop constant; pu value is obtained as D [kV^2 / MW] x Sb / Ubdc^2.
    droop: PU  = None
 
    # Compensation (resistance) constant. Used to compensate for voltage drop when
    # controlling voltage at a distant bus.
    droopCompensation: Resistance  = None
 
    # Kind of control of real power and/or DC voltage.
    pPccControl: VsPpccControlKind  = None
 
    qPccControl: VsQpccControlKind  = None
 
    # Reactive power sharing factor among parallel converters on Uac control.
    qShare: PerCent  = None
 
    # Reactive power injection target in AC grid, at point of common coupling.
    targetQpcc: ReactivePower  = None
 
    # Voltage target in AC grid, at point of common coupling.
    targetUpcc: Voltage  = None
     