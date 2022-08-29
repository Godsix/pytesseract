# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:14:11 2021

@author: 皓
"""
import sys
from ctypes import cdll, CDLL, c_void_p, POINTER, c_int, c_char


def func_ptr_init(func, restype, *argtypes):
    func.restype = restype
    func.argtypes = argtypes
    return func


if sys.platform[:3] == "win":  # pragma: no cover
    libc = cdll.msvcrt
    libc_fdopen = libc._fdopen
else:
    libc = CDLL("libc.so.6")
    libc_fdopen = libc.fdopen

func_ptr_init(libc_fdopen, c_void_p, c_int, POINTER(c_char))
# fopen = libc.fopen
# fwrite = libc.fwrite
# fclose = libc.fclose
# fseek = libc.fseek
# fread = libc.fread
# ftell = libc.ftell
# memset = libc.memset
# memcpy = libc.memcpy


def fdopen(fd: int, mode: str):
    return libc_fdopen(fd, mode.encode())
