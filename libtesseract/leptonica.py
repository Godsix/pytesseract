# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:22:18 2021

@author: 皓
"""
import locale
from .leptonica_capi import LEPTONICA_API


class CommonAPI:
    ENCODING = 'ascii'

    @classmethod
    def setlocale(cls, encoding=None):
        try:
            'encoding'.encode(encoding).decode(encoding)
        except Exception:
            encoding = locale.getdefaultlocale()[1]
        cls.ENCODING = encoding
        return

    @classmethod
    def decode(cls, value):
        if isinstance(value, bytes):
            return value.decode(cls.ENCODING)
        return value

    @classmethod
    def encode(cls, value):
        if isinstance(value, str):
            return value.encode(cls.ENCODING)
        return value

    @classmethod
    def decode_utf8(cls, value):
        if isinstance(value, bytes):
            return value.decode('utf-8')
        return value

    @classmethod
    def encode_utf8(cls, value):
        if isinstance(value, str):
            return value.encode('utf-8')
        return value

    def __getattr__(self, attr):
        if hasattr(LEPTONICA_API, attr):
            return getattr(LEPTONICA_API, attr)
        raise AttributeError(
            "'{}' object has no attribute '{}'".format(self.__class__.__name__,
                                                       attr))


CommonAPI.setlocale()


class Leptonica(CommonAPI):

    @classmethod
    def get_version(self) -> str:
        return self.decode(LEPTONICA_API.capi_get_leptonica_version())

    @classmethod
    def pix_read(self, path):
        return LEPTONICA_API.capi_pix_read(self.encode(path))
