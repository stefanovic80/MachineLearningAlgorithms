#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:04:01 2022

@author: stefano
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import os
#path = '/home/stefano/perceptron'
#os.chdir(path)
fileName = 'dataFlowers.xlsx'
df = pd.read_excel(fileName)#, header = None)

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0, 2]].values
plt.scatter(X[:50, 0], X[:50, 1], color = 'red', marker = 'o', label = 'setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color = 'blue', marker = 'x', label = 'versicolor')
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.legend(loc= 'upper left')
plt.grid()
plt.show()