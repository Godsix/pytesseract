# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:07 2022

@author: 皓
"""
from enum import IntEnum
from ctypes import Structure, POINTER, c_int, c_void_p, c_char_p
from ..datatype import LPFile


class RegtestMode(IntEnum):
    '''Regtest Mode'''
    L_REG_GENERATE = 0
    L_REG_COMPARE = 1
    L_REG_DISPLAY = 2


class L_RegParams(Structure):
    '''Regression test parameter packer'''
    _fields_ = [
        ("fp", LPFile),   # stream to temporary output file for compare mode
        ("testname", c_char_p),   # name of test, without '_reg'
        # name of temp file for compare mode output
        ("tempfile", c_char_p),
        ("mode", c_int),   # generate, compare or display
        ("index", c_int),   # index into saved files for this test; 0-based
        ("success", c_int),   # overall result of the test
        ("display", c_int),   # 1 if in display mode; 0 otherwise
        ("tstart", c_void_p)  # marks beginning of the reg test
    ]


LPL_RegParams = POINTER(L_RegParams)
LPLPL_RegParams = POINTER(LPL_RegParams)
