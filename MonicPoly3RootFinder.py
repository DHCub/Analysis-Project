from decimal import *

getcontext().prec = 16

E = Decimal("1E-10")

def BisectRoot(a: Decimal, b: Decimal, f: callable):
    if a > b: return BisectRoot(b, a, f)
    X = []

    while(True):
        m = (a + b)/2
        y = f(m)
        X.append([float(a), float(b)])
        if abs(y) < E: return (float(m), X)

        if y < 0: a = m
        else: b = m 

def MonicPoly3Root(a : float, b: float, c: float):
    f = lambda x: x**3 + a*x**2 + b*x + c
    if c < 0: return BisectRoot(abs(a) + abs(b) + abs(c) + 2, 0, f)
    if c > 0: return BisectRoot(-abs(a) - abs(b) - abs(c) - 2, 0, f)
    return (0.0, [[0, 0]])

