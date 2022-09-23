# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 00:14:21 2022

@author: 皓
"""
# import os
# import os.path as osp
# import re
from generate_code import PyCodeGenerator, XMLGenerator
from generate_code.utils import name_convert_to_snake


CUSTOM_MAP = {
    'ctypes': {
        'TessPageSegMode': ('c_int', 'int'),
        'TessOcrEngineMode': ('c_int', 'int'),
        'TessPolyBlockType': ('c_int', 'int'),
        'TessPageIteratorLevel': ('c_int', 'int'),
    },
    '.datatype': {
        'int *': ('c_int_p', 'c_int_p'),
        'bool *': ('c_bool_p', 'c_bool_p'),
        'BOOL *': ('c_bool_p', 'c_bool_p'),
        'unsigned char *': ('c_ubyte_p', 'c_ubyte_p'),
        'unsigned int *': ('c_uint_p', 'c_uint_p'),
        'float *': ('c_float_p', 'c_float_p'),
        'double *': ('c_double_p', 'c_double_p'),
        'size_t *': ('c_size_t_p', 'c_size_t_p'),
        'char *': ('LP_c_char', 'LP_c_char'),
        'signed char *': ('LP_c_char', 'LP_c_char'),
        'char * *': ('c_char_p_p', 'c_char_p_p'),
        'signed char * *': ('c_char_p_p', 'c_char_p_p'),
        'unsigned __int64 *': ('c_ulonglong_p', 'c_ulonglong_p'),
        'unsigned long long *': ('c_ulonglong_p', 'c_ulonglong_p'),
        'TessOrientation *': ('c_int_p', 'c_int_p'),
        'TessWritingDirection *': ('c_int_p', 'c_int_p'),
        'TessTextlineOrder *': ('c_int_p', 'c_int_p'),
        'TessParagraphJustification *': ('c_int_p', 'c_int_p'),
    },
    '.pytype.pix': {
        'Pix': ('Pix', 'Pix'),
        'Pix *': ('LPPix', 'LPPix'),
        'Boxa *': ('LPBoxa', 'LPBoxa'),
        'Pixa *': ('LPPixa', 'LPPixa'),
    },

    None: {
        'TessResultRenderer *': ('LPTessResultRenderer',
                                 'LPTessResultRenderer'),
        'TessBaseAPI *': ('LPTessBaseAPI', 'LPTessBaseAPI'),
        'TessPageIterator *': ('LPTessPageIterator', 'LPTessPageIterator'),
        'TessResultIterator *': ('LPTessResultIterator',
                                 'LPTessResultIterator'),
        'TessMutableIterator *': ('LPTessMutableIterator',
                                  'LPTessMutableIterator'),
        'TessChoiceIterator *': ('LPTessChoiceIterator',
                                 'LPTessChoiceIterator'),
        'ETEXT_DESC *': ('LPETEXT_DESC',
                         'LPETEXT_DESC'),
        'FILE *': ('LPFILE', 'LPFILE'),
        'TessCancelFunc': ('TessCancelFunc', 'TessCancelFunc'),
        'TessProgressFunc': ('TessProgressFunc', 'TessProgressFunc')}
}


def parse_functions(function, generater: PyCodeGenerator):
    function_info = {}
    function_name = function.get('name')
    try:
        new_function_name = name_convert_to_snake(function_name)
    except Exception:
        new_function_name = function_name
    function_info['name'] = f'capi_{new_function_name[5:]}'
    rtnType = function.get('rtnType')
    return_type = rtnType.replace('TESS_API ', '')
    ctype, ptype, pp = generater.parse_type(return_type)
    rtntype_annotation = (not ptype == 'None')
    if rtntype_annotation:
        function_info['rtntype'] = ptype
    arguments = {'self': None}
    params = []
    for parameter in function['parameters']:
        name = parameter.get('name')
        type_ = parameter.get('type')
        ctype, ptype, pp = generater.parse_type(type_)
        arguments[name] = ptype
        params.append(name)
    function_info['arguments'] = arguments
    function_info['return'] = rtntype_annotation
    param_text = ', '.join(params)
    function_info['return_content'] = f'self.{function_name}({param_text})'
    return function_info


def generate_py():
    generater = PyCodeGenerator(r'libtesseract\include\tesseract\capi.h')
    generater.function_callback = parse_functions
    generater.add_custom_type(CUSTOM_MAP)
    generater.parse()
    generater['class_name'] = "TessCAPI"
    generater['parent_classes'] = ["CAPI"]
    generater.import_object('.datatype', 'CAPI')
    generater['class_vars'] = ["NAME = 'Tesseract'"]
    # generater.dump('result.py', pep8=True, options={'aggressive': 2})
    generater.dump('capi.py', pep8=True)


def generate_xml():
    generater = XMLGenerator(r'libtesseract\include\tesseract\capi.h')
    generater.add_custom_type(CUSTOM_MAP)
    generater.rtn_type_callback = lambda x: x.replace('TESS_API ', '')
    generater.parse()
    print(generater.get_unknown_type())
    generater.dump('tesseract52.xml', pretty_print=True)


def main():
    # generate_py()
    generate_xml()


if __name__ == '__main__':
    main()
