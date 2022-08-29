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
from .leptonica_capi import Pix
from .leptonica import Leptonica
from .tesseract_api import (GeneralAPI, RendererAPI, BaseAPI,
                            TESSDATA_PREFIX, TesseractError,
                            OcrEngineMode, Orientation, PageSegMode,
                            PageIteratorLevel)


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

    def __init__(self):
        self.generalapi = GeneralAPI()
        self.rendererapi = RendererAPI
        self.baseapi = self.create_baseapi()
        self.api_list = self.generalapi, self.rendererapi, self.baseapi

    def create_baseapi(self,
                       datapath: str = TESSDATA_PREFIX,
                       language: str = 'eng',
                       mode: OcrEngineMode = None, *configs, **kwargs):
        return BaseAPI(datapath, language, mode, *configs, **kwargs)

    def get_baseapi(self,
                    datapath: str = TESSDATA_PREFIX,
                    language: str = 'eng',
                    mode: OcrEngineMode = None, *configs, **kwargs):
        self.baseapi.init(datapath, language, mode, *configs, **kwargs)
        return self

    def __getattr__(self, attr):
        for api in self.api_list:
            if hasattr(api, attr):
                return getattr(api, attr)
        raise AttributeError(
            "'{}' object has no attribute '{}'".format(self.__class__.__name__,
                                                       attr))

    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        del self.generalapi
        del self.rendererapi
        del self.baseapi

    @lru_cache
    def api_dir(self):
        apis = set()
        for api in self.api_list:
            apis = apis | set(dir(api))
        ret = [x for x in apis if not x.startswith('__')]
        ret.sort()
        return ret

    def __dir__(self):
        return super().__dir__() + self.api_dir()

    def get_version(self) -> tuple:
        version = self.version()
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
        return self.get_available_languages()

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

    def can_detect_orientation(self):
        return 'osd' in self.list_langs()

    @classmethod
    def detect_orientation(cls, image, lang=None):
        # C-API with Tesseract 4 segfaults if running OSD_ONLY
        # psm mode with other than osd language
        # lang argument left purely for compatibility reasons
        # tested on 4.0.0-rc2
        api = cls()
        with api.get_baseapi(TESSDATA_PREFIX, 'osd') as handle:
            handle.set_page_seg_mode(PageSegMode.OSD_ONLY)
            handle.set_image_data(image)
            res = handle.detect_orientation_script()
            if res['confidence'] <= 0:
                raise TesseractError(
                    "no script", "no script detected"
                )
            orientation = {
                Orientation.PAGE_UP: 0,
                Orientation.PAGE_RIGHT: 90,
                Orientation.PAGE_DOWN: 180,
                Orientation.PAGE_LEFT: 270,
            }[res['orientation_enum']]
            return {'angle': orientation,
                    'confidence': res['confidence']}

    @classmethod
    def image_to_string(cls, image, lang=None, builder=None):
        clang = lang if lang else "eng"
        api = cls()
        handle = api.get_baseapi(TESSDATA_PREFIX, clang)
        for lang_item in clang.split("+"):
            if lang_item not in handle.get_available_languages():
                raise TesseractError(
                    "no lang",
                    f"language {lang_item} is not available"
                )

        handle.set_page_seg_mode(builder.tesseract_layout)
        handle.set_debug_file(osp.devnull)

        handle.set_image_data(image)
        if "digits" in builder.tesseract_configs:
            handle.set_is_numeric(True)

        handle.recognize()
        result_iterator = handle.get_iterator()
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
