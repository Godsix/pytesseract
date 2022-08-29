# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 09:28:35 2021

@author: 皓
"""
import os.path as osp
import re
from functools import lru_cache
from PIL import Image
from ctypes import POINTER
from .common import TESSDATA_PREFIX
from .error import TesseractError
from .leptonica_capi import Pix
from .leptonica import Leptonica
from .tesseract_capi import (Orientation, OcrEngineMode, PageSegMode,
                             PageIteratorLevel)
from .tesseract_papi import GeneralAPI
from .tesseract_api import TessBase, ProgressMonitor, ResultRenderer


DPI_DEFAULT = 70


def digits_only(string):
    """Return all digits that the given string starts with."""
    match = re.match(r'\D*(?P<digits>\d+)', string)
    if match:
        return int(match.group('digits'))
    return 0


class Tesseract:
    LVL_LINE = PageIteratorLevel.TEXTLINE
    LVL_WORD = PageIteratorLevel.WORD
    GENERAL_API = GeneralAPI

    def __init__(self,
                 datapath: str = TESSDATA_PREFIX,
                 language: str = 'eng',
                 mode: OcrEngineMode = None,
                 *configs, **kwargs):
        self.api = TessBase(datapath, language, mode, *configs, **kwargs)

    def __getattr__(self, attr):
        if hasattr(self.api, attr):
            return getattr(self.api, attr)
        raise AttributeError(
            "'{}' object has no attribute '{}'".format(self.__class__.__name__,
                                                       attr))

    @lru_cache
    def api_dir(self):
        if hasattr(self, 'api'):
            ret = [x for x in dir(self.api) if not x.startswith('__')]
            ret.sort()
        else:
            ret = []
        return ret

    def __dir__(self):
        return super().__dir__() + self.api_dir()

    @property
    def opencl_device(self):
        return self.api.opencl_device

    @property
    def input_name(self) -> str:
        return self.api.input_name

    @input_name.setter
    def input_name(self, value: str):
        self.api.input_name = value

    @property
    def input_image(self):
        return self.api.input_image

    @input_image.setter
    def input_image(self, value):
        self.api.input_image = value

    @property
    def source_y_resolution(self) -> int:
        return self.api.source_y_resolution

    @property
    def datapath(self) -> str:
        return self.api.datapath

    @property
    def init_languages(self) -> str:
        return self.api.init_languages

    @property
    def loaded_languages(self) -> list[str]:
        return self.api.loaded_languages

    @property
    def available_languages(self) -> list[str]:
        return self.api.available_languages

    @property
    def page_seg_mode(self) -> PageSegMode:
        return self.api.page_seg_mode

    @page_seg_mode.setter
    def page_seg_mode(self, mode: PageSegMode):
        self.api.page_seg_mode = mode

    def set_is_numeric(self, mode):
        whitelist = "0123456789." if mode else ''
        return self.api.set_variable("tessedit_char_whitelist", whitelist)

    def set_debug_file(self, filename):
        return self.api.set_variable("debug_file", filename)

    def get_version(self) -> tuple:
        version = self.GENERAL_API.version()
        version = version.split(" ", 1)[0]

        # cut off "dev" string if exists for proper int conversion
        index = version.find("dev")
        if index >= 0:
            version = version[:index]

        version = version.split(".")
        major = digits_only(version[0])
        minor = digits_only(version[1])
        release = digits_only(version[2]) if len(version) >= 3 else 0
        return (major, minor, release)

    def list_langs(self) -> list[str]:
        return self.available_languages

    def set_image_data(self, img, use_leptonica=True):
        use_pix = False
        if osp.isfile(img):
            if use_leptonica:
                image = Leptonica.pix_read(img)
                use_pix = True
            else:
                image = Image.open(img)
        elif isinstance(img, Image.Image):
            image = img
        elif isinstance(img, POINTER(Pix)):
            image = img
            use_pix = True
        else:
            type_name = type(img).__name__
            raise TypeError(f'The image type is not support: {type_name}')
        if not use_pix:
            image = image.convert("RGB")
            image.load()
            imgdata = image.tobytes("raw", "RGB")
            width = image.width
            height = image.height
            self.set_image(imgdata, width, height, 3, width * 3)
            info = image.info
            if 'dpi' in info:
                dpi = info["dpi"][0]
            else:
                dpi = DPI_DEFAULT
            self.set_source_resolution(dpi)
        else:
            self.set_image2(image)

    @classmethod
    def detect_orientation(cls, image, lang=None):
        # C-API with Tesseract 4 segfaults if running OSD_ONLY
        # psm mode with other than osd language
        # lang argument left purely for compatibility reasons
        # tested on 4.0.0-rc2
        tesseract = cls(TESSDATA_PREFIX, 'osd')
        tesseract.page_seg_mode = PageSegMode.OSD_ONLY
        tesseract.set_image_data(image)
        res = tesseract.detect_orientation_script()
        if res.confidence <= 0:
            raise TesseractError("no script", "no script detected")
        return res

    @classmethod
    def image_to_string(cls, image, lang=None, builder=None):
        clang = lang if lang else "eng"
        tesseract = cls(TESSDATA_PREFIX, clang)
        for lang_item in clang.split("+"):
            if lang_item not in tesseract.list_langs():
                raise TesseractError(
                    "no lang",
                    f"language {lang_item} is not available"
                )

        tesseract.page_seg_mode = builder.tesseract_layout
        tesseract.set_debug_file(osp.devnull)

        tesseract.set_image_data(image)
        if "digits" in builder.tesseract_configs:
            tesseract.set_is_numeric(True)

        tesseract.recognize()
        result_iterator = tesseract.get_iterator()
        if result_iterator is None:
            raise TesseractError("no script", "no script detected")
        page_iterator = result_iterator.get_page_iterator()

        while True:
            if page_iterator.is_at_beginning_of(cls.LVL_LINE):
                box = page_iterator.bounding_box(cls.LVL_LINE)
                builder.start_line(box)

            last_word = page_iterator.is_at_final_element(cls.LVL_LINE,
                                                          cls.LVL_WORD)
            word = result_iterator.get_utf8_text(cls.LVL_WORD)
            confidence = result_iterator.confidence(cls.LVL_WORD)

            if word and confidence is not None:
                box = page_iterator.bounding_box(cls.LVL_WORD)
                builder.add_word(word, box, confidence)

                if last_word:
                    builder.end_line()
            if not page_iterator.next(cls.LVL_WORD):
                break
        ret = builder.get_output()
        return ret
