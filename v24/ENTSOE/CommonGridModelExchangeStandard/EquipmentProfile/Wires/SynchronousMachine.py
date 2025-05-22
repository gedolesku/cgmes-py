from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Resistance import Resistance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Reactance import Reactance     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.ReactivePower import ReactivePower     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PerCent import PerCent     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Integer import Integer     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.ShortCircuitRotorKind import ShortCircuitRotorKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.SynchronousMachineKind import SynchronousMachineKind     
from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.RotatingMachine import RotatingMachine
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.EquipmentProfile.Wires.ReactiveCapabilityCurve import ReactiveCapabilityCurve     

@dataclass
class SynchronousMachine(RotatingMachine):
    """An electromechanical device that operates with shaft rotating synchronously
    with the network. It is a single machine operating either as a generator or
    synchronous condenser or pump.
    """
    # Indicates whether or not the generator is earthed. Used for short circuit data
    # exchange according to IEC 60909
    earthing_: bool  = None
 
    # Generator star point earthing resistance (Re). Used for short circuit data
    # exchange according to IEC 60909
    earthingStarPointR_: Resistance  = None
 
    # Generator star point earthing reactance (Xe). Used for short circuit data
    # exchange according to IEC 60909
    earthingStarPointX_: Reactance  = None
 
    # Steady-state short-circuit current (in A for the profile) of generator with
    # compound excitation during 3-phase short circuit.
    # - Ikk=0: Generator with no compound excitation.
    # - Ikk?0: Generator with compound excitation.
    # Ikk is used to calculate the minimum steady-state short-circuit current for
    # generators with compound excitation
    # (Section 4.6.1.2 in the IEC 60909-0)
    # Used only for single fed short circuit on a generator. (Section 4.3.4.2. in the
    # IEC 60909-0)
    ikk_: CurrentFlow  = None
 
    # Maximum reactive power limit. This is the maximum (nameplate) limit for the
    # unit.
    maxQ_: ReactivePower  = None
 
    # Minimum reactive power limit for the unit.
    minQ_: ReactivePower  = None
 
    # Factor to calculate the breaking current (Section 4.5.2.1 in the IEC 60909-0).
    # Used only for single fed short circuit on a generator (Section 4.3.4.2. in the
    # IEC 60909-0).
    mu_: Simple_Float  = None
 
    # Percent of the coordinated reactive control that comes from this machine.
    qPercent_: PerCent  = None
 
    # Zero sequence resistance of the synchronous machine.
    r0_: PU  = None
 
    # Negative sequence resistance.
    r2_: PU  = None
 
    # Priority of unit for use as powerflow voltage phase angle reference bus
    # selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and
    # so on.
    referencePriority_: int  = None
 
    # Direct-axis subtransient reactance saturated, also known as Xd"sat.
    satDirectSubtransX_: PU  = None
 
    # Direct-axes saturated synchronous reactance (xdsat); reciprocal of short-
    # circuit ration. Used for short circuit data exchange, only for single fed short
    # circuit on a generator. (Section 4.3.4.2. in the IEC 60909-0).
    satDirectSyncX_: PU  = None
 
    # Saturated Direct-axis transient reactance. The attribute is primarily used for
    # short circuit calculations according to ANSI.
    satDirectTransX_: PU  = None
 
    # Type of rotor, used by short circuit applications, only for single fed short
    # circuit according to IEC 60909.
    shortCircuitRotorType_: ShortCircuitRotorKind  = None
 
    # Modes that this synchronous machine can operate in.
    type_: SynchronousMachineKind  = None
 
    # Range of generator voltage regulation (PG in the IEC 60909-0) used for
    # calculation of the impedance correction factor KG defined in IEC 60909-0
    # This attribute is used to describe the operating voltage of the generating unit.
    voltageRegulationRange_: PerCent  = None
 
    # Equivalent resistance (RG) of generator. RG is considered for the calculation
    # of all currents, except for the calculation of the peak current ip. Used for
    # short circuit data exchange according to IEC 60909
    r_: Resistance  = None
 
    # Zero sequence reactance of the synchronous machine.
    x0_: PU  = None
 
    # Negative sequence reactance.
    x2_: PU  = None
 
    # Synchronous machines using this curve as default.
    ReactiveCapabilityCurve_: Optional[ReactiveCapabilityCurve] = None
     