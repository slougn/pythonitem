#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2022-05-03 11:38:11
LastEditTime: 2022-05-03 11:38:11
LastEditors: 560130
Description: 
FilePath: /pythonitem/hgy/test1.py
'''


from scipy.optimize import minimize
import pandas as pd
import numpy as np

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


# 目标函数
def Fobj(x):
    '''
    description: F(x_1,x_2,x_3,x_4,x_5)=(5*x_1-100)^2+(6*x_2+7*x_3-200)^2+(8*x_4+9*x_5-300)^2
    param {x}:x_1->x[0], x_2->x[1], x_3->x[2], x_4->x[3]
    return {F(x_1,x_2,x_3,x_4,x_5)}
    '''
    y = ((Pch + Pchw + Pcw + Pcwt) * x)**2 
    out = sum((y[:12].sum(axis=1) + y[12:].sum(axis=1) - Out)**2)
    return out


#初始化
x0 = np.zeros(24,3)
for i in range(24):
    for j in range(3):
        if R[i,j] != 0:
            x0[i,j] = 1

#限制条件函数
def cons(x):  # 不等式约束 f(x) >= 0
    '''
    description: x_1 >= 1 --> x_1 -1 >=0
    param {x}:x_1->x[0], x_2->x[1], x_3->x[2], x_4->x[3]
    return {cons >= 0}
    '''
    if R[0,0] != 0

    return x[0*0] - 1





# 设置初始猜测值
x0 = np.asarray((1, 1, 1, 1, 1))

#设置限制条件
cons = (
    {
        'type': 'ineq',
        'fun': cons0
    },
    {
        'type': 'ineq',
        'fun': cons1
    },
    {
        'type': 'ineq',
        'fun': cons2
    },
    {
        'type': 'ineq',
        'fun': cons3
    },
    {
        'type': 'ineq',
        'fun': cons4
    },
    {
        'type': 'ineq',
        'fun': cons5
    },
    {
        'type': 'ineq',
        'fun': cons6
    },
)

res = minimize(Fobj, x0, method='SLSQP', constraints=cons)
print(res.fun)
print(res.success)
print(res.x)






