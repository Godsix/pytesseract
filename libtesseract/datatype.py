# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:26:57 2022

@author: 皓
"""
import os.path as osp
import locale
import logging
from ctypes import (CDLL, POINTER, c_int, c_bool, c_ubyte, c_float, c_double,
                    c_char, c_uint, c_size_t, c_ulonglong, c_void_p,
                    c_char_p, Array, cast)
from .utils import arch_hex_bit, load_data_from_xml

c_int_p = POINTER(c_int)
c_bool_p = POINTER(c_bool)
c_ubyte_p = POINTER(c_ubyte)
c_uint_p = POINTER(c_uint)
c_float_p = POINTER(c_float)
c_double_p = POINTER(c_double)
c_size_t_p = POINTER(c_size_t)
c_ulonglong_p = POINTER(c_ulonglong)
LP_c_char = POINTER(c_char)
c_char_p_p = POINTER(c_char_p)
LPFile = c_void_p


class CAPI:
    NAME = ''
    API = {}
    GLOBALS = None

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
        self.dll = CDLL(self._path)
        self.init_dll()

    def init_dll(self):
        if self.init_dll_from_dict():
            self.logger.info('%s init capi with API dict.',
                             self.__class__.__name__)
            return
        if self.init_dll_from_xml():
            self.logger.info('%s init capi with XML file.',
                             self.__class__.__name__)
            return
        self.logger.exception('%s init fail.', self.__class__.__name__)

    def get_xml_info(self):
        current_dir = osp.dirname(__file__)
        dirname, basename = osp.split(self._path)
        name = osp.splitext(basename)[0]
        find_paths = (current_dir, dirname)
        return load_data_from_xml(name, *find_paths, variables=self.GLOBALS)

    def init_dll_from_xml(self):
        result = self.get_xml_info()
        if result is None:
            return False
        for name, types in result.items():
            self.init_func_ptr(name, *types)
        return True

    def init_dll_from_dict(self):
        if not self.API:
            return False
        for name, types in self.API.items():
            self.init_func_ptr(name, *types)
        return True

    def init_func_ptr(self, name, restype, *argtypes):
        if not hasattr(self.dll, name):
            self.logger.error('The %s capi do not contain %s', self.NAME, name)
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

    @property
    def arch_id(self):
        address = id(self)
        bit = arch_hex_bit()
        return f'0x{address:0{bit}X}'

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'<{class_name} object at {self.arch_id}>'


def get_point(value):
    if not value:
        return None
    if isinstance(value, BaseObject):
        return value.handle
    return value


def get_point_value(var, quote: int = 1):
    v = var
    for i in range(quote):
        v = v.contents
        if bool(v) is False:
            return None
    else:
        if isinstance(v, c_void_p):
            return v
        if not hasattr(v, 'value'):
            return v
        return v.value


def list_to_array(obj: list[str]) -> tuple[Array, int]:
    encode_obj = [CommonAPI.encode(x) for x in obj]
    size = len(encode_obj)
    array = c_char_p * size
    c_object = array(*encode_obj)
    return c_object, size


def list_to_points(obj: list[str]) -> tuple[c_char_p_p, int]:
    c_object, size = list_to_array(obj)
    p_object = cast(c_object, c_char_p_p)
    return p_object, size


def dict_to_array(obj: dict[str, str]) -> tuple[Array, Array, int]:
    names, values = tuple(zip(*obj.items()))
    ppnames, names_size = list_to_array(names)
    ppvalues, values_size = list_to_array(values)
    return ppnames, ppvalues, names_size


def dict_to_points(obj: list[str]) -> tuple[c_char_p_p, int]:
    names, values = tuple(zip(*obj.items()))
    array_names, names_size = list_to_array(names)
    array_values, _ = list_to_array(values)
    ppnames = cast(array_names, c_char_p_p)
    ppvalues = cast(array_values, c_char_p_p)
    return ppnames, ppvalues, names_size
