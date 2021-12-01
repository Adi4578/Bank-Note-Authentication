# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:57:08 2021

@author: hp
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float