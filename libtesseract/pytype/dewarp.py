# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:05 2022

@author: 皓
"""
from ctypes import Structure, POINTER, c_int
from .pix import LPPix, LPFPix
from .array_h import LPNuma


class L_Dewarp(Structure):
    '''Data structure for a single dewarp'''
    pass


LPL_Dewarp = POINTER(L_Dewarp)
LPLPL_Dewarp = POINTER(LPL_Dewarp)


class L_Dewarpa(Structure):
    '''Data structure to hold a number of Dewarp'''
    _fields_ = [
        ("nalloc", c_int),   # size of dewarp ptr array
        ("maxpage", c_int),   # maximum page number in array
        ("dewarp", LPLPL_Dewarp),   # array of ptrs to page dewarp
        # array of ptrs to cached dewarps
        ("dewarpcache", LPLPL_Dewarp),
        ("namodels", LPNuma),   # list of page numbers for pages
        ("napages", LPNuma),   # list of page numbers with either
        ("redfactor", c_int),   # reduction factor of input: 1 or 2
        ("sampling", c_int),   # disparity arrays sampling factor
        ("minlines", c_int),   # min number of long lines required
        ("maxdist", c_int),   # max distance for getting ref page
        ("max_linecurv", c_int),   # maximum abs line curvature,
        ("min_diff_linecurv", c_int),   # minimum abs diff line
        ("max_diff_linecurv", c_int),   # maximum abs diff line
        ("max_edgeslope", c_int),   # maximum abs left or right edge
        ("max_edgecurv", c_int),   # maximum abs left or right edge
        ("max_diff_edgecurv", c_int),   # maximum abs diff left-right
        ("useboth", c_int),   # use both disparity arrays if
        ("check_columns", c_int),   # if there are multiple columns,
        ("modelsready", c_int)  # invalid models have been removed
    ]


LPL_Dewarpa = POINTER(L_Dewarpa)
LPLPL_Dewarpa = POINTER(LPL_Dewarpa)

L_Dewarp._fields_ = [
    ("dewa", LPL_Dewarpa),   # ptr to parent (not owned)
    ("pixs", LPPix),   # source pix, 1 bpp
    ("sampvdispar", LPFPix),   # sampled vert disparity array
    ("samphdispar", LPFPix),   # sampled horiz disparity array
    ("sampydispar", LPFPix),   # sampled slope h-disparity array
    ("fullvdispar", LPFPix),   # full vert disparity array
    ("fullhdispar", LPFPix),   # full horiz disparity array
    ("fullydispar", LPFPix),   # full slope h-disparity array
    ("namidys", LPNuma),   # sorted y val of midpoint each line
    ("nacurves", LPNuma),   # sorted curvature of each line
    ("w", c_int),   # width of source image
    ("h", c_int),   # height of source image
    ("pageno", c_int),   # page number; important for reuse
    ("sampling", c_int),   # sampling factor of disparity arrays
    ("redfactor", c_int),   # reduction factor of pixs: 1 or 2
    ("minlines", c_int),   # min number of long lines required
    ("nlines", c_int),   # number of long lines found
    ("mincurv", c_int),   # min line curvature in micro-units
    ("maxcurv", c_int),   # max line curvature in micro-units
    ("leftslope", c_int),   # left edge slope in milli-units
    ("rightslope", c_int),   # right edge slope in milli-units
    ("leftcurv", c_int),   # left edge curvature in micro-units
    ("rightcurv", c_int),   # right edge curvature in micro-units
    ("nx", c_int),   # number of sampling pts in x-dir
    ("ny", c_int),   # number of sampling pts in y-dir
    ("hasref", c_int),   # 0 if normal; 1 if has a refpage
    ("refpage", c_int),   # page with disparity model to use
    ("vsuccess", c_int),   # sets to 1 if vert disparity builds
    ("hsuccess", c_int),   # sets to 1 if horiz disparity builds
    ("ysuccess", c_int),   # sets to 1 if slope disparity builds
    ("vvalid", c_int),   # sets to 1 if valid vert disparity
    ("hvalid", c_int),   # sets to 1 if valid horiz disparity
    ("skip_horiz", c_int),   # if 1, skip horiz disparity
    ("debug", c_int)  # set to 1 if debug output requested
]
