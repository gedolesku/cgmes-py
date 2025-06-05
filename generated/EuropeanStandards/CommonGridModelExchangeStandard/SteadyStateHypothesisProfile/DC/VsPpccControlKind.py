from enum import Enum

class VsPpccControlKind(Enum):
    pPcc = 'pPcc'
    udc = 'udc'
    pPccAndUdcDroop = 'pPccAndUdcDroop'
    pPccAndUdcDroopWithCompensation = 'pPccAndUdcDroopWithCompensation'
    pPccAndUdcDroopPilot = 'pPccAndUdcDroopPilot'
