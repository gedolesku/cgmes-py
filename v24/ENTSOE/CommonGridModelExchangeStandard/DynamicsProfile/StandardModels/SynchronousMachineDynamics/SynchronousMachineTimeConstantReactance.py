from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.SynchronousMachineDynamics.RotorKind import RotorKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.SynchronousMachineDynamics.SynchronousMachineModelKind import SynchronousMachineModelKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.SynchronousMachineDynamics.SynchronousMachineDetailed import SynchronousMachineDetailed

@dataclass
class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
    """Synchronous machine detailed modelling types are defined by the combination of
    the attributes SynchronousMachineTimeConstantReactance.modelType and
    SynchronousMachineTimeConstantReactance.rotorType.
      <b>
      </b><b>Parameter notes:</b>
      <ol>
      	<li>The “p” in the time-related attribute names is a substitution for a
    “prime” in the usual parameter notation, e.g. tpdo refers to <b>T'do</b>.</li>
      </ol>
      <b>
      </b>The parameters used for models expressed in time constant reactance form
    include:
      <ul>
      	<li>RotatingMachine.ratedS (MVAbase)</li>
      	<li>RotatingMachineDynamics.damping (D)</li>
      	<li>RotatingMachineDynamics.inertia (H)</li>
      	<li>RotatingMachineDynamics.saturationFactor (S1)</li>
      	<li>RotatingMachineDynamics.saturationFactor120 (S12)</li>
      	<li>RotatingMachineDynamics.statorLeakageReactance (Xl)</li>
      	<li>RotatingMachineDynamics.statorResistance (Rs)</li>
      	<li>SynchronousMachineTimeConstantReactance.ks (Ks)</li>
      	<li>SynchronousMachineDetailed.saturationFactorQAxis (S1q)</li>
      	<li>SynchronousMachineDetailed.saturationFactor120QAxis (S12q)</li>
      	<li>SynchronousMachineDetailed.efdBaseRatio</li>
      	<li>SynchronousMachineDetailed.ifdBaseType</li>
      	<li>SynchronousMachineDetailed.ifdBaseValue, if present</li>
      	<li>.xDirectSync (Xd)</li>
      	<li>.xDirectTrans (X'd)</li>
      	<li>.xDirectSubtrans (X''d)</li>
      	<li>.xQuadSync (Xq)</li>
      	<li>.xQuadTrans (X'q)</li>
      	<li>.xQuadSubtrans (X''q)</li>
      	<li>.tpdo (T'do)</li>
      	<li>.tppdo (T''do)</li>
      	<li>.tpqo (T'qo)</li>
      	<li>.tppqo (T''qo)</li>
      	<li>.tc.</li>
      </ul>
    """
    # Type of rotor on physical machine.
    rotorType_: RotorKind  = None
 
    # Type of synchronous machine model used in Dynamic simulation applications.
    modelType_: SynchronousMachineModelKind  = None
 
    # Saturation loading correction factor (Ks) (>= 0).  Used only by Type J model.
    # Typical Value = 0.
    ks_: Simple_Float  = None
 
    # Direct-axis synchronous reactance (Xd) (>= X'd).
    # The quotient of a sustained value of that AC component of armature voltage that
    # is produced by the total direct-axis flux due to direct-axis armature current
    # and the value of the AC component of this current, the machine running at rated
    # speed. Typical Value = 1.8.
    xDirectSync_: PU  = None
 
    # Direct-axis transient reactance (unsaturated) (X'd) (> =X''d).  Typical Value =
    # 0.5.
    xDirectTrans_: PU  = None
 
    # Direct-axis subtransient reactance (unsaturated) (X''d) (> Xl).  Typical Value
    # = 0.2.
    xDirectSubtrans_: PU  = None
 
    # Quadrature-axis synchronous reactance (Xq) (> =X'q).
    # The ratio of the component of reactive armature voltage, due to the quadrature-
    # axis component of armature current, to this component of current, under steady
    # state conditions and at rated frequency.  Typical Value = 1.6.
    xQuadSync_: PU  = None
 
    # Quadrature-axis transient reactance (X'q) (> =X''q).  Typical Value = 0.3.
    xQuadTrans_: PU  = None
 
    # Quadrature-axis subtransient reactance (X''q) (> Xl).  Typical Value = 0.2.
    xQuadSubtrans_: PU  = None
 
    # Direct-axis transient rotor time constant (T'do) (> T''do).  Typical Value = 5.
    tpdo_: Seconds  = None
 
    # Direct-axis subtransient rotor time constant (T''do) (> 0).  Typical Value = 0.
    # 03.
    tppdo_: Seconds  = None
 
    # Quadrature-axis transient rotor time constant (T'qo) (> T''qo). Typical Value =
    # 0.5.
    tpqo_: Seconds  = None
 
    # Quadrature-axis subtransient rotor time constant (T''qo) (> 0). Typical Value =
    # 0.03.
    tppqo_: Seconds  = None
 
    # Damping time constant for “Canay” reactance.  Typical Value = 0.
    tc_: Seconds  = None
     