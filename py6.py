# 6
import math


def quad_Root(a=0, b=0, c=0):  # 0 assigned as default
    k = math.pow(b, 2) - 4*a*c
    if k < 0:
        return print('no roots')
    else:
        d = math.sqrt(k)
        x1 = (-b + d) / (2*a)
        x2 = (-b - d) / (2*a)
        print('root_1 :', x1)
        print('root_2: ', x2)


quad_Root(2, -1, -3)  # input :  cofficients only
