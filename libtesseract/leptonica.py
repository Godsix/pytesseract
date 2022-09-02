# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:22:18 2021

@author: 皓
"""
from .datatype import CommonAPI
from .leptonica_capi import LEPTONICA_API, LPPix, LPLPPix


class Leptonica(CommonAPI):

    @classmethod
    def get_version(self) -> str:
        return self.decode(LEPTONICA_API.capi_get_leptonica_version())

    @classmethod
    def pix_read(self, path: str):
        return LEPTONICA_API.capi_pix_read(self.encode(path))

    @classmethod
    def pix_clone(cls, pixs: LPPix) -> LPPix:
        return LEPTONICA_API.capi_pix_clone(pixs)

    @classmethod
    def pix_destroy(cls, ppix: LPLPPix):
        LEPTONICA_API.capi_pix_destroy(ppix)

    @classmethod
    def pix_copy(cls, pixd: LPPix, pixs: LPPix) -> LPPix:
        return LEPTONICA_API.capi_pix_copy(pixd, pixs)
