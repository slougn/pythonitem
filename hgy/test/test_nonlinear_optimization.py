#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2022-03-30 15:55:25
LastEditTime: 2022-03-30 17:06:58
LastEditors: 560130
Description: 
FilePath: /pythonitem/test/test_nonlinear_optimization.py
'''
from scipy.optimize import minimize
import numpy as np

# 目标函数
def Fobj(x):
    '''
    description: F(x_1,x_2,x_3,x_4,x_5)=(5*x_1-100)^2+(6*x_2+7*x_3-200)^2+(8*x_4+9*x_5-300)^2
    param {x}:x_1->x[0], x_2->x[1], x_3->x[2], x_4->x[3]
    return {F(x_1,x_2,x_3,x_4,x_5)}
    '''
    return (5 * x[0] - 100)**2 + (6 * x[1] + 7 * x[2] -
                                  200)**2 + (8 * x[3] + 9 * x[4] - 300)**2


#限制条件函数
def cons0(x):  # 不等式约束 f(x) >= 0
    '''
    description: x_1 >= 1 --> x_1 -1 >=0
    param {x}:x_1->x[0], x_2->x[1], x_3->x[2], x_4->x[3]
    return {cons >= 0}
    '''
    return x[0] - 1


def cons1(x):
    '''
    description: x_2 >= 1 --> x_2 -1 >=0
    param {*}
    return {*}
    '''
    return x[1] - 1


def cons2(x):
    '''
    description:x_3 >= 1 --> x_3 -1 >=0 
    param {*}
    return {*}
    '''
    return x[2] - 1


def cons3(x):
    '''
    description: x_4 >=1 --> x_4 -1 >=0
    param {*}
    return {*}
    '''
    return x[3] - 1


def cons4(x):
    '''
    description: x_5 >=1 --> x_5 -1 >=0 
    param {*}
    return {*}
    '''
    return x[4] - 1


def cons5(x):
    '''
    description: x_2 + x_3 <= 30 --> 30 - x_2 - x_3 >= 0
    param {*}
    return {*}
    '''
    return 30 - x[1] - x[2]


def cons6(x):
    '''
    description: x_4 + x_5 <= 21 --> 31 - x_4 - x_5 >= 0
    param {*}
    return {*}
    '''
    return 31 - x[3] - x[4]


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
