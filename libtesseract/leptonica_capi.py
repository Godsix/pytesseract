# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:43:58 2021

@author: 皓
"""
import os.path as osp
import logging
from ctypes import (POINTER, CDLL, Structure, c_void_p, c_int32, c_uint32,
                    c_char_p, c_char)
from .common import LEPT_DLL


class PixColormap(Structure):
    _fields_ = [("array", c_void_p),  # colormap table (array of RGBA_QUAD)
                ("depth", c_int32),  # of pix (1, 2, 4 or 8 bpp)
                ("nalloc", c_int32),  # number of color entries allocated
                ("n", c_int32)]  # number of color entries used


class Pix(Structure):
    _fields_ = [("w", c_uint32),  # width in pixels
                ("h", c_uint32),  # height in pixels
                ("d", c_uint32),  # depth in bits (bpp)
                ("spp", c_uint32),  # number of samples per pixel
                ("wpl", c_uint32),  # 32-bit words/line
                ("refcount", c_uint32),  # reference count (1 if no clones)
                # image res (ppi) in x direction (use 0 if unknown)
                ("xres", c_int32),
                # image res (ppi) in y direction (use 0 if unknown)
                ("yres", c_int32),
                ("informat", c_int32),  # input file format, IFF_*
                ("special", c_int32),  # special instructions for I/O, etc
                ("text", POINTER(c_char)),  # text string associated with pix
                ("colormap", POINTER(PixColormap)),  # colormap (may be null)
                ("data", POINTER(c_uint32))]  # the image data


class Box(Structure):
    _fields_ = [("x", c_int32),
                ("y", c_int32),
                ("w", c_int32),
                ("h", c_int32),
                ("refcount", c_uint32)]  # reference count (1 if no clones)


class Boxa(Structure):
    _fields_ = [("n", c_int32),  # number of box in ptr array
                ("nalloc", c_int32),  # number of box ptrs allocated
                ("refcount", c_uint32),  # reference count (1 if no clones)
                ("box", POINTER(POINTER(Box)))]  # box ptr array


class Pixa(Structure):
    _fields_ = [("n", c_int32),  # number of Pix in ptr array
                ("nalloc", c_int32),  # number of Pix ptrs allocated
                ("refcount", c_uint32),  # reference count (1 if no clones)
                ("pix", POINTER(POINTER(Pix))),  # the array of ptrs to pix
                ("boxa", POINTER(Boxa))]  # array of boxes


LPPix = POINTER(Pix)
LPBoxa = POINTER(Boxa)
LPPixa = POINTER(Pixa)
LPLPPixa = POINTER(LPPixa)


class LeptonicaAPI:

    API = {
        # General free functions
        'getLeptonicaVersion': (c_char_p, ),
        'pixRead':  (POINTER(Pix), c_char_p),
    }

    def __init__(self, path):
        self.path = path
        self.logger = logging.getLogger()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = osp.realpath(value)
        # import API dll
        self.dll = CDLL(self._path)
        self.dll_init()

    def dll_init(self):
        for name, types in self.API.items():
            self.func_ptr_init(name, *types)

    def func_ptr_init(self, name, restype, *argtypes):
        if not hasattr(self.dll, name):
            return
        func = getattr(self.dll, name)
        func.restype = restype
        func.argtypes = argtypes

    def __getattr__(self, attr):
        if hasattr(self.dll, attr):
            return getattr(self.dll, attr)
        raise AttributeError(
            "'{}' object has no attribute '{}'".format(self.__class__.__name__,
                                                       attr))

    def capi_get_leptonica_version(self) -> str:
        return self.getLeptonicaVersion()

    def capi_pix_read(self, path: bytes) -> POINTER(Pix):
        return self.pixRead(path)


LEPTONICA_API = LeptonicaAPI(LEPT_DLL)


def test():
    ret = LEPTONICA_API
    print(ret.getLeptonicaVersion())


if __name__ == '__main__':
    test()
