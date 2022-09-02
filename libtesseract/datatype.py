# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:26:57 2022

@author: 皓
"""
import os.path as osp
import locale
import logging
from ctypes import (CDLL, POINTER, c_int, c_bool, c_ubyte, c_float, c_double,
                    c_uint)

from .utils import arch_hex_bit

c_int_p = POINTER(c_int)
c_bool_p = POINTER(c_bool)
c_ubyte_p = POINTER(c_ubyte)
c_uint_p = POINTER(c_uint)
c_float_p = POINTER(c_float)
c_double_p = POINTER(c_double)


class CAPI:
    NAME = ''
    API = {}

    def __init__(self, path):
        self.logger = logging.getLogger()
        self.path = path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = osp.realpath(value)
        # import API dll
        try:
            self.dll = CDLL(self._path)
            self.init_dll()
        except Exception:
            self.dll = None

    def init_dll(self):
        for name, types in self.API.items():
            self.init_func_ptr(name, *types)

    def init_func_ptr(self, name, restype, *argtypes):
        if not hasattr(self.dll, name):
            self.logger.error('The %s capi do not contain %s',
                              self.NAME,
                              name)
            return
        func = getattr(self.dll, name)
        func.restype = restype
        func.argtypes = argtypes

    def is_available(self):
        return self.dll is not None

    def __getattr__(self, attr):
        if hasattr(self.dll, attr):
            return getattr(self.dll, attr)
        raise AttributeError(
            "'{}' object has no attribute '{}'".format(self.__class__.__name__,
                                                       attr))


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

    @property
    def arch_id(self):
        address = id(self)
        bit = arch_hex_bit()
        return f'0x{address:0{bit}X}'

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'<{class_name} object at {self.arch_id}>'
