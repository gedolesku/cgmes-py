from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock

@dataclass
class RotatingMachineDynamics(DynamicsFunctionBlock):
    """Abstract parent class for all synchronous and asynchronous machine standard
    models.
    """
    # Damping torque coefficient (D).  A proportionality constant that, when
    # multiplied by the angular velocity of the rotor poles with respect to the
    # magnetic field (frequency), results in the damping torque.  This value is often
    # zero when the sources of damping torques (generator damper windings, load
    # damping effects, etc.) are modelled in detail.  Typical Value = 0.
    damping_: Simple_Float  = None
 
    # Inertia constant of generator or motor and mechanical load (H) (>0).  This is
    # the specification for the stored energy in the rotating mass when operating at
    # rated speed.  For a generator, this includes the generator plus all other
    # elements (turbine, exciter) on the same shaft and has units of MW*sec.  For a
    # motor, it includes the motor plus its mechanical load. Conventional units are
    # per unit on the generator MVA base, usually expressed as MW*second/MVA or just
    # second.   This value is used in the accelerating power reference frame for
    # operator training simulator solutions.  Typical Value = 3.
    inertia_: Seconds  = None
 
    # Saturation factor at rated terminal voltage (S1) (> or =0).  Not used by
    # simplified model.  Defined by defined by S(E1) in the
    # SynchronousMachineSaturationParameters diagram.  Typical Value = 0.02.
    saturationFactor_: Simple_Float  = None
 
    # Saturation factor at 120% of rated terminal voltage (S12) (> or =S1). Not used
    # by the simplified model, defined by S(E2) in the
    # SynchronousMachineSaturationParameters diagram.  Typical Value = 0.12.
    saturationFactor120_: Simple_Float  = None
 
    # Stator leakage reactance (Xl) (> or =0). Typical Value = 0.15.
    statorLeakageReactance_: PU  = None
 
    # Stator (armature) resistance (Rs) (> or =0). Typical Value = 0.005.
    statorResistance_: PU  = None
     