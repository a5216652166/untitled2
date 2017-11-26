# -*- coding:utf-8 -*-
# import numpy
from sympy import *
import pandas

'''
a 投资金额
m 投资利率
n 借款利率
t 周期 单位月
T 年
b 当期所获收益
c 总收益
'''

a, b, c,d,e,f ,m, n, t, T, s, f, u, v, x, y, z = symbols('a b c d e f m n t T s f u v x y z')
i = 0


def cal(T,a):
    u = a * (m - n)
    b = calff(u, T,a)
    return b


def calff(f, T,a):
    global i
    i += 1
    # print i, T
    s = f * m + (a - f) * (m - n)
    return calff(s, T) if i < T else f
def calfs(a,b):
    s = a*(m+1) -b
    return s
def calmon(t, a):
    f=0.
    u = t / 12
    v = 12 / t
    # print v
    # for i in range(1,v+1):
    #     f += (a * ((1+(n/i)) **i))
    #     print i,'月',f-3*a
    # pprint(f)
    # f12= a*(1+((u)*n))**(1/u)
    # return summation(f,(x,1,v))
    f = (a * ((1 + (n / v)) ** v))
    return f
def calsum(T,t):
    c1= calfs(a,calmon(12,a))
    c2= calfs(a,calmon(12,(a-c1)))
    c3= calfs(a,calmon(12,(a-c2)))
    return c
    pass
def dd(ta,t,T):
    global i
    ta=calfs(a,calmon(t,a-ta))
    i +=1
    # return  ta
    print "第",i,"年:", ta
    return dd(ta,t,T) if i<T else ta
if __name__ == '__main__':
    # pprint(calsum(2,6))
    t_a=1.0
    t_m=0.07
    t_n=0.06
    t_0=0
    t_mon=12
    t_year=2
    t_a,t_m,t_n,t_0,t_mon,t_year = float(raw_input('输入金额：')),\
                                   float(raw_input('输入产品利率：')),\
                                   float(raw_input('输入借款利率:')),\
                                   float(raw_input('输入前置自有金额:')),\
                                   float(raw_input('输入借款记息周期（x>1 and x<12 and 12.mod(x)=0）单位月:')),\
                                   float(raw_input('输入产品周期单位年 便不能为负数:'))
    zzz=dd(t_0,t_mon,t_year).subs({a:t_a,m:t_m,n:t_n}).evalf(30)
    pprint (zzz)
