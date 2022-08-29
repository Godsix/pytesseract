# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 08:52:34 2021

@author: 皓
"""
import os.path as osp
from platform import architecture
from .utils import get_data_path, get_file_path


BITS = architecture()[0][:2]
DIR = osp.dirname(__file__)
DLLDIR = osp.join(DIR, 'x86' if BITS == '32' else 'x64')
TESS_DLL = get_file_path(osp.join(DLLDIR, 'tesseract*.dll'))
LEPT_DLL = get_file_path(osp.join(DLLDIR, 'leptonica-*.dll'))
TESSDATA_PREFIX = get_data_path('TESSDATA_PREFIX', osp.join(DIR, 'tessdata'))
