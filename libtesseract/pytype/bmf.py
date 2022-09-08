from enum import IntEnum
from ctypes import Structure, POINTER, c_int, c_char_p
from ..datatype import c_int_p
from .pix import LPPixa


class SplitText(IntEnum):
    '''Split Text'''
    SPLIT_ON_LEADING_WHITE = 1  # tab or space at beginning of line
    SPLIT_ON_BLANK_LINE = 2  # newline with optional white space
    SPLIT_ON_BOTH = 3  # leading white space or newline


class L_Bmf(Structure):
    '''Data structure to hold bitmap fonts and related data'''
    _fields_ = [
        ("pixa", LPPixa),   # pixa of bitmaps for 93 characters
        ("size", c_int),   # font size (in points at 300 ppi)
        ("directory", c_char_p),   # directory containing font bitmaps
        ("baseline1", c_int),   # baseline offset for ascii 33 - 57
        ("baseline2", c_int),   # baseline offset for ascii 58 - 91
        ("baseline3", c_int),   # baseline offset for ascii 93 - 126
        ("lineheight", c_int),   # max height of line of chars
        ("kernwidth", c_int),   # pixel dist between char bitmaps
        ("spacewidth", c_int),   # pixel dist between word bitmaps
        # extra vertical space between text lines
        ("vertlinesep", c_int),
        ("fonttab", c_int_p),   # table mapping ascii --> font index
        # table mapping ascii --> baseline offset
        ("baselinetab", c_int_p),
        ("widthtab", c_int_p)  # table mapping ascii --> char width
    ]


LPL_Bmf = POINTER(L_Bmf)
LPLPL_Bmf = POINTER(LPL_Bmf)
