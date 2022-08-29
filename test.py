# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:13:16 2022

@author: 皓
"""
import sys
from ctypes import POINTER
from libtesseract import Tesseract, TextBuilder, PageSegMode, Leptonica
from libtesseract.leptonica_capi import Pix
from libtesseract.utils import print_run_time


def test_version():
    tesseract = Tesseract()
    # language='chi_sim'
    print(tesseract.get_version())
    print(tesseract.get_init_languages())
    res = tesseract.get_available_languages()
    print(res)
    tesseract.set_variable('tessedit_create_boxfile', '1')
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
    # filename = '1.jpg'
    filename = '1.jpg'

    # 不设置成单行模式,没有输出
    builder = TextBuilder(tesseract_layout=3)
    # lang为语言,默认使用eng
    ret = Tesseract.detect_orientation(filename)
    ret = Tesseract.image_to_string(filename, lang='chi_sim', builder=builder)
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
    renderer_type = api.get_bool_variable('tessedit_create_hocr')
    if renderer_type:
        font_info = api.get_bool_variable('hocr_font_info')
        renderer = api.hocr_renderer_create(outputbase, font_info)
        renderers.append(renderer)
    renderer_type = api.get_bool_variable('tessedit_create_alto')
    if renderer_type:
        renderer = api.alto_renderer_create(outputbase)
        renderers.append(renderer)
    renderer_type = api.tsv_renderer_create('tessedit_create_tsv')
    if renderer_type:
        font_info = api.get_bool_variable('hocr_font_info')
        renderer = api.hocr_renderer_create(outputbase, font_info)
        renderers.append(renderer)
    renderer_type = api.get_bool_variable('tessedit_create_pdf')
    if renderer_type:
        textonly = api.get_bool_variable('textonly_pdf')
        renderer = api.pdf_renderer_create(outputbase, api.get_datapath(),
                                           textonly)
        renderers.append(renderer)
    renderer_type = api.get_bool_variable('tessedit_write_unlv')
    if renderer_type:
        api.set_variable("unlv_tilde_crunching", "true")
        renderer = api.unlv_renderer_create(outputbase)
        renderers.append(renderer)
    renderer_type = api.tsv_renderer_create('tessedit_create_lstmbox')
    if renderer_type:
        renderer = api.lstm_box_renderer_create(outputbase)
        renderers.append(renderer)
    renderer_type = api.get_bool_variable('tessedit_create_boxfile')
    if renderer_type:
        renderer = api.box_text_renderer_create(outputbase)
        renderers.append(renderer)
    renderer_type = api.get_bool_variable('tessedit_create_wordstrbox')
    if renderer_type:
        renderer = api.word_str_box_renderer_create(outputbase)
        renderers.append(renderer)
    renderer_type = api.tsv_renderer_create('tessedit_create_txt')
    if renderer_type:
        renderer = api.text_renderer_create(outputbase)
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


def test_leptonica():
    leptonica = Leptonica()
    print(leptonica.get_version())
    pix = leptonica.pix_read(r'C:/Users/皓/source/repos/pytesseract/1.tif')
    print(pix)
    print(isinstance(pix, POINTER(Pix)))

def main():
    test_version()
    # test_leptonica()
    test_ocr()


if __name__ == "__main__":
    main()
