from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcPIC(ExcitationSystemDynamics):
    """Proportional/Integral Regulator Excitation System Model.  This model can be
    used to represent excitation systems with a proportional-integral (PI) voltage
    regulator controller.
    """
    # PI controller gain (Ka).  Typical Value = 3.15.
    ka_: PU  = None
 
    # PI controller time constant (Ta1).  Typical Value = 1.
    ta1_: Seconds  = None
 
    # PI maximum limit (Vr1).  Typical Value = 1.
    vr1_: PU  = None
 
    # PI minimum limit (Vr2).  Typical Value = -0.87.
    vr2_: PU  = None
 
    # Voltage regulator time constant (Ta2).  Typical Value = 0.01.
    ta2_: Seconds  = None
 
    # Lead time constant (Ta3).  Typical Value = 0.
    ta3_: Seconds  = None
 
    # Lag time constant (Ta4).  Typical Value = 0.
    ta4_: Seconds  = None
 
    # Voltage regulator maximum limit (Vrmax).  Typical Value = 1.
    vrmax_: PU  = None
 
    # Voltage regulator minimum limit (Vrmin).  Typical Value = -0.87.
    vrmin_: PU  = None
 
    # Rate feedback gain (Kf).  Typical Value = 0.
    kf_: PU  = None
 
    # Rate feedback time constant (Tf1).  Typical Value = 0.
    tf1_: Seconds  = None
 
    # Rate feedback lag time constant (Tf2).  Typical Value = 0.
    tf2_: Seconds  = None
 
    # Exciter maximum limit (Efdmax).  Typical Value = 8.
    efdmax_: PU  = None
 
    # Exciter minimum limit (Efdmin).  Typical Value = -0.87.
    efdmin_: PU  = None
 
    # Exciter constant (Ke).  Typical Value = 0.
    ke_: PU  = None
 
    # Exciter time constant (Te).  Typical Value = 0.
    te_: Seconds  = None
 
    # Field voltage value 1 (E1).  Typical Value = 0.
    e1_: PU  = None
 
    # Saturation factor at E1 (Se1).  Typical Value = 0.
    se1_: PU  = None
 
    # Field voltage value 2 (E2).  Typical Value = 0.
    e2_: PU  = None
 
    # Saturation factor at E2 (Se2).  Typical Value = 0.
    se2_: PU  = None
 
    # Potential source gain (Kp).  Typical Value = 6.5.
    kp_: PU  = None
 
    # Current source gain (Ki).  Typical Value = 0.
    ki_: PU  = None
 
    # Exciter regulation factor (Kc).  Typical Value = 0.08.
    kc_: PU  = None
     