from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.GeneratorControlSource import GeneratorControlSource     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PerCent import PerCent     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ActivePower import ActivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Money import Money     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Production.GrossToNetActivePowerCurve import GrossToNetActivePowerCurve     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Core.Equipment import Equipment

@dataclass
class GeneratingUnit(Equipment):
    """A single or set of synchronous machines for converting mechanical power into
    alternating-current power. For example, individual machines within a set may be
    defined for scheduling purposes while a single control signal is derived for
    the set. In this case there would be a GeneratingUnit for each member of the
    set and an additional GeneratingUnit corresponding to the set.
    """
    # The source of controls for a generating unit.
    genControlSource_: GeneratorControlSource  = None
 
    # Governor Speed Changer Droop.   This is the change in generator power output
    # divided by the change in frequency normalized by the nominal power of the
    # generator and the nominal frequency and expressed in percent and negated. A
    # positive value of speed change droop provides additional generator output upon
    # a drop in frequency.
    governorSCD_: PerCent  = None
 
    # Default initial active power  which is used to store a powerflow result for the
    # initial active power for this unit in this network configuration.
    initialP_: ActivePower  = None
 
    # Generating unit long term economic participation factor.
    longPF_: Simple_Float  = None
 
    # Maximum allowable spinning reserve. Spinning reserve will never be considered
    # greater than this value regardless of the current operating point.
    maximumAllowableSpinningReserve_: ActivePower  = None
 
    # This is the maximum operating active power limit the dispatcher can enter for
    # this unit.
    maxOperatingP_: ActivePower  = None
 
    # This is the minimum operating active power limit the dispatcher can enter for
    # this unit.
    minOperatingP_: ActivePower  = None
 
    # The nominal power of the generating unit.  Used to give precise meaning to
    # percentage based attributes such as the governor speed change droop
    # (governorSCD attribute).
    # The attribute shall be a positive value equal or less than RotatingMachine.
    # ratedS.
    nominalP_: ActivePower  = None
 
    # The unit's gross rated maximum capacity (book value).
    ratedGrossMaxP_: ActivePower  = None
 
    # The gross rated minimum generation level which the unit can safely operate at
    # while delivering power to the transmission grid.
    ratedGrossMinP_: ActivePower  = None
 
    # The net rated maximum capacity determined by subtracting the auxiliary power
    # used to operate the internal plant machinery from the rated gross maximum
    # capacity.
    ratedNetMaxP_: ActivePower  = None
 
    # Generating unit short term economic participation factor.
    shortPF_: Simple_Float  = None
 
    # The initial startup cost incurred for each start of the GeneratingUnit.
    startupCost_: Money  = None
 
    # The variable cost component of production per unit of ActivePower.
    variableCost_: Money  = None
 
    # The efficiency of the unit in converting the fuel into electrical energy.
    totalEfficiency_: PerCent  = None
 
    # A generating unit may have a gross active power to net active power curve,
    # describing the losses and auxiliary power requirements of the unit.
    GrossToNetActivePowerCurve_: List[GrossToNetActivePowerCurve]  = field(default_factory=list)
     