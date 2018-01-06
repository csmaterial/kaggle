# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 12:22:05 2018

@author: zhang
"""

import numpy as np
import pandas as pd
import math

filename = 'C:\\Users\\zhang\\Desktop\\d.csv'
filename1 = 'C:\\Users\\zhang\\Desktop\\d_test.csv'
stock = pd.read_csv(filename)
stock1 = pd.read_csv(filename1)

#check all column
#l have the col which is none nan
def checkCol(stock):
    l = []
    for num in range(stock.shape[1]):
        count = 0
        for i in range(stock.shape[0]):
            #print(num,i)
            if math.isnan(stock[str(num)][i]):
                count+=1
        if count == 0:
            l.append(num)
    return l

#check all Row
#l have the row which is none nan
def checkRow(stock):
    l = []
    for num in range(stock.shape[0]):
        count = 0
        for i in ll:
            #print(num,i)
            te = stock[i][int(num)]
            if math.isnan(te):
                count+=1
        if count == 0:
            l.append(num)
    return l

l = checkCol(stock)
l = checkRow(stock)

