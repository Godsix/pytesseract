# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:07 2022

@author: 皓
"""
from enum import IntEnum
from ctypes import Structure, c_int, c_void_p, POINTER


class PtraRemoval(IntEnum):
    '''Ptra Removal'''
    L_NO_COMPACTION = 1  # null the pointer only
    L_COMPACTION = 2  # compact the array


class PtraInsertion(IntEnum):
    '''Ptra Insertion'''
    L_AUTO_DOWNSHIFT = 0  # choose based on number of holes
    L_MIN_DOWNSHIFT = 1  # downshifts min # of ptrs below insert
    L_FULL_DOWNSHIFT = 2  # downshifts all ptrs below insert


class PtraaAccessor(IntEnum):
    '''Ptraa Accessor'''
    L_HANDLE_ONLY = 0  # ptr to L_Ptra; caller can inspect only
    L_REMOVE = 1  # caller owns; destroy or save in L_Ptraa


class L_Ptra(Structure):
    '''Generic pointer array'''
    _fields_ = [
        ("nalloc", c_int),   # size of allocated ptr array
        ("imax", c_int),   # greatest valid index
        ("nactual", c_int),   # actual number of stored elements
        ("array", POINTER(c_void_p))  # ptr array
    ]


LPL_Ptra = POINTER(L_Ptra)
LPLPL_Ptra = POINTER(LPL_Ptra)


class L_Ptraa(Structure):
    '''Array of generic pointer arrays'''
    _fields_ = [
        ("nalloc", c_int),   # size of allocated ptr array
        ("ptra", LPLPL_Ptra)  # array of ptra
    ]


LPL_Ptraa = POINTER(L_Ptraa)
LPLPL_Ptraa = POINTER(LPL_Ptraa)
