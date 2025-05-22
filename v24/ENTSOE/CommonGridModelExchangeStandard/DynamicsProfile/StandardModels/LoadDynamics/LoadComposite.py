from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.LoadDynamics.LoadDynamics import LoadDynamics

@dataclass
class LoadComposite(LoadDynamics):
    """This models combines static load and induction motor load effects.
      The dynamics of the motor are simplified by linearizing the induction machine
    equations.
    """
    # Active load-voltage dependence index (static) (Epvs).  Typical Value = 0.7.
    epvs_: Simple_Float  = None
 
    # Active load-frequency dependence index (static) (Epfs).  Typical Value = 1.5.
    epfs_: Simple_Float  = None
 
    # Reactive load-voltage dependence index (static) (Eqvs).  Typical Value = 2.
    eqvs_: Simple_Float  = None
 
    # Reactive load-frequency dependence index (static) (Eqfs).  Typical Value = 0.
    eqfs_: Simple_Float  = None
 
    # Active load-voltage dependence index (dynamic) (Epvd).  Typical Value = 0.7.
    epvd_: Simple_Float  = None
 
    # Active load-frequency dependence index (dynamic) (Epfd).  Typical Value = 1.5.
    epfd_: Simple_Float  = None
 
    # Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical Value = 2.
    eqvd_: Simple_Float  = None
 
    # Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical Value = 0.
    eqfd_: Simple_Float  = None
 
    # Loading factor � ratio of initial P to motor MVA base (Lfrac).  Typical Value =
    # 0.8.
    lfrac_: Simple_Float  = None
 
    # Inertia constant (H).  Typical Value = 2.5.
    h_: Seconds  = None
 
    # Fraction of constant-power load to be represented by this motor model (Pfrac)
    # (>=0.0 and <=1.0).  Typical Value = 0.5.
    pfrac_: Simple_Float  = None
     