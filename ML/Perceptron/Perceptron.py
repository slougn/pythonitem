#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2022-03-07 11:46:11
LastEditTime: 2022-03-07 17:30:46
LastEditors: 560130
Description: 实现感知机,使用贪心方法
FilePath: /PythonItem/ML/Perceptron/Perceptron.py
'''

import numpy as np


class Perceptron():
    def __init__(self, accuracy, rounds) -> None:
        self.accuracy = accuracy  # 设置准确率，停止条件
        self.rounds = rounds  # 设置轮数，停止条件
        self.shape = None  # 保存数据大小
        self.W = None  # 权重
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
                if (self.y * np.dot(self.W , self.X)) > 0:
                    self.acc_count += 1
                else:
                    self.X_correct = (self.X, self.y)
            self.errors_.append(self.acc_count / self.shape[0])
            self.acc_count = 0
            if self.accuracy <= self.acc_count / self.shape[0]:  # 达到准确率
                pass
                # return self.W
            # 更新权重
            print("原权重:", self.W)
            if self.X_correct[1] > 0:
                self.W = self.W - self.X_correct[0]
            else:
                self.W = self.W + self.X_correct[0]
            self.rounds -= 1
        return self.W

if __name__ == "__main__":

    X = np.array([[3, 3], [4, 3], [1, 1]])
    y = np.array([1, 1, -1])

    p = Perceptron(0.9, 10)
    p.fit(X, y)
    print(p.W)
