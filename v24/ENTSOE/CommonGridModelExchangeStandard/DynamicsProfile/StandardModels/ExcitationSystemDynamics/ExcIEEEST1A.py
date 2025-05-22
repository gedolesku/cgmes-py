from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcIEEEST1AUELselectorKind import ExcIEEEST1AUELselectorKind     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEST1A(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type ST1A model. This model represents
    systems in which excitation power is supplied through a transformer from the
    generator terminals (or the unit’s auxiliary bus) and is regulated by a
    controlled rectifier.  The maximum exciter voltage available from such systems
    is directly related to the generator terminal voltage.
    
      Reference: IEEE Standard 421.5-2005 Section 7.1.
    """
    # Exciter output current limit reference (I<sub>LR</sub>).  Typical Value = 0.
    ilr_: PU  = None
 
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 190.
    ka_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
    # Typical Value = 0.08.
    kc_: PU  = None
 
    # Excitation control system stabilizer gains (K<sub>F</sub>).  Typical Value = 0.
    kf_: PU  = None
 
    # Exciter output current limiter gain (K<sub>LR</sub>).  Typical Value = 0.
    klr_: PU  = None
 
    # Selector of the Power System Stabilizer (PSS) input (PSSin).
    # true = PSS input (Vs) added to error signal
    # false = PSS input (Vs) added to voltage regulator output.
    # Typical Value = true.
    pssin_: bool  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.
    ta_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 10.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>B1</sub>).  Typical Value = 0.
    tb1_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 1.
    tc_: Seconds  = None
 
    # Voltage regulator time constant (T<sub>C1</sub>).  Typical Value = 0.
    tc1_: Seconds  = None
 
    # Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
    # Value = 1.
    tf_: Seconds  = None
 
    # Selector of the connection of the UEL input (UELin). Typical Value =
    # ignoreUELsignal.
    uelin_: ExcIEEEST1AUELselectorKind  = None
 
    # Maximum voltage regulator output (V<sub>AMAX</sub>).  Typical Value = 14.5.
    vamax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>AMIN</sub>).  Typical Value = -14.5.
    vamin_: PU  = None
 
    # Maximum voltage regulator input limit (V<sub>IMAX</sub>).  Typical Value = 999.
    vimax_: PU  = None
 
    # Minimum voltage regulator input limit (V<sub>IMIN</sub>).  Typical Value = -999.
    vimin_: PU  = None
 
    # Maximum voltage regulator outputs (V<sub>RMAX</sub>).  Typical Value = 7.8.
    vrmax_: PU  = None
 
    # Minimum voltage regulator outputs (V<sub>RMIN</sub>).  Typical Value = -6.7.
    vrmin_: PU  = None
     