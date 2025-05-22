from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEAC8B(ExcitationSystemDynamics):
    """The class represents IEEE Std 421.5-2005 type AC8B model. This model represents
    a PID voltage regulator with either a brushless exciter or dc exciter. The AVR
    in this model consists of PID control, with separate constants for the
    proportional (<b>K</b><b><sub>PR</sub></b>), integral
    (<b>K</b><b><sub>IR</sub></b>), and derivative (<b>K</b><b><sub>DR</sub></b>)
    gains. The representation of the brushless exciter (<b>T</b><b><sub>E</sub></b>,
    <b>K</b><b><sub>E</sub></b>, <b>S</b><b><sub>E</sub></b>,
    <b>K</b><b><sub>C</sub></b>, <b>K</b><b><sub>D</sub></b>) is similar to the
    model Type AC2A. The Type AC8B model can be used to represent static voltage
    regulators applied to brushless excitation systems. Digitally based voltage
    regulators feeding dc rotating main exciters can be represented with the AC
    Type AC8B model with the parameters <b>K</b><b><sub>C</sub></b> and
    <b>K</b><b><sub>D</sub></b> set to 0.  For thyristor power stages fed from the
    generator terminals, the limits <b>V</b><b><sub>RMAX</sub></b> and
    <b>V</b><b><sub>RMIN</sub></b> should be a function of terminal voltage:
    <b>V</b><b><sub>T</sub></b> * <b>V</b><b><sub>RMAX</sub></b><sub> </sub>and
    <b>V</b><b><sub>T</sub></b> * <b>V</b><b><sub>RMIN</sub></b>.
    
    
      Reference: IEEE Standard 421.5-2005 Section 6.8.
    """
    # Voltage regulator proportional gain (K<sub>PR</sub>).  Typical Value = 80.
    kpr_: PU  = None
 
    # Voltage regulator integral gain (K<sub>IR</sub>).  Typical Value = 5.
    kir_: PU  = None
 
    # Voltage regulator derivative gain (K<sub>DR</sub>).  Typical Value = 10.
    kdr_: PU  = None
 
    # Lag time constant (T<sub>DR</sub>).  Typical Value = 0.1.
    tdr_: Seconds  = None
 
    # Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 35.
    vrmax_: PU  = None
 
    # Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = 0.
    vrmin_: PU  = None
 
    # Voltage regulator gain (K<sub>A</sub>).  Typical Value = 1.
    ka_: PU  = None
 
    # Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.
    ta_: Seconds  = None
 
    # Exciter time constant, integration rate associated with exciter control
    # (T<sub>E</sub>).  Typical Value = 1.2.
    te_: Seconds  = None
 
    # Exciter field current limit reference (V<sub>FEMAX</sub>).  Typical Value = 6.
    vfemax_: PU  = None
 
    # Minimum exciter voltage output (V<sub>EMIN</sub>).  Typical Value = 0.
    vemin_: PU  = None
 
    # Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
    # = 1.
    ke_: PU  = None
 
    # Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
    # Typical Value = 0.55.
    kc_: PU  = None
 
    # Demagnetizing factor, a function of exciter alternator reactances
    # (K<sub>D</sub>).    Typical Value = 1.1.
    kd_: PU  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (V<sub>E1</sub>) equals V<sub>EMAX</sub> (V<sub>E1</sub>).
    #  Typical Value = 6.5.
    ve1_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]).
    # Typical Value = 0.3.
    seve1_: Simple_Float  = None
 
    # Exciter alternator output voltages back of commutating reactance at which
    # saturation is defined (V<sub>E2</sub>).  Typical Value = 9.
    ve2_: PU  = None
 
    # Exciter saturation function value at the corresponding exciter voltage,
    # V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]).
    # Typical Value = 3.
    seve2_: Simple_Float  = None
     