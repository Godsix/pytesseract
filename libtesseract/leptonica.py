# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:22:18 2021

@author: 皓
"""
from .datatype import CommonAPI
from .leptonica_capi import LEPTONICA_API


class Leptonica(CommonAPI):

    @classmethod
    def get_version(self) -> str:
        return self.decode(LEPTONICA_API.capi_get_leptonica_version())

    @classmethod
    def pix_read(self, path):
        return LEPTONICA_API.capi_pix_read(self.encode(path))
