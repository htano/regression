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
    temp_ave = get_average(temperature)
    sales_ave  = get_average(sales_num)

    # 共分散 covariance
    deviation_sum = 0
    for i in range(len(temperature)):
        deviation_sum += (temperature[i] - temp_ave) * (sales_num[i] - sales_ave)
    covariance = deviation_sum / len(temperature)

    # 標準偏差 standard deviation
    temp_standard_deviation = np.std(temperature)
    sales_standard_deviation = np.std(sales_num)

    # 単相関係数 correlation coefficient
    correlation_coefficient = covariance / (temp_standard_deviation * sales_standard_deviation)

    # 偏差平方和 sum of square deviation
    # Sxx : temp_sum_of_square_deviation, Syy : sales_sum_of_square_deviation
    temp_sum_of_square_deviation = calc_sum_of_square_deviation(temperature, temp_ave)
    sales_sum_of_square_deviation = calc_sum_of_square_deviation(sales_num, sales_ave)
    # 偏差積和 sum of products of deviation
    # Sxy : deviation_sum

    # a = Sxy / Sxx, b = ave_y - ave_x * a
    a = deviation_sum / temp_sum_of_square_deviation
    b = sales_ave - temp_ave * a

    predict_sales_num = []
    for i in range(len(temperature)):
        predict_sales_num.append(a * temperature[i] + b)
    predict_sales_ave = get_average(predict_sales_num)

    # 偏差平方和 sum of square deviation
    # Sy^y^
    predict_sales_sum_of_square_deviation = \
        calc_sum_of_square_deviation(predict_sales_num, predict_sales_ave)

    # 偏差積和 sum of products of deviation
    # Syy^ : Sy-y_
    Sy_y_ = 0
    for i in range(len(sales_num)):
        Sy_y_ += (sales_num[i] - sales_ave) * (predict_sales_num[i] - predict_sales_ave)

    Se = 0
    for i in range(len(sales_num)):
        Se += (sales_num[i] - predict_sales_num[i]) ** 2

    # 重相関係数 multiple correlation coefficient
    # R = Syy^ / sqrt(Syy * Sy^y^)
    R = Sy_y_ / math.sqrt(sales_sum_of_square_deviation * predict_sales_sum_of_square_deviation)
    # 寄与率 contribution ratio
    RR = R ** 2

    # RR = (a * Sxy)/Syy
    #print ((a * deviation_sum)/sales_sum_of_square_deviation)
    # RR = (1- Se/Syy)
    #print (1 - (Se/sales_sum_of_square_deviation))

    # 回帰係数の検定
    # 母回帰 y = Ax + B
    A = a
    B = b
    sigma = math.sqrt(Se/(len(temperature)-2))

    # 有意水準 significance level
    significance_level = 0.05

    # 回帰係数の検定
    approval_val = \
        (a ** 2)/(1/temp_sum_of_square_deviation) / (Se/(len(temperature) - 2))

    # F分布からPを求める
    # 保留

    # 気温 31度 信頼率 95% における信頼区間の算出
    # F(1, 14-2;0.05) = 4.7
    section = math.sqrt(4.7 * \
        ((1/len(temperature) + (31 - temp_ave)**2 / temp_sum_of_square_deviation) * \
        Se/(len(temperature) - 2 )))
