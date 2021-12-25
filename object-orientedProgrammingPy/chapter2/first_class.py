#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2021-12-25 14:56:14
LastEditTime: 2021-12-25 17:55:23
LastEditors: 560130
Description: 面向对面编程第二章python代码
FilePath: /PythonItem/object-orientedProgrammingPy/chapter2/first_class.py
'''
import math


class MyFirstClass:
    pass


class Point:
    '''
    description: 一个point类，可以移动，可以算距离
    '''

    def __init__(self, x=0, y=0) -> None:
        '''
        description:初始化point类，（x,y）坐标默认为0
        param {x=0,y=0}
        return {None}
        '''
        self.move(x, y)

    def move(self, x, y):
        '''
        description:把坐标移动到(x,y)
        param {x,y}
        return {None}
        '''
        self.x = x
        self.y = y

    def reset(self):
        '''
        description:重置坐标
        param {None}
        return {None}
        '''
        self.x = 0
        self.y = 0

    def calculate_distance(self, other_point):
        '''
        description:计算两个Point的距离
        param {other_point}
        return {float}
        '''
        return math.sqrt(
            (self.x - other_point.x)**2 + (self.y - other_point.y)**2
        )
