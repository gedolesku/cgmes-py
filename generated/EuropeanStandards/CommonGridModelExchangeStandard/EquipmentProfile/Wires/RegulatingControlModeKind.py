from enum import Enum

class RegulatingControlModeKind(Enum):
    voltage = 'voltage'
    activePower = 'activePower'
    reactivePower = 'reactivePower'
    currentFlow = 'currentFlow'
    admittance = 'admittance'
    timeScheduled = 'timeScheduled'
    temperature = 'temperature'
    powerFactor = 'powerFactor'
