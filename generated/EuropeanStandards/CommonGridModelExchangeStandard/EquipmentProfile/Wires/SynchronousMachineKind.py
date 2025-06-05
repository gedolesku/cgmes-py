from enum import Enum

class SynchronousMachineKind(Enum):
    generator = 'generator'
    condenser = 'condenser'
    generatorOrCondenser = 'generatorOrCondenser'
    motor = 'motor'
    generatorOrMotor = 'generatorOrMotor'
    motorOrCondenser = 'motorOrCondenser'
    generatorOrCondenserOrMotor = 'generatorOrCondenserOrMotor'
