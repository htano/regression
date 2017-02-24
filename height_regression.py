#!/Users/htano/.pyenv/versions/3.5.0/bin/python3

import math
import numpy as np
import pylab

if __name__ == '__main__':
    age = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    height = [100.1, 107.2, 114.1, 121.7, 126.8, 130.9, 137.5, 143.2, 149.4, 151.6, 154.0, 154.6, 155.0, 155.1, 155.3, 155.7]

    X = []
    for a in age:
        X.append(1.0/a)

    # 平均
    X_ave      = sum(X) / len(X)
    height_ave = sum(height) / len(height)

    # 偏差平方和
    Sxx = 0
    for x in X:
        Sxx += (x - X_ave) ** 2
    Syy = 0
    for h in height:
        Syy += (h - height_ave) ** 2
    # 偏差積和
    Sxy = 0
    for i in range(len(X)):
        Sxy += (X[i] - X_ave) * (height[i] - height_ave)

    a = Sxy / Sxx
    b = height_ave - a * X_ave

    regression = []
    for x in X:
        regression.append(a * x + b)

    pylab.figure()
    pylab.plot(X[::-1], height, 'k+', label='X')
    pylab.plot(X[::-1], regression, label='regression')
    pylab.legend()
    pylab.show()
