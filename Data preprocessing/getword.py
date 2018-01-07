# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:50:07 2018

@author: zhang
"""
import re
import numpy as np
import pandas as pd

filename = 'C:\\Users\\zhang\\Desktop\\Aspects\\tripword.csv'
word = pd.read_csv(filename)
word1 = word['word']
diction = []

for i in word1:
    #while(1):
    for j in range(100):
        start = i.find('(')
        end = i.find(')')
        if start == -1:
            break
        tempw = i[start+1:end]
        if tempw not in diction:
            diction.append(i[start+1:end])
        else:
            1
            #print(i[start+1:end])
        i = i[end+1:]
        



