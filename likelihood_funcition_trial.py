#!/Users/htano/.pyenv/versions/3.5.0/bin/python3
import math
import numpy as np

N = 10

if __name__ == '__main__':
    # 尤度関数
    max   = -1
    index = -1
    for i in range(1, N):
        P = i / 10.0
        y = (P ** 7) * ((1 - P) ** 3)
        if y > max or index == -1:
            max = y
            index = i

    print ('[likelihood function] P : ' + str(index/10.0) + ', max : ' + str(max))

    # 対数尤度関数
    max   = -1
    index = -1
    for i in range(1, N):
        P = i / 10.0
        y = math.log((P ** 7) * ((1 - P) ** 3))
        if y > max or index == -1:
            max = y
            index = i

    print ('[log likelihood function] P : ' + str(index/10.0) + ', max : ' + str(max))
