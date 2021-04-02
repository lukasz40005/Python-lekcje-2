from turtle import *
from math import sqrt

def kw_zp(a):
    for i in range(4):
        fd(a); lt(90)
    lt(45); fd(a*sqrt(2))
    lt(135); fd(a)
    lt(135); fd(a*sqrt(2))


kw_zp(100)
