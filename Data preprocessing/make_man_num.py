# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:33:29 2018

@author: zhang
"""

import numpy as np
import pandas as pd

filename = 'C:\\Users\\zhang\\Desktop\\d_test.xls'
p = pd.read_excel(filename)
s = p[1]

pl = []
for i in s:
    if i == '男':
        pl.append(1)
    else:
        pl.append(2)
        
p[1] = pl

p.to_csv('C:\\Users\\zhang\\Desktop\\d_test.csv')
