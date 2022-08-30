# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 13:41:23 2022

@author: 皓
"""
import os.path as osp
import weakref
from ctypes import c_void_p
from typing import Callable, Any
from .common import TESSDATA_PREFIX
from .datatype import BaseObject
from .leptonica_capi import LPBoxa, LPPixa, LPPix
from .tesseract_capi import (OcrEngineMode, PageSegMode, PolyBlockType,
                             PageIteratorLevel,
                             TessProgressFunc, TessCancelFunc)
from .tesseract_papi import (BaseAPI, ProgressMonitorAPI, RendererAPI,
                             PageIteratorAPI, ResultIteratorAPI,
                             ChoiceIteratorAPI,
                             OrientationScript, Bounding, Font)


class BaseTessObject(BaseObject):

    def __init__(self):
        super().__init__(self.create())

    def create(self):
        return self.API.create()


class BaseIterObject(BaseObject):

    def __init__(self, handle, parent=None):
        super().__init__(handle)
        self.parent = parent if parent is None else weakref.ref(parent)

    def __del__(self):
        if self.parent is not None and self.parent() is None:
            return
        super().__del__()


class CopyIterator(BaseIterObject):

    def copy(self):
        return self.API.copy(self.handle)

    def __copy__(self):
        handle = self.copy(self.handle)
        return self.__class__(handle)


class ResultRenderer(BaseObject):
    API = RendererAPI
    CREATE_FUNC = {
        'text': API.text_renderer_create,
        'hocr': API.hocr_renderer_create,
        'alto': API.alto_renderer_create,
        'tsv': API.tsv_renderer_create,
        'pdf': API.pdf_renderer_create,
        'unlv': API.unlv_renderer_create,
        'box': API.box_text_renderer_create,
        'lstm': API.lstm_box_renderer_create,
        'word': API.word_str_box_renderer_create
    }

    def __init__(self, handle, filetype=None):
        super().__init__(handle)
        self.filetype = filetype

    @classmethod
    def create(cls, outputbase: str, filetype: str, *args) -> 'ResultRenderer':
        func_name = f'{filetype.lower()}_renderer_create'
        if hasattr(cls.API, func_name):
            func = getattr(cls.API, func_name)
        elif filetype in cls.CREATE_FUNC:
            func = cls.CREATE_FUNC[filetype]
        else:
            raise AttributeError('filetype must be in {}'.format(
                ','.join(cls.CREATE_FUNC)))
        result = func(outputbase, *args)
        return cls(result)

    def insert(self, next_: 'ResultRenderer'):
        self.API.insert(self.handle, next_)

    def next(self) -> 'ResultRenderer':
        result = self.API.next(self.handle)
        return self.__class__(result)

    def extention(self) -> str:
        return self.API.extention(self.handle)

    def title(self) -> str:
        return self.API.title(self.handle)

    def begin_document(self, title: str) -> bool:
        return self.API.begin_document(self.handle, title)

    def end_document(self) -> bool:
        return self.API.end_document(self.handle)

    def add_image(self, api) -> bool:
        return self.API.add_image(self.handle, api)

    def image_num(self) -> int:
        return self.API.image_num(self.handle)


class PageIterator(BaseIterObject):
    API = PageIteratorAPI

    def begin(self):
        self.API.begin(self.handle)

    def next(self, level: PageIteratorLevel) -> bool:
        return self.API.next(self.handle, level)

    def is_at_beginning_of(self, level: PageIteratorLevel) -> bool:
        return self.API.is_at_beginning_of(self.handle, level)

    def is_at_final_element(self, level: PageIteratorLevel,
                            element: PageIteratorLevel) -> bool:
        return self.API.is_at_final_element(self.handle, level, element)

    def bounding_box(self, level: PageIteratorLevel) -> Bounding:
        return self.API.bounding_box(self.handle, level)

    def block_type(self) -> PolyBlockType:
        return self.API.block_type(self.handle)

    def get_binary_image(self, level: PageIteratorLevel) -> LPPix:
        return self.API.get_binary_image(self.handle, level)

    def get_image(self, level: PageIteratorLevel, padding: int,
                  original_image: LPPix) -> LPPix:
        return self.API.get_image(self.handle, level, padding, original_image)

    def baseline(self, level: PageIteratorLevel) -> bool:
        return self.API.baseline(self.handle, level)

    def orientation(self) -> tuple[int, int, int, float]:
        return self.API.orientation(self.handle)

    def paragraph_info(self) -> tuple[int, bool, bool, int]:
        return self.API.paragraph_info(self.handle)


class ChoiceIterator(BaseIterObject):
    API = ChoiceIteratorAPI

    def next(self) -> bool:
        return self.API.next(self.handle)

    def get_utf8_text(self) -> str:
        return self.API.get_utf8_text(self.handle)

    def confidence(self) -> float:
        return self.API.confidence(self.handle)


class ResultIterator(CopyIterator):
    API = ResultIteratorAPI

    def get_page_iterator(self) -> PageIterator:
        handle = self.API.get_page_iterator(self.handle)
        if not handle:
            return None
        return PageIterator(handle, self)

    def get_page_iterator_const(self) -> PageIterator:
        handle = self.API.get_page_iterator_const(self.handle)
        if not handle:
            return None
        return PageIterator(handle, self)

    def get_choice_iterator(self) -> ChoiceIterator:
        handle = self.API.get_choice_iterator(self.handle)
        if not handle:
            return None
        return ChoiceIterator(handle, self)

    def next(self, level: PageIteratorLevel) -> bool:
        return self.API.next(self.handle, level)

    def get_utf8_text(self, level: PageIteratorLevel) -> str:
        return self.API.get_utf8_text(self.handle, level)

    def confidence(self, level: PageIteratorLevel) -> float:
        return self.API.confidence(self.handle, level)

    def word_recognition_language(self) -> bytes:
        return self.API.word_recognition_language(self.handle)

    def word_font_attributes(self) -> Font:
        return self.API.word_font_attributes(self.handle)

    def word_is_from_dictionary(self) -> bool:
        return self.API.word_is_from_dictionary(self.handle)

    def word_is_numeric(self) -> bool:
        return self.API.word_is_numeric(self.handle)

    def symbol_is_superscript(self) -> bool:
        return self.API.symbol_is_superscript(self.handle)

    def symbol_is_subscript(self) -> bool:
        return self.API.symbol_is_subscript(self.handle)

    def symbol_is_dropcap(self) -> bool:
        return self.API.symbol_is_dropcap(self.handle)


class MutableIterator(ResultIterator):
    pass


def wrapper_cancel_func(func):

    @TessCancelFunc
    def wrapper(cancel_this: c_void_p, words: int) -> bool:
        return func(cancel_this, words)
    return wrapper


def wrapper_progress_func(func):

    @TessProgressFunc
    def wrapper(this: c_void_p,
                left: int, right: int,
                top: int, bottom: int) -> bool:
        monitor = ProgressMonitor(this)
        return func(monitor, left, right, top, bottom)
    return wrapper


class ProgressMonitor(BaseTessObject):
    API = ProgressMonitorAPI
    INSTANCES = {}

    def __new__(cls, handle=None):
        if handle is not None and handle in cls.INSTANCES:
            instance_ref = cls.INSTANCES[handle]
            instance = instance_ref()
            if instance is None:
                return super().__new__(cls)
            return instance
        return super().__new__(cls)

    def __init__(self, handle=None):
        if handle is None:
            handle = self.create()
            self.__class__.INSTANCES[handle] = weakref.ref(self)
        self.handle = handle

    @property
    def progress(self) -> int:
        return self.API.get_progress(self.handle)

    @property
    def cancel_this(self) -> c_void_p:
        return self.API.get_cancel_this(self.handle)

    @cancel_this.setter
    def cancel_this(self, value: c_void_p):
        self.API.set_cancel_this(self.handle, value)

    def set_cancel_func(self, cancel_func: Callable[[c_void_p, int], bool]):
        if isinstance(cancel_func, TessProgressFunc):
            self.callable_cancel_func = None
            self.cancel_func = cancel_func
        else:
            self.callable_cancel_func = cancel_func
            self.cancel_func = wrapper_cancel_func(cancel_func)
        self.API.set_cancel_func(self.handle, self.cancel_func)

    def set_progress_func(self, progress_func: Callable[[Any, int, int,
                                                         int, int], bool]):
        if isinstance(progress_func, TessProgressFunc):
            self.callable_progress_func = None
            self.progress_func = progress_func
        else:
            self.callable_progress_func = progress_func
            self.progress_func = wrapper_progress_func(progress_func)
        self.API.set_progress_func(self.handle, self.progress_func)

    def set_deadline_msecs(self, deadline: int):
        self.API.set_deadline_msecs(self.handle, deadline)


class TessBase(BaseTessObject):
    API = BaseAPI

    def __init__(self,
                 datapath: str = TESSDATA_PREFIX,
                 language: str = 'eng',
                 mode: OcrEngineMode = None,
                 *configs, **kwargs):
        super().__init__()
        rc = self.init(datapath, language, mode, *configs, **kwargs)
        if rc:
            raise RuntimeError("Could not initialize tesseract.")

    @property
    def opencl_device(self) -> (c_void_p, int):
        return self.get_opencl_device()

    @property
    def input_name(self) -> str:
        return self.get_input_name()

    @input_name.setter
    def input_name(self, value: str):
        self.set_input_name(value)

    @property
    def input_image(self) -> LPPix:
        return self.get_input_image()

    @input_image.setter
    def input_image(self, value: LPPix):
        self.set_input_image(value)

    @property
    def source_y_resolution(self) -> int:
        return self.get_source_y_resolution()

    @property
    def datapath(self) -> str:
        return self.get_datapath()

    @property
    def init_languages(self) -> str:
        return self.get_init_languages()

    @property
    def loaded_languages(self) -> list[str]:
        return self.get_loaded_languages()

    @property
    def available_languages(self) -> list[str]:
        return self.get_available_languages()

    @property
    def page_seg_mode(self) -> PageSegMode:
        return self.get_page_seg_mode()

    @page_seg_mode.setter
    def page_seg_mode(self, mode: PageSegMode):
        self.set_page_seg_mode(mode)

    def get_opencl_device(self) -> tuple[c_void_p, int]:
        return self.API.get_opencl_device(self.handle)

    def set_input_name(self, name: str):
        self.API.set_input_name(self.handle, name)

    def get_input_name(self) -> str:
        return self.API.get_input_name(self.handle)

    def set_input_image(self, pix: LPPix):
        self.API.set_input_image(self.handle, pix)

    def get_input_image(self) -> LPPix:
        return self.API.get_input_image(self.handle)

    def get_source_y_resolution(self) -> int:
        return self.API.get_source_y_resolution(self.handle)

    def get_datapath(self) -> str:
        return self.API.get_datapath(self.handle)

    def set_output_name(self, name: str):
        self.API.set_output_name(self.handle, name)

    def set_variable(self, name: str, value: str) -> bool:
        return self.API.set_variable(self.handle, name, value)

    def set_debug_variable(self, name: str, value: str) -> bool:
        return self.API.set_debug_variable(self.handle, name, value)

    def get_int_variable(self, name: str) -> int:
        return self.API.get_int_variable(self.handle, name)

    def get_bool_variable(self, name: str) -> bool:
        return self.API.get_bool_variable(self.handle, name)

    def get_double_variable(self, name: str) -> float:
        return self.API.get_double_variable(self.handle, name)

    def get_string_variable(self, name: str) -> str:
        return self.API.get_string_variable(self.handle, name)

    def print_variables(self, fp):
        self.API.print_variables(self.handle, fp)

    def print_variables_tofile(self, filename: str) -> bool:
        return self.API.print_variables_tofile(self.handle, filename)

    def init(self, datapath: str, language: str, mode: OcrEngineMode,
             *configs, **kwargs):
        if not datapath:
            raise TypeError('The datapath is necessary, but get None.')
        if not language:
            raise TypeError('The language is necessary, but get None.')
        if osp.isdir(datapath):
            if mode is None:
                return self.init3(datapath, language)
            if not configs:
                return self.init2(datapath, language, mode)
            if not kwargs:
                return self.init1(datapath, language, mode, configs)
            if 'set_only_non_debug_params' in kwargs:
                set_only_non_debug_params = kwargs['set_only_non_debug_params']
                del kwargs['set_only_non_debug_params']
            else:
                set_only_non_debug_params = False
            return self.init4(datapath, language, mode, configs, kwargs,
                              set_only_non_debug_params)
        elif isinstance(datapath, bytes) or hasattr(datapath, 'read'):
            if isinstance(datapath, bytes):
                data = datapath
            else:
                data = datapath.read()
            if 'set_only_non_debug_params' in kwargs:
                set_only_non_debug_params = kwargs['set_only_non_debug_params']
                del kwargs['set_only_non_debug_params']
            else:
                set_only_non_debug_params = False
            return self.init5(data, language, mode, configs, kwargs,
                              set_only_non_debug_params)
        else:
            raise TypeError(
                'Datapath must be an exist dir, traindata bytes or IO.')

    def init1(self, datapath: str, language: str,
              oem: OcrEngineMode, configs: list[str]) -> int:
        return self.API.init1(self.handle, datapath, language, oem, configs)

    def init2(self, datapath: str, language: str, oem: OcrEngineMode) -> int:
        return self.API.init2(self.handle, datapath, language, oem)

    def init3(self, datapath: str, language: str) -> int:
        return self.API.init3(self.handle, datapath, language)

    def init4(self, datapath: str, language: str, mode: OcrEngineMode,
              configs: list[str], variables: dict[str, str],
              set_only_non_debug_params: bool) -> int:
        return self.API.init4(self.handle, datapath, language, mode,
                              configs, variables, set_only_non_debug_params)

    def init5(self, data: bytes, language: str, mode: OcrEngineMode,
              configs: list[str], variables: dict[str, str],
              set_only_non_debug_params: bool) -> int:
        return self.API.init5(self.handle, data, language, mode,
                              configs, variables, set_only_non_debug_params)

    def get_init_languages(self) -> str:
        return self.API.get_init_languages(self.handle)

    def get_loaded_languages(self) -> list[str]:
        return self.API.get_loaded_languages(self.handle)

    def get_available_languages(self) -> list[str]:
        return self.API.get_available_languages(self.handle)

    def init_for_analyse_page(self):
        self.API.init_for_analyse_page(self.handle)

    def read_config_file(self, filename: str):
        self.API.read_config_file(self.handle, filename)

    def read_debug_config_file(self, filename: str):
        self.API.read_debug_config_file(self.handle, filename)

    def set_page_seg_mode(self, mode: PageSegMode):
        self.API.set_page_seg_mode(self.handle, mode)

    def get_page_seg_mode(self) -> PageSegMode:
        return self.API.get_page_seg_mode(self.handle)

    def rect(self, imagedata: bytes, bytes_per_pixel: int, bytes_per_line: int,
             left: int, top: int, width: int, height: int) -> str:
        return self.API.rect(self.handle, imagedata, bytes_per_pixel,
                             bytes_per_line, left, top, width, height)

    def clear_adaptive_classifier(self):
        self.API.clear_adaptive_classifier(self.handle)

    def set_image(self, imagedata: bytes, width: int, height: int,
                  bytes_per_pixel: int, bytes_per_line: int):
        self.API.set_image(self.handle, imagedata, width, height,
                           bytes_per_pixel, bytes_per_line)

    def set_image2(self, pix: LPPix):
        self.API.set_image2(self.handle, pix)

    def set_source_resolution(self, ppi: int):
        self.API.set_source_resolution(self.handle, ppi)

    def set_rectangle(self, left: int, top: int, width: int, height: int):
        self.API.set_rectangle(self.handle, left, top, width, height)

    def get_thresholded_image(self) -> LPPix:
        return self.API.get_thresholded_image(self.handle)

    def get_regions(self) -> tuple[LPBoxa, LPPixa]:
        return self.API.get_regions(self.handle)

    def get_textlines(self) -> tuple[LPBoxa, LPPixa, int]:
        return self.API.get_textlines(self.handle)

    def get_textlines1(self, raw_image: bool,
                       raw_padding: int) -> tuple[LPBoxa, LPPixa, int, int]:
        return self.API.get_textlines1(self.handle, raw_image, raw_padding)

    def get_strips(self) -> tuple[LPBoxa, LPPixa, int]:
        return self.API.get_strips(self.handle)

    def get_words(self) -> tuple[LPBoxa, LPPixa]:
        return self.API.get_words(self.handle)

    def get_connected_components(self) -> tuple[LPBoxa, LPPixa]:
        return self.API.get_connected_components(self.handle)

    def get_component_images(self, level: PageIteratorLevel,
                             text_only: bool) -> tuple[LPBoxa, LPPixa, int]:
        return self.API.get_component_images(self.handle, level, text_only)

    def get_component_images1(self, level: PageIteratorLevel, text_only: bool,
                              raw_image: bool,
                              raw_padding: int) -> tuple[LPBoxa, LPPixa,
                                                         int, int]:
        return self.API.get_component_images1(self.handle, level, text_only,
                                              raw_image, raw_padding)

    def get_thresholded_image_scale_factor(self) -> int:
        return self.API.get_thresholded_image_scale_factor(self.handle)

    def analyse_layout(self) -> PageIterator:
        iterator = self.API.analyse_layout(self.handle)
        if not iterator:
            return None
        return PageIterator(iterator)

    def recognize(self, monitor: ProgressMonitor = None) -> int:
        return self.API.recognize(self.handle, monitor)

    def process_pages(self, filename: str, retry_config: str,
                      timeout_millisec: int, renderer: ResultRenderer) -> bool:
        return self.API.process_pages(self.handle, filename, retry_config,
                                      timeout_millisec, renderer)

    def process_page(self, pix: LPPix, page_index: int, filename: bytes,
                     retry_config: bytes, timeout_millisec: int,
                     renderer: ResultRenderer) -> bool:
        return self.API.process_page(self.handle, pix, page_index, filename,
                                     retry_config, timeout_millisec,
                                     renderer)

    def get_iterator(self) -> ResultIterator:
        iterator = self.API.get_iterator(self.handle)
        if not iterator:
            return None
        return ResultIterator(iterator)

    def get_mutable_iterator(self) -> MutableIterator:
        iterator = self.API.get_mutable_iterator(self.handle)
        if not bool(iterator):
            return None
        return MutableIterator(iterator)

    def get_utf8_text(self) -> str:
        return self.API.get_utf8_text(self.handle)

    def get_hocr_text(self, page_number: int) -> str:
        return self.API.get_hocr_text(self.handle, page_number)

    def get_alto_text(self, page_number: int) -> str:
        return self.API.get_alto_text(self.handle, page_number)

    def get_tsv_text(self, page_number: int) -> str:
        return self.API.get_tsv_text(self.handle, page_number)

    def get_box_text(self, page_number: int) -> str:
        return self.API.get_box_text(self.handle, page_number)

    def get_lstm_box_text(self, page_number: int) -> str:
        return self.API.get_lstm_box_text(self.handle, page_number)

    def get_word_str_box_text(self, page_number: int) -> str:
        return self.API.get_word_str_box_text(self.handle, page_number)

    def get_unlv_text(self) -> str:
        return self.API.get_unlv_text(self.handle)

    def mean_text_conf(self) -> int:
        return self.API.mean_text_conf(self.handle)

    def all_word_confidences(self) -> list[int]:
        return self.API.all_word_confidences(self.handle)

    def adapt_toword_str(self, mode: PageSegMode, wordstr: str) -> bool:
        return self.API.adapt_toword_str(self.handle, mode, wordstr)

    def clear(self):
        self.API.clear(self.handle)

    def end(self):
        self.API.end(self.handle)

    def is_valid_word(self, word: str) -> int:
        return self.API.is_valid_word(self.handle, word)

    def get_text_direction(self) -> tuple[int, float]:
        return self.API.get_text_direction(self.handle)

    def get_unichar(self, unichar_id: int) -> bytes:
        return self.API.get_unichar(self.handle, unichar_id)

    def clear_persistent_cache(self):
        self.API.clear_persistent_cache(self.handle)

    def detect_orientation_script(self) -> OrientationScript:
        return self.API.detect_orientation_script(self.handle)

    def set_min_orientation_margin(self, margin: float):
        self.API.set_min_orientation_margin(self.handle, margin)

    def num_dawgs(self) -> int:
        return self.API.num_dawgs(self.handle)

    def oem(self) -> int:
        return self.API.oem(self.handle)

    def get_block_text_orientations(self) -> tuple[int, bool]:
        return self.API.get_block_text_orientations(self.handle)
