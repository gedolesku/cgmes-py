from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAC5A(ExcitationSystemDynamics):
    """Modified IEEE AC5A alternator-supplied rectifier excitation system with
    different minimum controller output.
    """
    # Voltage regulator gain (Ka).  Typical Value = 400.
    ka_: PU  = None
 
    # Coefficient to allow different usage of the model-speed coefficient (Ks).
    # Typical Value = 0.
    ks_: PU  = None
 
    # Voltage regulator time constant (Tb).  Typical Value = 0.
    tb_: Seconds  = None
 
    # Voltage regulator time constant (Tc).  Typical Value = 0.
    tc_: Seconds  = None
 
    # Voltage regulator time constant (Ta).  Typical Value = 0.02.
    ta_: Seconds  = None
 
    # Maximum voltage regulator output (Vrmax).  Typical Value = 7.3.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (Vrmin).  Typical Value =-7.3.
    vrmin_: PU  = None
 
    # Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    ke_: PU  = None
 
    # Exciter time constant, integration rate associated with exciter control (Te).
    # Typical Value = 0.8.
    te_: Seconds  = None
 
    # Excitation control system stabilizer gains (Kf).  Typical Value = 0.03.
    kf_: PU  = None
 
    # Excitation control system stabilizer time constant (Tf1).  Typical Value  = 1.
    tf1_: Seconds  = None
 
    # Excitation control system stabilizer time constant (Tf2).  Typical Value = 0.8.
    tf2_: Seconds  = None
 
    # Excitation control system stabilizer time constant (Tf3).  Typical Value = 0.
    tf3_: Seconds  = None
 
    # Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value =
    # 5.6.
    efd1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Efd1
    # (S<sub>E</sub>[Efd1]).  Typical Value = 0.86.
    seefd1_: Simple_Float  = None
 
    # Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value =
    # 4.2.
    efd2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage, Efd2
    # (S<sub>E</sub>[Efd2]).  Typical Value = 0.5.
    seefd2_: Simple_Float  = None
 
    # Coefficient to allow different usage of the model (a).  Typical Value = 1.
    a_: Simple_Float  = None
     