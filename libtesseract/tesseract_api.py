# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 08:45:54 2021

@author: 皓
"""
import os.path as osp
import sys
from ctypes import (POINTER, pointer, byref, cast, c_float, c_double, c_int,
                    c_bool, c_void_p, c_char_p)
import locale
from functools import wraps
from .common import TESSDATA_PREFIX
from .error import TesseractError
from .leptonica_capi import Pix
from .tesseract_capi import (TESSERACT_API, OcrEngineMode, PageSegMode,
                             PageIteratorLevel, Orientation, WritingDirection,
                             TextlineOrder, ParagraphJustification)
from .libc import fdopen


class CommonAPI:
    ENCODING = 'ascii'

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
        if hasattr(TESSERACT_API, attr):
            return getattr(TESSERACT_API, attr)
        raise AttributeError(
            "'{}' object has no attribute '{}'".format(self.__class__.__name__,
                                                       attr))


CommonAPI.setlocale()


class HandleAPI:
    HANDLES = {}

    @classmethod
    def get_point(cls, obj):
        if isinstance(obj, c_void_p):
            return obj
        if hasattr(obj, 'handle'):
            if isinstance(obj.handle, c_void_p):
                return obj.handle
        return obj

    def __init__(self, handle):
        self.handle = handle
        self.HANDLES[self.handle] = True

    def close(self):
        print(self.handle, self.HANDLES)
        if self.handle:
            if self.handle in self.HANDLES:
                print('delete', self.handle)
                self.delete(self.handle)
                del self.HANDLES[self.handle]
            self.handle = None

    def __del__(self):
        self.close()


class ContextAPI(HandleAPI, CommonAPI):
    def __init__(self):
        super().__init__(self.create())

    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        self.close()


class GeneralAPI(CommonAPI):

    def version(self) -> str:
        return self.decode(self.capi_version())

    def delete_text(self, text: bytes):
        self.capi_delete_text(text)

    def delete_text_array(self, arr: bytes):
        self.capi_delete_text_array(arr)

    def delete_int_array(self, arr: int):
        self.capi_delete_int_array(arr)


def pythonic_classmethod(func):

    @classmethod
    @wraps(func)
    def wrapper(*args, **kwargs):
        cls, *_ = args
        result = func(*args, **kwargs)
        return cls(result)
    return wrapper


def pythonic(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        self, *_ = args
        cls = self.__class__
        result = func(*args, **kwargs)
        return cls(result)
    return wrapper


class RendererAPI(HandleAPI, CommonAPI):

    def delete(self, renderer):
        self.delete_result_renderer(self.get_point(renderer))

    def insert(self, renderer, next_):
        self.result_renderer_insert(self.get_point(renderer),
                                    self.get_point(next_))

    @pythonic
    def next(self):
        return self.result_renderer_next(self.handle)

    def extention(self) -> str:
        return self.result_renderer_extention(self.handle)

    def title(self) -> str:
        return self.result_renderer_title(self.handle)

    def begin_document(self, title: str) -> bool:
        return self.result_renderer_begin_document(self.handle, title)

    def end_document(self) -> bool:
        return self.result_renderer_end_document(self.handle)

    def add_image(self, api) -> bool:
        return self.result_renderer_add_image(self.handle, api)

    def image_num(self) -> int:
        return self.result_renderer_image_num(self.handle)

    @pythonic_classmethod
    def text_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_text_renderer_create(cls.encode(outputbase))

    @classmethod
    def hocr_renderer_create(cls, outputbase: str, font_info: bool = False):
        if font_info is False:
            return cls._hocr_renderer_create(outputbase)
        else:
            return cls._hocr_renderer_create2(outputbase, font_info)

    @pythonic_classmethod
    def _hocr_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_hocr_renderer_create(cls.encode(outputbase))

    @pythonic_classmethod
    def _hocr_renderer_create2(cls, outputbase: str, font_info: bool):
        return TESSERACT_API.capi_hocr_renderer_create2(cls.encode(outputbase),
                                                        font_info)

    @pythonic_classmethod
    def alto_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_alto_renderer_create(cls.encode(outputbase))

    @pythonic_classmethod
    def tsv_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_tsv_renderer_create(cls.encode(outputbase))

    @pythonic_classmethod
    def pdf_renderer_create(cls, outputbase: str, datadir: str,
                            textonly: bool):
        return TESSERACT_API.capi_pdf_renderer_create(cls.encode(outputbase),
                                                      cls.encode(datadir),
                                                      textonly)

    @pythonic_classmethod
    def unlv_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_unlv_renderer_create(cls.encode(outputbase))

    @pythonic_classmethod
    def box_text_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_box_text_renderer_create(
            cls.encode(outputbase))

    @pythonic_classmethod
    def lstm_box_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_lstm_box_renderer_create(
            cls.encode(outputbase))

    @pythonic_classmethod
    def word_str_box_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_word_str_box_renderer_create(
            cls.encode(outputbase))

    @classmethod
    def delete_result_renderer(cls, renderer):
        TESSERACT_API.capi_delete_result_renderer(renderer)

    @classmethod
    def result_renderer_insert(cls, renderer, next_):
        TESSERACT_API.capi_result_renderer_insert(renderer, next_)

    @classmethod
    def result_renderer_next(cls, renderer):
        return TESSERACT_API.capi_result_renderer_next(renderer)

    @classmethod
    def result_renderer_begin_document(cls, renderer,
                                       title: str) -> bool:
        return TESSERACT_API.capi_result_renderer_begin_document(
            renderer,
            cls.encode(title))

    @classmethod
    def result_renderer_add_image(cls, renderer, api) -> bool:
        return TESSERACT_API.capi_result_renderer_add_image(renderer, api)

    @classmethod
    def result_renderer_end_document(cls, renderer) -> bool:
        return TESSERACT_API.capi_result_renderer_end_document(renderer)

    @classmethod
    def result_renderer_extention(cls, renderer) -> str:
        ret = TESSERACT_API.capi_result_renderer_extention(renderer)
        return cls.decode(ret)

    @classmethod
    def result_renderer_title(cls, renderer) -> str:
        ret = TESSERACT_API.capi_result_renderer_title(renderer)
        return cls.decode(ret)

    @classmethod
    def result_renderer_image_num(cls, renderer) -> int:
        return TESSERACT_API.capi_result_renderer_image_num(renderer)


class BaseAPI(ContextAPI):

    def __init__(self,
                 datapath: str = TESSDATA_PREFIX,
                 language: str = 'eng',
                 mode: OcrEngineMode = None,
                 *configs, **kwargs):
        super().__init__()
        rc = self.init(datapath, language, mode, *configs, **kwargs)
        if rc:
            raise RuntimeError("Could not initialize tesseract.")

    def init(self, datapath: str, language: str,
             mode: OcrEngineMode, *configs, **kwargs):
        if not datapath:
            raise TypeError(
                'Datapath is necessary, but get None.')
        language_value = self.encode(language) if language else b'eng'
        if osp.exists(datapath):
            datapath_value = self.encode(datapath)
            if mode is None:
                return self.capi_base_api_init3(self.handle, datapath_value,
                                                language_value)
            if not configs:
                return self.capi_base_api_init2(self.handle, datapath_value,
                                                language_value, mode)
            if not kwargs:
                return self.capi_base_api_init1(self.handle, datapath_value,
                                                language_value, mode,
                                                configs, len(configs))
            if 'set_only_non_debug_params' in kwargs:
                set_only_non_debug_params = kwargs['set_only_non_debug_params']
                del kwargs['set_only_non_debug_params']
            else:
                set_only_non_debug_params = False
            return self.capi_base_api_init4(self.handle,
                                            datapath_value,
                                            language_value,
                                            mode,
                                            configs, len(configs),
                                            tuple(kwargs.keys()),
                                            tuple(kwargs.values()),
                                            len(kwargs),
                                            set_only_non_debug_params)
        else:
            raise TypeError('Datapath must be an exist dir for traindata.')

    def create(self):
        return self.capi_base_api_create()

    def delete(self, handle):
        print('capi_base_api_delete', handle)
        self.capi_base_api_delete(handle)

    def get_open_cldevice(self, device) -> int:
        return self.capi_base_api_get_open_cldevice(self.handle, device)

    def set_input_name(self, name: str):
        self.capi_base_api_set_input_name(self.handle, self.encode(name))

    def get_input_name(self) -> str:
        ret = self.capi_base_api_get_input_name(self.handle)
        return self.decode(ret)

    def set_input_image(self, pix):
        self.capi_base_api_set_input_image(self.handle, pix)

    def get_input_image(self):
        self.capi_base_api_get_input_image(self.handle)

    def get_source_y_resolution(self) -> int:
        return self.capi_base_api_get_source_y_resolution(self.handle)

    def get_datapath(self) -> str:
        ret = self.capi_base_api_get_datapath(self.handle)
        return self.decode(ret)

    def set_output_name(self, name: str):
        self.capi_base_api_set_output_name(self.handle, self.encode(name))

    def set_is_numeric(self, mode):
        whitelist = "0123456789." if mode else ''
        return self.set_variable("tessedit_char_whitelist", whitelist)

    def set_debug_file(self, filename):
        return self.set_variable("debug_file", filename)

    def set_variable(self, name: str, value: str) -> bool:
        name_value = self.encode(name)
        value_value = self.encode(value)
        return self.capi_base_api_set_variable(self.handle,
                                               name_value,
                                               value_value)

    def set_debug_variable(self, name: bytes, value: bytes) -> bool:
        return self.capi_base_api_set_debug_variable(self.handle, name, value)

    def get_int_variable(self, name: str) -> int:
        value = c_int()
        ret = self.capi_base_api_get_int_variable(self.handle,
                                                  self.encode(name),
                                                  pointer(value))
        if not ret:
            return None
        return value.value

    def get_bool_variable(self, name: str) -> bool:
        value = c_bool()
        ret = self.capi_base_api_get_bool_variable(self.handle,
                                                   self.encode(name),
                                                   byref(value))
        if not ret:
            return None
        return value.value

    def get_double_variable(self, name: str) -> float:
        value = c_double()
        ret = self.capi_base_api_get_double_variable(self.handle,
                                                     self.encode(name),
                                                     byref(value))
        if not ret:
            return None
        return value.value

    def get_string_variable(self, name: str) -> str:
        ret = self.capi_base_api_get_string_variable(self.handle,
                                                     self.encode(name))
        return self.decode(ret)

    def print_variables(self, fp=sys.stdout):
        if hasattr(fp, 'fileno') and hasattr(fp, 'mode'):
            fileno = fp.fileno()
            mode = fp.mode
        elif isinstance(fp, int):
            fileno = fp
            mode = 'w'
        else:
            raise TypeError('fp type is not io or fileno:{}'.format(type(fp)))
        file_point = fdopen(fileno, mode)
        self.capi_base_api_print_variables(self.handle, file_point)

    def print_variables_tofile(self, filename: str) -> bool:
        return self.capi_base_api_print_variables_tofile(self.handle,
                                                         self.encode(filename))

    def get_init_languages(self) -> str:
        ret = self.capi_base_api_get_init_languages(self.handle)
        return self.decode(ret)

    def get_loaded_languages(self) -> list[str]:
        ret = self.capi_base_api_get_loaded_languages(self.handle)
        return [self.decode(x) for x in ret]

    def get_available_languages(self) -> list[str]:
        ret = self.capi_base_api_get_available_languages(self.handle)
        return [self.decode(x) for x in ret]

    def init_lang_mod(self, datapath: str, language: str) -> int:
        datapath_value = self.encode(datapath)
        language_value = self.encode(language)
        return self.capi_base_api_init_lang_mod(self.handle,
                                                datapath_value,
                                                language_value)

    def init_for_analyse_page(self):
        self.capi_base_api_init_for_analyse_page(self.handle)

    def read_config_file(self, filename: bytes):
        self.capi_base_api_read_config_file(self.handle, filename)

    def read_debug_config_file(self, filename: bytes):
        self.capi_base_api_read_debug_config_file(self.handle, filename)

    def set_page_seg_mode(self, mode: PageSegMode):
        self.capi_base_api_set_page_seg_mode(self.handle, mode)

    def get_page_seg_mode(self) -> PageSegMode:
        ret = self.capi_base_api_get_page_seg_mode(self.handle)
        return PageSegMode(ret)

    def rect(self, imagedata: bytes,
             bytes_per_pixel: int,
             bytes_per_line: int,
             left: int,
             top: int,
             width: int,
             height: int) -> str:
        return self.capi_base_api_rect(self.handle, imagedata,
                                       bytes_per_pixel, bytes_per_line,
                                       left, top,
                                       width, height).encode('utf-8')

    def clear_adaptive_classifier(self):
        self.capi_base_api_clear_adaptive_classifier(self.handle)

    def set_image(self, imagedata: bytes,
                  width: int,
                  height: int,
                  bytes_per_pixel: int,
                  bytes_per_line: int):

        self.capi_base_api_set_image(self.handle, imagedata,
                                     width, height,
                                     bytes_per_pixel, bytes_per_line)

    def set_image2(self, pix: POINTER(Pix)):
        self.capi_base_api_set_image2(self.handle, pix)

    def set_source_resolution(self, ppi: int):
        self.capi_base_api_set_source_resolution(self.handle, int(ppi))

    def set_rectangle(self,
                      left: int, top: int,
                      width: int, height: int):
        self.capi_base_api_set_rectangle(self.handle, left, top, width, height)

    def get_thresholded_image_scale_factor(self):
        return self.capi_base_api_get_thresholded_image_scale_factor()

    def analyse_layout(self):
        return self.capi_base_api_analyse_layout()

    def recognize(self, monitor=None):
        return self.capi_base_api_recognize(self.handle, monitor)

    def process_pages(self,
                      filename: str,
                      retry_config: str,
                      timeout_millisec: int,
                      renderer) -> bool:
        return self.capi_base_api_process_pages(self.handle,
                                                self.encode(filename),
                                                self.encode(retry_config),
                                                timeout_millisec,
                                                self.get_point(renderer))

    def process_page(self,
                     pix: POINTER(Pix),
                     page_index: int,
                     filename: bytes,
                     retry_config: bytes,
                     timeout_millisec: int, renderer) -> bool:
        return self.capi_base_api_process_page(self.handle,
                                               pix,
                                               page_index,
                                               self.encode(filename),
                                               self.encode(retry_config),
                                               timeout_millisec,
                                               self.get_point(renderer))

    def get_iterator(self):
        iterator = self.capi_base_api_get_iterator(self.handle)
        if iterator is None:
            return
        return ResultIterator(iterator)

    def get_mutable_iterator(self):
        return self.capi_base_api_get_mutable_iterator(self.handle)

    def get_utf8_text(self) -> str:
        ret = self.capi_base_api_get_utf8_text(self.handle)
        return self.decode_utf8(ret)

    def get_hocr_text(self, page_number: int) -> str:
        ret = self.capi_base_api_get_hocr_text(self.handle,
                                               page_number)
        return self.decode(ret)

    def get_alto_text(self, page_number: int) -> str:
        ret = self.capi_base_api_get_alto_text(self.handle,
                                               page_number)
        return self.decode(ret)

    def get_tsv_text(self, page_number: int) -> str:
        ret = self.capi_base_api_get_tsv_text(self.handle,
                                              page_number)
        return self.decode(ret)

    def get_box_text(self, page_number: int) -> str:
        ret = self.capi_base_api_get_box_text(self.handle,
                                              page_number)
        return self.decode(ret)

    def get_lstm_box_text(self, page_number: int) -> str:
        ret = self.capi_base_api_get_lstm_box_text(self.handle,
                                                   page_number)
        return self.decode(ret)

    def get_word_str_box_text(self,
                              page_number: int) -> str:
        ret = self.capi_base_api_get_word_str_box_text(self.handle,
                                                       page_number)
        return self.decode(ret)

    def get_unlv_text(self) -> str:
        ret = self.capi_base_api_get_unlv_text(self.handle)
        return self.decode(ret)

    def mean_text_conf(self) -> int:
        return self.capi_base_api_mean_text_conf(self.handle)

    def all_word_confidences(self) -> int:
        return self.capi_base_api_all_word_confidences(self.handle)

    def adapt_toword_str(self, mode: PageSegMode,
                         wordstr: bytes) -> bool:
        return self.capi_base_api_adapt_toword_str(self.handle, mode, wordstr)

    def clear(self):
        self.capi_base_api_clear(self.handle)

    def end(self):
        self.capi_base_api_end(self.handle)

    def isvalid_word(self, word: bytes) -> int:
        return self.capi_base_api_isvalid_word(self.handle, word)

    def get_text_direction(self, out_offset: int,
                           out_slope: float) -> bool:
        return self.capi_base_api_get_text_direction(self.handle,
                                                     out_offset,
                                                     out_slope)

    def get_unichar(self, unichar_id: int) -> bytes:
        return self.capi_base_api_get_unichar(self.handle, unichar_id)

    def clear_persistent_cache(self):
        self.capi_base_api_clear_persistent_cache(self.handle)

    def detect_orientation_script(self) -> bool:
        orientation_deg = c_int()
        orientation_confidence = c_float()
        script_name = pointer(c_char_p())
        script_conf = c_float()
        ret = self.capi_base_api_detect_orientation_script(
            self.handle,
            byref(orientation_deg),
            byref(orientation_confidence),
            script_name,
            byref(script_conf))
        if not ret:
            raise TesseractError("detect_orientation failed",
                                 "TessBaseAPIDetectOrientationScript() failed")
        print(script_name, script_name.contents,
              script_name.contents.value, script_conf.value)
        return {"orientation": orientation_deg.value,
                "orientation_enum": round(orientation_deg.value / 90),
                "confidence": orientation_confidence.value}

    def set_min_orientation_margin(self, margin: float):
        self.capi_base_api_set_min_orientation_margin(self.handle, margin)

    def num_dawgs(self) -> int:
        return self.capi_base_api_num_dawgs(self.handle)

    def oem(self) -> int:
        return self.capi_base_api_oem(self.handle)

    def get_block_text_orientations(self, handle,
                                    block_orientation: int,
                                    vertical_writing: bool):
        self.capi_base_get_block_text_orientations(
            handle, block_orientation, vertical_writing)


class ProgressMonitor(ContextAPI):

    def create(self):
        return self.capi_monitor_create()

    def delete(self, monitor):
        self.capi_monitor_delete(monitor)

    def set_cancel_func(self, cancelFunc):
        self.capi_monitor_set_cancel_func(self.handle, cancelFunc)

    def set_cancel_this(self, cancelThis):
        self.capi_monitor_set_cancel_this(self.handle, cancelThis)

    def get_cancel_this(self):
        return self.capi_monitor_get_cancel_this(self.handle)

    def set_progress_func(self, progressFunc):
        self.capi_monitor_set_progress_func(self.handle, progressFunc)

    def get_progress(self) -> int:
        return self.capi_monitor_get_progress(self.handle)

    def set_deadline_msecs(self, deadline: int):
        self.capi_monitor_set_deadline_msecs(self.handle, deadline)


class BaseIterator(HandleAPI, CommonAPI):
    pass


class PageIterator(BaseIterator):

    def delete(self, handle):
        print('PageIterator', 'delete')
        self.capi_page_iterator_delete(handle)

    def copy(self, handle):
        return self.capi_page_iterator_copy(handle)

    def begin(self):
        self.capi_page_iterator_begin(self.handle)

    def next(self, level: PageIteratorLevel) -> bool:
        return self.capi_page_iterator_next(self.handle, level)

    def is_at_beginning_of(self, level: PageIteratorLevel) -> bool:
        return self.capi_page_iterator_isat_beginning_of(self.handle, level)

    def is_at_final_element(self, level: PageIteratorLevel,
                            element: PageIteratorLevel) -> bool:
        return self.capi_page_iterator_isat_final_element(self.handle,
                                                          level, element)

    def bounding_box(self, level: PageIteratorLevel) -> bool:
        left = c_int()
        left_p = pointer(left)
        top = c_int()
        top_p = pointer(top)
        right = c_int()
        right_p = pointer(right)
        bottom = c_int()
        bottom_p = pointer(bottom)
        ret = self.capi_page_iterator_bounding_box(self.handle, level,
                                                   left_p, top_p,
                                                   right_p, bottom_p)
        if not ret:
            raise TesseractError("bounding_box failed",
                                 "TessPageIteratorBoundingBox() failed")
        return left.value, top.value, right.value, bottom.value

    def block_type(self) -> int:
        return self.capi_page_iterator_block_type(self.handle)

    def get_binary_image(self, level: PageIteratorLevel):
        return self.capi_page_iterator_get_binary_image(self.handle, level)

    def get_image(self, level: PageIteratorLevel,
                  padding: int, original_image,
                  left: int, top: int):
        self.capi_page_iterator_get_image(
            self.handle, level, padding, original_image, left, top)

    def baseline(self, level: PageIteratorLevel,
                 x1: int, y1: int,
                 x2: int, y2: int) -> bool:
        return self.capi_page_iterator_baseline(self.handle, level,
                                                x1, y1, x2, y2)

    def orientation(self, orientation: Orientation,
                    writing_direction: WritingDirection,
                    textline_order: TextlineOrder,
                    deskew_angle: float):
        self.capi_page_iterator_orientation(
            self.handle, orientation, writing_direction, textline_order,
            deskew_angle)

    def paragraph_info(
            self,
            justification: ParagraphJustification,
            is_list_item: bool, is_crown: bool,
            first_line_indent: int):
        self.capi_page_iterator_paragraph_info(
            self.handle, justification, is_list_item,
            is_crown, first_line_indent)

    def __copy__(self):
        _cls = self.__class__
        handle = self.copy(self.handle)
        return _cls(handle)

    def __iter__(self):
        return self

    def __next__(self):
        if self.data2 < self.data1:
            self.data2 += 1
            return self.data2
        else:
            raise StopIteration


class ResultIterator(BaseIterator):

    def delete(self, handle):
        print('ResultIterator', 'delete')
        self.capi_result_iterator_delete(handle)

    def copy(self, handle):
        return self.capi_result_iterator_copy(handle)

    def get_page_iterator(self):
        iterator = self.capi_result_iterator_get_page_iterator(self.handle)
        if iterator is None:
            return
        return PageIterator(iterator)

    def get_page_iterator_const(self):
        return self.capi_result_iterator_get_page_iterator_const(self.handle)

    def get_choice_iterator(self):
        return self.capi_result_iterator_get_choice_iterator(self.handle)

    def next(self, level: PageIteratorLevel) -> bool:
        return self.capi_result_iterator_next(self.handle, level)

    def get_utf8_text(self, level: PageIteratorLevel) -> str:
        ret = self.capi_result_iterator_get_utf8text(self.handle, level)
        return self.decode_utf8(ret)

    def confidence(self, level: PageIteratorLevel) -> float:
        return self.capi_result_iterator_confidence(self.handle, level)

    def word_recognition_language(self) -> bytes:
        return self.capi_result_iterator_word_recognition_language(self.handle)

    def word_font_attributes(self,
                             is_bold: bool,
                             is_italic: bool,
                             is_underlined: bool,
                             is_monospace: bool,
                             is_serif: bool,
                             is_smallcaps: bool,
                             pointsize: int,
                             font_id: int) -> bytes:
        return self.capi_result_iterator_word_font_attributes(
            self.handle, is_bold,
            is_italic,
            is_underlined,
            is_monospace,
            is_serif,
            is_smallcaps,
            pointsize, font_id)

    def word_isfrom_dictionary(self) -> bool:
        return self.capi_result_iterator_word_isfrom_dictionary(self.handle)

    def word_isnumeric(self) -> bool:
        return self.capi_result_iterator_word_isnumeric(self.handle)

    def symbol_issuperscript(self) -> bool:
        return self.capi_result_iterator_symbol_issuperscript(self.handle)

    def symbol_issubscript(self) -> bool:
        return self.capi_result_iterator_symbol_issubscript(self.handle)

    def symbol_isdropcap(self) -> bool:
        return self.capi_result_iterator_symbol_isdropcap(self.handle)

    def __copy__(self):
        _cls = self.__class__
        handle = self.copy(self.handle)
        return _cls(handle)


class ChoiceIterator(BaseIterator):

    def delete(self, handle):
        self.capi_choice_iterator_delete(handle)

    def next(self) -> bool:
        return self.capi_choice_iterator_next(self.handle)

    def get_utf8_text(self) -> str:
        ret = self.capi_choice_iterator_get_utf8_text(self.handle)
        return self.decode_utf8(ret)

    def confidence(self) -> float:
        return self.capi_choice_iterator_confidence(self.handle)


def main():
    pass


if __name__ == '__main__':
    main()
