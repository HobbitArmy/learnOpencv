# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 19:57:05 2018

@author: Green
"""

import pandas as pd

list1 = ['hb']*82
list2 = []
for i in range(82):
    list2.append('pgm/'+str(i)+'.pgm')
dataframe = pd.DataFrame({'data1' : list2, 'data2' : list1})
dataframe.to_csv('test.csv', index = False, header = False, sep = ';')