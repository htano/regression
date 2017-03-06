#!/Users/htano/.pyenv/versions/3.5.0/bin/python3
import math
import numpy as np

area_offset = 0
dist_offset = 1
sale_offset = 2

if __name__ == '__main__':
    data = [[10, 80, 469], [8, 0, 366], [8, 200, 371], [5, 200, 208], \
            [7, 300, 246], [8, 230, 297], [7, 40, 363], [9, 0, 436], \
            [6, 330, 198], [9, 180, 364]]

    area = []
    dist = []
    sale = []
    ones = []
    for d in data:
        area.append(d[area_offset])
        dist.append(d[dist_offset])
        sale.append(d[sale_offset])
        ones.append(1)

    # 行列の初期化
    m1 = np.matrix([area, dist, ones])
    m2 = np.transpose(m1)
    m3 = np.matrix([[sale[0]], [sale[1]], [sale[2]], [sale[3]], [sale[4]], \
                    [sale[5]], [sale[6]], [sale[7]], [sale[8]], [sale[9]]])
    # 行列計算
    m1_t_m2     = m1.dot(m2)
    inv_m1_t_m2 = np.linalg.inv(m1_t_m2)
    regression_coefficient_mat = (inv_m1_t_m2.dot(m1)).dot(m3)

    # 偏回帰係数
    a1 = regression_coefficient_mat[0, 0]
    a2 = regression_coefficient_mat[1, 0]
    b  = regression_coefficient_mat[2, 0]
    print ('a1 : ' + str(a1) + ', a2 : ' + str(a2) + ', b : ' + str(b))

    # 重相関係数, 寄与率を求める
    sale_ave = sum(sale)/len(sale)
    predicted_sale = []
    for d in data:
        predicted_sale.append(a1 * d[area_offset] + a2 * d[dist_offset] + b)
    predicted_sale_ave = sum(predicted_sale) / len(sale)

    print ('y average : ' + str(sale_ave) + ', predicted y average : ' + str(predicted_sale_ave))

    # 偏差平方和
    Syy = 0
    for i in range(len(sale)):
        Syy += (sale[i] - sale_ave) ** 2
    Sy_y_ = 0
    for i in range(len(predicted_sale)):
        Sy_y_ += (predicted_sale[i] - predicted_sale_ave) ** 2

    # 偏差積和
    Syy_ = 0
    for i in range(len(sale)):
        Syy_ += (sale[i] - sale_ave) * (predicted_sale[i] - predicted_sale_ave)

    # 残差平方和
    Se = 0
    for i in range(len(sale)):
        Se += (sale[i] - predicted_sale[i]) ** 2

    print ('Syy : ' + str(Syy) + ', Sy_y_ : ' + str(Sy_y_) + ', Syy_ : ' + str(Syy_) + ', Se : ' + str(Se))

    # 重相関係数, 寄与率
    R  = Syy_ / math.sqrt(Syy * Sy_y_)
    RR = R ** 2
    #RR = 1 - (Se/Syy)
    print ('R : ' + str(R) + ', R^2 : ' + str(RR))

    # 自由度調整済み寄与率
    R_2 = 1 - (Se/(len(data) - 2 - 1))/(Syy/(len(data) - 1))
    print ('R*2 : ' + str(R_2))

    '''
    # 説明変数に「店長の年齢」を加えたときの寄与率
    age = [42, 29, 33, 41, 33, 35, 40, 46, 44, 34]
    m1  = np.matrix([area, dist, age, ones])
    m2  = np.transpose(m1)
    m1_t_m2 = m1.dot(m2)
    inv_m1_t_m2 = np.linalg.inv(m1_t_m2)
    regression_coefficient_mat = (inv_m1_t_m2.dot(m1)).dot(m3)

    a1 = float(regression_coefficient_mat[0])
    a2 = float(regression_coefficient_mat[1])
    a3 = float(regression_coefficient_mat[2])
    b  = float(regression_coefficient_mat[3])

    predicted_sale = []
    for i in range(len(data)):
        p_sale = a1 * data[i][area_offset] + a2 * data[i][dist_offset] + a3 * age[i] + b
        predicted_sale.append(p_sale)

    Se = 0
    for i in range(len(sale)):
        Se += (sale[i] - predicted_sale[i]) ** 2
    RR = 1 - Se/Syy
    print ('additional R^2 : ' + str(RR))

    R_2 = 1 - (Se/(len(data) - 3 - 1))/(Syy/(len(data) - 1))
    print ('additional R*2 : ' + str(R_2))
    '''

    # 偏回帰係数の検定
    A1 = a1
    A2 = a2
    B  = b
    sigma = math.sqrt(Se/(len(data) - 2 - 1))
    print ('A1 : ' + str(A1) + ', A2 : ' + str(A2) + ', B : ' + str(B) + ', sigma : ' + str(sigma))

    # 有意水準 significance level
    significance_level = 0.05

    # 偏回帰係数を包括的に検討する検定
    # 検定統計量
    test_statistic = ((Syy - Se)/2)/(Se/(len(data) - 2 - 1))
    print ('test statistic : ' + str(test_statistic))

    # 偏回帰係数を個別に検討する検定
    S11 = inv_m1_t_m2[0, 0]
    test_statistic2 = (a1 ** 2 / S11) / (Se/(len(data) - 2 - 1))
    print ('test statistic2 : ' + str(test_statistic2))

    # マハラノビス汎距離 信頼区間
    S = inv_m1_t_m2
    area_ave = sum(area) / len(area)
    dist_ave = sum(dist) / len (dist)

    # マハラノビス汎距離の2乗
    DD = ((area[0] - area_ave) * (area[0] - area_ave) * S[0, 0] + \
          (area[0] - area_ave) * (dist[0] - dist_ave) * S[0, 1] + \
          (dist[0] - dist_ave) * (area[0] - area_ave) * S[1, 0] + \
          (dist[0] - dist_ave) * (dist[0] - dist_ave) * S[1, 1]) * \
          (len(data) - 1)
    print ('D^2 : ' + str(DD))

    # 信頼区間
    trusted_section = math.sqrt(5.6 * (1/len(data) + DD/(len(data) - 1)) * Se/(len(data) - 2 - 1))
    print ('trusted section : ' + str(trusted_section))

    # 母回帰 面積 10 距離 80のときの信頼区間
    predict_min = A1 * 10 + A2 * 80 + B - trusted_section
    predict_max = A1 * 10 + A2 * 80 + B + trusted_section

    print ('predicted sale : ' + str(predict_min) + ' - ' + str(predict_max))

    # 予測
    predicted_val = a1 * 10 + a2 * 110 + b

    print ('predicted val : ' + str(predicted_val))

    # 予測区間
    predicted_section = math.sqrt(5.6 * (1 + 1/len(data) + DD/(len(data) - 1)) * Se/(len(data) - 2 - 1))
    predict_min2 = a1 * 10 + a2 * 110 + b - predicted_section
    predict_max2 = a1 * 10 + a2 * 110 + b + predicted_section

    print ('predicted sale : ' + str(predict_min2) + ' - ' + str(predict_max2))
