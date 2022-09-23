# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:06 2022

@author: 皓
"""
from ctypes import c_void_p
from .pytype.pix import LPPix

LPHBITMAP = c_void_p


class TessCAPI:

    def capi_pix_get_windows_hbitmap(self, pixs: LPPix) -> LPHBITMAP:
        return self.pixGetWindowsHBITMAP(pixs)
