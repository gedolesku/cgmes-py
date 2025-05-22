from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Area import Area     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Frequency import Frequency     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.FrancisGovernorControlKind import FrancisGovernorControlKind     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Length import Length     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.VolumeFlowRate import VolumeFlowRate     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydroFrancis(TurbineGovernorDynamics):
    """Detailed hydro unit - Francis model.  This model can be used to represent three
    types of governors.
      A schematic of the hydraulic system of detailed hydro unit models, like
    Francis and Pelton, is provided in the DetailedHydroModelHydraulicSystem
    diagram.
    """
    # Opening section S<sub>eff</sub> at the maximum efficiency (Am).  Typical Value
    # = 0.7.
    am_: PU  = None
 
    # Area of the surge tank (A<sub>V0</sub>). Unit = m<sup>2</sup>. Typical Value =
    # 30.
    av0_: Area  = None
 
    # Area of the compensation tank (A<sub>V1</sub>). Unit = m<sup>2</sup>. Typical
    # Value = 700.
    av1_: Area  = None
 
    # Droop (Bp).  Typical Value = 0.05.
    bp_: PU  = None
 
    # Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0.
    db1_: Frequency  = None
 
    # Maximum efficiency (EtaMax).  Typical Value = 1.05.
    etamax_: PU  = None
 
    # Governor control flag (Cflag).  Typical Value =
    # mechanicHydrolicTachoAccelerator.
    governorControl_: FrancisGovernorControlKind  = None
 
    # Head of compensation chamber water level with respect to the level of penstock
    # (H<sub>1</sub>).  Unit = m. Typical Value = 4.
    h1_: Length  = None
 
    # Head of surge tank water level with respect to the level of penstock
    # (H<sub>2</sub>).  Unit = m. Typical Value = 40.
    h2_: Length  = None
 
    # Rated hydraulic head (H<sub>n</sub>).  Unit = m. Typical Value = 250.
    hn_: Length  = None
 
    # Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025.
    kc_: PU  = None
 
    # Water tunnel and surge chamber loss coefficient (due to friction) (Kg).
    # Typical Value = 0.025.
    kg_: PU  = None
 
    # Washout gain (Kt).  Typical Value = 0.25.
    kt_: PU  = None
 
    # No-load turbine flow at nominal head (Qc0).  Typical Value = 0.21.
    qc0_: PU  = None
 
    # Rated flow (Q<sub>n</sub>). Unit = m<sup>3</sup>/s. Typical Value = 40.
    qn_: VolumeFlowRate  = None
 
    # Derivative gain (Ta).  Typical Value = 3.
    ta_: Seconds  = None
 
    # Washout time constant (Td).  Typical Value = 3.
    td_: Seconds  = None
 
    # Gate servo time constant (Ts).  Typical Value = 0.5.
    ts_: Seconds  = None
 
    # Water inertia time constant (Twnc).  Typical Value = 1.
    twnc_: Seconds  = None
 
    # Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3.
    twng_: Seconds  = None
 
    # Derivative feedback gain (Tx).  Typical Value = 1.
    tx_: Seconds  = None
 
    # Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.011.
    va_: Simple_Float  = None
 
    # Maximum gate opening (ValvMax).  Typical Value = 1.
    valvmax_: PU  = None
 
    # Minimum gate opening (ValvMin).  Typical Value = 0.
    valvmin_: PU  = None
 
    # Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.011.
    vc_: Simple_Float  = None
 
    # Water tunnel and surge chamber simulation (Tflag).
    # true = enable of water tunnel and surge chamber simulation
    # false = inhibit of water tunnel and surge chamber simulation.
    # Typical Value = false.
    waterTunnelSurgeChamberSimulation_: bool  = None
 
    # Head of upper water level with respect to the level of penstock (Zsfc).  Unit =
    # m.  Typical Value = 25.
    zsfc_: Length  = None
     