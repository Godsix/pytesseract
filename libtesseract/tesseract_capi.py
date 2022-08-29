# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:43:58 2021

@author: 皓
"""
import os.path as osp
import logging
from enum import IntEnum
from functools import wraps
from ctypes import (POINTER, CDLL, CFUNCTYPE, c_float, c_void_p, c_int,
                    c_ubyte, c_char_p, c_bool, c_size_t, c_double,
                    cast)
from .common import TESS_DLL
from .leptonica_capi import Pix, Boxa, Pixa


def bytes_list(data):
    for item in data:
        if item is None:
            return
        yield item


def deprecated(name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            DeprecationWarning(f'capi {name} was deprecated in this version.')
            return func(*args, **kwargs)
        return wrapper
    return decorator


class OcrEngineMode(IntEnum):
    TESSERACT_ONLY = 0
    LSTM_ONLY = 1
    TESSERACT_LSTM_COMBINED = 2
    DEFAULT = 3


class PageSegMode(IntEnum):
    OSD_ONLY = 0
    AUTO_OSD = 1
    AUTO_ONLY = 2
    AUTO = 3
    SINGLE_COLUMN = 4
    SINGLE_BLOCK_VERT_TEXT = 5
    SINGLE_BLOCK = 6
    SINGLE_LINE = 7
    SINGLE_WORD = 8
    CIRCLE_WORD = 9
    SINGLE_CHAR = 10
    SPARSE_TEXT = 11
    SPARSE_TEXT_OSD = 12
    RAW_LINE = 13
    COUNT = 14


class PageIteratorLevel(IntEnum):
    BLOCK = 0
    PARA = 1
    TEXTLINE = 2
    WORD = 3
    SYMBOL = 4


class PolyBlockType(IntEnum):
    UNKNOWN = 0
    FLOWING_TEXT = 1
    HEADING_TEXT = 2
    PULLOUT_TEXT = 3
    EQUATION = 4
    INLINE_EQUATION = 5
    TABLE = 6
    VERTICAL_TEXT = 7
    CAPTION_TEXT = 8
    FLOWING_IMAGE = 9
    HEADING_IMAGE = 10
    PULLOUT_IMAGE = 11
    HORZ_LINE = 12
    VERT_LINE = 13
    NOISE = 14
    COUNT = 15


class Orientation(IntEnum):
    PAGE_UP = 0
    PAGE_RIGHT = 1
    PAGE_DOWN = 2
    PAGE_LEFT = 3


class ParagraphJustification(IntEnum):
    UNKNOWN = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3


class WritingDirection(IntEnum):
    DIRECTION_LEFT_TO_RIGHT = 0
    DIRECTION_RIGHT_TO_LEFT = 1
    DIRECTION_TOP_TO_BOTTOM = 2


class TextlineOrder(IntEnum):
    ORDER_LEFT_TO_RIGHT = 0
    ORDER_RIGHT_TO_LEFT = 1
    ORDER_TOP_TO_BOTTOM = 2


LPETEXT_DESC = c_void_p


LPPix = POINTER(Pix)
LPBoxa = POINTER(Boxa)
LPPixa = POINTER(Pixa)
LPLPPixa = POINTER(LPPixa)


TessCancelFunc = CFUNCTYPE(c_bool, c_void_p, c_int)
TessProgressFunc = CFUNCTYPE(c_bool, LPETEXT_DESC, c_int, c_int, c_int, c_int)


# class OSBestResult(Structure):
#     _fields_ = [
#         ("best_orientation_id", c_int),
#         ("best_script_id", c_int),
#         ("best_sconfidence", c_float),
#         ("best_oconfidence", c_float),
#     ]


# class OSResults(Structure):
#     _fields_ = [
#         ("orientations", c_float * 4),
#         ("scripts_na", c_float * 4 * (116 + 1 + 2 + 1)),
#         ("unicharset", c_void_p),
#         ("best_result", OSBestResult),
#         # # extra padding in case the structure is extended later
#         # ("padding", c_char * 512),
#     ]


class TesseractAPI:
    API = {
        # General free functions
        'TessVersion': (c_char_p, ),
        'TessDeleteText': (None, c_char_p),
        'TessDeleteTextArray': (None, POINTER(c_char_p)),
        'TessDeleteIntArray': (None, POINTER(c_int)),
        # Renderer API
        'TessTextRendererCreate': (c_void_p,
                                   c_char_p),  # const char* outputbase
        'TessHOcrRendererCreate': (c_void_p,
                                   c_char_p),  # const char* outputbase
        'TessHOcrRendererCreate2': (c_void_p,
                                    c_char_p,  # const char* outputbase
                                    c_bool),  # BOOL font_info
        'TessAltoRendererCreate': (c_void_p,
                                   c_char_p),  # const char* outputbase
        'TessTsvRendererCreate': (c_void_p,
                                  c_char_p),  # const char* outputbase
        'TessPDFRendererCreate': (c_void_p,
                                  c_char_p,  # const char* outputbase
                                  c_char_p,  # const char* datadir
                                  c_bool  # BOOL textonly
                                  ),
        'TessUnlvRendererCreate': (c_void_p,
                                   c_char_p),  # const char* outputbase
        'TessBoxTextRendererCreate': (c_void_p,
                                      c_char_p),  # const char* outputbase
        'TessLSTMBoxRendererCreate': (c_void_p,
                                      c_char_p),  # const char* outputbase
        'TessWordStrBoxRendererCreate': (c_void_p,
                                         c_char_p),  # const char* outputbase
        'TessDeleteResultRenderer': (None,
                                     # TessResultRenderer *renderer
                                     c_void_p
                                     ),
        'TessResultRendererInsert': (None,
                                     # TessResultRenderer *renderer
                                     c_void_p,
                                     # TessResultRenderer *next
                                     c_void_p),
        'TessResultRendererNext': (c_void_p,
                                   # TessResultRenderer *renderer
                                   c_void_p),
        'TessResultRendererBeginDocument': (c_bool,
                                            # TessResultRenderer* renderer
                                            c_void_p,
                                            # const char* title
                                            c_char_p
                                            ),
        'TessResultRendererAddImage': (c_bool,
                                       # TessResultRenderer* renderer
                                       c_void_p,
                                       # TessBaseAPI* api
                                       c_void_p
                                       ),
        'TessResultRendererEndDocument': (c_bool,
                                          # TessResultRenderer* renderer
                                          c_void_p
                                          ),
        'TessResultRendererExtention': (c_char_p,
                                        # TessResultRenderer *renderer
                                        c_void_p),
        'TessResultRendererTitle': (c_char_p,
                                    # TessResultRenderer *renderer
                                    c_void_p),
        'TessResultRendererImageNum': (c_int,
                                       # TessResultRenderer *renderer
                                       c_void_p),
        # Base API
        'TessBaseAPICreate': (c_void_p,  # TessBaseAPI*
                              ),
        'TessBaseAPIDelete': (None,
                              c_void_p),  # TessBaseAPI*
        'TessBaseAPIGetOpenCLDevice': (c_size_t,
                                       c_void_p,  # TessBaseAPI* handle
                                       POINTER(c_void_p)  # void **device
                                       ),
        'TessBaseAPISetInputName': (None,
                                    c_void_p,  # TessBaseAPI* handle
                                    c_char_p  # const char* name
                                    ),
        'TessBaseAPIGetInputName': (c_char_p,
                                    # TessResultRenderer* renderer
                                    c_void_p),
        'TessBaseAPISetInputImage': (None,
                                     c_void_p,  # TessResultRenderer* renderer
                                     LPPix),  # struct Pix *pix
        'TessBaseAPIGetInputImage': (LPPix,  # struct Pix *
                                     c_void_p),  # TessResultRenderer* renderer
        'TessBaseAPIGetSourceYResolution': (c_int, c_void_p),  # TessBaseAPI*
        'TessBaseAPIGetDatapath': (c_char_p, c_void_p),  # TessBaseAPI*
        'TessBaseAPISetOutputName': (None,
                                     c_void_p,  # TessBaseAPI*
                                     c_char_p,  # name
                                     ),
        'TessBaseAPISetVariable': (c_bool,
                                   c_void_p,  # TessBaseAPI*
                                   c_char_p,  # name
                                   c_char_p,  # value
                                   ),
        'TessBaseAPISetDebugVariable': (c_bool,
                                        c_void_p,  # TessBaseAPI*
                                        c_char_p,  # name
                                        c_char_p,  # value
                                        ),
        'TessBaseAPIGetIntVariable': (c_bool,
                                      c_void_p,  # TessBaseAPI*
                                      c_char_p,  # name
                                      POINTER(c_int),  # value
                                      ),
        'TessBaseAPIGetBoolVariable': (c_bool,
                                       c_void_p,  # TessBaseAPI*
                                       c_char_p,  # name
                                       POINTER(c_bool),  # value
                                       ),
        'TessBaseAPIGetDoubleVariable': (c_bool,
                                         c_void_p,  # TessBaseAPI*
                                         c_char_p,  # name
                                         POINTER(c_double),  # value
                                         ),
        'TessBaseAPIGetStringVariable': (c_char_p,
                                         c_void_p,  # TessBaseAPI*
                                         c_char_p,  # name
                                         ),
        'TessBaseAPIPrintVariables': (None,
                                      c_void_p,  # TessBaseAPI*
                                      c_void_p  # FILE *fp
                                      ),
        'TessBaseAPIPrintVariablesToFile': (c_bool,
                                            c_void_p,  # TessBaseAPI*
                                            c_char_p,  # filename
                                            ),
        'TessBaseAPIInit1': (c_int,
                             c_void_p,  # TessBaseAPI*
                             c_char_p,  # datapath
                             c_char_p,  # language
                             c_int,  # TessOcrEngineMode,oem
                             POINTER(c_char_p),  # configs
                             c_int),  # configs_size
        'TessBaseAPIInit2': (c_int,
                             c_void_p,  # TessBaseAPI*
                             c_char_p,  # datapath
                             c_char_p,  # language
                             c_int,  # TessOcrEngineMode,oem
                             ),
        'TessBaseAPIInit3': (c_int,
                             c_void_p,  # TessBaseAPI*
                             c_char_p,  # datapath
                             c_char_p,  # language
                             ),
        'TessBaseAPIInit4': (c_int,
                             c_void_p,  # TessBaseAPI*
                             c_char_p,  # datapath
                             c_char_p,  # language
                             c_int,  # TessOcrEngineMode,mode
                             POINTER(c_char_p),  # configs
                             c_int,  # configs_size
                             POINTER(c_char_p),  # vars_vec
                             POINTER(c_char_p),  # vars_values
                             c_size_t,  # vars_vec_size
                             c_bool  # set_only_non_debug_params
                             ),
        'TessBaseAPIGetInitLanguagesAsString': (c_char_p,
                                                c_void_p  # TessBaseAPI*
                                                ),
        'TessBaseAPIGetLoadedLanguagesAsVector': (POINTER(c_char_p),
                                                  c_void_p  # TessBaseAPI*
                                                  ),
        'TessBaseAPIGetAvailableLanguagesAsVector': (POINTER(c_char_p),
                                                     c_void_p  # TessBaseAPI*
                                                     ),
        'TessBaseAPIInitLangMod': (c_int,
                                   c_void_p,  # TessBaseAPI* handle
                                   c_char_p,  # const char * datapath
                                   c_char_p,  # const char * language
                                   ),
        'TessBaseAPIInitForAnalysePage': (None,
                                          c_void_p,  # TessBaseAPI*
                                          ),
        'TessBaseAPIReadConfigFile': (None,
                                      c_void_p,  # TessBaseAPI*
                                      c_char_p,  # filename
                                      ),
        'TessBaseAPIReadDebugConfigFile': (None,
                                           c_void_p,  # TessBaseAPI*
                                           c_char_p,  # filename
                                           ),
        'TessBaseAPISetPageSegMode': (None,
                                      c_void_p,  # TessBaseAPI*
                                      c_int,  # See PageSegMode
                                      ),
        'TessBaseAPIGetPageSegMode': (c_int,
                                      c_void_p,  # TessBaseAPI*
                                      ),
        'TessBaseAPIRect': (c_char_p,
                            c_void_p,  # TessBaseAPI*
                            POINTER(c_ubyte),  # imagedata
                            c_int,  # bytes_per_pixel
                            c_int,  # bytes_per_line
                            c_int,  # left
                            c_int,  # top
                            c_int,  # width
                            c_int,  # height
                            ),
        'TessBaseAPIClearAdaptiveClassifier': (None,
                                               c_void_p,  # TessBaseAPI*
                                               ),
        'TessBaseAPISetImage': (None,
                                c_void_p,  # TessBaseAPI*
                                POINTER(c_ubyte),  # imagedata
                                c_int,  # width
                                c_int,  # height
                                c_int,  # bytes_per_pixel
                                c_int,  # bytes_per_line
                                ),
        'TessBaseAPISetImage2': (None,
                                 c_void_p,  # TessBaseAPI*
                                 LPPix,  # struct Pix * pix
                                 ),
        'TessBaseAPISetSourceResolution': (None,
                                           c_void_p,  # TessBaseAPI*
                                           c_int,     # PPI
                                           ),
        'TessBaseAPISetRectangle': (None,
                                    c_void_p,  # TessBaseAPI*
                                    c_int,     # left
                                    c_int,     # top
                                    c_int,     # width
                                    c_int,     # height
                                    ),
        'TessBaseAPIGetThresholdedImage': (LPPix,  # struct Pix *
                                           c_void_p,  # TessBaseAPI*
                                           ),
        'TessBaseAPIGetRegions': (LPBoxa,  # struct Boxa *
                                  c_void_p,  # TessBaseAPI*
                                  LPLPPixa  # struct Pixa **pixa
                                  ),
        'TessBaseAPIGetTextlines': (LPBoxa,  # struct Boxa *
                                    c_void_p,  # TessBaseAPI*
                                    # struct Pixa **pixa
                                    LPLPPixa,
                                    POINTER(POINTER(c_int)),  # blockids
                                    ),
        'TessBaseAPIGetTextlines1': (LPBoxa,  # struct Boxa *
                                     c_void_p,  # TessBaseAPI*
                                     c_bool,  # raw_image
                                     c_int,  # raw_image
                                     # struct Pixa **pixa
                                     LPLPPixa,
                                     POINTER(POINTER(c_int)),  # blockids
                                     POINTER(POINTER(c_int))  # paraids
                                     ),
        'TessBaseAPIGetStrips': (LPBoxa,  # struct Boxa *
                                 c_void_p,  # TessBaseAPI*
                                 LPLPPixa,  # struct Pixa * * pixa
                                 POINTER(POINTER(c_int))  # blockids
                                 ),
        'TessBaseAPIGetWords': (LPBoxa,  # struct Boxa *
                                c_void_p,  # TessBaseAPI*
                                LPLPPixa,  # struct Pixa * * pixa
                                ),
        'TessBaseAPIGetConnectedComponents': (LPBoxa,  # struct Boxa *
                                              c_void_p,  # TessBaseAPI*
                                              # struct Pixa **cc
                                              LPLPPixa,  # struct Pixa * * cc
                                              ),
        'TessBaseAPIGetComponentImages': (LPBoxa,  # struct Boxa *
                                          c_void_p,  # TessBaseAPI*
                                          c_int,  # TessPageIteratorLevel level
                                          c_bool,  # text_only
                                          # struct Pixa **pixa
                                          LPLPPixa,
                                          POINTER(POINTER(c_int))  # blockids
                                          ),
        'TessBaseAPIGetComponentImages1': (LPBoxa,  # struct Boxa *
                                           c_void_p,  # TessBaseAPI*
                                           c_int,  # PageIteratorLevel level
                                           c_bool,  # text_only
                                           c_bool,  # raw_image
                                           c_int,  # raw_image
                                           # struct Pixa **pixa
                                           LPLPPixa,
                                           POINTER(POINTER(c_int)),  # blockids
                                           POINTER(POINTER(c_int))  # paraids
                                           ),
        'TessBaseAPIGetThresholdedImageScaleFactor': (c_int,
                                                      c_void_p,  # TessBaseAPI*
                                                      ),
        'TessBaseAPIAnalyseLayout': (c_void_p,  # TessPageIterator*
                                     c_void_p,  # TessBaseAPI*
                                     ),
        'TessBaseAPIRecognize': (c_int,
                                 c_void_p,  # TessBaseAPI*
                                 c_void_p,  # ETEXT_DESC*
                                 ),
        'TessBaseAPIProcessPages': (c_bool,
                                    c_void_p,  # TessBaseAPI*
                                    c_char_p,  # filename
                                    c_char_p,  # retry_config
                                    c_int,  # timeout_millisec
                                    c_void_p,  # TessResultRenderer *
                                    ),
        'TessBaseAPIProcessPage': (c_bool,
                                   c_void_p,  # TessBaseAPI*
                                   LPPix,  # struct Pix *pix
                                   c_int,  # page_index
                                   c_char_p,  # filename
                                   c_char_p,  # retry_config
                                   c_int,  # timeout_millisec
                                   c_void_p,  # TessResultRenderer *
                                   ),
        'TessBaseAPIGetIterator': (c_void_p,  # TessResultIterator
                                   c_void_p,  # TessBaseAPI*
                                   ),
        'TessBaseAPIGetMutableIterator': (c_void_p,  # TessMutableIterator
                                          c_void_p,  # TessBaseAPI*
                                          ),
        'TessBaseAPIGetUTF8Text': (c_char_p,
                                   c_void_p,  # TessBaseAPI * handle
                                   ),
        'TessBaseAPIGetHOCRText': (c_char_p,
                                   c_void_p,  # TessBaseAPI*
                                   c_int,  # page_number
                                   ),
        'TessBaseAPIGetAltoText': (c_char_p,
                                   c_void_p,  # TessBaseAPI*
                                   c_int,  # page_number
                                   ),
        'TessBaseAPIGetTsvText': (c_char_p,
                                  c_void_p,  # TessBaseAPI*
                                  c_int,  # page_number
                                  ),
        'TessBaseAPIGetBoxText': (c_char_p,
                                  c_void_p,  # TessBaseAPI*
                                  c_int,  # page_number
                                  ),
        'TessBaseAPIGetLSTMBoxText': (c_char_p,
                                      c_void_p,  # TessBaseAPI*
                                      c_int,  # page_number
                                      ),
        'TessBaseAPIGetWordStrBoxText': (c_char_p,
                                         c_void_p,  # TessBaseAPI*
                                         c_int,  # page_number
                                         ),
        'TessBaseAPIGetUNLVText': (c_char_p,
                                   c_void_p,  # TessBaseAPI*
                                   ),
        'TessBaseAPIMeanTextConf': (c_int,
                                    c_void_p,  # TessBaseAPI*
                                    ),
        'TessBaseAPIAllWordConfidences': (POINTER(c_int),
                                          c_void_p,  # TessBaseAPI*
                                          ),
        'TessBaseAPIAdaptToWordStr': (c_bool,
                                      c_void_p,  # TessBaseAPI*
                                      c_int,  # TessPageSegMode(mode)
                                      c_char_p,  # wordstr
                                      ),
        'TessBaseAPIClear': (None,
                             c_void_p,  # TessBaseAPI*
                             ),
        'TessBaseAPIEnd': (None,
                           c_void_p,  # TessBaseAPI*
                           ),
        'TessBaseAPIIsValidWord': (c_int,
                                   c_void_p,  # TessBaseAPI*
                                   c_char_p,  # word
                                   ),
        'TessBaseAPIGetTextDirection': (c_bool,
                                        c_void_p,  # TessBaseAPI*
                                        POINTER(c_int),  # out_offset
                                        POINTER(c_float),  # out_slope
                                        ),
        'TessBaseAPIGetUnichar': (c_char_p,
                                  c_void_p,  # TessBaseAPI*
                                  c_int  # unichar_id
                                  ),
        'TessBaseAPIClearPersistentCache': (None,
                                            c_void_p,  # TessBaseAPI*
                                            ),
        'TessBaseAPIDetectOrientationScript': (c_bool,
                                               c_void_p,  # TessBaseAPI*
                                               POINTER(c_int),  # orient_deg
                                               POINTER(c_float),  # orient_conf
                                               # script_name
                                               POINTER(c_char_p),
                                               POINTER(c_float),  # script_conf
                                               ),
        # 'TessBaseAPIDetectOS': (c_bool,
        #                         c_void_p,  # TessBaseAPI*
        #                         POINTER(OSResults),
        #                         ),
        'TessBaseAPISetMinOrientationMargin': (None,
                                               c_void_p,  # TessBaseAPI*
                                               c_double,  # margin
                                               ),
        'TessBaseAPINumDawgs': (c_int,
                                c_void_p,  # TessBaseAPI*
                                ),
        'TessBaseAPIOem': (c_int,  # TessOcrEngineMode
                           c_void_p,  # TessBaseAPI*
                           ),
        'TessBaseGetBlockTextOrientations': (None,
                                             c_void_p,  # TessBaseAPI*
                                             # block_orientation
                                             POINTER(POINTER(c_int)),
                                             # vertical_writing
                                             POINTER(POINTER(c_bool)),
                                             ),
        # Page iterator
        'TessPageIteratorDelete': (None,
                                   c_void_p,  # TessPageIterator*
                                   ),
        'TessPageIteratorCopy': (c_void_p,  # TessPageIterator*
                                 c_void_p,  # TessPageIterator*
                                 ),
        'TessPageIteratorBegin': (None,
                                  c_void_p,  # TessPageIterator*
                                  ),
        'TessPageIteratorNext': (c_bool,
                                 c_void_p,  # TessPageIterator*
                                 c_int,  # TessPageIteratorLevel
                                 ),
        'TessPageIteratorIsAtBeginningOf': (c_bool,
                                            c_void_p,  # TessPageIterator*
                                            c_int,  # TessPageIteratorLevel
                                            ),
        'TessPageIteratorIsAtFinalElement': (c_bool,
                                             c_void_p,  # TessPageIterator*
                                             # TessPageIteratorLevel (level)
                                             c_int,
                                             # TessPageIteratorLevel (element)
                                             c_int,
                                             ),
        'TessPageIteratorBoundingBox': (c_bool,
                                        c_void_p,  # TessPageIterator*
                                        c_int,  # TessPageIteratorLevel (level)
                                        POINTER(c_int),  # left
                                        POINTER(c_int),  # top
                                        POINTER(c_int),  # right
                                        POINTER(c_int),  # bottom
                                        ),
        'TessPageIteratorBlockType': (c_int,  # PolyBlockType
                                      c_void_p,  # TessPageIterator*
                                      ),
        'TessPageIteratorGetBinaryImage': (LPPix,
                                           c_void_p,  # TessPageIterator*
                                           c_int,  # PageIteratorLevel level
                                           ),
        'TessPageIteratorGetImage': (LPPix,
                                     c_void_p,  # TessPageIterator*
                                     c_int,  # PageIteratorLevel level
                                     c_int,  # padding,
                                     LPPix,  # original_image,
                                     POINTER(c_int),
                                     POINTER(c_int)
                                     ),
        'TessPageIteratorBaseline': (c_bool,
                                     c_void_p,  # TessPageIterator*
                                     c_int,  # TessPageIteratorLevel (level)
                                     POINTER(c_int),  # x1
                                     POINTER(c_int),  # y1
                                     POINTER(c_int),  # x2
                                     POINTER(c_int),  # y2
                                     ),
        'TessPageIteratorOrientation': (None,
                                        c_void_p,  # TessPageIterator*
                                        POINTER(c_int),  # TessOrientation*
                                        # TessWritingDirection*
                                        POINTER(c_int),
                                        POINTER(c_int),  # TessTextlineOrder*
                                        POINTER(c_float),  # deskew_angle
                                        ),
        'TessPageIteratorParagraphInfo': (None,
                                          c_void_p,  # TessPageIterator*
                                          # TessParagraphJustification*
                                          POINTER(c_int),
                                          POINTER(c_bool),  # is_list_item
                                          POINTER(c_bool),  # is_crown
                                          POINTER(c_int),  # first_line_indent
                                          ),
        # Result iterator
        'TessResultIteratorDelete': (None,
                                     # TessResultIterator*
                                     c_void_p,
                                     ),
        'TessResultIteratorCopy': (c_void_p,  # TessResultIterator *,
                                   # TessResultIterator*
                                   c_void_p,
                                   ),
        'TessResultIteratorGetPageIterator': (
            c_void_p,  # TessPageIterator*
            c_void_p,  # TessResultIterator*
        ),
        'TessResultIteratorGetPageIteratorConst': (
            # const TessPageIterator *
            c_void_p,
            # TessResultIterator*
            c_void_p,
        ),
        'TessResultIteratorGetChoiceIterator': (
            c_void_p,  # TessChoiceIterator *
            # TessResultIterator*
            c_void_p,
        ),
        'TessResultIteratorNext': (c_bool,
                                   c_void_p,  # TessResultIterator*
                                   # TessPageIteratorLevel (level)
                                   c_int,
                                   ),
        'TessResultIteratorGetUTF8Text': (c_char_p,
                                          c_void_p,  # TessResultIterator*
                                          # TessPageIteratorLevel (level)
                                          c_int,
                                          ),
        'TessResultIteratorConfidence': (c_float,
                                         c_void_p,  # TessResultIterator*
                                         # TessPageIteratorLevel (level)
                                         c_int,
                                         ),
        'TessResultIteratorWordRecognitionLanguage': (c_char_p,
                                                      # TessResultIterator*
                                                      c_void_p,
                                                      ),
        'TessResultIteratorWordFontAttributes': (
            c_char_p,
            c_void_p,  # TessResultIterator*
            POINTER(c_bool),  # is_bold
            POINTER(c_bool),  # is_italic
            POINTER(c_bool),  # is_underlined
            POINTER(c_bool),  # is_monospace
            POINTER(c_bool),  # is_serif
            POINTER(c_bool),  # is_smallcaps
            POINTER(c_int),  # pointsize
            POINTER(c_int),  # font_id
        ),
        'TessResultIteratorWordIsFromDictionary': (c_bool,
                                                   # TessResultIterator*
                                                   c_void_p,
                                                   ),
        'TessResultIteratorWordIsNumeric': (c_bool,
                                            c_void_p,  # TessResultIterator*
                                            ),
        'TessResultIteratorSymbolIsSuperscript': (c_bool,
                                                  # TessResultIterator*
                                                  c_void_p,
                                                  ),
        'TessResultIteratorSymbolIsSubscript': (c_bool,
                                                # TessResultIterator*
                                                c_void_p,
                                                ),
        'TessResultIteratorSymbolIsDropcap': (c_bool,
                                              c_void_p,  # TessResultIterator*
                                              ),
        'TessChoiceIteratorDelete': (None,
                                     c_void_p,  # TessChoiceIterator*
                                     ),
        'TessChoiceIteratorNext': (c_bool,
                                   c_void_p,  # TessChoiceIterator*
                                   ),
        'TessChoiceIteratorGetUTF8Text': (c_char_p,
                                          c_void_p,  # TessChoiceIterator*
                                          ),
        'TessChoiceIteratorConfidence': (c_float,
                                         c_void_p,  # TessChoiceIterator*
                                         ),
        # Progress monitor
        'TessMonitorCreate': (
            LPETEXT_DESC,  # ETEXT_DESC*
        ),
        'TessMonitorDelete': (None,
                              LPETEXT_DESC,  # ETEXT_DESC*
                              ),
        'TessMonitorSetCancelFunc': (None,
                                     LPETEXT_DESC,  # ETEXT_DESC*
                                     # TessCancelFunc cancelFunc
                                     TessCancelFunc,
                                     ),
        'TessMonitorSetCancelThis': (None,
                                     LPETEXT_DESC,  # ETEXT_DESC*
                                     c_void_p,  # cancelThis
                                     ),
        'TessMonitorGetCancelThis': (c_void_p,
                                     LPETEXT_DESC,  # ETEXT_DESC*
                                     ),
        'TessMonitorSetProgressFunc': (None,
                                       LPETEXT_DESC,  # ETEXT_DESC*
                                       # TessProgressFunc progressFunc
                                       TessProgressFunc,
                                       ),
        'TessMonitorGetProgress': (c_int,
                                   LPETEXT_DESC,  # ETEXT_DESC*
                                   ),
        'TessMonitorSetDeadlineMSecs': (None,
                                        LPETEXT_DESC,  # ETEXT_DESC*
                                        c_int,  # deadline
                                        ),
    }

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
        for name, types in self.API.items():
            self.func_ptr_init(name, *types)

    def func_ptr_init(self, name, restype, *argtypes):
        if not hasattr(self.dll, name):
            self.logger.error('The tesseract capi do not contain %s', name)
            return
        func = getattr(self.dll, name)
        func.restype = restype
        func.argtypes = argtypes

    def __getattr__(self, attr):
        if hasattr(self.dll, attr):
            return getattr(self.dll, attr)
        raise AttributeError(
            "'{}' object has no attribute '{}'".format(self.__class__.__name__,
                                                       attr))

    def is_available(self):
        return self.dll is not None
    # General free functions

    def capi_version(self) -> bytes:
        return self.TessVersion()

    def capi_delete_text(self, text: bytes):
        self.TessDeleteText(text)

    def capi_delete_text_array(self, arr: bytes):
        self.TessDeleteTextArray(arr)

    def capi_delete_int_array(self, arr: int):
        self.TessDeleteIntArray(arr)

    # Renderer API
    def capi_text_renderer_create(self, outputbase: bytes):
        return self.TessTextRendererCreate(outputbase)

    def capi_hocr_renderer_create(self, outputbase: bytes):
        return self.TessHOcrRendererCreate(outputbase)

    def capi_hocr_renderer_create2(self, outputbase: bytes, font_info: bool):
        return self.TessHOcrRendererCreate2(outputbase, font_info)

    def capi_alto_renderer_create(self, outputbase: bytes):
        return self.TessAltoRendererCreate(outputbase)

    def capi_tsv_renderer_create(self, outputbase: bytes):
        return self.TessTsvRendererCreate(outputbase)

    def capi_pdf_renderer_create(self, outputbase: bytes, datadir: bytes,
                                 textonly: bool):
        return self.TessPDFRendererCreate(outputbase, datadir, textonly)

    def capi_unlv_renderer_create(self, outputbase: bytes):
        return self.TessUnlvRendererCreate(outputbase)

    def capi_box_text_renderer_create(self, outputbase: bytes):
        return self.TessBoxTextRendererCreate(outputbase)

    def capi_lstm_box_renderer_create(self, outputbase: bytes):
        return self.TessLSTMBoxRendererCreate(outputbase)

    def capi_word_str_box_renderer_create(self, outputbase: bytes):
        return self.TessWordStrBoxRendererCreate(outputbase)

    def capi_delete_result_renderer(self, renderer):
        self.TessDeleteResultRenderer(renderer)

    def capi_result_renderer_insert(self, renderer, next):
        self.TessResultRendererInsert(renderer, next)

    def capi_result_renderer_next(self, renderer):
        return self.TessResultRendererNext(renderer)

    def capi_result_renderer_begin_document(self, renderer,
                                            title: bytes) -> bool:
        return self.TessResultRendererBeginDocument(renderer, title)

    def capi_result_renderer_add_image(self, renderer, api) -> bool:
        return self.TessResultRendererAddImage(renderer, api)

    def capi_result_renderer_end_document(self, renderer) -> bool:
        return self.TessResultRendererEndDocument(renderer)

    def capi_result_renderer_extention(self, renderer) -> bytes:
        return self.TessResultRendererExtention(renderer)

    def capi_result_renderer_title(self, renderer) -> bytes:
        return self.TessResultRendererTitle(renderer)

    def capi_result_renderer_image_num(self, renderer) -> int:
        return self.TessResultRendererImageNum(renderer)

    # Base API

    def capi_base_api_create(self):
        return self.TessBaseAPICreate()

    def capi_base_api_delete(self, handle):
        self.TessBaseAPIDelete(handle)

    def capi_base_api_get_open_cldevice(self, handle, device) -> int:
        return self.TessBaseAPIGetOpenCLDevice(handle, device)

    def capi_base_api_set_input_name(self, handle, name: bytes):
        self.TessBaseAPISetInputName(handle, name)

    def capi_base_api_get_input_name(self, handle) -> bytes:
        return self.TessBaseAPIGetInputName(handle)

    def capi_base_api_set_input_image(self, handle, pix):
        self.TessBaseAPISetInputImage(handle, pix)

    def capi_base_api_get_input_image(self, handle):
        return self.TessBaseAPIGetInputImage(handle)

    def capi_base_api_get_source_y_resolution(self, handle) -> int:
        return self.TessBaseAPIGetSourceYResolution(handle)

    def capi_base_api_get_datapath(self, handle) -> bytes:
        return self.TessBaseAPIGetDatapath(handle)

    def capi_base_api_set_output_name(self, handle, name: bytes):
        self.TessBaseAPISetOutputName(handle, name)

    def capi_base_api_set_variable(self, handle, name: bytes,
                                   value: bytes) -> bool:
        return self.TessBaseAPISetVariable(handle, name, value)

    def capi_base_api_set_debug_variable(self, handle, name: bytes,
                                         value: bytes) -> bool:
        return self.TessBaseAPISetDebugVariable(handle, name, value)

    def capi_base_api_get_int_variable(self, handle, name: bytes,
                                       value: int) -> bool:
        return self.TessBaseAPIGetIntVariable(handle, name, value)

    def capi_base_api_get_bool_variable(self, handle, name: bytes,
                                        value: bool) -> bool:
        return self.TessBaseAPIGetBoolVariable(handle, name, value)

    def capi_base_api_get_double_variable(self, handle, name: bytes,
                                          value: float) -> bool:
        return self.TessBaseAPIGetDoubleVariable(handle, name, value)

    def capi_base_api_get_string_variable(self, handle, name: bytes) -> bytes:
        return self.TessBaseAPIGetStringVariable(handle, name)

    def capi_base_api_print_variables(self, handle, fp):
        self.TessBaseAPIPrintVariables(handle, fp)

    def capi_base_api_print_variables_tofile(self, handle,
                                             filename: bytes) -> bool:
        return self.TessBaseAPIPrintVariablesToFile(handle, filename)

    def capi_base_api_init1(self, handle, datapath: bytes, language: bytes,
                            oem: OcrEngineMode, configs: bytes,
                            configs_size: int) -> int:
        return self.TessBaseAPIInit1(handle, datapath, language, oem,
                                     configs, configs_size)

    def capi_base_api_init2(self, handle, datapath: bytes, language: bytes,
                            oem: OcrEngineMode) -> int:
        return self.TessBaseAPIInit2(handle, datapath, language, oem)

    def capi_base_api_init3(self,
                            handle,
                            datapath: bytes,
                            language: bytes) -> int:
        return self.TessBaseAPIInit3(handle, datapath, language)

    def capi_base_api_init4(self, handle, datapath: bytes, language: bytes,
                            mode: OcrEngineMode,
                            configs: bytes,
                            configs_size: int,
                            vars_vec: bytes,
                            vars_values: bytes,
                            vars_vec_size: int,
                            set_only_non_debug_params: bool) -> int:
        return self.TessBaseAPIInit4(handle, datapath, language, mode, configs,
                                     configs_size, vars_vec, vars_values,
                                     vars_vec_size, set_only_non_debug_params)

    def capi_base_api_get_init_languages(self, handle) -> bytes:
        return self.TessBaseAPIGetInitLanguagesAsString(handle)

    def capi_base_api_get_loaded_languages(self, handle) -> list[bytes]:
        ret = self.TessBaseAPIGetLoadedLanguagesAsVector(handle)
        return list(bytes_list(ret))

    def capi_base_api_get_available_languages(self, handle) -> list[bytes]:
        ret = self.TessBaseAPIGetAvailableLanguagesAsVector(handle)
        return list(bytes_list(ret))

    def capi_base_api_init_lang_mod(self, handle, datapath: bytes,
                                    language: bytes) -> int:
        return self.TessBaseAPIInitLangMod(handle, datapath, language)

    def capi_base_api_init_for_analyse_page(self, handle):
        self.TessBaseAPIInitForAnalysePage(handle)

    def capi_base_api_read_config_file(self, handle, filename: bytes):
        self.TessBaseAPIReadConfigFile(handle, filename)

    def capi_base_api_read_debug_config_file(self, handle, filename: bytes):
        self.TessBaseAPIReadDebugConfigFile(handle, filename)

    def capi_base_api_set_page_seg_mode(self, handle, mode: PageSegMode):
        self.TessBaseAPISetPageSegMode(handle, mode)

    def capi_base_api_get_page_seg_mode(self, handle) -> int:
        return self.TessBaseAPIGetPageSegMode(handle)

    def capi_base_api_rect(self, handle, imagedata: bytes,
                           bytes_per_pixel: int,
                           bytes_per_line: int,
                           left: int,
                           top: int,
                           width: int,
                           height: int) -> bytes:
        return self.TessBaseAPIRect(handle, imagedata,
                                    bytes_per_pixel, bytes_per_line,
                                    left, top,
                                    width, height)

    def capi_base_api_clear_adaptive_classifier(self, handle):
        self.TessBaseAPIClearAdaptiveClassifier(handle)

    def capi_base_api_set_image(self, handle, imagedata: bytes,
                                width: int,
                                height: int,
                                bytes_per_pixel: int,
                                bytes_per_line: int):
        data = cast(imagedata, POINTER(c_ubyte))
        self.TessBaseAPISetImage(handle, data,
                                 width, height,
                                 bytes_per_pixel, bytes_per_line)

    def capi_base_api_set_image2(self, handle, pix: POINTER(Pix)):
        self.TessBaseAPISetImage2(handle, pix)

    def capi_base_api_set_source_resolution(self, handle, ppi: int):
        self.TessBaseAPISetSourceResolution(handle, ppi)

    def capi_base_api_set_rectangle(self, handle,
                                    left: int, top: int,
                                    width: int, height: int):
        self.TessBaseAPISetRectangle(handle, left, top, width, height)

    def capi_base_api_get_thresholded_image(self, handle):
        return self.TessBaseAPIGetThresholdedImage(handle)

    def capi_base_api_get_regions(self, handle, pixa):
        return self.TessBaseAPIGetRegions(handle, pixa)

    def capi_base_api_get_textlines(self, handle, pixa, blockids: int):
        return self.TessBaseAPIGetTextlines(handle, pixa, blockids)

    def capi_base_api_get_textlines1(self, handle,
                                     raw_image: bool, raw_padding: int,
                                     pixa, blockids: int, paraids: int):
        return self.TessBaseAPIGetTextlines1(handle, raw_image, raw_padding,
                                             pixa, blockids, paraids)

    def capi_base_api_get_strips(self, handle, pixa, blockids: int):
        return self.TessBaseAPIGetStrips(handle, pixa, blockids)

    def capi_base_api_get_words(self, handle, pixa):
        return self.TessBaseAPIGetWords(handle, pixa)

    def capi_base_api_get_connected_components(self, handle, cc):
        return self.TessBaseAPIGetConnectedComponents(handle, cc)

    def capi_base_api_get_component_images(self, handle,
                                           level: PageIteratorLevel,
                                           text_only: bool,
                                           pixa, blockids: int):
        return self.TessBaseAPIGetComponentImages(handle, level, text_only,
                                                  pixa, blockids)

    def capi_base_api_get_component_images1(self, handle,
                                            level: PageIteratorLevel,
                                            text_only: bool, raw_image: bool,
                                            raw_padding: int,
                                            pixa, blockids: int,
                                            paraids: int):
        return self.TessBaseAPIGetComponentImages1(handle, level, text_only,
                                                   raw_image, raw_padding,
                                                   pixa, blockids, paraids)

    def capi_base_api_get_thresholded_image_scale_factor(self):
        return self.TessBaseAPIGetThresholdedImageScaleFactor()

    def capi_base_api_analyse_layout(self):
        return self.TessBaseAPIAnalyseLayout()

    def capi_base_api_recognize(self, handle, monitor):
        return self.TessBaseAPIRecognize(handle, monitor)

    def capi_base_api_process_pages(self, handle,
                                    filename: bytes,
                                    retry_config: bytes,
                                    timeout_millisec: int,
                                    renderer) -> bool:
        return self.TessBaseAPIProcessPages(handle, filename, retry_config,
                                            timeout_millisec, renderer)

    def capi_base_api_process_page(self, handle, pix, page_index: int,
                                   filename: bytes, retry_config: bytes,
                                   timeout_millisec: int, renderer) -> bool:
        return self.TessBaseAPIProcessPage(handle, pix, page_index,
                                           filename, retry_config,
                                           timeout_millisec, renderer)

    def capi_base_api_get_iterator(self, handle):
        return self.TessBaseAPIGetIterator(handle)

    def capi_base_api_get_mutable_iterator(self, handle):
        return self.TessBaseAPIGetMutableIterator(handle)

    def capi_base_api_get_utf8_text(self, handle) -> bytes:
        return self.TessBaseAPIGetUTF8Text(handle)

    def capi_base_api_get_hocr_text(self, handle, page_number: int) -> bytes:
        return self.TessBaseAPIGetHOCRText(handle,
                                           page_number)

    def capi_base_api_get_alto_text(self, handle, page_number: int) -> bytes:
        return self.TessBaseAPIGetAltoText(handle,
                                           page_number)

    def capi_base_api_get_tsv_text(self, handle, page_number: int) -> bytes:
        return self.TessBaseAPIGetTsvText(handle,
                                          page_number)

    def capi_base_api_get_box_text(self, handle, page_number: int) -> bytes:
        return self.TessBaseAPIGetBoxText(handle,
                                          page_number)

    def capi_base_api_get_lstm_box_text(self, handle,
                                        page_number: int) -> bytes:
        return self.TessBaseAPIGetLSTMBoxText(handle,
                                              page_number)

    def capi_base_api_get_word_str_box_text(self, handle,
                                            page_number: int) -> bytes:
        return self.TessBaseAPIGetWordStrBoxText(handle,
                                                 page_number)

    def capi_base_api_get_unlv_text(self, handle) -> bytes:
        return self.TessBaseAPIGetUNLVText(handle)

    def capi_base_api_mean_text_conf(self, handle) -> int:
        return self.TessBaseAPIMeanTextConf(handle)

    def capi_base_api_all_word_confidences(self, handle) -> int:
        return self.TessBaseAPIAllWordConfidences(handle)

    def capi_base_api_adapt_toword_str(self, handle, mode: PageSegMode,
                                       wordstr: bytes) -> bool:
        return self.TessBaseAPIAdaptToWordStr(handle, mode, wordstr)

    def capi_base_api_clear(self, handle):
        self.TessBaseAPIClear(handle)

    def capi_base_api_end(self, handle):
        self.TessBaseAPIEnd(handle)

    def capi_base_api_isvalid_word(self, handle, word: bytes) -> int:
        return self.TessBaseAPIIsValidWord(handle, word)

    def capi_base_api_get_text_direction(self, handle, out_offset: int,
                                         out_slope: float) -> bool:
        return self.TessBaseAPIGetTextDirection(handle, out_offset, out_slope)

    def capi_base_api_get_unichar(self, handle, unichar_id: int) -> bytes:
        return self.TessBaseAPIGetUnichar(handle, unichar_id)

    def capi_base_api_clear_persistent_cache(self, handle):
        self.TessBaseAPIClearPersistentCache(handle)

    def capi_base_api_detect_orientation_script(self, handle, orient_deg: int,
                                                orient_conf: float,
                                                script_name: bytes,
                                                script_conf: float) -> bool:
        return self.TessBaseAPIDetectOrientationScript(handle, orient_deg,
                                                       orient_conf,
                                                       script_name,
                                                       script_conf)

    def capi_base_api_set_min_orientation_margin(self, handle, margin: float):
        self.TessBaseAPISetMinOrientationMargin(handle, margin)

    def capi_base_api_num_dawgs(self, handle) -> int:
        return self.TessBaseAPINumDawgs(handle)

    def capi_base_api_oem(self, handle) -> int:
        return self.TessBaseAPIOem(handle)

    def capi_base_get_block_text_orientations(self, handle,
                                              block_orientation: int,
                                              vertical_writing: bool):
        self.TessBaseGetBlockTextOrientations(
            handle, block_orientation, vertical_writing)

    # Page iterator

    def capi_page_iterator_delete(self, handle):
        self.TessPageIteratorDelete(handle)

    def capi_page_iterator_copy(self, handle):
        return self.TessPageIteratorCopy(handle)

    def capi_page_iterator_begin(self, handle):
        self.TessPageIteratorBegin(handle)

    def capi_page_iterator_next(self, handle,
                                level: PageIteratorLevel) -> bool:
        return self.TessPageIteratorNext(handle, level)

    def capi_page_iterator_isat_beginning_of(self, handle,
                                             level: PageIteratorLevel) -> bool:
        return self.TessPageIteratorIsAtBeginningOf(handle, level)

    def capi_page_iterator_isat_final_element(
        self, handle,
            level: PageIteratorLevel,
            element: PageIteratorLevel) -> bool:
        return self.TessPageIteratorIsAtFinalElement(handle, level, element)

    def capi_page_iterator_bounding_box(self, handle,
                                        level: PageIteratorLevel,
                                        left: int,
                                        top: int,
                                        right: int,
                                        bottom: int) -> bool:
        return self.TessPageIteratorBoundingBox(handle, level,
                                                left, top,
                                                right, bottom)

    def capi_page_iterator_block_type(self, handle) -> int:
        return self.TessPageIteratorBlockType(handle)

    def capi_page_iterator_get_binary_image(self, handle,
                                            level: PageIteratorLevel):
        return self.TessPageIteratorGetBinaryImage(handle, level)

    def capi_page_iterator_get_image(self, handle, level: PageIteratorLevel,
                                     padding: int, original_image,
                                     left: int, top: int):
        return self.TessPageIteratorGetImage(
            handle, level, padding, original_image, left, top)

    def capi_page_iterator_baseline(self, handle, level: PageIteratorLevel,
                                    x1: int, y1: int,
                                    x2: int, y2: int) -> bool:
        return self.TessPageIteratorBaseline(handle, level, x1, y1, x2, y2)

    def capi_page_iterator_orientation(self, handle, orientation: Orientation,
                                       writing_direction: WritingDirection,
                                       textline_order: TextlineOrder,
                                       deskew_angle: float):
        self.TessPageIteratorOrientation(
            handle, orientation, writing_direction, textline_order,
            deskew_angle)

    def capi_page_iterator_paragraph_info(
            self, handle,
            justification: ParagraphJustification,
            is_list_item: bool, is_crown: bool,
            first_line_indent: int):
        self.TessPageIteratorParagraphInfo(
            handle, justification, is_list_item, is_crown, first_line_indent)

    # Result iterator

    def capi_result_iterator_delete(self, handle):
        self.TessResultIteratorDelete(handle)

    def capi_result_iterator_copy(self, handle):
        return self.TessResultIteratorCopy(handle)

    def capi_result_iterator_get_page_iterator(self, handle):
        return self.TessResultIteratorGetPageIterator(handle)

    def capi_result_iterator_get_page_iterator_const(self, handle):
        return self.TessResultIteratorGetPageIteratorConst(handle)

    def capi_result_iterator_get_choice_iterator(self, handle):
        return self.TessResultIteratorGetChoiceIterator(handle)

    def capi_result_iterator_next(self, handle,
                                  level: PageIteratorLevel) -> bool:
        return self.TessResultIteratorNext(handle, level)

    def capi_result_iterator_get_utf8text(self, handle,
                                          level: PageIteratorLevel) -> bytes:
        return self.TessResultIteratorGetUTF8Text(handle, level)

    def capi_result_iterator_confidence(self, handle,
                                        level: PageIteratorLevel) -> float:
        return self.TessResultIteratorConfidence(handle, level)

    def capi_result_iterator_word_recognition_language(self, handle) -> bytes:
        return self.TessResultIteratorWordRecognitionLanguage(handle)

    def capi_result_iterator_word_font_attributes(self, handle,
                                                  is_bold: bool,
                                                  is_italic: bool,
                                                  is_underlined: bool,
                                                  is_monospace: bool,
                                                  is_serif: bool,
                                                  is_smallcaps: bool,
                                                  pointsize: int,
                                                  font_id: int) -> bytes:
        return self.TessResultIteratorWordFontAttributes(handle, is_bold,
                                                         is_italic,
                                                         is_underlined,
                                                         is_monospace,
                                                         is_serif,
                                                         is_smallcaps,
                                                         pointsize, font_id)

    def capi_result_iterator_word_isfrom_dictionary(self, handle) -> bool:
        return self.TessResultIteratorWordIsFromDictionary(handle)

    def capi_result_iterator_word_isnumeric(self, handle) -> bool:
        return self.TessResultIteratorWordIsNumeric(handle)

    def capi_result_iterator_symbol_issuperscript(self, handle) -> bool:
        return self.TessResultIteratorSymbolIsSuperscript(handle)

    def capi_result_iterator_symbol_issubscript(self, handle) -> bool:
        return self.TessResultIteratorSymbolIsSubscript(handle)

    def capi_result_iterator_symbol_isdropcap(self, handle) -> bool:
        return self.TessResultIteratorSymbolIsDropcap(handle)

    def capi_choice_iterator_delete(self, handle):
        self.TessChoiceIteratorDelete(handle)

    def capi_choice_iterator_next(self, handle) -> bool:
        return self.TessChoiceIteratorNext(handle)

    def capi_choice_iterator_get_utf8text(self, handle) -> bytes:
        return self.TessChoiceIteratorGetUTF8Text(handle)

    def capi_choice_iterator_confidence(self, handle) -> float:
        return self.TessChoiceIteratorConfidence(handle)

    # Progress monitor

    def capi_monitor_create(self):
        return self.TessMonitorCreate()

    def capi_monitor_delete(self, monitor):
        self.TessMonitorDelete(monitor)

    def capi_monitor_set_cancel_func(self, monitor, cancelFunc):
        self.TessMonitorSetCancelFunc(monitor, cancelFunc)

    def capi_monitor_set_cancel_this(self, monitor, cancelThis):
        self.TessMonitorSetCancelThis(monitor, cancelThis)

    def capi_monitor_get_cancel_this(self, monitor):
        return self.TessMonitorGetCancelThis(monitor)

    def capi_monitor_set_progress_func(self, monitor, progressFunc):
        self.TessMonitorSetProgressFunc(monitor, progressFunc)

    def capi_monitor_get_progress(self, monitor) -> int:
        return self.TessMonitorGetProgress(monitor)

    def capi_monitor_set_deadline_msecs(self, monitor, deadline: int):
        self.TessMonitorSetDeadlineMSecs(monitor, deadline)


TESSERACT_API = TesseractAPI(TESS_DLL)
