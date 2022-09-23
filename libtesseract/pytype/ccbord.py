# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:05 2022

@author: 皓
"""
from enum import IntEnum
from ctypes import Structure, POINTER, c_int
from .pix import LPPix, LPBoxa, LPPta, LPPtaa
from .array_h import LPNumaa


class CCBCoords(IntEnum):
    '''CCB Coords'''
    CCB_LOCAL_COORDS = 1
    CCB_GLOBAL_COORDS = 2


class CCBPoints(IntEnum):
    '''CCB Points'''
    CCB_SAVE_ALL_PTS = 1
    CCB_SAVE_TURNING_PTS = 2


class CCBord(Structure):
    '''
     CCBord contains:

        (1) a minimally-clipped bitmap of the component (pix),
        (2) a boxa consisting of:
              for the primary component:
                    (xul, yul) pixel location in global coords
                    (w, h) of the bitmap
              for the hole components:
                    (x, y) in relative coordinates in primary component
                    (w, h) of the hole border (which is 2 pixels
                           larger in each direction than the hole itself)
        (3) a pta ('start') of the initial border pixel location for each
            closed curve, all in relative coordinates of the primary
            component.  This is given for the primary component,
            followed by the hole components, if any.
        (4) a refcount of the ccbord; used internally when a ccbord
            is accessed from a ccborda (array of ccbord)
        (5) a ptaa for the chain code for the border in relative
            coordinates, where the first pta is the exterior border
            and all other pta are for interior borders (holes)
        (6) a ptaa for the global pixel loc rendition of the border,
            where the first pta is the exterior border and all other
            pta are for interior borders (holes).
            This is derived from the local or step chain code.
        (7) a numaa for the chain code for the border as orientation
            directions between successive border pixels, where
            the first numa is the exterior border and all other
            numa are for interior borders (holes).  This is derived
            from the local chain code.  The 8 directions are 0 - 7.
        (8) a pta for a single chain for each c.c., comprised of outer
            and hole borders, plus cut paths between them, all in
            local coords.
        (9) a pta for a single chain for each c.c., comprised of outer
            and hole borders, plus cut paths between them, all in
            global coords.
    '''
    _fields_ = [
        ("pix", LPPix),   # component bitmap (min size)
        ("boxa", LPBoxa),   # regions of each closed curve
        ("start", LPPta),   # initial border pixel locations
        ("refcount", c_int),   # number of handles; start at 1
        ("local", LPPtaa),   # ptaa of chain pixels (local)
        ("global", LPPtaa),   # ptaa of chain pixels (global)
        ("step", LPNumaa),   # numaa of chain code (step dir)
        ("splocal", LPPta),   # pta of single chain (local)
        ("spglobal", LPPta)  # pta of single chain (global)
    ]


LPCCBord = POINTER(CCBord)
LPLPCCBord = POINTER(LPCCBord)


class CCBorda(Structure):
    '''Array of CCBord'''
    _fields_ = [
        ("pix", LPPix),   # input pix (may be null)
        ("w", c_int),   # width of pix
        ("h", c_int),   # height of pix
        ("n", c_int),   # number of ccbord in ptr array
        ("nalloc", c_int),   # number of ccbord ptrs allocated
        ("ccb", LPLPCCBord)  # ccb ptr array
    ]


LPCCBorda = POINTER(CCBorda)
LPLPCCBorda = POINTER(LPCCBorda)
