# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 09:31:11 2021

@author: 皓
"""


class TesseractError(Exception):
    """
    Obsolete. You should look for PyocrException
    """

    def __init__(self, status, message):
        super().__init__(self, message)
        self.status = status
        self.message = message
        self.args = (status, message)
