# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:43:58 2021

@author: 皓
"""
from ctypes import CFUNCTYPE, POINTER, c_void_p, c_char_p
# from ctypes import (c_float, c_int, c_uint, c_ubyte, c_size_t, c_char,
#                     c_double, c_ulonglong, c_ushort)
from .common import LEPT_DLL
from .datatype import (c_float_p, c_int_p, c_uint_p, LP_c_char, c_ubyte_p,
                       c_size_t_p, LPFile, c_double_p, c_char_p_p,
                       c_ulonglong_p, CAPI)
from .pytype.pix import (LPPix, LPLPPix, LPPta, LPBoxa, LPLPPta, LPPixa, LPBox,
                         LPLPBox, LPLPBoxa, LPBoxaa, LPLPBoxaa, LPPtaa,
                         LPLPPixa, LPLPPixColormap, LPPixColormap, LPFPixa,
                         LPLPFPix, LPDPix, LPFPix, LPPixaComp, LPLPFPixa,
                         LPLPDPix, LPPixaa, alloc_fn, LPLPPixaa, LPPixacc,
                         LPLPPixacc, LPPixComp, LPLPPixComp, LPLPPixaComp,
                         LPLPPtaa, LPPixTiling, LPLPPixTiling)
from .pytype.array_h import (LPNuma, LPLPNuma, LPLPNumaa, LPNumaa, LPL_Bytea,
                             LPLPL_Bytea, LPLPL_Dna, LPSarray, LPL_Dna,
                             LPL_Dnaa, LPLPL_Dnaa, LPL_DnaHash, LPLPL_DnaHash,
                             LPLPSarray)
from .pytype.bbuffer import LPL_ByteBuffer, LPLPL_ByteBuffer
from .pytype.morph import (LPL_Kernel, LPSela, LPLPL_Kernel, LPSel, LPLPSel,
                           LPLPSela)
from .pytype.bmf import LPL_Bmf, LPLPL_Bmf
from .pytype.ccbord import LPCCBorda, LPLPCCBorda, LPCCBord, LPLPCCBord
from .pytype.jbclass import LPJbClasser, LPLPJbClasser, LPJbData, LPLPJbData
from .pytype.colorfill import LPL_Colorfill, LPLPL_Colorfill
from .pytype.stack import LPL_Stack, LPLPL_Stack
from .pytype.dewarp import LPL_Dewarp, LPLPL_Dewarp, LPL_Dewarpa, LPLPL_Dewarpa
from .pytype.rbtree import (LPL_Rbtree, LPRb_Type, Rb_Type, LPLPL_Rbtree,
                            LPL_Rbtree_Node)
from .pytype.hashmap import LPL_Hashmap, LPLPL_Hashmap, LPL_Hashitem
from .pytype.gplot import LPGPlot, LPLPGPlot
from .pytype.heap import LPL_Heap, LPLPL_Heap
from .pytype.list_h import LPLPDoubleLinkedList, LPDoubleLinkedList
from .pytype.imageio import (LPLPL_Pdf_Data, LPLPL_Compressed_Data,
                             LPL_Compressed_Data)
from .pytype.ptra import LPL_Ptra, LPLPL_Ptra, LPL_Ptraa, LPLPL_Ptraa
from .pytype.queue import LPL_Queue, LPLPL_Queue
from .pytype.recog import (LPL_Recog, LPLPL_Recog, LPL_Rdid, LPLPL_Rcha,
                           LPLPL_Rch, LPL_Rcha, LPL_Rch)
from .pytype.regutils import LPLPL_RegParams, LPL_RegParams
from .pytype.stringcode import LPL_StrCode, LPLPL_StrCode
from .pytype.sudoku import LPL_Sudoku, LPLPL_Sudoku
from .pytype.environ import LPL_WallTimer, LPLPL_WallTimer
from .pytype.watershed import LPL_WShed, LPLPL_WShed


# void  ( *handler ) ( const char * )
handler_fn = CFUNCTYPE(None, c_char_p)


class LeptCAPI(CAPI):
    NAME = 'Leptonica'
    GLOBALS = globals()

    def capi_pix_clean_background_to_white(self, pixs: LPPix, pixim: LPPix,
                                           pixg: LPPix, gamma: float,
                                           blackval: int,
                                           whiteval: int) -> LPPix:
        return self.pixCleanBackgroundToWhite(pixs, pixim, pixg, gamma,
                                              blackval, whiteval)

    def capi_pix_background_norm_simple(self, pixs: LPPix, pixim: LPPix,
                                        pixg: LPPix) -> LPPix:
        return self.pixBackgroundNormSimple(pixs, pixim, pixg)

    def capi_pix_background_norm(self, pixs: LPPix, pixim: LPPix, pixg: LPPix,
                                 sx: int, sy: int, thresh: int, mincount: int,
                                 bgval: int, smoothx: int,
                                 smoothy: int) -> LPPix:
        return self.pixBackgroundNorm(pixs, pixim, pixg, sx, sy, thresh,
                                      mincount, bgval, smoothx, smoothy)

    def capi_pix_background_norm_morph(self, pixs: LPPix, pixim: LPPix,
                                       reduction: int, size: int,
                                       bgval: int) -> LPPix:
        return self.pixBackgroundNormMorph(pixs, pixim, reduction, size, bgval)

    def capi_pix_background_norm_gray_array(self, pixs: LPPix, pixim: LPPix,
                                            sx: int, sy: int, thresh: int,
                                            mincount: int, bgval: int,
                                            smoothx: int, smoothy: int,
                                            ppixd: LPLPPix) -> int:
        return self.pixBackgroundNormGrayArray(pixs, pixim, sx, sy, thresh,
                                               mincount, bgval, smoothx,
                                               smoothy, ppixd)

    def capi_pix_background_norm_rgb_arrays(self, pixs: LPPix, pixim: LPPix,
                                            pixg: LPPix, sx: int, sy: int,
                                            thresh: int, mincount: int,
                                            bgval: int, smoothx: int,
                                            smoothy: int, ppixr: LPLPPix,
                                            ppixg: LPLPPix,
                                            ppixb: LPLPPix) -> int:
        return self.pixBackgroundNormRGBArrays(pixs, pixim, pixg, sx, sy,
                                               thresh, mincount, bgval,
                                               smoothx, smoothy, ppixr, ppixg,
                                               ppixb)

    def capi_pix_background_norm_gray_array_morph(self, pixs: LPPix,
                                                  pixim: LPPix, reduction: int,
                                                  size: int, bgval: int,
                                                  ppixd: LPLPPix) -> int:
        return self.pixBackgroundNormGrayArrayMorph(pixs, pixim, reduction,
                                                    size, bgval, ppixd)

    def capi_pix_background_norm_rgb_arrays_morph(self, pixs: LPPix,
                                                  pixim: LPPix, reduction: int,
                                                  size: int, bgval: int,
                                                  ppixr: LPLPPix,
                                                  ppixg: LPLPPix,
                                                  ppixb: LPLPPix) -> int:
        return self.pixBackgroundNormRGBArraysMorph(pixs, pixim, reduction,
                                                    size, bgval, ppixr, ppixg,
                                                    ppixb)

    def capi_pix_get_background_gray_map(self, pixs: LPPix, pixim: LPPix,
                                         sx: int, sy: int, thresh: int,
                                         mincount: int,
                                         ppixd: LPLPPix) -> int:
        return self.pixGetBackgroundGrayMap(pixs, pixim, sx, sy, thresh,
                                            mincount, ppixd)

    def capi_pix_get_background_rgb_map(self, pixs: LPPix, pixim: LPPix,
                                        pixg: LPPix, sx: int, sy: int,
                                        thresh: int, mincount: int,
                                        ppixmr: LPLPPix, ppixmg: LPLPPix,
                                        ppixmb: LPLPPix) -> int:
        return self.pixGetBackgroundRGBMap(pixs, pixim, pixg, sx, sy, thresh,
                                           mincount, ppixmr, ppixmg, ppixmb)

    def capi_pix_get_background_gray_map_morph(self, pixs: LPPix, pixim: LPPix,
                                               reduction: int, size: int,
                                               ppixm: LPLPPix) -> int:
        return self.pixGetBackgroundGrayMapMorph(pixs, pixim, reduction, size,
                                                 ppixm)

    def capi_pix_get_background_rgb_map_morph(self, pixs: LPPix, pixim: LPPix,
                                              reduction: int, size: int,
                                              ppixmr: LPLPPix, ppixmg: LPLPPix,
                                              ppixmb: LPLPPix) -> int:
        return self.pixGetBackgroundRGBMapMorph(pixs, pixim, reduction, size,
                                                ppixmr, ppixmg, ppixmb)

    def capi_pix_fill_map_holes(self, pix: LPPix, nx: int, ny: int,
                                filltype: int) -> int:
        return self.pixFillMapHoles(pix, nx, ny, filltype)

    def capi_pix_extend_by_replication(self, pixs: LPPix, addw: int,
                                       addh: int) -> LPPix:
        return self.pixExtendByReplication(pixs, addw, addh)

    def capi_pix_smooth_connected_regions(self, pixs: LPPix, pixm: LPPix,
                                          factor: int) -> int:
        return self.pixSmoothConnectedRegions(pixs, pixm, factor)

    def capi_pix_get_inv_background_map(self, pixs: LPPix, bgval: int,
                                        smoothx: int, smoothy: int) -> LPPix:
        return self.pixGetInvBackgroundMap(pixs, bgval, smoothx, smoothy)

    def capi_pix_apply_inv_background_gray_map(self, pixs: LPPix, pixm: LPPix,
                                               sx: int, sy: int) -> LPPix:
        return self.pixApplyInvBackgroundGrayMap(pixs, pixm, sx, sy)

    def capi_pix_apply_inv_background_rgb_map(self, pixs: LPPix, pixmr: LPPix,
                                              pixmg: LPPix, pixmb: LPPix,
                                              sx: int, sy: int) -> LPPix:
        return self.pixApplyInvBackgroundRGBMap(pixs, pixmr, pixmg, pixmb, sx,
                                                sy)

    def capi_pix_apply_variable_gray_map(self, pixs: LPPix, pixg: LPPix,
                                         target: int) -> LPPix:
        return self.pixApplyVariableGrayMap(pixs, pixg, target)

    def capi_pix_global_norm_rgb(self, pixd: LPPix, pixs: LPPix, rval: int,
                                 gval: int, bval: int, mapval: int) -> LPPix:
        return self.pixGlobalNormRGB(pixd, pixs, rval, gval, bval, mapval)

    def capi_pix_global_norm_no_sat_rgb(self, pixd: LPPix, pixs: LPPix,
                                        rval: int, gval: int, bval: int,
                                        factor: int, rank: float) -> LPPix:
        return self.pixGlobalNormNoSatRGB(pixd, pixs, rval, gval, bval, factor,
                                          rank)

    def capi_pix_threshold_spread_norm(self, pixs: LPPix, filtertype: int,
                                       edgethresh: int, smoothx: int,
                                       smoothy: int, gamma: float, minval: int,
                                       maxval: int, targetthresh: int,
                                       ppixth: LPLPPix, ppixb: LPLPPix,
                                       ppixd: LPLPPix) -> int:
        return self.pixThresholdSpreadNorm(pixs, filtertype, edgethresh,
                                           smoothx, smoothy, gamma, minval,
                                           maxval, targetthresh, ppixth, ppixb,
                                           ppixd)

    def capi_pix_background_norm_flex(self, pixs: LPPix, sx: int, sy: int,
                                      smoothx: int, smoothy: int,
                                      delta: int) -> LPPix:
        return self.pixBackgroundNormFlex(pixs, sx, sy, smoothx, smoothy,
                                          delta)

    def capi_pix_contrast_norm(self, pixd: LPPix, pixs: LPPix, sx: int,
                               sy: int, mindiff: int, smoothx: int,
                               smoothy: int) -> LPPix:
        return self.pixContrastNorm(pixd, pixs, sx, sy, mindiff, smoothx,
                                    smoothy)

    def capi_pix_affine_sampled_pta(self, pixs: LPPix, ptad: LPPta,
                                    ptas: LPPta, incolor: int) -> LPPix:
        return self.pixAffineSampledPta(pixs, ptad, ptas, incolor)

    def capi_pix_affine_sampled(self, pixs: LPPix, vc: c_float_p,
                                incolor: int) -> LPPix:
        return self.pixAffineSampled(pixs, vc, incolor)

    def capi_pix_affine_pta(self, pixs: LPPix, ptad: LPPta, ptas: LPPta,
                            incolor: int) -> LPPix:
        return self.pixAffinePta(pixs, ptad, ptas, incolor)

    def capi_pix_affine(self, pixs: LPPix, vc: c_float_p,
                        incolor: int) -> LPPix:
        return self.pixAffine(pixs, vc, incolor)

    def capi_pix_affine_pta_color(self, pixs: LPPix, ptad: LPPta, ptas: LPPta,
                                  colorval: int) -> LPPix:
        return self.pixAffinePtaColor(pixs, ptad, ptas, colorval)

    def capi_pix_affine_color(self, pixs: LPPix, vc: c_float_p,
                              colorval: int) -> LPPix:
        return self.pixAffineColor(pixs, vc, colorval)

    def capi_pix_affine_pta_gray(self, pixs: LPPix, ptad: LPPta, ptas: LPPta,
                                 grayval: int) -> LPPix:
        return self.pixAffinePtaGray(pixs, ptad, ptas, grayval)

    def capi_pix_affine_gray(self, pixs: LPPix, vc: c_float_p,
                             grayval: int) -> LPPix:
        return self.pixAffineGray(pixs, vc, grayval)

    def capi_pix_affine_pta_with_alpha(self, pixs: LPPix, ptad: LPPta,
                                       ptas: LPPta, pixg: LPPix, fract: float,
                                       border: int) -> LPPix:
        return self.pixAffinePtaWithAlpha(pixs, ptad, ptas, pixg, fract,
                                          border)

    def capi_get_affine_xform_coeffs(self, ptas: LPPta, ptad: LPPta,
                                     pvc: POINTER(c_float_p)) -> int:
        return self.getAffineXformCoeffs(ptas, ptad, pvc)

    def capi_affine_invert_xform(self, vc: c_float_p,
                                 pvci: POINTER(c_float_p)) -> int:
        return self.affineInvertXform(vc, pvci)

    def capi_affine_xform_sampled_pt(self, vc: c_float_p, x: int, y: int,
                                     pxp: c_int_p, pyp: c_int_p) -> int:
        return self.affineXformSampledPt(vc, x, y, pxp, pyp)

    def capi_affine_xform_pt(self, vc: c_float_p, x: int, y: int,
                             pxp: c_float_p, pyp: c_float_p) -> int:
        return self.affineXformPt(vc, x, y, pxp, pyp)

    def capi_linear_interpolate_pixel_color(self, datas: c_uint_p, wpls: int,
                                            w: int, h: int, x: float, y: float,
                                            colorval: int,
                                            pval: c_uint_p) -> int:
        return self.linearInterpolatePixelColor(datas, wpls, w, h, x, y,
                                                colorval, pval)

    def capi_linear_interpolate_pixel_gray(self, datas: c_uint_p, wpls: int,
                                           w: int, h: int, x: float, y: float,
                                           grayval: int,
                                           pval: c_int_p) -> int:
        return self.linearInterpolatePixelGray(datas, wpls, w, h, x, y,
                                               grayval, pval)

    def capi_gaussjordan(self, a: POINTER(c_float_p), b: c_float_p,
                         n: int) -> int:
        return self.gaussjordan(a, b, n)

    def capi_pix_affine_sequential(self, pixs: LPPix, ptad: LPPta, ptas: LPPta,
                                   bw: int, bh: int) -> LPPix:
        return self.pixAffineSequential(pixs, ptad, ptas, bw, bh)

    def capi_create_matrix2d_translate(self, transx: float,
                                       transy: float) -> c_float_p:
        return self.createMatrix2dTranslate(transx, transy)

    def capi_create_matrix2d_scale(self, scalex: float,
                                   scaley: float) -> c_float_p:
        return self.createMatrix2dScale(scalex, scaley)

    def capi_create_matrix2d_rotate(self, xc: float, yc: float,
                                    angle: float) -> c_float_p:
        return self.createMatrix2dRotate(xc, yc, angle)

    def capi_pta_translate(self, ptas: LPPta, transx: float,
                           transy: float) -> LPPta:
        return self.ptaTranslate(ptas, transx, transy)

    def capi_pta_scale(self, ptas: LPPta, scalex: float,
                       scaley: float) -> LPPta:
        return self.ptaScale(ptas, scalex, scaley)

    def capi_pta_rotate(self, ptas: LPPta, xc: float, yc: float,
                        angle: float) -> LPPta:
        return self.ptaRotate(ptas, xc, yc, angle)

    def capi_boxa_translate(self, boxas: LPBoxa, transx: float,
                            transy: float) -> LPBoxa:
        return self.boxaTranslate(boxas, transx, transy)

    def capi_boxa_scale(self, boxas: LPBoxa, scalex: float,
                        scaley: float) -> LPBoxa:
        return self.boxaScale(boxas, scalex, scaley)

    def capi_boxa_rotate(self, boxas: LPBoxa, xc: float, yc: float,
                         angle: float) -> LPBoxa:
        return self.boxaRotate(boxas, xc, yc, angle)

    def capi_pta_affine_transform(self, ptas: LPPta, mat: c_float_p) -> LPPta:
        return self.ptaAffineTransform(ptas, mat)

    def capi_boxa_affine_transform(self, boxas: LPBoxa,
                                   mat: c_float_p) -> LPBoxa:
        return self.boxaAffineTransform(boxas, mat)

    def capi_l_productMatVec(self, mat: c_float_p, vecs: c_float_p,
                             vecd: c_float_p, size: int) -> int:
        return self.l_productMatVec(mat, vecs, vecd, size)

    def capi_l_productMat2(self, mat1: c_float_p, mat2: c_float_p,
                           matd: c_float_p, size: int) -> int:
        return self.l_productMat2(mat1, mat2, matd, size)

    def capi_l_productMat3(self, mat1: c_float_p, mat2: c_float_p,
                           mat3: c_float_p, matd: c_float_p,
                           size: int) -> int:
        return self.l_productMat3(mat1, mat2, mat3, matd, size)

    def capi_l_productMat4(self, mat1: c_float_p, mat2: c_float_p,
                           mat3: c_float_p, mat4: c_float_p, matd: c_float_p,
                           size: int) -> int:
        return self.l_productMat4(mat1, mat2, mat3, mat4, matd, size)

    def capi_l_getDataBit(self, line: c_void_p, n: int) -> int:
        return self.l_getDataBit(line, n)

    def capi_l_setDataBit(self, line: c_void_p, n: int):
        self.l_setDataBit(line, n)

    def capi_l_clearDataBit(self, line: c_void_p, n: int):
        self.l_clearDataBit(line, n)

    def capi_l_setDataBitVal(self, line: c_void_p, n: int, val: int):
        self.l_setDataBitVal(line, n, val)

    def capi_l_getDataDibit(self, line: c_void_p, n: int) -> int:
        return self.l_getDataDibit(line, n)

    def capi_l_setDataDibit(self, line: c_void_p, n: int, val: int):
        self.l_setDataDibit(line, n, val)

    def capi_l_clearDataDibit(self, line: c_void_p, n: int):
        self.l_clearDataDibit(line, n)

    def capi_l_getDataQbit(self, line: c_void_p, n: int) -> int:
        return self.l_getDataQbit(line, n)

    def capi_l_setDataQbit(self, line: c_void_p, n: int, val: int):
        self.l_setDataQbit(line, n, val)

    def capi_l_clearDataQbit(self, line: c_void_p, n: int):
        self.l_clearDataQbit(line, n)

    def capi_l_getDataByte(self, line: c_void_p, n: int) -> int:
        return self.l_getDataByte(line, n)

    def capi_l_setDataByte(self, line: c_void_p, n: int, val: int):
        self.l_setDataByte(line, n, val)

    def capi_l_getDataTwoBytes(self, line: c_void_p, n: int) -> int:
        return self.l_getDataTwoBytes(line, n)

    def capi_l_setDataTwoBytes(self, line: c_void_p, n: int, val: int):
        self.l_setDataTwoBytes(line, n, val)

    def capi_l_getDataFourBytes(self, line: c_void_p, n: int) -> int:
        return self.l_getDataFourBytes(line, n)

    def capi_l_setDataFourBytes(self, line: c_void_p, n: int, val: int):
        self.l_setDataFourBytes(line, n, val)

    def capi_barcode_dispatch_decoder(self, barstr: LP_c_char, format: int,
                                      debugflag: int) -> LP_c_char:
        return self.barcodeDispatchDecoder(barstr, format, debugflag)

    def capi_barcode_format_is_supported(self, format: int) -> int:
        return self.barcodeFormatIsSupported(format)

    def capi_pix_find_baselines(self, pixs: LPPix, ppta: LPLPPta,
                                pixadb: LPPixa) -> LPNuma:
        return self.pixFindBaselines(pixs, ppta, pixadb)

    def capi_pix_deskew_local(self, pixs: LPPix, nslices: int, redsweep: int,
                              redsearch: int, sweeprange: float,
                              sweepdelta: float, minbsdelta: float) -> LPPix:
        return self.pixDeskewLocal(pixs, nslices, redsweep, redsearch,
                                   sweeprange, sweepdelta, minbsdelta)

    def capi_pix_get_local_skew_transform(self, pixs: LPPix, nslices: int,
                                          redsweep: int, redsearch: int,
                                          sweeprange: float, sweepdelta: float,
                                          minbsdelta: float, pptas: LPLPPta,
                                          pptad: LPLPPta) -> int:
        return self.pixGetLocalSkewTransform(pixs, nslices, redsweep,
                                             redsearch, sweeprange, sweepdelta,
                                             minbsdelta, pptas, pptad)

    def capi_pix_get_local_skew_angles(self, pixs: LPPix, nslices: int,
                                       redsweep: int, redsearch: int,
                                       sweeprange: float, sweepdelta: float,
                                       minbsdelta: float, pa: c_float_p,
                                       pb: c_float_p, debug: int) -> LPNuma:
        return self.pixGetLocalSkewAngles(pixs, nslices, redsweep, redsearch,
                                          sweeprange, sweepdelta, minbsdelta,
                                          pa, pb, debug)

    def capi_bbuffer_create(self, indata: c_ubyte_p,
                            nalloc: int) -> LPL_ByteBuffer:
        return self.bbufferCreate(indata, nalloc)

    def capi_bbuffer_destroy(self, pbb: LPLPL_ByteBuffer):
        self.bbufferDestroy(pbb)

    def capi_bbuffer_destroy_and_save_data(self, pbb: LPLPL_ByteBuffer,
                                           pnbytes: c_size_t_p) -> c_ubyte_p:
        return self.bbufferDestroyAndSaveData(pbb, pnbytes)

    def capi_bbuffer_read(self, bb: LPL_ByteBuffer, src: c_ubyte_p,
                          nbytes: int) -> int:
        return self.bbufferRead(bb, src, nbytes)

    def capi_bbuffer_read_stream(self, bb: LPL_ByteBuffer, fp: LPFile,
                                 nbytes: int) -> int:
        return self.bbufferReadStream(bb, fp, nbytes)

    def capi_bbuffer_extend_array(self, bb: LPL_ByteBuffer,
                                  nbytes: int) -> int:
        return self.bbufferExtendArray(bb, nbytes)

    def capi_bbuffer_write(self, bb: LPL_ByteBuffer, dest: c_ubyte_p,
                           nbytes: int, pnout: c_size_t_p) -> int:
        return self.bbufferWrite(bb, dest, nbytes, pnout)

    def capi_bbuffer_write_stream(self, bb: LPL_ByteBuffer, fp: LPFile,
                                  nbytes: int, pnout: c_size_t_p) -> int:
        return self.bbufferWriteStream(bb, fp, nbytes, pnout)

    def capi_pix_bilateral(self, pixs: LPPix, spatial_stdev: float,
                           range_stdev: float, ncomps: int,
                           reduction: int) -> LPPix:
        return self.pixBilateral(pixs, spatial_stdev, range_stdev, ncomps,
                                 reduction)

    def capi_pix_bilateral_gray(self, pixs: LPPix, spatial_stdev: float,
                                range_stdev: float, ncomps: int,
                                reduction: int) -> LPPix:
        return self.pixBilateralGray(pixs, spatial_stdev, range_stdev, ncomps,
                                     reduction)

    def capi_pix_bilateral_exact(self, pixs: LPPix, spatial_kel: LPL_Kernel,
                                 range_kel: LPL_Kernel) -> LPPix:
        return self.pixBilateralExact(pixs, spatial_kel, range_kel)

    def capi_pix_bilateral_gray_exact(self, pixs: LPPix,
                                      spatial_kel: LPL_Kernel,
                                      range_kel: LPL_Kernel) -> LPPix:
        return self.pixBilateralGrayExact(pixs, spatial_kel, range_kel)

    def capi_pix_block_bilateral_exact(self, pixs: LPPix, spatial_stdev: float,
                                       range_stdev: float) -> LPPix:
        return self.pixBlockBilateralExact(pixs, spatial_stdev, range_stdev)

    def capi_make_range_kernel(self, range_stdev: float) -> LPL_Kernel:
        return self.makeRangeKernel(range_stdev)

    def capi_pix_bilinear_sampled_pta(self, pixs: LPPix, ptad: LPPta,
                                      ptas: LPPta, incolor: int) -> LPPix:
        return self.pixBilinearSampledPta(pixs, ptad, ptas, incolor)

    def capi_pix_bilinear_sampled(self, pixs: LPPix, vc: c_float_p,
                                  incolor: int) -> LPPix:
        return self.pixBilinearSampled(pixs, vc, incolor)

    def capi_pix_bilinear_pta(self, pixs: LPPix, ptad: LPPta, ptas: LPPta,
                              incolor: int) -> LPPix:
        return self.pixBilinearPta(pixs, ptad, ptas, incolor)

    def capi_pix_bilinear(self, pixs: LPPix, vc: c_float_p,
                          incolor: int) -> LPPix:
        return self.pixBilinear(pixs, vc, incolor)

    def capi_pix_bilinear_pta_color(self, pixs: LPPix, ptad: LPPta,
                                    ptas: LPPta, colorval: int) -> LPPix:
        return self.pixBilinearPtaColor(pixs, ptad, ptas, colorval)

    def capi_pix_bilinear_color(self, pixs: LPPix, vc: c_float_p,
                                colorval: int) -> LPPix:
        return self.pixBilinearColor(pixs, vc, colorval)

    def capi_pix_bilinear_pta_gray(self, pixs: LPPix, ptad: LPPta, ptas: LPPta,
                                   grayval: int) -> LPPix:
        return self.pixBilinearPtaGray(pixs, ptad, ptas, grayval)

    def capi_pix_bilinear_gray(self, pixs: LPPix, vc: c_float_p,
                               grayval: int) -> LPPix:
        return self.pixBilinearGray(pixs, vc, grayval)

    def capi_pix_bilinear_pta_with_alpha(self, pixs: LPPix, ptad: LPPta,
                                         ptas: LPPta, pixg: LPPix,
                                         fract: float, border: int) -> LPPix:
        return self.pixBilinearPtaWithAlpha(pixs, ptad, ptas, pixg, fract,
                                            border)

    def capi_get_bilinear_xform_coeffs(self, ptas: LPPta, ptad: LPPta,
                                       pvc: POINTER(c_float_p)) -> int:
        return self.getBilinearXformCoeffs(ptas, ptad, pvc)

    def capi_bilinear_xform_sampled_pt(self, vc: c_float_p, x: int, y: int,
                                       pxp: c_int_p, pyp: c_int_p) -> int:
        return self.bilinearXformSampledPt(vc, x, y, pxp, pyp)

    def capi_bilinear_xform_pt(self, vc: c_float_p, x: int, y: int,
                               pxp: c_float_p, pyp: c_float_p) -> int:
        return self.bilinearXformPt(vc, x, y, pxp, pyp)

    def capi_pix_otsu_adaptive_threshold(self, pixs: LPPix, sx: int, sy: int,
                                         smoothx: int, smoothy: int,
                                         scorefract: float, ppixth: LPLPPix,
                                         ppixd: LPLPPix) -> int:
        return self.pixOtsuAdaptiveThreshold(pixs, sx, sy, smoothx, smoothy,
                                             scorefract, ppixth, ppixd)

    def capi_pix_otsu_thresh_on_background_norm(self, pixs: LPPix,
                                                pixim: LPPix, sx: int, sy: int,
                                                thresh: int, mincount: int,
                                                bgval: int, smoothx: int,
                                                smoothy: int,
                                                scorefract: float,
                                                pthresh: c_int_p) -> LPPix:
        return self.pixOtsuThreshOnBackgroundNorm(pixs, pixim, sx, sy, thresh,
                                                  mincount, bgval, smoothx,
                                                  smoothy, scorefract,
                                                  pthresh)

    def capi_pix_masked_thresh_on_background_norm(self, pixs: LPPix,
                                                  pixim: LPPix, sx: int,
                                                  sy: int, thresh: int,
                                                  mincount: int, smoothx: int,
                                                  smoothy: int,
                                                  scorefract: float,
                                                  pthresh: c_int_p) -> LPPix:
        return self.pixMaskedThreshOnBackgroundNorm(pixs, pixim, sx, sy,
                                                    thresh, mincount, smoothx,
                                                    smoothy, scorefract,
                                                    pthresh)

    def capi_pix_sauvola_binarize_tiled(self, pixs: LPPix, whsize: int,
                                        factor: float, nx: int, ny: int,
                                        ppixth: LPLPPix,
                                        ppixd: LPLPPix) -> int:
        return self.pixSauvolaBinarizeTiled(pixs, whsize, factor, nx, ny,
                                            ppixth, ppixd)

    def capi_pix_sauvola_binarize(self, pixs: LPPix, whsize: int,
                                  factor: float, addborder: int,
                                  ppixm: LPLPPix, ppixsd: LPLPPix,
                                  ppixth: LPLPPix, ppixd: LPLPPix) -> int:
        return self.pixSauvolaBinarize(pixs, whsize, factor, addborder, ppixm,
                                       ppixsd, ppixth, ppixd)

    def capi_pix_sauvola_on_contrast_norm(self, pixs: LPPix, mindiff: int,
                                          ppixn: LPLPPix,
                                          ppixth: LPLPPix) -> LPPix:
        return self.pixSauvolaOnContrastNorm(pixs, mindiff, ppixn, ppixth)

    def capi_pix_thresh_on_double_norm(self, pixs: LPPix,
                                       mindiff: int) -> LPPix:
        return self.pixThreshOnDoubleNorm(pixs, mindiff)

    def capi_pix_threshold_by_conn_comp(self, pixs: LPPix, pixm: LPPix,
                                        start: int, end: int, incr: int,
                                        thresh48: float, threshdiff: float,
                                        pglobthresh: c_int_p, ppixd: LPLPPix,
                                        debugflag: int) -> int:
        return self.pixThresholdByConnComp(pixs, pixm, start, end, incr,
                                           thresh48, threshdiff, pglobthresh,
                                           ppixd, debugflag)

    def capi_pix_threshold_by_histo(self, pixs: LPPix, factor: int, halfw: int,
                                    delta: float, pthresh: c_int_p,
                                    ppixd: LPLPPix,
                                    ppixhisto: LPLPPix) -> int:
        return self.pixThresholdByHisto(pixs, factor, halfw, delta, pthresh,
                                        ppixd, ppixhisto)

    def capi_pix_expand_binary_replicate(self, pixs: LPPix, xfact: int,
                                         yfact: int) -> LPPix:
        return self.pixExpandBinaryReplicate(pixs, xfact, yfact)

    def capi_pix_expand_binary_power2(self, pixs: LPPix, factor: int) -> LPPix:
        return self.pixExpandBinaryPower2(pixs, factor)

    def capi_pix_reduce_binary2(self, pixs: LPPix, intab: c_ubyte_p) -> LPPix:
        return self.pixReduceBinary2(pixs, intab)

    def capi_pix_reduce_rank_binary_cascade(self, pixs: LPPix, level1: int,
                                            level2: int, level3: int,
                                            level4: int) -> LPPix:
        return self.pixReduceRankBinaryCascade(pixs, level1, level2, level3,
                                               level4)

    def capi_pix_reduce_rank_binary2(self, pixs: LPPix, level: int,
                                     intab: c_ubyte_p) -> LPPix:
        return self.pixReduceRankBinary2(pixs, level, intab)

    def capi_make_subsample_tab2x(self) -> c_ubyte_p:
        return self.makeSubsampleTab2x()

    def capi_pix_blend(self, pixs1: LPPix, pixs2: LPPix, x: int, y: int,
                       fract: float) -> LPPix:
        return self.pixBlend(pixs1, pixs2, x, y, fract)

    def capi_pix_blend_mask(self, pixd: LPPix, pixs1: LPPix, pixs2: LPPix,
                            x: int, y: int, fract: float, type: int) -> LPPix:
        return self.pixBlendMask(pixd, pixs1, pixs2, x, y, fract, type)

    def capi_pix_blend_gray(self, pixd: LPPix, pixs1: LPPix, pixs2: LPPix,
                            x: int, y: int, fract: float, type: int,
                            transparent: int, transpix: int) -> LPPix:
        return self.pixBlendGray(pixd, pixs1, pixs2, x, y, fract, type,
                                 transparent, transpix)

    def capi_pix_blend_gray_inverse(self, pixd: LPPix, pixs1: LPPix,
                                    pixs2: LPPix, x: int, y: int,
                                    fract: float) -> LPPix:
        return self.pixBlendGrayInverse(pixd, pixs1, pixs2, x, y, fract)

    def capi_pix_blend_color(self, pixd: LPPix, pixs1: LPPix, pixs2: LPPix,
                             x: int, y: int, fract: float, transparent: int,
                             transpix: int) -> LPPix:
        return self.pixBlendColor(pixd, pixs1, pixs2, x, y, fract, transparent,
                                  transpix)

    def capi_pix_blend_color_by_channel(self, pixd: LPPix, pixs1: LPPix,
                                        pixs2: LPPix, x: int, y: int,
                                        rfract: float, gfract: float,
                                        bfract: float, transparent: int,
                                        transpix: int) -> LPPix:
        return self.pixBlendColorByChannel(pixd, pixs1, pixs2, x, y, rfract,
                                           gfract, bfract, transparent,
                                           transpix)

    def capi_pix_blend_gray_adapt(self, pixd: LPPix, pixs1: LPPix,
                                  pixs2: LPPix, x: int, y: int, fract: float,
                                  shift: int) -> LPPix:
        return self.pixBlendGrayAdapt(pixd, pixs1, pixs2, x, y, fract, shift)

    def capi_pix_fade_with_gray(self, pixs: LPPix, pixb: LPPix, factor: float,
                                type: int) -> LPPix:
        return self.pixFadeWithGray(pixs, pixb, factor, type)

    def capi_pix_blend_hard_light(self, pixd: LPPix, pixs1: LPPix,
                                  pixs2: LPPix, x: int, y: int,
                                  fract: float) -> LPPix:
        return self.pixBlendHardLight(pixd, pixs1, pixs2, x, y, fract)

    def capi_pix_blend_cmap(self, pixs: LPPix, pixb: LPPix, x: int, y: int,
                            sindex: int) -> int:
        return self.pixBlendCmap(pixs, pixb, x, y, sindex)

    def capi_pix_blend_with_gray_mask(self, pixs1: LPPix, pixs2: LPPix,
                                      pixg: LPPix, x: int, y: int) -> LPPix:
        return self.pixBlendWithGrayMask(pixs1, pixs2, pixg, x, y)

    def capi_pix_blend_background_to_color(self, pixd: LPPix, pixs: LPPix,
                                           box: LPBox, color: int,
                                           gamma: float, minval: int,
                                           maxval: int) -> LPPix:
        return self.pixBlendBackgroundToColor(pixd, pixs, box, color, gamma,
                                              minval, maxval)

    def capi_pix_multiply_by_color(self, pixd: LPPix, pixs: LPPix, box: LPBox,
                                   color: int) -> LPPix:
        return self.pixMultiplyByColor(pixd, pixs, box, color)

    def capi_pix_alpha_blend_uniform(self, pixs: LPPix, color: int) -> LPPix:
        return self.pixAlphaBlendUniform(pixs, color)

    def capi_pix_add_alpha_to_blend(self, pixs: LPPix, fract: float,
                                    invert: int) -> LPPix:
        return self.pixAddAlphaToBlend(pixs, fract, invert)

    def capi_pix_set_alpha_over_white(self, pixs: LPPix) -> LPPix:
        return self.pixSetAlphaOverWhite(pixs)

    def capi_pix_linear_edge_fade(self, pixs: LPPix, dir: int, fadeto: int,
                                  distfract: float, maxfade: float) -> int:
        return self.pixLinearEdgeFade(pixs, dir, fadeto, distfract, maxfade)

    def capi_bmf_create(self, dir: bytes, fontsize: int) -> LPL_Bmf:
        return self.bmfCreate(dir, fontsize)

    def capi_bmf_destroy(self, pbmf: LPLPL_Bmf):
        self.bmfDestroy(pbmf)

    def capi_bmf_get_pix(self, bmf: LPL_Bmf, chr: bytes) -> LPPix:
        return self.bmfGetPix(bmf, chr)

    def capi_bmf_get_width(self, bmf: LPL_Bmf, chr: bytes, pw: c_int_p) -> int:
        return self.bmfGetWidth(bmf, chr, pw)

    def capi_bmf_get_baseline(self, bmf: LPL_Bmf, chr: bytes,
                              pbaseline: c_int_p) -> int:
        return self.bmfGetBaseline(bmf, chr, pbaseline)

    def capi_pixa_get_font(self, dir: bytes, fontsize: int, pbl0: c_int_p,
                           pbl1: c_int_p, pbl2: c_int_p) -> LPPixa:
        return self.pixaGetFont(dir, fontsize, pbl0, pbl1, pbl2)

    def capi_pixa_save_font(self, indir: bytes, outdir: bytes,
                            fontsize: int) -> int:
        return self.pixaSaveFont(indir, outdir, fontsize)

    def capi_pix_read_stream_bmp(self, fp: LPFile) -> LPPix:
        return self.pixReadStreamBmp(fp)

    def capi_pix_read_mem_bmp(self, cdata: c_ubyte_p, size: int) -> LPPix:
        return self.pixReadMemBmp(cdata, size)

    def capi_pix_write_stream_bmp(self, fp: LPFile, pix: LPPix) -> int:
        return self.pixWriteStreamBmp(fp, pix)

    def capi_pix_write_mem_bmp(self, pfdata: POINTER(c_ubyte_p),
                               pfsize: c_size_t_p, pixs: LPPix) -> int:
        return self.pixWriteMemBmp(pfdata, pfsize, pixs)

    def capi_l_bootnum_gen1(self) -> LPPixa:
        return self.l_bootnum_gen1()

    def capi_l_bootnum_gen2(self) -> LPPixa:
        return self.l_bootnum_gen2()

    def capi_l_bootnum_gen3(self) -> LPPixa:
        return self.l_bootnum_gen3()

    def capi_l_bootnum_gen4(self, nsamp: int) -> LPPixa:
        return self.l_bootnum_gen4(nsamp)

    def capi_box_create(self, x: int, y: int, w: int, h: int) -> LPBox:
        return self.boxCreate(x, y, w, h)

    def capi_box_create_valid(self, x: int, y: int, w: int, h: int) -> LPBox:
        return self.boxCreateValid(x, y, w, h)

    def capi_box_copy(self, box: LPBox) -> LPBox:
        return self.boxCopy(box)

    def capi_box_clone(self, box: LPBox) -> LPBox:
        return self.boxClone(box)

    def capi_box_destroy(self, pbox: LPLPBox):
        self.boxDestroy(pbox)

    def capi_box_get_geometry(self, box: LPBox, px: c_int_p, py: c_int_p,
                              pw: c_int_p, ph: c_int_p) -> int:
        return self.boxGetGeometry(box, px, py, pw, ph)

    def capi_box_set_geometry(self, box: LPBox, x: int, y: int, w: int,
                              h: int) -> int:
        return self.boxSetGeometry(box, x, y, w, h)

    def capi_box_get_side_locations(self, box: LPBox, pl: c_int_p, pr: c_int_p,
                                    pt: c_int_p, pb: c_int_p) -> int:
        return self.boxGetSideLocations(box, pl, pr, pt, pb)

    def capi_box_set_side_locations(self, box: LPBox, l: int, r: int, t: int,
                                    b: int) -> int:
        return self.boxSetSideLocations(box, l, r, t, b)

    def capi_box_get_refcount(self, box: LPBox) -> int:
        return self.boxGetRefcount(box)

    def capi_box_change_refcount(self, box: LPBox, delta: int) -> int:
        return self.boxChangeRefcount(box, delta)

    def capi_box_is_valid(self, box: LPBox, pvalid: c_int_p) -> int:
        return self.boxIsValid(box, pvalid)

    def capi_boxa_create(self, n: int) -> LPBoxa:
        return self.boxaCreate(n)

    def capi_boxa_copy(self, boxa: LPBoxa, copyflag: int) -> LPBoxa:
        return self.boxaCopy(boxa, copyflag)

    def capi_boxa_destroy(self, pboxa: LPLPBoxa):
        self.boxaDestroy(pboxa)

    def capi_boxa_add_box(self, boxa: LPBoxa, box: LPBox,
                          copyflag: int) -> int:
        return self.boxaAddBox(boxa, box, copyflag)

    def capi_boxa_extend_array(self, boxa: LPBoxa) -> int:
        return self.boxaExtendArray(boxa)

    def capi_boxa_extend_array_to_size(self, boxa: LPBoxa, size: int) -> int:
        return self.boxaExtendArrayToSize(boxa, size)

    def capi_boxa_get_count(self, boxa: LPBoxa) -> int:
        return self.boxaGetCount(boxa)

    def capi_boxa_get_valid_count(self, boxa: LPBoxa) -> int:
        return self.boxaGetValidCount(boxa)

    def capi_boxa_get_box(self, boxa: LPBoxa, index: int,
                          accessflag: int) -> LPBox:
        return self.boxaGetBox(boxa, index, accessflag)

    def capi_boxa_get_valid_box(self, boxa: LPBoxa, index: int,
                                accessflag: int) -> LPBox:
        return self.boxaGetValidBox(boxa, index, accessflag)

    def capi_boxa_find_invalid_boxes(self, boxa: LPBoxa) -> LPNuma:
        return self.boxaFindInvalidBoxes(boxa)

    def capi_boxa_get_box_geometry(self, boxa: LPBoxa, index: int, px: c_int_p,
                                   py: c_int_p, pw: c_int_p,
                                   ph: c_int_p) -> int:
        return self.boxaGetBoxGeometry(boxa, index, px, py, pw, ph)

    def capi_boxa_is_full(self, boxa: LPBoxa, pfull: c_int_p) -> int:
        return self.boxaIsFull(boxa, pfull)

    def capi_boxa_replace_box(self, boxa: LPBoxa, index: int,
                              box: LPBox) -> int:
        return self.boxaReplaceBox(boxa, index, box)

    def capi_boxa_insert_box(self, boxa: LPBoxa, index: int,
                             box: LPBox) -> int:
        return self.boxaInsertBox(boxa, index, box)

    def capi_boxa_remove_box(self, boxa: LPBoxa, index: int) -> int:
        return self.boxaRemoveBox(boxa, index)

    def capi_boxa_remove_box_and_save(self, boxa: LPBoxa, index: int,
                                      pbox: LPLPBox) -> int:
        return self.boxaRemoveBoxAndSave(boxa, index, pbox)

    def capi_boxa_save_valid(self, boxas: LPBoxa, copyflag: int) -> LPBoxa:
        return self.boxaSaveValid(boxas, copyflag)

    def capi_boxa_init_full(self, boxa: LPBoxa, box: LPBox) -> int:
        return self.boxaInitFull(boxa, box)

    def capi_boxa_clear(self, boxa: LPBoxa) -> int:
        return self.boxaClear(boxa)

    def capi_boxaa_create(self, n: int) -> LPBoxaa:
        return self.boxaaCreate(n)

    def capi_boxaa_copy(self, baas: LPBoxaa, copyflag: int) -> LPBoxaa:
        return self.boxaaCopy(baas, copyflag)

    def capi_boxaa_destroy(self, pbaa: LPLPBoxaa):
        self.boxaaDestroy(pbaa)

    def capi_boxaa_add_boxa(self, baa: LPBoxaa, ba: LPBoxa,
                            copyflag: int) -> int:
        return self.boxaaAddBoxa(baa, ba, copyflag)

    def capi_boxaa_extend_array(self, baa: LPBoxaa) -> int:
        return self.boxaaExtendArray(baa)

    def capi_boxaa_extend_array_to_size(self, baa: LPBoxaa, size: int) -> int:
        return self.boxaaExtendArrayToSize(baa, size)

    def capi_boxaa_get_count(self, baa: LPBoxaa) -> int:
        return self.boxaaGetCount(baa)

    def capi_boxaa_get_box_count(self, baa: LPBoxaa) -> int:
        return self.boxaaGetBoxCount(baa)

    def capi_boxaa_get_boxa(self, baa: LPBoxaa, index: int,
                            accessflag: int) -> LPBoxa:
        return self.boxaaGetBoxa(baa, index, accessflag)

    def capi_boxaa_get_box(self, baa: LPBoxaa, iboxa: int, ibox: int,
                           accessflag: int) -> LPBox:
        return self.boxaaGetBox(baa, iboxa, ibox, accessflag)

    def capi_boxaa_init_full(self, baa: LPBoxaa, boxa: LPBoxa) -> int:
        return self.boxaaInitFull(baa, boxa)

    def capi_boxaa_extend_with_init(self, baa: LPBoxaa, maxindex: int,
                                    boxa: LPBoxa) -> int:
        return self.boxaaExtendWithInit(baa, maxindex, boxa)

    def capi_boxaa_replace_boxa(self, baa: LPBoxaa, index: int,
                                boxa: LPBoxa) -> int:
        return self.boxaaReplaceBoxa(baa, index, boxa)

    def capi_boxaa_insert_boxa(self, baa: LPBoxaa, index: int,
                               boxa: LPBoxa) -> int:
        return self.boxaaInsertBoxa(baa, index, boxa)

    def capi_boxaa_remove_boxa(self, baa: LPBoxaa, index: int) -> int:
        return self.boxaaRemoveBoxa(baa, index)

    def capi_boxaa_add_box(self, baa: LPBoxaa, index: int, box: LPBox,
                           accessflag: int) -> int:
        return self.boxaaAddBox(baa, index, box, accessflag)

    def capi_boxaa_read_from_files(self, dirname: bytes, substr: bytes,
                                   first: int, nfiles: int) -> LPBoxaa:
        return self.boxaaReadFromFiles(dirname, substr, first, nfiles)

    def capi_boxaa_read(self, filename: bytes) -> LPBoxaa:
        return self.boxaaRead(filename)

    def capi_boxaa_read_stream(self, fp: LPFile) -> LPBoxaa:
        return self.boxaaReadStream(fp)

    def capi_boxaa_read_mem(self, data: c_ubyte_p, size: int) -> LPBoxaa:
        return self.boxaaReadMem(data, size)

    def capi_boxaa_write(self, filename: bytes, baa: LPBoxaa) -> int:
        return self.boxaaWrite(filename, baa)

    def capi_boxaa_write_stream(self, fp: LPFile, baa: LPBoxaa) -> int:
        return self.boxaaWriteStream(fp, baa)

    def capi_boxaa_write_mem(self, pdata: POINTER(c_ubyte_p),
                             psize: c_size_t_p, baa: LPBoxaa) -> int:
        return self.boxaaWriteMem(pdata, psize, baa)

    def capi_boxa_read(self, filename: bytes) -> LPBoxa:
        return self.boxaRead(filename)

    def capi_boxa_read_stream(self, fp: LPFile) -> LPBoxa:
        return self.boxaReadStream(fp)

    def capi_boxa_read_mem(self, data: c_ubyte_p, size: int) -> LPBoxa:
        return self.boxaReadMem(data, size)

    def capi_boxa_write_debug(self, filename: bytes, boxa: LPBoxa) -> int:
        return self.boxaWriteDebug(filename, boxa)

    def capi_boxa_write(self, filename: bytes, boxa: LPBoxa) -> int:
        return self.boxaWrite(filename, boxa)

    def capi_boxa_write_stream(self, fp: LPFile, boxa: LPBoxa) -> int:
        return self.boxaWriteStream(fp, boxa)

    def capi_boxa_write_stderr(self, boxa: LPBoxa) -> int:
        return self.boxaWriteStderr(boxa)

    def capi_boxa_write_mem(self, pdata: POINTER(c_ubyte_p), psize: c_size_t_p,
                            boxa: LPBoxa) -> int:
        return self.boxaWriteMem(pdata, psize, boxa)

    def capi_box_print_stream_info(self, fp: LPFile, box: LPBox) -> int:
        return self.boxPrintStreamInfo(fp, box)

    def capi_box_contains(self, box1: LPBox, box2: LPBox,
                          presult: c_int_p) -> int:
        return self.boxContains(box1, box2, presult)

    def capi_box_intersects(self, box1: LPBox, box2: LPBox,
                            presult: c_int_p) -> int:
        return self.boxIntersects(box1, box2, presult)

    def capi_boxa_contained_in_box(self, boxas: LPBoxa, box: LPBox) -> LPBoxa:
        return self.boxaContainedInBox(boxas, box)

    def capi_boxa_contained_in_box_count(self, boxa: LPBoxa, box: LPBox,
                                         pcount: c_int_p) -> int:
        return self.boxaContainedInBoxCount(boxa, box, pcount)

    def capi_boxa_contained_in_boxa(self, boxa1: LPBoxa, boxa2: LPBoxa,
                                    pcontained: c_int_p) -> int:
        return self.boxaContainedInBoxa(boxa1, boxa2, pcontained)

    def capi_boxa_intersects_box(self, boxas: LPBoxa, box: LPBox) -> LPBoxa:
        return self.boxaIntersectsBox(boxas, box)

    def capi_boxa_intersects_box_count(self, boxa: LPBoxa, box: LPBox,
                                       pcount: c_int_p) -> int:
        return self.boxaIntersectsBoxCount(boxa, box, pcount)

    def capi_boxa_clip_to_box(self, boxas: LPBoxa, box: LPBox) -> LPBoxa:
        return self.boxaClipToBox(boxas, box)

    def capi_boxa_combine_overlaps(self, boxas: LPBoxa,
                                   pixadb: LPPixa) -> LPBoxa:
        return self.boxaCombineOverlaps(boxas, pixadb)

    def capi_boxa_combine_overlaps_in_pair(self, boxas1: LPBoxa,
                                           boxas2: LPBoxa, pboxad1: LPLPBoxa,
                                           pboxad2: LPLPBoxa,
                                           pixadb: LPPixa) -> int:
        return self.boxaCombineOverlapsInPair(boxas1, boxas2, pboxad1, pboxad2,
                                              pixadb)

    def capi_box_overlap_region(self, box1: LPBox, box2: LPBox) -> LPBox:
        return self.boxOverlapRegion(box1, box2)

    def capi_box_bounding_region(self, box1: LPBox, box2: LPBox) -> LPBox:
        return self.boxBoundingRegion(box1, box2)

    def capi_box_overlap_fraction(self, box1: LPBox, box2: LPBox,
                                  pfract: c_float_p) -> int:
        return self.boxOverlapFraction(box1, box2, pfract)

    def capi_box_overlap_area(self, box1: LPBox, box2: LPBox,
                              parea: c_int_p) -> int:
        return self.boxOverlapArea(box1, box2, parea)

    def capi_boxa_handle_overlaps(self, boxas: LPBoxa, op: int, range: int,
                                  min_overlap: float, max_ratio: float,
                                  pnamap: LPLPNuma) -> LPBoxa:
        return self.boxaHandleOverlaps(boxas, op, range, min_overlap,
                                       max_ratio, pnamap)

    def capi_box_overlap_distance(self, box1: LPBox, box2: LPBox,
                                  ph_ovl: c_int_p, pv_ovl: c_int_p) -> int:
        return self.boxOverlapDistance(box1, box2, ph_ovl, pv_ovl)

    def capi_box_separation_distance(self, box1: LPBox, box2: LPBox,
                                     ph_sep: c_int_p, pv_sep: c_int_p) -> int:
        return self.boxSeparationDistance(box1, box2, ph_sep, pv_sep)

    def capi_box_compare_size(self, box1: LPBox, box2: LPBox, type: int,
                              prel: c_int_p) -> int:
        return self.boxCompareSize(box1, box2, type, prel)

    def capi_box_contains_pt(self, box: LPBox, x: float, y: float,
                             pcontains: c_int_p) -> int:
        return self.boxContainsPt(box, x, y, pcontains)

    def capi_boxa_get_nearest_to_pt(self, boxa: LPBoxa, x: int,
                                    y: int) -> LPBox:
        return self.boxaGetNearestToPt(boxa, x, y)

    def capi_boxa_get_nearest_to_line(self, boxa: LPBoxa, x: int,
                                      y: int) -> LPBox:
        return self.boxaGetNearestToLine(boxa, x, y)

    def capi_boxa_find_nearest_boxes(self, boxa: LPBoxa, dist_select: int,
                                     range: int, pnaaindex: LPLPNumaa,
                                     pnaadist: LPLPNumaa) -> int:
        return self.boxaFindNearestBoxes(boxa, dist_select, range, pnaaindex,
                                         pnaadist)

    def capi_boxa_get_nearest_by_direction(self, boxa: LPBoxa, i: int,
                                           dir: int, dist_select: int,
                                           range: int, pindex: c_int_p,
                                           pdist: c_int_p) -> int:
        return self.boxaGetNearestByDirection(boxa, i, dir, dist_select, range,
                                              pindex, pdist)

    def capi_box_get_center(self, box: LPBox, pcx: c_float_p,
                            pcy: c_float_p) -> int:
        return self.boxGetCenter(box, pcx, pcy)

    def capi_box_intersect_by_line(self, box: LPBox, x: int, y: int,
                                   slope: float, px1: c_int_p, py1: c_int_p,
                                   px2: c_int_p, py2: c_int_p,
                                   pn: c_int_p) -> int:
        return self.boxIntersectByLine(box, x, y, slope, px1, py1, px2, py2,
                                       pn)

    def capi_box_clip_to_rectangle(self, box: LPBox, wi: int,
                                   hi: int) -> LPBox:
        return self.boxClipToRectangle(box, wi, hi)

    def capi_box_clip_to_rectangle_params(self, box: LPBox, w: int, h: int,
                                          pxstart: c_int_p, pystart: c_int_p,
                                          pxend: c_int_p, pyend: c_int_p,
                                          pbw: c_int_p, pbh: c_int_p) -> int:
        return self.boxClipToRectangleParams(box, w, h, pxstart, pystart,
                                             pxend, pyend, pbw, pbh)

    def capi_box_relocate_one_side(self, boxd: LPBox, boxs: LPBox, loc: int,
                                   sideflag: int) -> LPBox:
        return self.boxRelocateOneSide(boxd, boxs, loc, sideflag)

    def capi_boxa_adjust_sides(self, boxas: LPBoxa, delleft: int,
                               delright: int, deltop: int,
                               delbot: int) -> LPBoxa:
        return self.boxaAdjustSides(boxas, delleft, delright, deltop, delbot)

    def capi_boxa_adjust_box_sides(self, boxa: LPBoxa, index: int,
                                   delleft: int, delright: int, deltop: int,
                                   delbot: int) -> int:
        return self.boxaAdjustBoxSides(boxa, index, delleft, delright, deltop,
                                       delbot)

    def capi_box_adjust_sides(self, boxd: LPBox, boxs: LPBox, delleft: int,
                              delright: int, deltop: int,
                              delbot: int) -> LPBox:
        return self.boxAdjustSides(boxd, boxs, delleft, delright, deltop,
                                   delbot)

    def capi_boxa_set_side(self, boxad: LPBoxa, boxas: LPBoxa, side: int,
                           val: int, thresh: int) -> LPBoxa:
        return self.boxaSetSide(boxad, boxas, side, val, thresh)

    def capi_box_set_side(self, boxs: LPBox, side: int, val: int,
                          thresh: int) -> int:
        return self.boxSetSide(boxs, side, val, thresh)

    def capi_boxa_adjust_width_to_target(self, boxad: LPBoxa, boxas: LPBoxa,
                                         sides: int, target: int,
                                         thresh: int) -> LPBoxa:
        return self.boxaAdjustWidthToTarget(boxad, boxas, sides, target,
                                            thresh)

    def capi_boxa_adjust_height_to_target(self, boxad: LPBoxa, boxas: LPBoxa,
                                          sides: int, target: int,
                                          thresh: int) -> LPBoxa:
        return self.boxaAdjustHeightToTarget(boxad, boxas, sides, target,
                                             thresh)

    def capi_box_equal(self, box1: LPBox, box2: LPBox, psame: c_int_p) -> int:
        return self.boxEqual(box1, box2, psame)

    def capi_boxa_equal(self, boxa1: LPBoxa, boxa2: LPBoxa, maxdist: int,
                        pnaindex: LPLPNuma, psame: c_int_p) -> int:
        return self.boxaEqual(boxa1, boxa2, maxdist, pnaindex, psame)

    def capi_box_similar(self, box1: LPBox, box2: LPBox, leftdiff: int,
                         rightdiff: int, topdiff: int, botdiff: int,
                         psimilar: c_int_p) -> int:
        return self.boxSimilar(box1, box2, leftdiff, rightdiff, topdiff,
                               botdiff, psimilar)

    def capi_boxa_similar(self, boxa1: LPBoxa, boxa2: LPBoxa, leftdiff: int,
                          rightdiff: int, topdiff: int, botdiff: int,
                          debug: int, psimilar: c_int_p,
                          pnasim: LPLPNuma) -> int:
        return self.boxaSimilar(boxa1, boxa2, leftdiff, rightdiff, topdiff,
                                botdiff, debug, psimilar, pnasim)

    def capi_boxa_join(self, boxad: LPBoxa, boxas: LPBoxa, istart: int,
                       iend: int) -> int:
        return self.boxaJoin(boxad, boxas, istart, iend)

    def capi_boxaa_join(self, baad: LPBoxaa, baas: LPBoxaa, istart: int,
                        iend: int) -> int:
        return self.boxaaJoin(baad, baas, istart, iend)

    def capi_boxa_split_even_odd(self, boxa: LPBoxa, fillflag: int,
                                 pboxae: LPLPBoxa, pboxao: LPLPBoxa) -> int:
        return self.boxaSplitEvenOdd(boxa, fillflag, pboxae, pboxao)

    def capi_boxa_merge_even_odd(self, boxae: LPBoxa, boxao: LPBoxa,
                                 fillflag: int) -> LPBoxa:
        return self.boxaMergeEvenOdd(boxae, boxao, fillflag)

    def capi_boxa_transform(self, boxas: LPBoxa, shiftx: int, shifty: int,
                            scalex: float, scaley: float) -> LPBoxa:
        return self.boxaTransform(boxas, shiftx, shifty, scalex, scaley)

    def capi_box_transform(self, box: LPBox, shiftx: int, shifty: int,
                           scalex: float, scaley: float) -> LPBox:
        return self.boxTransform(box, shiftx, shifty, scalex, scaley)

    def capi_boxa_transform_ordered(self, boxas: LPBoxa, shiftx: int,
                                    shifty: int, scalex: float, scaley: float,
                                    xcen: int, ycen: int, angle: float,
                                    order: int) -> LPBoxa:
        return self.boxaTransformOrdered(boxas, shiftx, shifty, scalex, scaley,
                                         xcen, ycen, angle, order)

    def capi_box_transform_ordered(self, boxs: LPBox, shiftx: int, shifty: int,
                                   scalex: float, scaley: float, xcen: int,
                                   ycen: int, angle: float,
                                   order: int) -> LPBox:
        return self.boxTransformOrdered(boxs, shiftx, shifty, scalex, scaley,
                                        xcen, ycen, angle, order)

    def capi_boxa_rotate_orth(self, boxas: LPBoxa, w: int, h: int,
                              rotation: int) -> LPBoxa:
        return self.boxaRotateOrth(boxas, w, h, rotation)

    def capi_box_rotate_orth(self, box: LPBox, w: int, h: int,
                             rotation: int) -> LPBox:
        return self.boxRotateOrth(box, w, h, rotation)

    def capi_boxa_shift_with_pta(self, boxas: LPBoxa, pta: LPPta,
                                 dir: int) -> LPBoxa:
        return self.boxaShiftWithPta(boxas, pta, dir)

    def capi_boxa_sort(self, boxas: LPBoxa, sorttype: int, sortorder: int,
                       pnaindex: LPLPNuma) -> LPBoxa:
        return self.boxaSort(boxas, sorttype, sortorder, pnaindex)

    def capi_boxa_bin_sort(self, boxas: LPBoxa, sorttype: int, sortorder: int,
                           pnaindex: LPLPNuma) -> LPBoxa:
        return self.boxaBinSort(boxas, sorttype, sortorder, pnaindex)

    def capi_boxa_sort_by_index(self, boxas: LPBoxa,
                                naindex: LPNuma) -> LPBoxa:
        return self.boxaSortByIndex(boxas, naindex)

    def capi_boxa_sort2d(self, boxas: LPBoxa, pnaad: LPLPNumaa, delta1: int,
                         delta2: int, minh1: int) -> LPBoxaa:
        return self.boxaSort2d(boxas, pnaad, delta1, delta2, minh1)

    def capi_boxa_sort2d_by_index(self, boxas: LPBoxa,
                                  naa: LPNumaa) -> LPBoxaa:
        return self.boxaSort2dByIndex(boxas, naa)

    def capi_boxa_extract_as_numa(self, boxa: LPBoxa, pnal: LPLPNuma,
                                  pnat: LPLPNuma, pnar: LPLPNuma,
                                  pnab: LPLPNuma, pnaw: LPLPNuma,
                                  pnah: LPLPNuma, keepinvalid: int) -> int:
        return self.boxaExtractAsNuma(boxa, pnal, pnat, pnar, pnab, pnaw, pnah,
                                      keepinvalid)

    def capi_boxa_extract_as_pta(self, boxa: LPBoxa, pptal: LPLPPta,
                                 pptat: LPLPPta, pptar: LPLPPta,
                                 pptab: LPLPPta, pptaw: LPLPPta,
                                 pptah: LPLPPta, keepinvalid: int) -> int:
        return self.boxaExtractAsPta(boxa, pptal, pptat, pptar, pptab, pptaw,
                                     pptah, keepinvalid)

    def capi_boxa_extract_corners(self, boxa: LPBoxa, loc: int) -> LPPta:
        return self.boxaExtractCorners(boxa, loc)

    def capi_boxa_get_rank_vals(self, boxa: LPBoxa, fract: float, px: c_int_p,
                                py: c_int_p, pr: c_int_p, pb: c_int_p,
                                pw: c_int_p, ph: c_int_p) -> int:
        return self.boxaGetRankVals(boxa, fract, px, py, pr, pb, pw, ph)

    def capi_boxa_get_median_vals(self, boxa: LPBoxa, px: c_int_p, py: c_int_p,
                                  pr: c_int_p, pb: c_int_p, pw: c_int_p,
                                  ph: c_int_p) -> int:
        return self.boxaGetMedianVals(boxa, px, py, pr, pb, pw, ph)

    def capi_boxa_get_average_size(self, boxa: LPBoxa, pw: c_float_p,
                                   ph: c_float_p) -> int:
        return self.boxaGetAverageSize(boxa, pw, ph)

    def capi_boxaa_get_extent(self, baa: LPBoxaa, pw: c_int_p, ph: c_int_p,
                              pbox: LPLPBox, pboxa: LPLPBoxa) -> int:
        return self.boxaaGetExtent(baa, pw, ph, pbox, pboxa)

    def capi_boxaa_flatten_to_boxa(self, baa: LPBoxaa, pnaindex: LPLPNuma,
                                   copyflag: int) -> LPBoxa:
        return self.boxaaFlattenToBoxa(baa, pnaindex, copyflag)

    def capi_boxaa_flatten_aligned(self, baa: LPBoxaa, num: int,
                                   fillerbox: LPBox, copyflag: int) -> LPBoxa:
        return self.boxaaFlattenAligned(baa, num, fillerbox, copyflag)

    def capi_boxa_encapsulate_aligned(self, boxa: LPBoxa, num: int,
                                      copyflag: int) -> LPBoxaa:
        return self.boxaEncapsulateAligned(boxa, num, copyflag)

    def capi_boxaa_transpose(self, baas: LPBoxaa) -> LPBoxaa:
        return self.boxaaTranspose(baas)

    def capi_boxaa_align_box(self, baa: LPBoxaa, box: LPBox, delta: int,
                             pindex: c_int_p) -> int:
        return self.boxaaAlignBox(baa, box, delta, pindex)

    def capi_pix_mask_conn_comp(self, pixs: LPPix, connectivity: int,
                                pboxa: LPLPBoxa) -> LPPix:
        return self.pixMaskConnComp(pixs, connectivity, pboxa)

    def capi_pix_mask_boxa(self, pixd: LPPix, pixs: LPPix, boxa: LPBoxa,
                           op: int) -> LPPix:
        return self.pixMaskBoxa(pixd, pixs, boxa, op)

    def capi_pix_paint_boxa(self, pixs: LPPix, boxa: LPBoxa,
                            val: int) -> LPPix:
        return self.pixPaintBoxa(pixs, boxa, val)

    def capi_pix_set_black_or_white_boxa(self, pixs: LPPix, boxa: LPBoxa,
                                         op: int) -> LPPix:
        return self.pixSetBlackOrWhiteBoxa(pixs, boxa, op)

    def capi_pix_paint_boxa_random(self, pixs: LPPix, boxa: LPBoxa) -> LPPix:
        return self.pixPaintBoxaRandom(pixs, boxa)

    def capi_pix_blend_boxa_random(self, pixs: LPPix, boxa: LPBoxa,
                                   fract: float) -> LPPix:
        return self.pixBlendBoxaRandom(pixs, boxa, fract)

    def capi_pix_draw_boxa(self, pixs: LPPix, boxa: LPBoxa, width: int,
                           val: int) -> LPPix:
        return self.pixDrawBoxa(pixs, boxa, width, val)

    def capi_pix_draw_boxa_random(self, pixs: LPPix, boxa: LPBoxa,
                                  width: int) -> LPPix:
        return self.pixDrawBoxaRandom(pixs, boxa, width)

    def capi_boxaa_display(self, pixs: LPPix, baa: LPBoxaa, linewba: int,
                           linewb: int, colorba: int, colorb: int, w: int,
                           h: int) -> LPPix:
        return self.boxaaDisplay(pixs, baa, linewba, linewb, colorba, colorb,
                                 w, h)

    def capi_pixa_display_boxaa(self, pixas: LPPixa, baa: LPBoxaa,
                                colorflag: int, width: int) -> LPPixa:
        return self.pixaDisplayBoxaa(pixas, baa, colorflag, width)

    def capi_pix_split_into_boxa(self, pixs: LPPix, minsum: int, skipdist: int,
                                 delta: int, maxbg: int, maxcomps: int,
                                 remainder: int) -> LPBoxa:
        return self.pixSplitIntoBoxa(pixs, minsum, skipdist, delta, maxbg,
                                     maxcomps, remainder)

    def capi_pix_split_component_into_boxa(self, pix: LPPix, box: LPBox,
                                           minsum: int, skipdist: int,
                                           delta: int, maxbg: int,
                                           maxcomps: int,
                                           remainder: int) -> LPBoxa:
        return self.pixSplitComponentIntoBoxa(pix, box, minsum, skipdist,
                                              delta, maxbg, maxcomps,
                                              remainder)

    def capi_make_mosaic_strips(self, w: int, h: int, direction: int,
                                size: int) -> LPBoxa:
        return self.makeMosaicStrips(w, h, direction, size)

    def capi_boxa_compare_regions(self, boxa1: LPBoxa, boxa2: LPBoxa,
                                  areathresh: int, pnsame: c_int_p,
                                  pdiffarea: c_float_p, pdiffxor: c_float_p,
                                  ppixdb: LPLPPix) -> int:
        return self.boxaCompareRegions(boxa1, boxa2, areathresh, pnsame,
                                       pdiffarea, pdiffxor, ppixdb)

    def capi_pix_select_large_ul_comp(self, pixs: LPPix, areaslop: float,
                                      yslop: int, connectivity: int) -> LPBox:
        return self.pixSelectLargeULComp(pixs, areaslop, yslop, connectivity)

    def capi_boxa_select_large_ul_box(self, boxas: LPBoxa, areaslop: float,
                                      yslop: int) -> LPBox:
        return self.boxaSelectLargeULBox(boxas, areaslop, yslop)

    def capi_boxa_select_range(self, boxas: LPBoxa, first: int, last: int,
                               copyflag: int) -> LPBoxa:
        return self.boxaSelectRange(boxas, first, last, copyflag)

    def capi_boxaa_select_range(self, baas: LPBoxaa, first: int, last: int,
                                copyflag: int) -> LPBoxaa:
        return self.boxaaSelectRange(baas, first, last, copyflag)

    def capi_boxa_select_by_size(self, boxas: LPBoxa, width: int, height: int,
                                 type: int, relation: int,
                                 pchanged: c_int_p) -> LPBoxa:
        return self.boxaSelectBySize(boxas, width, height, type, relation,
                                     pchanged)

    def capi_boxa_make_size_indicator(self, boxa: LPBoxa, width: int,
                                      height: int, type: int,
                                      relation: int) -> LPNuma:
        return self.boxaMakeSizeIndicator(boxa, width, height, type, relation)

    def capi_boxa_select_by_area(self, boxas: LPBoxa, area: int, relation: int,
                                 pchanged: c_int_p) -> LPBoxa:
        return self.boxaSelectByArea(boxas, area, relation, pchanged)

    def capi_boxa_make_area_indicator(self, boxa: LPBoxa, area: int,
                                      relation: int) -> LPNuma:
        return self.boxaMakeAreaIndicator(boxa, area, relation)

    def capi_boxa_select_by_wh_ratio(self, boxas: LPBoxa, ratio: float,
                                     relation: int,
                                     pchanged: c_int_p) -> LPBoxa:
        return self.boxaSelectByWHRatio(boxas, ratio, relation, pchanged)

    def capi_boxa_make_wh_ratio_indicator(self, boxa: LPBoxa, ratio: float,
                                          relation: int) -> LPNuma:
        return self.boxaMakeWHRatioIndicator(boxa, ratio, relation)

    def capi_boxa_select_with_indicator(self, boxas: LPBoxa, na: LPNuma,
                                        pchanged: c_int_p) -> LPBoxa:
        return self.boxaSelectWithIndicator(boxas, na, pchanged)

    def capi_boxa_permute_pseudorandom(self, boxas: LPBoxa) -> LPBoxa:
        return self.boxaPermutePseudorandom(boxas)

    def capi_boxa_permute_random(self, boxad: LPBoxa, boxas: LPBoxa) -> LPBoxa:
        return self.boxaPermuteRandom(boxad, boxas)

    def capi_boxa_swap_boxes(self, boxa: LPBoxa, i: int, j: int) -> int:
        return self.boxaSwapBoxes(boxa, i, j)

    def capi_boxa_convert_to_pta(self, boxa: LPBoxa, ncorners: int) -> LPPta:
        return self.boxaConvertToPta(boxa, ncorners)

    def capi_pta_convert_to_boxa(self, pta: LPPta, ncorners: int) -> LPBoxa:
        return self.ptaConvertToBoxa(pta, ncorners)

    def capi_box_convert_to_pta(self, box: LPBox, ncorners: int) -> LPPta:
        return self.boxConvertToPta(box, ncorners)

    def capi_pta_convert_to_box(self, pta: LPPta) -> LPBox:
        return self.ptaConvertToBox(pta)

    def capi_boxa_get_extent(self, boxa: LPBoxa, pw: c_int_p, ph: c_int_p,
                             pbox: LPLPBox) -> int:
        return self.boxaGetExtent(boxa, pw, ph, pbox)

    def capi_boxa_get_coverage(self, boxa: LPBoxa, wc: int, hc: int,
                               exactflag: int, pfract: c_float_p) -> int:
        return self.boxaGetCoverage(boxa, wc, hc, exactflag, pfract)

    def capi_boxaa_size_range(self, baa: LPBoxaa, pminw: c_int_p,
                              pminh: c_int_p, pmaxw: c_int_p,
                              pmaxh: c_int_p) -> int:
        return self.boxaaSizeRange(baa, pminw, pminh, pmaxw, pmaxh)

    def capi_boxa_size_range(self, boxa: LPBoxa, pminw: c_int_p,
                             pminh: c_int_p, pmaxw: c_int_p,
                             pmaxh: c_int_p) -> int:
        return self.boxaSizeRange(boxa, pminw, pminh, pmaxw, pmaxh)

    def capi_boxa_location_range(self, boxa: LPBoxa, pminx: c_int_p,
                                 pminy: c_int_p, pmaxx: c_int_p,
                                 pmaxy: c_int_p) -> int:
        return self.boxaLocationRange(boxa, pminx, pminy, pmaxx, pmaxy)

    def capi_boxa_get_sizes(self, boxa: LPBoxa, pnaw: LPLPNuma,
                            pnah: LPLPNuma) -> int:
        return self.boxaGetSizes(boxa, pnaw, pnah)

    def capi_boxa_get_area(self, boxa: LPBoxa, parea: c_int_p) -> int:
        return self.boxaGetArea(boxa, parea)

    def capi_boxa_display_tiled(self, boxas: LPBoxa, pixa: LPPixa, first: int,
                                last: int, maxwidth: int, linewidth: int,
                                scalefactor: float, background: int,
                                spacing: int, border: int) -> LPPix:
        return self.boxaDisplayTiled(boxas, pixa, first, last, maxwidth,
                                     linewidth, scalefactor, background,
                                     spacing, border)

    def capi_boxa_smooth_sequence_median(self, boxas: LPBoxa, halfwin: int,
                                         subflag: int, maxdiff: int,
                                         extrapixels: int,
                                         debug: int) -> LPBoxa:
        return self.boxaSmoothSequenceMedian(boxas, halfwin, subflag, maxdiff,
                                             extrapixels, debug)

    def capi_boxa_windowed_median(self, boxas: LPBoxa, halfwin: int,
                                  debug: int) -> LPBoxa:
        return self.boxaWindowedMedian(boxas, halfwin, debug)

    def capi_boxa_modify_with_boxa(self, boxas: LPBoxa, boxam: LPBoxa,
                                   subflag: int, maxdiff: int,
                                   extrapixels: int) -> LPBoxa:
        return self.boxaModifyWithBoxa(boxas, boxam, subflag, maxdiff,
                                       extrapixels)

    def capi_boxa_reconcile_pair_width(self, boxas: LPBoxa, delw: int, op: int,
                                       factor: float, na: LPNuma) -> LPBoxa:
        return self.boxaReconcilePairWidth(boxas, delw, op, factor, na)

    def capi_boxa_size_consistency(self, boxas: LPBoxa, type: int,
                                   threshp: float, threshm: float,
                                   pfvarp: c_float_p, pfvarm: c_float_p,
                                   psame: c_int_p) -> int:
        return self.boxaSizeConsistency(boxas, type, threshp, threshm, pfvarp,
                                        pfvarm, psame)

    def capi_boxa_reconcile_all_by_median(self, boxas: LPBoxa, select1: int,
                                          select2: int, thresh: int,
                                          extra: int,
                                          pixadb: LPPixa) -> LPBoxa:
        return self.boxaReconcileAllByMedian(boxas, select1, select2, thresh,
                                             extra, pixadb)

    def capi_boxa_reconcile_sides_by_median(self, boxas: LPBoxa, select: int,
                                            thresh: int, extra: int,
                                            pixadb: LPPixa) -> LPBoxa:
        return self.boxaReconcileSidesByMedian(boxas, select, thresh, extra,
                                               pixadb)

    def capi_boxa_reconcile_size_by_median(self, boxas: LPBoxa, type: int,
                                           dfract: float, sfract: float,
                                           factor: float, pnadelw: LPLPNuma,
                                           pnadelh: LPLPNuma,
                                           pratiowh: c_float_p) -> LPBoxa:
        return self.boxaReconcileSizeByMedian(boxas, type, dfract, sfract,
                                              factor, pnadelw, pnadelh,
                                              pratiowh)

    def capi_boxa_plot_sides(self, boxa: LPBoxa, plotname: bytes,
                             pnal: LPLPNuma, pnat: LPLPNuma, pnar: LPLPNuma,
                             pnab: LPLPNuma, ppixd: LPLPPix) -> int:
        return self.boxaPlotSides(boxa, plotname, pnal, pnat, pnar, pnab,
                                  ppixd)

    def capi_boxa_plot_sizes(self, boxa: LPBoxa, plotname: bytes,
                             pnaw: LPLPNuma, pnah: LPLPNuma,
                             ppixd: LPLPPix) -> int:
        return self.boxaPlotSizes(boxa, plotname, pnaw, pnah, ppixd)

    def capi_boxa_fill_sequence(self, boxas: LPBoxa, useflag: int,
                                debug: int) -> LPBoxa:
        return self.boxaFillSequence(boxas, useflag, debug)

    def capi_boxa_size_variation(self, boxa: LPBoxa, type: int,
                                 pdel_evenodd: c_float_p, prms_even: c_float_p,
                                 prms_odd: c_float_p,
                                 prms_all: c_float_p) -> int:
        return self.boxaSizeVariation(boxa, type, pdel_evenodd, prms_even,
                                      prms_odd, prms_all)

    def capi_boxa_median_dimensions(self, boxas: LPBoxa, pmedw: c_int_p,
                                    pmedh: c_int_p, pmedwe: c_int_p,
                                    pmedwo: c_int_p, pmedhe: c_int_p,
                                    pmedho: c_int_p, pnadelw: LPLPNuma,
                                    pnadelh: LPLPNuma) -> int:
        return self.boxaMedianDimensions(boxas, pmedw, pmedh, pmedwe, pmedwo,
                                         pmedhe, pmedho, pnadelw, pnadelh)

    def capi_l_byteaCreate(self, nbytes: int) -> LPL_Bytea:
        return self.l_byteaCreate(nbytes)

    def capi_l_byteaInitFromMem(self, data: c_ubyte_p, size: int) -> LPL_Bytea:
        return self.l_byteaInitFromMem(data, size)

    def capi_l_byteaInitFromFile(self, fname: bytes) -> LPL_Bytea:
        return self.l_byteaInitFromFile(fname)

    def capi_l_byteaInitFromStream(self, fp: LPFile) -> LPL_Bytea:
        return self.l_byteaInitFromStream(fp)

    def capi_l_byteaCopy(self, bas: LPL_Bytea, copyflag: int) -> LPL_Bytea:
        return self.l_byteaCopy(bas, copyflag)

    def capi_l_byteaDestroy(self, pba: LPLPL_Bytea):
        self.l_byteaDestroy(pba)

    def capi_l_byteaGetSize(self, ba: LPL_Bytea) -> int:
        return self.l_byteaGetSize(ba)

    def capi_l_byteaGetData(self, ba: LPL_Bytea,
                            psize: c_size_t_p) -> c_ubyte_p:
        return self.l_byteaGetData(ba, psize)

    def capi_l_byteaCopyData(self, ba: LPL_Bytea,
                             psize: c_size_t_p) -> c_ubyte_p:
        return self.l_byteaCopyData(ba, psize)

    def capi_l_byteaAppendData(self, ba: LPL_Bytea, newdata: c_ubyte_p,
                               newbytes: int) -> int:
        return self.l_byteaAppendData(ba, newdata, newbytes)

    def capi_l_byteaAppendString(self, ba: LPL_Bytea, str: bytes) -> int:
        return self.l_byteaAppendString(ba, str)

    def capi_l_byteaJoin(self, ba1: LPL_Bytea, pba2: LPLPL_Bytea) -> int:
        return self.l_byteaJoin(ba1, pba2)

    def capi_l_byteaSplit(self, ba1: LPL_Bytea, splitloc: int,
                          pba2: LPLPL_Bytea) -> int:
        return self.l_byteaSplit(ba1, splitloc, pba2)

    def capi_l_byteaFindEachSequence(self, ba: LPL_Bytea, sequence: c_ubyte_p,
                                     seqlen: int, pda: LPLPL_Dna) -> int:
        return self.l_byteaFindEachSequence(ba, sequence, seqlen, pda)

    def capi_l_byteaWrite(self, fname: bytes, ba: LPL_Bytea, startloc: int,
                          nbytes: int) -> int:
        return self.l_byteaWrite(fname, ba, startloc, nbytes)

    def capi_l_byteaWriteStream(self, fp: LPFile, ba: LPL_Bytea, startloc: int,
                                nbytes: int) -> int:
        return self.l_byteaWriteStream(fp, ba, startloc, nbytes)

    def capi_ccba_create(self, pixs: LPPix, n: int) -> LPCCBorda:
        return self.ccbaCreate(pixs, n)

    def capi_ccba_destroy(self, pccba: LPLPCCBorda):
        self.ccbaDestroy(pccba)

    def capi_ccb_create(self, pixs: LPPix) -> LPCCBord:
        return self.ccbCreate(pixs)

    def capi_ccb_destroy(self, pccb: LPLPCCBord):
        self.ccbDestroy(pccb)

    def capi_ccba_add_ccb(self, ccba: LPCCBorda, ccb: LPCCBord) -> int:
        return self.ccbaAddCcb(ccba, ccb)

    def capi_ccba_get_count(self, ccba: LPCCBorda) -> int:
        return self.ccbaGetCount(ccba)

    def capi_ccba_get_ccb(self, ccba: LPCCBorda, index: int) -> LPCCBord:
        return self.ccbaGetCcb(ccba, index)

    def capi_pix_get_all_cc_borders(self, pixs: LPPix) -> LPCCBorda:
        return self.pixGetAllCCBorders(pixs)

    def capi_pix_get_outer_borders_ptaa(self, pixs: LPPix) -> LPPtaa:
        return self.pixGetOuterBordersPtaa(pixs)

    def capi_pix_get_outer_border(self, ccb: LPCCBord, pixs: LPPix,
                                  box: LPBox) -> int:
        return self.pixGetOuterBorder(ccb, pixs, box)

    def capi_ccba_generate_global_locs(self, ccba: LPCCBorda) -> int:
        return self.ccbaGenerateGlobalLocs(ccba)

    def capi_ccba_generate_step_chains(self, ccba: LPCCBorda) -> int:
        return self.ccbaGenerateStepChains(ccba)

    def capi_ccba_step_chains_to_pix_coords(self, ccba: LPCCBorda,
                                            coordtype: int) -> int:
        return self.ccbaStepChainsToPixCoords(ccba, coordtype)

    def capi_ccba_generate_sp_global_locs(self, ccba: LPCCBorda,
                                          ptsflag: int) -> int:
        return self.ccbaGenerateSPGlobalLocs(ccba, ptsflag)

    def capi_ccba_generate_single_path(self, ccba: LPCCBorda) -> int:
        return self.ccbaGenerateSinglePath(ccba)

    def capi_get_cut_path_for_hole(self, pix: LPPix, pta: LPPta,
                                   boxinner: LPBox, pdir: c_int_p,
                                   plen: c_int_p) -> LPPta:
        return self.getCutPathForHole(pix, pta, boxinner, pdir, plen)

    def capi_ccba_display_border(self, ccba: LPCCBorda) -> LPPix:
        return self.ccbaDisplayBorder(ccba)

    def capi_ccba_display_sp_border(self, ccba: LPCCBorda) -> LPPix:
        return self.ccbaDisplaySPBorder(ccba)

    def capi_ccba_display_image1(self, ccba: LPCCBorda) -> LPPix:
        return self.ccbaDisplayImage1(ccba)

    def capi_ccba_display_image2(self, ccba: LPCCBorda) -> LPPix:
        return self.ccbaDisplayImage2(ccba)

    def capi_ccba_write(self, filename: bytes, ccba: LPCCBorda) -> int:
        return self.ccbaWrite(filename, ccba)

    def capi_ccba_write_stream(self, fp: LPFile, ccba: LPCCBorda) -> int:
        return self.ccbaWriteStream(fp, ccba)

    def capi_ccba_read(self, filename: bytes) -> LPCCBorda:
        return self.ccbaRead(filename)

    def capi_ccba_read_stream(self, fp: LPFile) -> LPCCBorda:
        return self.ccbaReadStream(fp)

    def capi_ccba_write_svg(self, filename: bytes, ccba: LPCCBorda) -> int:
        return self.ccbaWriteSVG(filename, ccba)

    def capi_ccba_write_svg_string(self, ccba: LPCCBorda) -> LP_c_char:
        return self.ccbaWriteSVGString(ccba)

    def capi_pixa_thin_connected(self, pixas: LPPixa, type: int,
                                 connectivity: int, maxiters: int) -> LPPixa:
        return self.pixaThinConnected(pixas, type, connectivity, maxiters)

    def capi_pix_thin_connected(self, pixs: LPPix, type: int,
                                connectivity: int, maxiters: int) -> LPPix:
        return self.pixThinConnected(pixs, type, connectivity, maxiters)

    def capi_pix_thin_connected_by_set(self, pixs: LPPix, type: int,
                                       sela: LPSela, maxiters: int) -> LPPix:
        return self.pixThinConnectedBySet(pixs, type, sela, maxiters)

    def capi_sela_make_thin_sets(self, index: int, debug: int) -> LPSela:
        return self.selaMakeThinSets(index, debug)

    def capi_pix_find_checkerboard_corners(self, pixs: LPPix, size: int,
                                           dilation: int, nsels: int,
                                           ppix_corners: LPLPPix,
                                           ppta_corners: LPLPPta,
                                           pixadb: LPPixa) -> int:
        return self.pixFindCheckerboardCorners(pixs, size, dilation, nsels,
                                               ppix_corners, ppta_corners,
                                               pixadb)

    def capi_jb_correlation(self, dirin: bytes, thresh: float, weight: float,
                            components: int, rootname: bytes, firstpage: int,
                            npages: int, renderflag: int) -> int:
        return self.jbCorrelation(dirin, thresh, weight, components, rootname,
                                  firstpage, npages, renderflag)

    def capi_jb_rank_haus(self, dirin: bytes, size: int, rank: float,
                          components: int, rootname: bytes, firstpage: int,
                          npages: int, renderflag: int) -> int:
        return self.jbRankHaus(dirin, size, rank, components, rootname,
                               firstpage, npages, renderflag)

    def capi_jb_words_in_textlines(self, dirin: bytes, reduction: int,
                                   maxwidth: int, maxheight: int,
                                   thresh: float, weight: float,
                                   pnatl: LPLPNuma, firstpage: int,
                                   npages: int) -> LPJbClasser:
        return self.jbWordsInTextlines(dirin, reduction, maxwidth, maxheight,
                                       thresh, weight, pnatl, firstpage,
                                       npages)

    def capi_pix_get_words_in_textlines(self, pixs: LPPix, minwidth: int,
                                        minheight: int, maxwidth: int,
                                        maxheight: int, pboxad: LPLPBoxa,
                                        ppixad: LPLPPixa,
                                        pnai: LPLPNuma) -> int:
        return self.pixGetWordsInTextlines(pixs, minwidth, minheight, maxwidth,
                                           maxheight, pboxad, ppixad, pnai)

    def capi_pix_get_word_boxes_in_textlines(self, pixs: LPPix, minwidth: int,
                                             minheight: int, maxwidth: int,
                                             maxheight: int, pboxad: LPLPBoxa,
                                             pnai: LPLPNuma) -> int:
        return self.pixGetWordBoxesInTextlines(pixs, minwidth, minheight,
                                               maxwidth, maxheight, pboxad,
                                               pnai)

    def capi_pix_find_word_and_character_boxes(self, pixs: LPPix, boxs: LPBox,
                                               thresh: int, pboxaw: LPLPBoxa,
                                               pboxaac: LPLPBoxaa,
                                               debugdir: bytes) -> int:
        return self.pixFindWordAndCharacterBoxes(pixs, boxs, thresh, pboxaw,
                                                 pboxaac, debugdir)

    def capi_boxa_extract_sorted_pattern(self, boxa: LPBoxa,
                                         na: LPNuma) -> LPNumaa:
        return self.boxaExtractSortedPattern(boxa, na)

    def capi_numaa_compare_images_by_boxes(self, naa1: LPNumaa, naa2: LPNumaa,
                                           nperline: int, nreq: int,
                                           maxshiftx: int, maxshifty: int,
                                           delx: int, dely: int,
                                           psame: c_int_p,
                                           debugflag: int) -> int:
        return self.numaaCompareImagesByBoxes(naa1, naa2, nperline, nreq,
                                              maxshiftx, maxshifty, delx, dely,
                                              psame, debugflag)

    def capi_pix_color_content(self, pixs: LPPix, rref: int, gref: int,
                               bref: int, mingray: int, ppixr: LPLPPix,
                               ppixg: LPLPPix, ppixb: LPLPPix) -> int:
        return self.pixColorContent(pixs, rref, gref, bref, mingray, ppixr,
                                    ppixg, ppixb)

    def capi_pix_color_magnitude(self, pixs: LPPix, rref: int, gref: int,
                                 bref: int, type: int) -> LPPix:
        return self.pixColorMagnitude(pixs, rref, gref, bref, type)

    def capi_pix_color_fraction(self, pixs: LPPix, darkthresh: int,
                                lightthresh: int, diffthresh: int, factor: int,
                                ppixfract: c_float_p,
                                pcolorfract: c_float_p) -> int:
        return self.pixColorFraction(pixs, darkthresh, lightthresh, diffthresh,
                                     factor, ppixfract, pcolorfract)

    def capi_pix_color_shift_white_point(self, pixs: LPPix, rref: int,
                                         gref: int, bref: int) -> LPPix:
        return self.pixColorShiftWhitePoint(pixs, rref, gref, bref)

    def capi_pix_mask_over_color_pixels(self, pixs: LPPix, threshdiff: int,
                                        mindist: int) -> LPPix:
        return self.pixMaskOverColorPixels(pixs, threshdiff, mindist)

    def capi_pix_mask_over_gray_pixels(self, pixs: LPPix, maxlimit: int,
                                       satlimit: int) -> LPPix:
        return self.pixMaskOverGrayPixels(pixs, maxlimit, satlimit)

    def capi_pix_mask_over_color_range(self, pixs: LPPix, rmin: int, rmax: int,
                                       gmin: int, gmax: int, bmin: int,
                                       bmax: int) -> LPPix:
        return self.pixMaskOverColorRange(pixs, rmin, rmax, gmin, gmax, bmin,
                                          bmax)

    def capi_pix_find_color_regions(self, pixs: LPPix, pixm: LPPix,
                                    factor: int, lightthresh: int,
                                    darkthresh: int, mindiff: int,
                                    colordiff: int, edgefract: float,
                                    pcolorfract: c_float_p,
                                    pcolormask1: LPLPPix, pcolormask2: LPLPPix,
                                    pixadb: LPPixa) -> int:
        return self.pixFindColorRegions(pixs, pixm, factor, lightthresh,
                                        darkthresh, mindiff, colordiff,
                                        edgefract, pcolorfract, pcolormask1,
                                        pcolormask2, pixadb)

    def capi_pix_num_significant_gray_colors(self, pixs: LPPix,
                                             darkthresh: int, lightthresh: int,
                                             minfract: float, factor: int,
                                             pncolors: c_int_p) -> int:
        return self.pixNumSignificantGrayColors(pixs, darkthresh, lightthresh,
                                                minfract, factor, pncolors)

    def capi_pix_colors_for_quantization(self, pixs: LPPix, thresh: int,
                                         pncolors: c_int_p, piscolor: c_int_p,
                                         debug: int) -> int:
        return self.pixColorsForQuantization(pixs, thresh, pncolors, piscolor,
                                             debug)

    def capi_pix_num_colors(self, pixs: LPPix, factor: int,
                            pncolors: c_int_p) -> int:
        return self.pixNumColors(pixs, factor, pncolors)

    def capi_pix_convert_rgb_to_cmap_lossless(self, pixs: LPPix) -> LPPix:
        return self.pixConvertRGBToCmapLossless(pixs)

    def capi_pix_get_most_populated_colors(self, pixs: LPPix, sigbits: int,
                                           factor: int, ncolors: int,
                                           parray: POINTER(c_uint_p),
                                           pcmap: LPLPPixColormap) -> int:
        return self.pixGetMostPopulatedColors(pixs, sigbits, factor, ncolors,
                                              parray, pcmap)

    def capi_pix_simple_color_quantize(self, pixs: LPPix, sigbits: int,
                                       factor: int, ncolors: int) -> LPPix:
        return self.pixSimpleColorQuantize(pixs, sigbits, factor, ncolors)

    def capi_pix_get_rgb_histogram(self, pixs: LPPix, sigbits: int,
                                   factor: int) -> LPNuma:
        return self.pixGetRGBHistogram(pixs, sigbits, factor)

    def capi_make_rgb_index_tables(self, prtab: POINTER(c_uint_p),
                                   pgtab: POINTER(c_uint_p),
                                   pbtab: POINTER(c_uint_p),
                                   sigbits: int) -> int:
        return self.makeRGBIndexTables(prtab, pgtab, pbtab, sigbits)

    def capi_get_rgb_from_index(self, index: int, sigbits: int, prval: c_int_p,
                                pgval: c_int_p, pbval: c_int_p) -> int:
        return self.getRGBFromIndex(index, sigbits, prval, pgval, pbval)

    def capi_pix_has_highlight_red(self, pixs: LPPix, factor: int,
                                   minfract: float, fthresh: float,
                                   phasred: c_int_p, pratio: c_float_p,
                                   ppixdb: LPLPPix) -> int:
        return self.pixHasHighlightRed(pixs, factor, minfract, fthresh,
                                       phasred, pratio, ppixdb)

    def capi_l_colorfillCreate(self, pixs: LPPix, nx: int,
                               ny: int) -> LPL_Colorfill:
        return self.l_colorfillCreate(pixs, nx, ny)

    def capi_l_colorfillDestroy(self, pcf: LPLPL_Colorfill):
        self.l_colorfillDestroy(pcf)

    def capi_pix_color_content_by_location(self, cf: LPL_Colorfill, rref: int,
                                           gref: int, bref: int, minmax: int,
                                           maxdiff: int, minarea: int,
                                           smooth: int, debug: int) -> int:
        return self.pixColorContentByLocation(cf, rref, gref, bref, minmax,
                                              maxdiff, minarea, smooth, debug)

    def capi_pix_color_fill(self, pixs: LPPix, minmax: int, maxdiff: int,
                            smooth: int, minarea: int, debug: int) -> LPPix:
        return self.pixColorFill(pixs, minmax, maxdiff, smooth, minarea, debug)

    def capi_make_colorfill_test_data(self, w: int, h: int, nseeds: int,
                                      range: int) -> LPPixa:
        return self.makeColorfillTestData(w, h, nseeds, range)

    def capi_pix_color_gray_regions(self, pixs: LPPix, boxa: LPBoxa, type: int,
                                    thresh: int, rval: int, gval: int,
                                    bval: int) -> LPPix:
        return self.pixColorGrayRegions(pixs, boxa, type, thresh, rval, gval,
                                        bval)

    def capi_pix_color_gray(self, pixs: LPPix, box: LPBox, type: int,
                            thresh: int, rval: int, gval: int,
                            bval: int) -> int:
        return self.pixColorGray(pixs, box, type, thresh, rval, gval, bval)

    def capi_pix_color_gray_masked(self, pixs: LPPix, pixm: LPPix, type: int,
                                   thresh: int, rval: int, gval: int,
                                   bval: int) -> LPPix:
        return self.pixColorGrayMasked(pixs, pixm, type, thresh, rval, gval,
                                       bval)

    def capi_pix_snap_color(self, pixd: LPPix, pixs: LPPix, srcval: int,
                            dstval: int, diff: int) -> LPPix:
        return self.pixSnapColor(pixd, pixs, srcval, dstval, diff)

    def capi_pix_snap_color_cmap(self, pixd: LPPix, pixs: LPPix, srcval: int,
                                 dstval: int, diff: int) -> LPPix:
        return self.pixSnapColorCmap(pixd, pixs, srcval, dstval, diff)

    def capi_pix_linear_map_to_target_color(self, pixd: LPPix, pixs: LPPix,
                                            srcval: int,
                                            dstval: int) -> LPPix:
        return self.pixLinearMapToTargetColor(pixd, pixs, srcval, dstval)

    def capi_pixel_linear_map_to_target_color(self, scolor: int, srcmap: int,
                                              dstmap: int,
                                              pdcolor: c_uint_p) -> int:
        return self.pixelLinearMapToTargetColor(scolor, srcmap, dstmap,
                                                pdcolor)

    def capi_pix_shift_by_component(self, pixd: LPPix, pixs: LPPix,
                                    srcval: int, dstval: int) -> LPPix:
        return self.pixShiftByComponent(pixd, pixs, srcval, dstval)

    def capi_pixel_shift_by_component(self, rval: int, gval: int, bval: int,
                                      srcval: int, dstval: int,
                                      ppixel: c_uint_p) -> int:
        return self.pixelShiftByComponent(rval, gval, bval, srcval, dstval,
                                          ppixel)

    def capi_pixel_fractional_shift(self, rval: int, gval: int, bval: int,
                                    fract: float, ppixel: c_uint_p) -> int:
        return self.pixelFractionalShift(rval, gval, bval, fract, ppixel)

    def capi_pix_map_with_invariant_hue(self, pixd: LPPix, pixs: LPPix,
                                        srcval: int, fract: float) -> LPPix:
        return self.pixMapWithInvariantHue(pixd, pixs, srcval, fract)

    def capi_pixcmap_create(self, depth: int) -> LPPixColormap:
        return self.pixcmapCreate(depth)

    def capi_pixcmap_create_random(self, depth: int, hasblack: int,
                                   haswhite: int) -> LPPixColormap:
        return self.pixcmapCreateRandom(depth, hasblack, haswhite)

    def capi_pixcmap_create_linear(self, d: int,
                                   nlevels: int) -> LPPixColormap:
        return self.pixcmapCreateLinear(d, nlevels)

    def capi_pixcmap_copy(self, cmaps: LPPixColormap) -> LPPixColormap:
        return self.pixcmapCopy(cmaps)

    def capi_pixcmap_destroy(self, pcmap: LPLPPixColormap):
        self.pixcmapDestroy(pcmap)

    def capi_pixcmap_is_valid(self, cmap: LPPixColormap, pix: LPPix,
                              pvalid: c_int_p) -> int:
        return self.pixcmapIsValid(cmap, pix, pvalid)

    def capi_pixcmap_add_color(self, cmap: LPPixColormap, rval: int, gval: int,
                               bval: int) -> int:
        return self.pixcmapAddColor(cmap, rval, gval, bval)

    def capi_pixcmap_add_rgba(self, cmap: LPPixColormap, rval: int, gval: int,
                              bval: int, aval: int) -> int:
        return self.pixcmapAddRGBA(cmap, rval, gval, bval, aval)

    def capi_pixcmap_add_new_color(self, cmap: LPPixColormap, rval: int,
                                   gval: int, bval: int,
                                   pindex: c_int_p) -> int:
        return self.pixcmapAddNewColor(cmap, rval, gval, bval, pindex)

    def capi_pixcmap_add_nearest_color(self, cmap: LPPixColormap, rval: int,
                                       gval: int, bval: int,
                                       pindex: c_int_p) -> int:
        return self.pixcmapAddNearestColor(cmap, rval, gval, bval, pindex)

    def capi_pixcmap_usable_color(self, cmap: LPPixColormap, rval: int,
                                  gval: int, bval: int,
                                  pusable: c_int_p) -> int:
        return self.pixcmapUsableColor(cmap, rval, gval, bval, pusable)

    def capi_pixcmap_add_black_or_white(self, cmap: LPPixColormap, color: int,
                                        pindex: c_int_p) -> int:
        return self.pixcmapAddBlackOrWhite(cmap, color, pindex)

    def capi_pixcmap_set_black_and_white(self, cmap: LPPixColormap,
                                         setblack: int, setwhite: int) -> int:
        return self.pixcmapSetBlackAndWhite(cmap, setblack, setwhite)

    def capi_pixcmap_get_count(self, cmap: LPPixColormap) -> int:
        return self.pixcmapGetCount(cmap)

    def capi_pixcmap_get_free_count(self, cmap: LPPixColormap) -> int:
        return self.pixcmapGetFreeCount(cmap)

    def capi_pixcmap_get_depth(self, cmap: LPPixColormap) -> int:
        return self.pixcmapGetDepth(cmap)

    def capi_pixcmap_get_min_depth(self, cmap: LPPixColormap,
                                   pmindepth: c_int_p) -> int:
        return self.pixcmapGetMinDepth(cmap, pmindepth)

    def capi_pixcmap_clear(self, cmap: LPPixColormap) -> int:
        return self.pixcmapClear(cmap)

    def capi_pixcmap_get_color(self, cmap: LPPixColormap, index: int,
                               prval: c_int_p, pgval: c_int_p,
                               pbval: c_int_p) -> int:
        return self.pixcmapGetColor(cmap, index, prval, pgval, pbval)

    def capi_pixcmap_get_color32(self, cmap: LPPixColormap, index: int,
                                 pval32: c_uint_p) -> int:
        return self.pixcmapGetColor32(cmap, index, pval32)

    def capi_pixcmap_get_rgba(self, cmap: LPPixColormap, index: int,
                              prval: c_int_p, pgval: c_int_p, pbval: c_int_p,
                              paval: c_int_p) -> int:
        return self.pixcmapGetRGBA(cmap, index, prval, pgval, pbval, paval)

    def capi_pixcmap_get_rgba32(self, cmap: LPPixColormap, index: int,
                                pval32: c_uint_p) -> int:
        return self.pixcmapGetRGBA32(cmap, index, pval32)

    def capi_pixcmap_reset_color(self, cmap: LPPixColormap, index: int,
                                 rval: int, gval: int, bval: int) -> int:
        return self.pixcmapResetColor(cmap, index, rval, gval, bval)

    def capi_pixcmap_set_alpha(self, cmap: LPPixColormap, index: int,
                               aval: int) -> int:
        return self.pixcmapSetAlpha(cmap, index, aval)

    def capi_pixcmap_get_index(self, cmap: LPPixColormap, rval: int, gval: int,
                               bval: int, pindex: c_int_p) -> int:
        return self.pixcmapGetIndex(cmap, rval, gval, bval, pindex)

    def capi_pixcmap_has_color(self, cmap: LPPixColormap,
                               pcolor: c_int_p) -> int:
        return self.pixcmapHasColor(cmap, pcolor)

    def capi_pixcmap_is_opaque(self, cmap: LPPixColormap,
                               popaque: c_int_p) -> int:
        return self.pixcmapIsOpaque(cmap, popaque)

    def capi_pixcmap_non_opaque_colors_info(self, cmap: LPPixColormap,
                                            pntrans: c_int_p,
                                            pmax_trans: c_int_p,
                                            pmin_opaque: c_int_p) -> int:
        return self.pixcmapNonOpaqueColorsInfo(cmap, pntrans, pmax_trans,
                                               pmin_opaque)

    def capi_pixcmap_is_black_and_white(self, cmap: LPPixColormap,
                                        pblackwhite: c_int_p) -> int:
        return self.pixcmapIsBlackAndWhite(cmap, pblackwhite)

    def capi_pixcmap_count_gray_colors(self, cmap: LPPixColormap,
                                       pngray: c_int_p) -> int:
        return self.pixcmapCountGrayColors(cmap, pngray)

    def capi_pixcmap_get_rank_intensity(self, cmap: LPPixColormap,
                                        rankval: float,
                                        pindex: c_int_p) -> int:
        return self.pixcmapGetRankIntensity(cmap, rankval, pindex)

    def capi_pixcmap_get_nearest_index(self, cmap: LPPixColormap, rval: int,
                                       gval: int, bval: int,
                                       pindex: c_int_p) -> int:
        return self.pixcmapGetNearestIndex(cmap, rval, gval, bval, pindex)

    def capi_pixcmap_get_nearest_gray_index(self, cmap: LPPixColormap,
                                            val: int, pindex: c_int_p) -> int:
        return self.pixcmapGetNearestGrayIndex(cmap, val, pindex)

    def capi_pixcmap_get_distance_to_color(self, cmap: LPPixColormap,
                                           index: int, rval: int, gval: int,
                                           bval: int, pdist: c_int_p) -> int:
        return self.pixcmapGetDistanceToColor(cmap, index, rval, gval, bval,
                                              pdist)

    def capi_pixcmap_get_range_values(self, cmap: LPPixColormap, select: int,
                                      pminval: c_int_p, pmaxval: c_int_p,
                                      pminindex: c_int_p,
                                      pmaxindex: c_int_p) -> int:
        return self.pixcmapGetRangeValues(cmap, select, pminval, pmaxval,
                                          pminindex, pmaxindex)

    def capi_pixcmap_gray_to_false_color(self, gamma: float) -> LPPixColormap:
        return self.pixcmapGrayToFalseColor(gamma)

    def capi_pixcmap_gray_to_color(self, color: int) -> LPPixColormap:
        return self.pixcmapGrayToColor(color)

    def capi_pixcmap_color_to_gray(self, cmaps: LPPixColormap, rwt: float,
                                   gwt: float, bwt: float) -> LPPixColormap:
        return self.pixcmapColorToGray(cmaps, rwt, gwt, bwt)

    def capi_pixcmap_convert_to4(self, cmaps: LPPixColormap) -> LPPixColormap:
        return self.pixcmapConvertTo4(cmaps)

    def capi_pixcmap_convert_to8(self, cmaps: LPPixColormap) -> LPPixColormap:
        return self.pixcmapConvertTo8(cmaps)

    def capi_pixcmap_read(self, filename: bytes) -> LPPixColormap:
        return self.pixcmapRead(filename)

    def capi_pixcmap_read_stream(self, fp: LPFile) -> LPPixColormap:
        return self.pixcmapReadStream(fp)

    def capi_pixcmap_read_mem(self, data: c_ubyte_p,
                              size: int) -> LPPixColormap:
        return self.pixcmapReadMem(data, size)

    def capi_pixcmap_write(self, filename: bytes, cmap: LPPixColormap) -> int:
        return self.pixcmapWrite(filename, cmap)

    def capi_pixcmap_write_stream(self, fp: LPFile,
                                  cmap: LPPixColormap) -> int:
        return self.pixcmapWriteStream(fp, cmap)

    def capi_pixcmap_write_mem(self, pdata: POINTER(c_ubyte_p),
                               psize: c_size_t_p, cmap: LPPixColormap) -> int:
        return self.pixcmapWriteMem(pdata, psize, cmap)

    def capi_pixcmap_to_arrays(self, cmap: LPPixColormap,
                               prmap: POINTER(c_int_p),
                               pgmap: POINTER(c_int_p),
                               pbmap: POINTER(c_int_p),
                               pamap: POINTER(c_int_p)) -> int:
        return self.pixcmapToArrays(cmap, prmap, pgmap, pbmap, pamap)

    def capi_pixcmap_to_rgb_table(self, cmap: LPPixColormap,
                                  ptab: POINTER(c_uint_p),
                                  pncolors: c_int_p) -> int:
        return self.pixcmapToRGBTable(cmap, ptab, pncolors)

    def capi_pixcmap_serialize_to_memory(self, cmap: LPPixColormap, cpc: int,
                                         pncolors: c_int_p,
                                         pdata: POINTER(c_ubyte_p)) -> int:
        return self.pixcmapSerializeToMemory(cmap, cpc, pncolors, pdata)

    def capi_pixcmap_deserialize_from_memory(self, data: c_ubyte_p, cpc: int,
                                             ncolors: int) -> LPPixColormap:
        return self.pixcmapDeserializeFromMemory(data, cpc, ncolors)

    def capi_pixcmap_convert_to_hex(self, data: c_ubyte_p,
                                    ncolors: int) -> LP_c_char:
        return self.pixcmapConvertToHex(data, ncolors)

    def capi_pixcmap_gamma_trc(self, cmap: LPPixColormap, gamma: float,
                               minval: int, maxval: int) -> int:
        return self.pixcmapGammaTRC(cmap, gamma, minval, maxval)

    def capi_pixcmap_contrast_trc(self, cmap: LPPixColormap,
                                  factor: float) -> int:
        return self.pixcmapContrastTRC(cmap, factor)

    def capi_pixcmap_shift_intensity(self, cmap: LPPixColormap,
                                     fraction: float) -> int:
        return self.pixcmapShiftIntensity(cmap, fraction)

    def capi_pixcmap_shift_by_component(self, cmap: LPPixColormap, srcval: int,
                                        dstval: int) -> int:
        return self.pixcmapShiftByComponent(cmap, srcval, dstval)

    def capi_pix_color_morph(self, pixs: LPPix, type: int, hsize: int,
                             vsize: int) -> LPPix:
        return self.pixColorMorph(pixs, type, hsize, vsize)

    def capi_pix_octree_color_quant(self, pixs: LPPix, colors: int,
                                    ditherflag: int) -> LPPix:
        return self.pixOctreeColorQuant(pixs, colors, ditherflag)

    def capi_pix_octree_color_quant_general(self, pixs: LPPix, colors: int,
                                            ditherflag: int,
                                            validthresh: float,
                                            colorthresh: float) -> LPPix:
        return self.pixOctreeColorQuantGeneral(pixs, colors, ditherflag,
                                               validthresh, colorthresh)

    def capi_make_rgb_to_index_tables(self, cqlevels: int,
                                      prtab: POINTER(c_uint_p),
                                      pgtab: POINTER(c_uint_p),
                                      pbtab: POINTER(c_uint_p)) -> int:
        return self.makeRGBToIndexTables(cqlevels, prtab, pgtab, pbtab)

    def capi_get_octcube_index_from_rgb(self, rval: int, gval: int, bval: int,
                                        rtab: c_uint_p, gtab: c_uint_p,
                                        btab: c_uint_p, pindex: c_uint_p):
        self.getOctcubeIndexFromRGB(rval, gval, bval, rtab, gtab, btab, pindex)

    def capi_pix_octree_quant_by_population(self, pixs: LPPix, level: int,
                                            ditherflag: int) -> LPPix:
        return self.pixOctreeQuantByPopulation(pixs, level, ditherflag)

    def capi_pix_octree_quant_num_colors(self, pixs: LPPix, maxcolors: int,
                                         subsample: int) -> LPPix:
        return self.pixOctreeQuantNumColors(pixs, maxcolors, subsample)

    def capi_pix_octcube_quant_mixed_with_gray(self, pixs: LPPix, depth: int,
                                               graylevels: int,
                                               delta: int) -> LPPix:
        return self.pixOctcubeQuantMixedWithGray(pixs, depth, graylevels,
                                                 delta)

    def capi_pix_fixed_octcube_quant256(self, pixs: LPPix,
                                        ditherflag: int) -> LPPix:
        return self.pixFixedOctcubeQuant256(pixs, ditherflag)

    def capi_pix_few_colors_octcube_quant1(self, pixs: LPPix,
                                           level: int) -> LPPix:
        return self.pixFewColorsOctcubeQuant1(pixs, level)

    def capi_pix_few_colors_octcube_quant2(self, pixs: LPPix, level: int,
                                           na: LPNuma, ncolors: int,
                                           pnerrors: c_int_p) -> LPPix:
        return self.pixFewColorsOctcubeQuant2(pixs, level, na, ncolors,
                                              pnerrors)

    def capi_pix_few_colors_octcube_quant_mixed(self, pixs: LPPix, level: int,
                                                darkthresh: int,
                                                lightthresh: int,
                                                diffthresh: int,
                                                minfract: float,
                                                maxspan: int) -> LPPix:
        return self.pixFewColorsOctcubeQuantMixed(pixs, level, darkthresh,
                                                  lightthresh, diffthresh,
                                                  minfract, maxspan)

    def capi_pix_fixed_octcube_quant_gen_rgb(self, pixs: LPPix,
                                             level: int) -> LPPix:
        return self.pixFixedOctcubeQuantGenRGB(pixs, level)

    def capi_pix_quant_from_cmap(self, pixs: LPPix, cmap: LPPixColormap,
                                 mindepth: int, level: int,
                                 metric: int) -> LPPix:
        return self.pixQuantFromCmap(pixs, cmap, mindepth, level, metric)

    def capi_pix_octcube_quant_from_cmap(self, pixs: LPPix,
                                         cmap: LPPixColormap, mindepth: int,
                                         level: int, metric: int) -> LPPix:
        return self.pixOctcubeQuantFromCmap(pixs, cmap, mindepth, level,
                                            metric)

    def capi_pix_octcube_histogram(self, pixs: LPPix, level: int,
                                   pncolors: c_int_p) -> LPNuma:
        return self.pixOctcubeHistogram(pixs, level, pncolors)

    def capi_pixcmap_to_octcube_lut(self, cmap: LPPixColormap, level: int,
                                    metric: int) -> c_int_p:
        return self.pixcmapToOctcubeLUT(cmap, level, metric)

    def capi_pix_remove_unused_colors(self, pixs: LPPix) -> int:
        return self.pixRemoveUnusedColors(pixs)

    def capi_pix_number_occupied_octcubes(self, pix: LPPix, level: int,
                                          mincount: int, minfract: float,
                                          pncolors: c_int_p) -> int:
        return self.pixNumberOccupiedOctcubes(pix, level, mincount, minfract,
                                              pncolors)

    def capi_pix_median_cut_quant(self, pixs: LPPix, ditherflag: int) -> LPPix:
        return self.pixMedianCutQuant(pixs, ditherflag)

    def capi_pix_median_cut_quant_general(self, pixs: LPPix, ditherflag: int,
                                          outdepth: int, maxcolors: int,
                                          sigbits: int, maxsub: int,
                                          checkbw: int) -> LPPix:
        return self.pixMedianCutQuantGeneral(pixs, ditherflag, outdepth,
                                             maxcolors, sigbits, maxsub,
                                             checkbw)

    def capi_pix_median_cut_quant_mixed(self, pixs: LPPix, ncolor: int,
                                        ngray: int, darkthresh: int,
                                        lightthresh: int,
                                        diffthresh: int) -> LPPix:
        return self.pixMedianCutQuantMixed(pixs, ncolor, ngray, darkthresh,
                                           lightthresh, diffthresh)

    def capi_pix_few_colors_median_cut_quant_mixed(self, pixs: LPPix,
                                                   ncolor: int, ngray: int,
                                                   maxncolors: int,
                                                   darkthresh: int,
                                                   lightthresh: int,
                                                   diffthresh: int) -> LPPix:
        return self.pixFewColorsMedianCutQuantMixed(pixs, ncolor, ngray,
                                                    maxncolors, darkthresh,
                                                    lightthresh, diffthresh)

    def capi_pix_median_cut_histo(self, pixs: LPPix, sigbits: int,
                                  subsample: int) -> c_int_p:
        return self.pixMedianCutHisto(pixs, sigbits, subsample)

    def capi_pix_color_segment(self, pixs: LPPix, maxdist: int, maxcolors: int,
                               selsize: int, finalcolors: int,
                               debugflag: int) -> LPPix:
        return self.pixColorSegment(pixs, maxdist, maxcolors, selsize,
                                    finalcolors, debugflag)

    def capi_pix_color_segment_cluster(self, pixs: LPPix, maxdist: int,
                                       maxcolors: int,
                                       debugflag: int) -> LPPix:
        return self.pixColorSegmentCluster(pixs, maxdist, maxcolors, debugflag)

    def capi_pix_assign_to_nearest_color(self, pixd: LPPix, pixs: LPPix,
                                         pixm: LPPix, level: int,
                                         countarray: c_int_p) -> int:
        return self.pixAssignToNearestColor(pixd, pixs, pixm, level,
                                            countarray)

    def capi_pix_color_segment_clean(self, pixs: LPPix, selsize: int,
                                     countarray: c_int_p) -> int:
        return self.pixColorSegmentClean(pixs, selsize, countarray)

    def capi_pix_color_segment_remove_colors(self, pixd: LPPix, pixs: LPPix,
                                             finalcolors: int) -> int:
        return self.pixColorSegmentRemoveColors(pixd, pixs, finalcolors)

    def capi_pix_convert_rgb_to_hsv(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixConvertRGBToHSV(pixd, pixs)

    def capi_pix_convert_hsv_to_rgb(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixConvertHSVToRGB(pixd, pixs)

    def capi_convert_rgb_to_hsv(self, rval: int, gval: int, bval: int,
                                phval: c_int_p, psval: c_int_p,
                                pvval: c_int_p) -> int:
        return self.convertRGBToHSV(rval, gval, bval, phval, psval, pvval)

    def capi_convert_hsv_to_rgb(self, hval: int, sval: int, vval: int,
                                prval: c_int_p, pgval: c_int_p,
                                pbval: c_int_p) -> int:
        return self.convertHSVToRGB(hval, sval, vval, prval, pgval, pbval)

    def capi_pixcmap_convert_rgb_to_hsv(self, cmap: LPPixColormap) -> int:
        return self.pixcmapConvertRGBToHSV(cmap)

    def capi_pixcmap_convert_hsv_to_rgb(self, cmap: LPPixColormap) -> int:
        return self.pixcmapConvertHSVToRGB(cmap)

    def capi_pix_convert_rgb_to_hue(self, pixs: LPPix) -> LPPix:
        return self.pixConvertRGBToHue(pixs)

    def capi_pix_convert_rgb_to_saturation(self, pixs: LPPix) -> LPPix:
        return self.pixConvertRGBToSaturation(pixs)

    def capi_pix_convert_rgb_to_value(self, pixs: LPPix) -> LPPix:
        return self.pixConvertRGBToValue(pixs)

    def capi_pix_make_range_mask_hs(self, pixs: LPPix, huecenter: int,
                                    huehw: int, satcenter: int, sathw: int,
                                    regionflag: int) -> LPPix:
        return self.pixMakeRangeMaskHS(pixs, huecenter, huehw, satcenter,
                                       sathw, regionflag)

    def capi_pix_make_range_mask_hv(self, pixs: LPPix, huecenter: int,
                                    huehw: int, valcenter: int, valhw: int,
                                    regionflag: int) -> LPPix:
        return self.pixMakeRangeMaskHV(pixs, huecenter, huehw, valcenter,
                                       valhw, regionflag)

    def capi_pix_make_range_mask_sv(self, pixs: LPPix, satcenter: int,
                                    sathw: int, valcenter: int, valhw: int,
                                    regionflag: int) -> LPPix:
        return self.pixMakeRangeMaskSV(pixs, satcenter, sathw, valcenter,
                                       valhw, regionflag)

    def capi_pix_make_histo_hs(self, pixs: LPPix, factor: int,
                               pnahue: LPLPNuma, pnasat: LPLPNuma) -> LPPix:
        return self.pixMakeHistoHS(pixs, factor, pnahue, pnasat)

    def capi_pix_make_histo_hv(self, pixs: LPPix, factor: int,
                               pnahue: LPLPNuma, pnaval: LPLPNuma) -> LPPix:
        return self.pixMakeHistoHV(pixs, factor, pnahue, pnaval)

    def capi_pix_make_histo_sv(self, pixs: LPPix, factor: int,
                               pnasat: LPLPNuma, pnaval: LPLPNuma) -> LPPix:
        return self.pixMakeHistoSV(pixs, factor, pnasat, pnaval)

    def capi_pix_find_histo_peaks_hsv(self, pixs: LPPix, type: int, width: int,
                                      height: int, npeaks: int,
                                      erasefactor: float, ppta: LPLPPta,
                                      pnatot: LPLPNuma,
                                      ppixa: LPLPPixa) -> int:
        return self.pixFindHistoPeaksHSV(pixs, type, width, height, npeaks,
                                         erasefactor, ppta, pnatot, ppixa)

    def capi_display_hsv_color_range(self, hval: int, sval: int, vval: int,
                                     huehw: int, sathw: int, nsamp: int,
                                     factor: int) -> LPPix:
        return self.displayHSVColorRange(hval, sval, vval, huehw, sathw, nsamp,
                                         factor)

    def capi_pix_convert_rgb_to_yuv(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixConvertRGBToYUV(pixd, pixs)

    def capi_pix_convert_yuv_to_rgb(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixConvertYUVToRGB(pixd, pixs)

    def capi_convert_rgb_to_yuv(self, rval: int, gval: int, bval: int,
                                pyval: c_int_p, puval: c_int_p,
                                pvval: c_int_p) -> int:
        return self.convertRGBToYUV(rval, gval, bval, pyval, puval, pvval)

    def capi_convert_yuv_to_rgb(self, yval: int, uval: int, vval: int,
                                prval: c_int_p, pgval: c_int_p,
                                pbval: c_int_p) -> int:
        return self.convertYUVToRGB(yval, uval, vval, prval, pgval, pbval)

    def capi_pixcmap_convert_rgb_to_yuv(self, cmap: LPPixColormap) -> int:
        return self.pixcmapConvertRGBToYUV(cmap)

    def capi_pixcmap_convert_yuv_to_rgb(self, cmap: LPPixColormap) -> int:
        return self.pixcmapConvertYUVToRGB(cmap)

    def capi_pix_convert_rgb_to_xyz(self, pixs: LPPix) -> LPFPixa:
        return self.pixConvertRGBToXYZ(pixs)

    def capi_fpixa_convert_xyz_to_rgb(self, fpixa: LPFPixa) -> LPPix:
        return self.fpixaConvertXYZToRGB(fpixa)

    def capi_convert_rgb_to_xyz(self, rval: int, gval: int, bval: int,
                                pfxval: c_float_p, pfyval: c_float_p,
                                pfzval: c_float_p) -> int:
        return self.convertRGBToXYZ(rval, gval, bval, pfxval, pfyval, pfzval)

    def capi_convert_xyz_to_rgb(self, fxval: float, fyval: float, fzval: float,
                                blackout: int, prval: c_int_p, pgval: c_int_p,
                                pbval: c_int_p) -> int:
        return self.convertXYZToRGB(fxval, fyval, fzval, blackout, prval,
                                    pgval, pbval)

    def capi_fpixa_convert_xyz_to_lab(self, fpixas: LPFPixa) -> LPFPixa:
        return self.fpixaConvertXYZToLAB(fpixas)

    def capi_fpixa_convert_lab_to_xyz(self, fpixas: LPFPixa) -> LPFPixa:
        return self.fpixaConvertLABToXYZ(fpixas)

    def capi_convert_xyz_to_lab(self, xval: float, yval: float, zval: float,
                                plval: c_float_p, paval: c_float_p,
                                pbval: c_float_p) -> int:
        return self.convertXYZToLAB(xval, yval, zval, plval, paval, pbval)

    def capi_convert_lab_to_xyz(self, lval: float, aval: float, bval: float,
                                pxval: c_float_p, pyval: c_float_p,
                                pzval: c_float_p) -> int:
        return self.convertLABToXYZ(lval, aval, bval, pxval, pyval, pzval)

    def capi_pix_convert_rgb_to_lab(self, pixs: LPPix) -> LPFPixa:
        return self.pixConvertRGBToLAB(pixs)

    def capi_fpixa_convert_lab_to_rgb(self, fpixa: LPFPixa) -> LPPix:
        return self.fpixaConvertLABToRGB(fpixa)

    def capi_convert_rgb_to_lab(self, rval: int, gval: int, bval: int,
                                pflval: c_float_p, pfaval: c_float_p,
                                pfbval: c_float_p) -> int:
        return self.convertRGBToLAB(rval, gval, bval, pflval, pfaval, pfbval)

    def capi_convert_lab_to_rgb(self, flval: float, faval: float, fbval: float,
                                prval: c_int_p, pgval: c_int_p,
                                pbval: c_int_p) -> int:
        return self.convertLABToRGB(flval, faval, fbval, prval, pgval, pbval)

    def capi_pix_make_gamut_rgb(self, scale: int) -> LPPix:
        return self.pixMakeGamutRGB(scale)

    def capi_pix_equal(self, pix1: LPPix, pix2: LPPix, psame: c_int_p) -> int:
        return self.pixEqual(pix1, pix2, psame)

    def capi_pix_equal_with_alpha(self, pix1: LPPix, pix2: LPPix,
                                  use_alpha: int, psame: c_int_p) -> int:
        return self.pixEqualWithAlpha(pix1, pix2, use_alpha, psame)

    def capi_pix_equal_with_cmap(self, pix1: LPPix, pix2: LPPix,
                                 psame: c_int_p) -> int:
        return self.pixEqualWithCmap(pix1, pix2, psame)

    def capi_cmap_equal(self, cmap1: LPPixColormap, cmap2: LPPixColormap,
                        ncomps: int, psame: c_int_p) -> int:
        return self.cmapEqual(cmap1, cmap2, ncomps, psame)

    def capi_pix_uses_cmap_color(self, pixs: LPPix, pcolor: c_int_p) -> int:
        return self.pixUsesCmapColor(pixs, pcolor)

    def capi_pix_correlation_binary(self, pix1: LPPix, pix2: LPPix,
                                    pval: c_float_p) -> int:
        return self.pixCorrelationBinary(pix1, pix2, pval)

    def capi_pix_display_diff_binary(self, pix1: LPPix, pix2: LPPix) -> LPPix:
        return self.pixDisplayDiffBinary(pix1, pix2)

    def capi_pix_compare_binary(self, pix1: LPPix, pix2: LPPix, comptype: int,
                                pfract: c_float_p, ppixdiff: LPLPPix) -> int:
        return self.pixCompareBinary(pix1, pix2, comptype, pfract, ppixdiff)

    def capi_pix_compare_gray_or_rgb(self, pix1: LPPix, pix2: LPPix,
                                     comptype: int, plottype: int,
                                     psame: c_int_p, pdiff: c_float_p,
                                     prmsdiff: c_float_p,
                                     ppixdiff: LPLPPix) -> int:
        return self.pixCompareGrayOrRGB(pix1, pix2, comptype, plottype, psame,
                                        pdiff, prmsdiff, ppixdiff)

    def capi_pix_compare_gray(self, pix1: LPPix, pix2: LPPix, comptype: int,
                              plottype: int, psame: c_int_p, pdiff: c_float_p,
                              prmsdiff: c_float_p, ppixdiff: LPLPPix) -> int:
        return self.pixCompareGray(pix1, pix2, comptype, plottype, psame,
                                   pdiff, prmsdiff, ppixdiff)

    def capi_pix_compare_rgb(self, pix1: LPPix, pix2: LPPix, comptype: int,
                             plottype: int, psame: c_int_p, pdiff: c_float_p,
                             prmsdiff: c_float_p, ppixdiff: LPLPPix) -> int:
        return self.pixCompareRGB(pix1, pix2, comptype, plottype, psame, pdiff,
                                  prmsdiff, ppixdiff)

    def capi_pix_compare_tiled(self, pix1: LPPix, pix2: LPPix, sx: int,
                               sy: int, type: int, ppixdiff: LPLPPix) -> int:
        return self.pixCompareTiled(pix1, pix2, sx, sy, type, ppixdiff)

    def capi_pix_compare_rank_difference(self, pix1: LPPix, pix2: LPPix,
                                         factor: int) -> LPNuma:
        return self.pixCompareRankDifference(pix1, pix2, factor)

    def capi_pix_test_for_similarity(self, pix1: LPPix, pix2: LPPix,
                                     factor: int, mindiff: int,
                                     maxfract: float, maxave: float,
                                     psimilar: c_int_p, details: int) -> int:
        return self.pixTestForSimilarity(pix1, pix2, factor, mindiff, maxfract,
                                         maxave, psimilar, details)

    def capi_pix_get_difference_stats(self, pix1: LPPix, pix2: LPPix,
                                      factor: int, mindiff: int,
                                      pfractdiff: c_float_p,
                                      pavediff: c_float_p,
                                      details: int) -> int:
        return self.pixGetDifferenceStats(pix1, pix2, factor, mindiff,
                                          pfractdiff, pavediff, details)

    def capi_pix_get_difference_histogram(self, pix1: LPPix, pix2: LPPix,
                                          factor: int) -> LPNuma:
        return self.pixGetDifferenceHistogram(pix1, pix2, factor)

    def capi_pix_get_perceptual_diff(self, pixs1: LPPix, pixs2: LPPix,
                                     sampling: int, dilation: int,
                                     mindiff: int, pfract: c_float_p,
                                     ppixdiff1: LPLPPix,
                                     ppixdiff2: LPLPPix) -> int:
        return self.pixGetPerceptualDiff(pixs1, pixs2, sampling, dilation,
                                         mindiff, pfract, ppixdiff1,
                                         ppixdiff2)

    def capi_pix_get_psnr(self, pix1: LPPix, pix2: LPPix, factor: int,
                          ppsnr: c_float_p) -> int:
        return self.pixGetPSNR(pix1, pix2, factor, ppsnr)

    def capi_pixa_compare_photo_regions_by_histo(self, pixa: LPPixa,
                                                 minratio: float,
                                                 textthresh: float,
                                                 factor: int, n: int,
                                                 simthresh: float,
                                                 pnai: LPLPNuma,
                                                 pscores: POINTER(c_float_p),
                                                 ppixd: LPLPPix,
                                                 debug: int) -> int:
        return self.pixaComparePhotoRegionsByHisto(pixa, minratio, textthresh,
                                                   factor, n, simthresh, pnai,
                                                   pscores, ppixd, debug)

    def capi_pix_compare_photo_regions_by_histo(self, pix1: LPPix, pix2: LPPix,
                                                box1: LPBox, box2: LPBox,
                                                minratio: float, factor: int,
                                                n: int, pscore: c_float_p,
                                                debugflag: int) -> int:
        return self.pixComparePhotoRegionsByHisto(pix1, pix2, box1, box2,
                                                  minratio, factor, n, pscore,
                                                  debugflag)

    def capi_pix_gen_photo_histos(self, pixs: LPPix, box: LPBox, factor: int,
                                  thresh: float, n: int, pnaa: LPLPNumaa,
                                  pw: c_int_p, ph: c_int_p,
                                  debugindex: int) -> int:
        return self.pixGenPhotoHistos(pixs, box, factor, thresh, n, pnaa, pw,
                                      ph, debugindex)

    def capi_pix_pad_to_center_centroid(self, pixs: LPPix,
                                        factor: int) -> LPPix:
        return self.pixPadToCenterCentroid(pixs, factor)

    def capi_pix_centroid8(self, pixs: LPPix, factor: int, pcx: c_float_p,
                           pcy: c_float_p) -> int:
        return self.pixCentroid8(pixs, factor, pcx, pcy)

    def capi_pix_decide_if_photo_image(self, pix: LPPix, factor: int,
                                       thresh: float, n: int, pnaa: LPLPNumaa,
                                       pixadebug: LPPixa) -> int:
        return self.pixDecideIfPhotoImage(pix, factor, thresh, n, pnaa,
                                          pixadebug)

    def capi_compare_tiles_by_histo(self, naa1: LPNumaa, naa2: LPNumaa,
                                    minratio: float, w1: int, h1: int, w2: int,
                                    h2: int, pscore: c_float_p,
                                    pixadebug: LPPixa) -> int:
        return self.compareTilesByHisto(naa1, naa2, minratio, w1, h1, w2, h2,
                                        pscore, pixadebug)

    def capi_pix_compare_gray_by_histo(self, pix1: LPPix, pix2: LPPix,
                                       box1: LPBox, box2: LPBox,
                                       minratio: float, maxgray: int,
                                       factor: int, n: int, pscore: c_float_p,
                                       debugflag: int) -> int:
        return self.pixCompareGrayByHisto(pix1, pix2, box1, box2, minratio,
                                          maxgray, factor, n, pscore,
                                          debugflag)

    def capi_pix_crop_aligned_to_centroid(self, pix1: LPPix, pix2: LPPix,
                                          factor: int, pbox1: LPLPBox,
                                          pbox2: LPLPBox) -> int:
        return self.pixCropAlignedToCentroid(pix1, pix2, factor, pbox1, pbox2)

    def capi_l_compressGrayHistograms(self, naa: LPNumaa, w: int, h: int,
                                      psize: c_size_t_p) -> c_ubyte_p:
        return self.l_compressGrayHistograms(naa, w, h, psize)

    def capi_l_uncompressGrayHistograms(self, bytea: c_ubyte_p, size: int,
                                        pw: c_int_p, ph: c_int_p) -> LPNumaa:
        return self.l_uncompressGrayHistograms(bytea, size, pw, ph)

    def capi_pix_compare_with_translation(self, pix1: LPPix, pix2: LPPix,
                                          thresh: int, pdelx: c_int_p,
                                          pdely: c_int_p, pscore: c_float_p,
                                          debugflag: int) -> int:
        return self.pixCompareWithTranslation(pix1, pix2, thresh, pdelx, pdely,
                                              pscore, debugflag)

    def capi_pix_best_correlation(self, pix1: LPPix, pix2: LPPix, area1: int,
                                  area2: int, etransx: int, etransy: int,
                                  maxshift: int, tab8: c_int_p, pdelx: c_int_p,
                                  pdely: c_int_p, pscore: c_float_p,
                                  debugflag: int) -> int:
        return self.pixBestCorrelation(pix1, pix2, area1, area2, etransx,
                                       etransy, maxshift, tab8, pdelx, pdely,
                                       pscore, debugflag)

    def capi_pix_conn_comp(self, pixs: LPPix, ppixa: LPLPPixa,
                           connectivity: int) -> LPBoxa:
        return self.pixConnComp(pixs, ppixa, connectivity)

    def capi_pix_conn_comp_pixa(self, pixs: LPPix, ppixa: LPLPPixa,
                                connectivity: int) -> LPBoxa:
        return self.pixConnCompPixa(pixs, ppixa, connectivity)

    def capi_pix_conn_comp_bb(self, pixs: LPPix, connectivity: int) -> LPBoxa:
        return self.pixConnCompBB(pixs, connectivity)

    def capi_pix_count_conn_comp(self, pixs: LPPix, connectivity: int,
                                 pcount: c_int_p) -> int:
        return self.pixCountConnComp(pixs, connectivity, pcount)

    def capi_next_on_pixel_in_raster(self, pixs: LPPix, xstart: int,
                                     ystart: int, px: c_int_p,
                                     py: c_int_p) -> int:
        return self.nextOnPixelInRaster(pixs, xstart, ystart, px, py)

    def capi_pix_seedfill_bb(self, pixs: LPPix, stack: LPL_Stack, x: int,
                             y: int, connectivity: int) -> LPBox:
        return self.pixSeedfillBB(pixs, stack, x, y, connectivity)

    def capi_pix_seedfill4bb(self, pixs: LPPix, stack: LPL_Stack, x: int,
                             y: int) -> LPBox:
        return self.pixSeedfill4BB(pixs, stack, x, y)

    def capi_pix_seedfill8bb(self, pixs: LPPix, stack: LPL_Stack, x: int,
                             y: int) -> LPBox:
        return self.pixSeedfill8BB(pixs, stack, x, y)

    def capi_pix_seedfill(self, pixs: LPPix, stack: LPL_Stack, x: int, y: int,
                          connectivity: int) -> int:
        return self.pixSeedfill(pixs, stack, x, y, connectivity)

    def capi_pix_seedfill4(self, pixs: LPPix, stack: LPL_Stack, x: int,
                           y: int) -> int:
        return self.pixSeedfill4(pixs, stack, x, y)

    def capi_pix_seedfill8(self, pixs: LPPix, stack: LPL_Stack, x: int,
                           y: int) -> int:
        return self.pixSeedfill8(pixs, stack, x, y)

    def capi_convert_files_to1bpp(self, dirin: bytes, substr: bytes,
                                  upscaling: int, thresh: int, firstpage: int,
                                  npages: int, dirout: bytes,
                                  outformat: int) -> int:
        return self.convertFilesTo1bpp(dirin, substr, upscaling, thresh,
                                       firstpage, npages, dirout, outformat)

    def capi_pix_blockconv(self, pix: LPPix, wc: int, hc: int) -> LPPix:
        return self.pixBlockconv(pix, wc, hc)

    def capi_pix_blockconv_gray(self, pixs: LPPix, pixacc: LPPix, wc: int,
                                hc: int) -> LPPix:
        return self.pixBlockconvGray(pixs, pixacc, wc, hc)

    def capi_pix_blockconv_accum(self, pixs: LPPix) -> LPPix:
        return self.pixBlockconvAccum(pixs)

    def capi_pix_blockconv_gray_unnormalized(self, pixs: LPPix, wc: int,
                                             hc: int) -> LPPix:
        return self.pixBlockconvGrayUnnormalized(pixs, wc, hc)

    def capi_pix_blockconv_tiled(self, pix: LPPix, wc: int, hc: int, nx: int,
                                 ny: int) -> LPPix:
        return self.pixBlockconvTiled(pix, wc, hc, nx, ny)

    def capi_pix_blockconv_gray_tile(self, pixs: LPPix, pixacc: LPPix, wc: int,
                                     hc: int) -> LPPix:
        return self.pixBlockconvGrayTile(pixs, pixacc, wc, hc)

    def capi_pix_windowed_stats(self, pixs: LPPix, wc: int, hc: int,
                                hasborder: int, ppixm: LPLPPix,
                                ppixms: LPLPPix, pfpixv: LPLPFPix,
                                pfpixrv: LPLPFPix) -> int:
        return self.pixWindowedStats(pixs, wc, hc, hasborder, ppixm, ppixms,
                                     pfpixv, pfpixrv)

    def capi_pix_windowed_mean(self, pixs: LPPix, wc: int, hc: int,
                               hasborder: int, normflag: int) -> LPPix:
        return self.pixWindowedMean(pixs, wc, hc, hasborder, normflag)

    def capi_pix_windowed_mean_square(self, pixs: LPPix, wc: int, hc: int,
                                      hasborder: int) -> LPPix:
        return self.pixWindowedMeanSquare(pixs, wc, hc, hasborder)

    def capi_pix_windowed_variance(self, pixm: LPPix, pixms: LPPix,
                                   pfpixv: LPLPFPix,
                                   pfpixrv: LPLPFPix) -> int:
        return self.pixWindowedVariance(pixm, pixms, pfpixv, pfpixrv)

    def capi_pix_mean_square_accum(self, pixs: LPPix) -> LPDPix:
        return self.pixMeanSquareAccum(pixs)

    def capi_pix_blockrank(self, pixs: LPPix, pixacc: LPPix, wc: int, hc: int,
                           rank: float) -> LPPix:
        return self.pixBlockrank(pixs, pixacc, wc, hc, rank)

    def capi_pix_blocksum(self, pixs: LPPix, pixacc: LPPix, wc: int,
                          hc: int) -> LPPix:
        return self.pixBlocksum(pixs, pixacc, wc, hc)

    def capi_pix_census_transform(self, pixs: LPPix, halfsize: int,
                                  pixacc: LPPix) -> LPPix:
        return self.pixCensusTransform(pixs, halfsize, pixacc)

    def capi_pix_convolve(self, pixs: LPPix, kel: LPL_Kernel, outdepth: int,
                          normflag: int) -> LPPix:
        return self.pixConvolve(pixs, kel, outdepth, normflag)

    def capi_pix_convolve_sep(self, pixs: LPPix, kelx: LPL_Kernel,
                              kely: LPL_Kernel, outdepth: int,
                              normflag: int) -> LPPix:
        return self.pixConvolveSep(pixs, kelx, kely, outdepth, normflag)

    def capi_pix_convolve_rgb(self, pixs: LPPix, kel: LPL_Kernel) -> LPPix:
        return self.pixConvolveRGB(pixs, kel)

    def capi_pix_convolve_rgb_sep(self, pixs: LPPix, kelx: LPL_Kernel,
                                  kely: LPL_Kernel) -> LPPix:
        return self.pixConvolveRGBSep(pixs, kelx, kely)

    def capi_fpix_convolve(self, fpixs: LPFPix, kel: LPL_Kernel,
                           normflag: int) -> LPFPix:
        return self.fpixConvolve(fpixs, kel, normflag)

    def capi_fpix_convolve_sep(self, fpixs: LPFPix, kelx: LPL_Kernel,
                               kely: LPL_Kernel, normflag: int) -> LPFPix:
        return self.fpixConvolveSep(fpixs, kelx, kely, normflag)

    def capi_pix_convolve_with_bias(self, pixs: LPPix, kel1: LPL_Kernel,
                                    kel2: LPL_Kernel, force8: int,
                                    pbias: c_int_p) -> LPPix:
        return self.pixConvolveWithBias(pixs, kel1, kel2, force8, pbias)

    def capi_l_setConvolveSampling(self, xfact: int, yfact: int):
        self.l_setConvolveSampling(xfact, yfact)

    def capi_pix_add_gaussian_noise(self, pixs: LPPix, stdev: float) -> LPPix:
        return self.pixAddGaussianNoise(pixs, stdev)

    def capi_gauss_distrib_sampling(self) -> float:
        return self.gaussDistribSampling()

    def capi_pix_correlation_score(self, pix1: LPPix, pix2: LPPix, area1: int,
                                   area2: int, delx: float, dely: float,
                                   maxdiffw: int, maxdiffh: int, tab: c_int_p,
                                   pscore: c_float_p) -> int:
        return self.pixCorrelationScore(pix1, pix2, area1, area2, delx, dely,
                                        maxdiffw, maxdiffh, tab, pscore)

    def capi_pix_correlation_score_thresholded(self, pix1: LPPix, pix2: LPPix,
                                               area1: int, area2: int,
                                               delx: float, dely: float,
                                               maxdiffw: int, maxdiffh: int,
                                               tab: c_int_p,
                                               downcount: c_int_p,
                                               score_threshold: float) -> int:
        return self.pixCorrelationScoreThresholded(pix1, pix2, area1, area2,
                                                   delx, dely, maxdiffw,
                                                   maxdiffh, tab, downcount,
                                                   score_threshold)

    def capi_pix_correlation_score_simple(self, pix1: LPPix, pix2: LPPix,
                                          area1: int, area2: int, delx: float,
                                          dely: float, maxdiffw: int,
                                          maxdiffh: int, tab: c_int_p,
                                          pscore: c_float_p) -> int:
        return self.pixCorrelationScoreSimple(pix1, pix2, area1, area2, delx,
                                              dely, maxdiffw, maxdiffh, tab,
                                              pscore)

    def capi_pix_correlation_score_shifted(self, pix1: LPPix, pix2: LPPix,
                                           area1: int, area2: int, delx: int,
                                           dely: int, tab: c_int_p,
                                           pscore: c_float_p) -> int:
        return self.pixCorrelationScoreShifted(pix1, pix2, area1, area2, delx,
                                               dely, tab, pscore)

    def capi_dewarp_create(self, pixs: LPPix, pageno: int) -> LPL_Dewarp:
        return self.dewarpCreate(pixs, pageno)

    def capi_dewarp_create_ref(self, pageno: int, refpage: int) -> LPL_Dewarp:
        return self.dewarpCreateRef(pageno, refpage)

    def capi_dewarp_destroy(self, pdew: LPLPL_Dewarp):
        self.dewarpDestroy(pdew)

    def capi_dewarpa_create(self, nptrs: int, sampling: int, redfactor: int,
                            minlines: int, maxdist: int) -> LPL_Dewarpa:
        return self.dewarpaCreate(nptrs, sampling, redfactor, minlines,
                                  maxdist)

    def capi_dewarpa_create_from_pixacomp(self, pixac: LPPixaComp,
                                          useboth: int, sampling: int,
                                          minlines: int,
                                          maxdist: int) -> LPL_Dewarpa:
        return self.dewarpaCreateFromPixacomp(pixac, useboth, sampling,
                                              minlines, maxdist)

    def capi_dewarpa_destroy(self, pdewa: LPLPL_Dewarpa):
        self.dewarpaDestroy(pdewa)

    def capi_dewarpa_destroy_dewarp(self, dewa: LPL_Dewarpa,
                                    pageno: int) -> int:
        return self.dewarpaDestroyDewarp(dewa, pageno)

    def capi_dewarpa_insert_dewarp(self, dewa: LPL_Dewarpa,
                                   dew: LPL_Dewarp) -> int:
        return self.dewarpaInsertDewarp(dewa, dew)

    def capi_dewarpa_get_dewarp(self, dewa: LPL_Dewarpa,
                                index: int) -> LPL_Dewarp:
        return self.dewarpaGetDewarp(dewa, index)

    def capi_dewarpa_set_curvatures(self, dewa: LPL_Dewarpa, max_linecurv: int,
                                    min_diff_linecurv: int,
                                    max_diff_linecurv: int, max_edgecurv: int,
                                    max_diff_edgecurv: int,
                                    max_edgeslope: int) -> int:
        return self.dewarpaSetCurvatures(dewa, max_linecurv, min_diff_linecurv,
                                         max_diff_linecurv, max_edgecurv,
                                         max_diff_edgecurv, max_edgeslope)

    def capi_dewarpa_use_both_arrays(self, dewa: LPL_Dewarpa,
                                     useboth: int) -> int:
        return self.dewarpaUseBothArrays(dewa, useboth)

    def capi_dewarpa_set_check_columns(self, dewa: LPL_Dewarpa,
                                       check_columns: int) -> int:
        return self.dewarpaSetCheckColumns(dewa, check_columns)

    def capi_dewarpa_set_max_distance(self, dewa: LPL_Dewarpa,
                                      maxdist: int) -> int:
        return self.dewarpaSetMaxDistance(dewa, maxdist)

    def capi_dewarp_read(self, filename: bytes) -> LPL_Dewarp:
        return self.dewarpRead(filename)

    def capi_dewarp_read_stream(self, fp: LPFile) -> LPL_Dewarp:
        return self.dewarpReadStream(fp)

    def capi_dewarp_read_mem(self, data: c_ubyte_p, size: int) -> LPL_Dewarp:
        return self.dewarpReadMem(data, size)

    def capi_dewarp_write(self, filename: bytes, dew: LPL_Dewarp) -> int:
        return self.dewarpWrite(filename, dew)

    def capi_dewarp_write_stream(self, fp: LPFile, dew: LPL_Dewarp) -> int:
        return self.dewarpWriteStream(fp, dew)

    def capi_dewarp_write_mem(self, pdata: POINTER(c_ubyte_p),
                              psize: c_size_t_p, dew: LPL_Dewarp) -> int:
        return self.dewarpWriteMem(pdata, psize, dew)

    def capi_dewarpa_read(self, filename: bytes) -> LPL_Dewarpa:
        return self.dewarpaRead(filename)

    def capi_dewarpa_read_stream(self, fp: LPFile) -> LPL_Dewarpa:
        return self.dewarpaReadStream(fp)

    def capi_dewarpa_read_mem(self, data: c_ubyte_p, size: int) -> LPL_Dewarpa:
        return self.dewarpaReadMem(data, size)

    def capi_dewarpa_write(self, filename: bytes, dewa: LPL_Dewarpa) -> int:
        return self.dewarpaWrite(filename, dewa)

    def capi_dewarpa_write_stream(self, fp: LPFile, dewa: LPL_Dewarpa) -> int:
        return self.dewarpaWriteStream(fp, dewa)

    def capi_dewarpa_write_mem(self, pdata: POINTER(c_ubyte_p),
                               psize: c_size_t_p, dewa: LPL_Dewarpa) -> int:
        return self.dewarpaWriteMem(pdata, psize, dewa)

    def capi_dewarp_build_page_model(self, dew: LPL_Dewarp,
                                     debugfile: bytes) -> int:
        return self.dewarpBuildPageModel(dew, debugfile)

    def capi_dewarp_find_vert_disparity(self, dew: LPL_Dewarp, ptaa: LPPtaa,
                                        rotflag: int) -> int:
        return self.dewarpFindVertDisparity(dew, ptaa, rotflag)

    def capi_dewarp_find_horiz_disparity(self, dew: LPL_Dewarp,
                                         ptaa: LPPtaa) -> int:
        return self.dewarpFindHorizDisparity(dew, ptaa)

    def capi_dewarp_get_textline_centers(self, pixs: LPPix,
                                         debugflag: int) -> LPPtaa:
        return self.dewarpGetTextlineCenters(pixs, debugflag)

    def capi_dewarp_remove_short_lines(self, pixs: LPPix, ptaas: LPPtaa,
                                       fract: float,
                                       debugflag: int) -> LPPtaa:
        return self.dewarpRemoveShortLines(pixs, ptaas, fract, debugflag)

    def capi_dewarp_find_horiz_slope_disparity(self, dew: LPL_Dewarp,
                                               pixb: LPPix, fractthresh: float,
                                               parity: int) -> int:
        return self.dewarpFindHorizSlopeDisparity(dew, pixb, fractthresh,
                                                  parity)

    def capi_dewarp_build_line_model(self, dew: LPL_Dewarp, opensize: int,
                                     debugfile: bytes) -> int:
        return self.dewarpBuildLineModel(dew, opensize, debugfile)

    def capi_dewarpa_model_status(self, dewa: LPL_Dewarpa, pageno: int,
                                  pvsuccess: c_int_p,
                                  phsuccess: c_int_p) -> int:
        return self.dewarpaModelStatus(dewa, pageno, pvsuccess, phsuccess)

    def capi_dewarpa_apply_disparity(self, dewa: LPL_Dewarpa, pageno: int,
                                     pixs: LPPix, grayin: int, x: int, y: int,
                                     ppixd: LPLPPix, debugfile: bytes) -> int:
        return self.dewarpaApplyDisparity(dewa, pageno, pixs, grayin, x, y,
                                          ppixd, debugfile)

    def capi_dewarpa_apply_disparity_boxa(self, dewa: LPL_Dewarpa, pageno: int,
                                          pixs: LPPix, boxas: LPBoxa,
                                          mapdir: int, x: int, y: int,
                                          pboxad: LPLPBoxa,
                                          debugfile: bytes) -> int:
        return self.dewarpaApplyDisparityBoxa(dewa, pageno, pixs, boxas,
                                              mapdir, x, y, pboxad, debugfile)

    def capi_dewarp_minimize(self, dew: LPL_Dewarp) -> int:
        return self.dewarpMinimize(dew)

    def capi_dewarp_populate_full_res(self, dew: LPL_Dewarp, pix: LPPix,
                                      x: int, y: int) -> int:
        return self.dewarpPopulateFullRes(dew, pix, x, y)

    def capi_dewarp_single_page(self, pixs: LPPix, thresh: int, adaptive: int,
                                useboth: int, check_columns: int,
                                ppixd: LPLPPix, pdewa: LPLPL_Dewarpa,
                                debug: int) -> int:
        return self.dewarpSinglePage(pixs, thresh, adaptive, useboth,
                                     check_columns, ppixd, pdewa, debug)

    def capi_dewarp_single_page_init(self, pixs: LPPix, thresh: int,
                                     adaptive: int, useboth: int,
                                     check_columns: int, ppixb: LPLPPix,
                                     pdewa: LPLPL_Dewarpa) -> int:
        return self.dewarpSinglePageInit(pixs, thresh, adaptive, useboth,
                                         check_columns, ppixb, pdewa)

    def capi_dewarp_single_page_run(self, pixs: LPPix, pixb: LPPix,
                                    dewa: LPL_Dewarpa, ppixd: LPLPPix,
                                    debug: int) -> int:
        return self.dewarpSinglePageRun(pixs, pixb, dewa, ppixd, debug)

    def capi_dewarpa_list_pages(self, dewa: LPL_Dewarpa) -> int:
        return self.dewarpaListPages(dewa)

    def capi_dewarpa_set_valid_models(self, dewa: LPL_Dewarpa, notests: int,
                                      debug: int) -> int:
        return self.dewarpaSetValidModels(dewa, notests, debug)

    def capi_dewarpa_insert_ref_models(self, dewa: LPL_Dewarpa, notests: int,
                                       debug: int) -> int:
        return self.dewarpaInsertRefModels(dewa, notests, debug)

    def capi_dewarpa_strip_ref_models(self, dewa: LPL_Dewarpa) -> int:
        return self.dewarpaStripRefModels(dewa)

    def capi_dewarpa_restore_models(self, dewa: LPL_Dewarpa) -> int:
        return self.dewarpaRestoreModels(dewa)

    def capi_dewarpa_info(self, fp: LPFile, dewa: LPL_Dewarpa) -> int:
        return self.dewarpaInfo(fp, dewa)

    def capi_dewarpa_model_stats(self, dewa: LPL_Dewarpa, pnnone: c_int_p,
                                 pnvsuccess: c_int_p, pnvvalid: c_int_p,
                                 pnhsuccess: c_int_p, pnhvalid: c_int_p,
                                 pnref: c_int_p) -> int:
        return self.dewarpaModelStats(dewa, pnnone, pnvsuccess, pnvvalid,
                                      pnhsuccess, pnhvalid, pnref)

    def capi_dewarpa_show_arrays(self, dewa: LPL_Dewarpa, scalefact: float,
                                 first: int, last: int) -> int:
        return self.dewarpaShowArrays(dewa, scalefact, first, last)

    def capi_dewarp_debug(self, dew: LPL_Dewarp, subdirs: bytes,
                          index: int) -> int:
        return self.dewarpDebug(dew, subdirs, index)

    def capi_dewarp_show_results(self, dewa: LPL_Dewarpa, sa: LPSarray,
                                 boxa: LPBoxa, firstpage: int, lastpage: int,
                                 pdfout: bytes) -> int:
        return self.dewarpShowResults(dewa, sa, boxa, firstpage, lastpage,
                                      pdfout)

    def capi_l_dnaCreate(self, n: int) -> LPL_Dna:
        return self.l_dnaCreate(n)

    def capi_l_dnaCreateFromIArray(self, iarray: c_int_p,
                                   size: int) -> LPL_Dna:
        return self.l_dnaCreateFromIArray(iarray, size)

    def capi_l_dnaCreateFromDArray(self, darray: c_double_p, size: int,
                                   copyflag: int) -> LPL_Dna:
        return self.l_dnaCreateFromDArray(darray, size, copyflag)

    def capi_l_dnaMakeSequence(self, startval: float, increment: float,
                               size: int) -> LPL_Dna:
        return self.l_dnaMakeSequence(startval, increment, size)

    def capi_l_dnaDestroy(self, pda: LPLPL_Dna):
        self.l_dnaDestroy(pda)

    def capi_l_dnaCopy(self, da: LPL_Dna) -> LPL_Dna:
        return self.l_dnaCopy(da)

    def capi_l_dnaClone(self, da: LPL_Dna) -> LPL_Dna:
        return self.l_dnaClone(da)

    def capi_l_dnaEmpty(self, da: LPL_Dna) -> int:
        return self.l_dnaEmpty(da)

    def capi_l_dnaAddNumber(self, da: LPL_Dna, val: float) -> int:
        return self.l_dnaAddNumber(da, val)

    def capi_l_dnaInsertNumber(self, da: LPL_Dna, index: int,
                               val: float) -> int:
        return self.l_dnaInsertNumber(da, index, val)

    def capi_l_dnaRemoveNumber(self, da: LPL_Dna, index: int) -> int:
        return self.l_dnaRemoveNumber(da, index)

    def capi_l_dnaReplaceNumber(self, da: LPL_Dna, index: int,
                                val: float) -> int:
        return self.l_dnaReplaceNumber(da, index, val)

    def capi_l_dnaGetCount(self, da: LPL_Dna) -> int:
        return self.l_dnaGetCount(da)

    def capi_l_dnaSetCount(self, da: LPL_Dna, newcount: int) -> int:
        return self.l_dnaSetCount(da, newcount)

    def capi_l_dnaGetDValue(self, da: LPL_Dna, index: int,
                            pval: c_double_p) -> int:
        return self.l_dnaGetDValue(da, index, pval)

    def capi_l_dnaGetIValue(self, da: LPL_Dna, index: int,
                            pival: c_int_p) -> int:
        return self.l_dnaGetIValue(da, index, pival)

    def capi_l_dnaSetValue(self, da: LPL_Dna, index: int, val: float) -> int:
        return self.l_dnaSetValue(da, index, val)

    def capi_l_dnaShiftValue(self, da: LPL_Dna, index: int,
                             diff: float) -> int:
        return self.l_dnaShiftValue(da, index, diff)

    def capi_l_dnaGetIArray(self, da: LPL_Dna) -> c_int_p:
        return self.l_dnaGetIArray(da)

    def capi_l_dnaGetDArray(self, da: LPL_Dna, copyflag: int) -> c_double_p:
        return self.l_dnaGetDArray(da, copyflag)

    def capi_l_dnaGetRefcount(self, da: LPL_Dna) -> int:
        return self.l_dnaGetRefcount(da)

    def capi_l_dnaChangeRefcount(self, da: LPL_Dna, delta: int) -> int:
        return self.l_dnaChangeRefcount(da, delta)

    def capi_l_dnaGetParameters(self, da: LPL_Dna, pstartx: c_double_p,
                                pdelx: c_double_p) -> int:
        return self.l_dnaGetParameters(da, pstartx, pdelx)

    def capi_l_dnaSetParameters(self, da: LPL_Dna, startx: float,
                                delx: float) -> int:
        return self.l_dnaSetParameters(da, startx, delx)

    def capi_l_dnaCopyParameters(self, dad: LPL_Dna, das: LPL_Dna) -> int:
        return self.l_dnaCopyParameters(dad, das)

    def capi_l_dnaRead(self, filename: bytes) -> LPL_Dna:
        return self.l_dnaRead(filename)

    def capi_l_dnaReadStream(self, fp: LPFile) -> LPL_Dna:
        return self.l_dnaReadStream(fp)

    def capi_l_dnaReadMem(self, data: c_ubyte_p, size: int) -> LPL_Dna:
        return self.l_dnaReadMem(data, size)

    def capi_l_dnaWrite(self, filename: bytes, da: LPL_Dna) -> int:
        return self.l_dnaWrite(filename, da)

    def capi_l_dnaWriteStream(self, fp: LPFile, da: LPL_Dna) -> int:
        return self.l_dnaWriteStream(fp, da)

    def capi_l_dnaWriteStderr(self, da: LPL_Dna) -> int:
        return self.l_dnaWriteStderr(da)

    def capi_l_dnaWriteMem(self, pdata: POINTER(c_ubyte_p), psize: c_size_t_p,
                           da: LPL_Dna) -> int:
        return self.l_dnaWriteMem(pdata, psize, da)

    def capi_l_dnaaCreate(self, n: int) -> LPL_Dnaa:
        return self.l_dnaaCreate(n)

    def capi_l_dnaaCreateFull(self, nptr: int, n: int) -> LPL_Dnaa:
        return self.l_dnaaCreateFull(nptr, n)

    def capi_l_dnaaTruncate(self, daa: LPL_Dnaa) -> int:
        return self.l_dnaaTruncate(daa)

    def capi_l_dnaaDestroy(self, pdaa: LPLPL_Dnaa):
        self.l_dnaaDestroy(pdaa)

    def capi_l_dnaaAddDna(self, daa: LPL_Dnaa, da: LPL_Dna,
                          copyflag: int) -> int:
        return self.l_dnaaAddDna(daa, da, copyflag)

    def capi_l_dnaaGetCount(self, daa: LPL_Dnaa) -> int:
        return self.l_dnaaGetCount(daa)

    def capi_l_dnaaGetDnaCount(self, daa: LPL_Dnaa, index: int) -> int:
        return self.l_dnaaGetDnaCount(daa, index)

    def capi_l_dnaaGetNumberCount(self, daa: LPL_Dnaa) -> int:
        return self.l_dnaaGetNumberCount(daa)

    def capi_l_dnaaGetDna(self, daa: LPL_Dnaa, index: int,
                          accessflag: int) -> LPL_Dna:
        return self.l_dnaaGetDna(daa, index, accessflag)

    def capi_l_dnaaReplaceDna(self, daa: LPL_Dnaa, index: int,
                              da: LPL_Dna) -> int:
        return self.l_dnaaReplaceDna(daa, index, da)

    def capi_l_dnaaGetValue(self, daa: LPL_Dnaa, i: int, j: int,
                            pval: c_double_p) -> int:
        return self.l_dnaaGetValue(daa, i, j, pval)

    def capi_l_dnaaAddNumber(self, daa: LPL_Dnaa, index: int,
                             val: float) -> int:
        return self.l_dnaaAddNumber(daa, index, val)

    def capi_l_dnaaRead(self, filename: bytes) -> LPL_Dnaa:
        return self.l_dnaaRead(filename)

    def capi_l_dnaaReadStream(self, fp: LPFile) -> LPL_Dnaa:
        return self.l_dnaaReadStream(fp)

    def capi_l_dnaaReadMem(self, data: c_ubyte_p, size: int) -> LPL_Dnaa:
        return self.l_dnaaReadMem(data, size)

    def capi_l_dnaaWrite(self, filename: bytes, daa: LPL_Dnaa) -> int:
        return self.l_dnaaWrite(filename, daa)

    def capi_l_dnaaWriteStream(self, fp: LPFile, daa: LPL_Dnaa) -> int:
        return self.l_dnaaWriteStream(fp, daa)

    def capi_l_dnaaWriteMem(self, pdata: POINTER(c_ubyte_p), psize: c_size_t_p,
                            daa: LPL_Dnaa) -> int:
        return self.l_dnaaWriteMem(pdata, psize, daa)

    def capi_l_dnaJoin(self, dad: LPL_Dna, das: LPL_Dna, istart: int,
                       iend: int) -> int:
        return self.l_dnaJoin(dad, das, istart, iend)

    def capi_l_dnaaFlattenToDna(self, daa: LPL_Dnaa) -> LPL_Dna:
        return self.l_dnaaFlattenToDna(daa)

    def capi_l_dnaSelectRange(self, das: LPL_Dna, first: int,
                              last: int) -> LPL_Dna:
        return self.l_dnaSelectRange(das, first, last)

    def capi_l_dnaConvertToNuma(self, da: LPL_Dna) -> LPNuma:
        return self.l_dnaConvertToNuma(da)

    def capi_numa_convert_to_dna(self, na: LPNuma) -> LPL_Dna:
        return self.numaConvertToDna(na)

    def capi_pix_convert_data_to_dna(self, pix: LPPix) -> LPL_Dna:
        return self.pixConvertDataToDna(pix)

    def capi_l_asetCreateFromDna(self, da: LPL_Dna) -> LPL_Rbtree:
        return self.l_asetCreateFromDna(da)

    def capi_l_dnaRemoveDupsByAset(self, das: LPL_Dna, pdad: LPLPL_Dna) -> int:
        return self.l_dnaRemoveDupsByAset(das, pdad)

    def capi_l_dnaUnionByAset(self, da1: LPL_Dna, da2: LPL_Dna,
                              pdad: LPLPL_Dna) -> int:
        return self.l_dnaUnionByAset(da1, da2, pdad)

    def capi_l_dnaIntersectionByAset(self, da1: LPL_Dna, da2: LPL_Dna,
                                     pdad: LPLPL_Dna) -> int:
        return self.l_dnaIntersectionByAset(da1, da2, pdad)

    def capi_l_hmapCreateFromDna(self, da: LPL_Dna) -> LPL_Hashmap:
        return self.l_hmapCreateFromDna(da)

    def capi_l_dnaRemoveDupsByHmap(self, das: LPL_Dna, pdad: LPLPL_Dna,
                                   phmap: LPLPL_Hashmap) -> int:
        return self.l_dnaRemoveDupsByHmap(das, pdad, phmap)

    def capi_l_dnaUnionByHmap(self, da1: LPL_Dna, da2: LPL_Dna,
                              pdad: LPLPL_Dna) -> int:
        return self.l_dnaUnionByHmap(da1, da2, pdad)

    def capi_l_dnaIntersectionByHmap(self, da1: LPL_Dna, da2: LPL_Dna,
                                     pdad: LPLPL_Dna) -> int:
        return self.l_dnaIntersectionByHmap(da1, da2, pdad)

    def capi_l_dnaMakeHistoByHmap(self, das: LPL_Dna, pdav: LPLPL_Dna,
                                  pdac: LPLPL_Dna) -> int:
        return self.l_dnaMakeHistoByHmap(das, pdav, pdac)

    def capi_l_dnaDiffAdjValues(self, das: LPL_Dna) -> LPL_Dna:
        return self.l_dnaDiffAdjValues(das)

    def capi_l_dnaHashCreate(self, nbuckets: int,
                             initsize: int) -> LPL_DnaHash:
        return self.l_dnaHashCreate(nbuckets, initsize)

    def capi_l_dnaHashDestroy(self, pdahash: LPLPL_DnaHash):
        self.l_dnaHashDestroy(pdahash)

    def capi_l_dnaHashGetDna(self, dahash: LPL_DnaHash, key: int,
                             copyflag: int) -> LPL_Dna:
        return self.l_dnaHashGetDna(dahash, key, copyflag)

    def capi_l_dnaHashAdd(self, dahash: LPL_DnaHash, key: int,
                          value: float) -> int:
        return self.l_dnaHashAdd(dahash, key, value)

    def capi_pixMorphDwa_2(self, pixd: LPPix, pixs: LPPix, operation: int,
                           selname: LP_c_char) -> LPPix:
        return self.pixMorphDwa_2(pixd, pixs, operation, selname)

    def capi_pixFMorphopGen_2(self, pixd: LPPix, pixs: LPPix, operation: int,
                              selname: LP_c_char) -> LPPix:
        return self.pixFMorphopGen_2(pixd, pixs, operation, selname)

    def capi_fmorphopgen_low_2(self, datad: c_uint_p, w: int, h: int,
                               wpld: int, datas: c_uint_p, wpls: int,
                               index: int) -> int:
        return self.fmorphopgen_low_2(datad, w, h, wpld, datas, wpls, index)

    def capi_pix_sobel_edge_filter(self, pixs: LPPix,
                                   orientflag: int) -> LPPix:
        return self.pixSobelEdgeFilter(pixs, orientflag)

    def capi_pix_two_sided_edge_filter(self, pixs: LPPix,
                                       orientflag: int) -> LPPix:
        return self.pixTwoSidedEdgeFilter(pixs, orientflag)

    def capi_pix_measure_edge_smoothness(self, pixs: LPPix, side: int,
                                         minjump: int, minreversal: int,
                                         pjpl: c_float_p, pjspl: c_float_p,
                                         prpl: c_float_p,
                                         debugfile: bytes) -> int:
        return self.pixMeasureEdgeSmoothness(pixs, side, minjump, minreversal,
                                             pjpl, pjspl, prpl, debugfile)

    def capi_pix_get_edge_profile(self, pixs: LPPix, side: int,
                                  debugfile: bytes) -> LPNuma:
        return self.pixGetEdgeProfile(pixs, side, debugfile)

    def capi_pix_get_last_off_pixel_in_run(self, pixs: LPPix, x: int, y: int,
                                           direction: int,
                                           ploc: c_int_p) -> int:
        return self.pixGetLastOffPixelInRun(pixs, x, y, direction, ploc)

    def capi_pix_get_last_on_pixel_in_run(self, pixs: LPPix, x: int, y: int,
                                          direction: int,
                                          ploc: c_int_p) -> int:
        return self.pixGetLastOnPixelInRun(pixs, x, y, direction, ploc)

    def capi_encode_base64(self, inarray: c_ubyte_p, insize: int,
                           poutsize: c_int_p) -> LP_c_char:
        return self.encodeBase64(inarray, insize, poutsize)

    def capi_decode_base64(self, inarray: bytes, insize: int,
                           poutsize: c_int_p) -> c_ubyte_p:
        return self.decodeBase64(inarray, insize, poutsize)

    def capi_encode_ascii85(self, inarray: c_ubyte_p, insize: int,
                            poutsize: c_size_t_p) -> LP_c_char:
        return self.encodeAscii85(inarray, insize, poutsize)

    def capi_decode_ascii85(self, inarray: bytes, insize: int,
                            poutsize: c_size_t_p) -> c_ubyte_p:
        return self.decodeAscii85(inarray, insize, poutsize)

    def capi_encode_ascii85with_comp(self, indata: c_ubyte_p, insize: int,
                                     poutsize: c_size_t_p) -> LP_c_char:
        return self.encodeAscii85WithComp(indata, insize, poutsize)

    def capi_decode_ascii85with_comp(self, instr: bytes, insize: int,
                                     poutsize: c_size_t_p) -> c_ubyte_p:
        return self.decodeAscii85WithComp(instr, insize, poutsize)

    def capi_reformat_packed64(self, inarray: bytes, insize: int,
                               leadspace: int, linechars: int, addquotes: int,
                               poutsize: c_int_p) -> LP_c_char:
        return self.reformatPacked64(inarray, insize, leadspace, linechars,
                                     addquotes, poutsize)

    def capi_pix_gamma_trc(self, pixd: LPPix, pixs: LPPix, gamma: float,
                           minval: int, maxval: int) -> LPPix:
        return self.pixGammaTRC(pixd, pixs, gamma, minval, maxval)

    def capi_pix_gamma_trc_masked(self, pixd: LPPix, pixs: LPPix, pixm: LPPix,
                                  gamma: float, minval: int,
                                  maxval: int) -> LPPix:
        return self.pixGammaTRCMasked(pixd, pixs, pixm, gamma, minval, maxval)

    def capi_pix_gamma_trc_with_alpha(self, pixd: LPPix, pixs: LPPix,
                                      gamma: float, minval: int,
                                      maxval: int) -> LPPix:
        return self.pixGammaTRCWithAlpha(pixd, pixs, gamma, minval, maxval)

    def capi_numa_gamma_trc(self, gamma: float, minval: int,
                            maxval: int) -> LPNuma:
        return self.numaGammaTRC(gamma, minval, maxval)

    def capi_pix_contrast_trc(self, pixd: LPPix, pixs: LPPix,
                              factor: float) -> LPPix:
        return self.pixContrastTRC(pixd, pixs, factor)

    def capi_pix_contrast_trc_masked(self, pixd: LPPix, pixs: LPPix,
                                     pixm: LPPix, factor: float) -> LPPix:
        return self.pixContrastTRCMasked(pixd, pixs, pixm, factor)

    def capi_numa_contrast_trc(self, factor: float) -> LPNuma:
        return self.numaContrastTRC(factor)

    def capi_pix_equalize_trc(self, pixd: LPPix, pixs: LPPix, fract: float,
                              factor: int) -> LPPix:
        return self.pixEqualizeTRC(pixd, pixs, fract, factor)

    def capi_numa_equalize_trc(self, pix: LPPix, fract: float,
                               factor: int) -> LPNuma:
        return self.numaEqualizeTRC(pix, fract, factor)

    def capi_pix_trc_map(self, pixs: LPPix, pixm: LPPix, na: LPNuma) -> int:
        return self.pixTRCMap(pixs, pixm, na)

    def capi_pix_trc_map_general(self, pixs: LPPix, pixm: LPPix, nar: LPNuma,
                                 nag: LPNuma, nab: LPNuma) -> int:
        return self.pixTRCMapGeneral(pixs, pixm, nar, nag, nab)

    def capi_pix_unsharp_masking(self, pixs: LPPix, halfwidth: int,
                                 fract: float) -> LPPix:
        return self.pixUnsharpMasking(pixs, halfwidth, fract)

    def capi_pix_unsharp_masking_gray(self, pixs: LPPix, halfwidth: int,
                                      fract: float) -> LPPix:
        return self.pixUnsharpMaskingGray(pixs, halfwidth, fract)

    def capi_pix_unsharp_masking_fast(self, pixs: LPPix, halfwidth: int,
                                      fract: float, direction: int) -> LPPix:
        return self.pixUnsharpMaskingFast(pixs, halfwidth, fract, direction)

    def capi_pix_unsharp_masking_gray_fast(self, pixs: LPPix, halfwidth: int,
                                           fract: float,
                                           direction: int) -> LPPix:
        return self.pixUnsharpMaskingGrayFast(pixs, halfwidth, fract,
                                              direction)

    def capi_pix_unsharp_masking_gray1d(self, pixs: LPPix, halfwidth: int,
                                        fract: float,
                                        direction: int) -> LPPix:
        return self.pixUnsharpMaskingGray1D(pixs, halfwidth, fract, direction)

    def capi_pix_unsharp_masking_gray2d(self, pixs: LPPix, halfwidth: int,
                                        fract: float) -> LPPix:
        return self.pixUnsharpMaskingGray2D(pixs, halfwidth, fract)

    def capi_pix_modify_hue(self, pixd: LPPix, pixs: LPPix,
                            fract: float) -> LPPix:
        return self.pixModifyHue(pixd, pixs, fract)

    def capi_pix_modify_saturation(self, pixd: LPPix, pixs: LPPix,
                                   fract: float) -> LPPix:
        return self.pixModifySaturation(pixd, pixs, fract)

    def capi_pix_measure_saturation(self, pixs: LPPix, factor: int,
                                    psat: c_float_p) -> int:
        return self.pixMeasureSaturation(pixs, factor, psat)

    def capi_pix_modify_brightness(self, pixd: LPPix, pixs: LPPix,
                                   fract: float) -> LPPix:
        return self.pixModifyBrightness(pixd, pixs, fract)

    def capi_pix_mosaic_color_shift_rgb(self, pixs: LPPix, roff: float,
                                        goff: float, boff: float, delta: float,
                                        nincr: int) -> LPPix:
        return self.pixMosaicColorShiftRGB(pixs, roff, goff, boff, delta,
                                           nincr)

    def capi_pix_color_shift_rgb(self, pixs: LPPix, rfract: float,
                                 gfract: float, bfract: float) -> LPPix:
        return self.pixColorShiftRGB(pixs, rfract, gfract, bfract)

    def capi_pix_darken_gray(self, pixd: LPPix, pixs: LPPix, thresh: int,
                             satlimit: int) -> LPPix:
        return self.pixDarkenGray(pixd, pixs, thresh, satlimit)

    def capi_pix_mult_constant_color(self, pixs: LPPix, rfact: float,
                                     gfact: float, bfact: float) -> LPPix:
        return self.pixMultConstantColor(pixs, rfact, gfact, bfact)

    def capi_pix_mult_matrix_color(self, pixs: LPPix,
                                   kel: LPL_Kernel) -> LPPix:
        return self.pixMultMatrixColor(pixs, kel)

    def capi_pix_half_edge_by_bandpass(self, pixs: LPPix, sm1h: int, sm1v: int,
                                       sm2h: int, sm2v: int) -> LPPix:
        return self.pixHalfEdgeByBandpass(pixs, sm1h, sm1v, sm2h, sm2v)

    def capi_fhmtautogen(self, sela: LPSela, fileindex: int,
                         filename: bytes) -> int:
        return self.fhmtautogen(sela, fileindex, filename)

    def capi_fhmtautogen1(self, sela: LPSela, fileindex: int,
                          filename: bytes) -> int:
        return self.fhmtautogen1(sela, fileindex, filename)

    def capi_fhmtautogen2(self, sela: LPSela, fileindex: int,
                          filename: bytes) -> int:
        return self.fhmtautogen2(sela, fileindex, filename)

    def capi_pixHMTDwa_1(self, pixd: LPPix, pixs: LPPix,
                         selname: bytes) -> LPPix:
        return self.pixHMTDwa_1(pixd, pixs, selname)

    def capi_pixFHMTGen_1(self, pixd: LPPix, pixs: LPPix,
                          selname: bytes) -> LPPix:
        return self.pixFHMTGen_1(pixd, pixs, selname)

    def capi_fhmtgen_low_1(self, datad: c_uint_p, w: int, h: int, wpld: int,
                           datas: c_uint_p, wpls: int, index: int) -> int:
        return self.fhmtgen_low_1(datad, w, h, wpld, datas, wpls, index)

    def capi_pix_italic_words(self, pixs: LPPix, boxaw: LPBoxa, pixw: LPPix,
                              pboxa: LPLPBoxa, debugflag: int) -> int:
        return self.pixItalicWords(pixs, boxaw, pixw, pboxa, debugflag)

    def capi_pix_orient_correct(self, pixs: LPPix, minupconf: float,
                                minratio: float, pupconf: c_float_p,
                                pleftconf: c_float_p, protation: c_int_p,
                                debug: int) -> LPPix:
        return self.pixOrientCorrect(pixs, minupconf, minratio, pupconf,
                                     pleftconf, protation, debug)

    def capi_pix_orient_detect(self, pixs: LPPix, pupconf: c_float_p,
                               pleftconf: c_float_p, mincount: int,
                               debug: int) -> int:
        return self.pixOrientDetect(pixs, pupconf, pleftconf, mincount, debug)

    def capi_make_orient_decision(self, upconf: float, leftconf: float,
                                  minupconf: float, minratio: float,
                                  porient: c_int_p, debug: int) -> int:
        return self.makeOrientDecision(upconf, leftconf, minupconf, minratio,
                                       porient, debug)

    def capi_pix_up_down_detect(self, pixs: LPPix, pconf: c_float_p,
                                mincount: int, npixels: int,
                                debug: int) -> int:
        return self.pixUpDownDetect(pixs, pconf, mincount, npixels, debug)

    def capi_pix_mirror_detect(self, pixs: LPPix, pconf: c_float_p,
                               mincount: int, debug: int) -> int:
        return self.pixMirrorDetect(pixs, pconf, mincount, debug)

    def capi_fmorphautogen(self, sela: LPSela, fileindex: int,
                           filename: bytes) -> int:
        return self.fmorphautogen(sela, fileindex, filename)

    def capi_fmorphautogen1(self, sela: LPSela, fileindex: int,
                            filename: bytes) -> int:
        return self.fmorphautogen1(sela, fileindex, filename)

    def capi_fmorphautogen2(self, sela: LPSela, fileindex: int,
                            filename: bytes) -> int:
        return self.fmorphautogen2(sela, fileindex, filename)

    def capi_pixMorphDwa_1(self, pixd: LPPix, pixs: LPPix, operation: int,
                           selname: LP_c_char) -> LPPix:
        return self.pixMorphDwa_1(pixd, pixs, operation, selname)

    def capi_pixFMorphopGen_1(self, pixd: LPPix, pixs: LPPix, operation: int,
                              selname: LP_c_char) -> LPPix:
        return self.pixFMorphopGen_1(pixd, pixs, operation, selname)

    def capi_fmorphopgen_low_1(self, datad: c_uint_p, w: int, h: int,
                               wpld: int, datas: c_uint_p, wpls: int,
                               index: int) -> int:
        return self.fmorphopgen_low_1(datad, w, h, wpld, datas, wpls, index)

    def capi_fpix_create(self, width: int, height: int) -> LPFPix:
        return self.fpixCreate(width, height)

    def capi_fpix_create_template(self, fpixs: LPFPix) -> LPFPix:
        return self.fpixCreateTemplate(fpixs)

    def capi_fpix_clone(self, fpix: LPFPix) -> LPFPix:
        return self.fpixClone(fpix)

    def capi_fpix_copy(self, fpixs: LPFPix) -> LPFPix:
        return self.fpixCopy(fpixs)

    def capi_fpix_destroy(self, pfpix: LPLPFPix):
        self.fpixDestroy(pfpix)

    def capi_fpix_get_dimensions(self, fpix: LPFPix, pw: c_int_p,
                                 ph: c_int_p) -> int:
        return self.fpixGetDimensions(fpix, pw, ph)

    def capi_fpix_set_dimensions(self, fpix: LPFPix, w: int, h: int) -> int:
        return self.fpixSetDimensions(fpix, w, h)

    def capi_fpix_get_wpl(self, fpix: LPFPix) -> int:
        return self.fpixGetWpl(fpix)

    def capi_fpix_set_wpl(self, fpix: LPFPix, wpl: int) -> int:
        return self.fpixSetWpl(fpix, wpl)

    def capi_fpix_get_refcount(self, fpix: LPFPix) -> int:
        return self.fpixGetRefcount(fpix)

    def capi_fpix_change_refcount(self, fpix: LPFPix, delta: int) -> int:
        return self.fpixChangeRefcount(fpix, delta)

    def capi_fpix_get_resolution(self, fpix: LPFPix, pxres: c_int_p,
                                 pyres: c_int_p) -> int:
        return self.fpixGetResolution(fpix, pxres, pyres)

    def capi_fpix_set_resolution(self, fpix: LPFPix, xres: int,
                                 yres: int) -> int:
        return self.fpixSetResolution(fpix, xres, yres)

    def capi_fpix_copy_resolution(self, fpixd: LPFPix, fpixs: LPFPix) -> int:
        return self.fpixCopyResolution(fpixd, fpixs)

    def capi_fpix_get_data(self, fpix: LPFPix) -> c_float_p:
        return self.fpixGetData(fpix)

    def capi_fpix_set_data(self, fpix: LPFPix, data: c_float_p) -> int:
        return self.fpixSetData(fpix, data)

    def capi_fpix_get_pixel(self, fpix: LPFPix, x: int, y: int,
                            pval: c_float_p) -> int:
        return self.fpixGetPixel(fpix, x, y, pval)

    def capi_fpix_set_pixel(self, fpix: LPFPix, x: int, y: int,
                            val: float) -> int:
        return self.fpixSetPixel(fpix, x, y, val)

    def capi_fpixa_create(self, n: int) -> LPFPixa:
        return self.fpixaCreate(n)

    def capi_fpixa_copy(self, fpixa: LPFPixa, copyflag: int) -> LPFPixa:
        return self.fpixaCopy(fpixa, copyflag)

    def capi_fpixa_destroy(self, pfpixa: LPLPFPixa):
        self.fpixaDestroy(pfpixa)

    def capi_fpixa_add_fpix(self, fpixa: LPFPixa, fpix: LPFPix,
                            copyflag: int) -> int:
        return self.fpixaAddFPix(fpixa, fpix, copyflag)

    def capi_fpixa_get_count(self, fpixa: LPFPixa) -> int:
        return self.fpixaGetCount(fpixa)

    def capi_fpixa_change_refcount(self, fpixa: LPFPixa, delta: int) -> int:
        return self.fpixaChangeRefcount(fpixa, delta)

    def capi_fpixa_get_fpix(self, fpixa: LPFPixa, index: int,
                            accesstype: int) -> LPFPix:
        return self.fpixaGetFPix(fpixa, index, accesstype)

    def capi_fpixa_get_fpix_dimensions(self, fpixa: LPFPixa, index: int,
                                       pw: c_int_p, ph: c_int_p) -> int:
        return self.fpixaGetFPixDimensions(fpixa, index, pw, ph)

    def capi_fpixa_get_data(self, fpixa: LPFPixa, index: int) -> c_float_p:
        return self.fpixaGetData(fpixa, index)

    def capi_fpixa_get_pixel(self, fpixa: LPFPixa, index: int, x: int, y: int,
                             pval: c_float_p) -> int:
        return self.fpixaGetPixel(fpixa, index, x, y, pval)

    def capi_fpixa_set_pixel(self, fpixa: LPFPixa, index: int, x: int, y: int,
                             val: float) -> int:
        return self.fpixaSetPixel(fpixa, index, x, y, val)

    def capi_dpix_create(self, width: int, height: int) -> LPDPix:
        return self.dpixCreate(width, height)

    def capi_dpix_create_template(self, dpixs: LPDPix) -> LPDPix:
        return self.dpixCreateTemplate(dpixs)

    def capi_dpix_clone(self, dpix: LPDPix) -> LPDPix:
        return self.dpixClone(dpix)

    def capi_dpix_copy(self, dpixs: LPDPix) -> LPDPix:
        return self.dpixCopy(dpixs)

    def capi_dpix_destroy(self, pdpix: LPLPDPix):
        self.dpixDestroy(pdpix)

    def capi_dpix_get_dimensions(self, dpix: LPDPix, pw: c_int_p,
                                 ph: c_int_p) -> int:
        return self.dpixGetDimensions(dpix, pw, ph)

    def capi_dpix_set_dimensions(self, dpix: LPDPix, w: int, h: int) -> int:
        return self.dpixSetDimensions(dpix, w, h)

    def capi_dpix_get_wpl(self, dpix: LPDPix) -> int:
        return self.dpixGetWpl(dpix)

    def capi_dpix_set_wpl(self, dpix: LPDPix, wpl: int) -> int:
        return self.dpixSetWpl(dpix, wpl)

    def capi_dpix_get_refcount(self, dpix: LPDPix) -> int:
        return self.dpixGetRefcount(dpix)

    def capi_dpix_change_refcount(self, dpix: LPDPix, delta: int) -> int:
        return self.dpixChangeRefcount(dpix, delta)

    def capi_dpix_get_resolution(self, dpix: LPDPix, pxres: c_int_p,
                                 pyres: c_int_p) -> int:
        return self.dpixGetResolution(dpix, pxres, pyres)

    def capi_dpix_set_resolution(self, dpix: LPDPix, xres: int,
                                 yres: int) -> int:
        return self.dpixSetResolution(dpix, xres, yres)

    def capi_dpix_copy_resolution(self, dpixd: LPDPix, dpixs: LPDPix) -> int:
        return self.dpixCopyResolution(dpixd, dpixs)

    def capi_dpix_get_data(self, dpix: LPDPix) -> c_double_p:
        return self.dpixGetData(dpix)

    def capi_dpix_set_data(self, dpix: LPDPix, data: c_double_p) -> int:
        return self.dpixSetData(dpix, data)

    def capi_dpix_get_pixel(self, dpix: LPDPix, x: int, y: int,
                            pval: c_double_p) -> int:
        return self.dpixGetPixel(dpix, x, y, pval)

    def capi_dpix_set_pixel(self, dpix: LPDPix, x: int, y: int,
                            val: float) -> int:
        return self.dpixSetPixel(dpix, x, y, val)

    def capi_fpix_read(self, filename: bytes) -> LPFPix:
        return self.fpixRead(filename)

    def capi_fpix_read_stream(self, fp: LPFile) -> LPFPix:
        return self.fpixReadStream(fp)

    def capi_fpix_read_mem(self, data: c_ubyte_p, size: int) -> LPFPix:
        return self.fpixReadMem(data, size)

    def capi_fpix_write(self, filename: bytes, fpix: LPFPix) -> int:
        return self.fpixWrite(filename, fpix)

    def capi_fpix_write_stream(self, fp: LPFile, fpix: LPFPix) -> int:
        return self.fpixWriteStream(fp, fpix)

    def capi_fpix_write_mem(self, pdata: POINTER(c_ubyte_p), psize: c_size_t_p,
                            fpix: LPFPix) -> int:
        return self.fpixWriteMem(pdata, psize, fpix)

    def capi_fpix_endian_byte_swap(self, fpixd: LPFPix,
                                   fpixs: LPFPix) -> LPFPix:
        return self.fpixEndianByteSwap(fpixd, fpixs)

    def capi_dpix_read(self, filename: bytes) -> LPDPix:
        return self.dpixRead(filename)

    def capi_dpix_read_stream(self, fp: LPFile) -> LPDPix:
        return self.dpixReadStream(fp)

    def capi_dpix_read_mem(self, data: c_ubyte_p, size: int) -> LPDPix:
        return self.dpixReadMem(data, size)

    def capi_dpix_write(self, filename: bytes, dpix: LPDPix) -> int:
        return self.dpixWrite(filename, dpix)

    def capi_dpix_write_stream(self, fp: LPFile, dpix: LPDPix) -> int:
        return self.dpixWriteStream(fp, dpix)

    def capi_dpix_write_mem(self, pdata: POINTER(c_ubyte_p), psize: c_size_t_p,
                            dpix: LPDPix) -> int:
        return self.dpixWriteMem(pdata, psize, dpix)

    def capi_dpix_endian_byte_swap(self, dpixd: LPDPix,
                                   dpixs: LPDPix) -> LPDPix:
        return self.dpixEndianByteSwap(dpixd, dpixs)

    def capi_fpix_print_stream(self, fp: LPFile, fpix: LPFPix,
                               factor: int) -> int:
        return self.fpixPrintStream(fp, fpix, factor)

    def capi_pix_convert_to_fpix(self, pixs: LPPix, ncomps: int) -> LPFPix:
        return self.pixConvertToFPix(pixs, ncomps)

    def capi_pix_convert_to_dpix(self, pixs: LPPix, ncomps: int) -> LPDPix:
        return self.pixConvertToDPix(pixs, ncomps)

    def capi_fpix_convert_to_pix(self, fpixs: LPFPix, outdepth: int,
                                 negvals: int, errorflag: int) -> LPPix:
        return self.fpixConvertToPix(fpixs, outdepth, negvals, errorflag)

    def capi_fpix_display_max_dynamic_range(self, fpixs: LPFPix) -> LPPix:
        return self.fpixDisplayMaxDynamicRange(fpixs)

    def capi_fpix_convert_to_dpix(self, fpix: LPFPix) -> LPDPix:
        return self.fpixConvertToDPix(fpix)

    def capi_dpix_convert_to_pix(self, dpixs: LPDPix, outdepth: int,
                                 negvals: int, errorflag: int) -> LPPix:
        return self.dpixConvertToPix(dpixs, outdepth, negvals, errorflag)

    def capi_dpix_convert_to_fpix(self, dpix: LPDPix) -> LPFPix:
        return self.dpixConvertToFPix(dpix)

    def capi_fpix_get_min(self, fpix: LPFPix, pminval: c_float_p,
                          pxminloc: c_int_p, pyminloc: c_int_p) -> int:
        return self.fpixGetMin(fpix, pminval, pxminloc, pyminloc)

    def capi_fpix_get_max(self, fpix: LPFPix, pmaxval: c_float_p,
                          pxmaxloc: c_int_p, pymaxloc: c_int_p) -> int:
        return self.fpixGetMax(fpix, pmaxval, pxmaxloc, pymaxloc)

    def capi_dpix_get_min(self, dpix: LPDPix, pminval: c_double_p,
                          pxminloc: c_int_p, pyminloc: c_int_p) -> int:
        return self.dpixGetMin(dpix, pminval, pxminloc, pyminloc)

    def capi_dpix_get_max(self, dpix: LPDPix, pmaxval: c_double_p,
                          pxmaxloc: c_int_p, pymaxloc: c_int_p) -> int:
        return self.dpixGetMax(dpix, pmaxval, pxmaxloc, pymaxloc)

    def capi_fpix_scale_by_integer(self, fpixs: LPFPix, factor: int) -> LPFPix:
        return self.fpixScaleByInteger(fpixs, factor)

    def capi_dpix_scale_by_integer(self, dpixs: LPDPix, factor: int) -> LPDPix:
        return self.dpixScaleByInteger(dpixs, factor)

    def capi_fpix_linear_combination(self, fpixd: LPFPix, fpixs1: LPFPix,
                                     fpixs2: LPFPix, a: float,
                                     b: float) -> LPFPix:
        return self.fpixLinearCombination(fpixd, fpixs1, fpixs2, a, b)

    def capi_fpix_add_mult_constant(self, fpix: LPFPix, addc: float,
                                    multc: float) -> int:
        return self.fpixAddMultConstant(fpix, addc, multc)

    def capi_dpix_linear_combination(self, dpixd: LPDPix, dpixs1: LPDPix,
                                     dpixs2: LPDPix, a: float,
                                     b: float) -> LPDPix:
        return self.dpixLinearCombination(dpixd, dpixs1, dpixs2, a, b)

    def capi_dpix_add_mult_constant(self, dpix: LPDPix, addc: float,
                                    multc: float) -> int:
        return self.dpixAddMultConstant(dpix, addc, multc)

    def capi_fpix_set_all_arbitrary(self, fpix: LPFPix, inval: float) -> int:
        return self.fpixSetAllArbitrary(fpix, inval)

    def capi_dpix_set_all_arbitrary(self, dpix: LPDPix, inval: float) -> int:
        return self.dpixSetAllArbitrary(dpix, inval)

    def capi_fpix_add_border(self, fpixs: LPFPix, left: int, right: int,
                             top: int, bot: int) -> LPFPix:
        return self.fpixAddBorder(fpixs, left, right, top, bot)

    def capi_fpix_remove_border(self, fpixs: LPFPix, left: int, right: int,
                                top: int, bot: int) -> LPFPix:
        return self.fpixRemoveBorder(fpixs, left, right, top, bot)

    def capi_fpix_add_mirrored_border(self, fpixs: LPFPix, left: int,
                                      right: int, top: int,
                                      bot: int) -> LPFPix:
        return self.fpixAddMirroredBorder(fpixs, left, right, top, bot)

    def capi_fpix_add_continued_border(self, fpixs: LPFPix, left: int,
                                       right: int, top: int,
                                       bot: int) -> LPFPix:
        return self.fpixAddContinuedBorder(fpixs, left, right, top, bot)

    def capi_fpix_add_slope_border(self, fpixs: LPFPix, left: int, right: int,
                                   top: int, bot: int) -> LPFPix:
        return self.fpixAddSlopeBorder(fpixs, left, right, top, bot)

    def capi_fpix_rasterop(self, fpixd: LPFPix, dx: int, dy: int, dw: int,
                           dh: int, fpixs: LPFPix, sx: int, sy: int) -> int:
        return self.fpixRasterop(fpixd, dx, dy, dw, dh, fpixs, sx, sy)

    def capi_fpix_rotate_orth(self, fpixs: LPFPix, quads: int) -> LPFPix:
        return self.fpixRotateOrth(fpixs, quads)

    def capi_fpix_rotate180(self, fpixd: LPFPix, fpixs: LPFPix) -> LPFPix:
        return self.fpixRotate180(fpixd, fpixs)

    def capi_fpix_rotate90(self, fpixs: LPFPix, direction: int) -> LPFPix:
        return self.fpixRotate90(fpixs, direction)

    def capi_fpix_flip_lr(self, fpixd: LPFPix, fpixs: LPFPix) -> LPFPix:
        return self.fpixFlipLR(fpixd, fpixs)

    def capi_fpix_flip_tb(self, fpixd: LPFPix, fpixs: LPFPix) -> LPFPix:
        return self.fpixFlipTB(fpixd, fpixs)

    def capi_fpix_affine_pta(self, fpixs: LPFPix, ptad: LPPta, ptas: LPPta,
                             border: int, inval: float) -> LPFPix:
        return self.fpixAffinePta(fpixs, ptad, ptas, border, inval)

    def capi_fpix_affine(self, fpixs: LPFPix, vc: c_float_p,
                         inval: float) -> LPFPix:
        return self.fpixAffine(fpixs, vc, inval)

    def capi_fpix_projective_pta(self, fpixs: LPFPix, ptad: LPPta, ptas: LPPta,
                                 border: int, inval: float) -> LPFPix:
        return self.fpixProjectivePta(fpixs, ptad, ptas, border, inval)

    def capi_fpix_projective(self, fpixs: LPFPix, vc: c_float_p,
                             inval: float) -> LPFPix:
        return self.fpixProjective(fpixs, vc, inval)

    def capi_linear_interpolate_pixel_float(self, datas: c_float_p, w: int,
                                            h: int, x: float, y: float,
                                            inval: float,
                                            pval: c_float_p) -> int:
        return self.linearInterpolatePixelFloat(datas, w, h, x, y, inval, pval)

    def capi_fpix_threshold_to_pix(self, fpix: LPFPix, thresh: float) -> LPPix:
        return self.fpixThresholdToPix(fpix, thresh)

    def capi_pix_component_function(self, pix: LPPix, rnum: float, gnum: float,
                                    bnum: float, rdenom: float, gdenom: float,
                                    bdenom: float) -> LPFPix:
        return self.pixComponentFunction(pix, rnum, gnum, bnum, rdenom, gdenom,
                                         bdenom)

    def capi_pix_read_stream_gif(self, fp: LPFile) -> LPPix:
        return self.pixReadStreamGif(fp)

    def capi_pix_read_mem_gif(self, cdata: c_ubyte_p, size: int) -> LPPix:
        return self.pixReadMemGif(cdata, size)

    def capi_pix_write_stream_gif(self, fp: LPFile, pix: LPPix) -> int:
        return self.pixWriteStreamGif(fp, pix)

    def capi_pix_write_mem_gif(self, pdata: POINTER(c_ubyte_p),
                               psize: c_size_t_p, pix: LPPix) -> int:
        return self.pixWriteMemGif(pdata, psize, pix)

    def capi_gplot_create(self, rootname: bytes, outformat: int, title: bytes,
                          xlabel: bytes, ylabel: bytes) -> LPGPlot:
        return self.gplotCreate(rootname, outformat, title, xlabel, ylabel)

    def capi_gplot_destroy(self, pgplot: LPLPGPlot):
        self.gplotDestroy(pgplot)

    def capi_gplot_add_plot(self, gplot: LPGPlot, nax: LPNuma, nay: LPNuma,
                            plotstyle: int, plotlabel: bytes) -> int:
        return self.gplotAddPlot(gplot, nax, nay, plotstyle, plotlabel)

    def capi_gplot_set_scaling(self, gplot: LPGPlot, scaling: int) -> int:
        return self.gplotSetScaling(gplot, scaling)

    def capi_gplot_make_output_pix(self, gplot: LPGPlot) -> LPPix:
        return self.gplotMakeOutputPix(gplot)

    def capi_gplot_make_output(self, gplot: LPGPlot) -> int:
        return self.gplotMakeOutput(gplot)

    def capi_gplot_gen_command_file(self, gplot: LPGPlot) -> int:
        return self.gplotGenCommandFile(gplot)

    def capi_gplot_gen_data_files(self, gplot: LPGPlot) -> int:
        return self.gplotGenDataFiles(gplot)

    def capi_gplot_simple1(self, na: LPNuma, outformat: int, outroot: bytes,
                           title: bytes) -> int:
        return self.gplotSimple1(na, outformat, outroot, title)

    def capi_gplot_simple2(self, na1: LPNuma, na2: LPNuma, outformat: int,
                           outroot: bytes, title: bytes) -> int:
        return self.gplotSimple2(na1, na2, outformat, outroot, title)

    def capi_gplot_simplen(self, naa: LPNumaa, outformat: int, outroot: bytes,
                           title: bytes) -> int:
        return self.gplotSimpleN(naa, outformat, outroot, title)

    def capi_gplot_simple_pix1(self, na: LPNuma, title: bytes) -> LPPix:
        return self.gplotSimplePix1(na, title)

    def capi_gplot_simple_pix2(self, na1: LPNuma, na2: LPNuma,
                               title: bytes) -> LPPix:
        return self.gplotSimplePix2(na1, na2, title)

    def capi_gplot_simple_pixn(self, naa: LPNumaa, title: bytes) -> LPPix:
        return self.gplotSimplePixN(naa, title)

    def capi_gplot_simple_xy1(self, nax: LPNuma, nay: LPNuma, plotstyle: int,
                              outformat: int, outroot: bytes,
                              title: bytes) -> LPGPlot:
        return self.gplotSimpleXY1(nax, nay, plotstyle, outformat, outroot,
                                   title)

    def capi_gplot_simple_xy2(self, nax: LPNuma, nay1: LPNuma, nay2: LPNuma,
                              plotstyle: int, outformat: int, outroot: bytes,
                              title: bytes) -> LPGPlot:
        return self.gplotSimpleXY2(nax, nay1, nay2, plotstyle, outformat,
                                   outroot, title)

    def capi_gplot_simple_xyn(self, nax: LPNuma, naay: LPNumaa, plotstyle: int,
                              outformat: int, outroot: bytes,
                              title: bytes) -> LPGPlot:
        return self.gplotSimpleXYN(nax, naay, plotstyle, outformat, outroot,
                                   title)

    def capi_gplot_general_pix1(self, na: LPNuma, plotstyle: int,
                                rootname: bytes, title: bytes, xlabel: bytes,
                                ylabel: bytes) -> LPPix:
        return self.gplotGeneralPix1(na, plotstyle, rootname, title, xlabel,
                                     ylabel)

    def capi_gplot_general_pix2(self, na1: LPNuma, na2: LPNuma, plotstyle: int,
                                rootname: bytes, title: bytes, xlabel: bytes,
                                ylabel: bytes) -> LPPix:
        return self.gplotGeneralPix2(na1, na2, plotstyle, rootname, title,
                                     xlabel, ylabel)

    def capi_gplot_general_pixn(self, nax: LPNuma, naay: LPNumaa,
                                plotstyle: int, rootname: bytes, title: bytes,
                                xlabel: bytes, ylabel: bytes) -> LPPix:
        return self.gplotGeneralPixN(nax, naay, plotstyle, rootname, title,
                                     xlabel, ylabel)

    def capi_gplot_read(self, filename: bytes) -> LPGPlot:
        return self.gplotRead(filename)

    def capi_gplot_write(self, filename: bytes, gplot: LPGPlot) -> int:
        return self.gplotWrite(filename, gplot)

    def capi_generate_pta_line(self, x1: int, y1: int, x2: int,
                               y2: int) -> LPPta:
        return self.generatePtaLine(x1, y1, x2, y2)

    def capi_generate_pta_wide_line(self, x1: int, y1: int, x2: int, y2: int,
                                    width: int) -> LPPta:
        return self.generatePtaWideLine(x1, y1, x2, y2, width)

    def capi_generate_pta_box(self, box: LPBox, width: int) -> LPPta:
        return self.generatePtaBox(box, width)

    def capi_generate_pta_boxa(self, boxa: LPBoxa, width: int,
                               removedups: int) -> LPPta:
        return self.generatePtaBoxa(boxa, width, removedups)

    def capi_generate_pta_hash_box(self, box: LPBox, spacing: int, width: int,
                                   orient: int, outline: int) -> LPPta:
        return self.generatePtaHashBox(box, spacing, width, orient, outline)

    def capi_generate_pta_hash_boxa(self, boxa: LPBoxa, spacing: int,
                                    width: int, orient: int, outline: int,
                                    removedups: int) -> LPPta:
        return self.generatePtaHashBoxa(boxa, spacing, width, orient, outline,
                                        removedups)

    def capi_generate_ptaa_boxa(self, boxa: LPBoxa) -> LPPtaa:
        return self.generatePtaaBoxa(boxa)

    def capi_generate_ptaa_hash_boxa(self, boxa: LPBoxa, spacing: int,
                                     width: int, orient: int,
                                     outline: int) -> LPPtaa:
        return self.generatePtaaHashBoxa(boxa, spacing, width, orient, outline)

    def capi_generate_pta_polyline(self, ptas: LPPta, width: int,
                                   closeflag: int, removedups: int) -> LPPta:
        return self.generatePtaPolyline(ptas, width, closeflag, removedups)

    def capi_generate_pta_grid(self, w: int, h: int, nx: int, ny: int,
                               width: int) -> LPPta:
        return self.generatePtaGrid(w, h, nx, ny, width)

    def capi_convert_pta_line_to4cc(self, ptas: LPPta) -> LPPta:
        return self.convertPtaLineTo4cc(ptas)

    def capi_generate_pta_filled_circle(self, radius: int) -> LPPta:
        return self.generatePtaFilledCircle(radius)

    def capi_generate_pta_filled_square(self, side: int) -> LPPta:
        return self.generatePtaFilledSquare(side)

    def capi_generate_pta_line_from_pt(self, x: int, y: int, length: float,
                                       radang: float) -> LPPta:
        return self.generatePtaLineFromPt(x, y, length, radang)

    def capi_locate_pt_radially(self, xr: int, yr: int, dist: float,
                                radang: float, px: c_double_p,
                                py: c_double_p) -> int:
        return self.locatePtRadially(xr, yr, dist, radang, px, py)

    def capi_pix_render_plot_from_numa(self, ppix: LPLPPix, na: LPNuma,
                                       plotloc: int, linewidth: int, max: int,
                                       color: int) -> int:
        return self.pixRenderPlotFromNuma(ppix, na, plotloc, linewidth, max,
                                          color)

    def capi_make_plot_pta_from_numa(self, na: LPNuma, size: int, plotloc: int,
                                     linewidth: int, max: int) -> LPPta:
        return self.makePlotPtaFromNuma(na, size, plotloc, linewidth, max)

    def capi_pix_render_plot_from_numa_gen(self, ppix: LPLPPix, na: LPNuma,
                                           orient: int, linewidth: int,
                                           refpos: int, max: int, drawref: int,
                                           color: int) -> int:
        return self.pixRenderPlotFromNumaGen(ppix, na, orient, linewidth,
                                             refpos, max, drawref, color)

    def capi_make_plot_pta_from_numa_gen(self, na: LPNuma, orient: int,
                                         linewidth: int, refpos: int, max: int,
                                         drawref: int) -> LPPta:
        return self.makePlotPtaFromNumaGen(na, orient, linewidth, refpos, max,
                                           drawref)

    def capi_pix_render_pta(self, pix: LPPix, pta: LPPta, op: int) -> int:
        return self.pixRenderPta(pix, pta, op)

    def capi_pix_render_pta_arb(self, pix: LPPix, pta: LPPta, rval: int,
                                gval: int, bval: int) -> int:
        return self.pixRenderPtaArb(pix, pta, rval, gval, bval)

    def capi_pix_render_pta_blend(self, pix: LPPix, pta: LPPta, rval: int,
                                  gval: int, bval: int, fract: float) -> int:
        return self.pixRenderPtaBlend(pix, pta, rval, gval, bval, fract)

    def capi_pix_render_line(self, pix: LPPix, x1: int, y1: int, x2: int,
                             y2: int, width: int, op: int) -> int:
        return self.pixRenderLine(pix, x1, y1, x2, y2, width, op)

    def capi_pix_render_line_arb(self, pix: LPPix, x1: int, y1: int, x2: int,
                                 y2: int, width: int, rval: int, gval: int,
                                 bval: int) -> int:
        return self.pixRenderLineArb(pix, x1, y1, x2, y2, width, rval, gval,
                                     bval)

    def capi_pix_render_line_blend(self, pix: LPPix, x1: int, y1: int, x2: int,
                                   y2: int, width: int, rval: int, gval: int,
                                   bval: int, fract: float) -> int:
        return self.pixRenderLineBlend(pix, x1, y1, x2, y2, width, rval, gval,
                                       bval, fract)

    def capi_pix_render_box(self, pix: LPPix, box: LPBox, width: int,
                            op: int) -> int:
        return self.pixRenderBox(pix, box, width, op)

    def capi_pix_render_box_arb(self, pix: LPPix, box: LPBox, width: int,
                                rval: int, gval: int, bval: int) -> int:
        return self.pixRenderBoxArb(pix, box, width, rval, gval, bval)

    def capi_pix_render_box_blend(self, pix: LPPix, box: LPBox, width: int,
                                  rval: int, gval: int, bval: int,
                                  fract: float) -> int:
        return self.pixRenderBoxBlend(pix, box, width, rval, gval, bval, fract)

    def capi_pix_render_boxa(self, pix: LPPix, boxa: LPBoxa, width: int,
                             op: int) -> int:
        return self.pixRenderBoxa(pix, boxa, width, op)

    def capi_pix_render_boxa_arb(self, pix: LPPix, boxa: LPBoxa, width: int,
                                 rval: int, gval: int, bval: int) -> int:
        return self.pixRenderBoxaArb(pix, boxa, width, rval, gval, bval)

    def capi_pix_render_boxa_blend(self, pix: LPPix, boxa: LPBoxa, width: int,
                                   rval: int, gval: int, bval: int,
                                   fract: float, removedups: int) -> int:
        return self.pixRenderBoxaBlend(pix, boxa, width, rval, gval, bval,
                                       fract, removedups)

    def capi_pix_render_hash_box(self, pix: LPPix, box: LPBox, spacing: int,
                                 width: int, orient: int, outline: int,
                                 op: int) -> int:
        return self.pixRenderHashBox(pix, box, spacing, width, orient, outline,
                                     op)

    def capi_pix_render_hash_box_arb(self, pix: LPPix, box: LPBox,
                                     spacing: int, width: int, orient: int,
                                     outline: int, rval: int, gval: int,
                                     bval: int) -> int:
        return self.pixRenderHashBoxArb(pix, box, spacing, width, orient,
                                        outline, rval, gval, bval)

    def capi_pix_render_hash_box_blend(self, pix: LPPix, box: LPBox,
                                       spacing: int, width: int, orient: int,
                                       outline: int, rval: int, gval: int,
                                       bval: int, fract: float) -> int:
        return self.pixRenderHashBoxBlend(pix, box, spacing, width, orient,
                                          outline, rval, gval, bval, fract)

    def capi_pix_render_hash_mask_arb(self, pix: LPPix, pixm: LPPix, x: int,
                                      y: int, spacing: int, width: int,
                                      orient: int, outline: int, rval: int,
                                      gval: int, bval: int) -> int:
        return self.pixRenderHashMaskArb(pix, pixm, x, y, spacing, width,
                                         orient, outline, rval, gval, bval)

    def capi_pix_render_hash_boxa(self, pix: LPPix, boxa: LPBoxa, spacing: int,
                                  width: int, orient: int, outline: int,
                                  op: int) -> int:
        return self.pixRenderHashBoxa(pix, boxa, spacing, width, orient,
                                      outline, op)

    def capi_pix_render_hash_boxa_arb(self, pix: LPPix, boxa: LPBoxa,
                                      spacing: int, width: int, orient: int,
                                      outline: int, rval: int, gval: int,
                                      bval: int) -> int:
        return self.pixRenderHashBoxaArb(pix, boxa, spacing, width, orient,
                                         outline, rval, gval, bval)

    def capi_pix_render_hash_boxa_blend(self, pix: LPPix, boxa: LPBoxa,
                                        spacing: int, width: int, orient: int,
                                        outline: int, rval: int, gval: int,
                                        bval: int, fract: float) -> int:
        return self.pixRenderHashBoxaBlend(pix, boxa, spacing, width, orient,
                                           outline, rval, gval, bval, fract)

    def capi_pix_render_polyline(self, pix: LPPix, ptas: LPPta, width: int,
                                 op: int, closeflag: int) -> int:
        return self.pixRenderPolyline(pix, ptas, width, op, closeflag)

    def capi_pix_render_polyline_arb(self, pix: LPPix, ptas: LPPta, width: int,
                                     rval: int, gval: int, bval: int,
                                     closeflag: int) -> int:
        return self.pixRenderPolylineArb(pix, ptas, width, rval, gval, bval,
                                         closeflag)

    def capi_pix_render_polyline_blend(self, pix: LPPix, ptas: LPPta,
                                       width: int, rval: int, gval: int,
                                       bval: int, fract: float, closeflag: int,
                                       removedups: int) -> int:
        return self.pixRenderPolylineBlend(pix, ptas, width, rval, gval, bval,
                                           fract, closeflag, removedups)

    def capi_pix_render_grid_arb(self, pix: LPPix, nx: int, ny: int,
                                 width: int, rval: int, gval: int,
                                 bval: int) -> int:
        return self.pixRenderGridArb(pix, nx, ny, width, rval, gval, bval)

    def capi_pix_render_random_cmap_ptaa(self, pix: LPPix, ptaa: LPPtaa,
                                         polyflag: int, width: int,
                                         closeflag: int) -> LPPix:
        return self.pixRenderRandomCmapPtaa(pix, ptaa, polyflag, width,
                                            closeflag)

    def capi_pix_render_polygon(self, ptas: LPPta, width: int, pxmin: c_int_p,
                                pymin: c_int_p) -> LPPix:
        return self.pixRenderPolygon(ptas, width, pxmin, pymin)

    def capi_pix_fill_polygon(self, pixs: LPPix, pta: LPPta, xmin: int,
                              ymin: int) -> LPPix:
        return self.pixFillPolygon(pixs, pta, xmin, ymin)

    def capi_pix_render_contours(self, pixs: LPPix, startval: int, incr: int,
                                 outdepth: int) -> LPPix:
        return self.pixRenderContours(pixs, startval, incr, outdepth)

    def capi_fpix_auto_render_contours(self, fpix: LPFPix,
                                       ncontours: int) -> LPPix:
        return self.fpixAutoRenderContours(fpix, ncontours)

    def capi_fpix_render_contours(self, fpixs: LPFPix, incr: float,
                                  proxim: float) -> LPPix:
        return self.fpixRenderContours(fpixs, incr, proxim)

    def capi_pix_generate_pta_boundary(self, pixs: LPPix, width: int) -> LPPta:
        return self.pixGeneratePtaBoundary(pixs, width)

    def capi_pix_erode_gray(self, pixs: LPPix, hsize: int,
                            vsize: int) -> LPPix:
        return self.pixErodeGray(pixs, hsize, vsize)

    def capi_pix_dilate_gray(self, pixs: LPPix, hsize: int,
                             vsize: int) -> LPPix:
        return self.pixDilateGray(pixs, hsize, vsize)

    def capi_pix_open_gray(self, pixs: LPPix, hsize: int, vsize: int) -> LPPix:
        return self.pixOpenGray(pixs, hsize, vsize)

    def capi_pix_close_gray(self, pixs: LPPix, hsize: int,
                            vsize: int) -> LPPix:
        return self.pixCloseGray(pixs, hsize, vsize)

    def capi_pix_erode_gray3(self, pixs: LPPix, hsize: int,
                             vsize: int) -> LPPix:
        return self.pixErodeGray3(pixs, hsize, vsize)

    def capi_pix_dilate_gray3(self, pixs: LPPix, hsize: int,
                              vsize: int) -> LPPix:
        return self.pixDilateGray3(pixs, hsize, vsize)

    def capi_pix_open_gray3(self, pixs: LPPix, hsize: int,
                            vsize: int) -> LPPix:
        return self.pixOpenGray3(pixs, hsize, vsize)

    def capi_pix_close_gray3(self, pixs: LPPix, hsize: int,
                             vsize: int) -> LPPix:
        return self.pixCloseGray3(pixs, hsize, vsize)

    def capi_pix_dither_to_binary(self, pixs: LPPix) -> LPPix:
        return self.pixDitherToBinary(pixs)

    def capi_pix_dither_to_binary_spec(self, pixs: LPPix, lowerclip: int,
                                       upperclip: int) -> LPPix:
        return self.pixDitherToBinarySpec(pixs, lowerclip, upperclip)

    def capi_dither_to_binary_line_low(self, lined: c_uint_p, w: int,
                                       bufs1: c_uint_p, bufs2: c_uint_p,
                                       lowerclip: int, upperclip: int,
                                       lastlineflag: int):
        self.ditherToBinaryLineLow(
            lined, w, bufs1, bufs2, lowerclip, upperclip, lastlineflag)

    def capi_pix_threshold_to_binary(self, pixs: LPPix, thresh: int) -> LPPix:
        return self.pixThresholdToBinary(pixs, thresh)

    def capi_threshold_to_binary_line_low(self, lined: c_uint_p, w: int,
                                          lines: c_uint_p, d: int,
                                          thresh: int):
        self.thresholdToBinaryLineLow(lined, w, lines, d, thresh)

    def capi_pix_var_threshold_to_binary(self, pixs: LPPix,
                                         pixg: LPPix) -> LPPix:
        return self.pixVarThresholdToBinary(pixs, pixg)

    def capi_pix_adapt_threshold_to_binary(self, pixs: LPPix, pixm: LPPix,
                                           gamma: float) -> LPPix:
        return self.pixAdaptThresholdToBinary(pixs, pixm, gamma)

    def capi_pix_adapt_threshold_to_binary_gen(self, pixs: LPPix, pixm: LPPix,
                                               gamma: float, blackval: int,
                                               whiteval: int,
                                               thresh: int) -> LPPix:
        return self.pixAdaptThresholdToBinaryGen(pixs, pixm, gamma, blackval,
                                                 whiteval, thresh)

    def capi_pix_generate_mask_by_value(self, pixs: LPPix, val: int,
                                        usecmap: int) -> LPPix:
        return self.pixGenerateMaskByValue(pixs, val, usecmap)

    def capi_pix_generate_mask_by_band(self, pixs: LPPix, lower: int,
                                       upper: int, inband: int,
                                       usecmap: int) -> LPPix:
        return self.pixGenerateMaskByBand(pixs, lower, upper, inband, usecmap)

    def capi_pix_dither_to2bpp(self, pixs: LPPix, cmapflag: int) -> LPPix:
        return self.pixDitherTo2bpp(pixs, cmapflag)

    def capi_pix_dither_to2bpp_spec(self, pixs: LPPix, lowerclip: int,
                                    upperclip: int, cmapflag: int) -> LPPix:
        return self.pixDitherTo2bppSpec(pixs, lowerclip, upperclip, cmapflag)

    def capi_pix_threshold_to2bpp(self, pixs: LPPix, nlevels: int,
                                  cmapflag: int) -> LPPix:
        return self.pixThresholdTo2bpp(pixs, nlevels, cmapflag)

    def capi_pix_threshold_to4bpp(self, pixs: LPPix, nlevels: int,
                                  cmapflag: int) -> LPPix:
        return self.pixThresholdTo4bpp(pixs, nlevels, cmapflag)

    def capi_pix_threshold_on8bpp(self, pixs: LPPix, nlevels: int,
                                  cmapflag: int) -> LPPix:
        return self.pixThresholdOn8bpp(pixs, nlevels, cmapflag)

    def capi_pix_threshold_gray_arb(self, pixs: LPPix, edgevals: bytes,
                                    outdepth: int, use_average: int,
                                    setblack: int, setwhite: int) -> LPPix:
        return self.pixThresholdGrayArb(pixs, edgevals, outdepth, use_average,
                                        setblack, setwhite)

    def capi_make_gray_quant_index_table(self, nlevels: int) -> c_int_p:
        return self.makeGrayQuantIndexTable(nlevels)

    def capi_make_gray_quant_table_arb(self, na: LPNuma, outdepth: int,
                                       ptab: POINTER(c_int_p),
                                       pcmap: LPLPPixColormap) -> int:
        return self.makeGrayQuantTableArb(na, outdepth, ptab, pcmap)

    def capi_pix_generate_mask_by_band32(self, pixs: LPPix, refval: int,
                                         delm: int, delp: int, fractm: float,
                                         fractp: float) -> LPPix:
        return self.pixGenerateMaskByBand32(pixs, refval, delm, delp, fractm,
                                            fractp)

    def capi_pix_generate_mask_by_discr32(self, pixs: LPPix, refval1: int,
                                          refval2: int,
                                          distflag: int) -> LPPix:
        return self.pixGenerateMaskByDiscr32(pixs, refval1, refval2, distflag)

    def capi_pix_gray_quant_from_histo(self, pixd: LPPix, pixs: LPPix,
                                       pixm: LPPix, minfract: float,
                                       maxsize: int) -> LPPix:
        return self.pixGrayQuantFromHisto(pixd, pixs, pixm, minfract, maxsize)

    def capi_pix_gray_quant_from_cmap(self, pixs: LPPix, cmap: LPPixColormap,
                                      mindepth: int) -> LPPix:
        return self.pixGrayQuantFromCmap(pixs, cmap, mindepth)

    def capi_l_hmapCreate(self, ninit: int, maxocc: int) -> LPL_Hashmap:
        return self.l_hmapCreate(ninit, maxocc)

    def capi_l_hmapDestroy(self, phmap: LPLPL_Hashmap):
        self.l_hmapDestroy(phmap)

    def capi_l_hmapLookup(self, hmap: LPL_Hashmap, key: int, val: int,
                          op: int) -> LPL_Hashitem:
        return self.l_hmapLookup(hmap, key, val, op)

    def capi_l_hmapRehash(self, hmap: LPL_Hashmap) -> int:
        return self.l_hmapRehash(hmap)

    def capi_lheap_create(self, n: int, direction: int) -> LPL_Heap:
        return self.lheapCreate(n, direction)

    def capi_lheap_destroy(self, plh: LPLPL_Heap, freeflag: int):
        self.lheapDestroy(plh, freeflag)

    def capi_lheap_add(self, lh: LPL_Heap, item: c_void_p) -> int:
        return self.lheapAdd(lh, item)

    def capi_lheap_remove(self, lh: LPL_Heap) -> c_void_p:
        return self.lheapRemove(lh)

    def capi_lheap_get_count(self, lh: LPL_Heap) -> int:
        return self.lheapGetCount(lh)

    def capi_lheap_get_element(self, lh: LPL_Heap, index: int) -> c_void_p:
        return self.lheapGetElement(lh, index)

    def capi_lheap_sort(self, lh: LPL_Heap) -> int:
        return self.lheapSort(lh)

    def capi_lheap_sort_strict_order(self, lh: LPL_Heap) -> int:
        return self.lheapSortStrictOrder(lh)

    def capi_lheap_print(self, fp: LPFile, lh: LPL_Heap) -> int:
        return self.lheapPrint(fp, lh)

    def capi_jb_rank_haus_init(self, components: int, maxwidth: int,
                               maxheight: int, size: int,
                               rank: float) -> LPJbClasser:
        return self.jbRankHausInit(components, maxwidth, maxheight, size, rank)

    def capi_jb_correlation_init(self, components: int, maxwidth: int,
                                 maxheight: int, thresh: float,
                                 weightfactor: float) -> LPJbClasser:
        return self.jbCorrelationInit(components, maxwidth, maxheight, thresh,
                                      weightfactor)

    def capi_jb_correlation_init_without_components(self, components: int,
                                                    maxwidth: int,
                                                    maxheight: int,
                                                    thresh: float,
                                                    weightfactor: float
                                                    ) -> LPJbClasser:
        return self.jbCorrelationInitWithoutComponents(components, maxwidth,
                                                       maxheight, thresh,
                                                       weightfactor)

    def capi_jb_add_pages(self, classer: LPJbClasser,
                          safiles: LPSarray) -> int:
        return self.jbAddPages(classer, safiles)

    def capi_jb_add_page(self, classer: LPJbClasser, pixs: LPPix) -> int:
        return self.jbAddPage(classer, pixs)

    def capi_jb_add_page_components(self, classer: LPJbClasser, pixs: LPPix,
                                    boxas: LPBoxa, pixas: LPPixa) -> int:
        return self.jbAddPageComponents(classer, pixs, boxas, pixas)

    def capi_jb_classify_rank_haus(self, classer: LPJbClasser, boxa: LPBoxa,
                                   pixas: LPPixa) -> int:
        return self.jbClassifyRankHaus(classer, boxa, pixas)

    def capi_pix_haustest(self, pix1: LPPix, pix2: LPPix, pix3: LPPix,
                          pix4: LPPix, delx: float, dely: float, maxdiffw: int,
                          maxdiffh: int) -> int:
        return self.pixHaustest(pix1, pix2, pix3, pix4, delx, dely, maxdiffw,
                                maxdiffh)

    def capi_pix_rank_haustest(self, pix1: LPPix, pix2: LPPix, pix3: LPPix,
                               pix4: LPPix, delx: float, dely: float,
                               maxdiffw: int, maxdiffh: int, area1: int,
                               area3: int, rank: float, tab8: c_int_p) -> int:
        return self.pixRankHaustest(pix1, pix2, pix3, pix4, delx, dely,
                                    maxdiffw, maxdiffh, area1, area3, rank,
                                    tab8)

    def capi_jb_classify_correlation(self, classer: LPJbClasser, boxa: LPBoxa,
                                     pixas: LPPixa) -> int:
        return self.jbClassifyCorrelation(classer, boxa, pixas)

    def capi_jb_get_components(self, pixs: LPPix, components: int,
                               maxwidth: int, maxheight: int, pboxad: LPLPBoxa,
                               ppixad: LPLPPixa) -> int:
        return self.jbGetComponents(pixs, components, maxwidth, maxheight,
                                    pboxad, ppixad)

    def capi_pix_word_mask_by_dilation(self, pixs: LPPix, ppixm: LPLPPix,
                                       psize: c_int_p, pixadb: LPPixa) -> int:
        return self.pixWordMaskByDilation(pixs, ppixm, psize, pixadb)

    def capi_pix_word_boxes_by_dilation(self, pixs: LPPix, minwidth: int,
                                        minheight: int, maxwidth: int,
                                        maxheight: int, pboxa: LPLPBoxa,
                                        psize: c_int_p,
                                        pixadb: LPPixa) -> int:
        return self.pixWordBoxesByDilation(pixs, minwidth, minheight, maxwidth,
                                           maxheight, pboxa, psize, pixadb)

    def capi_jb_accumulate_composites(self, pixaa: LPPixaa, pna: LPLPNuma,
                                      pptat: LPLPPta) -> LPPixa:
        return self.jbAccumulateComposites(pixaa, pna, pptat)

    def capi_jb_templates_from_composites(self, pixac: LPPixa,
                                          na: LPNuma) -> LPPixa:
        return self.jbTemplatesFromComposites(pixac, na)

    def capi_jb_classer_create(self, method: int,
                               components: int) -> LPJbClasser:
        return self.jbClasserCreate(method, components)

    def capi_jb_classer_destroy(self, pclasser: LPLPJbClasser):
        self.jbClasserDestroy(pclasser)

    def capi_jb_data_save(self, classer: LPJbClasser) -> LPJbData:
        return self.jbDataSave(classer)

    def capi_jb_data_destroy(self, pdata: LPLPJbData):
        self.jbDataDestroy(pdata)

    def capi_jb_data_write(self, rootout: bytes, jbdata: LPJbData) -> int:
        return self.jbDataWrite(rootout, jbdata)

    def capi_jb_data_read(self, rootname: bytes) -> LPJbData:
        return self.jbDataRead(rootname)

    def capi_jb_data_render(self, data: LPJbData, debugflag: int) -> LPPixa:
        return self.jbDataRender(data, debugflag)

    def capi_jb_get_ul_corners(self, classer: LPJbClasser, pixs: LPPix,
                               boxa: LPBoxa) -> int:
        return self.jbGetULCorners(classer, pixs, boxa)

    def capi_jb_get_ll_corners(self, classer: LPJbClasser) -> int:
        return self.jbGetLLCorners(classer)

    def capi_read_header_jp2k(self, filename: bytes, pw: c_int_p, ph: c_int_p,
                              pbps: c_int_p, pspp: c_int_p,
                              pcodec: c_int_p) -> int:
        return self.readHeaderJp2k(filename, pw, ph, pbps, pspp, pcodec)

    def capi_fread_header_jp2k(self, fp: LPFile, pw: c_int_p, ph: c_int_p,
                               pbps: c_int_p, pspp: c_int_p,
                               pcodec: c_int_p) -> int:
        return self.freadHeaderJp2k(fp, pw, ph, pbps, pspp, pcodec)

    def capi_read_header_mem_jp2k(self, data: c_ubyte_p, size: int,
                                  pw: c_int_p, ph: c_int_p, pbps: c_int_p,
                                  pspp: c_int_p, pcodec: c_int_p) -> int:
        return self.readHeaderMemJp2k(data, size, pw, ph, pbps, pspp, pcodec)

    def capi_fget_jp2k_resolution(self, fp: LPFile, pxres: c_int_p,
                                  pyres: c_int_p) -> int:
        return self.fgetJp2kResolution(fp, pxres, pyres)

    def capi_pix_read_jp2k(self, filename: bytes, reduction: int, box: LPBox,
                           hint: int, debug: int) -> LPPix:
        return self.pixReadJp2k(filename, reduction, box, hint, debug)

    def capi_pix_read_stream_jp2k(self, fp: LPFile, reduction: int, box: LPBox,
                                  hint: int, debug: int) -> LPPix:
        return self.pixReadStreamJp2k(fp, reduction, box, hint, debug)

    def capi_pix_write_jp2k(self, filename: bytes, pix: LPPix, quality: int,
                            nlevels: int, hint: int, debug: int) -> int:
        return self.pixWriteJp2k(filename, pix, quality, nlevels, hint, debug)

    def capi_pix_write_stream_jp2k(self, fp: LPFile, pix: LPPix, quality: int,
                                   nlevels: int, codec: int, hint: int,
                                   debug: int) -> int:
        return self.pixWriteStreamJp2k(fp, pix, quality, nlevels, codec, hint,
                                       debug)

    def capi_pix_read_mem_jp2k(self, data: c_ubyte_p, size: int,
                               reduction: int, box: LPBox, hint: int,
                               debug: int) -> LPPix:
        return self.pixReadMemJp2k(data, size, reduction, box, hint, debug)

    def capi_pix_write_mem_jp2k(self, pdata: POINTER(c_ubyte_p),
                                psize: c_size_t_p, pix: LPPix, quality: int,
                                nlevels: int, hint: int, debug: int) -> int:
        return self.pixWriteMemJp2k(pdata, psize, pix, quality, nlevels, hint,
                                    debug)

    def capi_pix_read_jpeg(self, filename: bytes, cmapflag: int,
                           reduction: int, pnwarn: c_int_p,
                           hint: int) -> LPPix:
        return self.pixReadJpeg(filename, cmapflag, reduction, pnwarn, hint)

    def capi_pix_read_stream_jpeg(self, fp: LPFile, cmapflag: int,
                                  reduction: int, pnwarn: c_int_p,
                                  hint: int) -> LPPix:
        return self.pixReadStreamJpeg(fp, cmapflag, reduction, pnwarn, hint)

    def capi_read_header_jpeg(self, filename: bytes, pw: c_int_p, ph: c_int_p,
                              pspp: c_int_p, pycck: c_int_p,
                              pcmyk: c_int_p) -> int:
        return self.readHeaderJpeg(filename, pw, ph, pspp, pycck, pcmyk)

    def capi_fread_header_jpeg(self, fp: LPFile, pw: c_int_p, ph: c_int_p,
                               pspp: c_int_p, pycck: c_int_p,
                               pcmyk: c_int_p) -> int:
        return self.freadHeaderJpeg(fp, pw, ph, pspp, pycck, pcmyk)

    def capi_fget_jpeg_resolution(self, fp: LPFile, pxres: c_int_p,
                                  pyres: c_int_p) -> int:
        return self.fgetJpegResolution(fp, pxres, pyres)

    def capi_fget_jpeg_comment(self, fp: LPFile,
                               pcomment: POINTER(c_ubyte_p)) -> int:
        return self.fgetJpegComment(fp, pcomment)

    def capi_pix_write_jpeg(self, filename: bytes, pix: LPPix, quality: int,
                            progressive: int) -> int:
        return self.pixWriteJpeg(filename, pix, quality, progressive)

    def capi_pix_write_stream_jpeg(self, fp: LPFile, pixs: LPPix, quality: int,
                                   progressive: int) -> int:
        return self.pixWriteStreamJpeg(fp, pixs, quality, progressive)

    def capi_pix_read_mem_jpeg(self, data: c_ubyte_p, size: int, cmflag: int,
                               reduction: int, pnwarn: c_int_p,
                               hint: int) -> LPPix:
        return self.pixReadMemJpeg(data, size, cmflag, reduction, pnwarn, hint)

    def capi_read_header_mem_jpeg(self, data: c_ubyte_p, size: int,
                                  pw: c_int_p, ph: c_int_p, pspp: c_int_p,
                                  pycck: c_int_p, pcmyk: c_int_p) -> int:
        return self.readHeaderMemJpeg(data, size, pw, ph, pspp, pycck, pcmyk)

    def capi_read_resolution_mem_jpeg(self, data: c_ubyte_p, size: int,
                                      pxres: c_int_p, pyres: c_int_p) -> int:
        return self.readResolutionMemJpeg(data, size, pxres, pyres)

    def capi_pix_write_mem_jpeg(self, pdata: POINTER(c_ubyte_p),
                                psize: c_size_t_p, pix: LPPix, quality: int,
                                progressive: int) -> int:
        return self.pixWriteMemJpeg(pdata, psize, pix, quality, progressive)

    def capi_pix_set_chroma_sampling(self, pix: LPPix, sampling: int) -> int:
        return self.pixSetChromaSampling(pix, sampling)

    def capi_kernel_create(self, height: int, width: int) -> LPL_Kernel:
        return self.kernelCreate(height, width)

    def capi_kernel_destroy(self, pkel: LPLPL_Kernel):
        self.kernelDestroy(pkel)

    def capi_kernel_copy(self, kels: LPL_Kernel) -> LPL_Kernel:
        return self.kernelCopy(kels)

    def capi_kernel_get_element(self, kel: LPL_Kernel, row: int, col: int,
                                pval: c_float_p) -> int:
        return self.kernelGetElement(kel, row, col, pval)

    def capi_kernel_set_element(self, kel: LPL_Kernel, row: int, col: int,
                                val: float) -> int:
        return self.kernelSetElement(kel, row, col, val)

    def capi_kernel_get_parameters(self, kel: LPL_Kernel, psy: c_int_p,
                                   psx: c_int_p, pcy: c_int_p,
                                   pcx: c_int_p) -> int:
        return self.kernelGetParameters(kel, psy, psx, pcy, pcx)

    def capi_kernel_set_origin(self, kel: LPL_Kernel, cy: int, cx: int) -> int:
        return self.kernelSetOrigin(kel, cy, cx)

    def capi_kernel_get_sum(self, kel: LPL_Kernel, psum: c_float_p) -> int:
        return self.kernelGetSum(kel, psum)

    def capi_kernel_get_min_max(self, kel: LPL_Kernel, pmin: c_float_p,
                                pmax: c_float_p) -> int:
        return self.kernelGetMinMax(kel, pmin, pmax)

    def capi_kernel_normalize(self, kels: LPL_Kernel,
                              normsum: float) -> LPL_Kernel:
        return self.kernelNormalize(kels, normsum)

    def capi_kernel_invert(self, kels: LPL_Kernel) -> LPL_Kernel:
        return self.kernelInvert(kels)

    def capi_create2d_float_array(self, sy: int,
                                  sx: int) -> POINTER(c_float_p):
        return self.create2dFloatArray(sy, sx)

    def capi_kernel_read(self, fname: bytes) -> LPL_Kernel:
        return self.kernelRead(fname)

    def capi_kernel_read_stream(self, fp: LPFile) -> LPL_Kernel:
        return self.kernelReadStream(fp)

    def capi_kernel_write(self, fname: bytes, kel: LPL_Kernel) -> int:
        return self.kernelWrite(fname, kel)

    def capi_kernel_write_stream(self, fp: LPFile, kel: LPL_Kernel) -> int:
        return self.kernelWriteStream(fp, kel)

    def capi_kernel_create_from_string(self, h: int, w: int, cy: int, cx: int,
                                       kdata: bytes) -> LPL_Kernel:
        return self.kernelCreateFromString(h, w, cy, cx, kdata)

    def capi_kernel_create_from_file(self, filename: bytes) -> LPL_Kernel:
        return self.kernelCreateFromFile(filename)

    def capi_kernel_create_from_pix(self, pix: LPPix, cy: int,
                                    cx: int) -> LPL_Kernel:
        return self.kernelCreateFromPix(pix, cy, cx)

    def capi_kernel_display_in_pix(self, kel: LPL_Kernel, size: int,
                                   gthick: int) -> LPPix:
        return self.kernelDisplayInPix(kel, size, gthick)

    def capi_parse_string_for_numbers(self, str: bytes, seps: bytes) -> LPNuma:
        return self.parseStringForNumbers(str, seps)

    def capi_make_flat_kernel(self, height: int, width: int, cy: int,
                              cx: int) -> LPL_Kernel:
        return self.makeFlatKernel(height, width, cy, cx)

    def capi_make_gaussian_kernel(self, halfh: int, halfw: int, stdev: float,
                                  max: float) -> LPL_Kernel:
        return self.makeGaussianKernel(halfh, halfw, stdev, max)

    def capi_make_gaussian_kernel_sep(self, halfh: int, halfw: int,
                                      stdev: float, max: float,
                                      pkelx: LPLPL_Kernel,
                                      pkely: LPLPL_Kernel) -> int:
        return self.makeGaussianKernelSep(halfh, halfw, stdev, max, pkelx,
                                          pkely)

    def capi_make_do_gkernel(self, halfh: int, halfw: int, stdev: float,
                             ratio: float) -> LPL_Kernel:
        return self.makeDoGKernel(halfh, halfw, stdev, ratio)

    def capi_get_imagelib_versions(self) -> LP_c_char:
        return self.getImagelibVersions()

    def capi_list_destroy(self, phead: LPLPDoubleLinkedList):
        self.listDestroy(phead)

    def capi_list_add_to_head(self, phead: LPLPDoubleLinkedList,
                              data: c_void_p) -> int:
        return self.listAddToHead(phead, data)

    def capi_list_add_to_tail(self, phead: LPLPDoubleLinkedList,
                              ptail: LPLPDoubleLinkedList,
                              data: c_void_p) -> int:
        return self.listAddToTail(phead, ptail, data)

    def capi_list_insert_before(self, phead: LPLPDoubleLinkedList,
                                elem: LPDoubleLinkedList,
                                data: c_void_p) -> int:
        return self.listInsertBefore(phead, elem, data)

    def capi_list_insert_after(self, phead: LPLPDoubleLinkedList,
                               elem: LPDoubleLinkedList,
                               data: c_void_p) -> int:
        return self.listInsertAfter(phead, elem, data)

    def capi_list_remove_element(self, phead: LPLPDoubleLinkedList,
                                 elem: LPDoubleLinkedList) -> c_void_p:
        return self.listRemoveElement(phead, elem)

    def capi_list_remove_from_head(self,
                                   phead: LPLPDoubleLinkedList) -> c_void_p:
        return self.listRemoveFromHead(phead)

    def capi_list_remove_from_tail(self, phead: LPLPDoubleLinkedList,
                                   ptail: LPLPDoubleLinkedList) -> c_void_p:
        return self.listRemoveFromTail(phead, ptail)

    def capi_list_find_element(self, head: LPDoubleLinkedList,
                               data: c_void_p) -> LPDoubleLinkedList:
        return self.listFindElement(head, data)

    def capi_list_find_tail(self,
                            head: LPDoubleLinkedList) -> LPDoubleLinkedList:
        return self.listFindTail(head)

    def capi_list_get_count(self, head: LPDoubleLinkedList) -> int:
        return self.listGetCount(head)

    def capi_list_reverse(self, phead: LPLPDoubleLinkedList) -> int:
        return self.listReverse(phead)

    def capi_list_join(self, phead1: LPLPDoubleLinkedList,
                       phead2: LPLPDoubleLinkedList) -> int:
        return self.listJoin(phead1, phead2)

    def capi_l_amapCreate(self, keytype: int) -> LPL_Rbtree:
        return self.l_amapCreate(keytype)

    def capi_l_amapFind(self, m: LPL_Rbtree, key: Rb_Type) -> LPRb_Type:
        return self.l_amapFind(m, key)

    def capi_l_amapInsert(self, m: LPL_Rbtree, key: Rb_Type, value: Rb_Type):
        self.l_amapInsert(m, key, value)

    def capi_l_amapDelete(self, m: LPL_Rbtree, key: Rb_Type):
        self.l_amapDelete(m, key)

    def capi_l_amapDestroy(self, pm: LPLPL_Rbtree):
        self.l_amapDestroy(pm)

    def capi_l_amapGetFirst(self, m: LPL_Rbtree) -> LPL_Rbtree_Node:
        return self.l_amapGetFirst(m)

    def capi_l_amapGetNext(self, n: LPL_Rbtree_Node) -> LPL_Rbtree_Node:
        return self.l_amapGetNext(n)

    def capi_l_amapGetLast(self, m: LPL_Rbtree) -> LPL_Rbtree_Node:
        return self.l_amapGetLast(m)

    def capi_l_amapGetPrev(self, n: LPL_Rbtree_Node) -> LPL_Rbtree_Node:
        return self.l_amapGetPrev(n)

    def capi_l_amapSize(self, m: LPL_Rbtree) -> int:
        return self.l_amapSize(m)

    def capi_l_asetCreate(self, keytype: int) -> LPL_Rbtree:
        return self.l_asetCreate(keytype)

    def capi_l_asetFind(self, s: LPL_Rbtree, key: Rb_Type) -> LPRb_Type:
        return self.l_asetFind(s, key)

    def capi_l_asetInsert(self, s: LPL_Rbtree, key: Rb_Type):
        self.l_asetInsert(s, key)

    def capi_l_asetDelete(self, s: LPL_Rbtree, key: Rb_Type):
        self.l_asetDelete(s, key)

    def capi_l_asetDestroy(self, ps: LPLPL_Rbtree):
        self.l_asetDestroy(ps)

    def capi_l_asetGetFirst(self, s: LPL_Rbtree) -> LPL_Rbtree_Node:
        return self.l_asetGetFirst(s)

    def capi_l_asetGetNext(self, n: LPL_Rbtree_Node) -> LPL_Rbtree_Node:
        return self.l_asetGetNext(n)

    def capi_l_asetGetLast(self, s: LPL_Rbtree) -> LPL_Rbtree_Node:
        return self.l_asetGetLast(s)

    def capi_l_asetGetPrev(self, n: LPL_Rbtree_Node) -> LPL_Rbtree_Node:
        return self.l_asetGetPrev(n)

    def capi_l_asetSize(self, s: LPL_Rbtree) -> int:
        return self.l_asetSize(s)

    def capi_generate_binary_maze(self, w: int, h: int, xi: int, yi: int,
                                  wallps: float, ranis: float) -> LPPix:
        return self.generateBinaryMaze(w, h, xi, yi, wallps, ranis)

    def capi_pix_search_binary_maze(self, pixs: LPPix, xi: int, yi: int,
                                    xf: int, yf: int,
                                    ppixd: LPLPPix) -> LPPta:
        return self.pixSearchBinaryMaze(pixs, xi, yi, xf, yf, ppixd)

    def capi_pix_search_gray_maze(self, pixs: LPPix, xi: int, yi: int, xf: int,
                                  yf: int, ppixd: LPLPPix) -> LPPta:
        return self.pixSearchGrayMaze(pixs, xi, yi, xf, yf, ppixd)

    def capi_pix_dilate(self, pixd: LPPix, pixs: LPPix, sel: LPSel) -> LPPix:
        return self.pixDilate(pixd, pixs, sel)

    def capi_pix_erode(self, pixd: LPPix, pixs: LPPix, sel: LPSel) -> LPPix:
        return self.pixErode(pixd, pixs, sel)

    def capi_pix_hmt(self, pixd: LPPix, pixs: LPPix, sel: LPSel) -> LPPix:
        return self.pixHMT(pixd, pixs, sel)

    def capi_pix_open(self, pixd: LPPix, pixs: LPPix, sel: LPSel) -> LPPix:
        return self.pixOpen(pixd, pixs, sel)

    def capi_pix_close(self, pixd: LPPix, pixs: LPPix, sel: LPSel) -> LPPix:
        return self.pixClose(pixd, pixs, sel)

    def capi_pix_close_safe(self, pixd: LPPix, pixs: LPPix,
                            sel: LPSel) -> LPPix:
        return self.pixCloseSafe(pixd, pixs, sel)

    def capi_pix_open_generalized(self, pixd: LPPix, pixs: LPPix,
                                  sel: LPSel) -> LPPix:
        return self.pixOpenGeneralized(pixd, pixs, sel)

    def capi_pix_close_generalized(self, pixd: LPPix, pixs: LPPix,
                                   sel: LPSel) -> LPPix:
        return self.pixCloseGeneralized(pixd, pixs, sel)

    def capi_pix_dilate_brick(self, pixd: LPPix, pixs: LPPix, hsize: int,
                              vsize: int) -> LPPix:
        return self.pixDilateBrick(pixd, pixs, hsize, vsize)

    def capi_pix_erode_brick(self, pixd: LPPix, pixs: LPPix, hsize: int,
                             vsize: int) -> LPPix:
        return self.pixErodeBrick(pixd, pixs, hsize, vsize)

    def capi_pix_open_brick(self, pixd: LPPix, pixs: LPPix, hsize: int,
                            vsize: int) -> LPPix:
        return self.pixOpenBrick(pixd, pixs, hsize, vsize)

    def capi_pix_close_brick(self, pixd: LPPix, pixs: LPPix, hsize: int,
                             vsize: int) -> LPPix:
        return self.pixCloseBrick(pixd, pixs, hsize, vsize)

    def capi_pix_close_safe_brick(self, pixd: LPPix, pixs: LPPix, hsize: int,
                                  vsize: int) -> LPPix:
        return self.pixCloseSafeBrick(pixd, pixs, hsize, vsize)

    def capi_select_composable_sels(self, size: int, direction: int,
                                    psel1: LPLPSel, psel2: LPLPSel) -> int:
        return self.selectComposableSels(size, direction, psel1, psel2)

    def capi_select_composable_sizes(self, size: int, pfactor1: c_int_p,
                                     pfactor2: c_int_p) -> int:
        return self.selectComposableSizes(size, pfactor1, pfactor2)

    def capi_pix_dilate_comp_brick(self, pixd: LPPix, pixs: LPPix, hsize: int,
                                   vsize: int) -> LPPix:
        return self.pixDilateCompBrick(pixd, pixs, hsize, vsize)

    def capi_pix_erode_comp_brick(self, pixd: LPPix, pixs: LPPix, hsize: int,
                                  vsize: int) -> LPPix:
        return self.pixErodeCompBrick(pixd, pixs, hsize, vsize)

    def capi_pix_open_comp_brick(self, pixd: LPPix, pixs: LPPix, hsize: int,
                                 vsize: int) -> LPPix:
        return self.pixOpenCompBrick(pixd, pixs, hsize, vsize)

    def capi_pix_close_comp_brick(self, pixd: LPPix, pixs: LPPix, hsize: int,
                                  vsize: int) -> LPPix:
        return self.pixCloseCompBrick(pixd, pixs, hsize, vsize)

    def capi_pix_close_safe_comp_brick(self, pixd: LPPix, pixs: LPPix,
                                       hsize: int, vsize: int) -> LPPix:
        return self.pixCloseSafeCompBrick(pixd, pixs, hsize, vsize)

    def capi_reset_morph_boundary_condition(self, bc: int):
        self.resetMorphBoundaryCondition(bc)

    def capi_get_morph_border_pixel_color(self, type: int, depth: int) -> int:
        return self.getMorphBorderPixelColor(type, depth)

    def capi_pix_extract_boundary(self, pixs: LPPix, type: int) -> LPPix:
        return self.pixExtractBoundary(pixs, type)

    def capi_pix_morph_sequence_masked(self, pixs: LPPix, pixm: LPPix,
                                       sequence: bytes,
                                       dispsep: int) -> LPPix:
        return self.pixMorphSequenceMasked(pixs, pixm, sequence, dispsep)

    def capi_pix_morph_sequence_by_component(self, pixs: LPPix,
                                             sequence: bytes,
                                             connectivity: int, minw: int,
                                             minh: int,
                                             pboxa: LPLPBoxa) -> LPPix:
        return self.pixMorphSequenceByComponent(pixs, sequence, connectivity,
                                                minw, minh, pboxa)

    def capi_pixa_morph_sequence_by_component(self, pixas: LPPixa,
                                              sequence: bytes, minw: int,
                                              minh: int) -> LPPixa:
        return self.pixaMorphSequenceByComponent(pixas, sequence, minw, minh)

    def capi_pix_morph_sequence_by_region(self, pixs: LPPix, pixm: LPPix,
                                          sequence: bytes, connectivity: int,
                                          minw: int, minh: int,
                                          pboxa: LPLPBoxa) -> LPPix:
        return self.pixMorphSequenceByRegion(pixs, pixm, sequence,
                                             connectivity, minw, minh, pboxa)

    def capi_pixa_morph_sequence_by_region(self, pixs: LPPix, pixam: LPPixa,
                                           sequence: bytes, minw: int,
                                           minh: int) -> LPPixa:
        return self.pixaMorphSequenceByRegion(pixs, pixam, sequence, minw,
                                              minh)

    def capi_pix_union_of_morph_ops(self, pixs: LPPix, sela: LPSela,
                                    type: int) -> LPPix:
        return self.pixUnionOfMorphOps(pixs, sela, type)

    def capi_pix_intersection_of_morph_ops(self, pixs: LPPix, sela: LPSela,
                                           type: int) -> LPPix:
        return self.pixIntersectionOfMorphOps(pixs, sela, type)

    def capi_pix_selective_conn_comp_fill(self, pixs: LPPix, connectivity: int,
                                          minw: int, minh: int) -> LPPix:
        return self.pixSelectiveConnCompFill(pixs, connectivity, minw, minh)

    def capi_pix_remove_matched_pattern(self, pixs: LPPix, pixp: LPPix,
                                        pixe: LPPix, x0: int, y0: int,
                                        dsize: int) -> int:
        return self.pixRemoveMatchedPattern(pixs, pixp, pixe, x0, y0, dsize)

    def capi_pix_display_matched_pattern(self, pixs: LPPix, pixp: LPPix,
                                         pixe: LPPix, x0: int, y0: int,
                                         color: int, scale: float,
                                         nlevels: int) -> LPPix:
        return self.pixDisplayMatchedPattern(pixs, pixp, pixe, x0, y0, color,
                                             scale, nlevels)

    def capi_pixa_extend_by_morph(self, pixas: LPPixa, type: int, niters: int,
                                  sel: LPSel, include: int) -> LPPixa:
        return self.pixaExtendByMorph(pixas, type, niters, sel, include)

    def capi_pixa_extend_by_scaling(self, pixas: LPPixa, nasc: LPNuma,
                                    type: int, include: int) -> LPPixa:
        return self.pixaExtendByScaling(pixas, nasc, type, include)

    def capi_pix_seedfill_morph(self, pixs: LPPix, pixm: LPPix, maxiters: int,
                                connectivity: int) -> LPPix:
        return self.pixSeedfillMorph(pixs, pixm, maxiters, connectivity)

    def capi_pix_run_histogram_morph(self, pixs: LPPix, runtype: int,
                                     direction: int, maxsize: int) -> LPNuma:
        return self.pixRunHistogramMorph(pixs, runtype, direction, maxsize)

    def capi_pix_tophat(self, pixs: LPPix, hsize: int, vsize: int,
                        type: int) -> LPPix:
        return self.pixTophat(pixs, hsize, vsize, type)

    def capi_pix_hdome(self, pixs: LPPix, height: int,
                       connectivity: int) -> LPPix:
        return self.pixHDome(pixs, height, connectivity)

    def capi_pix_fast_tophat(self, pixs: LPPix, xsize: int, ysize: int,
                             type: int) -> LPPix:
        return self.pixFastTophat(pixs, xsize, ysize, type)

    def capi_pix_morph_gradient(self, pixs: LPPix, hsize: int, vsize: int,
                                smoothing: int) -> LPPix:
        return self.pixMorphGradient(pixs, hsize, vsize, smoothing)

    def capi_pixa_centroids(self, pixa: LPPixa) -> LPPta:
        return self.pixaCentroids(pixa)

    def capi_pix_centroid(self, pix: LPPix, centtab: c_int_p, sumtab: c_int_p,
                          pxave: c_float_p, pyave: c_float_p) -> int:
        return self.pixCentroid(pix, centtab, sumtab, pxave, pyave)

    def capi_pix_dilate_brick_dwa(self, pixd: LPPix, pixs: LPPix, hsize: int,
                                  vsize: int) -> LPPix:
        return self.pixDilateBrickDwa(pixd, pixs, hsize, vsize)

    def capi_pix_erode_brick_dwa(self, pixd: LPPix, pixs: LPPix, hsize: int,
                                 vsize: int) -> LPPix:
        return self.pixErodeBrickDwa(pixd, pixs, hsize, vsize)

    def capi_pix_open_brick_dwa(self, pixd: LPPix, pixs: LPPix, hsize: int,
                                vsize: int) -> LPPix:
        return self.pixOpenBrickDwa(pixd, pixs, hsize, vsize)

    def capi_pix_close_brick_dwa(self, pixd: LPPix, pixs: LPPix, hsize: int,
                                 vsize: int) -> LPPix:
        return self.pixCloseBrickDwa(pixd, pixs, hsize, vsize)

    def capi_pix_dilate_comp_brick_dwa(self, pixd: LPPix, pixs: LPPix,
                                       hsize: int, vsize: int) -> LPPix:
        return self.pixDilateCompBrickDwa(pixd, pixs, hsize, vsize)

    def capi_pix_erode_comp_brick_dwa(self, pixd: LPPix, pixs: LPPix,
                                      hsize: int, vsize: int) -> LPPix:
        return self.pixErodeCompBrickDwa(pixd, pixs, hsize, vsize)

    def capi_pix_open_comp_brick_dwa(self, pixd: LPPix, pixs: LPPix,
                                     hsize: int, vsize: int) -> LPPix:
        return self.pixOpenCompBrickDwa(pixd, pixs, hsize, vsize)

    def capi_pix_close_comp_brick_dwa(self, pixd: LPPix, pixs: LPPix,
                                      hsize: int, vsize: int) -> LPPix:
        return self.pixCloseCompBrickDwa(pixd, pixs, hsize, vsize)

    def capi_pix_dilate_comp_brick_extend_dwa(self, pixd: LPPix, pixs: LPPix,
                                              hsize: int,
                                              vsize: int) -> LPPix:
        return self.pixDilateCompBrickExtendDwa(pixd, pixs, hsize, vsize)

    def capi_pix_erode_comp_brick_extend_dwa(self, pixd: LPPix, pixs: LPPix,
                                             hsize: int, vsize: int) -> LPPix:
        return self.pixErodeCompBrickExtendDwa(pixd, pixs, hsize, vsize)

    def capi_pix_open_comp_brick_extend_dwa(self, pixd: LPPix, pixs: LPPix,
                                            hsize: int, vsize: int) -> LPPix:
        return self.pixOpenCompBrickExtendDwa(pixd, pixs, hsize, vsize)

    def capi_pix_close_comp_brick_extend_dwa(self, pixd: LPPix, pixs: LPPix,
                                             hsize: int, vsize: int) -> LPPix:
        return self.pixCloseCompBrickExtendDwa(pixd, pixs, hsize, vsize)

    def capi_get_extended_composite_parameters(self, size: int, pn: c_int_p,
                                               pextra: c_int_p,
                                               pactualsize: c_int_p) -> int:
        return self.getExtendedCompositeParameters(size, pn, pextra,
                                                   pactualsize)

    def capi_pix_morph_sequence(self, pixs: LPPix, sequence: bytes,
                                dispsep: int) -> LPPix:
        return self.pixMorphSequence(pixs, sequence, dispsep)

    def capi_pix_morph_comp_sequence(self, pixs: LPPix, sequence: bytes,
                                     dispsep: int) -> LPPix:
        return self.pixMorphCompSequence(pixs, sequence, dispsep)

    def capi_pix_morph_sequence_dwa(self, pixs: LPPix, sequence: bytes,
                                    dispsep: int) -> LPPix:
        return self.pixMorphSequenceDwa(pixs, sequence, dispsep)

    def capi_pix_morph_comp_sequence_dwa(self, pixs: LPPix, sequence: bytes,
                                         dispsep: int) -> LPPix:
        return self.pixMorphCompSequenceDwa(pixs, sequence, dispsep)

    def capi_morph_sequence_verify(self, sa: LPSarray) -> int:
        return self.morphSequenceVerify(sa)

    def capi_pix_gray_morph_sequence(self, pixs: LPPix, sequence: bytes,
                                     dispsep: int, dispy: int) -> LPPix:
        return self.pixGrayMorphSequence(pixs, sequence, dispsep, dispy)

    def capi_pix_color_morph_sequence(self, pixs: LPPix, sequence: bytes,
                                      dispsep: int, dispy: int) -> LPPix:
        return self.pixColorMorphSequence(pixs, sequence, dispsep, dispy)

    def capi_numa_create(self, n: int) -> LPNuma:
        return self.numaCreate(n)

    def capi_numa_create_from_iarray(self, iarray: c_int_p,
                                     size: int) -> LPNuma:
        return self.numaCreateFromIArray(iarray, size)

    def capi_numa_create_from_farray(self, farray: c_float_p, size: int,
                                     copyflag: int) -> LPNuma:
        return self.numaCreateFromFArray(farray, size, copyflag)

    def capi_numa_create_from_string(self, str: bytes) -> LPNuma:
        return self.numaCreateFromString(str)

    def capi_numa_destroy(self, pna: LPLPNuma):
        self.numaDestroy(pna)

    def capi_numa_copy(self, na: LPNuma) -> LPNuma:
        return self.numaCopy(na)

    def capi_numa_clone(self, na: LPNuma) -> LPNuma:
        return self.numaClone(na)

    def capi_numa_empty(self, na: LPNuma) -> int:
        return self.numaEmpty(na)

    def capi_numa_add_number(self, na: LPNuma, val: float) -> int:
        return self.numaAddNumber(na, val)

    def capi_numa_insert_number(self, na: LPNuma, index: int,
                                val: float) -> int:
        return self.numaInsertNumber(na, index, val)

    def capi_numa_remove_number(self, na: LPNuma, index: int) -> int:
        return self.numaRemoveNumber(na, index)

    def capi_numa_replace_number(self, na: LPNuma, index: int,
                                 val: float) -> int:
        return self.numaReplaceNumber(na, index, val)

    def capi_numa_get_count(self, na: LPNuma) -> int:
        return self.numaGetCount(na)

    def capi_numa_set_count(self, na: LPNuma, newcount: int) -> int:
        return self.numaSetCount(na, newcount)

    def capi_numa_get_fvalue(self, na: LPNuma, index: int,
                             pval: c_float_p) -> int:
        return self.numaGetFValue(na, index, pval)

    def capi_numa_get_ivalue(self, na: LPNuma, index: int,
                             pival: c_int_p) -> int:
        return self.numaGetIValue(na, index, pival)

    def capi_numa_set_value(self, na: LPNuma, index: int, val: float) -> int:
        return self.numaSetValue(na, index, val)

    def capi_numa_shift_value(self, na: LPNuma, index: int,
                              diff: float) -> int:
        return self.numaShiftValue(na, index, diff)

    def capi_numa_get_iarray(self, na: LPNuma) -> c_int_p:
        return self.numaGetIArray(na)

    def capi_numa_get_farray(self, na: LPNuma, copyflag: int) -> c_float_p:
        return self.numaGetFArray(na, copyflag)

    def capi_numa_get_refcount(self, na: LPNuma) -> int:
        return self.numaGetRefcount(na)

    def capi_numa_change_refcount(self, na: LPNuma, delta: int) -> int:
        return self.numaChangeRefcount(na, delta)

    def capi_numa_get_parameters(self, na: LPNuma, pstartx: c_float_p,
                                 pdelx: c_float_p) -> int:
        return self.numaGetParameters(na, pstartx, pdelx)

    def capi_numa_set_parameters(self, na: LPNuma, startx: float,
                                 delx: float) -> int:
        return self.numaSetParameters(na, startx, delx)

    def capi_numa_copy_parameters(self, nad: LPNuma, nas: LPNuma) -> int:
        return self.numaCopyParameters(nad, nas)

    def capi_numa_convert_to_sarray(self, na: LPNuma, size1: int, size2: int,
                                    addzeros: int, type: int) -> LPSarray:
        return self.numaConvertToSarray(na, size1, size2, addzeros, type)

    def capi_numa_read(self, filename: bytes) -> LPNuma:
        return self.numaRead(filename)

    def capi_numa_read_stream(self, fp: LPFile) -> LPNuma:
        return self.numaReadStream(fp)

    def capi_numa_read_mem(self, data: c_ubyte_p, size: int) -> LPNuma:
        return self.numaReadMem(data, size)

    def capi_numa_write_debug(self, filename: bytes, na: LPNuma) -> int:
        return self.numaWriteDebug(filename, na)

    def capi_numa_write(self, filename: bytes, na: LPNuma) -> int:
        return self.numaWrite(filename, na)

    def capi_numa_write_stream(self, fp: LPFile, na: LPNuma) -> int:
        return self.numaWriteStream(fp, na)

    def capi_numa_write_stderr(self, na: LPNuma) -> int:
        return self.numaWriteStderr(na)

    def capi_numa_write_mem(self, pdata: POINTER(c_ubyte_p), psize: c_size_t_p,
                            na: LPNuma) -> int:
        return self.numaWriteMem(pdata, psize, na)

    def capi_numaa_create(self, n: int) -> LPNumaa:
        return self.numaaCreate(n)

    def capi_numaa_create_full(self, nptr: int, n: int) -> LPNumaa:
        return self.numaaCreateFull(nptr, n)

    def capi_numaa_truncate(self, naa: LPNumaa) -> int:
        return self.numaaTruncate(naa)

    def capi_numaa_destroy(self, pnaa: LPLPNumaa):
        self.numaaDestroy(pnaa)

    def capi_numaa_add_numa(self, naa: LPNumaa, na: LPNuma,
                            copyflag: int) -> int:
        return self.numaaAddNuma(naa, na, copyflag)

    def capi_numaa_get_count(self, naa: LPNumaa) -> int:
        return self.numaaGetCount(naa)

    def capi_numaa_get_numa_count(self, naa: LPNumaa, index: int) -> int:
        return self.numaaGetNumaCount(naa, index)

    def capi_numaa_get_number_count(self, naa: LPNumaa) -> int:
        return self.numaaGetNumberCount(naa)

    def capi_numaa_get_ptr_array(self, naa: LPNumaa) -> LPLPNuma:
        return self.numaaGetPtrArray(naa)

    def capi_numaa_get_numa(self, naa: LPNumaa, index: int,
                            accessflag: int) -> LPNuma:
        return self.numaaGetNuma(naa, index, accessflag)

    def capi_numaa_replace_numa(self, naa: LPNumaa, index: int,
                                na: LPNuma) -> int:
        return self.numaaReplaceNuma(naa, index, na)

    def capi_numaa_get_value(self, naa: LPNumaa, i: int, j: int,
                             pfval: c_float_p, pival: c_int_p) -> int:
        return self.numaaGetValue(naa, i, j, pfval, pival)

    def capi_numaa_add_number(self, naa: LPNumaa, index: int,
                              val: float) -> int:
        return self.numaaAddNumber(naa, index, val)

    def capi_numaa_read(self, filename: bytes) -> LPNumaa:
        return self.numaaRead(filename)

    def capi_numaa_read_stream(self, fp: LPFile) -> LPNumaa:
        return self.numaaReadStream(fp)

    def capi_numaa_read_mem(self, data: c_ubyte_p, size: int) -> LPNumaa:
        return self.numaaReadMem(data, size)

    def capi_numaa_write(self, filename: bytes, naa: LPNumaa) -> int:
        return self.numaaWrite(filename, naa)

    def capi_numaa_write_stream(self, fp: LPFile, naa: LPNumaa) -> int:
        return self.numaaWriteStream(fp, naa)

    def capi_numaa_write_mem(self, pdata: POINTER(c_ubyte_p),
                             psize: c_size_t_p, naa: LPNumaa) -> int:
        return self.numaaWriteMem(pdata, psize, naa)

    def capi_numa_arith_op(self, nad: LPNuma, na1: LPNuma, na2: LPNuma,
                           op: int) -> LPNuma:
        return self.numaArithOp(nad, na1, na2, op)

    def capi_numa_logical_op(self, nad: LPNuma, na1: LPNuma, na2: LPNuma,
                             op: int) -> LPNuma:
        return self.numaLogicalOp(nad, na1, na2, op)

    def capi_numa_invert(self, nad: LPNuma, nas: LPNuma) -> LPNuma:
        return self.numaInvert(nad, nas)

    def capi_numa_similar(self, na1: LPNuma, na2: LPNuma, maxdiff: float,
                          psimilar: c_int_p) -> int:
        return self.numaSimilar(na1, na2, maxdiff, psimilar)

    def capi_numa_add_to_number(self, na: LPNuma, index: int,
                                val: float) -> int:
        return self.numaAddToNumber(na, index, val)

    def capi_numa_get_min(self, na: LPNuma, pminval: c_float_p,
                          piminloc: c_int_p) -> int:
        return self.numaGetMin(na, pminval, piminloc)

    def capi_numa_get_max(self, na: LPNuma, pmaxval: c_float_p,
                          pimaxloc: c_int_p) -> int:
        return self.numaGetMax(na, pmaxval, pimaxloc)

    def capi_numa_get_sum(self, na: LPNuma, psum: c_float_p) -> int:
        return self.numaGetSum(na, psum)

    def capi_numa_get_partial_sums(self, na: LPNuma) -> LPNuma:
        return self.numaGetPartialSums(na)

    def capi_numa_get_sum_on_interval(self, na: LPNuma, first: int, last: int,
                                      psum: c_float_p) -> int:
        return self.numaGetSumOnInterval(na, first, last, psum)

    def capi_numa_has_only_integers(self, na: LPNuma,
                                    pallints: c_int_p) -> int:
        return self.numaHasOnlyIntegers(na, pallints)

    def capi_numa_get_mean(self, na: LPNuma, pave: c_float_p) -> int:
        return self.numaGetMean(na, pave)

    def capi_numa_get_mean_absval(self, na: LPNuma, paveabs: c_float_p) -> int:
        return self.numaGetMeanAbsval(na, paveabs)

    def capi_numa_subsample(self, nas: LPNuma, subfactor: int) -> LPNuma:
        return self.numaSubsample(nas, subfactor)

    def capi_numa_make_delta(self, nas: LPNuma) -> LPNuma:
        return self.numaMakeDelta(nas)

    def capi_numa_make_sequence(self, startval: float, increment: float,
                                size: int) -> LPNuma:
        return self.numaMakeSequence(startval, increment, size)

    def capi_numa_make_constant(self, val: float, size: int) -> LPNuma:
        return self.numaMakeConstant(val, size)

    def capi_numa_make_absval(self, nad: LPNuma, nas: LPNuma) -> LPNuma:
        return self.numaMakeAbsval(nad, nas)

    def capi_numa_add_border(self, nas: LPNuma, left: int, right: int,
                             val: float) -> LPNuma:
        return self.numaAddBorder(nas, left, right, val)

    def capi_numa_add_specified_border(self, nas: LPNuma, left: int,
                                       right: int, type: int) -> LPNuma:
        return self.numaAddSpecifiedBorder(nas, left, right, type)

    def capi_numa_remove_border(self, nas: LPNuma, left: int,
                                right: int) -> LPNuma:
        return self.numaRemoveBorder(nas, left, right)

    def capi_numa_count_nonzero_runs(self, na: LPNuma, pcount: c_int_p) -> int:
        return self.numaCountNonzeroRuns(na, pcount)

    def capi_numa_get_nonzero_range(self, na: LPNuma, eps: float,
                                    pfirst: c_int_p, plast: c_int_p) -> int:
        return self.numaGetNonzeroRange(na, eps, pfirst, plast)

    def capi_numa_get_count_relative_to_zero(self, na: LPNuma, type: int,
                                             pcount: c_int_p) -> int:
        return self.numaGetCountRelativeToZero(na, type, pcount)

    def capi_numa_clip_to_interval(self, nas: LPNuma, first: int,
                                   last: int) -> LPNuma:
        return self.numaClipToInterval(nas, first, last)

    def capi_numa_make_threshold_indicator(self, nas: LPNuma, thresh: float,
                                           type: int) -> LPNuma:
        return self.numaMakeThresholdIndicator(nas, thresh, type)

    def capi_numa_uniform_sampling(self, nas: LPNuma, nsamp: int) -> LPNuma:
        return self.numaUniformSampling(nas, nsamp)

    def capi_numa_reverse(self, nad: LPNuma, nas: LPNuma) -> LPNuma:
        return self.numaReverse(nad, nas)

    def capi_numa_low_pass_intervals(self, nas: LPNuma, thresh: float,
                                     maxn: float) -> LPNuma:
        return self.numaLowPassIntervals(nas, thresh, maxn)

    def capi_numa_threshold_edges(self, nas: LPNuma, thresh1: float,
                                  thresh2: float, maxn: float) -> LPNuma:
        return self.numaThresholdEdges(nas, thresh1, thresh2, maxn)

    def capi_numa_get_span_values(self, na: LPNuma, span: int, pstart: c_int_p,
                                  pend: c_int_p) -> int:
        return self.numaGetSpanValues(na, span, pstart, pend)

    def capi_numa_get_edge_values(self, na: LPNuma, edge: int, pstart: c_int_p,
                                  pend: c_int_p, psign: c_int_p) -> int:
        return self.numaGetEdgeValues(na, edge, pstart, pend, psign)

    def capi_numa_interpolate_eqx_val(self, startx: float, deltax: float,
                                      nay: LPNuma, type: int, xval: float,
                                      pyval: c_float_p) -> int:
        return self.numaInterpolateEqxVal(startx, deltax, nay, type, xval,
                                          pyval)

    def capi_numa_interpolate_arbx_val(self, nax: LPNuma, nay: LPNuma,
                                       type: int, xval: float,
                                       pyval: c_float_p) -> int:
        return self.numaInterpolateArbxVal(nax, nay, type, xval, pyval)

    def capi_numa_interpolate_eqx_interval(self, startx: float, deltax: float,
                                           nasy: LPNuma, type: int, x0: float,
                                           x1: float, npts: int,
                                           pnax: LPLPNuma,
                                           pnay: LPLPNuma) -> int:
        return self.numaInterpolateEqxInterval(startx, deltax, nasy, type, x0,
                                               x1, npts, pnax, pnay)

    def capi_numa_interpolate_arbx_interval(self, nax: LPNuma, nay: LPNuma,
                                            type: int, x0: float, x1: float,
                                            npts: int, pnadx: LPLPNuma,
                                            pnady: LPLPNuma) -> int:
        return self.numaInterpolateArbxInterval(nax, nay, type, x0, x1, npts,
                                                pnadx, pnady)

    def capi_numa_fit_max(self, na: LPNuma, pmaxval: c_float_p, naloc: LPNuma,
                          pmaxloc: c_float_p) -> int:
        return self.numaFitMax(na, pmaxval, naloc, pmaxloc)

    def capi_numa_differentiate_interval(self, nax: LPNuma, nay: LPNuma,
                                         x0: float, x1: float, npts: int,
                                         pnadx: LPLPNuma,
                                         pnady: LPLPNuma) -> int:
        return self.numaDifferentiateInterval(nax, nay, x0, x1, npts, pnadx,
                                              pnady)

    def capi_numa_integrate_interval(self, nax: LPNuma, nay: LPNuma, x0: float,
                                     x1: float, npts: int,
                                     psum: c_float_p) -> int:
        return self.numaIntegrateInterval(nax, nay, x0, x1, npts, psum)

    def capi_numa_sort_general(self, na: LPNuma, pnasort: LPLPNuma,
                               pnaindex: LPLPNuma, pnainvert: LPLPNuma,
                               sortorder: int, sorttype: int) -> int:
        return self.numaSortGeneral(na, pnasort, pnaindex, pnainvert,
                                    sortorder, sorttype)

    def capi_numa_sort_auto_select(self, nas: LPNuma,
                                   sortorder: int) -> LPNuma:
        return self.numaSortAutoSelect(nas, sortorder)

    def capi_numa_sort_index_auto_select(self, nas: LPNuma,
                                         sortorder: int) -> LPNuma:
        return self.numaSortIndexAutoSelect(nas, sortorder)

    def capi_numa_choose_sort_type(self, nas: LPNuma) -> int:
        return self.numaChooseSortType(nas)

    def capi_numa_sort(self, naout: LPNuma, nain: LPNuma,
                       sortorder: int) -> LPNuma:
        return self.numaSort(naout, nain, sortorder)

    def capi_numa_bin_sort(self, nas: LPNuma, sortorder: int) -> LPNuma:
        return self.numaBinSort(nas, sortorder)

    def capi_numa_get_sort_index(self, na: LPNuma, sortorder: int) -> LPNuma:
        return self.numaGetSortIndex(na, sortorder)

    def capi_numa_get_bin_sort_index(self, nas: LPNuma,
                                     sortorder: int) -> LPNuma:
        return self.numaGetBinSortIndex(nas, sortorder)

    def capi_numa_sort_by_index(self, nas: LPNuma, naindex: LPNuma) -> LPNuma:
        return self.numaSortByIndex(nas, naindex)

    def capi_numa_is_sorted(self, nas: LPNuma, sortorder: int,
                            psorted: c_int_p) -> int:
        return self.numaIsSorted(nas, sortorder, psorted)

    def capi_numa_sort_pair(self, nax: LPNuma, nay: LPNuma, sortorder: int,
                            pnasx: LPLPNuma, pnasy: LPLPNuma) -> int:
        return self.numaSortPair(nax, nay, sortorder, pnasx, pnasy)

    def capi_numa_invert_map(self, nas: LPNuma) -> LPNuma:
        return self.numaInvertMap(nas)

    def capi_numa_add_sorted(self, na: LPNuma, val: float) -> int:
        return self.numaAddSorted(na, val)

    def capi_numa_find_sorted_loc(self, na: LPNuma, val: float,
                                  pindex: c_int_p) -> int:
        return self.numaFindSortedLoc(na, val, pindex)

    def capi_numa_pseudorandom_sequence(self, size: int, seed: int) -> LPNuma:
        return self.numaPseudorandomSequence(size, seed)

    def capi_numa_random_permutation(self, nas: LPNuma, seed: int) -> LPNuma:
        return self.numaRandomPermutation(nas, seed)

    def capi_numa_get_rank_value(self, na: LPNuma, fract: float,
                                 nasort: LPNuma, usebins: int,
                                 pval: c_float_p) -> int:
        return self.numaGetRankValue(na, fract, nasort, usebins, pval)

    def capi_numa_get_median(self, na: LPNuma, pval: c_float_p) -> int:
        return self.numaGetMedian(na, pval)

    def capi_numa_get_binned_median(self, na: LPNuma, pval: c_int_p) -> int:
        return self.numaGetBinnedMedian(na, pval)

    def capi_numa_get_mean_dev_from_median(self, na: LPNuma, med: float,
                                           pdev: c_float_p) -> int:
        return self.numaGetMeanDevFromMedian(na, med, pdev)

    def capi_numa_get_median_dev_from_median(self, na: LPNuma, pmed: c_float_p,
                                             pdev: c_float_p) -> int:
        return self.numaGetMedianDevFromMedian(na, pmed, pdev)

    def capi_numa_get_mode(self, na: LPNuma, pval: c_float_p,
                           pcount: c_int_p) -> int:
        return self.numaGetMode(na, pval, pcount)

    def capi_numa_join(self, nad: LPNuma, nas: LPNuma, istart: int,
                       iend: int) -> int:
        return self.numaJoin(nad, nas, istart, iend)

    def capi_numaa_join(self, naad: LPNumaa, naas: LPNumaa, istart: int,
                        iend: int) -> int:
        return self.numaaJoin(naad, naas, istart, iend)

    def capi_numaa_flatten_to_numa(self, naa: LPNumaa) -> LPNuma:
        return self.numaaFlattenToNuma(naa)

    def capi_numa_erode(self, nas: LPNuma, size: int) -> LPNuma:
        return self.numaErode(nas, size)

    def capi_numa_dilate(self, nas: LPNuma, size: int) -> LPNuma:
        return self.numaDilate(nas, size)

    def capi_numa_open(self, nas: LPNuma, size: int) -> LPNuma:
        return self.numaOpen(nas, size)

    def capi_numa_close(self, nas: LPNuma, size: int) -> LPNuma:
        return self.numaClose(nas, size)

    def capi_numa_transform(self, nas: LPNuma, shift: float,
                            scale: float) -> LPNuma:
        return self.numaTransform(nas, shift, scale)

    def capi_numa_simple_stats(self, na: LPNuma, first: int, last: int,
                               pmean: c_float_p, pvar: c_float_p,
                               prvar: c_float_p) -> int:
        return self.numaSimpleStats(na, first, last, pmean, pvar, prvar)

    def capi_numa_windowed_stats(self, nas: LPNuma, wc: int, pnam: LPLPNuma,
                                 pnams: LPLPNuma, pnav: LPLPNuma,
                                 pnarv: LPLPNuma) -> int:
        return self.numaWindowedStats(nas, wc, pnam, pnams, pnav, pnarv)

    def capi_numa_windowed_mean(self, nas: LPNuma, wc: int) -> LPNuma:
        return self.numaWindowedMean(nas, wc)

    def capi_numa_windowed_mean_square(self, nas: LPNuma, wc: int) -> LPNuma:
        return self.numaWindowedMeanSquare(nas, wc)

    def capi_numa_windowed_variance(self, nam: LPNuma, nams: LPNuma,
                                    pnav: LPLPNuma, pnarv: LPLPNuma) -> int:
        return self.numaWindowedVariance(nam, nams, pnav, pnarv)

    def capi_numa_windowed_median(self, nas: LPNuma, halfwin: int) -> LPNuma:
        return self.numaWindowedMedian(nas, halfwin)

    def capi_numa_convert_to_int(self, nas: LPNuma) -> LPNuma:
        return self.numaConvertToInt(nas)

    def capi_numa_make_histogram(self, na: LPNuma, maxbins: int,
                                 pbinsize: c_int_p,
                                 pbinstart: c_int_p) -> LPNuma:
        return self.numaMakeHistogram(na, maxbins, pbinsize, pbinstart)

    def capi_numa_make_histogram_auto(self, na: LPNuma,
                                      maxbins: int) -> LPNuma:
        return self.numaMakeHistogramAuto(na, maxbins)

    def capi_numa_make_histogram_clipped(self, na: LPNuma, binsize: float,
                                         maxsize: float) -> LPNuma:
        return self.numaMakeHistogramClipped(na, binsize, maxsize)

    def capi_numa_rebin_histogram(self, nas: LPNuma, newsize: int) -> LPNuma:
        return self.numaRebinHistogram(nas, newsize)

    def capi_numa_normalize_histogram(self, nas: LPNuma,
                                      tsum: float) -> LPNuma:
        return self.numaNormalizeHistogram(nas, tsum)

    def capi_numa_get_stats_using_histogram(self, na: LPNuma, maxbins: int,
                                            pmin: c_float_p, pmax: c_float_p,
                                            pmean: c_float_p,
                                            pvariance: c_float_p,
                                            pmedian: c_float_p, rank: float,
                                            prval: c_float_p,
                                            phisto: LPLPNuma) -> int:
        return self.numaGetStatsUsingHistogram(na, maxbins, pmin, pmax, pmean,
                                               pvariance, pmedian, rank, prval,
                                               phisto)

    def capi_numa_get_histogram_stats(self, nahisto: LPNuma, startx: float,
                                      deltax: float, pxmean: c_float_p,
                                      pxmedian: c_float_p, pxmode: c_float_p,
                                      pxvariance: c_float_p) -> int:
        return self.numaGetHistogramStats(nahisto, startx, deltax, pxmean,
                                          pxmedian, pxmode, pxvariance)

    def capi_numa_get_histogram_stats_on_interval(self, nahisto: LPNuma,
                                                  startx: float, deltax: float,
                                                  ifirst: int, ilast: int,
                                                  pxmean: c_float_p,
                                                  pxmedian: c_float_p,
                                                  pxmode: c_float_p,
                                                  pxvariance: c_float_p
                                                  ) -> int:
        return self.numaGetHistogramStatsOnInterval(nahisto, startx, deltax,
                                                    ifirst, ilast, pxmean,
                                                    pxmedian, pxmode,
                                                    pxvariance)

    def capi_numa_make_rank_from_histogram(self, startx: float, deltax: float,
                                           nasy: LPNuma, npts: int,
                                           pnax: LPLPNuma,
                                           pnay: LPLPNuma) -> int:
        return self.numaMakeRankFromHistogram(startx, deltax, nasy, npts, pnax,
                                              pnay)

    def capi_numa_histogram_get_rank_from_val(self, na: LPNuma, rval: float,
                                              prank: c_float_p) -> int:
        return self.numaHistogramGetRankFromVal(na, rval, prank)

    def capi_numa_histogram_get_val_from_rank(self, na: LPNuma, rank: float,
                                              prval: c_float_p) -> int:
        return self.numaHistogramGetValFromRank(na, rank, prval)

    def capi_numa_discretize_sorted_in_bins(self, na: LPNuma, nbins: int,
                                            pnabinval: LPLPNuma) -> int:
        return self.numaDiscretizeSortedInBins(na, nbins, pnabinval)

    def capi_numa_discretize_histo_in_bins(self, na: LPNuma, nbins: int,
                                           pnabinval: LPLPNuma,
                                           pnarank: LPLPNuma) -> int:
        return self.numaDiscretizeHistoInBins(na, nbins, pnabinval, pnarank)

    def capi_numa_get_rank_bin_values(self, na: LPNuma, nbins: int,
                                      pnam: LPLPNuma) -> int:
        return self.numaGetRankBinValues(na, nbins, pnam)

    def capi_numa_get_uniform_bin_sizes(self, ntotal: int,
                                        nbins: int) -> LPNuma:
        return self.numaGetUniformBinSizes(ntotal, nbins)

    def capi_numa_split_distribution(self, na: LPNuma, scorefract: float,
                                     psplitindex: c_int_p, pave1: c_float_p,
                                     pave2: c_float_p, pnum1: c_float_p,
                                     pnum2: c_float_p,
                                     pnascore: LPLPNuma) -> int:
        return self.numaSplitDistribution(na, scorefract, psplitindex, pave1,
                                          pave2, pnum1, pnum2, pnascore)

    def capi_gray_histograms_to_emd(self, naa1: LPNumaa, naa2: LPNumaa,
                                    pnad: LPLPNuma) -> int:
        return self.grayHistogramsToEMD(naa1, naa2, pnad)

    def capi_numa_earth_mover_distance(self, na1: LPNuma, na2: LPNuma,
                                       pdist: c_float_p) -> int:
        return self.numaEarthMoverDistance(na1, na2, pdist)

    def capi_gray_inter_histogram_stats(self, naa: LPNumaa, wc: int,
                                        pnam: LPLPNuma, pnams: LPLPNuma,
                                        pnav: LPLPNuma,
                                        pnarv: LPLPNuma) -> int:
        return self.grayInterHistogramStats(naa, wc, pnam, pnams, pnav, pnarv)

    def capi_numa_find_peaks(self, nas: LPNuma, nmax: int, fract1: float,
                             fract2: float) -> LPNuma:
        return self.numaFindPeaks(nas, nmax, fract1, fract2)

    def capi_numa_find_extrema(self, nas: LPNuma, delta: float,
                               pnav: LPLPNuma) -> LPNuma:
        return self.numaFindExtrema(nas, delta, pnav)

    def capi_numa_find_loc_for_threshold(self, na: LPNuma, skip: int,
                                         pthresh: c_int_p,
                                         pfract: c_float_p) -> int:
        return self.numaFindLocForThreshold(na, skip, pthresh, pfract)

    def capi_numa_count_reversals(self, nas: LPNuma, minreversal: float,
                                  pnr: c_int_p, prd: c_float_p) -> int:
        return self.numaCountReversals(nas, minreversal, pnr, prd)

    def capi_numa_select_crossing_threshold(self, nax: LPNuma, nay: LPNuma,
                                            estthresh: float,
                                            pbestthresh: c_float_p) -> int:
        return self.numaSelectCrossingThreshold(nax, nay, estthresh,
                                                pbestthresh)

    def capi_numa_crossings_by_threshold(self, nax: LPNuma, nay: LPNuma,
                                         thresh: float) -> LPNuma:
        return self.numaCrossingsByThreshold(nax, nay, thresh)

    def capi_numa_crossings_by_peaks(self, nax: LPNuma, nay: LPNuma,
                                     delta: float) -> LPNuma:
        return self.numaCrossingsByPeaks(nax, nay, delta)

    def capi_numa_eval_best_haar_parameters(self, nas: LPNuma,
                                            relweight: float, nwidth: int,
                                            nshift: int, minwidth: float,
                                            maxwidth: float,
                                            pbestwidth: c_float_p,
                                            pbestshift: c_float_p,
                                            pbestscore: c_float_p) -> int:
        return self.numaEvalBestHaarParameters(nas, relweight, nwidth, nshift,
                                               minwidth, maxwidth, pbestwidth,
                                               pbestshift, pbestscore)

    def capi_numa_eval_haar_sum(self, nas: LPNuma, width: float, shift: float,
                                relweight: float, pscore: c_float_p) -> int:
        return self.numaEvalHaarSum(nas, width, shift, relweight, pscore)

    def capi_gen_constrained_numa_in_range(self, first: int, last: int,
                                           nmax: int,
                                           use_pairs: int) -> LPNuma:
        return self.genConstrainedNumaInRange(first, last, nmax, use_pairs)

    def capi_pix_get_regions_binary(self, pixs: LPPix, ppixhm: LPLPPix,
                                    ppixtm: LPLPPix, ppixtb: LPLPPix,
                                    pixadb: LPPixa) -> int:
        return self.pixGetRegionsBinary(pixs, ppixhm, ppixtm, ppixtb, pixadb)

    def capi_pix_gen_halftone_mask(self, pixs: LPPix, ppixtext: LPLPPix,
                                   phtfound: c_int_p, debug: int) -> LPPix:
        return self.pixGenHalftoneMask(pixs, ppixtext, phtfound, debug)

    def capi_pix_generate_halftone_mask(self, pixs: LPPix, ppixtext: LPLPPix,
                                        phtfound: c_int_p,
                                        pixadb: LPPixa) -> LPPix:
        return self.pixGenerateHalftoneMask(pixs, ppixtext, phtfound, pixadb)

    def capi_pix_gen_textline_mask(self, pixs: LPPix, ppixvws: LPLPPix,
                                   ptlfound: c_int_p,
                                   pixadb: LPPixa) -> LPPix:
        return self.pixGenTextlineMask(pixs, ppixvws, ptlfound, pixadb)

    def capi_pix_gen_textblock_mask(self, pixs: LPPix, pixvws: LPPix,
                                    pixadb: LPPixa) -> LPPix:
        return self.pixGenTextblockMask(pixs, pixvws, pixadb)

    def capi_pix_find_page_foreground(self, pixs: LPPix, threshold: int,
                                      mindist: int, erasedist: int,
                                      showmorph: int,
                                      pixac: LPPixaComp) -> LPBox:
        return self.pixFindPageForeground(pixs, threshold, mindist, erasedist,
                                          showmorph, pixac)

    def capi_pix_split_into_characters(self, pixs: LPPix, minw: int, minh: int,
                                       pboxa: LPLPBoxa, ppixa: LPLPPixa,
                                       ppixdebug: LPLPPix) -> int:
        return self.pixSplitIntoCharacters(pixs, minw, minh, pboxa, ppixa,
                                           ppixdebug)

    def capi_pix_split_component_with_profile(self, pixs: LPPix, delta: int,
                                              mindel: int,
                                              ppixdebug: LPLPPix) -> LPBoxa:
        return self.pixSplitComponentWithProfile(pixs, delta, mindel,
                                                 ppixdebug)

    def capi_pix_extract_textlines(self, pixs: LPPix, maxw: int, maxh: int,
                                   minw: int, minh: int, adjw: int, adjh: int,
                                   pixadb: LPPixa) -> LPPixa:
        return self.pixExtractTextlines(pixs, maxw, maxh, minw, minh, adjw,
                                        adjh, pixadb)

    def capi_pix_extract_raw_textlines(self, pixs: LPPix, maxw: int, maxh: int,
                                       adjw: int, adjh: int,
                                       pixadb: LPPixa) -> LPPixa:
        return self.pixExtractRawTextlines(pixs, maxw, maxh, adjw, adjh,
                                           pixadb)

    def capi_pix_count_text_columns(self, pixs: LPPix, deltafract: float,
                                    peakfract: float, clipfract: float,
                                    pncols: c_int_p, pixadb: LPPixa) -> int:
        return self.pixCountTextColumns(pixs, deltafract, peakfract, clipfract,
                                        pncols, pixadb)

    def capi_pix_decide_if_text(self, pixs: LPPix, box: LPBox,
                                pistext: c_int_p, pixadb: LPPixa) -> int:
        return self.pixDecideIfText(pixs, box, pistext, pixadb)

    def capi_pix_find_thresh_fg_extent(self, pixs: LPPix, thresh: int,
                                       ptop: c_int_p, pbot: c_int_p) -> int:
        return self.pixFindThreshFgExtent(pixs, thresh, ptop, pbot)

    def capi_pix_decide_if_table(self, pixs: LPPix, box: LPBox, orient: int,
                                 pscore: c_int_p, pixadb: LPPixa) -> int:
        return self.pixDecideIfTable(pixs, box, orient, pscore, pixadb)

    def capi_pix_prepare1bpp(self, pixs: LPPix, box: LPBox, cropfract: float,
                             outres: int) -> LPPix:
        return self.pixPrepare1bpp(pixs, box, cropfract, outres)

    def capi_pix_estimate_background(self, pixs: LPPix, darkthresh: int,
                                     edgecrop: float, pbg: c_int_p) -> int:
        return self.pixEstimateBackground(pixs, darkthresh, edgecrop, pbg)

    def capi_pix_find_large_rectangles(self, pixs: LPPix, polarity: int,
                                       nrect: int, pboxa: LPLPBoxa,
                                       ppixdb: LPLPPix) -> int:
        return self.pixFindLargeRectangles(pixs, polarity, nrect, pboxa,
                                           ppixdb)

    def capi_pix_find_largest_rectangle(self, pixs: LPPix, polarity: int,
                                        pbox: LPLPBox,
                                        ppixdb: LPLPPix) -> int:
        return self.pixFindLargestRectangle(pixs, polarity, pbox, ppixdb)

    def capi_pix_find_rectangle_in_cc(self, pixs: LPPix, boxs: LPBox,
                                      fract: float, dir: int, select: int,
                                      debug: int) -> LPBox:
        return self.pixFindRectangleInCC(pixs, boxs, fract, dir, select, debug)

    def capi_pix_auto_photoinvert(self, pixs: LPPix, thresh: int,
                                  ppixm: LPLPPix, pixadb: LPPixa) -> LPPix:
        return self.pixAutoPhotoinvert(pixs, thresh, ppixm, pixadb)

    def capi_pix_set_select_cmap(self, pixs: LPPix, box: LPBox, sindex: int,
                                 rval: int, gval: int, bval: int) -> int:
        return self.pixSetSelectCmap(pixs, box, sindex, rval, gval, bval)

    def capi_pix_color_gray_regions_cmap(self, pixs: LPPix, boxa: LPBoxa,
                                         type: int, rval: int, gval: int,
                                         bval: int) -> int:
        return self.pixColorGrayRegionsCmap(pixs, boxa, type, rval, gval, bval)

    def capi_pix_color_gray_cmap(self, pixs: LPPix, box: LPBox, type: int,
                                 rval: int, gval: int, bval: int) -> int:
        return self.pixColorGrayCmap(pixs, box, type, rval, gval, bval)

    def capi_pix_color_gray_masked_cmap(self, pixs: LPPix, pixm: LPPix,
                                        type: int, rval: int, gval: int,
                                        bval: int) -> int:
        return self.pixColorGrayMaskedCmap(pixs, pixm, type, rval, gval, bval)

    def capi_add_colorized_gray_to_cmap(self, cmap: LPPixColormap, type: int,
                                        rval: int, gval: int, bval: int,
                                        pna: LPLPNuma) -> int:
        return self.addColorizedGrayToCmap(cmap, type, rval, gval, bval, pna)

    def capi_pix_set_select_masked_cmap(self, pixs: LPPix, pixm: LPPix, x: int,
                                        y: int, sindex: int, rval: int,
                                        gval: int, bval: int) -> int:
        return self.pixSetSelectMaskedCmap(pixs, pixm, x, y, sindex, rval,
                                           gval, bval)

    def capi_pix_set_masked_cmap(self, pixs: LPPix, pixm: LPPix, x: int,
                                 y: int, rval: int, gval: int,
                                 bval: int) -> int:
        return self.pixSetMaskedCmap(pixs, pixm, x, y, rval, gval, bval)

    def capi_parse_for_protos(self, filein: bytes,
                              prestring: bytes) -> LP_c_char:
        return self.parseForProtos(filein, prestring)

    def capi_partify_files(self, dirname: bytes, substr: bytes, nparts: int,
                           outroot: bytes, debugfile: bytes) -> int:
        return self.partifyFiles(dirname, substr, nparts, outroot, debugfile)

    def capi_partify_pixac(self, pixac: LPPixaComp, nparts: int,
                           outroot: bytes, pixadb: LPPixa) -> int:
        return self.partifyPixac(pixac, nparts, outroot, pixadb)

    def capi_boxa_get_whiteblocks(self, boxas: LPBoxa, box: LPBox,
                                  sortflag: int, maxboxes: int,
                                  maxoverlap: float, maxperim: int,
                                  fract: float, maxpops: int) -> LPBoxa:
        return self.boxaGetWhiteblocks(boxas, box, sortflag, maxboxes,
                                       maxoverlap, maxperim, fract, maxpops)

    def capi_boxa_prune_sorted_on_overlap(self, boxas: LPBoxa,
                                          maxoverlap: float) -> LPBoxa:
        return self.boxaPruneSortedOnOverlap(boxas, maxoverlap)

    def capi_convert_files_to_pdf(self, dirname: bytes, substr: bytes,
                                  res: int, scalefactor: float, type: int,
                                  quality: int, title: bytes,
                                  fileout: bytes) -> int:
        return self.convertFilesToPdf(dirname, substr, res, scalefactor, type,
                                      quality, title, fileout)

    def capi_sa_convert_files_to_pdf(self, sa: LPSarray, res: int,
                                     scalefactor: float, type: int,
                                     quality: int, title: bytes,
                                     fileout: bytes) -> int:
        return self.saConvertFilesToPdf(sa, res, scalefactor, type, quality,
                                        title, fileout)

    def capi_sa_convert_files_to_pdf_data(self, sa: LPSarray, res: int,
                                          scalefactor: float, type: int,
                                          quality: int, title: bytes,
                                          pdata: POINTER(c_ubyte_p),
                                          pnbytes: c_size_t_p) -> int:
        return self.saConvertFilesToPdfData(sa, res, scalefactor, type,
                                            quality, title, pdata, pnbytes)

    def capi_select_default_pdf_encoding(self, pix: LPPix,
                                         ptype: c_int_p) -> int:
        return self.selectDefaultPdfEncoding(pix, ptype)

    def capi_convert_unscaled_files_to_pdf(self, dirname: bytes, substr: bytes,
                                           title: bytes,
                                           fileout: bytes) -> int:
        return self.convertUnscaledFilesToPdf(dirname, substr, title, fileout)

    def capi_sa_convert_unscaled_files_to_pdf(self, sa: LPSarray, title: bytes,
                                              fileout: bytes) -> int:
        return self.saConvertUnscaledFilesToPdf(sa, title, fileout)

    def capi_sa_convert_unscaled_files_to_pdf_data(self, sa: LPSarray,
                                                   title: bytes,
                                                   pdata: POINTER(c_ubyte_p),
                                                   pnbytes: c_size_t_p) -> int:
        return self.saConvertUnscaledFilesToPdfData(sa, title, pdata, pnbytes)

    def capi_convert_unscaled_to_pdf_data(self, fname: bytes, title: bytes,
                                          pdata: POINTER(c_ubyte_p),
                                          pnbytes: c_size_t_p) -> int:
        return self.convertUnscaledToPdfData(fname, title, pdata, pnbytes)

    def capi_pixa_convert_to_pdf(self, pixa: LPPixa, res: int,
                                 scalefactor: float, type: int, quality: int,
                                 title: bytes, fileout: bytes) -> int:
        return self.pixaConvertToPdf(pixa, res, scalefactor, type, quality,
                                     title, fileout)

    def capi_pixa_convert_to_pdf_data(self, pixa: LPPixa, res: int,
                                      scalefactor: float, type: int,
                                      quality: int, title: bytes,
                                      pdata: POINTER(c_ubyte_p),
                                      pnbytes: c_size_t_p) -> int:
        return self.pixaConvertToPdfData(pixa, res, scalefactor, type, quality,
                                         title, pdata, pnbytes)

    def capi_convert_to_pdf(self, filein: bytes, type: int, quality: int,
                            fileout: bytes, x: int, y: int, res: int,
                            title: bytes, plpd: LPLPL_Pdf_Data,
                            position: int) -> int:
        return self.convertToPdf(filein, type, quality, fileout, x, y, res,
                                 title, plpd, position)

    def capi_convert_image_data_to_pdf(self, imdata: c_ubyte_p, size: int,
                                       type: int, quality: int, fileout: bytes,
                                       x: int, y: int, res: int, title: bytes,
                                       plpd: LPLPL_Pdf_Data,
                                       position: int) -> int:
        return self.convertImageDataToPdf(imdata, size, type, quality, fileout,
                                          x, y, res, title, plpd, position)

    def capi_convert_to_pdf_data(self, filein: bytes, type: int, quality: int,
                                 pdata: POINTER(c_ubyte_p),
                                 pnbytes: c_size_t_p, x: int, y: int, res: int,
                                 title: bytes, plpd: LPLPL_Pdf_Data,
                                 position: int) -> int:
        return self.convertToPdfData(filein, type, quality, pdata, pnbytes, x,
                                     y, res, title, plpd, position)

    def capi_convert_image_data_to_pdf_data(self, imdata: c_ubyte_p, size: int,
                                            type: int, quality: int,
                                            pdata: POINTER(c_ubyte_p),
                                            pnbytes: c_size_t_p, x: int,
                                            y: int, res: int, title: bytes,
                                            plpd: LPLPL_Pdf_Data,
                                            position: int) -> int:
        return self.convertImageDataToPdfData(imdata, size, type, quality,
                                              pdata, pnbytes, x, y, res, title,
                                              plpd, position)

    def capi_pix_convert_to_pdf(self, pix: LPPix, type: int, quality: int,
                                fileout: bytes, x: int, y: int, res: int,
                                title: bytes, plpd: LPLPL_Pdf_Data,
                                position: int) -> int:
        return self.pixConvertToPdf(pix, type, quality, fileout, x, y, res,
                                    title, plpd, position)

    def capi_pix_write_stream_pdf(self, fp: LPFile, pix: LPPix, res: int,
                                  title: bytes) -> int:
        return self.pixWriteStreamPdf(fp, pix, res, title)

    def capi_pix_write_mem_pdf(self, pdata: POINTER(c_ubyte_p),
                               pnbytes: c_size_t_p, pix: LPPix, res: int,
                               title: bytes) -> int:
        return self.pixWriteMemPdf(pdata, pnbytes, pix, res, title)

    def capi_convert_segmented_files_to_pdf(self, dirname: bytes,
                                            substr: bytes, res: int, type: int,
                                            thresh: int, baa: LPBoxaa,
                                            quality: int, scalefactor: float,
                                            title: bytes,
                                            fileout: bytes) -> int:
        return self.convertSegmentedFilesToPdf(dirname, substr, res, type,
                                               thresh, baa, quality,
                                               scalefactor, title, fileout)

    def capi_convert_numbered_masks_to_boxaa(self, dirname: bytes,
                                             substr: bytes, numpre: int,
                                             numpost: int) -> LPBoxaa:
        return self.convertNumberedMasksToBoxaa(dirname, substr, numpre,
                                                numpost)

    def capi_convert_to_pdf_segmented(self, filein: bytes, res: int, type: int,
                                      thresh: int, boxa: LPBoxa, quality: int,
                                      scalefactor: float, title: bytes,
                                      fileout: bytes) -> int:
        return self.convertToPdfSegmented(filein, res, type, thresh, boxa,
                                          quality, scalefactor, title,
                                          fileout)

    def capi_pix_convert_to_pdf_segmented(self, pixs: LPPix, res: int,
                                          type: int, thresh: int, boxa: LPBoxa,
                                          quality: int, scalefactor: float,
                                          title: bytes,
                                          fileout: bytes) -> int:
        return self.pixConvertToPdfSegmented(pixs, res, type, thresh, boxa,
                                             quality, scalefactor, title,
                                             fileout)

    def capi_convert_to_pdf_data_segmented(self, filein: bytes, res: int,
                                           type: int, thresh: int,
                                           boxa: LPBoxa, quality: int,
                                           scalefactor: float, title: bytes,
                                           pdata: POINTER(c_ubyte_p),
                                           pnbytes: c_size_t_p) -> int:
        return self.convertToPdfDataSegmented(filein, res, type, thresh, boxa,
                                              quality, scalefactor, title,
                                              pdata, pnbytes)

    def capi_pix_convert_to_pdf_data_segmented(self, pixs: LPPix, res: int,
                                               type: int, thresh: int,
                                               boxa: LPBoxa, quality: int,
                                               scalefactor: float,
                                               title: bytes,
                                               pdata: POINTER(c_ubyte_p),
                                               pnbytes: c_size_t_p) -> int:
        return self.pixConvertToPdfDataSegmented(pixs, res, type, thresh, boxa,
                                                 quality, scalefactor, title,
                                                 pdata, pnbytes)

    def capi_concatenate_pdf(self, dirname: bytes, substr: bytes,
                             fileout: bytes) -> int:
        return self.concatenatePdf(dirname, substr, fileout)

    def capi_sa_concatenate_pdf(self, sa: LPSarray, fileout: bytes) -> int:
        return self.saConcatenatePdf(sa, fileout)

    def capi_ptra_concatenate_pdf(self, pa: LPL_Ptra, fileout: bytes) -> int:
        return self.ptraConcatenatePdf(pa, fileout)

    def capi_concatenate_pdf_to_data(self, dirname: bytes, substr: bytes,
                                     pdata: POINTER(c_ubyte_p),
                                     pnbytes: c_size_t_p) -> int:
        return self.concatenatePdfToData(dirname, substr, pdata, pnbytes)

    def capi_sa_concatenate_pdf_to_data(self, sa: LPSarray,
                                        pdata: POINTER(c_ubyte_p),
                                        pnbytes: c_size_t_p) -> int:
        return self.saConcatenatePdfToData(sa, pdata, pnbytes)

    def capi_pix_convert_to_pdf_data(self, pix: LPPix, type: int, quality: int,
                                     pdata: POINTER(c_ubyte_p),
                                     pnbytes: c_size_t_p, x: int, y: int,
                                     res: int, title: bytes,
                                     plpd: LPLPL_Pdf_Data,
                                     position: int) -> int:
        return self.pixConvertToPdfData(pix, type, quality, pdata, pnbytes, x,
                                        y, res, title, plpd, position)

    def capi_ptra_concatenate_pdf_to_data(self, pa_data: LPL_Ptra,
                                          sa: LPSarray,
                                          pdata: POINTER(c_ubyte_p),
                                          pnbytes: c_size_t_p) -> int:
        return self.ptraConcatenatePdfToData(pa_data, sa, pdata, pnbytes)

    def capi_convert_tiff_multipage_to_pdf(self, filein: bytes,
                                           fileout: bytes) -> int:
        return self.convertTiffMultipageToPdf(filein, fileout)

    def capi_l_generateCIDataForPdf(self, fname: bytes, pix: LPPix,
                                    quality: int,
                                    pcid: LPLPL_Compressed_Data) -> int:
        return self.l_generateCIDataForPdf(fname, pix, quality, pcid)

    def capi_l_generateCIData(self, fname: bytes, type: int, quality: int,
                              ascii85: int,
                              pcid: LPLPL_Compressed_Data) -> int:
        return self.l_generateCIData(fname, type, quality, ascii85, pcid)

    def capi_l_generateFlateDataPdf(self, fname: bytes,
                                    pixs: LPPix) -> LPL_Compressed_Data:
        return self.l_generateFlateDataPdf(fname, pixs)

    def capi_l_generateJpegData(self, fname: bytes,
                                ascii85flag: int) -> LPL_Compressed_Data:
        return self.l_generateJpegData(fname, ascii85flag)

    def capi_l_generateJpegDataMem(self, data: c_ubyte_p, nbytes: int,
                                   ascii85flag: int) -> LPL_Compressed_Data:
        return self.l_generateJpegDataMem(data, nbytes, ascii85flag)

    def capi_l_generateG4Data(self, fname: bytes,
                              ascii85flag: int) -> LPL_Compressed_Data:
        return self.l_generateG4Data(fname, ascii85flag)

    def capi_pix_generate_ci_data(self, pixs: LPPix, type: int, quality: int,
                                  ascii85: int,
                                  pcid: LPLPL_Compressed_Data) -> int:
        return self.pixGenerateCIData(pixs, type, quality, ascii85, pcid)

    def capi_l_generateFlateData(self, fname: bytes,
                                 ascii85flag: int) -> LPL_Compressed_Data:
        return self.l_generateFlateData(fname, ascii85flag)

    def capi_cid_convert_to_pdf_data(self, cid: LPL_Compressed_Data,
                                     title: bytes, pdata: POINTER(c_ubyte_p),
                                     pnbytes: c_size_t_p) -> int:
        return self.cidConvertToPdfData(cid, title, pdata, pnbytes)

    def capi_l_CIDataDestroy(self, pcid: LPLPL_Compressed_Data):
        self.l_CIDataDestroy(pcid)

    def capi_l_pdfSetG4ImageMask(self, flag: int):
        self.l_pdfSetG4ImageMask(flag)

    def capi_l_pdfSetDateAndVersion(self, flag: int):
        self.l_pdfSetDateAndVersion(flag)

    def capi_set_pix_memory_manager(self, allocator: alloc_fn,
                                    deallocator: alloc_fn):
        self.setPixMemoryManager(allocator, deallocator)

    def capi_pix_create(self, width: int, height: int, depth: int) -> LPPix:
        return self.pixCreate(width, height, depth)

    def capi_pix_create_no_init(self, width: int, height: int,
                                depth: int) -> LPPix:
        return self.pixCreateNoInit(width, height, depth)

    def capi_pix_create_template(self, pixs: LPPix) -> LPPix:
        return self.pixCreateTemplate(pixs)

    def capi_pix_create_template_no_init(self, pixs: LPPix) -> LPPix:
        return self.pixCreateTemplateNoInit(pixs)

    def capi_pix_create_with_cmap(self, width: int, height: int, depth: int,
                                  initcolor: int) -> LPPix:
        return self.pixCreateWithCmap(width, height, depth, initcolor)

    def capi_pix_create_header(self, width: int, height: int,
                               depth: int) -> LPPix:
        return self.pixCreateHeader(width, height, depth)

    def capi_pix_clone(self, pixs: LPPix) -> LPPix:
        return self.pixClone(pixs)

    def capi_pix_destroy(self, ppix: LPLPPix):
        self.pixDestroy(ppix)

    def capi_pix_copy(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixCopy(pixd, pixs)

    def capi_pix_resize_image_data(self, pixd: LPPix, pixs: LPPix) -> int:
        return self.pixResizeImageData(pixd, pixs)

    def capi_pix_copy_colormap(self, pixd: LPPix, pixs: LPPix) -> int:
        return self.pixCopyColormap(pixd, pixs)

    def capi_pix_transfer_all_data(self, pixd: LPPix, ppixs: LPLPPix,
                                   copytext: int, copyformat: int) -> int:
        return self.pixTransferAllData(pixd, ppixs, copytext, copyformat)

    def capi_pix_swap_and_destroy(self, ppixd: LPLPPix, ppixs: LPLPPix) -> int:
        return self.pixSwapAndDestroy(ppixd, ppixs)

    def capi_pix_get_width(self, pix: LPPix) -> int:
        return self.pixGetWidth(pix)

    def capi_pix_set_width(self, pix: LPPix, width: int) -> int:
        return self.pixSetWidth(pix, width)

    def capi_pix_get_height(self, pix: LPPix) -> int:
        return self.pixGetHeight(pix)

    def capi_pix_set_height(self, pix: LPPix, height: int) -> int:
        return self.pixSetHeight(pix, height)

    def capi_pix_get_depth(self, pix: LPPix) -> int:
        return self.pixGetDepth(pix)

    def capi_pix_set_depth(self, pix: LPPix, depth: int) -> int:
        return self.pixSetDepth(pix, depth)

    def capi_pix_get_dimensions(self, pix: LPPix, pw: c_int_p, ph: c_int_p,
                                pd: c_int_p) -> int:
        return self.pixGetDimensions(pix, pw, ph, pd)

    def capi_pix_set_dimensions(self, pix: LPPix, w: int, h: int,
                                d: int) -> int:
        return self.pixSetDimensions(pix, w, h, d)

    def capi_pix_copy_dimensions(self, pixd: LPPix, pixs: LPPix) -> int:
        return self.pixCopyDimensions(pixd, pixs)

    def capi_pix_get_spp(self, pix: LPPix) -> int:
        return self.pixGetSpp(pix)

    def capi_pix_set_spp(self, pix: LPPix, spp: int) -> int:
        return self.pixSetSpp(pix, spp)

    def capi_pix_copy_spp(self, pixd: LPPix, pixs: LPPix) -> int:
        return self.pixCopySpp(pixd, pixs)

    def capi_pix_get_wpl(self, pix: LPPix) -> int:
        return self.pixGetWpl(pix)

    def capi_pix_set_wpl(self, pix: LPPix, wpl: int) -> int:
        return self.pixSetWpl(pix, wpl)

    def capi_pix_get_refcount(self, pix: LPPix) -> int:
        return self.pixGetRefcount(pix)

    def capi_pix_change_refcount(self, pix: LPPix, delta: int) -> int:
        return self.pixChangeRefcount(pix, delta)

    def capi_pix_get_xres(self, pix: LPPix) -> int:
        return self.pixGetXRes(pix)

    def capi_pix_set_xres(self, pix: LPPix, res: int) -> int:
        return self.pixSetXRes(pix, res)

    def capi_pix_get_yres(self, pix: LPPix) -> int:
        return self.pixGetYRes(pix)

    def capi_pix_set_yres(self, pix: LPPix, res: int) -> int:
        return self.pixSetYRes(pix, res)

    def capi_pix_get_resolution(self, pix: LPPix, pxres: c_int_p,
                                pyres: c_int_p) -> int:
        return self.pixGetResolution(pix, pxres, pyres)

    def capi_pix_set_resolution(self, pix: LPPix, xres: int, yres: int) -> int:
        return self.pixSetResolution(pix, xres, yres)

    def capi_pix_copy_resolution(self, pixd: LPPix, pixs: LPPix) -> int:
        return self.pixCopyResolution(pixd, pixs)

    def capi_pix_scale_resolution(self, pix: LPPix, xscale: float,
                                  yscale: float) -> int:
        return self.pixScaleResolution(pix, xscale, yscale)

    def capi_pix_get_input_format(self, pix: LPPix) -> int:
        return self.pixGetInputFormat(pix)

    def capi_pix_set_input_format(self, pix: LPPix, informat: int) -> int:
        return self.pixSetInputFormat(pix, informat)

    def capi_pix_copy_input_format(self, pixd: LPPix, pixs: LPPix) -> int:
        return self.pixCopyInputFormat(pixd, pixs)

    def capi_pix_set_special(self, pix: LPPix, special: int) -> int:
        return self.pixSetSpecial(pix, special)

    def capi_pix_get_text(self, pix: LPPix) -> LP_c_char:
        return self.pixGetText(pix)

    def capi_pix_set_text(self, pix: LPPix, textstring: bytes) -> int:
        return self.pixSetText(pix, textstring)

    def capi_pix_add_text(self, pix: LPPix, textstring: bytes) -> int:
        return self.pixAddText(pix, textstring)

    def capi_pix_copy_text(self, pixd: LPPix, pixs: LPPix) -> int:
        return self.pixCopyText(pixd, pixs)

    def capi_pix_get_text_comp_new(self, pix: LPPix,
                                   psize: c_size_t_p) -> c_ubyte_p:
        return self.pixGetTextCompNew(pix, psize)

    def capi_pix_set_text_comp_new(self, pix: LPPix, data: c_ubyte_p,
                                   size: int) -> int:
        return self.pixSetTextCompNew(pix, data, size)

    def capi_pix_get_colormap(self, pix: LPPix) -> LPPixColormap:
        return self.pixGetColormap(pix)

    def capi_pix_set_colormap(self, pix: LPPix,
                              colormap: LPPixColormap) -> int:
        return self.pixSetColormap(pix, colormap)

    def capi_pix_destroy_colormap(self, pix: LPPix) -> int:
        return self.pixDestroyColormap(pix)

    def capi_pix_get_data(self, pix: LPPix) -> c_uint_p:
        return self.pixGetData(pix)

    def capi_pix_set_data(self, pix: LPPix, data: c_uint_p) -> int:
        return self.pixSetData(pix, data)

    def capi_pix_extract_data(self, pixs: LPPix) -> c_uint_p:
        return self.pixExtractData(pixs)

    def capi_pix_free_data(self, pix: LPPix) -> int:
        return self.pixFreeData(pix)

    def capi_pix_get_line_ptrs(self, pix: LPPix,
                               psize: c_int_p) -> POINTER(c_void_p):
        return self.pixGetLinePtrs(pix, psize)

    def capi_pix_sizes_equal(self, pix1: LPPix, pix2: LPPix) -> int:
        return self.pixSizesEqual(pix1, pix2)

    def capi_pix_max_aspect_ratio(self, pixs: LPPix, pratio: c_float_p) -> int:
        return self.pixMaxAspectRatio(pixs, pratio)

    def capi_pix_print_stream_info(self, fp: LPFile, pix: LPPix,
                                   text: bytes) -> int:
        return self.pixPrintStreamInfo(fp, pix, text)

    def capi_pix_get_pixel(self, pix: LPPix, x: int, y: int,
                           pval: c_uint_p) -> int:
        return self.pixGetPixel(pix, x, y, pval)

    def capi_pix_set_pixel(self, pix: LPPix, x: int, y: int, val: int) -> int:
        return self.pixSetPixel(pix, x, y, val)

    def capi_pix_get_rgb_pixel(self, pix: LPPix, x: int, y: int,
                               prval: c_int_p, pgval: c_int_p,
                               pbval: c_int_p) -> int:
        return self.pixGetRGBPixel(pix, x, y, prval, pgval, pbval)

    def capi_pix_set_rgb_pixel(self, pix: LPPix, x: int, y: int, rval: int,
                               gval: int, bval: int) -> int:
        return self.pixSetRGBPixel(pix, x, y, rval, gval, bval)

    def capi_pix_set_cmap_pixel(self, pix: LPPix, x: int, y: int, rval: int,
                                gval: int, bval: int) -> int:
        return self.pixSetCmapPixel(pix, x, y, rval, gval, bval)

    def capi_pix_get_random_pixel(self, pix: LPPix, pval: c_uint_p,
                                  px: c_int_p, py: c_int_p) -> int:
        return self.pixGetRandomPixel(pix, pval, px, py)

    def capi_pix_clear_pixel(self, pix: LPPix, x: int, y: int) -> int:
        return self.pixClearPixel(pix, x, y)

    def capi_pix_flip_pixel(self, pix: LPPix, x: int, y: int) -> int:
        return self.pixFlipPixel(pix, x, y)

    def capi_set_pixel_low(self, line: c_uint_p, x: int, depth: int, val: int):
        self.setPixelLow(line, x, depth, val)

    def capi_pix_get_black_or_white_val(self, pixs: LPPix, op: int,
                                        pval: c_uint_p) -> int:
        return self.pixGetBlackOrWhiteVal(pixs, op, pval)

    def capi_pix_clear_all(self, pix: LPPix) -> int:
        return self.pixClearAll(pix)

    def capi_pix_set_all(self, pix: LPPix) -> int:
        return self.pixSetAll(pix)

    def capi_pix_set_all_gray(self, pix: LPPix, grayval: int) -> int:
        return self.pixSetAllGray(pix, grayval)

    def capi_pix_set_all_arbitrary(self, pix: LPPix, val: int) -> int:
        return self.pixSetAllArbitrary(pix, val)

    def capi_pix_set_black_or_white(self, pixs: LPPix, op: int) -> int:
        return self.pixSetBlackOrWhite(pixs, op)

    def capi_pix_set_component_arbitrary(self, pix: LPPix, comp: int,
                                         val: int) -> int:
        return self.pixSetComponentArbitrary(pix, comp, val)

    def capi_pix_clear_in_rect(self, pix: LPPix, box: LPBox) -> int:
        return self.pixClearInRect(pix, box)

    def capi_pix_set_in_rect(self, pix: LPPix, box: LPBox) -> int:
        return self.pixSetInRect(pix, box)

    def capi_pix_set_in_rect_arbitrary(self, pix: LPPix, box: LPBox,
                                       val: int) -> int:
        return self.pixSetInRectArbitrary(pix, box, val)

    def capi_pix_blend_in_rect(self, pixs: LPPix, box: LPBox, val: int,
                               fract: float) -> int:
        return self.pixBlendInRect(pixs, box, val, fract)

    def capi_pix_set_pad_bits(self, pix: LPPix, val: int) -> int:
        return self.pixSetPadBits(pix, val)

    def capi_pix_set_pad_bits_band(self, pix: LPPix, by: int, bh: int,
                                   val: int) -> int:
        return self.pixSetPadBitsBand(pix, by, bh, val)

    def capi_pix_set_or_clear_border(self, pixs: LPPix, left: int, right: int,
                                     top: int, bot: int, op: int) -> int:
        return self.pixSetOrClearBorder(pixs, left, right, top, bot, op)

    def capi_pix_set_border_val(self, pixs: LPPix, left: int, right: int,
                                top: int, bot: int, val: int) -> int:
        return self.pixSetBorderVal(pixs, left, right, top, bot, val)

    def capi_pix_set_border_ring_val(self, pixs: LPPix, dist: int,
                                     val: int) -> int:
        return self.pixSetBorderRingVal(pixs, dist, val)

    def capi_pix_set_mirrored_border(self, pixs: LPPix, left: int, right: int,
                                     top: int, bot: int) -> int:
        return self.pixSetMirroredBorder(pixs, left, right, top, bot)

    def capi_pix_copy_border(self, pixd: LPPix, pixs: LPPix, left: int,
                             right: int, top: int, bot: int) -> LPPix:
        return self.pixCopyBorder(pixd, pixs, left, right, top, bot)

    def capi_pix_add_border(self, pixs: LPPix, npix: int, val: int) -> LPPix:
        return self.pixAddBorder(pixs, npix, val)

    def capi_pix_add_black_or_white_border(self, pixs: LPPix, left: int,
                                           right: int, top: int, bot: int,
                                           op: int) -> LPPix:
        return self.pixAddBlackOrWhiteBorder(pixs, left, right, top, bot, op)

    def capi_pix_add_border_general(self, pixs: LPPix, left: int, right: int,
                                    top: int, bot: int, val: int) -> LPPix:
        return self.pixAddBorderGeneral(pixs, left, right, top, bot, val)

    def capi_pix_remove_border(self, pixs: LPPix, npix: int) -> LPPix:
        return self.pixRemoveBorder(pixs, npix)

    def capi_pix_remove_border_general(self, pixs: LPPix, left: int,
                                       right: int, top: int,
                                       bot: int) -> LPPix:
        return self.pixRemoveBorderGeneral(pixs, left, right, top, bot)

    def capi_pix_remove_border_to_size(self, pixs: LPPix, wd: int,
                                       hd: int) -> LPPix:
        return self.pixRemoveBorderToSize(pixs, wd, hd)

    def capi_pix_add_mirrored_border(self, pixs: LPPix, left: int, right: int,
                                     top: int, bot: int) -> LPPix:
        return self.pixAddMirroredBorder(pixs, left, right, top, bot)

    def capi_pix_add_repeated_border(self, pixs: LPPix, left: int, right: int,
                                     top: int, bot: int) -> LPPix:
        return self.pixAddRepeatedBorder(pixs, left, right, top, bot)

    def capi_pix_add_mixed_border(self, pixs: LPPix, left: int, right: int,
                                  top: int, bot: int) -> LPPix:
        return self.pixAddMixedBorder(pixs, left, right, top, bot)

    def capi_pix_add_continued_border(self, pixs: LPPix, left: int, right: int,
                                      top: int, bot: int) -> LPPix:
        return self.pixAddContinuedBorder(pixs, left, right, top, bot)

    def capi_pix_shift_and_transfer_alpha(self, pixd: LPPix, pixs: LPPix,
                                          shiftx: float,
                                          shifty: float) -> int:
        return self.pixShiftAndTransferAlpha(pixd, pixs, shiftx, shifty)

    def capi_pix_display_layers_rgba(self, pixs: LPPix, val: int,
                                     maxw: int) -> LPPix:
        return self.pixDisplayLayersRGBA(pixs, val, maxw)

    def capi_pix_create_rgb_image(self, pixr: LPPix, pixg: LPPix,
                                  pixb: LPPix) -> LPPix:
        return self.pixCreateRGBImage(pixr, pixg, pixb)

    def capi_pix_get_rgb_component(self, pixs: LPPix, comp: int) -> LPPix:
        return self.pixGetRGBComponent(pixs, comp)

    def capi_pix_set_rgb_component(self, pixd: LPPix, pixs: LPPix,
                                   comp: int) -> int:
        return self.pixSetRGBComponent(pixd, pixs, comp)

    def capi_pix_get_rgb_component_cmap(self, pixs: LPPix, comp: int) -> LPPix:
        return self.pixGetRGBComponentCmap(pixs, comp)

    def capi_pix_copy_rgb_component(self, pixd: LPPix, pixs: LPPix,
                                    comp: int) -> int:
        return self.pixCopyRGBComponent(pixd, pixs, comp)

    def capi_compose_rgb_pixel(self, rval: int, gval: int, bval: int,
                               ppixel: c_uint_p) -> int:
        return self.composeRGBPixel(rval, gval, bval, ppixel)

    def capi_compose_rgba_pixel(self, rval: int, gval: int, bval: int,
                                aval: int, ppixel: c_uint_p) -> int:
        return self.composeRGBAPixel(rval, gval, bval, aval, ppixel)

    def capi_extract_rgb_values(self, pixel: int, prval: c_int_p,
                                pgval: c_int_p, pbval: c_int_p):
        self.extractRGBValues(pixel, prval, pgval, pbval)

    def capi_extract_rgba_values(self, pixel: int, prval: c_int_p,
                                 pgval: c_int_p, pbval: c_int_p,
                                 paval: c_int_p):
        self.extractRGBAValues(pixel, prval, pgval, pbval, paval)

    def capi_extract_min_max_component(self, pixel: int, type: int) -> int:
        return self.extractMinMaxComponent(pixel, type)

    def capi_pix_get_rgb_line(self, pixs: LPPix, row: int, bufr: c_ubyte_p,
                              bufg: c_ubyte_p, bufb: c_ubyte_p) -> int:
        return self.pixGetRGBLine(pixs, row, bufr, bufg, bufb)

    def capi_set_line_data_val(self, line: c_uint_p, j: int, d: int,
                               val: int) -> int:
        return self.setLineDataVal(line, j, d, val)

    def capi_pix_endian_byte_swap_new(self, pixs: LPPix) -> LPPix:
        return self.pixEndianByteSwapNew(pixs)

    def capi_pix_endian_byte_swap(self, pixs: LPPix) -> int:
        return self.pixEndianByteSwap(pixs)

    def capi_line_endian_byte_swap(self, datad: c_uint_p, datas: c_uint_p,
                                   wpl: int) -> int:
        return self.lineEndianByteSwap(datad, datas, wpl)

    def capi_pix_endian_two_byte_swap_new(self, pixs: LPPix) -> LPPix:
        return self.pixEndianTwoByteSwapNew(pixs)

    def capi_pix_endian_two_byte_swap(self, pixs: LPPix) -> int:
        return self.pixEndianTwoByteSwap(pixs)

    def capi_pix_get_raster_data(self, pixs: LPPix, pdata: POINTER(c_ubyte_p),
                                 pnbytes: c_size_t_p) -> int:
        return self.pixGetRasterData(pixs, pdata, pnbytes)

    def capi_pix_infer_resolution(self, pix: LPPix, longside: float,
                                  pres: c_int_p) -> int:
        return self.pixInferResolution(pix, longside, pres)

    def capi_pix_alpha_is_opaque(self, pix: LPPix, popaque: c_int_p) -> int:
        return self.pixAlphaIsOpaque(pix, popaque)

    def capi_pix_setup_byte_processing(self, pix: LPPix, pw: c_int_p,
                                       ph: c_int_p) -> POINTER(c_ubyte_p):
        return self.pixSetupByteProcessing(pix, pw, ph)

    def capi_pix_cleanup_byte_processing(self, pix: LPPix,
                                         lineptrs: POINTER(c_ubyte_p)) -> int:
        return self.pixCleanupByteProcessing(pix, lineptrs)

    def capi_l_setAlphaMaskBorder(self, val1: float, val2: float):
        self.l_setAlphaMaskBorder(val1, val2)

    def capi_pix_set_masked(self, pixd: LPPix, pixm: LPPix, val: int) -> int:
        return self.pixSetMasked(pixd, pixm, val)

    def capi_pix_set_masked_general(self, pixd: LPPix, pixm: LPPix, val: int,
                                    x: int, y: int) -> int:
        return self.pixSetMaskedGeneral(pixd, pixm, val, x, y)

    def capi_pix_combine_masked(self, pixd: LPPix, pixs: LPPix,
                                pixm: LPPix) -> int:
        return self.pixCombineMasked(pixd, pixs, pixm)

    def capi_pix_combine_masked_general(self, pixd: LPPix, pixs: LPPix,
                                        pixm: LPPix, x: int, y: int) -> int:
        return self.pixCombineMaskedGeneral(pixd, pixs, pixm, x, y)

    def capi_pix_paint_through_mask(self, pixd: LPPix, pixm: LPPix, x: int,
                                    y: int, val: int) -> int:
        return self.pixPaintThroughMask(pixd, pixm, x, y, val)

    def capi_pix_copy_with_boxa(self, pixs: LPPix, boxa: LPBoxa,
                                background: int) -> LPPix:
        return self.pixCopyWithBoxa(pixs, boxa, background)

    def capi_pix_paint_self_through_mask(self, pixd: LPPix, pixm: LPPix,
                                         x: int, y: int, searchdir: int,
                                         mindist: int, tilesize: int,
                                         ntiles: int, distblend: int) -> int:
        return self.pixPaintSelfThroughMask(pixd, pixm, x, y, searchdir,
                                            mindist, tilesize, ntiles,
                                            distblend)

    def capi_pix_make_mask_from_val(self, pixs: LPPix, val: int) -> LPPix:
        return self.pixMakeMaskFromVal(pixs, val)

    def capi_pix_make_mask_from_lut(self, pixs: LPPix, tab: c_int_p) -> LPPix:
        return self.pixMakeMaskFromLUT(pixs, tab)

    def capi_pix_make_arb_mask_from_rgb(self, pixs: LPPix, rc: float,
                                        gc: float, bc: float,
                                        thresh: float) -> LPPix:
        return self.pixMakeArbMaskFromRGB(pixs, rc, gc, bc, thresh)

    def capi_pix_set_under_transparency(self, pixs: LPPix, val: int,
                                        debug: int) -> LPPix:
        return self.pixSetUnderTransparency(pixs, val, debug)

    def capi_pix_make_alpha_from_mask(self, pixs: LPPix, dist: int,
                                      pbox: LPLPBox) -> LPPix:
        return self.pixMakeAlphaFromMask(pixs, dist, pbox)

    def capi_pix_get_color_near_mask_boundary(self, pixs: LPPix, pixm: LPPix,
                                              box: LPBox, dist: int,
                                              pval: c_uint_p,
                                              debug: int) -> int:
        return self.pixGetColorNearMaskBoundary(pixs, pixm, box, dist, pval,
                                                debug)

    def capi_pix_display_selected_pixels(self, pixs: LPPix, pixm: LPPix,
                                         sel: LPSel, val: int) -> LPPix:
        return self.pixDisplaySelectedPixels(pixs, pixm, sel, val)

    def capi_pix_invert(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixInvert(pixd, pixs)

    def capi_pix_or(self, pixd: LPPix, pixs1: LPPix, pixs2: LPPix) -> LPPix:
        return self.pixOr(pixd, pixs1, pixs2)

    def capi_pix_and(self, pixd: LPPix, pixs1: LPPix, pixs2: LPPix) -> LPPix:
        return self.pixAnd(pixd, pixs1, pixs2)

    def capi_pix_xor(self, pixd: LPPix, pixs1: LPPix, pixs2: LPPix) -> LPPix:
        return self.pixXor(pixd, pixs1, pixs2)

    def capi_pix_subtract(self, pixd: LPPix, pixs1: LPPix,
                          pixs2: LPPix) -> LPPix:
        return self.pixSubtract(pixd, pixs1, pixs2)

    def capi_pix_zero(self, pix: LPPix, pempty: c_int_p) -> int:
        return self.pixZero(pix, pempty)

    def capi_pix_foreground_fraction(self, pix: LPPix,
                                     pfract: c_float_p) -> int:
        return self.pixForegroundFraction(pix, pfract)

    def capi_pixa_count_pixels(self, pixa: LPPixa) -> LPNuma:
        return self.pixaCountPixels(pixa)

    def capi_pix_count_pixels(self, pixs: LPPix, pcount: c_int_p,
                              tab8: c_int_p) -> int:
        return self.pixCountPixels(pixs, pcount, tab8)

    def capi_pix_count_pixels_in_rect(self, pixs: LPPix, box: LPBox,
                                      pcount: c_int_p, tab8: c_int_p) -> int:
        return self.pixCountPixelsInRect(pixs, box, pcount, tab8)

    def capi_pix_count_by_row(self, pix: LPPix, box: LPBox) -> LPNuma:
        return self.pixCountByRow(pix, box)

    def capi_pix_count_by_column(self, pix: LPPix, box: LPBox) -> LPNuma:
        return self.pixCountByColumn(pix, box)

    def capi_pix_count_pixels_by_row(self, pix: LPPix,
                                     tab8: c_int_p) -> LPNuma:
        return self.pixCountPixelsByRow(pix, tab8)

    def capi_pix_count_pixels_by_column(self, pix: LPPix) -> LPNuma:
        return self.pixCountPixelsByColumn(pix)

    def capi_pix_count_pixels_in_row(self, pix: LPPix, row: int,
                                     pcount: c_int_p, tab8: c_int_p) -> int:
        return self.pixCountPixelsInRow(pix, row, pcount, tab8)

    def capi_pix_get_moment_by_column(self, pix: LPPix, order: int) -> LPNuma:
        return self.pixGetMomentByColumn(pix, order)

    def capi_pix_threshold_pixel_sum(self, pix: LPPix, thresh: int,
                                     pabove: c_int_p, tab8: c_int_p) -> int:
        return self.pixThresholdPixelSum(pix, thresh, pabove, tab8)

    def capi_make_pixel_sum_tab8(self) -> c_int_p:
        return self.makePixelSumTab8()

    def capi_make_pixel_centroid_tab8(self) -> c_int_p:
        return self.makePixelCentroidTab8()

    def capi_pix_average_by_row(self, pix: LPPix, box: LPBox,
                                type: int) -> LPNuma:
        return self.pixAverageByRow(pix, box, type)

    def capi_pix_average_by_column(self, pix: LPPix, box: LPBox,
                                   type: int) -> LPNuma:
        return self.pixAverageByColumn(pix, box, type)

    def capi_pix_average_in_rect(self, pixs: LPPix, pixm: LPPix, box: LPBox,
                                 minval: int, maxval: int, subsamp: int,
                                 pave: c_float_p) -> int:
        return self.pixAverageInRect(pixs, pixm, box, minval, maxval, subsamp,
                                     pave)

    def capi_pix_average_in_rect_rgb(self, pixs: LPPix, pixm: LPPix,
                                     box: LPBox, subsamp: int,
                                     pave: c_uint_p) -> int:
        return self.pixAverageInRectRGB(pixs, pixm, box, subsamp, pave)

    def capi_pix_variance_by_row(self, pix: LPPix, box: LPBox) -> LPNuma:
        return self.pixVarianceByRow(pix, box)

    def capi_pix_variance_by_column(self, pix: LPPix, box: LPBox) -> LPNuma:
        return self.pixVarianceByColumn(pix, box)

    def capi_pix_variance_in_rect(self, pix: LPPix, box: LPBox,
                                  prootvar: c_float_p) -> int:
        return self.pixVarianceInRect(pix, box, prootvar)

    def capi_pix_abs_diff_by_row(self, pix: LPPix, box: LPBox) -> LPNuma:
        return self.pixAbsDiffByRow(pix, box)

    def capi_pix_abs_diff_by_column(self, pix: LPPix, box: LPBox) -> LPNuma:
        return self.pixAbsDiffByColumn(pix, box)

    def capi_pix_abs_diff_in_rect(self, pix: LPPix, box: LPBox, dir: int,
                                  pabsdiff: c_float_p) -> int:
        return self.pixAbsDiffInRect(pix, box, dir, pabsdiff)

    def capi_pix_abs_diff_on_line(self, pix: LPPix, x1: int, y1: int, x2: int,
                                  y2: int, pabsdiff: c_float_p) -> int:
        return self.pixAbsDiffOnLine(pix, x1, y1, x2, y2, pabsdiff)

    def capi_pix_count_arb_in_rect(self, pixs: LPPix, box: LPBox, val: int,
                                   factor: int, pcount: c_int_p) -> int:
        return self.pixCountArbInRect(pixs, box, val, factor, pcount)

    def capi_pix_mirrored_tiling(self, pixs: LPPix, w: int, h: int) -> LPPix:
        return self.pixMirroredTiling(pixs, w, h)

    def capi_pix_find_rep_close_tile(self, pixs: LPPix, box: LPBox,
                                     searchdir: int, mindist: int, tsize: int,
                                     ntiles: int, pboxtile: LPLPBox,
                                     debug: int) -> int:
        return self.pixFindRepCloseTile(pixs, box, searchdir, mindist, tsize,
                                        ntiles, pboxtile, debug)

    def capi_pix_get_gray_histogram(self, pixs: LPPix, factor: int) -> LPNuma:
        return self.pixGetGrayHistogram(pixs, factor)

    def capi_pix_get_gray_histogram_masked(self, pixs: LPPix, pixm: LPPix,
                                           x: int, y: int,
                                           factor: int) -> LPNuma:
        return self.pixGetGrayHistogramMasked(pixs, pixm, x, y, factor)

    def capi_pix_get_gray_histogram_in_rect(self, pixs: LPPix, box: LPBox,
                                            factor: int) -> LPNuma:
        return self.pixGetGrayHistogramInRect(pixs, box, factor)

    def capi_pix_get_gray_histogram_tiled(self, pixs: LPPix, factor: int,
                                          nx: int, ny: int) -> LPNumaa:
        return self.pixGetGrayHistogramTiled(pixs, factor, nx, ny)

    def capi_pix_get_color_histogram(self, pixs: LPPix, factor: int,
                                     pnar: LPLPNuma, pnag: LPLPNuma,
                                     pnab: LPLPNuma) -> int:
        return self.pixGetColorHistogram(pixs, factor, pnar, pnag, pnab)

    def capi_pix_get_color_histogram_masked(self, pixs: LPPix, pixm: LPPix,
                                            x: int, y: int, factor: int,
                                            pnar: LPLPNuma, pnag: LPLPNuma,
                                            pnab: LPLPNuma) -> int:
        return self.pixGetColorHistogramMasked(pixs, pixm, x, y, factor, pnar,
                                               pnag, pnab)

    def capi_pix_get_cmap_histogram(self, pixs: LPPix, factor: int) -> LPNuma:
        return self.pixGetCmapHistogram(pixs, factor)

    def capi_pix_get_cmap_histogram_masked(self, pixs: LPPix, pixm: LPPix,
                                           x: int, y: int,
                                           factor: int) -> LPNuma:
        return self.pixGetCmapHistogramMasked(pixs, pixm, x, y, factor)

    def capi_pix_get_cmap_histogram_in_rect(self, pixs: LPPix, box: LPBox,
                                            factor: int) -> LPNuma:
        return self.pixGetCmapHistogramInRect(pixs, box, factor)

    def capi_pix_count_rgb_colors_by_hash(self, pixs: LPPix,
                                          pncolors: c_int_p) -> int:
        return self.pixCountRGBColorsByHash(pixs, pncolors)

    def capi_pix_count_rgb_colors(self, pixs: LPPix, factor: int,
                                  pncolors: c_int_p) -> int:
        return self.pixCountRGBColors(pixs, factor, pncolors)

    def capi_pix_get_color_amap_histogram(self, pixs: LPPix,
                                          factor: int) -> LPL_Rbtree:
        return self.pixGetColorAmapHistogram(pixs, factor)

    def capi_amap_get_count_for_color(self, amap: LPL_Rbtree, val: int) -> int:
        return self.amapGetCountForColor(amap, val)

    def capi_pix_get_rank_value(self, pixs: LPPix, factor: int, rank: float,
                                pvalue: c_uint_p) -> int:
        return self.pixGetRankValue(pixs, factor, rank, pvalue)

    def capi_pix_get_rank_value_masked_rgb(self, pixs: LPPix, pixm: LPPix,
                                           x: int, y: int, factor: int,
                                           rank: float, prval: c_float_p,
                                           pgval: c_float_p,
                                           pbval: c_float_p) -> int:
        return self.pixGetRankValueMaskedRGB(pixs, pixm, x, y, factor, rank,
                                             prval, pgval, pbval)

    def capi_pix_get_rank_value_masked(self, pixs: LPPix, pixm: LPPix, x: int,
                                       y: int, factor: int, rank: float,
                                       pval: c_float_p, pna: LPLPNuma) -> int:
        return self.pixGetRankValueMasked(pixs, pixm, x, y, factor, rank, pval,
                                          pna)

    def capi_pix_get_pixel_average(self, pixs: LPPix, pixm: LPPix, x: int,
                                   y: int, factor: int,
                                   pval: c_uint_p) -> int:
        return self.pixGetPixelAverage(pixs, pixm, x, y, factor, pval)

    def capi_pix_get_pixel_stats(self, pixs: LPPix, factor: int, type: int,
                                 pvalue: c_uint_p) -> int:
        return self.pixGetPixelStats(pixs, factor, type, pvalue)

    def capi_pix_get_average_masked_rgb(self, pixs: LPPix, pixm: LPPix, x: int,
                                        y: int, factor: int, type: int,
                                        prval: c_float_p, pgval: c_float_p,
                                        pbval: c_float_p) -> int:
        return self.pixGetAverageMaskedRGB(pixs, pixm, x, y, factor, type,
                                           prval, pgval, pbval)

    def capi_pix_get_average_masked(self, pixs: LPPix, pixm: LPPix, x: int,
                                    y: int, factor: int, type: int,
                                    pval: c_float_p) -> int:
        return self.pixGetAverageMasked(pixs, pixm, x, y, factor, type, pval)

    def capi_pix_get_average_tiled_rgb(self, pixs: LPPix, sx: int, sy: int,
                                       type: int, ppixr: LPLPPix,
                                       ppixg: LPLPPix, ppixb: LPLPPix) -> int:
        return self.pixGetAverageTiledRGB(pixs, sx, sy, type, ppixr, ppixg,
                                          ppixb)

    def capi_pix_get_average_tiled(self, pixs: LPPix, sx: int, sy: int,
                                   type: int) -> LPPix:
        return self.pixGetAverageTiled(pixs, sx, sy, type)

    def capi_pix_row_stats(self, pixs: LPPix, box: LPBox, pnamean: LPLPNuma,
                           pnamedian: LPLPNuma, pnamode: LPLPNuma,
                           pnamodecount: LPLPNuma, pnavar: LPLPNuma,
                           pnarootvar: LPLPNuma) -> int:
        return self.pixRowStats(pixs, box, pnamean, pnamedian, pnamode,
                                pnamodecount, pnavar, pnarootvar)

    def capi_pix_column_stats(self, pixs: LPPix, box: LPBox, pnamean: LPLPNuma,
                              pnamedian: LPLPNuma, pnamode: LPLPNuma,
                              pnamodecount: LPLPNuma, pnavar: LPLPNuma,
                              pnarootvar: LPLPNuma) -> int:
        return self.pixColumnStats(pixs, box, pnamean, pnamedian, pnamode,
                                   pnamodecount, pnavar, pnarootvar)

    def capi_pix_get_range_values(self, pixs: LPPix, factor: int, color: int,
                                  pminval: c_int_p, pmaxval: c_int_p) -> int:
        return self.pixGetRangeValues(pixs, factor, color, pminval, pmaxval)

    def capi_pix_get_extreme_value(self, pixs: LPPix, factor: int, type: int,
                                   prval: c_int_p, pgval: c_int_p,
                                   pbval: c_int_p, pgrayval: c_int_p) -> int:
        return self.pixGetExtremeValue(pixs, factor, type, prval, pgval, pbval,
                                       pgrayval)

    def capi_pix_get_max_value_in_rect(self, pixs: LPPix, box: LPBox,
                                       pmaxval: c_uint_p, pxmax: c_int_p,
                                       pymax: c_int_p) -> int:
        return self.pixGetMaxValueInRect(pixs, box, pmaxval, pxmax, pymax)

    def capi_pix_get_max_color_index(self, pixs: LPPix,
                                     pmaxindex: c_int_p) -> int:
        return self.pixGetMaxColorIndex(pixs, pmaxindex)

    def capi_pix_get_binned_component_range(self, pixs: LPPix, nbins: int,
                                            factor: int, color: int,
                                            pminval: c_int_p, pmaxval: c_int_p,
                                            pcarray: POINTER(c_uint_p),
                                            fontsize: int) -> int:
        return self.pixGetBinnedComponentRange(pixs, nbins, factor, color,
                                               pminval, pmaxval, pcarray,
                                               fontsize)

    def capi_pix_get_rank_color_array(self, pixs: LPPix, nbins: int, type: int,
                                      factor: int, pcarray: POINTER(c_uint_p),
                                      pixadb: LPPixa, fontsize: int) -> int:
        return self.pixGetRankColorArray(pixs, nbins, type, factor, pcarray,
                                         pixadb, fontsize)

    def capi_pix_get_binned_color(self, pixs: LPPix, pixg: LPPix, factor: int,
                                  nbins: int, pcarray: POINTER(c_uint_p),
                                  pixadb: LPPixa) -> int:
        return self.pixGetBinnedColor(pixs, pixg, factor, nbins, pcarray,
                                      pixadb)

    def capi_pix_display_color_array(self, carray: c_uint_p, ncolors: int,
                                     side: int, ncols: int,
                                     fontsize: int) -> LPPix:
        return self.pixDisplayColorArray(carray, ncolors, side, ncols,
                                         fontsize)

    def capi_pix_rank_bin_by_strip(self, pixs: LPPix, direction: int,
                                   size: int, nbins: int, type: int) -> LPPix:
        return self.pixRankBinByStrip(pixs, direction, size, nbins, type)

    def capi_pixa_get_aligned_stats(self, pixa: LPPixa, type: int, nbins: int,
                                    thresh: int) -> LPPix:
        return self.pixaGetAlignedStats(pixa, type, nbins, thresh)

    def capi_pixa_extract_column_from_each_pix(self, pixa: LPPixa, col: int,
                                               pixd: LPPix) -> int:
        return self.pixaExtractColumnFromEachPix(pixa, col, pixd)

    def capi_pix_get_row_stats(self, pixs: LPPix, type: int, nbins: int,
                               thresh: int, colvect: c_float_p) -> int:
        return self.pixGetRowStats(pixs, type, nbins, thresh, colvect)

    def capi_pix_get_column_stats(self, pixs: LPPix, type: int, nbins: int,
                                  thresh: int, rowvect: c_float_p) -> int:
        return self.pixGetColumnStats(pixs, type, nbins, thresh, rowvect)

    def capi_pix_set_pixel_column(self, pix: LPPix, col: int,
                                  colvect: c_float_p) -> int:
        return self.pixSetPixelColumn(pix, col, colvect)

    def capi_pix_threshold_for_fg_bg(self, pixs: LPPix, factor: int,
                                     thresh: int, pfgval: c_int_p,
                                     pbgval: c_int_p) -> int:
        return self.pixThresholdForFgBg(pixs, factor, thresh, pfgval, pbgval)

    def capi_pix_split_distribution_fg_bg(self, pixs: LPPix, scorefract: float,
                                          factor: int, pthresh: c_int_p,
                                          pfgval: c_int_p, pbgval: c_int_p,
                                          ppixdb: LPLPPix) -> int:
        return self.pixSplitDistributionFgBg(pixs, scorefract, factor, pthresh,
                                             pfgval, pbgval, ppixdb)

    def capi_pixa_find_dimensions(self, pixa: LPPixa, pnaw: LPLPNuma,
                                  pnah: LPLPNuma) -> int:
        return self.pixaFindDimensions(pixa, pnaw, pnah)

    def capi_pix_find_area_perim_ratio(self, pixs: LPPix, tab: c_int_p,
                                       pfract: c_float_p) -> int:
        return self.pixFindAreaPerimRatio(pixs, tab, pfract)

    def capi_pixa_find_perim_to_area_ratio(self, pixa: LPPixa) -> LPNuma:
        return self.pixaFindPerimToAreaRatio(pixa)

    def capi_pix_find_perim_to_area_ratio(self, pixs: LPPix, tab: c_int_p,
                                          pfract: c_float_p) -> int:
        return self.pixFindPerimToAreaRatio(pixs, tab, pfract)

    def capi_pixa_find_perim_size_ratio(self, pixa: LPPixa) -> LPNuma:
        return self.pixaFindPerimSizeRatio(pixa)

    def capi_pix_find_perim_size_ratio(self, pixs: LPPix, tab: c_int_p,
                                       pratio: c_float_p) -> int:
        return self.pixFindPerimSizeRatio(pixs, tab, pratio)

    def capi_pixa_find_area_fraction(self, pixa: LPPixa) -> LPNuma:
        return self.pixaFindAreaFraction(pixa)

    def capi_pix_find_area_fraction(self, pixs: LPPix, tab: c_int_p,
                                    pfract: c_float_p) -> int:
        return self.pixFindAreaFraction(pixs, tab, pfract)

    def capi_pixa_find_area_fraction_masked(self, pixa: LPPixa, pixm: LPPix,
                                            debug: int) -> LPNuma:
        return self.pixaFindAreaFractionMasked(pixa, pixm, debug)

    def capi_pix_find_area_fraction_masked(self, pixs: LPPix, box: LPBox,
                                           pixm: LPPix, tab: c_int_p,
                                           pfract: c_float_p) -> int:
        return self.pixFindAreaFractionMasked(pixs, box, pixm, tab, pfract)

    def capi_pixa_find_width_height_ratio(self, pixa: LPPixa) -> LPNuma:
        return self.pixaFindWidthHeightRatio(pixa)

    def capi_pixa_find_width_height_product(self, pixa: LPPixa) -> LPNuma:
        return self.pixaFindWidthHeightProduct(pixa)

    def capi_pix_find_overlap_fraction(self, pixs1: LPPix, pixs2: LPPix,
                                       x2: int, y2: int, tab: c_int_p,
                                       pratio: c_float_p,
                                       pnoverlap: c_int_p) -> int:
        return self.pixFindOverlapFraction(pixs1, pixs2, x2, y2, tab, pratio,
                                           pnoverlap)

    def capi_pix_find_rectangle_comps(self, pixs: LPPix, dist: int, minw: int,
                                      minh: int) -> LPBoxa:
        return self.pixFindRectangleComps(pixs, dist, minw, minh)

    def capi_pix_conforms_to_rectangle(self, pixs: LPPix, box: LPBox,
                                       dist: int, pconforms: c_int_p) -> int:
        return self.pixConformsToRectangle(pixs, box, dist, pconforms)

    def capi_pix_clip_rectangles(self, pixs: LPPix, boxa: LPBoxa) -> LPPixa:
        return self.pixClipRectangles(pixs, boxa)

    def capi_pix_clip_rectangle(self, pixs: LPPix, box: LPBox,
                                pboxc: LPLPBox) -> LPPix:
        return self.pixClipRectangle(pixs, box, pboxc)

    def capi_pix_clip_rectangle_with_border(self, pixs: LPPix, box: LPBox,
                                            maxbord: int,
                                            pboxn: LPLPBox) -> LPPix:
        return self.pixClipRectangleWithBorder(pixs, box, maxbord, pboxn)

    def capi_pix_clip_masked(self, pixs: LPPix, pixm: LPPix, x: int, y: int,
                             outval: int) -> LPPix:
        return self.pixClipMasked(pixs, pixm, x, y, outval)

    def capi_pix_crop_to_match(self, pixs1: LPPix, pixs2: LPPix,
                               ppixd1: LPLPPix, ppixd2: LPLPPix) -> int:
        return self.pixCropToMatch(pixs1, pixs2, ppixd1, ppixd2)

    def capi_pix_crop_to_size(self, pixs: LPPix, w: int, h: int) -> LPPix:
        return self.pixCropToSize(pixs, w, h)

    def capi_pix_resize_to_match(self, pixs: LPPix, pixt: LPPix, w: int,
                                 h: int) -> LPPix:
        return self.pixResizeToMatch(pixs, pixt, w, h)

    def capi_pix_select_component_by_size(self, pixs: LPPix, rankorder: int,
                                          type: int, connectivity: int,
                                          pbox: LPLPBox) -> LPPix:
        return self.pixSelectComponentBySize(pixs, rankorder, type,
                                             connectivity, pbox)

    def capi_pix_filter_component_by_size(self, pixs: LPPix, rankorder: int,
                                          type: int, connectivity: int,
                                          pbox: LPLPBox) -> LPPix:
        return self.pixFilterComponentBySize(pixs, rankorder, type,
                                             connectivity, pbox)

    def capi_pix_make_symmetric_mask(self, w: int, h: int, hf: float,
                                     vf: float, type: int) -> LPPix:
        return self.pixMakeSymmetricMask(w, h, hf, vf, type)

    def capi_pix_make_frame_mask(self, w: int, h: int, hf1: float, hf2: float,
                                 vf1: float, vf2: float) -> LPPix:
        return self.pixMakeFrameMask(w, h, hf1, hf2, vf1, vf2)

    def capi_pix_make_covering_of_rectangles(self, pixs: LPPix,
                                             maxiters: int) -> LPPix:
        return self.pixMakeCoveringOfRectangles(pixs, maxiters)

    def capi_pix_fraction_fg_in_mask(self, pix1: LPPix, pix2: LPPix,
                                     pfract: c_float_p) -> int:
        return self.pixFractionFgInMask(pix1, pix2, pfract)

    def capi_pix_clip_to_foreground(self, pixs: LPPix, ppixd: LPLPPix,
                                    pbox: LPLPBox) -> int:
        return self.pixClipToForeground(pixs, ppixd, pbox)

    def capi_pix_test_clip_to_foreground(self, pixs: LPPix,
                                         pcanclip: c_int_p) -> int:
        return self.pixTestClipToForeground(pixs, pcanclip)

    def capi_pix_clip_box_to_foreground(self, pixs: LPPix, boxs: LPBox,
                                        ppixd: LPLPPix,
                                        pboxd: LPLPBox) -> int:
        return self.pixClipBoxToForeground(pixs, boxs, ppixd, pboxd)

    def capi_pix_scan_for_foreground(self, pixs: LPPix, box: LPBox,
                                     scanflag: int, ploc: c_int_p) -> int:
        return self.pixScanForForeground(pixs, box, scanflag, ploc)

    def capi_pix_clip_box_to_edges(self, pixs: LPPix, boxs: LPBox,
                                   lowthresh: int, highthresh: int,
                                   maxwidth: int, factor: int, ppixd: LPLPPix,
                                   pboxd: LPLPBox) -> int:
        return self.pixClipBoxToEdges(pixs, boxs, lowthresh, highthresh,
                                      maxwidth, factor, ppixd, pboxd)

    def capi_pix_scan_for_edge(self, pixs: LPPix, box: LPBox, lowthresh: int,
                               highthresh: int, maxwidth: int, factor: int,
                               scanflag: int, ploc: c_int_p) -> int:
        return self.pixScanForEdge(pixs, box, lowthresh, highthresh, maxwidth,
                                   factor, scanflag, ploc)

    def capi_pix_extract_on_line(self, pixs: LPPix, x1: int, y1: int, x2: int,
                                 y2: int, factor: int) -> LPNuma:
        return self.pixExtractOnLine(pixs, x1, y1, x2, y2, factor)

    def capi_pix_average_on_line(self, pixs: LPPix, x1: int, y1: int, x2: int,
                                 y2: int, factor: int) -> float:
        return self.pixAverageOnLine(pixs, x1, y1, x2, y2, factor)

    def capi_pix_average_intensity_profile(self, pixs: LPPix, fract: float,
                                           dir: int, first: int, last: int,
                                           factor1: int,
                                           factor2: int) -> LPNuma:
        return self.pixAverageIntensityProfile(pixs, fract, dir, first, last,
                                               factor1, factor2)

    def capi_pix_reversal_profile(self, pixs: LPPix, fract: float, dir: int,
                                  first: int, last: int, minreversal: int,
                                  factor1: int, factor2: int) -> LPNuma:
        return self.pixReversalProfile(pixs, fract, dir, first, last,
                                       minreversal, factor1, factor2)

    def capi_pix_windowed_variance_on_line(self, pixs: LPPix, dir: int,
                                           loc: int, c1: int, c2: int,
                                           size: int, pnad: LPLPNuma) -> int:
        return self.pixWindowedVarianceOnLine(pixs, dir, loc, c1, c2, size,
                                              pnad)

    def capi_pix_min_max_near_line(self, pixs: LPPix, x1: int, y1: int,
                                   x2: int, y2: int, dist: int, direction: int,
                                   pnamin: LPLPNuma, pnamax: LPLPNuma,
                                   pminave: c_float_p,
                                   pmaxave: c_float_p) -> int:
        return self.pixMinMaxNearLine(pixs, x1, y1, x2, y2, dist, direction,
                                      pnamin, pnamax, pminave, pmaxave)

    def capi_pix_rank_row_transform(self, pixs: LPPix) -> LPPix:
        return self.pixRankRowTransform(pixs)

    def capi_pix_rank_column_transform(self, pixs: LPPix) -> LPPix:
        return self.pixRankColumnTransform(pixs)

    def capi_pixa_create(self, n: int) -> LPPixa:
        return self.pixaCreate(n)

    def capi_pixa_create_from_pix(self, pixs: LPPix, n: int, cellw: int,
                                  cellh: int) -> LPPixa:
        return self.pixaCreateFromPix(pixs, n, cellw, cellh)

    def capi_pixa_create_from_boxa(self, pixs: LPPix, boxa: LPBoxa, start: int,
                                   num: int, pcropwarn: c_int_p) -> LPPixa:
        return self.pixaCreateFromBoxa(pixs, boxa, start, num, pcropwarn)

    def capi_pixa_split_pix(self, pixs: LPPix, nx: int, ny: int,
                            borderwidth: int, bordercolor: int) -> LPPixa:
        return self.pixaSplitPix(pixs, nx, ny, borderwidth, bordercolor)

    def capi_pixa_destroy(self, ppixa: LPLPPixa):
        self.pixaDestroy(ppixa)

    def capi_pixa_copy(self, pixa: LPPixa, copyflag: int) -> LPPixa:
        return self.pixaCopy(pixa, copyflag)

    def capi_pixa_add_pix(self, pixa: LPPixa, pix: LPPix,
                          copyflag: int) -> int:
        return self.pixaAddPix(pixa, pix, copyflag)

    def capi_pixa_add_box(self, pixa: LPPixa, box: LPBox,
                          copyflag: int) -> int:
        return self.pixaAddBox(pixa, box, copyflag)

    def capi_pixa_extend_array_to_size(self, pixa: LPPixa, size: int) -> int:
        return self.pixaExtendArrayToSize(pixa, size)

    def capi_pixa_get_count(self, pixa: LPPixa) -> int:
        return self.pixaGetCount(pixa)

    def capi_pixa_change_refcount(self, pixa: LPPixa, delta: int) -> int:
        return self.pixaChangeRefcount(pixa, delta)

    def capi_pixa_get_pix(self, pixa: LPPixa, index: int,
                          accesstype: int) -> LPPix:
        return self.pixaGetPix(pixa, index, accesstype)

    def capi_pixa_get_pix_dimensions(self, pixa: LPPixa, index: int,
                                     pw: c_int_p, ph: c_int_p,
                                     pd: c_int_p) -> int:
        return self.pixaGetPixDimensions(pixa, index, pw, ph, pd)

    def capi_pixa_get_boxa(self, pixa: LPPixa, accesstype: int) -> LPBoxa:
        return self.pixaGetBoxa(pixa, accesstype)

    def capi_pixa_get_boxa_count(self, pixa: LPPixa) -> int:
        return self.pixaGetBoxaCount(pixa)

    def capi_pixa_get_box(self, pixa: LPPixa, index: int,
                          accesstype: int) -> LPBox:
        return self.pixaGetBox(pixa, index, accesstype)

    def capi_pixa_get_box_geometry(self, pixa: LPPixa, index: int, px: c_int_p,
                                   py: c_int_p, pw: c_int_p,
                                   ph: c_int_p) -> int:
        return self.pixaGetBoxGeometry(pixa, index, px, py, pw, ph)

    def capi_pixa_set_boxa(self, pixa: LPPixa, boxa: LPBoxa,
                           accesstype: int) -> int:
        return self.pixaSetBoxa(pixa, boxa, accesstype)

    def capi_pixa_get_pix_array(self, pixa: LPPixa) -> LPLPPix:
        return self.pixaGetPixArray(pixa)

    def capi_pixa_verify_depth(self, pixa: LPPixa, psame: c_int_p,
                               pmaxd: c_int_p) -> int:
        return self.pixaVerifyDepth(pixa, psame, pmaxd)

    def capi_pixa_verify_dimensions(self, pixa: LPPixa, psame: c_int_p,
                                    pmaxw: c_int_p, pmaxh: c_int_p) -> int:
        return self.pixaVerifyDimensions(pixa, psame, pmaxw, pmaxh)

    def capi_pixa_is_full(self, pixa: LPPixa, pfullpa: c_int_p,
                          pfullba: c_int_p) -> int:
        return self.pixaIsFull(pixa, pfullpa, pfullba)

    def capi_pixa_count_text(self, pixa: LPPixa, pntext: c_int_p) -> int:
        return self.pixaCountText(pixa, pntext)

    def capi_pixa_set_text(self, pixa: LPPixa, text: bytes,
                           sa: LPSarray) -> int:
        return self.pixaSetText(pixa, text, sa)

    def capi_pixa_get_line_ptrs(self, pixa: LPPixa,
                                psize: c_int_p) -> POINTER(POINTER(c_void_p)):
        return self.pixaGetLinePtrs(pixa, psize)

    def capi_pixa_write_stream_info(self, fp: LPFile, pixa: LPPixa) -> int:
        return self.pixaWriteStreamInfo(fp, pixa)

    def capi_pixa_replace_pix(self, pixa: LPPixa, index: int, pix: LPPix,
                              box: LPBox) -> int:
        return self.pixaReplacePix(pixa, index, pix, box)

    def capi_pixa_insert_pix(self, pixa: LPPixa, index: int, pixs: LPPix,
                             box: LPBox) -> int:
        return self.pixaInsertPix(pixa, index, pixs, box)

    def capi_pixa_remove_pix(self, pixa: LPPixa, index: int) -> int:
        return self.pixaRemovePix(pixa, index)

    def capi_pixa_remove_pix_and_save(self, pixa: LPPixa, index: int,
                                      ppix: LPLPPix, pbox: LPLPBox) -> int:
        return self.pixaRemovePixAndSave(pixa, index, ppix, pbox)

    def capi_pixa_remove_selected(self, pixa: LPPixa, naindex: LPNuma) -> int:
        return self.pixaRemoveSelected(pixa, naindex)

    def capi_pixa_init_full(self, pixa: LPPixa, pix: LPPix, box: LPBox) -> int:
        return self.pixaInitFull(pixa, pix, box)

    def capi_pixa_clear(self, pixa: LPPixa) -> int:
        return self.pixaClear(pixa)

    def capi_pixa_join(self, pixad: LPPixa, pixas: LPPixa, istart: int,
                       iend: int) -> int:
        return self.pixaJoin(pixad, pixas, istart, iend)

    def capi_pixa_interleave(self, pixa1: LPPixa, pixa2: LPPixa,
                             copyflag: int) -> LPPixa:
        return self.pixaInterleave(pixa1, pixa2, copyflag)

    def capi_pixaa_join(self, paad: LPPixaa, paas: LPPixaa, istart: int,
                        iend: int) -> int:
        return self.pixaaJoin(paad, paas, istart, iend)

    def capi_pixaa_create(self, n: int) -> LPPixaa:
        return self.pixaaCreate(n)

    def capi_pixaa_create_from_pixa(self, pixa: LPPixa, n: int, type: int,
                                    copyflag: int) -> LPPixaa:
        return self.pixaaCreateFromPixa(pixa, n, type, copyflag)

    def capi_pixaa_destroy(self, ppaa: LPLPPixaa):
        self.pixaaDestroy(ppaa)

    def capi_pixaa_add_pixa(self, paa: LPPixaa, pixa: LPPixa,
                            copyflag: int) -> int:
        return self.pixaaAddPixa(paa, pixa, copyflag)

    def capi_pixaa_add_pix(self, paa: LPPixaa, index: int, pix: LPPix,
                           box: LPBox, copyflag: int) -> int:
        return self.pixaaAddPix(paa, index, pix, box, copyflag)

    def capi_pixaa_add_box(self, paa: LPPixaa, box: LPBox,
                           copyflag: int) -> int:
        return self.pixaaAddBox(paa, box, copyflag)

    def capi_pixaa_get_count(self, paa: LPPixaa, pna: LPLPNuma) -> int:
        return self.pixaaGetCount(paa, pna)

    def capi_pixaa_get_pixa(self, paa: LPPixaa, index: int,
                            accesstype: int) -> LPPixa:
        return self.pixaaGetPixa(paa, index, accesstype)

    def capi_pixaa_get_boxa(self, paa: LPPixaa, accesstype: int) -> LPBoxa:
        return self.pixaaGetBoxa(paa, accesstype)

    def capi_pixaa_get_pix(self, paa: LPPixaa, index: int, ipix: int,
                           accessflag: int) -> LPPix:
        return self.pixaaGetPix(paa, index, ipix, accessflag)

    def capi_pixaa_verify_depth(self, paa: LPPixaa, psame: c_int_p,
                                pmaxd: c_int_p) -> int:
        return self.pixaaVerifyDepth(paa, psame, pmaxd)

    def capi_pixaa_verify_dimensions(self, paa: LPPixaa, psame: c_int_p,
                                     pmaxw: c_int_p, pmaxh: c_int_p) -> int:
        return self.pixaaVerifyDimensions(paa, psame, pmaxw, pmaxh)

    def capi_pixaa_is_full(self, paa: LPPixaa, pfull: c_int_p) -> int:
        return self.pixaaIsFull(paa, pfull)

    def capi_pixaa_init_full(self, paa: LPPixaa, pixa: LPPixa) -> int:
        return self.pixaaInitFull(paa, pixa)

    def capi_pixaa_replace_pixa(self, paa: LPPixaa, index: int,
                                pixa: LPPixa) -> int:
        return self.pixaaReplacePixa(paa, index, pixa)

    def capi_pixaa_clear(self, paa: LPPixaa) -> int:
        return self.pixaaClear(paa)

    def capi_pixaa_truncate(self, paa: LPPixaa) -> int:
        return self.pixaaTruncate(paa)

    def capi_pixa_read(self, filename: bytes) -> LPPixa:
        return self.pixaRead(filename)

    def capi_pixa_read_stream(self, fp: LPFile) -> LPPixa:
        return self.pixaReadStream(fp)

    def capi_pixa_read_mem(self, data: c_ubyte_p, size: int) -> LPPixa:
        return self.pixaReadMem(data, size)

    def capi_pixa_write_debug(self, fname: bytes, pixa: LPPixa) -> int:
        return self.pixaWriteDebug(fname, pixa)

    def capi_pixa_write(self, filename: bytes, pixa: LPPixa) -> int:
        return self.pixaWrite(filename, pixa)

    def capi_pixa_write_stream(self, fp: LPFile, pixa: LPPixa) -> int:
        return self.pixaWriteStream(fp, pixa)

    def capi_pixa_write_mem(self, pdata: POINTER(c_ubyte_p), psize: c_size_t_p,
                            pixa: LPPixa) -> int:
        return self.pixaWriteMem(pdata, psize, pixa)

    def capi_pixa_read_both(self, filename: bytes) -> LPPixa:
        return self.pixaReadBoth(filename)

    def capi_pixaa_read_from_files(self, dirname: bytes, substr: bytes,
                                   first: int, nfiles: int) -> LPPixaa:
        return self.pixaaReadFromFiles(dirname, substr, first, nfiles)

    def capi_pixaa_read(self, filename: bytes) -> LPPixaa:
        return self.pixaaRead(filename)

    def capi_pixaa_read_stream(self, fp: LPFile) -> LPPixaa:
        return self.pixaaReadStream(fp)

    def capi_pixaa_read_mem(self, data: c_ubyte_p, size: int) -> LPPixaa:
        return self.pixaaReadMem(data, size)

    def capi_pixaa_write(self, filename: bytes, paa: LPPixaa) -> int:
        return self.pixaaWrite(filename, paa)

    def capi_pixaa_write_stream(self, fp: LPFile, paa: LPPixaa) -> int:
        return self.pixaaWriteStream(fp, paa)

    def capi_pixaa_write_mem(self, pdata: POINTER(c_ubyte_p),
                             psize: c_size_t_p, paa: LPPixaa) -> int:
        return self.pixaaWriteMem(pdata, psize, paa)

    def capi_pixacc_create(self, w: int, h: int, negflag: int) -> LPPixacc:
        return self.pixaccCreate(w, h, negflag)

    def capi_pixacc_create_from_pix(self, pix: LPPix,
                                    negflag: int) -> LPPixacc:
        return self.pixaccCreateFromPix(pix, negflag)

    def capi_pixacc_destroy(self, ppixacc: LPLPPixacc):
        self.pixaccDestroy(ppixacc)

    def capi_pixacc_final(self, pixacc: LPPixacc, outdepth: int) -> LPPix:
        return self.pixaccFinal(pixacc, outdepth)

    def capi_pixacc_get_pix(self, pixacc: LPPixacc) -> LPPix:
        return self.pixaccGetPix(pixacc)

    def capi_pixacc_get_offset(self, pixacc: LPPixacc) -> int:
        return self.pixaccGetOffset(pixacc)

    def capi_pixacc_add(self, pixacc: LPPixacc, pix: LPPix) -> int:
        return self.pixaccAdd(pixacc, pix)

    def capi_pixacc_subtract(self, pixacc: LPPixacc, pix: LPPix) -> int:
        return self.pixaccSubtract(pixacc, pix)

    def capi_pixacc_mult_const(self, pixacc: LPPixacc, factor: float) -> int:
        return self.pixaccMultConst(pixacc, factor)

    def capi_pixacc_mult_const_accumulate(self, pixacc: LPPixacc, pix: LPPix,
                                          factor: float) -> int:
        return self.pixaccMultConstAccumulate(pixacc, pix, factor)

    def capi_pix_select_by_size(self, pixs: LPPix, width: int, height: int,
                                connectivity: int, type: int, relation: int,
                                pchanged: c_int_p) -> LPPix:
        return self.pixSelectBySize(pixs, width, height, connectivity, type,
                                    relation, pchanged)

    def capi_pixa_select_by_size(self, pixas: LPPixa, width: int, height: int,
                                 type: int, relation: int,
                                 pchanged: c_int_p) -> LPPixa:
        return self.pixaSelectBySize(pixas, width, height, type, relation,
                                     pchanged)

    def capi_pixa_make_size_indicator(self, pixa: LPPixa, width: int,
                                      height: int, type: int,
                                      relation: int) -> LPNuma:
        return self.pixaMakeSizeIndicator(pixa, width, height, type, relation)

    def capi_pix_select_by_perim_to_area_ratio(self, pixs: LPPix,
                                               thresh: float,
                                               connectivity: int, type: int,
                                               pchanged: c_int_p) -> LPPix:
        return self.pixSelectByPerimToAreaRatio(pixs, thresh, connectivity,
                                                type, pchanged)

    def capi_pixa_select_by_perim_to_area_ratio(self, pixas: LPPixa,
                                                thresh: float, type: int,
                                                pchanged: c_int_p) -> LPPixa:
        return self.pixaSelectByPerimToAreaRatio(pixas, thresh, type, pchanged)

    def capi_pix_select_by_perim_size_ratio(self, pixs: LPPix, thresh: float,
                                            connectivity: int, type: int,
                                            pchanged: c_int_p) -> LPPix:
        return self.pixSelectByPerimSizeRatio(pixs, thresh, connectivity, type,
                                              pchanged)

    def capi_pixa_select_by_perim_size_ratio(self, pixas: LPPixa,
                                             thresh: float, type: int,
                                             pchanged: c_int_p) -> LPPixa:
        return self.pixaSelectByPerimSizeRatio(pixas, thresh, type, pchanged)

    def capi_pix_select_by_area_fraction(self, pixs: LPPix, thresh: float,
                                         connectivity: int, type: int,
                                         pchanged: c_int_p) -> LPPix:
        return self.pixSelectByAreaFraction(pixs, thresh, connectivity, type,
                                            pchanged)

    def capi_pixa_select_by_area_fraction(self, pixas: LPPixa, thresh: float,
                                          type: int,
                                          pchanged: c_int_p) -> LPPixa:
        return self.pixaSelectByAreaFraction(pixas, thresh, type, pchanged)

    def capi_pix_select_by_area(self, pixs: LPPix, thresh: float,
                                connectivity: int, type: int,
                                pchanged: c_int_p) -> LPPix:
        return self.pixSelectByArea(pixs, thresh, connectivity, type, pchanged)

    def capi_pixa_select_by_area(self, pixas: LPPixa, thresh: float, type: int,
                                 pchanged: c_int_p) -> LPPixa:
        return self.pixaSelectByArea(pixas, thresh, type, pchanged)

    def capi_pix_select_by_width_height_ratio(self, pixs: LPPix, thresh: float,
                                              connectivity: int, type: int,
                                              pchanged: c_int_p) -> LPPix:
        return self.pixSelectByWidthHeightRatio(pixs, thresh, connectivity,
                                                type, pchanged)

    def capi_pixa_select_by_width_height_ratio(self, pixas: LPPixa,
                                               thresh: float, type: int,
                                               pchanged: c_int_p) -> LPPixa:
        return self.pixaSelectByWidthHeightRatio(pixas, thresh, type, pchanged)

    def capi_pixa_select_by_num_conn_comp(self, pixas: LPPixa, nmin: int,
                                          nmax: int, connectivity: int,
                                          pchanged: c_int_p) -> LPPixa:
        return self.pixaSelectByNumConnComp(pixas, nmin, nmax, connectivity,
                                            pchanged)

    def capi_pixa_select_with_indicator(self, pixas: LPPixa, na: LPNuma,
                                        pchanged: c_int_p) -> LPPixa:
        return self.pixaSelectWithIndicator(pixas, na, pchanged)

    def capi_pix_remove_with_indicator(self, pixs: LPPix, pixa: LPPixa,
                                       na: LPNuma) -> int:
        return self.pixRemoveWithIndicator(pixs, pixa, na)

    def capi_pix_add_with_indicator(self, pixs: LPPix, pixa: LPPixa,
                                    na: LPNuma) -> int:
        return self.pixAddWithIndicator(pixs, pixa, na)

    def capi_pixa_select_with_string(self, pixas: LPPixa, str: bytes,
                                     perror: c_int_p) -> LPPixa:
        return self.pixaSelectWithString(pixas, str, perror)

    def capi_pixa_render_component(self, pixs: LPPix, pixa: LPPixa,
                                   index: int) -> LPPix:
        return self.pixaRenderComponent(pixs, pixa, index)

    def capi_pixa_sort(self, pixas: LPPixa, sorttype: int, sortorder: int,
                       pnaindex: LPLPNuma, copyflag: int) -> LPPixa:
        return self.pixaSort(pixas, sorttype, sortorder, pnaindex, copyflag)

    def capi_pixa_bin_sort(self, pixas: LPPixa, sorttype: int, sortorder: int,
                           pnaindex: LPLPNuma, copyflag: int) -> LPPixa:
        return self.pixaBinSort(pixas, sorttype, sortorder, pnaindex, copyflag)

    def capi_pixa_sort_by_index(self, pixas: LPPixa, naindex: LPNuma,
                                copyflag: int) -> LPPixa:
        return self.pixaSortByIndex(pixas, naindex, copyflag)

    def capi_pixa_sort2d_by_index(self, pixas: LPPixa, naa: LPNumaa,
                                  copyflag: int) -> LPPixaa:
        return self.pixaSort2dByIndex(pixas, naa, copyflag)

    def capi_pixa_select_range(self, pixas: LPPixa, first: int, last: int,
                               copyflag: int) -> LPPixa:
        return self.pixaSelectRange(pixas, first, last, copyflag)

    def capi_pixaa_select_range(self, paas: LPPixaa, first: int, last: int,
                                copyflag: int) -> LPPixaa:
        return self.pixaaSelectRange(paas, first, last, copyflag)

    def capi_pixaa_scale_to_size(self, paas: LPPixaa, wd: int,
                                 hd: int) -> LPPixaa:
        return self.pixaaScaleToSize(paas, wd, hd)

    def capi_pixaa_scale_to_size_var(self, paas: LPPixaa, nawd: LPNuma,
                                     nahd: LPNuma) -> LPPixaa:
        return self.pixaaScaleToSizeVar(paas, nawd, nahd)

    def capi_pixa_scale_to_size(self, pixas: LPPixa, wd: int,
                                hd: int) -> LPPixa:
        return self.pixaScaleToSize(pixas, wd, hd)

    def capi_pixa_scale_to_size_rel(self, pixas: LPPixa, delw: int,
                                    delh: int) -> LPPixa:
        return self.pixaScaleToSizeRel(pixas, delw, delh)

    def capi_pixa_scale(self, pixas: LPPixa, scalex: float,
                        scaley: float) -> LPPixa:
        return self.pixaScale(pixas, scalex, scaley)

    def capi_pixa_scale_by_sampling(self, pixas: LPPixa, scalex: float,
                                    scaley: float) -> LPPixa:
        return self.pixaScaleBySampling(pixas, scalex, scaley)

    def capi_pixa_rotate(self, pixas: LPPixa, angle: float, type: int,
                         incolor: int, width: int, height: int) -> LPPixa:
        return self.pixaRotate(pixas, angle, type, incolor, width, height)

    def capi_pixa_rotate_orth(self, pixas: LPPixa, rotation: int) -> LPPixa:
        return self.pixaRotateOrth(pixas, rotation)

    def capi_pixa_translate(self, pixas: LPPixa, hshift: int, vshift: int,
                            incolor: int) -> LPPixa:
        return self.pixaTranslate(pixas, hshift, vshift, incolor)

    def capi_pixa_add_border_general(self, pixad: LPPixa, pixas: LPPixa,
                                     left: int, right: int, top: int, bot: int,
                                     val: int) -> LPPixa:
        return self.pixaAddBorderGeneral(pixad, pixas, left, right, top, bot,
                                         val)

    def capi_pixaa_flatten_to_pixa(self, paa: LPPixaa, pnaindex: LPLPNuma,
                                   copyflag: int) -> LPPixa:
        return self.pixaaFlattenToPixa(paa, pnaindex, copyflag)

    def capi_pixaa_size_range(self, paa: LPPixaa, pminw: c_int_p,
                              pminh: c_int_p, pmaxw: c_int_p,
                              pmaxh: c_int_p) -> int:
        return self.pixaaSizeRange(paa, pminw, pminh, pmaxw, pmaxh)

    def capi_pixa_size_range(self, pixa: LPPixa, pminw: c_int_p,
                             pminh: c_int_p, pmaxw: c_int_p,
                             pmaxh: c_int_p) -> int:
        return self.pixaSizeRange(pixa, pminw, pminh, pmaxw, pmaxh)

    def capi_pixa_clip_to_pix(self, pixas: LPPixa, pixs: LPPix) -> LPPixa:
        return self.pixaClipToPix(pixas, pixs)

    def capi_pixa_clip_to_foreground(self, pixas: LPPixa, ppixad: LPLPPixa,
                                     pboxa: LPLPBoxa) -> int:
        return self.pixaClipToForeground(pixas, ppixad, pboxa)

    def capi_pixa_get_rendering_depth(self, pixa: LPPixa,
                                      pdepth: c_int_p) -> int:
        return self.pixaGetRenderingDepth(pixa, pdepth)

    def capi_pixa_has_color(self, pixa: LPPixa, phascolor: c_int_p) -> int:
        return self.pixaHasColor(pixa, phascolor)

    def capi_pixa_any_colormaps(self, pixa: LPPixa, phascmap: c_int_p) -> int:
        return self.pixaAnyColormaps(pixa, phascmap)

    def capi_pixa_get_depth_info(self, pixa: LPPixa, pmaxdepth: c_int_p,
                                 psame: c_int_p) -> int:
        return self.pixaGetDepthInfo(pixa, pmaxdepth, psame)

    def capi_pixa_convert_to_same_depth(self, pixas: LPPixa) -> LPPixa:
        return self.pixaConvertToSameDepth(pixas)

    def capi_pixa_convert_to_given_depth(self, pixas: LPPixa,
                                         depth: int) -> LPPixa:
        return self.pixaConvertToGivenDepth(pixas, depth)

    def capi_pixa_equal(self, pixa1: LPPixa, pixa2: LPPixa, maxdist: int,
                        pnaindex: LPLPNuma, psame: c_int_p) -> int:
        return self.pixaEqual(pixa1, pixa2, maxdist, pnaindex, psame)

    def capi_pixa_set_full_size_boxa(self, pixa: LPPixa) -> int:
        return self.pixaSetFullSizeBoxa(pixa)

    def capi_pixa_display(self, pixa: LPPixa, w: int, h: int) -> LPPix:
        return self.pixaDisplay(pixa, w, h)

    def capi_pixa_display_random_cmap(self, pixa: LPPixa, w: int,
                                      h: int) -> LPPix:
        return self.pixaDisplayRandomCmap(pixa, w, h)

    def capi_pixa_display_linearly(self, pixas: LPPixa, direction: int,
                                   scalefactor: float, background: int,
                                   spacing: int, border: int,
                                   pboxa: LPLPBoxa) -> LPPix:
        return self.pixaDisplayLinearly(pixas, direction, scalefactor,
                                        background, spacing, border, pboxa)

    def capi_pixa_display_on_lattice(self, pixa: LPPixa, cellw: int,
                                     cellh: int, pncols: c_int_p,
                                     pboxa: LPLPBoxa) -> LPPix:
        return self.pixaDisplayOnLattice(pixa, cellw, cellh, pncols, pboxa)

    def capi_pixa_display_unsplit(self, pixa: LPPixa, nx: int, ny: int,
                                  borderwidth: int,
                                  bordercolor: int) -> LPPix:
        return self.pixaDisplayUnsplit(pixa, nx, ny, borderwidth, bordercolor)

    def capi_pixa_display_tiled(self, pixa: LPPixa, maxwidth: int,
                                background: int, spacing: int) -> LPPix:
        return self.pixaDisplayTiled(pixa, maxwidth, background, spacing)

    def capi_pixa_display_tiled_in_rows(self, pixa: LPPixa, outdepth: int,
                                        maxwidth: int, scalefactor: float,
                                        background: int, spacing: int,
                                        border: int) -> LPPix:
        return self.pixaDisplayTiledInRows(pixa, outdepth, maxwidth,
                                           scalefactor, background, spacing,
                                           border)

    def capi_pixa_display_tiled_in_columns(self, pixas: LPPixa, nx: int,
                                           scalefactor: float, spacing: int,
                                           border: int) -> LPPix:
        return self.pixaDisplayTiledInColumns(pixas, nx, scalefactor, spacing,
                                              border)

    def capi_pixa_display_tiled_and_scaled(self, pixa: LPPixa, outdepth: int,
                                           tilewidth: int, ncols: int,
                                           background: int, spacing: int,
                                           border: int) -> LPPix:
        return self.pixaDisplayTiledAndScaled(pixa, outdepth, tilewidth, ncols,
                                              background, spacing, border)

    def capi_pixa_display_tiled_with_text(self, pixa: LPPixa, maxwidth: int,
                                          scalefactor: float, spacing: int,
                                          border: int, fontsize: int,
                                          textcolor: int) -> LPPix:
        return self.pixaDisplayTiledWithText(pixa, maxwidth, scalefactor,
                                             spacing, border, fontsize,
                                             textcolor)

    def capi_pixa_display_tiled_by_index(self, pixa: LPPixa, na: LPNuma,
                                         width: int, spacing: int, border: int,
                                         fontsize: int,
                                         textcolor: int) -> LPPix:
        return self.pixaDisplayTiledByIndex(pixa, na, width, spacing, border,
                                            fontsize, textcolor)

    def capi_pixa_display_pair_tiled_in_columns(self, pixas1: LPPixa,
                                                pixas2: LPPixa, nx: int,
                                                scalefactor: float,
                                                spacing1: int, spacing2: int,
                                                border1: int, border2: int,
                                                fontsize: int, startindex: int,
                                                sa: LPSarray) -> LPPix:
        return self.pixaDisplayPairTiledInColumns(pixas1, pixas2, nx,
                                                  scalefactor, spacing1,
                                                  spacing2, border1, border2,
                                                  fontsize, startindex, sa)

    def capi_pixaa_display(self, paa: LPPixaa, w: int, h: int) -> LPPix:
        return self.pixaaDisplay(paa, w, h)

    def capi_pixaa_display_by_pixa(self, paa: LPPixaa, maxnx: int,
                                   scalefactor: float, hspacing: int,
                                   vspacing: int, border: int) -> LPPix:
        return self.pixaaDisplayByPixa(paa, maxnx, scalefactor, hspacing,
                                       vspacing, border)

    def capi_pixaa_display_tiled_and_scaled(self, paa: LPPixaa, outdepth: int,
                                            tilewidth: int, ncols: int,
                                            background: int, spacing: int,
                                            border: int) -> LPPixa:
        return self.pixaaDisplayTiledAndScaled(paa, outdepth, tilewidth, ncols,
                                               background, spacing, border)

    def capi_pixa_convert_to1(self, pixas: LPPixa, thresh: int) -> LPPixa:
        return self.pixaConvertTo1(pixas, thresh)

    def capi_pixa_convert_to8(self, pixas: LPPixa, cmapflag: int) -> LPPixa:
        return self.pixaConvertTo8(pixas, cmapflag)

    def capi_pixa_convert_to8colormap(self, pixas: LPPixa,
                                      dither: int) -> LPPixa:
        return self.pixaConvertTo8Colormap(pixas, dither)

    def capi_pixa_convert_to32(self, pixas: LPPixa) -> LPPixa:
        return self.pixaConvertTo32(pixas)

    def capi_pixa_constrained_select(self, pixas: LPPixa, first: int,
                                     last: int, nmax: int, use_pairs: int,
                                     copyflag: int) -> LPPixa:
        return self.pixaConstrainedSelect(pixas, first, last, nmax, use_pairs,
                                          copyflag)

    def capi_pixa_select_to_pdf(self, pixas: LPPixa, first: int, last: int,
                                res: int, scalefactor: float, type: int,
                                quality: int, color: int, fontsize: int,
                                fileout: bytes) -> int:
        return self.pixaSelectToPdf(pixas, first, last, res, scalefactor, type,
                                    quality, color, fontsize, fileout)

    def capi_pixa_make_from_tiled_pixa(self, pixas: LPPixa, w: int, h: int,
                                       nsamp: int) -> LPPixa:
        return self.pixaMakeFromTiledPixa(pixas, w, h, nsamp)

    def capi_pixa_make_from_tiled_pix(self, pixs: LPPix, w: int, h: int,
                                      start: int, num: int,
                                      boxa: LPBoxa) -> LPPixa:
        return self.pixaMakeFromTiledPix(pixs, w, h, start, num, boxa)

    def capi_pix_get_tile_count(self, pix: LPPix, pn: c_int_p) -> int:
        return self.pixGetTileCount(pix, pn)

    def capi_pixa_display_multi_tiled(self, pixas: LPPixa, nx: int, ny: int,
                                      maxw: int, maxh: int, scalefactor: float,
                                      spacing: int, border: int) -> LPPixa:
        return self.pixaDisplayMultiTiled(pixas, nx, ny, maxw, maxh,
                                          scalefactor, spacing, border)

    def capi_pixa_split_into_files(self, pixas: LPPixa, nsplit: int,
                                   scale: float, outwidth: int,
                                   write_pixa: int, write_pix: int,
                                   write_pdf: int) -> int:
        return self.pixaSplitIntoFiles(pixas, nsplit, scale, outwidth,
                                       write_pixa, write_pix, write_pdf)

    def capi_convert_to_nup_files(self, dir: bytes, substr: bytes, nx: int,
                                  ny: int, tw: int, spacing: int, border: int,
                                  fontsize: int, outdir: bytes) -> int:
        return self.convertToNUpFiles(dir, substr, nx, ny, tw, spacing, border,
                                      fontsize, outdir)

    def capi_convert_to_nup_pixa(self, dir: bytes, substr: bytes, nx: int,
                                 ny: int, tw: int, spacing: int, border: int,
                                 fontsize: int) -> LPPixa:
        return self.convertToNUpPixa(dir, substr, nx, ny, tw, spacing, border,
                                     fontsize)

    def capi_pixa_convert_to_nup_pixa(self, pixas: LPPixa, sa: LPSarray,
                                      nx: int, ny: int, tw: int, spacing: int,
                                      border: int, fontsize: int) -> LPPixa:
        return self.pixaConvertToNUpPixa(pixas, sa, nx, ny, tw, spacing,
                                         border, fontsize)

    def capi_pixa_compare_in_pdf(self, pixa1: LPPixa, pixa2: LPPixa, nx: int,
                                 ny: int, tw: int, spacing: int, border: int,
                                 fontsize: int, fileout: bytes) -> int:
        return self.pixaCompareInPdf(pixa1, pixa2, nx, ny, tw, spacing, border,
                                     fontsize, fileout)

    def capi_pms_create(self, minsize: int, smallest: int, numalloc: LPNuma,
                        logfile: bytes) -> int:
        return self.pmsCreate(minsize, smallest, numalloc, logfile)

    def capi_pms_destroy(self):
        self.pmsDestroy()

    def capi_pms_custom_alloc(self, nbytes: int) -> c_void_p:
        return self.pmsCustomAlloc(nbytes)

    def capi_pms_custom_dealloc(self, data: c_void_p):
        self.pmsCustomDealloc(data)

    def capi_pms_get_alloc(self, nbytes: int) -> c_void_p:
        return self.pmsGetAlloc(nbytes)

    def capi_pms_get_level_for_alloc(self, nbytes: int,
                                     plevel: c_int_p) -> int:
        return self.pmsGetLevelForAlloc(nbytes, plevel)

    def capi_pms_get_level_for_dealloc(self, data: c_void_p,
                                       plevel: c_int_p) -> int:
        return self.pmsGetLevelForDealloc(data, plevel)

    def capi_pms_log_info(self):
        self.pmsLogInfo()

    def capi_pix_add_constant_gray(self, pixs: LPPix, val: int) -> int:
        return self.pixAddConstantGray(pixs, val)

    def capi_pix_mult_constant_gray(self, pixs: LPPix, val: float) -> int:
        return self.pixMultConstantGray(pixs, val)

    def capi_pix_add_gray(self, pixd: LPPix, pixs1: LPPix,
                          pixs2: LPPix) -> LPPix:
        return self.pixAddGray(pixd, pixs1, pixs2)

    def capi_pix_subtract_gray(self, pixd: LPPix, pixs1: LPPix,
                               pixs2: LPPix) -> LPPix:
        return self.pixSubtractGray(pixd, pixs1, pixs2)

    def capi_pix_multiply_gray(self, pixs: LPPix, pixg: LPPix,
                               norm: float) -> LPPix:
        return self.pixMultiplyGray(pixs, pixg, norm)

    def capi_pix_threshold_to_value(self, pixd: LPPix, pixs: LPPix,
                                    threshval: int, setval: int) -> LPPix:
        return self.pixThresholdToValue(pixd, pixs, threshval, setval)

    def capi_pix_init_accumulate(self, w: int, h: int, offset: int) -> LPPix:
        return self.pixInitAccumulate(w, h, offset)

    def capi_pix_final_accumulate(self, pixs: LPPix, offset: int,
                                  depth: int) -> LPPix:
        return self.pixFinalAccumulate(pixs, offset, depth)

    def capi_pix_final_accumulate_threshold(self, pixs: LPPix, offset: int,
                                            threshold: int) -> LPPix:
        return self.pixFinalAccumulateThreshold(pixs, offset, threshold)

    def capi_pix_accumulate(self, pixd: LPPix, pixs: LPPix, op: int) -> int:
        return self.pixAccumulate(pixd, pixs, op)

    def capi_pix_mult_const_accumulate(self, pixs: LPPix, factor: float,
                                       offset: int) -> int:
        return self.pixMultConstAccumulate(pixs, factor, offset)

    def capi_pix_abs_difference(self, pixs1: LPPix, pixs2: LPPix) -> LPPix:
        return self.pixAbsDifference(pixs1, pixs2)

    def capi_pix_add_rgb(self, pixs1: LPPix, pixs2: LPPix) -> LPPix:
        return self.pixAddRGB(pixs1, pixs2)

    def capi_pix_min_or_max(self, pixd: LPPix, pixs1: LPPix, pixs2: LPPix,
                            type: int) -> LPPix:
        return self.pixMinOrMax(pixd, pixs1, pixs2, type)

    def capi_pix_max_dynamic_range(self, pixs: LPPix, type: int) -> LPPix:
        return self.pixMaxDynamicRange(pixs, type)

    def capi_pix_max_dynamic_range_rgb(self, pixs: LPPix, type: int) -> LPPix:
        return self.pixMaxDynamicRangeRGB(pixs, type)

    def capi_linear_scale_rgb_val(self, sval: int, factor: float) -> int:
        return self.linearScaleRGBVal(sval, factor)

    def capi_log_scale_rgb_val(self, sval: int, tab: c_float_p,
                               factor: float) -> int:
        return self.logScaleRGBVal(sval, tab, factor)

    def capi_make_log_base2tab(self) -> c_float_p:
        return self.makeLogBase2Tab()

    def capi_get_log_base2(self, val: int, logtab: c_float_p) -> float:
        return self.getLogBase2(val, logtab)

    def capi_pixcomp_create_from_pix(self, pix: LPPix,
                                     comptype: int) -> LPPixComp:
        return self.pixcompCreateFromPix(pix, comptype)

    def capi_pixcomp_create_from_string(self, data: c_ubyte_p, size: int,
                                        copyflag: int) -> LPPixComp:
        return self.pixcompCreateFromString(data, size, copyflag)

    def capi_pixcomp_create_from_file(self, filename: bytes,
                                      comptype: int) -> LPPixComp:
        return self.pixcompCreateFromFile(filename, comptype)

    def capi_pixcomp_destroy(self, ppixc: LPLPPixComp):
        self.pixcompDestroy(ppixc)

    def capi_pixcomp_copy(self, pixcs: LPPixComp) -> LPPixComp:
        return self.pixcompCopy(pixcs)

    def capi_pixcomp_get_dimensions(self, pixc: LPPixComp, pw: c_int_p,
                                    ph: c_int_p, pd: c_int_p) -> int:
        return self.pixcompGetDimensions(pixc, pw, ph, pd)

    def capi_pixcomp_get_parameters(self, pixc: LPPixComp, pxres: c_int_p,
                                    pyres: c_int_p, pcomptype: c_int_p,
                                    pcmapflag: c_int_p) -> int:
        return self.pixcompGetParameters(pixc, pxres, pyres, pcomptype,
                                         pcmapflag)

    def capi_pixcomp_determine_format(self, comptype: int, d: int,
                                      cmapflag: int, pformat: c_int_p) -> int:
        return self.pixcompDetermineFormat(comptype, d, cmapflag, pformat)

    def capi_pix_create_from_pixcomp(self, pixc: LPPixComp) -> LPPix:
        return self.pixCreateFromPixcomp(pixc)

    def capi_pixacomp_create(self, n: int) -> LPPixaComp:
        return self.pixacompCreate(n)

    def capi_pixacomp_create_with_init(self, n: int, offset: int, pix: LPPix,
                                       comptype: int) -> LPPixaComp:
        return self.pixacompCreateWithInit(n, offset, pix, comptype)

    def capi_pixacomp_create_from_pixa(self, pixa: LPPixa, comptype: int,
                                       accesstype: int) -> LPPixaComp:
        return self.pixacompCreateFromPixa(pixa, comptype, accesstype)

    def capi_pixacomp_create_from_files(self, dirname: bytes, substr: bytes,
                                        comptype: int) -> LPPixaComp:
        return self.pixacompCreateFromFiles(dirname, substr, comptype)

    def capi_pixacomp_create_from_sa(self, sa: LPSarray,
                                     comptype: int) -> LPPixaComp:
        return self.pixacompCreateFromSA(sa, comptype)

    def capi_pixacomp_destroy(self, ppixac: LPLPPixaComp):
        self.pixacompDestroy(ppixac)

    def capi_pixacomp_add_pix(self, pixac: LPPixaComp, pix: LPPix,
                              comptype: int) -> int:
        return self.pixacompAddPix(pixac, pix, comptype)

    def capi_pixacomp_add_pixcomp(self, pixac: LPPixaComp, pixc: LPPixComp,
                                  copyflag: int) -> int:
        return self.pixacompAddPixcomp(pixac, pixc, copyflag)

    def capi_pixacomp_replace_pix(self, pixac: LPPixaComp, index: int,
                                  pix: LPPix, comptype: int) -> int:
        return self.pixacompReplacePix(pixac, index, pix, comptype)

    def capi_pixacomp_replace_pixcomp(self, pixac: LPPixaComp, index: int,
                                      pixc: LPPixComp) -> int:
        return self.pixacompReplacePixcomp(pixac, index, pixc)

    def capi_pixacomp_add_box(self, pixac: LPPixaComp, box: LPBox,
                              copyflag: int) -> int:
        return self.pixacompAddBox(pixac, box, copyflag)

    def capi_pixacomp_get_count(self, pixac: LPPixaComp) -> int:
        return self.pixacompGetCount(pixac)

    def capi_pixacomp_get_pixcomp(self, pixac: LPPixaComp, index: int,
                                  copyflag: int) -> LPPixComp:
        return self.pixacompGetPixcomp(pixac, index, copyflag)

    def capi_pixacomp_get_pix(self, pixac: LPPixaComp, index: int) -> LPPix:
        return self.pixacompGetPix(pixac, index)

    def capi_pixacomp_get_pix_dimensions(self, pixac: LPPixaComp, index: int,
                                         pw: c_int_p, ph: c_int_p,
                                         pd: c_int_p) -> int:
        return self.pixacompGetPixDimensions(pixac, index, pw, ph, pd)

    def capi_pixacomp_get_boxa(self, pixac: LPPixaComp,
                               accesstype: int) -> LPBoxa:
        return self.pixacompGetBoxa(pixac, accesstype)

    def capi_pixacomp_get_boxa_count(self, pixac: LPPixaComp) -> int:
        return self.pixacompGetBoxaCount(pixac)

    def capi_pixacomp_get_box(self, pixac: LPPixaComp, index: int,
                              accesstype: int) -> LPBox:
        return self.pixacompGetBox(pixac, index, accesstype)

    def capi_pixacomp_get_box_geometry(self, pixac: LPPixaComp, index: int,
                                       px: c_int_p, py: c_int_p, pw: c_int_p,
                                       ph: c_int_p) -> int:
        return self.pixacompGetBoxGeometry(pixac, index, px, py, pw, ph)

    def capi_pixacomp_get_offset(self, pixac: LPPixaComp) -> int:
        return self.pixacompGetOffset(pixac)

    def capi_pixacomp_set_offset(self, pixac: LPPixaComp, offset: int) -> int:
        return self.pixacompSetOffset(pixac, offset)

    def capi_pixa_create_from_pixacomp(self, pixac: LPPixaComp,
                                       accesstype: int) -> LPPixa:
        return self.pixaCreateFromPixacomp(pixac, accesstype)

    def capi_pixacomp_join(self, pixacd: LPPixaComp, pixacs: LPPixaComp,
                           istart: int, iend: int) -> int:
        return self.pixacompJoin(pixacd, pixacs, istart, iend)

    def capi_pixacomp_interleave(self, pixac1: LPPixaComp,
                                 pixac2: LPPixaComp) -> LPPixaComp:
        return self.pixacompInterleave(pixac1, pixac2)

    def capi_pixacomp_read(self, filename: bytes) -> LPPixaComp:
        return self.pixacompRead(filename)

    def capi_pixacomp_read_stream(self, fp: LPFile) -> LPPixaComp:
        return self.pixacompReadStream(fp)

    def capi_pixacomp_read_mem(self, data: c_ubyte_p, size: int) -> LPPixaComp:
        return self.pixacompReadMem(data, size)

    def capi_pixacomp_write(self, filename: bytes, pixac: LPPixaComp) -> int:
        return self.pixacompWrite(filename, pixac)

    def capi_pixacomp_write_stream(self, fp: LPFile, pixac: LPPixaComp) -> int:
        return self.pixacompWriteStream(fp, pixac)

    def capi_pixacomp_write_mem(self, pdata: POINTER(c_ubyte_p),
                                psize: c_size_t_p, pixac: LPPixaComp) -> int:
        return self.pixacompWriteMem(pdata, psize, pixac)

    def capi_pixacomp_convert_to_pdf(self, pixac: LPPixaComp, res: int,
                                     scalefactor: float, type: int,
                                     quality: int, title: bytes,
                                     fileout: bytes) -> int:
        return self.pixacompConvertToPdf(pixac, res, scalefactor, type,
                                         quality, title, fileout)

    def capi_pixacomp_convert_to_pdf_data(self, pixac: LPPixaComp, res: int,
                                          scalefactor: float, type: int,
                                          quality: int, title: bytes,
                                          pdata: POINTER(c_ubyte_p),
                                          pnbytes: c_size_t_p) -> int:
        return self.pixacompConvertToPdfData(pixac, res, scalefactor, type,
                                             quality, title, pdata, pnbytes)

    def capi_pixacomp_fast_convert_to_pdf_data(self, pixac: LPPixaComp,
                                               title: bytes,
                                               pdata: POINTER(c_ubyte_p),
                                               pnbytes: c_size_t_p) -> int:
        return self.pixacompFastConvertToPdfData(pixac, title, pdata, pnbytes)

    def capi_pixacomp_write_stream_info(self, fp: LPFile, pixac: LPPixaComp,
                                        text: bytes) -> int:
        return self.pixacompWriteStreamInfo(fp, pixac, text)

    def capi_pixcomp_write_stream_info(self, fp: LPFile, pixc: LPPixComp,
                                       text: bytes) -> int:
        return self.pixcompWriteStreamInfo(fp, pixc, text)

    def capi_pixacomp_display_tiled_and_scaled(self, pixac: LPPixaComp,
                                               outdepth: int, tilewidth: int,
                                               ncols: int, background: int,
                                               spacing: int,
                                               border: int) -> LPPix:
        return self.pixacompDisplayTiledAndScaled(pixac, outdepth, tilewidth,
                                                  ncols, background, spacing,
                                                  border)

    def capi_pixacomp_write_files(self, pixac: LPPixaComp,
                                  subdir: bytes) -> int:
        return self.pixacompWriteFiles(pixac, subdir)

    def capi_pixcomp_write_file(self, rootname: bytes, pixc: LPPixComp) -> int:
        return self.pixcompWriteFile(rootname, pixc)

    def capi_pix_threshold8(self, pixs: LPPix, d: int, nlevels: int,
                            cmapflag: int) -> LPPix:
        return self.pixThreshold8(pixs, d, nlevels, cmapflag)

    def capi_pix_remove_colormap_general(self, pixs: LPPix, type: int,
                                         ifnocmap: int) -> LPPix:
        return self.pixRemoveColormapGeneral(pixs, type, ifnocmap)

    def capi_pix_remove_colormap(self, pixs: LPPix, type: int) -> LPPix:
        return self.pixRemoveColormap(pixs, type)

    def capi_pix_add_gray_colormap8(self, pixs: LPPix) -> int:
        return self.pixAddGrayColormap8(pixs)

    def capi_pix_add_minimal_gray_colormap8(self, pixs: LPPix) -> LPPix:
        return self.pixAddMinimalGrayColormap8(pixs)

    def capi_pix_convert_rgb_to_luminance(self, pixs: LPPix) -> LPPix:
        return self.pixConvertRGBToLuminance(pixs)

    def capi_pix_convert_rgb_to_gray_general(self, pixs: LPPix, type: int,
                                             rwt: float, gwt: float,
                                             bwt: float) -> LPPix:
        return self.pixConvertRGBToGrayGeneral(pixs, type, rwt, gwt, bwt)

    def capi_pix_convert_rgb_to_gray(self, pixs: LPPix, rwt: float, gwt: float,
                                     bwt: float) -> LPPix:
        return self.pixConvertRGBToGray(pixs, rwt, gwt, bwt)

    def capi_pix_convert_rgb_to_gray_fast(self, pixs: LPPix) -> LPPix:
        return self.pixConvertRGBToGrayFast(pixs)

    def capi_pix_convert_rgb_to_gray_min_max(self, pixs: LPPix,
                                             type: int) -> LPPix:
        return self.pixConvertRGBToGrayMinMax(pixs, type)

    def capi_pix_convert_rgb_to_gray_sat_boost(self, pixs: LPPix,
                                               refval: int) -> LPPix:
        return self.pixConvertRGBToGraySatBoost(pixs, refval)

    def capi_pix_convert_rgb_to_gray_arb(self, pixs: LPPix, rc: float,
                                         gc: float, bc: float) -> LPPix:
        return self.pixConvertRGBToGrayArb(pixs, rc, gc, bc)

    def capi_pix_convert_rgb_to_binary_arb(self, pixs: LPPix, rc: float,
                                           gc: float, bc: float, thresh: int,
                                           relation: int) -> LPPix:
        return self.pixConvertRGBToBinaryArb(pixs, rc, gc, bc, thresh,
                                             relation)

    def capi_pix_convert_gray_to_colormap(self, pixs: LPPix) -> LPPix:
        return self.pixConvertGrayToColormap(pixs)

    def capi_pix_convert_gray_to_colormap8(self, pixs: LPPix,
                                           mindepth: int) -> LPPix:
        return self.pixConvertGrayToColormap8(pixs, mindepth)

    def capi_pix_colorize_gray(self, pixs: LPPix, color: int,
                               cmapflag: int) -> LPPix:
        return self.pixColorizeGray(pixs, color, cmapflag)

    def capi_pix_convert_rgb_to_colormap(self, pixs: LPPix,
                                         ditherflag: int) -> LPPix:
        return self.pixConvertRGBToColormap(pixs, ditherflag)

    def capi_pix_convert_cmap_to1(self, pixs: LPPix) -> LPPix:
        return self.pixConvertCmapTo1(pixs)

    def capi_pix_quantize_if_few_colors(self, pixs: LPPix, maxcolors: int,
                                        mingraycolors: int, octlevel: int,
                                        ppixd: LPLPPix) -> int:
        return self.pixQuantizeIfFewColors(pixs, maxcolors, mingraycolors,
                                           octlevel, ppixd)

    def capi_pix_convert16to8(self, pixs: LPPix, type: int) -> LPPix:
        return self.pixConvert16To8(pixs, type)

    def capi_pix_convert_gray_to_false_color(self, pixs: LPPix,
                                             gamma: float) -> LPPix:
        return self.pixConvertGrayToFalseColor(pixs, gamma)

    def capi_pix_unpack_binary(self, pixs: LPPix, depth: int,
                               invert: int) -> LPPix:
        return self.pixUnpackBinary(pixs, depth, invert)

    def capi_pix_convert1to16(self, pixd: LPPix, pixs: LPPix, val0: int,
                              val1: int) -> LPPix:
        return self.pixConvert1To16(pixd, pixs, val0, val1)

    def capi_pix_convert1to32(self, pixd: LPPix, pixs: LPPix, val0: int,
                              val1: int) -> LPPix:
        return self.pixConvert1To32(pixd, pixs, val0, val1)

    def capi_pix_convert1to2cmap(self, pixs: LPPix) -> LPPix:
        return self.pixConvert1To2Cmap(pixs)

    def capi_pix_convert1to2(self, pixd: LPPix, pixs: LPPix, val0: int,
                             val1: int) -> LPPix:
        return self.pixConvert1To2(pixd, pixs, val0, val1)

    def capi_pix_convert1to4cmap(self, pixs: LPPix) -> LPPix:
        return self.pixConvert1To4Cmap(pixs)

    def capi_pix_convert1to4(self, pixd: LPPix, pixs: LPPix, val0: int,
                             val1: int) -> LPPix:
        return self.pixConvert1To4(pixd, pixs, val0, val1)

    def capi_pix_convert1to8cmap(self, pixs: LPPix) -> LPPix:
        return self.pixConvert1To8Cmap(pixs)

    def capi_pix_convert1to8(self, pixd: LPPix, pixs: LPPix, val0: int,
                             val1: int) -> LPPix:
        return self.pixConvert1To8(pixd, pixs, val0, val1)

    def capi_pix_convert2to8(self, pixs: LPPix, val0: int, val1: int,
                             val2: int, val3: int, cmapflag: int) -> LPPix:
        return self.pixConvert2To8(pixs, val0, val1, val2, val3, cmapflag)

    def capi_pix_convert4to8(self, pixs: LPPix, cmapflag: int) -> LPPix:
        return self.pixConvert4To8(pixs, cmapflag)

    def capi_pix_convert8to16(self, pixs: LPPix, leftshift: int) -> LPPix:
        return self.pixConvert8To16(pixs, leftshift)

    def capi_pix_convert_to2(self, pixs: LPPix) -> LPPix:
        return self.pixConvertTo2(pixs)

    def capi_pix_convert8to2(self, pix: LPPix) -> LPPix:
        return self.pixConvert8To2(pix)

    def capi_pix_convert_to4(self, pixs: LPPix) -> LPPix:
        return self.pixConvertTo4(pixs)

    def capi_pix_convert8to4(self, pix: LPPix) -> LPPix:
        return self.pixConvert8To4(pix)

    def capi_pix_convert_to1adaptive(self, pixs: LPPix) -> LPPix:
        return self.pixConvertTo1Adaptive(pixs)

    def capi_pix_convert_to1(self, pixs: LPPix, threshold: int) -> LPPix:
        return self.pixConvertTo1(pixs, threshold)

    def capi_pix_convert_to1by_sampling(self, pixs: LPPix, factor: int,
                                        threshold: int) -> LPPix:
        return self.pixConvertTo1BySampling(pixs, factor, threshold)

    def capi_pix_convert_to8(self, pixs: LPPix, cmapflag: int) -> LPPix:
        return self.pixConvertTo8(pixs, cmapflag)

    def capi_pix_convert_to8by_sampling(self, pixs: LPPix, factor: int,
                                        cmapflag: int) -> LPPix:
        return self.pixConvertTo8BySampling(pixs, factor, cmapflag)

    def capi_pix_convert_to8colormap(self, pixs: LPPix, dither: int) -> LPPix:
        return self.pixConvertTo8Colormap(pixs, dither)

    def capi_pix_convert_to16(self, pixs: LPPix) -> LPPix:
        return self.pixConvertTo16(pixs)

    def capi_pix_convert_to32(self, pixs: LPPix) -> LPPix:
        return self.pixConvertTo32(pixs)

    def capi_pix_convert_to32by_sampling(self, pixs: LPPix,
                                         factor: int) -> LPPix:
        return self.pixConvertTo32BySampling(pixs, factor)

    def capi_pix_convert8to32(self, pixs: LPPix) -> LPPix:
        return self.pixConvert8To32(pixs)

    def capi_pix_convert_to8or32(self, pixs: LPPix, copyflag: int,
                                 warnflag: int) -> LPPix:
        return self.pixConvertTo8Or32(pixs, copyflag, warnflag)

    def capi_pix_convert24to32(self, pixs: LPPix) -> LPPix:
        return self.pixConvert24To32(pixs)

    def capi_pix_convert32to24(self, pixs: LPPix) -> LPPix:
        return self.pixConvert32To24(pixs)

    def capi_pix_convert32to16(self, pixs: LPPix, type: int) -> LPPix:
        return self.pixConvert32To16(pixs, type)

    def capi_pix_convert32to8(self, pixs: LPPix, type16: int,
                              type8: int) -> LPPix:
        return self.pixConvert32To8(pixs, type16, type8)

    def capi_pix_remove_alpha(self, pixs: LPPix) -> LPPix:
        return self.pixRemoveAlpha(pixs)

    def capi_pix_add_alpha_to1bpp(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixAddAlphaTo1bpp(pixd, pixs)

    def capi_pix_convert_lossless(self, pixs: LPPix, d: int) -> LPPix:
        return self.pixConvertLossless(pixs, d)

    def capi_pix_convert_for_ps_wrap(self, pixs: LPPix) -> LPPix:
        return self.pixConvertForPSWrap(pixs)

    def capi_pix_convert_to_subpixel_rgb(self, pixs: LPPix, scalex: float,
                                         scaley: float, order: int) -> LPPix:
        return self.pixConvertToSubpixelRGB(pixs, scalex, scaley, order)

    def capi_pix_convert_gray_to_subpixel_rgb(self, pixs: LPPix, scalex: float,
                                              scaley: float,
                                              order: int) -> LPPix:
        return self.pixConvertGrayToSubpixelRGB(pixs, scalex, scaley, order)

    def capi_pix_convert_color_to_subpixel_rgb(self, pixs: LPPix,
                                               scalex: float, scaley: float,
                                               order: int) -> LPPix:
        return self.pixConvertColorToSubpixelRGB(pixs, scalex, scaley, order)

    def capi_l_setNeutralBoostVal(self, val: int):
        self.l_setNeutralBoostVal(val)

    def capi_pix_conn_comp_transform(self, pixs: LPPix, connect: int,
                                     depth: int) -> LPPix:
        return self.pixConnCompTransform(pixs, connect, depth)

    def capi_pix_conn_comp_area_transform(self, pixs: LPPix,
                                          connect: int) -> LPPix:
        return self.pixConnCompAreaTransform(pixs, connect)

    def capi_pix_conn_comp_incr_init(self, pixs: LPPix, conn: int,
                                     ppixd: LPLPPix, pptaa: LPLPPtaa,
                                     pncc: c_int_p) -> int:
        return self.pixConnCompIncrInit(pixs, conn, ppixd, pptaa, pncc)

    def capi_pix_conn_comp_incr_add(self, pixs: LPPix, ptaa: LPPtaa,
                                    pncc: c_int_p, x: float, y: float,
                                    debug: int) -> int:
        return self.pixConnCompIncrAdd(pixs, ptaa, pncc, x, y, debug)

    def capi_pix_get_sorted_neighbor_values(self, pixs: LPPix, x: int, y: int,
                                            conn: int,
                                            pneigh: POINTER(c_int_p),
                                            pnvals: c_int_p) -> int:
        return self.pixGetSortedNeighborValues(pixs, x, y, conn, pneigh,
                                               pnvals)

    def capi_pix_loc_to_color_transform(self, pixs: LPPix) -> LPPix:
        return self.pixLocToColorTransform(pixs)

    def capi_pix_tiling_create(self, pixs: LPPix, nx: int, ny: int, w: int,
                               h: int, xoverlap: int,
                               yoverlap: int) -> LPPixTiling:
        return self.pixTilingCreate(pixs, nx, ny, w, h, xoverlap, yoverlap)

    def capi_pix_tiling_destroy(self, ppt: LPLPPixTiling):
        self.pixTilingDestroy(ppt)

    def capi_pix_tiling_get_count(self, pt: LPPixTiling, pnx: c_int_p,
                                  pny: c_int_p) -> int:
        return self.pixTilingGetCount(pt, pnx, pny)

    def capi_pix_tiling_get_size(self, pt: LPPixTiling, pw: c_int_p,
                                 ph: c_int_p) -> int:
        return self.pixTilingGetSize(pt, pw, ph)

    def capi_pix_tiling_get_tile(self, pt: LPPixTiling, i: int,
                                 j: int) -> LPPix:
        return self.pixTilingGetTile(pt, i, j)

    def capi_pix_tiling_no_strip_on_paint(self, pt: LPPixTiling) -> int:
        return self.pixTilingNoStripOnPaint(pt)

    def capi_pix_tiling_paint_tile(self, pixd: LPPix, i: int, j: int,
                                   pixs: LPPix, pt: LPPixTiling) -> int:
        return self.pixTilingPaintTile(pixd, i, j, pixs, pt)

    def capi_pix_read_stream_png(self, fp: LPFile) -> LPPix:
        return self.pixReadStreamPng(fp)

    def capi_read_header_png(self, filename: bytes, pw: c_int_p, ph: c_int_p,
                             pbps: c_int_p, pspp: c_int_p,
                             piscmap: c_int_p) -> int:
        return self.readHeaderPng(filename, pw, ph, pbps, pspp, piscmap)

    def capi_fread_header_png(self, fp: LPFile, pw: c_int_p, ph: c_int_p,
                              pbps: c_int_p, pspp: c_int_p,
                              piscmap: c_int_p) -> int:
        return self.freadHeaderPng(fp, pw, ph, pbps, pspp, piscmap)

    def capi_read_header_mem_png(self, data: c_ubyte_p, size: int, pw: c_int_p,
                                 ph: c_int_p, pbps: c_int_p, pspp: c_int_p,
                                 piscmap: c_int_p) -> int:
        return self.readHeaderMemPng(data, size, pw, ph, pbps, pspp, piscmap)

    def capi_fget_png_resolution(self, fp: LPFile, pxres: c_int_p,
                                 pyres: c_int_p) -> int:
        return self.fgetPngResolution(fp, pxres, pyres)

    def capi_is_png_interlaced(self, filename: bytes,
                               pinterlaced: c_int_p) -> int:
        return self.isPngInterlaced(filename, pinterlaced)

    def capi_fget_png_colormap_info(self, fp: LPFile, pcmap: LPLPPixColormap,
                                    ptransparency: c_int_p) -> int:
        return self.fgetPngColormapInfo(fp, pcmap, ptransparency)

    def capi_pix_write_png(self, filename: bytes, pix: LPPix,
                           gamma: float) -> int:
        return self.pixWritePng(filename, pix, gamma)

    def capi_pix_write_stream_png(self, fp: LPFile, pix: LPPix,
                                  gamma: float) -> int:
        return self.pixWriteStreamPng(fp, pix, gamma)

    def capi_pix_set_zlib_compression(self, pix: LPPix, compval: int) -> int:
        return self.pixSetZlibCompression(pix, compval)

    def capi_l_pngSetReadStrip16To8(self, flag: int):
        self.l_pngSetReadStrip16To8(flag)

    def capi_pix_read_mem_png(self, filedata: c_ubyte_p,
                              filesize: int) -> LPPix:
        return self.pixReadMemPng(filedata, filesize)

    def capi_pix_write_mem_png(self, pfiledata: POINTER(c_ubyte_p),
                               pfilesize: c_size_t_p, pix: LPPix,
                               gamma: float) -> int:
        return self.pixWriteMemPng(pfiledata, pfilesize, pix, gamma)

    def capi_pix_read_stream_pnm(self, fp: LPFile) -> LPPix:
        return self.pixReadStreamPnm(fp)

    def capi_read_header_pnm(self, filename: bytes, pw: c_int_p, ph: c_int_p,
                             pd: c_int_p, ptype: c_int_p, pbps: c_int_p,
                             pspp: c_int_p) -> int:
        return self.readHeaderPnm(filename, pw, ph, pd, ptype, pbps, pspp)

    def capi_fread_header_pnm(self, fp: LPFile, pw: c_int_p, ph: c_int_p,
                              pd: c_int_p, ptype: c_int_p, pbps: c_int_p,
                              pspp: c_int_p) -> int:
        return self.freadHeaderPnm(fp, pw, ph, pd, ptype, pbps, pspp)

    def capi_pix_write_stream_pnm(self, fp: LPFile, pix: LPPix) -> int:
        return self.pixWriteStreamPnm(fp, pix)

    def capi_pix_write_stream_ascii_pnm(self, fp: LPFile, pix: LPPix) -> int:
        return self.pixWriteStreamAsciiPnm(fp, pix)

    def capi_pix_write_stream_pam(self, fp: LPFile, pix: LPPix) -> int:
        return self.pixWriteStreamPam(fp, pix)

    def capi_pix_read_mem_pnm(self, data: c_ubyte_p, size: int) -> LPPix:
        return self.pixReadMemPnm(data, size)

    def capi_read_header_mem_pnm(self, data: c_ubyte_p, size: int, pw: c_int_p,
                                 ph: c_int_p, pd: c_int_p, ptype: c_int_p,
                                 pbps: c_int_p, pspp: c_int_p) -> int:
        return self.readHeaderMemPnm(data, size, pw, ph, pd, ptype, pbps, pspp)

    def capi_pix_write_mem_pnm(self, pdata: POINTER(c_ubyte_p),
                               psize: c_size_t_p, pix: LPPix) -> int:
        return self.pixWriteMemPnm(pdata, psize, pix)

    def capi_pix_write_mem_pam(self, pdata: POINTER(c_ubyte_p),
                               psize: c_size_t_p, pix: LPPix) -> int:
        return self.pixWriteMemPam(pdata, psize, pix)

    def capi_pix_projective_sampled_pta(self, pixs: LPPix, ptad: LPPta,
                                        ptas: LPPta, incolor: int) -> LPPix:
        return self.pixProjectiveSampledPta(pixs, ptad, ptas, incolor)

    def capi_pix_projective_sampled(self, pixs: LPPix, vc: c_float_p,
                                    incolor: int) -> LPPix:
        return self.pixProjectiveSampled(pixs, vc, incolor)

    def capi_pix_projective_pta(self, pixs: LPPix, ptad: LPPta, ptas: LPPta,
                                incolor: int) -> LPPix:
        return self.pixProjectivePta(pixs, ptad, ptas, incolor)

    def capi_pix_projective(self, pixs: LPPix, vc: c_float_p,
                            incolor: int) -> LPPix:
        return self.pixProjective(pixs, vc, incolor)

    def capi_pix_projective_pta_color(self, pixs: LPPix, ptad: LPPta,
                                      ptas: LPPta, colorval: int) -> LPPix:
        return self.pixProjectivePtaColor(pixs, ptad, ptas, colorval)

    def capi_pix_projective_color(self, pixs: LPPix, vc: c_float_p,
                                  colorval: int) -> LPPix:
        return self.pixProjectiveColor(pixs, vc, colorval)

    def capi_pix_projective_pta_gray(self, pixs: LPPix, ptad: LPPta,
                                     ptas: LPPta, grayval: int) -> LPPix:
        return self.pixProjectivePtaGray(pixs, ptad, ptas, grayval)

    def capi_pix_projective_gray(self, pixs: LPPix, vc: c_float_p,
                                 grayval: int) -> LPPix:
        return self.pixProjectiveGray(pixs, vc, grayval)

    def capi_pix_projective_pta_with_alpha(self, pixs: LPPix, ptad: LPPta,
                                           ptas: LPPta, pixg: LPPix,
                                           fract: float,
                                           border: int) -> LPPix:
        return self.pixProjectivePtaWithAlpha(pixs, ptad, ptas, pixg, fract,
                                              border)

    def capi_get_projective_xform_coeffs(self, ptas: LPPta, ptad: LPPta,
                                         pvc: POINTER(c_float_p)) -> int:
        return self.getProjectiveXformCoeffs(ptas, ptad, pvc)

    def capi_projective_xform_sampled_pt(self, vc: c_float_p, x: int, y: int,
                                         pxp: c_int_p, pyp: c_int_p) -> int:
        return self.projectiveXformSampledPt(vc, x, y, pxp, pyp)

    def capi_projective_xform_pt(self, vc: c_float_p, x: int, y: int,
                                 pxp: c_float_p, pyp: c_float_p) -> int:
        return self.projectiveXformPt(vc, x, y, pxp, pyp)

    def capi_convert_files_to_ps(self, dirin: bytes, substr: bytes, res: int,
                                 fileout: bytes) -> int:
        return self.convertFilesToPS(dirin, substr, res, fileout)

    def capi_sarray_convert_files_to_ps(self, sa: LPSarray, res: int,
                                        fileout: bytes) -> int:
        return self.sarrayConvertFilesToPS(sa, res, fileout)

    def capi_convert_files_fitted_to_ps(self, dirin: bytes, substr: bytes,
                                        xpts: float, ypts: float,
                                        fileout: bytes) -> int:
        return self.convertFilesFittedToPS(dirin, substr, xpts, ypts, fileout)

    def capi_sarray_convert_files_fitted_to_ps(self, sa: LPSarray, xpts: float,
                                               ypts: float,
                                               fileout: bytes) -> int:
        return self.sarrayConvertFilesFittedToPS(sa, xpts, ypts, fileout)

    def capi_write_image_compressed_to_ps_file(self, filein: bytes,
                                               fileout: bytes, res: int,
                                               pindex: c_int_p) -> int:
        return self.writeImageCompressedToPSFile(filein, fileout, res, pindex)

    def capi_convert_segmented_pages_to_ps(self, pagedir: bytes,
                                           pagestr: bytes, page_numpre: int,
                                           maskdir: bytes, maskstr: bytes,
                                           mask_numpre: int, numpost: int,
                                           maxnum: int, textscale: float,
                                           imagescale: float, threshold: int,
                                           fileout: bytes) -> int:
        return self.convertSegmentedPagesToPS(pagedir, pagestr, page_numpre,
                                              maskdir, maskstr, mask_numpre,
                                              numpost, maxnum, textscale,
                                              imagescale, threshold, fileout)

    def capi_pix_write_segmented_page_to_ps(self, pixs: LPPix, pixm: LPPix,
                                            textscale: float,
                                            imagescale: float, threshold: int,
                                            pageno: int,
                                            fileout: bytes) -> int:
        return self.pixWriteSegmentedPageToPS(pixs, pixm, textscale,
                                              imagescale, threshold, pageno,
                                              fileout)

    def capi_pix_write_mixed_to_ps(self, pixb: LPPix, pixc: LPPix,
                                   scale: float, pageno: int,
                                   fileout: bytes) -> int:
        return self.pixWriteMixedToPS(pixb, pixc, scale, pageno, fileout)

    def capi_convert_to_ps_embed(self, filein: bytes, fileout: bytes,
                                 level: int) -> int:
        return self.convertToPSEmbed(filein, fileout, level)

    def capi_pixa_write_compressed_to_ps(self, pixa: LPPixa, fileout: bytes,
                                         res: int, level: int) -> int:
        return self.pixaWriteCompressedToPS(pixa, fileout, res, level)

    def capi_pix_write_compressed_to_ps(self, pix: LPPix, fileout: bytes,
                                        res: int, level: int,
                                        pindex: c_int_p) -> int:
        return self.pixWriteCompressedToPS(pix, fileout, res, level, pindex)

    def capi_pix_write_ps_embed(self, filein: bytes, fileout: bytes) -> int:
        return self.pixWritePSEmbed(filein, fileout)

    def capi_pix_write_stream_ps(self, fp: LPFile, pix: LPPix, box: LPBox,
                                 res: int, scale: float) -> int:
        return self.pixWriteStreamPS(fp, pix, box, res, scale)

    def capi_pix_write_string_ps(self, pixs: LPPix, box: LPBox, res: int,
                                 scale: float) -> LP_c_char:
        return self.pixWriteStringPS(pixs, box, res, scale)

    def capi_generate_uncompressed_ps(self, hexdata: LP_c_char, w: int, h: int,
                                      d: int, psbpl: int, bps: int, xpt: float,
                                      ypt: float, wpt: float, hpt: float,
                                      boxflag: int) -> LP_c_char:
        return self.generateUncompressedPS(hexdata, w, h, d, psbpl, bps, xpt,
                                           ypt, wpt, hpt, boxflag)

    def capi_convert_jpeg_to_ps_embed(self, filein: bytes,
                                      fileout: bytes) -> int:
        return self.convertJpegToPSEmbed(filein, fileout)

    def capi_convert_jpeg_to_ps(self, filein: bytes, fileout: bytes,
                                operation: bytes, x: int, y: int, res: int,
                                scale: float, pageno: int,
                                endpage: int) -> int:
        return self.convertJpegToPS(filein, fileout, operation, x, y, res,
                                    scale, pageno, endpage)

    def capi_convertg4to_ps_embed(self, filein: bytes, fileout: bytes) -> int:
        return self.convertG4ToPSEmbed(filein, fileout)

    def capi_convertg4to_ps(self, filein: bytes, fileout: bytes,
                            operation: bytes, x: int, y: int, res: int,
                            scale: float, pageno: int, maskflag: int,
                            endpage: int) -> int:
        return self.convertG4ToPS(filein, fileout, operation, x, y, res, scale,
                                  pageno, maskflag, endpage)

    def capi_convert_tiff_multipage_to_ps(self, filein: bytes, fileout: bytes,
                                          fillfract: float) -> int:
        return self.convertTiffMultipageToPS(filein, fileout, fillfract)

    def capi_convert_flate_to_ps_embed(self, filein: bytes,
                                       fileout: bytes) -> int:
        return self.convertFlateToPSEmbed(filein, fileout)

    def capi_convert_flate_to_ps(self, filein: bytes, fileout: bytes,
                                 operation: bytes, x: int, y: int, res: int,
                                 scale: float, pageno: int,
                                 endpage: int) -> int:
        return self.convertFlateToPS(filein, fileout, operation, x, y, res,
                                     scale, pageno, endpage)

    def capi_pix_write_mem_ps(self, pdata: POINTER(c_ubyte_p),
                              psize: c_size_t_p, pix: LPPix, box: LPBox,
                              res: int, scale: float) -> int:
        return self.pixWriteMemPS(pdata, psize, pix, box, res, scale)

    def capi_get_res_letter_page(self, w: int, h: int,
                                 fillfract: float) -> int:
        return self.getResLetterPage(w, h, fillfract)

    def capi_get_resa4page(self, w: int, h: int, fillfract: float) -> int:
        return self.getResA4Page(w, h, fillfract)

    def capi_l_psWriteBoundingBox(self, flag: int):
        self.l_psWriteBoundingBox(flag)

    def capi_pta_create(self, n: int) -> LPPta:
        return self.ptaCreate(n)

    def capi_pta_create_from_numa(self, nax: LPNuma, nay: LPNuma) -> LPPta:
        return self.ptaCreateFromNuma(nax, nay)

    def capi_pta_destroy(self, ppta: LPLPPta):
        self.ptaDestroy(ppta)

    def capi_pta_copy(self, pta: LPPta) -> LPPta:
        return self.ptaCopy(pta)

    def capi_pta_copy_range(self, ptas: LPPta, istart: int,
                            iend: int) -> LPPta:
        return self.ptaCopyRange(ptas, istart, iend)

    def capi_pta_clone(self, pta: LPPta) -> LPPta:
        return self.ptaClone(pta)

    def capi_pta_empty(self, pta: LPPta) -> int:
        return self.ptaEmpty(pta)

    def capi_pta_add_pt(self, pta: LPPta, x: float, y: float) -> int:
        return self.ptaAddPt(pta, x, y)

    def capi_pta_insert_pt(self, pta: LPPta, index: int, x: int,
                           y: int) -> int:
        return self.ptaInsertPt(pta, index, x, y)

    def capi_pta_remove_pt(self, pta: LPPta, index: int) -> int:
        return self.ptaRemovePt(pta, index)

    def capi_pta_get_refcount(self, pta: LPPta) -> int:
        return self.ptaGetRefcount(pta)

    def capi_pta_change_refcount(self, pta: LPPta, delta: int) -> int:
        return self.ptaChangeRefcount(pta, delta)

    def capi_pta_get_count(self, pta: LPPta) -> int:
        return self.ptaGetCount(pta)

    def capi_pta_get_pt(self, pta: LPPta, index: int, px: c_float_p,
                        py: c_float_p) -> int:
        return self.ptaGetPt(pta, index, px, py)

    def capi_pta_get_ipt(self, pta: LPPta, index: int, px: c_int_p,
                         py: c_int_p) -> int:
        return self.ptaGetIPt(pta, index, px, py)

    def capi_pta_set_pt(self, pta: LPPta, index: int, x: float,
                        y: float) -> int:
        return self.ptaSetPt(pta, index, x, y)

    def capi_pta_get_arrays(self, pta: LPPta, pnax: LPLPNuma,
                            pnay: LPLPNuma) -> int:
        return self.ptaGetArrays(pta, pnax, pnay)

    def capi_pta_read(self, filename: bytes) -> LPPta:
        return self.ptaRead(filename)

    def capi_pta_read_stream(self, fp: LPFile) -> LPPta:
        return self.ptaReadStream(fp)

    def capi_pta_read_mem(self, data: c_ubyte_p, size: int) -> LPPta:
        return self.ptaReadMem(data, size)

    def capi_pta_write_debug(self, filename: bytes, pta: LPPta,
                             type: int) -> int:
        return self.ptaWriteDebug(filename, pta, type)

    def capi_pta_write(self, filename: bytes, pta: LPPta, type: int) -> int:
        return self.ptaWrite(filename, pta, type)

    def capi_pta_write_stream(self, fp: LPFile, pta: LPPta, type: int) -> int:
        return self.ptaWriteStream(fp, pta, type)

    def capi_pta_write_mem(self, pdata: POINTER(c_ubyte_p), psize: c_size_t_p,
                           pta: LPPta, type: int) -> int:
        return self.ptaWriteMem(pdata, psize, pta, type)

    def capi_ptaa_create(self, n: int) -> LPPtaa:
        return self.ptaaCreate(n)

    def capi_ptaa_destroy(self, pptaa: LPLPPtaa):
        self.ptaaDestroy(pptaa)

    def capi_ptaa_add_pta(self, ptaa: LPPtaa, pta: LPPta,
                          copyflag: int) -> int:
        return self.ptaaAddPta(ptaa, pta, copyflag)

    def capi_ptaa_get_count(self, ptaa: LPPtaa) -> int:
        return self.ptaaGetCount(ptaa)

    def capi_ptaa_get_pta(self, ptaa: LPPtaa, index: int,
                          accessflag: int) -> LPPta:
        return self.ptaaGetPta(ptaa, index, accessflag)

    def capi_ptaa_get_pt(self, ptaa: LPPtaa, ipta: int, jpt: int,
                         px: c_float_p, py: c_float_p) -> int:
        return self.ptaaGetPt(ptaa, ipta, jpt, px, py)

    def capi_ptaa_init_full(self, ptaa: LPPtaa, pta: LPPta) -> int:
        return self.ptaaInitFull(ptaa, pta)

    def capi_ptaa_replace_pta(self, ptaa: LPPtaa, index: int,
                              pta: LPPta) -> int:
        return self.ptaaReplacePta(ptaa, index, pta)

    def capi_ptaa_add_pt(self, ptaa: LPPtaa, ipta: int, x: float,
                         y: float) -> int:
        return self.ptaaAddPt(ptaa, ipta, x, y)

    def capi_ptaa_truncate(self, ptaa: LPPtaa) -> int:
        return self.ptaaTruncate(ptaa)

    def capi_ptaa_read(self, filename: bytes) -> LPPtaa:
        return self.ptaaRead(filename)

    def capi_ptaa_read_stream(self, fp: LPFile) -> LPPtaa:
        return self.ptaaReadStream(fp)

    def capi_ptaa_read_mem(self, data: c_ubyte_p, size: int) -> LPPtaa:
        return self.ptaaReadMem(data, size)

    def capi_ptaa_write_debug(self, filename: bytes, ptaa: LPPtaa,
                              type: int) -> int:
        return self.ptaaWriteDebug(filename, ptaa, type)

    def capi_ptaa_write(self, filename: bytes, ptaa: LPPtaa, type: int) -> int:
        return self.ptaaWrite(filename, ptaa, type)

    def capi_ptaa_write_stream(self, fp: LPFile, ptaa: LPPtaa,
                               type: int) -> int:
        return self.ptaaWriteStream(fp, ptaa, type)

    def capi_ptaa_write_mem(self, pdata: POINTER(c_ubyte_p), psize: c_size_t_p,
                            ptaa: LPPtaa, type: int) -> int:
        return self.ptaaWriteMem(pdata, psize, ptaa, type)

    def capi_pta_subsample(self, ptas: LPPta, subfactor: int) -> LPPta:
        return self.ptaSubsample(ptas, subfactor)

    def capi_pta_join(self, ptad: LPPta, ptas: LPPta, istart: int,
                      iend: int) -> int:
        return self.ptaJoin(ptad, ptas, istart, iend)

    def capi_ptaa_join(self, ptaad: LPPtaa, ptaas: LPPtaa, istart: int,
                       iend: int) -> int:
        return self.ptaaJoin(ptaad, ptaas, istart, iend)

    def capi_pta_reverse(self, ptas: LPPta, type: int) -> LPPta:
        return self.ptaReverse(ptas, type)

    def capi_pta_transpose(self, ptas: LPPta) -> LPPta:
        return self.ptaTranspose(ptas)

    def capi_pta_cyclic_perm(self, ptas: LPPta, xs: int, ys: int) -> LPPta:
        return self.ptaCyclicPerm(ptas, xs, ys)

    def capi_pta_select_range(self, ptas: LPPta, first: int,
                              last: int) -> LPPta:
        return self.ptaSelectRange(ptas, first, last)

    def capi_pta_get_bounding_region(self, pta: LPPta) -> LPBox:
        return self.ptaGetBoundingRegion(pta)

    def capi_pta_get_range(self, pta: LPPta, pminx: c_float_p,
                           pmaxx: c_float_p, pminy: c_float_p,
                           pmaxy: c_float_p) -> int:
        return self.ptaGetRange(pta, pminx, pmaxx, pminy, pmaxy)

    def capi_pta_get_inside_box(self, ptas: LPPta, box: LPBox) -> LPPta:
        return self.ptaGetInsideBox(ptas, box)

    def capi_pix_find_corner_pixels(self, pixs: LPPix) -> LPPta:
        return self.pixFindCornerPixels(pixs)

    def capi_pta_contains_pt(self, pta: LPPta, x: int, y: int) -> int:
        return self.ptaContainsPt(pta, x, y)

    def capi_pta_test_intersection(self, pta1: LPPta, pta2: LPPta) -> int:
        return self.ptaTestIntersection(pta1, pta2)

    def capi_pta_transform(self, ptas: LPPta, shiftx: int, shifty: int,
                           scalex: float, scaley: float) -> LPPta:
        return self.ptaTransform(ptas, shiftx, shifty, scalex, scaley)

    def capi_pta_pt_inside_polygon(self, pta: LPPta, x: float, y: float,
                                   pinside: c_int_p) -> int:
        return self.ptaPtInsidePolygon(pta, x, y, pinside)

    def capi_l_angleBetweenVectors(self, x1: float, y1: float, x2: float,
                                   y2: float) -> float:
        return self.l_angleBetweenVectors(x1, y1, x2, y2)

    def capi_pta_polygon_is_convex(self, pta: LPPta,
                                   pisconvex: c_int_p) -> int:
        return self.ptaPolygonIsConvex(pta, pisconvex)

    def capi_pta_get_min_max(self, pta: LPPta, pxmin: c_float_p,
                             pymin: c_float_p, pxmax: c_float_p,
                             pymax: c_float_p) -> int:
        return self.ptaGetMinMax(pta, pxmin, pymin, pxmax, pymax)

    def capi_pta_select_by_value(self, ptas: LPPta, xth: float, yth: float,
                                 type: int, relation: int) -> LPPta:
        return self.ptaSelectByValue(ptas, xth, yth, type, relation)

    def capi_pta_crop_to_mask(self, ptas: LPPta, pixm: LPPix) -> LPPta:
        return self.ptaCropToMask(ptas, pixm)

    def capi_pta_get_linear_lsf(self, pta: LPPta, pa: c_float_p, pb: c_float_p,
                                pnafit: LPLPNuma) -> int:
        return self.ptaGetLinearLSF(pta, pa, pb, pnafit)

    def capi_pta_get_quadratic_lsf(self, pta: LPPta, pa: c_float_p,
                                   pb: c_float_p, pc: c_float_p,
                                   pnafit: LPLPNuma) -> int:
        return self.ptaGetQuadraticLSF(pta, pa, pb, pc, pnafit)

    def capi_pta_get_cubic_lsf(self, pta: LPPta, pa: c_float_p, pb: c_float_p,
                               pc: c_float_p, pd: c_float_p,
                               pnafit: LPLPNuma) -> int:
        return self.ptaGetCubicLSF(pta, pa, pb, pc, pd, pnafit)

    def capi_pta_get_quartic_lsf(self, pta: LPPta, pa: c_float_p,
                                 pb: c_float_p, pc: c_float_p, pd: c_float_p,
                                 pe: c_float_p, pnafit: LPLPNuma) -> int:
        return self.ptaGetQuarticLSF(pta, pa, pb, pc, pd, pe, pnafit)

    def capi_pta_noisy_linear_lsf(self, pta: LPPta, factor: float,
                                  pptad: LPLPPta, pa: c_float_p, pb: c_float_p,
                                  pmederr: c_float_p,
                                  pnafit: LPLPNuma) -> int:
        return self.ptaNoisyLinearLSF(pta, factor, pptad, pa, pb, pmederr,
                                      pnafit)

    def capi_pta_noisy_quadratic_lsf(self, pta: LPPta, factor: float,
                                     pptad: LPLPPta, pa: c_float_p,
                                     pb: c_float_p, pc: c_float_p,
                                     pmederr: c_float_p,
                                     pnafit: LPLPNuma) -> int:
        return self.ptaNoisyQuadraticLSF(pta, factor, pptad, pa, pb, pc,
                                         pmederr, pnafit)

    def capi_apply_linear_fit(self, a: float, b: float, x: float,
                              py: c_float_p) -> int:
        return self.applyLinearFit(a, b, x, py)

    def capi_apply_quadratic_fit(self, a: float, b: float, c: float, x: float,
                                 py: c_float_p) -> int:
        return self.applyQuadraticFit(a, b, c, x, py)

    def capi_apply_cubic_fit(self, a: float, b: float, c: float, d: float,
                             x: float, py: c_float_p) -> int:
        return self.applyCubicFit(a, b, c, d, x, py)

    def capi_apply_quartic_fit(self, a: float, b: float, c: float, d: float,
                               e: float, x: float, py: c_float_p) -> int:
        return self.applyQuarticFit(a, b, c, d, e, x, py)

    def capi_pix_plot_along_pta(self, pixs: LPPix, pta: LPPta, outformat: int,
                                title: bytes) -> int:
        return self.pixPlotAlongPta(pixs, pta, outformat, title)

    def capi_pta_get_pixels_from_pix(self, pixs: LPPix, box: LPBox) -> LPPta:
        return self.ptaGetPixelsFromPix(pixs, box)

    def capi_pix_generate_from_pta(self, pta: LPPta, w: int, h: int) -> LPPix:
        return self.pixGenerateFromPta(pta, w, h)

    def capi_pta_get_boundary_pixels(self, pixs: LPPix, type: int) -> LPPta:
        return self.ptaGetBoundaryPixels(pixs, type)

    def capi_ptaa_get_boundary_pixels(self, pixs: LPPix, type: int,
                                      connectivity: int, pboxa: LPLPBoxa,
                                      ppixa: LPLPPixa) -> LPPtaa:
        return self.ptaaGetBoundaryPixels(pixs, type, connectivity, pboxa,
                                          ppixa)

    def capi_ptaa_index_labeled_pixels(self, pixs: LPPix,
                                       pncc: c_int_p) -> LPPtaa:
        return self.ptaaIndexLabeledPixels(pixs, pncc)

    def capi_pta_get_neighbor_pix_locs(self, pixs: LPPix, x: int, y: int,
                                       conn: int) -> LPPta:
        return self.ptaGetNeighborPixLocs(pixs, x, y, conn)

    def capi_numa_convert_to_pta1(self, na: LPNuma) -> LPPta:
        return self.numaConvertToPta1(na)

    def capi_numa_convert_to_pta2(self, nax: LPNuma, nay: LPNuma) -> LPPta:
        return self.numaConvertToPta2(nax, nay)

    def capi_pta_convert_to_numa(self, pta: LPPta, pnax: LPLPNuma,
                                 pnay: LPLPNuma) -> int:
        return self.ptaConvertToNuma(pta, pnax, pnay)

    def capi_pix_display_pta(self, pixd: LPPix, pixs: LPPix,
                             pta: LPPta) -> LPPix:
        return self.pixDisplayPta(pixd, pixs, pta)

    def capi_pix_display_ptaa_pattern(self, pixd: LPPix, pixs: LPPix,
                                      ptaa: LPPtaa, pixp: LPPix, cx: int,
                                      cy: int) -> LPPix:
        return self.pixDisplayPtaaPattern(pixd, pixs, ptaa, pixp, cx, cy)

    def capi_pix_display_pta_pattern(self, pixd: LPPix, pixs: LPPix,
                                     pta: LPPta, pixp: LPPix, cx: int, cy: int,
                                     color: int) -> LPPix:
        return self.pixDisplayPtaPattern(pixd, pixs, pta, pixp, cx, cy, color)

    def capi_pta_replicate_pattern(self, ptas: LPPta, pixp: LPPix, ptap: LPPta,
                                   cx: int, cy: int, w: int, h: int) -> LPPta:
        return self.ptaReplicatePattern(ptas, pixp, ptap, cx, cy, w, h)

    def capi_pix_display_ptaa(self, pixs: LPPix, ptaa: LPPtaa) -> LPPix:
        return self.pixDisplayPtaa(pixs, ptaa)

    def capi_pta_sort(self, ptas: LPPta, sorttype: int, sortorder: int,
                      pnaindex: LPLPNuma) -> LPPta:
        return self.ptaSort(ptas, sorttype, sortorder, pnaindex)

    def capi_pta_get_sort_index(self, ptas: LPPta, sorttype: int,
                                sortorder: int, pnaindex: LPLPNuma) -> int:
        return self.ptaGetSortIndex(ptas, sorttype, sortorder, pnaindex)

    def capi_pta_sort_by_index(self, ptas: LPPta, naindex: LPNuma) -> LPPta:
        return self.ptaSortByIndex(ptas, naindex)

    def capi_ptaa_sort_by_index(self, ptaas: LPPtaa,
                                naindex: LPNuma) -> LPPtaa:
        return self.ptaaSortByIndex(ptaas, naindex)

    def capi_pta_get_rank_value(self, pta: LPPta, fract: float, ptasort: LPPta,
                                sorttype: int, pval: c_float_p) -> int:
        return self.ptaGetRankValue(pta, fract, ptasort, sorttype, pval)

    def capi_pta_sort2d(self, pta: LPPta) -> LPPta:
        return self.ptaSort2d(pta)

    def capi_pta_equal(self, pta1: LPPta, pta2: LPPta, psame: c_int_p) -> int:
        return self.ptaEqual(pta1, pta2, psame)

    def capi_l_asetCreateFromPta(self, pta: LPPta) -> LPL_Rbtree:
        return self.l_asetCreateFromPta(pta)

    def capi_pta_remove_dups_by_aset(self, ptas: LPPta, pptad: LPLPPta) -> int:
        return self.ptaRemoveDupsByAset(ptas, pptad)

    def capi_pta_union_by_aset(self, pta1: LPPta, pta2: LPPta,
                               pptad: LPLPPta) -> int:
        return self.ptaUnionByAset(pta1, pta2, pptad)

    def capi_pta_intersection_by_aset(self, pta1: LPPta, pta2: LPPta,
                                      pptad: LPLPPta) -> int:
        return self.ptaIntersectionByAset(pta1, pta2, pptad)

    def capi_l_hmapCreateFromPta(self, pta: LPPta) -> LPL_Hashmap:
        return self.l_hmapCreateFromPta(pta)

    def capi_pta_remove_dups_by_hmap(self, ptas: LPPta, pptad: LPLPPta,
                                     phmap: LPLPL_Hashmap) -> int:
        return self.ptaRemoveDupsByHmap(ptas, pptad, phmap)

    def capi_pta_union_by_hmap(self, pta1: LPPta, pta2: LPPta,
                               pptad: LPLPPta) -> int:
        return self.ptaUnionByHmap(pta1, pta2, pptad)

    def capi_pta_intersection_by_hmap(self, pta1: LPPta, pta2: LPPta,
                                      pptad: LPLPPta) -> int:
        return self.ptaIntersectionByHmap(pta1, pta2, pptad)

    def capi_ptra_create(self, n: int) -> LPL_Ptra:
        return self.ptraCreate(n)

    def capi_ptra_destroy(self, ppa: LPLPL_Ptra, freeflag: int, warnflag: int):
        self.ptraDestroy(ppa, freeflag, warnflag)

    def capi_ptra_add(self, pa: LPL_Ptra, item: c_void_p) -> int:
        return self.ptraAdd(pa, item)

    def capi_ptra_insert(self, pa: LPL_Ptra, index: int, item: c_void_p,
                         shiftflag: int) -> int:
        return self.ptraInsert(pa, index, item, shiftflag)

    def capi_ptra_remove(self, pa: LPL_Ptra, index: int,
                         flag: int) -> c_void_p:
        return self.ptraRemove(pa, index, flag)

    def capi_ptra_remove_last(self, pa: LPL_Ptra) -> c_void_p:
        return self.ptraRemoveLast(pa)

    def capi_ptra_replace(self, pa: LPL_Ptra, index: int, item: c_void_p,
                          freeflag: int) -> c_void_p:
        return self.ptraReplace(pa, index, item, freeflag)

    def capi_ptra_swap(self, pa: LPL_Ptra, index1: int, index2: int) -> int:
        return self.ptraSwap(pa, index1, index2)

    def capi_ptra_compact_array(self, pa: LPL_Ptra) -> int:
        return self.ptraCompactArray(pa)

    def capi_ptra_reverse(self, pa: LPL_Ptra) -> int:
        return self.ptraReverse(pa)

    def capi_ptra_join(self, pa1: LPL_Ptra, pa2: LPL_Ptra) -> int:
        return self.ptraJoin(pa1, pa2)

    def capi_ptra_get_max_index(self, pa: LPL_Ptra, pmaxindex: c_int_p) -> int:
        return self.ptraGetMaxIndex(pa, pmaxindex)

    def capi_ptra_get_actual_count(self, pa: LPL_Ptra, pcount: c_int_p) -> int:
        return self.ptraGetActualCount(pa, pcount)

    def capi_ptra_get_ptr_to_item(self, pa: LPL_Ptra, index: int) -> c_void_p:
        return self.ptraGetPtrToItem(pa, index)

    def capi_ptraa_create(self, n: int) -> LPL_Ptraa:
        return self.ptraaCreate(n)

    def capi_ptraa_destroy(self, ppaa: LPLPL_Ptraa, freeflag: int,
                           warnflag: int):
        self.ptraaDestroy(ppaa, freeflag, warnflag)

    def capi_ptraa_get_size(self, paa: LPL_Ptraa, psize: c_int_p) -> int:
        return self.ptraaGetSize(paa, psize)

    def capi_ptraa_insert_ptra(self, paa: LPL_Ptraa, index: int,
                               pa: LPL_Ptra) -> int:
        return self.ptraaInsertPtra(paa, index, pa)

    def capi_ptraa_get_ptra(self, paa: LPL_Ptraa, index: int,
                            accessflag: int) -> LPL_Ptra:
        return self.ptraaGetPtra(paa, index, accessflag)

    def capi_ptraa_flatten_to_ptra(self, paa: LPL_Ptraa) -> LPL_Ptra:
        return self.ptraaFlattenToPtra(paa)

    def capi_pix_quadtree_mean(self, pixs: LPPix, nlevels: int, pix_ma: LPPix,
                               pfpixa: LPLPFPixa) -> int:
        return self.pixQuadtreeMean(pixs, nlevels, pix_ma, pfpixa)

    def capi_pix_quadtree_variance(self, pixs: LPPix, nlevels: int,
                                   pix_ma: LPPix, dpix_msa: LPDPix,
                                   pfpixa_v: LPLPFPixa,
                                   pfpixa_rv: LPLPFPixa) -> int:
        return self.pixQuadtreeVariance(pixs, nlevels, pix_ma, dpix_msa,
                                        pfpixa_v, pfpixa_rv)

    def capi_pix_mean_in_rectangle(self, pixs: LPPix, box: LPBox, pixma: LPPix,
                                   pval: c_float_p) -> int:
        return self.pixMeanInRectangle(pixs, box, pixma, pval)

    def capi_pix_variance_in_rectangle(self, pixs: LPPix, box: LPBox,
                                       pix_ma: LPPix, dpix_msa: LPDPix,
                                       pvar: c_float_p,
                                       prvar: c_float_p) -> int:
        return self.pixVarianceInRectangle(pixs, box, pix_ma, dpix_msa, pvar,
                                           prvar)

    def capi_boxaa_quadtree_regions(self, w: int, h: int,
                                    nlevels: int) -> LPBoxaa:
        return self.boxaaQuadtreeRegions(w, h, nlevels)

    def capi_quadtree_get_parent(self, fpixa: LPFPixa, level: int, x: int,
                                 y: int, pval: c_float_p) -> int:
        return self.quadtreeGetParent(fpixa, level, x, y, pval)

    def capi_quadtree_get_children(self, fpixa: LPFPixa, level: int, x: int,
                                   y: int, pval00: c_float_p,
                                   pval10: c_float_p, pval01: c_float_p,
                                   pval11: c_float_p) -> int:
        return self.quadtreeGetChildren(fpixa, level, x, y, pval00, pval10,
                                        pval01, pval11)

    def capi_quadtree_max_levels(self, w: int, h: int) -> int:
        return self.quadtreeMaxLevels(w, h)

    def capi_fpixa_display_quadtree(self, fpixa: LPFPixa, factor: int,
                                    fontsize: int) -> LPPix:
        return self.fpixaDisplayQuadtree(fpixa, factor, fontsize)

    def capi_lqueue_create(self, nalloc: int) -> LPL_Queue:
        return self.lqueueCreate(nalloc)

    def capi_lqueue_destroy(self, plq: LPLPL_Queue, freeflag: int):
        self.lqueueDestroy(plq, freeflag)

    def capi_lqueue_add(self, lq: LPL_Queue, item: c_void_p) -> int:
        return self.lqueueAdd(lq, item)

    def capi_lqueue_remove(self, lq: LPL_Queue) -> c_void_p:
        return self.lqueueRemove(lq)

    def capi_lqueue_get_count(self, lq: LPL_Queue) -> int:
        return self.lqueueGetCount(lq)

    def capi_lqueue_print(self, fp: LPFile, lq: LPL_Queue) -> int:
        return self.lqueuePrint(fp, lq)

    def capi_pix_rank_filter(self, pixs: LPPix, wf: int, hf: int,
                             rank: float) -> LPPix:
        return self.pixRankFilter(pixs, wf, hf, rank)

    def capi_pix_rank_filter_rgb(self, pixs: LPPix, wf: int, hf: int,
                                 rank: float) -> LPPix:
        return self.pixRankFilterRGB(pixs, wf, hf, rank)

    def capi_pix_rank_filter_gray(self, pixs: LPPix, wf: int, hf: int,
                                  rank: float) -> LPPix:
        return self.pixRankFilterGray(pixs, wf, hf, rank)

    def capi_pix_median_filter(self, pixs: LPPix, wf: int, hf: int) -> LPPix:
        return self.pixMedianFilter(pixs, wf, hf)

    def capi_pix_rank_filter_with_scaling(self, pixs: LPPix, wf: int, hf: int,
                                          rank: float,
                                          scalefactor: float) -> LPPix:
        return self.pixRankFilterWithScaling(pixs, wf, hf, rank, scalefactor)

    def capi_l_rbtreeCreate(self, keytype: int) -> LPL_Rbtree:
        return self.l_rbtreeCreate(keytype)

    def capi_l_rbtreeLookup(self, t: LPL_Rbtree, key: Rb_Type) -> LPRb_Type:
        return self.l_rbtreeLookup(t, key)

    def capi_l_rbtreeInsert(self, t: LPL_Rbtree, key: Rb_Type, value: Rb_Type):
        self.l_rbtreeInsert(t, key, value)

    def capi_l_rbtreeDelete(self, t: LPL_Rbtree, key: Rb_Type):
        self.l_rbtreeDelete(t, key)

    def capi_l_rbtreeDestroy(self, pt: LPLPL_Rbtree):
        self.l_rbtreeDestroy(pt)

    def capi_l_rbtreeGetFirst(self, t: LPL_Rbtree) -> LPL_Rbtree_Node:
        return self.l_rbtreeGetFirst(t)

    def capi_l_rbtreeGetNext(self, n: LPL_Rbtree_Node) -> LPL_Rbtree_Node:
        return self.l_rbtreeGetNext(n)

    def capi_l_rbtreeGetLast(self, t: LPL_Rbtree) -> LPL_Rbtree_Node:
        return self.l_rbtreeGetLast(t)

    def capi_l_rbtreeGetPrev(self, n: LPL_Rbtree_Node) -> LPL_Rbtree_Node:
        return self.l_rbtreeGetPrev(n)

    def capi_l_rbtreeGetCount(self, t: LPL_Rbtree) -> int:
        return self.l_rbtreeGetCount(t)

    def capi_l_rbtreePrint(self, fp: LPFile, t: LPL_Rbtree):
        self.l_rbtreePrint(fp, t)

    def capi_pix_process_barcodes(self, pixs: LPPix, format: int, method: int,
                                  psaw: LPLPSarray,
                                  debugflag: int) -> LPSarray:
        return self.pixProcessBarcodes(pixs, format, method, psaw, debugflag)

    def capi_pix_extract_barcodes(self, pixs: LPPix, debugflag: int) -> LPPixa:
        return self.pixExtractBarcodes(pixs, debugflag)

    def capi_pix_read_barcodes(self, pixa: LPPixa, format: int, method: int,
                               psaw: LPLPSarray, debugflag: int) -> LPSarray:
        return self.pixReadBarcodes(pixa, format, method, psaw, debugflag)

    def capi_pix_read_barcode_widths(self, pixs: LPPix, method: int,
                                     debugflag: int) -> LPNuma:
        return self.pixReadBarcodeWidths(pixs, method, debugflag)

    def capi_pix_locate_barcodes(self, pixs: LPPix, thresh: int,
                                 ppixb: LPLPPix, ppixm: LPLPPix) -> LPBoxa:
        return self.pixLocateBarcodes(pixs, thresh, ppixb, ppixm)

    def capi_pix_deskew_barcode(self, pixs: LPPix, pixb: LPPix, box: LPBox,
                                margin: int, threshold: int, pangle: c_float_p,
                                pconf: c_float_p) -> LPPix:
        return self.pixDeskewBarcode(pixs, pixb, box, margin, threshold,
                                     pangle, pconf)

    def capi_pix_extract_barcode_widths1(self, pixs: LPPix, thresh: float,
                                         binfract: float, pnaehist: LPLPNuma,
                                         pnaohist: LPLPNuma,
                                         debugflag: int) -> LPNuma:
        return self.pixExtractBarcodeWidths1(pixs, thresh, binfract, pnaehist,
                                             pnaohist, debugflag)

    def capi_pix_extract_barcode_widths2(self, pixs: LPPix, thresh: float,
                                         pwidth: c_float_p, pnac: LPLPNuma,
                                         debugflag: int) -> LPNuma:
        return self.pixExtractBarcodeWidths2(pixs, thresh, pwidth, pnac,
                                             debugflag)

    def capi_pix_extract_barcode_crossings(self, pixs: LPPix, thresh: float,
                                           debugflag: int) -> LPNuma:
        return self.pixExtractBarcodeCrossings(pixs, thresh, debugflag)

    def capi_numa_quantize_crossings_by_width(self, nas: LPNuma,
                                              binfract: float,
                                              pnaehist: LPLPNuma,
                                              pnaohist: LPLPNuma,
                                              debugflag: int) -> LPNuma:
        return self.numaQuantizeCrossingsByWidth(nas, binfract, pnaehist,
                                                 pnaohist, debugflag)

    def capi_numa_quantize_crossings_by_window(self, nas: LPNuma, ratio: float,
                                               pwidth: c_float_p,
                                               pfirstloc: c_float_p,
                                               pnac: LPLPNuma,
                                               debugflag: int) -> LPNuma:
        return self.numaQuantizeCrossingsByWindow(nas, ratio, pwidth,
                                                  pfirstloc, pnac, debugflag)

    def capi_pixa_read_files(self, dirname: bytes, substr: bytes) -> LPPixa:
        return self.pixaReadFiles(dirname, substr)

    def capi_pixa_read_files_sa(self, sa: LPSarray) -> LPPixa:
        return self.pixaReadFilesSA(sa)

    def capi_pix_read(self, filename: bytes) -> LPPix:
        return self.pixRead(filename)

    def capi_pix_read_with_hint(self, filename: bytes, hint: int) -> LPPix:
        return self.pixReadWithHint(filename, hint)

    def capi_pix_read_indexed(self, sa: LPSarray, index: int) -> LPPix:
        return self.pixReadIndexed(sa, index)

    def capi_pix_read_stream(self, fp: LPFile, hint: int) -> LPPix:
        return self.pixReadStream(fp, hint)

    def capi_pix_read_header(self, filename: bytes, pformat: c_int_p,
                             pw: c_int_p, ph: c_int_p, pbps: c_int_p,
                             pspp: c_int_p, piscmap: c_int_p) -> int:
        return self.pixReadHeader(filename, pformat, pw, ph, pbps, pspp,
                                  piscmap)

    def capi_find_file_format(self, filename: bytes, pformat: c_int_p) -> int:
        return self.findFileFormat(filename, pformat)

    def capi_find_file_format_stream(self, fp: LPFile,
                                     pformat: c_int_p) -> int:
        return self.findFileFormatStream(fp, pformat)

    def capi_find_file_format_buffer(self, buf: c_ubyte_p,
                                     pformat: c_int_p) -> int:
        return self.findFileFormatBuffer(buf, pformat)

    def capi_file_format_is_tiff(self, fp: LPFile) -> int:
        return self.fileFormatIsTiff(fp)

    def capi_pix_read_mem(self, data: c_ubyte_p, size: int) -> LPPix:
        return self.pixReadMem(data, size)

    def capi_pix_read_header_mem(self, data: c_ubyte_p, size: int,
                                 pformat: c_int_p, pw: c_int_p, ph: c_int_p,
                                 pbps: c_int_p, pspp: c_int_p,
                                 piscmap: c_int_p) -> int:
        return self.pixReadHeaderMem(data, size, pformat, pw, ph, pbps, pspp,
                                     piscmap)

    def capi_write_image_file_info(self, filename: bytes, fpout: LPFile,
                                   headeronly: int) -> int:
        return self.writeImageFileInfo(filename, fpout, headeronly)

    def capi_io_format_test(self, filename: bytes) -> int:
        return self.ioFormatTest(filename)

    def capi_recog_create_from_recog(self, recs: LPL_Recog, scalew: int,
                                     scaleh: int, linew: int, threshold: int,
                                     maxyshift: int) -> LPL_Recog:
        return self.recogCreateFromRecog(recs, scalew, scaleh, linew,
                                         threshold, maxyshift)

    def capi_recog_create_from_pixa(self, pixa: LPPixa, scalew: int,
                                    scaleh: int, linew: int, threshold: int,
                                    maxyshift: int) -> LPL_Recog:
        return self.recogCreateFromPixa(pixa, scalew, scaleh, linew, threshold,
                                        maxyshift)

    def capi_recog_create_from_pixa_no_finish(self, pixa: LPPixa, scalew: int,
                                              scaleh: int, linew: int,
                                              threshold: int,
                                              maxyshift: int) -> LPL_Recog:
        return self.recogCreateFromPixaNoFinish(pixa, scalew, scaleh, linew,
                                                threshold, maxyshift)

    def capi_recog_create(self, scalew: int, scaleh: int, linew: int,
                          threshold: int, maxyshift: int) -> LPL_Recog:
        return self.recogCreate(scalew, scaleh, linew, threshold, maxyshift)

    def capi_recog_destroy(self, precog: LPLPL_Recog):
        self.recogDestroy(precog)

    def capi_recog_get_count(self, recog: LPL_Recog) -> int:
        return self.recogGetCount(recog)

    def capi_recog_set_params(self, recog: LPL_Recog, type: int,
                              min_nopad: int, max_wh_ratio: float,
                              max_ht_ratio: float) -> int:
        return self.recogSetParams(recog, type, min_nopad, max_wh_ratio,
                                   max_ht_ratio)

    def capi_recog_get_class_index(self, recog: LPL_Recog, val: int,
                                   text: LP_c_char, pindex: c_int_p) -> int:
        return self.recogGetClassIndex(recog, val, text, pindex)

    def capi_recog_string_to_index(self, recog: LPL_Recog, text: LP_c_char,
                                   pindex: c_int_p) -> int:
        return self.recogStringToIndex(recog, text, pindex)

    def capi_recog_get_class_string(self, recog: LPL_Recog, index: int,
                                    pcharstr: c_char_p_p) -> int:
        return self.recogGetClassString(recog, index, pcharstr)

    def capi_l_convertCharstrToInt(self, str: bytes, pval: c_int_p) -> int:
        return self.l_convertCharstrToInt(str, pval)

    def capi_recog_read(self, filename: bytes) -> LPL_Recog:
        return self.recogRead(filename)

    def capi_recog_read_stream(self, fp: LPFile) -> LPL_Recog:
        return self.recogReadStream(fp)

    def capi_recog_read_mem(self, data: c_ubyte_p, size: int) -> LPL_Recog:
        return self.recogReadMem(data, size)

    def capi_recog_write(self, filename: bytes, recog: LPL_Recog) -> int:
        return self.recogWrite(filename, recog)

    def capi_recog_write_stream(self, fp: LPFile, recog: LPL_Recog) -> int:
        return self.recogWriteStream(fp, recog)

    def capi_recog_write_mem(self, pdata: POINTER(c_ubyte_p),
                             psize: c_size_t_p, recog: LPL_Recog) -> int:
        return self.recogWriteMem(pdata, psize, recog)

    def capi_recog_extract_pixa(self, recog: LPL_Recog) -> LPPixa:
        return self.recogExtractPixa(recog)

    def capi_recog_decode(self, recog: LPL_Recog, pixs: LPPix, nlevels: int,
                          ppixdb: LPLPPix) -> LPBoxa:
        return self.recogDecode(recog, pixs, nlevels, ppixdb)

    def capi_recog_create_did(self, recog: LPL_Recog, pixs: LPPix) -> int:
        return self.recogCreateDid(recog, pixs)

    def capi_recog_destroy_did(self, recog: LPL_Recog) -> int:
        return self.recogDestroyDid(recog)

    def capi_recog_did_exists(self, recog: LPL_Recog) -> int:
        return self.recogDidExists(recog)

    def capi_recog_get_did(self, recog: LPL_Recog) -> LPL_Rdid:
        return self.recogGetDid(recog)

    def capi_recog_set_channel_params(self, recog: LPL_Recog,
                                      nlevels: int) -> int:
        return self.recogSetChannelParams(recog, nlevels)

    def capi_recog_identify_multiple(self, recog: LPL_Recog, pixs: LPPix,
                                     minh: int, skipsplit: int,
                                     pboxa: LPLPBoxa, ppixa: LPLPPixa,
                                     ppixdb: LPLPPix, debugsplit: int) -> int:
        return self.recogIdentifyMultiple(recog, pixs, minh, skipsplit, pboxa,
                                          ppixa, ppixdb, debugsplit)

    def capi_recog_split_into_characters(self, recog: LPL_Recog, pixs: LPPix,
                                         minh: int, skipsplit: int,
                                         pboxa: LPLPBoxa, ppixa: LPLPPixa,
                                         debug: int) -> int:
        return self.recogSplitIntoCharacters(recog, pixs, minh, skipsplit,
                                             pboxa, ppixa, debug)

    def capi_recog_correlation_best_row(self, recog: LPL_Recog, pixs: LPPix,
                                        pboxa: LPLPBoxa, pnascore: LPLPNuma,
                                        pnaindex: LPLPNuma,
                                        psachar: LPLPSarray,
                                        debug: int) -> int:
        return self.recogCorrelationBestRow(recog, pixs, pboxa, pnascore,
                                            pnaindex, psachar, debug)

    def capi_recog_correlation_best_char(self, recog: LPL_Recog, pixs: LPPix,
                                         pbox: LPLPBox, pscore: c_float_p,
                                         pindex: c_int_p, pcharstr: c_char_p_p,
                                         ppixdb: LPLPPix) -> int:
        return self.recogCorrelationBestChar(recog, pixs, pbox, pscore, pindex,
                                             pcharstr, ppixdb)

    def capi_recog_identify_pixa(self, recog: LPL_Recog, pixa: LPPixa,
                                 ppixdb: LPLPPix) -> int:
        return self.recogIdentifyPixa(recog, pixa, ppixdb)

    def capi_recog_identify_pix(self, recog: LPL_Recog, pixs: LPPix,
                                ppixdb: LPLPPix) -> int:
        return self.recogIdentifyPix(recog, pixs, ppixdb)

    def capi_recog_skip_identify(self, recog: LPL_Recog) -> int:
        return self.recogSkipIdentify(recog)

    def capi_rcha_destroy(self, prcha: LPLPL_Rcha):
        self.rchaDestroy(prcha)

    def capi_rch_destroy(self, prch: LPLPL_Rch):
        self.rchDestroy(prch)

    def capi_rcha_extract(self, rcha: LPL_Rcha, pnaindex: LPLPNuma,
                          pnascore: LPLPNuma, psatext: LPLPSarray,
                          pnasample: LPLPNuma, pnaxloc: LPLPNuma,
                          pnayloc: LPLPNuma, pnawidth: LPLPNuma) -> int:
        return self.rchaExtract(rcha, pnaindex, pnascore, psatext, pnasample,
                                pnaxloc, pnayloc, pnawidth)

    def capi_rch_extract(self, rch: LPL_Rch, pindex: c_int_p,
                         pscore: c_float_p, ptext: c_char_p_p,
                         psample: c_int_p, pxloc: c_int_p, pyloc: c_int_p,
                         pwidth: c_int_p) -> int:
        return self.rchExtract(rch, pindex, pscore, ptext, psample, pxloc,
                               pyloc, pwidth)

    def capi_recog_process_to_identify(self, recog: LPL_Recog, pixs: LPPix,
                                       pad: int) -> LPPix:
        return self.recogProcessToIdentify(recog, pixs, pad)

    def capi_recog_extract_numbers(self, recog: LPL_Recog, boxas: LPBoxa,
                                   scorethresh: float, spacethresh: int,
                                   pbaa: LPLPBoxaa,
                                   pnaa: LPLPNumaa) -> LPSarray:
        return self.recogExtractNumbers(recog, boxas, scorethresh, spacethresh,
                                        pbaa, pnaa)

    def capi_show_extract_numbers(self, pixs: LPPix, sa: LPSarray,
                                  baa: LPBoxaa, naa: LPNumaa,
                                  ppixdb: LPLPPix) -> LPPixa:
        return self.showExtractNumbers(pixs, sa, baa, naa, ppixdb)

    def capi_recog_train_labeled(self, recog: LPL_Recog, pixs: LPPix,
                                 box: LPBox, text: LP_c_char,
                                 debug: int) -> int:
        return self.recogTrainLabeled(recog, pixs, box, text, debug)

    def capi_recog_process_labeled(self, recog: LPL_Recog, pixs: LPPix,
                                   box: LPBox, text: LP_c_char,
                                   ppix: LPLPPix) -> int:
        return self.recogProcessLabeled(recog, pixs, box, text, ppix)

    def capi_recog_add_sample(self, recog: LPL_Recog, pix: LPPix,
                              debug: int) -> int:
        return self.recogAddSample(recog, pix, debug)

    def capi_recog_modify_template(self, recog: LPL_Recog,
                                   pixs: LPPix) -> LPPix:
        return self.recogModifyTemplate(recog, pixs)

    def capi_recog_average_samples(self, precog: LPLPL_Recog,
                                   debug: int) -> int:
        return self.recogAverageSamples(precog, debug)

    def capi_pixa_accumulate_samples(self, pixa: LPPixa, pta: LPPta,
                                     ppixd: LPLPPix, px: c_float_p,
                                     py: c_float_p) -> int:
        return self.pixaAccumulateSamples(pixa, pta, ppixd, px, py)

    def capi_recog_training_finished(self, precog: LPLPL_Recog,
                                     modifyflag: int, minsize: int,
                                     minfract: float) -> int:
        return self.recogTrainingFinished(precog, modifyflag, minsize,
                                          minfract)

    def capi_recog_filter_pixa_by_size(self, pixas: LPPixa, setsize: int,
                                       maxkeep: int, max_ht_ratio: float,
                                       pna: LPLPNuma) -> LPPixa:
        return self.recogFilterPixaBySize(pixas, setsize, maxkeep,
                                          max_ht_ratio, pna)

    def capi_recog_sort_pixa_by_class(self, pixa: LPPixa,
                                      setsize: int) -> LPPixaa:
        return self.recogSortPixaByClass(pixa, setsize)

    def capi_recog_remove_outliers1(self, precog: LPLPL_Recog, minscore: float,
                                    mintarget: int, minsize: int,
                                    ppixsave: LPLPPix,
                                    ppixrem: LPLPPix) -> int:
        return self.recogRemoveOutliers1(precog, minscore, mintarget, minsize,
                                         ppixsave, ppixrem)

    def capi_pixa_remove_outliers1(self, pixas: LPPixa, minscore: float,
                                   mintarget: int, minsize: int,
                                   ppixsave: LPLPPix,
                                   ppixrem: LPLPPix) -> LPPixa:
        return self.pixaRemoveOutliers1(pixas, minscore, mintarget, minsize,
                                        ppixsave, ppixrem)

    def capi_recog_remove_outliers2(self, precog: LPLPL_Recog, minscore: float,
                                    minsize: int, ppixsave: LPLPPix,
                                    ppixrem: LPLPPix) -> int:
        return self.recogRemoveOutliers2(precog, minscore, minsize, ppixsave,
                                         ppixrem)

    def capi_pixa_remove_outliers2(self, pixas: LPPixa, minscore: float,
                                   minsize: int, ppixsave: LPLPPix,
                                   ppixrem: LPLPPix) -> LPPixa:
        return self.pixaRemoveOutliers2(pixas, minscore, minsize, ppixsave,
                                        ppixrem)

    def capi_recog_train_from_boot(self, recogboot: LPL_Recog, pixas: LPPixa,
                                   minscore: float, threshold: int,
                                   debug: int) -> LPPixa:
        return self.recogTrainFromBoot(recogboot, pixas, minscore, threshold,
                                       debug)

    def capi_recog_pad_digit_training_set(self, precog: LPLPL_Recog,
                                          scaleh: int, linew: int) -> int:
        return self.recogPadDigitTrainingSet(precog, scaleh, linew)

    def capi_recog_is_padding_needed(self, recog: LPL_Recog,
                                     psa: LPLPSarray) -> int:
        return self.recogIsPaddingNeeded(recog, psa)

    def capi_recog_add_digit_pad_templates(self, recog: LPL_Recog,
                                           sa: LPSarray) -> LPPixa:
        return self.recogAddDigitPadTemplates(recog, sa)

    def capi_recog_make_boot_digit_recog(self, nsamp: int, scaleh: int,
                                         linew: int, maxyshift: int,
                                         debug: int) -> LPL_Recog:
        return self.recogMakeBootDigitRecog(nsamp, scaleh, linew, maxyshift,
                                            debug)

    def capi_recog_make_boot_digit_templates(self, nsamp: int,
                                             debug: int) -> LPPixa:
        return self.recogMakeBootDigitTemplates(nsamp, debug)

    def capi_recog_show_content(self, fp: LPFile, recog: LPL_Recog, index: int,
                                display: int) -> int:
        return self.recogShowContent(fp, recog, index, display)

    def capi_recog_debug_averages(self, precog: LPLPL_Recog,
                                  debug: int) -> int:
        return self.recogDebugAverages(precog, debug)

    def capi_recog_show_average_templates(self, recog: LPL_Recog) -> int:
        return self.recogShowAverageTemplates(recog)

    def capi_recog_show_matches_in_range(self, recog: LPL_Recog, pixa: LPPixa,
                                         minscore: float, maxscore: float,
                                         display: int) -> int:
        return self.recogShowMatchesInRange(recog, pixa, minscore, maxscore,
                                            display)

    def capi_recog_show_match(self, recog: LPL_Recog, pix1: LPPix, pix2: LPPix,
                              box: LPBox, index: int, score: float) -> LPPix:
        return self.recogShowMatch(recog, pix1, pix2, box, index, score)

    def capi_reg_test_setup(self, argc: int, argv: c_char_p_p,
                            prp: LPLPL_RegParams) -> int:
        return self.regTestSetup(argc, argv, prp)

    def capi_reg_test_cleanup(self, rp: LPL_RegParams) -> int:
        return self.regTestCleanup(rp)

    def capi_reg_test_compare_values(self, rp: LPL_RegParams, val1: float,
                                     val2: float, delta: float) -> int:
        return self.regTestCompareValues(rp, val1, val2, delta)

    def capi_reg_test_compare_strings(self, rp: LPL_RegParams,
                                      string1: c_ubyte_p, bytes1: int,
                                      string2: c_ubyte_p, bytes2: int) -> int:
        return self.regTestCompareStrings(rp, string1, bytes1, string2, bytes2)

    def capi_reg_test_compare_pix(self, rp: LPL_RegParams, pix1: LPPix,
                                  pix2: LPPix) -> int:
        return self.regTestComparePix(rp, pix1, pix2)

    def capi_reg_test_compare_similar_pix(self, rp: LPL_RegParams, pix1: LPPix,
                                          pix2: LPPix, mindiff: int,
                                          maxfract: float,
                                          printstats: int) -> int:
        return self.regTestCompareSimilarPix(rp, pix1, pix2, mindiff, maxfract,
                                             printstats)

    def capi_reg_test_check_file(self, rp: LPL_RegParams,
                                 localname: bytes) -> int:
        return self.regTestCheckFile(rp, localname)

    def capi_reg_test_compare_files(self, rp: LPL_RegParams, index1: int,
                                    index2: int) -> int:
        return self.regTestCompareFiles(rp, index1, index2)

    def capi_reg_test_write_pix_and_check(self, rp: LPL_RegParams, pix: LPPix,
                                          format: int) -> int:
        return self.regTestWritePixAndCheck(rp, pix, format)

    def capi_reg_test_write_data_and_check(self, rp: LPL_RegParams,
                                           data: c_void_p, nbytes: int,
                                           ext: bytes) -> int:
        return self.regTestWriteDataAndCheck(rp, data, nbytes, ext)

    def capi_reg_test_gen_local_filename(self, rp: LPL_RegParams, index: int,
                                         format: int) -> LP_c_char:
        return self.regTestGenLocalFilename(rp, index, format)

    def capi_pix_rasterop(self, pixd: LPPix, dx: int, dy: int, dw: int,
                          dh: int, op: int, pixs: LPPix, sx: int,
                          sy: int) -> int:
        return self.pixRasterop(pixd, dx, dy, dw, dh, op, pixs, sx, sy)

    def capi_pix_rasterop_vip(self, pixd: LPPix, bx: int, bw: int, vshift: int,
                              incolor: int) -> int:
        return self.pixRasteropVip(pixd, bx, bw, vshift, incolor)

    def capi_pix_rasterop_hip(self, pixd: LPPix, by: int, bh: int, hshift: int,
                              incolor: int) -> int:
        return self.pixRasteropHip(pixd, by, bh, hshift, incolor)

    def capi_pix_translate(self, pixd: LPPix, pixs: LPPix, hshift: int,
                           vshift: int, incolor: int) -> LPPix:
        return self.pixTranslate(pixd, pixs, hshift, vshift, incolor)

    def capi_pix_rasterop_ip(self, pixd: LPPix, hshift: int, vshift: int,
                             incolor: int) -> int:
        return self.pixRasteropIP(pixd, hshift, vshift, incolor)

    def capi_pix_rasterop_full_image(self, pixd: LPPix, pixs: LPPix,
                                     op: int) -> int:
        return self.pixRasteropFullImage(pixd, pixs, op)

    def capi_rasterop_uni_low(self, datad: c_uint_p, dpixw: int, dpixh: int,
                              depth: int, dwpl: int, dx: int, dy: int, dw: int,
                              dh: int, op: int):
        self.rasteropUniLow(datad, dpixw, dpixh, depth,
                            dwpl, dx, dy, dw, dh, op)

    def capi_rasterop_low(self, datad: c_uint_p, dpixw: int, dpixh: int,
                          depth: int, dwpl: int, dx: int, dy: int, dw: int,
                          dh: int, op: int, datas: c_uint_p, spixw: int,
                          spixh: int, swpl: int, sx: int, sy: int):
        self.rasteropLow(datad, dpixw, dpixh, depth, dwpl, dx,
                         dy, dw, dh, op, datas, spixw, spixh, swpl, sx, sy)

    def capi_rasterop_vip_low(self, data: c_uint_p, pixw: int, pixh: int,
                              depth: int, wpl: int, x: int, w: int,
                              shift: int):
        self.rasteropVipLow(data, pixw, pixh, depth, wpl, x, w, shift)

    def capi_rasterop_hip_low(self, data: c_uint_p, pixh: int, depth: int,
                              wpl: int, y: int, h: int, shift: int):
        self.rasteropHipLow(data, pixh, depth, wpl, y, h, shift)

    def capi_pix_rotate(self, pixs: LPPix, angle: float, type: int,
                        incolor: int, width: int, height: int) -> LPPix:
        return self.pixRotate(pixs, angle, type, incolor, width, height)

    def capi_pix_embed_for_rotation(self, pixs: LPPix, angle: float,
                                    incolor: int, width: int,
                                    height: int) -> LPPix:
        return self.pixEmbedForRotation(pixs, angle, incolor, width, height)

    def capi_pix_rotate_by_sampling(self, pixs: LPPix, xcen: int, ycen: int,
                                    angle: float, incolor: int) -> LPPix:
        return self.pixRotateBySampling(pixs, xcen, ycen, angle, incolor)

    def capi_pix_rotate_binary_nice(self, pixs: LPPix, angle: float,
                                    incolor: int) -> LPPix:
        return self.pixRotateBinaryNice(pixs, angle, incolor)

    def capi_pix_rotate_with_alpha(self, pixs: LPPix, angle: float,
                                   pixg: LPPix, fract: float) -> LPPix:
        return self.pixRotateWithAlpha(pixs, angle, pixg, fract)

    def capi_pix_rotate_am(self, pixs: LPPix, angle: float,
                           incolor: int) -> LPPix:
        return self.pixRotateAM(pixs, angle, incolor)

    def capi_pix_rotate_am_color(self, pixs: LPPix, angle: float,
                                 colorval: int) -> LPPix:
        return self.pixRotateAMColor(pixs, angle, colorval)

    def capi_pix_rotate_am_gray(self, pixs: LPPix, angle: float,
                                grayval: int) -> LPPix:
        return self.pixRotateAMGray(pixs, angle, grayval)

    def capi_pix_rotate_am_corner(self, pixs: LPPix, angle: float,
                                  incolor: int) -> LPPix:
        return self.pixRotateAMCorner(pixs, angle, incolor)

    def capi_pix_rotate_am_color_corner(self, pixs: LPPix, angle: float,
                                        fillval: int) -> LPPix:
        return self.pixRotateAMColorCorner(pixs, angle, fillval)

    def capi_pix_rotate_am_gray_corner(self, pixs: LPPix, angle: float,
                                       grayval: int) -> LPPix:
        return self.pixRotateAMGrayCorner(pixs, angle, grayval)

    def capi_pix_rotate_am_color_fast(self, pixs: LPPix, angle: float,
                                      colorval: int) -> LPPix:
        return self.pixRotateAMColorFast(pixs, angle, colorval)

    def capi_pix_rotate_orth(self, pixs: LPPix, quads: int) -> LPPix:
        return self.pixRotateOrth(pixs, quads)

    def capi_pix_rotate180(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixRotate180(pixd, pixs)

    def capi_pix_rotate90(self, pixs: LPPix, direction: int) -> LPPix:
        return self.pixRotate90(pixs, direction)

    def capi_pix_flip_lr(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixFlipLR(pixd, pixs)

    def capi_pix_flip_tb(self, pixd: LPPix, pixs: LPPix) -> LPPix:
        return self.pixFlipTB(pixd, pixs)

    def capi_pix_rotate_shear(self, pixs: LPPix, xcen: int, ycen: int,
                              angle: float, incolor: int) -> LPPix:
        return self.pixRotateShear(pixs, xcen, ycen, angle, incolor)

    def capi_pix_rotate2shear(self, pixs: LPPix, xcen: int, ycen: int,
                              angle: float, incolor: int) -> LPPix:
        return self.pixRotate2Shear(pixs, xcen, ycen, angle, incolor)

    def capi_pix_rotate3shear(self, pixs: LPPix, xcen: int, ycen: int,
                              angle: float, incolor: int) -> LPPix:
        return self.pixRotate3Shear(pixs, xcen, ycen, angle, incolor)

    def capi_pix_rotate_shear_ip(self, pixs: LPPix, xcen: int, ycen: int,
                                 angle: float, incolor: int) -> int:
        return self.pixRotateShearIP(pixs, xcen, ycen, angle, incolor)

    def capi_pix_rotate_shear_center(self, pixs: LPPix, angle: float,
                                     incolor: int) -> LPPix:
        return self.pixRotateShearCenter(pixs, angle, incolor)

    def capi_pix_rotate_shear_center_ip(self, pixs: LPPix, angle: float,
                                        incolor: int) -> int:
        return self.pixRotateShearCenterIP(pixs, angle, incolor)

    def capi_pix_stroke_width_transform(self, pixs: LPPix, color: int,
                                        depth: int, nangles: int) -> LPPix:
        return self.pixStrokeWidthTransform(pixs, color, depth, nangles)

    def capi_pix_runlength_transform(self, pixs: LPPix, color: int,
                                     direction: int, depth: int) -> LPPix:
        return self.pixRunlengthTransform(pixs, color, direction, depth)

    def capi_pix_find_horizontal_runs(self, pix: LPPix, y: int,
                                      xstart: c_int_p, xend: c_int_p,
                                      pn: c_int_p) -> int:
        return self.pixFindHorizontalRuns(pix, y, xstart, xend, pn)

    def capi_pix_find_vertical_runs(self, pix: LPPix, x: int, ystart: c_int_p,
                                    yend: c_int_p, pn: c_int_p) -> int:
        return self.pixFindVerticalRuns(pix, x, ystart, yend, pn)

    def capi_pix_find_max_runs(self, pix: LPPix, direction: int,
                               pnastart: LPLPNuma) -> LPNuma:
        return self.pixFindMaxRuns(pix, direction, pnastart)

    def capi_pix_find_max_horizontal_run_on_line(self, pix: LPPix, y: int,
                                                 pxstart: c_int_p,
                                                 psize: c_int_p) -> int:
        return self.pixFindMaxHorizontalRunOnLine(pix, y, pxstart, psize)

    def capi_pix_find_max_vertical_run_on_line(self, pix: LPPix, x: int,
                                               pystart: c_int_p,
                                               psize: c_int_p) -> int:
        return self.pixFindMaxVerticalRunOnLine(pix, x, pystart, psize)

    def capi_runlength_membership_on_line(self, buffer: c_int_p, size: int,
                                          depth: int, start: c_int_p,
                                          end: c_int_p, n: int) -> int:
        return self.runlengthMembershipOnLine(buffer, size, depth, start, end,
                                              n)

    def capi_make_ms_bit_loc_tab(self, bitval: int) -> c_int_p:
        return self.makeMSBitLocTab(bitval)

    def capi_sarray_create(self, n: int) -> LPSarray:
        return self.sarrayCreate(n)

    def capi_sarray_create_initialized(self, n: int,
                                       initstr: bytes) -> LPSarray:
        return self.sarrayCreateInitialized(n, initstr)

    def capi_sarray_create_words_from_string(self, string: bytes) -> LPSarray:
        return self.sarrayCreateWordsFromString(string)

    def capi_sarray_create_lines_from_string(self, string: bytes,
                                             blankflag: int) -> LPSarray:
        return self.sarrayCreateLinesFromString(string, blankflag)

    def capi_sarray_destroy(self, psa: LPLPSarray):
        self.sarrayDestroy(psa)

    def capi_sarray_copy(self, sa: LPSarray) -> LPSarray:
        return self.sarrayCopy(sa)

    def capi_sarray_clone(self, sa: LPSarray) -> LPSarray:
        return self.sarrayClone(sa)

    def capi_sarray_add_string(self, sa: LPSarray, string: bytes,
                               copyflag: int) -> int:
        return self.sarrayAddString(sa, string, copyflag)

    def capi_sarray_remove_string(self, sa: LPSarray, index: int) -> LP_c_char:
        return self.sarrayRemoveString(sa, index)

    def capi_sarray_replace_string(self, sa: LPSarray, index: int,
                                   newstr: LP_c_char, copyflag: int) -> int:
        return self.sarrayReplaceString(sa, index, newstr, copyflag)

    def capi_sarray_clear(self, sa: LPSarray) -> int:
        return self.sarrayClear(sa)

    def capi_sarray_get_count(self, sa: LPSarray) -> int:
        return self.sarrayGetCount(sa)

    def capi_sarray_get_array(self, sa: LPSarray, pnalloc: c_int_p,
                              pn: c_int_p) -> c_char_p_p:
        return self.sarrayGetArray(sa, pnalloc, pn)

    def capi_sarray_get_string(self, sa: LPSarray, index: int,
                               copyflag: int) -> LP_c_char:
        return self.sarrayGetString(sa, index, copyflag)

    def capi_sarray_get_refcount(self, sa: LPSarray) -> int:
        return self.sarrayGetRefcount(sa)

    def capi_sarray_change_refcount(self, sa: LPSarray, delta: int) -> int:
        return self.sarrayChangeRefcount(sa, delta)

    def capi_sarray_to_string(self, sa: LPSarray, addnlflag: int) -> LP_c_char:
        return self.sarrayToString(sa, addnlflag)

    def capi_sarray_to_string_range(self, sa: LPSarray, first: int,
                                    nstrings: int,
                                    addnlflag: int) -> LP_c_char:
        return self.sarrayToStringRange(sa, first, nstrings, addnlflag)

    def capi_sarray_concat_uniformly(self, sa: LPSarray, n: int,
                                     addnlflag: int) -> LPSarray:
        return self.sarrayConcatUniformly(sa, n, addnlflag)

    def capi_sarray_join(self, sa1: LPSarray, sa2: LPSarray) -> int:
        return self.sarrayJoin(sa1, sa2)

    def capi_sarray_append_range(self, sa1: LPSarray, sa2: LPSarray,
                                 start: int, end: int) -> int:
        return self.sarrayAppendRange(sa1, sa2, start, end)

    def capi_sarray_pad_to_same_size(self, sa1: LPSarray, sa2: LPSarray,
                                     padstring: bytes) -> int:
        return self.sarrayPadToSameSize(sa1, sa2, padstring)

    def capi_sarray_convert_words_to_lines(self, sa: LPSarray,
                                           linesize: int) -> LPSarray:
        return self.sarrayConvertWordsToLines(sa, linesize)

    def capi_sarray_split_string(self, sa: LPSarray, str: bytes,
                                 separators: bytes) -> int:
        return self.sarraySplitString(sa, str, separators)

    def capi_sarray_select_by_substring(self, sain: LPSarray,
                                        substr: bytes) -> LPSarray:
        return self.sarraySelectBySubstring(sain, substr)

    def capi_sarray_select_range(self, sain: LPSarray, first: int,
                                 last: int) -> LPSarray:
        return self.sarraySelectRange(sain, first, last)

    def capi_sarray_parse_range(self, sa: LPSarray, start: int,
                                pactualstart: c_int_p, pend: c_int_p,
                                pnewstart: c_int_p, substr: bytes,
                                loc: int) -> int:
        return self.sarrayParseRange(sa, start, pactualstart, pend, pnewstart,
                                     substr, loc)

    def capi_sarray_read(self, filename: bytes) -> LPSarray:
        return self.sarrayRead(filename)

    def capi_sarray_read_stream(self, fp: LPFile) -> LPSarray:
        return self.sarrayReadStream(fp)

    def capi_sarray_read_mem(self, data: c_ubyte_p, size: int) -> LPSarray:
        return self.sarrayReadMem(data, size)

    def capi_sarray_write(self, filename: bytes, sa: LPSarray) -> int:
        return self.sarrayWrite(filename, sa)

    def capi_sarray_write_stream(self, fp: LPFile, sa: LPSarray) -> int:
        return self.sarrayWriteStream(fp, sa)

    def capi_sarray_write_stderr(self, sa: LPSarray) -> int:
        return self.sarrayWriteStderr(sa)

    def capi_sarray_write_mem(self, pdata: POINTER(c_ubyte_p),
                              psize: c_size_t_p, sa: LPSarray) -> int:
        return self.sarrayWriteMem(pdata, psize, sa)

    def capi_sarray_append(self, filename: bytes, sa: LPSarray) -> int:
        return self.sarrayAppend(filename, sa)

    def capi_get_numbered_pathnames_in_directory(self, dirname: bytes,
                                                 substr: bytes, numpre: int,
                                                 numpost: int,
                                                 maxnum: int) -> LPSarray:
        return self.getNumberedPathnamesInDirectory(dirname, substr, numpre,
                                                    numpost, maxnum)

    def capi_get_sorted_pathnames_in_directory(self, dirname: bytes,
                                               substr: bytes, first: int,
                                               nfiles: int) -> LPSarray:
        return self.getSortedPathnamesInDirectory(dirname, substr, first,
                                                  nfiles)

    def capi_convert_sorted_to_numbered_pathnames(self, sa: LPSarray,
                                                  numpre: int, numpost: int,
                                                  maxnum: int) -> LPSarray:
        return self.convertSortedToNumberedPathnames(sa, numpre, numpost,
                                                     maxnum)

    def capi_get_filenames_in_directory(self, dirname: bytes) -> LPSarray:
        return self.getFilenamesInDirectory(dirname)

    def capi_sarray_sort(self, saout: LPSarray, sain: LPSarray,
                         sortorder: int) -> LPSarray:
        return self.sarraySort(saout, sain, sortorder)

    def capi_sarray_sort_by_index(self, sain: LPSarray,
                                  naindex: LPNuma) -> LPSarray:
        return self.sarraySortByIndex(sain, naindex)

    def capi_string_compare_lexical(self, str1: bytes, str2: bytes) -> int:
        return self.stringCompareLexical(str1, str2)

    def capi_l_asetCreateFromSarray(self, sa: LPSarray) -> LPL_Rbtree:
        return self.l_asetCreateFromSarray(sa)

    def capi_sarray_remove_dups_by_aset(self, sas: LPSarray,
                                        psad: LPLPSarray) -> int:
        return self.sarrayRemoveDupsByAset(sas, psad)

    def capi_sarray_union_by_aset(self, sa1: LPSarray, sa2: LPSarray,
                                  psad: LPLPSarray) -> int:
        return self.sarrayUnionByAset(sa1, sa2, psad)

    def capi_sarray_intersection_by_aset(self, sa1: LPSarray, sa2: LPSarray,
                                         psad: LPLPSarray) -> int:
        return self.sarrayIntersectionByAset(sa1, sa2, psad)

    def capi_l_hmapCreateFromSarray(self, sa: LPSarray) -> LPL_Hashmap:
        return self.l_hmapCreateFromSarray(sa)

    def capi_sarray_remove_dups_by_hmap(self, sas: LPSarray, psad: LPLPSarray,
                                        phmap: LPLPL_Hashmap) -> int:
        return self.sarrayRemoveDupsByHmap(sas, psad, phmap)

    def capi_sarray_union_by_hmap(self, sa1: LPSarray, sa2: LPSarray,
                                  psad: LPLPSarray) -> int:
        return self.sarrayUnionByHmap(sa1, sa2, psad)

    def capi_sarray_intersection_by_hmap(self, sa1: LPSarray, sa2: LPSarray,
                                         psad: LPLPSarray) -> int:
        return self.sarrayIntersectionByHmap(sa1, sa2, psad)

    def capi_sarray_generate_integers(self, n: int) -> LPSarray:
        return self.sarrayGenerateIntegers(n)

    def capi_sarray_lookup_cskv(self, sa: LPSarray, keystring: bytes,
                                pvalstring: c_char_p_p) -> int:
        return self.sarrayLookupCSKV(sa, keystring, pvalstring)

    def capi_pix_scale(self, pixs: LPPix, scalex: float,
                       scaley: float) -> LPPix:
        return self.pixScale(pixs, scalex, scaley)

    def capi_pix_scale_to_size_rel(self, pixs: LPPix, delw: int,
                                   delh: int) -> LPPix:
        return self.pixScaleToSizeRel(pixs, delw, delh)

    def capi_pix_scale_to_size(self, pixs: LPPix, wd: int, hd: int) -> LPPix:
        return self.pixScaleToSize(pixs, wd, hd)

    def capi_pix_scale_to_resolution(self, pixs: LPPix, target: float,
                                     assumed: float,
                                     pscalefact: c_float_p) -> LPPix:
        return self.pixScaleToResolution(pixs, target, assumed, pscalefact)

    def capi_pix_scale_general(self, pixs: LPPix, scalex: float, scaley: float,
                               sharpfract: float, sharpwidth: int) -> LPPix:
        return self.pixScaleGeneral(pixs, scalex, scaley, sharpfract,
                                    sharpwidth)

    def capi_pix_scale_li(self, pixs: LPPix, scalex: float,
                          scaley: float) -> LPPix:
        return self.pixScaleLI(pixs, scalex, scaley)

    def capi_pix_scale_color_li(self, pixs: LPPix, scalex: float,
                                scaley: float) -> LPPix:
        return self.pixScaleColorLI(pixs, scalex, scaley)

    def capi_pix_scale_color2x_li(self, pixs: LPPix) -> LPPix:
        return self.pixScaleColor2xLI(pixs)

    def capi_pix_scale_color4x_li(self, pixs: LPPix) -> LPPix:
        return self.pixScaleColor4xLI(pixs)

    def capi_pix_scale_gray_li(self, pixs: LPPix, scalex: float,
                               scaley: float) -> LPPix:
        return self.pixScaleGrayLI(pixs, scalex, scaley)

    def capi_pix_scale_gray2x_li(self, pixs: LPPix) -> LPPix:
        return self.pixScaleGray2xLI(pixs)

    def capi_pix_scale_gray4x_li(self, pixs: LPPix) -> LPPix:
        return self.pixScaleGray4xLI(pixs)

    def capi_pix_scale_gray2x_li_thresh(self, pixs: LPPix,
                                        thresh: int) -> LPPix:
        return self.pixScaleGray2xLIThresh(pixs, thresh)

    def capi_pix_scale_gray2x_li_dither(self, pixs: LPPix) -> LPPix:
        return self.pixScaleGray2xLIDither(pixs)

    def capi_pix_scale_gray4x_li_thresh(self, pixs: LPPix,
                                        thresh: int) -> LPPix:
        return self.pixScaleGray4xLIThresh(pixs, thresh)

    def capi_pix_scale_gray4x_li_dither(self, pixs: LPPix) -> LPPix:
        return self.pixScaleGray4xLIDither(pixs)

    def capi_pix_scale_by_sampling(self, pixs: LPPix, scalex: float,
                                   scaley: float) -> LPPix:
        return self.pixScaleBySampling(pixs, scalex, scaley)

    def capi_pix_scale_by_sampling_to_size(self, pixs: LPPix, wd: int,
                                           hd: int) -> LPPix:
        return self.pixScaleBySamplingToSize(pixs, wd, hd)

    def capi_pix_scale_by_int_sampling(self, pixs: LPPix,
                                       factor: int) -> LPPix:
        return self.pixScaleByIntSampling(pixs, factor)

    def capi_pix_scale_rgb_to_gray_fast(self, pixs: LPPix, factor: int,
                                        color: int) -> LPPix:
        return self.pixScaleRGBToGrayFast(pixs, factor, color)

    def capi_pix_scale_rgb_to_binary_fast(self, pixs: LPPix, factor: int,
                                          thresh: int) -> LPPix:
        return self.pixScaleRGBToBinaryFast(pixs, factor, thresh)

    def capi_pix_scale_gray_to_binary_fast(self, pixs: LPPix, factor: int,
                                           thresh: int) -> LPPix:
        return self.pixScaleGrayToBinaryFast(pixs, factor, thresh)

    def capi_pix_scale_smooth(self, pix: LPPix, scalex: float,
                              scaley: float) -> LPPix:
        return self.pixScaleSmooth(pix, scalex, scaley)

    def capi_pix_scale_smooth_to_size(self, pixs: LPPix, wd: int,
                                      hd: int) -> LPPix:
        return self.pixScaleSmoothToSize(pixs, wd, hd)

    def capi_pix_scale_rgb_to_gray2(self, pixs: LPPix, rwt: float, gwt: float,
                                    bwt: float) -> LPPix:
        return self.pixScaleRGBToGray2(pixs, rwt, gwt, bwt)

    def capi_pix_scale_area_map(self, pix: LPPix, scalex: float,
                                scaley: float) -> LPPix:
        return self.pixScaleAreaMap(pix, scalex, scaley)

    def capi_pix_scale_area_map2(self, pix: LPPix) -> LPPix:
        return self.pixScaleAreaMap2(pix)

    def capi_pix_scale_area_map_to_size(self, pixs: LPPix, wd: int,
                                        hd: int) -> LPPix:
        return self.pixScaleAreaMapToSize(pixs, wd, hd)

    def capi_pix_scale_binary(self, pixs: LPPix, scalex: float,
                              scaley: float) -> LPPix:
        return self.pixScaleBinary(pixs, scalex, scaley)

    def capi_pix_scale_to_gray(self, pixs: LPPix, scalefactor: float) -> LPPix:
        return self.pixScaleToGray(pixs, scalefactor)

    def capi_pix_scale_to_gray_fast(self, pixs: LPPix,
                                    scalefactor: float) -> LPPix:
        return self.pixScaleToGrayFast(pixs, scalefactor)

    def capi_pix_scale_to_gray2(self, pixs: LPPix) -> LPPix:
        return self.pixScaleToGray2(pixs)

    def capi_pix_scale_to_gray3(self, pixs: LPPix) -> LPPix:
        return self.pixScaleToGray3(pixs)

    def capi_pix_scale_to_gray4(self, pixs: LPPix) -> LPPix:
        return self.pixScaleToGray4(pixs)

    def capi_pix_scale_to_gray6(self, pixs: LPPix) -> LPPix:
        return self.pixScaleToGray6(pixs)

    def capi_pix_scale_to_gray8(self, pixs: LPPix) -> LPPix:
        return self.pixScaleToGray8(pixs)

    def capi_pix_scale_to_gray16(self, pixs: LPPix) -> LPPix:
        return self.pixScaleToGray16(pixs)

    def capi_pix_scale_to_gray_mipmap(self, pixs: LPPix,
                                      scalefactor: float) -> LPPix:
        return self.pixScaleToGrayMipmap(pixs, scalefactor)

    def capi_pix_scale_mipmap(self, pixs1: LPPix, pixs2: LPPix,
                              scale: float) -> LPPix:
        return self.pixScaleMipmap(pixs1, pixs2, scale)

    def capi_pix_expand_replicate(self, pixs: LPPix, factor: int) -> LPPix:
        return self.pixExpandReplicate(pixs, factor)

    def capi_pix_scale_gray_min_max(self, pixs: LPPix, xfact: int, yfact: int,
                                    type: int) -> LPPix:
        return self.pixScaleGrayMinMax(pixs, xfact, yfact, type)

    def capi_pix_scale_gray_min_max2(self, pixs: LPPix, type: int) -> LPPix:
        return self.pixScaleGrayMinMax2(pixs, type)

    def capi_pix_scale_gray_rank_cascade(self, pixs: LPPix, level1: int,
                                         level2: int, level3: int,
                                         level4: int) -> LPPix:
        return self.pixScaleGrayRankCascade(pixs, level1, level2, level3,
                                            level4)

    def capi_pix_scale_gray_rank2(self, pixs: LPPix, rank: int) -> LPPix:
        return self.pixScaleGrayRank2(pixs, rank)

    def capi_pix_scale_and_transfer_alpha(self, pixd: LPPix, pixs: LPPix,
                                          scalex: float,
                                          scaley: float) -> int:
        return self.pixScaleAndTransferAlpha(pixd, pixs, scalex, scaley)

    def capi_pix_scale_with_alpha(self, pixs: LPPix, scalex: float,
                                  scaley: float, pixg: LPPix,
                                  fract: float) -> LPPix:
        return self.pixScaleWithAlpha(pixs, scalex, scaley, pixg, fract)

    def capi_pix_seedfill_binary(self, pixd: LPPix, pixs: LPPix, pixm: LPPix,
                                 connectivity: int) -> LPPix:
        return self.pixSeedfillBinary(pixd, pixs, pixm, connectivity)

    def capi_pix_seedfill_binary_restricted(self, pixd: LPPix, pixs: LPPix,
                                            pixm: LPPix, connectivity: int,
                                            xmax: int, ymax: int) -> LPPix:
        return self.pixSeedfillBinaryRestricted(pixd, pixs, pixm, connectivity,
                                                xmax, ymax)

    def capi_pix_holes_by_filling(self, pixs: LPPix,
                                  connectivity: int) -> LPPix:
        return self.pixHolesByFilling(pixs, connectivity)

    def capi_pix_fill_closed_borders(self, pixs: LPPix,
                                     connectivity: int) -> LPPix:
        return self.pixFillClosedBorders(pixs, connectivity)

    def capi_pix_extract_border_conn_comps(self, pixs: LPPix,
                                           connectivity: int) -> LPPix:
        return self.pixExtractBorderConnComps(pixs, connectivity)

    def capi_pix_remove_border_conn_comps(self, pixs: LPPix,
                                          connectivity: int) -> LPPix:
        return self.pixRemoveBorderConnComps(pixs, connectivity)

    def capi_pix_fill_bg_from_border(self, pixs: LPPix,
                                     connectivity: int) -> LPPix:
        return self.pixFillBgFromBorder(pixs, connectivity)

    def capi_pix_fill_holes_to_bounding_rect(self, pixs: LPPix, minsize: int,
                                             maxhfract: float,
                                             minfgfract: float) -> LPPix:
        return self.pixFillHolesToBoundingRect(pixs, minsize, maxhfract,
                                               minfgfract)

    def capi_pix_seedfill_gray(self, pixs: LPPix, pixm: LPPix,
                               connectivity: int) -> int:
        return self.pixSeedfillGray(pixs, pixm, connectivity)

    def capi_pix_seedfill_gray_inv(self, pixs: LPPix, pixm: LPPix,
                                   connectivity: int) -> int:
        return self.pixSeedfillGrayInv(pixs, pixm, connectivity)

    def capi_pix_seedfill_gray_simple(self, pixs: LPPix, pixm: LPPix,
                                      connectivity: int) -> int:
        return self.pixSeedfillGraySimple(pixs, pixm, connectivity)

    def capi_pix_seedfill_gray_inv_simple(self, pixs: LPPix, pixm: LPPix,
                                          connectivity: int) -> int:
        return self.pixSeedfillGrayInvSimple(pixs, pixm, connectivity)

    def capi_pix_seedfill_gray_basin(self, pixb: LPPix, pixm: LPPix,
                                     delta: int, connectivity: int) -> LPPix:
        return self.pixSeedfillGrayBasin(pixb, pixm, delta, connectivity)

    def capi_pix_distance_function(self, pixs: LPPix, connectivity: int,
                                   outdepth: int, boundcond: int) -> LPPix:
        return self.pixDistanceFunction(pixs, connectivity, outdepth,
                                        boundcond)

    def capi_pix_seedspread(self, pixs: LPPix, connectivity: int) -> LPPix:
        return self.pixSeedspread(pixs, connectivity)

    def capi_pix_local_extrema(self, pixs: LPPix, maxmin: int, minmax: int,
                               ppixmin: LPLPPix, ppixmax: LPLPPix) -> int:
        return self.pixLocalExtrema(pixs, maxmin, minmax, ppixmin, ppixmax)

    def capi_pix_selected_local_extrema(self, pixs: LPPix, mindist: int,
                                        ppixmin: LPLPPix,
                                        ppixmax: LPLPPix) -> int:
        return self.pixSelectedLocalExtrema(pixs, mindist, ppixmin, ppixmax)

    def capi_pix_find_equal_values(self, pixs1: LPPix, pixs2: LPPix) -> LPPix:
        return self.pixFindEqualValues(pixs1, pixs2)

    def capi_pix_select_min_in_conn_comp(self, pixs: LPPix, pixm: LPPix,
                                         ppta: LPLPPta,
                                         pnav: LPLPNuma) -> int:
        return self.pixSelectMinInConnComp(pixs, pixm, ppta, pnav)

    def capi_pix_remove_seeded_components(self, pixd: LPPix, pixs: LPPix,
                                          pixm: LPPix, connectivity: int,
                                          bordersize: int) -> LPPix:
        return self.pixRemoveSeededComponents(pixd, pixs, pixm, connectivity,
                                              bordersize)

    def capi_sela_create(self, n: int) -> LPSela:
        return self.selaCreate(n)

    def capi_sela_destroy(self, psela: LPLPSela):
        self.selaDestroy(psela)

    def capi_sel_create(self, height: int, width: int, name: bytes) -> LPSel:
        return self.selCreate(height, width, name)

    def capi_sel_destroy(self, psel: LPLPSel):
        self.selDestroy(psel)

    def capi_sel_copy(self, sel: LPSel) -> LPSel:
        return self.selCopy(sel)

    def capi_sel_create_brick(self, h: int, w: int, cy: int, cx: int,
                              type: int) -> LPSel:
        return self.selCreateBrick(h, w, cy, cx, type)

    def capi_sel_create_comb(self, factor1: int, factor2: int,
                             direction: int) -> LPSel:
        return self.selCreateComb(factor1, factor2, direction)

    def capi_create2d_int_array(self, sy: int, sx: int) -> POINTER(c_int_p):
        return self.create2dIntArray(sy, sx)

    def capi_sela_add_sel(self, sela: LPSela, sel: LPSel, selname: bytes,
                          copyflag: int) -> int:
        return self.selaAddSel(sela, sel, selname, copyflag)

    def capi_sela_get_count(self, sela: LPSela) -> int:
        return self.selaGetCount(sela)

    def capi_sela_get_sel(self, sela: LPSela, i: int) -> LPSel:
        return self.selaGetSel(sela, i)

    def capi_sel_get_name(self, sel: LPSel) -> LP_c_char:
        return self.selGetName(sel)

    def capi_sel_set_name(self, sel: LPSel, name: bytes) -> int:
        return self.selSetName(sel, name)

    def capi_sela_find_sel_by_name(self, sela: LPSela, name: bytes,
                                   pindex: c_int_p, psel: LPLPSel) -> int:
        return self.selaFindSelByName(sela, name, pindex, psel)

    def capi_sel_get_element(self, sel: LPSel, row: int, col: int,
                             ptype: c_int_p) -> int:
        return self.selGetElement(sel, row, col, ptype)

    def capi_sel_set_element(self, sel: LPSel, row: int, col: int,
                             type: int) -> int:
        return self.selSetElement(sel, row, col, type)

    def capi_sel_get_parameters(self, sel: LPSel, psy: c_int_p, psx: c_int_p,
                                pcy: c_int_p, pcx: c_int_p) -> int:
        return self.selGetParameters(sel, psy, psx, pcy, pcx)

    def capi_sel_set_origin(self, sel: LPSel, cy: int, cx: int) -> int:
        return self.selSetOrigin(sel, cy, cx)

    def capi_sel_get_type_at_origin(self, sel: LPSel, ptype: c_int_p) -> int:
        return self.selGetTypeAtOrigin(sel, ptype)

    def capi_sela_get_brick_name(self, sela: LPSela, hsize: int,
                                 vsize: int) -> LP_c_char:
        return self.selaGetBrickName(sela, hsize, vsize)

    def capi_sela_get_comb_name(self, sela: LPSela, size: int,
                                direction: int) -> LP_c_char:
        return self.selaGetCombName(sela, size, direction)

    def capi_get_composite_parameters(self, size: int, psize1: c_int_p,
                                      psize2: c_int_p, pnameh1: c_char_p_p,
                                      pnameh2: c_char_p_p, pnamev1: c_char_p_p,
                                      pnamev2: c_char_p_p) -> int:
        return self.getCompositeParameters(size, psize1, psize2, pnameh1,
                                           pnameh2, pnamev1, pnamev2)

    def capi_sela_get_selnames(self, sela: LPSela) -> LPSarray:
        return self.selaGetSelnames(sela)

    def capi_sel_find_max_translations(self, sel: LPSel, pxp: c_int_p,
                                       pyp: c_int_p, pxn: c_int_p,
                                       pyn: c_int_p) -> int:
        return self.selFindMaxTranslations(sel, pxp, pyp, pxn, pyn)

    def capi_sel_rotate_orth(self, sel: LPSel, quads: int) -> LPSel:
        return self.selRotateOrth(sel, quads)

    def capi_sela_read(self, fname: bytes) -> LPSela:
        return self.selaRead(fname)

    def capi_sela_read_stream(self, fp: LPFile) -> LPSela:
        return self.selaReadStream(fp)

    def capi_sel_read(self, fname: bytes) -> LPSel:
        return self.selRead(fname)

    def capi_sel_read_stream(self, fp: LPFile) -> LPSel:
        return self.selReadStream(fp)

    def capi_sela_write(self, fname: bytes, sela: LPSela) -> int:
        return self.selaWrite(fname, sela)

    def capi_sela_write_stream(self, fp: LPFile, sela: LPSela) -> int:
        return self.selaWriteStream(fp, sela)

    def capi_sel_write(self, fname: bytes, sel: LPSel) -> int:
        return self.selWrite(fname, sel)

    def capi_sel_write_stream(self, fp: LPFile, sel: LPSel) -> int:
        return self.selWriteStream(fp, sel)

    def capi_sel_create_from_string(self, text: bytes, h: int, w: int,
                                    name: bytes) -> LPSel:
        return self.selCreateFromString(text, h, w, name)

    def capi_sel_print_to_string(self, sel: LPSel) -> LP_c_char:
        return self.selPrintToString(sel)

    def capi_sela_create_from_file(self, filename: bytes) -> LPSela:
        return self.selaCreateFromFile(filename)

    def capi_sel_create_from_pta(self, pta: LPPta, cy: int, cx: int,
                                 name: bytes) -> LPSel:
        return self.selCreateFromPta(pta, cy, cx, name)

    def capi_sel_create_from_pix(self, pix: LPPix, cy: int, cx: int,
                                 name: bytes) -> LPSel:
        return self.selCreateFromPix(pix, cy, cx, name)

    def capi_sel_read_from_color_image(self, pathname: bytes) -> LPSel:
        return self.selReadFromColorImage(pathname)

    def capi_sel_create_from_color_pix(self, pixs: LPPix,
                                       selname: bytes) -> LPSel:
        return self.selCreateFromColorPix(pixs, selname)

    def capi_sela_create_from_color_pixa(self, pixa: LPPixa,
                                         sa: LPSarray) -> LPSela:
        return self.selaCreateFromColorPixa(pixa, sa)

    def capi_sel_display_in_pix(self, sel: LPSel, size: int,
                                gthick: int) -> LPPix:
        return self.selDisplayInPix(sel, size, gthick)

    def capi_sela_display_in_pix(self, sela: LPSela, size: int, gthick: int,
                                 spacing: int, ncols: int) -> LPPix:
        return self.selaDisplayInPix(sela, size, gthick, spacing, ncols)

    def capi_sela_add_basic(self, sela: LPSela) -> LPSela:
        return self.selaAddBasic(sela)

    def capi_sela_add_hit_miss(self, sela: LPSela) -> LPSela:
        return self.selaAddHitMiss(sela)

    def capi_sela_add_dwa_linear(self, sela: LPSela) -> LPSela:
        return self.selaAddDwaLinear(sela)

    def capi_sela_add_dwa_combs(self, sela: LPSela) -> LPSela:
        return self.selaAddDwaCombs(sela)

    def capi_sela_add_cross_junctions(self, sela: LPSela, hlsize: float,
                                      mdist: float, norient: int,
                                      debugflag: int) -> LPSela:
        return self.selaAddCrossJunctions(sela, hlsize, mdist, norient,
                                          debugflag)

    def capi_sela_add_tjunctions(self, sela: LPSela, hlsize: float,
                                 mdist: float, norient: int,
                                 debugflag: int) -> LPSela:
        return self.selaAddTJunctions(sela, hlsize, mdist, norient, debugflag)

    def capi_sela4cc_thin(self, sela: LPSela) -> LPSela:
        return self.sela4ccThin(sela)

    def capi_sela8cc_thin(self, sela: LPSela) -> LPSela:
        return self.sela8ccThin(sela)

    def capi_sela4and8cc_thin(self, sela: LPSela) -> LPSela:
        return self.sela4and8ccThin(sela)

    def capi_sel_make_plus_sign(self, size: int, linewidth: int) -> LPSel:
        return self.selMakePlusSign(size, linewidth)

    def capi_pix_generate_sel_with_runs(self, pixs: LPPix, nhlines: int,
                                        nvlines: int, distance: int,
                                        minlength: int, toppix: int,
                                        botpix: int, leftpix: int,
                                        rightpix: int,
                                        ppixe: LPLPPix) -> LPSel:
        return self.pixGenerateSelWithRuns(pixs, nhlines, nvlines, distance,
                                           minlength, toppix, botpix, leftpix,
                                           rightpix, ppixe)

    def capi_pix_generate_sel_random(self, pixs: LPPix, hitfract: float,
                                     missfract: float, distance: int,
                                     toppix: int, botpix: int, leftpix: int,
                                     rightpix: int, ppixe: LPLPPix) -> LPSel:
        return self.pixGenerateSelRandom(pixs, hitfract, missfract, distance,
                                         toppix, botpix, leftpix, rightpix,
                                         ppixe)

    def capi_pix_generate_sel_boundary(self, pixs: LPPix, hitdist: int,
                                       missdist: int, hitskip: int,
                                       missskip: int, topflag: int,
                                       botflag: int, leftflag: int,
                                       rightflag: int,
                                       ppixe: LPLPPix) -> LPSel:
        return self.pixGenerateSelBoundary(pixs, hitdist, missdist, hitskip,
                                           missskip, topflag, botflag,
                                           leftflag, rightflag, ppixe)

    def capi_pix_get_run_centers_on_line(self, pixs: LPPix, x: int, y: int,
                                         minlength: int) -> LPNuma:
        return self.pixGetRunCentersOnLine(pixs, x, y, minlength)

    def capi_pix_get_runs_on_line(self, pixs: LPPix, x1: int, y1: int, x2: int,
                                  y2: int) -> LPNuma:
        return self.pixGetRunsOnLine(pixs, x1, y1, x2, y2)

    def capi_pix_subsample_boundary_pixels(self, pixs: LPPix,
                                           skip: int) -> LPPta:
        return self.pixSubsampleBoundaryPixels(pixs, skip)

    def capi_adjacent_on_pixel_in_raster(self, pixs: LPPix, x: int, y: int,
                                         pxa: c_int_p, pya: c_int_p) -> int:
        return self.adjacentOnPixelInRaster(pixs, x, y, pxa, pya)

    def capi_pix_display_hit_miss_sel(self, pixs: LPPix, sel: LPSel,
                                      scalefactor: int, hitcolor: int,
                                      misscolor: int) -> LPPix:
        return self.pixDisplayHitMissSel(pixs, sel, scalefactor, hitcolor,
                                         misscolor)

    def capi_pix_hshear(self, pixd: LPPix, pixs: LPPix, yloc: int,
                        radang: float, incolor: int) -> LPPix:
        return self.pixHShear(pixd, pixs, yloc, radang, incolor)

    def capi_pix_vshear(self, pixd: LPPix, pixs: LPPix, xloc: int,
                        radang: float, incolor: int) -> LPPix:
        return self.pixVShear(pixd, pixs, xloc, radang, incolor)

    def capi_pix_hshear_corner(self, pixd: LPPix, pixs: LPPix, radang: float,
                               incolor: int) -> LPPix:
        return self.pixHShearCorner(pixd, pixs, radang, incolor)

    def capi_pix_vshear_corner(self, pixd: LPPix, pixs: LPPix, radang: float,
                               incolor: int) -> LPPix:
        return self.pixVShearCorner(pixd, pixs, radang, incolor)

    def capi_pix_hshear_center(self, pixd: LPPix, pixs: LPPix, radang: float,
                               incolor: int) -> LPPix:
        return self.pixHShearCenter(pixd, pixs, radang, incolor)

    def capi_pix_vshear_center(self, pixd: LPPix, pixs: LPPix, radang: float,
                               incolor: int) -> LPPix:
        return self.pixVShearCenter(pixd, pixs, radang, incolor)

    def capi_pix_hshear_ip(self, pixs: LPPix, yloc: int, radang: float,
                           incolor: int) -> int:
        return self.pixHShearIP(pixs, yloc, radang, incolor)

    def capi_pix_vshear_ip(self, pixs: LPPix, xloc: int, radang: float,
                           incolor: int) -> int:
        return self.pixVShearIP(pixs, xloc, radang, incolor)

    def capi_pix_hshear_li(self, pixs: LPPix, yloc: int, radang: float,
                           incolor: int) -> LPPix:
        return self.pixHShearLI(pixs, yloc, radang, incolor)

    def capi_pix_vshear_li(self, pixs: LPPix, xloc: int, radang: float,
                           incolor: int) -> LPPix:
        return self.pixVShearLI(pixs, xloc, radang, incolor)

    def capi_pix_deskew_both(self, pixs: LPPix, redsearch: int) -> LPPix:
        return self.pixDeskewBoth(pixs, redsearch)

    def capi_pix_deskew(self, pixs: LPPix, redsearch: int) -> LPPix:
        return self.pixDeskew(pixs, redsearch)

    def capi_pix_find_skew_and_deskew(self, pixs: LPPix, redsearch: int,
                                      pangle: c_float_p,
                                      pconf: c_float_p) -> LPPix:
        return self.pixFindSkewAndDeskew(pixs, redsearch, pangle, pconf)

    def capi_pix_deskew_general(self, pixs: LPPix, redsweep: int,
                                sweeprange: float, sweepdelta: float,
                                redsearch: int, thresh: int, pangle: c_float_p,
                                pconf: c_float_p) -> LPPix:
        return self.pixDeskewGeneral(pixs, redsweep, sweeprange, sweepdelta,
                                     redsearch, thresh, pangle, pconf)

    def capi_pix_find_skew(self, pixs: LPPix, pangle: c_float_p,
                           pconf: c_float_p) -> int:
        return self.pixFindSkew(pixs, pangle, pconf)

    def capi_pix_find_skew_sweep(self, pixs: LPPix, pangle: c_float_p,
                                 reduction: int, sweeprange: float,
                                 sweepdelta: float) -> int:
        return self.pixFindSkewSweep(pixs, pangle, reduction, sweeprange,
                                     sweepdelta)

    def capi_pix_find_skew_sweep_and_search(self, pixs: LPPix,
                                            pangle: c_float_p,
                                            pconf: c_float_p, redsweep: int,
                                            redsearch: int, sweeprange: float,
                                            sweepdelta: float,
                                            minbsdelta: float) -> int:
        return self.pixFindSkewSweepAndSearch(pixs, pangle, pconf, redsweep,
                                              redsearch, sweeprange,
                                              sweepdelta, minbsdelta)

    def capi_pix_find_skew_sweep_and_search_score(self, pixs: LPPix,
                                                  pangle: c_float_p,
                                                  pconf: c_float_p,
                                                  pendscore: c_float_p,
                                                  redsweep: int,
                                                  redsearch: int,
                                                  sweepcenter: float,
                                                  sweeprange: float,
                                                  sweepdelta: float,
                                                  minbsdelta: float) -> int:
        return self.pixFindSkewSweepAndSearchScore(pixs, pangle, pconf,
                                                   pendscore, redsweep,
                                                   redsearch, sweepcenter,
                                                   sweeprange, sweepdelta,
                                                   minbsdelta)

    def capi_pix_find_skew_sweep_and_search_score_pivot(self, pixs: LPPix,
                                                        pangle: c_float_p,
                                                        pconf: c_float_p,
                                                        pendscore: c_float_p,
                                                        redsweep: int,
                                                        redsearch: int,
                                                        sweepcenter: float,
                                                        sweeprange: float,
                                                        sweepdelta: float,
                                                        minbsdelta: float,
                                                        pivot: int) -> int:
        return self.pixFindSkewSweepAndSearchScorePivot(pixs, pangle, pconf,
                                                        pendscore, redsweep,
                                                        redsearch, sweepcenter,
                                                        sweeprange, sweepdelta,
                                                        minbsdelta, pivot)

    def capi_pix_find_skew_orthogonal_range(self, pixs: LPPix,
                                            pangle: c_float_p,
                                            pconf: c_float_p, redsweep: int,
                                            redsearch: int, sweeprange: float,
                                            sweepdelta: float,
                                            minbsdelta: float,
                                            confprior: float) -> int:
        return self.pixFindSkewOrthogonalRange(pixs, pangle, pconf, redsweep,
                                               redsearch, sweeprange,
                                               sweepdelta, minbsdelta,
                                               confprior)

    def capi_pix_find_differential_square_sum(self, pixs: LPPix,
                                              psum: c_float_p) -> int:
        return self.pixFindDifferentialSquareSum(pixs, psum)

    def capi_pix_find_normalized_square_sum(self, pixs: LPPix,
                                            phratio: c_float_p,
                                            pvratio: c_float_p,
                                            pfract: c_float_p) -> int:
        return self.pixFindNormalizedSquareSum(pixs, phratio, pvratio, pfract)

    def capi_pix_read_stream_spix(self, fp: LPFile) -> LPPix:
        return self.pixReadStreamSpix(fp)

    def capi_read_header_spix(self, filename: bytes, pwidth: c_int_p,
                              pheight: c_int_p, pbps: c_int_p, pspp: c_int_p,
                              piscmap: c_int_p) -> int:
        return self.readHeaderSpix(filename, pwidth, pheight, pbps, pspp,
                                   piscmap)

    def capi_fread_header_spix(self, fp: LPFile, pwidth: c_int_p,
                               pheight: c_int_p, pbps: c_int_p, pspp: c_int_p,
                               piscmap: c_int_p) -> int:
        return self.freadHeaderSpix(fp, pwidth, pheight, pbps, pspp, piscmap)

    def capi_sread_header_spix(self, data: c_uint_p, size: int,
                               pwidth: c_int_p, pheight: c_int_p,
                               pbps: c_int_p, pspp: c_int_p,
                               piscmap: c_int_p) -> int:
        return self.sreadHeaderSpix(data, size, pwidth, pheight, pbps, pspp,
                                    piscmap)

    def capi_pix_write_stream_spix(self, fp: LPFile, pix: LPPix) -> int:
        return self.pixWriteStreamSpix(fp, pix)

    def capi_pix_read_mem_spix(self, data: c_ubyte_p, size: int) -> LPPix:
        return self.pixReadMemSpix(data, size)

    def capi_pix_write_mem_spix(self, pdata: POINTER(c_ubyte_p),
                                psize: c_size_t_p, pix: LPPix) -> int:
        return self.pixWriteMemSpix(pdata, psize, pix)

    def capi_pix_serialize_to_memory(self, pixs: LPPix,
                                     pdata: POINTER(c_uint_p),
                                     pnbytes: c_size_t_p) -> int:
        return self.pixSerializeToMemory(pixs, pdata, pnbytes)

    def capi_pix_deserialize_from_memory(self, data: c_uint_p,
                                         nbytes: int) -> LPPix:
        return self.pixDeserializeFromMemory(data, nbytes)

    def capi_lstack_create(self, n: int) -> LPL_Stack:
        return self.lstackCreate(n)

    def capi_lstack_destroy(self, plstack: LPLPL_Stack, freeflag: int):
        self.lstackDestroy(plstack, freeflag)

    def capi_lstack_add(self, lstack: LPL_Stack, item: c_void_p) -> int:
        return self.lstackAdd(lstack, item)

    def capi_lstack_remove(self, lstack: LPL_Stack) -> c_void_p:
        return self.lstackRemove(lstack)

    def capi_lstack_get_count(self, lstack: LPL_Stack) -> int:
        return self.lstackGetCount(lstack)

    def capi_lstack_print(self, fp: LPFile, lstack: LPL_Stack) -> int:
        return self.lstackPrint(fp, lstack)

    def capi_strcode_create(self, fileno: int) -> LPL_StrCode:
        return self.strcodeCreate(fileno)

    def capi_strcode_create_from_file(self, filein: bytes, fileno: int,
                                      outdir: bytes) -> int:
        return self.strcodeCreateFromFile(filein, fileno, outdir)

    def capi_strcode_generate(self, strcode: LPL_StrCode, filein: bytes,
                              type: bytes) -> int:
        return self.strcodeGenerate(strcode, filein, type)

    def capi_strcode_finalize(self, pstrcode: LPLPL_StrCode,
                              outdir: bytes) -> int:
        return self.strcodeFinalize(pstrcode, outdir)

    def capi_l_getStructStrFromFile(self, filename: bytes, field: int,
                                    pstr: c_char_p_p) -> int:
        return self.l_getStructStrFromFile(filename, field, pstr)

    def capi_pix_find_stroke_length(self, pixs: LPPix, tab8: c_int_p,
                                    plength: c_int_p) -> int:
        return self.pixFindStrokeLength(pixs, tab8, plength)

    def capi_pix_find_stroke_width(self, pixs: LPPix, thresh: float,
                                   tab8: c_int_p, pwidth: c_float_p,
                                   pnahisto: LPLPNuma) -> int:
        return self.pixFindStrokeWidth(pixs, thresh, tab8, pwidth, pnahisto)

    def capi_pixa_find_stroke_width(self, pixa: LPPixa, thresh: float,
                                    tab8: c_int_p, debug: int) -> LPNuma:
        return self.pixaFindStrokeWidth(pixa, thresh, tab8, debug)

    def capi_pixa_modify_stroke_width(self, pixas: LPPixa,
                                      targetw: float) -> LPPixa:
        return self.pixaModifyStrokeWidth(pixas, targetw)

    def capi_pix_modify_stroke_width(self, pixs: LPPix, width: float,
                                     targetw: float) -> LPPix:
        return self.pixModifyStrokeWidth(pixs, width, targetw)

    def capi_pixa_set_stroke_width(self, pixas: LPPixa, width: int,
                                   thinfirst: int,
                                   connectivity: int) -> LPPixa:
        return self.pixaSetStrokeWidth(pixas, width, thinfirst, connectivity)

    def capi_pix_set_stroke_width(self, pixs: LPPix, width: int,
                                  thinfirst: int, connectivity: int) -> LPPix:
        return self.pixSetStrokeWidth(pixs, width, thinfirst, connectivity)

    def capi_sudoku_read_file(self, filename: bytes) -> c_int_p:
        return self.sudokuReadFile(filename)

    def capi_sudoku_read_string(self, str: bytes) -> c_int_p:
        return self.sudokuReadString(str)

    def capi_sudoku_create(self, array: c_int_p) -> LPL_Sudoku:
        return self.sudokuCreate(array)

    def capi_sudoku_destroy(self, psud: LPLPL_Sudoku):
        self.sudokuDestroy(psud)

    def capi_sudoku_solve(self, sud: LPL_Sudoku) -> int:
        return self.sudokuSolve(sud)

    def capi_sudoku_test_uniqueness(self, array: c_int_p,
                                    punique: c_int_p) -> int:
        return self.sudokuTestUniqueness(array, punique)

    def capi_sudoku_generate(self, array: c_int_p, seed: int, minelems: int,
                             maxtries: int) -> LPL_Sudoku:
        return self.sudokuGenerate(array, seed, minelems, maxtries)

    def capi_sudoku_output(self, sud: LPL_Sudoku, arraytype: int) -> int:
        return self.sudokuOutput(sud, arraytype)

    def capi_pix_add_single_textblock(self, pixs: LPPix, bmf: LPL_Bmf,
                                      textstr: bytes, val: int, location: int,
                                      poverflow: c_int_p) -> LPPix:
        return self.pixAddSingleTextblock(pixs, bmf, textstr, val, location,
                                          poverflow)

    def capi_pix_add_textlines(self, pixs: LPPix, bmf: LPL_Bmf, textstr: bytes,
                               val: int, location: int) -> LPPix:
        return self.pixAddTextlines(pixs, bmf, textstr, val, location)

    def capi_pix_set_textblock(self, pixs: LPPix, bmf: LPL_Bmf, textstr: bytes,
                               val: int, x0: int, y0: int, wtext: int,
                               firstindent: int, poverflow: c_int_p) -> int:
        return self.pixSetTextblock(pixs, bmf, textstr, val, x0, y0, wtext,
                                    firstindent, poverflow)

    def capi_pix_set_textline(self, pixs: LPPix, bmf: LPL_Bmf, textstr: bytes,
                              val: int, x0: int, y0: int, pwidth: c_int_p,
                              poverflow: c_int_p) -> int:
        return self.pixSetTextline(pixs, bmf, textstr, val, x0, y0, pwidth,
                                   poverflow)

    def capi_pixa_add_text_number(self, pixas: LPPixa, bmf: LPL_Bmf,
                                  na: LPNuma, val: int,
                                  location: int) -> LPPixa:
        return self.pixaAddTextNumber(pixas, bmf, na, val, location)

    def capi_pixa_add_textlines(self, pixas: LPPixa, bmf: LPL_Bmf,
                                sa: LPSarray, val: int,
                                location: int) -> LPPixa:
        return self.pixaAddTextlines(pixas, bmf, sa, val, location)

    def capi_pixa_add_pix_with_text(self, pixa: LPPixa, pixs: LPPix,
                                    reduction: int, bmf: LPL_Bmf,
                                    textstr: bytes, val: int,
                                    location: int) -> int:
        return self.pixaAddPixWithText(pixa, pixs, reduction, bmf, textstr,
                                       val, location)

    def capi_bmf_get_line_strings(self, bmf: LPL_Bmf, textstr: bytes,
                                  maxw: int, firstindent: int,
                                  ph: c_int_p) -> LPSarray:
        return self.bmfGetLineStrings(bmf, textstr, maxw, firstindent, ph)

    def capi_bmf_get_word_widths(self, bmf: LPL_Bmf, textstr: bytes,
                                 sa: LPSarray) -> LPNuma:
        return self.bmfGetWordWidths(bmf, textstr, sa)

    def capi_bmf_get_string_width(self, bmf: LPL_Bmf, textstr: bytes,
                                  pw: c_int_p) -> int:
        return self.bmfGetStringWidth(bmf, textstr, pw)

    def capi_split_string_to_paragraphs(self, textstr: LP_c_char,
                                        splitflag: int) -> LPSarray:
        return self.splitStringToParagraphs(textstr, splitflag)

    def capi_pix_read_tiff(self, filename: bytes, n: int) -> LPPix:
        return self.pixReadTiff(filename, n)

    def capi_pix_read_stream_tiff(self, fp: LPFile, n: int) -> LPPix:
        return self.pixReadStreamTiff(fp, n)

    def capi_pix_write_tiff(self, filename: bytes, pix: LPPix, comptype: int,
                            modestr: bytes) -> int:
        return self.pixWriteTiff(filename, pix, comptype, modestr)

    def capi_pix_write_tiff_custom(self, filename: bytes, pix: LPPix,
                                   comptype: int, modestr: bytes,
                                   natags: LPNuma, savals: LPSarray,
                                   satypes: LPSarray, nasizes: LPNuma) -> int:
        return self.pixWriteTiffCustom(filename, pix, comptype, modestr,
                                       natags, savals, satypes, nasizes)

    def capi_pix_write_stream_tiff(self, fp: LPFile, pix: LPPix,
                                   comptype: int) -> int:
        return self.pixWriteStreamTiff(fp, pix, comptype)

    def capi_pix_write_stream_tiff_wa(self, fp: LPFile, pix: LPPix,
                                      comptype: int, modestr: bytes) -> int:
        return self.pixWriteStreamTiffWA(fp, pix, comptype, modestr)

    def capi_pix_read_from_multipage_tiff(self, fname: bytes,
                                          poffset: c_size_t_p) -> LPPix:
        return self.pixReadFromMultipageTiff(fname, poffset)

    def capi_pixa_read_multipage_tiff(self, filename: bytes) -> LPPixa:
        return self.pixaReadMultipageTiff(filename)

    def capi_pixa_write_multipage_tiff(self, fname: bytes,
                                       pixa: LPPixa) -> int:
        return self.pixaWriteMultipageTiff(fname, pixa)

    def capi_write_multipage_tiff(self, dirin: bytes, substr: bytes,
                                  fileout: bytes) -> int:
        return self.writeMultipageTiff(dirin, substr, fileout)

    def capi_write_multipage_tiff_sa(self, sa: LPSarray,
                                     fileout: bytes) -> int:
        return self.writeMultipageTiffSA(sa, fileout)

    def capi_fprint_tiff_info(self, fpout: LPFile, tiffile: bytes) -> int:
        return self.fprintTiffInfo(fpout, tiffile)

    def capi_tiff_get_count(self, fp: LPFile, pn: c_int_p) -> int:
        return self.tiffGetCount(fp, pn)

    def capi_get_tiff_resolution(self, fp: LPFile, pxres: c_int_p,
                                 pyres: c_int_p) -> int:
        return self.getTiffResolution(fp, pxres, pyres)

    def capi_read_header_tiff(self, filename: bytes, n: int, pw: c_int_p,
                              ph: c_int_p, pbps: c_int_p, pspp: c_int_p,
                              pres: c_int_p, pcmap: c_int_p,
                              pformat: c_int_p) -> int:
        return self.readHeaderTiff(filename, n, pw, ph, pbps, pspp, pres,
                                   pcmap, pformat)

    def capi_fread_header_tiff(self, fp: LPFile, n: int, pw: c_int_p,
                               ph: c_int_p, pbps: c_int_p, pspp: c_int_p,
                               pres: c_int_p, pcmap: c_int_p,
                               pformat: c_int_p) -> int:
        return self.freadHeaderTiff(fp, n, pw, ph, pbps, pspp, pres, pcmap,
                                    pformat)

    def capi_read_header_mem_tiff(self, cdata: c_ubyte_p, size: int, n: int,
                                  pw: c_int_p, ph: c_int_p, pbps: c_int_p,
                                  pspp: c_int_p, pres: c_int_p, pcmap: c_int_p,
                                  pformat: c_int_p) -> int:
        return self.readHeaderMemTiff(cdata, size, n, pw, ph, pbps, pspp, pres,
                                      pcmap, pformat)

    def capi_find_tiff_compression(self, fp: LPFile,
                                   pcomptype: c_int_p) -> int:
        return self.findTiffCompression(fp, pcomptype)

    def capi_extractg4data_from_file(self, filein: bytes,
                                     pdata: POINTER(c_ubyte_p),
                                     pnbytes: c_size_t_p, pw: c_int_p,
                                     ph: c_int_p,
                                     pminisblack: c_int_p) -> int:
        return self.extractG4DataFromFile(filein, pdata, pnbytes, pw, ph,
                                          pminisblack)

    def capi_pix_read_mem_tiff(self, cdata: c_ubyte_p, size: int,
                               n: int) -> LPPix:
        return self.pixReadMemTiff(cdata, size, n)

    def capi_pix_read_mem_from_multipage_tiff(self, cdata: c_ubyte_p,
                                              size: int,
                                              poffset: c_size_t_p) -> LPPix:
        return self.pixReadMemFromMultipageTiff(cdata, size, poffset)

    def capi_pixa_read_mem_multipage_tiff(self, data: c_ubyte_p,
                                          size: int) -> LPPixa:
        return self.pixaReadMemMultipageTiff(data, size)

    def capi_pixa_write_mem_multipage_tiff(self, pdata: POINTER(c_ubyte_p),
                                           psize: c_size_t_p,
                                           pixa: LPPixa) -> int:
        return self.pixaWriteMemMultipageTiff(pdata, psize, pixa)

    def capi_pix_write_mem_tiff(self, pdata: POINTER(c_ubyte_p),
                                psize: c_size_t_p, pix: LPPix,
                                comptype: int) -> int:
        return self.pixWriteMemTiff(pdata, psize, pix, comptype)

    def capi_pix_write_mem_tiff_custom(self, pdata: POINTER(c_ubyte_p),
                                       psize: c_size_t_p, pix: LPPix,
                                       comptype: int, natags: LPNuma,
                                       savals: LPSarray, satypes: LPSarray,
                                       nasizes: LPNuma) -> int:
        return self.pixWriteMemTiffCustom(pdata, psize, pix, comptype, natags,
                                          savals, satypes, nasizes)

    def capi_set_msg_severity(self, newsev: int) -> int:
        return self.setMsgSeverity(newsev)

    def capi_return_error_int(self, msg: bytes, procname: bytes,
                              ival: int) -> int:
        return self.returnErrorInt(msg, procname, ival)

    def capi_return_error_float(self, msg: bytes, procname: bytes,
                                fval: float) -> float:
        return self.returnErrorFloat(msg, procname, fval)

    def capi_return_error_ptr(self, msg: bytes, procname: bytes,
                              pval: c_void_p) -> c_void_p:
        return self.returnErrorPtr(msg, procname, pval)

    def capi_lept_set_stderr_handler(self, handler: handler_fn):
        self.leptSetStderrHandler(handler)

    def capi_lept_stderr(self, fmt: bytes):
        self.lept_stderr(fmt)

    def capi_files_are_identical(self, fname1: bytes, fname2: bytes,
                                 psame: c_int_p) -> int:
        return self.filesAreIdentical(fname1, fname2, psame)

    def capi_convert_on_little_end16(self, shortin: int) -> int:
        return self.convertOnLittleEnd16(shortin)

    def capi_convert_on_big_end16(self, shortin: int) -> int:
        return self.convertOnBigEnd16(shortin)

    def capi_convert_on_little_end32(self, wordin: int) -> int:
        return self.convertOnLittleEnd32(wordin)

    def capi_convert_on_big_end32(self, wordin: int) -> int:
        return self.convertOnBigEnd32(wordin)

    def capi_file_corrupt_by_deletion(self, filein: bytes, loc: float,
                                      size: float, fileout: bytes) -> int:
        return self.fileCorruptByDeletion(filein, loc, size, fileout)

    def capi_file_corrupt_by_mutation(self, filein: bytes, loc: float,
                                      size: float, fileout: bytes) -> int:
        return self.fileCorruptByMutation(filein, loc, size, fileout)

    def capi_file_replace_bytes(self, filein: bytes, start: int, nbytes: int,
                                newdata: c_ubyte_p, newsize: int,
                                fileout: bytes) -> int:
        return self.fileReplaceBytes(filein, start, nbytes, newdata, newsize,
                                     fileout)

    def capi_gen_random_int_on_interval(self, start: int, end: int, seed: int,
                                        pval: c_int_p) -> int:
        return self.genRandomIntOnInterval(start, end, seed, pval)

    def capi_lept_roundftoi(self, fval: float) -> int:
        return self.lept_roundftoi(fval)

    def capi_l_hashStringToUint64(self, str: bytes,
                                  phash: c_ulonglong_p) -> int:
        return self.l_hashStringToUint64(str, phash)

    def capi_l_hashStringToUint64Fast(self, str: bytes,
                                      phash: c_ulonglong_p) -> int:
        return self.l_hashStringToUint64Fast(str, phash)

    def capi_l_hashPtToUint64(self, x: int, y: int,
                              phash: c_ulonglong_p) -> int:
        return self.l_hashPtToUint64(x, y, phash)

    def capi_l_hashFloat64ToUint64(self, val: float,
                                   phash: c_ulonglong_p) -> int:
        return self.l_hashFloat64ToUint64(val, phash)

    def capi_find_next_larger_prime(self, start: int, pprime: c_uint_p) -> int:
        return self.findNextLargerPrime(start, pprime)

    def capi_lept_isPrime(self, n: int, pis_prime: c_int_p,
                          pfactor: c_uint_p) -> int:
        return self.lept_isPrime(n, pis_prime, pfactor)

    def capi_convert_int_to_gray_code(self, val: int) -> int:
        return self.convertIntToGrayCode(val)

    def capi_convert_gray_code_to_int(self, val: int) -> int:
        return self.convertGrayCodeToInt(val)

    def capi_get_leptonica_version(self) -> LP_c_char:
        return self.getLeptonicaVersion()

    def capi_start_timer(self):
        self.startTimer()

    def capi_stop_timer(self) -> float:
        return self.stopTimer()

    def capi_start_timer_nested(self) -> c_void_p:
        return self.startTimerNested()

    def capi_stop_timer_nested(self, rusage_start: c_void_p) -> float:
        return self.stopTimerNested(rusage_start)

    def capi_l_getCurrentTime(self, sec: c_int_p, usec: c_int_p):
        self.l_getCurrentTime(sec, usec)

    def capi_start_wall_timer(self) -> LPL_WallTimer:
        return self.startWallTimer()

    def capi_stop_wall_timer(self, ptimer: LPLPL_WallTimer) -> float:
        return self.stopWallTimer(ptimer)

    def capi_l_getFormattedDate(self) -> LP_c_char:
        return self.l_getFormattedDate()

    def capi_string_new(self, src: bytes) -> LP_c_char:
        return self.stringNew(src)

    def capi_string_copy(self, dest: LP_c_char, src: bytes, n: int) -> int:
        return self.stringCopy(dest, src, n)

    def capi_string_copy_segment(self, src: bytes, start: int,
                                 nbytes: int) -> LP_c_char:
        return self.stringCopySegment(src, start, nbytes)

    def capi_string_replace(self, pdest: c_char_p_p, src: bytes) -> int:
        return self.stringReplace(pdest, src)

    def capi_string_length(self, src: bytes, size: int) -> int:
        return self.stringLength(src, size)

    def capi_string_cat(self, dest: LP_c_char, size: int, src: bytes) -> int:
        return self.stringCat(dest, size, src)

    def capi_string_concat_new(self, first: bytes) -> LP_c_char:
        return self.stringConcatNew(first)

    def capi_string_join(self, src1: bytes, src2: bytes) -> LP_c_char:
        return self.stringJoin(src1, src2)

    def capi_string_join_ip(self, psrc1: c_char_p_p, src2: bytes) -> int:
        return self.stringJoinIP(psrc1, src2)

    def capi_string_reverse(self, src: bytes) -> LP_c_char:
        return self.stringReverse(src)

    def capi_strtok_safe(self, cstr: LP_c_char, seps: bytes,
                         psaveptr: c_char_p_p) -> LP_c_char:
        return self.strtokSafe(cstr, seps, psaveptr)

    def capi_string_split_on_token(self, cstr: LP_c_char, seps: bytes,
                                   phead: c_char_p_p,
                                   ptail: c_char_p_p) -> int:
        return self.stringSplitOnToken(cstr, seps, phead, ptail)

    def capi_string_check_for_chars(self, src: bytes, chars: bytes,
                                    pfound: c_int_p) -> int:
        return self.stringCheckForChars(src, chars, pfound)

    def capi_string_remove_chars(self, src: bytes,
                                 remchars: bytes) -> LP_c_char:
        return self.stringRemoveChars(src, remchars)

    def capi_string_replace_each_substr(self, src: bytes, sub1: bytes,
                                        sub2: bytes,
                                        pcount: c_int_p) -> LP_c_char:
        return self.stringReplaceEachSubstr(src, sub1, sub2, pcount)

    def capi_string_replace_substr(self, src: bytes, sub1: bytes, sub2: bytes,
                                   ploc: c_int_p,
                                   pfound: c_int_p) -> LP_c_char:
        return self.stringReplaceSubstr(src, sub1, sub2, ploc, pfound)

    def capi_string_find_each_substr(self, src: bytes, sub: bytes) -> LPL_Dna:
        return self.stringFindEachSubstr(src, sub)

    def capi_string_find_substr(self, src: bytes, sub: bytes,
                                ploc: c_int_p) -> int:
        return self.stringFindSubstr(src, sub, ploc)

    def capi_array_replace_each_sequence(self, datas: c_ubyte_p, dataslen: int,
                                         seq: c_ubyte_p, seqlen: int,
                                         newseq: c_ubyte_p, newseqlen: int,
                                         pdatadlen: c_size_t_p,
                                         pcount: c_int_p) -> c_ubyte_p:
        return self.arrayReplaceEachSequence(datas, dataslen, seq, seqlen,
                                             newseq, newseqlen, pdatadlen,
                                             pcount)

    def capi_array_find_each_sequence(self, data: c_ubyte_p, datalen: int,
                                      sequence: c_ubyte_p,
                                      seqlen: int) -> LPL_Dna:
        return self.arrayFindEachSequence(data, datalen, sequence, seqlen)

    def capi_array_find_sequence(self, data: c_ubyte_p, datalen: int,
                                 sequence: c_ubyte_p, seqlen: int,
                                 poffset: c_int_p, pfound: c_int_p) -> int:
        return self.arrayFindSequence(data, datalen, sequence, seqlen, poffset,
                                      pfound)

    def capi_realloc_new(self, pindata: POINTER(c_void_p), oldsize: int,
                         newsize: int) -> c_void_p:
        return self.reallocNew(pindata, oldsize, newsize)

    def capi_l_binaryRead(self, filename: bytes,
                          pnbytes: c_size_t_p) -> c_ubyte_p:
        return self.l_binaryRead(filename, pnbytes)

    def capi_l_binaryReadStream(self, fp: LPFile,
                                pnbytes: c_size_t_p) -> c_ubyte_p:
        return self.l_binaryReadStream(fp, pnbytes)

    def capi_l_binaryReadSelect(self, filename: bytes, start: int, nbytes: int,
                                pnread: c_size_t_p) -> c_ubyte_p:
        return self.l_binaryReadSelect(filename, start, nbytes, pnread)

    def capi_l_binaryReadSelectStream(self, fp: LPFile, start: int,
                                      nbytes: int,
                                      pnread: c_size_t_p) -> c_ubyte_p:
        return self.l_binaryReadSelectStream(fp, start, nbytes, pnread)

    def capi_l_binaryWrite(self, filename: bytes, operation: bytes,
                           data: c_void_p, nbytes: int) -> int:
        return self.l_binaryWrite(filename, operation, data, nbytes)

    def capi_nbytes_in_file(self, filename: bytes) -> int:
        return self.nbytesInFile(filename)

    def capi_fnbytes_in_file(self, fp: LPFile) -> int:
        return self.fnbytesInFile(fp)

    def capi_l_binaryCopy(self, datas: c_ubyte_p, size: int) -> c_ubyte_p:
        return self.l_binaryCopy(datas, size)

    def capi_l_binaryCompare(self, data1: c_ubyte_p, size1: int,
                             data2: c_ubyte_p, size2: int,
                             psame: c_int_p) -> int:
        return self.l_binaryCompare(data1, size1, data2, size2, psame)

    def capi_file_copy(self, srcfile: bytes, newfile: bytes) -> int:
        return self.fileCopy(srcfile, newfile)

    def capi_file_concatenate(self, srcfile: bytes, destfile: bytes) -> int:
        return self.fileConcatenate(srcfile, destfile)

    def capi_file_append_string(self, filename: bytes, str: bytes) -> int:
        return self.fileAppendString(filename, str)

    def capi_file_split_lines_uniform(self, filename: bytes, n: int,
                                      save_empty: int, rootpath: bytes,
                                      ext: bytes) -> int:
        return self.fileSplitLinesUniform(filename, n, save_empty, rootpath,
                                          ext)

    def capi_fopen_read_stream(self, filename: bytes) -> LPFile:
        return self.fopenReadStream(filename)

    def capi_fopen_write_stream(self, filename: bytes,
                                modestring: bytes) -> LPFile:
        return self.fopenWriteStream(filename, modestring)

    def capi_fopen_read_from_memory(self, data: c_ubyte_p,
                                    size: int) -> LPFile:
        return self.fopenReadFromMemory(data, size)

    def capi_fopen_write_win_tempfile(self) -> LPFile:
        return self.fopenWriteWinTempfile()

    def capi_lept_fopen(self, filename: bytes, mode: bytes) -> LPFile:
        return self.lept_fopen(filename, mode)

    def capi_lept_fclose(self, fp: LPFile) -> int:
        return self.lept_fclose(fp)

    def capi_lept_calloc(self, nmemb: int, size: int) -> c_void_p:
        return self.lept_calloc(nmemb, size)

    def capi_lept_free(self, ptr: c_void_p):
        self.lept_free(ptr)

    def capi_lept_mkdir(self, subdir: bytes) -> int:
        return self.lept_mkdir(subdir)

    def capi_lept_rmdir(self, subdir: bytes) -> int:
        return self.lept_rmdir(subdir)

    def capi_lept_direxists(self, dir: bytes, pexists: c_int_p):
        self.lept_direxists(dir, pexists)

    def capi_lept_rm_match(self, subdir: bytes, substr: bytes) -> int:
        return self.lept_rm_match(subdir, substr)

    def capi_lept_rm(self, subdir: bytes, tail: bytes) -> int:
        return self.lept_rm(subdir, tail)

    def capi_lept_rmfile(self, filepath: bytes) -> int:
        return self.lept_rmfile(filepath)

    def capi_lept_mv(self, srcfile: bytes, newdir: bytes, newtail: bytes,
                     pnewpath: c_char_p_p) -> int:
        return self.lept_mv(srcfile, newdir, newtail, pnewpath)

    def capi_lept_cp(self, srcfile: bytes, newdir: bytes, newtail: bytes,
                     pnewpath: c_char_p_p) -> int:
        return self.lept_cp(srcfile, newdir, newtail, pnewpath)

    def capi_call_system_debug(self, cmd: bytes):
        self.callSystemDebug(cmd)

    def capi_split_path_at_directory(self, pathname: bytes, pdir: c_char_p_p,
                                     ptail: c_char_p_p) -> int:
        return self.splitPathAtDirectory(pathname, pdir, ptail)

    def capi_split_path_at_extension(self, pathname: bytes,
                                     pbasename: c_char_p_p,
                                     pextension: c_char_p_p) -> int:
        return self.splitPathAtExtension(pathname, pbasename, pextension)

    def capi_path_join(self, dir: bytes, fname: bytes) -> LP_c_char:
        return self.pathJoin(dir, fname)

    def capi_append_subdirs(self, basedir: bytes, subdirs: bytes) -> LP_c_char:
        return self.appendSubdirs(basedir, subdirs)

    def capi_convert_sep_chars_in_path(self, path: LP_c_char,
                                       type: int) -> int:
        return self.convertSepCharsInPath(path, type)

    def capi_gen_pathname(self, dir: bytes, fname: bytes) -> LP_c_char:
        return self.genPathname(dir, fname)

    def capi_make_temp_dirname(self, result: LP_c_char, nbytes: int,
                               subdir: bytes) -> int:
        return self.makeTempDirname(result, nbytes, subdir)

    def capi_modify_trailing_slash(self, path: LP_c_char, nbytes: int,
                                   flag: int) -> int:
        return self.modifyTrailingSlash(path, nbytes, flag)

    def capi_l_makeTempFilename(self) -> LP_c_char:
        return self.l_makeTempFilename()

    def capi_extract_number_from_filename(self, fname: bytes, numpre: int,
                                          numpost: int) -> int:
        return self.extractNumberFromFilename(fname, numpre, numpost)

    def capi_pix_simple_captcha(self, pixs: LPPix, border: int, nterms: int,
                                seed: int, color: int,
                                cmapflag: int) -> LPPix:
        return self.pixSimpleCaptcha(pixs, border, nterms, seed, color,
                                     cmapflag)

    def capi_pix_random_harmonic_warp(self, pixs: LPPix, xmag: float,
                                      ymag: float, xfreq: float, yfreq: float,
                                      nx: int, ny: int, seed: int,
                                      grayval: int) -> LPPix:
        return self.pixRandomHarmonicWarp(pixs, xmag, ymag, xfreq, yfreq, nx,
                                          ny, seed, grayval)

    def capi_pix_warp_stereoscopic(self, pixs: LPPix, zbend: int, zshiftt: int,
                                   zshiftb: int, ybendt: int, ybendb: int,
                                   redleft: int) -> LPPix:
        return self.pixWarpStereoscopic(pixs, zbend, zshiftt, zshiftb, ybendt,
                                        ybendb, redleft)

    def capi_pix_stretch_horizontal(self, pixs: LPPix, dir: int, type: int,
                                    hmax: int, operation: int,
                                    incolor: int) -> LPPix:
        return self.pixStretchHorizontal(pixs, dir, type, hmax, operation,
                                         incolor)

    def capi_pix_stretch_horizontal_sampled(self, pixs: LPPix, dir: int,
                                            type: int, hmax: int,
                                            incolor: int) -> LPPix:
        return self.pixStretchHorizontalSampled(pixs, dir, type, hmax, incolor)

    def capi_pix_stretch_horizontal_li(self, pixs: LPPix, dir: int, type: int,
                                       hmax: int, incolor: int) -> LPPix:
        return self.pixStretchHorizontalLI(pixs, dir, type, hmax, incolor)

    def capi_pix_quadratic_vshear(self, pixs: LPPix, dir: int, vmaxt: int,
                                  vmaxb: int, operation: int,
                                  incolor: int) -> LPPix:
        return self.pixQuadraticVShear(pixs, dir, vmaxt, vmaxb, operation,
                                       incolor)

    def capi_pix_quadratic_vshear_sampled(self, pixs: LPPix, dir: int,
                                          vmaxt: int, vmaxb: int,
                                          incolor: int) -> LPPix:
        return self.pixQuadraticVShearSampled(pixs, dir, vmaxt, vmaxb, incolor)

    def capi_pix_quadratic_vshear_li(self, pixs: LPPix, dir: int, vmaxt: int,
                                     vmaxb: int, incolor: int) -> LPPix:
        return self.pixQuadraticVShearLI(pixs, dir, vmaxt, vmaxb, incolor)

    def capi_pix_stereo_from_pair(self, pix1: LPPix, pix2: LPPix, rwt: float,
                                  gwt: float, bwt: float) -> LPPix:
        return self.pixStereoFromPair(pix1, pix2, rwt, gwt, bwt)

    def capi_wshed_create(self, pixs: LPPix, pixm: LPPix, mindepth: int,
                          debugflag: int) -> LPL_WShed:
        return self.wshedCreate(pixs, pixm, mindepth, debugflag)

    def capi_wshed_destroy(self, pwshed: LPLPL_WShed):
        self.wshedDestroy(pwshed)

    def capi_wshed_apply(self, wshed: LPL_WShed) -> int:
        return self.wshedApply(wshed)

    def capi_wshed_basins(self, wshed: LPL_WShed, ppixa: LPLPPixa,
                          pnalevels: LPLPNuma) -> int:
        return self.wshedBasins(wshed, ppixa, pnalevels)

    def capi_wshed_render_fill(self, wshed: LPL_WShed) -> LPPix:
        return self.wshedRenderFill(wshed)

    def capi_wshed_render_colors(self, wshed: LPL_WShed) -> LPPix:
        return self.wshedRenderColors(wshed)

    def capi_pixa_write_web_panim(self, filename: bytes, pixa: LPPixa,
                                  loopcount: int, duration: int, quality: int,
                                  lossless: int) -> int:
        return self.pixaWriteWebPAnim(filename, pixa, loopcount, duration,
                                      quality, lossless)

    def capi_pixa_write_stream_web_panim(self, fp: LPFile, pixa: LPPixa,
                                         loopcount: int, duration: int,
                                         quality: int, lossless: int) -> int:
        return self.pixaWriteStreamWebPAnim(fp, pixa, loopcount, duration,
                                            quality, lossless)

    def capi_pixa_write_mem_web_panim(self, pencdata: POINTER(c_ubyte_p),
                                      pencsize: c_size_t_p, pixa: LPPixa,
                                      loopcount: int, duration: int,
                                      quality: int, lossless: int) -> int:
        return self.pixaWriteMemWebPAnim(pencdata, pencsize, pixa, loopcount,
                                         duration, quality, lossless)

    def capi_pix_read_stream_webp(self, fp: LPFile) -> LPPix:
        return self.pixReadStreamWebP(fp)

    def capi_pix_read_mem_webp(self, filedata: c_ubyte_p,
                               filesize: int) -> LPPix:
        return self.pixReadMemWebP(filedata, filesize)

    def capi_read_header_webp(self, filename: bytes, pw: c_int_p, ph: c_int_p,
                              pspp: c_int_p) -> int:
        return self.readHeaderWebP(filename, pw, ph, pspp)

    def capi_read_header_mem_webp(self, data: c_ubyte_p, size: int,
                                  pw: c_int_p, ph: c_int_p,
                                  pspp: c_int_p) -> int:
        return self.readHeaderMemWebP(data, size, pw, ph, pspp)

    def capi_pix_write_webp(self, filename: bytes, pixs: LPPix, quality: int,
                            lossless: int) -> int:
        return self.pixWriteWebP(filename, pixs, quality, lossless)

    def capi_pix_write_stream_webp(self, fp: LPFile, pixs: LPPix, quality: int,
                                   lossless: int) -> int:
        return self.pixWriteStreamWebP(fp, pixs, quality, lossless)

    def capi_pix_write_mem_webp(self, pencdata: POINTER(c_ubyte_p),
                                pencsize: c_size_t_p, pixs: LPPix,
                                quality: int, lossless: int) -> int:
        return self.pixWriteMemWebP(pencdata, pencsize, pixs, quality,
                                    lossless)

    def capi_l_jpegSetQuality(self, new_quality: int) -> int:
        return self.l_jpegSetQuality(new_quality)

    def capi_set_lept_debug_ok(self, allow: int):
        self.setLeptDebugOK(allow)

    def capi_pixa_write_files(self, rootname: bytes, pixa: LPPixa,
                              format: int) -> int:
        return self.pixaWriteFiles(rootname, pixa, format)

    def capi_pix_write_debug(self, fname: bytes, pix: LPPix,
                             format: int) -> int:
        return self.pixWriteDebug(fname, pix, format)

    def capi_pix_write(self, fname: bytes, pix: LPPix, format: int) -> int:
        return self.pixWrite(fname, pix, format)

    def capi_pix_write_auto_format(self, filename: bytes, pix: LPPix) -> int:
        return self.pixWriteAutoFormat(filename, pix)

    def capi_pix_write_stream(self, fp: LPFile, pix: LPPix,
                              format: int) -> int:
        return self.pixWriteStream(fp, pix, format)

    def capi_pix_write_implied_format(self, filename: bytes, pix: LPPix,
                                      quality: int, progressive: int) -> int:
        return self.pixWriteImpliedFormat(filename, pix, quality, progressive)

    def capi_pix_choose_output_format(self, pix: LPPix) -> int:
        return self.pixChooseOutputFormat(pix)

    def capi_get_implied_file_format(self, filename: bytes) -> int:
        return self.getImpliedFileFormat(filename)

    def capi_pix_get_auto_format(self, pix: LPPix, pformat: c_int_p) -> int:
        return self.pixGetAutoFormat(pix, pformat)

    def capi_get_format_extension(self, format: int) -> bytes:
        return self.getFormatExtension(format)

    def capi_pix_write_mem(self, pdata: POINTER(c_ubyte_p), psize: c_size_t_p,
                           pix: LPPix, format: int) -> int:
        return self.pixWriteMem(pdata, psize, pix, format)

    def capi_l_fileDisplay(self, fname: bytes, x: int, y: int,
                           scale: float) -> int:
        return self.l_fileDisplay(fname, x, y, scale)

    def capi_pix_display(self, pixs: LPPix, x: int, y: int) -> int:
        return self.pixDisplay(pixs, x, y)

    def capi_pix_display_with_title(self, pixs: LPPix, x: int, y: int,
                                    title: bytes, dispflag: int) -> int:
        return self.pixDisplayWithTitle(pixs, x, y, title, dispflag)

    def capi_pix_make_color_square(self, color: int, size: int, addlabel: int,
                                   location: int, textcolor: int) -> LPPix:
        return self.pixMakeColorSquare(color, size, addlabel, location,
                                       textcolor)

    def capi_l_chooseDisplayProg(self, selection: int):
        self.l_chooseDisplayProg(selection)

    def capi_change_format_for_missing_lib(self, pformat: c_int_p):
        self.changeFormatForMissingLib(pformat)

    def capi_pix_display_write(self, pixs: LPPix, reduction: int) -> int:
        return self.pixDisplayWrite(pixs, reduction)

    def capi_zlib_compress(self, datain: c_ubyte_p, nin: int,
                           pnout: c_size_t_p) -> c_ubyte_p:
        return self.zlibCompress(datain, nin, pnout)

    def capi_zlib_uncompress(self, datain: c_ubyte_p, nin: int,
                             pnout: c_size_t_p) -> c_ubyte_p:
        return self.zlibUncompress(datain, nin, pnout)


LEPTONICA_API = LeptCAPI(LEPT_DLL)
