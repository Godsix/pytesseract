# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:05 2022

@author: 皓
"""
from ctypes import Structure, POINTER, c_int
from ..datatype import c_ubyte_p


class L_ByteBuffer(Structure):
    '''Expandable byte buffer for memory read/write operations'''
    _fields_ = [
        ("nalloc", c_int),   # size of allocated byte array
        ("n", c_int),   # number of bytes read into to the array
        ("nwritten", c_int),   # number of bytes written from the array
        ("array", c_ubyte_p)  # byte array
    ]


LPL_ByteBuffer = POINTER(L_ByteBuffer)
LPLPL_ByteBuffer = POINTER(LPL_ByteBuffer)
