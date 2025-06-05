from enum import Enum

class SynchronousMachineOperatingMode(Enum):
    generator = 'generator'
    condenser = 'condenser'
    motor = 'motor'
