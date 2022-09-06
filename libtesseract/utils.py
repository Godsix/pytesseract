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
import platform


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


SNAKE = re.compile('([A-Z])([A-Z](?=[a-z]))|([a-z])([A-Z](?=[A-Z]))|([a-z])([A-Z](?=[a-z]))')


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


if __name__ == '__main__':
    print(name_convert('HelloAPIWorld'))  # -> hello_world_world
    # print(name_convert('wo_shi_osin'))  # -> woShiOsin
