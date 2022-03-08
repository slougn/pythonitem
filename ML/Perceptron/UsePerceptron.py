#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2022-03-07 11:34:22
LastEditTime: 2022-03-08 10:22:05
LastEditors: 560130
Description: 使用感知机
FilePath: /PythonItem/ML/Perceptron/UsePerceptron.py
'''

from matplotlib import markers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Perceptron import Perceptron

# 准备数据
df = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    header=None)  #下载数据
print(df.tail())  #显示数据后5行

#画图
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0, 2]].values  # 取df中的前三列，前100行数据

plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o',
            label='setosa')  # 散点图
plt.scatter(X[50:100, 0],
            X[50:100, 1],
            color='blue',
            marker='x',
            label='versicolor')  # 散点图
plt.xlabel('petal length')  # x轴说明
plt.ylabel('sepal length')  # y轴说明
plt.legend(loc='upper left')  # 说明位置
plt.show()  # 画图

ppn = Perceptron(0.1, 10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel("Epoches")
plt.ylabel('Number of misclassifications')
plt.show()
