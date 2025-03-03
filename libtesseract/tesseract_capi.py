# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:43:58 2021

@author: 皓
"""
from enum import IntEnum
from functools import wraps
from ctypes import (POINTER, CFUNCTYPE, c_float, c_void_p, c_int, c_char_p,
                    c_bool, c_size_t, c_double, cast)
from .common import TESS_DLL
from .datatype import (c_int_p, c_bool_p, c_double_p, c_ubyte_p, c_float_p,
                       LP_c_char, CAPI, c_char_p_p)
from .leptonica_capi import LPPix, LPBoxa, LPLPPixa


def bytes_list(data):
    for item in data:
        if item is None:
            return
        yield item


def int_list(data):
    for item in data:
        if item == -1:
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


LPTessResultRenderer = c_void_p
LPTessBaseAPI = c_void_p
LPTessPageIterator = c_void_p
LPTessResultIterator = c_void_p
LPTessMutableIterator = c_void_p
LPTessChoiceIterator = c_void_p
LPETEXT_DESC = c_void_p
LPFILE = c_void_p


TessCancelFunc = CFUNCTYPE(c_bool, c_void_p, c_int)
TessProgressFunc = CFUNCTYPE(c_bool, LPETEXT_DESC, c_int, c_int, c_int, c_int)


class TessCAPI(CAPI):
    NAME = 'Tesseract'
    API = {
        # General free functions
        'TessVersion': (c_char_p, ),
        'TessDeleteText': (None,
                           c_char_p,  # const char * text
                           ),
        'TessDeleteTextArray': (None,
                                c_char_p_p,  # char ** arr
                                ),
        'TessDeleteIntArray': (None,
                               c_int_p,  # const int * arr
                               ),

        # Renderer API
        'TessTextRendererCreate': (LPTessResultRenderer,  # TessResultRenderer *
                                   c_char_p,  # const char * outputbase
                                   ),
        'TessHOcrRendererCreate': (LPTessResultRenderer,  # TessResultRenderer *
                                   c_char_p,  # const char * outputbase
                                   ),
        'TessHOcrRendererCreate2': (LPTessResultRenderer,  # TessResultRenderer *
                                    c_char_p,  # const char * outputbase
                                    c_bool,  # BOOL font_info
                                    ),
        'TessAltoRendererCreate': (LPTessResultRenderer,  # TessResultRenderer *
                                   c_char_p,  # const char * outputbase
                                   ),
        'TessTsvRendererCreate': (LPTessResultRenderer,  # TessResultRenderer *
                                  c_char_p,  # const char * outputbase
                                  ),
        'TessPDFRendererCreate': (LPTessResultRenderer,  # TessResultRenderer *
                                  c_char_p,  # const char * outputbase
                                  c_char_p,  # const char * datadir
                                  c_bool,  # BOOL textonly
                                  ),
        'TessUnlvRendererCreate': (LPTessResultRenderer,  # TessResultRenderer *
                                   c_char_p,  # const char * outputbase
                                   ),
        'TessBoxTextRendererCreate': (LPTessResultRenderer,  # TessResultRenderer *
                                      c_char_p,  # const char * outputbase
                                      ),
        'TessLSTMBoxRendererCreate': (LPTessResultRenderer,  # TessResultRenderer *
                                      c_char_p,  # const char * outputbase
                                      ),
        'TessWordStrBoxRendererCreate': (LPTessResultRenderer,  # TessResultRenderer *
                                         c_char_p,  # const char * outputbase
                                         ),
        'TessDeleteResultRenderer': (None,
                                     # TessResultRenderer * renderer
                                     LPTessResultRenderer,
                                     ),
        'TessResultRendererInsert': (None,
                                     # TessResultRenderer * renderer
                                     LPTessResultRenderer,
                                     # TessResultRenderer * next
                                     LPTessResultRenderer,
                                     ),
        'TessResultRendererNext': (LPTessResultRenderer,  # TessResultRenderer *
                                   # TessResultRenderer * renderer
                                   LPTessResultRenderer,
                                   ),
        'TessResultRendererBeginDocument': (c_bool,
                                            # TessResultRenderer * renderer
                                            LPTessResultRenderer,
                                            c_char_p,  # const char * title
                                            ),
        'TessResultRendererAddImage': (c_bool,
                                       # TessResultRenderer * renderer
                                       LPTessResultRenderer,
                                       LPTessBaseAPI,  # TessBaseAPI * api
                                       ),
        'TessResultRendererEndDocument': (c_bool,
                                          # TessResultRenderer * renderer
                                          LPTessResultRenderer,
                                          ),
        'TessResultRendererExtention': (c_char_p,
                                        # TessResultRenderer * renderer
                                        LPTessResultRenderer,
                                        ),
        'TessResultRendererTitle': (c_char_p,
                                    # TessResultRenderer * renderer
                                    LPTessResultRenderer,
                                    ),
        'TessResultRendererImageNum': (c_int,
                                       # TessResultRenderer * renderer
                                       LPTessResultRenderer,
                                       ),
        # Base API
        'TessBaseAPICreate': (LPTessBaseAPI, ),  # TessBaseAPI *
        'TessBaseAPIDelete': (None,
                              LPTessBaseAPI,  # TessBaseAPI * handle
                              ),
        'TessBaseAPIGetOpenCLDevice': (c_size_t,
                                       LPTessBaseAPI,  # TessBaseAPI * handle
                                       POINTER(c_void_p),  # void ** device
                                       ),
        'TessBaseAPISetInputName': (None,
                                    LPTessBaseAPI,  # TessBaseAPI * handle
                                    c_char_p,  # const char * name
                                    ),
        'TessBaseAPIGetInputName': (c_char_p,
                                    LPTessBaseAPI,  # TessBaseAPI * handle
                                    ),
        'TessBaseAPISetInputImage': (None,
                                     LPTessBaseAPI,  # TessBaseAPI * handle
                                     LPPix,  # struct Pix * pix
                                     ),
        'TessBaseAPIGetInputImage': (LPPix,  # struct Pix *
                                     LPTessBaseAPI,  # TessBaseAPI * handle
                                     ),
        'TessBaseAPIGetSourceYResolution': (c_int,
                                            # TessBaseAPI * handle
                                            LPTessBaseAPI,
                                            ),
        'TessBaseAPIGetDatapath': (c_char_p,
                                   LPTessBaseAPI,  # TessBaseAPI * handle
                                   ),
        'TessBaseAPISetOutputName': (None,
                                     LPTessBaseAPI,  # TessBaseAPI * handle
                                     c_char_p,  # const char * name
                                     ),
        'TessBaseAPISetVariable': (c_bool,
                                   LPTessBaseAPI,  # TessBaseAPI * handle
                                   c_char_p,  # const char * name
                                   c_char_p,  # const char * value
                                   ),
        'TessBaseAPISetDebugVariable': (c_bool,
                                        LPTessBaseAPI,  # TessBaseAPI * handle
                                        c_char_p,  # const char * name
                                        c_char_p,  # const char * value
                                        ),
        'TessBaseAPIGetIntVariable': (c_bool,
                                      # const TessBaseAPI * handle
                                      LPTessBaseAPI,
                                      c_char_p,  # const char * name
                                      c_int_p,  # int * value
                                      ),
        'TessBaseAPIGetBoolVariable': (c_bool,
                                       # const TessBaseAPI * handle
                                       LPTessBaseAPI,
                                       c_char_p,  # const char * name
                                       c_bool_p,  # BOOL * value
                                       ),
        'TessBaseAPIGetDoubleVariable': (c_bool,
                                         # const TessBaseAPI * handle
                                         LPTessBaseAPI,
                                         c_char_p,  # const char * name
                                         c_double_p,  # double * value
                                         ),
        'TessBaseAPIGetStringVariable': (c_char_p,
                                         # const TessBaseAPI * handle
                                         LPTessBaseAPI,
                                         c_char_p,  # const char * name
                                         ),
        'TessBaseAPIPrintVariables': (None,
                                      # const TessBaseAPI * handle
                                      LPTessBaseAPI,
                                      LPFILE,  # FILE * fp
                                      ),
        'TessBaseAPIPrintVariablesToFile': (c_bool,
                                            # const TessBaseAPI * handle
                                            LPTessBaseAPI,
                                            c_char_p,  # const char * filename
                                            ),
        'TessBaseAPIInit1': (c_int,
                             LPTessBaseAPI,  # TessBaseAPI * handle
                             c_char_p,  # const char * datapath
                             c_char_p,  # const char * language
                             c_int,  # TessOcrEngineMode oem
                             c_char_p_p,  # char ** configs
                             c_int,  # int configs_size
                             ),
        'TessBaseAPIInit2': (c_int,
                             LPTessBaseAPI,  # TessBaseAPI * handle
                             c_char_p,  # const char * datapath
                             c_char_p,  # const char * language
                             c_int,  # TessOcrEngineMode oem
                             ),
        'TessBaseAPIInit3': (c_int,
                             LPTessBaseAPI,  # TessBaseAPI * handle
                             c_char_p,  # const char * datapath
                             c_char_p,  # const char * language
                             ),
        'TessBaseAPIInit4': (c_int,
                             LPTessBaseAPI,  # TessBaseAPI * handle
                             c_char_p,  # const char * datapath
                             c_char_p,  # const char * language
                             c_int,  # TessOcrEngineMode mode
                             c_char_p_p,  # char ** configs
                             c_int,  # int configs_size
                             c_char_p_p,  # char ** vars_vec
                             c_char_p_p,  # char ** vars_values
                             c_size_t,  # size_t vars_vec_size
                             c_bool,  # BOOL set_only_non_debug_params
                             ),
        'TessBaseAPIInit5': (c_int,
                             LPTessBaseAPI,  # TessBaseAPI * handle
                             c_char_p,  # const char * data
                             c_int,  # int data_size
                             c_char_p,  # const char * language
                             c_int,  # TessOcrEngineMode mode
                             c_char_p_p,  # char ** configs
                             c_int,  # int configs_size
                             c_char_p_p,  # char ** vars_vec
                             c_char_p_p,  # char ** vars_values
                             c_size_t,  # size_t vars_vec_size
                             c_bool,  # BOOL set_only_non_debug_params
                             ),
        'TessBaseAPIGetInitLanguagesAsString': (c_char_p,
                                                # const TessBaseAPI * handle
                                                LPTessBaseAPI,
                                                ),
        'TessBaseAPIGetLoadedLanguagesAsVector': (c_char_p_p,
                                                  # const TessBaseAPI * handle
                                                  LPTessBaseAPI,
                                                  ),
        'TessBaseAPIGetAvailableLanguagesAsVector': (c_char_p_p,
                                                     # const TessBaseAPI * handle
                                                     LPTessBaseAPI,
                                                     ),
        'TessBaseAPIInitForAnalysePage': (None,
                                          # TessBaseAPI * handle
                                          LPTessBaseAPI,
                                          ),
        'TessBaseAPIReadConfigFile': (None,
                                      LPTessBaseAPI,  # TessBaseAPI * handle
                                      c_char_p,  # const char * filename
                                      ),
        'TessBaseAPIReadDebugConfigFile': (None,
                                           # TessBaseAPI * handle
                                           LPTessBaseAPI,
                                           c_char_p,  # const char * filename
                                           ),
        'TessBaseAPISetPageSegMode': (None,
                                      LPTessBaseAPI,  # TessBaseAPI * handle
                                      c_int,  # TessPageSegMode mode
                                      ),
        'TessBaseAPIGetPageSegMode': (c_int,  # TessPageSegMode
                                      # const TessBaseAPI * handle
                                      LPTessBaseAPI,
                                      ),
        'TessBaseAPIRect': (LP_c_char,
                            LPTessBaseAPI,  # TessBaseAPI * handle
                            c_ubyte_p,  # const unsigned char * imagedata
                            c_int,  # int bytes_per_pixel
                            c_int,  # int bytes_per_line
                            c_int,  # int left
                            c_int,  # int top
                            c_int,  # int width
                            c_int,  # int height
                            ),
        'TessBaseAPIClearAdaptiveClassifier': (None,
                                               # TessBaseAPI * handle
                                               LPTessBaseAPI,
                                               ),
        'TessBaseAPISetImage': (None,
                                LPTessBaseAPI,  # TessBaseAPI * handle
                                c_ubyte_p,  # const unsigned char * imagedata
                                c_int,  # int width
                                c_int,  # int height
                                c_int,  # int bytes_per_pixel
                                c_int,  # int bytes_per_line
                                ),
        'TessBaseAPISetImage2': (None,
                                 LPTessBaseAPI,  # TessBaseAPI * handle
                                 LPPix,  # struct Pix * pix
                                 ),
        'TessBaseAPISetSourceResolution': (None,
                                           # TessBaseAPI * handle
                                           LPTessBaseAPI,
                                           c_int,  # int ppi
                                           ),
        'TessBaseAPISetRectangle': (None,
                                    LPTessBaseAPI,  # TessBaseAPI * handle
                                    c_int,  # int left
                                    c_int,  # int top
                                    c_int,  # int width
                                    c_int,  # int height
                                    ),
        'TessBaseAPIGetThresholdedImage': (LPPix,  # struct Pix *
                                           # TessBaseAPI * handle
                                           LPTessBaseAPI,
                                           ),
        'TessBaseAPIGetRegions': (LPBoxa,  # struct Boxa *
                                  LPTessBaseAPI,  # TessBaseAPI * handle
                                  LPLPPixa,  # struct Pixa ** pixa
                                  ),
        'TessBaseAPIGetTextlines': (LPBoxa,  # struct Boxa *
                                    LPTessBaseAPI,  # TessBaseAPI * handle
                                    LPLPPixa,  # struct Pixa ** pixa
                                    # int ** blockids
                                    POINTER(c_int_p),
                                    ),
        'TessBaseAPIGetTextlines1': (LPBoxa,  # struct Boxa *
                                     LPTessBaseAPI,  # TessBaseAPI * handle
                                     c_bool,  # BOOL raw_image
                                     c_int,  # int raw_padding
                                     LPLPPixa,  # struct Pixa ** pixa
                                     # int ** blockids
                                     POINTER(c_int_p),
                                     # int ** paraids
                                     POINTER(c_int_p),
                                     ),
        'TessBaseAPIGetStrips': (LPBoxa,  # struct Boxa *
                                 LPTessBaseAPI,  # TessBaseAPI * handle
                                 LPLPPixa,  # struct Pixa ** pixa
                                 POINTER(c_int_p),  # int ** blockids
                                 ),
        'TessBaseAPIGetWords': (LPBoxa,  # struct Boxa *
                                LPTessBaseAPI,  # TessBaseAPI * handle
                                LPLPPixa,  # struct Pixa ** pixa
                                ),
        'TessBaseAPIGetConnectedComponents': (LPBoxa,  # struct Boxa *
                                              # TessBaseAPI * handle
                                              LPTessBaseAPI,
                                              LPLPPixa,  # struct Pixa ** cc
                                              ),
        'TessBaseAPIGetComponentImages': (LPBoxa,  # struct Boxa *
                                          # TessBaseAPI * handle
                                          LPTessBaseAPI,
                                          # TessPageIteratorLevel level
                                          c_int,
                                          c_bool,  # BOOL text_only
                                          LPLPPixa,  # struct Pixa ** pixa
                                          # int ** blockids
                                          POINTER(c_int_p),
                                          ),
        'TessBaseAPIGetComponentImages1': (LPBoxa,  # struct Boxa *
                                           # TessBaseAPI * handle
                                           LPTessBaseAPI,
                                           # TessPageIteratorLevel level
                                           c_int,
                                           c_bool,  # BOOL text_only
                                           c_bool,  # BOOL raw_image
                                           c_int,  # int raw_padding
                                           LPLPPixa,  # struct Pixa ** pixa
                                           # int ** blockids
                                           POINTER(c_int_p),
                                           # int ** paraids
                                           POINTER(c_int_p),
                                           ),
        'TessBaseAPIGetThresholdedImageScaleFactor': (c_int,
                                                      # const TessBaseAPI * handle
                                                      LPTessBaseAPI,
                                                      ),
        'TessBaseAPIAnalyseLayout': (LPTessPageIterator,  # TessPageIterator *
                                     LPTessBaseAPI,  # TessBaseAPI * handle
                                     ),
        'TessBaseAPIRecognize': (c_int,
                                 LPTessBaseAPI,  # TessBaseAPI * handle
                                 LPETEXT_DESC,  # ETEXT_DESC * monitor
                                 ),
        'TessBaseAPIProcessPages': (c_bool,
                                    LPTessBaseAPI,  # TessBaseAPI * handle
                                    c_char_p,  # const char * filename
                                    c_char_p,  # const char * retry_config
                                    c_int,  # int timeout_millisec
                                    # TessResultRenderer * renderer
                                    LPTessResultRenderer,
                                    ),
        'TessBaseAPIProcessPage': (c_bool,
                                   LPTessBaseAPI,  # TessBaseAPI * handle
                                   LPPix,  # struct Pix * pix
                                   c_int,  # int page_index
                                   c_char_p,  # const char * filename
                                   c_char_p,  # const char * retry_config
                                   c_int,  # int timeout_millisec
                                   # TessResultRenderer * renderer
                                   LPTessResultRenderer,
                                   ),
        'TessBaseAPIGetIterator': (LPTessResultIterator,  # TessResultIterator *
                                   LPTessBaseAPI,  # TessBaseAPI * handle
                                   ),
        'TessBaseAPIGetMutableIterator': (LPTessMutableIterator,  # TessMutableIterator *
                                          # TessBaseAPI * handle
                                          LPTessBaseAPI,
                                          ),
        'TessBaseAPIGetUTF8Text': (LP_c_char,
                                   LPTessBaseAPI,  # TessBaseAPI * handle
                                   ),
        'TessBaseAPIGetHOCRText': (LP_c_char,
                                   LPTessBaseAPI,  # TessBaseAPI * handle
                                   c_int,  # int page_number
                                   ),
        'TessBaseAPIGetAltoText': (LP_c_char,
                                   LPTessBaseAPI,  # TessBaseAPI * handle
                                   c_int,  # int page_number
                                   ),
        'TessBaseAPIGetTsvText': (LP_c_char,
                                  LPTessBaseAPI,  # TessBaseAPI * handle
                                  c_int,  # int page_number
                                  ),
        'TessBaseAPIGetBoxText': (LP_c_char,
                                  LPTessBaseAPI,  # TessBaseAPI * handle
                                  c_int,  # int page_number
                                  ),
        'TessBaseAPIGetLSTMBoxText': (LP_c_char,
                                      LPTessBaseAPI,  # TessBaseAPI * handle
                                      c_int,  # int page_number
                                      ),
        'TessBaseAPIGetWordStrBoxText': (LP_c_char,
                                         # TessBaseAPI * handle
                                         LPTessBaseAPI,
                                         c_int,  # int page_number
                                         ),
        'TessBaseAPIGetUNLVText': (LP_c_char,
                                   LPTessBaseAPI,  # TessBaseAPI * handle
                                   ),
        'TessBaseAPIMeanTextConf': (c_int,
                                    LPTessBaseAPI,  # TessBaseAPI * handle
                                    ),
        'TessBaseAPIAllWordConfidences': (c_int_p,
                                          # TessBaseAPI * handle
                                          LPTessBaseAPI,
                                          ),
        'TessBaseAPIAdaptToWordStr': (c_bool,
                                      LPTessBaseAPI,  # TessBaseAPI * handle
                                      c_int,  # TessPageSegMode mode
                                      c_char_p,  # const char * wordstr
                                      ),
        'TessBaseAPIClear': (None,
                             LPTessBaseAPI,  # TessBaseAPI * handle
                             ),
        'TessBaseAPIEnd': (None,
                           LPTessBaseAPI,  # TessBaseAPI * handle
                           ),
        'TessBaseAPIIsValidWord': (c_int,
                                   LPTessBaseAPI,  # TessBaseAPI * handle
                                   c_char_p,  # const char * word
                                   ),
        'TessBaseAPIGetTextDirection': (c_bool,
                                        LPTessBaseAPI,  # TessBaseAPI * handle
                                        c_int_p,  # int * out_offset
                                        c_float_p,  # float * out_slope
                                        ),
        'TessBaseAPIGetUnichar': (c_char_p,
                                  LPTessBaseAPI,  # TessBaseAPI * handle
                                  c_int,  # int unichar_id
                                  ),
        'TessBaseAPIClearPersistentCache': (None,
                                            # TessBaseAPI * handle
                                            LPTessBaseAPI,
                                            ),
        'TessBaseAPIDetectOrientationScript': (c_bool,
                                               # TessBaseAPI * handle
                                               LPTessBaseAPI,
                                               c_int_p,  # int * orient_deg
                                               # float * orient_conf
                                               c_float_p,
                                               # const char ** script_name
                                               c_char_p_p,
                                               # float * script_conf
                                               c_float_p,
                                               ),
        'TessBaseAPISetMinOrientationMargin': (None,
                                               # TessBaseAPI * handle
                                               LPTessBaseAPI,
                                               c_double,  # double margin
                                               ),
        'TessBaseAPINumDawgs': (c_int,
                                LPTessBaseAPI,  # const TessBaseAPI * handle
                                ),
        'TessBaseAPIOem': (c_int,  # TessOcrEngineMode
                           LPTessBaseAPI,  # const TessBaseAPI * handle
                           ),
        'TessBaseGetBlockTextOrientations': (None,
                                             # TessBaseAPI * handle
                                             LPTessBaseAPI,
                                             # int ** block_orientation
                                             POINTER(c_int_p),
                                             # bool ** vertical_writing
                                             POINTER(c_bool_p),
                                             ),
        # Page iterator
        'TessPageIteratorDelete': (None,
                                   # TessPageIterator * handle
                                   LPTessPageIterator,
                                   ),
        'TessPageIteratorCopy': (LPTessPageIterator,  # TessPageIterator *
                                 # const TessPageIterator * handle
                                 LPTessPageIterator,
                                 ),
        'TessPageIteratorBegin': (None,
                                  # TessPageIterator * handle
                                  LPTessPageIterator,
                                  ),
        'TessPageIteratorNext': (c_bool,
                                 # TessPageIterator * handle
                                 LPTessPageIterator,
                                 c_int,  # TessPageIteratorLevel level
                                 ),
        'TessPageIteratorIsAtBeginningOf': (c_bool,
                                            # const TessPageIterator * handle
                                            LPTessPageIterator,
                                            # TessPageIteratorLevel level
                                            c_int,
                                            ),
        'TessPageIteratorIsAtFinalElement': (c_bool,
                                             # const TessPageIterator * handle
                                             LPTessPageIterator,
                                             # TessPageIteratorLevel level
                                             c_int,
                                             # TessPageIteratorLevel element
                                             c_int,
                                             ),
        'TessPageIteratorBoundingBox': (c_bool,
                                        # const TessPageIterator * handle
                                        LPTessPageIterator,
                                        c_int,  # TessPageIteratorLevel level
                                        c_int_p,  # int * left
                                        c_int_p,  # int * top
                                        c_int_p,  # int * right
                                        c_int_p,  # int * bottom
                                        ),
        'TessPageIteratorBlockType': (c_int,  # TessPolyBlockType
                                      # const TessPageIterator * handle
                                      LPTessPageIterator,
                                      ),
        'TessPageIteratorGetBinaryImage': (LPPix,  # struct Pix *
                                           # const TessPageIterator * handle
                                           LPTessPageIterator,
                                           # TessPageIteratorLevel level
                                           c_int,
                                           ),
        'TessPageIteratorGetImage': (LPPix,  # struct Pix *
                                     # const TessPageIterator * handle
                                     LPTessPageIterator,
                                     c_int,  # TessPageIteratorLevel level
                                     c_int,  # int padding
                                     LPPix,  # struct Pix * original_image
                                     c_int_p,  # int * left
                                     c_int_p,  # int * top
                                     ),
        'TessPageIteratorBaseline': (c_bool,
                                     # const TessPageIterator * handle
                                     LPTessPageIterator,
                                     c_int,  # TessPageIteratorLevel level
                                     c_int_p,  # int * x1
                                     c_int_p,  # int * y1
                                     c_int_p,  # int * x2
                                     c_int_p,  # int * y2
                                     ),
        'TessPageIteratorOrientation': (None,
                                        # TessPageIterator * handle
                                        LPTessPageIterator,
                                        # TessOrientation * orientation
                                        c_int_p,
                                        # TessWritingDirection * writing_direction
                                        c_int_p,
                                        # TessTextlineOrder * textline_order
                                        c_int_p,
                                        c_float_p,  # float * deskew_angle
                                        ),
        'TessPageIteratorParagraphInfo': (None,
                                          # TessPageIterator * handle
                                          LPTessPageIterator,
                                          # TessParagraphJustification * justification
                                          c_int_p,
                                          c_bool_p,  # BOOL * is_list_item
                                          c_bool_p,  # BOOL * is_crown
                                          c_int_p,  # int * first_line_indent
                                          ),
        # Result iterator
        'TessResultIteratorDelete': (None,
                                     # TessResultIterator * handle
                                     LPTessResultIterator,
                                     ),
        'TessResultIteratorCopy': (LPTessResultIterator,  # TessResultIterator *
                                   # const TessResultIterator * handle
                                   LPTessResultIterator,
                                   ),
        'TessResultIteratorGetPageIterator': (LPTessPageIterator,  # TessPageIterator *
                                              # TessResultIterator * handle
                                              LPTessResultIterator,
                                              ),
        'TessResultIteratorGetPageIteratorConst': (LPTessPageIterator,  # const TessPageIterator *
                                                   # const TessResultIterator * handle
                                                   LPTessResultIterator,
                                                   ),
        'TessResultIteratorGetChoiceIterator': (LPTessChoiceIterator,  # TessChoiceIterator *
                                                # const TessResultIterator * handle
                                                LPTessResultIterator,
                                                ),
        'TessResultIteratorNext': (c_bool,
                                   # TessResultIterator * handle
                                   LPTessResultIterator,
                                   c_int,  # TessPageIteratorLevel level
                                   ),
        'TessResultIteratorGetUTF8Text': (LP_c_char,
                                          # const TessResultIterator * handle
                                          LPTessResultIterator,
                                          # TessPageIteratorLevel level
                                          c_int,
                                          ),
        'TessResultIteratorConfidence': (c_float,
                                         # const TessResultIterator * handle
                                         LPTessResultIterator,
                                         c_int,  # TessPageIteratorLevel level
                                         ),
        'TessResultIteratorWordRecognitionLanguage': (c_char_p,
                                                      # const TessResultIterator * handle
                                                      LPTessResultIterator,
                                                      ),
        'TessResultIteratorWordFontAttributes': (c_char_p,
                                                 # const TessResultIterator * handle
                                                 LPTessResultIterator,
                                                 c_bool_p,  # BOOL * is_bold
                                                 c_bool_p,  # BOOL * is_italic
                                                 # BOOL * is_underlined
                                                 c_bool_p,
                                                 # BOOL * is_monospace
                                                 c_bool_p,
                                                 c_bool_p,  # BOOL * is_serif
                                                 # BOOL * is_smallcaps
                                                 c_bool_p,
                                                 c_int_p,  # int * pointsize
                                                 c_int_p,  # int * font_id
                                                 ),
        'TessResultIteratorWordIsFromDictionary': (c_bool,
                                                   # const TessResultIterator * handle
                                                   LPTessResultIterator,
                                                   ),
        'TessResultIteratorWordIsNumeric': (c_bool,
                                            # const TessResultIterator * handle
                                            LPTessResultIterator,
                                            ),
        'TessResultIteratorSymbolIsSuperscript': (c_bool,
                                                  # const TessResultIterator * handle
                                                  LPTessResultIterator,
                                                  ),
        'TessResultIteratorSymbolIsSubscript': (c_bool,
                                                # const TessResultIterator * handle
                                                LPTessResultIterator,
                                                ),
        'TessResultIteratorSymbolIsDropcap': (c_bool,
                                              # const TessResultIterator * handle
                                              LPTessResultIterator,
                                              ),
        'TessChoiceIteratorDelete': (None,
                                     # TessChoiceIterator * handle
                                     LPTessChoiceIterator,
                                     ),
        'TessChoiceIteratorNext': (c_bool,
                                   # TessChoiceIterator * handle
                                   LPTessChoiceIterator,
                                   ),
        'TessChoiceIteratorGetUTF8Text': (c_char_p,
                                          # const TessChoiceIterator * handle
                                          LPTessChoiceIterator,
                                          ),
        'TessChoiceIteratorConfidence': (c_float,
                                         # const TessChoiceIterator * handle
                                         LPTessChoiceIterator,
                                         ),
        # Progress monitor
        'TessMonitorCreate': (LPETEXT_DESC, ),  # ETEXT_DESC *
        'TessMonitorDelete': (None,
                              LPETEXT_DESC,  # ETEXT_DESC * monitor
                              ),
        'TessMonitorSetCancelFunc': (None,
                                     LPETEXT_DESC,  # ETEXT_DESC * monitor
                                     # TessCancelFunc cancelFunc
                                     TessCancelFunc,
                                     ),
        'TessMonitorSetCancelThis': (None,
                                     LPETEXT_DESC,  # ETEXT_DESC * monitor
                                     c_void_p,  # void * cancelThis
                                     ),
        'TessMonitorGetCancelThis': (c_void_p,
                                     LPETEXT_DESC,  # ETEXT_DESC * monitor
                                     ),
        'TessMonitorSetProgressFunc': (None,
                                       LPETEXT_DESC,  # ETEXT_DESC * monitor
                                       # TessProgressFunc progressFunc
                                       TessProgressFunc,
                                       ),
        'TessMonitorGetProgress': (c_int,
                                   LPETEXT_DESC,  # ETEXT_DESC * monitor
                                   ),
        'TessMonitorSetDeadlineMSecs': (None,
                                        LPETEXT_DESC,  # ETEXT_DESC * monitor
                                        c_int,  # int deadline
                                        )
    }

    # General free functions

    def capi_version(self) -> bytes:
        return self.TessVersion()

    def capi_delete_text(self, text: c_char_p):
        self.TessDeleteText(text)

    def capi_delete_text_array(self, arr: c_char_p_p):
        self.TessDeleteTextArray(arr)

    def capi_delete_int_array(self, arr: c_int_p):
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

    def capi_delete_result_renderer(self,
                                    renderer: LPTessResultRenderer):
        self.TessDeleteResultRenderer(renderer)

    def capi_result_renderer_insert(self,
                                    renderer: LPTessResultRenderer,
                                    next_: LPTessResultRenderer):
        self.TessResultRendererInsert(renderer, next_)

    def capi_result_renderer_next(
            self, renderer: LPTessResultRenderer) -> LPTessResultRenderer:
        return self.TessResultRendererNext(renderer)

    def capi_result_renderer_begin_document(self,
                                            renderer: LPTessResultRenderer,
                                            title: bytes) -> bool:
        return self.TessResultRendererBeginDocument(renderer, title)

    def capi_result_renderer_add_image(self,
                                       renderer: LPTessResultRenderer,
                                       api: LPTessBaseAPI) -> bool:
        return self.TessResultRendererAddImage(renderer, api)

    def capi_result_renderer_end_document(
            self, renderer: LPTessResultRenderer) -> bool:
        return self.TessResultRendererEndDocument(renderer)

    def capi_result_renderer_extention(
            self,
            renderer: LPTessResultRenderer) -> bytes:
        return self.TessResultRendererExtention(renderer)

    def capi_result_renderer_title(self,
                                   renderer: LPTessResultRenderer) -> bytes:
        return self.TessResultRendererTitle(renderer)

    def capi_result_renderer_image_num(self,
                                       renderer: LPTessResultRenderer) -> int:
        return self.TessResultRendererImageNum(renderer)

    # Base API

    def capi_base_api_create(self):
        return self.TessBaseAPICreate()

    def capi_base_api_delete(self, handle):
        self.TessBaseAPIDelete(handle)

    def capi_base_api_get_opencl_device(self, handle, device) -> int:
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

    def capi_base_api_print_variables_to_file(self, handle,
                                              filename: bytes) -> bool:
        return self.TessBaseAPIPrintVariablesToFile(handle, filename)

    def capi_base_api_init1(self, handle, datapath: bytes, language: bytes,
                            oem: OcrEngineMode, configs: c_char_p_p,
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
                            configs: c_char_p_p,
                            configs_size: int,
                            vars_vec: c_char_p_p,
                            vars_values: c_char_p_p,
                            vars_vec_size: int,
                            set_only_non_debug_params: bool) -> int:
        return self.TessBaseAPIInit4(handle, datapath, language, mode, configs,
                                     configs_size, vars_vec, vars_values,
                                     vars_vec_size, set_only_non_debug_params)

    def capi_base_api_init5(self, handle, data: bytes, data_size: int,
                            language: bytes,
                            mode: OcrEngineMode,
                            configs: c_char_p_p,
                            configs_size: int,
                            vars_vec: c_char_p_p,
                            vars_values: c_char_p_p,
                            vars_vec_size: int,
                            set_only_non_debug_params: bool) -> int:
        return self.TessBaseAPIInit5(handle, data, data_size, language, mode,
                                     configs, configs_size,
                                     vars_vec, vars_values, vars_vec_size,
                                     set_only_non_debug_params)

    def capi_base_api_get_init_languages(self, handle) -> bytes:
        return self.TessBaseAPIGetInitLanguagesAsString(handle)

    def capi_base_api_get_loaded_languages(self, handle) -> list[bytes]:
        ret = self.TessBaseAPIGetLoadedLanguagesAsVector(handle)
        return list(bytes_list(ret))

    def capi_base_api_get_available_languages(self, handle) -> list[bytes]:
        ret = self.TessBaseAPIGetAvailableLanguagesAsVector(handle)
        return list(bytes_list(ret))

    # @deprecated('TessBaseAPIInitLangMod')
    # def capi_base_api_init_lang_mod(self, handle, datapath: bytes,
    #                                 language: bytes) -> int:
    #     return 0

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
                           height: int) -> LP_c_char:
        data = cast(imagedata, c_ubyte_p)
        return self.TessBaseAPIRect(handle, data,
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
        data = cast(imagedata, c_ubyte_p)
        self.TessBaseAPISetImage(handle, data,
                                 width, height,
                                 bytes_per_pixel, bytes_per_line)

    def capi_base_api_set_image2(self, handle, pix: LPPix):
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

    def capi_base_api_get_textlines(self, handle,
                                    pixa: LPLPPixa,
                                    blockids: POINTER(c_int_p)):
        return self.TessBaseAPIGetTextlines(handle, pixa, blockids)

    def capi_base_api_get_textlines1(self, handle,
                                     raw_image: bool, raw_padding: int,
                                     pixa: LPLPPixa,
                                     blockids: POINTER(c_int_p),
                                     paraids: POINTER(c_int_p)):
        return self.TessBaseAPIGetTextlines1(handle, raw_image, raw_padding,
                                             pixa, blockids, paraids)

    def capi_base_api_get_strips(self, handle, pixa,
                                 blockids: POINTER(c_int_p)):
        return self.TessBaseAPIGetStrips(handle, pixa, blockids)

    def capi_base_api_get_words(self, handle, pixa):
        return self.TessBaseAPIGetWords(handle, pixa)

    def capi_base_api_get_connected_components(self, handle, cc):
        return self.TessBaseAPIGetConnectedComponents(handle, cc)

    def capi_base_api_get_component_images(self, handle,
                                           level: PageIteratorLevel,
                                           text_only: bool,
                                           pixa, blockids: POINTER(c_int_p)):
        return self.TessBaseAPIGetComponentImages(handle, level, text_only,
                                                  pixa, blockids)

    def capi_base_api_get_component_images1(self, handle,
                                            level: PageIteratorLevel,
                                            text_only: bool, raw_image: bool,
                                            raw_padding: int,
                                            pixa, blockids: POINTER(c_int_p),
                                            paraids: POINTER(c_int_p)):
        return self.TessBaseAPIGetComponentImages1(handle, level, text_only,
                                                   raw_image, raw_padding,
                                                   pixa, blockids, paraids)

    def capi_base_api_get_thresholded_image_scale_factor(self, handle):
        return self.TessBaseAPIGetThresholdedImageScaleFactor(handle)

    def capi_base_api_analyse_layout(self, handle):
        return self.TessBaseAPIAnalyseLayout(handle)

    def capi_base_api_recognize(self, handle, monitor) -> int:
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

    def capi_base_api_get_utf8_text(self, handle) -> LP_c_char:
        return self.TessBaseAPIGetUTF8Text(handle)

    def capi_base_api_get_hocr_text(self, handle,
                                    page_number: int) -> LP_c_char:
        return self.TessBaseAPIGetHOCRText(handle,
                                           page_number)

    def capi_base_api_get_alto_text(self, handle,
                                    page_number: int) -> LP_c_char:
        return self.TessBaseAPIGetAltoText(handle,
                                           page_number)

    def capi_base_api_get_tsv_text(self, handle,
                                   page_number: int) -> LP_c_char:
        return self.TessBaseAPIGetTsvText(handle,
                                          page_number)

    def capi_base_api_get_box_text(self, handle,
                                   page_number: int) -> LP_c_char:
        return self.TessBaseAPIGetBoxText(handle,
                                          page_number)

    def capi_base_api_get_lstm_box_text(self, handle,
                                        page_number: int) -> LP_c_char:
        return self.TessBaseAPIGetLSTMBoxText(handle,
                                              page_number)

    def capi_base_api_get_word_str_box_text(self, handle,
                                            page_number: int) -> LP_c_char:
        return self.TessBaseAPIGetWordStrBoxText(handle,
                                                 page_number)

    def capi_base_api_get_unlv_text(self, handle) -> LP_c_char:
        return self.TessBaseAPIGetUNLVText(handle)

    def capi_base_api_mean_text_conf(self, handle) -> int:
        return self.TessBaseAPIMeanTextConf(handle)

    def capi_base_api_all_word_confidences(self, handle) -> list[int]:
        ret = self.TessBaseAPIAllWordConfidences(handle)
        return list(int_list(ret))

    def capi_base_api_adapt_to_word_str(self, handle, mode: PageSegMode,
                                        wordstr: bytes) -> bool:
        return self.TessBaseAPIAdaptToWordStr(handle, mode, wordstr)

    def capi_base_api_clear(self, handle):
        self.TessBaseAPIClear(handle)

    def capi_base_api_end(self, handle):
        self.TessBaseAPIEnd(handle)

    def capi_base_api_is_valid_word(self, handle, word: bytes) -> int:
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
                                                script_name: c_char_p_p,
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

    def capi_base_get_block_text_orientations(
            self, handle,
            block_orientation: POINTER(c_int_p),
            vertical_writing: POINTER(c_bool_p)):
        self.TessBaseGetBlockTextOrientations(handle, block_orientation,
                                              vertical_writing)

    # Page iterator

    def capi_page_iterator_delete(self, handle: LPTessPageIterator):
        self.TessPageIteratorDelete(handle)

    def capi_page_iterator_copy(
            self, handle: LPTessPageIterator) -> LPTessPageIterator:
        return self.TessPageIteratorCopy(handle)

    def capi_page_iterator_begin(self, handle: LPTessPageIterator):
        self.TessPageIteratorBegin(handle)

    def capi_page_iterator_next(self, handle: LPTessPageIterator,
                                level: PageIteratorLevel) -> bool:
        return self.TessPageIteratorNext(handle, level)

    def capi_page_iterator_is_at_beginning_of(
            self, handle: LPTessPageIterator,
            level: PageIteratorLevel) -> bool:
        return self.TessPageIteratorIsAtBeginningOf(handle, level)

    def capi_page_iterator_is_at_final_element(
        self, handle: LPTessPageIterator,
            level: PageIteratorLevel,
            element: PageIteratorLevel) -> bool:
        return self.TessPageIteratorIsAtFinalElement(handle, level, element)

    def capi_page_iterator_bounding_box(self, handle: LPTessPageIterator,
                                        level: PageIteratorLevel,
                                        left: int,
                                        top: int,
                                        right: int,
                                        bottom: int) -> bool:
        return self.TessPageIteratorBoundingBox(handle, level,
                                                left, top,
                                                right, bottom)

    def capi_page_iterator_block_type(self, handle: LPTessPageIterator) -> int:
        return self.TessPageIteratorBlockType(handle)

    def capi_page_iterator_get_binary_image(self, handle: LPTessPageIterator,
                                            level: PageIteratorLevel) -> LPPix:
        return self.TessPageIteratorGetBinaryImage(handle, level)

    def capi_page_iterator_get_image(self,
                                     handle: LPTessPageIterator,
                                     level: PageIteratorLevel,
                                     padding: int, original_image,
                                     left: int, top: int) -> LPPix:
        return self.TessPageIteratorGetImage(handle,
                                             level, padding, original_image,
                                             left, top)

    def capi_page_iterator_baseline(self,
                                    handle: LPTessPageIterator,
                                    level: PageIteratorLevel,
                                    x1: int, y1: int,
                                    x2: int, y2: int) -> bool:
        return self.TessPageIteratorBaseline(handle, level, x1, y1, x2, y2)

    def capi_page_iterator_orientation(self,
                                       handle: LPTessPageIterator,
                                       orientation: Orientation,
                                       writing_direction: WritingDirection,
                                       textline_order: TextlineOrder,
                                       deskew_angle: float):
        self.TessPageIteratorOrientation(handle, orientation,
                                         writing_direction, textline_order,
                                         deskew_angle)

    def capi_page_iterator_paragraph_info(
            self, handle: LPTessPageIterator,
            justification: ParagraphJustification,
            is_list_item: bool, is_crown: bool,
            first_line_indent: int):
        self.TessPageIteratorParagraphInfo(
            handle, justification, is_list_item, is_crown, first_line_indent)

    # Result iterator

    def capi_result_iterator_delete(self, handle: LPTessResultIterator):
        self.TessResultIteratorDelete(handle)

    def capi_result_iterator_copy(
            self,
            handle: LPTessResultIterator) -> LPTessResultIterator:
        return self.TessResultIteratorCopy(handle)

    def capi_result_iterator_get_page_iterator(
            self,
            handle: LPTessResultIterator) -> LPTessPageIterator:
        return self.TessResultIteratorGetPageIterator(handle)

    def capi_result_iterator_get_page_iterator_const(
            self,
            handle: LPTessResultIterator) -> LPTessPageIterator:
        return self.TessResultIteratorGetPageIteratorConst(handle)

    def capi_result_iterator_get_choice_iterator(
            self,
            handle: LPTessResultIterator) -> LPTessChoiceIterator:
        return self.TessResultIteratorGetChoiceIterator(handle)

    def capi_result_iterator_next(self, handle: LPTessResultIterator,
                                  level: PageIteratorLevel) -> bool:
        return self.TessResultIteratorNext(handle, level)

    def capi_result_iterator_get_utf8_text(
            self, handle: LPTessResultIterator,
            level: PageIteratorLevel) -> LP_c_char:
        return self.TessResultIteratorGetUTF8Text(handle, level)

    def capi_result_iterator_confidence(self, handle: LPTessResultIterator,
                                        level: PageIteratorLevel) -> float:
        return self.TessResultIteratorConfidence(handle, level)

    def capi_result_iterator_word_recognition_language(
            self,
            handle: LPTessResultIterator) -> bytes:
        return self.TessResultIteratorWordRecognitionLanguage(handle)

    def capi_result_iterator_word_font_attributes(self,
                                                  handle: LPTessResultIterator,
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

    def capi_result_iterator_word_is_from_dictionary(
            self,
            handle: LPTessResultIterator) -> bool:
        return self.TessResultIteratorWordIsFromDictionary(handle)

    def capi_result_iterator_word_is_numeric(
            self,
            handle: LPTessResultIterator) -> bool:
        return self.TessResultIteratorWordIsNumeric(handle)

    def capi_result_iterator_symbol_is_superscript(
            self,
            handle: LPTessResultIterator) -> bool:
        return self.TessResultIteratorSymbolIsSuperscript(handle)

    def capi_result_iterator_symbol_is_subscript(
            self,
            handle: LPTessResultIterator) -> bool:
        return self.TessResultIteratorSymbolIsSubscript(handle)

    def capi_result_iterator_symbol_is_dropcap(
            self,
            handle: LPTessResultIterator) -> bool:
        return self.TessResultIteratorSymbolIsDropcap(handle)

    def capi_choice_iterator_delete(self, handle: LPTessChoiceIterator):
        self.TessChoiceIteratorDelete(handle)

    def capi_choice_iterator_next(self, handle: LPTessChoiceIterator) -> bool:
        return self.TessChoiceIteratorNext(handle)

    def capi_choice_iterator_get_utf8_text(
            self, handle: LPTessChoiceIterator) -> bytes:
        return self.TessChoiceIteratorGetUTF8Text(handle)

    def capi_choice_iterator_confidence(self,
                                        handle: LPTessChoiceIterator) -> float:
        return self.TessChoiceIteratorConfidence(handle)

    # Progress monitor

    def capi_monitor_create(self) -> LPETEXT_DESC:
        return self.TessMonitorCreate()

    def capi_monitor_delete(self, monitor: LPETEXT_DESC):
        self.TessMonitorDelete(monitor)

    def capi_monitor_set_cancel_func(self, monitor: LPETEXT_DESC,
                                     cancelFunc: TessCancelFunc):
        self.TessMonitorSetCancelFunc(monitor, cancelFunc)

    def capi_monitor_set_cancel_this(self, monitor: LPETEXT_DESC,
                                     cancelThis: c_void_p):
        self.TessMonitorSetCancelThis(monitor, cancelThis)

    def capi_monitor_get_cancel_this(self, monitor: LPETEXT_DESC) -> c_void_p:
        return self.TessMonitorGetCancelThis(monitor)

    def capi_monitor_set_progress_func(self, monitor: LPETEXT_DESC,
                                       progressFunc: TessProgressFunc):
        self.TessMonitorSetProgressFunc(monitor, progressFunc)

    def capi_monitor_get_progress(self, monitor: LPETEXT_DESC) -> int:
        return self.TessMonitorGetProgress(monitor)

    def capi_monitor_set_deadline_msecs(self, monitor: LPETEXT_DESC,
                                        deadline: int):
        self.TessMonitorSetDeadlineMSecs(monitor, deadline)


TESSERACT_API = TessCAPI(TESS_DLL)
