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
        'word': API.word_str_box_renderer_create,

        'lstmbox': API.lstm_box_renderer_create,
        'wordstrbox': API.word_str_box_renderer_create,
        'boxfile': API.box_text_renderer_create,
        'txt': API.text_renderer_create,
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
        return cls(result, filetype)

    def insert(self, next_: 'ResultRenderer'):
        '''
        Takes ownership of pointer so must be new'd instance.
        Renderers aren't ordered, but appends the sequences of next parameter
        and existing next(). The renderers should be unique across both lists.
        '''
        self.API.insert(self.handle, next_)

    def next(self) -> 'ResultRenderer':
        '''Returns the next renderer or nullptr.'''
        result = self.API.next(self.handle)
        return self.__class__(result)

    def extention(self) -> str:
        '''Get standard extension for generated output'''
        return self.API.extention(self.handle)

    def title(self) -> str:
        '''Get title of document being rendered'''
        return self.API.title(self.handle)

    def begin_document(self, title: str) -> bool:
        '''
        Starts a new document with the given title.
        This clears the contents of the output data.
        Title should use UTF-8 encoding.
        '''
        return self.API.begin_document(self.handle, title)

    def end_document(self) -> bool:
        '''
        Finishes the document and finalizes the output data
        Invalid if BeginDocument not yet called.
        '''
        return self.API.end_document(self.handle)

    def add_image(self, api) -> bool:
        '''
        Adds the recognized text from the source image to the current document.
        Invalid if BeginDocument not yet called.
        Note that this API is a bit weird but is designed to fit into the
        current TessBaseAPI implementation where the api has lots of state
        information that we might want to add in.
        '''
        return self.API.add_image(self.handle, api)

    def image_num(self) -> int:
        '''
        Returns the index of the last image given to AddImage
        (i.e. images are incremented whether the image succeeded or not)
        This is always defined. It means either the number of the
        current image, the last image ended, or in the completed document
        depending on when in the document lifecycle you are looking at it.
        Will return -1 if a document was never started.
        '''
        return self.API.image_num(self.handle)

    def __repr__(self):
        if not self.filetype:
            return super().__repr__()
        class_name = self.__class__.__name__
        return f'<{class_name} object type {self.filetype} at {self.arch_id}>'


class PageIterator(BaseIterObject):
    API = PageIteratorAPI

    def begin(self):
        self.API.begin(self.handle)

    def next(self, level: PageIteratorLevel) -> bool:
        return self.API.next(self.handle, level)

    def is_at_beginning_of(self, level: PageIteratorLevel) -> bool:
        '''
        Returns true if the iterator is at the start of an object at the given
        level. Possible uses include determining if a call to Next(RIL_WORD)
        moved to the start of a RIL_PARA.
        '''
        return self.API.is_at_beginning_of(self.handle, level)

    def is_at_final_element(self, level: PageIteratorLevel,
                            element: PageIteratorLevel) -> bool:
        '''
        Returns whether the iterator is positioned at the last element in a
        given level. (e.g. the last word in a line, the last line in a block)
        '''
        return self.API.is_at_final_element(self.handle, level, element)

    def bounding_box(self, level: PageIteratorLevel) -> Bounding:
        '''
        Returns the bounding rectangle of the current object at the given level
        in coordinates of the original image.
        See comment on coordinate system above.
        Returns false if there is no such object at the current position.
        '''
        return self.API.bounding_box(self.handle, level)

    def block_type(self) -> PolyBlockType:
        '''
        Returns the type of the current block.
        See tesseract/publictypes.h for PolyBlockType.
        '''
        return self.API.block_type(self.handle)

    def get_binary_image(self, level: PageIteratorLevel) -> LPPix:
        '''
        Returns a binary image of the current object at the given level.
        The position and size match the return from BoundingBoxInternal, and so
        thiscould be upscaled with respect to the original input image.
        Use pixDestroy to delete the image after use.
        The following methods are used to generate the images:
        RIL_BLOCK: mask the page image with the block polygon.
        RIL_TEXTLINE: Clip the rectangle of the line box from the page image.
        TODO(rays) fix this to generate and use a line polygon.
        RIL_WORD: Clip the rectangle of the word box from the page image.
        RIL_SYMBOL: Render the symbol outline to an image for cblobs (prior
        to recognition) or the bounding box otherwise.
        A reconstruction of the original image (using xor to check for double
        representation) should be reasonably accurate,
        apart from removed noise, at the block level. Below the block level,
        the reconstruction will be missing images and line separators.
        At the symbol level, kerned characters will be invade the bounding box
        if rendered after recognition, making an xor reconstruction inaccurate,
        but an or construction better. Before recognition, symbol-level
        reconstruction should be good, even with xor, since the images come
        from the connected components.
        '''
        return self.API.get_binary_image(self.handle, level)

    def get_image(self, level: PageIteratorLevel, padding: int,
                  original_image: LPPix) -> LPPix:
        '''
        Returns an image of the current object at the given level in greyscale
        if available in the input. To guarantee a binary image use BinaryImage.
        NOTE that in order to give the best possible image, the bounds are
        expanded slightly over the binary connected component, by the supplied
        padding, so the top-left position of the returned image is returned
        in (left,top). These will most likely not match the coordinates
        returned by BoundingBox.
        If you do not supply an original image, you will get a binary one.
        Use pixDestroy to delete the image after use.
        '''
        return self.API.get_image(self.handle, level, padding, original_image)

    def baseline(self, level: PageIteratorLevel) -> bool:
        '''
        Returns the baseline of the current object at the given level.
        The baseline is the line that passes through (x1, y1) and (x2, y2).
        WARNING: with vertical text, baselines may be vertical!
        '''
        return self.API.baseline(self.handle, level)

    def orientation(self) -> tuple[int, int, int, float]:
        return self.API.orientation(self.handle)

    def paragraph_info(self) -> tuple[int, bool, bool, int]:
        return self.API.paragraph_info(self.handle)


class ChoiceIterator(BaseIterObject):
    API = ChoiceIteratorAPI

    def next(self) -> bool:
        '''
        Moves to the next choice for the symbol and returns false if there
        are none left.
        '''
        return self.API.next(self.handle)

    def get_utf8_text(self) -> str:
        '''
        Returns the null terminated UTF-8 encoded text string for the current
        choice. Do NOT use delete [] to free after use.
        '''
        return self.API.get_utf8_text(self.handle)

    def confidence(self) -> float:
        '''
        Returns the confidence of the current choice depending on the used
        language data. If only LSTM traineddata is used the value range is
        0.0f - 1.0f. All choices for one symbol should roughly add up to 1.0f.
        If only traineddata of the legacy engine is used, the number should be
        interpreted as a percent probability. (0.0f-100.0f) In this case
        probabilities won't add up to 100. Each one stands on its own.
        '''
        return self.API.confidence(self.handle)


class ResultIterator(CopyIterator):
    API = ResultIteratorAPI

    def get_page_iterator(self) -> PageIterator:
        '''return TessResultIterator * this'''
        handle = self.API.get_page_iterator(self.handle)
        if not handle:
            return None
        return PageIterator(handle, self)

    def get_page_iterator_const(self) -> PageIterator:
        '''return TessResultIterator * this'''
        handle = self.API.get_page_iterator_const(self.handle)
        if not handle:
            return None
        return PageIterator(handle, self)

    def get_choice_iterator(self) -> ChoiceIterator:
        '''return new TessChoiceIterator *'''
        handle = self.API.get_choice_iterator(self.handle)
        if not handle:
            return None
        return ChoiceIterator(handle)

    def next(self, level: PageIteratorLevel) -> bool:
        return self.API.next(self.handle, level)

    def get_utf8_text(self, level: PageIteratorLevel) -> str:
        '''
        Returns the null terminated UTF-8 encoded text string for the current
        object at the given level. Use delete [] to free after use.
        '''
        return self.API.get_utf8_text(self.handle, level)

    def confidence(self, level: PageIteratorLevel) -> float:
        '''
        Returns the mean confidence of the current object at the given level.
        The number should be interpreted as a percent probability.
        (0.0f-100.0f)
        '''
        return self.API.confidence(self.handle, level)

    def word_recognition_language(self) -> bytes:
        '''Returns the name of the language used to recognize this word.'''
        return self.API.word_recognition_language(self.handle)

    def word_font_attributes(self) -> Font:
        '''
        Returns the font attributes of the current word. If iterating at a
        higher level object than words, eg textlines, then this will return the
        attributes of the first word in that textline.
        The actual return value is a string representing a font name. It points
        to an internal table and SHOULD NOT BE DELETED. Lifespan is the same as
        the iterator itself, ie rendered invalid by various members of
        TessBaseAPI, including Init, SetImage, End or deleting the TessBaseAPI.
        Pointsize is returned in printers points (1/72 inch.)
        '''
        return self.API.word_font_attributes(self.handle)

    def word_is_from_dictionary(self) -> bool:
        '''Returns true if the current word was found in a dictionary.'''
        return self.API.word_is_from_dictionary(self.handle)

    def word_is_numeric(self) -> bool:
        '''Returns true if the current word is numeric.'''
        return self.API.word_is_numeric(self.handle)

    def symbol_is_superscript(self) -> bool:
        '''
        Returns true if the current symbol is a superscript.
        If iterating at a higher level object than symbols, eg words, then
        this will return the attributes of the first symbol in that word.
        '''
        return self.API.symbol_is_superscript(self.handle)

    def symbol_is_subscript(self) -> bool:
        '''
        Returns true if the current symbol is a subscript.
        If iterating at a higher level object than symbols, eg words, then
        this will return the attributes of the first symbol in that word.
        '''
        return self.API.symbol_is_subscript(self.handle)

    def symbol_is_dropcap(self) -> bool:
        '''
        Returns true if the current symbol is a dropcap.
        If iterating at a higher level object than symbols, eg words, then
        this will return the attributes of the first symbol in that word.
        '''
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
        '''percent complete increasing (0-100)'''
        return self.API.get_progress(self.handle)

    @property
    def cancel_this(self) -> c_void_p:
        '''this or other data for cancel'''
        return self.API.get_cancel_this(self.handle)

    @cancel_this.setter
    def cancel_this(self, value: c_void_p):
        '''this or other data for cancel'''
        self.API.set_cancel_this(self.handle, value)

    def set_cancel_func(self, cancel_func: Callable[[c_void_p, int], bool]):
        '''returns true to cancel'''
        if isinstance(cancel_func, TessProgressFunc):
            self.callable_cancel_func = None
            self.cancel_func = cancel_func
        else:
            self.callable_cancel_func = cancel_func
            self.cancel_func = wrapper_cancel_func(cancel_func)
        self.API.set_cancel_func(self.handle, self.cancel_func)

    def set_progress_func(self, progress_func: Callable[[Any, int, int,
                                                         int, int], bool]):
        '''monitor-aware progress callback'''
        if isinstance(progress_func, TessProgressFunc):
            self.callable_progress_func = None
            self.progress_func = progress_func
        else:
            self.callable_progress_func = progress_func
            self.progress_func = wrapper_progress_func(progress_func)
        self.API.set_progress_func(self.handle, self.progress_func)

    def set_deadline_msecs(self, deadline: int):
        '''Sets the end time to be deadline_msecs milliseconds from now.'''
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
        '''
        If compiled with OpenCL AND an available OpenCL
        device is deemed faster than serial code, then
        "device" is populated with the cl_device_id
        and returns sizeof(cl_device_id)
        otherwise *device=nullptr and returns 0.
        '''
        return self.API.get_opencl_device(self.handle)

    def set_input_name(self, name: str):
        '''
        Set the name of the input file. Needed only for training and
        loading a UNLV zone file.
        '''
        self.API.set_input_name(self.handle, name)

    def get_input_name(self) -> str:
        return self.API.get_input_name(self.handle)

    def set_input_image(self, pix: LPPix):
        '''Takes ownership of the input pix.'''
        self.API.set_input_image(self.handle, pix)

    def get_input_image(self) -> LPPix:
        return self.API.get_input_image(self.handle)

    def get_source_y_resolution(self) -> int:
        '''Get y pixels/inch in source image.'''
        return self.API.get_source_y_resolution(self.handle)

    def get_datapath(self) -> str:
        '''Get dir for data files'''
        return self.API.get_datapath(self.handle)

    def set_output_name(self, name: str):
        '''Set the name of the output files. Needed only for debugging.'''
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
        '''Get value of named variable as a string, if it exists.'''
        return self.API.get_string_variable(self.handle, name)

    def print_variables(self, fp):
        '''Print Tesseract parameters to the given file.'''
        self.API.print_variables(self.handle, fp)

    def print_variables_tofile(self, filename: str) -> bool:
        return self.API.print_variables_tofile(self.handle, filename)

    def init(self, datapath: str, language: str, mode: OcrEngineMode,
             *configs, **kwargs):
        '''
        The datapath must be the name of the data directory or
        some other file in which the data directory resides (for instance
        argv[0].)
        The language is (usually) an ISO 639-3 string or nullptr will default
        to eng.
        If numeric_mode is true, then only digits and Roman numerals will
        be returned.
        @return: 0 on success and -1 on initialization failure.
        '''
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
        '''
        Returns the languages string used in the last valid initialization.
        If the last initialization specified "deu+hin" then that will be
        returned. If hin loaded eng automatically as well, then that will
        not be included in this list. To find the languages actually
        loaded use GetLoadedLanguagesAsVector.
        The returned string should NOT be deleted.
        '''
        return self.API.get_init_languages(self.handle)

    def get_loaded_languages(self) -> list[str]:
        '''
        Returns the loaded languages in the vector of std::string.
        Includes all languages loaded by the last Init, including those loaded
        as dependencies of other loaded languages.
        '''
        return self.API.get_loaded_languages(self.handle)

    def get_available_languages(self) -> list[str]:
        '''
        Returns the available languages in the sorted vector of std::string.
        '''
        return self.API.get_available_languages(self.handle)

    def init_for_analyse_page(self):
        '''
        Init only for page layout analysis. Use only for calls to SetImage and
        AnalysePage. Calls that attempt recognition will generate an error.
        '''
        self.API.init_for_analyse_page(self.handle)

    def read_config_file(self, filename: str):
        '''
        Read a "config" file containing a set of parameter name, value pairs.
        Searches the standard places: tessdata/configs, tessdata/tessconfigs
        and also accepts a relative or absolute path name.
        '''
        self.API.read_config_file(self.handle, filename)

    def read_debug_config_file(self, filename: str):
        '''
        Same as above, but only set debug params from the given config file.
        '''
        self.API.read_debug_config_file(self.handle, filename)

    def set_page_seg_mode(self, mode: PageSegMode):
        '''
        Set the current page segmentation mode. Defaults to PSM_AUTO.
        The mode is stored as an IntParam so it can also be modified by
        ReadConfigFile or SetVariable("tessedit_pageseg_mode", mode as string).
        '''
        self.API.set_page_seg_mode(self.handle, mode)

    def get_page_seg_mode(self) -> PageSegMode:
        '''Return the current page segmentation mode.'''
        return self.API.get_page_seg_mode(self.handle)

    def rect(self, imagedata: bytes, bytes_per_pixel: int, bytes_per_line: int,
             left: int, top: int, width: int, height: int) -> str:
        '''
        Recognize a rectangle from an image and return the result as a string.
        May be called many times for a single Init.
        Currently has no error checking.
        Greyscale of 8 and color of 24 or 32 bits per pixel may be given.
        Palette color images will not work properly and must be converted to
        24 bit.
        Binary images of 1 bit per pixel may also be given but they must be
        byte packed with the MSB of the first byte being the first pixel, and a
        one pixel is WHITE. For binary images set bytes_per_pixel=0.
        The recognized text is returned as a char* which is coded
        as UTF8 and must be freed with the delete [] operator.
        '''
        return self.API.rect(self.handle, imagedata, bytes_per_pixel,
                             bytes_per_line, left, top, width, height)

    def clear_adaptive_classifier(self):
        '''
        Call between pages or documents etc to free up memory and forget
        adaptive data.
        '''
        self.API.clear_adaptive_classifier(self.handle)

    def set_image(self, imagedata: bytes, width: int, height: int,
                  bytes_per_pixel: int, bytes_per_line: int):
        '''
        Provide an image for Tesseract to recognize. Format is as
        TesseractRect above. Copies the image buffer and converts to Pix.
        SetImage clears all recognition results, and sets the rectangle to the
        full image, so it may be followed immediately by a GetUTF8Text, and it
        will automatically perform recognition.
        '''
        self.API.set_image(self.handle, imagedata, width, height,
                           bytes_per_pixel, bytes_per_line)

    def set_image2(self, pix: LPPix):
        '''
        Provide an image for Tesseract to recognize. As with SetImage above,
        Tesseract takes its own copy of the image, so it need not persist until
        after Recognize.
        Pix vs raw, which to use?
        Use Pix where possible. Tesseract uses Pix as its internal
        representation and it is therefore more efficient to provide a Pix
        directly.
        '''
        self.API.set_image2(self.handle, pix)

    def set_source_resolution(self, ppi: int):
        '''
        Set the resolution of the source image in pixels per inch.
        This should be called right after SetImage(), and will let us return
        appropriate font sizes for the text.
        '''
        self.API.set_source_resolution(self.handle, ppi)

    def set_rectangle(self, left: int, top: int, width: int, height: int):
        '''
        Restrict recognition to a sub-rectangle of the image. Call after
        SetImage.
        Each SetRectangle clears the recogntion results so multiple rectangles
        can be recognized with the same image.
        '''
        self.API.set_rectangle(self.handle, left, top, width, height)

    def get_thresholded_image(self) -> LPPix:
        '''
        ONLY available after SetImage if you have Leptonica installed.
        Get a copy of the internal thresholded image from Tesseract.
        '''
        return self.API.get_thresholded_image(self.handle)

    def get_regions(self) -> tuple[LPBoxa, LPPixa]:
        '''
        Get the result of page layout analysis as a leptonica-style
        Boxa, Pixa pair, in reading order.
        Can be called before or after Recognize.
        '''
        return self.API.get_regions(self.handle)

    def get_textlines(self) -> tuple[LPBoxa, LPPixa, list[int]]:
        '''
        Get the textlines as a leptonica-style Boxa, Pixa pair, in reading
        order.
        Can be called before or after Recognize.
        If blockids is not nullptr, the block-id of each line is also returned
        as an array of one element per line. delete [] after use.
        If paraids is not nullptr, the paragraph-id of each line within its
        block is also returned as an array of one element per line. delete []
        after use.
        '''
        return self.API.get_textlines(self.handle)

    def get_textlines1(self, raw_image: bool,
                       raw_padding: int) -> tuple[LPBoxa, LPPixa,
                                                  list[int], list[int]]:
        '''
        Get the textlines as a leptonica-style Boxa, Pixa pair, in reading
        order.
        Can be called before or after Recognize.
        If blockids is not nullptr, the block-id of each line is also returned
        as an array of one element per line. delete [] after use.
        If paraids is not nullptr, the paragraph-id of each line within its
        block is also returned as an array of one element per line. delete []
        after use.
        '''
        return self.API.get_textlines1(self.handle, raw_image, raw_padding)

    def get_strips(self) -> tuple[LPBoxa, LPPixa, list[int]]:
        '''
        Get textlines and strips of image regions as a leptonica-style Boxa,
        Pixa pair, in reading order. Enables downstream handling of
        non-rectangular regions.
        Can be called before or after Recognize.
        If blockids is not nullptr, the block-id of each line is also returned
        as an array of one element per line. delete [] after use.
        '''
        return self.API.get_strips(self.handle)

    def get_words(self) -> tuple[LPBoxa, LPPixa]:
        '''
        Get the words as a leptonica-style Boxa, Pixa pair, in reading order.
        Can be called before or after Recognize.
        '''
        return self.API.get_words(self.handle)

    def get_connected_components(self) -> tuple[LPBoxa, LPPixa]:
        '''
        Gets the individual connected (text) components (created
        after pages segmentation step, but before recognition)
        as a leptonica-style Boxa, Pixa pair, in reading order.
        Can be called before or after Recognize.
        '''
        return self.API.get_connected_components(self.handle)

    def get_component_images(self, level: PageIteratorLevel,
                             text_only: bool) -> tuple[LPBoxa, LPPixa,
                                                       list[int]]:
        '''
        Get the given level kind of components (block, textline, word etc.)
        as a leptonica-style Boxa, Pixa pair, in reading order.
        Can be called before or after Recognize.
        If blockids is not nullptr, the block-id of each component is also
        returned as an array of one element per component. delete [] after use.
        If text_only is true, then only text components are returned.
        '''
        return self.API.get_component_images(self.handle, level, text_only)

    def get_component_images1(self, level: PageIteratorLevel, text_only: bool,
                              raw_image: bool,
                              raw_padding: int) -> tuple[LPBoxa, LPPixa,
                                                         list[int], list[int]]:
        '''
        Get the given level kind of components (block, textline, word etc.)
        as a leptonica-style Boxa, Pixa pair, in reading order.
        Can be called before or after Recognize.
        If blockids is not nullptr, the block-id of each component is also
        returned as an array of one element per component. delete [] after use.
        If text_only is true, then only text components are returned.
        '''
        return self.API.get_component_images1(self.handle, level, text_only,
                                              raw_image, raw_padding)

    def get_thresholded_image_scale_factor(self) -> int:
        '''Scale factor from original image.'''
        return self.API.get_thresholded_image_scale_factor(self.handle)

    def analyse_layout(self) -> PageIterator:
        '''
        Runs page layout analysis in the mode set by SetPageSegMode.
        May optionally be called prior to Recognize to get access to just
        the page layout results. Returns an iterator to the results.
        If merge_similar_words is true, words are combined where suitable for
        use with a line recognizer. Use if you want to use AnalyseLayout to
        find the textlines, and then want to process textline fragments with
        an external line recognizer.
        Returns nullptr on error or an empty page.
        The returned iterator must be deleted after use.
        WARNING! This class points to data held within the TessBaseAPI class,
        and therefore can only be used while the TessBaseAPI class still exists
        and has not been subjected to a call of Init, SetImage, Recognize,
        Clear, End DetectOS, or anything else that changes the internal
        PAGE_RES.
        '''
        iterator = self.API.analyse_layout(self.handle)
        if not iterator:
            return None
        return PageIterator(iterator)

    def recognize(self, monitor: ProgressMonitor = None) -> int:
        '''
        Recognize the tesseract global image and return the result as Tesseract
        internal structures.
        '''
        return self.API.recognize(self.handle, monitor)

    def process_pages(self, filename: str, retry_config: str,
                      timeout_millisec: int, renderer: ResultRenderer) -> bool:
        '''
        Master ProcessPages calls ProcessPagesInternal and then does any post-
        processing required due to being in a training mode.
        '''
        return self.API.process_pages(self.handle, filename, retry_config,
                                      timeout_millisec, renderer)

    def process_page(self, pix: LPPix, page_index: int, filename: bytes,
                     retry_config: bytes, timeout_millisec: int,
                     renderer: ResultRenderer) -> bool:
        return self.API.process_page(self.handle, pix, page_index, filename,
                                     retry_config, timeout_millisec,
                                     renderer)

    def get_iterator(self) -> ResultIterator:
        '''
        Get a reading-order iterator to the results of LayoutAnalysis and/or
        Recognize. The returned iterator must be deleted after use.
        WARNING! This class points to data held within the TessBaseAPI class,
        and therefore can only be used while the TessBaseAPI class still exists
        and has not been subjected to a call of Init, SetImage, Recognize,
        Clear, End DetectOS, or anything else that changes the internal
        PAGE_RES.
        '''
        iterator = self.API.get_iterator(self.handle)
        if not iterator:
            return None
        return ResultIterator(iterator)

    def get_mutable_iterator(self) -> MutableIterator:
        '''
        Get a mutable iterator to the results of LayoutAnalysis and/or
        Recognize.The returned iterator must be deleted after use.
        WARNING! This class points to data held within the TessBaseAPI class,
        and therefore can only be used while the TessBaseAPI class still exists
        and has not been subjected to a call of Init, SetImage, Recognize,
        Clear, End DetectOS, or anything else that changes the internal
        PAGE_RES.
        '''
        iterator = self.API.get_mutable_iterator(self.handle)
        if not bool(iterator):
            return None
        return MutableIterator(iterator)

    def get_utf8_text(self) -> str:
        '''Make a text string from the internal data structures.'''
        return self.API.get_utf8_text(self.handle)

    def get_hocr_text(self, page_number: int) -> str:
        '''
        Make a HTML-formatted string with hOCR markup from the internal
        data structures.
        page_number is 0-based but will appear in the output as 1-based.
        Image name/input_file_ can be set by SetInputName before calling
        GetHOCRText
        STL removed from original patch submission and refactored by rays.
        Returned string must be freed with the delete [] operator.
        '''
        return self.API.get_hocr_text(self.handle, page_number)

    def get_alto_text(self, page_number: int) -> str:
        '''
        Make an XML-formatted string with ALTO markup from the internal
        data structures.
        '''
        return self.API.get_alto_text(self.handle, page_number)

    def get_tsv_text(self, page_number: int) -> str:
        '''
        Make a TSV-formatted string from the internal data structures.
        page_number is 0-based but will appear in the output as 1-based.
        Returned string must be freed with the delete [] operator.
        '''
        return self.API.get_tsv_text(self.handle, page_number)

    def get_box_text(self, page_number: int) -> str:
        '''
        The recognized text is returned as a char* which is coded
        as a UTF8 box file.
        page_number is a 0-base page index that will appear in the box file.
        Returned string must be freed with the delete [] operator.
        '''
        return self.API.get_box_text(self.handle, page_number)

    def get_lstm_box_text(self, page_number: int) -> str:
        '''
        Create a UTF8 box file for LSTM training from the internal data
        structures.
        page_number is a 0-base page index that will appear in the box file.
        Returned string must be freed with the delete [] operator.
        '''
        return self.API.get_lstm_box_text(self.handle, page_number)

    def get_word_str_box_text(self, page_number: int) -> str:
        '''
        Create a UTF8 box file with WordStr strings from the internal data
        structures. page_number is a 0-base page index that will appear in the
        box file. Returned string must be freed with the delete [] operator.
        '''
        return self.API.get_word_str_box_text(self.handle, page_number)

    def get_unlv_text(self) -> str:
        '''
        The recognized text is returned as a char* which is coded
        as UNLV format Latin-1 with specific reject and suspect codes.
        Returned string must be freed with the delete [] operator.
        '''
        return self.API.get_unlv_text(self.handle)

    def mean_text_conf(self) -> int:
        '''Returns the average word confidence for Tesseract page result.'''
        return self.API.mean_text_conf(self.handle)

    def all_word_confidences(self) -> list[int]:
        '''Returns an array of all word confidences, terminated by -1.'''
        return self.API.all_word_confidences(self.handle)

    def adapt_to_word_str(self, mode: PageSegMode, wordstr: str) -> bool:
        '''
        Applies the given word to the adaptive classifier if possible.
        The word must be SPACE-DELIMITED UTF-8 - l i k e t h i s , so it can
        tell the boundaries of the graphemes.
        Assumes that SetImage/SetRectangle have been used to set the image
        to the given word. The mode arg should be PSM_SINGLE_WORD or
        PSM_CIRCLE_WORD, as that will be used to control layout analysis.
        The currently set PageSegMode is preserved.
        Returns false if adaption was not possible for some reason.
        '''
        return self.API.adapt_to_word_str(self.handle, mode, wordstr)

    def clear(self):
        '''
        Free up recognition results and any stored image data, without actually
        freeing any recognition data that would be time-consuming to reload.
        Afterwards, you must call SetImage or TesseractRect before doing
        any Recognize or Get* operation.
        '''
        self.API.clear(self.handle)

    def end(self):
        '''
        Close down tesseract and free up all memory. End() is equivalent to
        destructing and reconstructing your TessBaseAPI.
        Once End() has been used, none of the other API functions may be used
        other than Init and anything declared above it in the class definition.
        '''
        self.API.end(self.handle)

    def is_valid_word(self, word: str) -> int:
        '''
        Check whether a word is valid according to Tesseract's language model
        returns 0 if the word is invalid, non-zero if valid
        '''
        return self.API.is_valid_word(self.handle, word)

    def get_text_direction(self) -> tuple[int, float]:
        '''
        TODO(rays) Obsolete this function and replace with a more aptly named
        function that returns image coordinates rather than tesseract
        coordinates.
        '''
        return self.API.get_text_direction(self.handle)

    def get_unichar(self, unichar_id: int) -> bytes:
        '''This method returns the string form of the specified unichar.'''
        return self.API.get_unichar(self.handle, unichar_id)

    def clear_persistent_cache(self):
        '''
        Clear any library-level memory caches.
        There are a variety of expensive-to-load constant data structures (
        mostly language dictionaries) that are cached globally -- surviving the
        Init() and End() of individual TessBaseAPI's.  This function allows
        the clearing of these caches.
        '''
        self.API.clear_persistent_cache(self.handle)

    def detect_orientation_script(self) -> OrientationScript:
        '''
        Detect the orientation of the input image and apparent script
        (alphabet).
        orient_deg is the detected clockwise rotation of the input image in
        degrees (0, 90, 180, 270)
        orient_conf is the confidence (15.0 is reasonably confident)
        script_name is an ASCII string, the name of the script, e.g. "Latin"
        script_conf is confidence level in the script
        Returns true on success and writes values to each parameter as an
        output
        '''
        return self.API.detect_orientation_script(self.handle)

    def set_min_orientation_margin(self, margin: float):
        '''
        Min acceptable orientation margin (difference in scores between top and
        2nd choice in OSResults::orientations) to believe the page orientation.
        '''
        self.API.set_min_orientation_margin(self.handle, margin)

    def num_dawgs(self) -> int:
        '''Return the number of dawgs loaded into tesseract_ object.'''
        return self.API.num_dawgs(self.handle)

    def oem(self) -> int:
        '''Last ocr language mode requested.'''
        return self.API.oem(self.handle)

    def get_block_text_orientations(self) -> tuple[int, bool]:
        '''
        Return text orientation of each block as determined in an earlier page
        layout analysis operation. Orientation is returned as the number of
        ccw 90-degree rotations (in [0..3]) required to make the text in the
        block upright(readable). Note that this may not necessary be the block
        orientation preferred for recognition (such as the case of vertical
        CJK text).
        Also returns whether the text in the block is believed to have vertical
        writing direction (when in an upright page orientation).
        The returned array is of length equal to the number of text blocks,
        which may be less than the total number of blocks. The ordering is
        intended to be consistent with GetTextLines().
        '''
        return self.API.get_block_text_orientations(self.handle)
