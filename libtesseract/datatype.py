# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:26:57 2022

@author: 皓
"""
import locale
from ctypes import POINTER, c_int, c_bool
from .utils import arch_hex_bit

c_int_p = POINTER(c_int)
c_bool_p = POINTER(c_bool)


class CommonAPI:
    ENCODING = 'ascii'
    API = None

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
        if self.API and hasattr(self.API, attr):
            return getattr(self.API, attr)
        raise AttributeError(
            "'{}' object has no attribute '{}'".format(self.__class__.__name__,
                                                       attr))


CommonAPI.setlocale()


class BaseObject:
    API = None

    def __init__(self, handle):
        self.handle = handle

    def delete(self, handle):
        self.API.delete(handle)

    def __del__(self):
        if hasattr(self, 'handle') and self.handle:
            handle = self.handle
            self.handle = None
            self.delete(handle)

    def __repr__(self):
        address = id(self)
        class_name = self.__class__.__name__
        bit = arch_hex_bit()
        return f'<{class_name} object at 0x{address:0{bit}X}>'
