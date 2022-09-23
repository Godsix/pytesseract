# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:07 2022

@author: 皓
"""
from ctypes import Structure, c_int, c_void_p, POINTER
from ..datatype import c_int_p
from .pix import LPPix, LPPixa, LPPta
from .array_h import LPNuma, LPLPNuma


class L_WShed(Structure):
    '''Simple data structure to hold watershed data.'''
    _fields_ = [
        ("pixs", LPPix),   # clone of input 8 bpp pixs
        ("pixm", LPPix),   # clone of input 1 bpp seed (marker) pixm
        ("mindepth", c_int),   # minimum depth allowed for a watershed
        ("pixlab", LPPix),   # 16 bpp label pix
        ("pixt", LPPix),   # scratch pix for computing wshed regions
        ("lines8", POINTER(c_void_p)),   # line ptrs for pixs
        ("linem1", POINTER(c_void_p)),   # line ptrs for pixm
        ("linelab32", POINTER(c_void_p)),   # line ptrs for pixlab
        ("linet1", POINTER(c_void_p)),   # line ptrs for pixt
        ("pixad", LPPixa),   # result: 1 bpp pixa of watersheds
        ("ptas", LPPta),   # pta of initial seed pixels
        ("nasi", LPNuma),   # numa of seed indicators; 0 if completed
        ("nash", LPNuma),   # numa of initial seed heights
        ("namh", LPNuma),   # numa of initial minima heights
        ("nalevels", LPNuma),   # result: numa of watershed levels
        ("nseeds", c_int),   # number of seeds (markers)
        ("nother", c_int),   # number of minima different from seeds
        ("lut", c_int_p),   # lut for pixel indices
        ("links", LPLPNuma),   # back-links into lut, for updates
        ("arraysize", c_int),   # size of links array
        ("debug", c_int)  # set to 1 for debug output
    ]


LPL_WShed = POINTER(L_WShed)
LPLPL_WShed = POINTER(LPL_WShed)
