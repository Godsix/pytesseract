# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:05 2022

@author: 皓
"""
from ctypes import Structure, c_int, c_void_p, POINTER


class L_Heap(Structure):
    '''Heap of arbitrary void* data'''
    _fields_ = [
        ("nalloc", c_int),   # size of allocated ptr array
        ("n", c_int),   # number of elements stored in the heap
        ("array", POINTER(c_void_p)),   # ptr array
        ("direction", c_int)  # L_SORT_INCREASING or L_SORT_DECREASING
    ]


LPL_Heap = POINTER(L_Heap)
LPLPL_Heap = POINTER(LPL_Heap)
