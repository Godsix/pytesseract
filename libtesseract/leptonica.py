# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 17:10:41 2022

@author: 皓
"""
import weakref
from functools import wraps
from ctypes import pointer, addressof
from .datatype import (c_int_p, c_uint_p, c_float_p, c_ubyte_p, BaseObject,
                       get_point)
from .leptonica_capi import (LPPix, LPLPPix, LPLPPixa,
                             LPBox, LPLPBox, LPBoxa, LPPta, LPPixa, LPNuma)
from .leptonica_papi import (PixAPI, LeptAPI)


def instance_of(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg0, *_ = args
        handle = func(*args, **kwargs)
        if isinstance(arg0, type):
            cls = arg0
        else:
            cls = arg0.__class__
        return cls(handle)
    return wrapper


class PyPix(BaseObject):
    API = PixAPI
    TYPE = LPPix
    INSTANCES = {}

    def __new__(cls, handle):
        if not handle:
            return None
        if not hasattr(handle, 'contents'):
            raise AttributeError(
                f'Handle must be a C pointer,but {type(handle)}')
        try:
            contents = handle.contents
            handle_address = addressof(contents)
        except Exception as e:
            e_name = e.__class__.__name__
            print(f'{e_name}: {e}')
            return None
        if handle_address in cls.INSTANCES:
            instance_ref = cls.INSTANCES[handle_address]
            instance = instance_ref()
            if instance is None:
                instance = super().__new__(cls)
                cls.INSTANCES[handle_address] = weakref.ref(instance)
            return instance
        instance = super().__new__(cls)
        cls.INSTANCES[handle_address] = weakref.ref(instance)
        return instance

    def __del__(self):
        if hasattr(self, 'handle') and self.handle:
            handle = self.handle
            self.handle = None
            self.destroy(handle)

    def __invert__(self):
        return self.invert(None, self.handle)

    def __or__(self, other):
        return self.pix_or(None, self.handle, get_point(other))

    def __and__(self, other):
        return self.pix_and(None, self.handle, get_point(other))

    def __sub__(self, other):
        return self.subtract(None, self.handle, get_point(other))

    def __xor__(self, other):
        return self.xor(None, self.handle, get_point(other))

    def otsu_adaptive_threshold(self, sx: int, sy: int,
                                smoothx: int, smoothy: int,
                                scorefract: float) -> tuple['PyPix', 'PyPix']:
        th, d = self.API.pix_otsu_adaptive_threshold(self.handle, sx, sy,
                                                     smoothx, smoothy,
                                                     scorefract)
        cls = self.__class__
        return cls(th), cls(d)

    def sauvola_binarize_tiled(self, whsize: int, factor: float, nx: int,
                               ny: int) -> tuple['PyPix', 'PyPix']:
        th, d = self.API.pix_sauvola_binarize_tiled(self.handle, whsize,
                                                    factor, nx, ny)
        cls = self.__class__
        return cls(th), cls(d)

    @instance_of
    def reduce_rank_binary_cascade(self, level1: int, level2: int,
                                   level3: int, level4: int) -> 'PyPix':
        return self.API.pix_reduce_rank_binary_cascade(self.handle, level1,
                                                       level2, level3, level4)

    def conn_comp(self, ppixa: LPLPPixa, connectivity: int) -> LPBoxa:
        return self.API.pix_conn_comp(self.handle, ppixa, connectivity)

    def count_conn_comp(self, connectivity: int) -> int:
        return self.API.pix_count_conn_comp(self.handle, connectivity)

    @instance_of
    def blockconv(self, wc: int, hc: int) -> 'PyPix':
        return self.API.pix_blockconv(self.handle, wc, hc)

    @instance_of
    def add_gaussian_noise(self, stdev: float) -> 'PyPix':
        return self.API.pix_add_gaussian_noise(self.handle, stdev)

    def render_box_arb(self, box: LPBox, width: int, rval: int, gval: int,
                       bval: int) -> int:
        return self.API.pix_render_box_arb(
            self.handle, box, width, rval, gval, bval)

    def render_polyline(
            self,
            ptas: LPPta,
            width: int,
            op: int,
            closeflag: int) -> int:
        return self.API.pix_render_polyline(
            self.handle, ptas, width, op, closeflag)

    def render_polyline_arb(
            self,
            ptas: LPPta,
            width: int,
            rval: int,
            gval: int,
            bval: int,
            closeflag: int) -> int:
        return self.API.pix_render_polyline_arb(
            self.handle, ptas, width, rval, gval, bval, closeflag)

    @instance_of
    def erode_gray(self, hsize: int, vsize: int) -> 'PyPix':
        return self.API.pix_erode_gray(self.handle, hsize, vsize)

    @instance_of
    def threshold_to_binary(self, thresh: int) -> 'PyPix':
        return self.API.pix_threshold_to_binary(self.handle, thresh)

    def write_jpeg(self, filename: str, quality: int, progressive: int) -> int:
        return self.API.pix_write_jpeg(filename, self.handle, quality,
                                       progressive)

    @instance_of
    def dilate_brick(
            self,
            pixd: LPPix,
            pixs: LPPix,
            hsize: int,
            vsize: int) -> 'PyPix':
        return self.API.pix_dilate_brick(self.handle, pixs, hsize, vsize)

    @instance_of
    def erode_brick(
            self,
            pixd: LPPix,
            pixs: LPPix,
            hsize: int,
            vsize: int) -> 'PyPix':
        return self.API.pix_erode_brick(self.handle, pixs, hsize, vsize)

    @instance_of
    def open_brick(
            self,
            pixd: LPPix,
            pixs: LPPix,
            hsize: int,
            vsize: int) -> 'PyPix':
        return self.API.pix_open_brick(self.handle, pixs, hsize, vsize)

    @instance_of
    def close_brick(
            self,
            pixd: LPPix,
            pixs: LPPix,
            hsize: int,
            vsize: int) -> 'PyPix':
        return self.API.pix_close_brick(self.handle, pixs, hsize, vsize)

    @instance_of
    def gen_halftone_mask(
            self,
            ppixtext: LPLPPix,
            phtfound: c_int_p,
            debug: int) -> 'PyPix':
        return self.API.pix_gen_halftone_mask(self.handle, ppixtext,
                                              phtfound, debug)

    @instance_of
    def generate_halftone_mask(
            self,
            pixs: LPPix,
            ppixtext: LPLPPix,
            phtfound: c_int_p,
            pixadb: LPPixa) -> 'PyPix':
        return self.API.pix_generate_halftone_mask(
            self.handle, ppixtext, phtfound, pixadb)

    @classmethod
    @instance_of
    def create(cls, width: int, height: int, depth: int) -> 'PyPix':
        return cls.API.pix_create(width, height, depth)

    @classmethod
    @instance_of
    def create_template(cls, pix: 'PyPix') -> 'PyPix':
        return cls.API.pix_create_template(pix)

    @classmethod
    @instance_of
    def create_header(cls, width: int, height: int, depth: int) -> 'PyPix':
        return cls.API.pix_create_header(width, height, depth)

    @instance_of
    def clone(self) -> 'PyPix':
        return self.API.pix_clone(self.handle)

    def destroy(self, handle):
        phandle = pointer(handle)
        self.API.pix_destroy(phandle)

    @instance_of
    def copy(self, pix: 'PyPix') -> 'PyPix':
        return self.API.pix_copy(get_point(pix), self.handle)

    def get_width(self) -> int:
        return self.API.pix_get_width(self.handle)

    def get_height(self) -> int:
        return self.API.pix_get_height(self.handle)

    def get_depth(self) -> int:
        return self.API.pix_get_depth(self.handle)

    def get_dimensions(self) -> tuple[int, int, int]:
        return self.API.pix_get_dimensions(self.handle)

    def get_spp(self) -> int:
        return self.API.pix_get_spp(self.handle)

    def set_spp(self, spp: int):
        self.API.pix_set_spp(self.handle, spp)

    def get_wpl(self) -> int:
        return self.API.pix_get_wpl(self.handle)

    def get_x_res(self) -> int:
        return self.API.pix_get_x_res(self.handle)

    def set_x_res(self, res: int) -> int:
        return self.API.pix_set_x_res(self.handle, res)

    def get_y_res(self) -> int:
        return self.API.pix_get_y_res(self.handle)

    def set_y_res(self, res: int) -> int:
        return self.API.pix_set_y_res(self.handle, res)

    def get_input_format(self) -> int:
        return self.API.pix_get_input_format(self.handle)

    def set_text(self, textstring: str) -> int:
        return self.API.pix_set_text(self.handle, textstring)

    def get_data(self) -> c_uint_p:
        return self.API.pix_get_data(self.handle)

    def set_data(self, data: c_uint_p) -> int:
        return self.API.pix_set_data(self.handle, data)

    def get_pixel(self, x: int, y: int, pval: c_uint_p) -> int:
        return self.API.pix_get_pixel(self.handle, x, y, pval)

    def set_pixel(self, x: int, y: int, val: int) -> int:
        return self.API.pix_set_pixel(self.handle, x, y, val)

    def set_all(self) -> int:
        return self.API.pix_set_all(self.handle)

    def set_all_arbitrary(self, val: int) -> int:
        return self.API.pix_set_all_arbitrary(self.handle, val)

    def clear_in_rect(self, box: LPBox) -> int:
        return self.API.pix_clear_in_rect(self.handle, box)

    def set_in_rect(self, box: LPBox) -> int:
        return self.API.pix_set_in_rect(self.handle, box)

    def set_or_clear_border(
            self,
            pixs: LPPix,
            left: int,
            right: int,
            top: int,
            bot: int,
            op: int) -> int:
        return self.API.pix_set_or_clear_border(
            self.handle, left, right, top, bot, op)

    @instance_of
    def add_border(self, npix: int, val: int) -> 'PyPix':
        return self.API.pix_add_border(self.handle, npix, val)

    def set_masked(self, pixd: LPPix, pixm: LPPix, val: int) -> int:
        return self.API.pix_set_masked(self.handle, pixm, val)

    @classmethod
    @instance_of
    def invert(cls, pixd: LPPix, pixs: LPPix) -> 'PyPix':
        return cls.API.pix_invert(pixd, pixs)

    @classmethod
    @instance_of
    def pix_or(cls, pixd: LPPix, pixs1: LPPix, pixs2: LPPix) -> 'PyPix':
        return cls.API.pix_or(pixd, pixs1, pixs2)

    @classmethod
    @instance_of
    def pix_and(cls, pixd: LPPix, pixs1: LPPix, pixs2: LPPix) -> 'PyPix':
        return cls.API.pix_and(pixd, pixs1, pixs2)

    @classmethod
    @instance_of
    def xor(cls, pixd: LPPix, pixs1: LPPix, pixs2: LPPix) -> 'PyPix':
        return cls.API.pix_xor(pixd, pixs1, pixs2)

    @classmethod
    @instance_of
    def subtract(cls, pixd: LPPix, pixs1: LPPix, pixs2: LPPix) -> 'PyPix':
        return cls.API.pix_subtract(pixd, pixs1, pixs2)

    def zero(self) -> int:
        '''
        Notes:
            (1) For a binary image, if there are no fg (black) pixels,
            empty = 1.
            (2) For a grayscale image, if all pixels are black (0), empty = 1.
            (3) For an RGB image, if all 4 components in every pixel is 0,
            empty = 1.
            (4) For a colormapped image, pixel values are 0.  The colormap
            is ignored.

        Returns
        -------
        int
            1 if all bits in image data field are 0; 0 otherwise.

        '''
        return self.API.pix_zero(self.handle)

    def foreground_fraction(self) -> int:
        return self.API.pix_foreground_fraction(self.handle)

    def count_pixels(self) -> int:
        return self.API.pix_count_pixels(self.handle)

    def count_pixels_by_row(self) -> LPNuma:
        return self.API.pix_count_pixels_by_row(self.handle)

    def count_pixels_in_row(self, row: int) -> int:
        return self.API.pix_count_pixels_in_row(self.handle, row)

    @instance_of
    def clip_rectangle(self, box: LPBox, pboxc: LPLPBox) -> 'PyPix':
        return self.API.pix_clip_rectangle(self.handle, box, pboxc)

    def clip_box_to_foreground(
            self,
            pixs: LPPix,
            boxs: LPBox,
            ppixd: LPLPPix,
            pboxd: LPLPBox) -> int:
        return self.API.pix_clip_box_to_foreground(
            self.handle, boxs, ppixd, pboxd)

    @instance_of
    def convert_to8(self, cmapflag: int) -> 'PyPix':
        return self.API.pix_convert_to8(self.handle, cmapflag)

    @instance_of
    def convert_to32(self) -> 'PyPix':
        return self.API.pix_convert_to32(self.handle)

    @instance_of
    def convert24to32(self) -> 'PyPix':
        return self.API.pix_convert24to32(self.handle)

    @instance_of
    def remove_alpha(self) -> 'PyPix':
        return self.API.pix_remove_alpha(self.handle)

    @instance_of
    def projective(self, vc: c_float_p, incolor: int) -> 'PyPix':
        return self.API.pix_projective(self.handle, vc, incolor)

    @classmethod
    @instance_of
    def read(cls, filename: str) -> 'PyPix':
        return cls.API.pix_read(filename)

    @instance_of
    def read_mem(self, data: c_ubyte_p, size: int) -> 'PyPix':
        return self.API.pix_read_mem(self.handle, size)

    def rasterop(
            self,
            dx: int,
            dy: int,
            dw: int,
            dh: int,
            op: int,
            pixs: LPPix,
            sx: int,
            sy: int) -> int:
        return self.API.pix_rasterop(
            self.handle, dx, dy, dw, dh, op, pixs, sx, sy)

    @instance_of
    def rotate(self, angle: float, type: int, incolor: int, width: int,
               height: int) -> 'PyPix':
        return self.API.pix_rotate(self.handle, angle, type, incolor, width,
                                   height)

    @instance_of
    def rotate_orth(self, quads: int) -> 'PyPix':
        return self.API.pix_rotate_orth(self.handle, quads)

    @instance_of
    def rotate180(self, pixd: LPPix, pixs: LPPix) -> 'PyPix':
        return self.API.pix_rotate180(self.handle, pixs)

    @instance_of
    def scale(self, scalex: float, scaley: float) -> 'PyPix':
        return self.API.pix_scale(self.handle, scalex, scaley)

    @instance_of
    def scale_tosize(self, wd: int, hd: int) -> 'PyPix':
        return self.API.pix_scale_to_size(self.handle, wd, hd)

    @instance_of
    def expand_replicate(self, factor: int) -> 'PyPix':
        return self.API.pix_expand_replicate(self.handle, factor)

    @instance_of
    def seedfill_binary(
            self,
            pixd: LPPix,
            pixs: LPPix,
            pixm: LPPix,
            connectivity: int) -> 'PyPix':
        return self.API.pix_seedfill_binary(
            self.handle, pixs, pixm, connectivity)

    @instance_of
    def distance_function(
            self,
            connectivity: int,
            outdepth: int,
            boundcond: int) -> 'PyPix':
        return self.API.pix_distance_function(
            self.handle, connectivity, outdepth, boundcond)

    @classmethod
    @instance_of
    def read_tiff(self, filename: str, n: int) -> 'PyPix':
        '''
        Notes:
        (1) This is a version of read(), specialized for tiff
        files, that allows specification of the page to be returned
        (2) No warning messages on failure, because of how multi-page
        TIFF reading works. You are supposed to keep trying until
        it stops working.

        Parameters
        ----------
        filename : str
        n : int
            page number 0 based.

        Returns
        -------
        PyPix
            pix, or None on error.

        '''
        return self.API.pix_read_tiff(filename, n)

    def write_tiff(self, filename: str, comptype: int, modestr: str) -> int:
        '''
        Notes:
        (1) For multipage tiff, write the first pix with mode "w" and
        all subsequent pix with mode "a".
        (2) For multipage tiff, there is considerable overhead in the
        machinery to append an image and add the directory entry,
        and the time required for each image increases linearly
        with the number of images in the file.

        Parameters
        ----------
        filename : str
            to write to.
        pix : LPPix
            any depth, colormap will be removed.
        comptype : int
            IFF_TIFF, IFF_TIFF_RLE, IFF_TIFF_PACKBITS,
            IFF_TIFF_G3, IFF_TIFF_G4,
            IFF_TIFF_LZW, IFF_TIFF_ZIP, IFF_TIFF_JPEG.
        modestr : str
            "a" or "w".

        Returns
        -------
        int
            0 if OK, 1 on error.

        '''
        return self.API.pix_write_tiff(filename, self.handle, comptype,
                                       modestr)

    @classmethod
    def read_from_multipage_tiff(self, fname: str,
                                 offset: int) -> tuple['PyPix', int]:
        '''
        Notes:
        (1) This allows overhead for traversal of a multipage tiff file
        to be linear in the number of images.  This will also work
        with a singlepage tiff file.
        (2) No TIFF internal data structures are exposed to the caller
        (thanks to Jeff Breidenbach).
        (3) offset is the byte offset of a particular image in a multipage
        tiff file. To get the first image in the file, input the
        special offset value of 0.
        (4) The offset is updated to point to the next image, for a
        subsequent call.
        (5) On the last image, the offset returned is 0.  Exit the loop
        when the returned offset is 0.
        (6) For reading a multipage tiff from a memory buffer, see
        pixReadMemFromMultipageTiff()
        (7) Example usage for reading all the images in the tif file:
            offset = 0
            pix, offset = read_from_multipage_tiff(filename, offset)
            while not offset == 0:
                pix, offset = read_from_multipage_tiff(filename, offset)
                # do something with pix

        Parameters
        ----------
        fname : str
            filename.
        offset : int
            set offset to 0 for first image.

        Returns
        -------
        tuple['PyPix', int]
            pix, or NULL on error or if previous call returned the last image.

        '''
        ret, off = self.API.pix_read_from_multipage_tiff(fname, offset)
        cls = self.__class__
        return cls(ret), off

    @classmethod
    @instance_of
    def read_mem_tiff(self, cdata: bytes, n: int) -> 'PyPix':
        '''
        Notes:
        (1) This is a version of pixReadTiff(), where the data is read
        from a memory buffer and uncompressed.
        (2) Use TIFFClose(); TIFFCleanup() doesn't free internal memstream.
        (3) No warning messages on failure, because of how multi-page
        TIFF reading works. You are supposed to keep trying until
        it stops working.
        (4) Tiff directory overhead is linear in the input page number.
        If reading many images, use pixReadMemFromMultipageTiff().

        Parameters
        ----------
        cdata : bytes
            tiff-encoded.
        n : int
            page image number: 0-based.

        Returns
        -------
        PyPix
            pix, or NULL on error.

        '''
        return self.API.pix_read_mem_tiff(cdata, n)

    @classmethod
    def read_mem_from_multipage_tiff(self, cdata: bytes,
                                     offset: int) -> tuple['PyPix', int]:
        '''
        Notes:
        (1) This is a read-from-memory version of read_from_multipage_tiff().
        See that function for usage.
        (2) If reading sequentially from the tiff data, this is more
        efficient than read_mem_tiff(), which has an overhead
        proportional to the image index n.
        (3) Example usage for reading all the images:
            offset = 0
            pix, offset = read_from_multipage_tiff(filename, offset)
            while not offset == 0:
                pix, offset = read_mem_from_multipage_tiff(data, offset)
                # do something with pix

        Parameters
        ----------
        cdata : bytes
            DESCRIPTION.
        offset : int
            DESCRIPTION.

        Returns
        -------
        tuple['PyPix', int]
            DESCRIPTION.

        '''
        ret, off = self.API.pix_read_mem_from_multipage_tiff(cdata, offset)
        cls = self.__class__
        return cls(ret), off

    def write(self, fname: str, format: int) -> int:
        '''
        Notes:
            (1) Open for write using binary mode (with the "b" flag)
            to avoid having Windows automatically translate the NL
            into CRLF, which corrupts image files.  On non-windows
            systems this flag should be ignored, per ISO C90.
            Thanks to Dave Bryan for pointing this out.
            (2) If the default image format IFF_DEFAULT is requested:
            use the input format if known; otherwise, use a lossless format.
            (3) The default jpeg quality is 75.  For some other value,
            Use l_jpegSetQuality().

        Parameters
        ----------
        fname : str
            filename.
        format : int
            defined in imageio.h.

        Returns
        -------
        int
            0 if OK; 1 on error.

        '''
        return self.API.pix_write(fname, self.handle, format)

    def write_mem(self, format: int) -> bytes:
        '''
        Notes:
            (1) On windows, this will only write tiff and PostScript to memory.
            For other formats, it requires open_memstream(3).
            (2) PostScript output is uncompressed, in hex ascii.
            Most printers support level 2 compression (tiff_g4 for 1 bpp,
            jpeg for 8 and 32 bpp).
            (3) The default jpeg quality is 75.  For some other value,
            Use l_jpegSetQuality().

        Parameters
        ----------
        format : int
            defined in imageio.h.

        Returns
        -------
        bytes
            pdata data of tiff compressed image

        '''
        return self.API.pix_write_mem(self.handle, format)


class Leptonica:
    @classmethod
    def get_version(self) -> str:
        return LeptAPI.get_version()

    @classmethod
    def pix_read(cls, filename: str) -> PyPix:
        return PyPix.read(filename)
