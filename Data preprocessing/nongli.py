# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 13:06:12 2018

@author: zhang
"""

import numpy as np
import pandas as pd

train = 5642
test = 1000
#http://data.weather.gov.hk/gts/time/calendar/text/T2017c.txt
#带月是初一
nongli = pd.read_excel('C:\\Users\\zhang\\Desktop\\date.xlsx')
nongli = nongli[0]
date = np.genfromtxt('C:\\Users\\zhang\\Desktop\\date.csv',delimiter=',')
dic = np.genfromtxt('C:\\Users\\zhang\\Desktop\\datedic.csv',delimiter=',')

l = []
for i in range(12):
    i+=1
    ltemp = []
    for j in range(len(dic)):
        if dic[j,1] == i:
            ltemp.append(j)
    l.append(ltemp)

e = np.zeros(len(date))
for i in range(len(date)):
    ll = l[int(date[i,1])-1]
    e[i] = ll[int(date[i,0])-1]

datee = []
for i in range(len(date)):
    datee.append(nongli[int(e[i])])
#双数日是-1 单数日是1
e = np.zeros(len(date))
count = 0
for i in datee:
    if i[1] == '二':
        e[count] = -1
    elif i[1] == '四':
        e[count] = -1
    elif i[1] == '六':
        e[count] = -1
    elif i[1] == '八':
        e[count] = -1
    elif i[1] == '十':
        e[count] = -1
    else:
        e[count] = 1
    count+=1

tr = e[0:train]
te = e[train:]        

np.savetxt('C:\\Users\\zhang\\Desktop\\file.csv',tr,delimiter=',')
np.savetxt('C:\\Users\\zhang\\Desktop\\file.csv',te,delimiter=',')

