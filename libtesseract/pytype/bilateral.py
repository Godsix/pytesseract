from ctypes import Structure, c_int, c_float, POINTER
from ..datatype import c_float_p, c_int_p, c_uint_p
from .pix import LPPix, LPPixa


class L_Bilateral(Structure):
    '''Bilateral filter'''
    _fields_ = [
        ("pixs", LPPix),   # clone of source pix
        ("pixsc", LPPix),   # downscaled pix with mirrored border
        ("reduction", c_int),   # 1, 2 or 4x for intermediates
        ("spatial_stdev", c_float),   # stdev of spatial gaussian
        ("range_stdev", c_float),   # stdev of range gaussian
        ("spatial", c_float_p),   # 1D gaussian spatial kernel
        ("range", c_float_p),   # one-sided gaussian range kernel
        ("minval", c_int),   # min value in 8 bpp pix
        ("maxval", c_int),   # max value in 8 bpp pix
        ("ncomps", c_int),   # number of intermediate results
        ("nc", c_int_p),   # set of k values (size ncomps)
        ("kindex", c_int_p),   # mapping from intensity to lower k
        ("kfract", c_float_p),   # mapping from intensity to fract k
        ("pixac", LPPixa),   # intermediate result images (PBC)
        ("lineset", POINTER(POINTER(c_uint_p)))  # lineptrs for pixac
    ]


LPL_Bilateral = POINTER(L_Bilateral)
LPLPL_Bilateral = POINTER(LPL_Bilateral)
