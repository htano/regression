#!/Users/htano/.pyenv/versions/3.5.0/bin/python3
import numpy as np

def cal_sum_of_square_deviation(list, average):
    sum_of_square_deviation = 0
    for val in list:
        sum_of_square_deviation += (val - average) ** 2
    return sum_of_square_deviation


if __name__ == '__main__':
    temperature = [29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30]
    sales_num   = [77, 62, 93, 84, 59, 64, 80, 75, 58, 91, 51, 73, 65, 84]

    # 平均 average
    temp_ave = sum(temperature) / len(temperature)
    sales_ave  = sum(sales_num) / len(sales_num)

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
    temp_sum_of_square_deviation = cal_sum_of_square_deviation(temperature, temp_ave)
    sales_sum_of_square_deviation = cal_sum_of_square_deviation(sales_num, sales_ave)
    # 偏差積和 sum of products of deviation
    # Sxy : deviation_sum

    # a = Sxy / Sxx, b = ave_y - ave_x * a
    a = deviation_sum / temp_sum_of_square_deviation
    b = sales_ave - temp_ave * a
