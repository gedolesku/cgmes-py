from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.DC.CsOperatingModeKind import CsOperatingModeKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.DC.CsPpccControlKind import CsPpccControlKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.AngleDegrees import AngleDegrees     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
from ENTSOE.CommonGridModelExchangeStandard.SteadyStateHypothesisProfile.DC.ACDCConverter import ACDCConverter

@dataclass
class CsConverter(ACDCConverter):
    """DC side of the current source converter (CSC).
    """
    # Indicates whether the DC pole is operating as an inverter or as a rectifier.
    # CSC control variable used in power flow.
    operatingMode_: CsOperatingModeKind  = None
 
    pPccControl_: CsPpccControlKind  = None
 
    # Target firing angle. CSC control variable used in power flow.
    targetAlpha_: AngleDegrees  = None
 
    # Target extinction angle. CSC  control variable used in power flow.
    targetGamma_: AngleDegrees  = None
 
    # DC current target value. CSC control variable used in power flow.
    targetIdc_: CurrentFlow  = None
     