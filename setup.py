# -*- coding: utf-8 -*-
# Copyright 2020 wanghao
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import os
import os.path as osp
import codecs
from setuptools import setup, find_packages
from libtesseract import __version__

LIBNAME = 'libtesseract'


try:
    with codecs.open('README.rst', encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''


def get_subpackages(name):
    """Return subpackages of package *name*"""
    splist = []
    for dirpath, _dirnames, _filenames in os.walk(name):
        if 'tests' not in dirpath:
            if osp.isfile(osp.join(dirpath, '__init__.py')):
                splist.append(".".join(dirpath.split(os.sep)))
    return splist


def get_package_data(name, exclude=[]):
    """Return data files for package *name* with extensions exclude ext in
    *exclude*"""
    flist = []
    # Workaround to replace os.path.relpath (not available until Python 2.6):
    offset = len(name) + len(os.pathsep)
    for dirpath, _dirnames, filenames in os.walk(name):
        if '__pycache__' not in dirpath:
            for fname in filenames:
                if (not fname.startswith('.') and
                        not osp.splitext(fname)[1] in exclude):
                    flist.append(osp.join(dirpath, fname)[offset:])
    return flist


setup(
    name=LIBNAME,
    version=__version__,
    description='A pythonic wrapper of tesseract capi for OCR',
    long_description=long_description,
    keywords='python wrapper tesseract ocr',
    author='wanghao',
    author_email='haoyueshangren@gmail.com',
    url='https://github.com/GodSix/pytesseract',
    license='Apache License, Version 2.0',
    packages=find_packages(exclude=['*.contrib', '*.docs', '*.tests']),
    install_requires=[
        'Pillow>=8.0.0'
    ],
    platforms=["Windows"],
    python_requires='>=3.6',
    package_data={LIBNAME: get_package_data(LIBNAME)},
    classifiers=[
        "Environment :: Win32 (MS Windows)",
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: Microsoft :: Windows',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Communications',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
