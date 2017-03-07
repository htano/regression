#!/Users/htano/.pyenv/versions/3.5.0/bin/python3
import math
import numpy as np
import pylab

if __name__ == '__main__':
    day_of_weeks = [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1]
    temperatures = [28, 24, 26, 24, 23, 28, 24, 26, 25, 28, 21, 22, 27, 26, 26, 21, 21, 27, 23, 22, 24]
    sales        = [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]

    data_num = len(sales)

    # 平均値
    day_of_weeks_ave = sum(day_of_weeks)/len(day_of_weeks)
    temperatures_ave = sum(temperatures)/len(temperatures)
    sales_ave        = sum(sales)/len(sales)

    # 共分散
    sum_d_x_s = 0
    sum_t_x_s = 0
    for i in range(data_num):
        sum_d_x_s  += (day_of_weeks[i] - day_of_weeks_ave) * (sales[i] - sales_ave)
        sum_t_x_s += (temperatures[i] - temperatures_ave) * (sales[i] - sales_ave)
    covariance_d_x_s = sum_d_x_s/data_num
    covariance_t_x_s = sum_t_x_s/data_num

    # 標準偏差
    day_of_weeks_deviation = np.std(day_of_weeks)
    temperatures_deviation = np.std(temperatures)
    sales_deviation        = np.std(sales)

    # 単相関係数
    correlation_coefficient_d_x_s = covariance_d_x_s / (day_of_weeks_deviation * sales_deviation)
    correlation_coefficient_t_x_s = covariance_t_x_s / (temperatures_deviation * sales_deviation)

    print ('correlation coefficient (day of weeks x sales) : ' + str(correlation_coefficient_d_x_s))
    print ('correlation coefficient (temperatures x sales) : ' + str(correlation_coefficient_t_x_s))

    '''
    pylab.figure()
    pylab.plot(sales, day_of_weeks, 'k+')
    pylab.show()
    '''
