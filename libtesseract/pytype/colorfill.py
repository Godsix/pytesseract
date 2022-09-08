from ctypes import Structure, POINTER, c_int
from .pix import LPPix, LPPixa, LPBoxa
from .array_h import LPNumaa, LPL_Dnaa


class L_Colorfill(Structure):
    '''Colorfill data'''
    _fields_ = [
        ("pixs", LPPix),   # clone of source pix
        ("pixst", LPPix),   # source pix, after optional transform
        ("nx", c_int),   # number of tiles in each tile row
        ("ny", c_int),   # number of tiles in each tile column
        ("tw", c_int),   # width of each tile
        ("th", c_int),   # height of each tile
        ("minarea", c_int),   # min number of pixels in a color region
        ("boxas", LPBoxa),   # tile locations
        ("pixas", LPPixa),   # tiles from source pix
        ("pixam", LPPixa),   # mask tiles with components covering
        ("naa", LPNumaa),   # sizes of color regions (in pixels)
        ("dnaa", LPL_Dnaa),   # average color in each region
        ("pixadb", LPPixa)  # debug reconstruction from segmentation
    ]


LPL_Colorfill = POINTER(L_Colorfill)
LPLPL_Colorfill = POINTER(LPL_Colorfill)
