from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEAC4A(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type AC4A model. The model represents
    type AC4A alternator-supplied controlled-rectifier excitation system which is
    quite different from the other type ac systems. This high initial response
    excitation system utilizes a full thyristor bridge in the exciter output
    circuit.  The voltage regulator controls the firing of the thyristor bridges.
    The exciter alternator uses an independent voltage regulator to control its
    output voltage to a constant value. These effects are not modeled; however,
    transient loading effects on the exciter alternator are included.
    
    
      Reference: IEEE Standard 421.5-2005 Section 6.4.
    """
    # Maximum voltage regulator input limit (V<sub>IMAX</sub>).  Typical Value = 10.
    vimax_: PU  = None
 
    # Minimum voltage regulator input limit (V<sub>IMIN</sub>).  Typical Value = -10.
    vimin_: PU  = None
 
    # Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 1.
    tc_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 10.
    tb_: Seconds  = None
 
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 200.
    ka_: PU  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.015.
    ta_: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 5.64.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -4.53.
    vrmin_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
    # Typical Value = 0.
    kc_: PU  = None
     