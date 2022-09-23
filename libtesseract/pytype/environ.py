# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:05 2022

@author: 皓
"""
from enum import IntEnum
from ctypes import Structure, POINTER, c_int


class SearchState(IntEnum):
    '''Search State'''
    L_NOT_FOUND = 0
    L_FOUND = 1


class PathSeparators(IntEnum):
    '''Path Separators'''
    UNIX_PATH_SEPCHAR = 0
    WIN_PATH_SEPCHAR = 1


class MessageControl(IntEnum):
    '''Message Control'''
    L_SEVERITY_EXTERNAL = 0
    L_SEVERITY_ALL = 1
    L_SEVERITY_DEBUG = 2
    L_SEVERITY_INFO = 3
    L_SEVERITY_WARNING = 4
    L_SEVERITY_ERROR = 5
    L_SEVERITY_NONE = 6


class L_WallTimer(Structure):
    '''Timing struct'''
    _fields_ = [("start_sec", c_int),
                ("start_usec", c_int),
                ("stop_sec", c_int),
                ("stop_usec", c_int)]


LPL_WallTimer = POINTER(L_WallTimer)
LPLPL_WallTimer = POINTER(LPL_WallTimer)
