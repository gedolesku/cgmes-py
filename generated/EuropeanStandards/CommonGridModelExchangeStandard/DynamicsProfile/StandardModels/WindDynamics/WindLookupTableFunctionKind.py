from enum import Enum

class WindLookupTableFunctionKind(Enum):
    fpslip = 'fpslip'
    fpomega = 'fpomega'
    ipvdl = 'ipvdl'
    iqvdl = 'iqvdl'
    fdpf = 'fdpf'
