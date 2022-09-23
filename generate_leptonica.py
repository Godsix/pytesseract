# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 00:14:21 2022

@author: 皓
"""
import os
import os.path as osp
import re
import json
import shutil
import lxml.etree as ET
from glob import iglob
import libtesseract.leptonica_capi
# import libtesseract.pytype
from generate_code import PyCodeGenerator, XMLGenerator, parse_all_header
from generate_code.utils import regexp_findall, name_convert_to_snake


CUSTOM_MAP = {
    'ctypes': {
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
        'FILE *': ('LPFile', 'LPFile'),
    },
    '.pytype.array_h': {
        'Numa *': ('LPNuma', 'LPNuma'),
        'Numa * *': ('LPLPNuma', 'LPLPNuma'),
        'Numaa *': ('LPNumaa', 'LPNumaa'),
        'Numaa * *': ('LPLPNumaa', 'LPLPNumaa'),
        'L_Dna *': ('LPL_Dna', 'LPL_Dna'),
        'L_Dna * *': ('LPLPL_Dna', 'LPLPL_Dna'),
        'L_Dnaa *': ('LPL_Dnaa', 'LPL_Dnaa'),
        'L_Dnaa * *': ('LPLPL_Dnaa', 'LPLPL_Dnaa'),
        'L_DnaHash *': ('LPL_DnaHash', 'LPL_DnaHash'),
        'L_DnaHash * *': ('LPLPL_DnaHash', 'LPLPL_DnaHash'),
        'Sarray *': ('LPSarray', 'LPSarray'),
        'Sarray * *': ('LPLPSarray', 'LPLPSarray'),
        'L_Bytea *': ('LPL_Bytea', 'LPL_Bytea'),
        'L_Bytea * *': ('LPLPL_Bytea', 'LPLPL_Bytea')
    },
    '.pytype.bbuffer': {
        'L_ByteBuffer *': ('LPL_ByteBuffer', 'LPL_ByteBuffer'),
        'L_ByteBuffer * *': ('LPLPL_ByteBuffer', 'LPLPL_ByteBuffer')
    },
    '.pytype.bmf': {
        'L_Bmf *': ('LPL_Bmf', 'LPL_Bmf'),
        'L_Bmf * *': ('LPLPL_Bmf', 'LPLPL_Bmf')
    },
    '.pytype.ccbord': {
        'CCBord *': ('LPCCBord', 'LPCCBord'),
        'CCBord * *': ('LPLPCCBord', 'LPLPCCBord'),
        'CCBorda *': ('LPCCBorda', 'LPCCBorda'),
        'CCBorda * *': ('LPLPCCBorda', 'LPLPCCBorda')
    },
    '.pytype.colorfill': {
        'L_Colorfill *': ('LPL_Colorfill', 'LPL_Colorfill'),
        'L_Colorfill * *': ('LPLPL_Colorfill', 'LPLPL_Colorfill')
    },
    '.pytype.dewarp': {
        'L_Dewarp *': ('LPL_Dewarp', 'LPL_Dewarp'),
        'L_Dewarp * *': ('LPLPL_Dewarp', 'LPLPL_Dewarp'),
        'L_Dewarpa *': ('LPL_Dewarpa', 'LPL_Dewarpa'),
        'L_Dewarpa * *': ('LPLPL_Dewarpa', 'LPLPL_Dewarpa')
    },
    '.pytype.environ': {
        'L_WallTimer *': ('LPL_WallTimer', 'LPL_WallTimer'),
        'L_WallTimer * *': ('LPLPL_WallTimer', 'LPLPL_WallTimer')
    },
    '.pytype.gplot': {
        'GPlot *': ('LPGPlot', 'LPGPlot'),
        'GPlot * *': ('LPLPGPlot', 'LPLPGPlot')
    },
    '.pytype.hashmap': {
        'L_Hashitem *': ('LPL_Hashitem', 'LPL_Hashitem'),
        'L_Hashmap *': ('LPL_Hashmap', 'LPL_Hashmap'),
        'L_Hashmap * *': ('LPLPL_Hashmap', 'LPLPL_Hashmap')
    },
    '.pytype.heap': {
        'L_Heap *': ('LPL_Heap', 'LPL_Heap'),
        'L_Heap * *': ('LPLPL_Heap', 'LPLPL_Heap')
    },
    '.pytype.imageio': {
        'L_Compressed_Data *': ('LPL_Compressed_Data', 'LPL_Compressed_Data'),
        'L_Compressed_Data * *': ('LPLPL_Compressed_Data',
                                  'LPLPL_Compressed_Data'),
        'L_Pdf_Data * *': ('LPLPL_Pdf_Data', 'LPLPL_Pdf_Data')
    },
    '.pytype.jbclass': {
        'JbClasser *': ('LPJbClasser', 'LPJbClasser'),
        'JbClasser * *': ('LPLPJbClasser', 'LPLPJbClasser'),
        'JbData *': ('LPJbData', 'LPJbData'),
        'JbData * *': ('LPLPJbData', 'LPLPJbData')
    },
    '.pytype.list_h': {
        'DoubleLinkedList *': ('LPDoubleLinkedList', 'LPDoubleLinkedList'),
        'DoubleLinkedList * *': ('LPLPDoubleLinkedList',
                                 'LPLPDoubleLinkedList')
    },
    '.pytype.morph': {
        'Sel *': ('LPSel', 'LPSel'),
        'Sel * *': ('LPLPSel', 'LPLPSel'),
        'Sela *': ('LPSela', 'LPSela'),
        'Sela * *': ('LPLPSela', 'LPLPSela'),
        'L_Kernel *': ('LPL_Kernel', 'LPL_Kernel'),
        'L_Kernel * *': ('LPLPL_Kernel', 'LPLPL_Kernel')
    },
    '.pytype.pix': {
        'PixColormap *': ('LPPixColormap', 'LPPixColormap'),
        'PixColormap * *': ('LPLPPixColormap', 'LPLPPixColormap'),
        'Pix *': ('LPPix', 'LPPix'),
        'Pix * *': ('LPLPPix', 'LPLPPix'),
        'Box *': ('LPBox', 'LPBox'),
        'Box * *': ('LPLPBox', 'LPLPBox'),
        'Boxa *': ('LPBoxa', 'LPBoxa'),
        'Boxa * *': ('LPLPBoxa', 'LPLPBoxa'),
        'Boxaa *': ('LPBoxaa', 'LPBoxaa'),
        'Boxaa * *': ('LPLPBoxaa', 'LPLPBoxaa'),
        'Pixa *': ('LPPixa', 'LPPixa'),
        'Pixa * *': ('LPLPPixa', 'LPLPPixa'),
        'Pixaa *': ('LPPixaa', 'LPPixaa'),
        'Pixaa * *': ('LPLPPixaa', 'LPLPPixaa'),
        'Pta *': ('LPPta', 'LPPta'),
        'Pta * *': ('LPLPPta', 'LPLPPta'),
        'Ptaa *': ('LPPtaa', 'LPPtaa'),
        'Ptaa * *': ('LPLPPtaa', 'LPLPPtaa'),
        'Pixacc *': ('LPPixacc', 'LPPixacc'),
        'Pixacc * *': ('LPLPPixacc', 'LPLPPixacc'),
        'PixTiling *': ('LPPixTiling', 'LPPixTiling'),
        'PixTiling * *': ('LPLPPixTiling', 'LPLPPixTiling'),
        'FPix *': ('LPFPix', 'LPFPix'),
        'FPix * *': ('LPLPFPix', 'LPLPFPix'),
        'FPixa *': ('LPFPixa', 'LPFPixa'),
        'FPixa * *': ('LPLPFPixa', 'LPLPFPixa'),
        'DPix *': ('LPDPix', 'LPDPix'),
        'DPix * *': ('LPLPDPix', 'LPLPDPix'),
        'PixComp *': ('LPPixComp', 'LPPixComp'),
        'PixComp * *': ('LPLPPixComp', 'LPLPPixComp'),
        'PixaComp *': ('LPPixaComp', 'LPPixaComp'),
        'PixaComp * *': ('LPLPPixaComp', 'LPLPPixaComp'),
        'alloc_fn': ('alloc_fn', 'alloc_fn'),
        'dealloc_fn': ('alloc_fn', 'alloc_fn'),
    },
    '.pytype.ptra': {
        'L_Ptra *': ('LPL_Ptra', 'LPL_Ptra'),
        'L_Ptra * *': ('LPLPL_Ptra', 'LPLPL_Ptra'),
        'L_Ptraa *': ('LPL_Ptraa', 'LPL_Ptraa'),
        'L_Ptraa * *': ('LPLPL_Ptraa', 'LPLPL_Ptraa')
    },
    '.pytype.queue': {
        'L_Queue *': ('LPL_Queue', 'LPL_Queue'),
        'L_Queue * *': ('LPLPL_Queue', 'LPLPL_Queue')
    },
    '.pytype.rbtree': {
        'Rb_Type': ('Rb_Type', 'Rb_Type'),
        'Rb_Type *': ('LPRb_Type', 'LPRb_Type'),
        'L_Rbtree_Node *': ('LPL_Rbtree_Node', 'LPL_Rbtree_Node'),
        'L_Rbtree *': ('LPL_Rbtree', 'LPL_Rbtree'),
        'L_Rbtree * *': ('LPLPL_Rbtree', 'LPLPL_Rbtree')
    },
    '.pytype.recog': {
        'L_Rch *': ('LPL_Rch', 'LPL_Rch'),
        'L_Rch * *': ('LPLPL_Rch', 'LPLPL_Rch'),
        'L_Rcha *': ('LPL_Rcha', 'LPL_Rcha'),
        'L_Rcha * *': ('LPLPL_Rcha', 'LPLPL_Rcha'),
        'L_Rdid *': ('LPL_Rdid', 'LPL_Rdid'),
        'L_Recog *': ('LPL_Recog', 'LPL_Recog'),
        'L_Recog * *': ('LPLPL_Recog', 'LPLPL_Recog')
    },
    '.pytype.regutils': {
        'L_RegParams *': ('LPL_RegParams', 'LPL_RegParams'),
        'L_RegParams * *': ('LPLPL_RegParams', 'LPLPL_RegParams')
    },
    '.pytype.stack': {
        'L_Stack *': ('LPL_Stack', 'LPL_Stack'),
        'L_Stack * *': ('LPLPL_Stack', 'LPLPL_Stack')
    },
    '.pytype.stringcode': {
        'L_StrCode *': ('LPL_StrCode', 'LPL_StrCode'),
        'L_StrCode * *': ('LPLPL_StrCode', 'LPLPL_StrCode')
    },
    '.pytype.sudoku': {
        'L_Sudoku *': ('LPL_Sudoku', 'LPL_Sudoku'),
        'L_Sudoku * *': ('LPLPL_Sudoku', 'LPLPL_Sudoku')
    },
    '.pytype.watershed': {
        'L_WShed *': ('LPL_WShed', 'LPL_WShed'),
        'L_WShed * *': ('LPLPL_WShed', 'LPLPL_WShed')},
    None: {
        'void ( * ) ( const char * )': ('handler_fn', 'handler_fn'),
    }
}


def parse_functions(function, generater: PyCodeGenerator):
    function_info = {}
    function_name = function.get('name')
    try:
        new_function_name = name_convert_to_snake(function_name)
    except Exception:
        new_function_name = function_name
    function_info['name'] = f'capi_{new_function_name}'
    rtnType = function.get('rtnType')
    return_type = rtnType.replace('LEPT_DLL extern ', '')
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


def generate_pys():
    gen = PyCodeGenerator(r'libtesseract\include\leptonica\allheaders.h')
    for item in os.listdir(r'libtesseract\include\leptonica'):
        if item in ('allheaders.h', ):
            continue
        item_path = osp.join(r'libtesseract\include\leptonica', item)
        generater = PyCodeGenerator(item_path)
        generater.function_callback = parse_functions
        generater.add_custom_type(CUSTOM_MAP)
        generater.add_type_defs(gen.get_type_defs())
        generater.parse()
        generater['class_name'] = "TessCAPI"
        item_name = osp.splitext(item)[0]
        out_file = osp.join('output', f'{item_name}.py')
        generater.dump(out_file, pep8=False, options={'aggressive': 1})
    return


def generate_py():
    all_gen = PyCodeGenerator(r'libtesseract\include\leptonica\allheaders.h')
    generater = all_gen
    generater.function_callback = parse_functions
    generater.add_custom_type(CUSTOM_MAP)
    # print(generater.get_type_defs())
    generater.add_type_defs(all_gen.get_type_defs())
    generater.parse()
    # print(generater.get_unknown_type())
    generater['class_name'] = "LeptCAPI"
    generater['parent_classes'] = ["CAPI"]
    generater.import_object('.datatype', 'CAPI')
    generater['class_vars'] = ["NAME = 'Leptonica'"]
    generater['global_exps'] = ["# void  ( *handler ) ( const char * )",
                                "handler_fn = CFUNCTYPE(None, c_char_p)"]
    generater.import_object('ctypes', 'CFUNCTYPE', 'c_char_p')
    # generater.dump('allheaders.py', pep8=True, options={'aggressive': 2})
    generater.dump('allheaders.py', pep8=True)


def generate_xml():
    generater = XMLGenerator(r'libtesseract\include\leptonica\allheaders.h')
    generater.add_custom_type(CUSTOM_MAP)
    generater.rtn_type_callback = lambda x: x.replace('LEPT_DLL extern ', '')
    generater.parse()
    print(generater.get_unknown_type())
    generater.dump('leptonica-1.82.0.xml', pretty_print=True)


def check_xml_data():
    lept = libtesseract.leptonica_capi.LEPTONICA_API
    xml_info = lept.get_xml_info()
    # print(xml_info)
    lept2 = libtesseract.leptonica_capi_.LEPTONICA_API
    # print(lept2.API)
    # for k, v in xml_info.items():
    #     if k in lept2.API:
    #         if not v == lept2.API[k]:
    #             print(k, v, lept2.API[k])

    for k, v in lept2.API.items():
        if k not in xml_info:
            print(k)


def load_json(path):
    with open(path, encoding='utf-8') as fp:
        return json.load(fp)


DOXYGEN_PREFIX = re.compile(r'^( *\* *)[^$]', re.M)
DOXYGEN_REPLACE = re.compile(r'^( *\* *)[^$]', re.M)


def process_doxygen(c_in):
    ret = DOXYGEN_PREFIX.findall(c_in)
    if not ret:
        # print(c_in.encode())
        return c_in
    min_len = min(len(x) for x in ret)
    ll = len(ret[0]) - len(ret[0].lstrip())
    rl = min_len - ll - 1
    pattern = re.compile(fr'^{" " * ll}\*{" " * rl}', re.M)
    return re.sub(pattern, '', c_in).strip(' \r\n')


def process_comment(c_in):
    c_in = c_in.strip()
    if c_in.startswith('/*'):
        c_in = c_in[2:]
    if c_in.endswith('*/'):
        c_in = c_in[:-2]
    c_c_in = process_doxygen(c_in)
    cl = [x.strip('\r\n ') for x in c_c_in.split('\n')]
    result = ' '.join(x for x in cl if x)
    if not result:
        return None
    return result


def process_attrib(c_in):
    if isinstance(c_in, bool):
        return 'true' if c_in else 'false'
    if isinstance(c_in, int):
        return str(c_in)
    return c_in


DIFF = {
    'pixMorphDwa_2': {
        'selname': 'sel'
    },
    'pixFMorphopGen_2': {
        'selname': 'sel'
    },
    'pixHMTDwa_1': {
        'selname': 'sel'
    },
    'pixFHMTGen_1': {
        'selname': 'sel'
    },
    'pixMorphDwa_1': {
        'selname': 'sel'
    },
    'pixFMorphopGen_1': {
        'selname': 'sel'
    },
    'pixRenderHashBoxaArb': {
        'boxa': 'box'
    },

    'jbAddPages': {
        'classer': 'jbclasser'
    },
    'jbAddPage': {
        'classer': 'jbclasser'
    },
    'jbAddPageComponents': {
        'classer': 'jbclasser'
    },
    'jbClassifyRankHaus': {
        'classer': 'jbclasser'
    },
    'jbClassifyCorrelation': {
        'classer': 'jbclasser'
    },
    'jbGetComponents': {
        'pboxad': 'ppboxa',
        'ppixad': 'pppixa'
    },

    'jbDataSave': {
        'classer': 'jbclasser'
    },
    'jbGetULCorners': {
        'classer': 'jbclasser'
    },
    'jbGetLLCorners': {
        'classer': 'jbclasser'
    },
    'pixExtractData': {
        'pixs': 'pix'
    },
    'pixGetTileCount': {
        'pn': '*pn'
    },
    'sarrayConvertFilesToPS': {
        'sa': 'sarray',
    },

    'pixWordMaskByDilation': {
        'ppixm': 'pmask',
    },
    'jbAccumulateComposites': {
        'pna': 'ppna',
    },
    'jbDataWrite': {
        'data': 'jbdata',
        'rootout': 'rootname',
    },
    'numaFindLocForThreshold': {
        'na': 'nas'
    },
    'sarrayUnionByHmap': {
        'psad': '*psad',
    },
    'sarrayIntersectionByHmap': {
        'psad': '*psad',
    },

    'jbDataRender': {
        'data': 'jbdata'
    },
    'numaFindSortedLoc': {
        'pindex': '*ploc',
    },
    'sarrayConvertFilesFittedToPS': {
        'sa': 'sarray',
    },
    'ptaSort2d': {
        'pta': 'ptas',
    },
    'pixGetAutoFormat': {
        'pformat': '&format'
    },
    'pixDisplay': {
        'pixs': 'pix',
    },
    'pixDisplayWithTitle': {
        'pixs': 'pix',
    },
    'pixDisplayWrite': {
        'pixs': 'pix',
    },

}


SUB1 = re.compile(r'><document>')
SUB2 = re.compile(r'</document><')


def xml_test(path):
    et = ET.parse(path)
    root = et.getroot()
    functions = root.find('functions')
    function = functions.find('function[@name="ccbaGenerateGlobalLocs"]')
    print(function, function.find('document').text.encode())
    et.write(path, pretty_print=True, encoding='utf-8',
             xml_declaration=True, strip_text=False)
    with open(path, encoding='utf-8') as fr:
        c = fr.read()
        with open(path, 'w+', encoding='utf-8') as fw:
            fw.write(SUB1.sub(r'>\n    <document>',
                     SUB2.sub(r'</document>\n    <', c)))


def xml_doc(path, doc_dir):
    et = ET.parse(path)
    root = et.getroot()
    functions = root.find('functions')
    for function in functions:
        f_name = function.get('name')
        doc_path = osp.join(doc_dir, f'{f_name}.json')
        if not osp.exists(doc_path):
            print('*', f_name, 'not exist')
            continue
        doc_info = load_json(doc_path)
        return_node = function.find('return')
        if return_node is None:
            return_node = ET.SubElement(function, 'return')
            for item in ('rtn_type', 'rtn_ctype', 'rtn_pytype'):
                return_node.set(item[4:], function.get(item))
                if item in function.attrib:
                    del function.attrib[item]
            return_node.text = process_comment(doc_info.get('return'))
        doc_desc = doc_info.get('desc')
        if doc_desc.strip():
            doc_content = process_doxygen(doc_desc)
            doc_node = ET.SubElement(function, 'document')
            doc_node.text = doc_content
        doc_params = doc_info.get('params')
        params_info = {}
        for param in doc_params:
            p_names = param.get('names')
            for p_name in p_names:
                params_info[p_name] = param
        parameters = function.find('parameters')
        if parameters is not None:
            for i, parameter in enumerate(parameters):
                p_name = parameter.get('name')
                if p_name in params_info:
                    param_item = params_info[p_name]
                    parameter.set('optional',
                                  process_attrib(
                                      param_item.get('optional')))
                    parameter.set('io',
                                  process_attrib(
                                      param_item.get('type')))
                    parameter.text = process_comment(param_item.get('desc'))
                else:
                    if f_name in DIFF and p_name in DIFF[f_name]:
                        p_name_ = DIFF[f_name][p_name]
                        if p_name_ in params_info:
                            param_item = params_info[p_name_]
                            parameter.set('optional',
                                          process_attrib(
                                              param_item.get('optional')))
                            parameter.set('io',
                                          process_attrib(
                                              param_item.get('type')))
                            p_desc = param_item.get('desc')
                            if p_desc.strip():
                                parameter.text = process_comment(p_desc)
                            else:
                                parameter.text = process_comment(p_name_)
                        else:
                            ppl = list(params_info)
                            print('+', f_name, p_name, ppl)
                            print()
                    else:
                        ppl = list(params_info)
                        try:
                            ppli = ppl[i]
                        except Exception:
                            ppli = None
                        print('-', f_name, p_name, ppli, ppl)
                        print()
        shutil.move(doc_path, osp.join('finish', osp.basename(doc_path)))

    # return
    fname, ext = osp.splitext(path)
    et.write(f'{fname}_doc{ext}', pretty_print=True, encoding='utf-8',
             xml_declaration=True)


def check_func_doc(path, doc_dir):
    et = ET.parse(path)
    root = et.getroot()
    functions = root.find('functions')
    for function in functions:
        doc = function.find('doc')
        if doc is not None:
            print(doc.text)
    return
    fname, ext = osp.splitext(path)
    et.write(f'{fname}_doc{ext}', pretty_print=True, encoding='utf-8',
             xml_declaration=True)


def main():
    # generate_pys()
    # generate_py()
    # generate_xml()
    xml_doc('leptonica-1.82.0.xml', 'annotation')
    # xml_test('leptonica-1.82.0_doc.xml')
    # check_func_doc('leptonica-1.82.0_doc.xml', 'annotation')
    # check_xml_data()
    # type_map()
    # find_import()


if __name__ == '__main__':
    main()
