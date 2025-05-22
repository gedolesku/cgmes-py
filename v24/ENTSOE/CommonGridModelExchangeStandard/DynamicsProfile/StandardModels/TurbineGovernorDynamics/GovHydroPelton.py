from __future__ import annotations
from typing import List, Optional, Any, TYPE_CHECKING
from dataclasses import dataclass, field
from enum import Enum, auto
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Area import Area     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.PU import PU     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Frequency import Frequency     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Length import Length     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.VolumeFlowRate import VolumeFlowRate     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Boolean import Boolean     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Seconds import Seconds     
if TYPE_CHECKING:          from ENTSOE.CommonGridModelExchangeStandard.DomainProfile.Simple_Float import Simple_Float     
from ENTSOE.CommonGridModelExchangeStandard.DynamicsProfile.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydroPelton(TurbineGovernorDynamics):
    """Detailed hydro unit - Pelton model.  This model can be used to represent the
    dynamic related to water tunnel and surge chamber.
      A schematic of the hydraulic system of detailed hydro unit models, like
    Francis and Pelton, is located under the GovHydroFrancis class.
    """
    # Area of the surge tank (A<sub>V0</sub>). Unit = m<sup>2</sup>. Typical Value =
    # 30.
    av0_: Area  = None
 
    # Area of the compensation tank (A<sub>V1</sub>). Unit = m<sup>2</sup>. Typical
    # Value = 700.
    av1_: Area  = None
 
    # Droop (bp).  Typical Value = 0.05.
    bp_: PU  = None
 
    # Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0.
    db1_: Frequency  = None
 
    # Intentional dead-band width of valve opening error (DB2). Unit = Hz.  Typical
    # Value = 0.01.
    db2_: Frequency  = None
 
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
    # Typical Value = -0.025.
    kg_: PU  = None
 
    # No-load turbine flow at nominal head (Qc0).  Typical Value = 0.05.
    qc0_: PU  = None
 
    # Rated flow (Q<sub>n</sub>). Unit = m<sup>3</sup>/s. Typical Value = 40.
    qn_: VolumeFlowRate  = None
 
    # Simplified Pelton model simulation (Sflag).
    # true = enable of simplified Pelton model simulation
    # false = enable of complete Pelton model simulation (non linear gain).
    # Typical Value = false.
    simplifiedPelton_: bool  = None
 
    # Static compensating characteristic (Cflag).
    # true = enable of static compensating characteristic
    # false = inhibit of static compensating characteristic.
    # Typical Value = false.
    staticCompensating_: bool  = None
 
    # Derivative gain (accelerometer time constant) (Ta).  Typical Value = 3.
    ta_: Seconds  = None
 
    # Gate servo time constant (Ts).  Typical Value = 0.15.
    ts_: Seconds  = None
 
    # Servomotor integrator time constant (TV).  Typical Value = 0.3.
    tv_: Seconds  = None
 
    # Water inertia time constant (Twnc).  Typical Value = 1.
    twnc_: Seconds  = None
 
    # Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3.
    twng_: Seconds  = None
 
    # Electronic integrator time constant (Tx).  Typical Value = 0.5.
    tx_: Seconds  = None
 
    # Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.016.
    va_: Simple_Float  = None
 
    # Maximum gate opening (ValvMax).  Typical Value = 1.
    valvmax_: PU  = None
 
    # Minimum gate opening (ValvMin).  Typical Value = 0.
    valvmin_: PU  = None
 
    # Maximum servomotor valve opening velocity (Vav).  Typical Value = 0.017.
    vav_: PU  = None
 
    # Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.016.
    vc_: Simple_Float  = None
 
    # Maximum servomotor valve closing velocity (Vcv).  Typical Value = -0.017.
    vcv_: PU  = None
 
    # Water tunnel and surge chamber simulation (Tflag).
    # true = enable of water tunnel and surge chamber simulation
    # false = inhibit of water tunnel and surge chamber simulation.
    # Typical Value = false.
    waterTunnelSurgeChamberSimulation_: bool  = None
 
    # Head of upper water level with respect to the level of penstock (Zsfc).  Unit =
    # m. Typical Value = 25.
    zsfc_: Length  = None
     