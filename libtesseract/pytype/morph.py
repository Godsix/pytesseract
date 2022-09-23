# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:06 2022

@author: 皓
"""
from enum import IntEnum
from ctypes import Structure, c_int, c_char_p, POINTER
from ..datatype import c_int_p, c_float_p


class MorphBoundary(IntEnum):
    '''Morph Boundary'''
    SYMMETRIC_MORPH_BC = 0
    ASYMMETRIC_MORPH_BC = 1


class SELVals(IntEnum):
    '''SEL Vals'''
    SEL_DONT_CARE = 0
    SEL_HIT = 1
    SEL_MISS = 2


class RunlengthPolarity(IntEnum):
    '''Runlength Polarity'''
    L_RUN_OFF = 0
    L_RUN_ON = 1


class DirectionFlags(IntEnum):
    '''Direction Flags'''
    L_HORIZ = 1
    L_VERT = 2
    L_BOTH_DIRECTIONS = 3


class MorphOperator(IntEnum):
    '''Morph Operator'''
    L_MORPH_DILATE = 1
    L_MORPH_ERODE = 2
    L_MORPH_OPEN = 3
    L_MORPH_CLOSE = 4
    L_MORPH_HMT = 5


class PixelValueScaling(IntEnum):
    '''Pixel Value Scaling'''
    L_LINEAR_SCALE = 1
    L_LOG_SCALE = 2


class MorphTophat(IntEnum):
    '''Morph Tophat'''
    L_TOPHAT_WHITE = 0
    L_TOPHAT_BLACK = 1


class ArithLogicalOps(IntEnum):
    '''ArithLogical Ops'''
    L_ARITH_ADD = 1
    L_ARITH_SUBTRACT = 2
    L_ARITH_MULTIPLY = 3
    L_ARITH_DIVIDE = 4
    L_UNION = 5
    L_INTERSECTION = 6
    L_SUBTRACTION = 7
    L_EXCLUSIVE_OR = 8


class MinMaxSelection(IntEnum):
    '''MinMax Selection'''
    L_CHOOSE_MIN = 1
    L_CHOOSE_MAX = 2
    L_CHOOSE_MAXDIFF = 3
    L_CHOOSE_MIN_BOOST = 4
    L_CHOOSE_MAX_BOOST = 5


class ExteriorValue(IntEnum):
    '''Exterior Value'''
    L_BOUNDARY_BG = 1
    L_BOUNDARY_FG = 2


class ImageComparison(IntEnum):
    '''Image Comparison'''
    L_COMPARE_XOR = 1
    L_COMPARE_SUBTRACT = 2
    L_COMPARE_ABS_DIFF = 3


class Sel(Structure):
    '''Selection'''
    _fields_ = [
        ("sy", c_int),   # sel height
        ("sx", c_int),   # sel width
        ("cy", c_int),   # y location of sel origin
        ("cx", c_int),   # x location of sel origin
        # {0,1,2}; data[i][j] in [row][col] order
        ("data", POINTER(c_int_p)),
        ("name", c_char_p)  # used to find sel by name
    ]


LPSel = POINTER(Sel)
LPLPSel = POINTER(LPSel)


class Sela(Structure):
    '''Array of Sel'''
    _fields_ = [
        ("n", c_int),   # number of sel actually stored
        ("nalloc", c_int),   # size of allocated ptr array
        ("sel", LPLPSel)  # sel ptr array
    ]


LPSela = POINTER(Sela)
LPLPSela = POINTER(LPSela)


class L_Kernel(Structure):
    '''Kernel'''
    _fields_ = [
        ("sy", c_int),   # kernel height
        ("sx", c_int),   # kernel width
        ("cy", c_int),   # y location of kernel origin
        ("cx", c_int),   # x location of kernel origin
        ("data", POINTER(c_float_p))  # data[i][j] in [row][col] order
    ]


LPL_Kernel = POINTER(L_Kernel)
LPLPL_Kernel = POINTER(LPL_Kernel)
