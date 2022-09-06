# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 09:28:35 2021

@author: 皓
"""
import os.path as osp
import re
try:
    from PIL import Image
except ModuleNotFoundError:
    Image = None
from .common import TESSDATA_PREFIX
from .error import TesseractError
from .leptonica_capi import LPPix
from .leptonica import Leptonica, PyPix
from .tesseract_capi import PageSegMode, PageIteratorLevel
from .tesseract_papi import GeneralAPI
from .tesseract_api import TessBase, ProgressMonitor


DPI_DEFAULT = 70


def digits_only(string):
    """Return all digits that the given string starts with."""
    match = re.match(r'\D*(?P<digits>\d+)', string)
    if match:
        return int(match.group('digits'))
    return 0


class Tesseract(TessBase):
    LVL_LINE = PageIteratorLevel.TEXTLINE
    LVL_WORD = PageIteratorLevel.WORD

    @property
    def version(self) -> str:
        '''
        Returns the version identifier as a static string. Do not delete.
        '''
        return GeneralAPI.version()

    def set_is_numeric(self, mode):
        whitelist = "0123456789." if mode else ''
        return self.set_variable("tessedit_char_whitelist", whitelist)

    def set_debug_file(self, filename):
        return self.set_variable("debug_file", filename)

    def get_version(self) -> tuple:
        version = self.version
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

    def set_image_data(self, img, use_leptonica=False):
        use_pix = False
        if osp.isfile(img):
            if use_leptonica or Image is None:
                image = Leptonica.pix_read(img)
                use_pix = True
            else:
                image = Image.open(img)
        elif Image is not None and isinstance(img, Image.Image):
            image = img
        elif isinstance(img, (LPPix, PyPix)):
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

    def get_rect(self, img, left: int, top: int, width: int, height: int):
        if osp.isfile(img):
            image = Image.open(img)
        elif isinstance(img, Image.Image):
            image = img
        else:
            type_name = type(img).__name__
            raise TypeError(f'The image type is not support: {type_name}')
        image = image.convert("RGB")
        image.load()
        imgdata = image.tobytes("raw", "RGB")
        width = image.width
        height = image.height
        ret = self.rect(imgdata, 1, width * 1, left, top, width, height)
        return ret

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
    def image_to_string(cls, image, lang=None, builder=None,
                        progress_func=None):
        clang = lang if lang else "eng"
        tesseract = cls(TESSDATA_PREFIX, clang)
        available_languages = tesseract.get_available_languages()
        invalid_langs = set(clang.split("+")) - set(available_languages)
        if invalid_langs:
            invalids = ', '.join(invalid_langs)
            raise TesseractError("no lang",
                                 f"language {invalids} is not available")

        tesseract.page_seg_mode = builder.tesseract_layout
        tesseract.set_debug_file(osp.devnull)

        tesseract.set_image_data(image)
        if "digits" in builder.tesseract_configs:
            tesseract.set_is_numeric(True)
        monitor = None
        if progress_func is not None:
            monitor = ProgressMonitor()
            monitor.set_progress_func(progress_func)
        tesseract.recognize(monitor)
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
