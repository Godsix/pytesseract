# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:07 2022

@author: 皓
"""
from enum import IntEnum
from ctypes import Structure, POINTER, c_int
from ..datatype import c_int_p


class SudokuOutput(IntEnum):
    '''Sudoku Output'''
    L_SUDOKU_INIT = 0
    L_SUDOKU_STATE = 1


class L_Sudoku(Structure):
    _fields_ = [
        ("num", c_int),   # number of unknowns
        ("locs", c_int_p),   # location of unknowns
        ("current", c_int),   # index into %locs of current location
        ("init", c_int_p),   # initial state, with 0 representing
        ("state", c_int_p),   # present state, including inits and
        ("nguess", c_int),   # shows current number of guesses
        ("finished", c_int),   # set to 1 when solved
        ("failure", c_int)  # set to 1 if no solution is possible
    ]


LPL_Sudoku = POINTER(L_Sudoku)
LPLPL_Sudoku = POINTER(LPL_Sudoku)
