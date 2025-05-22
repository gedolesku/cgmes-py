from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics import AsynchronousMachineDynamics

@dataclass
class AsynchronousMachineEquivalentCircuit(AsynchronousMachineDynamics):
    """The electrical equations of all variations of the asynchronous model are based
    on the AsynchronousEquivalentCircuit diagram for the direct and quadrature axes,
    with two equivalent rotor windings in each axis.
    
      <b>Equations for conversion between Equivalent Circuit and Time Constant
    Reactance forms:</b>
      <b>Xs</b> = <b>Xm</b> + <b>Xl</b>
      <b>X'</b> = <b>Xl</b> + <b>Xm</b> * <b>Xlr1</b> / (<b>Xm</b> + <b>Xlr1</b>)
      <b>X''</b> = <b>Xl</b> + <b>Xm</b> * <b>Xlr1</b>* <b>Xlr2</b> / (<b>Xm</b> *
    <b>Xlr1</b> + <b>Xm</b> * <b>Xlr2</b> + <b>Xlr1</b> * <b>Xlr2</b>)
      <b>T'o</b> = (<b>Xm</b> + <b>Xlr1</b>) / (<b>omega</b><b><sub>0</sub></b> *
    <b>Rr1</b>)
      <b>T''o</b> = (<b>Xm</b> * <b>Xlr1</b> + <b>Xm</b> * <b>Xlr2</b> +
    <b>Xlr1</b> * <b>Xlr2</b>) / (<b>omega</b><b><sub>0</sub></b> * <b>Rr2</b> *
    (<b>Xm </b>+ <b>Xlr1</b>)
      <b>
      </b>Same equations using CIM attributes from
    AsynchronousMachineTimeConstantReactance class on left of = sign and
    AsynchronousMachineEquivalentCircuit class on right (except as noted):
      xs = xm + RotatingMachineDynamics.statorLeakageReactance
      xp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1 / (xm + xlr1)
      xpp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1* xlr2 / (xm
    * xlr1 + xm * xlr2 + xlr1 * xlr2)
      tpo = (xm + xlr1) / (2*pi*nominal frequency * rr1)
      tppo = (xm * xlr1 + xm * xlr2 + xlr1 * xlr2) / (2*pi*nominal frequency * rr2
    * (xm + xlr1).
    """
    # Magnetizing reactance.
    xm_: PU  = None
 
    # Damper 1 winding resistance.
    rr1_: PU  = None
 
    # Damper 1 winding leakage reactance.
    xlr1_: PU  = None
 
    # Damper 2 winding resistance.
    rr2_: PU  = None
 
    # Damper 2 winding leakage reactance.
    xlr2_: PU  = None
     