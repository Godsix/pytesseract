# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:56:02 2021

@author: 皓
"""
import os
import os.path as osp
import re
import time
from functools import wraps, lru_cache
from glob import glob
import logging
import platform
from zipfile import ZipFile, is_zipfile
import importlib
try:
    import lxml.etree as ET
except ModuleNotFoundError:
    import xml.etree.ElementTree as ET


@lru_cache()
def arch_bit():
    bit, *_ = platform.architecture()
    if bit == '32bit':
        return 32
    return 64


@lru_cache()
def arch_hex_bit():
    return arch_bit() // 4


def print_run_time(fmt='{name} spend time: {time:.3f} s.', logger=print):
    if isinstance(fmt, str):
        def decorator(func):
            name = getattr(func, '__name__', repr(func))
            param = {'name': name}

            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                ret = func(*args, **kwargs)
                end = time.time()
                _ = param.setdefault('time', end - start)
                logger(fmt.format_map(param))
                return ret
            return wrapper
        return decorator
    elif callable(fmt):
        default_fmt = '{name} spend time: {time:.3f} s.'
        name = getattr(fmt, '__name__', repr(fmt))
        param = {'name': name}

        @wraps(fmt)
        def wrapper(*args, **kwargs):
            start = time.time()
            ret = fmt(*args, **kwargs)
            end = time.time()
            _ = param.setdefault('time', end - start)
            logger(default_fmt.format_map(param))
            return ret
        return wrapper
    raise TypeError(
        'Expected first argument to be an string, or a callable.')


def name_convert_to_camel(name: str) -> str:
    """下划线转驼峰(小驼峰)"""
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), name)


def sub_snake(match):
    ret = [x for x in match.groups() if x]
    return '{}_{}'.format(ret[0], ret[1])


SNAKE = re.compile(
    '([A-Z])([A-Z](?=[a-z]))|([a-z])([A-Z](?=[A-Z]))|([a-z])([A-Z](?=[a-z]))')


def name_convert_to_snake(name: str) -> str:
    """驼峰转下划线"""
    if '_' not in name:
        name = SNAKE.sub(sub_snake, name)
    else:
        raise ValueError(f'{name}字符中包含下划线，无法转换')
    return name.lower()


def name_convert(name: str) -> str:
    """驼峰式命名和下划线式命名互转"""
    icn = True  # 是否为驼峰式命名 is_camel_name
    if '_' in name and re.match(r'[a-zA-Z_]+$', name):
        icn = False
    elif re.match(r'[a-zA-Z\d]+$', name) is None:
        raise ValueError(f'Value of "name" is invalid: {name}')
    return name_convert_to_snake(name) if icn else name_convert_to_camel(name)


def get_data_path(name, default=None):
    '''获取 datapath 路径'''
    path = os.environ.get(name)
    if path:
        if osp.exists(path):
            return path
        else:
            Warning(f'{name} variable exists, but path is not exists.')
    if default and osp.exists(default):
        return default
    raise ValueError(f'Get {name} value fail.')


def get_file_path(path):
    '''获取目录下文件路径，如果多个文件取最后一个'''
    files = glob(path)
    if files:
        return files[-1]
    return None


def find_xml(name, *paths):
    for path in paths:
        xml_path = osp.join(path, f'{name}.xml')
        if osp.exists(xml_path):
            data_path = xml_path
            is_zip = False
            break
        zip_path = osp.join(path, f'{name}.zip')
        if osp.exists(zip_path):
            data_path = zip_path
            is_zip = True
            break
    else:
        return None
    if is_zip:
        if not is_zipfile(data_path):
            return None
        xml_name = f'{name}.xml'
        with ZipFile(data_path) as zf:
            namelist = zf.namelist()
            if not namelist:
                return None
            zfile = xml_name if xml_name in namelist else namelist[-1]
            with zf.open(zfile) as fp:
                logging.debug('Parse zip file %s from %s', zfile, data_path)
                root = ET.fromstring(fp.read())
                return ET.ElementTree(root)
    else:
        logging.debug('Parse xml file from %s', data_path)
        return ET.parse(data_path)


def load_data_from_xml(name, *paths, variables=None):
    et = find_xml(name, *paths)
    if et is None:
        return None
    root_node = et.getroot()
    local_var = {}
    result = {}
    imports_node = root_node.find('imports')
    if imports_node is not None:
        for module_node in imports_node:
            module_name = module_node.get('name')
            if module_name.startswith('.'):
                package = __package__
            else:
                package = None
            try:
                module_object = importlib.import_module(module_name, package)
            except ImportError as e:
                logging.error('from %s import %s error.', module_name, package)
                raise e
            if len(module_node) > 0:
                for obj in module_node:
                    obj_name = obj.get('name')
                    obj_value = getattr(module_object, obj_name)
                    local_var[obj_name] = obj_value
            else:
                local_var[module_name] = module_object
    functions_node = root_node.find('functions')
    if functions_node is not None:
        for function in functions_node:
            name = function.get('name')
            return_node = function.find('return')
            rtn_ctype = return_node.get('ctype')
            restype = eval(rtn_ctype, variables, local_var)
            parameters = function.find('parameters')
            if parameters is None or len(parameters) == 0:
                argtypes = []
            else:
                argtypes = [eval(x.get('ctype'),
                                 variables,
                                 local_var) for x in parameters]
            result[name] = restype, *argtypes
    return result


if __name__ == '__main__':
    print(name_convert('HelloAPIWorld'))  # -> hello_world_world
    # print(name_convert('wo_shi_osin'))  # -> woShiOsin
