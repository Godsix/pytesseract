# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:05 2022

@author: 皓
"""
from enum import IntEnum
from ctypes import Structure, POINTER, c_int, c_float, c_double, c_size_t
from ..datatype import c_float_p, c_double_p, c_char_p_p, c_ubyte_p


class NumaInterpolation(IntEnum):
    '''Numa Interpolation'''
    L_LINEAR_INTERP = 1  # linear
    L_QUADRATIC_INTERP = 2  # quadratic


class NumaBorderAdding(IntEnum):
    '''Numa Border Adding'''
    L_CONTINUED_BORDER = 1  # extended with same value
    L_SLOPE_BORDER = 2  # extended with constant normal derivative
    L_MIRRORED_BORDER = 3  # mirrored


class NumaDataConversion(IntEnum):
    '''Numa Data Conversion'''
    L_INTEGER_VALUE = 1  # convert to integer
    L_FLOAT_VALUE = 2  # convert to float


class Numa(Structure):
    '''Number array: an array of floats'''
    _fields_ = [("nalloc", c_int),  # size of allocated number array
                ("n", c_int),  # number of numbers saved
                ("refcount", c_int),  # reference count (1 if no clones)
                ("startx", c_float),  # x value assigned to array[0]
                ("delx", c_float),  # change in x value as i --> i + 1
                ("array", c_float_p)]  # number array


LPNuma = POINTER(Numa)
LPLPNuma = POINTER(LPNuma)


class Numaa(Structure):
    '''Array of number arrays'''
    _fields_ = [("nalloc", c_int),  # size of allocated ptr array
                ("n", c_int),  # number of Numa saved
                ("numa", LPLPNuma)]  # array of Numa


LPNumaa = POINTER(Numaa)
LPLPNumaa = POINTER(LPNumaa)


class L_Dna(Structure):
    '''Double number array: an array of doubles'''
    _fields_ = [("nalloc", c_int),  # size of allocated number array
                ("n", c_int),  # number of numbers saved
                ("refcount", c_int),  # reference count (1 if no clones)
                ("startx", c_double),  # x value assigned to array[0]
                ("delx", c_double),  # change in x value as i --> i + 1
                ("array", c_double_p)]  # number array


LPL_Dna = POINTER(L_Dna)
LPLPL_Dna = POINTER(LPL_Dna)


class L_Dnaa(Structure):
    '''Array of double number arrays'''
    _fields_ = [("nalloc", c_int),  # size of allocated ptr array
                ("n", c_int),  # number of L_Dna saved
                ("dna", LPLPL_Dna)]  # array of L_Dna


LPL_Dnaa = POINTER(L_Dnaa)
LPLPL_Dnaa = POINTER(LPL_Dnaa)


class L_DnaHash(Structure):
    _fields_ = [("nbuckets", c_int),
                ("initsize", c_int),  # initial size of each dna that is made
                ("dna", LPLPL_Dna)]  # array of L_Dna


LPL_DnaHash = POINTER(L_DnaHash)
LPLPL_DnaHash = POINTER(LPL_DnaHash)


class Sarray(Structure):
    '''String array: an array of C strings'''
    _fields_ = [("nalloc", c_int),  # size of allocated ptr array
                ("n", c_int),  # number of strings allocated
                ("refcount", c_int),  # reference count (1 if no clones)
                ("array", c_char_p_p)]  # string array


LPSarray = POINTER(Sarray)
LPLPSarray = POINTER(LPSarray)


class L_Bytea(Structure):
    '''Byte array (analogous to C++ "string")'''
    _fields_ = [
        ("nalloc", c_size_t),  # number of bytes allocated in data array
        ("size", c_size_t),  # number of bytes presently used
        ("refcount", c_int),  # reference count (1 if no clones)
        ("data", c_ubyte_p)]  # data array


LPL_Bytea = POINTER(L_Bytea)
LPLPL_Bytea = POINTER(LPL_Bytea)
