# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 11:59:55 2017

@author: Green
"""

""" join（）函数
语法：‘sep’.join（seq）
参数： sep：分隔符。可以为空; seq：要连接的元素序列、字符串、元组、字典等
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串
"""

seq1 = ['hello', 'you', 'oo', 'things']
print(' '.join(seq1))
print('$'.join(seq1))
seq2 = 'my name is hobbit'
print('.'.join(seq2))
seq3 = ('bala', 'baba', 'lala')
print(','.join(seq3))
seq4 = {'im':1, 'a':2, 'dict':3, 'what?':4}
print('+'.join(seq4))
"""os.path.join()函数
语法：  os.path.join(path1,path2,......)
返回值：将多个路径组合后返回
注：第一个绝对路径之前的参数将被忽略
"""
import os
path = os.path.join('C:', 'Users', 'Green', 'Desktop', 'PyCode')
print(path)