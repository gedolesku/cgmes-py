from enum import Enum

class WindQcontrolModesKind(Enum):
    voltage = 'voltage'
    reactivePower = 'reactivePower'
    openLoopReactivePower = 'openLoopReactivePower'
    powerFactor = 'powerFactor'
