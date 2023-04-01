# Constants file
from enum import Enum


class QUBIT_PARA(Enum):
    # Frequency unit
    KHZ = 1.0e3
    MHZ = 1.0e6
    GHZ = 1.0e9

    # th-Qubit used for running
    NUM_QUBIT_TYPE1 = 0
    NUM_QUBIT_TYPE2 = 6

    # Other constants
    CBIT = 0
    ACQUIRE_ALIGNMENT = 16
    PULSE_ALIGNMENT = 16
    GRANULARITY = 16
    LCM = 16

    # Scale
    SCALE_FACTOR = 1e-7
