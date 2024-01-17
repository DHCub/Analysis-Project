from random import random

from MonicPoly3RootFinder import *

def GetFR():
    a = 300*random() - 150
    b = 300*random() - 150
    c = 300*random() - 150

    f = lambda x: x**3 + a*x**2 + b*x + c
    r = MonicPoly3Root(a, b, c)
    return (f, r)

def GetAxes(f: callable, x1: float, x2: float, amount: int = 1080):
    inc = (x2 - x1)/amount
    X = []
    Y = []
    while(x1 < x2):
        X.append(x1)
        Y.append(f(x1))
        x1 += inc

    return (X, Y)

