# -*- coding:utf-8 -*-
import numpy as np
'''
先求x,y的平均值X,Y
再用公式代入求解：b=(x1y1+x2y2+...xnyn-nXY)/(x12+x22+...xn2-nX2)
后把x,y的平均数X，Y代入a=Y-bX
求出a并代入总的公式y=bx+a得到线性回归方程

>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)
[(1, 2, 3), (4, 5, 6)]

zip(*)行列互换  
'''
def fix(x,y):
    n=len(x)
    numerator=0 #分子
    dinominator=0 #分母
    for v in zip(x,y):
        numerator+=(v[0]-np.mean(x))*(v[1]-np.mean(y))
        dinominator+=(v[0]-np.mean(x))**2
    b1=numerator/dinominator
    b0=np.mean(y)-b1*np.mean(x)
    return b0,b1

def predict(x,b0,b1):
    return b1*x+b0

x = [1, 3, 2, 1, 3]
y = [14, 24, 18, 17, 27]

b0,b1=fix(x,y)

print '截距intercept:',b0,'斜率slope:',b1
print 'y=',b1,'x+',b0
print '当x为6时预测结果为:',predict(6,b0,b1)