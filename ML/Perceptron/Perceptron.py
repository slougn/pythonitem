#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2022-03-07 11:46:11
LastEditTime: 2022-03-08 10:17:19
LastEditors: 560130
Description: 实现感知机,使用贪心方法
FilePath: /PythonItem/ML/Perceptron/Perceptron.py
'''

import numpy as np


class Perceptron():
    def __init__(self, eta, rounds) -> None:
        self.rounds = rounds  # 设置轮数，停止条件
        self.shape = None  # 保存数据大小
        self.W = None  # 权重
        self.b = 0 # 截距
        self.eta = eta
        self.X = None  # 数据
        self.y = None  # 标签
        self.acc_count = 0  # 每一轮的准确个数
        self.X_correct = None  # 用来保存错误的点
        self.round_count = 0  # 统计轮数
        self.errors_ = []  #用来保存历史准确率

    def fit(self, X, y):
        self.shape = X.shape
        self.W = np.random.randn(1, self.shape[1])
        while self.rounds > 0:
            for i in range(0, self.shape[0]):  # 遍历计算准确个数
                self.X = X[i]
                self.y = y[i] 
                if (self.y * (np.dot(self.W , self.X) + self.b)) > 0:
                    self.acc_count += 1
                else:
                    self.X_correct = (self.X, self.y)
            self.errors_.append(self.acc_count / self.shape[0])
            print("原权重:", self.W,"准确率:", self.acc_count / self.shape[0])
            self.acc_count = 0
            # 更新权重
            self.W = self.W + self.eta * self.X_correct[1] * self.X_correct[0]
            self.b = self.b + self.eta * self.X_correct[1]
            self.rounds -= 1
        return self.W

if __name__ == "__main__":

    X = np.array([[3, 3], [4, 3], [1, 1]])
    y = np.array([1, 1, -1])

    p = Perceptron(0.9, 20)
    p.fit(X, y)
    print(p.W)
