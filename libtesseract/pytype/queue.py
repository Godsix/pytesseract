# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:07 2022

@author: 皓
"""
from ctypes import Structure, c_int, c_void_p, POINTER
from .stack import LPL_Stack


class L_Queue(Structure):
    '''Expandable pointer queue for arbitrary void* data'''
    _fields_ = [
        ("nalloc", c_int),   # size of allocated ptr array
        ("nhead", c_int),   # location of head (in ptrs) from the
        ("nelem", c_int),   # number of elements stored in the queue
        ("array", POINTER(c_void_p)),   # ptr array
        ("stack", LPL_Stack)  # auxiliary stack
    ]


LPL_Queue = POINTER(L_Queue)
LPLPL_Queue = POINTER(LPL_Queue)
