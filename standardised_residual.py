#!/Users/htano/.pyenv/versions/3.5.0/bin/python3

import math
import numpy as np

if __name__ == '__main__':
    temperature = [29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30]
    sales_num   = [77, 62, 93, 84, 59, 64, 80, 75, 58, 91, 51, 73, 65, 84]

    temp_ave  = sum(temperature) / len(temperature)
    sales_ave = sum(sales_num) / len(sales_num)

    # 偏差平方和
    Sxx = 0
    for temp in temperature:
        Sxx += (temp - temp_ave) ** 2
    Syy = 0
    for sale in sales_num:
        Syy += (sale - sales_ave) ** 2
    # 偏差積和
    Sxy = 0
    for i in range(len(temperature)):
        Sxy += (temperature[i] - temp_ave) * (sales_num[i] - sales_ave)
    a = Sxy / Sxx
    b = sales_ave - temp_ave * a

    # 残差
    residual = []
    # 残差平方和
    Se = 0
    for i in range(len(temperature)):
        y  = sales_num[i]
        y_ = a * temperature[i] + b
        r = y - y_
        Se += r ** 2
        residual.append(r)

    # 標準化残差
    standardised_residual = []
    for i in range(len(residual)):
        sr = residual[i] / math.sqrt(Se/(len(temperature)-2))
        standardised_residual.append(sr)

    print (standardised_residual)
