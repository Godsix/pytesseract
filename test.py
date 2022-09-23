# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:13:16 2022

@author: 皓
"""
import sys
from libtesseract import (Tesseract, TextBuilder, PageSegMode, Leptonica,
                          ResultRenderer)
from libtesseract.utils import print_run_time


def progress_func(this, left: int, right: int,
                  top: int, bottom: int) -> bool:
    print(this.progress, left, right, top, bottom)
    return True


def test_version():
    tesseract = Tesseract(language='chi_sim')
    print(tesseract.get_version())
    print(tesseract.init_languages)
    # res = tesseract.available_languages
    # print(res)
    # tesseract.set_variable('tessedit_create_boxfile', '1')
    # pix = Leptonica.pix_read(r'C:/Users/皓/source/repos/pytesseract/1.jpg')
    # render = tesseract.rendererapi.box_text_renderer_create(r'C:/Users/皓/source/repos/pytesseract/1111')
    # print(render.image_num())
    # print(tesseract.process_page(pix, 1, None, None, 0, render))


def test_ocr():
    # instance = Tesseract()
    # print(instance.get_version())
    # instance.get_baseapi(language='chi_sim')
    # print(instance.get_init_languages())
    # res = instance.get_available_languages()
    # print(res)
    filename = '1.jpg'
    # filename = '1.png'

    # 不设置成单行模式,没有输出
    builder = TextBuilder(tesseract_layout=3)
    # lang为语言,默认使用eng
    ret = Tesseract.detect_orientation(filename)
    print(ret)
    ret = Tesseract.image_to_string(filename, lang='chi_sim', builder=builder,
                                    progress_func=progress_func)
    print(ret)
    # print(instance.detect_orientation(img, lang='chi_sim'))


@print_run_time
def test_command():
    import subprocess
    subprocess.call(
        args=r'libtesseract\x64\tesseract.exe 1.jpg  1  -l chi_sim --psm 3 --tessdata-dir .\libtesseract\tessdata', shell=True)


def fix_page_seg_mode(api, pagesegmode: PageSegMode):
    if api.get_page_seg_mode() == PageSegMode.SINGLE_BLOCK:
        api.set_page_seg_mode(pagesegmode)


def preload_renderers(api, pagesegmode, outputbase):
    renderers = []
    for item in ('alto', 'tsv', 'lstmbox', 'boxfile', 'wordstrbox', 'txt'):
        renderer_type = api.get_bool_variable(f'tessedit_create_{item}')
        if renderer_type:
            renderer = ResultRenderer.create(outputbase, item)
            renderers.append(renderer)
    renderer_type = api.get_bool_variable('tessedit_create_hocr')
    if renderer_type:
        font_info = api.get_bool_variable('hocr_font_info')
        renderer = ResultRenderer.create(outputbase, 'hocr', font_info)
        renderers.append(renderer)

    renderer_type = api.get_bool_variable('tessedit_create_pdf')
    if renderer_type:
        textonly = api.get_bool_variable('textonly_pdf')
        renderer = ResultRenderer.create(outputbase, 'pdf',
                                         api.get_datapath(), textonly)
        renderers.append(renderer)
    renderer_type = api.get_bool_variable('tessedit_write_unlv')
    if renderer_type:
        api.set_variable("unlv_tilde_crunching", "true")
        renderer = ResultRenderer.create(outputbase, 'unlv')
        renderers.append(renderer)
    return renderers


def test():
    image = r'F:/Project/OCR/pytesseract/libtesseract/1.jpg'
    outputbase = r'F:/Project/OCR/pytesseract/libtesseract/result'
    instance = Tesseract()
    # print(dir(instance))
    instance.get_baseapi(language='chi_sim')
    print(instance.get_init_languages())
    print(instance.get_version())
    print(instance.get_bool_variable('hocr_font_info'))
    instance.set_output_name(outputbase)
    fix_page_seg_mode(instance, PageSegMode.AUTO)
    renderers = preload_renderers(instance, PageSegMode.AUTO, outputbase)
    print(renderers)
    succeed = instance.process_pages(image, None, 0, renderers[0])
    if not succeed:
        print("Error during processing.", file=sys.stderr)
    for item in renderers:
        instance.delete_result_renderer(item)


def test_renderer():
    image = r'F:/Project/OCR/pytesseract/libtesseract/1.jpg'
    outputbase = r'F:/Project/OCR/pytesseract/libtesseract/result'
    instance = Tesseract()
    # instance.get_baseapi(language='chi_sim')
    print(instance.get_init_languages())
    print(instance.get_version())
    print(instance.get_bool_variable('hocr_font_info'))
    # instance.set_output_name(outputbase)
    instance.set_variable('tessedit_create_hocr', '1')
    fix_page_seg_mode(instance, PageSegMode.AUTO)
    renderers = preload_renderers(instance, PageSegMode.AUTO, outputbase)
    print(renderers)
    # succeed = instance.process_pages(image, None, 0, renderers[0])
    # if not succeed:
    #     print("Error during processing.", file=sys.stderr)
    # for item in renderers:
    #     instance.delete_result_renderer(item)


def make_boxs(path, page):
    tesseract = Tesseract(language='chi_sim')
    tesseract.set_image_data(path)
    tesseract.recognize()
    result = tesseract.get_box_text(page)
    tesseract.end()
    return result


def test11():
    tesseract = Tesseract(language='chi_sim')
    filename = '1.jpg'
    tesseract.set_image_data(filename)
    # tesseract.set_rectangle(38, 8, 100, 100)
    # ret = tesseract.get_utf8_text()
    # print('ret1', ret)
    ret = tesseract.get_textlines()
    print(ret)
    # ret = tesseract.get_rect(filename, 38, 8, 100, 100)
    # print('ret', ret)


@print_run_time
def test_leptonica():
    leptonica = Leptonica()
    print(leptonica.get_version())
    pix = leptonica.pix_read(r'C:/Users/皓/source/repos/pytesseract/1.tif')
    print(pix)
    print(pix.get_dimensions())
    # from libtesseract.leptonica_capi import LEPTONICA_API
    # print(len(LEPTONICA_API.API))
    # print(isinstance(pix, LPPix))


def main():
    test_version()
    test_leptonica()
    # test_ocr()
    # test_renderer()
    # test11()
    # print(make_boxs('1.jpg', 0))


if __name__ == "__main__":
    main()
