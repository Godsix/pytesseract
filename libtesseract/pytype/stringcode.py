from enum import IntEnum
from ctypes import Structure, POINTER, c_int
from .array_h import LPSarray


class StringcodeSelect(IntEnum):
    '''Stringcode Select'''
    L_STR_TYPE = 0  # typedef for the data type
    L_STR_NAME = 1  # name of the data type
    L_STR_READER = 2  # reader to get the data type from file
    L_STR_MEMREADER = 3  # reader to get the compressed string in memory


class L_StrCode(Structure):
    _fields_ = [
        ("fileno", c_int),   # index for function and output file names
        ("ifunc", c_int),   # index into struct currently being stored
        ("function", LPSarray),   # store case code for extraction
        ("data", LPSarray),   # store base64 encoded data as strings
        ("descr", LPSarray),   # store line in description table
        ("n", c_int)  # number of data strings
    ]


LPL_StrCode = POINTER(L_StrCode)
LPLPL_StrCode = POINTER(LPL_StrCode)
