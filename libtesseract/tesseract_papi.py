# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 08:45:54 2021

@author: 皓
"""
import sys
from typing import Callable
from collections import namedtuple
from ctypes import (POINTER, pointer, byref, c_float, c_double, c_int, c_bool,
                    c_void_p, c_char_p, cast)
from .datatype import (c_int_p, c_bool_p, LP_c_char,  CommonAPI, get_point,
                       get_point_value, list_to_array, dict_to_array)
from .error import TesseractError
from .leptonica_capi import LPBoxa, LPPix, LPPixa
from .tesseract_capi import (TESSERACT_API, OcrEngineMode, PageSegMode,
                             PageIteratorLevel, Orientation, WritingDirection,
                             TextlineOrder, ParagraphJustification,
                             PolyBlockType,
                             LPTessBaseAPI,
                             LPTessResultIterator,
                             LPTessPageIterator,
                             LPTessMutableIterator,
                             LPETEXT_DESC)
from .libc import fdopen


OrientationScript = namedtuple('OrientationScript',
                               ['degree', 'confidence',
                                'script_name', 'script_confidence'])

Bounding = namedtuple('Bounding', ['left', 'top', 'right', 'bottom'])
Baseline = namedtuple('Baseline', ['x1', 'y1', 'x2', 'y2'])
Font = namedtuple('Font', ['name', 'is_italic', 'is_underlined',
                           'is_monospace', 'is_serif', 'is_smallcaps',
                           'pointsize', 'font_id'])


class GeneralAPI(CommonAPI):

    @classmethod
    def version(cls) -> str:
        ret = TESSERACT_API.capi_version()
        return cls.decode(ret)

    @classmethod
    def delete_text(cls, text: c_char_p):
        TESSERACT_API.capi_delete_text(text)

    @classmethod
    def delete_text_array(cls, arr: POINTER(c_char_p)):
        TESSERACT_API.capi_delete_text_array(arr)

    @classmethod
    def delete_int_array(cls, arr: c_int_p):
        TESSERACT_API.capi_delete_int_array(arr)

    @classmethod
    def get_text_value(cls, pdata: LP_c_char) -> bytes:
        assert isinstance(pdata, LP_c_char), "Arg pdata type isn't LP_c_char"
        data = cast(pdata, c_char_p)
        result = data.value
        cls.delete_text(data)
        return result

    @classmethod
    def get_int_list(cls, lp_lp_c_int: POINTER(c_int_p), n) -> list[int]:
        if not lp_lp_c_int:
            return []
        lp_c_int = lp_lp_c_int.contents
        if not lp_c_int:
            return []
        result = list(lp_c_int[:n])
        GeneralAPI.delete_int_array(lp_c_int)
        return result


class RendererAPI(CommonAPI):
    @classmethod
    def text_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_text_renderer_create(cls.encode(outputbase))

    @classmethod
    def hocr_renderer_create(cls, outputbase: str, font_info: bool = False):
        outputbase = cls.encode(outputbase)
        if font_info is False:
            return TESSERACT_API.capi_hocr_renderer_create(outputbase)
        else:
            return TESSERACT_API.capi_hocr_renderer_create2(outputbase,
                                                            font_info)

    @classmethod
    def alto_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_alto_renderer_create(cls.encode(outputbase))

    @classmethod
    def tsv_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_tsv_renderer_create(cls.encode(outputbase))

    @classmethod
    def pdf_renderer_create(cls, outputbase: str, datadir: str,
                            textonly: bool):
        return TESSERACT_API.capi_pdf_renderer_create(cls.encode(outputbase),
                                                      cls.encode(datadir),
                                                      textonly)

    @classmethod
    def unlv_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_unlv_renderer_create(cls.encode(outputbase))

    @classmethod
    def box_text_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_box_text_renderer_create(
            cls.encode(outputbase))

    @classmethod
    def lstm_box_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_lstm_box_renderer_create(
            cls.encode(outputbase))

    @classmethod
    def word_str_box_renderer_create(cls, outputbase: str):
        return TESSERACT_API.capi_word_str_box_renderer_create(
            cls.encode(outputbase))

    @classmethod
    def delete(cls, renderer):
        TESSERACT_API.capi_delete_result_renderer(renderer)

    @classmethod
    def insert(cls, renderer, next_):
        TESSERACT_API.capi_result_renderer_insert(renderer, get_point(next_))

    @classmethod
    def next(cls, renderer):
        return TESSERACT_API.capi_result_renderer_next(renderer)

    @classmethod
    def begin_document(cls, renderer, title: str) -> bool:
        return TESSERACT_API.capi_result_renderer_begin_document(
            renderer, cls.encode_utf8(title))

    @classmethod
    def add_image(cls, renderer, api) -> bool:
        return TESSERACT_API.capi_result_renderer_add_image(renderer, api)

    @classmethod
    def end_document(cls, renderer) -> bool:
        return TESSERACT_API.capi_result_renderer_end_document(renderer)

    @classmethod
    def extention(cls, renderer) -> str:
        ret = TESSERACT_API.capi_result_renderer_extention(renderer)
        return cls.decode(ret)

    @classmethod
    def title(cls, renderer) -> str:
        ret = TESSERACT_API.capi_result_renderer_title(renderer)
        return cls.decode(ret)

    @classmethod
    def image_num(cls, renderer) -> int:
        return TESSERACT_API.capi_result_renderer_image_num(renderer)


class BaseAPI(CommonAPI):
    @classmethod
    def create(cls) -> LPTessBaseAPI:
        return TESSERACT_API.capi_base_api_create()

    @classmethod
    def delete(cls, handle):
        TESSERACT_API.capi_base_api_delete(handle)

    @classmethod
    def get_opencl_device(cls, handle) -> tuple[c_void_p, int]:
        ppdevice = pointer(c_void_p())
        size = TESSERACT_API.capi_base_api_get_opencl_device(handle, ppdevice)
        device = get_point_value(ppdevice)
        return device, size

    @classmethod
    def set_input_name(cls, handle, name: str):
        TESSERACT_API.capi_base_api_set_input_name(handle, cls.encode(name))

    @classmethod
    def get_input_name(cls, handle) -> str:
        ret = TESSERACT_API.capi_base_api_get_input_name(handle)
        return cls.decode(ret)

    @classmethod
    def set_input_image(cls, handle, pix: LPPix):
        TESSERACT_API.capi_base_api_set_input_image(handle, pix)

    @classmethod
    def get_input_image(cls, handle) -> LPPix:
        return TESSERACT_API.capi_base_api_get_input_image(handle)

    @classmethod
    def get_source_y_resolution(cls, handle) -> int:
        return TESSERACT_API.capi_base_api_get_source_y_resolution(handle)

    @classmethod
    def get_datapath(cls, handle) -> str:
        ret = TESSERACT_API.capi_base_api_get_datapath(handle)
        return cls.decode(ret)

    @classmethod
    def set_output_name(cls, handle, name: str):
        TESSERACT_API.capi_base_api_set_output_name(handle, cls.encode(name))

    @classmethod
    def set_variable(cls, handle, name: str, value: str) -> bool:
        return TESSERACT_API.capi_base_api_set_variable(handle,
                                                        cls.encode(name),
                                                        cls.encode(value))

    @classmethod
    def set_debug_variable(cls, handle, name: str, value: str) -> bool:
        return TESSERACT_API.capi_base_api_set_debug_variable(
            handle,
            cls.encode(name),
            cls.encode(value))

    @classmethod
    def get_int_variable(cls, handle, name: str) -> int:
        value = c_int()
        rc = TESSERACT_API.capi_base_api_get_int_variable(handle,
                                                          cls.encode(name),
                                                          byref(value))
        if not rc:
            return None
        return value.value

    @classmethod
    def get_bool_variable(cls, handle, name: str) -> bool:
        value = c_bool()
        rc = TESSERACT_API.capi_base_api_get_bool_variable(handle,
                                                           cls.encode(name),
                                                           byref(value))
        if not rc:
            return None
        return value.value

    @classmethod
    def get_double_variable(cls, handle, name: str) -> float:
        value = c_double()
        rc = TESSERACT_API.capi_base_api_get_double_variable(handle,
                                                             cls.encode(name),
                                                             byref(value))
        if not rc:
            return None
        return value.value

    @classmethod
    def get_string_variable(cls, handle, name: str) -> str:
        ret = TESSERACT_API.capi_base_api_get_string_variable(handle,
                                                              cls.encode(name))
        return cls.decode(ret)

    @classmethod
    def print_variables(cls, handle, fp=sys.stdout):
        if hasattr(fp, 'fileno') and hasattr(fp, 'mode'):
            fileno = fp.fileno()
            mode = fp.mode
        elif isinstance(fp, int):
            fileno = fp
            mode = 'w'
        else:
            raise TypeError('fp type is not io or fileno:{}'.format(type(fp)))
        file_point = fdopen(fileno, mode)
        TESSERACT_API.capi_base_api_print_variables(handle, file_point)

    @classmethod
    def print_variables_tofile(cls, handle,
                               filename: str) -> bool:
        return TESSERACT_API.capi_base_api_print_variables_to_file(
            handle, cls.encode(filename))

    @classmethod
    def init1(cls, handle, datapath: str, language: str, oem: OcrEngineMode,
              configs: list[str]) -> int:
        config_object, configs_size = list_to_array(configs)
        return TESSERACT_API.capi_base_api_init1(handle,
                                                 cls.encode(datapath),
                                                 cls.encode(language), oem,
                                                 config_object, configs_size)

    @classmethod
    def init2(cls, handle, datapath: str, language: str,
              oem: OcrEngineMode) -> int:
        return TESSERACT_API.capi_base_api_init2(handle,
                                                 cls.encode(datapath),
                                                 cls.encode(language), oem)

    @classmethod
    def init3(cls, handle, datapath: str, language: str) -> int:
        return TESSERACT_API.capi_base_api_init3(handle,
                                                 cls.encode(datapath),
                                                 cls.encode(language))

    @classmethod
    def init4(cls, handle, datapath: str, language: str, mode: OcrEngineMode,
              configs: list[str], variables: dict[str, str],
              set_only_non_debug_params: bool) -> int:
        config_object, configs_size = list_to_array(configs)
        vars_vec, vars_values, vars_vec_size = dict_to_array(variables)
        return TESSERACT_API.capi_base_api_init4(handle,
                                                 cls.encode(datapath),
                                                 cls.encode(language),
                                                 mode,
                                                 config_object, configs_size,
                                                 vars_vec, vars_values,
                                                 vars_vec_size,
                                                 set_only_non_debug_params)

    @classmethod
    def init5(cls, handle, data: bytes, language: str, mode: OcrEngineMode,
              configs: list[str], variables: dict[str, str],
              set_only_non_debug_params: bool) -> int:
        config_object, configs_size = list_to_array(configs)
        vars_vec, vars_values, vars_vec_size = dict_to_array(variables)
        return TESSERACT_API.capi_base_api_init5(handle, data, len(data),
                                                 language, mode, config_object,
                                                 configs_size, vars_vec,
                                                 vars_values, vars_vec_size,
                                                 set_only_non_debug_params)

    @classmethod
    def get_init_languages(cls, handle) -> str:
        ret = TESSERACT_API.capi_base_api_get_init_languages(handle)
        return cls.decode(ret)

    @classmethod
    def get_loaded_languages(cls, handle) -> list[str]:
        ret = TESSERACT_API.capi_base_api_get_loaded_languages(handle)
        return [cls.decode(x) for x in ret]

    @classmethod
    def get_available_languages(cls, handle) -> list[str]:
        ret = TESSERACT_API.capi_base_api_get_available_languages(handle)
        return [cls.decode(x) for x in ret]

    @classmethod
    def init_for_analyse_page(cls, handle):
        TESSERACT_API.capi_base_api_init_for_analyse_page(handle)

    @classmethod
    def read_config_file(cls, handle, filename: str):
        TESSERACT_API.capi_base_api_read_config_file(handle,
                                                     cls.encode(filename))

    @classmethod
    def read_debug_config_file(cls, handle, filename: str):
        TESSERACT_API.capi_base_api_read_debug_config_file(
            handle,
            cls.encode(filename))

    @classmethod
    def set_page_seg_mode(cls, handle, mode: PageSegMode):
        TESSERACT_API.capi_base_api_set_page_seg_mode(handle, mode)

    @classmethod
    def get_page_seg_mode(cls, handle) -> PageSegMode:
        ret = TESSERACT_API.capi_base_api_get_page_seg_mode(handle)
        return PageSegMode(ret)

    @classmethod
    def rect(cls, handle, imagedata: bytes,
             bytes_per_pixel: int,
             bytes_per_line: int,
             left: int,
             top: int,
             width: int,
             height: int) -> str:
        data = TESSERACT_API.capi_base_api_rect(handle, imagedata,
                                                bytes_per_pixel,
                                                bytes_per_line,
                                                left, top,
                                                width, height)
        ret = GeneralAPI.get_text_value(data)
        return cls.decode_utf8(ret)

    @classmethod
    def clear_adaptive_classifier(cls, handle):
        TESSERACT_API.capi_base_api_clear_adaptive_classifier(handle)

    @classmethod
    def set_image(cls, handle, imagedata: bytes,
                  width: int, height: int,
                  bytes_per_pixel: int, bytes_per_line: int):
        TESSERACT_API.capi_base_api_set_image(handle, imagedata,
                                              width, height,
                                              bytes_per_pixel, bytes_per_line)

    @classmethod
    def set_image2(cls, handle, pix: LPPix):
        TESSERACT_API.capi_base_api_set_image2(handle, get_point(pix))

    @classmethod
    def set_source_resolution(cls, handle, ppi: int):
        TESSERACT_API.capi_base_api_set_source_resolution(handle, int(ppi))

    @classmethod
    def set_rectangle(cls, handle,
                      left: int, top: int,
                      width: int, height: int):
        TESSERACT_API.capi_base_api_set_rectangle(handle, left, top,
                                                  width, height)

    @classmethod
    def get_thresholded_image(cls, handle) -> LPPix:
        ppix = TESSERACT_API.capi_base_api_get_thresholded_image(handle)
        return ppix

    @classmethod
    def get_regions(cls, handle) -> tuple[LPBoxa, LPPixa]:
        pppixa = pointer(LPPixa())
        pboxa = TESSERACT_API.capi_base_api_get_regions(handle, pppixa)
        ppixa = get_point_value(pppixa)
        return pboxa, ppixa

    @classmethod
    def get_textlines(cls, handle) -> tuple[LPBoxa, LPPixa, list[int]]:
        pppixa = pointer(LPPixa())
        ppblockids = pointer(c_int_p())
        pboxa = TESSERACT_API.capi_base_api_get_textlines(handle,
                                                          pppixa,
                                                          ppblockids)
        ppixa = get_point_value(pppixa)
        n = pboxa.contents.n if pboxa else 0
        blockids = GeneralAPI.get_int_list(ppblockids, n)
        return pboxa, ppixa, blockids

    @classmethod
    def get_textlines1(cls, handle,
                       raw_image: bool,
                       raw_padding: int) -> tuple[LPBoxa, LPPixa,
                                                  list[int], list[int]]:
        pppixa = pointer(LPPixa())
        ppblockids = pointer(c_int_p())
        ppparaids = pointer(c_int_p())
        pboxa = TESSERACT_API.capi_base_api_get_textlines1(handle, raw_image,
                                                           raw_padding,
                                                           pppixa,
                                                           ppblockids,
                                                           ppparaids)
        ppixa = get_point_value(pppixa)
        n = pboxa.contents.n if pboxa else 0
        blockids = GeneralAPI.get_int_list(ppblockids, n)
        paraids = GeneralAPI.get_int_list(ppparaids, n)
        return pboxa, ppixa, blockids, paraids

    @classmethod
    def get_strips(cls, handle) -> tuple[LPBoxa, LPPixa, list[int]]:
        pppixa = pointer(LPPixa())
        ppblockids = pointer(c_int_p())
        pboxa = TESSERACT_API.capi_base_api_get_strips(handle,
                                                       pppixa, ppblockids)
        ppixa = get_point_value(pppixa)
        n = pboxa.contents.n if pboxa else 0
        blockids = GeneralAPI.get_int_list(ppblockids, n)
        return pboxa, ppixa, blockids

    @classmethod
    def get_words(cls, handle) -> tuple[LPBoxa, LPPixa]:
        pppixa = pointer(LPPixa())
        pboxa = TESSERACT_API.capi_base_api_get_words(handle, pppixa)
        ppixa = get_point_value(pppixa)
        return pboxa, ppixa

    @classmethod
    def get_connected_components(cls, handle) -> tuple[LPBoxa, LPPixa]:
        pppixa = pointer(LPPixa())
        pboxa = TESSERACT_API.capi_base_api_get_connected_components(handle,
                                                                     pppixa)
        ppixa = get_point_value(pppixa)
        return pboxa, ppixa

    @classmethod
    def get_component_images(cls, handle,
                             level: PageIteratorLevel,
                             text_only: bool) -> tuple[LPBoxa, LPPixa, int]:
        pppixa = pointer(LPPixa())
        ppblockids = pointer(c_int_p())
        pboxa = TESSERACT_API.capi_base_api_get_component_images(handle, level,
                                                                 text_only,
                                                                 pppixa,
                                                                 ppblockids)
        ppixa = get_point_value(pppixa)
        n = pboxa.contents.n if pboxa else 0
        blockids = GeneralAPI.get_int_list(ppblockids, n)
        return pboxa, ppixa, blockids

    @classmethod
    def get_component_images1(cls, handle, level: PageIteratorLevel,
                              text_only: bool, raw_image: bool,
                              raw_padding: int) -> tuple[LPBoxa, LPPixa,
                                                         int, int]:
        pppixa = pointer(LPPixa())
        ppblockids = pointer(c_int_p())
        ppparaids = pointer(c_int_p())
        pboxa = TESSERACT_API.capi_base_api_get_component_images1(handle,
                                                                  level,
                                                                  text_only,
                                                                  raw_image,
                                                                  raw_padding,
                                                                  pppixa,
                                                                  ppblockids,
                                                                  ppparaids)
        ppixa = get_point_value(pppixa)
        n = pboxa.contents.n if pboxa else 0
        blockids = GeneralAPI.get_int_list(ppblockids, n)
        paraids = GeneralAPI.get_int_list(ppparaids, n)
        return pboxa, ppixa, blockids, paraids

    @classmethod
    def get_thresholded_image_scale_factor(cls, handle) -> int:
        return TESSERACT_API.capi_base_api_get_thresholded_image_scale_factor(
            handle)

    @classmethod
    def analyse_layout(cls, handle) -> LPTessPageIterator:
        return TESSERACT_API.capi_base_api_analyse_layout(handle)

    @classmethod
    def recognize(cls, handle, monitor=None) -> int:
        return TESSERACT_API.capi_base_api_recognize(handle,
                                                     get_point(monitor))

    @classmethod
    def process_pages(cls, handle,
                      filename: str,
                      retry_config: str,
                      timeout_millisec: int,
                      renderer) -> bool:
        return TESSERACT_API.capi_base_api_process_pages(
            handle,
            cls.encode(filename),
            cls.encode(retry_config),
            timeout_millisec,
            get_point(renderer))

    @classmethod
    def process_page(cls, handle,
                     pix: LPPix,
                     page_index: int,
                     filename: bytes,
                     retry_config: bytes,
                     timeout_millisec: int, renderer) -> bool:
        return TESSERACT_API.capi_base_api_process_page(handle,
                                                        pix,
                                                        page_index,
                                                        cls.encode(filename),
                                                        cls.encode(
                                                            retry_config),
                                                        timeout_millisec,
                                                        get_point(renderer))

    @classmethod
    def get_iterator(cls, handle) -> LPTessResultIterator:
        return TESSERACT_API.capi_base_api_get_iterator(handle)

    @classmethod
    def get_mutable_iterator(cls, handle) -> LPTessMutableIterator:
        return TESSERACT_API.capi_base_api_get_mutable_iterator(handle)

    @classmethod
    def get_utf8_text(cls, handle) -> str:
        data = TESSERACT_API.capi_base_api_get_utf8_text(handle)
        ret = GeneralAPI.get_text_value(data)
        return cls.decode_utf8(ret)

    @classmethod
    def get_hocr_text(cls, handle, page_number: int) -> str:
        data = TESSERACT_API.capi_base_api_get_hocr_text(handle,
                                                         page_number)
        ret = GeneralAPI.get_text_value(data)
        return cls.decode_utf8(ret)

    @classmethod
    def get_alto_text(cls, handle, page_number: int) -> str:
        data = TESSERACT_API.capi_base_api_get_alto_text(handle,
                                                         page_number)
        ret = GeneralAPI.get_text_value(data)
        return cls.decode_utf8(ret)

    @classmethod
    def get_tsv_text(cls, handle, page_number: int) -> str:
        data = TESSERACT_API.capi_base_api_get_tsv_text(handle,
                                                        page_number)
        ret = GeneralAPI.get_text_value(data)
        return cls.decode_utf8(ret)

    @classmethod
    def get_box_text(cls, handle, page_number: int) -> str:
        data = TESSERACT_API.capi_base_api_get_box_text(handle,
                                                        page_number)
        ret = GeneralAPI.get_text_value(data)
        return cls.decode_utf8(ret)

    @classmethod
    def get_lstm_box_text(cls, handle, page_number: int) -> str:
        data = TESSERACT_API.capi_base_api_get_lstm_box_text(handle,
                                                             page_number)
        ret = GeneralAPI.get_text_value(data)
        return cls.decode_utf8(ret)

    @classmethod
    def get_word_str_box_text(cls, handle,
                              page_number: int) -> str:
        data = TESSERACT_API.capi_base_api_get_word_str_box_text(handle,
                                                                 page_number)
        ret = GeneralAPI.get_text_value(data)
        return cls.decode_utf8(ret)

    @classmethod
    def get_unlv_text(cls, handle) -> str:
        data = TESSERACT_API.capi_base_api_get_unlv_text(handle)
        ret = GeneralAPI.get_text_value(data)
        return cls.decode_utf8(ret)

    @classmethod
    def mean_text_conf(cls, handle) -> int:
        return TESSERACT_API.capi_base_api_mean_text_conf(handle)

    @classmethod
    def all_word_confidences(cls, handle) -> list[int]:
        return TESSERACT_API.capi_base_api_all_word_confidences(handle)

    @classmethod
    def adapt_to_word_str(cls, handle, mode: PageSegMode,
                          wordstr: str) -> bool:
        return TESSERACT_API.capi_base_api_adapt_to_word_str(
            handle, mode, cls.encode_utf8(wordstr))

    @classmethod
    def clear(cls, handle):
        TESSERACT_API.capi_base_api_clear(handle)

    @classmethod
    def end(cls, handle):
        TESSERACT_API.capi_base_api_end(handle)

    @classmethod
    def is_valid_word(cls, handle, word: str) -> int:
        return TESSERACT_API.capi_base_api_is_valid_word(handle,
                                                         cls.encode(word))

    @classmethod
    def get_text_direction(cls, handle) -> tuple[int, float]:
        out_offset = c_int()
        out_slope = c_float()
        rc = TESSERACT_API.capi_base_api_get_text_direction(handle,
                                                            byref(out_offset),
                                                            byref(out_slope))
        if not rc:
            return None
        return out_offset.value, out_slope.value

    @classmethod
    def get_unichar(cls, handle, unichar_id: int) -> bytes:
        return TESSERACT_API.capi_base_api_get_unichar(handle, unichar_id)

    @classmethod
    def clear_persistent_cache(cls, handle):
        TESSERACT_API.capi_base_api_clear_persistent_cache(handle)

    @classmethod
    def detect_orientation_script(cls, handle) -> OrientationScript:
        orientation_degree = c_int()
        orientation_conf = c_float()
        pscript_name = pointer(c_char_p())
        script_conf = c_float()
        ret = TESSERACT_API.capi_base_api_detect_orientation_script(
            handle,
            byref(orientation_degree),
            byref(orientation_conf),
            pscript_name,
            byref(script_conf))
        if not ret:
            return None
        script_name_value = get_point_value(pscript_name)
        if script_name_value is None:
            script_name = None
        else:
            script_name = cls.decode(script_name_value)
            # GeneralAPI.delete_text(pscript_name.contents)
        return OrientationScript(orientation_degree.value,
                                 orientation_conf.value,
                                 script_name,
                                 script_conf.value)

    @classmethod
    def set_min_orientation_margin(cls, handle, margin: float):
        TESSERACT_API.capi_base_api_set_min_orientation_margin(handle, margin)

    @classmethod
    def num_dawgs(cls, handle) -> int:
        return TESSERACT_API.capi_base_api_num_dawgs(handle)

    @classmethod
    def oem(cls, handle) -> int:
        return TESSERACT_API.capi_base_api_oem(handle)

    @classmethod
    def get_block_text_orientations(cls, handle) -> tuple[int, bool]:
        ppblock_orientation = pointer(c_int_p())
        ppvertical_writing = pointer(c_bool_p())
        TESSERACT_API.capi_base_get_block_text_orientations(
            handle,
            ppblock_orientation,
            ppvertical_writing)
        return (get_point_value(ppblock_orientation, 2),
                get_point_value(ppvertical_writing, 2))


class ProgressMonitorAPI(CommonAPI):
    @classmethod
    def create(cls) -> LPETEXT_DESC:
        return TESSERACT_API.capi_monitor_create()

    @classmethod
    def delete(cls, monitor: LPETEXT_DESC):
        TESSERACT_API.capi_monitor_delete(monitor)

    @classmethod
    def set_cancel_func(cls, monitor: LPETEXT_DESC,
                        cancelFunc: Callable[[c_void_p, int], bool]):
        TESSERACT_API.capi_monitor_set_cancel_func(monitor, cancelFunc)

    @classmethod
    def set_cancel_this(cls, monitor: LPETEXT_DESC, cancelThis):
        TESSERACT_API.capi_monitor_set_cancel_this(monitor, cancelThis)

    @classmethod
    def get_cancel_this(cls, monitor: LPETEXT_DESC) -> c_void_p:
        return TESSERACT_API.capi_monitor_get_cancel_this(monitor)

    @classmethod
    def set_progress_func(cls, monitor: LPETEXT_DESC,
                          progressFunc: Callable[[LPETEXT_DESC, int, int,
                                                  int, int], bool]):
        TESSERACT_API.capi_monitor_set_progress_func(monitor, progressFunc)

    @classmethod
    def get_progress(cls, monitor: LPETEXT_DESC) -> int:
        return TESSERACT_API.capi_monitor_get_progress(monitor)

    @classmethod
    def set_deadline_msecs(cls, monitor: LPETEXT_DESC, deadline: int):
        TESSERACT_API.capi_monitor_set_deadline_msecs(monitor, deadline)


class PageIteratorAPI(CommonAPI):

    @classmethod
    def delete(cls, handle: LPTessPageIterator):
        TESSERACT_API.capi_page_iterator_delete(handle)

    @classmethod
    def copy(cls, handle: LPTessPageIterator) -> LPTessPageIterator:
        return TESSERACT_API.capi_page_iterator_copy(handle)

    @classmethod
    def begin(cls, handle: LPTessPageIterator):
        TESSERACT_API.capi_page_iterator_begin(handle)

    @classmethod
    def next(cls, handle: LPTessPageIterator,
             level: PageIteratorLevel) -> bool:
        return TESSERACT_API.capi_page_iterator_next(handle, level)

    @classmethod
    def is_at_beginning_of(cls, handle: LPTessPageIterator,
                           level: PageIteratorLevel) -> bool:
        return TESSERACT_API.capi_page_iterator_is_at_beginning_of(handle,
                                                                   level)

    @classmethod
    def is_at_final_element(cls, handle: LPTessPageIterator,
                            level: PageIteratorLevel,
                            element: PageIteratorLevel) -> bool:
        return TESSERACT_API.capi_page_iterator_is_at_final_element(handle,
                                                                    level,
                                                                    element)

    @classmethod
    def bounding_box(cls, handle: LPTessPageIterator,
                     level: PageIteratorLevel) -> Bounding:
        # 'left', 'top', 'right', 'bottom'
        args = [c_int()] * 4
        c_args = [byref(x) for x in args]
        ret = TESSERACT_API.capi_page_iterator_bounding_box(handle,
                                                            level, *c_args)
        if not ret:
            raise TesseractError("bounding_box failed",
                                 "TessPageIteratorBoundingBox() failed")
        return Bounding(*[x.value for x in args])

    @classmethod
    def block_type(cls, handle: LPTessPageIterator) -> PolyBlockType:
        ret = TESSERACT_API.capi_page_iterator_block_type(handle)
        return PolyBlockType(ret)

    @classmethod
    def get_binary_image(cls, handle: LPTessPageIterator,
                         level: PageIteratorLevel) -> LPPix:
        return TESSERACT_API.capi_page_iterator_get_binary_image(handle, level)

    @classmethod
    def get_image(cls, handle: LPTessPageIterator,
                  level: PageIteratorLevel, padding: int,
                  original_image: LPPix) -> LPPix:
        # left, top
        args = [c_int()] * 2
        c_args = [byref(x) for x in args]
        ppix = TESSERACT_API.capi_page_iterator_get_image(handle, level,
                                                          padding,
                                                          original_image,
                                                          *c_args)
        return ppix, *[x.value for x in args]

    @classmethod
    def baseline(cls, handle: LPTessPageIterator,
                 level: PageIteratorLevel) -> bool:
        # x1, y1, x2, y2
        args = [c_int()] * 4
        c_args = [byref(x) for x in args]
        rc = TESSERACT_API.capi_page_iterator_baseline(handle, level, *c_args)
        if not rc:
            raise TesseractError("baseline failed",
                                 "TessPageIteratorBaseline() failed")
        return Baseline(*[x.value for x in args])

    @classmethod
    def orientation(cls, handle: LPTessPageIterator) -> tuple[int, int,
                                                              int, float]:
        args = [c_int(), c_int(), c_int(), c_float()]
        c_args = [byref(x) for x in args]
        # orientation, writing_direction, textline_order, deskew_angle
        TESSERACT_API.capi_page_iterator_orientation(handle, *c_args)
        return (Orientation(args[0]), WritingDirection(args[1]),
                TextlineOrder(args[2]), args[3])

    @classmethod
    def paragraph_info(cls, handle: LPTessPageIterator) -> tuple[int, bool,
                                                                 bool, int]:
        args = [c_int(), c_bool(), c_bool(), c_int()]
        c_args = [byref(x) for x in args]
        # justification, is_list_item, is_crown, first_line_indent
        TESSERACT_API.capi_page_iterator_paragraph_info(handle, *c_args)
        result = list(x.value for x in args)
        result[0] = ParagraphJustification(result[0])
        return tuple(result)


class ResultIteratorAPI(CommonAPI):

    @classmethod
    def delete(cls, handle):
        TESSERACT_API.capi_result_iterator_delete(handle)

    @classmethod
    def copy(cls, handle):
        return TESSERACT_API.capi_result_iterator_copy(handle)

    @classmethod
    def get_page_iterator(cls, handle):
        iterator = TESSERACT_API.capi_result_iterator_get_page_iterator(handle)
        return iterator

    @classmethod
    def get_page_iterator_const(cls, handle):
        return TESSERACT_API.capi_result_iterator_get_page_iterator_const(
            handle)

    @classmethod
    def get_choice_iterator(cls, handle):
        return TESSERACT_API.capi_result_iterator_get_choice_iterator(handle)

    @classmethod
    def next(cls, handle, level: PageIteratorLevel) -> bool:
        return TESSERACT_API.capi_result_iterator_next(handle, level)

    @classmethod
    def get_utf8_text(cls, handle, level: PageIteratorLevel) -> str:
        data = TESSERACT_API.capi_result_iterator_get_utf8_text(handle, level)
        ret = GeneralAPI.get_text_value(data)
        return cls.decode_utf8(ret)

    @classmethod
    def confidence(cls, handle, level: PageIteratorLevel) -> float:
        return TESSERACT_API.capi_result_iterator_confidence(handle, level)

    @classmethod
    def word_recognition_language(cls, handle) -> bytes:
        return TESSERACT_API.capi_result_iterator_word_recognition_language(
            handle)

    @classmethod
    def word_font_attributes(cls, handle) -> Font:
        # is_italic, is_underlined, is_monospace, is_serif, is_smallcaps,
        # pointsize, font_id
        args = [c_bool()] * 6 + [c_int()] * 2
        c_args = [byref(x) for x in args]
        ret = TESSERACT_API.capi_result_iterator_word_font_attributes(handle,
                                                                      *c_args)
        font_name = cls.decode(ret)
        return Font(font_name, *[x.value for x in args])

    @classmethod
    def word_is_from_dictionary(cls, handle) -> bool:
        return TESSERACT_API.capi_result_iterator_word_is_from_dictionary(
            handle)

    @classmethod
    def word_is_numeric(cls, handle) -> bool:
        return TESSERACT_API.capi_result_iterator_word_is_numeric(handle)

    @classmethod
    def symbol_is_superscript(cls, handle) -> bool:
        return TESSERACT_API.capi_result_iterator_symbol_is_superscript(handle)

    @classmethod
    def symbol_is_subscript(cls, handle) -> bool:
        return TESSERACT_API.capi_result_iterator_symbol_is_subscript(handle)

    @classmethod
    def symbol_is_dropcap(cls, handle) -> bool:
        return TESSERACT_API.capi_result_iterator_symbol_is_dropcap(handle)


class ChoiceIteratorAPI(CommonAPI):

    @classmethod
    def delete(cls, handle):
        TESSERACT_API.capi_choice_iterator_delete(handle)

    @classmethod
    def next(cls, handle) -> bool:
        return TESSERACT_API.capi_choice_iterator_next(handle)

    @classmethod
    def get_utf8_text(cls, handle) -> str:
        ret = TESSERACT_API.capi_choice_iterator_get_utf8_text(handle)
        return cls.decode_utf8(ret)

    @classmethod
    def confidence(cls, handle) -> float:
        return TESSERACT_API.capi_choice_iterator_confidence(handle)
