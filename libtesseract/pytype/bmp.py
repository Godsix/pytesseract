# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:05 2022

@author: 皓
"""
from ctypes import Structure, POINTER, c_ubyte, c_int, c_short


class BMP_FileHeader(Structure):
    '''BMP file header

     Notes:
      (1) The bfSize field is stored as a 32 bit integer and includes
          the size of the BMP_FileHeader, BMP_InfoHeader, the color
          table (if any), and the size of the DIB bits.
      (2) The bfOffBits field is also stored as a 32 bit integer and
          contains the absolute offset in bytes of the image data
          in this file. Some bmp files have additional data after the
          BMP_InfoHeader and before the color table (if it exists).
          However, enabling reading of these files makes the reader
          vulnerable to various malware attacks.  Therefore we do not
          read bmp files with extra data, and require that the size
          of the color table in bytes is
             offset - sizeof(BMP_FileHeader) - sizeof(BMP_InfoHeader)
      (3) Use arrays of l_uint8[] to make an endianness agnostic
          access to the BMP_FileHeader easier.
    '''
    _fields_ = [
        ("bfType", c_ubyte * 2),   # file type; must be "BM"
        # length of the file; sizeof(BMP_FileHeader) + sizeof(BMP_InfoHeader)+
        # size of optional extra data + size of color table + size of DIB bits
        ("bfSize", c_ubyte * 4),
        ("bfReserved1", c_ubyte * 2),   # don't care (set to 0)
        ("bfReserved2", c_ubyte * 2),   # don't care (set to 0)
        ("bfOffBits", c_ubyte * 4)  # offset from beginning of file
    ]


LPBMP_FileHeader = POINTER(BMP_FileHeader)
LPLPBMP_FileHeader = POINTER(LPBMP_FileHeader)


class BMP_InfoHeader(Structure):
    '''BMP info header'''
    _fields_ = [
        ("biSize", c_int),   # size of the BMP_InfoHeader struct
        ("biWidth", c_int),   # bitmap width in pixels
        ("biHeight", c_int),   # bitmap height in pixels
        ("biPlanes", c_short),   # number of bitmap planes
        ("biBitCount", c_short),   # number of bits per pixel
        ("biCompression", c_int),   # compress format (0 == uncompressed)
        ("biSizeImage", c_int),   # size of image in bytes
        ("biXPelsPerMeter", c_int),   # pixels per meter in x direction
        ("biYPelsPerMeter", c_int),   # pixels per meter in y direction
        ("biClrUsed", c_int),   # number of colors used
        ("biClrImportant", c_int)  # number of important colors used
    ]


LPBMP_InfoHeader = POINTER(BMP_InfoHeader)
LPLPBMP_InfoHeader = POINTER(LPBMP_InfoHeader)
