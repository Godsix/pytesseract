# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:19:06 2022

@author: 皓
"""
from enum import IntEnum
from ctypes import Structure, POINTER, c_int, c_size_t, c_char_p
from ..datatype import c_ubyte_p, LP_c_char
from .pix import LPBox, LPPta
from .array_h import LPSarray, LPL_Dna
from .ptra import LPL_Ptra


class ImageFormats(IntEnum):
    '''Image Formats'''
    IFF_UNKNOWN = 0
    IFF_BMP = 1
    IFF_JFIF_JPEG = 2
    IFF_PNG = 3
    IFF_TIFF = 4
    IFF_TIFF_PACKBITS = 5
    IFF_TIFF_RLE = 6
    IFF_TIFF_G3 = 7
    IFF_TIFF_G4 = 8
    IFF_TIFF_LZW = 9
    IFF_TIFF_ZIP = 10
    IFF_PNM = 11
    IFF_PS = 12
    IFF_GIF = 13
    IFF_JP2 = 14
    IFF_WEBP = 15
    IFF_LPDF = 16
    IFF_TIFF_JPEG = 17
    IFF_DEFAULT = 18
    IFF_SPIX = 19


class HeaderIds(IntEnum):
    '''Header Ids'''
    BMP_ID = 19778  # BM - for bitmaps
    TIFF_BIGEND_ID = 19789  # MM - for 'motorola'
    TIFF_LITTLEEND_ID = 18761  # II - for 'intel'


class JpegHints(IntEnum):
    '''Jpeg Hints'''
    L_JPEG_READ_LUMINANCE = 1  # only want luminance data; no chroma
    L_JPEG_CONTINUE_WITH_BAD_DATA = 2  # return possibly damaged pix


class Jp2kCodecs(IntEnum):
    '''Jp2k Codecs'''
    L_J2K_CODEC = 1  # codestream
    L_JP2_CODEC = 2  # file format with 'ihdr'


class PdfEncoding(IntEnum):
    '''Pdf Encoding'''
    L_DEFAULT_ENCODE = 0  # use default encoding based on image
    L_JPEG_ENCODE = 1  # use dct encoding: 8 and 32 bpp, no cmap
    L_G4_ENCODE = 2  # use ccitt g4 fax encoding: 1 bpp
    L_FLATE_ENCODE = 3  # use flate encoding: any depth, cmap ok
    L_JP2K_ENCODE = 4  # use jp2k encoding: 8 and 32 bpp, no cmap


class PdfMultiImage(IntEnum):
    '''Pdf MultiImage'''
    L_FIRST_IMAGE = 1  # first image to be used
    L_NEXT_IMAGE = 2  # intermediate image; not first or last
    L_LAST_IMAGE = 3  # last image to be used


class L_Compressed_Data(Structure):
    '''Compressed image data'''
    _fields_ = [
        ("type", c_int),   # encoding type: L_JPEG_ENCODE, etc
        ("datacomp", c_ubyte_p),   # gzipped raster data
        ("nbytescomp", c_size_t),   # number of compressed bytes
        ("data85", LP_c_char),   # ascii85-encoded gzipped raster data
        ("nbytes85", c_size_t),   # number of ascii85 encoded bytes
        ("cmapdata85", c_char_p),   # ascii85-encoded uncompressed cmap
        ("cmapdatahex", c_char_p),   # hex pdf array for the cmap
        ("ncolors", c_int),   # number of colors in cmap
        ("w", c_int),   # image width
        ("h", c_int),   # image height
        ("bps", c_int),   # bits/sample; typ. 1, 2, 4 or 8
        ("spp", c_int),   # samples/pixel; typ. 1 or 3
        ("minisblack", c_int),   # tiff g4 photometry
        ("predictor", c_int),   # flate data has PNG predictors
        ("nbytes", c_size_t),   # number of uncompressed raster bytes
        ("res", c_int)  # resolution (ppi)
    ]


LPL_Compressed_Data = POINTER(L_Compressed_Data)
LPLPL_Compressed_Data = POINTER(LPL_Compressed_Data)


class L_Pdf_Data(Structure):
    '''Intermediate pdf generation data'''
    _fields_ = [
        ("title", c_char_p),   # optional title for pdf
        ("n", c_int),   # number of images
        ("ncmap", c_int),   # number of colormaps
        ("cida", LPL_Ptra),   # array of compressed image data
        ("id", c_char_p),   # %PDF-1.2 id string
        ("obj1", c_char_p),   # catalog string
        ("obj2", c_char_p),   # metadata string
        ("obj3", c_char_p),   # pages string
        ("obj4", c_char_p),   # page string (variable data)
        ("obj5", c_char_p),   # content string (variable data)
        ("poststream", c_char_p),   # post-binary-stream string
        ("trailer", c_char_p),   # trailer string (variable data)
        ("xy", LPPta),   # store (xpt, ypt) array
        ("wh", LPPta),   # store (wpt, hpt) array
        ("mediabox", LPBox),   # bounding region for all images
        ("saprex", LPSarray),   # pre-binary-stream xobject strings
        ("sacmap", LPSarray),   # colormap pdf object strings
        ("objsize", LPL_Dna),   # sizes of each pdf string object
        ("objloc", LPL_Dna),   # location of each pdf string object
        ("xrefloc", c_int)  # location of xref
    ]


LPL_Pdf_Data = POINTER(L_Pdf_Data)
LPLPL_Pdf_Data = POINTER(LPL_Pdf_Data)
