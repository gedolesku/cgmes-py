from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.SynchronousMachineDynamics.IfdBaseKind import IfdBaseKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.CurrentFlow import CurrentFlow     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics import SynchronousMachineDynamics

@dataclass
class SynchronousMachineDetailed(SynchronousMachineDynamics):
    """All synchronous machine detailed types use a subset of the same data parameters
    and input/output variables.
      The several variations differ in the following ways:
      <ul>
      	<li>The number of  equivalent windings that are included</li>
      	<li>The way in which saturation is incorporated into the model.</li>
      	<li>Whether or not “subtransient saliency” (<b>X''q</b> not = <b>X''d</b>)
    is represented.</li>
      </ul>
      <b>Note:</b> It is not necessary for each simulation tool to have separate
    models for each of the model types.  The same model can often be used for
    several types by alternative logic within the model.  Also, differences in
    saturation representation may not result in significant model performance
    differences so model substitutions are often acceptable.
    """
    # Q-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical Value
    # = 0.02.
    saturationFactorQAxis_: Simple_Float  = None
 
    # Q-axis saturation factor at 120% of rated terminal voltage (S12q) (>=S1q).
    # Typical Value = 0.12.
    saturationFactor120QAxis_: Simple_Float  = None
 
    # Ratio of Efd bases of exciter and generator models.  Typical Value = 1.
    efdBaseRatio_: Simple_Float  = None
 
    # Excitation base system mode.  Typical Value = ifag.
    ifdBaseType_: IfdBaseKind  = None
 
    # Ifd base current if .ifdBaseType = other.
    # Not needed if .ifdBaseType not = other.
    # Unit = A.  Typical Value = 0.
    ifdBaseValue_: CurrentFlow  = None
     