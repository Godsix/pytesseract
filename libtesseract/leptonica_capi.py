# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:43:58 2021

@author: 皓
"""
from ctypes import (POINTER, Structure, c_void_p, c_float, c_int, c_uint,
                    c_ubyte, c_size_t, c_char_p, c_double, c_ulonglong, c_char,
                    c_ushort)
from .datatype import (c_ubyte_p, c_float_p, c_double_p, c_uint_p, c_int_p,
                       c_size_t_p, c_ulonglong_p, LP_c_char)
from .common import LEPT_DLL
from .datatype import CAPI


LPFile = c_void_p


# pix.h
class PixColormap(Structure):
    '''Colormap of a Pix'''
    _fields_ = [("array", c_void_p),  # colormap table (array of RGBA_QUAD)
                ("depth", c_int),  # of pix (1, 2, 4 or 8 bpp)
                ("nalloc", c_int),  # number of color entries allocated
                ("n", c_int)]  # number of color entries used


LPPixColormap = POINTER(PixColormap)
LPLPPixColormap = POINTER(LPPixColormap)


class Pix(Structure):
    '''Basic Pix'''
    _fields_ = [("w", c_uint),  # width in pixels
                ("h", c_uint),  # height in pixels
                ("d", c_uint),  # depth in bits (bpp)
                ("spp", c_uint),  # number of samples per pixel
                ("wpl", c_uint),  # 32-bit words/line
                ("refcount", c_uint),  # reference count (1 if no clones)
                # image res (ppi) in x direction (use 0 if unknown)
                ("xres", c_uint),
                # image res (ppi) in y direction (use 0 if unknown)
                ("yres", c_uint),
                ("informat", c_uint),  # input file format, IFF_*
                ("special", c_uint),  # special instructions for I/O, etc
                ("text", c_char_p),  # text string associated with pix
                ("colormap", LPPixColormap),  # colormap (may be null)
                ("data", c_uint_p)]  # the image data


LPPix = POINTER(Pix)
LPLPPix = POINTER(LPPix)


class RGBA_Quad(Structure):
    '''
    Colormap table entry (after the BMP version).
    Note that the BMP format stores the colormap table exactly
    as it appears here, with color samples being stored sequentially,
    in the order (b,g,r,a).
    '''
    _fields_ = [("blue", c_ubyte),  # blue value
                ("green", c_ubyte),  # green value
                ("red", c_ubyte),  # red value
                ("alpha", c_ubyte)]  # alpha value


class Box(Structure):
    '''Basic rectangle'''
    _fields_ = [("x", c_int),  # left coordinate
                ("y", c_int),  # top coordinate
                ("w", c_int),  # box width
                ("h", c_int),  # box height
                ("refcount", c_uint)]  # reference count (1 if no clones)


LPBox = POINTER(Box)
LPLPBox = POINTER(LPBox)


class Boxa(Structure):
    '''Array of Box'''
    _fields_ = [("n", c_int),  # number of box in ptr array
                ("nalloc", c_int),  # number of box ptrs allocated
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("box", LPLPBox),  # box ptr array
                ]


LPBoxa = POINTER(Boxa)

LPLPBoxa = POINTER(LPBoxa)


class Boxaa(Structure):
    '''Array of Boxa'''
    _fields_ = [("n", c_int),  # number of boxa in ptr array
                ("nalloc", c_int),  # number of boxa ptrs allocated
                ("boxa", LPLPBoxa)]  # boxa ptr array


LPBoxaa = POINTER(Boxaa)
LPLPBoxaa = POINTER(LPBoxaa)


class Pixa(Structure):
    '''Array of pix'''
    _fields_ = [("n", c_int),  # number of Pix in ptr array
                ("nalloc", c_int),  # number of Pix ptrs allocated
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("pix", LPLPPix),  # the array of ptrs to pix
                ("boxa", LPBoxa),  # array of boxes
                ]


LPPixa = POINTER(Pixa)

LPLPPixa = POINTER(LPPixa)


class Pixaa(Structure):
    '''Array of arrays of pix'''
    _fields_ = [("n", c_int),  # number of Pixa in ptr array
                ("nalloc", c_int),  # number of Pixa ptrs allocated
                ("pixa", LPLPPixa),  # array of ptrs to pixa
                ("boxa", LPBoxa),  # array of boxes
                ]


LPPixaa = POINTER(Pixaa)
LPLPPixaa = POINTER(LPPixaa)


class Pta(Structure):
    '''Array of points'''
    _fields_ = [("n", c_int),  # actual number of pts
                ("nalloc", c_int),  # size of allocated arrays
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("x", c_float_p),  # arrays of floats
                ("y", c_float_p)]  # arrays of floats


LPPta = POINTER(Pta)

LPLPPta = POINTER(LPPta)


class Ptaa(Structure):
    '''Array of Pta'''
    _fields_ = [("n", c_int),  # number of pta in ptr array
                ("nalloc", c_int),  # number of pta ptrs allocated
                ("pta", LPLPPta)]  # pta ptr array


LPPtaa = POINTER(Ptaa)
LPLPPtaa = POINTER(LPPtaa)


class Pixacc(Structure):
    '''Pix accumulator container'''
    _fields_ = [("w", c_int),  # array width
                ("h", c_int),  # array height
                ("offset", c_int),  # used to allow negative
                ("pix", LPPix)]  # the 32 bit accumulator pix


LPPixacc = POINTER(Pixacc)
LPLPPixacc = POINTER(LPPixacc)


class PixTiling(Structure):
    '''Pix tiling'''
    _fields_ = [("pix", LPPix),  # input pix (a clone)
                ("nx", c_int),  # number of tiles horizontally
                ("ny", c_int),  # number of tiles vertically
                ("w", c_int),  # tile width
                ("h", c_int),  # tile height
                ("xoverlap", c_int),  # overlap on left and right
                ("yoverlap", c_int),  # overlap on top and bottom
                ("strip", c_int)]  # strip for paint; default is TRUE


LPPixTiling = POINTER(PixTiling)
LPLPPixTiling = POINTER(LPPixTiling)


class FPix(Structure):
    '''Pix with float array'''
    _fields_ = [("w", c_int),  # width in pixels
                ("h", c_int),  # height in pixels
                ("wpl", c_int),  # 32-bit words/line
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("xres", c_int),  # image res (ppi) in x direction
                ("yres", c_int),  # image res (ppi) in y direction
                ("data", c_float_p),  # the float image data
                ]


LPFPix = POINTER(FPix)
LPLPFPix = POINTER(LPFPix)


class FPixa(Structure):
    '''Array of FPix'''
    _fields_ = [("n", c_int),  # number of fpix in ptr array
                ("nalloc", c_int),  # number of fpix ptrs allocated
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("fpix", LPLPFPix)]  # the array of ptrs to fpix


LPFPixa = POINTER(FPixa)
LPLPFPixa = POINTER(LPFPixa)


class DPix(Structure):
    '''Pix with double array'''
    _fields_ = [("w", c_int),  # width in pixels
                ("h", c_int),  # height in pixels
                ("wpl", c_int),  # 32-bit words/line
                ("refcount", c_uint),  # reference count (1 if no clones)
                ("xres", c_int),  # image res (ppi) in x direction
                ("yres", c_int),  # image res (ppi) in y direction
                ("data", c_double_p)]  # the double image data


LPDPix = POINTER(DPix)
LPLPDPix = POINTER(LPDPix)


class PixComp(Structure):
    '''Compressed Pix'''
    _fields_ = [("w", c_int),  # width in pixels
                ("h", c_int),  # height in pixels
                ("d", c_int),  # depth in bits
                ("xres", c_int),  # image res (ppi) in x direction
                ("yres", c_int),  # image res (ppi) in y direction
                ("comptype", c_int),  # compressed format (IFF_TIFF_G4,
                ("text", c_char_p),  # text string associated with pix
                ("cmapflag", c_int),  # flag (1 for cmap, 0 otherwise)
                ("data", c_ubyte_p),  # the compressed image data
                ("size", c_size_t)]  # size of the data array


LPPixComp = POINTER(PixComp)
LPLPPixComp = POINTER(LPPixComp)


class PixaComp(Structure):
    '''Array of compressed pix'''
    _fields_ = [("n", c_int),  # number of PixComp in ptr array
                ("nalloc", c_int),  # number of PixComp ptrs allocated
                ("offset", c_int),  # indexing offset into ptr array
                ("pixc", LPLPPixComp),  # the array of ptrs to PixComp
                ("boxa", LPBoxa)]  # array of boxes


LPPixaComp = POINTER(PixaComp)
LPLPPixaComp = POINTER(LPPixaComp)
# array.h


class Numa(Structure):
    '''Number array: an array of floats'''
    _fields_ = [("nalloc", c_int),  # size of allocated number array
                ("n", c_int),  # number of numbers saved
                ("refcount", c_int),  # reference count (1 if no clones)
                ("startx", c_float),  # x value assigned to array[0]
                ("delx", c_float),  # change in x value as i --> i + 1
                ("array", c_float_p)]  # number array


LPNuma = POINTER(Numa)
LPLPNuma = POINTER(LPNuma)


class Numaa(Structure):
    '''Array of number arrays'''
    _fields_ = [("nalloc", c_int),  # size of allocated ptr array
                ("n", c_int),  # number of Numa saved
                ("numa", LPLPNuma)]  # array of Numa


LPNumaa = POINTER(Numaa)
LPLPNumaa = POINTER(LPNumaa)


class L_Dna(Structure):
    '''Double number array: an array of doubles'''
    _fields_ = [("nalloc", c_int),  # size of allocated number array
                ("n", c_int),  # number of numbers saved
                ("refcount", c_int),  # reference count (1 if no clones)
                ("startx", c_double),  # x value assigned to array[0]
                ("delx", c_double),  # change in x value as i --> i + 1
                ("array", c_double_p)]  # number array


LPL_Dna = POINTER(L_Dna)
LPLPL_Dna = POINTER(LPL_Dna)


class L_Dnaa(Structure):
    '''Array of double number arrays'''
    _fields_ = [("nalloc", c_int),  # size of allocated ptr array
                ("n", c_int),  # number of L_Dna saved
                ("dna", LPLPL_Dna)]  # array of L_Dna


class L_DnaHash(Structure):
    ''''''
    _fields_ = [("nbuckets", c_int),  #
                ("initsize", c_int),  # initial size of each dna that is made
                ("dna", LPLPL_Dna)]  # array of L_Dna


class Sarray(Structure):
    '''String array: an array of C strings'''
    _fields_ = [("nalloc", c_int),  # size of allocated ptr array
                ("n", c_int),  # number of strings allocated
                ("refcount", c_int),  # reference count (1 if no clones)
                ("array", POINTER(c_char_p))]  # string array


LPSarray = POINTER(Sarray)
LPLPSarray = POINTER(LPSarray)


class L_Bytea(Structure):
    '''Byte array (analogous to C++ "string")'''
    _fields_ = [
        ("nalloc", c_size_t),  # number of bytes allocated in data array
        ("size", c_size_t),  # number of bytes presently used
        ("refcount", c_int),  # reference count (1 if no clones)
        ("data", c_ubyte_p)]  # data array


class LeptCAPI(CAPI):
    NAME = 'Leptonica'
    API = {
        'pixCleanBackgroundToWhite': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      LPPix,  # PIX * pixim
                                      LPPix,  # PIX * pixg
                                      c_float,  # l_float32 gamma
                                      c_int,  # l_int32 blackval
                                      c_int,  # l_int32 whiteval
                                      ),
        'pixBackgroundNormSimple': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    LPPix,  # PIX * pixim
                                    LPPix,  # PIX * pixg
                                    ),
        'pixBackgroundNorm': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              LPPix,  # PIX * pixim
                              LPPix,  # PIX * pixg
                              c_int,  # l_int32 sx
                              c_int,  # l_int32 sy
                              c_int,  # l_int32 thresh
                              c_int,  # l_int32 mincount
                              c_int,  # l_int32 bgval
                              c_int,  # l_int32 smoothx
                              c_int,  # l_int32 smoothy
                              ),
        'pixBackgroundNormMorph': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   LPPix,  # PIX * pixim
                                   c_int,  # l_int32 reduction
                                   c_int,  # l_int32 size
                                   c_int,  # l_int32 bgval
                                   ),
        'pixBackgroundNormGrayArray': (c_int,
                                       LPPix,  # PIX * pixs
                                       LPPix,  # PIX * pixim
                                       c_int,  # l_int32 sx
                                       c_int,  # l_int32 sy
                                       c_int,  # l_int32 thresh
                                       c_int,  # l_int32 mincount
                                       c_int,  # l_int32 bgval
                                       c_int,  # l_int32 smoothx
                                       c_int,  # l_int32 smoothy
                                       LPLPPix,  # PIX ** ppixd
                                       ),
        'pixBackgroundNormRGBArrays': (c_int,
                                       LPPix,  # PIX * pixs
                                       LPPix,  # PIX * pixim
                                       LPPix,  # PIX * pixg
                                       c_int,  # l_int32 sx
                                       c_int,  # l_int32 sy
                                       c_int,  # l_int32 thresh
                                       c_int,  # l_int32 mincount
                                       c_int,  # l_int32 bgval
                                       c_int,  # l_int32 smoothx
                                       c_int,  # l_int32 smoothy
                                       LPLPPix,  # PIX ** ppixr
                                       LPLPPix,  # PIX ** ppixg
                                       LPLPPix,  # PIX ** ppixb
                                       ),
        'pixBackgroundNormGrayArrayMorph': (c_int,
                                            LPPix,  # PIX * pixs
                                            LPPix,  # PIX * pixim
                                            c_int,  # l_int32 reduction
                                            c_int,  # l_int32 size
                                            c_int,  # l_int32 bgval
                                            LPLPPix,  # PIX ** ppixd
                                            ),
        'pixBackgroundNormRGBArraysMorph': (c_int,
                                            LPPix,  # PIX * pixs
                                            LPPix,  # PIX * pixim
                                            c_int,  # l_int32 reduction
                                            c_int,  # l_int32 size
                                            c_int,  # l_int32 bgval
                                            LPLPPix,  # PIX ** ppixr
                                            LPLPPix,  # PIX ** ppixg
                                            LPLPPix,  # PIX ** ppixb
                                            ),
        'pixGetBackgroundGrayMap': (c_int,
                                    LPPix,  # PIX * pixs
                                    LPPix,  # PIX * pixim
                                    c_int,  # l_int32 sx
                                    c_int,  # l_int32 sy
                                    c_int,  # l_int32 thresh
                                    c_int,  # l_int32 mincount
                                    LPLPPix,  # PIX ** ppixd
                                    ),
        'pixGetBackgroundRGBMap': (c_int,
                                   LPPix,  # PIX * pixs
                                   LPPix,  # PIX * pixim
                                   LPPix,  # PIX * pixg
                                   c_int,  # l_int32 sx
                                   c_int,  # l_int32 sy
                                   c_int,  # l_int32 thresh
                                   c_int,  # l_int32 mincount
                                   LPLPPix,  # PIX ** ppixmr
                                   LPLPPix,  # PIX ** ppixmg
                                   LPLPPix,  # PIX ** ppixmb
                                   ),
        'pixGetBackgroundGrayMapMorph': (c_int,
                                         LPPix,  # PIX * pixs
                                         LPPix,  # PIX * pixim
                                         c_int,  # l_int32 reduction
                                         c_int,  # l_int32 size
                                         LPLPPix,  # PIX ** ppixm
                                         ),
        'pixGetBackgroundRGBMapMorph': (c_int,
                                        LPPix,  # PIX * pixs
                                        LPPix,  # PIX * pixim
                                        c_int,  # l_int32 reduction
                                        c_int,  # l_int32 size
                                        LPLPPix,  # PIX ** ppixmr
                                        LPLPPix,  # PIX ** ppixmg
                                        LPLPPix,  # PIX ** ppixmb
                                        ),
        'pixFillMapHoles': (c_int,
                            LPPix,  # PIX * pix
                            c_int,  # l_int32 nx
                            c_int,  # l_int32 ny
                            c_int,  # l_int32 filltype
                            ),
        'pixExtendByReplication': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 addw
                                   c_int,  # l_int32 addh
                                   ),
        'pixSmoothConnectedRegions': (c_int,
                                      LPPix,  # PIX * pixs
                                      LPPix,  # PIX * pixm
                                      c_int,  # l_int32 factor
                                      ),
        'pixGetInvBackgroundMap': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 bgval
                                   c_int,  # l_int32 smoothx
                                   c_int,  # l_int32 smoothy
                                   ),
        'pixApplyInvBackgroundGrayMap': (LPPix,  # PIX *
                                         LPPix,  # PIX * pixs
                                         LPPix,  # PIX * pixm
                                         c_int,  # l_int32 sx
                                         c_int,  # l_int32 sy
                                         ),
        'pixApplyInvBackgroundRGBMap': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixs
                                        LPPix,  # PIX * pixmr
                                        LPPix,  # PIX * pixmg
                                        LPPix,  # PIX * pixmb
                                        c_int,  # l_int32 sx
                                        c_int,  # l_int32 sy
                                        ),
        'pixApplyVariableGrayMap': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    LPPix,  # PIX * pixg
                                    c_int,  # l_int32 target
                                    ),
        'pixGlobalNormRGB': (LPPix,  # PIX *
                             LPPix,  # PIX * pixd
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 rval
                             c_int,  # l_int32 gval
                             c_int,  # l_int32 bval
                             c_int,  # l_int32 mapval
                             ),
        'pixGlobalNormNoSatRGB': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixd
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 rval
                                  c_int,  # l_int32 gval
                                  c_int,  # l_int32 bval
                                  c_int,  # l_int32 factor
                                  c_float,  # l_float32 rank
                                  ),
        'pixThresholdSpreadNorm': (c_int,
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 filtertype
                                   c_int,  # l_int32 edgethresh
                                   c_int,  # l_int32 smoothx
                                   c_int,  # l_int32 smoothy
                                   c_float,  # l_float32 gamma
                                   c_int,  # l_int32 minval
                                   c_int,  # l_int32 maxval
                                   c_int,  # l_int32 targetthresh
                                   LPLPPix,  # PIX ** ppixth
                                   LPLPPix,  # PIX ** ppixb
                                   LPLPPix,  # PIX ** ppixd
                                   ),
        'pixBackgroundNormFlex': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 sx
                                  c_int,  # l_int32 sy
                                  c_int,  # l_int32 smoothx
                                  c_int,  # l_int32 smoothy
                                  c_int,  # l_int32 delta
                                  ),
        'pixContrastNorm': (LPPix,  # PIX *
                            LPPix,  # PIX * pixd
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 sx
                            c_int,  # l_int32 sy
                            c_int,  # l_int32 mindiff
                            c_int,  # l_int32 smoothx
                            c_int,  # l_int32 smoothy
                            ),
        'pixAffineSampledPta': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                LPPta,  # PTA * ptad
                                LPPta,  # PTA * ptas
                                c_int,  # l_int32 incolor
                                ),
        'pixAffineSampled': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_float_p,  # l_float32 * vc
                             c_int,  # l_int32 incolor
                             ),
        'pixAffinePta': (LPPix,  # PIX *
                         LPPix,  # PIX * pixs
                         LPPta,  # PTA * ptad
                         LPPta,  # PTA * ptas
                         c_int,  # l_int32 incolor
                         ),
        'pixAffine': (LPPix,  # PIX *
                      LPPix,  # PIX * pixs
                      c_float_p,  # l_float32 * vc
                      c_int,  # l_int32 incolor
                      ),
        'pixAffinePtaColor': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              LPPta,  # PTA * ptad
                              LPPta,  # PTA * ptas
                              c_uint,  # l_uint32 colorval
                              ),
        'pixAffineColor': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_float_p,  # l_float32 * vc
                           c_uint,  # l_uint32 colorval
                           ),
        'pixAffinePtaGray': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             LPPta,  # PTA * ptad
                             LPPta,  # PTA * ptas
                             c_ubyte,  # l_uint8 grayval
                             ),
        'pixAffineGray': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_float_p,  # l_float32 * vc
                          c_ubyte,  # l_uint8 grayval
                          ),
        'pixAffinePtaWithAlpha': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  LPPta,  # PTA * ptad
                                  LPPta,  # PTA * ptas
                                  LPPix,  # PIX * pixg
                                  c_float,  # l_float32 fract
                                  c_int,  # l_int32 border
                                  ),
        'getAffineXformCoeffs': (c_int,
                                 LPPta,  # PTA * ptas
                                 LPPta,  # PTA * ptad
                                 # l_float32 ** pvc
                                 POINTER(c_float_p),
                                 ),
        'affineInvertXform': (c_int,
                              c_float_p,  # l_float32 * vc
                              POINTER(c_float_p),  # l_float32 ** pvci
                              ),
        'affineXformSampledPt': (c_int,
                                 c_float_p,  # l_float32 * vc
                                 c_int,  # l_int32 x
                                 c_int,  # l_int32 y
                                 c_int_p,  # l_int32 * pxp
                                 c_int_p,  # l_int32 * pyp
                                 ),
        'affineXformPt': (c_int,
                          c_float_p,  # l_float32 * vc
                          c_int,  # l_int32 x
                          c_int,  # l_int32 y
                          c_float_p,  # l_float32 * pxp
                          c_float_p,  # l_float32 * pyp
                          ),
        'linearInterpolatePixelColor': (c_int,
                                        c_uint_p,  # l_uint32 * datas
                                        c_int,  # l_int32 wpls
                                        c_int,  # l_int32 w
                                        c_int,  # l_int32 h
                                        c_float,  # l_float32 x
                                        c_float,  # l_float32 y
                                        c_uint,  # l_uint32 colorval
                                        c_uint_p,  # l_uint32 * pval
                                        ),
        'linearInterpolatePixelGray': (c_int,
                                       c_uint_p,  # l_uint32 * datas
                                       c_int,  # l_int32 wpls
                                       c_int,  # l_int32 w
                                       c_int,  # l_int32 h
                                       c_float,  # l_float32 x
                                       c_float,  # l_float32 y
                                       c_int,  # l_int32 grayval
                                       c_int_p,  # l_int32 * pval
                                       ),
        'gaussjordan': (c_int,
                        POINTER(c_float_p),  # l_float32 ** a
                        c_float_p,  # l_float32 * b
                        c_int,  # l_int32 n
                        ),
        'pixAffineSequential': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                LPPta,  # PTA * ptad
                                LPPta,  # PTA * ptas
                                c_int,  # l_int32 bw
                                c_int,  # l_int32 bh
                                ),
        'createMatrix2dTranslate': (c_float_p,
                                    c_float,  # l_float32 transx
                                    c_float,  # l_float32 transy
                                    ),
        'createMatrix2dScale': (c_float_p,
                                c_float,  # l_float32 scalex
                                c_float,  # l_float32 scaley
                                ),
        'createMatrix2dRotate': (c_float_p,
                                 c_float,  # l_float32 xc
                                 c_float,  # l_float32 yc
                                 c_float,  # l_float32 angle
                                 ),
        'ptaTranslate': (LPPta,  # PTA *
                         LPPta,  # PTA * ptas
                         c_float,  # l_float32 transx
                         c_float,  # l_float32 transy
                         ),
        'ptaScale': (LPPta,  # PTA *
                     LPPta,  # PTA * ptas
                     c_float,  # l_float32 scalex
                     c_float,  # l_float32 scaley
                     ),
        'ptaRotate': (LPPta,  # PTA *
                      LPPta,  # PTA * ptas
                      c_float,  # l_float32 xc
                      c_float,  # l_float32 yc
                      c_float,  # l_float32 angle
                      ),
        'boxaTranslate': (LPBoxa,  # BOXA *
                          LPBoxa,  # BOXA * boxas
                          c_float,  # l_float32 transx
                          c_float,  # l_float32 transy
                          ),
        'boxaScale': (LPBoxa,  # BOXA *
                      LPBoxa,  # BOXA * boxas
                      c_float,  # l_float32 scalex
                      c_float,  # l_float32 scaley
                      ),
        'boxaRotate': (LPBoxa,  # BOXA *
                       LPBoxa,  # BOXA * boxas
                       c_float,  # l_float32 xc
                       c_float,  # l_float32 yc
                       c_float,  # l_float32 angle
                       ),
        'ptaAffineTransform': (LPPta,  # PTA *
                               LPPta,  # PTA * ptas
                               c_float_p,  # l_float32 * mat
                               ),
        'boxaAffineTransform': (LPBoxa,  # BOXA *
                                LPBoxa,  # BOXA * boxas
                                c_float_p,  # l_float32 * mat
                                ),
        'l_productMatVec': (c_int,
                            c_float_p,  # l_float32 * mat
                            c_float_p,  # l_float32 * vecs
                            c_float_p,  # l_float32 * vecd
                            c_int,  # l_int32 size
                            ),
        'l_productMat2': (c_int,
                          c_float_p,  # l_float32 * mat1
                          c_float_p,  # l_float32 * mat2
                          c_float_p,  # l_float32 * matd
                          c_int,  # l_int32 size
                          ),
        'l_productMat3': (c_int,
                          c_float_p,  # l_float32 * mat1
                          c_float_p,  # l_float32 * mat2
                          c_float_p,  # l_float32 * mat3
                          c_float_p,  # l_float32 * matd
                          c_int,  # l_int32 size
                          ),
        'l_productMat4': (c_int,
                          c_float_p,  # l_float32 * mat1
                          c_float_p,  # l_float32 * mat2
                          c_float_p,  # l_float32 * mat3
                          c_float_p,  # l_float32 * mat4
                          c_float_p,  # l_float32 * matd
                          c_int,  # l_int32 size
                          ),
        'l_getDataBit': (c_int,
                         c_void_p,  # const void * line
                         c_int,  # l_int32 n
                         ),
        'l_setDataBit': (None,
                         c_void_p,  # void * line
                         c_int,  # l_int32 n
                         ),
        'l_clearDataBit': (None,
                           c_void_p,  # void * line
                           c_int,  # l_int32 n
                           ),
        'l_setDataBitVal': (None,
                            c_void_p,  # void * line
                            c_int,  # l_int32 n
                            c_int,  # l_int32 val
                            ),
        'l_getDataDibit': (c_int,
                           c_void_p,  # const void * line
                           c_int,  # l_int32 n
                           ),
        'l_setDataDibit': (None,
                           c_void_p,  # void * line
                           c_int,  # l_int32 n
                           c_int,  # l_int32 val
                           ),
        'l_clearDataDibit': (None,
                             c_void_p,  # void * line
                             c_int,  # l_int32 n
                             ),
        'l_getDataQbit': (c_int,
                          c_void_p,  # const void * line
                          c_int,  # l_int32 n
                          ),
        'l_setDataQbit': (None,
                          c_void_p,  # void * line
                          c_int,  # l_int32 n
                          c_int,  # l_int32 val
                          ),
        'l_clearDataQbit': (None,
                            c_void_p,  # void * line
                            c_int,  # l_int32 n
                            ),
        'l_getDataByte': (c_int,
                          c_void_p,  # const void * line
                          c_int,  # l_int32 n
                          ),
        'l_setDataByte': (None,
                          c_void_p,  # void * line
                          c_int,  # l_int32 n
                          c_int,  # l_int32 val
                          ),
        'l_getDataTwoBytes': (c_int,
                              c_void_p,  # const void * line
                              c_int,  # l_int32 n
                              ),
        'l_setDataTwoBytes': (None,
                              c_void_p,  # void * line
                              c_int,  # l_int32 n
                              c_int,  # l_int32 val
                              ),
        'l_getDataFourBytes': (c_int,
                               c_void_p,  # const void * line
                               c_int,  # l_int32 n
                               ),
        'l_setDataFourBytes': (None,
                               c_void_p,  # void * line
                               c_int,  # l_int32 n
                               c_int,  # l_int32 val
                               ),
        'barcodeDispatchDecoder': (c_char_p,
                                   c_char_p,  # char * barstr
                                   c_int,  # l_int32 format
                                   c_int,  # l_int32 debugflag
                                   ),
        'barcodeFormatIsSupported': (c_int,
                                     c_int,  # l_int32 format
                                     ),
        'pixFindBaselines': (LPNuma,  # NUMA *
                             LPPix,  # PIX * pixs
                             LPLPPta,  # PTA ** ppta
                             LPPixa,  # PIXA * pixadb
                             ),
        'pixDeskewLocal': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 nslices
                           c_int,  # l_int32 redsweep
                           c_int,  # l_int32 redsearch
                           c_float,  # l_float32 sweeprange
                           c_float,  # l_float32 sweepdelta
                           c_float,  # l_float32 minbsdelta
                           ),
        'pixGetLocalSkewTransform': (c_int,
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 nslices
                                     c_int,  # l_int32 redsweep
                                     c_int,  # l_int32 redsearch
                                     c_float,  # l_float32 sweeprange
                                     c_float,  # l_float32 sweepdelta
                                     c_float,  # l_float32 minbsdelta
                                     LPLPPta,  # PTA ** pptas
                                     LPLPPta,  # PTA ** pptad
                                     ),
        'pixGetLocalSkewAngles': (LPNuma,  # NUMA *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 nslices
                                  c_int,  # l_int32 redsweep
                                  c_int,  # l_int32 redsearch
                                  c_float,  # l_float32 sweeprange
                                  c_float,  # l_float32 sweepdelta
                                  c_float,  # l_float32 minbsdelta
                                  c_float_p,  # l_float32 * pa
                                  c_float_p,  # l_float32 * pb
                                  c_int,  # l_int32 debug
                                  ),
        'pixBilateral': (LPPix,  # PIX *
                         LPPix,  # PIX * pixs
                         c_float,  # l_float32 spatial_stdev
                         c_float,  # l_float32 range_stdev
                         c_int,  # l_int32 ncomps
                         c_int,  # l_int32 reduction
                         ),
        'pixBilateralGray': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_float,  # l_float32 spatial_stdev
                             c_float,  # l_float32 range_stdev
                             c_int,  # l_int32 ncomps
                             c_int,  # l_int32 reduction
                             ),
        'pixBlockBilateralExact': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_float,  # l_float32 spatial_stdev
                                   c_float,  # l_float32 range_stdev
                                   ),
        'pixBilinearSampledPta': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  LPPta,  # PTA * ptad
                                  LPPta,  # PTA * ptas
                                  c_int,  # l_int32 incolor
                                  ),
        'pixBilinearSampled': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_float_p,  # l_float32 * vc
                               c_int,  # l_int32 incolor
                               ),
        'pixBilinearPta': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           LPPta,  # PTA * ptad
                           LPPta,  # PTA * ptas
                           c_int,  # l_int32 incolor
                           ),
        'pixBilinear': (LPPix,  # PIX *
                        LPPix,  # PIX * pixs
                        c_float_p,  # l_float32 * vc
                        c_int,  # l_int32 incolor
                        ),
        'pixBilinearPtaColor': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                LPPta,  # PTA * ptad
                                LPPta,  # PTA * ptas
                                c_uint,  # l_uint32 colorval
                                ),
        'pixBilinearColor': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_float_p,  # l_float32 * vc
                             c_uint,  # l_uint32 colorval
                             ),
        'pixBilinearPtaGray': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               LPPta,  # PTA * ptad
                               LPPta,  # PTA * ptas
                               c_ubyte,  # l_uint8 grayval
                               ),
        'pixBilinearGray': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_float_p,  # l_float32 * vc
                            c_ubyte,  # l_uint8 grayval
                            ),
        'pixBilinearPtaWithAlpha': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    LPPta,  # PTA * ptad
                                    LPPta,  # PTA * ptas
                                    LPPix,  # PIX * pixg
                                    c_float,  # l_float32 fract
                                    c_int,  # l_int32 border
                                    ),
        'getBilinearXformCoeffs': (c_int,
                                   LPPta,  # PTA * ptas
                                   LPPta,  # PTA * ptad
                                   # l_float32 ** pvc
                                   POINTER(c_float_p),
                                   ),
        'bilinearXformSampledPt': (c_int,
                                   c_float_p,  # l_float32 * vc
                                   c_int,  # l_int32 x
                                   c_int,  # l_int32 y
                                   c_int_p,  # l_int32 * pxp
                                   c_int_p,  # l_int32 * pyp
                                   ),
        'bilinearXformPt': (c_int,
                            c_float_p,  # l_float32 * vc
                            c_int,  # l_int32 x
                            c_int,  # l_int32 y
                            c_float_p,  # l_float32 * pxp
                            c_float_p,  # l_float32 * pyp
                            ),
        'pixOtsuAdaptiveThreshold': (c_int,
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 sx
                                     c_int,  # l_int32 sy
                                     c_int,  # l_int32 smoothx
                                     c_int,  # l_int32 smoothy
                                     c_float,  # l_float32 scorefract
                                     LPLPPix,  # PIX ** ppixth
                                     LPLPPix,  # PIX ** ppixd
                                     ),
        'pixOtsuThreshOnBackgroundNorm': (LPPix,  # PIX *
                                          LPPix,  # PIX * pixs
                                          LPPix,  # PIX * pixim
                                          c_int,  # l_int32 sx
                                          c_int,  # l_int32 sy
                                          c_int,  # l_int32 thresh
                                          c_int,  # l_int32 mincount
                                          c_int,  # l_int32 bgval
                                          c_int,  # l_int32 smoothx
                                          c_int,  # l_int32 smoothy
                                          c_float,  # l_float32 scorefract
                                          c_int_p,  # l_int32 * pthresh
                                          ),
        'pixMaskedThreshOnBackgroundNorm': (LPPix,  # PIX *
                                            LPPix,  # PIX * pixs
                                            LPPix,  # PIX * pixim
                                            c_int,  # l_int32 sx
                                            c_int,  # l_int32 sy
                                            c_int,  # l_int32 thresh
                                            c_int,  # l_int32 mincount
                                            c_int,  # l_int32 smoothx
                                            c_int,  # l_int32 smoothy
                                            c_float,  # l_float32 scorefract
                                            # l_int32 * pthresh
                                            c_int_p,
                                            ),
        'pixSauvolaBinarizeTiled': (c_int,
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 whsize
                                    c_float,  # l_float32 factor
                                    c_int,  # l_int32 nx
                                    c_int,  # l_int32 ny
                                    LPLPPix,  # PIX ** ppixth
                                    LPLPPix,  # PIX ** ppixd
                                    ),
        'pixSauvolaBinarize': (c_int,
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 whsize
                               c_float,  # l_float32 factor
                               c_int,  # l_int32 addborder
                               LPLPPix,  # PIX ** ppixm
                               LPLPPix,  # PIX ** ppixsd
                               LPLPPix,  # PIX ** ppixth
                               LPLPPix,  # PIX ** ppixd
                               ),
        'pixSauvolaOnContrastNorm': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 mindiff
                                     LPLPPix,  # PIX ** ppixn
                                     LPLPPix,  # PIX ** ppixth
                                     ),
        'pixThreshOnDoubleNorm': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 mindiff
                                  ),
        'pixThresholdByConnComp': (c_int,
                                   LPPix,  # PIX * pixs
                                   LPPix,  # PIX * pixm
                                   c_int,  # l_int32 start
                                   c_int,  # l_int32 end
                                   c_int,  # l_int32 incr
                                   c_float,  # l_float32 thresh48
                                   c_float,  # l_float32 threshdiff
                                   c_int_p,  # l_int32 * pglobthresh
                                   LPLPPix,  # PIX ** ppixd
                                   c_int,  # l_int32 debugflag
                                   ),
        'pixThresholdByHisto': (c_int,
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 factor
                                c_int,  # l_int32 halfw
                                c_float,  # l_float32 delta
                                c_int_p,  # l_int32 * pthresh
                                LPLPPix,  # PIX ** ppixd
                                LPLPPix,  # PIX ** ppixhisto
                                ),
        'pixExpandBinaryReplicate': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 xfact
                                     c_int,  # l_int32 yfact
                                     ),
        'pixExpandBinaryPower2': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 factor
                                  ),
        'pixReduceBinary2': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_ubyte_p,  # l_uint8 * intab
                             ),
        'pixReduceRankBinaryCascade': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 level1
                                       c_int,  # l_int32 level2
                                       c_int,  # l_int32 level3
                                       c_int,  # l_int32 level4
                                       ),
        'pixReduceRankBinary2': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 level
                                 c_ubyte_p,  # l_uint8 * intab
                                 ),
        'makeSubsampleTab2x': (c_ubyte_p, ),
        'pixBlend': (LPPix,  # PIX *
                     LPPix,  # PIX * pixs1
                     LPPix,  # PIX * pixs2
                     c_int,  # l_int32 x
                     c_int,  # l_int32 y
                     c_float,  # l_float32 fract
                     ),
        'pixBlendMask': (LPPix,  # PIX *
                         LPPix,  # PIX * pixd
                         LPPix,  # PIX * pixs1
                         LPPix,  # PIX * pixs2
                         c_int,  # l_int32 x
                         c_int,  # l_int32 y
                         c_float,  # l_float32 fract
                         c_int,  # l_int32 type
                         ),
        'pixBlendGray': (LPPix,  # PIX *
                         LPPix,  # PIX * pixd
                         LPPix,  # PIX * pixs1
                         LPPix,  # PIX * pixs2
                         c_int,  # l_int32 x
                         c_int,  # l_int32 y
                         c_float,  # l_float32 fract
                         c_int,  # l_int32 type
                         c_int,  # l_int32 transparent
                         c_uint,  # l_uint32 transpix
                         ),
        'pixBlendGrayInverse': (LPPix,  # PIX *
                                LPPix,  # PIX * pixd
                                LPPix,  # PIX * pixs1
                                LPPix,  # PIX * pixs2
                                c_int,  # l_int32 x
                                c_int,  # l_int32 y
                                c_float,  # l_float32 fract
                                ),
        'pixBlendColor': (LPPix,  # PIX *
                          LPPix,  # PIX * pixd
                          LPPix,  # PIX * pixs1
                          LPPix,  # PIX * pixs2
                          c_int,  # l_int32 x
                          c_int,  # l_int32 y
                          c_float,  # l_float32 fract
                          c_int,  # l_int32 transparent
                          c_uint,  # l_uint32 transpix
                          ),
        'pixBlendColorByChannel': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixd
                                   LPPix,  # PIX * pixs1
                                   LPPix,  # PIX * pixs2
                                   c_int,  # l_int32 x
                                   c_int,  # l_int32 y
                                   c_float,  # l_float32 rfract
                                   c_float,  # l_float32 gfract
                                   c_float,  # l_float32 bfract
                                   c_int,  # l_int32 transparent
                                   c_uint,  # l_uint32 transpix
                                   ),
        'pixBlendGrayAdapt': (LPPix,  # PIX *
                              LPPix,  # PIX * pixd
                              LPPix,  # PIX * pixs1
                              LPPix,  # PIX * pixs2
                              c_int,  # l_int32 x
                              c_int,  # l_int32 y
                              c_float,  # l_float32 fract
                              c_int,  # l_int32 shift
                              ),
        'pixFadeWithGray': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            LPPix,  # PIX * pixb
                            c_float,  # l_float32 factor
                            c_int,  # l_int32 type
                            ),
        'pixBlendHardLight': (LPPix,  # PIX *
                              LPPix,  # PIX * pixd
                              LPPix,  # PIX * pixs1
                              LPPix,  # PIX * pixs2
                              c_int,  # l_int32 x
                              c_int,  # l_int32 y
                              c_float,  # l_float32 fract
                              ),
        'pixBlendCmap': (c_int,
                         LPPix,  # PIX * pixs
                         LPPix,  # PIX * pixb
                         c_int,  # l_int32 x
                         c_int,  # l_int32 y
                         c_int,  # l_int32 sindex
                         ),
        'pixBlendWithGrayMask': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs1
                                 LPPix,  # PIX * pixs2
                                 LPPix,  # PIX * pixg
                                 c_int,  # l_int32 x
                                 c_int,  # l_int32 y
                                 ),
        'pixBlendBackgroundToColor': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixd
                                      LPPix,  # PIX * pixs
                                      LPBox,  # BOX * box
                                      c_uint,  # l_uint32 color
                                      c_float,  # l_float32 gamma
                                      c_int,  # l_int32 minval
                                      c_int,  # l_int32 maxval
                                      ),
        'pixMultiplyByColor': (LPPix,  # PIX *
                               LPPix,  # PIX * pixd
                               LPPix,  # PIX * pixs
                               LPBox,  # BOX * box
                               c_uint,  # l_uint32 color
                               ),
        'pixAlphaBlendUniform': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_uint,  # l_uint32 color
                                 ),
        'pixAddAlphaToBlend': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_float,  # l_float32 fract
                               c_int,  # l_int32 invert
                               ),
        'pixSetAlphaOverWhite': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 ),
        'pixLinearEdgeFade': (c_int,
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 dir
                              c_int,  # l_int32 fadeto
                              c_float,  # l_float32 distfract
                              c_float,  # l_float32 maxfade
                              ),
        'pixaGetFont': (LPPixa,  # PIXA *
                        c_char_p,  # const char * dir
                        c_int,  # l_int32 fontsize
                        c_int_p,  # l_int32 * pbl0
                        c_int_p,  # l_int32 * pbl1
                        c_int_p,  # l_int32 * pbl2
                        ),
        'pixaSaveFont': (c_int,
                         c_char_p,  # const char * indir
                         c_char_p,  # const char * outdir
                         c_int,  # l_int32 fontsize
                         ),
        'pixReadStreamBmp': (LPPix,  # PIX *
                             LPFile,  # FILE * fp
                             ),
        'pixReadMemBmp': (LPPix,  # PIX *
                          c_ubyte_p,  # const l_uint8 * cdata
                          c_size_t,  # size_t size
                          ),
        'pixWriteStreamBmp': (c_int,
                              LPFile,  # FILE * fp
                              LPPix,  # PIX * pix
                              ),
        'pixWriteMemBmp': (c_int,
                           POINTER(c_ubyte_p),  # l_uint8 ** pfdata
                           c_size_t_p,  # size_t * pfsize
                           LPPix,  # PIX * pixs
                           ),
        'l_bootnum_gen1': (LPPixa, ),  # PIXA *
        'l_bootnum_gen2': (LPPixa, ),  # PIXA *
        'l_bootnum_gen3': (LPPixa, ),  # PIXA *
        'l_bootnum_gen4': (LPPixa,  # PIXA *
                           c_int,  # l_int32 nsamp
                           ),
        'boxCreate': (LPBox,  # BOX *
                      c_int,  # l_int32 x
                      c_int,  # l_int32 y
                      c_int,  # l_int32 w
                      c_int,  # l_int32 h
                      ),
        'boxCreateValid': (LPBox,  # BOX *
                           c_int,  # l_int32 x
                           c_int,  # l_int32 y
                           c_int,  # l_int32 w
                           c_int,  # l_int32 h
                           ),
        'boxCopy': (LPBox,  # BOX *
                    LPBox,  # BOX * box
                    ),
        'boxClone': (LPBox,  # BOX *
                     LPBox,  # BOX * box
                     ),
        'boxDestroy': (None,
                       LPLPBox,  # BOX ** pbox
                       ),
        'boxGetGeometry': (c_int,
                           LPBox,  # BOX * box
                           c_int_p,  # l_int32 * px
                           c_int_p,  # l_int32 * py
                           c_int_p,  # l_int32 * pw
                           c_int_p,  # l_int32 * ph
                           ),
        'boxSetGeometry': (c_int,
                           LPBox,  # BOX * box
                           c_int,  # l_int32 x
                           c_int,  # l_int32 y
                           c_int,  # l_int32 w
                           c_int,  # l_int32 h
                           ),
        'boxGetSideLocations': (c_int,
                                LPBox,  # BOX * box
                                c_int_p,  # l_int32 * pl
                                c_int_p,  # l_int32 * pr
                                c_int_p,  # l_int32 * pt
                                c_int_p,  # l_int32 * pb
                                ),
        'boxSetSideLocations': (c_int,
                                LPBox,  # BOX * box
                                c_int,  # l_int32 l
                                c_int,  # l_int32 r
                                c_int,  # l_int32 t
                                c_int,  # l_int32 b
                                ),
        'boxGetRefcount': (c_int,
                           LPBox,  # BOX * box
                           ),
        'boxChangeRefcount': (c_int,
                              LPBox,  # BOX * box
                              c_int,  # l_int32 delta
                              ),
        'boxIsValid': (c_int,
                       LPBox,  # BOX * box
                       c_int_p,  # l_int32 * pvalid
                       ),
        'boxaCreate': (LPBoxa,  # BOXA *
                       c_int,  # l_int32 n
                       ),
        'boxaCopy': (LPBoxa,  # BOXA *
                     LPBoxa,  # BOXA * boxa
                     c_int,  # l_int32 copyflag
                     ),
        'boxaDestroy': (None,
                        LPLPBoxa,  # BOXA ** pboxa
                        ),
        'boxaAddBox': (c_int,
                       LPBoxa,  # BOXA * boxa
                       LPBox,  # BOX * box
                       c_int,  # l_int32 copyflag
                       ),
        'boxaExtendArray': (c_int,
                            LPBoxa,  # BOXA * boxa
                            ),
        'boxaExtendArrayToSize': (c_int,
                                  LPBoxa,  # BOXA * boxa
                                  c_size_t,  # size_t size
                                  ),
        'boxaGetCount': (c_int,
                         LPBoxa,  # BOXA * boxa
                         ),
        'boxaGetValidCount': (c_int,
                              LPBoxa,  # BOXA * boxa
                              ),
        'boxaGetBox': (LPBox,  # BOX *
                       LPBoxa,  # BOXA * boxa
                       c_int,  # l_int32 index
                       c_int,  # l_int32 accessflag
                       ),
        'boxaGetValidBox': (LPBox,  # BOX *
                            LPBoxa,  # BOXA * boxa
                            c_int,  # l_int32 index
                            c_int,  # l_int32 accessflag
                            ),
        'boxaFindInvalidBoxes': (LPNuma,  # NUMA *
                                 LPBoxa,  # BOXA * boxa
                                 ),
        'boxaGetBoxGeometry': (c_int,
                               LPBoxa,  # BOXA * boxa
                               c_int,  # l_int32 index
                               c_int_p,  # l_int32 * px
                               c_int_p,  # l_int32 * py
                               c_int_p,  # l_int32 * pw
                               c_int_p,  # l_int32 * ph
                               ),
        'boxaIsFull': (c_int,
                       LPBoxa,  # BOXA * boxa
                       c_int_p,  # l_int32 * pfull
                       ),
        'boxaReplaceBox': (c_int,
                           LPBoxa,  # BOXA * boxa
                           c_int,  # l_int32 index
                           LPBox,  # BOX * box
                           ),
        'boxaInsertBox': (c_int,
                          LPBoxa,  # BOXA * boxa
                          c_int,  # l_int32 index
                          LPBox,  # BOX * box
                          ),
        'boxaRemoveBox': (c_int,
                          LPBoxa,  # BOXA * boxa
                          c_int,  # l_int32 index
                          ),
        'boxaRemoveBoxAndSave': (c_int,
                                 LPBoxa,  # BOXA * boxa
                                 c_int,  # l_int32 index
                                 LPLPBox,  # BOX ** pbox
                                 ),
        'boxaSaveValid': (LPBoxa,  # BOXA *
                          LPBoxa,  # BOXA * boxas
                          c_int,  # l_int32 copyflag
                          ),
        'boxaInitFull': (c_int,
                         LPBoxa,  # BOXA * boxa
                         LPBox,  # BOX * box
                         ),
        'boxaClear': (c_int,
                      LPBoxa,  # BOXA * boxa
                      ),
        'boxaaCreate': (LPBoxaa,  # BOXAA *
                        c_int,  # l_int32 n
                        ),
        'boxaaCopy': (LPBoxaa,  # BOXAA *
                      LPBoxaa,  # BOXAA * baas
                      c_int,  # l_int32 copyflag
                      ),
        'boxaaDestroy': (None,
                         LPLPBoxaa,  # BOXAA ** pbaa
                         ),
        'boxaaAddBoxa': (c_int,
                         LPBoxaa,  # BOXAA * baa
                         LPBoxa,  # BOXA * ba
                         c_int,  # l_int32 copyflag
                         ),
        'boxaaExtendArray': (c_int,
                             LPBoxaa,  # BOXAA * baa
                             ),
        'boxaaExtendArrayToSize': (c_int,
                                   LPBoxaa,  # BOXAA * baa
                                   c_int,  # l_int32 size
                                   ),
        'boxaaGetCount': (c_int,
                          LPBoxaa,  # BOXAA * baa
                          ),
        'boxaaGetBoxCount': (c_int,
                             LPBoxaa,  # BOXAA * baa
                             ),
        'boxaaGetBoxa': (LPBoxa,  # BOXA *
                         LPBoxaa,  # BOXAA * baa
                         c_int,  # l_int32 index
                         c_int,  # l_int32 accessflag
                         ),
        'boxaaGetBox': (LPBox,  # BOX *
                        LPBoxaa,  # BOXAA * baa
                        c_int,  # l_int32 iboxa
                        c_int,  # l_int32 ibox
                        c_int,  # l_int32 accessflag
                        ),
        'boxaaInitFull': (c_int,
                          LPBoxaa,  # BOXAA * baa
                          LPBoxa,  # BOXA * boxa
                          ),
        'boxaaExtendWithInit': (c_int,
                                LPBoxaa,  # BOXAA * baa
                                c_int,  # l_int32 maxindex
                                LPBoxa,  # BOXA * boxa
                                ),
        'boxaaReplaceBoxa': (c_int,
                             LPBoxaa,  # BOXAA * baa
                             c_int,  # l_int32 index
                             LPBoxa,  # BOXA * boxa
                             ),
        'boxaaInsertBoxa': (c_int,
                            LPBoxaa,  # BOXAA * baa
                            c_int,  # l_int32 index
                            LPBoxa,  # BOXA * boxa
                            ),
        'boxaaRemoveBoxa': (c_int,
                            LPBoxaa,  # BOXAA * baa
                            c_int,  # l_int32 index
                            ),
        'boxaaAddBox': (c_int,
                        LPBoxaa,  # BOXAA * baa
                        c_int,  # l_int32 index
                        LPBox,  # BOX * box
                        c_int,  # l_int32 accessflag
                        ),
        'boxaaReadFromFiles': (LPBoxaa,  # BOXAA *
                               c_char_p,  # const char * dirname
                               c_char_p,  # const char * substr
                               c_int,  # l_int32 first
                               c_int,  # l_int32 nfiles
                               ),
        'boxaaRead': (LPBoxaa,  # BOXAA *
                      c_char_p,  # const char * filename
                      ),
        'boxaaReadStream': (LPBoxaa,  # BOXAA *
                            LPFile,  # FILE * fp
                            ),
        'boxaaReadMem': (LPBoxaa,  # BOXAA *
                         c_ubyte_p,  # const l_uint8 * data
                         c_size_t,  # size_t size
                         ),
        'boxaaWrite': (c_int,
                       c_char_p,  # const char * filename
                       LPBoxaa,  # BOXAA * baa
                       ),
        'boxaaWriteStream': (c_int,
                             LPFile,  # FILE * fp
                             LPBoxaa,  # BOXAA * baa
                             ),
        'boxaaWriteMem': (c_int,
                          POINTER(c_ubyte_p),  # l_uint8 ** pdata
                          c_size_t_p,  # size_t * psize
                          LPBoxaa,  # BOXAA * baa
                          ),
        'boxaRead': (LPBoxa,  # BOXA *
                     c_char_p,  # const char * filename
                     ),
        'boxaReadStream': (LPBoxa,  # BOXA *
                           LPFile,  # FILE * fp
                           ),
        'boxaReadMem': (LPBoxa,  # BOXA *
                        c_ubyte_p,  # const l_uint8 * data
                        c_size_t,  # size_t size
                        ),
        'boxaWriteDebug': (c_int,
                           c_char_p,  # const char * filename
                           LPBoxa,  # BOXA * boxa
                           ),
        'boxaWrite': (c_int,
                      c_char_p,  # const char * filename
                      LPBoxa,  # BOXA * boxa
                      ),
        'boxaWriteStream': (c_int,
                            LPFile,  # FILE * fp
                            LPBoxa,  # BOXA * boxa
                            ),
        'boxaWriteStderr': (c_int,
                            LPBoxa,  # BOXA * boxa
                            ),
        'boxaWriteMem': (c_int,
                         POINTER(c_ubyte_p),  # l_uint8 ** pdata
                         c_size_t_p,  # size_t * psize
                         LPBoxa,  # BOXA * boxa
                         ),
        'boxPrintStreamInfo': (c_int,
                               LPFile,  # FILE * fp
                               LPBox,  # BOX * box
                               ),
        'boxContains': (c_int,
                        LPBox,  # BOX * box1
                        LPBox,  # BOX * box2
                        c_int_p,  # l_int32 * presult
                        ),
        'boxIntersects': (c_int,
                          LPBox,  # BOX * box1
                          LPBox,  # BOX * box2
                          c_int_p,  # l_int32 * presult
                          ),
        'boxaContainedInBox': (LPBoxa,  # BOXA *
                               LPBoxa,  # BOXA * boxas
                               LPBox,  # BOX * box
                               ),
        'boxaContainedInBoxCount': (c_int,
                                    LPBoxa,  # BOXA * boxa
                                    LPBox,  # BOX * box
                                    c_int_p,  # l_int32 * pcount
                                    ),
        'boxaContainedInBoxa': (c_int,
                                LPBoxa,  # BOXA * boxa1
                                LPBoxa,  # BOXA * boxa2
                                c_int_p,  # l_int32 * pcontained
                                ),
        'boxaIntersectsBox': (LPBoxa,  # BOXA *
                              LPBoxa,  # BOXA * boxas
                              LPBox,  # BOX * box
                              ),
        'boxaIntersectsBoxCount': (c_int,
                                   LPBoxa,  # BOXA * boxa
                                   LPBox,  # BOX * box
                                   c_int_p,  # l_int32 * pcount
                                   ),
        'boxaClipToBox': (LPBoxa,  # BOXA *
                          LPBoxa,  # BOXA * boxas
                          LPBox,  # BOX * box
                          ),
        'boxaCombineOverlaps': (LPBoxa,  # BOXA *
                                LPBoxa,  # BOXA * boxas
                                LPPixa,  # PIXA * pixadb
                                ),
        'boxaCombineOverlapsInPair': (c_int,
                                      LPBoxa,  # BOXA * boxas1
                                      LPBoxa,  # BOXA * boxas2
                                      LPLPBoxa,  # BOXA ** pboxad1
                                      LPLPBoxa,  # BOXA ** pboxad2
                                      LPPixa,  # PIXA * pixadb
                                      ),
        'boxOverlapRegion': (LPBox,  # BOX *
                             LPBox,  # BOX * box1
                             LPBox,  # BOX * box2
                             ),
        'boxBoundingRegion': (LPBox,  # BOX *
                              LPBox,  # BOX * box1
                              LPBox,  # BOX * box2
                              ),
        'boxOverlapFraction': (c_int,
                               LPBox,  # BOX * box1
                               LPBox,  # BOX * box2
                               c_float_p,  # l_float32 * pfract
                               ),
        'boxOverlapArea': (c_int,
                           LPBox,  # BOX * box1
                           LPBox,  # BOX * box2
                           c_int_p,  # l_int32 * parea
                           ),
        'boxaHandleOverlaps': (LPBoxa,  # BOXA *
                               LPBoxa,  # BOXA * boxas
                               c_int,  # l_int32 op
                               c_int,  # l_int32 range
                               c_float,  # l_float32 min_overlap
                               c_float,  # l_float32 max_ratio
                               LPLPNuma,  # NUMA ** pnamap
                               ),
        'boxOverlapDistance': (c_int,
                               LPBox,  # BOX * box1
                               LPBox,  # BOX * box2
                               c_int_p,  # l_int32 * ph_ovl
                               c_int_p,  # l_int32 * pv_ovl
                               ),
        'boxSeparationDistance': (c_int,
                                  LPBox,  # BOX * box1
                                  LPBox,  # BOX * box2
                                  c_int_p,  # l_int32 * ph_sep
                                  c_int_p,  # l_int32 * pv_sep
                                  ),
        'boxCompareSize': (c_int,
                           LPBox,  # BOX * box1
                           LPBox,  # BOX * box2
                           c_int,  # l_int32 type
                           c_int_p,  # l_int32 * prel
                           ),
        'boxContainsPt': (c_int,
                          LPBox,  # BOX * box
                          c_float,  # l_float32 x
                          c_float,  # l_float32 y
                          c_int_p,  # l_int32 * pcontains
                          ),
        'boxaGetNearestToPt': (LPBox,  # BOX *
                               LPBoxa,  # BOXA * boxa
                               c_int,  # l_int32 x
                               c_int,  # l_int32 y
                               ),
        'boxaGetNearestToLine': (LPBox,  # BOX *
                                 LPBoxa,  # BOXA * boxa
                                 c_int,  # l_int32 x
                                 c_int,  # l_int32 y
                                 ),
        'boxaFindNearestBoxes': (c_int,
                                 LPBoxa,  # BOXA * boxa
                                 c_int,  # l_int32 dist_select
                                 c_int,  # l_int32 range
                                 LPLPNumaa,  # NUMAA ** pnaaindex
                                 LPLPNumaa,  # NUMAA ** pnaadist
                                 ),
        'boxaGetNearestByDirection': (c_int,
                                      LPBoxa,  # BOXA * boxa
                                      c_int,  # l_int32 i
                                      c_int,  # l_int32 dir
                                      c_int,  # l_int32 dist_select
                                      c_int,  # l_int32 range
                                      c_int_p,  # l_int32 * pindex
                                      c_int_p,  # l_int32 * pdist
                                      ),
        'boxGetCenter': (c_int,
                         LPBox,  # BOX * box
                         c_float_p,  # l_float32 * pcx
                         c_float_p,  # l_float32 * pcy
                         ),
        'boxIntersectByLine': (c_int,
                               LPBox,  # BOX * box
                               c_int,  # l_int32 x
                               c_int,  # l_int32 y
                               c_float,  # l_float32 slope
                               c_int_p,  # l_int32 * px1
                               c_int_p,  # l_int32 * py1
                               c_int_p,  # l_int32 * px2
                               c_int_p,  # l_int32 * py2
                               c_int_p,  # l_int32 * pn
                               ),
        'boxClipToRectangle': (LPBox,  # BOX *
                               LPBox,  # BOX * box
                               c_int,  # l_int32 wi
                               c_int,  # l_int32 hi
                               ),
        'boxClipToRectangleParams': (c_int,
                                     LPBox,  # BOX * box
                                     c_int,  # l_int32 w
                                     c_int,  # l_int32 h
                                     c_int_p,  # l_int32 * pxstart
                                     c_int_p,  # l_int32 * pystart
                                     c_int_p,  # l_int32 * pxend
                                     c_int_p,  # l_int32 * pyend
                                     c_int_p,  # l_int32 * pbw
                                     c_int_p,  # l_int32 * pbh
                                     ),
        'boxRelocateOneSide': (LPBox,  # BOX *
                               LPBox,  # BOX * boxd
                               LPBox,  # BOX * boxs
                               c_int,  # l_int32 loc
                               c_int,  # l_int32 sideflag
                               ),
        'boxaAdjustSides': (LPBoxa,  # BOXA *
                            LPBoxa,  # BOXA * boxas
                            c_int,  # l_int32 delleft
                            c_int,  # l_int32 delright
                            c_int,  # l_int32 deltop
                            c_int,  # l_int32 delbot
                            ),
        'boxaAdjustBoxSides': (c_int,
                               LPBoxa,  # BOXA * boxa
                               c_int,  # l_int32 index
                               c_int,  # l_int32 delleft
                               c_int,  # l_int32 delright
                               c_int,  # l_int32 deltop
                               c_int,  # l_int32 delbot
                               ),
        'boxAdjustSides': (LPBox,  # BOX *
                           LPBox,  # BOX * boxd
                           LPBox,  # BOX * boxs
                           c_int,  # l_int32 delleft
                           c_int,  # l_int32 delright
                           c_int,  # l_int32 deltop
                           c_int,  # l_int32 delbot
                           ),
        'boxaSetSide': (LPBoxa,  # BOXA *
                        LPBoxa,  # BOXA * boxad
                        LPBoxa,  # BOXA * boxas
                        c_int,  # l_int32 side
                        c_int,  # l_int32 val
                        c_int,  # l_int32 thresh
                        ),
        'boxSetSide': (c_int,
                       LPBox,  # BOX * boxs
                       c_int,  # l_int32 side
                       c_int,  # l_int32 val
                       c_int,  # l_int32 thresh
                       ),
        'boxaAdjustWidthToTarget': (LPBoxa,  # BOXA *
                                    LPBoxa,  # BOXA * boxad
                                    LPBoxa,  # BOXA * boxas
                                    c_int,  # l_int32 sides
                                    c_int,  # l_int32 target
                                    c_int,  # l_int32 thresh
                                    ),
        'boxaAdjustHeightToTarget': (LPBoxa,  # BOXA *
                                     LPBoxa,  # BOXA * boxad
                                     LPBoxa,  # BOXA * boxas
                                     c_int,  # l_int32 sides
                                     c_int,  # l_int32 target
                                     c_int,  # l_int32 thresh
                                     ),
        'boxEqual': (c_int,
                     LPBox,  # BOX * box1
                     LPBox,  # BOX * box2
                     c_int_p,  # l_int32 * psame
                     ),
        'boxaEqual': (c_int,
                      LPBoxa,  # BOXA * boxa1
                      LPBoxa,  # BOXA * boxa2
                      c_int,  # l_int32 maxdist
                      LPLPNuma,  # NUMA ** pnaindex
                      c_int_p,  # l_int32 * psame
                      ),
        'boxSimilar': (c_int,
                       LPBox,  # BOX * box1
                       LPBox,  # BOX * box2
                       c_int,  # l_int32 leftdiff
                       c_int,  # l_int32 rightdiff
                       c_int,  # l_int32 topdiff
                       c_int,  # l_int32 botdiff
                       c_int_p,  # l_int32 * psimilar
                       ),
        'boxaSimilar': (c_int,
                        LPBoxa,  # BOXA * boxa1
                        LPBoxa,  # BOXA * boxa2
                        c_int,  # l_int32 leftdiff
                        c_int,  # l_int32 rightdiff
                        c_int,  # l_int32 topdiff
                        c_int,  # l_int32 botdiff
                        c_int,  # l_int32 debug
                        c_int_p,  # l_int32 * psimilar
                        LPLPNuma,  # NUMA ** pnasim
                        ),
        'boxaJoin': (c_int,
                     LPBoxa,  # BOXA * boxad
                     LPBoxa,  # BOXA * boxas
                     c_int,  # l_int32 istart
                     c_int,  # l_int32 iend
                     ),
        'boxaaJoin': (c_int,
                      LPBoxaa,  # BOXAA * baad
                      LPBoxaa,  # BOXAA * baas
                      c_int,  # l_int32 istart
                      c_int,  # l_int32 iend
                      ),
        'boxaSplitEvenOdd': (c_int,
                             LPBoxa,  # BOXA * boxa
                             c_int,  # l_int32 fillflag
                             LPLPBoxa,  # BOXA ** pboxae
                             LPLPBoxa,  # BOXA ** pboxao
                             ),
        'boxaMergeEvenOdd': (LPBoxa,  # BOXA *
                             LPBoxa,  # BOXA * boxae
                             LPBoxa,  # BOXA * boxao
                             c_int,  # l_int32 fillflag
                             ),
        'boxaTransform': (LPBoxa,  # BOXA *
                          LPBoxa,  # BOXA * boxas
                          c_int,  # l_int32 shiftx
                          c_int,  # l_int32 shifty
                          c_float,  # l_float32 scalex
                          c_float,  # l_float32 scaley
                          ),
        'boxTransform': (LPBox,  # BOX *
                         LPBox,  # BOX * box
                         c_int,  # l_int32 shiftx
                         c_int,  # l_int32 shifty
                         c_float,  # l_float32 scalex
                         c_float,  # l_float32 scaley
                         ),
        'boxaTransformOrdered': (LPBoxa,  # BOXA *
                                 LPBoxa,  # BOXA * boxas
                                 c_int,  # l_int32 shiftx
                                 c_int,  # l_int32 shifty
                                 c_float,  # l_float32 scalex
                                 c_float,  # l_float32 scaley
                                 c_int,  # l_int32 xcen
                                 c_int,  # l_int32 ycen
                                 c_float,  # l_float32 angle
                                 c_int,  # l_int32 order
                                 ),
        'boxTransformOrdered': (LPBox,  # BOX *
                                LPBox,  # BOX * boxs
                                c_int,  # l_int32 shiftx
                                c_int,  # l_int32 shifty
                                c_float,  # l_float32 scalex
                                c_float,  # l_float32 scaley
                                c_int,  # l_int32 xcen
                                c_int,  # l_int32 ycen
                                c_float,  # l_float32 angle
                                c_int,  # l_int32 order
                                ),
        'boxaRotateOrth': (LPBoxa,  # BOXA *
                           LPBoxa,  # BOXA * boxas
                           c_int,  # l_int32 w
                           c_int,  # l_int32 h
                           c_int,  # l_int32 rotation
                           ),
        'boxRotateOrth': (LPBox,  # BOX *
                          LPBox,  # BOX * box
                          c_int,  # l_int32 w
                          c_int,  # l_int32 h
                          c_int,  # l_int32 rotation
                          ),
        'boxaShiftWithPta': (LPBoxa,  # BOXA *
                             LPBoxa,  # BOXA * boxas
                             LPPta,  # PTA * pta
                             c_int,  # l_int32 dir
                             ),
        'boxaSort': (LPBoxa,  # BOXA *
                     LPBoxa,  # BOXA * boxas
                     c_int,  # l_int32 sorttype
                     c_int,  # l_int32 sortorder
                     LPLPNuma,  # NUMA ** pnaindex
                     ),
        'boxaBinSort': (LPBoxa,  # BOXA *
                        LPBoxa,  # BOXA * boxas
                        c_int,  # l_int32 sorttype
                        c_int,  # l_int32 sortorder
                        LPLPNuma,  # NUMA ** pnaindex
                        ),
        'boxaSortByIndex': (LPBoxa,  # BOXA *
                            LPBoxa,  # BOXA * boxas
                            LPNuma,  # NUMA * naindex
                            ),
        'boxaSort2d': (LPBoxaa,  # BOXAA *
                       LPBoxa,  # BOXA * boxas
                       LPLPNumaa,  # NUMAA ** pnaad
                       c_int,  # l_int32 delta1
                       c_int,  # l_int32 delta2
                       c_int,  # l_int32 minh1
                       ),
        'boxaSort2dByIndex': (LPBoxaa,  # BOXAA *
                              LPBoxa,  # BOXA * boxas
                              LPNumaa,  # NUMAA * naa
                              ),
        'boxaExtractAsNuma': (c_int,
                              LPBoxa,  # BOXA * boxa
                              LPLPNuma,  # NUMA ** pnal
                              LPLPNuma,  # NUMA ** pnat
                              LPLPNuma,  # NUMA ** pnar
                              LPLPNuma,  # NUMA ** pnab
                              LPLPNuma,  # NUMA ** pnaw
                              LPLPNuma,  # NUMA ** pnah
                              c_int,  # l_int32 keepinvalid
                              ),
        'boxaExtractAsPta': (c_int,
                             LPBoxa,  # BOXA * boxa
                             LPLPPta,  # PTA ** pptal
                             LPLPPta,  # PTA ** pptat
                             LPLPPta,  # PTA ** pptar
                             LPLPPta,  # PTA ** pptab
                             LPLPPta,  # PTA ** pptaw
                             LPLPPta,  # PTA ** pptah
                             c_int,  # l_int32 keepinvalid
                             ),
        'boxaExtractCorners': (LPPta,  # PTA *
                               LPBoxa,  # BOXA * boxa
                               c_int,  # l_int32 loc
                               ),
        'boxaGetRankVals': (c_int,
                            LPBoxa,  # BOXA * boxa
                            c_float,  # l_float32 fract
                            c_int_p,  # l_int32 * px
                            c_int_p,  # l_int32 * py
                            c_int_p,  # l_int32 * pr
                            c_int_p,  # l_int32 * pb
                            c_int_p,  # l_int32 * pw
                            c_int_p,  # l_int32 * ph
                            ),
        'boxaGetMedianVals': (c_int,
                              LPBoxa,  # BOXA * boxa
                              c_int_p,  # l_int32 * px
                              c_int_p,  # l_int32 * py
                              c_int_p,  # l_int32 * pr
                              c_int_p,  # l_int32 * pb
                              c_int_p,  # l_int32 * pw
                              c_int_p,  # l_int32 * ph
                              ),
        'boxaGetAverageSize': (c_int,
                               LPBoxa,  # BOXA * boxa
                               c_float_p,  # l_float32 * pw
                               c_float_p,  # l_float32 * ph
                               ),
        'boxaaGetExtent': (c_int,
                           LPBoxaa,  # BOXAA * baa
                           c_int_p,  # l_int32 * pw
                           c_int_p,  # l_int32 * ph
                           LPLPBox,  # BOX ** pbox
                           LPLPBoxa,  # BOXA ** pboxa
                           ),
        'boxaaFlattenToBoxa': (LPBoxa,  # BOXA *
                               LPBoxaa,  # BOXAA * baa
                               LPLPNuma,  # NUMA ** pnaindex
                               c_int,  # l_int32 copyflag
                               ),
        'boxaaFlattenAligned': (LPBoxa,  # BOXA *
                                LPBoxaa,  # BOXAA * baa
                                c_int,  # l_int32 num
                                LPBox,  # BOX * fillerbox
                                c_int,  # l_int32 copyflag
                                ),
        'boxaEncapsulateAligned': (LPBoxaa,  # BOXAA *
                                   LPBoxa,  # BOXA * boxa
                                   c_int,  # l_int32 num
                                   c_int,  # l_int32 copyflag
                                   ),
        'boxaaTranspose': (LPBoxaa,  # BOXAA *
                           LPBoxaa,  # BOXAA * baas
                           ),
        'boxaaAlignBox': (c_int,
                          LPBoxaa,  # BOXAA * baa
                          LPBox,  # BOX * box
                          c_int,  # l_int32 delta
                          c_int_p,  # l_int32 * pindex
                          ),
        'pixMaskConnComp': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 connectivity
                            LPLPBoxa,  # BOXA ** pboxa
                            ),
        'pixMaskBoxa': (LPPix,  # PIX *
                        LPPix,  # PIX * pixd
                        LPPix,  # PIX * pixs
                        LPBoxa,  # BOXA * boxa
                        c_int,  # l_int32 op
                        ),
        'pixPaintBoxa': (LPPix,  # PIX *
                         LPPix,  # PIX * pixs
                         LPBoxa,  # BOXA * boxa
                         c_uint,  # l_uint32 val
                         ),
        'pixSetBlackOrWhiteBoxa': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   LPBoxa,  # BOXA * boxa
                                   c_int,  # l_int32 op
                                   ),
        'pixPaintBoxaRandom': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               LPBoxa,  # BOXA * boxa
                               ),
        'pixBlendBoxaRandom': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               LPBoxa,  # BOXA * boxa
                               c_float,  # l_float32 fract
                               ),
        'pixDrawBoxa': (LPPix,  # PIX *
                        LPPix,  # PIX * pixs
                        LPBoxa,  # BOXA * boxa
                        c_int,  # l_int32 width
                        c_uint,  # l_uint32 val
                        ),
        'pixDrawBoxaRandom': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              LPBoxa,  # BOXA * boxa
                              c_int,  # l_int32 width
                              ),
        'boxaaDisplay': (LPPix,  # PIX *
                         LPPix,  # PIX * pixs
                         LPBoxaa,  # BOXAA * baa
                         c_int,  # l_int32 linewba
                         c_int,  # l_int32 linewb
                         c_uint,  # l_uint32 colorba
                         c_uint,  # l_uint32 colorb
                         c_int,  # l_int32 w
                         c_int,  # l_int32 h
                         ),
        'pixaDisplayBoxaa': (LPPixa,  # PIXA *
                             LPPixa,  # PIXA * pixas
                             LPBoxaa,  # BOXAA * baa
                             c_int,  # l_int32 colorflag
                             c_int,  # l_int32 width
                             ),
        'pixSplitIntoBoxa': (LPBoxa,  # BOXA *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 minsum
                             c_int,  # l_int32 skipdist
                             c_int,  # l_int32 delta
                             c_int,  # l_int32 maxbg
                             c_int,  # l_int32 maxcomps
                             c_int,  # l_int32 remainder
                             ),
        'pixSplitComponentIntoBoxa': (LPBoxa,  # BOXA *
                                      LPPix,  # PIX * pix
                                      LPBox,  # BOX * box
                                      c_int,  # l_int32 minsum
                                      c_int,  # l_int32 skipdist
                                      c_int,  # l_int32 delta
                                      c_int,  # l_int32 maxbg
                                      c_int,  # l_int32 maxcomps
                                      c_int,  # l_int32 remainder
                                      ),
        'makeMosaicStrips': (LPBoxa,  # BOXA *
                             c_int,  # l_int32 w
                             c_int,  # l_int32 h
                             c_int,  # l_int32 direction
                             c_int,  # l_int32 size
                             ),
        'boxaCompareRegions': (c_int,
                               LPBoxa,  # BOXA * boxa1
                               LPBoxa,  # BOXA * boxa2
                               c_int,  # l_int32 areathresh
                               c_int_p,  # l_int32 * pnsame
                               c_float_p,  # l_float32 * pdiffarea
                               c_float_p,  # l_float32 * pdiffxor
                               LPLPPix,  # PIX ** ppixdb
                               ),
        'pixSelectLargeULComp': (LPBox,  # BOX *
                                 LPPix,  # PIX * pixs
                                 c_float,  # l_float32 areaslop
                                 c_int,  # l_int32 yslop
                                 c_int,  # l_int32 connectivity
                                 ),
        'boxaSelectLargeULBox': (LPBox,  # BOX *
                                 LPBoxa,  # BOXA * boxas
                                 c_float,  # l_float32 areaslop
                                 c_int,  # l_int32 yslop
                                 ),
        'boxaSelectRange': (LPBoxa,  # BOXA *
                            LPBoxa,  # BOXA * boxas
                            c_int,  # l_int32 first
                            c_int,  # l_int32 last
                            c_int,  # l_int32 copyflag
                            ),
        'boxaaSelectRange': (LPBoxaa,  # BOXAA *
                             LPBoxaa,  # BOXAA * baas
                             c_int,  # l_int32 first
                             c_int,  # l_int32 last
                             c_int,  # l_int32 copyflag
                             ),
        'boxaSelectBySize': (LPBoxa,  # BOXA *
                             LPBoxa,  # BOXA * boxas
                             c_int,  # l_int32 width
                             c_int,  # l_int32 height
                             c_int,  # l_int32 type
                             c_int,  # l_int32 relation
                             c_int_p,  # l_int32 * pchanged
                             ),
        'boxaMakeSizeIndicator': (LPNuma,  # NUMA *
                                  LPBoxa,  # BOXA * boxa
                                  c_int,  # l_int32 width
                                  c_int,  # l_int32 height
                                  c_int,  # l_int32 type
                                  c_int,  # l_int32 relation
                                  ),
        'boxaSelectByArea': (LPBoxa,  # BOXA *
                             LPBoxa,  # BOXA * boxas
                             c_int,  # l_int32 area
                             c_int,  # l_int32 relation
                             c_int_p,  # l_int32 * pchanged
                             ),
        'boxaMakeAreaIndicator': (LPNuma,  # NUMA *
                                  LPBoxa,  # BOXA * boxa
                                  c_int,  # l_int32 area
                                  c_int,  # l_int32 relation
                                  ),
        'boxaSelectByWHRatio': (LPBoxa,  # BOXA *
                                LPBoxa,  # BOXA * boxas
                                c_float,  # l_float32 ratio
                                c_int,  # l_int32 relation
                                c_int_p,  # l_int32 * pchanged
                                ),
        'boxaMakeWHRatioIndicator': (LPNuma,  # NUMA *
                                     LPBoxa,  # BOXA * boxa
                                     c_float,  # l_float32 ratio
                                     c_int,  # l_int32 relation
                                     ),
        'boxaSelectWithIndicator': (LPBoxa,  # BOXA *
                                    LPBoxa,  # BOXA * boxas
                                    LPNuma,  # NUMA * na
                                    c_int_p,  # l_int32 * pchanged
                                    ),
        'boxaPermutePseudorandom': (LPBoxa,  # BOXA *
                                    LPBoxa,  # BOXA * boxas
                                    ),
        'boxaPermuteRandom': (LPBoxa,  # BOXA *
                              LPBoxa,  # BOXA * boxad
                              LPBoxa,  # BOXA * boxas
                              ),
        'boxaSwapBoxes': (c_int,
                          LPBoxa,  # BOXA * boxa
                          c_int,  # l_int32 i
                          c_int,  # l_int32 j
                          ),
        'boxaConvertToPta': (LPPta,  # PTA *
                             LPBoxa,  # BOXA * boxa
                             c_int,  # l_int32 ncorners
                             ),
        'ptaConvertToBoxa': (LPBoxa,  # BOXA *
                             LPPta,  # PTA * pta
                             c_int,  # l_int32 ncorners
                             ),
        'boxConvertToPta': (LPPta,  # PTA *
                            LPBox,  # BOX * box
                            c_int,  # l_int32 ncorners
                            ),
        'ptaConvertToBox': (LPBox,  # BOX *
                            LPPta,  # PTA * pta
                            ),
        'boxaGetExtent': (c_int,
                          LPBoxa,  # BOXA * boxa
                          c_int_p,  # l_int32 * pw
                          c_int_p,  # l_int32 * ph
                          LPLPBox,  # BOX ** pbox
                          ),
        'boxaGetCoverage': (c_int,
                            LPBoxa,  # BOXA * boxa
                            c_int,  # l_int32 wc
                            c_int,  # l_int32 hc
                            c_int,  # l_int32 exactflag
                            c_float_p,  # l_float32 * pfract
                            ),
        'boxaaSizeRange': (c_int,
                           LPBoxaa,  # BOXAA * baa
                           c_int_p,  # l_int32 * pminw
                           c_int_p,  # l_int32 * pminh
                           c_int_p,  # l_int32 * pmaxw
                           c_int_p,  # l_int32 * pmaxh
                           ),
        'boxaSizeRange': (c_int,
                          LPBoxa,  # BOXA * boxa
                          c_int_p,  # l_int32 * pminw
                          c_int_p,  # l_int32 * pminh
                          c_int_p,  # l_int32 * pmaxw
                          c_int_p,  # l_int32 * pmaxh
                          ),
        'boxaLocationRange': (c_int,
                              LPBoxa,  # BOXA * boxa
                              c_int_p,  # l_int32 * pminx
                              c_int_p,  # l_int32 * pminy
                              c_int_p,  # l_int32 * pmaxx
                              c_int_p,  # l_int32 * pmaxy
                              ),
        'boxaGetSizes': (c_int,
                         LPBoxa,  # BOXA * boxa
                         LPLPNuma,  # NUMA ** pnaw
                         LPLPNuma,  # NUMA ** pnah
                         ),
        'boxaGetArea': (c_int,
                        LPBoxa,  # BOXA * boxa
                        c_int_p,  # l_int32 * parea
                        ),
        'boxaDisplayTiled': (LPPix,  # PIX *
                             LPBoxa,  # BOXA * boxas
                             LPPixa,  # PIXA * pixa
                             c_int,  # l_int32 first
                             c_int,  # l_int32 last
                             c_int,  # l_int32 maxwidth
                             c_int,  # l_int32 linewidth
                             c_float,  # l_float32 scalefactor
                             c_int,  # l_int32 background
                             c_int,  # l_int32 spacing
                             c_int,  # l_int32 border
                             ),
        'boxaSmoothSequenceMedian': (LPBoxa,  # BOXA *
                                     LPBoxa,  # BOXA * boxas
                                     c_int,  # l_int32 halfwin
                                     c_int,  # l_int32 subflag
                                     c_int,  # l_int32 maxdiff
                                     c_int,  # l_int32 extrapixels
                                     c_int,  # l_int32 debug
                                     ),
        'boxaWindowedMedian': (LPBoxa,  # BOXA *
                               LPBoxa,  # BOXA * boxas
                               c_int,  # l_int32 halfwin
                               c_int,  # l_int32 debug
                               ),
        'boxaModifyWithBoxa': (LPBoxa,  # BOXA *
                               LPBoxa,  # BOXA * boxas
                               LPBoxa,  # BOXA * boxam
                               c_int,  # l_int32 subflag
                               c_int,  # l_int32 maxdiff
                               c_int,  # l_int32 extrapixels
                               ),
        'boxaReconcilePairWidth': (LPBoxa,  # BOXA *
                                   LPBoxa,  # BOXA * boxas
                                   c_int,  # l_int32 delw
                                   c_int,  # l_int32 op
                                   c_float,  # l_float32 factor
                                   LPNuma,  # NUMA * na
                                   ),
        'boxaSizeConsistency': (c_int,
                                LPBoxa,  # BOXA * boxas
                                c_int,  # l_int32 type
                                c_float,  # l_float32 threshp
                                c_float,  # l_float32 threshm
                                c_float_p,  # l_float32 * pfvarp
                                c_float_p,  # l_float32 * pfvarm
                                c_int_p,  # l_int32 * psame
                                ),
        'boxaReconcileAllByMedian': (LPBoxa,  # BOXA *
                                     LPBoxa,  # BOXA * boxas
                                     c_int,  # l_int32 select1
                                     c_int,  # l_int32 select2
                                     c_int,  # l_int32 thresh
                                     c_int,  # l_int32 extra
                                     LPPixa,  # PIXA * pixadb
                                     ),
        'boxaReconcileSidesByMedian': (LPBoxa,  # BOXA *
                                       LPBoxa,  # BOXA * boxas
                                       c_int,  # l_int32 select
                                       c_int,  # l_int32 thresh
                                       c_int,  # l_int32 extra
                                       LPPixa,  # PIXA * pixadb
                                       ),
        'boxaReconcileSizeByMedian': (LPBoxa,  # BOXA *
                                      LPBoxa,  # BOXA * boxas
                                      c_int,  # l_int32 type
                                      c_float,  # l_float32 dfract
                                      c_float,  # l_float32 sfract
                                      c_float,  # l_float32 factor
                                      LPLPNuma,  # NUMA ** pnadelw
                                      LPLPNuma,  # NUMA ** pnadelh
                                      # l_float32 * pratiowh
                                      c_float_p,
                                      ),
        'boxaPlotSides': (c_int,
                          LPBoxa,  # BOXA * boxa
                          c_char_p,  # const char * plotname
                          LPLPNuma,  # NUMA ** pnal
                          LPLPNuma,  # NUMA ** pnat
                          LPLPNuma,  # NUMA ** pnar
                          LPLPNuma,  # NUMA ** pnab
                          LPLPPix,  # PIX ** ppixd
                          ),
        'boxaPlotSizes': (c_int,
                          LPBoxa,  # BOXA * boxa
                          c_char_p,  # const char * plotname
                          LPLPNuma,  # NUMA ** pnaw
                          LPLPNuma,  # NUMA ** pnah
                          LPLPPix,  # PIX ** ppixd
                          ),
        'boxaFillSequence': (LPBoxa,  # BOXA *
                             LPBoxa,  # BOXA * boxas
                             c_int,  # l_int32 useflag
                             c_int,  # l_int32 debug
                             ),
        'boxaSizeVariation': (c_int,
                              LPBoxa,  # BOXA * boxa
                              c_int,  # l_int32 type
                              c_float_p,  # l_float32 * pdel_evenodd
                              c_float_p,  # l_float32 * prms_even
                              c_float_p,  # l_float32 * prms_odd
                              c_float_p,  # l_float32 * prms_all
                              ),
        'boxaMedianDimensions': (c_int,
                                 LPBoxa,  # BOXA * boxas
                                 c_int_p,  # l_int32 * pmedw
                                 c_int_p,  # l_int32 * pmedh
                                 c_int_p,  # l_int32 * pmedwe
                                 c_int_p,  # l_int32 * pmedwo
                                 c_int_p,  # l_int32 * pmedhe
                                 c_int_p,  # l_int32 * pmedho
                                 LPLPNuma,  # NUMA ** pnadelw
                                 LPLPNuma,  # NUMA ** pnadelh
                                 ),
        'pixGetOuterBordersPtaa': (LPPtaa,  # PTAA *
                                   LPPix,  # PIX * pixs
                                   ),
        'getCutPathForHole': (LPPta,  # PTA *
                              LPPix,  # PIX * pix
                              LPPta,  # PTA * pta
                              LPBox,  # BOX * boxinner
                              c_int_p,  # l_int32 * pdir
                              c_int_p,  # l_int32 * plen
                              ),
        'pixaThinConnected': (LPPixa,  # PIXA *
                              LPPixa,  # PIXA * pixas
                              c_int,  # l_int32 type
                              c_int,  # l_int32 connectivity
                              c_int,  # l_int32 maxiters
                              ),
        'pixThinConnected': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 type
                             c_int,  # l_int32 connectivity
                             c_int,  # l_int32 maxiters
                             ),
        'pixFindCheckerboardCorners': (c_int,
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 size
                                       c_int,  # l_int32 dilation
                                       c_int,  # l_int32 nsels
                                       LPLPPix,  # PIX ** ppix_corners
                                       LPLPPta,  # PTA ** ppta_corners
                                       LPPixa,  # PIXA * pixadb
                                       ),
        'jbCorrelation': (c_int,
                          c_char_p,  # const char * dirin
                          c_float,  # l_float32 thresh
                          c_float,  # l_float32 weight
                          c_int,  # l_int32 components
                          c_char_p,  # const char * rootname
                          c_int,  # l_int32 firstpage
                          c_int,  # l_int32 npages
                          c_int,  # l_int32 renderflag
                          ),
        'jbRankHaus': (c_int,
                       c_char_p,  # const char * dirin
                       c_int,  # l_int32 size
                       c_float,  # l_float32 rank
                       c_int,  # l_int32 components
                       c_char_p,  # const char * rootname
                       c_int,  # l_int32 firstpage
                       c_int,  # l_int32 npages
                       c_int,  # l_int32 renderflag
                       ),
        'pixGetWordsInTextlines': (c_int,
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 minwidth
                                   c_int,  # l_int32 minheight
                                   c_int,  # l_int32 maxwidth
                                   c_int,  # l_int32 maxheight
                                   LPLPBoxa,  # BOXA ** pboxad
                                   LPLPPixa,  # PIXA ** ppixad
                                   LPLPNuma,  # NUMA ** pnai
                                   ),
        'pixGetWordBoxesInTextlines': (c_int,
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 minwidth
                                       c_int,  # l_int32 minheight
                                       c_int,  # l_int32 maxwidth
                                       c_int,  # l_int32 maxheight
                                       LPLPBoxa,  # BOXA ** pboxad
                                       LPLPNuma,  # NUMA ** pnai
                                       ),
        'pixFindWordAndCharacterBoxes': (c_int,
                                         LPPix,  # PIX * pixs
                                         LPBox,  # BOX * boxs
                                         c_int,  # l_int32 thresh
                                         LPLPBoxa,  # BOXA ** pboxaw
                                         # BOXAA ** pboxaac
                                         LPLPBoxaa,
                                         c_char_p,  # const char * debugdir
                                         ),
        'boxaExtractSortedPattern': (LPNumaa,  # NUMAA *
                                     LPBoxa,  # BOXA * boxa
                                     LPNuma,  # NUMA * na
                                     ),
        'numaaCompareImagesByBoxes': (c_int,
                                      LPNumaa,  # NUMAA * naa1
                                      LPNumaa,  # NUMAA * naa2
                                      c_int,  # l_int32 nperline
                                      c_int,  # l_int32 nreq
                                      c_int,  # l_int32 maxshiftx
                                      c_int,  # l_int32 maxshifty
                                      c_int,  # l_int32 delx
                                      c_int,  # l_int32 dely
                                      c_int_p,  # l_int32 * psame
                                      c_int,  # l_int32 debugflag
                                      ),
        'pixColorContent': (c_int,
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 rref
                            c_int,  # l_int32 gref
                            c_int,  # l_int32 bref
                            c_int,  # l_int32 mingray
                            LPLPPix,  # PIX ** ppixr
                            LPLPPix,  # PIX ** ppixg
                            LPLPPix,  # PIX ** ppixb
                            ),
        'pixColorMagnitude': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 rref
                              c_int,  # l_int32 gref
                              c_int,  # l_int32 bref
                              c_int,  # l_int32 type
                              ),
        'pixColorFraction': (c_int,
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 darkthresh
                             c_int,  # l_int32 lightthresh
                             c_int,  # l_int32 diffthresh
                             c_int,  # l_int32 factor
                             c_float_p,  # l_float32 * ppixfract
                             c_float_p,  # l_float32 * pcolorfract
                             ),
        'pixColorShiftWhitePoint': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 rref
                                    c_int,  # l_int32 gref
                                    c_int,  # l_int32 bref
                                    ),
        'pixMaskOverColorPixels': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 threshdiff
                                   c_int,  # l_int32 mindist
                                   ),
        'pixMaskOverGrayPixels': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 maxlimit
                                  c_int,  # l_int32 satlimit
                                  ),
        'pixMaskOverColorRange': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 rmin
                                  c_int,  # l_int32 rmax
                                  c_int,  # l_int32 gmin
                                  c_int,  # l_int32 gmax
                                  c_int,  # l_int32 bmin
                                  c_int,  # l_int32 bmax
                                  ),
        'pixFindColorRegions': (c_int,
                                LPPix,  # PIX * pixs
                                LPPix,  # PIX * pixm
                                c_int,  # l_int32 factor
                                c_int,  # l_int32 lightthresh
                                c_int,  # l_int32 darkthresh
                                c_int,  # l_int32 mindiff
                                c_int,  # l_int32 colordiff
                                c_float,  # l_float32 edgefract
                                c_float_p,  # l_float32 * pcolorfract
                                LPLPPix,  # PIX ** pcolormask1
                                LPLPPix,  # PIX ** pcolormask2
                                LPPixa,  # PIXA * pixadb
                                ),
        'pixNumSignificantGrayColors': (c_int,
                                        LPPix,  # PIX * pixs
                                        c_int,  # l_int32 darkthresh
                                        c_int,  # l_int32 lightthresh
                                        c_float,  # l_float32 minfract
                                        c_int,  # l_int32 factor
                                        c_int_p,  # l_int32 * pncolors
                                        ),
        'pixColorsForQuantization': (c_int,
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 thresh
                                     c_int_p,  # l_int32 * pncolors
                                     c_int_p,  # l_int32 * piscolor
                                     c_int,  # l_int32 debug
                                     ),
        'pixNumColors': (c_int,
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 factor
                         c_int_p,  # l_int32 * pncolors
                         ),
        'pixConvertRGBToCmapLossless': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixs
                                        ),
        'pixGetMostPopulatedColors': (c_int,
                                      LPPix,  # PIX * pixs
                                      c_int,  # l_int32 sigbits
                                      c_int,  # l_int32 factor
                                      c_int,  # l_int32 ncolors
                                      # l_uint32 ** parray
                                      POINTER(c_uint_p),
                                      # PIXCMAP ** pcmap
                                      LPLPPixColormap,
                                      ),
        'pixSimpleColorQuantize': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 sigbits
                                   c_int,  # l_int32 factor
                                   c_int,  # l_int32 ncolors
                                   ),
        'pixGetRGBHistogram': (LPNuma,  # NUMA *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 sigbits
                               c_int,  # l_int32 factor
                               ),
        'makeRGBIndexTables': (c_int,
                               POINTER(c_uint_p),  # l_uint32 ** prtab
                               POINTER(c_uint_p),  # l_uint32 ** pgtab
                               POINTER(c_uint_p),  # l_uint32 ** pbtab
                               c_int,  # l_int32 sigbits
                               ),
        'getRGBFromIndex': (c_int,
                            c_uint,  # l_uint32 index
                            c_int,  # l_int32 sigbits
                            c_int_p,  # l_int32 * prval
                            c_int_p,  # l_int32 * pgval
                            c_int_p,  # l_int32 * pbval
                            ),
        'pixHasHighlightRed': (c_int,
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 factor
                               c_float,  # l_float32 minfract
                               c_float,  # l_float32 fthresh
                               c_int_p,  # l_int32 * phasred
                               c_float_p,  # l_float32 * pratio
                               LPLPPix,  # PIX ** ppixdb
                               ),
        'pixColorFill': (LPPix,  # PIX *
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 minmax
                         c_int,  # l_int32 maxdiff
                         c_int,  # l_int32 smooth
                         c_int,  # l_int32 minarea
                         c_int,  # l_int32 debug
                         ),
        'makeColorfillTestData': (LPPixa,  # PIXA *
                                  c_int,  # l_int32 w
                                  c_int,  # l_int32 h
                                  c_int,  # l_int32 nseeds
                                  c_int,  # l_int32 range
                                  ),
        'pixColorGrayRegions': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                LPBoxa,  # BOXA * boxa
                                c_int,  # l_int32 type
                                c_int,  # l_int32 thresh
                                c_int,  # l_int32 rval
                                c_int,  # l_int32 gval
                                c_int,  # l_int32 bval
                                ),
        'pixColorGray': (c_int,
                         LPPix,  # PIX * pixs
                         LPBox,  # BOX * box
                         c_int,  # l_int32 type
                         c_int,  # l_int32 thresh
                         c_int,  # l_int32 rval
                         c_int,  # l_int32 gval
                         c_int,  # l_int32 bval
                         ),
        'pixColorGrayMasked': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               LPPix,  # PIX * pixm
                               c_int,  # l_int32 type
                               c_int,  # l_int32 thresh
                               c_int,  # l_int32 rval
                               c_int,  # l_int32 gval
                               c_int,  # l_int32 bval
                               ),
        'pixSnapColor': (LPPix,  # PIX *
                         LPPix,  # PIX * pixd
                         LPPix,  # PIX * pixs
                         c_uint,  # l_uint32 srcval
                         c_uint,  # l_uint32 dstval
                         c_int,  # l_int32 diff
                         ),
        'pixSnapColorCmap': (LPPix,  # PIX *
                             LPPix,  # PIX * pixd
                             LPPix,  # PIX * pixs
                             c_uint,  # l_uint32 srcval
                             c_uint,  # l_uint32 dstval
                             c_int,  # l_int32 diff
                             ),
        'pixLinearMapToTargetColor': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixd
                                      LPPix,  # PIX * pixs
                                      c_uint,  # l_uint32 srcval
                                      c_uint,  # l_uint32 dstval
                                      ),
        'pixelLinearMapToTargetColor': (c_int,
                                        c_uint,  # l_uint32 scolor
                                        c_uint,  # l_uint32 srcmap
                                        c_uint,  # l_uint32 dstmap
                                        c_uint_p,  # l_uint32 * pdcolor
                                        ),
        'pixShiftByComponent': (LPPix,  # PIX *
                                LPPix,  # PIX * pixd
                                LPPix,  # PIX * pixs
                                c_uint,  # l_uint32 srcval
                                c_uint,  # l_uint32 dstval
                                ),
        'pixelShiftByComponent': (c_int,
                                  c_int,  # l_int32 rval
                                  c_int,  # l_int32 gval
                                  c_int,  # l_int32 bval
                                  c_uint,  # l_uint32 srcval
                                  c_uint,  # l_uint32 dstval
                                  c_uint_p,  # l_uint32 * ppixel
                                  ),
        'pixelFractionalShift': (c_int,
                                 c_int,  # l_int32 rval
                                 c_int,  # l_int32 gval
                                 c_int,  # l_int32 bval
                                 c_float,  # l_float32 fract
                                 c_uint_p,  # l_uint32 * ppixel
                                 ),
        'pixMapWithInvariantHue': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixd
                                   LPPix,  # PIX * pixs
                                   c_uint,  # l_uint32 srcval
                                   c_float,  # l_float32 fract
                                   ),
        'pixcmapCreate': (LPPixColormap,  # PIXCMAP *
                          c_int,  # l_int32 depth
                          ),
        'pixcmapCreateRandom': (LPPixColormap,  # PIXCMAP *
                                c_int,  # l_int32 depth
                                c_int,  # l_int32 hasblack
                                c_int,  # l_int32 haswhite
                                ),
        'pixcmapCreateLinear': (LPPixColormap,  # PIXCMAP *
                                c_int,  # l_int32 d
                                c_int,  # l_int32 nlevels
                                ),
        'pixcmapCopy': (LPPixColormap,  # PIXCMAP *
                        LPPixColormap,  # const PIXCMAP * cmaps
                        ),
        'pixcmapDestroy': (None,
                           LPLPPixColormap,  # PIXCMAP ** pcmap
                           ),
        'pixcmapIsValid': (c_int,
                           LPPixColormap,  # const PIXCMAP * cmap
                           LPPix,  # PIX * pix
                           c_int_p,  # l_int32 * pvalid
                           ),
        'pixcmapAddColor': (c_int,
                            LPPixColormap,  # PIXCMAP * cmap
                            c_int,  # l_int32 rval
                            c_int,  # l_int32 gval
                            c_int,  # l_int32 bval
                            ),
        'pixcmapAddRGBA': (c_int,
                           LPPixColormap,  # PIXCMAP * cmap
                           c_int,  # l_int32 rval
                           c_int,  # l_int32 gval
                           c_int,  # l_int32 bval
                           c_int,  # l_int32 aval
                           ),
        'pixcmapAddNewColor': (c_int,
                               LPPixColormap,  # PIXCMAP * cmap
                               c_int,  # l_int32 rval
                               c_int,  # l_int32 gval
                               c_int,  # l_int32 bval
                               c_int_p,  # l_int32 * pindex
                               ),
        'pixcmapAddNearestColor': (c_int,
                                   LPPixColormap,  # PIXCMAP * cmap
                                   c_int,  # l_int32 rval
                                   c_int,  # l_int32 gval
                                   c_int,  # l_int32 bval
                                   c_int_p,  # l_int32 * pindex
                                   ),
        'pixcmapUsableColor': (c_int,
                               LPPixColormap,  # PIXCMAP * cmap
                               c_int,  # l_int32 rval
                               c_int,  # l_int32 gval
                               c_int,  # l_int32 bval
                               c_int_p,  # l_int32 * pusable
                               ),
        'pixcmapAddBlackOrWhite': (c_int,
                                   LPPixColormap,  # PIXCMAP * cmap
                                   c_int,  # l_int32 color
                                   c_int_p,  # l_int32 * pindex
                                   ),
        'pixcmapSetBlackAndWhite': (c_int,
                                    LPPixColormap,  # PIXCMAP * cmap
                                    c_int,  # l_int32 setblack
                                    c_int,  # l_int32 setwhite
                                    ),
        'pixcmapGetCount': (c_int,
                            LPPixColormap,  # const PIXCMAP * cmap
                            ),
        'pixcmapGetFreeCount': (c_int,
                                LPPixColormap,  # PIXCMAP * cmap
                                ),
        'pixcmapGetDepth': (c_int,
                            LPPixColormap,  # PIXCMAP * cmap
                            ),
        'pixcmapGetMinDepth': (c_int,
                               LPPixColormap,  # PIXCMAP * cmap
                               c_int_p,  # l_int32 * pmindepth
                               ),
        'pixcmapClear': (c_int,
                         LPPixColormap,  # PIXCMAP * cmap
                         ),
        'pixcmapGetColor': (c_int,
                            LPPixColormap,  # PIXCMAP * cmap
                            c_int,  # l_int32 index
                            c_int_p,  # l_int32 * prval
                            c_int_p,  # l_int32 * pgval
                            c_int_p,  # l_int32 * pbval
                            ),
        'pixcmapGetColor32': (c_int,
                              LPPixColormap,  # PIXCMAP * cmap
                              c_int,  # l_int32 index
                              c_uint_p,  # l_uint32 * pval32
                              ),
        'pixcmapGetRGBA': (c_int,
                           LPPixColormap,  # PIXCMAP * cmap
                           c_int,  # l_int32 index
                           c_int_p,  # l_int32 * prval
                           c_int_p,  # l_int32 * pgval
                           c_int_p,  # l_int32 * pbval
                           c_int_p,  # l_int32 * paval
                           ),
        'pixcmapGetRGBA32': (c_int,
                             LPPixColormap,  # PIXCMAP * cmap
                             c_int,  # l_int32 index
                             c_uint_p,  # l_uint32 * pval32
                             ),
        'pixcmapResetColor': (c_int,
                              LPPixColormap,  # PIXCMAP * cmap
                              c_int,  # l_int32 index
                              c_int,  # l_int32 rval
                              c_int,  # l_int32 gval
                              c_int,  # l_int32 bval
                              ),
        'pixcmapSetAlpha': (c_int,
                            LPPixColormap,  # PIXCMAP * cmap
                            c_int,  # l_int32 index
                            c_int,  # l_int32 aval
                            ),
        'pixcmapGetIndex': (c_int,
                            LPPixColormap,  # PIXCMAP * cmap
                            c_int,  # l_int32 rval
                            c_int,  # l_int32 gval
                            c_int,  # l_int32 bval
                            c_int_p,  # l_int32 * pindex
                            ),
        'pixcmapHasColor': (c_int,
                            LPPixColormap,  # PIXCMAP * cmap
                            c_int_p,  # l_int32 * pcolor
                            ),
        'pixcmapIsOpaque': (c_int,
                            LPPixColormap,  # PIXCMAP * cmap
                            c_int_p,  # l_int32 * popaque
                            ),
        'pixcmapNonOpaqueColorsInfo': (c_int,
                                       LPPixColormap,  # PIXCMAP * cmap
                                       c_int_p,  # l_int32 * pntrans
                                       c_int_p,  # l_int32 * pmax_trans
                                       # l_int32 * pmin_opaque
                                       c_int_p,
                                       ),
        'pixcmapIsBlackAndWhite': (c_int,
                                   LPPixColormap,  # PIXCMAP * cmap
                                   c_int_p,  # l_int32 * pblackwhite
                                   ),
        'pixcmapCountGrayColors': (c_int,
                                   LPPixColormap,  # PIXCMAP * cmap
                                   c_int_p,  # l_int32 * pngray
                                   ),
        'pixcmapGetRankIntensity': (c_int,
                                    LPPixColormap,  # PIXCMAP * cmap
                                    c_float,  # l_float32 rankval
                                    c_int_p,  # l_int32 * pindex
                                    ),
        'pixcmapGetNearestIndex': (c_int,
                                   LPPixColormap,  # PIXCMAP * cmap
                                   c_int,  # l_int32 rval
                                   c_int,  # l_int32 gval
                                   c_int,  # l_int32 bval
                                   c_int_p,  # l_int32 * pindex
                                   ),
        'pixcmapGetNearestGrayIndex': (c_int,
                                       LPPixColormap,  # PIXCMAP * cmap
                                       c_int,  # l_int32 val
                                       c_int_p,  # l_int32 * pindex
                                       ),
        'pixcmapGetDistanceToColor': (c_int,
                                      LPPixColormap,  # PIXCMAP * cmap
                                      c_int,  # l_int32 index
                                      c_int,  # l_int32 rval
                                      c_int,  # l_int32 gval
                                      c_int,  # l_int32 bval
                                      c_int_p,  # l_int32 * pdist
                                      ),
        'pixcmapGetRangeValues': (c_int,
                                  LPPixColormap,  # PIXCMAP * cmap
                                  c_int,  # l_int32 select
                                  c_int_p,  # l_int32 * pminval
                                  c_int_p,  # l_int32 * pmaxval
                                  c_int_p,  # l_int32 * pminindex
                                  c_int_p,  # l_int32 * pmaxindex
                                  ),
        'pixcmapGrayToFalseColor': (LPPixColormap,  # PIXCMAP *
                                    c_float,  # l_float32 gamma
                                    ),
        'pixcmapGrayToColor': (LPPixColormap,  # PIXCMAP *
                               c_uint,  # l_uint32 color
                               ),
        'pixcmapColorToGray': (LPPixColormap,  # PIXCMAP *
                               LPPixColormap,  # PIXCMAP * cmaps
                               c_float,  # l_float32 rwt
                               c_float,  # l_float32 gwt
                               c_float,  # l_float32 bwt
                               ),
        'pixcmapConvertTo4': (LPPixColormap,  # PIXCMAP *
                              LPPixColormap,  # PIXCMAP * cmaps
                              ),
        'pixcmapConvertTo8': (LPPixColormap,  # PIXCMAP *
                              LPPixColormap,  # PIXCMAP * cmaps
                              ),
        'pixcmapRead': (LPPixColormap,  # PIXCMAP *
                        c_char_p,  # const char * filename
                        ),
        'pixcmapReadStream': (LPPixColormap,  # PIXCMAP *
                              LPFile,  # FILE * fp
                              ),
        'pixcmapReadMem': (LPPixColormap,  # PIXCMAP *
                           c_ubyte_p,  # const l_uint8 * data
                           c_size_t,  # size_t size
                           ),
        'pixcmapWrite': (c_int,
                         c_char_p,  # const char * filename
                         LPPixColormap,  # const PIXCMAP * cmap
                         ),
        'pixcmapWriteStream': (c_int,
                               LPFile,  # FILE * fp
                               LPPixColormap,  # const PIXCMAP * cmap
                               ),
        'pixcmapWriteMem': (c_int,
                            POINTER(c_ubyte_p),  # l_uint8 ** pdata
                            c_size_t_p,  # size_t * psize
                            LPPixColormap,  # const PIXCMAP * cmap
                            ),
        'pixcmapToArrays': (c_int,
                            LPPixColormap,  # const PIXCMAP * cmap
                            POINTER(c_int_p),  # l_int32 ** prmap
                            POINTER(c_int_p),  # l_int32 ** pgmap
                            POINTER(c_int_p),  # l_int32 ** pbmap
                            POINTER(c_int_p),  # l_int32 ** pamap
                            ),
        'pixcmapToRGBTable': (c_int,
                              LPPixColormap,  # PIXCMAP * cmap
                              POINTER(c_uint_p),  # l_uint32 ** ptab
                              c_int_p,  # l_int32 * pncolors
                              ),
        'pixcmapSerializeToMemory': (c_int,
                                     LPPixColormap,  # PIXCMAP * cmap
                                     c_int,  # l_int32 cpc
                                     c_int_p,  # l_int32 * pncolors
                                     # l_uint8 ** pdata
                                     POINTER(c_ubyte_p),
                                     ),
        'pixcmapDeserializeFromMemory': (LPPixColormap,  # PIXCMAP *
                                         c_ubyte_p,  # l_uint8 * data
                                         c_int,  # l_int32 cpc
                                         c_int,  # l_int32 ncolors
                                         ),
        'pixcmapConvertToHex': (c_char_p,
                                c_ubyte_p,  # l_uint8 * data
                                c_int,  # l_int32 ncolors
                                ),
        'pixcmapGammaTRC': (c_int,
                            LPPixColormap,  # PIXCMAP * cmap
                            c_float,  # l_float32 gamma
                            c_int,  # l_int32 minval
                            c_int,  # l_int32 maxval
                            ),
        'pixcmapContrastTRC': (c_int,
                               LPPixColormap,  # PIXCMAP * cmap
                               c_float,  # l_float32 factor
                               ),
        'pixcmapShiftIntensity': (c_int,
                                  LPPixColormap,  # PIXCMAP * cmap
                                  c_float,  # l_float32 fraction
                                  ),
        'pixcmapShiftByComponent': (c_int,
                                    LPPixColormap,  # PIXCMAP * cmap
                                    c_uint,  # l_uint32 srcval
                                    c_uint,  # l_uint32 dstval
                                    ),
        'pixColorMorph': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 type
                          c_int,  # l_int32 hsize
                          c_int,  # l_int32 vsize
                          ),
        'pixOctreeColorQuant': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 colors
                                c_int,  # l_int32 ditherflag
                                ),
        'pixOctreeColorQuantGeneral': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 colors
                                       c_int,  # l_int32 ditherflag
                                       c_float,  # l_float32 validthresh
                                       c_float,  # l_float32 colorthresh
                                       ),
        'makeRGBToIndexTables': (c_int,
                                 c_int,  # l_int32 cqlevels
                                 # l_uint32 ** prtab
                                 POINTER(c_uint_p),
                                 # l_uint32 ** pgtab
                                 POINTER(c_uint_p),
                                 # l_uint32 ** pbtab
                                 POINTER(c_uint_p),
                                 ),
        'getOctcubeIndexFromRGB': (None,
                                   c_int,  # l_int32 rval
                                   c_int,  # l_int32 gval
                                   c_int,  # l_int32 bval
                                   c_uint_p,  # l_uint32 * rtab
                                   c_uint_p,  # l_uint32 * gtab
                                   c_uint_p,  # l_uint32 * btab
                                   c_uint_p,  # l_uint32 * pindex
                                   ),
        'pixOctreeQuantByPopulation': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 level
                                       c_int,  # l_int32 ditherflag
                                       ),
        'pixOctreeQuantNumColors': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 maxcolors
                                    c_int,  # l_int32 subsample
                                    ),
        'pixOctcubeQuantMixedWithGray': (LPPix,  # PIX *
                                         LPPix,  # PIX * pixs
                                         c_int,  # l_int32 depth
                                         c_int,  # l_int32 graylevels
                                         c_int,  # l_int32 delta
                                         ),
        'pixFixedOctcubeQuant256': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 ditherflag
                                    ),
        'pixFewColorsOctcubeQuant1': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      c_int,  # l_int32 level
                                      ),
        'pixFewColorsOctcubeQuant2': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      c_int,  # l_int32 level
                                      LPNuma,  # NUMA * na
                                      c_int,  # l_int32 ncolors
                                      c_int_p,  # l_int32 * pnerrors
                                      ),
        'pixFewColorsOctcubeQuantMixed': (LPPix,  # PIX *
                                          LPPix,  # PIX * pixs
                                          c_int,  # l_int32 level
                                          c_int,  # l_int32 darkthresh
                                          c_int,  # l_int32 lightthresh
                                          c_int,  # l_int32 diffthresh
                                          c_float,  # l_float32 minfract
                                          c_int,  # l_int32 maxspan
                                          ),
        'pixFixedOctcubeQuantGenRGB': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 level
                                       ),
        'pixQuantFromCmap': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             LPPixColormap,  # PIXCMAP * cmap
                             c_int,  # l_int32 mindepth
                             c_int,  # l_int32 level
                             c_int,  # l_int32 metric
                             ),
        'pixOctcubeQuantFromCmap': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    LPPixColormap,  # PIXCMAP * cmap
                                    c_int,  # l_int32 mindepth
                                    c_int,  # l_int32 level
                                    c_int,  # l_int32 metric
                                    ),
        'pixOctcubeHistogram': (LPNuma,  # NUMA *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 level
                                c_int_p,  # l_int32 * pncolors
                                ),
        'pixcmapToOctcubeLUT': (c_int_p,
                                LPPixColormap,  # PIXCMAP * cmap
                                c_int,  # l_int32 level
                                c_int,  # l_int32 metric
                                ),
        'pixRemoveUnusedColors': (c_int,
                                  LPPix,  # PIX * pixs
                                  ),
        'pixNumberOccupiedOctcubes': (c_int,
                                      LPPix,  # PIX * pix
                                      c_int,  # l_int32 level
                                      c_int,  # l_int32 mincount
                                      c_float,  # l_float32 minfract
                                      c_int_p,  # l_int32 * pncolors
                                      ),
        'pixMedianCutQuant': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 ditherflag
                              ),
        'pixMedianCutQuantGeneral': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 ditherflag
                                     c_int,  # l_int32 outdepth
                                     c_int,  # l_int32 maxcolors
                                     c_int,  # l_int32 sigbits
                                     c_int,  # l_int32 maxsub
                                     c_int,  # l_int32 checkbw
                                     ),
        'pixMedianCutQuantMixed': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 ncolor
                                   c_int,  # l_int32 ngray
                                   c_int,  # l_int32 darkthresh
                                   c_int,  # l_int32 lightthresh
                                   c_int,  # l_int32 diffthresh
                                   ),
        'pixFewColorsMedianCutQuantMixed': (LPPix,  # PIX *
                                            LPPix,  # PIX * pixs
                                            c_int,  # l_int32 ncolor
                                            c_int,  # l_int32 ngray
                                            c_int,  # l_int32 maxncolors
                                            c_int,  # l_int32 darkthresh
                                            c_int,  # l_int32 lightthresh
                                            c_int,  # l_int32 diffthresh
                                            ),
        'pixMedianCutHisto': (c_int_p,
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 sigbits
                              c_int,  # l_int32 subsample
                              ),
        'pixColorSegment': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 maxdist
                            c_int,  # l_int32 maxcolors
                            c_int,  # l_int32 selsize
                            c_int,  # l_int32 finalcolors
                            c_int,  # l_int32 debugflag
                            ),
        'pixColorSegmentCluster': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 maxdist
                                   c_int,  # l_int32 maxcolors
                                   c_int,  # l_int32 debugflag
                                   ),
        'pixAssignToNearestColor': (c_int,
                                    LPPix,  # PIX * pixd
                                    LPPix,  # PIX * pixs
                                    LPPix,  # PIX * pixm
                                    c_int,  # l_int32 level
                                    c_int_p,  # l_int32 * countarray
                                    ),
        'pixColorSegmentClean': (c_int,
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 selsize
                                 c_int_p,  # l_int32 * countarray
                                 ),
        'pixColorSegmentRemoveColors': (c_int,
                                        LPPix,  # PIX * pixd
                                        LPPix,  # PIX * pixs
                                        c_int,  # l_int32 finalcolors
                                        ),
        'pixConvertRGBToHSV': (LPPix,  # PIX *
                               LPPix,  # PIX * pixd
                               LPPix,  # PIX * pixs
                               ),
        'pixConvertHSVToRGB': (LPPix,  # PIX *
                               LPPix,  # PIX * pixd
                               LPPix,  # PIX * pixs
                               ),
        'convertRGBToHSV': (c_int,
                            c_int,  # l_int32 rval
                            c_int,  # l_int32 gval
                            c_int,  # l_int32 bval
                            c_int_p,  # l_int32 * phval
                            c_int_p,  # l_int32 * psval
                            c_int_p,  # l_int32 * pvval
                            ),
        'convertHSVToRGB': (c_int,
                            c_int,  # l_int32 hval
                            c_int,  # l_int32 sval
                            c_int,  # l_int32 vval
                            c_int_p,  # l_int32 * prval
                            c_int_p,  # l_int32 * pgval
                            c_int_p,  # l_int32 * pbval
                            ),
        'pixcmapConvertRGBToHSV': (c_int,
                                   LPPixColormap,  # PIXCMAP * cmap
                                   ),
        'pixcmapConvertHSVToRGB': (c_int,
                                   LPPixColormap,  # PIXCMAP * cmap
                                   ),
        'pixConvertRGBToHue': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               ),
        'pixConvertRGBToSaturation': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      ),
        'pixConvertRGBToValue': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 ),
        'pixMakeRangeMaskHS': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 huecenter
                               c_int,  # l_int32 huehw
                               c_int,  # l_int32 satcenter
                               c_int,  # l_int32 sathw
                               c_int,  # l_int32 regionflag
                               ),
        'pixMakeRangeMaskHV': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 huecenter
                               c_int,  # l_int32 huehw
                               c_int,  # l_int32 valcenter
                               c_int,  # l_int32 valhw
                               c_int,  # l_int32 regionflag
                               ),
        'pixMakeRangeMaskSV': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 satcenter
                               c_int,  # l_int32 sathw
                               c_int,  # l_int32 valcenter
                               c_int,  # l_int32 valhw
                               c_int,  # l_int32 regionflag
                               ),
        'pixMakeHistoHS': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 factor
                           LPLPNuma,  # NUMA ** pnahue
                           LPLPNuma,  # NUMA ** pnasat
                           ),
        'pixMakeHistoHV': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 factor
                           LPLPNuma,  # NUMA ** pnahue
                           LPLPNuma,  # NUMA ** pnaval
                           ),
        'pixMakeHistoSV': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 factor
                           LPLPNuma,  # NUMA ** pnasat
                           LPLPNuma,  # NUMA ** pnaval
                           ),
        'pixFindHistoPeaksHSV': (c_int,
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 type
                                 c_int,  # l_int32 width
                                 c_int,  # l_int32 height
                                 c_int,  # l_int32 npeaks
                                 c_float,  # l_float32 erasefactor
                                 LPLPPta,  # PTA ** ppta
                                 LPLPNuma,  # NUMA ** pnatot
                                 LPLPPixa,  # PIXA ** ppixa
                                 ),
        'displayHSVColorRange': (LPPix,  # PIX *
                                 c_int,  # l_int32 hval
                                 c_int,  # l_int32 sval
                                 c_int,  # l_int32 vval
                                 c_int,  # l_int32 huehw
                                 c_int,  # l_int32 sathw
                                 c_int,  # l_int32 nsamp
                                 c_int,  # l_int32 factor
                                 ),
        'pixConvertRGBToYUV': (LPPix,  # PIX *
                               LPPix,  # PIX * pixd
                               LPPix,  # PIX * pixs
                               ),
        'pixConvertYUVToRGB': (LPPix,  # PIX *
                               LPPix,  # PIX * pixd
                               LPPix,  # PIX * pixs
                               ),
        'convertRGBToYUV': (c_int,
                            c_int,  # l_int32 rval
                            c_int,  # l_int32 gval
                            c_int,  # l_int32 bval
                            c_int_p,  # l_int32 * pyval
                            c_int_p,  # l_int32 * puval
                            c_int_p,  # l_int32 * pvval
                            ),
        'convertYUVToRGB': (c_int,
                            c_int,  # l_int32 yval
                            c_int,  # l_int32 uval
                            c_int,  # l_int32 vval
                            c_int_p,  # l_int32 * prval
                            c_int_p,  # l_int32 * pgval
                            c_int_p,  # l_int32 * pbval
                            ),
        'pixcmapConvertRGBToYUV': (c_int,
                                   LPPixColormap,  # PIXCMAP * cmap
                                   ),
        'pixcmapConvertYUVToRGB': (c_int,
                                   LPPixColormap,  # PIXCMAP * cmap
                                   ),
        'pixConvertRGBToXYZ': (LPFPixa,  # FPIXA *
                               LPPix,  # PIX * pixs
                               ),
        'fpixaConvertXYZToRGB': (LPPix,  # PIX *
                                 LPFPixa,  # FPIXA * fpixa
                                 ),
        'convertRGBToXYZ': (c_int,
                            c_int,  # l_int32 rval
                            c_int,  # l_int32 gval
                            c_int,  # l_int32 bval
                            c_float_p,  # l_float32 * pfxval
                            c_float_p,  # l_float32 * pfyval
                            c_float_p,  # l_float32 * pfzval
                            ),
        'convertXYZToRGB': (c_int,
                            c_float,  # l_float32 fxval
                            c_float,  # l_float32 fyval
                            c_float,  # l_float32 fzval
                            c_int,  # l_int32 blackout
                            c_int_p,  # l_int32 * prval
                            c_int_p,  # l_int32 * pgval
                            c_int_p,  # l_int32 * pbval
                            ),
        'fpixaConvertXYZToLAB': (LPFPixa,  # FPIXA *
                                 LPFPixa,  # FPIXA * fpixas
                                 ),
        'fpixaConvertLABToXYZ': (LPFPixa,  # FPIXA *
                                 LPFPixa,  # FPIXA * fpixas
                                 ),
        'convertXYZToLAB': (c_int,
                            c_float,  # l_float32 xval
                            c_float,  # l_float32 yval
                            c_float,  # l_float32 zval
                            c_float_p,  # l_float32 * plval
                            c_float_p,  # l_float32 * paval
                            c_float_p,  # l_float32 * pbval
                            ),
        'convertLABToXYZ': (c_int,
                            c_float,  # l_float32 lval
                            c_float,  # l_float32 aval
                            c_float,  # l_float32 bval
                            c_float_p,  # l_float32 * pxval
                            c_float_p,  # l_float32 * pyval
                            c_float_p,  # l_float32 * pzval
                            ),
        'pixConvertRGBToLAB': (LPFPixa,  # FPIXA *
                               LPPix,  # PIX * pixs
                               ),
        'fpixaConvertLABToRGB': (LPPix,  # PIX *
                                 LPFPixa,  # FPIXA * fpixa
                                 ),
        'convertRGBToLAB': (c_int,
                            c_int,  # l_int32 rval
                            c_int,  # l_int32 gval
                            c_int,  # l_int32 bval
                            c_float_p,  # l_float32 * pflval
                            c_float_p,  # l_float32 * pfaval
                            c_float_p,  # l_float32 * pfbval
                            ),
        'convertLABToRGB': (c_int,
                            c_float,  # l_float32 flval
                            c_float,  # l_float32 faval
                            c_float,  # l_float32 fbval
                            c_int_p,  # l_int32 * prval
                            c_int_p,  # l_int32 * pgval
                            c_int_p,  # l_int32 * pbval
                            ),
        'pixMakeGamutRGB': (LPPix,  # PIX *
                            c_int,  # l_int32 scale
                            ),
        'pixEqual': (c_int,
                     LPPix,  # PIX * pix1
                     LPPix,  # PIX * pix2
                     c_int_p,  # l_int32 * psame
                     ),
        'pixEqualWithAlpha': (c_int,
                              LPPix,  # PIX * pix1
                              LPPix,  # PIX * pix2
                              c_int,  # l_int32 use_alpha
                              c_int_p,  # l_int32 * psame
                              ),
        'pixEqualWithCmap': (c_int,
                             LPPix,  # PIX * pix1
                             LPPix,  # PIX * pix2
                             c_int_p,  # l_int32 * psame
                             ),
        'cmapEqual': (c_int,
                      LPPixColormap,  # PIXCMAP * cmap1
                      LPPixColormap,  # PIXCMAP * cmap2
                      c_int,  # l_int32 ncomps
                      c_int_p,  # l_int32 * psame
                      ),
        'pixUsesCmapColor': (c_int,
                             LPPix,  # PIX * pixs
                             c_int_p,  # l_int32 * pcolor
                             ),
        'pixCorrelationBinary': (c_int,
                                 LPPix,  # PIX * pix1
                                 LPPix,  # PIX * pix2
                                 c_float_p,  # l_float32 * pval
                                 ),
        'pixDisplayDiffBinary': (LPPix,  # PIX *
                                 LPPix,  # PIX * pix1
                                 LPPix,  # PIX * pix2
                                 ),
        'pixCompareBinary': (c_int,
                             LPPix,  # PIX * pix1
                             LPPix,  # PIX * pix2
                             c_int,  # l_int32 comptype
                             c_float_p,  # l_float32 * pfract
                             LPLPPix,  # PIX ** ppixdiff
                             ),
        'pixCompareGrayOrRGB': (c_int,
                                LPPix,  # PIX * pix1
                                LPPix,  # PIX * pix2
                                c_int,  # l_int32 comptype
                                c_int,  # l_int32 plottype
                                c_int_p,  # l_int32 * psame
                                c_float_p,  # l_float32 * pdiff
                                c_float_p,  # l_float32 * prmsdiff
                                LPLPPix,  # PIX ** ppixdiff
                                ),
        'pixCompareGray': (c_int,
                           LPPix,  # PIX * pix1
                           LPPix,  # PIX * pix2
                           c_int,  # l_int32 comptype
                           c_int,  # l_int32 plottype
                           c_int_p,  # l_int32 * psame
                           c_float_p,  # l_float32 * pdiff
                           c_float_p,  # l_float32 * prmsdiff
                           LPLPPix,  # PIX ** ppixdiff
                           ),
        'pixCompareRGB': (c_int,
                          LPPix,  # PIX * pix1
                          LPPix,  # PIX * pix2
                          c_int,  # l_int32 comptype
                          c_int,  # l_int32 plottype
                          c_int_p,  # l_int32 * psame
                          c_float_p,  # l_float32 * pdiff
                          c_float_p,  # l_float32 * prmsdiff
                          LPLPPix,  # PIX ** ppixdiff
                          ),
        'pixCompareTiled': (c_int,
                            LPPix,  # PIX * pix1
                            LPPix,  # PIX * pix2
                            c_int,  # l_int32 sx
                            c_int,  # l_int32 sy
                            c_int,  # l_int32 type
                            LPLPPix,  # PIX ** ppixdiff
                            ),
        'pixCompareRankDifference': (LPNuma,  # NUMA *
                                     LPPix,  # PIX * pix1
                                     LPPix,  # PIX * pix2
                                     c_int,  # l_int32 factor
                                     ),
        'pixTestForSimilarity': (c_int,
                                 LPPix,  # PIX * pix1
                                 LPPix,  # PIX * pix2
                                 c_int,  # l_int32 factor
                                 c_int,  # l_int32 mindiff
                                 c_float,  # l_float32 maxfract
                                 c_float,  # l_float32 maxave
                                 c_int_p,  # l_int32 * psimilar
                                 c_int,  # l_int32 details
                                 ),
        'pixGetDifferenceStats': (c_int,
                                  LPPix,  # PIX * pix1
                                  LPPix,  # PIX * pix2
                                  c_int,  # l_int32 factor
                                  c_int,  # l_int32 mindiff
                                  c_float_p,  # l_float32 * pfractdiff
                                  c_float_p,  # l_float32 * pavediff
                                  c_int,  # l_int32 details
                                  ),
        'pixGetDifferenceHistogram': (LPNuma,  # NUMA *
                                      LPPix,  # PIX * pix1
                                      LPPix,  # PIX * pix2
                                      c_int,  # l_int32 factor
                                      ),
        'pixGetPerceptualDiff': (c_int,
                                 LPPix,  # PIX * pixs1
                                 LPPix,  # PIX * pixs2
                                 c_int,  # l_int32 sampling
                                 c_int,  # l_int32 dilation
                                 c_int,  # l_int32 mindiff
                                 c_float_p,  # l_float32 * pfract
                                 LPLPPix,  # PIX ** ppixdiff1
                                 LPLPPix,  # PIX ** ppixdiff2
                                 ),
        'pixGetPSNR': (c_int,
                       LPPix,  # PIX * pix1
                       LPPix,  # PIX * pix2
                       c_int,  # l_int32 factor
                       c_float_p,  # l_float32 * ppsnr
                       ),
        'pixaComparePhotoRegionsByHisto': (c_int,
                                           LPPixa,  # PIXA * pixa
                                           c_float,  # l_float32 minratio
                                           c_float,  # l_float32 textthresh
                                           c_int,  # l_int32 factor
                                           c_int,  # l_int32 n
                                           c_float,  # l_float32 simthresh
                                           LPLPNuma,  # NUMA ** pnai
                                           # l_float32 ** pscores
                                           POINTER(c_float_p),
                                           LPLPPix,  # PIX ** ppixd
                                           c_int,  # l_int32 debug
                                           ),
        'pixComparePhotoRegionsByHisto': (c_int,
                                          LPPix,  # PIX * pix1
                                          LPPix,  # PIX * pix2
                                          LPBox,  # BOX * box1
                                          LPBox,  # BOX * box2
                                          c_float,  # l_float32 minratio
                                          c_int,  # l_int32 factor
                                          c_int,  # l_int32 n
                                          # l_float32 * pscore
                                          c_float_p,
                                          c_int,  # l_int32 debugflag
                                          ),
        'pixGenPhotoHistos': (c_int,
                              LPPix,  # PIX * pixs
                              LPBox,  # BOX * box
                              c_int,  # l_int32 factor
                              c_float,  # l_float32 thresh
                              c_int,  # l_int32 n
                              LPLPNumaa,  # NUMAA ** pnaa
                              c_int_p,  # l_int32 * pw
                              c_int_p,  # l_int32 * ph
                              c_int,  # l_int32 debugindex
                              ),
        'pixPadToCenterCentroid': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 factor
                                   ),
        'pixCentroid8': (c_int,
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 factor
                         c_float_p,  # l_float32 * pcx
                         c_float_p,  # l_float32 * pcy
                         ),
        'pixDecideIfPhotoImage': (c_int,
                                  LPPix,  # PIX * pix
                                  c_int,  # l_int32 factor
                                  c_float,  # l_float32 thresh
                                  c_int,  # l_int32 n
                                  LPLPNumaa,  # NUMAA ** pnaa
                                  LPPixa,  # PIXA * pixadebug
                                  ),
        'compareTilesByHisto': (c_int,
                                LPNumaa,  # NUMAA * naa1
                                LPNumaa,  # NUMAA * naa2
                                c_float,  # l_float32 minratio
                                c_int,  # l_int32 w1
                                c_int,  # l_int32 h1
                                c_int,  # l_int32 w2
                                c_int,  # l_int32 h2
                                c_float_p,  # l_float32 * pscore
                                LPPixa,  # PIXA * pixadebug
                                ),
        'pixCompareGrayByHisto': (c_int,
                                  LPPix,  # PIX * pix1
                                  LPPix,  # PIX * pix2
                                  LPBox,  # BOX * box1
                                  LPBox,  # BOX * box2
                                  c_float,  # l_float32 minratio
                                  c_int,  # l_int32 maxgray
                                  c_int,  # l_int32 factor
                                  c_int,  # l_int32 n
                                  c_float_p,  # l_float32 * pscore
                                  c_int,  # l_int32 debugflag
                                  ),
        'pixCropAlignedToCentroid': (c_int,
                                     LPPix,  # PIX * pix1
                                     LPPix,  # PIX * pix2
                                     c_int,  # l_int32 factor
                                     LPLPBox,  # BOX ** pbox1
                                     LPLPBox,  # BOX ** pbox2
                                     ),
        'l_compressGrayHistograms': (c_ubyte_p,
                                     LPNumaa,  # NUMAA * naa
                                     c_int,  # l_int32 w
                                     c_int,  # l_int32 h
                                     c_size_t_p,  # size_t * psize
                                     ),
        'l_uncompressGrayHistograms': (LPNumaa,  # NUMAA *
                                       c_ubyte_p,  # l_uint8 * bytea
                                       c_size_t,  # size_t size
                                       c_int_p,  # l_int32 * pw
                                       c_int_p,  # l_int32 * ph
                                       ),
        'pixCompareWithTranslation': (c_int,
                                      LPPix,  # PIX * pix1
                                      LPPix,  # PIX * pix2
                                      c_int,  # l_int32 thresh
                                      c_int_p,  # l_int32 * pdelx
                                      c_int_p,  # l_int32 * pdely
                                      c_float_p,  # l_float32 * pscore
                                      c_int,  # l_int32 debugflag
                                      ),
        'pixBestCorrelation': (c_int,
                               LPPix,  # PIX * pix1
                               LPPix,  # PIX * pix2
                               c_int,  # l_int32 area1
                               c_int,  # l_int32 area2
                               c_int,  # l_int32 etransx
                               c_int,  # l_int32 etransy
                               c_int,  # l_int32 maxshift
                               c_int_p,  # l_int32 * tab8
                               c_int_p,  # l_int32 * pdelx
                               c_int_p,  # l_int32 * pdely
                               c_float_p,  # l_float32 * pscore
                               c_int,  # l_int32 debugflag
                               ),
        'pixConnComp': (LPBoxa,  # BOXA *
                        LPPix,  # PIX * pixs
                        LPLPPixa,  # PIXA ** ppixa
                        c_int,  # l_int32 connectivity
                        ),
        'pixConnCompPixa': (LPBoxa,  # BOXA *
                            LPPix,  # PIX * pixs
                            LPLPPixa,  # PIXA ** ppixa
                            c_int,  # l_int32 connectivity
                            ),
        'pixConnCompBB': (LPBoxa,  # BOXA *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 connectivity
                          ),
        'pixCountConnComp': (c_int,
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 connectivity
                             c_int_p,  # l_int32 * pcount
                             ),
        'nextOnPixelInRaster': (c_int,
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 xstart
                                c_int,  # l_int32 ystart
                                c_int_p,  # l_int32 * px
                                c_int_p,  # l_int32 * py
                                ),
        'convertFilesTo1bpp': (c_int,
                               c_char_p,  # const char * dirin
                               c_char_p,  # const char * substr
                               c_int,  # l_int32 upscaling
                               c_int,  # l_int32 thresh
                               c_int,  # l_int32 firstpage
                               c_int,  # l_int32 npages
                               c_char_p,  # const char * dirout
                               c_int,  # l_int32 outformat
                               ),
        'pixBlockconv': (LPPix,  # PIX *
                         LPPix,  # PIX * pix
                         c_int,  # l_int32 wc
                         c_int,  # l_int32 hc
                         ),
        'pixBlockconvGray': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             LPPix,  # PIX * pixacc
                             c_int,  # l_int32 wc
                             c_int,  # l_int32 hc
                             ),
        'pixBlockconvAccum': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              ),
        'pixBlockconvGrayUnnormalized': (LPPix,  # PIX *
                                         LPPix,  # PIX * pixs
                                         c_int,  # l_int32 wc
                                         c_int,  # l_int32 hc
                                         ),
        'pixBlockconvTiled': (LPPix,  # PIX *
                              LPPix,  # PIX * pix
                              c_int,  # l_int32 wc
                              c_int,  # l_int32 hc
                              c_int,  # l_int32 nx
                              c_int,  # l_int32 ny
                              ),
        'pixBlockconvGrayTile': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 LPPix,  # PIX * pixacc
                                 c_int,  # l_int32 wc
                                 c_int,  # l_int32 hc
                                 ),
        'pixWindowedStats': (c_int,
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 wc
                             c_int,  # l_int32 hc
                             c_int,  # l_int32 hasborder
                             LPLPPix,  # PIX ** ppixm
                             LPLPPix,  # PIX ** ppixms
                             LPLPFPix,  # FPIX ** pfpixv
                             LPLPFPix,  # FPIX ** pfpixrv
                             ),
        'pixWindowedMean': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 wc
                            c_int,  # l_int32 hc
                            c_int,  # l_int32 hasborder
                            c_int,  # l_int32 normflag
                            ),
        'pixWindowedMeanSquare': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 wc
                                  c_int,  # l_int32 hc
                                  c_int,  # l_int32 hasborder
                                  ),
        'pixWindowedVariance': (c_int,
                                LPPix,  # PIX * pixm
                                LPPix,  # PIX * pixms
                                LPLPFPix,  # FPIX ** pfpixv
                                LPLPFPix,  # FPIX ** pfpixrv
                                ),
        'pixMeanSquareAccum': (LPDPix,  # DPIX *
                               LPPix,  # PIX * pixs
                               ),
        'pixBlockrank': (LPPix,  # PIX *
                         LPPix,  # PIX * pixs
                         LPPix,  # PIX * pixacc
                         c_int,  # l_int32 wc
                         c_int,  # l_int32 hc
                         c_float,  # l_float32 rank
                         ),
        'pixBlocksum': (LPPix,  # PIX *
                        LPPix,  # PIX * pixs
                        LPPix,  # PIX * pixacc
                        c_int,  # l_int32 wc
                        c_int,  # l_int32 hc
                        ),
        'pixCensusTransform': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 halfsize
                               LPPix,  # PIX * pixacc
                               ),
        'l_setConvolveSampling': (None,
                                  c_int,  # l_int32 xfact
                                  c_int,  # l_int32 yfact
                                  ),
        'pixAddGaussianNoise': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_float,  # l_float32 stdev
                                ),
        'gaussDistribSampling': (c_float, ),
        'pixCorrelationScore': (c_int,
                                LPPix,  # PIX * pix1
                                LPPix,  # PIX * pix2
                                c_int,  # l_int32 area1
                                c_int,  # l_int32 area2
                                c_float,  # l_float32 delx
                                c_float,  # l_float32 dely
                                c_int,  # l_int32 maxdiffw
                                c_int,  # l_int32 maxdiffh
                                c_int_p,  # l_int32 * tab
                                c_float_p,  # l_float32 * pscore
                                ),
        'pixCorrelationScoreThresholded': (c_int,
                                           LPPix,  # PIX * pix1
                                           LPPix,  # PIX * pix2
                                           c_int,  # l_int32 area1
                                           c_int,  # l_int32 area2
                                           c_float,  # l_float32 delx
                                           c_float,  # l_float32 dely
                                           c_int,  # l_int32 maxdiffw
                                           c_int,  # l_int32 maxdiffh
                                           c_int_p,  # l_int32 * tab
                                           # l_int32 * downcount
                                           c_int_p,
                                           # l_float32 score_threshold
                                           c_float,
                                           ),
        'pixCorrelationScoreSimple': (c_int,
                                      LPPix,  # PIX * pix1
                                      LPPix,  # PIX * pix2
                                      c_int,  # l_int32 area1
                                      c_int,  # l_int32 area2
                                      c_float,  # l_float32 delx
                                      c_float,  # l_float32 dely
                                      c_int,  # l_int32 maxdiffw
                                      c_int,  # l_int32 maxdiffh
                                      c_int_p,  # l_int32 * tab
                                      c_float_p,  # l_float32 * pscore
                                      ),
        'pixCorrelationScoreShifted': (c_int,
                                       LPPix,  # PIX * pix1
                                       LPPix,  # PIX * pix2
                                       c_int,  # l_int32 area1
                                       c_int,  # l_int32 area2
                                       c_int,  # l_int32 delx
                                       c_int,  # l_int32 dely
                                       c_int_p,  # l_int32 * tab
                                       c_float_p,  # l_float32 * pscore
                                       ),
        'dewarpGetTextlineCenters': (LPPtaa,  # PTAA *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 debugflag
                                     ),
        'dewarpRemoveShortLines': (LPPtaa,  # PTAA *
                                   LPPix,  # PIX * pixs
                                   LPPtaa,  # PTAA * ptaas
                                   c_float,  # l_float32 fract
                                   c_int,  # l_int32 debugflag
                                   ),
        'pixMorphDwa_2': (LPPix,  # PIX *
                          LPPix,  # PIX * pixd
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 operation
                          c_char_p,  # char * selname
                          ),
        'pixFMorphopGen_2': (LPPix,  # PIX *
                             LPPix,  # PIX * pixd
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 operation
                             c_char_p,  # char * selname
                             ),
        'fmorphopgen_low_2': (c_int,
                              c_uint_p,  # l_uint32 * datad
                              c_int,  # l_int32 w
                              c_int,  # l_int32 h
                              c_int,  # l_int32 wpld
                              c_uint_p,  # l_uint32 * datas
                              c_int,  # l_int32 wpls
                              c_int,  # l_int32 index
                              ),
        'pixSobelEdgeFilter': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 orientflag
                               ),
        'pixTwoSidedEdgeFilter': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 orientflag
                                  ),
        'pixMeasureEdgeSmoothness': (c_int,
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 side
                                     c_int,  # l_int32 minjump
                                     c_int,  # l_int32 minreversal
                                     c_float_p,  # l_float32 * pjpl
                                     c_float_p,  # l_float32 * pjspl
                                     c_float_p,  # l_float32 * prpl
                                     c_char_p,  # const char * debugfile
                                     ),
        'pixGetEdgeProfile': (LPNuma,  # NUMA *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 side
                              c_char_p,  # const char * debugfile
                              ),
        'pixGetLastOffPixelInRun': (c_int,
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 x
                                    c_int,  # l_int32 y
                                    c_int,  # l_int32 direction
                                    c_int_p,  # l_int32 * ploc
                                    ),
        'pixGetLastOnPixelInRun': (c_int,
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 x
                                   c_int,  # l_int32 y
                                   c_int,  # l_int32 direction
                                   c_int_p,  # l_int32 * ploc
                                   ),
        'encodeBase64': (c_char_p,
                         c_ubyte_p,  # const l_uint8 * inarray
                         c_int,  # l_int32 insize
                         c_int_p,  # l_int32 * poutsize
                         ),
        'decodeBase64': (c_ubyte_p,
                         c_char_p,  # const char * inarray
                         c_int,  # l_int32 insize
                         c_int_p,  # l_int32 * poutsize
                         ),
        'encodeAscii85': (c_char_p,
                          c_ubyte_p,  # const l_uint8 * inarray
                          c_size_t,  # size_t insize
                          c_size_t_p,  # size_t * poutsize
                          ),
        'decodeAscii85': (c_ubyte_p,
                          c_char_p,  # const char * inarray
                          c_size_t,  # size_t insize
                          c_size_t_p,  # size_t * poutsize
                          ),
        'encodeAscii85WithComp': (c_char_p,
                                  c_ubyte_p,  # const l_uint8 * indata
                                  c_size_t,  # size_t insize
                                  c_size_t_p,  # size_t * poutsize
                                  ),
        'decodeAscii85WithComp': (c_ubyte_p,
                                  c_char_p,  # const char * instr
                                  c_size_t,  # size_t insize
                                  c_size_t_p,  # size_t * poutsize
                                  ),
        'reformatPacked64': (c_char_p,
                             c_char_p,  # const char * inarray
                             c_int,  # l_int32 insize
                             c_int,  # l_int32 leadspace
                             c_int,  # l_int32 linechars
                             c_int,  # l_int32 addquotes
                             c_int_p,  # l_int32 * poutsize
                             ),
        'pixGammaTRC': (LPPix,  # PIX *
                        LPPix,  # PIX * pixd
                        LPPix,  # PIX * pixs
                        c_float,  # l_float32 gamma
                        c_int,  # l_int32 minval
                        c_int,  # l_int32 maxval
                        ),
        'pixGammaTRCMasked': (LPPix,  # PIX *
                              LPPix,  # PIX * pixd
                              LPPix,  # PIX * pixs
                              LPPix,  # PIX * pixm
                              c_float,  # l_float32 gamma
                              c_int,  # l_int32 minval
                              c_int,  # l_int32 maxval
                              ),
        'pixGammaTRCWithAlpha': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixd
                                 LPPix,  # PIX * pixs
                                 c_float,  # l_float32 gamma
                                 c_int,  # l_int32 minval
                                 c_int,  # l_int32 maxval
                                 ),
        'numaGammaTRC': (LPNuma,  # NUMA *
                         c_float,  # l_float32 gamma
                         c_int,  # l_int32 minval
                         c_int,  # l_int32 maxval
                         ),
        'pixContrastTRC': (LPPix,  # PIX *
                           LPPix,  # PIX * pixd
                           LPPix,  # PIX * pixs
                           c_float,  # l_float32 factor
                           ),
        'pixContrastTRCMasked': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixd
                                 LPPix,  # PIX * pixs
                                 LPPix,  # PIX * pixm
                                 c_float,  # l_float32 factor
                                 ),
        'numaContrastTRC': (LPNuma,  # NUMA *
                            c_float,  # l_float32 factor
                            ),
        'pixEqualizeTRC': (LPPix,  # PIX *
                           LPPix,  # PIX * pixd
                           LPPix,  # PIX * pixs
                           c_float,  # l_float32 fract
                           c_int,  # l_int32 factor
                           ),
        'numaEqualizeTRC': (LPNuma,  # NUMA *
                            LPPix,  # PIX * pix
                            c_float,  # l_float32 fract
                            c_int,  # l_int32 factor
                            ),
        'pixTRCMap': (c_int,
                      LPPix,  # PIX * pixs
                      LPPix,  # PIX * pixm
                      LPNuma,  # NUMA * na
                      ),
        'pixTRCMapGeneral': (c_int,
                             LPPix,  # PIX * pixs
                             LPPix,  # PIX * pixm
                             LPNuma,  # NUMA * nar
                             LPNuma,  # NUMA * nag
                             LPNuma,  # NUMA * nab
                             ),
        'pixUnsharpMasking': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 halfwidth
                              c_float,  # l_float32 fract
                              ),
        'pixUnsharpMaskingGray': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 halfwidth
                                  c_float,  # l_float32 fract
                                  ),
        'pixUnsharpMaskingFast': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 halfwidth
                                  c_float,  # l_float32 fract
                                  c_int,  # l_int32 direction
                                  ),
        'pixUnsharpMaskingGrayFast': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      c_int,  # l_int32 halfwidth
                                      c_float,  # l_float32 fract
                                      c_int,  # l_int32 direction
                                      ),
        'pixUnsharpMaskingGray1D': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 halfwidth
                                    c_float,  # l_float32 fract
                                    c_int,  # l_int32 direction
                                    ),
        'pixUnsharpMaskingGray2D': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 halfwidth
                                    c_float,  # l_float32 fract
                                    ),
        'pixModifyHue': (LPPix,  # PIX *
                         LPPix,  # PIX * pixd
                         LPPix,  # PIX * pixs
                         c_float,  # l_float32 fract
                         ),
        'pixModifySaturation': (LPPix,  # PIX *
                                LPPix,  # PIX * pixd
                                LPPix,  # PIX * pixs
                                c_float,  # l_float32 fract
                                ),
        'pixMeasureSaturation': (c_int,
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 factor
                                 c_float_p,  # l_float32 * psat
                                 ),
        'pixModifyBrightness': (LPPix,  # PIX *
                                LPPix,  # PIX * pixd
                                LPPix,  # PIX * pixs
                                c_float,  # l_float32 fract
                                ),
        'pixMosaicColorShiftRGB': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_float,  # l_float32 roff
                                   c_float,  # l_float32 goff
                                   c_float,  # l_float32 boff
                                   c_float,  # l_float32 delta
                                   c_int,  # l_int32 nincr
                                   ),
        'pixColorShiftRGB': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_float,  # l_float32 rfract
                             c_float,  # l_float32 gfract
                             c_float,  # l_float32 bfract
                             ),
        'pixDarkenGray': (LPPix,  # PIX *
                          LPPix,  # PIX * pixd
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 thresh
                          c_int,  # l_int32 satlimit
                          ),
        'pixMultConstantColor': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_float,  # l_float32 rfact
                                 c_float,  # l_float32 gfact
                                 c_float,  # l_float32 bfact
                                 ),
        'pixHalfEdgeByBandpass': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 sm1h
                                  c_int,  # l_int32 sm1v
                                  c_int,  # l_int32 sm2h
                                  c_int,  # l_int32 sm2v
                                  ),
        'pixHMTDwa_1': (LPPix,  # PIX *
                        LPPix,  # PIX * pixd
                        LPPix,  # PIX * pixs
                        c_char_p,  # const char * selname
                        ),
        'pixFHMTGen_1': (LPPix,  # PIX *
                         LPPix,  # PIX * pixd
                         LPPix,  # PIX * pixs
                         c_char_p,  # const char * selname
                         ),
        'fhmtgen_low_1': (c_int,
                          c_uint_p,  # l_uint32 * datad
                          c_int,  # l_int32 w
                          c_int,  # l_int32 h
                          c_int,  # l_int32 wpld
                          c_uint_p,  # l_uint32 * datas
                          c_int,  # l_int32 wpls
                          c_int,  # l_int32 index
                          ),
        'pixItalicWords': (c_int,
                           LPPix,  # PIX * pixs
                           LPBoxa,  # BOXA * boxaw
                           LPPix,  # PIX * pixw
                           LPLPBoxa,  # BOXA ** pboxa
                           c_int,  # l_int32 debugflag
                           ),
        'pixOrientCorrect': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_float,  # l_float32 minupconf
                             c_float,  # l_float32 minratio
                             c_float_p,  # l_float32 * pupconf
                             c_float_p,  # l_float32 * pleftconf
                             c_int_p,  # l_int32 * protation
                             c_int,  # l_int32 debug
                             ),
        'pixOrientDetect': (c_int,
                            LPPix,  # PIX * pixs
                            c_float_p,  # l_float32 * pupconf
                            c_float_p,  # l_float32 * pleftconf
                            c_int,  # l_int32 mincount
                            c_int,  # l_int32 debug
                            ),
        'makeOrientDecision': (c_int,
                               c_float,  # l_float32 upconf
                               c_float,  # l_float32 leftconf
                               c_float,  # l_float32 minupconf
                               c_float,  # l_float32 minratio
                               c_int_p,  # l_int32 * porient
                               c_int,  # l_int32 debug
                               ),
        'pixUpDownDetect': (c_int,
                            LPPix,  # PIX * pixs
                            c_float_p,  # l_float32 * pconf
                            c_int,  # l_int32 mincount
                            c_int,  # l_int32 npixels
                            c_int,  # l_int32 debug
                            ),
        'pixMirrorDetect': (c_int,
                            LPPix,  # PIX * pixs
                            c_float_p,  # l_float32 * pconf
                            c_int,  # l_int32 mincount
                            c_int,  # l_int32 debug
                            ),
        'pixMorphDwa_1': (LPPix,  # PIX *
                          LPPix,  # PIX * pixd
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 operation
                          c_char_p,  # char * selname
                          ),
        'pixFMorphopGen_1': (LPPix,  # PIX *
                             LPPix,  # PIX * pixd
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 operation
                             c_char_p,  # char * selname
                             ),
        'fmorphopgen_low_1': (c_int,
                              c_uint_p,  # l_uint32 * datad
                              c_int,  # l_int32 w
                              c_int,  # l_int32 h
                              c_int,  # l_int32 wpld
                              c_uint_p,  # l_uint32 * datas
                              c_int,  # l_int32 wpls
                              c_int,  # l_int32 index
                              ),
        'fpixCreate': (LPFPix,  # FPIX *
                       c_int,  # l_int32 width
                       c_int,  # l_int32 height
                       ),
        'fpixCreateTemplate': (LPFPix,  # FPIX *
                               LPFPix,  # FPIX * fpixs
                               ),
        'fpixClone': (LPFPix,  # FPIX *
                      LPFPix,  # FPIX * fpix
                      ),
        'fpixCopy': (LPFPix,  # FPIX *
                     LPFPix,  # FPIX * fpixs
                     ),
        'fpixDestroy': (None,
                        LPLPFPix,  # FPIX ** pfpix
                        ),
        'fpixGetDimensions': (c_int,
                              LPFPix,  # FPIX * fpix
                              c_int_p,  # l_int32 * pw
                              c_int_p,  # l_int32 * ph
                              ),
        'fpixSetDimensions': (c_int,
                              LPFPix,  # FPIX * fpix
                              c_int,  # l_int32 w
                              c_int,  # l_int32 h
                              ),
        'fpixGetWpl': (c_int,
                       LPFPix,  # FPIX * fpix
                       ),
        'fpixSetWpl': (c_int,
                       LPFPix,  # FPIX * fpix
                       c_int,  # l_int32 wpl
                       ),
        'fpixGetRefcount': (c_int,
                            LPFPix,  # FPIX * fpix
                            ),
        'fpixChangeRefcount': (c_int,
                               LPFPix,  # FPIX * fpix
                               c_int,  # l_int32 delta
                               ),
        'fpixGetResolution': (c_int,
                              LPFPix,  # FPIX * fpix
                              c_int_p,  # l_int32 * pxres
                              c_int_p,  # l_int32 * pyres
                              ),
        'fpixSetResolution': (c_int,
                              LPFPix,  # FPIX * fpix
                              c_int,  # l_int32 xres
                              c_int,  # l_int32 yres
                              ),
        'fpixCopyResolution': (c_int,
                               LPFPix,  # FPIX * fpixd
                               LPFPix,  # FPIX * fpixs
                               ),
        'fpixGetData': (c_float_p,
                        LPFPix,  # FPIX * fpix
                        ),
        'fpixSetData': (c_int,
                        LPFPix,  # FPIX * fpix
                        c_float_p,  # l_float32 * data
                        ),
        'fpixGetPixel': (c_int,
                         LPFPix,  # FPIX * fpix
                         c_int,  # l_int32 x
                         c_int,  # l_int32 y
                         c_float_p,  # l_float32 * pval
                         ),
        'fpixSetPixel': (c_int,
                         LPFPix,  # FPIX * fpix
                         c_int,  # l_int32 x
                         c_int,  # l_int32 y
                         c_float,  # l_float32 val
                         ),
        'fpixaCreate': (LPFPixa,  # FPIXA *
                        c_int,  # l_int32 n
                        ),
        'fpixaCopy': (LPFPixa,  # FPIXA *
                      LPFPixa,  # FPIXA * fpixa
                      c_int,  # l_int32 copyflag
                      ),
        'fpixaDestroy': (None,
                         LPLPFPixa,  # FPIXA ** pfpixa
                         ),
        'fpixaAddFPix': (c_int,
                         LPFPixa,  # FPIXA * fpixa
                         LPFPix,  # FPIX * fpix
                         c_int,  # l_int32 copyflag
                         ),
        'fpixaGetCount': (c_int,
                          LPFPixa,  # FPIXA * fpixa
                          ),
        'fpixaChangeRefcount': (c_int,
                                LPFPixa,  # FPIXA * fpixa
                                c_int,  # l_int32 delta
                                ),
        'fpixaGetFPix': (LPFPix,  # FPIX *
                         LPFPixa,  # FPIXA * fpixa
                         c_int,  # l_int32 index
                         c_int,  # l_int32 accesstype
                         ),
        'fpixaGetFPixDimensions': (c_int,
                                   LPFPixa,  # FPIXA * fpixa
                                   c_int,  # l_int32 index
                                   c_int_p,  # l_int32 * pw
                                   c_int_p,  # l_int32 * ph
                                   ),
        'fpixaGetData': (c_float_p,
                         LPFPixa,  # FPIXA * fpixa
                         c_int,  # l_int32 index
                         ),
        'fpixaGetPixel': (c_int,
                          LPFPixa,  # FPIXA * fpixa
                          c_int,  # l_int32 index
                          c_int,  # l_int32 x
                          c_int,  # l_int32 y
                          c_float_p,  # l_float32 * pval
                          ),
        'fpixaSetPixel': (c_int,
                          LPFPixa,  # FPIXA * fpixa
                          c_int,  # l_int32 index
                          c_int,  # l_int32 x
                          c_int,  # l_int32 y
                          c_float,  # l_float32 val
                          ),
        'dpixCreate': (LPDPix,  # DPIX *
                       c_int,  # l_int32 width
                       c_int,  # l_int32 height
                       ),
        'dpixCreateTemplate': (LPDPix,  # DPIX *
                               LPDPix,  # DPIX * dpixs
                               ),
        'dpixClone': (LPDPix,  # DPIX *
                      LPDPix,  # DPIX * dpix
                      ),
        'dpixCopy': (LPDPix,  # DPIX *
                     LPDPix,  # DPIX * dpixs
                     ),
        'dpixDestroy': (None,
                        LPLPDPix,  # DPIX ** pdpix
                        ),
        'dpixGetDimensions': (c_int,
                              LPDPix,  # DPIX * dpix
                              c_int_p,  # l_int32 * pw
                              c_int_p,  # l_int32 * ph
                              ),
        'dpixSetDimensions': (c_int,
                              LPDPix,  # DPIX * dpix
                              c_int,  # l_int32 w
                              c_int,  # l_int32 h
                              ),
        'dpixGetWpl': (c_int,
                       LPDPix,  # DPIX * dpix
                       ),
        'dpixSetWpl': (c_int,
                       LPDPix,  # DPIX * dpix
                       c_int,  # l_int32 wpl
                       ),
        'dpixGetRefcount': (c_int,
                            LPDPix,  # DPIX * dpix
                            ),
        'dpixChangeRefcount': (c_int,
                               LPDPix,  # DPIX * dpix
                               c_int,  # l_int32 delta
                               ),
        'dpixGetResolution': (c_int,
                              LPDPix,  # DPIX * dpix
                              c_int_p,  # l_int32 * pxres
                              c_int_p,  # l_int32 * pyres
                              ),
        'dpixSetResolution': (c_int,
                              LPDPix,  # DPIX * dpix
                              c_int,  # l_int32 xres
                              c_int,  # l_int32 yres
                              ),
        'dpixCopyResolution': (c_int,
                               LPDPix,  # DPIX * dpixd
                               LPDPix,  # DPIX * dpixs
                               ),
        'dpixGetData': (c_double_p,
                        LPDPix,  # DPIX * dpix
                        ),
        'dpixSetData': (c_int,
                        LPDPix,  # DPIX * dpix
                        c_double_p,  # l_float64 * data
                        ),
        'dpixGetPixel': (c_int,
                         LPDPix,  # DPIX * dpix
                         c_int,  # l_int32 x
                         c_int,  # l_int32 y
                         c_double_p,  # l_float64 * pval
                         ),
        'dpixSetPixel': (c_int,
                         LPDPix,  # DPIX * dpix
                         c_int,  # l_int32 x
                         c_int,  # l_int32 y
                         c_double,  # l_float64 val
                         ),
        'fpixRead': (LPFPix,  # FPIX *
                     c_char_p,  # const char * filename
                     ),
        'fpixReadStream': (LPFPix,  # FPIX *
                           LPFile,  # FILE * fp
                           ),
        'fpixReadMem': (LPFPix,  # FPIX *
                        c_ubyte_p,  # const l_uint8 * data
                        c_size_t,  # size_t size
                        ),
        'fpixWrite': (c_int,
                      c_char_p,  # const char * filename
                      LPFPix,  # FPIX * fpix
                      ),
        'fpixWriteStream': (c_int,
                            LPFile,  # FILE * fp
                            LPFPix,  # FPIX * fpix
                            ),
        'fpixWriteMem': (c_int,
                         POINTER(c_ubyte_p),  # l_uint8 ** pdata
                         c_size_t_p,  # size_t * psize
                         LPFPix,  # FPIX * fpix
                         ),
        'fpixEndianByteSwap': (LPFPix,  # FPIX *
                               LPFPix,  # FPIX * fpixd
                               LPFPix,  # FPIX * fpixs
                               ),
        'dpixRead': (LPDPix,  # DPIX *
                     c_char_p,  # const char * filename
                     ),
        'dpixReadStream': (LPDPix,  # DPIX *
                           LPFile,  # FILE * fp
                           ),
        'dpixReadMem': (LPDPix,  # DPIX *
                        c_ubyte_p,  # const l_uint8 * data
                        c_size_t,  # size_t size
                        ),
        'dpixWrite': (c_int,
                      c_char_p,  # const char * filename
                      LPDPix,  # DPIX * dpix
                      ),
        'dpixWriteStream': (c_int,
                            LPFile,  # FILE * fp
                            LPDPix,  # DPIX * dpix
                            ),
        'dpixWriteMem': (c_int,
                         POINTER(c_ubyte_p),  # l_uint8 ** pdata
                         c_size_t_p,  # size_t * psize
                         LPDPix,  # DPIX * dpix
                         ),
        'dpixEndianByteSwap': (LPDPix,  # DPIX *
                               LPDPix,  # DPIX * dpixd
                               LPDPix,  # DPIX * dpixs
                               ),
        'fpixPrintStream': (c_int,
                            LPFile,  # FILE * fp
                            LPFPix,  # FPIX * fpix
                            c_int,  # l_int32 factor
                            ),
        'pixConvertToFPix': (LPFPix,  # FPIX *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 ncomps
                             ),
        'pixConvertToDPix': (LPDPix,  # DPIX *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 ncomps
                             ),
        'fpixConvertToPix': (LPPix,  # PIX *
                             LPFPix,  # FPIX * fpixs
                             c_int,  # l_int32 outdepth
                             c_int,  # l_int32 negvals
                             c_int,  # l_int32 errorflag
                             ),
        'fpixDisplayMaxDynamicRange': (LPPix,  # PIX *
                                       LPFPix,  # FPIX * fpixs
                                       ),
        'fpixConvertToDPix': (LPDPix,  # DPIX *
                              LPFPix,  # FPIX * fpix
                              ),
        'dpixConvertToPix': (LPPix,  # PIX *
                             LPDPix,  # DPIX * dpixs
                             c_int,  # l_int32 outdepth
                             c_int,  # l_int32 negvals
                             c_int,  # l_int32 errorflag
                             ),
        'dpixConvertToFPix': (LPFPix,  # FPIX *
                              LPDPix,  # DPIX * dpix
                              ),
        'fpixGetMin': (c_int,
                       LPFPix,  # FPIX * fpix
                       c_float_p,  # l_float32 * pminval
                       c_int_p,  # l_int32 * pxminloc
                       c_int_p,  # l_int32 * pyminloc
                       ),
        'fpixGetMax': (c_int,
                       LPFPix,  # FPIX * fpix
                       c_float_p,  # l_float32 * pmaxval
                       c_int_p,  # l_int32 * pxmaxloc
                       c_int_p,  # l_int32 * pymaxloc
                       ),
        'dpixGetMin': (c_int,
                       LPDPix,  # DPIX * dpix
                       c_double_p,  # l_float64 * pminval
                       c_int_p,  # l_int32 * pxminloc
                       c_int_p,  # l_int32 * pyminloc
                       ),
        'dpixGetMax': (c_int,
                       LPDPix,  # DPIX * dpix
                       c_double_p,  # l_float64 * pmaxval
                       c_int_p,  # l_int32 * pxmaxloc
                       c_int_p,  # l_int32 * pymaxloc
                       ),
        'fpixScaleByInteger': (LPFPix,  # FPIX *
                               LPFPix,  # FPIX * fpixs
                               c_int,  # l_int32 factor
                               ),
        'dpixScaleByInteger': (LPDPix,  # DPIX *
                               LPDPix,  # DPIX * dpixs
                               c_int,  # l_int32 factor
                               ),
        'fpixLinearCombination': (LPFPix,  # FPIX *
                                  LPFPix,  # FPIX * fpixd
                                  LPFPix,  # FPIX * fpixs1
                                  LPFPix,  # FPIX * fpixs2
                                  c_float,  # l_float32 a
                                  c_float,  # l_float32 b
                                  ),
        'fpixAddMultConstant': (c_int,
                                LPFPix,  # FPIX * fpix
                                c_float,  # l_float32 addc
                                c_float,  # l_float32 multc
                                ),
        'dpixLinearCombination': (LPDPix,  # DPIX *
                                  LPDPix,  # DPIX * dpixd
                                  LPDPix,  # DPIX * dpixs1
                                  LPDPix,  # DPIX * dpixs2
                                  c_float,  # l_float32 a
                                  c_float,  # l_float32 b
                                  ),
        'dpixAddMultConstant': (c_int,
                                LPDPix,  # DPIX * dpix
                                c_double,  # l_float64 addc
                                c_double,  # l_float64 multc
                                ),
        'fpixSetAllArbitrary': (c_int,
                                LPFPix,  # FPIX * fpix
                                c_float,  # l_float32 inval
                                ),
        'dpixSetAllArbitrary': (c_int,
                                LPDPix,  # DPIX * dpix
                                c_double,  # l_float64 inval
                                ),
        'fpixAddBorder': (LPFPix,  # FPIX *
                          LPFPix,  # FPIX * fpixs
                          c_int,  # l_int32 left
                          c_int,  # l_int32 right
                          c_int,  # l_int32 top
                          c_int,  # l_int32 bot
                          ),
        'fpixRemoveBorder': (LPFPix,  # FPIX *
                             LPFPix,  # FPIX * fpixs
                             c_int,  # l_int32 left
                             c_int,  # l_int32 right
                             c_int,  # l_int32 top
                             c_int,  # l_int32 bot
                             ),
        'fpixAddMirroredBorder': (LPFPix,  # FPIX *
                                  LPFPix,  # FPIX * fpixs
                                  c_int,  # l_int32 left
                                  c_int,  # l_int32 right
                                  c_int,  # l_int32 top
                                  c_int,  # l_int32 bot
                                  ),
        'fpixAddContinuedBorder': (LPFPix,  # FPIX *
                                   LPFPix,  # FPIX * fpixs
                                   c_int,  # l_int32 left
                                   c_int,  # l_int32 right
                                   c_int,  # l_int32 top
                                   c_int,  # l_int32 bot
                                   ),
        'fpixAddSlopeBorder': (LPFPix,  # FPIX *
                               LPFPix,  # FPIX * fpixs
                               c_int,  # l_int32 left
                               c_int,  # l_int32 right
                               c_int,  # l_int32 top
                               c_int,  # l_int32 bot
                               ),
        'fpixRasterop': (c_int,
                         LPFPix,  # FPIX * fpixd
                         c_int,  # l_int32 dx
                         c_int,  # l_int32 dy
                         c_int,  # l_int32 dw
                         c_int,  # l_int32 dh
                         LPFPix,  # FPIX * fpixs
                         c_int,  # l_int32 sx
                         c_int,  # l_int32 sy
                         ),
        'fpixRotateOrth': (LPFPix,  # FPIX *
                           LPFPix,  # FPIX * fpixs
                           c_int,  # l_int32 quads
                           ),
        'fpixRotate180': (LPFPix,  # FPIX *
                          LPFPix,  # FPIX * fpixd
                          LPFPix,  # FPIX * fpixs
                          ),
        'fpixRotate90': (LPFPix,  # FPIX *
                         LPFPix,  # FPIX * fpixs
                         c_int,  # l_int32 direction
                         ),
        'fpixFlipLR': (LPFPix,  # FPIX *
                       LPFPix,  # FPIX * fpixd
                       LPFPix,  # FPIX * fpixs
                       ),
        'fpixFlipTB': (LPFPix,  # FPIX *
                       LPFPix,  # FPIX * fpixd
                       LPFPix,  # FPIX * fpixs
                       ),
        'fpixAffinePta': (LPFPix,  # FPIX *
                          LPFPix,  # FPIX * fpixs
                          LPPta,  # PTA * ptad
                          LPPta,  # PTA * ptas
                          c_int,  # l_int32 border
                          c_float,  # l_float32 inval
                          ),
        'fpixAffine': (LPFPix,  # FPIX *
                       LPFPix,  # FPIX * fpixs
                       c_float_p,  # l_float32 * vc
                       c_float,  # l_float32 inval
                       ),
        'fpixProjectivePta': (LPFPix,  # FPIX *
                              LPFPix,  # FPIX * fpixs
                              LPPta,  # PTA * ptad
                              LPPta,  # PTA * ptas
                              c_int,  # l_int32 border
                              c_float,  # l_float32 inval
                              ),
        'fpixProjective': (LPFPix,  # FPIX *
                           LPFPix,  # FPIX * fpixs
                           c_float_p,  # l_float32 * vc
                           c_float,  # l_float32 inval
                           ),
        'linearInterpolatePixelFloat': (c_int,
                                        c_float_p,  # l_float32 * datas
                                        c_int,  # l_int32 w
                                        c_int,  # l_int32 h
                                        c_float,  # l_float32 x
                                        c_float,  # l_float32 y
                                        c_float,  # l_float32 inval
                                        c_float_p,  # l_float32 * pval
                                        ),
        'fpixThresholdToPix': (LPPix,  # PIX *
                               LPFPix,  # FPIX * fpix
                               c_float,  # l_float32 thresh
                               ),
        'pixComponentFunction': (LPFPix,  # FPIX *
                                 LPPix,  # PIX * pix
                                 c_float,  # l_float32 rnum
                                 c_float,  # l_float32 gnum
                                 c_float,  # l_float32 bnum
                                 c_float,  # l_float32 rdenom
                                 c_float,  # l_float32 gdenom
                                 c_float,  # l_float32 bdenom
                                 ),
        'pixReadStreamGif': (LPPix,  # PIX *
                             LPFile,  # FILE * fp
                             ),
        'pixReadMemGif': (LPPix,  # PIX *
                          c_ubyte_p,  # const l_uint8 * cdata
                          c_size_t,  # size_t size
                          ),
        'pixWriteStreamGif': (c_int,
                              LPFile,  # FILE * fp
                              LPPix,  # PIX * pix
                              ),
        'pixWriteMemGif': (c_int,
                           POINTER(c_ubyte_p),  # l_uint8 ** pdata
                           c_size_t_p,  # size_t * psize
                           LPPix,  # PIX * pix
                           ),
        'gplotSimple1': (c_int,
                         LPNuma,  # NUMA * na
                         c_int,  # l_int32 outformat
                         c_char_p,  # const char * outroot
                         c_char_p,  # const char * title
                         ),
        'gplotSimple2': (c_int,
                         LPNuma,  # NUMA * na1
                         LPNuma,  # NUMA * na2
                         c_int,  # l_int32 outformat
                         c_char_p,  # const char * outroot
                         c_char_p,  # const char * title
                         ),
        'gplotSimpleN': (c_int,
                         LPNumaa,  # NUMAA * naa
                         c_int,  # l_int32 outformat
                         c_char_p,  # const char * outroot
                         c_char_p,  # const char * title
                         ),
        'gplotSimplePix1': (LPPix,  # PIX *
                            LPNuma,  # NUMA * na
                            c_char_p,  # const char * title
                            ),
        'gplotSimplePix2': (LPPix,  # PIX *
                            LPNuma,  # NUMA * na1
                            LPNuma,  # NUMA * na2
                            c_char_p,  # const char * title
                            ),
        'gplotSimplePixN': (LPPix,  # PIX *
                            LPNumaa,  # NUMAA * naa
                            c_char_p,  # const char * title
                            ),
        'gplotGeneralPix1': (LPPix,  # PIX *
                             LPNuma,  # NUMA * na
                             c_int,  # l_int32 plotstyle
                             c_char_p,  # const char * rootname
                             c_char_p,  # const char * title
                             c_char_p,  # const char * xlabel
                             c_char_p,  # const char * ylabel
                             ),
        'gplotGeneralPix2': (LPPix,  # PIX *
                             LPNuma,  # NUMA * na1
                             LPNuma,  # NUMA * na2
                             c_int,  # l_int32 plotstyle
                             c_char_p,  # const char * rootname
                             c_char_p,  # const char * title
                             c_char_p,  # const char * xlabel
                             c_char_p,  # const char * ylabel
                             ),
        'gplotGeneralPixN': (LPPix,  # PIX *
                             LPNuma,  # NUMA * nax
                             LPNumaa,  # NUMAA * naay
                             c_int,  # l_int32 plotstyle
                             c_char_p,  # const char * rootname
                             c_char_p,  # const char * title
                             c_char_p,  # const char * xlabel
                             c_char_p,  # const char * ylabel
                             ),
        'generatePtaLine': (LPPta,  # PTA *
                            c_int,  # l_int32 x1
                            c_int,  # l_int32 y1
                            c_int,  # l_int32 x2
                            c_int,  # l_int32 y2
                            ),
        'generatePtaWideLine': (LPPta,  # PTA *
                                c_int,  # l_int32 x1
                                c_int,  # l_int32 y1
                                c_int,  # l_int32 x2
                                c_int,  # l_int32 y2
                                c_int,  # l_int32 width
                                ),
        'generatePtaBox': (LPPta,  # PTA *
                           LPBox,  # BOX * box
                           c_int,  # l_int32 width
                           ),
        'generatePtaBoxa': (LPPta,  # PTA *
                            LPBoxa,  # BOXA * boxa
                            c_int,  # l_int32 width
                            c_int,  # l_int32 removedups
                            ),
        'generatePtaHashBox': (LPPta,  # PTA *
                               LPBox,  # BOX * box
                               c_int,  # l_int32 spacing
                               c_int,  # l_int32 width
                               c_int,  # l_int32 orient
                               c_int,  # l_int32 outline
                               ),
        'generatePtaHashBoxa': (LPPta,  # PTA *
                                LPBoxa,  # BOXA * boxa
                                c_int,  # l_int32 spacing
                                c_int,  # l_int32 width
                                c_int,  # l_int32 orient
                                c_int,  # l_int32 outline
                                c_int,  # l_int32 removedups
                                ),
        'generatePtaaBoxa': (LPPtaa,  # PTAA *
                             LPBoxa,  # BOXA * boxa
                             ),
        'generatePtaaHashBoxa': (LPPtaa,  # PTAA *
                                 LPBoxa,  # BOXA * boxa
                                 c_int,  # l_int32 spacing
                                 c_int,  # l_int32 width
                                 c_int,  # l_int32 orient
                                 c_int,  # l_int32 outline
                                 ),
        'generatePtaPolyline': (LPPta,  # PTA *
                                LPPta,  # PTA * ptas
                                c_int,  # l_int32 width
                                c_int,  # l_int32 closeflag
                                c_int,  # l_int32 removedups
                                ),
        'generatePtaGrid': (LPPta,  # PTA *
                            c_int,  # l_int32 w
                            c_int,  # l_int32 h
                            c_int,  # l_int32 nx
                            c_int,  # l_int32 ny
                            c_int,  # l_int32 width
                            ),
        'convertPtaLineTo4cc': (LPPta,  # PTA *
                                LPPta,  # PTA * ptas
                                ),
        'generatePtaFilledCircle': (LPPta,  # PTA *
                                    c_int,  # l_int32 radius
                                    ),
        'generatePtaFilledSquare': (LPPta,  # PTA *
                                    c_int,  # l_int32 side
                                    ),
        'generatePtaLineFromPt': (LPPta,  # PTA *
                                  c_int,  # l_int32 x
                                  c_int,  # l_int32 y
                                  c_double,  # l_float64 length
                                  c_double,  # l_float64 radang
                                  ),
        'locatePtRadially': (c_int,
                             c_int,  # l_int32 xr
                             c_int,  # l_int32 yr
                             c_double,  # l_float64 dist
                             c_double,  # l_float64 radang
                             c_double_p,  # l_float64 * px
                             c_double_p,  # l_float64 * py
                             ),
        'pixRenderPlotFromNuma': (c_int,
                                  LPLPPix,  # PIX ** ppix
                                  LPNuma,  # NUMA * na
                                  c_int,  # l_int32 plotloc
                                  c_int,  # l_int32 linewidth
                                  c_int,  # l_int32 max
                                  c_uint,  # l_uint32 color
                                  ),
        'makePlotPtaFromNuma': (LPPta,  # PTA *
                                LPNuma,  # NUMA * na
                                c_int,  # l_int32 size
                                c_int,  # l_int32 plotloc
                                c_int,  # l_int32 linewidth
                                c_int,  # l_int32 max
                                ),
        'pixRenderPlotFromNumaGen': (c_int,
                                     LPLPPix,  # PIX ** ppix
                                     LPNuma,  # NUMA * na
                                     c_int,  # l_int32 orient
                                     c_int,  # l_int32 linewidth
                                     c_int,  # l_int32 refpos
                                     c_int,  # l_int32 max
                                     c_int,  # l_int32 drawref
                                     c_uint,  # l_uint32 color
                                     ),
        'makePlotPtaFromNumaGen': (LPPta,  # PTA *
                                   LPNuma,  # NUMA * na
                                   c_int,  # l_int32 orient
                                   c_int,  # l_int32 linewidth
                                   c_int,  # l_int32 refpos
                                   c_int,  # l_int32 max
                                   c_int,  # l_int32 drawref
                                   ),
        'pixRenderPta': (c_int,
                         LPPix,  # PIX * pix
                         LPPta,  # PTA * pta
                         c_int,  # l_int32 op
                         ),
        'pixRenderPtaArb': (c_int,
                            LPPix,  # PIX * pix
                            LPPta,  # PTA * pta
                            c_ubyte,  # l_uint8 rval
                            c_ubyte,  # l_uint8 gval
                            c_ubyte,  # l_uint8 bval
                            ),
        'pixRenderPtaBlend': (c_int,
                              LPPix,  # PIX * pix
                              LPPta,  # PTA * pta
                              c_ubyte,  # l_uint8 rval
                              c_ubyte,  # l_uint8 gval
                              c_ubyte,  # l_uint8 bval
                              c_float,  # l_float32 fract
                              ),
        'pixRenderLine': (c_int,
                          LPPix,  # PIX * pix
                          c_int,  # l_int32 x1
                          c_int,  # l_int32 y1
                          c_int,  # l_int32 x2
                          c_int,  # l_int32 y2
                          c_int,  # l_int32 width
                          c_int,  # l_int32 op
                          ),
        'pixRenderLineArb': (c_int,
                             LPPix,  # PIX * pix
                             c_int,  # l_int32 x1
                             c_int,  # l_int32 y1
                             c_int,  # l_int32 x2
                             c_int,  # l_int32 y2
                             c_int,  # l_int32 width
                             c_ubyte,  # l_uint8 rval
                             c_ubyte,  # l_uint8 gval
                             c_ubyte,  # l_uint8 bval
                             ),
        'pixRenderLineBlend': (c_int,
                               LPPix,  # PIX * pix
                               c_int,  # l_int32 x1
                               c_int,  # l_int32 y1
                               c_int,  # l_int32 x2
                               c_int,  # l_int32 y2
                               c_int,  # l_int32 width
                               c_ubyte,  # l_uint8 rval
                               c_ubyte,  # l_uint8 gval
                               c_ubyte,  # l_uint8 bval
                               c_float,  # l_float32 fract
                               ),
        'pixRenderBox': (c_int,
                         LPPix,  # PIX * pix
                         LPBox,  # BOX * box
                         c_int,  # l_int32 width
                         c_int,  # l_int32 op
                         ),
        'pixRenderBoxArb': (c_int,
                            LPPix,  # PIX * pix
                            LPBox,  # BOX * box
                            c_int,  # l_int32 width
                            c_ubyte,  # l_uint8 rval
                            c_ubyte,  # l_uint8 gval
                            c_ubyte,  # l_uint8 bval
                            ),
        'pixRenderBoxBlend': (c_int,
                              LPPix,  # PIX * pix
                              LPBox,  # BOX * box
                              c_int,  # l_int32 width
                              c_ubyte,  # l_uint8 rval
                              c_ubyte,  # l_uint8 gval
                              c_ubyte,  # l_uint8 bval
                              c_float,  # l_float32 fract
                              ),
        'pixRenderBoxa': (c_int,
                          LPPix,  # PIX * pix
                          LPBoxa,  # BOXA * boxa
                          c_int,  # l_int32 width
                          c_int,  # l_int32 op
                          ),
        'pixRenderBoxaArb': (c_int,
                             LPPix,  # PIX * pix
                             LPBoxa,  # BOXA * boxa
                             c_int,  # l_int32 width
                             c_ubyte,  # l_uint8 rval
                             c_ubyte,  # l_uint8 gval
                             c_ubyte,  # l_uint8 bval
                             ),
        'pixRenderBoxaBlend': (c_int,
                               LPPix,  # PIX * pix
                               LPBoxa,  # BOXA * boxa
                               c_int,  # l_int32 width
                               c_ubyte,  # l_uint8 rval
                               c_ubyte,  # l_uint8 gval
                               c_ubyte,  # l_uint8 bval
                               c_float,  # l_float32 fract
                               c_int,  # l_int32 removedups
                               ),
        'pixRenderHashBox': (c_int,
                             LPPix,  # PIX * pix
                             LPBox,  # BOX * box
                             c_int,  # l_int32 spacing
                             c_int,  # l_int32 width
                             c_int,  # l_int32 orient
                             c_int,  # l_int32 outline
                             c_int,  # l_int32 op
                             ),
        'pixRenderHashBoxArb': (c_int,
                                LPPix,  # PIX * pix
                                LPBox,  # BOX * box
                                c_int,  # l_int32 spacing
                                c_int,  # l_int32 width
                                c_int,  # l_int32 orient
                                c_int,  # l_int32 outline
                                c_int,  # l_int32 rval
                                c_int,  # l_int32 gval
                                c_int,  # l_int32 bval
                                ),
        'pixRenderHashBoxBlend': (c_int,
                                  LPPix,  # PIX * pix
                                  LPBox,  # BOX * box
                                  c_int,  # l_int32 spacing
                                  c_int,  # l_int32 width
                                  c_int,  # l_int32 orient
                                  c_int,  # l_int32 outline
                                  c_int,  # l_int32 rval
                                  c_int,  # l_int32 gval
                                  c_int,  # l_int32 bval
                                  c_float,  # l_float32 fract
                                  ),
        'pixRenderHashMaskArb': (c_int,
                                 LPPix,  # PIX * pix
                                 LPPix,  # PIX * pixm
                                 c_int,  # l_int32 x
                                 c_int,  # l_int32 y
                                 c_int,  # l_int32 spacing
                                 c_int,  # l_int32 width
                                 c_int,  # l_int32 orient
                                 c_int,  # l_int32 outline
                                 c_int,  # l_int32 rval
                                 c_int,  # l_int32 gval
                                 c_int,  # l_int32 bval
                                 ),
        'pixRenderHashBoxa': (c_int,
                              LPPix,  # PIX * pix
                              LPBoxa,  # BOXA * boxa
                              c_int,  # l_int32 spacing
                              c_int,  # l_int32 width
                              c_int,  # l_int32 orient
                              c_int,  # l_int32 outline
                              c_int,  # l_int32 op
                              ),
        'pixRenderHashBoxaArb': (c_int,
                                 LPPix,  # PIX * pix
                                 LPBoxa,  # BOXA * boxa
                                 c_int,  # l_int32 spacing
                                 c_int,  # l_int32 width
                                 c_int,  # l_int32 orient
                                 c_int,  # l_int32 outline
                                 c_int,  # l_int32 rval
                                 c_int,  # l_int32 gval
                                 c_int,  # l_int32 bval
                                 ),
        'pixRenderHashBoxaBlend': (c_int,
                                   LPPix,  # PIX * pix
                                   LPBoxa,  # BOXA * boxa
                                   c_int,  # l_int32 spacing
                                   c_int,  # l_int32 width
                                   c_int,  # l_int32 orient
                                   c_int,  # l_int32 outline
                                   c_int,  # l_int32 rval
                                   c_int,  # l_int32 gval
                                   c_int,  # l_int32 bval
                                   c_float,  # l_float32 fract
                                   ),
        'pixRenderPolyline': (c_int,
                              LPPix,  # PIX * pix
                              LPPta,  # PTA * ptas
                              c_int,  # l_int32 width
                              c_int,  # l_int32 op
                              c_int,  # l_int32 closeflag
                              ),
        'pixRenderPolylineArb': (c_int,
                                 LPPix,  # PIX * pix
                                 LPPta,  # PTA * ptas
                                 c_int,  # l_int32 width
                                 c_ubyte,  # l_uint8 rval
                                 c_ubyte,  # l_uint8 gval
                                 c_ubyte,  # l_uint8 bval
                                 c_int,  # l_int32 closeflag
                                 ),
        'pixRenderPolylineBlend': (c_int,
                                   LPPix,  # PIX * pix
                                   LPPta,  # PTA * ptas
                                   c_int,  # l_int32 width
                                   c_ubyte,  # l_uint8 rval
                                   c_ubyte,  # l_uint8 gval
                                   c_ubyte,  # l_uint8 bval
                                   c_float,  # l_float32 fract
                                   c_int,  # l_int32 closeflag
                                   c_int,  # l_int32 removedups
                                   ),
        'pixRenderGridArb': (c_int,
                             LPPix,  # PIX * pix
                             c_int,  # l_int32 nx
                             c_int,  # l_int32 ny
                             c_int,  # l_int32 width
                             c_ubyte,  # l_uint8 rval
                             c_ubyte,  # l_uint8 gval
                             c_ubyte,  # l_uint8 bval
                             ),
        'pixRenderRandomCmapPtaa': (LPPix,  # PIX *
                                    LPPix,  # PIX * pix
                                    LPPtaa,  # PTAA * ptaa
                                    c_int,  # l_int32 polyflag
                                    c_int,  # l_int32 width
                                    c_int,  # l_int32 closeflag
                                    ),
        'pixRenderPolygon': (LPPix,  # PIX *
                             LPPta,  # PTA * ptas
                             c_int,  # l_int32 width
                             c_int_p,  # l_int32 * pxmin
                             c_int_p,  # l_int32 * pymin
                             ),
        'pixFillPolygon': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           LPPta,  # PTA * pta
                           c_int,  # l_int32 xmin
                           c_int,  # l_int32 ymin
                           ),
        'pixRenderContours': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 startval
                              c_int,  # l_int32 incr
                              c_int,  # l_int32 outdepth
                              ),
        'fpixAutoRenderContours': (LPPix,  # PIX *
                                   LPFPix,  # FPIX * fpix
                                   c_int,  # l_int32 ncontours
                                   ),
        'fpixRenderContours': (LPPix,  # PIX *
                               LPFPix,  # FPIX * fpixs
                               c_float,  # l_float32 incr
                               c_float,  # l_float32 proxim
                               ),
        'pixGeneratePtaBoundary': (LPPta,  # PTA *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 width
                                   ),
        'pixErodeGray': (LPPix,  # PIX *
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 hsize
                         c_int,  # l_int32 vsize
                         ),
        'pixDilateGray': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 hsize
                          c_int,  # l_int32 vsize
                          ),
        'pixOpenGray': (LPPix,  # PIX *
                        LPPix,  # PIX * pixs
                        c_int,  # l_int32 hsize
                        c_int,  # l_int32 vsize
                        ),
        'pixCloseGray': (LPPix,  # PIX *
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 hsize
                         c_int,  # l_int32 vsize
                         ),
        'pixErodeGray3': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 hsize
                          c_int,  # l_int32 vsize
                          ),
        'pixDilateGray3': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 hsize
                           c_int,  # l_int32 vsize
                           ),
        'pixOpenGray3': (LPPix,  # PIX *
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 hsize
                         c_int,  # l_int32 vsize
                         ),
        'pixCloseGray3': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 hsize
                          c_int,  # l_int32 vsize
                          ),
        'pixDitherToBinary': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              ),
        'pixDitherToBinarySpec': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 lowerclip
                                  c_int,  # l_int32 upperclip
                                  ),
        'ditherToBinaryLineLow': (None,
                                  c_uint_p,  # l_uint32 * lined
                                  c_int,  # l_int32 w
                                  c_uint_p,  # l_uint32 * bufs1
                                  c_uint_p,  # l_uint32 * bufs2
                                  c_int,  # l_int32 lowerclip
                                  c_int,  # l_int32 upperclip
                                  c_int,  # l_int32 lastlineflag
                                  ),
        'pixThresholdToBinary': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 thresh
                                 ),
        'thresholdToBinaryLineLow': (None,
                                     c_uint_p,  # l_uint32 * lined
                                     c_int,  # l_int32 w
                                     c_uint_p,  # l_uint32 * lines
                                     c_int,  # l_int32 d
                                     c_int,  # l_int32 thresh
                                     ),
        'pixVarThresholdToBinary': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    LPPix,  # PIX * pixg
                                    ),
        'pixAdaptThresholdToBinary': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      LPPix,  # PIX * pixm
                                      c_float,  # l_float32 gamma
                                      ),
        'pixAdaptThresholdToBinaryGen': (LPPix,  # PIX *
                                         LPPix,  # PIX * pixs
                                         LPPix,  # PIX * pixm
                                         c_float,  # l_float32 gamma
                                         c_int,  # l_int32 blackval
                                         c_int,  # l_int32 whiteval
                                         c_int,  # l_int32 thresh
                                         ),
        'pixGenerateMaskByValue': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 val
                                   c_int,  # l_int32 usecmap
                                   ),
        'pixGenerateMaskByBand': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 lower
                                  c_int,  # l_int32 upper
                                  c_int,  # l_int32 inband
                                  c_int,  # l_int32 usecmap
                                  ),
        'pixDitherTo2bpp': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 cmapflag
                            ),
        'pixDitherTo2bppSpec': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 lowerclip
                                c_int,  # l_int32 upperclip
                                c_int,  # l_int32 cmapflag
                                ),
        'pixThresholdTo2bpp': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 nlevels
                               c_int,  # l_int32 cmapflag
                               ),
        'pixThresholdTo4bpp': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 nlevels
                               c_int,  # l_int32 cmapflag
                               ),
        'pixThresholdOn8bpp': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 nlevels
                               c_int,  # l_int32 cmapflag
                               ),
        'pixThresholdGrayArb': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_char_p,  # const char * edgevals
                                c_int,  # l_int32 outdepth
                                c_int,  # l_int32 use_average
                                c_int,  # l_int32 setblack
                                c_int,  # l_int32 setwhite
                                ),
        'makeGrayQuantIndexTable': (c_int_p,
                                    c_int,  # l_int32 nlevels
                                    ),
        'makeGrayQuantTableArb': (c_int,
                                  LPNuma,  # NUMA * na
                                  c_int,  # l_int32 outdepth
                                  POINTER(c_int_p),  # l_int32 ** ptab
                                  LPLPPixColormap,  # PIXCMAP ** pcmap
                                  ),
        'pixGenerateMaskByBand32': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_uint,  # l_uint32 refval
                                    c_int,  # l_int32 delm
                                    c_int,  # l_int32 delp
                                    c_float,  # l_float32 fractm
                                    c_float,  # l_float32 fractp
                                    ),
        'pixGenerateMaskByDiscr32': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_uint,  # l_uint32 refval1
                                     c_uint,  # l_uint32 refval2
                                     c_int,  # l_int32 distflag
                                     ),
        'pixGrayQuantFromHisto': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixd
                                  LPPix,  # PIX * pixs
                                  LPPix,  # PIX * pixm
                                  c_float,  # l_float32 minfract
                                  c_int,  # l_int32 maxsize
                                  ),
        'pixGrayQuantFromCmap': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 LPPixColormap,  # PIXCMAP * cmap
                                 c_int,  # l_int32 mindepth
                                 ),
        'pixHaustest': (c_int,
                        LPPix,  # PIX * pix1
                        LPPix,  # PIX * pix2
                        LPPix,  # PIX * pix3
                        LPPix,  # PIX * pix4
                        c_float,  # l_float32 delx
                        c_float,  # l_float32 dely
                        c_int,  # l_int32 maxdiffw
                        c_int,  # l_int32 maxdiffh
                        ),
        'pixRankHaustest': (c_int,
                            LPPix,  # PIX * pix1
                            LPPix,  # PIX * pix2
                            LPPix,  # PIX * pix3
                            LPPix,  # PIX * pix4
                            c_float,  # l_float32 delx
                            c_float,  # l_float32 dely
                            c_int,  # l_int32 maxdiffw
                            c_int,  # l_int32 maxdiffh
                            c_int,  # l_int32 area1
                            c_int,  # l_int32 area3
                            c_float,  # l_float32 rank
                            c_int_p,  # l_int32 * tab8
                            ),
        'jbGetComponents': (c_int,
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 components
                            c_int,  # l_int32 maxwidth
                            c_int,  # l_int32 maxheight
                            LPLPBoxa,  # BOXA ** pboxad
                            LPLPPixa,  # PIXA ** ppixad
                            ),
        'pixWordMaskByDilation': (c_int,
                                  LPPix,  # PIX * pixs
                                  LPLPPix,  # PIX ** ppixm
                                  c_int_p,  # l_int32 * psize
                                  LPPixa,  # PIXA * pixadb
                                  ),
        'pixWordBoxesByDilation': (c_int,
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 minwidth
                                   c_int,  # l_int32 minheight
                                   c_int,  # l_int32 maxwidth
                                   c_int,  # l_int32 maxheight
                                   LPLPBoxa,  # BOXA ** pboxa
                                   c_int_p,  # l_int32 * psize
                                   LPPixa,  # PIXA * pixadb
                                   ),
        'jbAccumulateComposites': (LPPixa,  # PIXA *
                                   LPPixaa,  # PIXAA * pixaa
                                   LPLPNuma,  # NUMA ** pna
                                   LPLPPta,  # PTA ** pptat
                                   ),
        'jbTemplatesFromComposites': (LPPixa,  # PIXA *
                                      LPPixa,  # PIXA * pixac
                                      LPNuma,  # NUMA * na
                                      ),
        'readHeaderJp2k': (c_int,
                           c_char_p,  # const char * filename
                           c_int_p,  # l_int32 * pw
                           c_int_p,  # l_int32 * ph
                           c_int_p,  # l_int32 * pbps
                           c_int_p,  # l_int32 * pspp
                           c_int_p,  # l_int32 * pcodec
                           ),
        'freadHeaderJp2k': (c_int,
                            LPFile,  # FILE * fp
                            c_int_p,  # l_int32 * pw
                            c_int_p,  # l_int32 * ph
                            c_int_p,  # l_int32 * pbps
                            c_int_p,  # l_int32 * pspp
                            c_int_p,  # l_int32 * pcodec
                            ),
        'readHeaderMemJp2k': (c_int,
                              c_ubyte_p,  # const l_uint8 * data
                              c_size_t,  # size_t size
                              c_int_p,  # l_int32 * pw
                              c_int_p,  # l_int32 * ph
                              c_int_p,  # l_int32 * pbps
                              c_int_p,  # l_int32 * pspp
                              c_int_p,  # l_int32 * pcodec
                              ),
        'fgetJp2kResolution': (c_int,
                               LPFile,  # FILE * fp
                               c_int_p,  # l_int32 * pxres
                               c_int_p,  # l_int32 * pyres
                               ),
        'pixReadJp2k': (LPPix,  # PIX *
                        c_char_p,  # const char * filename
                        c_uint,  # l_uint32 reduction
                        LPBox,  # BOX * box
                        c_int,  # l_int32 hint
                        c_int,  # l_int32 debug
                        ),
        'pixReadStreamJp2k': (LPPix,  # PIX *
                              LPFile,  # FILE * fp
                              c_uint,  # l_uint32 reduction
                              LPBox,  # BOX * box
                              c_int,  # l_int32 hint
                              c_int,  # l_int32 debug
                              ),
        'pixWriteJp2k': (c_int,
                         c_char_p,  # const char * filename
                         LPPix,  # PIX * pix
                         c_int,  # l_int32 quality
                         c_int,  # l_int32 nlevels
                         c_int,  # l_int32 hint
                         c_int,  # l_int32 debug
                         ),
        'pixWriteStreamJp2k': (c_int,
                               LPFile,  # FILE * fp
                               LPPix,  # PIX * pix
                               c_int,  # l_int32 quality
                               c_int,  # l_int32 nlevels
                               c_int,  # l_int32 codec
                               c_int,  # l_int32 hint
                               c_int,  # l_int32 debug
                               ),
        'pixReadMemJp2k': (LPPix,  # PIX *
                           c_ubyte_p,  # const l_uint8 * data
                           c_size_t,  # size_t size
                           c_uint,  # l_uint32 reduction
                           LPBox,  # BOX * box
                           c_int,  # l_int32 hint
                           c_int,  # l_int32 debug
                           ),
        'pixWriteMemJp2k': (c_int,
                            POINTER(c_ubyte_p),  # l_uint8 ** pdata
                            c_size_t_p,  # size_t * psize
                            LPPix,  # PIX * pix
                            c_int,  # l_int32 quality
                            c_int,  # l_int32 nlevels
                            c_int,  # l_int32 hint
                            c_int,  # l_int32 debug
                            ),
        'pixReadJpeg': (LPPix,  # PIX *
                        c_char_p,  # const char * filename
                        c_int,  # l_int32 cmapflag
                        c_int,  # l_int32 reduction
                        c_int_p,  # l_int32 * pnwarn
                        c_int,  # l_int32 hint
                        ),
        'pixReadStreamJpeg': (LPPix,  # PIX *
                              LPFile,  # FILE * fp
                              c_int,  # l_int32 cmapflag
                              c_int,  # l_int32 reduction
                              c_int_p,  # l_int32 * pnwarn
                              c_int,  # l_int32 hint
                              ),
        'readHeaderJpeg': (c_int,
                           c_char_p,  # const char * filename
                           c_int_p,  # l_int32 * pw
                           c_int_p,  # l_int32 * ph
                           c_int_p,  # l_int32 * pspp
                           c_int_p,  # l_int32 * pycck
                           c_int_p,  # l_int32 * pcmyk
                           ),
        'freadHeaderJpeg': (c_int,
                            LPFile,  # FILE * fp
                            c_int_p,  # l_int32 * pw
                            c_int_p,  # l_int32 * ph
                            c_int_p,  # l_int32 * pspp
                            c_int_p,  # l_int32 * pycck
                            c_int_p,  # l_int32 * pcmyk
                            ),
        'fgetJpegResolution': (c_int,
                               LPFile,  # FILE * fp
                               c_int_p,  # l_int32 * pxres
                               c_int_p,  # l_int32 * pyres
                               ),
        'fgetJpegComment': (c_int,
                            LPFile,  # FILE * fp
                            POINTER(c_ubyte_p),  # l_uint8 ** pcomment
                            ),
        'pixWriteJpeg': (c_int,
                         c_char_p,  # const char * filename
                         LPPix,  # PIX * pix
                         c_int,  # l_int32 quality
                         c_int,  # l_int32 progressive
                         ),
        'pixWriteStreamJpeg': (c_int,
                               LPFile,  # FILE * fp
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 quality
                               c_int,  # l_int32 progressive
                               ),
        'pixReadMemJpeg': (LPPix,  # PIX *
                           c_ubyte_p,  # const l_uint8 * data
                           c_size_t,  # size_t size
                           c_int,  # l_int32 cmflag
                           c_int,  # l_int32 reduction
                           c_int_p,  # l_int32 * pnwarn
                           c_int,  # l_int32 hint
                           ),
        'readHeaderMemJpeg': (c_int,
                              c_ubyte_p,  # const l_uint8 * data
                              c_size_t,  # size_t size
                              c_int_p,  # l_int32 * pw
                              c_int_p,  # l_int32 * ph
                              c_int_p,  # l_int32 * pspp
                              c_int_p,  # l_int32 * pycck
                              c_int_p,  # l_int32 * pcmyk
                              ),
        'readResolutionMemJpeg': (c_int,
                                  c_ubyte_p,  # const l_uint8 * data
                                  c_size_t,  # size_t size
                                  c_int_p,  # l_int32 * pxres
                                  c_int_p,  # l_int32 * pyres
                                  ),
        'pixWriteMemJpeg': (c_int,
                            POINTER(c_ubyte_p),  # l_uint8 ** pdata
                            c_size_t_p,  # size_t * psize
                            LPPix,  # PIX * pix
                            c_int,  # l_int32 quality
                            c_int,  # l_int32 progressive
                            ),
        'pixSetChromaSampling': (c_int,
                                 LPPix,  # PIX * pix
                                 c_int,  # l_int32 sampling
                                 ),
        'create2dFloatArray': (POINTER(c_float_p),
                               c_int,  # l_int32 sy
                               c_int,  # l_int32 sx
                               ),
        'parseStringForNumbers': (LPNuma,  # NUMA *
                                  c_char_p,  # const char * str
                                  c_char_p,  # const char * seps
                                  ),
        'getImagelibVersions': (c_char_p, ),
        'generateBinaryMaze': (LPPix,  # PIX *
                               c_int,  # l_int32 w
                               c_int,  # l_int32 h
                               c_int,  # l_int32 xi
                               c_int,  # l_int32 yi
                               c_float,  # l_float32 wallps
                               c_float,  # l_float32 ranis
                               ),
        'pixSearchBinaryMaze': (LPPta,  # PTA *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 xi
                                c_int,  # l_int32 yi
                                c_int,  # l_int32 xf
                                c_int,  # l_int32 yf
                                LPLPPix,  # PIX ** ppixd
                                ),
        'pixSearchGrayMaze': (LPPta,  # PTA *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 xi
                              c_int,  # l_int32 yi
                              c_int,  # l_int32 xf
                              c_int,  # l_int32 yf
                              LPLPPix,  # PIX ** ppixd
                              ),
        'pixDilateBrick': (LPPix,  # PIX *
                           LPPix,  # PIX * pixd
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 hsize
                           c_int,  # l_int32 vsize
                           ),
        'pixErodeBrick': (LPPix,  # PIX *
                          LPPix,  # PIX * pixd
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 hsize
                          c_int,  # l_int32 vsize
                          ),
        'pixOpenBrick': (LPPix,  # PIX *
                         LPPix,  # PIX * pixd
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 hsize
                         c_int,  # l_int32 vsize
                         ),
        'pixCloseBrick': (LPPix,  # PIX *
                          LPPix,  # PIX * pixd
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 hsize
                          c_int,  # l_int32 vsize
                          ),
        'pixCloseSafeBrick': (LPPix,  # PIX *
                              LPPix,  # PIX * pixd
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 hsize
                              c_int,  # l_int32 vsize
                              ),
        'selectComposableSizes': (c_int,
                                  c_int,  # l_int32 size
                                  c_int_p,  # l_int32 * pfactor1
                                  c_int_p,  # l_int32 * pfactor2
                                  ),
        'pixDilateCompBrick': (LPPix,  # PIX *
                               LPPix,  # PIX * pixd
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 hsize
                               c_int,  # l_int32 vsize
                               ),
        'pixErodeCompBrick': (LPPix,  # PIX *
                              LPPix,  # PIX * pixd
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 hsize
                              c_int,  # l_int32 vsize
                              ),
        'pixOpenCompBrick': (LPPix,  # PIX *
                             LPPix,  # PIX * pixd
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 hsize
                             c_int,  # l_int32 vsize
                             ),
        'pixCloseCompBrick': (LPPix,  # PIX *
                              LPPix,  # PIX * pixd
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 hsize
                              c_int,  # l_int32 vsize
                              ),
        'pixCloseSafeCompBrick': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixd
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 hsize
                                  c_int,  # l_int32 vsize
                                  ),
        'resetMorphBoundaryCondition': (None,
                                        c_int,  # l_int32 bc
                                        ),
        'getMorphBorderPixelColor': (c_uint,
                                     c_int,  # l_int32 type
                                     c_int,  # l_int32 depth
                                     ),
        'pixExtractBoundary': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 type
                               ),
        'pixMorphSequenceMasked': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   LPPix,  # PIX * pixm
                                   c_char_p,  # const char * sequence
                                   c_int,  # l_int32 dispsep
                                   ),
        'pixMorphSequenceByComponent': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixs
                                        c_char_p,  # const char * sequence
                                        c_int,  # l_int32 connectivity
                                        c_int,  # l_int32 minw
                                        c_int,  # l_int32 minh
                                        LPLPBoxa,  # BOXA ** pboxa
                                        ),
        'pixaMorphSequenceByComponent': (LPPixa,  # PIXA *
                                         LPPixa,  # PIXA * pixas
                                         c_char_p,  # const char * sequence
                                         c_int,  # l_int32 minw
                                         c_int,  # l_int32 minh
                                         ),
        'pixMorphSequenceByRegion': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     LPPix,  # PIX * pixm
                                     c_char_p,  # const char * sequence
                                     c_int,  # l_int32 connectivity
                                     c_int,  # l_int32 minw
                                     c_int,  # l_int32 minh
                                     LPLPBoxa,  # BOXA ** pboxa
                                     ),
        'pixaMorphSequenceByRegion': (LPPixa,  # PIXA *
                                      LPPix,  # PIX * pixs
                                      LPPixa,  # PIXA * pixam
                                      c_char_p,  # const char * sequence
                                      c_int,  # l_int32 minw
                                      c_int,  # l_int32 minh
                                      ),
        'pixSelectiveConnCompFill': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 connectivity
                                     c_int,  # l_int32 minw
                                     c_int,  # l_int32 minh
                                     ),
        'pixRemoveMatchedPattern': (c_int,
                                    LPPix,  # PIX * pixs
                                    LPPix,  # PIX * pixp
                                    LPPix,  # PIX * pixe
                                    c_int,  # l_int32 x0
                                    c_int,  # l_int32 y0
                                    c_int,  # l_int32 dsize
                                    ),
        'pixDisplayMatchedPattern': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     LPPix,  # PIX * pixp
                                     LPPix,  # PIX * pixe
                                     c_int,  # l_int32 x0
                                     c_int,  # l_int32 y0
                                     c_uint,  # l_uint32 color
                                     c_float,  # l_float32 scale
                                     c_int,  # l_int32 nlevels
                                     ),
        'pixaExtendByScaling': (LPPixa,  # PIXA *
                                LPPixa,  # PIXA * pixas
                                LPNuma,  # NUMA * nasc
                                c_int,  # l_int32 type
                                c_int,  # l_int32 include
                                ),
        'pixSeedfillMorph': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             LPPix,  # PIX * pixm
                             c_int,  # l_int32 maxiters
                             c_int,  # l_int32 connectivity
                             ),
        'pixRunHistogramMorph': (LPNuma,  # NUMA *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 runtype
                                 c_int,  # l_int32 direction
                                 c_int,  # l_int32 maxsize
                                 ),
        'pixTophat': (LPPix,  # PIX *
                      LPPix,  # PIX * pixs
                      c_int,  # l_int32 hsize
                      c_int,  # l_int32 vsize
                      c_int,  # l_int32 type
                      ),
        'pixHDome': (LPPix,  # PIX *
                     LPPix,  # PIX * pixs
                     c_int,  # l_int32 height
                     c_int,  # l_int32 connectivity
                     ),
        'pixFastTophat': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 xsize
                          c_int,  # l_int32 ysize
                          c_int,  # l_int32 type
                          ),
        'pixMorphGradient': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 hsize
                             c_int,  # l_int32 vsize
                             c_int,  # l_int32 smoothing
                             ),
        'pixaCentroids': (LPPta,  # PTA *
                          LPPixa,  # PIXA * pixa
                          ),
        'pixCentroid': (c_int,
                        LPPix,  # PIX * pix
                        c_int_p,  # l_int32 * centtab
                        c_int_p,  # l_int32 * sumtab
                        c_float_p,  # l_float32 * pxave
                        c_float_p,  # l_float32 * pyave
                        ),
        'pixDilateBrickDwa': (LPPix,  # PIX *
                              LPPix,  # PIX * pixd
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 hsize
                              c_int,  # l_int32 vsize
                              ),
        'pixErodeBrickDwa': (LPPix,  # PIX *
                             LPPix,  # PIX * pixd
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 hsize
                             c_int,  # l_int32 vsize
                             ),
        'pixOpenBrickDwa': (LPPix,  # PIX *
                            LPPix,  # PIX * pixd
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 hsize
                            c_int,  # l_int32 vsize
                            ),
        'pixCloseBrickDwa': (LPPix,  # PIX *
                             LPPix,  # PIX * pixd
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 hsize
                             c_int,  # l_int32 vsize
                             ),
        'pixDilateCompBrickDwa': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixd
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 hsize
                                  c_int,  # l_int32 vsize
                                  ),
        'pixErodeCompBrickDwa': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixd
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 hsize
                                 c_int,  # l_int32 vsize
                                 ),
        'pixOpenCompBrickDwa': (LPPix,  # PIX *
                                LPPix,  # PIX * pixd
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 hsize
                                c_int,  # l_int32 vsize
                                ),
        'pixCloseCompBrickDwa': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixd
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 hsize
                                 c_int,  # l_int32 vsize
                                 ),
        'pixDilateCompBrickExtendDwa': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixd
                                        LPPix,  # PIX * pixs
                                        c_int,  # l_int32 hsize
                                        c_int,  # l_int32 vsize
                                        ),
        'pixErodeCompBrickExtendDwa': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixd
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 hsize
                                       c_int,  # l_int32 vsize
                                       ),
        'pixOpenCompBrickExtendDwa': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixd
                                      LPPix,  # PIX * pixs
                                      c_int,  # l_int32 hsize
                                      c_int,  # l_int32 vsize
                                      ),
        'pixCloseCompBrickExtendDwa': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixd
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 hsize
                                       c_int,  # l_int32 vsize
                                       ),
        'getExtendedCompositeParameters': (c_int,
                                           c_int,  # l_int32 size
                                           c_int_p,  # l_int32 * pn
                                           c_int_p,  # l_int32 * pextra
                                           # l_int32 * pactualsize
                                           c_int_p,
                                           ),
        'pixMorphSequence': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_char_p,  # const char * sequence
                             c_int,  # l_int32 dispsep
                             ),
        'pixMorphCompSequence': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_char_p,  # const char * sequence
                                 c_int,  # l_int32 dispsep
                                 ),
        'pixMorphSequenceDwa': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_char_p,  # const char * sequence
                                c_int,  # l_int32 dispsep
                                ),
        'pixMorphCompSequenceDwa': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_char_p,  # const char * sequence
                                    c_int,  # l_int32 dispsep
                                    ),
        'morphSequenceVerify': (c_int,
                                LPSarray,  # SARRAY * sa
                                ),
        'pixGrayMorphSequence': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_char_p,  # const char * sequence
                                 c_int,  # l_int32 dispsep
                                 c_int,  # l_int32 dispy
                                 ),
        'pixColorMorphSequence': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_char_p,  # const char * sequence
                                  c_int,  # l_int32 dispsep
                                  c_int,  # l_int32 dispy
                                  ),
        'numaCreate': (LPNuma,  # NUMA *
                       c_int,  # l_int32 n
                       ),
        'numaCreateFromIArray': (LPNuma,  # NUMA *
                                 c_int_p,  # l_int32 * iarray
                                 c_int,  # l_int32 size
                                 ),
        'numaCreateFromFArray': (LPNuma,  # NUMA *
                                 c_float_p,  # l_float32 * farray
                                 c_int,  # l_int32 size
                                 c_int,  # l_int32 copyflag
                                 ),
        'numaCreateFromString': (LPNuma,  # NUMA *
                                 c_char_p,  # const char * str
                                 ),
        'numaDestroy': (None,
                        LPLPNuma,  # NUMA ** pna
                        ),
        'numaCopy': (LPNuma,  # NUMA *
                     LPNuma,  # NUMA * na
                     ),
        'numaClone': (LPNuma,  # NUMA *
                      LPNuma,  # NUMA * na
                      ),
        'numaEmpty': (c_int,
                      LPNuma,  # NUMA * na
                      ),
        'numaAddNumber': (c_int,
                          LPNuma,  # NUMA * na
                          c_float,  # l_float32 val
                          ),
        'numaInsertNumber': (c_int,
                             LPNuma,  # NUMA * na
                             c_int,  # l_int32 index
                             c_float,  # l_float32 val
                             ),
        'numaRemoveNumber': (c_int,
                             LPNuma,  # NUMA * na
                             c_int,  # l_int32 index
                             ),
        'numaReplaceNumber': (c_int,
                              LPNuma,  # NUMA * na
                              c_int,  # l_int32 index
                              c_float,  # l_float32 val
                              ),
        'numaGetCount': (c_int,
                         LPNuma,  # NUMA * na
                         ),
        'numaSetCount': (c_int,
                         LPNuma,  # NUMA * na
                         c_int,  # l_int32 newcount
                         ),
        'numaGetFValue': (c_int,
                          LPNuma,  # NUMA * na
                          c_int,  # l_int32 index
                          c_float_p,  # l_float32 * pval
                          ),
        'numaGetIValue': (c_int,
                          LPNuma,  # NUMA * na
                          c_int,  # l_int32 index
                          c_int_p,  # l_int32 * pival
                          ),
        'numaSetValue': (c_int,
                         LPNuma,  # NUMA * na
                         c_int,  # l_int32 index
                         c_float,  # l_float32 val
                         ),
        'numaShiftValue': (c_int,
                           LPNuma,  # NUMA * na
                           c_int,  # l_int32 index
                           c_float,  # l_float32 diff
                           ),
        'numaGetIArray': (c_int_p,
                          LPNuma,  # NUMA * na
                          ),
        'numaGetFArray': (c_float_p,
                          LPNuma,  # NUMA * na
                          c_int,  # l_int32 copyflag
                          ),
        'numaGetRefcount': (c_int,
                            LPNuma,  # NUMA * na
                            ),
        'numaChangeRefcount': (c_int,
                               LPNuma,  # NUMA * na
                               c_int,  # l_int32 delta
                               ),
        'numaGetParameters': (c_int,
                              LPNuma,  # NUMA * na
                              c_float_p,  # l_float32 * pstartx
                              c_float_p,  # l_float32 * pdelx
                              ),
        'numaSetParameters': (c_int,
                              LPNuma,  # NUMA * na
                              c_float,  # l_float32 startx
                              c_float,  # l_float32 delx
                              ),
        'numaCopyParameters': (c_int,
                               LPNuma,  # NUMA * nad
                               LPNuma,  # NUMA * nas
                               ),
        'numaConvertToSarray': (LPSarray,  # SARRAY *
                                LPNuma,  # NUMA * na
                                c_int,  # l_int32 size1
                                c_int,  # l_int32 size2
                                c_int,  # l_int32 addzeros
                                c_int,  # l_int32 type
                                ),
        'numaRead': (LPNuma,  # NUMA *
                     c_char_p,  # const char * filename
                     ),
        'numaReadStream': (LPNuma,  # NUMA *
                           LPFile,  # FILE * fp
                           ),
        'numaReadMem': (LPNuma,  # NUMA *
                        c_ubyte_p,  # const l_uint8 * data
                        c_size_t,  # size_t size
                        ),
        'numaWriteDebug': (c_int,
                           c_char_p,  # const char * filename
                           LPNuma,  # NUMA * na
                           ),
        'numaWrite': (c_int,
                      c_char_p,  # const char * filename
                      LPNuma,  # NUMA * na
                      ),
        'numaWriteStream': (c_int,
                            LPFile,  # FILE * fp
                            LPNuma,  # NUMA * na
                            ),
        'numaWriteStderr': (c_int,
                            LPNuma,  # NUMA * na
                            ),
        'numaWriteMem': (c_int,
                         POINTER(c_ubyte_p),  # l_uint8 ** pdata
                         c_size_t_p,  # size_t * psize
                         LPNuma,  # NUMA * na
                         ),
        'numaaCreate': (LPNumaa,  # NUMAA *
                        c_int,  # l_int32 n
                        ),
        'numaaCreateFull': (LPNumaa,  # NUMAA *
                            c_int,  # l_int32 nptr
                            c_int,  # l_int32 n
                            ),
        'numaaTruncate': (c_int,
                          LPNumaa,  # NUMAA * naa
                          ),
        'numaaDestroy': (None,
                         LPLPNumaa,  # NUMAA ** pnaa
                         ),
        'numaaAddNuma': (c_int,
                         LPNumaa,  # NUMAA * naa
                         LPNuma,  # NUMA * na
                         c_int,  # l_int32 copyflag
                         ),
        'numaaGetCount': (c_int,
                          LPNumaa,  # NUMAA * naa
                          ),
        'numaaGetNumaCount': (c_int,
                              LPNumaa,  # NUMAA * naa
                              c_int,  # l_int32 index
                              ),
        'numaaGetNumberCount': (c_int,
                                LPNumaa,  # NUMAA * naa
                                ),
        'numaaGetPtrArray': (LPLPNuma,  # NUMA *
                             LPNumaa,  # NUMAA * naa
                             ),
        'numaaGetNuma': (LPNuma,  # NUMA *
                         LPNumaa,  # NUMAA * naa
                         c_int,  # l_int32 index
                         c_int,  # l_int32 accessflag
                         ),
        'numaaReplaceNuma': (c_int,
                             LPNumaa,  # NUMAA * naa
                             c_int,  # l_int32 index
                             LPNuma,  # NUMA * na
                             ),
        'numaaGetValue': (c_int,
                          LPNumaa,  # NUMAA * naa
                          c_int,  # l_int32 i
                          c_int,  # l_int32 j
                          c_float_p,  # l_float32 * pfval
                          c_int_p,  # l_int32 * pival
                          ),
        'numaaAddNumber': (c_int,
                           LPNumaa,  # NUMAA * naa
                           c_int,  # l_int32 index
                           c_float,  # l_float32 val
                           ),
        'numaaRead': (LPNumaa,  # NUMAA *
                      c_char_p,  # const char * filename
                      ),
        'numaaReadStream': (LPNumaa,  # NUMAA *
                            LPFile,  # FILE * fp
                            ),
        'numaaReadMem': (LPNumaa,  # NUMAA *
                         c_ubyte_p,  # const l_uint8 * data
                         c_size_t,  # size_t size
                         ),
        'numaaWrite': (c_int,
                       c_char_p,  # const char * filename
                       LPNumaa,  # NUMAA * naa
                       ),
        'numaaWriteStream': (c_int,
                             LPFile,  # FILE * fp
                             LPNumaa,  # NUMAA * naa
                             ),
        'numaaWriteMem': (c_int,
                          POINTER(c_ubyte_p),  # l_uint8 ** pdata
                          c_size_t_p,  # size_t * psize
                          LPNumaa,  # NUMAA * naa
                          ),
        'numaArithOp': (LPNuma,  # NUMA *
                        LPNuma,  # NUMA * nad
                        LPNuma,  # NUMA * na1
                        LPNuma,  # NUMA * na2
                        c_int,  # l_int32 op
                        ),
        'numaLogicalOp': (LPNuma,  # NUMA *
                          LPNuma,  # NUMA * nad
                          LPNuma,  # NUMA * na1
                          LPNuma,  # NUMA * na2
                          c_int,  # l_int32 op
                          ),
        'numaInvert': (LPNuma,  # NUMA *
                       LPNuma,  # NUMA * nad
                       LPNuma,  # NUMA * nas
                       ),
        'numaSimilar': (c_int,
                        LPNuma,  # NUMA * na1
                        LPNuma,  # NUMA * na2
                        c_float,  # l_float32 maxdiff
                        c_int_p,  # l_int32 * psimilar
                        ),
        'numaAddToNumber': (c_int,
                            LPNuma,  # NUMA * na
                            c_int,  # l_int32 index
                            c_float,  # l_float32 val
                            ),
        'numaGetMin': (c_int,
                       LPNuma,  # NUMA * na
                       c_float_p,  # l_float32 * pminval
                       c_int_p,  # l_int32 * piminloc
                       ),
        'numaGetMax': (c_int,
                       LPNuma,  # NUMA * na
                       c_float_p,  # l_float32 * pmaxval
                       c_int_p,  # l_int32 * pimaxloc
                       ),
        'numaGetSum': (c_int,
                       LPNuma,  # NUMA * na
                       c_float_p,  # l_float32 * psum
                       ),
        'numaGetPartialSums': (LPNuma,  # NUMA *
                               LPNuma,  # NUMA * na
                               ),
        'numaGetSumOnInterval': (c_int,
                                 LPNuma,  # NUMA * na
                                 c_int,  # l_int32 first
                                 c_int,  # l_int32 last
                                 c_float_p,  # l_float32 * psum
                                 ),
        'numaHasOnlyIntegers': (c_int,
                                LPNuma,  # NUMA * na
                                c_int_p,  # l_int32 * pallints
                                ),
        'numaGetMean': (c_int,
                        LPNuma,  # NUMA * na
                        c_float_p,  # l_float32 * pave
                        ),
        'numaGetMeanAbsval': (c_int,
                              LPNuma,  # NUMA * na
                              c_float_p,  # l_float32 * paveabs
                              ),
        'numaSubsample': (LPNuma,  # NUMA *
                          LPNuma,  # NUMA * nas
                          c_int,  # l_int32 subfactor
                          ),
        'numaMakeDelta': (LPNuma,  # NUMA *
                          LPNuma,  # NUMA * nas
                          ),
        'numaMakeSequence': (LPNuma,  # NUMA *
                             c_float,  # l_float32 startval
                             c_float,  # l_float32 increment
                             c_int,  # l_int32 size
                             ),
        'numaMakeConstant': (LPNuma,  # NUMA *
                             c_float,  # l_float32 val
                             c_int,  # l_int32 size
                             ),
        'numaMakeAbsval': (LPNuma,  # NUMA *
                           LPNuma,  # NUMA * nad
                           LPNuma,  # NUMA * nas
                           ),
        'numaAddBorder': (LPNuma,  # NUMA *
                          LPNuma,  # NUMA * nas
                          c_int,  # l_int32 left
                          c_int,  # l_int32 right
                          c_float,  # l_float32 val
                          ),
        'numaAddSpecifiedBorder': (LPNuma,  # NUMA *
                                   LPNuma,  # NUMA * nas
                                   c_int,  # l_int32 left
                                   c_int,  # l_int32 right
                                   c_int,  # l_int32 type
                                   ),
        'numaRemoveBorder': (LPNuma,  # NUMA *
                             LPNuma,  # NUMA * nas
                             c_int,  # l_int32 left
                             c_int,  # l_int32 right
                             ),
        'numaCountNonzeroRuns': (c_int,
                                 LPNuma,  # NUMA * na
                                 c_int_p,  # l_int32 * pcount
                                 ),
        'numaGetNonzeroRange': (c_int,
                                LPNuma,  # NUMA * na
                                c_float,  # l_float32 eps
                                c_int_p,  # l_int32 * pfirst
                                c_int_p,  # l_int32 * plast
                                ),
        'numaGetCountRelativeToZero': (c_int,
                                       LPNuma,  # NUMA * na
                                       c_int,  # l_int32 type
                                       c_int_p,  # l_int32 * pcount
                                       ),
        'numaClipToInterval': (LPNuma,  # NUMA *
                               LPNuma,  # NUMA * nas
                               c_int,  # l_int32 first
                               c_int,  # l_int32 last
                               ),
        'numaMakeThresholdIndicator': (LPNuma,  # NUMA *
                                       LPNuma,  # NUMA * nas
                                       c_float,  # l_float32 thresh
                                       c_int,  # l_int32 type
                                       ),
        'numaUniformSampling': (LPNuma,  # NUMA *
                                LPNuma,  # NUMA * nas
                                c_int,  # l_int32 nsamp
                                ),
        'numaReverse': (LPNuma,  # NUMA *
                        LPNuma,  # NUMA * nad
                        LPNuma,  # NUMA * nas
                        ),
        'numaLowPassIntervals': (LPNuma,  # NUMA *
                                 LPNuma,  # NUMA * nas
                                 c_float,  # l_float32 thresh
                                 c_float,  # l_float32 maxn
                                 ),
        'numaThresholdEdges': (LPNuma,  # NUMA *
                               LPNuma,  # NUMA * nas
                               c_float,  # l_float32 thresh1
                               c_float,  # l_float32 thresh2
                               c_float,  # l_float32 maxn
                               ),
        'numaGetSpanValues': (c_int,
                              LPNuma,  # NUMA * na
                              c_int,  # l_int32 span
                              c_int_p,  # l_int32 * pstart
                              c_int_p,  # l_int32 * pend
                              ),
        'numaGetEdgeValues': (c_int,
                              LPNuma,  # NUMA * na
                              c_int,  # l_int32 edge
                              c_int_p,  # l_int32 * pstart
                              c_int_p,  # l_int32 * pend
                              c_int_p,  # l_int32 * psign
                              ),
        'numaInterpolateEqxVal': (c_int,
                                  c_float,  # l_float32 startx
                                  c_float,  # l_float32 deltax
                                  LPNuma,  # NUMA * nay
                                  c_int,  # l_int32 type
                                  c_float,  # l_float32 xval
                                  c_float_p,  # l_float32 * pyval
                                  ),
        'numaInterpolateArbxVal': (c_int,
                                   LPNuma,  # NUMA * nax
                                   LPNuma,  # NUMA * nay
                                   c_int,  # l_int32 type
                                   c_float,  # l_float32 xval
                                   c_float_p,  # l_float32 * pyval
                                   ),
        'numaInterpolateEqxInterval': (c_int,
                                       c_float,  # l_float32 startx
                                       c_float,  # l_float32 deltax
                                       LPNuma,  # NUMA * nasy
                                       c_int,  # l_int32 type
                                       c_float,  # l_float32 x0
                                       c_float,  # l_float32 x1
                                       c_int,  # l_int32 npts
                                       LPLPNuma,  # NUMA ** pnax
                                       LPLPNuma,  # NUMA ** pnay
                                       ),
        'numaInterpolateArbxInterval': (c_int,
                                        LPNuma,  # NUMA * nax
                                        LPNuma,  # NUMA * nay
                                        c_int,  # l_int32 type
                                        c_float,  # l_float32 x0
                                        c_float,  # l_float32 x1
                                        c_int,  # l_int32 npts
                                        LPLPNuma,  # NUMA ** pnadx
                                        LPLPNuma,  # NUMA ** pnady
                                        ),
        'numaFitMax': (c_int,
                       LPNuma,  # NUMA * na
                       c_float_p,  # l_float32 * pmaxval
                       LPNuma,  # NUMA * naloc
                       c_float_p,  # l_float32 * pmaxloc
                       ),
        'numaDifferentiateInterval': (c_int,
                                      LPNuma,  # NUMA * nax
                                      LPNuma,  # NUMA * nay
                                      c_float,  # l_float32 x0
                                      c_float,  # l_float32 x1
                                      c_int,  # l_int32 npts
                                      LPLPNuma,  # NUMA ** pnadx
                                      LPLPNuma,  # NUMA ** pnady
                                      ),
        'numaIntegrateInterval': (c_int,
                                  LPNuma,  # NUMA * nax
                                  LPNuma,  # NUMA * nay
                                  c_float,  # l_float32 x0
                                  c_float,  # l_float32 x1
                                  c_int,  # l_int32 npts
                                  c_float_p,  # l_float32 * psum
                                  ),
        'numaSortGeneral': (c_int,
                            LPNuma,  # NUMA * na
                            LPLPNuma,  # NUMA ** pnasort
                            LPLPNuma,  # NUMA ** pnaindex
                            LPLPNuma,  # NUMA ** pnainvert
                            c_int,  # l_int32 sortorder
                            c_int,  # l_int32 sorttype
                            ),
        'numaSortAutoSelect': (LPNuma,  # NUMA *
                               LPNuma,  # NUMA * nas
                               c_int,  # l_int32 sortorder
                               ),
        'numaSortIndexAutoSelect': (LPNuma,  # NUMA *
                                    LPNuma,  # NUMA * nas
                                    c_int,  # l_int32 sortorder
                                    ),
        'numaChooseSortType': (c_int,
                               LPNuma,  # NUMA * nas
                               ),
        'numaSort': (LPNuma,  # NUMA *
                     LPNuma,  # NUMA * naout
                     LPNuma,  # NUMA * nain
                     c_int,  # l_int32 sortorder
                     ),
        'numaBinSort': (LPNuma,  # NUMA *
                        LPNuma,  # NUMA * nas
                        c_int,  # l_int32 sortorder
                        ),
        'numaGetSortIndex': (LPNuma,  # NUMA *
                             LPNuma,  # NUMA * na
                             c_int,  # l_int32 sortorder
                             ),
        'numaGetBinSortIndex': (LPNuma,  # NUMA *
                                LPNuma,  # NUMA * nas
                                c_int,  # l_int32 sortorder
                                ),
        'numaSortByIndex': (LPNuma,  # NUMA *
                            LPNuma,  # NUMA * nas
                            LPNuma,  # NUMA * naindex
                            ),
        'numaIsSorted': (c_int,
                         LPNuma,  # NUMA * nas
                         c_int,  # l_int32 sortorder
                         c_int_p,  # l_int32 * psorted
                         ),
        'numaSortPair': (c_int,
                         LPNuma,  # NUMA * nax
                         LPNuma,  # NUMA * nay
                         c_int,  # l_int32 sortorder
                         LPLPNuma,  # NUMA ** pnasx
                         LPLPNuma,  # NUMA ** pnasy
                         ),
        'numaInvertMap': (LPNuma,  # NUMA *
                          LPNuma,  # NUMA * nas
                          ),
        'numaAddSorted': (c_int,
                          LPNuma,  # NUMA * na
                          c_float,  # l_float32 val
                          ),
        'numaFindSortedLoc': (c_int,
                              LPNuma,  # NUMA * na
                              c_float,  # l_float32 val
                              c_int_p,  # l_int32 * pindex
                              ),
        'numaPseudorandomSequence': (LPNuma,  # NUMA *
                                     c_int,  # l_int32 size
                                     c_int,  # l_int32 seed
                                     ),
        'numaRandomPermutation': (LPNuma,  # NUMA *
                                  LPNuma,  # NUMA * nas
                                  c_int,  # l_int32 seed
                                  ),
        'numaGetRankValue': (c_int,
                             LPNuma,  # NUMA * na
                             c_float,  # l_float32 fract
                             LPNuma,  # NUMA * nasort
                             c_int,  # l_int32 usebins
                             c_float_p,  # l_float32 * pval
                             ),
        'numaGetMedian': (c_int,
                          LPNuma,  # NUMA * na
                          c_float_p,  # l_float32 * pval
                          ),
        'numaGetBinnedMedian': (c_int,
                                LPNuma,  # NUMA * na
                                c_int_p,  # l_int32 * pval
                                ),
        'numaGetMeanDevFromMedian': (c_int,
                                     LPNuma,  # NUMA * na
                                     c_float,  # l_float32 med
                                     c_float_p,  # l_float32 * pdev
                                     ),
        'numaGetMedianDevFromMedian': (c_int,
                                       LPNuma,  # NUMA * na
                                       c_float_p,  # l_float32 * pmed
                                       c_float_p,  # l_float32 * pdev
                                       ),
        'numaGetMode': (c_int,
                        LPNuma,  # NUMA * na
                        c_float_p,  # l_float32 * pval
                        c_int_p,  # l_int32 * pcount
                        ),
        'numaJoin': (c_int,
                     LPNuma,  # NUMA * nad
                     LPNuma,  # NUMA * nas
                     c_int,  # l_int32 istart
                     c_int,  # l_int32 iend
                     ),
        'numaaJoin': (c_int,
                      LPNumaa,  # NUMAA * naad
                      LPNumaa,  # NUMAA * naas
                      c_int,  # l_int32 istart
                      c_int,  # l_int32 iend
                      ),
        'numaaFlattenToNuma': (LPNuma,  # NUMA *
                               LPNumaa,  # NUMAA * naa
                               ),
        'numaErode': (LPNuma,  # NUMA *
                      LPNuma,  # NUMA * nas
                      c_int,  # l_int32 size
                      ),
        'numaDilate': (LPNuma,  # NUMA *
                       LPNuma,  # NUMA * nas
                       c_int,  # l_int32 size
                       ),
        'numaOpen': (LPNuma,  # NUMA *
                     LPNuma,  # NUMA * nas
                     c_int,  # l_int32 size
                     ),
        'numaClose': (LPNuma,  # NUMA *
                      LPNuma,  # NUMA * nas
                      c_int,  # l_int32 size
                      ),
        'numaTransform': (LPNuma,  # NUMA *
                          LPNuma,  # NUMA * nas
                          c_float,  # l_float32 shift
                          c_float,  # l_float32 scale
                          ),
        'numaSimpleStats': (c_int,
                            LPNuma,  # NUMA * na
                            c_int,  # l_int32 first
                            c_int,  # l_int32 last
                            c_float_p,  # l_float32 * pmean
                            c_float_p,  # l_float32 * pvar
                            c_float_p,  # l_float32 * prvar
                            ),
        'numaWindowedStats': (c_int,
                              LPNuma,  # NUMA * nas
                              c_int,  # l_int32 wc
                              LPLPNuma,  # NUMA ** pnam
                              LPLPNuma,  # NUMA ** pnams
                              LPLPNuma,  # NUMA ** pnav
                              LPLPNuma,  # NUMA ** pnarv
                              ),
        'numaWindowedMean': (LPNuma,  # NUMA *
                             LPNuma,  # NUMA * nas
                             c_int,  # l_int32 wc
                             ),
        'numaWindowedMeanSquare': (LPNuma,  # NUMA *
                                   LPNuma,  # NUMA * nas
                                   c_int,  # l_int32 wc
                                   ),
        'numaWindowedVariance': (c_int,
                                 LPNuma,  # NUMA * nam
                                 LPNuma,  # NUMA * nams
                                 LPLPNuma,  # NUMA ** pnav
                                 LPLPNuma,  # NUMA ** pnarv
                                 ),
        'numaWindowedMedian': (LPNuma,  # NUMA *
                               LPNuma,  # NUMA * nas
                               c_int,  # l_int32 halfwin
                               ),
        'numaConvertToInt': (LPNuma,  # NUMA *
                             LPNuma,  # NUMA * nas
                             ),
        'numaMakeHistogram': (LPNuma,  # NUMA *
                              LPNuma,  # NUMA * na
                              c_int,  # l_int32 maxbins
                              c_int_p,  # l_int32 * pbinsize
                              c_int_p,  # l_int32 * pbinstart
                              ),
        'numaMakeHistogramAuto': (LPNuma,  # NUMA *
                                  LPNuma,  # NUMA * na
                                  c_int,  # l_int32 maxbins
                                  ),
        'numaMakeHistogramClipped': (LPNuma,  # NUMA *
                                     LPNuma,  # NUMA * na
                                     c_float,  # l_float32 binsize
                                     c_float,  # l_float32 maxsize
                                     ),
        'numaRebinHistogram': (LPNuma,  # NUMA *
                               LPNuma,  # NUMA * nas
                               c_int,  # l_int32 newsize
                               ),
        'numaNormalizeHistogram': (LPNuma,  # NUMA *
                                   LPNuma,  # NUMA * nas
                                   c_float,  # l_float32 tsum
                                   ),
        'numaGetStatsUsingHistogram': (c_int,
                                       LPNuma,  # NUMA * na
                                       c_int,  # l_int32 maxbins
                                       c_float_p,  # l_float32 * pmin
                                       c_float_p,  # l_float32 * pmax
                                       c_float_p,  # l_float32 * pmean
                                       # l_float32 * pvariance
                                       c_float_p,
                                       # l_float32 * pmedian
                                       c_float_p,
                                       c_float,  # l_float32 rank
                                       c_float_p,  # l_float32 * prval
                                       LPLPNuma,  # NUMA ** phisto
                                       ),
        'numaGetHistogramStats': (c_int,
                                  LPNuma,  # NUMA * nahisto
                                  c_float,  # l_float32 startx
                                  c_float,  # l_float32 deltax
                                  c_float_p,  # l_float32 * pxmean
                                  c_float_p,  # l_float32 * pxmedian
                                  c_float_p,  # l_float32 * pxmode
                                  c_float_p,  # l_float32 * pxvariance
                                  ),
        'numaGetHistogramStatsOnInterval': (c_int,
                                            LPNuma,  # NUMA * nahisto
                                            c_float,  # l_float32 startx
                                            c_float,  # l_float32 deltax
                                            c_int,  # l_int32 ifirst
                                            c_int,  # l_int32 ilast
                                            # l_float32 * pxmean
                                            c_float_p,
                                            # l_float32 * pxmedian
                                            c_float_p,
                                            # l_float32 * pxmode
                                            c_float_p,
                                            # l_float32 * pxvariance
                                            c_float_p,
                                            ),
        'numaMakeRankFromHistogram': (c_int,
                                      c_float,  # l_float32 startx
                                      c_float,  # l_float32 deltax
                                      LPNuma,  # NUMA * nasy
                                      c_int,  # l_int32 npts
                                      LPLPNuma,  # NUMA ** pnax
                                      LPLPNuma,  # NUMA ** pnay
                                      ),
        'numaHistogramGetRankFromVal': (c_int,
                                        LPNuma,  # NUMA * na
                                        c_float,  # l_float32 rval
                                        c_float_p,  # l_float32 * prank
                                        ),
        'numaHistogramGetValFromRank': (c_int,
                                        LPNuma,  # NUMA * na
                                        c_float,  # l_float32 rank
                                        c_float_p,  # l_float32 * prval
                                        ),
        'numaDiscretizeSortedInBins': (c_int,
                                       LPNuma,  # NUMA * na
                                       c_int,  # l_int32 nbins
                                       LPLPNuma,  # NUMA ** pnabinval
                                       ),
        'numaDiscretizeHistoInBins': (c_int,
                                      LPNuma,  # NUMA * na
                                      c_int,  # l_int32 nbins
                                      LPLPNuma,  # NUMA ** pnabinval
                                      LPLPNuma,  # NUMA ** pnarank
                                      ),
        'numaGetRankBinValues': (c_int,
                                 LPNuma,  # NUMA * na
                                 c_int,  # l_int32 nbins
                                 LPLPNuma,  # NUMA ** pnam
                                 ),
        'numaGetUniformBinSizes': (LPNuma,  # NUMA *
                                   c_int,  # l_int32 ntotal
                                   c_int,  # l_int32 nbins
                                   ),
        'numaSplitDistribution': (c_int,
                                  LPNuma,  # NUMA * na
                                  c_float,  # l_float32 scorefract
                                  c_int_p,  # l_int32 * psplitindex
                                  c_float_p,  # l_float32 * pave1
                                  c_float_p,  # l_float32 * pave2
                                  c_float_p,  # l_float32 * pnum1
                                  c_float_p,  # l_float32 * pnum2
                                  LPLPNuma,  # NUMA ** pnascore
                                  ),
        'grayHistogramsToEMD': (c_int,
                                LPNumaa,  # NUMAA * naa1
                                LPNumaa,  # NUMAA * naa2
                                LPLPNuma,  # NUMA ** pnad
                                ),
        'numaEarthMoverDistance': (c_int,
                                   LPNuma,  # NUMA * na1
                                   LPNuma,  # NUMA * na2
                                   c_float_p,  # l_float32 * pdist
                                   ),
        'grayInterHistogramStats': (c_int,
                                    LPNumaa,  # NUMAA * naa
                                    c_int,  # l_int32 wc
                                    LPLPNuma,  # NUMA ** pnam
                                    LPLPNuma,  # NUMA ** pnams
                                    LPLPNuma,  # NUMA ** pnav
                                    LPLPNuma,  # NUMA ** pnarv
                                    ),
        'numaFindPeaks': (LPNuma,  # NUMA *
                          LPNuma,  # NUMA * nas
                          c_int,  # l_int32 nmax
                          c_float,  # l_float32 fract1
                          c_float,  # l_float32 fract2
                          ),
        'numaFindExtrema': (LPNuma,  # NUMA *
                            LPNuma,  # NUMA * nas
                            c_float,  # l_float32 delta
                            LPLPNuma,  # NUMA ** pnav
                            ),
        'numaFindLocForThreshold': (c_int,
                                    LPNuma,  # NUMA * na
                                    c_int,  # l_int32 skip
                                    c_int_p,  # l_int32 * pthresh
                                    c_float_p,  # l_float32 * pfract
                                    ),
        'numaCountReversals': (c_int,
                               LPNuma,  # NUMA * nas
                               c_float,  # l_float32 minreversal
                               c_int_p,  # l_int32 * pnr
                               c_float_p,  # l_float32 * prd
                               ),
        'numaSelectCrossingThreshold': (c_int,
                                        LPNuma,  # NUMA * nax
                                        LPNuma,  # NUMA * nay
                                        c_float,  # l_float32 estthresh
                                        # l_float32 * pbestthresh
                                        c_float_p,
                                        ),
        'numaCrossingsByThreshold': (LPNuma,  # NUMA *
                                     LPNuma,  # NUMA * nax
                                     LPNuma,  # NUMA * nay
                                     c_float,  # l_float32 thresh
                                     ),
        'numaCrossingsByPeaks': (LPNuma,  # NUMA *
                                 LPNuma,  # NUMA * nax
                                 LPNuma,  # NUMA * nay
                                 c_float,  # l_float32 delta
                                 ),
        'numaEvalBestHaarParameters': (c_int,
                                       LPNuma,  # NUMA * nas
                                       c_float,  # l_float32 relweight
                                       c_int,  # l_int32 nwidth
                                       c_int,  # l_int32 nshift
                                       c_float,  # l_float32 minwidth
                                       c_float,  # l_float32 maxwidth
                                       # l_float32 * pbestwidth
                                       c_float_p,
                                       # l_float32 * pbestshift
                                       c_float_p,
                                       # l_float32 * pbestscore
                                       c_float_p,
                                       ),
        'numaEvalHaarSum': (c_int,
                            LPNuma,  # NUMA * nas
                            c_float,  # l_float32 width
                            c_float,  # l_float32 shift
                            c_float,  # l_float32 relweight
                            c_float_p,  # l_float32 * pscore
                            ),
        'genConstrainedNumaInRange': (LPNuma,  # NUMA *
                                      c_int,  # l_int32 first
                                      c_int,  # l_int32 last
                                      c_int,  # l_int32 nmax
                                      c_int,  # l_int32 use_pairs
                                      ),
        'pixGetRegionsBinary': (c_int,
                                LPPix,  # PIX * pixs
                                LPLPPix,  # PIX ** ppixhm
                                LPLPPix,  # PIX ** ppixtm
                                LPLPPix,  # PIX ** ppixtb
                                LPPixa,  # PIXA * pixadb
                                ),
        'pixGenHalftoneMask': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               LPLPPix,  # PIX ** ppixtext
                               c_int_p,  # l_int32 * phtfound
                               c_int,  # l_int32 debug
                               ),
        'pixGenerateHalftoneMask': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    LPLPPix,  # PIX ** ppixtext
                                    c_int_p,  # l_int32 * phtfound
                                    LPPixa,  # PIXA * pixadb
                                    ),
        'pixGenTextlineMask': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               LPLPPix,  # PIX ** ppixvws
                               c_int_p,  # l_int32 * ptlfound
                               LPPixa,  # PIXA * pixadb
                               ),
        'pixGenTextblockMask': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                LPPix,  # PIX * pixvws
                                LPPixa,  # PIXA * pixadb
                                ),
        'pixFindPageForeground': (LPBox,  # BOX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 threshold
                                  c_int,  # l_int32 mindist
                                  c_int,  # l_int32 erasedist
                                  c_int,  # l_int32 showmorph
                                  LPPixaComp,  # PIXAC * pixac
                                  ),
        'pixSplitIntoCharacters': (c_int,
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 minw
                                   c_int,  # l_int32 minh
                                   LPLPBoxa,  # BOXA ** pboxa
                                   LPLPPixa,  # PIXA ** ppixa
                                   LPLPPix,  # PIX ** ppixdebug
                                   ),
        'pixSplitComponentWithProfile': (LPBoxa,  # BOXA *
                                         LPPix,  # PIX * pixs
                                         c_int,  # l_int32 delta
                                         c_int,  # l_int32 mindel
                                         LPLPPix,  # PIX ** ppixdebug
                                         ),
        'pixExtractTextlines': (LPPixa,  # PIXA *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 maxw
                                c_int,  # l_int32 maxh
                                c_int,  # l_int32 minw
                                c_int,  # l_int32 minh
                                c_int,  # l_int32 adjw
                                c_int,  # l_int32 adjh
                                LPPixa,  # PIXA * pixadb
                                ),
        'pixExtractRawTextlines': (LPPixa,  # PIXA *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 maxw
                                   c_int,  # l_int32 maxh
                                   c_int,  # l_int32 adjw
                                   c_int,  # l_int32 adjh
                                   LPPixa,  # PIXA * pixadb
                                   ),
        'pixCountTextColumns': (c_int,
                                LPPix,  # PIX * pixs
                                c_float,  # l_float32 deltafract
                                c_float,  # l_float32 peakfract
                                c_float,  # l_float32 clipfract
                                c_int_p,  # l_int32 * pncols
                                LPPixa,  # PIXA * pixadb
                                ),
        'pixDecideIfText': (c_int,
                            LPPix,  # PIX * pixs
                            LPBox,  # BOX * box
                            c_int_p,  # l_int32 * pistext
                            LPPixa,  # PIXA * pixadb
                            ),
        'pixFindThreshFgExtent': (c_int,
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 thresh
                                  c_int_p,  # l_int32 * ptop
                                  c_int_p,  # l_int32 * pbot
                                  ),
        'pixDecideIfTable': (c_int,
                             LPPix,  # PIX * pixs
                             LPBox,  # BOX * box
                             c_int,  # l_int32 orient
                             c_int_p,  # l_int32 * pscore
                             LPPixa,  # PIXA * pixadb
                             ),
        'pixPrepare1bpp': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           LPBox,  # BOX * box
                           c_float,  # l_float32 cropfract
                           c_int,  # l_int32 outres
                           ),
        'pixEstimateBackground': (c_int,
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 darkthresh
                                  c_float,  # l_float32 edgecrop
                                  c_int_p,  # l_int32 * pbg
                                  ),
        'pixFindLargeRectangles': (c_int,
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 polarity
                                   c_int,  # l_int32 nrect
                                   LPLPBoxa,  # BOXA ** pboxa
                                   LPLPPix,  # PIX ** ppixdb
                                   ),
        'pixFindLargestRectangle': (c_int,
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 polarity
                                    LPLPBox,  # BOX ** pbox
                                    LPLPPix,  # PIX ** ppixdb
                                    ),
        'pixFindRectangleInCC': (LPBox,  # BOX *
                                 LPPix,  # PIX * pixs
                                 LPBox,  # BOX * boxs
                                 c_float,  # l_float32 fract
                                 c_int,  # l_int32 dir
                                 c_int,  # l_int32 select
                                 c_int,  # l_int32 debug
                                 ),
        'pixAutoPhotoinvert': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 thresh
                               LPLPPix,  # PIX ** ppixm
                               LPPixa,  # PIXA * pixadb
                               ),
        'pixSetSelectCmap': (c_int,
                             LPPix,  # PIX * pixs
                             LPBox,  # BOX * box
                             c_int,  # l_int32 sindex
                             c_int,  # l_int32 rval
                             c_int,  # l_int32 gval
                             c_int,  # l_int32 bval
                             ),
        'pixColorGrayRegionsCmap': (c_int,
                                    LPPix,  # PIX * pixs
                                    LPBoxa,  # BOXA * boxa
                                    c_int,  # l_int32 type
                                    c_int,  # l_int32 rval
                                    c_int,  # l_int32 gval
                                    c_int,  # l_int32 bval
                                    ),
        'pixColorGrayCmap': (c_int,
                             LPPix,  # PIX * pixs
                             LPBox,  # BOX * box
                             c_int,  # l_int32 type
                             c_int,  # l_int32 rval
                             c_int,  # l_int32 gval
                             c_int,  # l_int32 bval
                             ),
        'pixColorGrayMaskedCmap': (c_int,
                                   LPPix,  # PIX * pixs
                                   LPPix,  # PIX * pixm
                                   c_int,  # l_int32 type
                                   c_int,  # l_int32 rval
                                   c_int,  # l_int32 gval
                                   c_int,  # l_int32 bval
                                   ),
        'addColorizedGrayToCmap': (c_int,
                                   LPPixColormap,  # PIXCMAP * cmap
                                   c_int,  # l_int32 type
                                   c_int,  # l_int32 rval
                                   c_int,  # l_int32 gval
                                   c_int,  # l_int32 bval
                                   LPLPNuma,  # NUMA ** pna
                                   ),
        'pixSetSelectMaskedCmap': (c_int,
                                   LPPix,  # PIX * pixs
                                   LPPix,  # PIX * pixm
                                   c_int,  # l_int32 x
                                   c_int,  # l_int32 y
                                   c_int,  # l_int32 sindex
                                   c_int,  # l_int32 rval
                                   c_int,  # l_int32 gval
                                   c_int,  # l_int32 bval
                                   ),
        'pixSetMaskedCmap': (c_int,
                             LPPix,  # PIX * pixs
                             LPPix,  # PIX * pixm
                             c_int,  # l_int32 x
                             c_int,  # l_int32 y
                             c_int,  # l_int32 rval
                             c_int,  # l_int32 gval
                             c_int,  # l_int32 bval
                             ),
        'parseForProtos': (c_char_p,
                           c_char_p,  # const char * filein
                           c_char_p,  # const char * prestring
                           ),
        'partifyFiles': (c_int,
                         c_char_p,  # const char * dirname
                         c_char_p,  # const char * substr
                         c_int,  # l_int32 nparts
                         c_char_p,  # const char * outroot
                         c_char_p,  # const char * debugfile
                         ),
        'partifyPixac': (c_int,
                         LPPixaComp,  # PIXAC * pixac
                         c_int,  # l_int32 nparts
                         c_char_p,  # const char * outroot
                         LPPixa,  # PIXA * pixadb
                         ),
        'boxaGetWhiteblocks': (LPBoxa,  # BOXA *
                               LPBoxa,  # BOXA * boxas
                               LPBox,  # BOX * box
                               c_int,  # l_int32 sortflag
                               c_int,  # l_int32 maxboxes
                               c_float,  # l_float32 maxoverlap
                               c_int,  # l_int32 maxperim
                               c_float,  # l_float32 fract
                               c_int,  # l_int32 maxpops
                               ),
        'boxaPruneSortedOnOverlap': (LPBoxa,  # BOXA *
                                     LPBoxa,  # BOXA * boxas
                                     c_float,  # l_float32 maxoverlap
                                     ),
        'convertFilesToPdf': (c_int,
                              c_char_p,  # const char * dirname
                              c_char_p,  # const char * substr
                              c_int,  # l_int32 res
                              c_float,  # l_float32 scalefactor
                              c_int,  # l_int32 type
                              c_int,  # l_int32 quality
                              c_char_p,  # const char * title
                              c_char_p,  # const char * fileout
                              ),
        'saConvertFilesToPdf': (c_int,
                                LPSarray,  # SARRAY * sa
                                c_int,  # l_int32 res
                                c_float,  # l_float32 scalefactor
                                c_int,  # l_int32 type
                                c_int,  # l_int32 quality
                                c_char_p,  # const char * title
                                c_char_p,  # const char * fileout
                                ),
        'saConvertFilesToPdfData': (c_int,
                                    LPSarray,  # SARRAY * sa
                                    c_int,  # l_int32 res
                                    c_float,  # l_float32 scalefactor
                                    c_int,  # l_int32 type
                                    c_int,  # l_int32 quality
                                    c_char_p,  # const char * title
                                    # l_uint8 ** pdata
                                    POINTER(c_ubyte_p),
                                    c_size_t_p,  # size_t * pnbytes
                                    ),
        'selectDefaultPdfEncoding': (c_int,
                                     LPPix,  # PIX * pix
                                     c_int_p,  # l_int32 * ptype
                                     ),
        'convertUnscaledFilesToPdf': (c_int,
                                      c_char_p,  # const char * dirname
                                      c_char_p,  # const char * substr
                                      c_char_p,  # const char * title
                                      c_char_p,  # const char * fileout
                                      ),
        'saConvertUnscaledFilesToPdf': (c_int,
                                        LPSarray,  # SARRAY * sa
                                        c_char_p,  # const char * title
                                        c_char_p,  # const char * fileout
                                        ),
        'saConvertUnscaledFilesToPdfData': (c_int,
                                            LPSarray,  # SARRAY * sa
                                            c_char_p,  # const char * title
                                            # l_uint8 ** pdata
                                            POINTER(c_ubyte_p),
                                            # size_t * pnbytes
                                            c_size_t_p,
                                            ),
        'convertUnscaledToPdfData': (c_int,
                                     c_char_p,  # const char * fname
                                     c_char_p,  # const char * title
                                     # l_uint8 ** pdata
                                     POINTER(c_ubyte_p),
                                     c_size_t_p,  # size_t * pnbytes
                                     ),
        'pixaConvertToPdf': (c_int,
                             LPPixa,  # PIXA * pixa
                             c_int,  # l_int32 res
                             c_float,  # l_float32 scalefactor
                             c_int,  # l_int32 type
                             c_int,  # l_int32 quality
                             c_char_p,  # const char * title
                             c_char_p,  # const char * fileout
                             ),
        'pixaConvertToPdfData': (c_int,
                                 LPPixa,  # PIXA * pixa
                                 c_int,  # l_int32 res
                                 c_float,  # l_float32 scalefactor
                                 c_int,  # l_int32 type
                                 c_int,  # l_int32 quality
                                 c_char_p,  # const char * title
                                 # l_uint8 ** pdata
                                 POINTER(c_ubyte_p),
                                 c_size_t_p,  # size_t * pnbytes
                                 ),
        'pixWriteStreamPdf': (c_int,
                              LPFile,  # FILE * fp
                              LPPix,  # PIX * pix
                              c_int,  # l_int32 res
                              c_char_p,  # const char * title
                              ),
        'pixWriteMemPdf': (c_int,
                           POINTER(c_ubyte_p),  # l_uint8 ** pdata
                           c_size_t_p,  # size_t * pnbytes
                           LPPix,  # PIX * pix
                           c_int,  # l_int32 res
                           c_char_p,  # const char * title
                           ),
        'convertSegmentedFilesToPdf': (c_int,
                                       c_char_p,  # const char * dirname
                                       c_char_p,  # const char * substr
                                       c_int,  # l_int32 res
                                       c_int,  # l_int32 type
                                       c_int,  # l_int32 thresh
                                       LPBoxaa,  # BOXAA * baa
                                       c_int,  # l_int32 quality
                                       c_float,  # l_float32 scalefactor
                                       c_char_p,  # const char * title
                                       c_char_p,  # const char * fileout
                                       ),
        'convertNumberedMasksToBoxaa': (LPBoxaa,  # BOXAA *
                                        c_char_p,  # const char * dirname
                                        c_char_p,  # const char * substr
                                        c_int,  # l_int32 numpre
                                        c_int,  # l_int32 numpost
                                        ),
        'convertToPdfSegmented': (c_int,
                                  c_char_p,  # const char * filein
                                  c_int,  # l_int32 res
                                  c_int,  # l_int32 type
                                  c_int,  # l_int32 thresh
                                  LPBoxa,  # BOXA * boxa
                                  c_int,  # l_int32 quality
                                  c_float,  # l_float32 scalefactor
                                  c_char_p,  # const char * title
                                  c_char_p,  # const char * fileout
                                  ),
        'pixConvertToPdfSegmented': (c_int,
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 res
                                     c_int,  # l_int32 type
                                     c_int,  # l_int32 thresh
                                     LPBoxa,  # BOXA * boxa
                                     c_int,  # l_int32 quality
                                     c_float,  # l_float32 scalefactor
                                     c_char_p,  # const char * title
                                     c_char_p,  # const char * fileout
                                     ),
        'convertToPdfDataSegmented': (c_int,
                                      c_char_p,  # const char * filein
                                      c_int,  # l_int32 res
                                      c_int,  # l_int32 type
                                      c_int,  # l_int32 thresh
                                      LPBoxa,  # BOXA * boxa
                                      c_int,  # l_int32 quality
                                      c_float,  # l_float32 scalefactor
                                      c_char_p,  # const char * title
                                      # l_uint8 ** pdata
                                      POINTER(c_ubyte_p),
                                      c_size_t_p,  # size_t * pnbytes
                                      ),
        'pixConvertToPdfDataSegmented': (c_int,
                                         LPPix,  # PIX * pixs
                                         c_int,  # l_int32 res
                                         c_int,  # l_int32 type
                                         c_int,  # l_int32 thresh
                                         LPBoxa,  # BOXA * boxa
                                         c_int,  # l_int32 quality
                                         c_float,  # l_float32 scalefactor
                                         c_char_p,  # const char * title
                                         # l_uint8 ** pdata
                                         POINTER(c_ubyte_p),
                                         # size_t * pnbytes
                                         c_size_t_p,
                                         ),
        'concatenatePdf': (c_int,
                           c_char_p,  # const char * dirname
                           c_char_p,  # const char * substr
                           c_char_p,  # const char * fileout
                           ),
        'saConcatenatePdf': (c_int,
                             LPSarray,  # SARRAY * sa
                             c_char_p,  # const char * fileout
                             ),
        'concatenatePdfToData': (c_int,
                                 c_char_p,  # const char * dirname
                                 c_char_p,  # const char * substr
                                 # l_uint8 ** pdata
                                 POINTER(c_ubyte_p),
                                 c_size_t_p,  # size_t * pnbytes
                                 ),
        'saConcatenatePdfToData': (c_int,
                                   LPSarray,  # SARRAY * sa
                                   # l_uint8 ** pdata
                                   POINTER(c_ubyte_p),
                                   c_size_t_p,  # size_t * pnbytes
                                   ),
        'convertTiffMultipageToPdf': (c_int,
                                      c_char_p,  # const char * filein
                                      c_char_p,  # const char * fileout
                                      ),
        'l_pdfSetG4ImageMask': (None,
                                c_int,  # l_int32 flag
                                ),
        'l_pdfSetDateAndVersion': (None,
                                   c_int,  # l_int32 flag
                                   ),
        'pixCreate': (LPPix,  # PIX *
                      c_int,  # l_int32 width
                      c_int,  # l_int32 height
                      c_int,  # l_int32 depth
                      ),
        'pixCreateNoInit': (LPPix,  # PIX *
                            c_int,  # l_int32 width
                            c_int,  # l_int32 height
                            c_int,  # l_int32 depth
                            ),
        'pixCreateTemplate': (LPPix,  # PIX *
                              LPPix,  # const PIX * pixs
                              ),
        'pixCreateTemplateNoInit': (LPPix,  # PIX *
                                    LPPix,  # const PIX * pixs
                                    ),
        'pixCreateWithCmap': (LPPix,  # PIX *
                              c_int,  # l_int32 width
                              c_int,  # l_int32 height
                              c_int,  # l_int32 depth
                              c_int,  # l_int32 initcolor
                              ),
        'pixCreateHeader': (LPPix,  # PIX *
                            c_int,  # l_int32 width
                            c_int,  # l_int32 height
                            c_int,  # l_int32 depth
                            ),
        'pixClone': (LPPix,  # PIX *
                     LPPix,  # PIX * pixs
                     ),
        'pixDestroy': (None,
                       LPLPPix,  # PIX ** ppix
                       ),
        'pixCopy': (LPPix,  # PIX *
                    LPPix,  # PIX * pixd
                    LPPix,  # const PIX * pixs
                    ),
        'pixResizeImageData': (c_int,
                               LPPix,  # PIX * pixd
                               LPPix,  # const PIX * pixs
                               ),
        'pixCopyColormap': (c_int,
                            LPPix,  # PIX * pixd
                            LPPix,  # const PIX * pixs
                            ),
        'pixTransferAllData': (c_int,
                               LPPix,  # PIX * pixd
                               LPLPPix,  # PIX ** ppixs
                               c_int,  # l_int32 copytext
                               c_int,  # l_int32 copyformat
                               ),
        'pixSwapAndDestroy': (c_int,
                              LPLPPix,  # PIX ** ppixd
                              LPLPPix,  # PIX ** ppixs
                              ),
        'pixGetWidth': (c_int,
                        LPPix,  # const PIX * pix
                        ),
        'pixSetWidth': (c_int,
                        LPPix,  # PIX * pix
                        c_int,  # l_int32 width
                        ),
        'pixGetHeight': (c_int,
                         LPPix,  # const PIX * pix
                         ),
        'pixSetHeight': (c_int,
                         LPPix,  # PIX * pix
                         c_int,  # l_int32 height
                         ),
        'pixGetDepth': (c_int,
                        LPPix,  # const PIX * pix
                        ),
        'pixSetDepth': (c_int,
                        LPPix,  # PIX * pix
                        c_int,  # l_int32 depth
                        ),
        'pixGetDimensions': (c_int,
                             LPPix,  # const PIX * pix
                             c_int_p,  # l_int32 * pw
                             c_int_p,  # l_int32 * ph
                             c_int_p,  # l_int32 * pd
                             ),
        'pixSetDimensions': (c_int,
                             LPPix,  # PIX * pix
                             c_int,  # l_int32 w
                             c_int,  # l_int32 h
                             c_int,  # l_int32 d
                             ),
        'pixCopyDimensions': (c_int,
                              LPPix,  # PIX * pixd
                              LPPix,  # const PIX * pixs
                              ),
        'pixGetSpp': (c_int,
                      LPPix,  # const PIX * pix
                      ),
        'pixSetSpp': (c_int,
                      LPPix,  # PIX * pix
                      c_int,  # l_int32 spp
                      ),
        'pixCopySpp': (c_int,
                       LPPix,  # PIX * pixd
                       LPPix,  # const PIX * pixs
                       ),
        'pixGetWpl': (c_int,
                      LPPix,  # const PIX * pix
                      ),
        'pixSetWpl': (c_int,
                      LPPix,  # PIX * pix
                      c_int,  # l_int32 wpl
                      ),
        'pixGetRefcount': (c_int,
                           LPPix,  # const PIX * pix
                           ),
        'pixChangeRefcount': (c_int,
                              LPPix,  # PIX * pix
                              c_int,  # l_int32 delta
                              ),
        'pixGetXRes': (c_int,
                       LPPix,  # const PIX * pix
                       ),
        'pixSetXRes': (c_int,
                       LPPix,  # PIX * pix
                       c_int,  # l_int32 res
                       ),
        'pixGetYRes': (c_int,
                       LPPix,  # const PIX * pix
                       ),
        'pixSetYRes': (c_int,
                       LPPix,  # PIX * pix
                       c_int,  # l_int32 res
                       ),
        'pixGetResolution': (c_int,
                             LPPix,  # const PIX * pix
                             c_int_p,  # l_int32 * pxres
                             c_int_p,  # l_int32 * pyres
                             ),
        'pixSetResolution': (c_int,
                             LPPix,  # PIX * pix
                             c_int,  # l_int32 xres
                             c_int,  # l_int32 yres
                             ),
        'pixCopyResolution': (c_int,
                              LPPix,  # PIX * pixd
                              LPPix,  # const PIX * pixs
                              ),
        'pixScaleResolution': (c_int,
                               LPPix,  # PIX * pix
                               c_float,  # l_float32 xscale
                               c_float,  # l_float32 yscale
                               ),
        'pixGetInputFormat': (c_int,
                              LPPix,  # const PIX * pix
                              ),
        'pixSetInputFormat': (c_int,
                              LPPix,  # PIX * pix
                              c_int,  # l_int32 informat
                              ),
        'pixCopyInputFormat': (c_int,
                               LPPix,  # PIX * pixd
                               LPPix,  # const PIX * pixs
                               ),
        'pixSetSpecial': (c_int,
                          LPPix,  # PIX * pix
                          c_int,  # l_int32 special
                          ),
        'pixGetText': (c_char_p,
                       LPPix,  # PIX * pix
                       ),
        'pixSetText': (c_int,
                       LPPix,  # PIX * pix
                       c_char_p,  # const char * textstring
                       ),
        'pixAddText': (c_int,
                       LPPix,  # PIX * pix
                       c_char_p,  # const char * textstring
                       ),
        'pixCopyText': (c_int,
                        LPPix,  # PIX * pixd
                        LPPix,  # const PIX * pixs
                        ),
        'pixGetTextCompNew': (c_ubyte_p,
                              LPPix,  # PIX * pix
                              c_size_t_p,  # size_t * psize
                              ),
        'pixSetTextCompNew': (c_int,
                              LPPix,  # PIX * pix
                              c_ubyte_p,  # const l_uint8 * data
                              c_size_t,  # size_t size
                              ),
        'pixGetColormap': (LPPixColormap,  # PIXCMAP *
                           LPPix,  # PIX * pix
                           ),
        'pixSetColormap': (c_int,
                           LPPix,  # PIX * pix
                           LPPixColormap,  # PIXCMAP * colormap
                           ),
        'pixDestroyColormap': (c_int,
                               LPPix,  # PIX * pix
                               ),
        'pixGetData': (c_uint_p,
                       LPPix,  # PIX * pix
                       ),
        'pixSetData': (c_int,
                       LPPix,  # PIX * pix
                       c_uint_p,  # l_uint32 * data
                       ),
        'pixExtractData': (c_uint_p,
                           LPPix,  # PIX * pixs
                           ),
        'pixFreeData': (c_int,
                        LPPix,  # PIX * pix
                        ),
        'pixGetLinePtrs': (POINTER(c_void_p),
                           LPPix,  # PIX * pix
                           c_int_p,  # l_int32 * psize
                           ),
        'pixSizesEqual': (c_int,
                          LPPix,  # const PIX * pix1
                          LPPix,  # const PIX * pix2
                          ),
        'pixMaxAspectRatio': (c_int,
                              LPPix,  # PIX * pixs
                              c_float_p,  # l_float32 * pratio
                              ),
        'pixPrintStreamInfo': (c_int,
                               LPFile,  # FILE * fp
                               LPPix,  # const PIX * pix
                               c_char_p,  # const char * text
                               ),
        'pixGetPixel': (c_int,
                        LPPix,  # PIX * pix
                        c_int,  # l_int32 x
                        c_int,  # l_int32 y
                        c_uint_p,  # l_uint32 * pval
                        ),
        'pixSetPixel': (c_int,
                        LPPix,  # PIX * pix
                        c_int,  # l_int32 x
                        c_int,  # l_int32 y
                        c_uint,  # l_uint32 val
                        ),
        'pixGetRGBPixel': (c_int,
                           LPPix,  # PIX * pix
                           c_int,  # l_int32 x
                           c_int,  # l_int32 y
                           c_int_p,  # l_int32 * prval
                           c_int_p,  # l_int32 * pgval
                           c_int_p,  # l_int32 * pbval
                           ),
        'pixSetRGBPixel': (c_int,
                           LPPix,  # PIX * pix
                           c_int,  # l_int32 x
                           c_int,  # l_int32 y
                           c_int,  # l_int32 rval
                           c_int,  # l_int32 gval
                           c_int,  # l_int32 bval
                           ),
        'pixSetCmapPixel': (c_int,
                            LPPix,  # PIX * pix
                            c_int,  # l_int32 x
                            c_int,  # l_int32 y
                            c_int,  # l_int32 rval
                            c_int,  # l_int32 gval
                            c_int,  # l_int32 bval
                            ),
        'pixGetRandomPixel': (c_int,
                              LPPix,  # PIX * pix
                              c_uint_p,  # l_uint32 * pval
                              c_int_p,  # l_int32 * px
                              c_int_p,  # l_int32 * py
                              ),
        'pixClearPixel': (c_int,
                          LPPix,  # PIX * pix
                          c_int,  # l_int32 x
                          c_int,  # l_int32 y
                          ),
        'pixFlipPixel': (c_int,
                         LPPix,  # PIX * pix
                         c_int,  # l_int32 x
                         c_int,  # l_int32 y
                         ),
        'setPixelLow': (None,
                        c_uint_p,  # l_uint32 * line
                        c_int,  # l_int32 x
                        c_int,  # l_int32 depth
                        c_uint,  # l_uint32 val
                        ),
        'pixGetBlackOrWhiteVal': (c_int,
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 op
                                  c_uint_p,  # l_uint32 * pval
                                  ),
        'pixClearAll': (c_int,
                        LPPix,  # PIX * pix
                        ),
        'pixSetAll': (c_int,
                      LPPix,  # PIX * pix
                      ),
        'pixSetAllGray': (c_int,
                          LPPix,  # PIX * pix
                          c_int,  # l_int32 grayval
                          ),
        'pixSetAllArbitrary': (c_int,
                               LPPix,  # PIX * pix
                               c_uint,  # l_uint32 val
                               ),
        'pixSetBlackOrWhite': (c_int,
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 op
                               ),
        'pixSetComponentArbitrary': (c_int,
                                     LPPix,  # PIX * pix
                                     c_int,  # l_int32 comp
                                     c_int,  # l_int32 val
                                     ),
        'pixClearInRect': (c_int,
                           LPPix,  # PIX * pix
                           LPBox,  # BOX * box
                           ),
        'pixSetInRect': (c_int,
                         LPPix,  # PIX * pix
                         LPBox,  # BOX * box
                         ),
        'pixSetInRectArbitrary': (c_int,
                                  LPPix,  # PIX * pix
                                  LPBox,  # BOX * box
                                  c_uint,  # l_uint32 val
                                  ),
        'pixBlendInRect': (c_int,
                           LPPix,  # PIX * pixs
                           LPBox,  # BOX * box
                           c_uint,  # l_uint32 val
                           c_float,  # l_float32 fract
                           ),
        'pixSetPadBits': (c_int,
                          LPPix,  # PIX * pix
                          c_int,  # l_int32 val
                          ),
        'pixSetPadBitsBand': (c_int,
                              LPPix,  # PIX * pix
                              c_int,  # l_int32 by
                              c_int,  # l_int32 bh
                              c_int,  # l_int32 val
                              ),
        'pixSetOrClearBorder': (c_int,
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 left
                                c_int,  # l_int32 right
                                c_int,  # l_int32 top
                                c_int,  # l_int32 bot
                                c_int,  # l_int32 op
                                ),
        'pixSetBorderVal': (c_int,
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 left
                            c_int,  # l_int32 right
                            c_int,  # l_int32 top
                            c_int,  # l_int32 bot
                            c_uint,  # l_uint32 val
                            ),
        'pixSetBorderRingVal': (c_int,
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 dist
                                c_uint,  # l_uint32 val
                                ),
        'pixSetMirroredBorder': (c_int,
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 left
                                 c_int,  # l_int32 right
                                 c_int,  # l_int32 top
                                 c_int,  # l_int32 bot
                                 ),
        'pixCopyBorder': (LPPix,  # PIX *
                          LPPix,  # PIX * pixd
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 left
                          c_int,  # l_int32 right
                          c_int,  # l_int32 top
                          c_int,  # l_int32 bot
                          ),
        'pixAddBorder': (LPPix,  # PIX *
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 npix
                         c_uint,  # l_uint32 val
                         ),
        'pixAddBlackOrWhiteBorder': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 left
                                     c_int,  # l_int32 right
                                     c_int,  # l_int32 top
                                     c_int,  # l_int32 bot
                                     c_int,  # l_int32 op
                                     ),
        'pixAddBorderGeneral': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 left
                                c_int,  # l_int32 right
                                c_int,  # l_int32 top
                                c_int,  # l_int32 bot
                                c_uint,  # l_uint32 val
                                ),
        'pixRemoveBorder': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 npix
                            ),
        'pixRemoveBorderGeneral': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 left
                                   c_int,  # l_int32 right
                                   c_int,  # l_int32 top
                                   c_int,  # l_int32 bot
                                   ),
        'pixRemoveBorderToSize': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 wd
                                  c_int,  # l_int32 hd
                                  ),
        'pixAddMirroredBorder': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 left
                                 c_int,  # l_int32 right
                                 c_int,  # l_int32 top
                                 c_int,  # l_int32 bot
                                 ),
        'pixAddRepeatedBorder': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 left
                                 c_int,  # l_int32 right
                                 c_int,  # l_int32 top
                                 c_int,  # l_int32 bot
                                 ),
        'pixAddMixedBorder': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 left
                              c_int,  # l_int32 right
                              c_int,  # l_int32 top
                              c_int,  # l_int32 bot
                              ),
        'pixAddContinuedBorder': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 left
                                  c_int,  # l_int32 right
                                  c_int,  # l_int32 top
                                  c_int,  # l_int32 bot
                                  ),
        'pixShiftAndTransferAlpha': (c_int,
                                     LPPix,  # PIX * pixd
                                     LPPix,  # PIX * pixs
                                     c_float,  # l_float32 shiftx
                                     c_float,  # l_float32 shifty
                                     ),
        'pixDisplayLayersRGBA': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_uint,  # l_uint32 val
                                 c_int,  # l_int32 maxw
                                 ),
        'pixCreateRGBImage': (LPPix,  # PIX *
                              LPPix,  # PIX * pixr
                              LPPix,  # PIX * pixg
                              LPPix,  # PIX * pixb
                              ),
        'pixGetRGBComponent': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 comp
                               ),
        'pixSetRGBComponent': (c_int,
                               LPPix,  # PIX * pixd
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 comp
                               ),
        'pixGetRGBComponentCmap': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 comp
                                   ),
        'pixCopyRGBComponent': (c_int,
                                LPPix,  # PIX * pixd
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 comp
                                ),
        'composeRGBPixel': (c_int,
                            c_int,  # l_int32 rval
                            c_int,  # l_int32 gval
                            c_int,  # l_int32 bval
                            c_uint_p,  # l_uint32 * ppixel
                            ),
        'composeRGBAPixel': (c_int,
                             c_int,  # l_int32 rval
                             c_int,  # l_int32 gval
                             c_int,  # l_int32 bval
                             c_int,  # l_int32 aval
                             c_uint_p,  # l_uint32 * ppixel
                             ),
        'extractRGBValues': (None,
                             c_uint,  # l_uint32 pixel
                             c_int_p,  # l_int32 * prval
                             c_int_p,  # l_int32 * pgval
                             c_int_p,  # l_int32 * pbval
                             ),
        'extractRGBAValues': (None,
                              c_uint,  # l_uint32 pixel
                              c_int_p,  # l_int32 * prval
                              c_int_p,  # l_int32 * pgval
                              c_int_p,  # l_int32 * pbval
                              c_int_p,  # l_int32 * paval
                              ),
        'extractMinMaxComponent': (c_int,
                                   c_uint,  # l_uint32 pixel
                                   c_int,  # l_int32 type
                                   ),
        'pixGetRGBLine': (c_int,
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 row
                          c_ubyte_p,  # l_uint8 * bufr
                          c_ubyte_p,  # l_uint8 * bufg
                          c_ubyte_p,  # l_uint8 * bufb
                          ),
        'setLineDataVal': (c_int,
                           c_uint_p,  # l_uint32 * line
                           c_int,  # l_int32 j
                           c_int,  # l_int32 d
                           c_uint,  # l_uint32 val
                           ),
        'pixEndianByteSwapNew': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 ),
        'pixEndianByteSwap': (c_int,
                              LPPix,  # PIX * pixs
                              ),
        'lineEndianByteSwap': (c_int,
                               c_uint_p,  # l_uint32 * datad
                               c_uint_p,  # l_uint32 * datas
                               c_int,  # l_int32 wpl
                               ),
        'pixEndianTwoByteSwapNew': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    ),
        'pixEndianTwoByteSwap': (c_int,
                                 LPPix,  # PIX * pixs
                                 ),
        'pixGetRasterData': (c_int,
                             LPPix,  # PIX * pixs
                             POINTER(c_ubyte_p),  # l_uint8 ** pdata
                             c_size_t_p,  # size_t * pnbytes
                             ),
        'pixInferResolution': (c_int,
                               LPPix,  # PIX * pix
                               c_float,  # l_float32 longside
                               c_int_p,  # l_int32 * pres
                               ),
        'pixAlphaIsOpaque': (c_int,
                             LPPix,  # PIX * pix
                             c_int_p,  # l_int32 * popaque
                             ),
        'pixSetupByteProcessing': (POINTER(c_ubyte_p),
                                   LPPix,  # PIX * pix
                                   c_int_p,  # l_int32 * pw
                                   c_int_p,  # l_int32 * ph
                                   ),
        'pixCleanupByteProcessing': (c_int,
                                     LPPix,  # PIX * pix
                                     # l_uint8 ** lineptrs
                                     POINTER(c_ubyte_p),
                                     ),
        'l_setAlphaMaskBorder': (None,
                                 c_float,  # l_float32 val1
                                 c_float,  # l_float32 val2
                                 ),
        'pixSetMasked': (c_int,
                         LPPix,  # PIX * pixd
                         LPPix,  # PIX * pixm
                         c_uint,  # l_uint32 val
                         ),
        'pixSetMaskedGeneral': (c_int,
                                LPPix,  # PIX * pixd
                                LPPix,  # PIX * pixm
                                c_uint,  # l_uint32 val
                                c_int,  # l_int32 x
                                c_int,  # l_int32 y
                                ),
        'pixCombineMasked': (c_int,
                             LPPix,  # PIX * pixd
                             LPPix,  # PIX * pixs
                             LPPix,  # PIX * pixm
                             ),
        'pixCombineMaskedGeneral': (c_int,
                                    LPPix,  # PIX * pixd
                                    LPPix,  # PIX * pixs
                                    LPPix,  # PIX * pixm
                                    c_int,  # l_int32 x
                                    c_int,  # l_int32 y
                                    ),
        'pixPaintThroughMask': (c_int,
                                LPPix,  # PIX * pixd
                                LPPix,  # PIX * pixm
                                c_int,  # l_int32 x
                                c_int,  # l_int32 y
                                c_uint,  # l_uint32 val
                                ),
        'pixCopyWithBoxa': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            LPBoxa,  # BOXA * boxa
                            c_int,  # l_int32 background
                            ),
        'pixPaintSelfThroughMask': (c_int,
                                    LPPix,  # PIX * pixd
                                    LPPix,  # PIX * pixm
                                    c_int,  # l_int32 x
                                    c_int,  # l_int32 y
                                    c_int,  # l_int32 searchdir
                                    c_int,  # l_int32 mindist
                                    c_int,  # l_int32 tilesize
                                    c_int,  # l_int32 ntiles
                                    c_int,  # l_int32 distblend
                                    ),
        'pixMakeMaskFromVal': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 val
                               ),
        'pixMakeMaskFromLUT': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int_p,  # l_int32 * tab
                               ),
        'pixMakeArbMaskFromRGB': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_float,  # l_float32 rc
                                  c_float,  # l_float32 gc
                                  c_float,  # l_float32 bc
                                  c_float,  # l_float32 thresh
                                  ),
        'pixSetUnderTransparency': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_uint,  # l_uint32 val
                                    c_int,  # l_int32 debug
                                    ),
        'pixMakeAlphaFromMask': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 dist
                                 LPLPBox,  # BOX ** pbox
                                 ),
        'pixGetColorNearMaskBoundary': (c_int,
                                        LPPix,  # PIX * pixs
                                        LPPix,  # PIX * pixm
                                        LPBox,  # BOX * box
                                        c_int,  # l_int32 dist
                                        c_uint_p,  # l_uint32 * pval
                                        c_int,  # l_int32 debug
                                        ),
        'pixInvert': (LPPix,  # PIX *
                      LPPix,  # PIX * pixd
                      LPPix,  # PIX * pixs
                      ),
        'pixOr': (LPPix,  # PIX *
                  LPPix,  # PIX * pixd
                  LPPix,  # PIX * pixs1
                  LPPix,  # PIX * pixs2
                  ),
        'pixAnd': (LPPix,  # PIX *
                   LPPix,  # PIX * pixd
                   LPPix,  # PIX * pixs1
                   LPPix,  # PIX * pixs2
                   ),
        'pixXor': (LPPix,  # PIX *
                   LPPix,  # PIX * pixd
                   LPPix,  # PIX * pixs1
                   LPPix,  # PIX * pixs2
                   ),
        'pixSubtract': (LPPix,  # PIX *
                        LPPix,  # PIX * pixd
                        LPPix,  # PIX * pixs1
                        LPPix,  # PIX * pixs2
                        ),
        'pixZero': (c_int,
                    LPPix,  # PIX * pix
                    c_int_p,  # l_int32 * pempty
                    ),
        'pixForegroundFraction': (c_int,
                                  LPPix,  # PIX * pix
                                  c_float_p,  # l_float32 * pfract
                                  ),
        'pixaCountPixels': (LPNuma,  # NUMA *
                            LPPixa,  # PIXA * pixa
                            ),
        'pixCountPixels': (c_int,
                           LPPix,  # PIX * pixs
                           c_int_p,  # l_int32 * pcount
                           c_int_p,  # l_int32 * tab8
                           ),
        'pixCountPixelsInRect': (c_int,
                                 LPPix,  # PIX * pixs
                                 LPBox,  # BOX * box
                                 c_int_p,  # l_int32 * pcount
                                 c_int_p,  # l_int32 * tab8
                                 ),
        'pixCountByRow': (LPNuma,  # NUMA *
                          LPPix,  # PIX * pix
                          LPBox,  # BOX * box
                          ),
        'pixCountByColumn': (LPNuma,  # NUMA *
                             LPPix,  # PIX * pix
                             LPBox,  # BOX * box
                             ),
        'pixCountPixelsByRow': (LPNuma,  # NUMA *
                                LPPix,  # PIX * pix
                                c_int_p,  # l_int32 * tab8
                                ),
        'pixCountPixelsByColumn': (LPNuma,  # NUMA *
                                   LPPix,  # PIX * pix
                                   ),
        'pixCountPixelsInRow': (c_int,
                                LPPix,  # PIX * pix
                                c_int,  # l_int32 row
                                c_int_p,  # l_int32 * pcount
                                c_int_p,  # l_int32 * tab8
                                ),
        'pixGetMomentByColumn': (LPNuma,  # NUMA *
                                 LPPix,  # PIX * pix
                                 c_int,  # l_int32 order
                                 ),
        'pixThresholdPixelSum': (c_int,
                                 LPPix,  # PIX * pix
                                 c_int,  # l_int32 thresh
                                 c_int_p,  # l_int32 * pabove
                                 c_int_p,  # l_int32 * tab8
                                 ),
        'makePixelSumTab8': (c_int_p, ),
        'makePixelCentroidTab8': (c_int_p, ),
        'pixAverageByRow': (LPNuma,  # NUMA *
                            LPPix,  # PIX * pix
                            LPBox,  # BOX * box
                            c_int,  # l_int32 type
                            ),
        'pixAverageByColumn': (LPNuma,  # NUMA *
                               LPPix,  # PIX * pix
                               LPBox,  # BOX * box
                               c_int,  # l_int32 type
                               ),
        'pixAverageInRect': (c_int,
                             LPPix,  # PIX * pixs
                             LPPix,  # PIX * pixm
                             LPBox,  # BOX * box
                             c_int,  # l_int32 minval
                             c_int,  # l_int32 maxval
                             c_int,  # l_int32 subsamp
                             c_float_p,  # l_float32 * pave
                             ),
        'pixAverageInRectRGB': (c_int,
                                LPPix,  # PIX * pixs
                                LPPix,  # PIX * pixm
                                LPBox,  # BOX * box
                                c_int,  # l_int32 subsamp
                                c_uint_p,  # l_uint32 * pave
                                ),
        'pixVarianceByRow': (LPNuma,  # NUMA *
                             LPPix,  # PIX * pix
                             LPBox,  # BOX * box
                             ),
        'pixVarianceByColumn': (LPNuma,  # NUMA *
                                LPPix,  # PIX * pix
                                LPBox,  # BOX * box
                                ),
        'pixVarianceInRect': (c_int,
                              LPPix,  # PIX * pix
                              LPBox,  # BOX * box
                              c_float_p,  # l_float32 * prootvar
                              ),
        'pixAbsDiffByRow': (LPNuma,  # NUMA *
                            LPPix,  # PIX * pix
                            LPBox,  # BOX * box
                            ),
        'pixAbsDiffByColumn': (LPNuma,  # NUMA *
                               LPPix,  # PIX * pix
                               LPBox,  # BOX * box
                               ),
        'pixAbsDiffInRect': (c_int,
                             LPPix,  # PIX * pix
                             LPBox,  # BOX * box
                             c_int,  # l_int32 dir
                             c_float_p,  # l_float32 * pabsdiff
                             ),
        'pixAbsDiffOnLine': (c_int,
                             LPPix,  # PIX * pix
                             c_int,  # l_int32 x1
                             c_int,  # l_int32 y1
                             c_int,  # l_int32 x2
                             c_int,  # l_int32 y2
                             c_float_p,  # l_float32 * pabsdiff
                             ),
        'pixCountArbInRect': (c_int,
                              LPPix,  # PIX * pixs
                              LPBox,  # BOX * box
                              c_int,  # l_int32 val
                              c_int,  # l_int32 factor
                              c_int_p,  # l_int32 * pcount
                              ),
        'pixMirroredTiling': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 w
                              c_int,  # l_int32 h
                              ),
        'pixFindRepCloseTile': (c_int,
                                LPPix,  # PIX * pixs
                                LPBox,  # BOX * box
                                c_int,  # l_int32 searchdir
                                c_int,  # l_int32 mindist
                                c_int,  # l_int32 tsize
                                c_int,  # l_int32 ntiles
                                LPLPBox,  # BOX ** pboxtile
                                c_int,  # l_int32 debug
                                ),
        'pixGetGrayHistogram': (LPNuma,  # NUMA *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 factor
                                ),
        'pixGetGrayHistogramMasked': (LPNuma,  # NUMA *
                                      LPPix,  # PIX * pixs
                                      LPPix,  # PIX * pixm
                                      c_int,  # l_int32 x
                                      c_int,  # l_int32 y
                                      c_int,  # l_int32 factor
                                      ),
        'pixGetGrayHistogramInRect': (LPNuma,  # NUMA *
                                      LPPix,  # PIX * pixs
                                      LPBox,  # BOX * box
                                      c_int,  # l_int32 factor
                                      ),
        'pixGetGrayHistogramTiled': (LPNumaa,  # NUMAA *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 factor
                                     c_int,  # l_int32 nx
                                     c_int,  # l_int32 ny
                                     ),
        'pixGetColorHistogram': (c_int,
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 factor
                                 LPLPNuma,  # NUMA ** pnar
                                 LPLPNuma,  # NUMA ** pnag
                                 LPLPNuma,  # NUMA ** pnab
                                 ),
        'pixGetColorHistogramMasked': (c_int,
                                       LPPix,  # PIX * pixs
                                       LPPix,  # PIX * pixm
                                       c_int,  # l_int32 x
                                       c_int,  # l_int32 y
                                       c_int,  # l_int32 factor
                                       LPLPNuma,  # NUMA ** pnar
                                       LPLPNuma,  # NUMA ** pnag
                                       LPLPNuma,  # NUMA ** pnab
                                       ),
        'pixGetCmapHistogram': (LPNuma,  # NUMA *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 factor
                                ),
        'pixGetCmapHistogramMasked': (LPNuma,  # NUMA *
                                      LPPix,  # PIX * pixs
                                      LPPix,  # PIX * pixm
                                      c_int,  # l_int32 x
                                      c_int,  # l_int32 y
                                      c_int,  # l_int32 factor
                                      ),
        'pixGetCmapHistogramInRect': (LPNuma,  # NUMA *
                                      LPPix,  # PIX * pixs
                                      LPBox,  # BOX * box
                                      c_int,  # l_int32 factor
                                      ),
        'pixCountRGBColorsByHash': (c_int,
                                    LPPix,  # PIX * pixs
                                    c_int_p,  # l_int32 * pncolors
                                    ),
        'pixCountRGBColors': (c_int,
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 factor
                              c_int_p,  # l_int32 * pncolors
                              ),
        'pixGetRankValue': (c_int,
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 factor
                            c_float,  # l_float32 rank
                            c_uint_p,  # l_uint32 * pvalue
                            ),
        'pixGetRankValueMaskedRGB': (c_int,
                                     LPPix,  # PIX * pixs
                                     LPPix,  # PIX * pixm
                                     c_int,  # l_int32 x
                                     c_int,  # l_int32 y
                                     c_int,  # l_int32 factor
                                     c_float,  # l_float32 rank
                                     c_float_p,  # l_float32 * prval
                                     c_float_p,  # l_float32 * pgval
                                     c_float_p,  # l_float32 * pbval
                                     ),
        'pixGetRankValueMasked': (c_int,
                                  LPPix,  # PIX * pixs
                                  LPPix,  # PIX * pixm
                                  c_int,  # l_int32 x
                                  c_int,  # l_int32 y
                                  c_int,  # l_int32 factor
                                  c_float,  # l_float32 rank
                                  c_float_p,  # l_float32 * pval
                                  LPLPNuma,  # NUMA ** pna
                                  ),
        'pixGetPixelAverage': (c_int,
                               LPPix,  # PIX * pixs
                               LPPix,  # PIX * pixm
                               c_int,  # l_int32 x
                               c_int,  # l_int32 y
                               c_int,  # l_int32 factor
                               c_uint_p,  # l_uint32 * pval
                               ),
        'pixGetPixelStats': (c_int,
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 factor
                             c_int,  # l_int32 type
                             c_uint_p,  # l_uint32 * pvalue
                             ),
        'pixGetAverageMaskedRGB': (c_int,
                                   LPPix,  # PIX * pixs
                                   LPPix,  # PIX * pixm
                                   c_int,  # l_int32 x
                                   c_int,  # l_int32 y
                                   c_int,  # l_int32 factor
                                   c_int,  # l_int32 type
                                   c_float_p,  # l_float32 * prval
                                   c_float_p,  # l_float32 * pgval
                                   c_float_p,  # l_float32 * pbval
                                   ),
        'pixGetAverageMasked': (c_int,
                                LPPix,  # PIX * pixs
                                LPPix,  # PIX * pixm
                                c_int,  # l_int32 x
                                c_int,  # l_int32 y
                                c_int,  # l_int32 factor
                                c_int,  # l_int32 type
                                c_float_p,  # l_float32 * pval
                                ),
        'pixGetAverageTiledRGB': (c_int,
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 sx
                                  c_int,  # l_int32 sy
                                  c_int,  # l_int32 type
                                  LPLPPix,  # PIX ** ppixr
                                  LPLPPix,  # PIX ** ppixg
                                  LPLPPix,  # PIX ** ppixb
                                  ),
        'pixGetAverageTiled': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 sx
                               c_int,  # l_int32 sy
                               c_int,  # l_int32 type
                               ),
        'pixRowStats': (c_int,
                        LPPix,  # PIX * pixs
                        LPBox,  # BOX * box
                        LPLPNuma,  # NUMA ** pnamean
                        LPLPNuma,  # NUMA ** pnamedian
                        LPLPNuma,  # NUMA ** pnamode
                        LPLPNuma,  # NUMA ** pnamodecount
                        LPLPNuma,  # NUMA ** pnavar
                        LPLPNuma,  # NUMA ** pnarootvar
                        ),
        'pixColumnStats': (c_int,
                           LPPix,  # PIX * pixs
                           LPBox,  # BOX * box
                           LPLPNuma,  # NUMA ** pnamean
                           LPLPNuma,  # NUMA ** pnamedian
                           LPLPNuma,  # NUMA ** pnamode
                           LPLPNuma,  # NUMA ** pnamodecount
                           LPLPNuma,  # NUMA ** pnavar
                           LPLPNuma,  # NUMA ** pnarootvar
                           ),
        'pixGetRangeValues': (c_int,
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 factor
                              c_int,  # l_int32 color
                              c_int_p,  # l_int32 * pminval
                              c_int_p,  # l_int32 * pmaxval
                              ),
        'pixGetExtremeValue': (c_int,
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 factor
                               c_int,  # l_int32 type
                               c_int_p,  # l_int32 * prval
                               c_int_p,  # l_int32 * pgval
                               c_int_p,  # l_int32 * pbval
                               c_int_p,  # l_int32 * pgrayval
                               ),
        'pixGetMaxValueInRect': (c_int,
                                 LPPix,  # PIX * pixs
                                 LPBox,  # BOX * box
                                 c_uint_p,  # l_uint32 * pmaxval
                                 c_int_p,  # l_int32 * pxmax
                                 c_int_p,  # l_int32 * pymax
                                 ),
        'pixGetMaxColorIndex': (c_int,
                                LPPix,  # PIX * pixs
                                c_int_p,  # l_int32 * pmaxindex
                                ),
        'pixGetBinnedComponentRange': (c_int,
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 nbins
                                       c_int,  # l_int32 factor
                                       c_int,  # l_int32 color
                                       c_int_p,  # l_int32 * pminval
                                       c_int_p,  # l_int32 * pmaxval
                                       # l_uint32 ** pcarray
                                       POINTER(c_uint_p),
                                       c_int,  # l_int32 fontsize
                                       ),
        'pixGetRankColorArray': (c_int,
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 nbins
                                 c_int,  # l_int32 type
                                 c_int,  # l_int32 factor
                                 # l_uint32 ** pcarray
                                 POINTER(c_uint_p),
                                 LPPixa,  # PIXA * pixadb
                                 c_int,  # l_int32 fontsize
                                 ),
        'pixGetBinnedColor': (c_int,
                              LPPix,  # PIX * pixs
                              LPPix,  # PIX * pixg
                              c_int,  # l_int32 factor
                              c_int,  # l_int32 nbins
                              # l_uint32 ** pcarray
                              POINTER(c_uint_p),
                              LPPixa,  # PIXA * pixadb
                              ),
        'pixDisplayColorArray': (LPPix,  # PIX *
                                 c_uint_p,  # l_uint32 * carray
                                 c_int,  # l_int32 ncolors
                                 c_int,  # l_int32 side
                                 c_int,  # l_int32 ncols
                                 c_int,  # l_int32 fontsize
                                 ),
        'pixRankBinByStrip': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 direction
                              c_int,  # l_int32 size
                              c_int,  # l_int32 nbins
                              c_int,  # l_int32 type
                              ),
        'pixaGetAlignedStats': (LPPix,  # PIX *
                                LPPixa,  # PIXA * pixa
                                c_int,  # l_int32 type
                                c_int,  # l_int32 nbins
                                c_int,  # l_int32 thresh
                                ),
        'pixaExtractColumnFromEachPix': (c_int,
                                         LPPixa,  # PIXA * pixa
                                         c_int,  # l_int32 col
                                         LPPix,  # PIX * pixd
                                         ),
        'pixGetRowStats': (c_int,
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 type
                           c_int,  # l_int32 nbins
                           c_int,  # l_int32 thresh
                           c_float_p,  # l_float32 * colvect
                           ),
        'pixGetColumnStats': (c_int,
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 type
                              c_int,  # l_int32 nbins
                              c_int,  # l_int32 thresh
                              c_float_p,  # l_float32 * rowvect
                              ),
        'pixSetPixelColumn': (c_int,
                              LPPix,  # PIX * pix
                              c_int,  # l_int32 col
                              c_float_p,  # l_float32 * colvect
                              ),
        'pixThresholdForFgBg': (c_int,
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 factor
                                c_int,  # l_int32 thresh
                                c_int_p,  # l_int32 * pfgval
                                c_int_p,  # l_int32 * pbgval
                                ),
        'pixSplitDistributionFgBg': (c_int,
                                     LPPix,  # PIX * pixs
                                     c_float,  # l_float32 scorefract
                                     c_int,  # l_int32 factor
                                     c_int_p,  # l_int32 * pthresh
                                     c_int_p,  # l_int32 * pfgval
                                     c_int_p,  # l_int32 * pbgval
                                     LPLPPix,  # PIX ** ppixdb
                                     ),
        'pixaFindDimensions': (c_int,
                               LPPixa,  # PIXA * pixa
                               LPLPNuma,  # NUMA ** pnaw
                               LPLPNuma,  # NUMA ** pnah
                               ),
        'pixFindAreaPerimRatio': (c_int,
                                  LPPix,  # PIX * pixs
                                  c_int_p,  # l_int32 * tab
                                  c_float_p,  # l_float32 * pfract
                                  ),
        'pixaFindPerimToAreaRatio': (LPNuma,  # NUMA *
                                     LPPixa,  # PIXA * pixa
                                     ),
        'pixFindPerimToAreaRatio': (c_int,
                                    LPPix,  # PIX * pixs
                                    c_int_p,  # l_int32 * tab
                                    c_float_p,  # l_float32 * pfract
                                    ),
        'pixaFindPerimSizeRatio': (LPNuma,  # NUMA *
                                   LPPixa,  # PIXA * pixa
                                   ),
        'pixFindPerimSizeRatio': (c_int,
                                  LPPix,  # PIX * pixs
                                  c_int_p,  # l_int32 * tab
                                  c_float_p,  # l_float32 * pratio
                                  ),
        'pixaFindAreaFraction': (LPNuma,  # NUMA *
                                 LPPixa,  # PIXA * pixa
                                 ),
        'pixFindAreaFraction': (c_int,
                                LPPix,  # PIX * pixs
                                c_int_p,  # l_int32 * tab
                                c_float_p,  # l_float32 * pfract
                                ),
        'pixaFindAreaFractionMasked': (LPNuma,  # NUMA *
                                       LPPixa,  # PIXA * pixa
                                       LPPix,  # PIX * pixm
                                       c_int,  # l_int32 debug
                                       ),
        'pixFindAreaFractionMasked': (c_int,
                                      LPPix,  # PIX * pixs
                                      LPBox,  # BOX * box
                                      LPPix,  # PIX * pixm
                                      c_int_p,  # l_int32 * tab
                                      c_float_p,  # l_float32 * pfract
                                      ),
        'pixaFindWidthHeightRatio': (LPNuma,  # NUMA *
                                     LPPixa,  # PIXA * pixa
                                     ),
        'pixaFindWidthHeightProduct': (LPNuma,  # NUMA *
                                       LPPixa,  # PIXA * pixa
                                       ),
        'pixFindOverlapFraction': (c_int,
                                   LPPix,  # PIX * pixs1
                                   LPPix,  # PIX * pixs2
                                   c_int,  # l_int32 x2
                                   c_int,  # l_int32 y2
                                   c_int_p,  # l_int32 * tab
                                   c_float_p,  # l_float32 * pratio
                                   c_int_p,  # l_int32 * pnoverlap
                                   ),
        'pixFindRectangleComps': (LPBoxa,  # BOXA *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 dist
                                  c_int,  # l_int32 minw
                                  c_int,  # l_int32 minh
                                  ),
        'pixConformsToRectangle': (c_int,
                                   LPPix,  # PIX * pixs
                                   LPBox,  # BOX * box
                                   c_int,  # l_int32 dist
                                   c_int_p,  # l_int32 * pconforms
                                   ),
        'pixClipRectangles': (LPPixa,  # PIXA *
                              LPPix,  # PIX * pixs
                              LPBoxa,  # BOXA * boxa
                              ),
        'pixClipRectangle': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             LPBox,  # BOX * box
                             LPLPBox,  # BOX ** pboxc
                             ),
        'pixClipRectangleWithBorder': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixs
                                       LPBox,  # BOX * box
                                       c_int,  # l_int32 maxbord
                                       LPLPBox,  # BOX ** pboxn
                                       ),
        'pixClipMasked': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          LPPix,  # PIX * pixm
                          c_int,  # l_int32 x
                          c_int,  # l_int32 y
                          c_uint,  # l_uint32 outval
                          ),
        'pixCropToMatch': (c_int,
                           LPPix,  # PIX * pixs1
                           LPPix,  # PIX * pixs2
                           LPLPPix,  # PIX ** ppixd1
                           LPLPPix,  # PIX ** ppixd2
                           ),
        'pixCropToSize': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 w
                          c_int,  # l_int32 h
                          ),
        'pixResizeToMatch': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             LPPix,  # PIX * pixt
                             c_int,  # l_int32 w
                             c_int,  # l_int32 h
                             ),
        'pixSelectComponentBySize': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 rankorder
                                     c_int,  # l_int32 type
                                     c_int,  # l_int32 connectivity
                                     LPLPBox,  # BOX ** pbox
                                     ),
        'pixFilterComponentBySize': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 rankorder
                                     c_int,  # l_int32 type
                                     c_int,  # l_int32 connectivity
                                     LPLPBox,  # BOX ** pbox
                                     ),
        'pixMakeSymmetricMask': (LPPix,  # PIX *
                                 c_int,  # l_int32 w
                                 c_int,  # l_int32 h
                                 c_float,  # l_float32 hf
                                 c_float,  # l_float32 vf
                                 c_int,  # l_int32 type
                                 ),
        'pixMakeFrameMask': (LPPix,  # PIX *
                             c_int,  # l_int32 w
                             c_int,  # l_int32 h
                             c_float,  # l_float32 hf1
                             c_float,  # l_float32 hf2
                             c_float,  # l_float32 vf1
                             c_float,  # l_float32 vf2
                             ),
        'pixMakeCoveringOfRectangles': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixs
                                        c_int,  # l_int32 maxiters
                                        ),
        'pixFractionFgInMask': (c_int,
                                LPPix,  # PIX * pix1
                                LPPix,  # PIX * pix2
                                c_float_p,  # l_float32 * pfract
                                ),
        'pixClipToForeground': (c_int,
                                LPPix,  # PIX * pixs
                                LPLPPix,  # PIX ** ppixd
                                LPLPBox,  # BOX ** pbox
                                ),
        'pixTestClipToForeground': (c_int,
                                    LPPix,  # PIX * pixs
                                    c_int_p,  # l_int32 * pcanclip
                                    ),
        'pixClipBoxToForeground': (c_int,
                                   LPPix,  # PIX * pixs
                                   LPBox,  # BOX * boxs
                                   LPLPPix,  # PIX ** ppixd
                                   LPLPBox,  # BOX ** pboxd
                                   ),
        'pixScanForForeground': (c_int,
                                 LPPix,  # PIX * pixs
                                 LPBox,  # BOX * box
                                 c_int,  # l_int32 scanflag
                                 c_int_p,  # l_int32 * ploc
                                 ),
        'pixClipBoxToEdges': (c_int,
                              LPPix,  # PIX * pixs
                              LPBox,  # BOX * boxs
                              c_int,  # l_int32 lowthresh
                              c_int,  # l_int32 highthresh
                              c_int,  # l_int32 maxwidth
                              c_int,  # l_int32 factor
                              LPLPPix,  # PIX ** ppixd
                              LPLPBox,  # BOX ** pboxd
                              ),
        'pixScanForEdge': (c_int,
                           LPPix,  # PIX * pixs
                           LPBox,  # BOX * box
                           c_int,  # l_int32 lowthresh
                           c_int,  # l_int32 highthresh
                           c_int,  # l_int32 maxwidth
                           c_int,  # l_int32 factor
                           c_int,  # l_int32 scanflag
                           c_int_p,  # l_int32 * ploc
                           ),
        'pixExtractOnLine': (LPNuma,  # NUMA *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 x1
                             c_int,  # l_int32 y1
                             c_int,  # l_int32 x2
                             c_int,  # l_int32 y2
                             c_int,  # l_int32 factor
                             ),
        'pixAverageOnLine': (c_float,
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 x1
                             c_int,  # l_int32 y1
                             c_int,  # l_int32 x2
                             c_int,  # l_int32 y2
                             c_int,  # l_int32 factor
                             ),
        'pixAverageIntensityProfile': (LPNuma,  # NUMA *
                                       LPPix,  # PIX * pixs
                                       c_float,  # l_float32 fract
                                       c_int,  # l_int32 dir
                                       c_int,  # l_int32 first
                                       c_int,  # l_int32 last
                                       c_int,  # l_int32 factor1
                                       c_int,  # l_int32 factor2
                                       ),
        'pixReversalProfile': (LPNuma,  # NUMA *
                               LPPix,  # PIX * pixs
                               c_float,  # l_float32 fract
                               c_int,  # l_int32 dir
                               c_int,  # l_int32 first
                               c_int,  # l_int32 last
                               c_int,  # l_int32 minreversal
                               c_int,  # l_int32 factor1
                               c_int,  # l_int32 factor2
                               ),
        'pixWindowedVarianceOnLine': (c_int,
                                      LPPix,  # PIX * pixs
                                      c_int,  # l_int32 dir
                                      c_int,  # l_int32 loc
                                      c_int,  # l_int32 c1
                                      c_int,  # l_int32 c2
                                      c_int,  # l_int32 size
                                      LPLPNuma,  # NUMA ** pnad
                                      ),
        'pixMinMaxNearLine': (c_int,
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 x1
                              c_int,  # l_int32 y1
                              c_int,  # l_int32 x2
                              c_int,  # l_int32 y2
                              c_int,  # l_int32 dist
                              c_int,  # l_int32 direction
                              LPLPNuma,  # NUMA ** pnamin
                              LPLPNuma,  # NUMA ** pnamax
                              c_float_p,  # l_float32 * pminave
                              c_float_p,  # l_float32 * pmaxave
                              ),
        'pixRankRowTransform': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                ),
        'pixRankColumnTransform': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   ),
        'pixaCreate': (LPPixa,  # PIXA *
                       c_int,  # l_int32 n
                       ),
        'pixaCreateFromPix': (LPPixa,  # PIXA *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 n
                              c_int,  # l_int32 cellw
                              c_int,  # l_int32 cellh
                              ),
        'pixaCreateFromBoxa': (LPPixa,  # PIXA *
                               LPPix,  # PIX * pixs
                               LPBoxa,  # BOXA * boxa
                               c_int,  # l_int32 start
                               c_int,  # l_int32 num
                               c_int_p,  # l_int32 * pcropwarn
                               ),
        'pixaSplitPix': (LPPixa,  # PIXA *
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 nx
                         c_int,  # l_int32 ny
                         c_int,  # l_int32 borderwidth
                         c_uint,  # l_uint32 bordercolor
                         ),
        'pixaDestroy': (None,
                        LPLPPixa,  # PIXA ** ppixa
                        ),
        'pixaCopy': (LPPixa,  # PIXA *
                     LPPixa,  # PIXA * pixa
                     c_int,  # l_int32 copyflag
                     ),
        'pixaAddPix': (c_int,
                       LPPixa,  # PIXA * pixa
                       LPPix,  # PIX * pix
                       c_int,  # l_int32 copyflag
                       ),
        'pixaAddBox': (c_int,
                       LPPixa,  # PIXA * pixa
                       LPBox,  # BOX * box
                       c_int,  # l_int32 copyflag
                       ),
        'pixaExtendArrayToSize': (c_int,
                                  LPPixa,  # PIXA * pixa
                                  c_size_t,  # size_t size
                                  ),
        'pixaGetCount': (c_int,
                         LPPixa,  # PIXA * pixa
                         ),
        'pixaChangeRefcount': (c_int,
                               LPPixa,  # PIXA * pixa
                               c_int,  # l_int32 delta
                               ),
        'pixaGetPix': (LPPix,  # PIX *
                       LPPixa,  # PIXA * pixa
                       c_int,  # l_int32 index
                       c_int,  # l_int32 accesstype
                       ),
        'pixaGetPixDimensions': (c_int,
                                 LPPixa,  # PIXA * pixa
                                 c_int,  # l_int32 index
                                 c_int_p,  # l_int32 * pw
                                 c_int_p,  # l_int32 * ph
                                 c_int_p,  # l_int32 * pd
                                 ),
        'pixaGetBoxa': (LPBoxa,  # BOXA *
                        LPPixa,  # PIXA * pixa
                        c_int,  # l_int32 accesstype
                        ),
        'pixaGetBoxaCount': (c_int,
                             LPPixa,  # PIXA * pixa
                             ),
        'pixaGetBox': (LPBox,  # BOX *
                       LPPixa,  # PIXA * pixa
                       c_int,  # l_int32 index
                       c_int,  # l_int32 accesstype
                       ),
        'pixaGetBoxGeometry': (c_int,
                               LPPixa,  # PIXA * pixa
                               c_int,  # l_int32 index
                               c_int_p,  # l_int32 * px
                               c_int_p,  # l_int32 * py
                               c_int_p,  # l_int32 * pw
                               c_int_p,  # l_int32 * ph
                               ),
        'pixaSetBoxa': (c_int,
                        LPPixa,  # PIXA * pixa
                        LPBoxa,  # BOXA * boxa
                        c_int,  # l_int32 accesstype
                        ),
        'pixaGetPixArray': (LPLPPix,  # PIX *
                            LPPixa,  # PIXA * pixa
                            ),
        'pixaVerifyDepth': (c_int,
                            LPPixa,  # PIXA * pixa
                            c_int_p,  # l_int32 * psame
                            c_int_p,  # l_int32 * pmaxd
                            ),
        'pixaVerifyDimensions': (c_int,
                                 LPPixa,  # PIXA * pixa
                                 c_int_p,  # l_int32 * psame
                                 c_int_p,  # l_int32 * pmaxw
                                 c_int_p,  # l_int32 * pmaxh
                                 ),
        'pixaIsFull': (c_int,
                       LPPixa,  # PIXA * pixa
                       c_int_p,  # l_int32 * pfullpa
                       c_int_p,  # l_int32 * pfullba
                       ),
        'pixaCountText': (c_int,
                          LPPixa,  # PIXA * pixa
                          c_int_p,  # l_int32 * pntext
                          ),
        'pixaSetText': (c_int,
                        LPPixa,  # PIXA * pixa
                        c_char_p,  # const char * text
                        LPSarray,  # SARRAY * sa
                        ),
        'pixaGetLinePtrs': (POINTER(POINTER(c_void_p)),
                            LPPixa,  # PIXA * pixa
                            c_int_p,  # l_int32 * psize
                            ),
        'pixaWriteStreamInfo': (c_int,
                                LPFile,  # FILE * fp
                                LPPixa,  # PIXA * pixa
                                ),
        'pixaReplacePix': (c_int,
                           LPPixa,  # PIXA * pixa
                           c_int,  # l_int32 index
                           LPPix,  # PIX * pix
                           LPBox,  # BOX * box
                           ),
        'pixaInsertPix': (c_int,
                          LPPixa,  # PIXA * pixa
                          c_int,  # l_int32 index
                          LPPix,  # PIX * pixs
                          LPBox,  # BOX * box
                          ),
        'pixaRemovePix': (c_int,
                          LPPixa,  # PIXA * pixa
                          c_int,  # l_int32 index
                          ),
        'pixaRemovePixAndSave': (c_int,
                                 LPPixa,  # PIXA * pixa
                                 c_int,  # l_int32 index
                                 LPLPPix,  # PIX ** ppix
                                 LPLPBox,  # BOX ** pbox
                                 ),
        'pixaRemoveSelected': (c_int,
                               LPPixa,  # PIXA * pixa
                               LPNuma,  # NUMA * naindex
                               ),
        'pixaInitFull': (c_int,
                         LPPixa,  # PIXA * pixa
                         LPPix,  # PIX * pix
                         LPBox,  # BOX * box
                         ),
        'pixaClear': (c_int,
                      LPPixa,  # PIXA * pixa
                      ),
        'pixaJoin': (c_int,
                     LPPixa,  # PIXA * pixad
                     LPPixa,  # PIXA * pixas
                     c_int,  # l_int32 istart
                     c_int,  # l_int32 iend
                     ),
        'pixaInterleave': (LPPixa,  # PIXA *
                           LPPixa,  # PIXA * pixa1
                           LPPixa,  # PIXA * pixa2
                           c_int,  # l_int32 copyflag
                           ),
        'pixaaJoin': (c_int,
                      LPPixaa,  # PIXAA * paad
                      LPPixaa,  # PIXAA * paas
                      c_int,  # l_int32 istart
                      c_int,  # l_int32 iend
                      ),
        'pixaaCreate': (LPPixaa,  # PIXAA *
                        c_int,  # l_int32 n
                        ),
        'pixaaCreateFromPixa': (LPPixaa,  # PIXAA *
                                LPPixa,  # PIXA * pixa
                                c_int,  # l_int32 n
                                c_int,  # l_int32 type
                                c_int,  # l_int32 copyflag
                                ),
        'pixaaDestroy': (None,
                         LPLPPixaa,  # PIXAA ** ppaa
                         ),
        'pixaaAddPixa': (c_int,
                         LPPixaa,  # PIXAA * paa
                         LPPixa,  # PIXA * pixa
                         c_int,  # l_int32 copyflag
                         ),
        'pixaaAddPix': (c_int,
                        LPPixaa,  # PIXAA * paa
                        c_int,  # l_int32 index
                        LPPix,  # PIX * pix
                        LPBox,  # BOX * box
                        c_int,  # l_int32 copyflag
                        ),
        'pixaaAddBox': (c_int,
                        LPPixaa,  # PIXAA * paa
                        LPBox,  # BOX * box
                        c_int,  # l_int32 copyflag
                        ),
        'pixaaGetCount': (c_int,
                          LPPixaa,  # PIXAA * paa
                          LPLPNuma,  # NUMA ** pna
                          ),
        'pixaaGetPixa': (LPPixa,  # PIXA *
                         LPPixaa,  # PIXAA * paa
                         c_int,  # l_int32 index
                         c_int,  # l_int32 accesstype
                         ),
        'pixaaGetBoxa': (LPBoxa,  # BOXA *
                         LPPixaa,  # PIXAA * paa
                         c_int,  # l_int32 accesstype
                         ),
        'pixaaGetPix': (LPPix,  # PIX *
                        LPPixaa,  # PIXAA * paa
                        c_int,  # l_int32 index
                        c_int,  # l_int32 ipix
                        c_int,  # l_int32 accessflag
                        ),
        'pixaaVerifyDepth': (c_int,
                             LPPixaa,  # PIXAA * paa
                             c_int_p,  # l_int32 * psame
                             c_int_p,  # l_int32 * pmaxd
                             ),
        'pixaaVerifyDimensions': (c_int,
                                  LPPixaa,  # PIXAA * paa
                                  c_int_p,  # l_int32 * psame
                                  c_int_p,  # l_int32 * pmaxw
                                  c_int_p,  # l_int32 * pmaxh
                                  ),
        'pixaaIsFull': (c_int,
                        LPPixaa,  # PIXAA * paa
                        c_int_p,  # l_int32 * pfull
                        ),
        'pixaaInitFull': (c_int,
                          LPPixaa,  # PIXAA * paa
                          LPPixa,  # PIXA * pixa
                          ),
        'pixaaReplacePixa': (c_int,
                             LPPixaa,  # PIXAA * paa
                             c_int,  # l_int32 index
                             LPPixa,  # PIXA * pixa
                             ),
        'pixaaClear': (c_int,
                       LPPixaa,  # PIXAA * paa
                       ),
        'pixaaTruncate': (c_int,
                          LPPixaa,  # PIXAA * paa
                          ),
        'pixaRead': (LPPixa,  # PIXA *
                     c_char_p,  # const char * filename
                     ),
        'pixaReadStream': (LPPixa,  # PIXA *
                           LPFile,  # FILE * fp
                           ),
        'pixaReadMem': (LPPixa,  # PIXA *
                        c_ubyte_p,  # const l_uint8 * data
                        c_size_t,  # size_t size
                        ),
        'pixaWriteDebug': (c_int,
                           c_char_p,  # const char * fname
                           LPPixa,  # PIXA * pixa
                           ),
        'pixaWrite': (c_int,
                      c_char_p,  # const char * filename
                      LPPixa,  # PIXA * pixa
                      ),
        'pixaWriteStream': (c_int,
                            LPFile,  # FILE * fp
                            LPPixa,  # PIXA * pixa
                            ),
        'pixaWriteMem': (c_int,
                         POINTER(c_ubyte_p),  # l_uint8 ** pdata
                         c_size_t_p,  # size_t * psize
                         LPPixa,  # PIXA * pixa
                         ),
        'pixaReadBoth': (LPPixa,  # PIXA *
                         c_char_p,  # const char * filename
                         ),
        'pixaaReadFromFiles': (LPPixaa,  # PIXAA *
                               c_char_p,  # const char * dirname
                               c_char_p,  # const char * substr
                               c_int,  # l_int32 first
                               c_int,  # l_int32 nfiles
                               ),
        'pixaaRead': (LPPixaa,  # PIXAA *
                      c_char_p,  # const char * filename
                      ),
        'pixaaReadStream': (LPPixaa,  # PIXAA *
                            LPFile,  # FILE * fp
                            ),
        'pixaaReadMem': (LPPixaa,  # PIXAA *
                         c_ubyte_p,  # const l_uint8 * data
                         c_size_t,  # size_t size
                         ),
        'pixaaWrite': (c_int,
                       c_char_p,  # const char * filename
                       LPPixaa,  # PIXAA * paa
                       ),
        'pixaaWriteStream': (c_int,
                             LPFile,  # FILE * fp
                             LPPixaa,  # PIXAA * paa
                             ),
        'pixaaWriteMem': (c_int,
                          POINTER(c_ubyte_p),  # l_uint8 ** pdata
                          c_size_t_p,  # size_t * psize
                          LPPixaa,  # PIXAA * paa
                          ),
        'pixaccCreate': (LPPixacc,  # PIXACC *
                         c_int,  # l_int32 w
                         c_int,  # l_int32 h
                         c_int,  # l_int32 negflag
                         ),
        'pixaccCreateFromPix': (LPPixacc,  # PIXACC *
                                LPPix,  # PIX * pix
                                c_int,  # l_int32 negflag
                                ),
        'pixaccDestroy': (None,
                          LPLPPixacc,  # PIXACC ** ppixacc
                          ),
        'pixaccFinal': (LPPix,  # PIX *
                        LPPixacc,  # PIXACC * pixacc
                        c_int,  # l_int32 outdepth
                        ),
        'pixaccGetPix': (LPPix,  # PIX *
                         LPPixacc,  # PIXACC * pixacc
                         ),
        'pixaccGetOffset': (c_int,
                            LPPixacc,  # PIXACC * pixacc
                            ),
        'pixaccAdd': (c_int,
                      LPPixacc,  # PIXACC * pixacc
                      LPPix,  # PIX * pix
                      ),
        'pixaccSubtract': (c_int,
                           LPPixacc,  # PIXACC * pixacc
                           LPPix,  # PIX * pix
                           ),
        'pixaccMultConst': (c_int,
                            LPPixacc,  # PIXACC * pixacc
                            c_float,  # l_float32 factor
                            ),
        'pixaccMultConstAccumulate': (c_int,
                                      LPPixacc,  # PIXACC * pixacc
                                      LPPix,  # PIX * pix
                                      c_float,  # l_float32 factor
                                      ),
        'pixSelectBySize': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 width
                            c_int,  # l_int32 height
                            c_int,  # l_int32 connectivity
                            c_int,  # l_int32 type
                            c_int,  # l_int32 relation
                            c_int_p,  # l_int32 * pchanged
                            ),
        'pixaSelectBySize': (LPPixa,  # PIXA *
                             LPPixa,  # PIXA * pixas
                             c_int,  # l_int32 width
                             c_int,  # l_int32 height
                             c_int,  # l_int32 type
                             c_int,  # l_int32 relation
                             c_int_p,  # l_int32 * pchanged
                             ),
        'pixaMakeSizeIndicator': (LPNuma,  # NUMA *
                                  LPPixa,  # PIXA * pixa
                                  c_int,  # l_int32 width
                                  c_int,  # l_int32 height
                                  c_int,  # l_int32 type
                                  c_int,  # l_int32 relation
                                  ),
        'pixSelectByPerimToAreaRatio': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixs
                                        c_float,  # l_float32 thresh
                                        c_int,  # l_int32 connectivity
                                        c_int,  # l_int32 type
                                        c_int_p,  # l_int32 * pchanged
                                        ),
        'pixaSelectByPerimToAreaRatio': (LPPixa,  # PIXA *
                                         LPPixa,  # PIXA * pixas
                                         c_float,  # l_float32 thresh
                                         c_int,  # l_int32 type
                                         c_int_p,  # l_int32 * pchanged
                                         ),
        'pixSelectByPerimSizeRatio': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      c_float,  # l_float32 thresh
                                      c_int,  # l_int32 connectivity
                                      c_int,  # l_int32 type
                                      c_int_p,  # l_int32 * pchanged
                                      ),
        'pixaSelectByPerimSizeRatio': (LPPixa,  # PIXA *
                                       LPPixa,  # PIXA * pixas
                                       c_float,  # l_float32 thresh
                                       c_int,  # l_int32 type
                                       c_int_p,  # l_int32 * pchanged
                                       ),
        'pixSelectByAreaFraction': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_float,  # l_float32 thresh
                                    c_int,  # l_int32 connectivity
                                    c_int,  # l_int32 type
                                    c_int_p,  # l_int32 * pchanged
                                    ),
        'pixaSelectByAreaFraction': (LPPixa,  # PIXA *
                                     LPPixa,  # PIXA * pixas
                                     c_float,  # l_float32 thresh
                                     c_int,  # l_int32 type
                                     c_int_p,  # l_int32 * pchanged
                                     ),
        'pixSelectByArea': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_float,  # l_float32 thresh
                            c_int,  # l_int32 connectivity
                            c_int,  # l_int32 type
                            c_int_p,  # l_int32 * pchanged
                            ),
        'pixaSelectByArea': (LPPixa,  # PIXA *
                             LPPixa,  # PIXA * pixas
                             c_float,  # l_float32 thresh
                             c_int,  # l_int32 type
                             c_int_p,  # l_int32 * pchanged
                             ),
        'pixSelectByWidthHeightRatio': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixs
                                        c_float,  # l_float32 thresh
                                        c_int,  # l_int32 connectivity
                                        c_int,  # l_int32 type
                                        c_int_p,  # l_int32 * pchanged
                                        ),
        'pixaSelectByWidthHeightRatio': (LPPixa,  # PIXA *
                                         LPPixa,  # PIXA * pixas
                                         c_float,  # l_float32 thresh
                                         c_int,  # l_int32 type
                                         c_int_p,  # l_int32 * pchanged
                                         ),
        'pixaSelectByNumConnComp': (LPPixa,  # PIXA *
                                    LPPixa,  # PIXA * pixas
                                    c_int,  # l_int32 nmin
                                    c_int,  # l_int32 nmax
                                    c_int,  # l_int32 connectivity
                                    c_int_p,  # l_int32 * pchanged
                                    ),
        'pixaSelectWithIndicator': (LPPixa,  # PIXA *
                                    LPPixa,  # PIXA * pixas
                                    LPNuma,  # NUMA * na
                                    c_int_p,  # l_int32 * pchanged
                                    ),
        'pixRemoveWithIndicator': (c_int,
                                   LPPix,  # PIX * pixs
                                   LPPixa,  # PIXA * pixa
                                   LPNuma,  # NUMA * na
                                   ),
        'pixAddWithIndicator': (c_int,
                                LPPix,  # PIX * pixs
                                LPPixa,  # PIXA * pixa
                                LPNuma,  # NUMA * na
                                ),
        'pixaSelectWithString': (LPPixa,  # PIXA *
                                 LPPixa,  # PIXA * pixas
                                 c_char_p,  # const char * str
                                 c_int_p,  # l_int32 * perror
                                 ),
        'pixaRenderComponent': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                LPPixa,  # PIXA * pixa
                                c_int,  # l_int32 index
                                ),
        'pixaSort': (LPPixa,  # PIXA *
                     LPPixa,  # PIXA * pixas
                     c_int,  # l_int32 sorttype
                     c_int,  # l_int32 sortorder
                     LPLPNuma,  # NUMA ** pnaindex
                     c_int,  # l_int32 copyflag
                     ),
        'pixaBinSort': (LPPixa,  # PIXA *
                        LPPixa,  # PIXA * pixas
                        c_int,  # l_int32 sorttype
                        c_int,  # l_int32 sortorder
                        LPLPNuma,  # NUMA ** pnaindex
                        c_int,  # l_int32 copyflag
                        ),
        'pixaSortByIndex': (LPPixa,  # PIXA *
                            LPPixa,  # PIXA * pixas
                            LPNuma,  # NUMA * naindex
                            c_int,  # l_int32 copyflag
                            ),
        'pixaSort2dByIndex': (LPPixaa,  # PIXAA *
                              LPPixa,  # PIXA * pixas
                              LPNumaa,  # NUMAA * naa
                              c_int,  # l_int32 copyflag
                              ),
        'pixaSelectRange': (LPPixa,  # PIXA *
                            LPPixa,  # PIXA * pixas
                            c_int,  # l_int32 first
                            c_int,  # l_int32 last
                            c_int,  # l_int32 copyflag
                            ),
        'pixaaSelectRange': (LPPixaa,  # PIXAA *
                             LPPixaa,  # PIXAA * paas
                             c_int,  # l_int32 first
                             c_int,  # l_int32 last
                             c_int,  # l_int32 copyflag
                             ),
        'pixaaScaleToSize': (LPPixaa,  # PIXAA *
                             LPPixaa,  # PIXAA * paas
                             c_int,  # l_int32 wd
                             c_int,  # l_int32 hd
                             ),
        'pixaaScaleToSizeVar': (LPPixaa,  # PIXAA *
                                LPPixaa,  # PIXAA * paas
                                LPNuma,  # NUMA * nawd
                                LPNuma,  # NUMA * nahd
                                ),
        'pixaScaleToSize': (LPPixa,  # PIXA *
                            LPPixa,  # PIXA * pixas
                            c_int,  # l_int32 wd
                            c_int,  # l_int32 hd
                            ),
        'pixaScaleToSizeRel': (LPPixa,  # PIXA *
                               LPPixa,  # PIXA * pixas
                               c_int,  # l_int32 delw
                               c_int,  # l_int32 delh
                               ),
        'pixaScale': (LPPixa,  # PIXA *
                      LPPixa,  # PIXA * pixas
                      c_float,  # l_float32 scalex
                      c_float,  # l_float32 scaley
                      ),
        'pixaScaleBySampling': (LPPixa,  # PIXA *
                                LPPixa,  # PIXA * pixas
                                c_float,  # l_float32 scalex
                                c_float,  # l_float32 scaley
                                ),
        'pixaRotate': (LPPixa,  # PIXA *
                       LPPixa,  # PIXA * pixas
                       c_float,  # l_float32 angle
                       c_int,  # l_int32 type
                       c_int,  # l_int32 incolor
                       c_int,  # l_int32 width
                       c_int,  # l_int32 height
                       ),
        'pixaRotateOrth': (LPPixa,  # PIXA *
                           LPPixa,  # PIXA * pixas
                           c_int,  # l_int32 rotation
                           ),
        'pixaTranslate': (LPPixa,  # PIXA *
                          LPPixa,  # PIXA * pixas
                          c_int,  # l_int32 hshift
                          c_int,  # l_int32 vshift
                          c_int,  # l_int32 incolor
                          ),
        'pixaAddBorderGeneral': (LPPixa,  # PIXA *
                                 LPPixa,  # PIXA * pixad
                                 LPPixa,  # PIXA * pixas
                                 c_int,  # l_int32 left
                                 c_int,  # l_int32 right
                                 c_int,  # l_int32 top
                                 c_int,  # l_int32 bot
                                 c_uint,  # l_uint32 val
                                 ),
        'pixaaFlattenToPixa': (LPPixa,  # PIXA *
                               LPPixaa,  # PIXAA * paa
                               LPLPNuma,  # NUMA ** pnaindex
                               c_int,  # l_int32 copyflag
                               ),
        'pixaaSizeRange': (c_int,
                           LPPixaa,  # PIXAA * paa
                           c_int_p,  # l_int32 * pminw
                           c_int_p,  # l_int32 * pminh
                           c_int_p,  # l_int32 * pmaxw
                           c_int_p,  # l_int32 * pmaxh
                           ),
        'pixaSizeRange': (c_int,
                          LPPixa,  # PIXA * pixa
                          c_int_p,  # l_int32 * pminw
                          c_int_p,  # l_int32 * pminh
                          c_int_p,  # l_int32 * pmaxw
                          c_int_p,  # l_int32 * pmaxh
                          ),
        'pixaClipToPix': (LPPixa,  # PIXA *
                          LPPixa,  # PIXA * pixas
                          LPPix,  # PIX * pixs
                          ),
        'pixaClipToForeground': (c_int,
                                 LPPixa,  # PIXA * pixas
                                 LPLPPixa,  # PIXA ** ppixad
                                 LPLPBoxa,  # BOXA ** pboxa
                                 ),
        'pixaGetRenderingDepth': (c_int,
                                  LPPixa,  # PIXA * pixa
                                  c_int_p,  # l_int32 * pdepth
                                  ),
        'pixaHasColor': (c_int,
                         LPPixa,  # PIXA * pixa
                         c_int_p,  # l_int32 * phascolor
                         ),
        'pixaAnyColormaps': (c_int,
                             LPPixa,  # PIXA * pixa
                             c_int_p,  # l_int32 * phascmap
                             ),
        'pixaGetDepthInfo': (c_int,
                             LPPixa,  # PIXA * pixa
                             c_int_p,  # l_int32 * pmaxdepth
                             c_int_p,  # l_int32 * psame
                             ),
        'pixaConvertToSameDepth': (LPPixa,  # PIXA *
                                   LPPixa,  # PIXA * pixas
                                   ),
        'pixaConvertToGivenDepth': (LPPixa,  # PIXA *
                                    LPPixa,  # PIXA * pixas
                                    c_int,  # l_int32 depth
                                    ),
        'pixaEqual': (c_int,
                      LPPixa,  # PIXA * pixa1
                      LPPixa,  # PIXA * pixa2
                      c_int,  # l_int32 maxdist
                      LPLPNuma,  # NUMA ** pnaindex
                      c_int_p,  # l_int32 * psame
                      ),
        'pixaSetFullSizeBoxa': (c_int,
                                LPPixa,  # PIXA * pixa
                                ),
        'pixaDisplay': (LPPix,  # PIX *
                        LPPixa,  # PIXA * pixa
                        c_int,  # l_int32 w
                        c_int,  # l_int32 h
                        ),
        'pixaDisplayRandomCmap': (LPPix,  # PIX *
                                  LPPixa,  # PIXA * pixa
                                  c_int,  # l_int32 w
                                  c_int,  # l_int32 h
                                  ),
        'pixaDisplayLinearly': (LPPix,  # PIX *
                                LPPixa,  # PIXA * pixas
                                c_int,  # l_int32 direction
                                c_float,  # l_float32 scalefactor
                                c_int,  # l_int32 background
                                c_int,  # l_int32 spacing
                                c_int,  # l_int32 border
                                LPLPBoxa,  # BOXA ** pboxa
                                ),
        'pixaDisplayOnLattice': (LPPix,  # PIX *
                                 LPPixa,  # PIXA * pixa
                                 c_int,  # l_int32 cellw
                                 c_int,  # l_int32 cellh
                                 c_int_p,  # l_int32 * pncols
                                 LPLPBoxa,  # BOXA ** pboxa
                                 ),
        'pixaDisplayUnsplit': (LPPix,  # PIX *
                               LPPixa,  # PIXA * pixa
                               c_int,  # l_int32 nx
                               c_int,  # l_int32 ny
                               c_int,  # l_int32 borderwidth
                               c_uint,  # l_uint32 bordercolor
                               ),
        'pixaDisplayTiled': (LPPix,  # PIX *
                             LPPixa,  # PIXA * pixa
                             c_int,  # l_int32 maxwidth
                             c_int,  # l_int32 background
                             c_int,  # l_int32 spacing
                             ),
        'pixaDisplayTiledInRows': (LPPix,  # PIX *
                                   LPPixa,  # PIXA * pixa
                                   c_int,  # l_int32 outdepth
                                   c_int,  # l_int32 maxwidth
                                   c_float,  # l_float32 scalefactor
                                   c_int,  # l_int32 background
                                   c_int,  # l_int32 spacing
                                   c_int,  # l_int32 border
                                   ),
        'pixaDisplayTiledInColumns': (LPPix,  # PIX *
                                      LPPixa,  # PIXA * pixas
                                      c_int,  # l_int32 nx
                                      c_float,  # l_float32 scalefactor
                                      c_int,  # l_int32 spacing
                                      c_int,  # l_int32 border
                                      ),
        'pixaDisplayTiledAndScaled': (LPPix,  # PIX *
                                      LPPixa,  # PIXA * pixa
                                      c_int,  # l_int32 outdepth
                                      c_int,  # l_int32 tilewidth
                                      c_int,  # l_int32 ncols
                                      c_int,  # l_int32 background
                                      c_int,  # l_int32 spacing
                                      c_int,  # l_int32 border
                                      ),
        'pixaDisplayTiledWithText': (LPPix,  # PIX *
                                     LPPixa,  # PIXA * pixa
                                     c_int,  # l_int32 maxwidth
                                     c_float,  # l_float32 scalefactor
                                     c_int,  # l_int32 spacing
                                     c_int,  # l_int32 border
                                     c_int,  # l_int32 fontsize
                                     c_uint,  # l_uint32 textcolor
                                     ),
        'pixaDisplayTiledByIndex': (LPPix,  # PIX *
                                    LPPixa,  # PIXA * pixa
                                    LPNuma,  # NUMA * na
                                    c_int,  # l_int32 width
                                    c_int,  # l_int32 spacing
                                    c_int,  # l_int32 border
                                    c_int,  # l_int32 fontsize
                                    c_uint,  # l_uint32 textcolor
                                    ),
        'pixaDisplayPairTiledInColumns': (LPPix,  # PIX *
                                          LPPixa,  # PIXA * pixas1
                                          LPPixa,  # PIXA * pixas2
                                          c_int,  # l_int32 nx
                                          c_float,  # l_float32 scalefactor
                                          c_int,  # l_int32 spacing1
                                          c_int,  # l_int32 spacing2
                                          c_int,  # l_int32 border1
                                          c_int,  # l_int32 border2
                                          c_int,  # l_int32 fontsize
                                          c_int,  # l_int32 startindex
                                          LPSarray,  # SARRAY * sa
                                          ),
        'pixaaDisplay': (LPPix,  # PIX *
                         LPPixaa,  # PIXAA * paa
                         c_int,  # l_int32 w
                         c_int,  # l_int32 h
                         ),
        'pixaaDisplayByPixa': (LPPix,  # PIX *
                               LPPixaa,  # PIXAA * paa
                               c_int,  # l_int32 maxnx
                               c_float,  # l_float32 scalefactor
                               c_int,  # l_int32 hspacing
                               c_int,  # l_int32 vspacing
                               c_int,  # l_int32 border
                               ),
        'pixaaDisplayTiledAndScaled': (LPPixa,  # PIXA *
                                       LPPixaa,  # PIXAA * paa
                                       c_int,  # l_int32 outdepth
                                       c_int,  # l_int32 tilewidth
                                       c_int,  # l_int32 ncols
                                       c_int,  # l_int32 background
                                       c_int,  # l_int32 spacing
                                       c_int,  # l_int32 border
                                       ),
        'pixaConvertTo1': (LPPixa,  # PIXA *
                           LPPixa,  # PIXA * pixas
                           c_int,  # l_int32 thresh
                           ),
        'pixaConvertTo8': (LPPixa,  # PIXA *
                           LPPixa,  # PIXA * pixas
                           c_int,  # l_int32 cmapflag
                           ),
        'pixaConvertTo8Colormap': (LPPixa,  # PIXA *
                                   LPPixa,  # PIXA * pixas
                                   c_int,  # l_int32 dither
                                   ),
        'pixaConvertTo32': (LPPixa,  # PIXA *
                            LPPixa,  # PIXA * pixas
                            ),
        'pixaConstrainedSelect': (LPPixa,  # PIXA *
                                  LPPixa,  # PIXA * pixas
                                  c_int,  # l_int32 first
                                  c_int,  # l_int32 last
                                  c_int,  # l_int32 nmax
                                  c_int,  # l_int32 use_pairs
                                  c_int,  # l_int32 copyflag
                                  ),
        'pixaSelectToPdf': (c_int,
                            LPPixa,  # PIXA * pixas
                            c_int,  # l_int32 first
                            c_int,  # l_int32 last
                            c_int,  # l_int32 res
                            c_float,  # l_float32 scalefactor
                            c_int,  # l_int32 type
                            c_int,  # l_int32 quality
                            c_uint,  # l_uint32 color
                            c_int,  # l_int32 fontsize
                            c_char_p,  # const char * fileout
                            ),
        'pixaMakeFromTiledPixa': (LPPixa,  # PIXA *
                                  LPPixa,  # PIXA * pixas
                                  c_int,  # l_int32 w
                                  c_int,  # l_int32 h
                                  c_int,  # l_int32 nsamp
                                  ),
        'pixaMakeFromTiledPix': (LPPixa,  # PIXA *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 w
                                 c_int,  # l_int32 h
                                 c_int,  # l_int32 start
                                 c_int,  # l_int32 num
                                 LPBoxa,  # BOXA * boxa
                                 ),
        'pixGetTileCount': (c_int,
                            LPPix,  # PIX * pix
                            c_int_p,  # l_int32 * pn
                            ),
        'pixaDisplayMultiTiled': (LPPixa,  # PIXA *
                                  LPPixa,  # PIXA * pixas
                                  c_int,  # l_int32 nx
                                  c_int,  # l_int32 ny
                                  c_int,  # l_int32 maxw
                                  c_int,  # l_int32 maxh
                                  c_float,  # l_float32 scalefactor
                                  c_int,  # l_int32 spacing
                                  c_int,  # l_int32 border
                                  ),
        'pixaSplitIntoFiles': (c_int,
                               LPPixa,  # PIXA * pixas
                               c_int,  # l_int32 nsplit
                               c_float,  # l_float32 scale
                               c_int,  # l_int32 outwidth
                               c_int,  # l_int32 write_pixa
                               c_int,  # l_int32 write_pix
                               c_int,  # l_int32 write_pdf
                               ),
        'convertToNUpFiles': (c_int,
                              c_char_p,  # const char * dir
                              c_char_p,  # const char * substr
                              c_int,  # l_int32 nx
                              c_int,  # l_int32 ny
                              c_int,  # l_int32 tw
                              c_int,  # l_int32 spacing
                              c_int,  # l_int32 border
                              c_int,  # l_int32 fontsize
                              c_char_p,  # const char * outdir
                              ),
        'convertToNUpPixa': (LPPixa,  # PIXA *
                             c_char_p,  # const char * dir
                             c_char_p,  # const char * substr
                             c_int,  # l_int32 nx
                             c_int,  # l_int32 ny
                             c_int,  # l_int32 tw
                             c_int,  # l_int32 spacing
                             c_int,  # l_int32 border
                             c_int,  # l_int32 fontsize
                             ),
        'pixaConvertToNUpPixa': (LPPixa,  # PIXA *
                                 LPPixa,  # PIXA * pixas
                                 LPSarray,  # SARRAY * sa
                                 c_int,  # l_int32 nx
                                 c_int,  # l_int32 ny
                                 c_int,  # l_int32 tw
                                 c_int,  # l_int32 spacing
                                 c_int,  # l_int32 border
                                 c_int,  # l_int32 fontsize
                                 ),
        'pixaCompareInPdf': (c_int,
                             LPPixa,  # PIXA * pixa1
                             LPPixa,  # PIXA * pixa2
                             c_int,  # l_int32 nx
                             c_int,  # l_int32 ny
                             c_int,  # l_int32 tw
                             c_int,  # l_int32 spacing
                             c_int,  # l_int32 border
                             c_int,  # l_int32 fontsize
                             c_char_p,  # const char * fileout
                             ),
        'pmsCreate': (c_int,
                      c_size_t,  # size_t minsize
                      c_size_t,  # size_t smallest
                      LPNuma,  # NUMA * numalloc
                      c_char_p,  # const char * logfile
                      ),
        'pmsDestroy': (None, ),
        'pmsCustomAlloc': (c_void_p,
                           c_size_t,  # size_t nbytes
                           ),
        'pmsCustomDealloc': (None,
                             c_void_p,  # void * data
                             ),
        'pmsGetAlloc': (c_void_p,
                        c_size_t,  # size_t nbytes
                        ),
        'pmsGetLevelForAlloc': (c_int,
                                c_size_t,  # size_t nbytes
                                c_int_p,  # l_int32 * plevel
                                ),
        'pmsGetLevelForDealloc': (c_int,
                                  c_void_p,  # void * data
                                  c_int_p,  # l_int32 * plevel
                                  ),
        'pmsLogInfo': (None, ),
        'pixAddConstantGray': (c_int,
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 val
                               ),
        'pixMultConstantGray': (c_int,
                                LPPix,  # PIX * pixs
                                c_float,  # l_float32 val
                                ),
        'pixAddGray': (LPPix,  # PIX *
                       LPPix,  # PIX * pixd
                       LPPix,  # PIX * pixs1
                       LPPix,  # PIX * pixs2
                       ),
        'pixSubtractGray': (LPPix,  # PIX *
                            LPPix,  # PIX * pixd
                            LPPix,  # PIX * pixs1
                            LPPix,  # PIX * pixs2
                            ),
        'pixMultiplyGray': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            LPPix,  # PIX * pixg
                            c_float,  # l_float32 norm
                            ),
        'pixThresholdToValue': (LPPix,  # PIX *
                                LPPix,  # PIX * pixd
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 threshval
                                c_int,  # l_int32 setval
                                ),
        'pixInitAccumulate': (LPPix,  # PIX *
                              c_int,  # l_int32 w
                              c_int,  # l_int32 h
                              c_uint,  # l_uint32 offset
                              ),
        'pixFinalAccumulate': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_uint,  # l_uint32 offset
                               c_int,  # l_int32 depth
                               ),
        'pixFinalAccumulateThreshold': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixs
                                        c_uint,  # l_uint32 offset
                                        c_uint,  # l_uint32 threshold
                                        ),
        'pixAccumulate': (c_int,
                          LPPix,  # PIX * pixd
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 op
                          ),
        'pixMultConstAccumulate': (c_int,
                                   LPPix,  # PIX * pixs
                                   c_float,  # l_float32 factor
                                   c_uint,  # l_uint32 offset
                                   ),
        'pixAbsDifference': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs1
                             LPPix,  # PIX * pixs2
                             ),
        'pixAddRGB': (LPPix,  # PIX *
                      LPPix,  # PIX * pixs1
                      LPPix,  # PIX * pixs2
                      ),
        'pixMinOrMax': (LPPix,  # PIX *
                        LPPix,  # PIX * pixd
                        LPPix,  # PIX * pixs1
                        LPPix,  # PIX * pixs2
                        c_int,  # l_int32 type
                        ),
        'pixMaxDynamicRange': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 type
                               ),
        'pixMaxDynamicRangeRGB': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 type
                                  ),
        'linearScaleRGBVal': (c_uint,
                              c_uint,  # l_uint32 sval
                              c_float,  # l_float32 factor
                              ),
        'logScaleRGBVal': (c_uint,
                           c_uint,  # l_uint32 sval
                           c_float_p,  # l_float32 * tab
                           c_float,  # l_float32 factor
                           ),
        'makeLogBase2Tab': (c_float_p, ),
        'getLogBase2': (c_float,
                        c_int,  # l_int32 val
                        c_float_p,  # l_float32 * logtab
                        ),
        'pixcompCreateFromPix': (LPPixComp,  # PIXC *
                                 LPPix,  # PIX * pix
                                 c_int,  # l_int32 comptype
                                 ),
        'pixcompCreateFromString': (LPPixComp,  # PIXC *
                                    c_ubyte_p,  # l_uint8 * data
                                    c_size_t,  # size_t size
                                    c_int,  # l_int32 copyflag
                                    ),
        'pixcompCreateFromFile': (LPPixComp,  # PIXC *
                                  c_char_p,  # const char * filename
                                  c_int,  # l_int32 comptype
                                  ),
        'pixcompDestroy': (None,
                           LPLPPixComp,  # PIXC ** ppixc
                           ),
        'pixcompCopy': (LPPixComp,  # PIXC *
                        LPPixComp,  # PIXC * pixcs
                        ),
        'pixcompGetDimensions': (c_int,
                                 LPPixComp,  # PIXC * pixc
                                 c_int_p,  # l_int32 * pw
                                 c_int_p,  # l_int32 * ph
                                 c_int_p,  # l_int32 * pd
                                 ),
        'pixcompGetParameters': (c_int,
                                 LPPixComp,  # PIXC * pixc
                                 c_int_p,  # l_int32 * pxres
                                 c_int_p,  # l_int32 * pyres
                                 c_int_p,  # l_int32 * pcomptype
                                 c_int_p,  # l_int32 * pcmapflag
                                 ),
        'pixcompDetermineFormat': (c_int,
                                   c_int,  # l_int32 comptype
                                   c_int,  # l_int32 d
                                   c_int,  # l_int32 cmapflag
                                   c_int_p,  # l_int32 * pformat
                                   ),
        'pixCreateFromPixcomp': (LPPix,  # PIX *
                                 LPPixComp,  # PIXC * pixc
                                 ),
        'pixacompCreate': (LPPixaComp,  # PIXAC *
                           c_int,  # l_int32 n
                           ),
        'pixacompCreateWithInit': (LPPixaComp,  # PIXAC *
                                   c_int,  # l_int32 n
                                   c_int,  # l_int32 offset
                                   LPPix,  # PIX * pix
                                   c_int,  # l_int32 comptype
                                   ),
        'pixacompCreateFromPixa': (LPPixaComp,  # PIXAC *
                                   LPPixa,  # PIXA * pixa
                                   c_int,  # l_int32 comptype
                                   c_int,  # l_int32 accesstype
                                   ),
        'pixacompCreateFromFiles': (LPPixaComp,  # PIXAC *
                                    c_char_p,  # const char * dirname
                                    c_char_p,  # const char * substr
                                    c_int,  # l_int32 comptype
                                    ),
        'pixacompCreateFromSA': (LPPixaComp,  # PIXAC *
                                 LPSarray,  # SARRAY * sa
                                 c_int,  # l_int32 comptype
                                 ),
        'pixacompDestroy': (None,
                            LPLPPixaComp,  # PIXAC ** ppixac
                            ),
        'pixacompAddPix': (c_int,
                           LPPixaComp,  # PIXAC * pixac
                           LPPix,  # PIX * pix
                           c_int,  # l_int32 comptype
                           ),
        'pixacompAddPixcomp': (c_int,
                               LPPixaComp,  # PIXAC * pixac
                               LPPixComp,  # PIXC * pixc
                               c_int,  # l_int32 copyflag
                               ),
        'pixacompReplacePix': (c_int,
                               LPPixaComp,  # PIXAC * pixac
                               c_int,  # l_int32 index
                               LPPix,  # PIX * pix
                               c_int,  # l_int32 comptype
                               ),
        'pixacompReplacePixcomp': (c_int,
                                   LPPixaComp,  # PIXAC * pixac
                                   c_int,  # l_int32 index
                                   LPPixComp,  # PIXC * pixc
                                   ),
        'pixacompAddBox': (c_int,
                           LPPixaComp,  # PIXAC * pixac
                           LPBox,  # BOX * box
                           c_int,  # l_int32 copyflag
                           ),
        'pixacompGetCount': (c_int,
                             LPPixaComp,  # PIXAC * pixac
                             ),
        'pixacompGetPixcomp': (LPPixComp,  # PIXC *
                               LPPixaComp,  # PIXAC * pixac
                               c_int,  # l_int32 index
                               c_int,  # l_int32 copyflag
                               ),
        'pixacompGetPix': (LPPix,  # PIX *
                           LPPixaComp,  # PIXAC * pixac
                           c_int,  # l_int32 index
                           ),
        'pixacompGetPixDimensions': (c_int,
                                     LPPixaComp,  # PIXAC * pixac
                                     c_int,  # l_int32 index
                                     c_int_p,  # l_int32 * pw
                                     c_int_p,  # l_int32 * ph
                                     c_int_p,  # l_int32 * pd
                                     ),
        'pixacompGetBoxa': (LPBoxa,  # BOXA *
                            LPPixaComp,  # PIXAC * pixac
                            c_int,  # l_int32 accesstype
                            ),
        'pixacompGetBoxaCount': (c_int,
                                 LPPixaComp,  # PIXAC * pixac
                                 ),
        'pixacompGetBox': (LPBox,  # BOX *
                           LPPixaComp,  # PIXAC * pixac
                           c_int,  # l_int32 index
                           c_int,  # l_int32 accesstype
                           ),
        'pixacompGetBoxGeometry': (c_int,
                                   LPPixaComp,  # PIXAC * pixac
                                   c_int,  # l_int32 index
                                   c_int_p,  # l_int32 * px
                                   c_int_p,  # l_int32 * py
                                   c_int_p,  # l_int32 * pw
                                   c_int_p,  # l_int32 * ph
                                   ),
        'pixacompGetOffset': (c_int,
                              LPPixaComp,  # PIXAC * pixac
                              ),
        'pixacompSetOffset': (c_int,
                              LPPixaComp,  # PIXAC * pixac
                              c_int,  # l_int32 offset
                              ),
        'pixaCreateFromPixacomp': (LPPixa,  # PIXA *
                                   LPPixaComp,  # PIXAC * pixac
                                   c_int,  # l_int32 accesstype
                                   ),
        'pixacompJoin': (c_int,
                         LPPixaComp,  # PIXAC * pixacd
                         LPPixaComp,  # PIXAC * pixacs
                         c_int,  # l_int32 istart
                         c_int,  # l_int32 iend
                         ),
        'pixacompInterleave': (LPPixaComp,  # PIXAC *
                               LPPixaComp,  # PIXAC * pixac1
                               LPPixaComp,  # PIXAC * pixac2
                               ),
        'pixacompRead': (LPPixaComp,  # PIXAC *
                         c_char_p,  # const char * filename
                         ),
        'pixacompReadStream': (LPPixaComp,  # PIXAC *
                               LPFile,  # FILE * fp
                               ),
        'pixacompReadMem': (LPPixaComp,  # PIXAC *
                            c_ubyte_p,  # const l_uint8 * data
                            c_size_t,  # size_t size
                            ),
        'pixacompWrite': (c_int,
                          c_char_p,  # const char * filename
                          LPPixaComp,  # PIXAC * pixac
                          ),
        'pixacompWriteStream': (c_int,
                                LPFile,  # FILE * fp
                                LPPixaComp,  # PIXAC * pixac
                                ),
        'pixacompWriteMem': (c_int,
                             POINTER(c_ubyte_p),  # l_uint8 ** pdata
                             c_size_t_p,  # size_t * psize
                             LPPixaComp,  # PIXAC * pixac
                             ),
        'pixacompConvertToPdf': (c_int,
                                 LPPixaComp,  # PIXAC * pixac
                                 c_int,  # l_int32 res
                                 c_float,  # l_float32 scalefactor
                                 c_int,  # l_int32 type
                                 c_int,  # l_int32 quality
                                 c_char_p,  # const char * title
                                 c_char_p,  # const char * fileout
                                 ),
        'pixacompConvertToPdfData': (c_int,
                                     LPPixaComp,  # PIXAC * pixac
                                     c_int,  # l_int32 res
                                     c_float,  # l_float32 scalefactor
                                     c_int,  # l_int32 type
                                     c_int,  # l_int32 quality
                                     c_char_p,  # const char * title
                                     # l_uint8 ** pdata
                                     POINTER(c_ubyte_p),
                                     c_size_t_p,  # size_t * pnbytes
                                     ),
        'pixacompFastConvertToPdfData': (c_int,
                                         LPPixaComp,  # PIXAC * pixac
                                         c_char_p,  # const char * title
                                         # l_uint8 ** pdata
                                         POINTER(c_ubyte_p),
                                         # size_t * pnbytes
                                         c_size_t_p,
                                         ),
        'pixacompWriteStreamInfo': (c_int,
                                    LPFile,  # FILE * fp
                                    LPPixaComp,  # PIXAC * pixac
                                    c_char_p,  # const char * text
                                    ),
        'pixcompWriteStreamInfo': (c_int,
                                   LPFile,  # FILE * fp
                                   LPPixComp,  # PIXC * pixc
                                   c_char_p,  # const char * text
                                   ),
        'pixacompDisplayTiledAndScaled': (LPPix,  # PIX *
                                          LPPixaComp,  # PIXAC * pixac
                                          c_int,  # l_int32 outdepth
                                          c_int,  # l_int32 tilewidth
                                          c_int,  # l_int32 ncols
                                          c_int,  # l_int32 background
                                          c_int,  # l_int32 spacing
                                          c_int,  # l_int32 border
                                          ),
        'pixacompWriteFiles': (c_int,
                               LPPixaComp,  # PIXAC * pixac
                               c_char_p,  # const char * subdir
                               ),
        'pixcompWriteFile': (c_int,
                             c_char_p,  # const char * rootname
                             LPPixComp,  # PIXC * pixc
                             ),
        'pixThreshold8': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 d
                          c_int,  # l_int32 nlevels
                          c_int,  # l_int32 cmapflag
                          ),
        'pixRemoveColormapGeneral': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 type
                                     c_int,  # l_int32 ifnocmap
                                     ),
        'pixRemoveColormap': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 type
                              ),
        'pixAddGrayColormap8': (c_int,
                                LPPix,  # PIX * pixs
                                ),
        'pixAddMinimalGrayColormap8': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixs
                                       ),
        'pixConvertRGBToLuminance': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     ),
        'pixConvertRGBToGrayGeneral': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 type
                                       c_float,  # l_float32 rwt
                                       c_float,  # l_float32 gwt
                                       c_float,  # l_float32 bwt
                                       ),
        'pixConvertRGBToGray': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_float,  # l_float32 rwt
                                c_float,  # l_float32 gwt
                                c_float,  # l_float32 bwt
                                ),
        'pixConvertRGBToGrayFast': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    ),
        'pixConvertRGBToGrayMinMax': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      c_int,  # l_int32 type
                                      ),
        'pixConvertRGBToGraySatBoost': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixs
                                        c_int,  # l_int32 refval
                                        ),
        'pixConvertRGBToGrayArb': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_float,  # l_float32 rc
                                   c_float,  # l_float32 gc
                                   c_float,  # l_float32 bc
                                   ),
        'pixConvertRGBToBinaryArb': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_float,  # l_float32 rc
                                     c_float,  # l_float32 gc
                                     c_float,  # l_float32 bc
                                     c_int,  # l_int32 thresh
                                     c_int,  # l_int32 relation
                                     ),
        'pixConvertGrayToColormap': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     ),
        'pixConvertGrayToColormap8': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      c_int,  # l_int32 mindepth
                                      ),
        'pixColorizeGray': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_uint,  # l_uint32 color
                            c_int,  # l_int32 cmapflag
                            ),
        'pixConvertRGBToColormap': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 ditherflag
                                    ),
        'pixConvertCmapTo1': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              ),
        'pixQuantizeIfFewColors': (c_int,
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 maxcolors
                                   c_int,  # l_int32 mingraycolors
                                   c_int,  # l_int32 octlevel
                                   LPLPPix,  # PIX ** ppixd
                                   ),
        'pixConvert16To8': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 type
                            ),
        'pixConvertGrayToFalseColor': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixs
                                       c_float,  # l_float32 gamma
                                       ),
        'pixUnpackBinary': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 depth
                            c_int,  # l_int32 invert
                            ),
        'pixConvert1To16': (LPPix,  # PIX *
                            LPPix,  # PIX * pixd
                            LPPix,  # PIX * pixs
                            c_ushort,  # l_uint16 val0
                            c_ushort,  # l_uint16 val1
                            ),
        'pixConvert1To32': (LPPix,  # PIX *
                            LPPix,  # PIX * pixd
                            LPPix,  # PIX * pixs
                            c_uint,  # l_uint32 val0
                            c_uint,  # l_uint32 val1
                            ),
        'pixConvert1To2Cmap': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               ),
        'pixConvert1To2': (LPPix,  # PIX *
                           LPPix,  # PIX * pixd
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 val0
                           c_int,  # l_int32 val1
                           ),
        'pixConvert1To4Cmap': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               ),
        'pixConvert1To4': (LPPix,  # PIX *
                           LPPix,  # PIX * pixd
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 val0
                           c_int,  # l_int32 val1
                           ),
        'pixConvert1To8Cmap': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               ),
        'pixConvert1To8': (LPPix,  # PIX *
                           LPPix,  # PIX * pixd
                           LPPix,  # PIX * pixs
                           c_ubyte,  # l_uint8 val0
                           c_ubyte,  # l_uint8 val1
                           ),
        'pixConvert2To8': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_ubyte,  # l_uint8 val0
                           c_ubyte,  # l_uint8 val1
                           c_ubyte,  # l_uint8 val2
                           c_ubyte,  # l_uint8 val3
                           c_int,  # l_int32 cmapflag
                           ),
        'pixConvert4To8': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 cmapflag
                           ),
        'pixConvert8To16': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 leftshift
                            ),
        'pixConvertTo2': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          ),
        'pixConvert8To2': (LPPix,  # PIX *
                           LPPix,  # PIX * pix
                           ),
        'pixConvertTo4': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          ),
        'pixConvert8To4': (LPPix,  # PIX *
                           LPPix,  # PIX * pix
                           ),
        'pixConvertTo1Adaptive': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  ),
        'pixConvertTo1': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 threshold
                          ),
        'pixConvertTo1BySampling': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 factor
                                    c_int,  # l_int32 threshold
                                    ),
        'pixConvertTo8': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 cmapflag
                          ),
        'pixConvertTo8BySampling': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 factor
                                    c_int,  # l_int32 cmapflag
                                    ),
        'pixConvertTo8Colormap': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 dither
                                  ),
        'pixConvertTo16': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           ),
        'pixConvertTo32': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           ),
        'pixConvertTo32BySampling': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 factor
                                     ),
        'pixConvert8To32': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            ),
        'pixConvertTo8Or32': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 copyflag
                              c_int,  # l_int32 warnflag
                              ),
        'pixConvert24To32': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             ),
        'pixConvert32To24': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             ),
        'pixConvert32To16': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 type
                             ),
        'pixConvert32To8': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 type16
                            c_int,  # l_int32 type8
                            ),
        'pixRemoveAlpha': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           ),
        'pixAddAlphaTo1bpp': (LPPix,  # PIX *
                              LPPix,  # PIX * pixd
                              LPPix,  # PIX * pixs
                              ),
        'pixConvertLossless': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 d
                               ),
        'pixConvertForPSWrap': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                ),
        'pixConvertToSubpixelRGB': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_float,  # l_float32 scalex
                                    c_float,  # l_float32 scaley
                                    c_int,  # l_int32 order
                                    ),
        'pixConvertGrayToSubpixelRGB': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixs
                                        c_float,  # l_float32 scalex
                                        c_float,  # l_float32 scaley
                                        c_int,  # l_int32 order
                                        ),
        'pixConvertColorToSubpixelRGB': (LPPix,  # PIX *
                                         LPPix,  # PIX * pixs
                                         c_float,  # l_float32 scalex
                                         c_float,  # l_float32 scaley
                                         c_int,  # l_int32 order
                                         ),
        'l_setNeutralBoostVal': (None,
                                 c_int,  # l_int32 val
                                 ),
        'pixConnCompTransform': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 connect
                                 c_int,  # l_int32 depth
                                 ),
        'pixConnCompAreaTransform': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 connect
                                     ),
        'pixConnCompIncrInit': (c_int,
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 conn
                                LPLPPix,  # PIX ** ppixd
                                LPLPPtaa,  # PTAA ** pptaa
                                c_int_p,  # l_int32 * pncc
                                ),
        'pixConnCompIncrAdd': (c_int,
                               LPPix,  # PIX * pixs
                               LPPtaa,  # PTAA * ptaa
                               c_int_p,  # l_int32 * pncc
                               c_float,  # l_float32 x
                               c_float,  # l_float32 y
                               c_int,  # l_int32 debug
                               ),
        'pixGetSortedNeighborValues': (c_int,
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 x
                                       c_int,  # l_int32 y
                                       c_int,  # l_int32 conn
                                       # l_int32 ** pneigh
                                       POINTER(c_int_p),
                                       c_int_p,  # l_int32 * pnvals
                                       ),
        'pixLocToColorTransform': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   ),
        'pixTilingCreate': (LPPixTiling,  # PIXTILING *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 nx
                            c_int,  # l_int32 ny
                            c_int,  # l_int32 w
                            c_int,  # l_int32 h
                            c_int,  # l_int32 xoverlap
                            c_int,  # l_int32 yoverlap
                            ),
        'pixTilingDestroy': (None,
                             LPLPPixTiling,  # PIXTILING ** ppt
                             ),
        'pixTilingGetCount': (c_int,
                              LPPixTiling,  # PIXTILING * pt
                              c_int_p,  # l_int32 * pnx
                              c_int_p,  # l_int32 * pny
                              ),
        'pixTilingGetSize': (c_int,
                             LPPixTiling,  # PIXTILING * pt
                             c_int_p,  # l_int32 * pw
                             c_int_p,  # l_int32 * ph
                             ),
        'pixTilingGetTile': (LPPix,  # PIX *
                             LPPixTiling,  # PIXTILING * pt
                             c_int,  # l_int32 i
                             c_int,  # l_int32 j
                             ),
        'pixTilingNoStripOnPaint': (c_int,
                                    LPPixTiling,  # PIXTILING * pt
                                    ),
        'pixTilingPaintTile': (c_int,
                               LPPix,  # PIX * pixd
                               c_int,  # l_int32 i
                               c_int,  # l_int32 j
                               LPPix,  # PIX * pixs
                               LPPixTiling,  # PIXTILING * pt
                               ),
        'pixReadStreamPng': (LPPix,  # PIX *
                             LPFile,  # FILE * fp
                             ),
        'readHeaderPng': (c_int,
                          c_char_p,  # const char * filename
                          c_int_p,  # l_int32 * pw
                          c_int_p,  # l_int32 * ph
                          c_int_p,  # l_int32 * pbps
                          c_int_p,  # l_int32 * pspp
                          c_int_p,  # l_int32 * piscmap
                          ),
        'freadHeaderPng': (c_int,
                           LPFile,  # FILE * fp
                           c_int_p,  # l_int32 * pw
                           c_int_p,  # l_int32 * ph
                           c_int_p,  # l_int32 * pbps
                           c_int_p,  # l_int32 * pspp
                           c_int_p,  # l_int32 * piscmap
                           ),
        'readHeaderMemPng': (c_int,
                             c_ubyte_p,  # const l_uint8 * data
                             c_size_t,  # size_t size
                             c_int_p,  # l_int32 * pw
                             c_int_p,  # l_int32 * ph
                             c_int_p,  # l_int32 * pbps
                             c_int_p,  # l_int32 * pspp
                             c_int_p,  # l_int32 * piscmap
                             ),
        'fgetPngResolution': (c_int,
                              LPFile,  # FILE * fp
                              c_int_p,  # l_int32 * pxres
                              c_int_p,  # l_int32 * pyres
                              ),
        'isPngInterlaced': (c_int,
                            c_char_p,  # const char * filename
                            c_int_p,  # l_int32 * pinterlaced
                            ),
        'fgetPngColormapInfo': (c_int,
                                LPFile,  # FILE * fp
                                LPLPPixColormap,  # PIXCMAP ** pcmap
                                c_int_p,  # l_int32 * ptransparency
                                ),
        'pixWritePng': (c_int,
                        c_char_p,  # const char * filename
                        LPPix,  # PIX * pix
                        c_float,  # l_float32 gamma
                        ),
        'pixWriteStreamPng': (c_int,
                              LPFile,  # FILE * fp
                              LPPix,  # PIX * pix
                              c_float,  # l_float32 gamma
                              ),
        'pixSetZlibCompression': (c_int,
                                  LPPix,  # PIX * pix
                                  c_int,  # l_int32 compval
                                  ),
        'l_pngSetReadStrip16To8': (None,
                                   c_int,  # l_int32 flag
                                   ),
        'pixReadMemPng': (LPPix,  # PIX *
                          c_ubyte_p,  # const l_uint8 * filedata
                          c_size_t,  # size_t filesize
                          ),
        'pixWriteMemPng': (c_int,
                           POINTER(c_ubyte_p),  # l_uint8 ** pfiledata
                           c_size_t_p,  # size_t * pfilesize
                           LPPix,  # PIX * pix
                           c_float,  # l_float32 gamma
                           ),
        'pixReadStreamPnm': (LPPix,  # PIX *
                             LPFile,  # FILE * fp
                             ),
        'readHeaderPnm': (c_int,
                          c_char_p,  # const char * filename
                          c_int_p,  # l_int32 * pw
                          c_int_p,  # l_int32 * ph
                          c_int_p,  # l_int32 * pd
                          c_int_p,  # l_int32 * ptype
                          c_int_p,  # l_int32 * pbps
                          c_int_p,  # l_int32 * pspp
                          ),
        'freadHeaderPnm': (c_int,
                           LPFile,  # FILE * fp
                           c_int_p,  # l_int32 * pw
                           c_int_p,  # l_int32 * ph
                           c_int_p,  # l_int32 * pd
                           c_int_p,  # l_int32 * ptype
                           c_int_p,  # l_int32 * pbps
                           c_int_p,  # l_int32 * pspp
                           ),
        'pixWriteStreamPnm': (c_int,
                              LPFile,  # FILE * fp
                              LPPix,  # PIX * pix
                              ),
        'pixWriteStreamAsciiPnm': (c_int,
                                   LPFile,  # FILE * fp
                                   LPPix,  # PIX * pix
                                   ),
        'pixWriteStreamPam': (c_int,
                              LPFile,  # FILE * fp
                              LPPix,  # PIX * pix
                              ),
        'pixReadMemPnm': (LPPix,  # PIX *
                          c_ubyte_p,  # const l_uint8 * data
                          c_size_t,  # size_t size
                          ),
        'readHeaderMemPnm': (c_int,
                             c_ubyte_p,  # const l_uint8 * data
                             c_size_t,  # size_t size
                             c_int_p,  # l_int32 * pw
                             c_int_p,  # l_int32 * ph
                             c_int_p,  # l_int32 * pd
                             c_int_p,  # l_int32 * ptype
                             c_int_p,  # l_int32 * pbps
                             c_int_p,  # l_int32 * pspp
                             ),
        'pixWriteMemPnm': (c_int,
                           POINTER(c_ubyte_p),  # l_uint8 ** pdata
                           c_size_t_p,  # size_t * psize
                           LPPix,  # PIX * pix
                           ),
        'pixWriteMemPam': (c_int,
                           POINTER(c_ubyte_p),  # l_uint8 ** pdata
                           c_size_t_p,  # size_t * psize
                           LPPix,  # PIX * pix
                           ),
        'pixProjectiveSampledPta': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    LPPta,  # PTA * ptad
                                    LPPta,  # PTA * ptas
                                    c_int,  # l_int32 incolor
                                    ),
        'pixProjectiveSampled': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_float_p,  # l_float32 * vc
                                 c_int,  # l_int32 incolor
                                 ),
        'pixProjectivePta': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             LPPta,  # PTA * ptad
                             LPPta,  # PTA * ptas
                             c_int,  # l_int32 incolor
                             ),
        'pixProjective': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_float_p,  # l_float32 * vc
                          c_int,  # l_int32 incolor
                          ),
        'pixProjectivePtaColor': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  LPPta,  # PTA * ptad
                                  LPPta,  # PTA * ptas
                                  c_uint,  # l_uint32 colorval
                                  ),
        'pixProjectiveColor': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_float_p,  # l_float32 * vc
                               c_uint,  # l_uint32 colorval
                               ),
        'pixProjectivePtaGray': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 LPPta,  # PTA * ptad
                                 LPPta,  # PTA * ptas
                                 c_ubyte,  # l_uint8 grayval
                                 ),
        'pixProjectiveGray': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_float_p,  # l_float32 * vc
                              c_ubyte,  # l_uint8 grayval
                              ),
        'pixProjectivePtaWithAlpha': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      LPPta,  # PTA * ptad
                                      LPPta,  # PTA * ptas
                                      LPPix,  # PIX * pixg
                                      c_float,  # l_float32 fract
                                      c_int,  # l_int32 border
                                      ),
        'getProjectiveXformCoeffs': (c_int,
                                     LPPta,  # PTA * ptas
                                     LPPta,  # PTA * ptad
                                     # l_float32 ** pvc
                                     POINTER(c_float_p),
                                     ),
        'projectiveXformSampledPt': (c_int,
                                     c_float_p,  # l_float32 * vc
                                     c_int,  # l_int32 x
                                     c_int,  # l_int32 y
                                     c_int_p,  # l_int32 * pxp
                                     c_int_p,  # l_int32 * pyp
                                     ),
        'projectiveXformPt': (c_int,
                              c_float_p,  # l_float32 * vc
                              c_int,  # l_int32 x
                              c_int,  # l_int32 y
                              c_float_p,  # l_float32 * pxp
                              c_float_p,  # l_float32 * pyp
                              ),
        'convertFilesToPS': (c_int,
                             c_char_p,  # const char * dirin
                             c_char_p,  # const char * substr
                             c_int,  # l_int32 res
                             c_char_p,  # const char * fileout
                             ),
        'sarrayConvertFilesToPS': (c_int,
                                   LPSarray,  # SARRAY * sa
                                   c_int,  # l_int32 res
                                   c_char_p,  # const char * fileout
                                   ),
        'convertFilesFittedToPS': (c_int,
                                   c_char_p,  # const char * dirin
                                   c_char_p,  # const char * substr
                                   c_float,  # l_float32 xpts
                                   c_float,  # l_float32 ypts
                                   c_char_p,  # const char * fileout
                                   ),
        'sarrayConvertFilesFittedToPS': (c_int,
                                         LPSarray,  # SARRAY * sa
                                         c_float,  # l_float32 xpts
                                         c_float,  # l_float32 ypts
                                         c_char_p,  # const char * fileout
                                         ),
        'writeImageCompressedToPSFile': (c_int,
                                         c_char_p,  # const char * filein
                                         c_char_p,  # const char * fileout
                                         c_int,  # l_int32 res
                                         c_int_p,  # l_int32 * pindex
                                         ),
        'convertSegmentedPagesToPS': (c_int,
                                      c_char_p,  # const char * pagedir
                                      c_char_p,  # const char * pagestr
                                      c_int,  # l_int32 page_numpre
                                      c_char_p,  # const char * maskdir
                                      c_char_p,  # const char * maskstr
                                      c_int,  # l_int32 mask_numpre
                                      c_int,  # l_int32 numpost
                                      c_int,  # l_int32 maxnum
                                      c_float,  # l_float32 textscale
                                      c_float,  # l_float32 imagescale
                                      c_int,  # l_int32 threshold
                                      c_char_p,  # const char * fileout
                                      ),
        'pixWriteSegmentedPageToPS': (c_int,
                                      LPPix,  # PIX * pixs
                                      LPPix,  # PIX * pixm
                                      c_float,  # l_float32 textscale
                                      c_float,  # l_float32 imagescale
                                      c_int,  # l_int32 threshold
                                      c_int,  # l_int32 pageno
                                      c_char_p,  # const char * fileout
                                      ),
        'pixWriteMixedToPS': (c_int,
                              LPPix,  # PIX * pixb
                              LPPix,  # PIX * pixc
                              c_float,  # l_float32 scale
                              c_int,  # l_int32 pageno
                              c_char_p,  # const char * fileout
                              ),
        'convertToPSEmbed': (c_int,
                             c_char_p,  # const char * filein
                             c_char_p,  # const char * fileout
                             c_int,  # l_int32 level
                             ),
        'pixaWriteCompressedToPS': (c_int,
                                    LPPixa,  # PIXA * pixa
                                    c_char_p,  # const char * fileout
                                    c_int,  # l_int32 res
                                    c_int,  # l_int32 level
                                    ),
        'pixWriteCompressedToPS': (c_int,
                                   LPPix,  # PIX * pix
                                   c_char_p,  # const char * fileout
                                   c_int,  # l_int32 res
                                   c_int,  # l_int32 level
                                   c_int_p,  # l_int32 * pindex
                                   ),
        'pixWritePSEmbed': (c_int,
                            c_char_p,  # const char * filein
                            c_char_p,  # const char * fileout
                            ),
        'pixWriteStreamPS': (c_int,
                             LPFile,  # FILE * fp
                             LPPix,  # PIX * pix
                             LPBox,  # BOX * box
                             c_int,  # l_int32 res
                             c_float,  # l_float32 scale
                             ),
        'pixWriteStringPS': (c_char_p,
                             LPPix,  # PIX * pixs
                             LPBox,  # BOX * box
                             c_int,  # l_int32 res
                             c_float,  # l_float32 scale
                             ),
        'generateUncompressedPS': (c_char_p,
                                   c_char_p,  # char * hexdata
                                   c_int,  # l_int32 w
                                   c_int,  # l_int32 h
                                   c_int,  # l_int32 d
                                   c_int,  # l_int32 psbpl
                                   c_int,  # l_int32 bps
                                   c_float,  # l_float32 xpt
                                   c_float,  # l_float32 ypt
                                   c_float,  # l_float32 wpt
                                   c_float,  # l_float32 hpt
                                   c_int,  # l_int32 boxflag
                                   ),
        'convertJpegToPSEmbed': (c_int,
                                 c_char_p,  # const char * filein
                                 c_char_p,  # const char * fileout
                                 ),
        'convertJpegToPS': (c_int,
                            c_char_p,  # const char * filein
                            c_char_p,  # const char * fileout
                            c_char_p,  # const char * operation
                            c_int,  # l_int32 x
                            c_int,  # l_int32 y
                            c_int,  # l_int32 res
                            c_float,  # l_float32 scale
                            c_int,  # l_int32 pageno
                            c_int,  # l_int32 endpage
                            ),
        'convertG4ToPSEmbed': (c_int,
                               c_char_p,  # const char * filein
                               c_char_p,  # const char * fileout
                               ),
        'convertG4ToPS': (c_int,
                          c_char_p,  # const char * filein
                          c_char_p,  # const char * fileout
                          c_char_p,  # const char * operation
                          c_int,  # l_int32 x
                          c_int,  # l_int32 y
                          c_int,  # l_int32 res
                          c_float,  # l_float32 scale
                          c_int,  # l_int32 pageno
                          c_int,  # l_int32 maskflag
                          c_int,  # l_int32 endpage
                          ),
        'convertTiffMultipageToPS': (c_int,
                                     c_char_p,  # const char * filein
                                     c_char_p,  # const char * fileout
                                     c_float,  # l_float32 fillfract
                                     ),
        'convertFlateToPSEmbed': (c_int,
                                  c_char_p,  # const char * filein
                                  c_char_p,  # const char * fileout
                                  ),
        'convertFlateToPS': (c_int,
                             c_char_p,  # const char * filein
                             c_char_p,  # const char * fileout
                             c_char_p,  # const char * operation
                             c_int,  # l_int32 x
                             c_int,  # l_int32 y
                             c_int,  # l_int32 res
                             c_float,  # l_float32 scale
                             c_int,  # l_int32 pageno
                             c_int,  # l_int32 endpage
                             ),
        'pixWriteMemPS': (c_int,
                          POINTER(c_ubyte_p),  # l_uint8 ** pdata
                          c_size_t_p,  # size_t * psize
                          LPPix,  # PIX * pix
                          LPBox,  # BOX * box
                          c_int,  # l_int32 res
                          c_float,  # l_float32 scale
                          ),
        'getResLetterPage': (c_int,
                             c_int,  # l_int32 w
                             c_int,  # l_int32 h
                             c_float,  # l_float32 fillfract
                             ),
        'getResA4Page': (c_int,
                         c_int,  # l_int32 w
                         c_int,  # l_int32 h
                         c_float,  # l_float32 fillfract
                         ),
        'l_psWriteBoundingBox': (None,
                                 c_int,  # l_int32 flag
                                 ),
        'ptaCreate': (LPPta,  # PTA *
                      c_int,  # l_int32 n
                      ),
        'ptaCreateFromNuma': (LPPta,  # PTA *
                              LPNuma,  # NUMA * nax
                              LPNuma,  # NUMA * nay
                              ),
        'ptaDestroy': (None,
                       LPLPPta,  # PTA ** ppta
                       ),
        'ptaCopy': (LPPta,  # PTA *
                    LPPta,  # PTA * pta
                    ),
        'ptaCopyRange': (LPPta,  # PTA *
                         LPPta,  # PTA * ptas
                         c_int,  # l_int32 istart
                         c_int,  # l_int32 iend
                         ),
        'ptaClone': (LPPta,  # PTA *
                     LPPta,  # PTA * pta
                     ),
        'ptaEmpty': (c_int,
                     LPPta,  # PTA * pta
                     ),
        'ptaAddPt': (c_int,
                     LPPta,  # PTA * pta
                     c_float,  # l_float32 x
                     c_float,  # l_float32 y
                     ),
        'ptaInsertPt': (c_int,
                        LPPta,  # PTA * pta
                        c_int,  # l_int32 index
                        c_int,  # l_int32 x
                        c_int,  # l_int32 y
                        ),
        'ptaRemovePt': (c_int,
                        LPPta,  # PTA * pta
                        c_int,  # l_int32 index
                        ),
        'ptaGetRefcount': (c_int,
                           LPPta,  # PTA * pta
                           ),
        'ptaChangeRefcount': (c_int,
                              LPPta,  # PTA * pta
                              c_int,  # l_int32 delta
                              ),
        'ptaGetCount': (c_int,
                        LPPta,  # PTA * pta
                        ),
        'ptaGetPt': (c_int,
                     LPPta,  # PTA * pta
                     c_int,  # l_int32 index
                     c_float_p,  # l_float32 * px
                     c_float_p,  # l_float32 * py
                     ),
        'ptaGetIPt': (c_int,
                      LPPta,  # PTA * pta
                      c_int,  # l_int32 index
                      c_int_p,  # l_int32 * px
                      c_int_p,  # l_int32 * py
                      ),
        'ptaSetPt': (c_int,
                     LPPta,  # PTA * pta
                     c_int,  # l_int32 index
                     c_float,  # l_float32 x
                     c_float,  # l_float32 y
                     ),
        'ptaGetArrays': (c_int,
                         LPPta,  # PTA * pta
                         LPLPNuma,  # NUMA ** pnax
                         LPLPNuma,  # NUMA ** pnay
                         ),
        'ptaRead': (LPPta,  # PTA *
                    c_char_p,  # const char * filename
                    ),
        'ptaReadStream': (LPPta,  # PTA *
                          LPFile,  # FILE * fp
                          ),
        'ptaReadMem': (LPPta,  # PTA *
                       c_ubyte_p,  # const l_uint8 * data
                       c_size_t,  # size_t size
                       ),
        'ptaWriteDebug': (c_int,
                          c_char_p,  # const char * filename
                          LPPta,  # PTA * pta
                          c_int,  # l_int32 type
                          ),
        'ptaWrite': (c_int,
                     c_char_p,  # const char * filename
                     LPPta,  # PTA * pta
                     c_int,  # l_int32 type
                     ),
        'ptaWriteStream': (c_int,
                           LPFile,  # FILE * fp
                           LPPta,  # PTA * pta
                           c_int,  # l_int32 type
                           ),
        'ptaWriteMem': (c_int,
                        POINTER(c_ubyte_p),  # l_uint8 ** pdata
                        c_size_t_p,  # size_t * psize
                        LPPta,  # PTA * pta
                        c_int,  # l_int32 type
                        ),
        'ptaaCreate': (LPPtaa,  # PTAA *
                       c_int,  # l_int32 n
                       ),
        'ptaaDestroy': (None,
                        LPLPPtaa,  # PTAA ** pptaa
                        ),
        'ptaaAddPta': (c_int,
                       LPPtaa,  # PTAA * ptaa
                       LPPta,  # PTA * pta
                       c_int,  # l_int32 copyflag
                       ),
        'ptaaGetCount': (c_int,
                         LPPtaa,  # PTAA * ptaa
                         ),
        'ptaaGetPta': (LPPta,  # PTA *
                       LPPtaa,  # PTAA * ptaa
                       c_int,  # l_int32 index
                       c_int,  # l_int32 accessflag
                       ),
        'ptaaGetPt': (c_int,
                      LPPtaa,  # PTAA * ptaa
                      c_int,  # l_int32 ipta
                      c_int,  # l_int32 jpt
                      c_float_p,  # l_float32 * px
                      c_float_p,  # l_float32 * py
                      ),
        'ptaaInitFull': (c_int,
                         LPPtaa,  # PTAA * ptaa
                         LPPta,  # PTA * pta
                         ),
        'ptaaReplacePta': (c_int,
                           LPPtaa,  # PTAA * ptaa
                           c_int,  # l_int32 index
                           LPPta,  # PTA * pta
                           ),
        'ptaaAddPt': (c_int,
                      LPPtaa,  # PTAA * ptaa
                      c_int,  # l_int32 ipta
                      c_float,  # l_float32 x
                      c_float,  # l_float32 y
                      ),
        'ptaaTruncate': (c_int,
                         LPPtaa,  # PTAA * ptaa
                         ),
        'ptaaRead': (LPPtaa,  # PTAA *
                     c_char_p,  # const char * filename
                     ),
        'ptaaReadStream': (LPPtaa,  # PTAA *
                           LPFile,  # FILE * fp
                           ),
        'ptaaReadMem': (LPPtaa,  # PTAA *
                        c_ubyte_p,  # const l_uint8 * data
                        c_size_t,  # size_t size
                        ),
        'ptaaWriteDebug': (c_int,
                           c_char_p,  # const char * filename
                           LPPtaa,  # PTAA * ptaa
                           c_int,  # l_int32 type
                           ),
        'ptaaWrite': (c_int,
                      c_char_p,  # const char * filename
                      LPPtaa,  # PTAA * ptaa
                      c_int,  # l_int32 type
                      ),
        'ptaaWriteStream': (c_int,
                            LPFile,  # FILE * fp
                            LPPtaa,  # PTAA * ptaa
                            c_int,  # l_int32 type
                            ),
        'ptaaWriteMem': (c_int,
                         POINTER(c_ubyte_p),  # l_uint8 ** pdata
                         c_size_t_p,  # size_t * psize
                         LPPtaa,  # PTAA * ptaa
                         c_int,  # l_int32 type
                         ),
        'ptaSubsample': (LPPta,  # PTA *
                         LPPta,  # PTA * ptas
                         c_int,  # l_int32 subfactor
                         ),
        'ptaJoin': (c_int,
                    LPPta,  # PTA * ptad
                    LPPta,  # PTA * ptas
                    c_int,  # l_int32 istart
                    c_int,  # l_int32 iend
                    ),
        'ptaaJoin': (c_int,
                     LPPtaa,  # PTAA * ptaad
                     LPPtaa,  # PTAA * ptaas
                     c_int,  # l_int32 istart
                     c_int,  # l_int32 iend
                     ),
        'ptaReverse': (LPPta,  # PTA *
                       LPPta,  # PTA * ptas
                       c_int,  # l_int32 type
                       ),
        'ptaTranspose': (LPPta,  # PTA *
                         LPPta,  # PTA * ptas
                         ),
        'ptaCyclicPerm': (LPPta,  # PTA *
                          LPPta,  # PTA * ptas
                          c_int,  # l_int32 xs
                          c_int,  # l_int32 ys
                          ),
        'ptaSelectRange': (LPPta,  # PTA *
                           LPPta,  # PTA * ptas
                           c_int,  # l_int32 first
                           c_int,  # l_int32 last
                           ),
        'ptaGetBoundingRegion': (LPBox,  # BOX *
                                 LPPta,  # PTA * pta
                                 ),
        'ptaGetRange': (c_int,
                        LPPta,  # PTA * pta
                        c_float_p,  # l_float32 * pminx
                        c_float_p,  # l_float32 * pmaxx
                        c_float_p,  # l_float32 * pminy
                        c_float_p,  # l_float32 * pmaxy
                        ),
        'ptaGetInsideBox': (LPPta,  # PTA *
                            LPPta,  # PTA * ptas
                            LPBox,  # BOX * box
                            ),
        'pixFindCornerPixels': (LPPta,  # PTA *
                                LPPix,  # PIX * pixs
                                ),
        'ptaContainsPt': (c_int,
                          LPPta,  # PTA * pta
                          c_int,  # l_int32 x
                          c_int,  # l_int32 y
                          ),
        'ptaTestIntersection': (c_int,
                                LPPta,  # PTA * pta1
                                LPPta,  # PTA * pta2
                                ),
        'ptaTransform': (LPPta,  # PTA *
                         LPPta,  # PTA * ptas
                         c_int,  # l_int32 shiftx
                         c_int,  # l_int32 shifty
                         c_float,  # l_float32 scalex
                         c_float,  # l_float32 scaley
                         ),
        'ptaPtInsidePolygon': (c_int,
                               LPPta,  # PTA * pta
                               c_float,  # l_float32 x
                               c_float,  # l_float32 y
                               c_int_p,  # l_int32 * pinside
                               ),
        'l_angleBetweenVectors': (c_float,
                                  c_float,  # l_float32 x1
                                  c_float,  # l_float32 y1
                                  c_float,  # l_float32 x2
                                  c_float,  # l_float32 y2
                                  ),
        'ptaPolygonIsConvex': (c_int,
                               LPPta,  # PTA * pta
                               c_int_p,  # l_int32 * pisconvex
                               ),
        'ptaGetMinMax': (c_int,
                         LPPta,  # PTA * pta
                         c_float_p,  # l_float32 * pxmin
                         c_float_p,  # l_float32 * pymin
                         c_float_p,  # l_float32 * pxmax
                         c_float_p,  # l_float32 * pymax
                         ),
        'ptaSelectByValue': (LPPta,  # PTA *
                             LPPta,  # PTA * ptas
                             c_float,  # l_float32 xth
                             c_float,  # l_float32 yth
                             c_int,  # l_int32 type
                             c_int,  # l_int32 relation
                             ),
        'ptaCropToMask': (LPPta,  # PTA *
                          LPPta,  # PTA * ptas
                          LPPix,  # PIX * pixm
                          ),
        'ptaGetLinearLSF': (c_int,
                            LPPta,  # PTA * pta
                            c_float_p,  # l_float32 * pa
                            c_float_p,  # l_float32 * pb
                            LPLPNuma,  # NUMA ** pnafit
                            ),
        'ptaGetQuadraticLSF': (c_int,
                               LPPta,  # PTA * pta
                               c_float_p,  # l_float32 * pa
                               c_float_p,  # l_float32 * pb
                               c_float_p,  # l_float32 * pc
                               LPLPNuma,  # NUMA ** pnafit
                               ),
        'ptaGetCubicLSF': (c_int,
                           LPPta,  # PTA * pta
                           c_float_p,  # l_float32 * pa
                           c_float_p,  # l_float32 * pb
                           c_float_p,  # l_float32 * pc
                           c_float_p,  # l_float32 * pd
                           LPLPNuma,  # NUMA ** pnafit
                           ),
        'ptaGetQuarticLSF': (c_int,
                             LPPta,  # PTA * pta
                             c_float_p,  # l_float32 * pa
                             c_float_p,  # l_float32 * pb
                             c_float_p,  # l_float32 * pc
                             c_float_p,  # l_float32 * pd
                             c_float_p,  # l_float32 * pe
                             LPLPNuma,  # NUMA ** pnafit
                             ),
        'ptaNoisyLinearLSF': (c_int,
                              LPPta,  # PTA * pta
                              c_float,  # l_float32 factor
                              LPLPPta,  # PTA ** pptad
                              c_float_p,  # l_float32 * pa
                              c_float_p,  # l_float32 * pb
                              c_float_p,  # l_float32 * pmederr
                              LPLPNuma,  # NUMA ** pnafit
                              ),
        'ptaNoisyQuadraticLSF': (c_int,
                                 LPPta,  # PTA * pta
                                 c_float,  # l_float32 factor
                                 LPLPPta,  # PTA ** pptad
                                 c_float_p,  # l_float32 * pa
                                 c_float_p,  # l_float32 * pb
                                 c_float_p,  # l_float32 * pc
                                 c_float_p,  # l_float32 * pmederr
                                 LPLPNuma,  # NUMA ** pnafit
                                 ),
        'applyLinearFit': (c_int,
                           c_float,  # l_float32 a
                           c_float,  # l_float32 b
                           c_float,  # l_float32 x
                           c_float_p,  # l_float32 * py
                           ),
        'applyQuadraticFit': (c_int,
                              c_float,  # l_float32 a
                              c_float,  # l_float32 b
                              c_float,  # l_float32 c
                              c_float,  # l_float32 x
                              c_float_p,  # l_float32 * py
                              ),
        'applyCubicFit': (c_int,
                          c_float,  # l_float32 a
                          c_float,  # l_float32 b
                          c_float,  # l_float32 c
                          c_float,  # l_float32 d
                          c_float,  # l_float32 x
                          c_float_p,  # l_float32 * py
                          ),
        'applyQuarticFit': (c_int,
                            c_float,  # l_float32 a
                            c_float,  # l_float32 b
                            c_float,  # l_float32 c
                            c_float,  # l_float32 d
                            c_float,  # l_float32 e
                            c_float,  # l_float32 x
                            c_float_p,  # l_float32 * py
                            ),
        'pixPlotAlongPta': (c_int,
                            LPPix,  # PIX * pixs
                            LPPta,  # PTA * pta
                            c_int,  # l_int32 outformat
                            c_char_p,  # const char * title
                            ),
        'ptaGetPixelsFromPix': (LPPta,  # PTA *
                                LPPix,  # PIX * pixs
                                LPBox,  # BOX * box
                                ),
        'pixGenerateFromPta': (LPPix,  # PIX *
                               LPPta,  # PTA * pta
                               c_int,  # l_int32 w
                               c_int,  # l_int32 h
                               ),
        'ptaGetBoundaryPixels': (LPPta,  # PTA *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 type
                                 ),
        'ptaaGetBoundaryPixels': (LPPtaa,  # PTAA *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 type
                                  c_int,  # l_int32 connectivity
                                  LPLPBoxa,  # BOXA ** pboxa
                                  LPLPPixa,  # PIXA ** ppixa
                                  ),
        'ptaaIndexLabeledPixels': (LPPtaa,  # PTAA *
                                   LPPix,  # PIX * pixs
                                   c_int_p,  # l_int32 * pncc
                                   ),
        'ptaGetNeighborPixLocs': (LPPta,  # PTA *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 x
                                  c_int,  # l_int32 y
                                  c_int,  # l_int32 conn
                                  ),
        'numaConvertToPta1': (LPPta,  # PTA *
                              LPNuma,  # NUMA * na
                              ),
        'numaConvertToPta2': (LPPta,  # PTA *
                              LPNuma,  # NUMA * nax
                              LPNuma,  # NUMA * nay
                              ),
        'ptaConvertToNuma': (c_int,
                             LPPta,  # PTA * pta
                             LPLPNuma,  # NUMA ** pnax
                             LPLPNuma,  # NUMA ** pnay
                             ),
        'pixDisplayPta': (LPPix,  # PIX *
                          LPPix,  # PIX * pixd
                          LPPix,  # PIX * pixs
                          LPPta,  # PTA * pta
                          ),
        'pixDisplayPtaaPattern': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixd
                                  LPPix,  # PIX * pixs
                                  LPPtaa,  # PTAA * ptaa
                                  LPPix,  # PIX * pixp
                                  c_int,  # l_int32 cx
                                  c_int,  # l_int32 cy
                                  ),
        'pixDisplayPtaPattern': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixd
                                 LPPix,  # PIX * pixs
                                 LPPta,  # PTA * pta
                                 LPPix,  # PIX * pixp
                                 c_int,  # l_int32 cx
                                 c_int,  # l_int32 cy
                                 c_uint,  # l_uint32 color
                                 ),
        'ptaReplicatePattern': (LPPta,  # PTA *
                                LPPta,  # PTA * ptas
                                LPPix,  # PIX * pixp
                                LPPta,  # PTA * ptap
                                c_int,  # l_int32 cx
                                c_int,  # l_int32 cy
                                c_int,  # l_int32 w
                                c_int,  # l_int32 h
                                ),
        'pixDisplayPtaa': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           LPPtaa,  # PTAA * ptaa
                           ),
        'ptaSort': (LPPta,  # PTA *
                    LPPta,  # PTA * ptas
                    c_int,  # l_int32 sorttype
                    c_int,  # l_int32 sortorder
                    LPLPNuma,  # NUMA ** pnaindex
                    ),
        'ptaGetSortIndex': (c_int,
                            LPPta,  # PTA * ptas
                            c_int,  # l_int32 sorttype
                            c_int,  # l_int32 sortorder
                            LPLPNuma,  # NUMA ** pnaindex
                            ),
        'ptaSortByIndex': (LPPta,  # PTA *
                           LPPta,  # PTA * ptas
                           LPNuma,  # NUMA * naindex
                           ),
        'ptaaSortByIndex': (LPPtaa,  # PTAA *
                            LPPtaa,  # PTAA * ptaas
                            LPNuma,  # NUMA * naindex
                            ),
        'ptaGetRankValue': (c_int,
                            LPPta,  # PTA * pta
                            c_float,  # l_float32 fract
                            LPPta,  # PTA * ptasort
                            c_int,  # l_int32 sorttype
                            c_float_p,  # l_float32 * pval
                            ),
        'ptaSort2d': (LPPta,  # PTA *
                      LPPta,  # PTA * pta
                      ),
        'ptaEqual': (c_int,
                     LPPta,  # PTA * pta1
                     LPPta,  # PTA * pta2
                     c_int_p,  # l_int32 * psame
                     ),
        'ptaRemoveDupsByAset': (c_int,
                                LPPta,  # PTA * ptas
                                LPLPPta,  # PTA ** pptad
                                ),
        'ptaUnionByAset': (c_int,
                           LPPta,  # PTA * pta1
                           LPPta,  # PTA * pta2
                           LPLPPta,  # PTA ** pptad
                           ),
        'ptaIntersectionByAset': (c_int,
                                  LPPta,  # PTA * pta1
                                  LPPta,  # PTA * pta2
                                  LPLPPta,  # PTA ** pptad
                                  ),
        'ptaUnionByHmap': (c_int,
                           LPPta,  # PTA * pta1
                           LPPta,  # PTA * pta2
                           LPLPPta,  # PTA ** pptad
                           ),
        'ptaIntersectionByHmap': (c_int,
                                  LPPta,  # PTA * pta1
                                  LPPta,  # PTA * pta2
                                  LPLPPta,  # PTA ** pptad
                                  ),
        'pixQuadtreeMean': (c_int,
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 nlevels
                            LPPix,  # PIX * pix_ma
                            LPLPFPixa,  # FPIXA ** pfpixa
                            ),
        'pixQuadtreeVariance': (c_int,
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 nlevels
                                LPPix,  # PIX * pix_ma
                                LPDPix,  # DPIX * dpix_msa
                                LPLPFPixa,  # FPIXA ** pfpixa_v
                                LPLPFPixa,  # FPIXA ** pfpixa_rv
                                ),
        'pixMeanInRectangle': (c_int,
                               LPPix,  # PIX * pixs
                               LPBox,  # BOX * box
                               LPPix,  # PIX * pixma
                               c_float_p,  # l_float32 * pval
                               ),
        'pixVarianceInRectangle': (c_int,
                                   LPPix,  # PIX * pixs
                                   LPBox,  # BOX * box
                                   LPPix,  # PIX * pix_ma
                                   LPDPix,  # DPIX * dpix_msa
                                   c_float_p,  # l_float32 * pvar
                                   c_float_p,  # l_float32 * prvar
                                   ),
        'boxaaQuadtreeRegions': (LPBoxaa,  # BOXAA *
                                 c_int,  # l_int32 w
                                 c_int,  # l_int32 h
                                 c_int,  # l_int32 nlevels
                                 ),
        'quadtreeGetParent': (c_int,
                              LPFPixa,  # FPIXA * fpixa
                              c_int,  # l_int32 level
                              c_int,  # l_int32 x
                              c_int,  # l_int32 y
                              c_float_p,  # l_float32 * pval
                              ),
        'quadtreeGetChildren': (c_int,
                                LPFPixa,  # FPIXA * fpixa
                                c_int,  # l_int32 level
                                c_int,  # l_int32 x
                                c_int,  # l_int32 y
                                c_float_p,  # l_float32 * pval00
                                c_float_p,  # l_float32 * pval10
                                c_float_p,  # l_float32 * pval01
                                c_float_p,  # l_float32 * pval11
                                ),
        'quadtreeMaxLevels': (c_int,
                              c_int,  # l_int32 w
                              c_int,  # l_int32 h
                              ),
        'fpixaDisplayQuadtree': (LPPix,  # PIX *
                                 LPFPixa,  # FPIXA * fpixa
                                 c_int,  # l_int32 factor
                                 c_int,  # l_int32 fontsize
                                 ),
        'pixRankFilter': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 wf
                          c_int,  # l_int32 hf
                          c_float,  # l_float32 rank
                          ),
        'pixRankFilterRGB': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 wf
                             c_int,  # l_int32 hf
                             c_float,  # l_float32 rank
                             ),
        'pixRankFilterGray': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 wf
                              c_int,  # l_int32 hf
                              c_float,  # l_float32 rank
                              ),
        'pixMedianFilter': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 wf
                            c_int,  # l_int32 hf
                            ),
        'pixRankFilterWithScaling': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 wf
                                     c_int,  # l_int32 hf
                                     c_float,  # l_float32 rank
                                     c_float,  # l_float32 scalefactor
                                     ),
        'pixProcessBarcodes': (LPSarray,  # SARRAY *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 format
                               c_int,  # l_int32 method
                               LPLPSarray,  # SARRAY ** psaw
                               c_int,  # l_int32 debugflag
                               ),
        'pixExtractBarcodes': (LPPixa,  # PIXA *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 debugflag
                               ),
        'pixReadBarcodes': (LPSarray,  # SARRAY *
                            LPPixa,  # PIXA * pixa
                            c_int,  # l_int32 format
                            c_int,  # l_int32 method
                            LPLPSarray,  # SARRAY ** psaw
                            c_int,  # l_int32 debugflag
                            ),
        'pixReadBarcodeWidths': (LPNuma,  # NUMA *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 method
                                 c_int,  # l_int32 debugflag
                                 ),
        'pixLocateBarcodes': (LPBoxa,  # BOXA *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 thresh
                              LPLPPix,  # PIX ** ppixb
                              LPLPPix,  # PIX ** ppixm
                              ),
        'pixDeskewBarcode': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             LPPix,  # PIX * pixb
                             LPBox,  # BOX * box
                             c_int,  # l_int32 margin
                             c_int,  # l_int32 threshold
                             c_float_p,  # l_float32 * pangle
                             c_float_p,  # l_float32 * pconf
                             ),
        'pixExtractBarcodeWidths1': (LPNuma,  # NUMA *
                                     LPPix,  # PIX * pixs
                                     c_float,  # l_float32 thresh
                                     c_float,  # l_float32 binfract
                                     LPLPNuma,  # NUMA ** pnaehist
                                     LPLPNuma,  # NUMA ** pnaohist
                                     c_int,  # l_int32 debugflag
                                     ),
        'pixExtractBarcodeWidths2': (LPNuma,  # NUMA *
                                     LPPix,  # PIX * pixs
                                     c_float,  # l_float32 thresh
                                     c_float_p,  # l_float32 * pwidth
                                     LPLPNuma,  # NUMA ** pnac
                                     c_int,  # l_int32 debugflag
                                     ),
        'pixExtractBarcodeCrossings': (LPNuma,  # NUMA *
                                       LPPix,  # PIX * pixs
                                       c_float,  # l_float32 thresh
                                       c_int,  # l_int32 debugflag
                                       ),
        'numaQuantizeCrossingsByWidth': (LPNuma,  # NUMA *
                                         LPNuma,  # NUMA * nas
                                         c_float,  # l_float32 binfract
                                         LPLPNuma,  # NUMA ** pnaehist
                                         LPLPNuma,  # NUMA ** pnaohist
                                         c_int,  # l_int32 debugflag
                                         ),
        'numaQuantizeCrossingsByWindow': (LPNuma,  # NUMA *
                                          LPNuma,  # NUMA * nas
                                          c_float,  # l_float32 ratio
                                          # l_float32 * pwidth
                                          c_float_p,
                                          # l_float32 * pfirstloc
                                          c_float_p,
                                          LPLPNuma,  # NUMA ** pnac
                                          c_int,  # l_int32 debugflag
                                          ),
        'pixaReadFiles': (LPPixa,  # PIXA *
                          c_char_p,  # const char * dirname
                          c_char_p,  # const char * substr
                          ),
        'pixaReadFilesSA': (LPPixa,  # PIXA *
                            LPSarray,  # SARRAY * sa
                            ),
        'pixRead': (LPPix,  # PIX *
                    c_char_p,  # const char * filename
                    ),
        'pixReadWithHint': (LPPix,  # PIX *
                            c_char_p,  # const char * filename
                            c_int,  # l_int32 hint
                            ),
        'pixReadIndexed': (LPPix,  # PIX *
                           LPSarray,  # SARRAY * sa
                           c_int,  # l_int32 index
                           ),
        'pixReadStream': (LPPix,  # PIX *
                          LPFile,  # FILE * fp
                          c_int,  # l_int32 hint
                          ),
        'pixReadHeader': (c_int,
                          c_char_p,  # const char * filename
                          c_int_p,  # l_int32 * pformat
                          c_int_p,  # l_int32 * pw
                          c_int_p,  # l_int32 * ph
                          c_int_p,  # l_int32 * pbps
                          c_int_p,  # l_int32 * pspp
                          c_int_p,  # l_int32 * piscmap
                          ),
        'findFileFormat': (c_int,
                           c_char_p,  # const char * filename
                           c_int_p,  # l_int32 * pformat
                           ),
        'findFileFormatStream': (c_int,
                                 LPFile,  # FILE * fp
                                 c_int_p,  # l_int32 * pformat
                                 ),
        'findFileFormatBuffer': (c_int,
                                 c_ubyte_p,  # const l_uint8 * buf
                                 c_int_p,  # l_int32 * pformat
                                 ),
        'fileFormatIsTiff': (c_int,
                             LPFile,  # FILE * fp
                             ),
        'pixReadMem': (LPPix,  # PIX *
                       c_ubyte_p,  # const l_uint8 * data
                       c_size_t,  # size_t size
                       ),
        'pixReadHeaderMem': (c_int,
                             c_ubyte_p,  # const l_uint8 * data
                             c_size_t,  # size_t size
                             c_int_p,  # l_int32 * pformat
                             c_int_p,  # l_int32 * pw
                             c_int_p,  # l_int32 * ph
                             c_int_p,  # l_int32 * pbps
                             c_int_p,  # l_int32 * pspp
                             c_int_p,  # l_int32 * piscmap
                             ),
        'writeImageFileInfo': (c_int,
                               c_char_p,  # const char * filename
                               LPFile,  # FILE * fpout
                               c_int,  # l_int32 headeronly
                               ),
        'ioFormatTest': (c_int,
                         c_char_p,  # const char * filename
                         ),
        'l_convertCharstrToInt': (c_int,
                                  c_char_p,  # const char * str
                                  c_int_p,  # l_int32 * pval
                                  ),
        'showExtractNumbers': (LPPixa,  # PIXA *
                               LPPix,  # PIX * pixs
                               LPSarray,  # SARRAY * sa
                               LPBoxaa,  # BOXAA * baa
                               LPNumaa,  # NUMAA * naa
                               LPLPPix,  # PIX ** ppixdb
                               ),
        'pixaAccumulateSamples': (c_int,
                                  LPPixa,  # PIXA * pixa
                                  LPPta,  # PTA * pta
                                  LPLPPix,  # PIX ** ppixd
                                  c_float_p,  # l_float32 * px
                                  c_float_p,  # l_float32 * py
                                  ),
        'recogFilterPixaBySize': (LPPixa,  # PIXA *
                                  LPPixa,  # PIXA * pixas
                                  c_int,  # l_int32 setsize
                                  c_int,  # l_int32 maxkeep
                                  c_float,  # l_float32 max_ht_ratio
                                  LPLPNuma,  # NUMA ** pna
                                  ),
        'recogSortPixaByClass': (LPPixaa,  # PIXAA *
                                 LPPixa,  # PIXA * pixa
                                 c_int,  # l_int32 setsize
                                 ),
        'pixaRemoveOutliers1': (LPPixa,  # PIXA *
                                LPPixa,  # PIXA * pixas
                                c_float,  # l_float32 minscore
                                c_int,  # l_int32 mintarget
                                c_int,  # l_int32 minsize
                                LPLPPix,  # PIX ** ppixsave
                                LPLPPix,  # PIX ** ppixrem
                                ),
        'pixaRemoveOutliers2': (LPPixa,  # PIXA *
                                LPPixa,  # PIXA * pixas
                                c_float,  # l_float32 minscore
                                c_int,  # l_int32 minsize
                                LPLPPix,  # PIX ** ppixsave
                                LPLPPix,  # PIX ** ppixrem
                                ),
        'recogMakeBootDigitTemplates': (LPPixa,  # PIXA *
                                        c_int,  # l_int32 nsamp
                                        c_int,  # l_int32 debug
                                        ),
        'pixRasterop': (c_int,
                        LPPix,  # PIX * pixd
                        c_int,  # l_int32 dx
                        c_int,  # l_int32 dy
                        c_int,  # l_int32 dw
                        c_int,  # l_int32 dh
                        c_int,  # l_int32 op
                        LPPix,  # PIX * pixs
                        c_int,  # l_int32 sx
                        c_int,  # l_int32 sy
                        ),
        'pixRasteropVip': (c_int,
                           LPPix,  # PIX * pixd
                           c_int,  # l_int32 bx
                           c_int,  # l_int32 bw
                           c_int,  # l_int32 vshift
                           c_int,  # l_int32 incolor
                           ),
        'pixRasteropHip': (c_int,
                           LPPix,  # PIX * pixd
                           c_int,  # l_int32 by
                           c_int,  # l_int32 bh
                           c_int,  # l_int32 hshift
                           c_int,  # l_int32 incolor
                           ),
        'pixTranslate': (LPPix,  # PIX *
                         LPPix,  # PIX * pixd
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 hshift
                         c_int,  # l_int32 vshift
                         c_int,  # l_int32 incolor
                         ),
        'pixRasteropIP': (c_int,
                          LPPix,  # PIX * pixd
                          c_int,  # l_int32 hshift
                          c_int,  # l_int32 vshift
                          c_int,  # l_int32 incolor
                          ),
        'pixRasteropFullImage': (c_int,
                                 LPPix,  # PIX * pixd
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 op
                                 ),
        'rasteropUniLow': (None,
                           c_uint_p,  # l_uint32 * datad
                           c_int,  # l_int32 dpixw
                           c_int,  # l_int32 dpixh
                           c_int,  # l_int32 depth
                           c_int,  # l_int32 dwpl
                           c_int,  # l_int32 dx
                           c_int,  # l_int32 dy
                           c_int,  # l_int32 dw
                           c_int,  # l_int32 dh
                           c_int,  # l_int32 op
                           ),
        'rasteropLow': (None,
                        c_uint_p,  # l_uint32 * datad
                        c_int,  # l_int32 dpixw
                        c_int,  # l_int32 dpixh
                        c_int,  # l_int32 depth
                        c_int,  # l_int32 dwpl
                        c_int,  # l_int32 dx
                        c_int,  # l_int32 dy
                        c_int,  # l_int32 dw
                        c_int,  # l_int32 dh
                        c_int,  # l_int32 op
                        c_uint_p,  # l_uint32 * datas
                        c_int,  # l_int32 spixw
                        c_int,  # l_int32 spixh
                        c_int,  # l_int32 swpl
                        c_int,  # l_int32 sx
                        c_int,  # l_int32 sy
                        ),
        'rasteropVipLow': (None,
                           c_uint_p,  # l_uint32 * data
                           c_int,  # l_int32 pixw
                           c_int,  # l_int32 pixh
                           c_int,  # l_int32 depth
                           c_int,  # l_int32 wpl
                           c_int,  # l_int32 x
                           c_int,  # l_int32 w
                           c_int,  # l_int32 shift
                           ),
        'rasteropHipLow': (None,
                           c_uint_p,  # l_uint32 * data
                           c_int,  # l_int32 pixh
                           c_int,  # l_int32 depth
                           c_int,  # l_int32 wpl
                           c_int,  # l_int32 y
                           c_int,  # l_int32 h
                           c_int,  # l_int32 shift
                           ),
        'pixRotate': (LPPix,  # PIX *
                      LPPix,  # PIX * pixs
                      c_float,  # l_float32 angle
                      c_int,  # l_int32 type
                      c_int,  # l_int32 incolor
                      c_int,  # l_int32 width
                      c_int,  # l_int32 height
                      ),
        'pixEmbedForRotation': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_float,  # l_float32 angle
                                c_int,  # l_int32 incolor
                                c_int,  # l_int32 width
                                c_int,  # l_int32 height
                                ),
        'pixRotateBySampling': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 xcen
                                c_int,  # l_int32 ycen
                                c_float,  # l_float32 angle
                                c_int,  # l_int32 incolor
                                ),
        'pixRotateBinaryNice': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_float,  # l_float32 angle
                                c_int,  # l_int32 incolor
                                ),
        'pixRotateWithAlpha': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_float,  # l_float32 angle
                               LPPix,  # PIX * pixg
                               c_float,  # l_float32 fract
                               ),
        'pixRotateAM': (LPPix,  # PIX *
                        LPPix,  # PIX * pixs
                        c_float,  # l_float32 angle
                        c_int,  # l_int32 incolor
                        ),
        'pixRotateAMColor': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_float,  # l_float32 angle
                             c_uint,  # l_uint32 colorval
                             ),
        'pixRotateAMGray': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_float,  # l_float32 angle
                            c_ubyte,  # l_uint8 grayval
                            ),
        'pixRotateAMCorner': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_float,  # l_float32 angle
                              c_int,  # l_int32 incolor
                              ),
        'pixRotateAMColorCorner': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_float,  # l_float32 angle
                                   c_uint,  # l_uint32 fillval
                                   ),
        'pixRotateAMGrayCorner': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_float,  # l_float32 angle
                                  c_ubyte,  # l_uint8 grayval
                                  ),
        'pixRotateAMColorFast': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_float,  # l_float32 angle
                                 c_uint,  # l_uint32 colorval
                                 ),
        'pixRotateOrth': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 quads
                          ),
        'pixRotate180': (LPPix,  # PIX *
                         LPPix,  # PIX * pixd
                         LPPix,  # PIX * pixs
                         ),
        'pixRotate90': (LPPix,  # PIX *
                        LPPix,  # PIX * pixs
                        c_int,  # l_int32 direction
                        ),
        'pixFlipLR': (LPPix,  # PIX *
                      LPPix,  # PIX * pixd
                      LPPix,  # PIX * pixs
                      ),
        'pixFlipTB': (LPPix,  # PIX *
                      LPPix,  # PIX * pixd
                      LPPix,  # PIX * pixs
                      ),
        'pixRotateShear': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 xcen
                           c_int,  # l_int32 ycen
                           c_float,  # l_float32 angle
                           c_int,  # l_int32 incolor
                           ),
        'pixRotate2Shear': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 xcen
                            c_int,  # l_int32 ycen
                            c_float,  # l_float32 angle
                            c_int,  # l_int32 incolor
                            ),
        'pixRotate3Shear': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 xcen
                            c_int,  # l_int32 ycen
                            c_float,  # l_float32 angle
                            c_int,  # l_int32 incolor
                            ),
        'pixRotateShearIP': (c_int,
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 xcen
                             c_int,  # l_int32 ycen
                             c_float,  # l_float32 angle
                             c_int,  # l_int32 incolor
                             ),
        'pixRotateShearCenter': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_float,  # l_float32 angle
                                 c_int,  # l_int32 incolor
                                 ),
        'pixRotateShearCenterIP': (c_int,
                                   LPPix,  # PIX * pixs
                                   c_float,  # l_float32 angle
                                   c_int,  # l_int32 incolor
                                   ),
        'pixStrokeWidthTransform': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 color
                                    c_int,  # l_int32 depth
                                    c_int,  # l_int32 nangles
                                    ),
        'pixRunlengthTransform': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 color
                                  c_int,  # l_int32 direction
                                  c_int,  # l_int32 depth
                                  ),
        'pixFindHorizontalRuns': (c_int,
                                  LPPix,  # PIX * pix
                                  c_int,  # l_int32 y
                                  c_int_p,  # l_int32 * xstart
                                  c_int_p,  # l_int32 * xend
                                  c_int_p,  # l_int32 * pn
                                  ),
        'pixFindVerticalRuns': (c_int,
                                LPPix,  # PIX * pix
                                c_int,  # l_int32 x
                                c_int_p,  # l_int32 * ystart
                                c_int_p,  # l_int32 * yend
                                c_int_p,  # l_int32 * pn
                                ),
        'pixFindMaxRuns': (LPNuma,  # NUMA *
                           LPPix,  # PIX * pix
                           c_int,  # l_int32 direction
                           LPLPNuma,  # NUMA ** pnastart
                           ),
        'pixFindMaxHorizontalRunOnLine': (c_int,
                                          LPPix,  # PIX * pix
                                          c_int,  # l_int32 y
                                          c_int_p,  # l_int32 * pxstart
                                          c_int_p,  # l_int32 * psize
                                          ),
        'pixFindMaxVerticalRunOnLine': (c_int,
                                        LPPix,  # PIX * pix
                                        c_int,  # l_int32 x
                                        c_int_p,  # l_int32 * pystart
                                        c_int_p,  # l_int32 * psize
                                        ),
        'runlengthMembershipOnLine': (c_int,
                                      c_int_p,  # l_int32 * buffer
                                      c_int,  # l_int32 size
                                      c_int,  # l_int32 depth
                                      c_int_p,  # l_int32 * start
                                      c_int_p,  # l_int32 * end
                                      c_int,  # l_int32 n
                                      ),
        'makeMSBitLocTab': (c_int_p,
                            c_int,  # l_int32 bitval
                            ),
        'sarrayCreate': (LPSarray,  # SARRAY *
                         c_int,  # l_int32 n
                         ),
        'sarrayCreateInitialized': (LPSarray,  # SARRAY *
                                    c_int,  # l_int32 n
                                    c_char_p,  # const char * initstr
                                    ),
        'sarrayCreateWordsFromString': (LPSarray,  # SARRAY *
                                        c_char_p,  # const char * string
                                        ),
        'sarrayCreateLinesFromString': (LPSarray,  # SARRAY *
                                        c_char_p,  # const char * string
                                        c_int,  # l_int32 blankflag
                                        ),
        'sarrayDestroy': (None,
                          LPLPSarray,  # SARRAY ** psa
                          ),
        'sarrayCopy': (LPSarray,  # SARRAY *
                       LPSarray,  # SARRAY * sa
                       ),
        'sarrayClone': (LPSarray,  # SARRAY *
                        LPSarray,  # SARRAY * sa
                        ),
        'sarrayAddString': (c_int,
                            LPSarray,  # SARRAY * sa
                            c_char_p,  # const char * string
                            c_int,  # l_int32 copyflag
                            ),
        'sarrayRemoveString': (c_char_p,
                               LPSarray,  # SARRAY * sa
                               c_int,  # l_int32 index
                               ),
        'sarrayReplaceString': (c_int,
                                LPSarray,  # SARRAY * sa
                                c_int,  # l_int32 index
                                c_char_p,  # char * newstr
                                c_int,  # l_int32 copyflag
                                ),
        'sarrayClear': (c_int,
                        LPSarray,  # SARRAY * sa
                        ),
        'sarrayGetCount': (c_int,
                           LPSarray,  # SARRAY * sa
                           ),
        'sarrayGetArray': (POINTER(c_char_p),
                           LPSarray,  # SARRAY * sa
                           c_int_p,  # l_int32 * pnalloc
                           c_int_p,  # l_int32 * pn
                           ),
        'sarrayGetString': (c_char_p,
                            LPSarray,  # SARRAY * sa
                            c_int,  # l_int32 index
                            c_int,  # l_int32 copyflag
                            ),
        'sarrayGetRefcount': (c_int,
                              LPSarray,  # SARRAY * sa
                              ),
        'sarrayChangeRefcount': (c_int,
                                 LPSarray,  # SARRAY * sa
                                 c_int,  # l_int32 delta
                                 ),
        'sarrayToString': (c_char_p,
                           LPSarray,  # SARRAY * sa
                           c_int,  # l_int32 addnlflag
                           ),
        'sarrayToStringRange': (c_char_p,
                                LPSarray,  # SARRAY * sa
                                c_int,  # l_int32 first
                                c_int,  # l_int32 nstrings
                                c_int,  # l_int32 addnlflag
                                ),
        'sarrayConcatUniformly': (LPSarray,  # SARRAY *
                                  LPSarray,  # SARRAY * sa
                                  c_int,  # l_int32 n
                                  c_int,  # l_int32 addnlflag
                                  ),
        'sarrayJoin': (c_int,
                       LPSarray,  # SARRAY * sa1
                       LPSarray,  # SARRAY * sa2
                       ),
        'sarrayAppendRange': (c_int,
                              LPSarray,  # SARRAY * sa1
                              LPSarray,  # SARRAY * sa2
                              c_int,  # l_int32 start
                              c_int,  # l_int32 end
                              ),
        'sarrayPadToSameSize': (c_int,
                                LPSarray,  # SARRAY * sa1
                                LPSarray,  # SARRAY * sa2
                                c_char_p,  # const char * padstring
                                ),
        'sarrayConvertWordsToLines': (LPSarray,  # SARRAY *
                                      LPSarray,  # SARRAY * sa
                                      c_int,  # l_int32 linesize
                                      ),
        'sarraySplitString': (c_int,
                              LPSarray,  # SARRAY * sa
                              c_char_p,  # const char * str
                              c_char_p,  # const char * separators
                              ),
        'sarraySelectBySubstring': (LPSarray,  # SARRAY *
                                    LPSarray,  # SARRAY * sain
                                    c_char_p,  # const char * substr
                                    ),
        'sarraySelectRange': (LPSarray,  # SARRAY *
                              LPSarray,  # SARRAY * sain
                              c_int,  # l_int32 first
                              c_int,  # l_int32 last
                              ),
        'sarrayParseRange': (c_int,
                             LPSarray,  # SARRAY * sa
                             c_int,  # l_int32 start
                             c_int_p,  # l_int32 * pactualstart
                             c_int_p,  # l_int32 * pend
                             c_int_p,  # l_int32 * pnewstart
                             c_char_p,  # const char * substr
                             c_int,  # l_int32 loc
                             ),
        'sarrayRead': (LPSarray,  # SARRAY *
                       c_char_p,  # const char * filename
                       ),
        'sarrayReadStream': (LPSarray,  # SARRAY *
                             LPFile,  # FILE * fp
                             ),
        'sarrayReadMem': (LPSarray,  # SARRAY *
                          c_ubyte_p,  # const l_uint8 * data
                          c_size_t,  # size_t size
                          ),
        'sarrayWrite': (c_int,
                        c_char_p,  # const char * filename
                        LPSarray,  # SARRAY * sa
                        ),
        'sarrayWriteStream': (c_int,
                              LPFile,  # FILE * fp
                              LPSarray,  # SARRAY * sa
                              ),
        'sarrayWriteStderr': (c_int,
                              LPSarray,  # SARRAY * sa
                              ),
        'sarrayWriteMem': (c_int,
                           POINTER(c_ubyte_p),  # l_uint8 ** pdata
                           c_size_t_p,  # size_t * psize
                           LPSarray,  # SARRAY * sa
                           ),
        'sarrayAppend': (c_int,
                         c_char_p,  # const char * filename
                         LPSarray,  # SARRAY * sa
                         ),
        'getNumberedPathnamesInDirectory': (LPSarray,  # SARRAY *
                                            c_char_p,  # const char * dirname
                                            c_char_p,  # const char * substr
                                            c_int,  # l_int32 numpre
                                            c_int,  # l_int32 numpost
                                            c_int,  # l_int32 maxnum
                                            ),
        'getSortedPathnamesInDirectory': (LPSarray,  # SARRAY *
                                          c_char_p,  # const char * dirname
                                          c_char_p,  # const char * substr
                                          c_int,  # l_int32 first
                                          c_int,  # l_int32 nfiles
                                          ),
        'convertSortedToNumberedPathnames': (LPSarray,  # SARRAY *
                                             LPSarray,  # SARRAY * sa
                                             c_int,  # l_int32 numpre
                                             c_int,  # l_int32 numpost
                                             c_int,  # l_int32 maxnum
                                             ),
        'getFilenamesInDirectory': (LPSarray,  # SARRAY *
                                    c_char_p,  # const char * dirname
                                    ),
        'sarraySort': (LPSarray,  # SARRAY *
                       LPSarray,  # SARRAY * saout
                       LPSarray,  # SARRAY * sain
                       c_int,  # l_int32 sortorder
                       ),
        'sarraySortByIndex': (LPSarray,  # SARRAY *
                              LPSarray,  # SARRAY * sain
                              LPNuma,  # NUMA * naindex
                              ),
        'stringCompareLexical': (c_int,
                                 c_char_p,  # const char * str1
                                 c_char_p,  # const char * str2
                                 ),
        'sarrayRemoveDupsByAset': (c_int,
                                   LPSarray,  # SARRAY * sas
                                   LPLPSarray,  # SARRAY ** psad
                                   ),
        'sarrayUnionByAset': (c_int,
                              LPSarray,  # SARRAY * sa1
                              LPSarray,  # SARRAY * sa2
                              LPLPSarray,  # SARRAY ** psad
                              ),
        'sarrayIntersectionByAset': (c_int,
                                     LPSarray,  # SARRAY * sa1
                                     LPSarray,  # SARRAY * sa2
                                     LPLPSarray,  # SARRAY ** psad
                                     ),
        'sarrayUnionByHmap': (c_int,
                              LPSarray,  # SARRAY * sa1
                              LPSarray,  # SARRAY * sa2
                              LPLPSarray,  # SARRAY ** psad
                              ),
        'sarrayIntersectionByHmap': (c_int,
                                     LPSarray,  # SARRAY * sa1
                                     LPSarray,  # SARRAY * sa2
                                     LPLPSarray,  # SARRAY ** psad
                                     ),
        'sarrayGenerateIntegers': (LPSarray,  # SARRAY *
                                   c_int,  # l_int32 n
                                   ),
        'sarrayLookupCSKV': (c_int,
                             LPSarray,  # SARRAY * sa
                             c_char_p,  # const char * keystring
                             POINTER(c_char_p),  # char ** pvalstring
                             ),
        'pixScale': (LPPix,  # PIX *
                     LPPix,  # PIX * pixs
                     c_float,  # l_float32 scalex
                     c_float,  # l_float32 scaley
                     ),
        'pixScaleToSizeRel': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 delw
                              c_int,  # l_int32 delh
                              ),
        'pixScaleToSize': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_int,  # l_int32 wd
                           c_int,  # l_int32 hd
                           ),
        'pixScaleToResolution': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_float,  # l_float32 target
                                 c_float,  # l_float32 assumed
                                 c_float_p,  # l_float32 * pscalefact
                                 ),
        'pixScaleGeneral': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_float,  # l_float32 scalex
                            c_float,  # l_float32 scaley
                            c_float,  # l_float32 sharpfract
                            c_int,  # l_int32 sharpwidth
                            ),
        'pixScaleLI': (LPPix,  # PIX *
                       LPPix,  # PIX * pixs
                       c_float,  # l_float32 scalex
                       c_float,  # l_float32 scaley
                       ),
        'pixScaleColorLI': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            c_float,  # l_float32 scalex
                            c_float,  # l_float32 scaley
                            ),
        'pixScaleColor2xLI': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              ),
        'pixScaleColor4xLI': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              ),
        'pixScaleGrayLI': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_float,  # l_float32 scalex
                           c_float,  # l_float32 scaley
                           ),
        'pixScaleGray2xLI': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             ),
        'pixScaleGray4xLI': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             ),
        'pixScaleGray2xLIThresh': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 thresh
                                   ),
        'pixScaleGray2xLIDither': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   ),
        'pixScaleGray4xLIThresh': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 thresh
                                   ),
        'pixScaleGray4xLIDither': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   ),
        'pixScaleBySampling': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_float,  # l_float32 scalex
                               c_float,  # l_float32 scaley
                               ),
        'pixScaleBySamplingToSize': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 wd
                                     c_int,  # l_int32 hd
                                     ),
        'pixScaleByIntSampling': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 factor
                                  ),
        'pixScaleRGBToGrayFast': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 factor
                                  c_int,  # l_int32 color
                                  ),
        'pixScaleRGBToBinaryFast': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 factor
                                    c_int,  # l_int32 thresh
                                    ),
        'pixScaleGrayToBinaryFast': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 factor
                                     c_int,  # l_int32 thresh
                                     ),
        'pixScaleSmooth': (LPPix,  # PIX *
                           LPPix,  # PIX * pix
                           c_float,  # l_float32 scalex
                           c_float,  # l_float32 scaley
                           ),
        'pixScaleSmoothToSize': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 wd
                                 c_int,  # l_int32 hd
                                 ),
        'pixScaleRGBToGray2': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_float,  # l_float32 rwt
                               c_float,  # l_float32 gwt
                               c_float,  # l_float32 bwt
                               ),
        'pixScaleAreaMap': (LPPix,  # PIX *
                            LPPix,  # PIX * pix
                            c_float,  # l_float32 scalex
                            c_float,  # l_float32 scaley
                            ),
        'pixScaleAreaMap2': (LPPix,  # PIX *
                             LPPix,  # PIX * pix
                             ),
        'pixScaleAreaMapToSize': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_int,  # l_int32 wd
                                  c_int,  # l_int32 hd
                                  ),
        'pixScaleBinary': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_float,  # l_float32 scalex
                           c_float,  # l_float32 scaley
                           ),
        'pixScaleToGray': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs
                           c_float,  # l_float32 scalefactor
                           ),
        'pixScaleToGrayFast': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_float,  # l_float32 scalefactor
                               ),
        'pixScaleToGray2': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            ),
        'pixScaleToGray3': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            ),
        'pixScaleToGray4': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            ),
        'pixScaleToGray6': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            ),
        'pixScaleToGray8': (LPPix,  # PIX *
                            LPPix,  # PIX * pixs
                            ),
        'pixScaleToGray16': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             ),
        'pixScaleToGrayMipmap': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_float,  # l_float32 scalefactor
                                 ),
        'pixScaleMipmap': (LPPix,  # PIX *
                           LPPix,  # PIX * pixs1
                           LPPix,  # PIX * pixs2
                           c_float,  # l_float32 scale
                           ),
        'pixExpandReplicate': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 factor
                               ),
        'pixScaleGrayMinMax': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 xfact
                               c_int,  # l_int32 yfact
                               c_int,  # l_int32 type
                               ),
        'pixScaleGrayMinMax2': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 type
                                ),
        'pixScaleGrayRankCascade': (LPPix,  # PIX *
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 level1
                                    c_int,  # l_int32 level2
                                    c_int,  # l_int32 level3
                                    c_int,  # l_int32 level4
                                    ),
        'pixScaleGrayRank2': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 rank
                              ),
        'pixScaleAndTransferAlpha': (c_int,
                                     LPPix,  # PIX * pixd
                                     LPPix,  # PIX * pixs
                                     c_float,  # l_float32 scalex
                                     c_float,  # l_float32 scaley
                                     ),
        'pixScaleWithAlpha': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_float,  # l_float32 scalex
                              c_float,  # l_float32 scaley
                              LPPix,  # PIX * pixg
                              c_float,  # l_float32 fract
                              ),
        'pixSeedfillBinary': (LPPix,  # PIX *
                              LPPix,  # PIX * pixd
                              LPPix,  # PIX * pixs
                              LPPix,  # PIX * pixm
                              c_int,  # l_int32 connectivity
                              ),
        'pixSeedfillBinaryRestricted': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixd
                                        LPPix,  # PIX * pixs
                                        LPPix,  # PIX * pixm
                                        c_int,  # l_int32 connectivity
                                        c_int,  # l_int32 xmax
                                        c_int,  # l_int32 ymax
                                        ),
        'pixHolesByFilling': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 connectivity
                              ),
        'pixFillClosedBorders': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 connectivity
                                 ),
        'pixExtractBorderConnComps': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      c_int,  # l_int32 connectivity
                                      ),
        'pixRemoveBorderConnComps': (LPPix,  # PIX *
                                     LPPix,  # PIX * pixs
                                     c_int,  # l_int32 connectivity
                                     ),
        'pixFillBgFromBorder': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 connectivity
                                ),
        'pixFillHolesToBoundingRect': (LPPix,  # PIX *
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 minsize
                                       c_float,  # l_float32 maxhfract
                                       c_float,  # l_float32 minfgfract
                                       ),
        'pixSeedfillGray': (c_int,
                            LPPix,  # PIX * pixs
                            LPPix,  # PIX * pixm
                            c_int,  # l_int32 connectivity
                            ),
        'pixSeedfillGrayInv': (c_int,
                               LPPix,  # PIX * pixs
                               LPPix,  # PIX * pixm
                               c_int,  # l_int32 connectivity
                               ),
        'pixSeedfillGraySimple': (c_int,
                                  LPPix,  # PIX * pixs
                                  LPPix,  # PIX * pixm
                                  c_int,  # l_int32 connectivity
                                  ),
        'pixSeedfillGrayInvSimple': (c_int,
                                     LPPix,  # PIX * pixs
                                     LPPix,  # PIX * pixm
                                     c_int,  # l_int32 connectivity
                                     ),
        'pixSeedfillGrayBasin': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixb
                                 LPPix,  # PIX * pixm
                                 c_int,  # l_int32 delta
                                 c_int,  # l_int32 connectivity
                                 ),
        'pixDistanceFunction': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 connectivity
                                c_int,  # l_int32 outdepth
                                c_int,  # l_int32 boundcond
                                ),
        'pixSeedspread': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 connectivity
                          ),
        'pixLocalExtrema': (c_int,
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 maxmin
                            c_int,  # l_int32 minmax
                            LPLPPix,  # PIX ** ppixmin
                            LPLPPix,  # PIX ** ppixmax
                            ),
        'pixSelectedLocalExtrema': (c_int,
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 mindist
                                    LPLPPix,  # PIX ** ppixmin
                                    LPLPPix,  # PIX ** ppixmax
                                    ),
        'pixFindEqualValues': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs1
                               LPPix,  # PIX * pixs2
                               ),
        'pixSelectMinInConnComp': (c_int,
                                   LPPix,  # PIX * pixs
                                   LPPix,  # PIX * pixm
                                   LPLPPta,  # PTA ** ppta
                                   LPLPNuma,  # NUMA ** pnav
                                   ),
        'pixRemoveSeededComponents': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixd
                                      LPPix,  # PIX * pixs
                                      LPPix,  # PIX * pixm
                                      c_int,  # l_int32 connectivity
                                      c_int,  # l_int32 bordersize
                                      ),
        'create2dIntArray': (POINTER(c_int_p),
                             c_int,  # l_int32 sy
                             c_int,  # l_int32 sx
                             ),
        'getCompositeParameters': (c_int,
                                   c_int,  # l_int32 size
                                   c_int_p,  # l_int32 * psize1
                                   c_int_p,  # l_int32 * psize2
                                   POINTER(c_char_p),  # char ** pnameh1
                                   POINTER(c_char_p),  # char ** pnameh2
                                   POINTER(c_char_p),  # char ** pnamev1
                                   POINTER(c_char_p),  # char ** pnamev2
                                   ),
        'pixGetRunCentersOnLine': (LPNuma,  # NUMA *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 x
                                   c_int,  # l_int32 y
                                   c_int,  # l_int32 minlength
                                   ),
        'pixGetRunsOnLine': (LPNuma,  # NUMA *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 x1
                             c_int,  # l_int32 y1
                             c_int,  # l_int32 x2
                             c_int,  # l_int32 y2
                             ),
        'pixSubsampleBoundaryPixels': (LPPta,  # PTA *
                                       LPPix,  # PIX * pixs
                                       c_int,  # l_int32 skip
                                       ),
        'adjacentOnPixelInRaster': (c_int,
                                    LPPix,  # PIX * pixs
                                    c_int,  # l_int32 x
                                    c_int,  # l_int32 y
                                    c_int_p,  # l_int32 * pxa
                                    c_int_p,  # l_int32 * pya
                                    ),
        'pixHShear': (LPPix,  # PIX *
                      LPPix,  # PIX * pixd
                      LPPix,  # PIX * pixs
                      c_int,  # l_int32 yloc
                      c_float,  # l_float32 radang
                      c_int,  # l_int32 incolor
                      ),
        'pixVShear': (LPPix,  # PIX *
                      LPPix,  # PIX * pixd
                      LPPix,  # PIX * pixs
                      c_int,  # l_int32 xloc
                      c_float,  # l_float32 radang
                      c_int,  # l_int32 incolor
                      ),
        'pixHShearCorner': (LPPix,  # PIX *
                            LPPix,  # PIX * pixd
                            LPPix,  # PIX * pixs
                            c_float,  # l_float32 radang
                            c_int,  # l_int32 incolor
                            ),
        'pixVShearCorner': (LPPix,  # PIX *
                            LPPix,  # PIX * pixd
                            LPPix,  # PIX * pixs
                            c_float,  # l_float32 radang
                            c_int,  # l_int32 incolor
                            ),
        'pixHShearCenter': (LPPix,  # PIX *
                            LPPix,  # PIX * pixd
                            LPPix,  # PIX * pixs
                            c_float,  # l_float32 radang
                            c_int,  # l_int32 incolor
                            ),
        'pixVShearCenter': (LPPix,  # PIX *
                            LPPix,  # PIX * pixd
                            LPPix,  # PIX * pixs
                            c_float,  # l_float32 radang
                            c_int,  # l_int32 incolor
                            ),
        'pixHShearIP': (c_int,
                        LPPix,  # PIX * pixs
                        c_int,  # l_int32 yloc
                        c_float,  # l_float32 radang
                        c_int,  # l_int32 incolor
                        ),
        'pixVShearIP': (c_int,
                        LPPix,  # PIX * pixs
                        c_int,  # l_int32 xloc
                        c_float,  # l_float32 radang
                        c_int,  # l_int32 incolor
                        ),
        'pixHShearLI': (LPPix,  # PIX *
                        LPPix,  # PIX * pixs
                        c_int,  # l_int32 yloc
                        c_float,  # l_float32 radang
                        c_int,  # l_int32 incolor
                        ),
        'pixVShearLI': (LPPix,  # PIX *
                        LPPix,  # PIX * pixs
                        c_int,  # l_int32 xloc
                        c_float,  # l_float32 radang
                        c_int,  # l_int32 incolor
                        ),
        'pixDeskewBoth': (LPPix,  # PIX *
                          LPPix,  # PIX * pixs
                          c_int,  # l_int32 redsearch
                          ),
        'pixDeskew': (LPPix,  # PIX *
                      LPPix,  # PIX * pixs
                      c_int,  # l_int32 redsearch
                      ),
        'pixFindSkewAndDeskew': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 redsearch
                                 c_float_p,  # l_float32 * pangle
                                 c_float_p,  # l_float32 * pconf
                                 ),
        'pixDeskewGeneral': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 redsweep
                             c_float,  # l_float32 sweeprange
                             c_float,  # l_float32 sweepdelta
                             c_int,  # l_int32 redsearch
                             c_int,  # l_int32 thresh
                             c_float_p,  # l_float32 * pangle
                             c_float_p,  # l_float32 * pconf
                             ),
        'pixFindSkew': (c_int,
                        LPPix,  # PIX * pixs
                        c_float_p,  # l_float32 * pangle
                        c_float_p,  # l_float32 * pconf
                        ),
        'pixFindSkewSweep': (c_int,
                             LPPix,  # PIX * pixs
                             c_float_p,  # l_float32 * pangle
                             c_int,  # l_int32 reduction
                             c_float,  # l_float32 sweeprange
                             c_float,  # l_float32 sweepdelta
                             ),
        'pixFindSkewSweepAndSearch': (c_int,
                                      LPPix,  # PIX * pixs
                                      c_float_p,  # l_float32 * pangle
                                      c_float_p,  # l_float32 * pconf
                                      c_int,  # l_int32 redsweep
                                      c_int,  # l_int32 redsearch
                                      c_float,  # l_float32 sweeprange
                                      c_float,  # l_float32 sweepdelta
                                      c_float,  # l_float32 minbsdelta
                                      ),
        'pixFindSkewSweepAndSearchScore': (c_int,
                                           LPPix,  # PIX * pixs
                                           # l_float32 * pangle
                                           c_float_p,
                                           # l_float32 * pconf
                                           c_float_p,
                                           # l_float32 * pendscore
                                           c_float_p,
                                           c_int,  # l_int32 redsweep
                                           c_int,  # l_int32 redsearch
                                           c_float,  # l_float32 sweepcenter
                                           c_float,  # l_float32 sweeprange
                                           c_float,  # l_float32 sweepdelta
                                           c_float,  # l_float32 minbsdelta
                                           ),
        'pixFindSkewSweepAndSearchScorePivot': (c_int,
                                                LPPix,  # PIX * pixs
                                                # l_float32 * pangle
                                                c_float_p,
                                                # l_float32 * pconf
                                                c_float_p,
                                                # l_float32 * pendscore
                                                c_float_p,
                                                c_int,  # l_int32 redsweep
                                                c_int,  # l_int32 redsearch
                                                # l_float32 sweepcenter
                                                c_float,
                                                # l_float32 sweeprange
                                                c_float,
                                                # l_float32 sweepdelta
                                                c_float,
                                                # l_float32 minbsdelta
                                                c_float,
                                                c_int,  # l_int32 pivot
                                                ),
        'pixFindSkewOrthogonalRange': (c_int,
                                       LPPix,  # PIX * pixs
                                       c_float_p,  # l_float32 * pangle
                                       c_float_p,  # l_float32 * pconf
                                       c_int,  # l_int32 redsweep
                                       c_int,  # l_int32 redsearch
                                       c_float,  # l_float32 sweeprange
                                       c_float,  # l_float32 sweepdelta
                                       c_float,  # l_float32 minbsdelta
                                       c_float,  # l_float32 confprior
                                       ),
        'pixFindDifferentialSquareSum': (c_int,
                                         LPPix,  # PIX * pixs
                                         c_float_p,  # l_float32 * psum
                                         ),
        'pixFindNormalizedSquareSum': (c_int,
                                       LPPix,  # PIX * pixs
                                       # l_float32 * phratio
                                       c_float_p,
                                       # l_float32 * pvratio
                                       c_float_p,
                                       c_float_p,  # l_float32 * pfract
                                       ),
        'pixReadStreamSpix': (LPPix,  # PIX *
                              LPFile,  # FILE * fp
                              ),
        'readHeaderSpix': (c_int,
                           c_char_p,  # const char * filename
                           c_int_p,  # l_int32 * pwidth
                           c_int_p,  # l_int32 * pheight
                           c_int_p,  # l_int32 * pbps
                           c_int_p,  # l_int32 * pspp
                           c_int_p,  # l_int32 * piscmap
                           ),
        'freadHeaderSpix': (c_int,
                            LPFile,  # FILE * fp
                            c_int_p,  # l_int32 * pwidth
                            c_int_p,  # l_int32 * pheight
                            c_int_p,  # l_int32 * pbps
                            c_int_p,  # l_int32 * pspp
                            c_int_p,  # l_int32 * piscmap
                            ),
        'sreadHeaderSpix': (c_int,
                            c_uint_p,  # const l_uint32 * data
                            c_size_t,  # size_t size
                            c_int_p,  # l_int32 * pwidth
                            c_int_p,  # l_int32 * pheight
                            c_int_p,  # l_int32 * pbps
                            c_int_p,  # l_int32 * pspp
                            c_int_p,  # l_int32 * piscmap
                            ),
        'pixWriteStreamSpix': (c_int,
                               LPFile,  # FILE * fp
                               LPPix,  # PIX * pix
                               ),
        'pixReadMemSpix': (LPPix,  # PIX *
                           c_ubyte_p,  # const l_uint8 * data
                           c_size_t,  # size_t size
                           ),
        'pixWriteMemSpix': (c_int,
                            POINTER(c_ubyte_p),  # l_uint8 ** pdata
                            c_size_t_p,  # size_t * psize
                            LPPix,  # PIX * pix
                            ),
        'pixSerializeToMemory': (c_int,
                                 LPPix,  # PIX * pixs
                                 # l_uint32 ** pdata
                                 POINTER(c_uint_p),
                                 c_size_t_p,  # size_t * pnbytes
                                 ),
        'pixDeserializeFromMemory': (LPPix,  # PIX *
                                     c_uint_p,  # const l_uint32 * data
                                     c_size_t,  # size_t nbytes
                                     ),
        'strcodeCreateFromFile': (c_int,
                                  c_char_p,  # const char * filein
                                  c_int,  # l_int32 fileno
                                  c_char_p,  # const char * outdir
                                  ),
        'l_getStructStrFromFile': (c_int,
                                   c_char_p,  # const char * filename
                                   c_int,  # l_int32 field
                                   POINTER(c_char_p),  # char ** pstr
                                   ),
        'pixFindStrokeLength': (c_int,
                                LPPix,  # PIX * pixs
                                c_int_p,  # l_int32 * tab8
                                c_int_p,  # l_int32 * plength
                                ),
        'pixFindStrokeWidth': (c_int,
                               LPPix,  # PIX * pixs
                               c_float,  # l_float32 thresh
                               c_int_p,  # l_int32 * tab8
                               c_float_p,  # l_float32 * pwidth
                               LPLPNuma,  # NUMA ** pnahisto
                               ),
        'pixaFindStrokeWidth': (LPNuma,  # NUMA *
                                LPPixa,  # PIXA * pixa
                                c_float,  # l_float32 thresh
                                c_int_p,  # l_int32 * tab8
                                c_int,  # l_int32 debug
                                ),
        'pixaModifyStrokeWidth': (LPPixa,  # PIXA *
                                  LPPixa,  # PIXA * pixas
                                  c_float,  # l_float32 targetw
                                  ),
        'pixModifyStrokeWidth': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_float,  # l_float32 width
                                 c_float,  # l_float32 targetw
                                 ),
        'pixaSetStrokeWidth': (LPPixa,  # PIXA *
                               LPPixa,  # PIXA * pixas
                               c_int,  # l_int32 width
                               c_int,  # l_int32 thinfirst
                               c_int,  # l_int32 connectivity
                               ),
        'pixSetStrokeWidth': (LPPix,  # PIX *
                              LPPix,  # PIX * pixs
                              c_int,  # l_int32 width
                              c_int,  # l_int32 thinfirst
                              c_int,  # l_int32 connectivity
                              ),
        'sudokuReadFile': (c_int_p,
                           c_char_p,  # const char * filename
                           ),
        'sudokuReadString': (c_int_p,
                             c_char_p,  # const char * str
                             ),
        'sudokuTestUniqueness': (c_int,
                                 c_int_p,  # l_int32 * array
                                 c_int_p,  # l_int32 * punique
                                 ),
        'splitStringToParagraphs': (LPSarray,  # SARRAY *
                                    c_char_p,  # char * textstr
                                    c_int,  # l_int32 splitflag
                                    ),
        'pixReadTiff': (LPPix,  # PIX *
                        c_char_p,  # const char * filename
                        c_int,  # l_int32 n
                        ),
        'pixReadStreamTiff': (LPPix,  # PIX *
                              LPFile,  # FILE * fp
                              c_int,  # l_int32 n
                              ),
        'pixWriteTiff': (c_int,
                         c_char_p,  # const char * filename
                         LPPix,  # PIX * pix
                         c_int,  # l_int32 comptype
                         c_char_p,  # const char * modestr
                         ),
        'pixWriteTiffCustom': (c_int,
                               c_char_p,  # const char * filename
                               LPPix,  # PIX * pix
                               c_int,  # l_int32 comptype
                               c_char_p,  # const char * modestr
                               LPNuma,  # NUMA * natags
                               LPSarray,  # SARRAY * savals
                               LPSarray,  # SARRAY * satypes
                               LPNuma,  # NUMA * nasizes
                               ),
        'pixWriteStreamTiff': (c_int,
                               LPFile,  # FILE * fp
                               LPPix,  # PIX * pix
                               c_int,  # l_int32 comptype
                               ),
        'pixWriteStreamTiffWA': (c_int,
                                 LPFile,  # FILE * fp
                                 LPPix,  # PIX * pix
                                 c_int,  # l_int32 comptype
                                 c_char_p,  # const char * modestr
                                 ),
        'pixReadFromMultipageTiff': (LPPix,  # PIX *
                                     c_char_p,  # const char * fname
                                     c_size_t_p,  # size_t * poffset
                                     ),
        'pixaReadMultipageTiff': (LPPixa,  # PIXA *
                                  c_char_p,  # const char * filename
                                  ),
        'pixaWriteMultipageTiff': (c_int,
                                   c_char_p,  # const char * fname
                                   LPPixa,  # PIXA * pixa
                                   ),
        'writeMultipageTiff': (c_int,
                               c_char_p,  # const char * dirin
                               c_char_p,  # const char * substr
                               c_char_p,  # const char * fileout
                               ),
        'writeMultipageTiffSA': (c_int,
                                 LPSarray,  # SARRAY * sa
                                 c_char_p,  # const char * fileout
                                 ),
        'fprintTiffInfo': (c_int,
                           LPFile,  # FILE * fpout
                           c_char_p,  # const char * tiffile
                           ),
        'tiffGetCount': (c_int,
                         LPFile,  # FILE * fp
                         c_int_p,  # l_int32 * pn
                         ),
        'getTiffResolution': (c_int,
                              LPFile,  # FILE * fp
                              c_int_p,  # l_int32 * pxres
                              c_int_p,  # l_int32 * pyres
                              ),
        'readHeaderTiff': (c_int,
                           c_char_p,  # const char * filename
                           c_int,  # l_int32 n
                           c_int_p,  # l_int32 * pw
                           c_int_p,  # l_int32 * ph
                           c_int_p,  # l_int32 * pbps
                           c_int_p,  # l_int32 * pspp
                           c_int_p,  # l_int32 * pres
                           c_int_p,  # l_int32 * pcmap
                           c_int_p,  # l_int32 * pformat
                           ),
        'freadHeaderTiff': (c_int,
                            LPFile,  # FILE * fp
                            c_int,  # l_int32 n
                            c_int_p,  # l_int32 * pw
                            c_int_p,  # l_int32 * ph
                            c_int_p,  # l_int32 * pbps
                            c_int_p,  # l_int32 * pspp
                            c_int_p,  # l_int32 * pres
                            c_int_p,  # l_int32 * pcmap
                            c_int_p,  # l_int32 * pformat
                            ),
        'readHeaderMemTiff': (c_int,
                              c_ubyte_p,  # const l_uint8 * cdata
                              c_size_t,  # size_t size
                              c_int,  # l_int32 n
                              c_int_p,  # l_int32 * pw
                              c_int_p,  # l_int32 * ph
                              c_int_p,  # l_int32 * pbps
                              c_int_p,  # l_int32 * pspp
                              c_int_p,  # l_int32 * pres
                              c_int_p,  # l_int32 * pcmap
                              c_int_p,  # l_int32 * pformat
                              ),
        'findTiffCompression': (c_int,
                                LPFile,  # FILE * fp
                                c_int_p,  # l_int32 * pcomptype
                                ),
        'extractG4DataFromFile': (c_int,
                                  c_char_p,  # const char * filein
                                  # l_uint8 ** pdata
                                  POINTER(c_ubyte_p),
                                  c_size_t_p,  # size_t * pnbytes
                                  c_int_p,  # l_int32 * pw
                                  c_int_p,  # l_int32 * ph
                                  c_int_p,  # l_int32 * pminisblack
                                  ),
        'pixReadMemTiff': (LPPix,  # PIX *
                           c_ubyte_p,  # const l_uint8 * cdata
                           c_size_t,  # size_t size
                           c_int,  # l_int32 n
                           ),
        'pixReadMemFromMultipageTiff': (LPPix,  # PIX *
                                        # const l_uint8 * cdata
                                        c_ubyte_p,
                                        c_size_t,  # size_t size
                                        c_size_t_p,  # size_t * poffset
                                        ),
        'pixaReadMemMultipageTiff': (LPPixa,  # PIXA *
                                     c_ubyte_p,  # const l_uint8 * data
                                     c_size_t,  # size_t size
                                     ),
        'pixaWriteMemMultipageTiff': (c_int,
                                      # l_uint8 ** pdata
                                      POINTER(c_ubyte_p),
                                      c_size_t_p,  # size_t * psize
                                      LPPixa,  # PIXA * pixa
                                      ),
        'pixWriteMemTiff': (c_int,
                            POINTER(c_ubyte_p),  # l_uint8 ** pdata
                            c_size_t_p,  # size_t * psize
                            LPPix,  # PIX * pix
                            c_int,  # l_int32 comptype
                            ),
        'pixWriteMemTiffCustom': (c_int,
                                  # l_uint8 ** pdata
                                  POINTER(c_ubyte_p),
                                  c_size_t_p,  # size_t * psize
                                  LPPix,  # PIX * pix
                                  c_int,  # l_int32 comptype
                                  LPNuma,  # NUMA * natags
                                  LPSarray,  # SARRAY * savals
                                  LPSarray,  # SARRAY * satypes
                                  LPNuma,  # NUMA * nasizes
                                  ),
        'setMsgSeverity': (c_int,
                           c_int,  # l_int32 newsev
                           ),
        'returnErrorInt': (c_int,
                           c_char_p,  # const char * msg
                           c_char_p,  # const char * procname
                           c_int,  # l_int32 ival
                           ),
        'returnErrorFloat': (c_float,
                             c_char_p,  # const char * msg
                             c_char_p,  # const char * procname
                             c_float,  # l_float32 fval
                             ),
        'returnErrorPtr': (c_void_p,
                           c_char_p,  # const char * msg
                           c_char_p,  # const char * procname
                           c_void_p,  # void * pval
                           ),
        'lept_stderr': (None,
                        c_char_p,  # const char * fmt
                        ),
        'filesAreIdentical': (c_int,
                              c_char_p,  # const char * fname1
                              c_char_p,  # const char * fname2
                              c_int_p,  # l_int32 * psame
                              ),
        'convertOnLittleEnd16': (c_ushort,
                                 c_ushort,  # l_uint16 shortin
                                 ),
        'convertOnBigEnd16': (c_ushort,
                              c_ushort,  # l_uint16 shortin
                              ),
        'convertOnLittleEnd32': (c_uint,
                                 c_uint,  # l_uint32 wordin
                                 ),
        'convertOnBigEnd32': (c_uint,
                              c_uint,  # l_uint32 wordin
                              ),
        'fileCorruptByDeletion': (c_int,
                                  c_char_p,  # const char * filein
                                  c_float,  # l_float32 loc
                                  c_float,  # l_float32 size
                                  c_char_p,  # const char * fileout
                                  ),
        'fileCorruptByMutation': (c_int,
                                  c_char_p,  # const char * filein
                                  c_float,  # l_float32 loc
                                  c_float,  # l_float32 size
                                  c_char_p,  # const char * fileout
                                  ),
        'fileReplaceBytes': (c_int,
                             c_char_p,  # const char * filein
                             c_int,  # l_int32 start
                             c_int,  # l_int32 nbytes
                             c_ubyte_p,  # l_uint8 * newdata
                             c_size_t,  # size_t newsize
                             c_char_p,  # const char * fileout
                             ),
        'genRandomIntOnInterval': (c_int,
                                   c_int,  # l_int32 start
                                   c_int,  # l_int32 end
                                   c_int,  # l_int32 seed
                                   c_int_p,  # l_int32 * pval
                                   ),
        'lept_roundftoi': (c_int,
                           c_float,  # l_float32 fval
                           ),
        'l_hashStringToUint64': (c_int,
                                 c_char_p,  # const char * str
                                 c_ulonglong_p,  # l_uint64 * phash
                                 ),
        'l_hashStringToUint64Fast': (c_int,
                                     c_char_p,  # const char * str
                                     c_ulonglong_p,  # l_uint64 * phash
                                     ),
        'l_hashPtToUint64': (c_int,
                             c_int,  # l_int32 x
                             c_int,  # l_int32 y
                             c_ulonglong_p,  # l_uint64 * phash
                             ),
        'l_hashFloat64ToUint64': (c_int,
                                  c_double,  # l_float64 val
                                  c_ulonglong_p,  # l_uint64 * phash
                                  ),
        'findNextLargerPrime': (c_int,
                                c_int,  # l_int32 start
                                c_uint_p,  # l_uint32 * pprime
                                ),
        'lept_isPrime': (c_int,
                         c_ulonglong,  # l_uint64 n
                         c_int_p,  # l_int32 * pis_prime
                         c_uint_p,  # l_uint32 * pfactor
                         ),
        'convertIntToGrayCode': (c_uint,
                                 c_uint,  # l_uint32 val
                                 ),
        'convertGrayCodeToInt': (c_uint,
                                 c_uint,  # l_uint32 val
                                 ),
        'getLeptonicaVersion': (LP_c_char, ),
        'startTimer': (None, ),
        'stopTimer': (c_float, ),
        'l_getCurrentTime': (None,
                             c_int_p,  # l_int32 * sec
                             c_int_p,  # l_int32 * usec
                             ),
        'l_getFormattedDate': (c_char_p, ),
        'stringNew': (c_char_p,
                      c_char_p,  # const char * src
                      ),
        'stringCopy': (c_int,
                       c_char_p,  # char * dest
                       c_char_p,  # const char * src
                       c_int,  # l_int32 n
                       ),
        'stringCopySegment': (c_char_p,
                              c_char_p,  # const char * src
                              c_int,  # l_int32 start
                              c_int,  # l_int32 nbytes
                              ),
        'stringReplace': (c_int,
                          POINTER(c_char_p),  # char ** pdest
                          c_char_p,  # const char * src
                          ),
        'stringLength': (c_int,
                         c_char_p,  # const char * src
                         c_size_t,  # size_t size
                         ),
        'stringCat': (c_int,
                      c_char_p,  # char * dest
                      c_size_t,  # size_t size
                      c_char_p,  # const char * src
                      ),
        'stringConcatNew': (c_char_p,
                            c_char_p,  # const char * first
                            ),
        'stringJoin': (c_char_p,
                       c_char_p,  # const char * src1
                       c_char_p,  # const char * src2
                       ),
        'stringJoinIP': (c_int,
                         POINTER(c_char_p),  # char ** psrc1
                         c_char_p,  # const char * src2
                         ),
        'stringReverse': (c_char_p,
                          c_char_p,  # const char * src
                          ),
        'strtokSafe': (c_char_p,
                       c_char_p,  # char * cstr
                       c_char_p,  # const char * seps
                       POINTER(c_char_p),  # char ** psaveptr
                       ),
        'stringSplitOnToken': (c_int,
                               c_char_p,  # char * cstr
                               c_char_p,  # const char * seps
                               POINTER(c_char_p),  # char ** phead
                               POINTER(c_char_p),  # char ** ptail
                               ),
        'stringCheckForChars': (c_int,
                                c_char_p,  # const char * src
                                c_char_p,  # const char * chars
                                c_int_p,  # l_int32 * pfound
                                ),
        'stringRemoveChars': (c_char_p,
                              c_char_p,  # const char * src
                              c_char_p,  # const char * remchars
                              ),
        'stringReplaceEachSubstr': (c_char_p,
                                    c_char_p,  # const char * src
                                    c_char_p,  # const char * sub1
                                    c_char_p,  # const char * sub2
                                    c_int_p,  # l_int32 * pcount
                                    ),
        'stringReplaceSubstr': (c_char_p,
                                c_char_p,  # const char * src
                                c_char_p,  # const char * sub1
                                c_char_p,  # const char * sub2
                                c_int_p,  # l_int32 * ploc
                                c_int_p,  # l_int32 * pfound
                                ),
        'stringFindSubstr': (c_int,
                             c_char_p,  # const char * src
                             c_char_p,  # const char * sub
                             c_int_p,  # l_int32 * ploc
                             ),
        'arrayReplaceEachSequence': (c_ubyte_p,
                                     # const l_uint8 * datas
                                     c_ubyte_p,
                                     c_size_t,  # size_t dataslen
                                     c_ubyte_p,  # const l_uint8 * seq
                                     c_size_t,  # size_t seqlen
                                     # const l_uint8 * newseq
                                     c_ubyte_p,
                                     c_size_t,  # size_t newseqlen
                                     c_size_t_p,  # size_t * pdatadlen
                                     c_int_p,  # l_int32 * pcount
                                     ),
        'arrayFindSequence': (c_int,
                              c_ubyte_p,  # const l_uint8 * data
                              c_size_t,  # size_t datalen
                              c_ubyte_p,  # const l_uint8 * sequence
                              c_size_t,  # size_t seqlen
                              c_int_p,  # l_int32 * poffset
                              c_int_p,  # l_int32 * pfound
                              ),
        'reallocNew': (c_void_p,
                       POINTER(c_void_p),  # void ** pindata
                       c_size_t,  # size_t oldsize
                       c_size_t,  # size_t newsize
                       ),
        'l_binaryRead': (c_ubyte_p,
                         c_char_p,  # const char * filename
                         c_size_t_p,  # size_t * pnbytes
                         ),
        'l_binaryReadStream': (c_ubyte_p,
                               LPFile,  # FILE * fp
                               c_size_t_p,  # size_t * pnbytes
                               ),
        'l_binaryReadSelect': (c_ubyte_p,
                               c_char_p,  # const char * filename
                               c_size_t,  # size_t start
                               c_size_t,  # size_t nbytes
                               c_size_t_p,  # size_t * pnread
                               ),
        'l_binaryReadSelectStream': (c_ubyte_p,
                                     LPFile,  # FILE * fp
                                     c_size_t,  # size_t start
                                     c_size_t,  # size_t nbytes
                                     c_size_t_p,  # size_t * pnread
                                     ),
        'l_binaryWrite': (c_int,
                          c_char_p,  # const char * filename
                          c_char_p,  # const char * operation
                          c_void_p,  # const void * data
                          c_size_t,  # size_t nbytes
                          ),
        'nbytesInFile': (c_size_t,
                         c_char_p,  # const char * filename
                         ),
        'fnbytesInFile': (c_size_t,
                          LPFile,  # FILE * fp
                          ),
        'l_binaryCopy': (c_ubyte_p,
                         c_ubyte_p,  # const l_uint8 * datas
                         c_size_t,  # size_t size
                         ),
        'l_binaryCompare': (c_int,
                            c_ubyte_p,  # const l_uint8 * data1
                            c_size_t,  # size_t size1
                            c_ubyte_p,  # const l_uint8 * data2
                            c_size_t,  # size_t size2
                            c_int_p,  # l_int32 * psame
                            ),
        'fileCopy': (c_int,
                     c_char_p,  # const char * srcfile
                     c_char_p,  # const char * newfile
                     ),
        'fileConcatenate': (c_int,
                            c_char_p,  # const char * srcfile
                            c_char_p,  # const char * destfile
                            ),
        'fileAppendString': (c_int,
                             c_char_p,  # const char * filename
                             c_char_p,  # const char * str
                             ),
        'fileSplitLinesUniform': (c_int,
                                  c_char_p,  # const char * filename
                                  c_int,  # l_int32 n
                                  c_int,  # l_int32 save_empty
                                  c_char_p,  # const char * rootpath
                                  c_char_p,  # const char * ext
                                  ),
        'fopenReadStream': (LPFile,  # FILE *
                            c_char_p,  # const char * filename
                            ),
        'fopenWriteStream': (LPFile,  # FILE *
                             c_char_p,  # const char * filename
                             c_char_p,  # const char * modestring
                             ),
        'fopenReadFromMemory': (LPFile,  # FILE *
                                c_ubyte_p,  # const l_uint8 * data
                                c_size_t,  # size_t size
                                ),
        'fopenWriteWinTempfile': (LPFile, ),  # FILE *
        'lept_fopen': (LPFile,  # FILE *
                       c_char_p,  # const char * filename
                       c_char_p,  # const char * mode
                       ),
        'lept_fclose': (c_int,
                        LPFile,  # FILE * fp
                        ),
        'lept_calloc': (c_void_p,
                        c_size_t,  # size_t nmemb
                        c_size_t,  # size_t size
                        ),
        'lept_free': (None,
                      c_void_p,  # void * ptr
                      ),
        'lept_mkdir': (c_int,
                       c_char_p,  # const char * subdir
                       ),
        'lept_rmdir': (c_int,
                       c_char_p,  # const char * subdir
                       ),
        'lept_direxists': (None,
                           c_char_p,  # const char * dir
                           c_int_p,  # l_int32 * pexists
                           ),
        'lept_rm_match': (c_int,
                          c_char_p,  # const char * subdir
                          c_char_p,  # const char * substr
                          ),
        'lept_rm': (c_int,
                    c_char_p,  # const char * subdir
                    c_char_p,  # const char * tail
                    ),
        'lept_rmfile': (c_int,
                        c_char_p,  # const char * filepath
                        ),
        'lept_mv': (c_int,
                    c_char_p,  # const char * srcfile
                    c_char_p,  # const char * newdir
                    c_char_p,  # const char * newtail
                    POINTER(c_char_p),  # char ** pnewpath
                    ),
        'lept_cp': (c_int,
                    c_char_p,  # const char * srcfile
                    c_char_p,  # const char * newdir
                    c_char_p,  # const char * newtail
                    POINTER(c_char_p),  # char ** pnewpath
                    ),
        'callSystemDebug': (None,
                            c_char_p,  # const char * cmd
                            ),
        'splitPathAtDirectory': (c_int,
                                 c_char_p,  # const char * pathname
                                 POINTER(c_char_p),  # char ** pdir
                                 POINTER(c_char_p),  # char ** ptail
                                 ),
        'splitPathAtExtension': (c_int,
                                 c_char_p,  # const char * pathname
                                 POINTER(c_char_p),  # char ** pbasename
                                 POINTER(c_char_p),  # char ** pextension
                                 ),
        'pathJoin': (c_char_p,
                     c_char_p,  # const char * dir
                     c_char_p,  # const char * fname
                     ),
        'appendSubdirs': (c_char_p,
                          c_char_p,  # const char * basedir
                          c_char_p,  # const char * subdirs
                          ),
        'convertSepCharsInPath': (c_int,
                                  c_char_p,  # char * path
                                  c_int,  # l_int32 type
                                  ),
        'genPathname': (c_char_p,
                        c_char_p,  # const char * dir
                        c_char_p,  # const char * fname
                        ),
        'makeTempDirname': (c_int,
                            c_char_p,  # char * result
                            c_size_t,  # size_t nbytes
                            c_char_p,  # const char * subdir
                            ),
        'modifyTrailingSlash': (c_int,
                                c_char_p,  # char * path
                                c_size_t,  # size_t nbytes
                                c_int,  # l_int32 flag
                                ),
        'l_makeTempFilename': (c_char_p, ),
        'extractNumberFromFilename': (c_int,
                                      c_char_p,  # const char * fname
                                      c_int,  # l_int32 numpre
                                      c_int,  # l_int32 numpost
                                      ),
        'pixSimpleCaptcha': (LPPix,  # PIX *
                             LPPix,  # PIX * pixs
                             c_int,  # l_int32 border
                             c_int,  # l_int32 nterms
                             c_uint,  # l_uint32 seed
                             c_uint,  # l_uint32 color
                             c_int,  # l_int32 cmapflag
                             ),
        'pixRandomHarmonicWarp': (LPPix,  # PIX *
                                  LPPix,  # PIX * pixs
                                  c_float,  # l_float32 xmag
                                  c_float,  # l_float32 ymag
                                  c_float,  # l_float32 xfreq
                                  c_float,  # l_float32 yfreq
                                  c_int,  # l_int32 nx
                                  c_int,  # l_int32 ny
                                  c_uint,  # l_uint32 seed
                                  c_int,  # l_int32 grayval
                                  ),
        'pixWarpStereoscopic': (LPPix,  # PIX *
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 zbend
                                c_int,  # l_int32 zshiftt
                                c_int,  # l_int32 zshiftb
                                c_int,  # l_int32 ybendt
                                c_int,  # l_int32 ybendb
                                c_int,  # l_int32 redleft
                                ),
        'pixStretchHorizontal': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 dir
                                 c_int,  # l_int32 type
                                 c_int,  # l_int32 hmax
                                 c_int,  # l_int32 operation
                                 c_int,  # l_int32 incolor
                                 ),
        'pixStretchHorizontalSampled': (LPPix,  # PIX *
                                        LPPix,  # PIX * pixs
                                        c_int,  # l_int32 dir
                                        c_int,  # l_int32 type
                                        c_int,  # l_int32 hmax
                                        c_int,  # l_int32 incolor
                                        ),
        'pixStretchHorizontalLI': (LPPix,  # PIX *
                                   LPPix,  # PIX * pixs
                                   c_int,  # l_int32 dir
                                   c_int,  # l_int32 type
                                   c_int,  # l_int32 hmax
                                   c_int,  # l_int32 incolor
                                   ),
        'pixQuadraticVShear': (LPPix,  # PIX *
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 dir
                               c_int,  # l_int32 vmaxt
                               c_int,  # l_int32 vmaxb
                               c_int,  # l_int32 operation
                               c_int,  # l_int32 incolor
                               ),
        'pixQuadraticVShearSampled': (LPPix,  # PIX *
                                      LPPix,  # PIX * pixs
                                      c_int,  # l_int32 dir
                                      c_int,  # l_int32 vmaxt
                                      c_int,  # l_int32 vmaxb
                                      c_int,  # l_int32 incolor
                                      ),
        'pixQuadraticVShearLI': (LPPix,  # PIX *
                                 LPPix,  # PIX * pixs
                                 c_int,  # l_int32 dir
                                 c_int,  # l_int32 vmaxt
                                 c_int,  # l_int32 vmaxb
                                 c_int,  # l_int32 incolor
                                 ),
        'pixStereoFromPair': (LPPix,  # PIX *
                              LPPix,  # PIX * pix1
                              LPPix,  # PIX * pix2
                              c_float,  # l_float32 rwt
                              c_float,  # l_float32 gwt
                              c_float,  # l_float32 bwt
                              ),
        'pixaWriteWebPAnim': (c_int,
                              c_char_p,  # const char * filename
                              LPPixa,  # PIXA * pixa
                              c_int,  # l_int32 loopcount
                              c_int,  # l_int32 duration
                              c_int,  # l_int32 quality
                              c_int,  # l_int32 lossless
                              ),
        'pixaWriteStreamWebPAnim': (c_int,
                                    LPFile,  # FILE * fp
                                    LPPixa,  # PIXA * pixa
                                    c_int,  # l_int32 loopcount
                                    c_int,  # l_int32 duration
                                    c_int,  # l_int32 quality
                                    c_int,  # l_int32 lossless
                                    ),
        'pixaWriteMemWebPAnim': (c_int,
                                 # l_uint8 ** pencdata
                                 POINTER(c_ubyte_p),
                                 c_size_t_p,  # size_t * pencsize
                                 LPPixa,  # PIXA * pixa
                                 c_int,  # l_int32 loopcount
                                 c_int,  # l_int32 duration
                                 c_int,  # l_int32 quality
                                 c_int,  # l_int32 lossless
                                 ),
        'pixReadStreamWebP': (LPPix,  # PIX *
                              LPFile,  # FILE * fp
                              ),
        'pixReadMemWebP': (LPPix,  # PIX *
                           c_ubyte_p,  # const l_uint8 * filedata
                           c_size_t,  # size_t filesize
                           ),
        'readHeaderWebP': (c_int,
                           c_char_p,  # const char * filename
                           c_int_p,  # l_int32 * pw
                           c_int_p,  # l_int32 * ph
                           c_int_p,  # l_int32 * pspp
                           ),
        'readHeaderMemWebP': (c_int,
                              c_ubyte_p,  # const l_uint8 * data
                              c_size_t,  # size_t size
                              c_int_p,  # l_int32 * pw
                              c_int_p,  # l_int32 * ph
                              c_int_p,  # l_int32 * pspp
                              ),
        'pixWriteWebP': (c_int,
                         c_char_p,  # const char * filename
                         LPPix,  # PIX * pixs
                         c_int,  # l_int32 quality
                         c_int,  # l_int32 lossless
                         ),
        'pixWriteStreamWebP': (c_int,
                               LPFile,  # FILE * fp
                               LPPix,  # PIX * pixs
                               c_int,  # l_int32 quality
                               c_int,  # l_int32 lossless
                               ),
        'pixWriteMemWebP': (c_int,
                            POINTER(c_ubyte_p),  # l_uint8 ** pencdata
                            c_size_t_p,  # size_t * pencsize
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 quality
                            c_int,  # l_int32 lossless
                            ),
        'l_jpegSetQuality': (c_int,
                             c_int,  # l_int32 new_quality
                             ),
        'setLeptDebugOK': (None,
                           c_int,  # l_int32 allow
                           ),
        'pixaWriteFiles': (c_int,
                           c_char_p,  # const char * rootname
                           LPPixa,  # PIXA * pixa
                           c_int,  # l_int32 format
                           ),
        'pixWriteDebug': (c_int,
                          c_char_p,  # const char * fname
                          LPPix,  # PIX * pix
                          c_int,  # l_int32 format
                          ),
        'pixWrite': (c_int,
                     c_char_p,  # const char * fname
                     LPPix,  # PIX * pix
                     c_int,  # l_int32 format
                     ),
        'pixWriteAutoFormat': (c_int,
                               c_char_p,  # const char * filename
                               LPPix,  # PIX * pix
                               ),
        'pixWriteStream': (c_int,
                           LPFile,  # FILE * fp
                           LPPix,  # PIX * pix
                           c_int,  # l_int32 format
                           ),
        'pixWriteImpliedFormat': (c_int,
                                  c_char_p,  # const char * filename
                                  LPPix,  # PIX * pix
                                  c_int,  # l_int32 quality
                                  c_int,  # l_int32 progressive
                                  ),
        'pixChooseOutputFormat': (c_int,
                                  LPPix,  # PIX * pix
                                  ),
        'getImpliedFileFormat': (c_int,
                                 c_char_p,  # const char * filename
                                 ),
        'pixGetAutoFormat': (c_int,
                             LPPix,  # PIX * pix
                             c_int_p,  # l_int32 * pformat
                             ),
        'getFormatExtension': (c_char_p,
                               c_int,  # l_int32 format
                               ),
        'pixWriteMem': (c_int,
                        POINTER(c_ubyte_p),  # l_uint8 ** pdata
                        c_size_t_p,  # size_t * psize
                        LPPix,  # PIX * pix
                        c_int,  # l_int32 format
                        ),
        'l_fileDisplay': (c_int,
                          c_char_p,  # const char * fname
                          c_int,  # l_int32 x
                          c_int,  # l_int32 y
                          c_float,  # l_float32 scale
                          ),
        'pixDisplay': (c_int,
                       LPPix,  # PIX * pixs
                       c_int,  # l_int32 x
                       c_int,  # l_int32 y
                       ),
        'pixDisplayWithTitle': (c_int,
                                LPPix,  # PIX * pixs
                                c_int,  # l_int32 x
                                c_int,  # l_int32 y
                                c_char_p,  # const char * title
                                c_int,  # l_int32 dispflag
                                ),
        'pixMakeColorSquare': (LPPix,  # PIX *
                               c_uint,  # l_uint32 color
                               c_int,  # l_int32 size
                               c_int,  # l_int32 addlabel
                               c_int,  # l_int32 location
                               c_uint,  # l_uint32 textcolor
                               ),
        'l_chooseDisplayProg': (None,
                                c_int,  # l_int32 selection
                                ),
        'changeFormatForMissingLib': (None,
                                      c_int_p,  # l_int32 * pformat
                                      ),
        'pixDisplayWrite': (c_int,
                            LPPix,  # PIX * pixs
                            c_int,  # l_int32 reduction
                            ),
        'zlibCompress': (c_ubyte_p,
                         c_ubyte_p,  # const l_uint8 * datain
                         c_size_t,  # size_t nin
                         c_size_t_p,  # size_t * pnout
                         ),
        'zlibUncompress': (c_ubyte_p,
                           c_ubyte_p,  # const l_uint8 * datain
                           c_size_t,  # size_t nin
                           c_size_t_p,  # size_t * pnout
                           ),
    }

    def capi_lept_stderr(self, fmt: bytes, *args):
        self.lept_stderr.argtypes = [c_char_p] * (len(args) + 1)
        self.lept_stderr(fmt, *args)

    def capi_lept_roundftoi(self, fval: float) -> int:
        return self.lept_roundftoi(fval)

    def capi_lept_isPrime(
            self,
            n: int,
            pis_prime: c_int_p,
            pfactor: c_uint_p) -> int:
        return self.lept_isPrime(n, pis_prime, pfactor)

    def capi_lept_fopen(self, filename: bytes, mode: bytes) -> LPFile:
        return self.lept_fopen(filename, mode)

    def capi_lept_fclose(self, fp: LPFile) -> int:
        return self.lept_fclose(fp)

    def capi_lept_calloc(self, nmemb: int, size: int) -> c_void_p:
        return self.lept_calloc(nmemb, size)

    def capi_lept_free(self, ptr: c_void_p):
        self.lept_free(ptr)

    def capi_lept_mkdir(self, subdir: bytes) -> int:
        return self.lept_mkdir(subdir)

    def capi_lept_rmdir(self, subdir: bytes) -> int:
        return self.lept_rmdir(subdir)

    def capi_lept_direxists(self, dir: bytes, pexists: c_int_p):
        self.lept_direxists(dir, pexists)

    def capi_lept_rm_match(self, subdir: bytes, substr: bytes) -> int:
        return self.lept_rm_match(subdir, substr)

    def capi_lept_rm(self, subdir: bytes, tail: bytes) -> int:
        return self.lept_rm(subdir, tail)

    def capi_lept_rmfile(self, filepath: bytes) -> int:
        return self.lept_rmfile(filepath)

    def capi_lept_mv(
            self,
            srcfile: bytes,
            newdir: bytes,
            newtail: bytes,
            pnewpath: POINTER(POINTER(c_char))) -> int:
        return self.lept_mv(srcfile, newdir, newtail, pnewpath)

    def capi_lept_cp(
            self,
            srcfile: bytes,
            newdir: bytes,
            newtail: bytes,
            pnewpath: POINTER(POINTER(c_char))) -> int:
        return self.lept_cp(srcfile, newdir, newtail, pnewpath)

    def capi_pix_otsu_adaptive_threshold(
            self,
            pixs: LPPix,
            sx: int,
            sy: int,
            smoothx: int,
            smoothy: int,
            scorefract: float,
            ppixth: LPLPPix,
            ppixd: LPLPPix) -> int:
        return self.pixOtsuAdaptiveThreshold(
            pixs, sx, sy, smoothx, smoothy, scorefract, ppixth, ppixd)

    def capi_pix_sauvola_binarize_tiled(
            self,
            pixs: LPPix,
            whsize: int,
            factor: float,
            nx: int,
            ny: int,
            ppixth: LPLPPix,
            ppixd: LPLPPix) -> int:
        return self.pixSauvolaBinarizeTiled(
            pixs, whsize, factor, nx, ny, ppixth, ppixd)

    def capi_pix_reduce_rank_binary_cascade(
            self,
            pixs: LPPix,
            level1: int,
            level2: int,
            level3: int,
            level4: int) -> LPPix:
        return self.pixReduceRankBinaryCascade(
            pixs, level1, level2, level3, level4)

    def capi_pix_conn_comp(
            self,
            pixs: LPPix,
            ppixa: LPLPPixa,
            connectivity: int) -> LPBoxa:
        return self.pixConnComp(pixs, ppixa, connectivity)

    def capi_pix_count_conn_comp(
            self,
            pixs: LPPix,
            connectivity: int,
            pcount: c_int_p) -> int:
        return self.pixCountConnComp(pixs, connectivity, pcount)

    def capi_pix_blockconv(self, pix: LPPix, wc: int, hc: int) -> LPPix:
        return self.pixBlockconv(pix, wc, hc)

    def capi_pix_add_gaussian_noise(self, pixs: LPPix, stdev: float) -> LPPix:
        return self.pixAddGaussianNoise(pixs, stdev)

    def capi_pix_render_box_arb(
            self,
            pix: LPPix,
            box: LPBox,
            width: int,
            rval: int,
            gval: int,
            bval: int) -> int:
        return self.pixRenderBoxArb(pix, box, width, rval, gval, bval)

    def capi_pix_render_polyline(
            self,
            pix: LPPix,
            ptas: LPPta,
            width: int,
            op: int,
            closeflag: int) -> int:
        return self.pixRenderPolyline(pix, ptas, width, op, closeflag)

    def capi_pix_render_polyline_arb(
            self,
            pix: LPPix,
            ptas: LPPta,
            width: int,
            rval: int,
            gval: int,
            bval: int,
            closeflag: int) -> int:
        return self.pixRenderPolylineArb(
            pix, ptas, width, rval, gval, bval, closeflag)

    def capi_pix_erode_gray(
            self,
            pixs: LPPix,
            hsize: int,
            vsize: int) -> LPPix:
        return self.pixErodeGray(pixs, hsize, vsize)

    def capi_pix_threshold_to_binary(self, pixs: LPPix, thresh: int) -> LPPix:
        return self.pixThresholdToBinary(pixs, thresh)

    def capi_pix_write_jpeg(
            self,
            filename: bytes,
            pix: LPPix,
            quality: int,
            progressive: int) -> int:
        return self.pixWriteJpeg(filename, pix, quality, progressive)

    def capi_pix_dilate_brick(
            self,
            pixd: LPPix,
            pixs: LPPix,
            hsize: int,
            vsize: int) -> LPPix:
        return self.pixDilateBrick(pixd, pixs, hsize, vsize)

    def capi_pix_erode_brick(
            self,
            pixd: LPPix,
            pixs: LPPix,
            hsize: int,
            vsize: int) -> LPPix:
        return self.pixErodeBrick(pixd, pixs, hsize, vsize)

    def capi_pix_open_brick(
            self,
            pixd: LPPix,
            pixs: LPPix,
            hsize: int,
            vsize: int) -> LPPix:
        return self.pixOpenBrick(pixd, pixs, hsize, vsize)

    def capi_pix_close_brick(
            self,
            pixd: LPPix,
            pixs: LPPix,
            hsize: int,
            vsize: int) -> LPPix:
        return self.pixCloseBrick(pixd, pixs, hsize, vsize)

    def capi_pix_gen_halftone_mask(
            self,
            pixs: LPPix,
            ppixtext: LPLPPix,
            phtfound: c_int_p,
            debug: int) -> LPPix:
        return self.pixGenHalftoneMask(pixs, ppixtext, phtfound, debug)

    def capi_pix_generate_halftone_mask(
            self,
            pixs: LPPix,
            ppixtext: LPLPPix,
            phtfound: c_int_p,
            pixadb: LPPixa) -> LPPix:
        return self.pixGenerateHalftoneMask(pixs, ppixtext, phtfound, pixadb)

    def capi_pix_create(self, width: int, height: int, depth: int) -> LPPix:
        return self.pixCreate(width, height, depth)

    def capi_pix_create_no_init(self, width: int, height: int,
                                depth: int) -> LPPix:
        return self.pixCreateNoInit(width, height, depth)

    def capi_pix_create_template(self, pixs: LPPix) -> LPPix:
        return self.pixCreateTemplate(pixs)

    def capi_pix_create_template_no_init(self, pixs: LPPix) -> LPPix:
        return self.pixCreateTemplateNoInit(pixs)

    def capi_pix_create_header(
            self,
            width: int,
            height: int,
            depth: int) -> LPPix:
        return self.pixCreateHeader(width, height, depth)

    def capi_pix_clone(self, pixs: LPPix) -> LPPix:
        return self.pixClone(pixs)

    def capi_pix_destroy(self, ppix: LPLPPix):
        self.pixDestroy(ppix)

    def capi_pix_copy(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixCopy(pixd, pixs)

    def capi_pix_get_width(self, pix: LPPix) -> int:
        return self.pixGetWidth(pix)

    def capi_pix_get_height(self, pix: LPPix) -> int:
        return self.pixGetHeight(pix)

    def capi_pix_get_depth(self, pix: LPPix) -> int:
        return self.pixGetDepth(pix)

    def capi_pix_get_dimensions(
            self,
            pix: LPPix,
            pw: c_int_p,
            ph: c_int_p,
            pd: c_int_p) -> int:
        return self.pixGetDimensions(pix, pw, ph, pd)

    def capi_pix_get_spp(self, pix: LPPix) -> int:
        return self.pixGetSpp(pix)

    def capi_pix_set_spp(self, pix: LPPix, spp: int) -> int:
        return self.pixSetSpp(pix, spp)

    def capi_pix_get_wpl(self, pix: LPPix) -> int:
        return self.pixGetWpl(pix)

    def capi_pix_get_x_res(self, pix: LPPix) -> int:
        return self.pixGetXRes(pix)

    def capi_pix_set_x_res(self, pix: LPPix, res: int) -> int:
        return self.pixSetXRes(pix, res)

    def capi_pix_get_y_res(self, pix: LPPix) -> int:
        return self.pixGetYRes(pix)

    def capi_pix_set_y_res(self, pix: LPPix, res: int) -> int:
        return self.pixSetYRes(pix, res)

    def capi_pix_get_input_format(self, pix: LPPix) -> int:
        return self.pixGetInputFormat(pix)

    def capi_pix_set_text(self, pix: LPPix, textstring: bytes) -> int:
        return self.pixSetText(pix, textstring)

    def capi_pix_get_data(self, pix: LPPix) -> c_uint_p:
        return self.pixGetData(pix)

    def capi_pix_set_data(self, pix: LPPix, data: c_uint_p) -> int:
        return self.pixSetData(pix, data)

    def capi_pix_get_pixel(
            self,
            pix: LPPix,
            x: int,
            y: int,
            pval: c_uint_p) -> int:
        return self.pixGetPixel(pix, x, y, pval)

    def capi_pix_set_pixel(self, pix: LPPix, x: int, y: int, val: int) -> int:
        return self.pixSetPixel(pix, x, y, val)

    def capi_pix_set_all(self, pix: LPPix) -> int:
        return self.pixSetAll(pix)

    def capi_pix_set_all_arbitrary(self, pix: LPPix, val: int) -> int:
        return self.pixSetAllArbitrary(pix, val)

    def capi_pix_clear_in_rect(self, pix: LPPix, box: LPBox) -> int:
        return self.pixClearInRect(pix, box)

    def capi_pix_set_in_rect(self, pix: LPPix, box: LPBox) -> int:
        return self.pixSetInRect(pix, box)

    def capi_pix_set_or_clear_border(
            self,
            pixs: LPPix,
            left: int,
            right: int,
            top: int,
            bot: int,
            op: int) -> int:
        return self.pixSetOrClearBorder(pixs, left, right, top, bot, op)

    def capi_pix_add_border(self, pixs: LPPix, npix: int, val: int) -> LPPix:
        return self.pixAddBorder(pixs, npix, val)

    def capi_pix_set_masked(self, pixd: LPPix, pixm: LPPix, val: int) -> int:
        return self.pixSetMasked(pixd, pixm, val)

    def capi_pix_invert(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixInvert(pixd, pixs)

    def capi_pix_or(self, pixd: LPPix, pixs1: LPPix, pixs2: LPPix) -> LPPix:
        return self.pixOr(pixd, pixs1, pixs2)

    def capi_pix_and(self, pixd: LPPix, pixs1: LPPix, pixs2: LPPix) -> LPPix:
        return self.pixAnd(pixd, pixs1, pixs2)

    def capi_pix_xor(
            self,
            pixd: LPPix,
            pixs1: LPPix,
            pixs2: LPPix) -> LPPix:
        return self.pixXor(pixd, pixs1, pixs2)

    def capi_pix_subtract(
            self,
            pixd: LPPix,
            pixs1: LPPix,
            pixs2: LPPix) -> LPPix:
        return self.pixSubtract(pixd, pixs1, pixs2)

    def capi_pix_zero(self, pix: LPPix, pempty: c_int_p) -> int:
        return self.pixZero(pix, pempty)

    def capi_pix_foreground_fraction(
            self, pix: LPPix, pfract: c_float_p) -> int:
        return self.pixForegroundFraction(pix, pfract)

    def capi_pix_count_pixels(
            self,
            pixs: LPPix,
            pcount: c_int_p,
            tab8: c_int_p) -> int:
        return self.pixCountPixels(pixs, pcount, tab8)

    def capi_pix_count_pixels_by_row(self, pix: LPPix,
                                     tab8: c_int_p) -> LPNuma:
        return self.pixCountPixelsByRow(pix, tab8)

    def capi_pix_count_pixels_in_row(
            self,
            pix: LPPix,
            row: int,
            pcount: c_int_p,
            tab8: c_int_p) -> int:
        return self.pixCountPixelsInRow(pix, row, pcount, tab8)

    def capi_pix_clip_rectangle(
            self,
            pixs: LPPix,
            box: LPBox,
            pboxc: LPLPBox) -> LPPix:
        return self.pixClipRectangle(pixs, box, pboxc)

    def capi_pix_clip_box_to_foreground(
            self,
            pixs: LPPix,
            boxs: LPBox,
            ppixd: LPLPPix,
            pboxd: LPLPBox) -> int:
        return self.pixClipBoxToForeground(pixs, boxs, ppixd, pboxd)

    def capi_pix_convert_to8(self, pixs: LPPix, cmapflag: int) -> LPPix:
        return self.pixConvertTo8(pixs, cmapflag)

    def capi_pix_convert_to32(self, pixs: LPPix) -> LPPix:
        return self.pixConvertTo32(pixs)

    def capi_pix_convert24to32(self, pixs: LPPix) -> LPPix:
        return self.pixConvert24To32(pixs)

    def capi_pix_remove_alpha(self, pixs: LPPix) -> LPPix:
        return self.pixRemoveAlpha(pixs)

    def capi_pix_projective(
            self,
            pixs: LPPix,
            vc: c_float_p,
            incolor: int) -> LPPix:
        return self.pixProjective(pixs, vc, incolor)

    def capi_pix_read(self, filename: bytes) -> LPPix:
        return self.pixRead(filename)

    def capi_pix_read_mem(self, data: c_ubyte_p, size: int) -> LPPix:
        return self.pixReadMem(data, size)

    def capi_pix_rasterop(
            self,
            pixd: LPPix,
            dx: int,
            dy: int,
            dw: int,
            dh: int,
            op: int,
            pixs: LPPix,
            sx: int,
            sy: int) -> int:
        return self.pixRasterop(pixd, dx, dy, dw, dh, op, pixs, sx, sy)

    def capi_pix_rotate(
            self,
            pixs: LPPix,
            angle: float,
            type: int,
            incolor: int,
            width: int,
            height: int) -> LPPix:
        return self.pixRotate(pixs, angle, type, incolor, width, height)

    def capi_pix_rotate_orth(self, pixs: LPPix, quads: int) -> LPPix:
        return self.pixRotateOrth(pixs, quads)

    def capi_pix_rotate180(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixRotate180(pixd, pixs)

    def capi_pix_scale(
            self,
            pixs: LPPix,
            scalex: float,
            scaley: float) -> LPPix:
        return self.pixScale(pixs, scalex, scaley)

    def capi_pix_scale_to_size(self, pixs: LPPix, wd: int, hd: int) -> LPPix:
        return self.pixScaleToSize(pixs, wd, hd)

    def capi_pix_expand_replicate(self, pixs: LPPix, factor: int) -> LPPix:
        return self.pixExpandReplicate(pixs, factor)

    def capi_pix_seedfill_binary(
            self,
            pixd: LPPix,
            pixs: LPPix,
            pixm: LPPix,
            connectivity: int) -> LPPix:
        return self.pixSeedfillBinary(pixd, pixs, pixm, connectivity)

    def capi_pix_distance_function(
            self,
            pixs: LPPix,
            connectivity: int,
            outdepth: int,
            boundcond: int) -> LPPix:
        return self.pixDistanceFunction(
            pixs, connectivity, outdepth, boundcond)

    def capi_pix_read_tiff(self, filename: bytes, n: int) -> LPPix:
        return self.pixReadTiff(filename, n)

    def capi_pix_write_tiff(
            self,
            filename: bytes,
            pix: LPPix,
            comptype: int,
            modestr: bytes) -> int:
        return self.pixWriteTiff(filename, pix, comptype, modestr)

    def capi_pix_read_from_multipage_tiff(
            self, fname: bytes, poffset: c_size_t_p) -> LPPix:
        return self.pixReadFromMultipageTiff(fname, poffset)

    def capi_pix_read_mem_tiff(
            self,
            cdata: c_ubyte_p,
            size: int,
            n: int) -> LPPix:
        return self.pixReadMemTiff(cdata, size, n)

    def capi_pix_read_mem_from_multipage_tiff(
            self,
            cdata: c_ubyte_p,
            size: int,
            poffset: c_size_t_p) -> LPPix:
        return self.pixReadMemFromMultipageTiff(cdata, size, poffset)

    def capi_pix_write(self, fname: bytes, pix: LPPix, format: int) -> int:
        return self.pixWrite(fname, pix, format)

    def capi_pix_write_mem(
            self,
            pdata: POINTER(c_ubyte_p),
            psize: c_size_t_p,
            pix: LPPix,
            format: int) -> int:
        return self.pixWriteMem(pdata, psize, pix, format)

    def capi_get_leptonica_version(self) -> LP_c_char:
        return self.getLeptonicaVersion()


LEPTONICA_API = LeptCAPI(LEPT_DLL)


def test():
    ret = LEPTONICA_API
    print(ret.getLeptonicaVersion())


if __name__ == '__main__':
    test()
