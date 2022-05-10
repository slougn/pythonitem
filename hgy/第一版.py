#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2022-05-01 14:26:18
LastEditTime: 2022-05-03 15:04:41
LastEditors: 560130
Description: 
FilePath: /pythonitem/hgy/inputData.py
'''

from scipy.optimize import minimize
import pandas as pd
import numpy as np
from scipy import optimize

cool_machine = pd.read_excel(
    '/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/data/XLS 工作表.xls',
    sheet_name='Sheet1')
cool_out = pd.read_excel(
    '/home/gree/MyDocument/MyWorkSpace/pythonitem/hgy/data/XLS 工作表.xls',
    sheet_name='Sheet2')

R = cool_machine[["one_R","two_R","three_R"]].values
Pch = cool_machine[["one_Pch","two_Pch","three_Pch"]].values
Pchw = cool_machine[["one_Pchw","two_Pchw","three_Pchw"]].values
Pcw = cool_machine[["one_Pcw","two_Pcw","three_Pcw"]].values
Pcwt = cool_machine[["one_Pcwt","two_Pcwt","three_Pcwt"]].values
param0 = cool_machine[["param1","param2","param3"]].values
Out = cool_out["peng_Pch"].values


print(param0.shape)


def toVector(param):
    assert param.shape == (24,3)
    return param.flatten()

def toMatrix(vec):
    assert vec.shape == (24*3,)
    return vec.reshape(24,3)


def Fobj(param):
    y = abs((Pch + Pchw + Pcw + Pcwt) * param)
    out = sum((y[:12].sum(axis=1) + y[12:].sum(axis=1) - Out)**2)
    return out

def OutFobj(param):
    y = abs((Pch + Pchw + Pcw + Pcwt) * param)
    out = (y[:12].sum(axis=1) + y[12:].sum(axis=1))
    return out


def cons_fun(x):
    x = toMatrix(x)
    y = abs((Pch + Pchw + Pcw + Pcwt) * x) 
    out = y[:12].sum(axis=1) + y[12:].sum(axis=1)
    return out

#限制条件函数
def cons_0(x):
    return cons_fun(x)[0] / sum(cons_fun(x)) - Out[0]/sum(Out)

def cons_1(x):
    return cons_fun(x)[1] / sum(cons_fun(x)) - Out[1]/sum(Out)

def cons_2(x):
    return cons_fun(x)[2] / sum(cons_fun(x)) - Out[2]/sum(Out)

def cons_3(x):
    return cons_fun(x)[3] / sum(cons_fun(x)) - Out[3]/sum(Out)

def cons_4(x):
    return cons_fun(x)[4] / sum(cons_fun(x)) - Out[4]/sum(Out)

def cons_5(x):
    return cons_fun(x)[5] / sum(cons_fun(x)) - Out[5]/sum(Out)

def cons_6(x):
    return cons_fun(x)[6] / sum(cons_fun(x)) - Out[6]/sum(Out)

def cons_7(x):
    return cons_fun(x)[7] / sum(cons_fun(x)) - Out[7]/sum(Out)

def cons_8(x):
    return cons_fun(x)[8] / sum(cons_fun(x)) - Out[8]/sum(Out)

def cons_9(x):
    return cons_fun(x)[9] / sum(cons_fun(x)) - Out[9]/sum(Out)

def cons_10(x):
    return cons_fun(x)[10] / sum(cons_fun(x)) - Out[10]/sum(Out)

def cons_11(x):
    return cons_fun(x)[11] / sum(cons_fun(x)) - Out[11]/sum(Out)

list_cons_1 = [
     {
        'type': 'eq',
        'fun': cons_0
    },
    {
        'type': 'eq',
        'fun': cons_1
    },
    {
        'type': 'eq',
        'fun': cons_2
    },
    {
        'type': 'eq',
        'fun': cons_3
    },
    {
        'type': 'eq',
        'fun': cons_4
    },
    {
        'type': 'eq',
        'fun': cons_5
    },
    {
        'type': 'eq',
        'fun': cons_6
    },
    {
        'type': 'eq',
        'fun': cons_7
    },
    {
        'type': 'eq',
        'fun': cons_8
    },
    {
        'type': 'eq',
        'fun': cons_9
    },
    {
        'type': 'eq',
        'fun': cons_10
    },
    {
        'type': 'eq',
        'fun': cons_11
    },
]




type : 'eq'
    
cons_list = []


for i in range(24):
    for j in range(3):
        if R[i,j]!=0:
            def makefunc(i,j):
                def consf(x):
                    return x[i*3+j]
                return consf
            cons_list.append(makefunc(i,j))
        else:
            continue

# print(cons_list)


list_cons = []
for i in range(len(cons_list)):
    list_cons.append(("type","ineq"))
    list_cons.append(("fun",cons_list[i]))


list_cons_dict = []
for i in range(0,len(cons_list),2):
    temp = dict(list_cons[i:i+2])
    list_cons_dict.append(temp)

list_cons_dict = list_cons_dict + list_cons_1

tuple_cons = tuple(list_cons_dict)
# print(list_cons_dict)
# a = 100000


#设置限制条件
#cons = (
#    {
#        'type': 'ineq',
#        'fun': cons0
#    },
#)

def doOptimization(Fobj, parma0):
    def f(x): 
        param = toMatrix(x)
        return Fobj(param)
    
    # fprime = lambda x: optimize.approx_fprime(x, f, 0.01)
    # result = minimize(f, toVector(parma0), method='Newton-CG', constraints=tuple_cons,jac = fprime)
    result = minimize(f, toVector(parma0), method='L-BFGS-B', constraints=tuple_cons)
    # result = minimize(f, toVector(parma0), method='TNC', constraints=tuple_cons)

    # Different optimize functions return their
    # vector result differently. In this case it's result.x:
    result.x = toMatrix(result.x) 
    return result

    # X = (15*12)矩阵

result = doOptimization(Fobj=Fobj,parma0=param0)

print(result)
x = result.x
print(OutFobj(x))
# print(OutFobj(result.x)