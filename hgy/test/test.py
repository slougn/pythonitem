#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2022-05-09 21:26:53
LastEditTime: 2022-05-09 21:59:21
LastEditors: 560130
Description: 
FilePath: /PythonItem/test/test.py
'''

import numpy as np
import copy

A = [np.array([1,1,1,1,1,1]),np.array([100,100,100,100]),np.array([0,0,0])]
def test(A):
    B = copy.deepcopy(A)
    tmp = 0
    for b in B:
        b[b==1] = 2
        b[b>50] = -100
        print("b",b is B[tmp]," ",b)
        tmp = tmp +1
    return B

def AI_column(AG):
    # AI = []
    # for ag in AG:
        # AI.append(ag/250*50)
    AI = copy.deepcopy(AG)
    tmp = 0
    for ai in AI:
        tt = ai
        ai[:] = ai/250*50   #重新拷贝新的一份
        ai[ai == 0] = 0
        ai[(ai>0) & (ai < 30)] = 30
        ai[ai >50] = 50
        print("ai",ai is AI[tmp]," ",ai)
        tmp = tmp +1
    return AI


print(A)

print(test(A))

print(AI_column(A))