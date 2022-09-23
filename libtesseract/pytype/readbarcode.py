# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:07 2022

@author: 皓
"""
from enum import IntEnum


class BarcodeMethod(IntEnum):
    '''Barcode Method'''
    L_USE_WIDTHS = 1  # use histogram of barcode widths
    L_USE_WINDOWS = 2  # find best window for decoding transitions


class BarcodeFormat(IntEnum):
    '''Barcode Format'''
    L_BF_UNKNOWN = 0  # unknown format
    L_BF_ANY = 1  # try decoding with all known formats
    L_BF_CODE128 = 2  # decode with Code128 format
    L_BF_EAN8 = 3  # decode with EAN8 format
    L_BF_EAN13 = 4  # decode with EAN13 format
    L_BF_CODE2OF5 = 5  # decode with Code 2 of 5 format
    L_BF_CODEI2OF5 = 6  # decode with Interleaved 2 of 5 format
    L_BF_CODE39 = 7  # decode with Code39 format
    L_BF_CODE93 = 8  # decode with Code93 format
    L_BF_CODABAR = 9  # decode with Code93 format
    L_BF_UPCA = 10  # decode with UPC A format
