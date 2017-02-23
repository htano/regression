#!/Users/htano/.pyenv/versions/3.5.0/bin/python3
import math
import numpy as np
from scipy  import integrate
def get_average(list):
    return sum(list)/len(list)

def calc_sum_of_square_deviation(list, average):
    sum_of_square_deviation = 0
    for val in list:
        sum_of_square_deviation += (val - average) ** 2
    return sum_of_square_deviation

if __name__ == '__main__':
    temperature = [29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30]
    sales_num   = [77, 62, 93, 84, 59, 64, 80, 75, 58, 91, 51, 73, 65, 84]

    # 平均 average
    # 気温の平均 : temp_ave = x, 注文数の平均 : sales_num = y
    temp_ave   = get_average(temperature)
    sales_ave  = get_average(sales_num)

    print ('temperature averag    : ' + str(temp_ave))
    print ('sales average          : ' + str(sales_ave))

    # 偏差積和 sum of products of deviation : Sxy
    Sxy = 0
    for i in range(len(temperature)):
        Sxy += (temperature[i] - temp_ave) * (sales_num[i] - sales_ave)
    # 共分散 covariance
    covariance = Sxy / len(temperature)

    print ('covariance             : ' + str(covariance))

    # 標準偏差 standard deviation
    temp_standard_deviation = np.std(temperature)
    sales_standard_deviation = np.std(sales_num)

    # 単相関係数 correlation coefficient
    correlation_coefficient = covariance / (temp_standard_deviation * sales_standard_deviation)

    print ('correlation coeficient : ' + str(correlation_coefficient))

    # 偏差平方和 sum of square deviation
    # 気温の偏差平方和 : Sxx, 注文数の偏差平方和 : Syy
    Sxx = calc_sum_of_square_deviation(temperature, temp_ave)
    Syy = calc_sum_of_square_deviation(sales_num, sales_ave)

    print ('Sxx : ' + str(Sxx))
    print ('Syy : ' + str(Syy))
    print ('Sxy : ' + str(Sxy))

    # a = Sxy / Sxx, b = ave_y - ave_x * a
    a = Sxy / Sxx
    b = sales_ave - temp_ave * a

    print ('a : ' + str(a))
    print ('b : ' + str(b))

    predict_sales_num = []
    for i in range(len(temperature)):
        predict_sales_num.append(a * temperature[i] + b)

    # 予想値 : y
    predict_sales_ave = get_average(predict_sales_num)

    print ('predict sales ave : ' + str(predict_sales_ave))

    # 偏差平方和 sum of square deviation
    # Sy^y^ : Sy_y_
    Sy_y_ = calc_sum_of_square_deviation(predict_sales_num, predict_sales_ave)

    print ('Sy^y^  : ' + str(Sy_y_))

    # 偏差積和 sum of products of deviation
    # Syy^ : Syy_
    Syy_ = 0
    for i in range(len(sales_num)):
        Syy_ += (sales_num[i] - sales_ave) * (predict_sales_num[i] - predict_sales_ave)

    print ('Syy^ : ' + str(Syy_))

    Se = 0
    for i in range(len(sales_num)):
        Se += (sales_num[i] - predict_sales_num[i]) ** 2

    print ('Se : ' + str(Se))

    # 重相関係数 multiple correlation coefficient
    # R = Syy^ / sqrt(Syy * Sy^y^)
    R = Syy_ / math.sqrt(Syy * Sy_y_)
    # 寄与率 contribution ratio
    RR = R ** 2

    print ('R    : ' + str(R))
    print ('R**2 : ' + str(RR))

    # RR = (a * Sxy)/Syy
    #print ((a * Sxy)/Syy)
    # RR = (1- Se/Syy)
    #print (1 - (Se/Syy))

    # 回帰係数の検定
    # 母回帰 y = Ax + B
    A = a
    B = b
    sigma = math.sqrt(Se/(len(temperature)-2))

    print ('A     : ' + str(A))
    print ('B     : ' + str(B))
    print ('sigma : ' + str(sigma))
    # 有意水準 significance level
    significance_level = 0.05

    # 回帰係数の検定
    approval_val = \
        (a ** 2)/(1/Sxx) / (Se/(len(temperature) - 2))

    print ('approval val : ' + str(approval_val))

    # F分布からPを求める
    # 保留

    # 気温 31度 信頼率 95% における信頼区間の算出
    # F(1, 14-2;0.05) = 4.7
    trusted_section = math.sqrt(4.7 * \
        ((1/len(temperature) + (31 - temp_ave)**2 / Sxx) * \
        Se/(len(temperature) - 2 )))

    print ('trusted section : ' + str(trusted_section))

    # 推定
    # 気温 27度 信頼率 95% における予測区間の算出
    # F(1, 14-2;0.05) = 4.7
    predicted_section = math.sqrt(4.7 * \
        (1 + 1/len(temperature) + (27 - temp_ave) ** 2 / Sxx) * \
        Se / (len(temperature) - 2))
    print ('predicted section : ' + str(predicted_section))
